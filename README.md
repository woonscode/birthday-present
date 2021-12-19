# birthday-present
## Background
This is a personal project I made as a birthday present to a friend of mine. It is a combination of a Telegram chatbot and a webpage.

### Telegram Bot
* Hosted on Heroku
* Uses a webhook on Heroku (app url as a reverse proxy) for updates
* Sensitive information stored as environment variables on Heroku
* GitHub repo integrated with Heroku to automatically deploy on push to **main** branch
* Bot will ask for user's information to validate identity
* Upon validation, the link to the webpage will be sent to the user

### Webpage
* Hosted on Netlify
* Uses HTML, CSS, JavaScript, jQuery, Bootstrap
* 3 different scrolls
    * 1st - Present + Cake
    * 2nd - Carousel of photos
    * 3rd - Well-wishes from friends

**Credits:**
* One page scrolling feature - https://github.com/peachananr/onepage-scroll
* Birthday cake CSS - https://codepen.io/JinJay/pen/BqbKNm