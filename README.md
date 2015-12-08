# Recommendation System

This is the basic recommendation system for CMS system we have accomplished in the previous phase. So far this project includes
a basic scraper to gather data from websites like Guardians and CNN. The recommender will be based on NLP and basic machine 
learning stuff.

## Scraper
Issues running Scraper project in the OS X:
*ImportError: cannot import name xmlrpc_client:*

- sudo rm -rf /Library/Python/2.7/site-packages/six*
- sudo rm -rf /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six*
- sudo pip install six
