{
    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs";
    };

    outputs = {self, nixpkgs}:
        let pkgs = nixpkgs.legacyPackages.x86_64-linux;
            ppkgs = pkgs.python310Packages;
        in {
            defaultPackage.x86_64-linux = pkgs.hello;

            devShell.x86_64-linux =
                pkgs.mkShell {
                    buildInputs = [
                        pkgs.python3
                        pkgs.xvfb-run
                        pkgs.chromedriver
                        pkgs.chromium
                        # Yak shaving section
                        ppkgs.selenium
                        ppkgs.requests
                        ppkgs.beautifulsoup4
                        ppkgs.pandas
                        ppkgs.python-dateutil
                        ppkgs.numpy
                        ppkgs.lxml
                        # Helpers
                        pkgs.jupyter
                    ];
                };
        };
}
