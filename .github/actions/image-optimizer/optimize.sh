#!/usr/bin/env bash

process_image() {
  local source_file="$1"
  local destination_file="$2"
  local hash_file="$destination_file.hash"

  mkdir -p "$(dirname "$destination_file")"

  # Generate hash of source
  local current_hash
  current_hash=$(sha256sum "$source_file" | awk '{print $1}')

  # If hash exists and if match skip image
  if [ -f "$destination_file" ] && [ -f "$hash_file" ]; then
    local cached_hash
    cached_hash=$(cat "$hash_file")

    if [ "$current_hash" = "$cached_hash" ]; then
      echo "[SKIP] Unchanged: $source_file"
      return
    else
      echo "[MODIFIED → REPROCESS] $source_file"
    fi
  else
    echo "[NEW → PROCESS] $source_file"
  fi

  # Run optimization
  pngquant --quality=75-90 --output "$destination_file" --force "$source_file" \
    || { echo "[SKIPPED pngquant] $source_file"; return; }

  oxipng -o 3 --strip safe -q "$destination_file" \
    || { echo "[SKIPPED oxipng] $destination_file"; return; }

  # Save new hash
  echo "$current_hash" > "$hash_file"
}

delete_image() {
  local destination_file="$1"
  local hash_file="$destination_file.hash"

  echo "[DELETE] $destination_file"
  rm -f "$destination_file" "$hash_file"
}

# -------------------------------------------------------------------

source_path_segment="$1"
destination_path_segment="$2"

# --- PROCESS / UPDATE ---
find "$source_path_segment" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) \
| while IFS= read -r source_file; do

  destination_file="${source_file/$source_path_segment/$destination_path_segment}"
  
  destination_file_full="${GITHUB_WORKSPACE}/$destination_file"
  source_file_full="${GITHUB_WORKSPACE}/$source_file"

  process_image "$source_file_full" "$destination_file_full"
done

# --- DELETE ORPHANS ---
find "$destination_path_segment" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) \
| while IFS= read -r destination_file; do

  source_file="${destination_file/$destination_path_segment/$source_path_segment}"

  source_file_full="${GITHUB_WORKSPACE}/$source_file"
  destination_file_full="${GITHUB_WORKSPACE}/$destination_file"

  if [ ! -f "$source_file_full" ]; then
    echo "[EXTRA → DELETE] $destination_file_full"
    delete_image "$destination_file_full"
  fi
done
