import os


class Baseconfig:

	DEBUG = False
	TESTING = False
	SECRET = os.getenv('SECRET')
	# print(SECRET)
	DATABASE_URI = 'postgres://postgres:rashid123@localhost:5432/dbireporter'


class Developmentconfig(Baseconfig):
	DEBUG = True
	TESTING = False
	ENV = 'Development'
	DATABASE_URI = 'postgresL://postgres:rashid123@localhost:5432/dbireporter'

class Testingconfig(Baseconfig):
	DEBUG = True
	TESTING = True
	ENV = 'Testing'
	DATABASE_URI = 'postgres://postgres:rashid123@localhost:5432/test_ireporter'


class Productionconfig(Baseconfig):
	DEBUG = False
	Testing = False
	ENV = 'Production'
	DATABASE_URI = 'postgres://cwzwwmybfdnund:c88bb6f2d5ef6e19aea84410009e78196de78219036e89c5b6ba5248c91b103b@ec2-54-83-192-245.compute-1.amazonaws.com:5432/d9b83nf6dba47b'


app_config = {
	"Development":Developmentconfig,
	"Testing": Testingconfig,
	"Production":Productionconfig
}