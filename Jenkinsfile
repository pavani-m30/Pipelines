import subprocess
import sys
import os

# ---------- CONFIGURATION ----------
REPO_URL = "https://github.com/pavani-m30/Pipelines.git"
BRANCH_NAME = "main"
APP_RUN_COMMAND = ["python", "app.py"]  # Change to your app start command
STAGES = ["plan", "code", "test", "deploy"]  # Pipeline stages
WORK_DIR = "/home/administrator/Pipelines"
# -----------------------------------

def run_command(command, cwd=None):
    """Run a shell command and stop if it fails."""
    try:
        print(f"\n[RUNNING] {' '.join(command)}")
        result = subprocess.run(command, cwd=cwd, check=True, text=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {' '.join(command)}")
        sys.exit(1)

def clone_and_checkout():
    """Clone the repository and checkout the branch."""
    if not os.path.exists(WORK_DIR):
        run_command(["git", "clone", REPO_URL, WORK_DIR])
    else:
        print("[INFO] Repository already cloned.")

    run_command(["git", "fetch"], cwd=WORK_DIR)
    run_command(["git", "checkout", BRANCH_NAME], cwd=WORK_DIR)
    run_command(["git", "pull"], cwd=WORK_DIR)

def run_application():
    """Run the application and stop if it fails."""
    print("\n[INFO] Starting application...")
    try:
        subprocess.run(APP_RUN_COMMAND, cwd=WORK_DIR, check=True)
        print("[SUCCESS] Application ran successfully.")
    except subprocess.CalledProcessError:
        print("[FAILURE] Application failed. Terminating pipeline.")
        sys.exit(1)

def run_stage(stage_name):
    """Simulate running a pipeline stage."""
    print(f"\n[STAGE] {stage_name.upper()} started...")
    # Replace with actual commands for each stage
    if stage_name == "plan":
        run_command(["echo", "Planning deployment..."])
    elif stage_name == "code":
        run_command(["echo", "Running code quality checks..."])
    elif stage_name == "test":
        run_command(["pytest", "--maxfail=1", "--disable-warnings", "-q"], cwd=WORK_DIR)
    elif stage_name == "deploy":
        run_command(["echo", "Deploying application..."])
    print(f"[STAGE] {stage_name.upper()} completed.")

def main():
    print("=== CI/CD Pipeline Started ===")
    clone_and_checkout()
    run_application()

    for stage in STAGES:
        run_stage(stage)

    print("\n=== CI/CD Pipeline Completed Successfully ===")

if __name__ == "__main__":
    main()

