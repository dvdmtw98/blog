#!/usr/bin/env bash

process_image() {
  local source_file="$1"
  local destination_file="$2"

  mkdir -p "$(dirname "$destination_file")"

  pngquant --quality=75-90 --output "$destination_file" --force "$source_file" \
    || { echo "[SKIPPED pngquant] $source_file"; return; }

  oxipng -o 3 --strip safe -q "$destination_file" \
    || { echo "[SKIPPED oxipng] $destination_file"; return; }
}

source_path_segment="$1"
destination_path_segment="$2"

find "$source_path_segment" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) \
| while IFS= read -r source_file; do

  destination_file="${source_file/$source_path_segment/$destination_path_segment}"
  destination_file_full="${GITHUB_WORKSPACE}/$destination_file"
  source_file_full="${GITHUB_WORKSPACE}/$source_file"

  if [ -f "$source_file_full" ] && [ ! -f "$destination_file_full" ]; then
    echo "[MISSING → PROCESS] $source_file_full"
    process_image "$source_file_full" "$destination_file_full"
  fi

done
