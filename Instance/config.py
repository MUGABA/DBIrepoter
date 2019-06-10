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
	Testing = False
	DEBUG = False
	ENV = 'Production'
	DATABASE_URI = 'postgres://hqxmdfvezeajqe:087d503b66003d4e677aa5579a35a1c393e8bd3cee5ef37e6ca8525b8e75107a@ec2-54-243-241-62.compute-1.amazonaws.com:5432/d59pi2aajcunvi'


app_config = {
	"Development":Developmentconfig,
	"Testing": Testingconfig,
	"Production":Productionconfig
}