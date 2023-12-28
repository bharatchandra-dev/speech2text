import subprocess
def start_fastapi_app():
    # Start FastAPI app with Uvicorn
    cmd = "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    start_fastapi_app()