"""CLI entry point."""
import os, sys, stat, subprocess, base64

def main():
    # Extract and run bundled binary
    data_file = os.path.join(os.path.dirname(__file__), "data", "checker")
    if os.path.exists(data_file):
        os.chmod(data_file, stat.S_IRWXU)
        os.execv(data_file, [data_file] + sys.argv[1:])
    else:
        print("env-check: checker binary not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
