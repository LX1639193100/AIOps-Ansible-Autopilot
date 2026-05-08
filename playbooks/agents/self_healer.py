import subprocess

def fix_ssh_permission(host, password):
    """
    当检测到 SSH 连接失败时，自动尝试分发公钥
    """
    print(f"检测到 {host} 连接失败，正在尝试自动分发 SSH 秘钥...")
    try:
        # 使用 sshpass 自动处理密钥分发
        cmd = f"sshpass -p {password} ssh-copy-id -o StrictHostKeyChecking=no root@{host}"
        subprocess.run(cmd, shell=True, check=True)
        return True
    except Exception as e:
        print(f"修复失败: {e}")
        return False
