# DBIrepoter
[![Build Status](https://travis-ci.org/MUGABA/DBIrepoter.svg?branch=master)](https://travis-ci.org/MUGABA/DBIrepoter)
[![Coverage Status](https://coveralls.io/repos/github/MUGABA/DBIrepoter/badge.svg?branch=master)](https://coveralls.io/github/MUGABA/DBIrepoter?branch=master)

## About Irepoter

Irepoter lets any/every citizen on notice to the government what is is happening to its citizens. In irepoter citizens report about incidents like accidents,occassions and things that require the government interventions. Citizens can also report issues of corruptions

## Features

 - A user can create an account or Signup.
 - A user can signin inti the application after creating the account.
 - A user can report an Incidents that just happened call it red-flag or interventions
 - A user can update the location of the incident 
 - A user can update also their comment upon creation of their incident.
 - A user can view a specific incident created by using thier id...
 - A user can view all the incidents that have been created whether red-flags or interventions
 - A user can delete an incident they created but they cannot delete the one they didnot create
 - An admin can change the status of the incident and once the status changed nothing can be doen on it.An incident is either 'Draft','Under investigation','Resolved',or 'Rejected'..


## Getting Started:
Clone the repository to your computer [link](https://github.com/MUGABA/DBIrepoter)

## prequisites:
A computer with windows, linus or macOs operating system will work.
-python 3.6.
flamework is vanilla- flask
-pytest for testing
- Postman to test the endpoints
- a prefered text editor.
- Git to keep track of the changes.

## Installing 
Clone the repository to your computer [link](https://github.com/MUGABA/DBIrepoter)

Open the terminal or command prompt for windows

Type the following;

$ cd DBirepoter
$ git checkout develop # to switch to the develop branch
$ pip install -r requirements.txt
$ python run.py

## Testing the Api
install the tester or test runner

$ pip install pytest

$ pytest ## To run the tests


## Endpoints

| Endpoint                  | Functionality|
| ---------                 | ---------------|
| POST /api/v1/users        | Create User account|
| POST /api/vi/users/login  | Signin a user |
| POST /api/v1/red-flags    | To report a redflag by the user|
| POST /api/v1/interventions | To report an interventions by the user |
| GET /api/v1/red-flags     | To get all redflags created by the users|
| GET /api/v1/interventions | To get all interventions created by the users|
| GET /api/v1/red-flags/<int:incident_id> | To get a specific red-flag created by the users|
| GET /api/v1/interventions/<int:incident_id> | To get specific  intervention created by users |
| PATCH /api/v1/red-flags/<int:incident_id>/location | To edit the location of a redflag |
| PATCH /api/v1/interventions/<int:incident_id>/location | to edit locaton of an interventions |
| PATCH /api/v1/red-flags/<int:incident_id>/comment | To edit the comment  of a redflag |
| PATCH /api/v1/interventions/<int:incident_id>/comment | to edit comment of an interventions |
| PATCH /api/v1/red-flags/<int:incident_id>/status | To edit the status  of a redflag |
| PATCH /api/v1/interventions/<int:incident_id>/status | to edit status of an interventions |
| DELETE /api/v1/red-flags/<int:incident_id> | To delete a specific red-flag created |
| DELETE /api/v1/interventions/<int:incident_id> | To delete specific  intervention created |

## Built with
- python 3.6.5
- flask (python microframework)

## Author
- MUGABA MUHAMAD RASHID
- EMAIL: mugabamuha@gmail.com
- Contact: 256774389392

## Tools Used
- pylint
- pytest
- virtual environment

## Acknowledgements

Thanks to great friends Keneth,Bashir and Andela for setting search a high standard that has triggered me to learn more than I expected..
