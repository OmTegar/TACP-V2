def update_system():
    import subprocess
    update_status = subprocess.run(["apt-get", "update", "-y"], capture_output=True, text=True).returncode

    if update_status != 0:
        update_process = subprocess.Popen(["apt-get", "update", "-y"])
        update_process.wait()