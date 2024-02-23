# Perplex

![image](https://github.com/cognivore/perplex/assets/66186054/6f1995a3-4920-45fb-bf33-bcefc7668d69)

A template to bootstrap Selenium scraping with Nix.

## Installation

If you have `nix` and `direnv`, then just `direnv allow`.

## Installing `nix` and `direnv`

Luckily for you, we have a [single-click installer](https://github.com/cognivore/icfpc-compute/blob/main/installer.sh) for `nix`, `direnv` and [`home-manager`](https://www.youtube.com/watch?v=PmD8Qe8z2sY).

## Running

`./demo.py` should just work. If it doesn't, try `xvfb-run ./demo.py`. This one will work for sure, even on a server without a real X framebuffer!

## Open questions

 - [ ] Can we use `which` instead of nix store lookup to find `chromedriver` and `chromium`?
