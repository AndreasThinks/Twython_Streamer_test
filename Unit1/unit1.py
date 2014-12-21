from twython import TwythonStreamer

consumer_key = 'uVUteW2inRpnphqf1qaAPDb8s'
consumer_secret = 'Up4dH27jugMYkF1CHGTgcBF1TJK6Shwfy8s6JjiCewxPsqEiRv'

access_token = '14881209-0MiNGaQLI1LrDKyBEzaAykaFe9VOFzzQvDahDw347'
access_token_secret = 'QoX7kZ4ejtVelLP7cHvGnqhbbBtkwKCTgsY1UQBcyH80J'

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

stream = MyStreamer(consumer_key, consumer_secret,
                    access_token, access_token_secret)
stream.statuses.filter(locations='-122.75,36.8,-121.75,37.8')