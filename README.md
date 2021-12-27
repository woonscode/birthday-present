# birthday-present
## Background
This is a personal project I made as a birthday present to a close friend of mine. It is a combination of a Telegram chatbot and a webpage.

**Note: Most of the commits have been squashed into the first commit as they contained information related to my friends.**

### Telegram Bot
* Written in Python
* Hosted on Heroku
* Uses a webhook on Heroku (app url acts as a reverse proxy) for updates
* Sensitive information stored as environment variables on Heroku
* GitHub repo integrated with Heroku to automatically deploy on push to **main** branch
* Bot will ask for user's credentials (email, password) to validate identity
* Upon validation, the link to the webpage will be sent to the user

### Webpage
* Hosted on Netlify
* Uses HTML, CSS, JavaScript, jQuery, Bootstrap
* 3 different scroll pages
    * 1st - Present + Cake
    * 2nd - Carousel of photos
    * 3rd - Well-wishes from friends

**Credits:**
* One page scrolling feature - https://github.com/peachananr/onepage-scroll
* Birthday cake CSS - https://codepen.io/JinJay/pen/BqbKNm