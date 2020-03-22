import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '6dVMAZOdaNfMIzsOFhjVRv6l5dy07UHS'