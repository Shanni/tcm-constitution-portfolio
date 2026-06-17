#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA_DIR="$ROOT/../data/raw"
mkdir -p "$DATA_DIR/mendeley_274"

echo "Downloading Zenodo CCMQ test data + code..."
curl -fsSL -o "$DATA_DIR/TEST_DATA.xlsx" \
  "https://zenodo.org/api/records/4431679/files/TEST_DATA.xlsx/content"
curl -fsSL -o "$DATA_DIR/CCMQ_SAS.sas" \
  "https://zenodo.org/api/records/4431679/files/CCMQ%20SAS%20code.sas/content"

echo "Downloading Zenodo cross-sectional SPSS dataset..."
curl -fsSL -o "$DATA_DIR/dataset_phyact_Psychodistress_TCMBC.sav" \
  "https://zenodo.org/api/records/18779514/files/dataset_phyact_Psychodistress_TCMBC.sav/content"

echo "Downloading Mendeley 274-subject multimodal dataset..."
curl -fsSL -L -o "$DATA_DIR/mendeley_274/mendeley_cxtph3tjsg.zip" \
  "https://data.mendeley.com/public-api/zip/cxtph3tjsg/download/1"
unzip -o "$DATA_DIR/mendeley_274/mendeley_cxtph3tjsg.zip" -d "$DATA_DIR/mendeley_274/"

echo "Done. Files in $DATA_DIR/"
