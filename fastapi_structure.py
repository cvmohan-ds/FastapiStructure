import os

def create_structure(project_name):
    directories = [
        f"{project_name}/app/api/v1/endpoints",
        f"{project_name}/app/core",
        f"{project_name}/app/db",
        f"{project_name}/app/models",
        f"{project_name}/app/schemas",
        f"{project_name}/tests",
        f"{project_name}/app/utils",
        f"{project_name}/app/external_services"
    ]
    
    files = [
        f"{project_name}/app/__init__.py",
        f"{project_name}/app/api/__init__.py",
        f"{project_name}/app/api/v1/__init__.py",
        f"{project_name}/app/api/v1/endpoints/__init__.py",
        f"{project_name}/app/core/__init__.py",
        f"{project_name}/app/db/__init__.py",
        f"{project_name}/app/models/__init__.py",
        f"{project_name}/app/schemas/__init__.py",
        f"{project_name}/tests/__init__.py",
        f"{project_name}/app/utils/__init__.py",
        f"{project_name}/app/external_services/__init__.py",
        f"{project_name}/app/main.py"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    for file in files:
        with open(file, 'w') as f:
            pass

    # Create a basic main.py file
    with open(f"{project_name}/app/main.py", 'w') as f:
        f.write("""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Vamsi"}
""")

def main():
    with os.scandir(".") as entries:
        for entry in entries:
            if entry.is_dir():
                if entry.name.startswith("."):
                    pass
                else:
                    create_structure(entry.name)
            else:
                print("Nothing to do!!!")

if __name__ == "__main__":
    main()
