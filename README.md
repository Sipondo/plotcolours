# plotcolours
Custom cycler for Python plotting.

This is my attempt after years of plotting and manually changing settings to streamline the process and settle on a personal style. The concept behind this solution is that the library can simply be imported when importing matplotlib/seaborn. All subsequent plots will automatically follow the style, including markers and hatching.

Paramount is readability when viewed in grayscale (as the happy owner of a grayscale Boox device and to accomodate printing) as well as accessibility to those suffering from colourblindness. The test scripts generate a few example plots in both colour and grayscale. Colourblindness is manually checked via [this simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/).

I heavily recommend this solution for those interested, and feel free to tweak or swap the colours to your liking. The current settings are subject to change as this is the first version.

## Examples

### Colour vs grayscale

| Colour graph                                    | Grayscale graph                                              |
| ----------------------------------------------- | ------------------------------------------------------------ |
| ![colour lineplot](results/line_test.png)       | ![grayscale lineplot](results/line_test_grayscale.png)       |
| ![colour histogram](results/histogram_test.png) | ![grayscale histogram](results/histogram_test_grayscale.png) |
| ![colour barplot](results/barplot_test.png)     | ![grayscale barplot](results/barplot_test_grayscale.png)     |

### Compared to default

| Matplotlib default                                        | Plotcolours                                                                   |
| --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![spectrum default](results/spectrum_default.png)         | ![spectrum grayscale default](results/spectrum_default_grayscale.png)         |
| ![spectrum plotcolours](results/spectrum_plotcolours.png) | ![spectrum grayscale plotcolours](results/spectrum_plotcolours_grayscale.png) |


### Colourblindness

Via: [https://www.color-blindness.com/coblis-color-blindness-simulator/](https://www.color-blindness.com/coblis-color-blindness-simulator/)

| Colourblindness name                  | Graph                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------- |
| Default (no colourblindness)          | ![default](results/barplot_test.png)                                      |
| Protanomaly (red-weak)                | ![protanomaly](results/colourblind/protanomaly.png)                       |
| Deuteranomaly (green-weak)            | ![deuteranomaly](results/colourblind/deuteranomaly.png)                   |
| Tritanomaly (blue-weak)               | ![tritanomaly](results/colourblind/tritanomaly.png)                       |
| Protanopia (red-blind)                | ![protanopia](results/colourblind/protanopia.png)                         |
| Deuteranopia (green-blind)            | ![deuteranopia](results/colourblind/deuteranopia.png)                     |
| Tritanopia (blue-blind)               | ![tritanopia](results/colourblind/tritanopia.png)                         |
| Achromatopsia (total color blindness) | ![achromatopsia](results/colourblind/achromatopsia.png)                   |
| Blue Cone Monochromacy                | ![blue cone monochromacy](results/colourblind/blue_cone_monochromacy.png) |
