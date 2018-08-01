# TwitterRealtimedata
This module is used to fetch realtime data tweets related to any topic.Module stores the tweets with hashtags in the file system.Data in the file contains tweets and corresponding hashtags.


#How to use code:
a.)Code reads configuration from the file named config.ini
b.)config.ini contains logging_level header and user header
c.)logging_level header contains the level on which you want logginng and user header contains twitter credentails for the user app.


#Command to use code:

1.)python Streamdata.py -ushubham -s"NRC,Assam,Mamta Banerjee,mamta" -f"/home/shubham/Desktop/streaming.txt"
2.)Use python Streamdata.py -h to know more about arguements.

Usage: Streamdata.py [options]

Optional app description

Options:
  -h, --help            show this help message and exit
  -u USERNAME, --username=USERNAME
                        enter the username for which you have access
                        token,consumer_token etc.
  -s SEARCH_STRING, --search_string=SEARCH_STRING
                        Query string which you want to filter for realtimedata
  -f FILEPATH, --filepath=FILEPATH
                        enter the filepath in which you want to write real
                        time data
