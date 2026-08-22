#!/usr/bin/env bash

# Create or update the stable Markdown showcase paste in the local development instance.

set -euo pipefail

pb_url="${PB_URL:-http://localhost:10002}"
source_file="dev/markdown-showcase.md"

response="$(curl --fail --silent --show-error --request POST \
    --form "content=@${source_file};filename=markdown-showcase.md" \
    "${pb_url}/")"
paste_url="$(printf '%s\n' "${response}" | awk '/^url:/{print $2; exit}')"

if [[ -z "${paste_url}" ]]; then
    printf 'Could not determine the Markdown showcase URL.\n' >&2
    exit 1
fi

printf 'Open %s/r/%s\n' "${pb_url}" "${paste_url#"${pb_url}/"}"
