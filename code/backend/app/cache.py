#import and initialize caching
from flask_caching import Cache
cache = Cache()

# created as a separate entity to avoid any circular import