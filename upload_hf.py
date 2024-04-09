import subprocess
from huggingface_hub import login
# login()
from huggingface_hub import HfApi
api = HfApi()

# checkpoint_dir="./cms_backend/finetune/ft_models/flan-t5-xl-mt5-v1/"
# checkpoint_name=subprocess.check_output(f"ls {checkpoint_dir} | grep checkpoint | tail -1",shell=True,)
# checkpoint_name=str(checkpoint_name).replace("b'","").replace("\\n'","")
# lcp_path=checkpoint_dir+checkpoint_name
lcp_path='./cms_backend/finetune/ft_models/flan-t5-xl-mt5-v1/checkpoint-31500'
model_path=lcp_path
api.upload_folder(
    folder_path=model_path,
    repo_id="blur0b0t/mh_bhasha3",
    repo_type="model",
)


webapp_path="./cms_interface/build/web"
api.upload_folder(
    folder_path=webapp_path,
    repo_id="blur0b0t/mh_bhasha3",
    repo_type="space",
)