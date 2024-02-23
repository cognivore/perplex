import subprocess

def get_nix_output_path(attribute_name):
    command = ["nix", "eval", "--inputs-from", ".", "--raw", f"nixpkgs#legacyPackages.x86_64-linux.{attribute_name}"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        raise Exception(f"Failed to get path for {attribute_name}")

def nix_which(attribute_name):
    y = get_nix_output_path(attribute_name)
    return f"{y}/bin/{attribute_name}"

if __name__ == "__main__":
    print(get_nix_package_path("hello"))
