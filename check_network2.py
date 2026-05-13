"""Find the Windows host IP that ComfyUI is listening on"""
import subprocess
import socket

# Try to resolve the Windows host
r = subprocess.run(["hostname"], capture_output=True, text=True)
print(f"WSL hostname: {r.stdout.strip()}")

# Try getting Windows IP from /etc/resolv.conf or other mechanisms
r2 = subprocess.run(["cat", "/etc/resolv.conf"], capture_output=True, text=True)
print(f"DNS: {r2.stdout}")

# Check if we can reach ComfyUI on the Windows host
# The Windows ComfyUI was launched with 秋叶整合包
# Let's see if we can restart it or adjust the firewall from WSL
r3 = subprocess.run(["powershell.exe", "-Command", 
    "Get-NetFirewallRule | Where-Object { $_.DisplayName -like '*Comfy*' -or $_.DisplayName -like '*8188*' } | Format-Table Name,Enabled,Action,Direction -AutoSize"],
    capture_output=True, text=True, timeout=10)
print(f"Firewall rules:\n{r3.stdout[:500]}")

# Check the actual ComfyUI executable path
r4 = subprocess.run(["powershell.exe", "-Command", 
    "Get-Process -Id 5764 -ErrorAction SilentlyContinue | Select-Object ProcessName,Path,StartTime | Format-List"],
    capture_output=True, text=True, timeout=10)
print(f"ComfyUI process:\n{r4.stdout[:500]}")

# Check Windows IP addresses
r5 = subprocess.run(["powershell.exe", "-Command",
    "Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.IPAddress -like '192*' -or $_.IPAddress -like '10*'} | Select-Object IPAddress,InterfaceAlias"],
    capture_output=True, text=True, timeout=10)
print(f"Windows IPs:\n{r5.stdout[:500]}")
