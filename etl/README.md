## Полный пайплайн
```bash
python -m etl.main --file-id "1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL"
```

## Отдельные этапы
```bash
python -m etl.main --file-id "1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL" --skip-load
python -m etl.main --file-id "1NaXgQ0LiW-RjNohEZ_uwRw19E-czPizL" --max-rows 50
```