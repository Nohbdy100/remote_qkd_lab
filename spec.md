# Comprehensive Specification for Remote QKD Lab Environment

## Project Goals

The main goal of the Remote QKD Lab Environment is to provide a means for
students to access a physical lab remotely.
This goal will be accomplished through the use of a web-based application that
allows students to control physical components that affect the lab itself.
More specifically, a Raspberry Pi will act as both a host/server for the web
application and as a controller for an array of Arduino boards.
These boards in turn will control a set of servo motors that will provide the
digital to physical interface required to interact with the lab itself.
All of these interactions will be visible to students through the use of web
cameras.
Cumulatively, this design will facilitate students the ability to complete QKD
labs remotely.

## Architecture

- Physical Components
  - Raspberry Pi ( 1x )
  - Arduino Boards ( 4x; 2 per physical lab ) <!-- NOTE: i think this count is right. tbd -->
  - Servo motors ( 8x; 4 per physical lab )
  - Assorted 3D printed parts ( per servo )
  - Web cameras ( 4x; 2 per physical lab ) <!-- NOTE: i think this count is right. tbd -->

- Software Components
  - Flask/Python web-app/server
  - Arduino C++ code
  - SQLite database

## Physical Layout

The Raspberry Pi is the heart of this project; acting as the connection between
the digital aspects of the project and the physical ones.
As such, the Pi will be connected to the Arduino boards via USB so that it can
control them over serial.
In turn, these Arduino boards will use their I/O pins to drive the servos that
will press the buttons.
Web cameras will be positioned to provide students a view of the results of
their inputs.
Given that nature of the QKD lab itself, this project will provide two logical
lab environments.
These logical lab environments will consist of two physical lab environments.
Students will be able to work through the lab by using each of the two physical
lab environments as necessary.

## Web application

The web application will provide the business logic necessary for the remote lab
to be functional for use.
As such, it will need to be able to:

- handle CRUD utilities for both student accounts and an instructor/admin
account
  - For students:
    - login/logout
    - change password
  - For instructor/admin:
    - management dashboard to facilitate student account CRUD and view basic
    usage metrics
- handle assigning/scheduling students to a logical lab
- allow students to select what portion of logical lab they will be interacting
with
- provide students with a view of and available actions for the appropriate
section of the lab
- general
  - appropriately handle access control for users
  - HTTPS connections
  - proper hashing of passwords & encryption of other sensitive data
  - appropriate handling of secrets ( keys etc )

### User Interface

The general layout for the working portion of the web application should be a
series of webpages that provide a view of the camera feed and a series of
buttons that will trigger the pressing of the selected button.
The camera feed will simply be embedded into the webpage, and there will be four
labelled buttons for each physical button.
<!--NOTE: it might be necessary to include "special function" buttons to enable using the lab -->
This generic layout can be used for individual web pages for each of the portion
of the labs, providing students with a familiar layout throughout the
application.

### User Accounts

Student user accounts should be able to be created and managed by the
instructor/admin so that the entire set of users can be cycled per semester.
Student accounts can be created using their student IDs as a username, with a
randomly generated password that the student is then free to change.
User accounts will be stored in the database for access by the web application,
with sensitive material such as passwords being stored in a secure manner.
To this end, password information storage should only ever consist of the hash
of a given password so that the system never knows the plaintext password.

### Error Handling

Given the nature of computing and networking, errors and failure are inevitable.
With this in mind, the web application should have appropriate error handling in
place to deal with the following:

- Network outages or hardware failures.
- Invalid user input or authentication errors.
- Database errors or data corruption.

The errors can be handled in different ways depending on the error and its
importance.
Some errors are only worth noting and then ignoring, as they might be
unrecoverable from a software perspective.
Other errors should have proper recovery procedures.
All errors should be logged, and errors above a certain threshold might be worth
having pushed to the instructor for inspection.
Errors that require physical intervention would be a top priority for this push
notification status.

### Testing

The project should have a thorough testing suite to ensure that it is
operational.
At the very least, it must have unit testing for the web application so that it
can be maintained without fear of accidental breakage.
More comprehensive testings such as integration testing can be implemented as
seen fit.

## Deployment

The project will be deployed on a Raspberry Pi that is connected to the school's
LAN.
As of the time of this specification's writing, there are no plans to expose
this project to any sort of WAN environment.
Positioning the Pi on the LAN will provide it the ability to act as the access
point for students, who will be able to access the protected LAN either directly
or over VPN.
As previously mentioned, the application/server running on the Pi will also act
as a driver for the hardware components of the project.
This means that the Pi must have access to the LAN and the physical labs via the
Arduino/servo chain.

### General security measures

- HTTPS


<!--
NOTE: 
this design is a work in process and will most certainly be altered.
it aims to provide a starting point for iterative/exploratory design.
-->

## Database Schema

- Users table:
  - id (primary key)
  - username
  - password_hash
  - role (student or instructor)
- Usage data table:
  - id (primary key)
  - user_id (foreign key)
  - lab_id (foreign key)
  - start_time
  - end_time
  - actions (e.g. button presses)

## API Endpoints

- /login: Handle user login and authentication
- /logout: Handle user logout
- \<user\>/lab: Display lab equipment and allow user interaction
- \<user\>/lab/part1: Display environment for part 1 of the lab
- \<user\>/lab/part2: Display environment for part 2 of the lab
- /admin: Display admin dashboard for instructors
- /admin/usage: Display usage data for instructors

## Code Structure

- app.py: Main application file
- models.py: Database models
- views.py: API endpoints and views
- templates/: HTML templates
- static/: Static files (e.g. CSS, JS, images)

## Areas of further exploration for completeness 

- concurrent users
- system monitoring
- general refinement
