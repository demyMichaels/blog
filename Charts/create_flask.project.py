import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def create_file(path, content=""):
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write(content)
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

def setup_flask_project(project_name):
    project_root = project_name

    # Create directories
    create_directory(project_root)
    create_directory(os.path.join(project_root, 'app'))
    create_directory(os.path.join(project_root, 'app/templates'))
    create_directory(os.path.join(project_root, 'static'))
    create_directory(os.path.join(project_root, 'static/css'))
    create_directory(os.path.join(project_root, 'static/js'))
    create_directory(os.path.join(project_root, 'static/images'))
    create_directory(os.path.join(project_root, 'tests'))

    # Create files with basic content
    create_file(os.path.join(project_root, 'app/__init__.py'), """from flask import Flask\napp = Flask(__name__)\nfrom app import routes\n""")
    create_file(os.path.join(project_root, 'app/routes.py'), """from app import app\n\n@app.route('/')\ndef index():\n    return "Hello, World!"\n""")
    create_file(os.path.join(project_root, 'app/models.py'), "")
    create_file(os.path.join(project_root, 'app/templates/index.html'), "<h1>Hello, World!</h1>")
    create_file(os.path.join(project_root, 'static/css/style.css'), "/* CSS styles go here */")
    create_file(os.path.join(project_root, 'tests/__init__.py'), "")
    create_file(os.path.join(project_root, 'tests/test_basic.py'), """import unittest\n\nclass BasicTests(unittest.TestCase):\n    def test_basic(self):\n        self.assertEqual(1, 1)\n\nif __name__ == '__main__':\n    unittest.main()\n""")
    create_file(os.path.join(project_root, 'config.py'), """import os\n\nclass Config:\n    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'\n""")
    create_file(os.path.join(project_root, 'requirements.txt'), "Flask\n")
    create_file(os.path.join(project_root, 'run.py'), """from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)\n""")

if __name__ == "__main__":
    project_name = input("Enter the project name: ")
    setup_flask_project(project_name)
