from pathlib import Path

def rename_and_move_files(article_id):
    raw_dir = Path("./static/raw")
    images_dir = Path("./static/images/articles")

    # Получаем список всех файлов в ./raw
    files = list(raw_dir.glob("*.*"))

    # Сортируем файлы по имени
    files.sort(key=lambda x: x.name)

    for i, file in enumerate(files, start=1):
        # Создаем новое имя файла
        new_name = f"{article_id}.{i}.{file.suffix}"
        new_path = images_dir / new_name

        # Переименовываем и перемещаем файл
        file.rename(new_path)
