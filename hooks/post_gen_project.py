import os
import shutil
import sys

# Cookiecutter will replace these values during project generation
CREATE_DOCS = "{{ cookiecutter.create_docs }}"
PROJECT_SLUG = "{{ cookiecutter.project_slug }}"

def remove_docs():
    """Removes the documentation directory if the user opted out."""
    docs_path = os.path.join(os.getcwd(), "docs")
    if os.path.exists(docs_path):
        shutil.rmtree(docs_path)
        print("INFO: Removed documentation directory.")

def main():
    if CREATE_DOCS == "no":
        remove_docs()
    
    # You can also use this hook to initialize a git repo automatically
    print(f"SUCCESS: Project {PROJECT_SLUG} initialized!")

if __name__ == "__main__":
    main()
