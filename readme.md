<h1>
URL Hashing System 
</h1>

URL shortening is used to create shorter aliases for long URLs. We call these shortened aliases “short links.” Users are redirected to the original URL when they hit these short links. Short links save a lot of space when displayed, printed, messaged, or tweeted. Additionally, users are less likely to mistype shorter URLs.
***
<h2>
Requirements
</h2>

* Given a URL, our service should generate a shorter and unique alias of it. This is called a short link.
* When users access a short link, our service should redirect them to the original link.
* Links will expire after a standard default timespan ***(3 years)***. Users should be able to specify the expiration time.
* User can specify if the short url will be one time use. If the url is one-time-use it will expire as soon as it is used once or if it reaches its expiration date.

<br>
<br>

<h2>
URL Encoding
</h2>
To convert a long URL into a unique short URL Base62 hashing techniques is used. Each long URL is given a record_id before saving to a database. This record_id will be similar to index as in:
it will be an auto increment intiger field and will be unique in the table. As this record_id is unique it can be used for creating a the Base62 hash for the long URL.

<br>
<br>

<h2>
Database
</h2>
The database used is MongoDb as it is highly scalable and we dont need relationships  between our objects.

<br>
<br>

<h2>
Web Framework
</h2>

Django was used as the web framework for developing this URL Hashing System. Django is an open-source framework for backend web applications based on Python. Its main goals are simplicity, flexibility, reliability, and scalability.

<br>
<br>

***