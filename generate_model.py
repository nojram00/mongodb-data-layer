from .templates import model_template
import argparse
import os

def to_pascal_case(s):
    return ''.join(word.capitalize() for word in s.split('_'))

def create_file_with_template(file_path, collection_name, class_name):
    content = model_template.PYTHON_TEMPLATE.format(model_name=class_name, collection_name=collection_name)
    with open(file_path, 'w') as f:
        f.write(content)
    print(f'File created at {file_path}')

def main():
    parser = argparse.ArgumentParser(description="Generate a Python file with a template")
    parser.add_argument('file_path', type=str, help="The path of the file to create")
    args = parser.parse_args()

    base_name = os.path.basename(args.file_path).replace('.py', '')

    create_file_with_template(args.file_path, base_name + "s", to_pascal_case(base_name))

if __name__ == "__main__":
    main()