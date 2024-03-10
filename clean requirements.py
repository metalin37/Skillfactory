def clean_requirements(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        package_name = line.split('==')[0].strip()
        cleaned_lines.append(package_name + '\n')

    with open(filename, 'w') as file:
        file.writelines(cleaned_lines)

# Пример использования
requirements_file = 'requirements.txt'
clean_requirements(requirements_file)