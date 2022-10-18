# Lord Of The Rings SDK Design

This describes areas put into consideration while working on this SDK.

1. With respect to Authentication, the requests.Session class was subclassed to take advantage of 
certain methods. At the same time deliberate effort was made to keep it separate from the main code. 

Similar effort can be seen in the class `LordOfTheRings`, inheriting from `TheOneAPIBase` class.

2. I noted that `TheOneAPI`mainly uses the `GET` method. I considered having one method that accepts 
different endpoint, but discarded the idea as the codebase wouldn't be easily extensible.

3. Creating the resource, the idea was to gradually build out the endpoint, first as a bare-metal endpoint,
then adding the id (identifier), then subsequent paths.

4. I debated mocking the external API calls in the tests. Seeing as this SDK solely depends on the API, I think
any changes to the API should be caught immediately. Mocking external calls here would make such changes go
under the radar. I am a bit conflicted here.

5. Made use of Makefile to make my life (and the life of others attempting to run this SDK locally) easier.