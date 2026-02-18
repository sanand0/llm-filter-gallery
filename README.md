# Image Filters Discovery with LLMs

## Install Fred's ImageMagick Scripts and GMIC

Install these tools however you like. I used:

```bash
# Install ImageMagick
cd ~/.local/bin; curl -L https://imagemagick.org/archive/binaries/magick -o magick && chmod +x magick

# Copy a 2-year old clone of Fred's ImageMagick Scripts into fred/bin
git clone --depth 1 https://github.com/milahu/imagemagick-scripts fred

cd fred/bin
rg --no-filename --no-line-number '# (NAME|PURPOSE|DESCRIPTION)' -A 3 * > fred-imagemagick-scripts-descriptions.txt

# Install GMIC
wget https://gmic.eu/get_file.php?file=linux/gmic_3.7.0_ubuntu24-04_noble_amd64.deb
sudo apt install ./gmic_*.deb
```
