import os
import shutil
import sys

def copy_and_sort_files(source_dir, target_dir):
    # Створюємо директорію призначення, якщо вона не існує
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Проходимося по всім елементам у директорії
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        if os.path.isdir(source_item):
            # Рекурсивно викликаємо функцію для піддиректорії
            copy_and_sort_files(source_item, target_dir)
        else:
            # Копіюємо файл у відповідну піддиректорію на основі розширення файла
            file_ext = os.path.splitext(item)[1][1:]  # Вилучаємо розширення файла без крапки
            ext_dir = os.path.join(target_dir, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)
            shutil.copy(source_item, ext_dir)

def main():
    if len(sys.argv) >= 2:
        source_dir = sys.argv[1]
        target_dir = sys.argv[2] if len(sys.argv) >= 3 else 'dist'
    else:
        print("Usage: python script.py <source_dir> [<target_dir>]")
        sys.exit(1)

    try:
        copy_and_sort_files(source_dir, target_dir)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
