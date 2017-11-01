#!/bin/bash
PYTHON_PROCESS_FILES='/home/evroon/Development/segura/preparation/processTransactionFiles.py'
NO_DUPLICATES_MASTER_FILE='/home/evroon/stack/SEGURA/Rabobank/noDuplicatesMasterCsv.csv'

python ${PYTHON_PROCESS_FILES}

# remove quotes from csv file
awk -F "\",\"" -v OFS='|' -v NFS='\"|\"' -v LEFT_QUOTE='\"|' -v  RIGHT_QUOTE='|\"' '{
	gsub(/"/, "", $1); \
	gsub(/"/, "", $5); \
	gsub(/"/, "", $19); \
	print \
		$1 OFS \
		$2 OFS \
		$3 OFS \
		$4 OFS \
		$5 OFS \
		$6 OFS \
		$7 OFS \
		$8 OFS \
		$9 OFS \
		$10 OFS \
		$11 OFS \
		$12 OFS \
		$13 OFS \
		$14 OFS \
		$15 OFS \
		$16 OFS \
		$17 OFS \
		$18 OFS \
		$19 \
	}' $NO_DUPLICATES_MASTER_FILE > docker/init_config/data/noDuplicatesMasterCsv.csv
