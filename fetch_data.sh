#!/usr/bin/env bash

# For each of the following hosts:
# ssh://doma.dev
# ssh://maja.doma.dev
# ssh://dimir.memorici.de:2222
#
# Download ${host}:perplex/51/data.csv to 51/${human_readable_date}-${host}-data.csv
# where ${human_readable_date} is the current date in the format YYYY-MM-DD
# and ${host} is the host name (e.g. doma.dev)
#
# Then download ${host}:perplex/51/invocations.csv to 51/${human_readable_date}-${host}-invocations.csv

# Implementation using `rsync` follows:

# Get the current date in the format YYYY-MM-DD
human_readable_date=$(date +%Y-%m-%d)

# Define the hosts
hosts=(
  "doma.dev"
  "maja.doma.dev"
  "dimir.memorici.de:2222"
)

# Loop through the hosts
for host in "${hosts[@]}"; do
  port="22"
  # Check if the host has a port number
  if [[ $host == *":"* ]]; then
    port="${host##*:}"
    host="${host%:*}"
  fi

  # Use rsync -Pave 'ssh -p ${port}' to download the files
  rsync -Pave "ssh -p ${port}" "${host}:perplex/51/data.csv" "51/${human_readable_date}-${host}-data.csv"
  rsync -Pave "ssh -p ${port}" "${host}:perplex/51/invocations.csv" "51/${human_readable_date}-${host}-invocations.csv"
done
