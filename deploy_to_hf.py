from huggingface_hub import HfApi
import os

api = HfApi()

api.upload_folder(
    folder_path=".",
    repo_id="Diaure/Futurisys_API_ML",
    repo_type="space",
    token=os.environ["HF_TOKEN"],
    commit_message="CD: update from GitHub main"
)
