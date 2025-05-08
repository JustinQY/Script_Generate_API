from huggingface_hub import snapshot_download, login


hf_token = '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'
login(token=hf_token)

# 下载模型（需同意许可的模型如 LLaMA2 必须先申请权限）
snapshot_download(
    # repo_id="meta-llama/Llama-2-7b-hf",  # 替换成你要下载的模型名
    repo_id="google/flan-t5-small",
    local_dir="./flan-t5-small",             # 下载到的本地目录
    token=True                           # 使用已登录 token
)