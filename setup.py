from pip._internal.cli.main import main

def install_package(package_name: str):
    main(["install", "-U", package_name])

if __name__ == '__main__':
    packages_to_install = ["requests", "colorama"]
    for package in packages_to_install:
        install_package(package)