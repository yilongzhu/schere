# Schere - A Cross Platform Copy/Paste Tool


## Motivation
It's frustrating to get links on your phone in mobile only apps. You get a link to a form that has massive word-minimums that you can't type out on a tiny screen. A website sends you a text message with a ridiculous verification code.

**Schere** solves this problem by allowing you to copy and paste text from your phone to your computer or vice versa.


## Technologies Used
* **nginx** for routing
* **Flask** to build the API
* **Flask-SQLAlchemy** as our ORM
* **Flask-Migrate** for database migration
* **marshmallow** for validating input data and serialization/deserialization
* **webargs** for parsing HTTP request arguments
* **Flask-Socket.IO** to use WebSocket connections
