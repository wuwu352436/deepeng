"""Launch ComfyUI 秋叶整合包 from WSL via PowerShell"""
import subprocess
import time
import socket

# The ComfyUI bundle path
bundle_path = "/mnt/d/BaiduNetdiskDownload/【课程推荐】高级版最新整合包(12.9已更新到最新）/ComfyUI-aki-v3.7"
comfy_dir = f"{bundle_path}/ComfyUI"
python_exe = f"{bundle_path}/python/python.exe"
main_py = f"D:\\BaiduNetdiskDownload\\【课程推荐】高级版最新整合包(12.9已更新到最新）\\ComfyUI-aki-v3.7\\ComfyUI\\main.py"

print(f"Bundle: {bundle_path}")
print(f"Python: {python_exe}")
print(f"Main: {main_py}")

# First check if there's a running ComfyUI on Windows
r = subprocess.run([
    "powershell.exe", "-Command",
    'Get-Process | Where-Object {$_.ProcessName -like "*python*" -or $_.ProcessName -like "*Comfy*"} | Select-Object Id,ProcessName,CPU | Format-Table -AutoSize'
], capture_output=True, text=True, timeout=10)
print(f"\nExisting Python/ComfyUI processes:\n{r.stdout}")

# Kill existing python processes that might be ComfyUI
# (careful not to kill the WSL python)
kill = subprocess.run([
    "powershell.exe", "-Command",
    'Get-Process | Where-Object {$_.ProcessName -eq "python" -and $_.Id -ne 0} | Stop-Process -Force -ErrorAction SilentlyContinue; Write-Output "Cleaned up"'
], capture_output=True, text=True, timeout=10)
print(f"Cleanup: {kill.stdout[:200]}")

# Wait a moment
time.sleep(1)

# Launch ComfyUI from WSL using the Windows Python
# Use the launch command as suggested in the skill docs
launch_cmd = f'Start-Process -NoNewWindow -FilePath "{python_exe}" -ArgumentList \'"{main_py}" --listen 0.0.0.0 --port 8188\''
print(f"\nLaunch command: {launch_cmd}")

result = subprocess.run([
    "powershell.exe", "-Command", launch_cmd
], capture_output=True, text=True, timeout=30)
print(f"Launch stdout: {result.stdout[:200]}")
print(f"Launch stderr: {result.stderr[:200]}")
print(f"Launch rc: {result.returncode}")
