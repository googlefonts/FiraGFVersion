import os

REMAP_FONTS = [
# Roman
('FiraSans-Hair.ttf', 'FiraSansHairline-Regular.ttf.renamed'),
('FiraSans-Thin.ttf', 'FiraSans-Thin.ttf.renamed'),
('FiraSans-ExtraLight.ttf', 'FiraSans-ExtraLight.ttf.renamed'),
('FiraSans-Light.ttf', 'FiraSans-Light.ttf.renamed'),
('FiraSans-Regular.ttf', 'FiraSans-Regular.ttf.renamed'),
('FiraSans-Medium.ttf', 'FiraSans-Medium.ttf.renamed'),
('FiraSans-SemiBold.ttf', 'FiraSans-SemiBold.ttf.renamed'),
('FiraSans-Bold.ttf', 'FiraSans-Bold.ttf.renamed'),
('FiraSans-ExtraBold.ttf', 'FiraSans-ExtraBold.ttf.renamed'),
('FiraSans-Heavy.ttf', 'FiraSans-Black.ttf.renamed'),
('FiraSans-Ultra.ttf', 'FiraSansUltra-Regular.ttf.renamed'),
# Roman Italic
('FiraSans-HairItalic.ttf', 'FiraSansHairline-Italic.ttf.renamed'),
('FiraSans-ThinItalic.ttf', 'FiraSans-ThinItalic.ttf.renamed'),
('FiraSans-ExtraLightItalic.ttf', 'FiraSans-ExtraLightItalic.ttf.renamed'),
('FiraSans-LightItalic.ttf', 'FiraSans-LightItalic.ttf.renamed'),
('FiraSans-Italic.ttf', 'FiraSans-Italic.ttf.renamed'),
('FiraSans-MediumItalic.ttf', 'FiraSans-MediumItalic.ttf.renamed'),
('FiraSans-SemiBoldItalic.ttf', 'FiraSans-SemiBoldItalic.ttf.renamed'),
('FiraSans-BoldItalic.ttf', 'FiraSans-BoldItalic.ttf.renamed'),
('FiraSans-ExtraBoldItalic.ttf', 'FiraSans-ExtraBoldItalic.ttf.renamed'),
('FiraSans-HeavyItalic.ttf', 'FiraSans-BlackItalic.ttf.renamed'),
('FiraSans-UltraItalic.ttf', 'FiraSansUltra-Italic.ttf.renamed'),

# Compressed
('FiraSansCompressed-Hair.ttf', 'FiraSansCompressedHairline-Regular.ttf.renamed'),
('FiraSansCompressed-Thin.ttf', 'FiraSansCompressed-Thin.ttf.renamed'),
('FiraSansCompressed-ExtraLight.ttf', 'FiraSansCompressed-ExtraLight.ttf.renamed'),
('FiraSansCompressed-Light.ttf', 'FiraSansCompressed-Light.ttf.renamed'),
('FiraSansCompressed-Regular.ttf', 'FiraSansCompressed-Regular.ttf.renamed'),
('FiraSansCompressed-Medium.ttf', 'FiraSansCompressed-Medium.ttf.renamed'),
('FiraSansCompressed-SemiBold.ttf', 'FiraSansCompressed-SemiBold.ttf.renamed'),
('FiraSansCompressed-Bold.ttf', 'FiraSansCompressed-Bold.ttf.renamed'),
('FiraSansCompressed-ExtraBold.ttf', 'FiraSansCompressed-ExtraBold.ttf.renamed'),
('FiraSansCompressed-Heavy.ttf', 'FiraSansCompressed-Black.ttf.renamed'),
('FiraSansCompressed-Ultra.ttf', 'FiraSansCompressedUltra-Regular.ttf.renamed'),
# Compressed Italic
('FiraSansCompressed-HairItalic.ttf', 'FiraSansCompressedHairline-Italic.ttf.renamed'),
('FiraSansCompressed-ThinItalic.ttf', 'FiraSansCompressed-ThinItalic.ttf.renamed'),
('FiraSansCompressed-ExtraLightItalic.ttf', 'FiraSansCompressed-ExtraLightItalic.ttf.renamed'),
('FiraSansCompressed-LightItalic.ttf', 'FiraSansCompressed-LightItalic.ttf.renamed'),
('FiraSansCompressed-Italic.ttf', 'FiraSansCompressed-Italic.ttf.renamed'),
('FiraSansCompressed-MediumItalic.ttf', 'FiraSansCompressed-MediumItalic.ttf.renamed'),
('FiraSansCompressed-SemiBoldItalic.ttf', 'FiraSansCompressed-SemiBoldItalic.ttf.renamed'),
('FiraSansCompressed-BoldItalic.ttf', 'FiraSansCompressed-BoldItalic.ttf.renamed'),
('FiraSansCompressed-ExtraBoldItalic.ttf', 'FiraSansCompressed-ExtraBoldItalic.ttf.renamed'),
('FiraSansCompressed-HeavyItalic.ttf', 'FiraSansCompressed-BlackItalic.ttf.renamed'),
('FiraSansCompressed-UltraItalic.ttf', 'FiraSansCompressedUltra-Italic.ttf.renamed'),

# Condensed
('FiraSansCondensed-Hair.ttf', 'FiraSansCondensedHairline-Regular.ttf.renamed'),
('FiraSansCondensed-Thin.ttf', 'FiraSansCondensed-Thin.ttf.renamed'),
('FiraSansCondensed-ExtraLight.ttf', 'FiraSansCondensed-ExtraLight.ttf.renamed'),
('FiraSansCondensed-Light.ttf', 'FiraSansCondensed-Light.ttf.renamed'),
('FiraSansCondensed-Regular.ttf', 'FiraSansCondensed-Regular.ttf.renamed'),
('FiraSansCondensed-Medium.ttf', 'FiraSansCondensed-Medium.ttf.renamed'),
('FiraSansCondensed-SemiBold.ttf', 'FiraSansCondensed-SemiBold.ttf.renamed'),
('FiraSansCondensed-Bold.ttf', 'FiraSansCondensed-Bold.ttf.renamed'),
('FiraSansCondensed-ExtraBold.ttf', 'FiraSansCondensed-ExtraBold.ttf.renamed'),
('FiraSansCondensed-Heavy.ttf', 'FiraSansCondensed-Black.ttf.renamed'),
('FiraSansCondensed-Ultra.ttf', 'FiraSansCondensedUltra-Regular.ttf.renamed'),
# Condensed Italic
('FiraSansCondensed-HairItalic.ttf', 'FiraSansCondensedHairline-Italic.ttf.renamed'),
('FiraSansCondensed-ThinItalic.ttf', 'FiraSansCondensed-ThinItalic.ttf.renamed'),
('FiraSansCondensed-ExtraLightItalic.ttf', 'FiraSansCondensed-ExtraLightItalic.ttf.renamed'),
('FiraSansCondensed-LightItalic.ttf', 'FiraSansCondensed-LightItalic.ttf.renamed'),
('FiraSansCondensed-Italic.ttf', 'FiraSansCondensed-Italic.ttf.renamed'),
('FiraSansCondensed-MediumItalic.ttf', 'FiraSansCondensed-MediumItalic.ttf.renamed'),
('FiraSansCondensed-SemiBoldItalic.ttf', 'FiraSansCondensed-SemiBoldItalic.ttf.renamed'),
('FiraSansCondensed-BoldItalic.ttf', 'FiraSansCondensed-BoldItalic.ttf.renamed'),
('FiraSansCondensed-ExtraBoldItalic.ttf', 'FiraSansCondensed-ExtraBoldItalic.ttf.renamed'),
('FiraSansCondensed-HeavyItalic.ttf', 'FiraSansCondensed-BlackItalic.ttf.renamed'),
('FiraSansCondensed-UltraItalic.ttf', 'FiraSansCondensedUltra-Italic.ttf.renamed'),
]

for old_name, new_name in REMAP_FONTS:
    if old_name in os.listdir('.'):
        os.rename(os.path.join('.', old_name), os.path.join('.', new_name))
        print 'renamed %s to %s' % (old_name, new_name)
print 'Done renaming'

for font in os.listdir('../fonts'):
    print font