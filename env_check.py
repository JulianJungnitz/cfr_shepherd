#%%
import yaml
import subprocess
import sys

def check_conda_availability(pkg_name):
    """
    Uses `conda search` to check if a package with name `pkg_name` exists.
    Returns True if any match is found, otherwise False.
    """
    try:
        # Run conda search
        result = subprocess.run(
            ["conda", "search", pkg_name],
            capture_output=True,
            text=True,
            check=False
        )
        # If 'No match found' is in stdout or stderr, then conda didn't find it
        if "No match found" in result.stdout or "No match found" in result.stderr:
            return False
        # Otherwise, assume we found at least one match
        return True
    except FileNotFoundError:
        print("Error: conda not found on your PATH. Make sure conda is installed and activated.")
        sys.exit(1)

def main(env_file="v1_shepherd.yml"):
    """
    Reads `env_file`, locates the pip dependencies, and checks for their presence in conda.
    """
    with open(env_file, "r") as f:
        data = yaml.safe_load(f)

    # Grab dependencies
    dependencies = data.get("dependencies", [])

    # Collect any packages found in pip:
    pip_packages = []
    for item in dependencies:
        # item can be a string or a dict if it includes 'pip'
        if isinstance(item, dict) and "pip" in item:
            pip_packages.extend(item["pip"])

    if not pip_packages:
        print("No pip dependencies found in the environment file.")
        return

    print(f"Found {len(pip_packages)} pip packages in '{env_file}':\n")
    
    available = []
    not_available = []
    for pkg in pip_packages:
        # pkg might have a version specifier, e.g., 'package==1.2.3'
        pkg_name = pkg.split("==")[0]
        # Another scenario: 'package>=1.2' or other PEP 440 specifiers
        # For a more thorough approach, you'd parse or strip them differently.
        
        # Check conda availability
        is_available = check_conda_availability(pkg_name)
        if is_available:
            print(f"[AVAILABLE on conda]   {pkg}")
            available.append(pkg)

        else:
            print(f"[NOT on conda]         {pkg}")
            not_available.append(pkg)

    print("\nSummary:")
    for pkg in available:
        print(f"  - {pkg}")
    
    print("\nPackages not found on conda:")
    for pkg in not_available:
        print(f"  - {pkg}")
    

if __name__ == "__main__":
    main()
