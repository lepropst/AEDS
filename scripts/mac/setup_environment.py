import os

import subprocess
import sys
from urllib.request import urlopen

def setup_virtual_environment(venv_name='venv'):
    # Check if the 'venv' module is available
    try:
        import venv
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'virtualenv'])
        import venv

    # Create a new virtual environment
    venv_dir = os.path.join(os.getcwd(), venv_name)
    if not os.path.exists(venv_dir):
        venv.create(venv_dir, with_pip=True)

    # Activate the virtual environment
    activate_script = os.path.join(venv_dir, 'bin', 'activate')
    if os.path.exists(activate_script):
        subprocess.run(['source', activate_script], shell=True)
    else:
        print(f"Failed to find the activation script: {activate_script}")
        sys.exit(1)

    # Install packages or perform any other setup tasks
    # For example, installing a package using pip
    subprocess.check_call([venv_dir+'/bin/pip', 'install', 'package_name'])

# Usage: python script_name.py [venv_name]
# If no venv_name is provided, it defaults to 'venv'
if __name__ == '__main__':
    venv_name = sys.argv[1] if len(sys.argv) > 1 else 'venv'
    setup_virtual_environment(venv_name)