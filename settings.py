MONGO_URI = 'mongodb://steemit:steemit@mongo1.steemdata.com:27017/SteemData'
MONGO_DBNAME = 'SteemData'

# 50 items per page by default
PAGINATION_DEFAULT = 50

# allow 1000 requests per minute
RATE_LIMIT_GET = (1000, 60)

# change status message
STATUS_ERR = 'ERROR'

# change default response fields
EXTRA_RESPONSE_FIELDS = ['ID_FIELD']

# no need to define schemas manually
ALLOW_UNKNOWN = True

# can use API from any js app (CORS)
X_DOMAINS = '*'
# X_HEADERS = '*'

# our models
DOMAIN = {
    'Accounts': {
        'id_field': 'name',
        'item_lookup': True,
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'name',
        },
    },
    'Posts': {
        'id_field': 'identifier',
        'item_lookup': True,
        'additional_lookup': {
            'url': 'regex("@[\w]+/[\w]+")',
            'field': 'identifier',
        },
    },
    'Comments': {
        'id_field': 'identifier',
        'item_lookup': True,
        'additional_lookup': {
            'url': 'regex("@[\w]+/[\w]+")',
            'field': 'identifier',
        },
    },
    'PriceHistory': {},
    'Operations': {},
    'AccountOperations': {},
}


