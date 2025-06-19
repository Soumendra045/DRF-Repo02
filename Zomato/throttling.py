from rest_framework.throttling import UserRateThrottle

class ProductThrottle(UserRateThrottle):
    scope='product-list'

class CustomerThrottle(UserRateThrottle):
    scope='customer-list'