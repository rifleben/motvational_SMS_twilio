# motvational_SMS_twilio

Quick application created to learn how to use Twilio's API for SMS messaging. Sends a motivational text message at 4:30 pm machine time, to a selected recipient with a random quote from a random quote API.




Python Packages Used:
- Twilio.rest:
  - Used to access Twilio Client and send messages
- Requests:
  - Handles API requests from random quotes API
- Datetime:
  - Used to check current time in order to send message at accurate time
- Random:
  - Used to select a random quote from our API response quotes
- Time:
  - Used to "sleep" the program between text messages
