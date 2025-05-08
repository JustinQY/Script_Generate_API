# 使用官方 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 拷贝依赖和代码
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 设置默认端口
ENV PORT=7860

# 启动 FastAPI 服务
CMD ["./start.sh"]