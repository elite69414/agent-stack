import os, sys
import subprocess



def run_cli(*args):
    """Helper method to run the CLI with arguments. Cross-platform."""
    try:
        # Use shell=True on Windows to handle path issues
        else:
            result = subprocess.run(
                [*CLI_ENTRY, *args],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
        
        if result.returncode != 0:
            print(f"Command failed with code {result.returncode}")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            
        return result
    except Exception as e:
        print(f"Exception running command: {e}")
        raise