"""
A Python module to import a hex color string from colors listed Flat UI Colors (http://flatuicolors.com/)
"""
_flatuicolors = {
    'turquoise':       '#1abc9c',
    'greensea':        '#16a085',
    'emerald':         '#2ecc71',
    'nepharitis':      '#27ae60',
    'peterriver':      '#3498db',
    'belizehole':      '#2980b9',
    'amethyst':        '#9b59b6',
    'wisteria' :       '#8e44ad',
    'wetasphalt':      '#34495e',
    'midnightblue':    '#2c3e50',
    'sunflower':       '#f1c40f',
    'orange':          '#f39c12',
    'carrot':          '#e67e22',
    'pumpkin':         '#d35400',
    'alizarin':        '#e74c3c',
    'pomegranate':     '#c0392b',
    'clouds':          '#ecf0f1',
    'silver':          '#bdc3c7',
    'concrete':        '#95a5a6',
    'asbestos':        '#7f8c8d'}

def pick(cname):
    try:
        cname_sanitized = cname.lower().replace(" ","")
        return _flatuicolors.get(cname_sanitized)
    except:
        print 'No color %s is in flat ui colors.' % cname
        print 'Available colors are:'
        for i in _flatuicolors.keys():
            print "  %-14s" % i

def list():
    for i in _flatuicolors.keys():
        print "  %-14s" % i

def all_color_keys():
    return _flatuicolors.keys()

def all_color_values():
    return _flatuicolors.values()
