# Video-content-processing-for-query-search

If you have a dataset containing large number of videos and you have to search video against your query,Moreover if you're required video have hours of duration and you have to search specific sub topic within video. Can yoou imagine how time consuming this process will be. Further more the dataset can also be dynamic, may be it is increasing and you are adding more and more video. The goal of this project is to resolve this problem.

This is an offline GUI-based desktop application which allow user to upload video in dataset and can search query against the videos.

User can upload video and can see the transcribe form of it on the screen.User can see the transcribtion only and can upload as well.

User can ask query in form of text and speech both.If user ask query iin voice, then his/her voice is transcribe.The application finds most similarity between video (which are already transcribe, lemmatize and strored in .txt form in the application) and query. Relevent video are shown on to the user screen in the descending order(most similar one on top). User is allowes to either play any single video or can play All. Furthermore, user can ask query against any specific video and search. The application can search the query within the video and list all the points of time at which particular asked topic is discussed. Now user also allow to jump to that duration of video automatically.

In this project different python libraries are used. Moreover the concept of multi threading is also implemented.The lemmatization and stemming is also applied on the entired transcribe video and user asked query.

For finding the similarity against dataset documents and user ask query vector space model is used.

This application also provide interactive user friend to reduce user's slips or mistakes.