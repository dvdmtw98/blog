#!/usr/bin/env bash

process_image() {
  local source_file="$1"
  local destination_file="$2"

  echo "[PROCESS] $source_file"

  mkdir -p "$(dirname "$destination_file")"

  pngquant --quality=75-90 --output "$destination_file" --force "$source_file" \
    || { echo "[SKIPPED pngquant] $source_file"; return; }

  oxipng -o 3 --strip safe -q "$destination_file" \
    || { echo "[SKIPPED oxipng] $destination_file"; return; }
}

delete_image() {
  local destination_file="$1"

  echo "[DELETE] $destination_file"
  rm -f "$destination_file"
}

to_output_path() {
  local source_file="$1"
  local source_path_segment="$2"
  local destination_path_segment="$3"

  echo "${source_file/$source_path_segment/$destination_path_segment}"
}

# Main Logic

source_path_segment="$1"
destination_path_segment="$2"
source_repo="main"

git -C "${GITHUB_WORKSPACE}/main" diff --name-status HEAD~1 HEAD \
| grep -F "$source_path_segment" | grep -Ei '\.(png|jpg|jpeg)$' \
| while IFS=$'\t' read -r status source_file modified_file; do

  source_file="$source_repo/$source_file"

  destination_file=$(to_output_path "$source_file" "$source_path_segment" "$destination_path_segment")
  destination_file_full="${GITHUB_WORKSPACE}/$destination_file"
  source_file_full="${GITHUB_WORKSPACE}/$source_file"

  case "$status" in

    A|M)
      process_image "$source_file_full" "$destination_file_full"
      ;;

    D)
      delete_image "$destination_file_full"
      ;;

    R*)
      modified_file="$source_repo/$modified_file"
      echo "[RENAME] $source_file -> $modified_file"

      new_destination_file_full="${GITHUB_WORKSPACE}/$(to_output_path "$modified_file" "$source_path_segment" "$destination_path_segment")"
      modified_file_full="${GITHUB_WORKSPACE}/$modified_file"

      delete_image "$destination_file_full"
      process_image "$modified_file_full" "$new_destination_file_full"
      ;;

    *)
      echo "[IGNORE] $status $source_file $modified_file"
      ;;
  esac

done
