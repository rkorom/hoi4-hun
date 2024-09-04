import subprocess
import os
from dotenv import load_dotenv


def load_environment_variables(project_root):
    """Loads the environment variables from the .env file located at the project root."""
    env_path = os.path.join(project_root, ".env")
    load_dotenv(dotenv_path=env_path)

    steam_username = os.getenv("STEAM_USERNAME")
    steam_cmd_path = os.getenv("STEAM_CMD_PATH")

    if not steam_username:
        raise ValueError("Hiba: A Steam felhasználónév nem található a .env fájlban.")

    return steam_username, steam_cmd_path


def get_latest_commit_id(project_root):
    """Returns the latest commit ID for the given project."""
    return (
        subprocess.check_output(["git", "log", "-1", "--pretty=%H"], cwd=project_root)
        .strip()
        .decode("utf-8")
    )


def update_metadata_file(metadata_file_path, latest_commit_id):
    """Updates the 'changenote' field in the metadata.vdf file with the latest commit ID."""
    with open(metadata_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if '"changenote"' in line:
            lines[i] = f'	"changenote"\t\t\t"{latest_commit_id}"\n'
            break

    with open(metadata_file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def steam_workshop_update(steam_cmd_path, steam_username, metadata_file_path):
    """Runs the Steam workshop update command using the given credentials and metadata file."""
    subprocess.run(
        [
            steam_cmd_path,
            "+login",
            steam_username,
            "+workshop_build_item",
            metadata_file_path,
            "+quit",
        ]
    )


def git_add_commit_push(project_root, metadata_file_path, latest_commit_id):
    """Adds, commits, and pushes the updated metadata file to the Git repository."""
    subprocess.run(["git", "add", metadata_file_path], cwd=project_root)
    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            f"Update changenote to latest commit: {latest_commit_id}",
        ],
        cwd=project_root,
    )
    subprocess.run(["git", "push"], cwd=project_root)


def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # 1. Load environment variables
    steam_username, steam_cmd_path = load_environment_variables(project_root)

    # 2. Get the latest commit ID
    latest_commit_id = get_latest_commit_id(project_root)

    # 3. Update the metadata file
    metadata_file_path = os.path.join(project_root, "src", "metadata.vdf")
    update_metadata_file(metadata_file_path, latest_commit_id)

    # 4. Run the Steam workshop update
    steam_workshop_update(steam_cmd_path, steam_username, metadata_file_path)

    # 5. Git add, commit, and push
    git_add_commit_push(project_root, metadata_file_path, latest_commit_id)

    print("Deploy script sikeresen lefutott!")


if __name__ == "__main__":
    main()
