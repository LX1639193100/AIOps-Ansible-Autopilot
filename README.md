# AIOps-Ansible-Autopilot 🚀

基于 AI 驱动的异构服务器自动化初始化与自愈系统。

## 🌟 项目亮点
- **智能初始化**：结合 AI 自动识别 OS 类型并配置标准环境（Hostname, Directory, Permissions）。
- **自愈闭环**：当 Ansible 出现 `UNREACHABLE`（如 SSH 权限拒绝）时，系统自动触发修复流程。
- **模块化设计**：深度利用 Ansible `file`、`hostname`、`copy` 等核心模块。

## 🛠️ 核心功能展示
### 1. 自动处理权限 (Permissions)
系统自动计算 `chmod` 权限位，避免手动配置导致的 `Permission denied`。


### 2. 自动化逻辑流
1. AI 接收自然语言指令。
2. 生成针对性的 Ansible Inventory。
3. 执行 Playbook 进行基础环境构建。
4. 实时监控执行状态，失败则启动 SSH 秘钥重分发。

## 🚀 快速开始
```bash
# 克隆项目
git clone [https://github.com/your-username/AIOps-Ansible-Autopilot.git](https://github.com/your-username/AIOps-Ansible-Autopilot.git)

# 安装依赖
pip install ansible

# 运行初始化示例
ansible-playbook -i inventory/hosts.ini playbooks/site.yml
