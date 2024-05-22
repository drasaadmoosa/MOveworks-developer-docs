import os

def combine_md_files(root_path):
    combined_file_path = os.path.join(root_path, 'combined.md')

    # Remove the combined file if it already exists
    if os.path.exists(combined_file_path):
        os.remove(combined_file_path)

    with open(combined_file_path, 'a', encoding='utf-8') as combined_file:
        for subdir, _, files in os.walk(root_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r', encoding='utf-8') as md_file:
                        combined_file.write(md_file.read())
                        combined_file.write('\n')  # Add a newline after each file

    print(f"All .md files have been combined into {combined_file_path}")

# Set the path to the root directory of your GitHub repo
root_path = os.path.dirname(os.path.abspath(__file__))
combine_md_files(root_path)
