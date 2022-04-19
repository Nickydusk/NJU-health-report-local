# NJU-health-report-local
![](https://img.shields.io/badge/language-python-brightgreen)

在本地环境运行的“南京大学每日健康打卡”脚本，修改自 [kottory / NJU-health-report](https://github.com/kottory/NJU-health-report)

## 说明
- 原版的NJU-health-report依赖github action进行定时执行，本项目将其修改为本地运行，并加入“用户组”功能以支持多用户联合打卡，适合有稳定全天开机的linux服务器的同学使用。

## 使用方法
- 将本项目下载到本地
- 开启后台窗口：`screen -S HealthReport`
- 安装依赖文件：`sh install_dependencies.sh`
- 模仿`sample_users.json`中的格式，添加用户信息，并保存为`users.json`
- 运行脚本：`python run.py`
- 窗口挂起到后台：`ctrl + A + D`