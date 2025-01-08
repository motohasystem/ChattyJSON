@echo off
chcp 65001
set WORK_DIR=.\sample
set PROMPT_FILE=%WORK_DIR%\prompt.md
set SYSTEM_PROMPT_FILE=%WORK_DIR%\system.md
set SCHEMA_JSON=%WORK_DIR%\dialogue_schema.json
set OUTPUT_FILE=result.json

echo python main.py --prompt_file %PROMPT_FILE% --system_prompt_file %SYSTEM_PROMPT_FILE% --output_file %OUTPUT_FILE% --dictionary_tsv %DICTIONARY_TSV% --schema_json %SCHEMA_JSON%
