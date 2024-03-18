import os
import re

def convert_file(id):
    # Получаем пути к исходному и результирующему файлам
    source_path = os.path.join(".", "events", "static", "text", "source.txt")
    result_path = os.path.join(".", "events", "static", "text", "result.html")

    # Читаем исходный файл
    with open(source_path, "r", encoding="utf-8") as source_file:
        source_text = source_file.read()

    # Преобразуем текст в HTML
    html_text = ""
    for line in source_text.split("\n"):
        indent = len(line) - len(line.lstrip())
        if indent > 0:
            if line.startswith("\t"):  # Проверяем отступ на табуляцию
                indent = 4
            elif indent % 4 != 0:  # Проверяем, что отступ не кратен 4 пробелам
                indent = (indent // 4 + 1) * 4  # Округляем отступ до ближайшего кратного 4
            html_text += f"<span style='margin-left:{20 * indent // 4}px'>{' ' * indent + line.lstrip()}</span><br>\n"
        else:
            html_text += f"{line}<br>\n"

    # Заменяем специальные конструкции
    html_text = re.sub(r"<img-(\d+\.\w+)>", lambda m: f"<img src='./static/images/articles/{id}.{m.group(1)}'/>", html_text)
    html_text = re.sub(r"<by-line>(.*?)</by-line>", r"<p style='font-size: 70%'>\1</p>", html_text)

    # Записываем результат в файл
    with open(result_path, "w", encoding="utf-8") as result_file:
        result_file.write(html_text)

# Пример использования
convert_file(2)  # Замена изображений с id 2