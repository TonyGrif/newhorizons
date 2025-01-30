{
  description = "Nix flake for newhorizons";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-24.11";
    nixpkgs-unstable.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    nixpkgs,
    nixpkgs-unstable,
    ...
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      overlays = [
        (final: prev: {
          unstable = import nixpkgs-unstable {
            system = prev.system;
          };
        })
      ];
    };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [ unstable.uv ];

      shellHook = ''
        if [ -d ".venv" ]; then
          source .venv/bin/activate
        else
          uv sync
          source .venv/bin/activate
        fi
      '';
    };
  };
}
