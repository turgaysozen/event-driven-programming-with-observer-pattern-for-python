 **You can compare api(normal usage) vs api_v2(observer pattern approach with EDP) and observer_before.py vs observer_after.py**

The observer pattern and event driven programming is similiar to nodejs infrastructure. Nodejs uses single thread event loop
and the event loop waits for events to occur (to observe an event). When an events occured it calls its handler.

Sometimes the observer pattern also called as a listener. Its like an event management system. 
In observer pattern there are 2 roles :subject and observer.
Subject does things, changes things and notifies the observers of any changes that happend. 

Lets suppose that we write backend api and work on the register user function. It does database operations then sends notification to the sales team on the Slack and it sends also a welcome email to the user then writes logs to a server somewhere.
It is possible to write long functions to do all of this actions but functions should be simple and should does only one thing, so we can develop something better. 
Actually python has several event libraries but in this example you'll see a simple solution without any libraries.
