import requests

def test_teams_transcript():
    # Define the URL and headers
    url = 'http://13.126.15.191/fetch-summary'
    headers = {
        'authToken': '9960e106-af5b-4a93-bdae-8e9295a9b847',
        'Content-Type': 'application/json'
    }

    # Define the data payload
    data = {
        "transcript": "WEBVTT 00:00:24.802 --> 00:00:27.862 <v Abhishek Sharma>Hello can you share what is the purpose of this call?</v> 00:00:30.832 --> 00:00:34.782 <v Rahul Kumar Singh>It'\''s written on the top PIMCO stand up.</v> 00:00:40.482 --> 00:00:42.252 <v Harvesh Kumar>As you have this habit, what do you accept that?</v> 00:00:46.542 --> 00:00:50.252 <v Rahul Kumar Singh>Your call is being recorded for training and monitoring purpose.</v> 00:00:53.212 --> 00:00:55.652 <v Vipra Sagar>It will all be transcribed in some time.</v> 00:00:56.852 --> 00:00:57.842 <v Harvesh Kumar>Nice call to winning.</v> 00:01:10.812 --> 00:01:13.222 <v Rahul Kumar Singh>Ohh, we have 9 participants.</v> 00:01:13.762 --> 00:01:16.662 <v Rahul Kumar Singh>We can start vipra can we start with you?</v> 00:01:21.702 --> 00:01:23.472 <v Vipra Sagar>Is showing the daily stand up right?</v> 00:01:24.702 --> 00:01:25.062 <v Rahul Kumar Singh>Uh, yes.</v> 00:01:25.942 --> 00:01:29.332 <v Vipra Sagar>OK, so hiding I will be working on Syria.</v> 00:01:29.342 --> 00:01:36.462 <v Vipra Sagar>New test is automation and apart from that I also have a new A application aldoc to automate.</v> 00:01:36.472 --> 00:01:41.372 <v Vipra Sagar>So I'\''ll be trying to do the manual testing and further work on its automation.</v> 00:01:41.842 --> 00:01:43.932 <v Vipra Sagar>That'\''s all next can be susheel.</v> 00:01:58.902 --> 00:01:59.722 <v Vipra Sagar>So she got you there.</v> 00:02:03.632 --> 00:02:04.762 <v Susheel Mahobia>Hey, how about yes.</v> 00:02:03.682 --> 00:02:05.442 <v Vipra Sagar>We can go home. Yep.</v> 00:02:05.632 --> 00:02:21.682 <v Susheel Mahobia>So Ohh, hiding for today I'\''ll be doing JIRA testing over bar application as I have some newly assigned 0 and once done I will be doing the regression as we the release or this week and that'\''s it from my side.</v> 00:02:21.872 --> 00:02:23.622 <v Susheel Mahobia>Next can be grinder.</v> 00:02:23.632 --> 00:02:24.012 <v Susheel Mahobia>If not then.</v> 00:02:25.942 --> 00:02:26.172 <v Dhirender Singh>Yeah.</v> 00:02:26.182 --> 00:02:26.452 <v Dhirender Singh>Thanks.</v> 00:02:26.462 --> 00:02:26.872 <v Dhirender Singh>You should.</v> 00:02:27.482 --> 00:02:27.972 <v Dhirender Singh>Bye guys.</v> 00:02:28.022 --> 00:02:31.512 <v Dhirender Singh>So I'\''m occupied with some 0 testing for application.</v> 00:02:31.662 --> 00:02:33.812 <v Dhirender Singh>Some tickets are related to the UI code refactoring.</v> 00:02:34.062 --> 00:02:38.682 <v Dhirender Singh>I'\''m working over them apart from this, so without any context.</v> 00:02:42.882 --> 00:02:43.792 <v Savitra Marathe>Uh, didn'\''t you?</v> 00:02:43.852 --> 00:02:44.482 <v Savitra Marathe>You took my name.</v> 00:02:46.522 --> 00:02:46.892 <v Dhirender Singh>I guess so.</v> 00:02:48.132 --> 00:02:48.412 <v Savitra Marathe>OK.</v> 00:02:48.622 --> 00:02:50.122 <v Savitra Marathe>Thank you so much.</v> 00:02:50.132 --> 00:03:06.722 <v Savitra Marathe>I'\''ll be doing the automation fixes today and we have a a service ready which has been migrated to Aurora so it will check the changes manually with the automation as well and on the other hand I have angered the migration changes on the US so I need to test it as well.</v> 00:03:07.772 --> 00:03:08.552 <v Savitra Marathe>Yeah, that'\''s all.</v> 00:03:08.632 --> 00:03:09.052 <v Savitra Marathe>Thank you.</v> 00:03:09.492 --> 00:03:10.352 <v Savitra Marathe>Next time we leave show.</v>"
    }

    # Send the POST request
    response = requests.post(url, headers=headers, json=data)

    # Check the response
    if response.status_code == 200:
        print("Request was successful!")
        print("Response:", response.json())  # Print the JSON response if applicable
        return "Working"
    else:
        print("Request failed with status code:", response.status_code)
        return "Failed"

# Call the test function
result = test_teams_transcript()
print("Test result:", result)