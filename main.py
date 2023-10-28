import subprocess
import sys
import os
import logging

logging.basicConfig(level=logging.INFO)

def run_fastapi():
    try:
        command = ["uvicorn", "ng_api.neuroguard_api:app", "--host", "0.0.0.0", "--reload"]
        subprocess.run(command, shell=False)  # Set shell to False for security reasons
    except Exception as e:
        print(f"Failed to start FastAPI server: {e}")


def run_streamlit():
    try:
        command = ["streamlit", "run", "ng_interface/neuroguard_interface.py"]
        subprocess.run(command, shell=False)  # Set shell to False for security reasons
    except Exception as e:
        print(f"Failed to start Streamlit server: {e}")

if __name__ == "__main__":
    if "api" in sys.argv:
        run_fastapi()
    elif "interface" in sys.argv:
        run_streamlit()
    else:
        logging.info("Usage: python main.py [api|interface]")
        print("Usage: python main.py [api|interface]")
