import subprocess

class DockerExecutor:
    def run_command(self, cmd):
        print(f"\n[>] Executing: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Execution Failed:\n{result.stderr}")
        print(f"[✓] Output:\n{result.stdout}")
        return result.stdout
