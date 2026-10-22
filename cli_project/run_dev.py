import sys
from mcp.cli.cli import app

if __name__ == "__main__":
    # Inject the command-line arguments the framework expects
    sys.argv = ["mcp", "dev", "mcp_server.py"]
    
    # Fire up the official CLI directly inside your stable .venv
    app()
