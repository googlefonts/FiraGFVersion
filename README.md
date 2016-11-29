# Fira v2.0 for Google Fonts
by Carrois Apostrophe

This repository hot fixes the binary sources for [Fira](https://github.com/carrois/Fira/tree/master/Fira_Sans_4_2)

## Changes from source
1. Change font names to fit within Google Font's api. We can only have weights from Thin to Black.
2. Convert .otfs to ttfs
3. Autohint 


## Building fonts
```
$ cd build
$ sh build.sh
```

## Dependencies
[FontTools](https://github.com/fonttools/fonttools)
[Font Bakery](https://github.com/googlefonts/fontbakery)
[ttfautohint](https://www.freetype.org/ttfautohint/)
[fontforge](https://fontforge.github.io/en-US/)