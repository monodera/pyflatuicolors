# pyflatuicolors

pyflatuicolors is a python module to access to the flat UI colors by their names. 

## Flat UI Colors
See [http://flatuicolors.com/](Flat UI Colors) for more details.

## Examples
Put flatuicolors.py at any locations which are in `$PYTHONPATH`.

```python
    import flatuicolors
    
    # pick up one of the colors
    flatuicolors.pick('clouds')
    
    # list all color names
    flatuicolors.list()
    
    # get all color keys
    flatuicolors.get_color_keys()
    
    # get all color values (hex color codes)
    flatuicolors.get_color_values()
```
