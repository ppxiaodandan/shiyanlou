import os
class DefaultConfig(object):
	PROJECT = "loucloud"

	DEBUG =False
	TESTING =False
	SECRET_KEY='your secret ky'
	SQLALCHEMY_ECHO=True
	CACHE_TYPE='simple'
	CACHE_DEFAULT_TIMEOUT=60
