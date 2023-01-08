<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/utsav82/Bollywood-Back">
  </a>

  <h3 align="center">Ani-Oke</h3>

  <p align="center">
    "Sing along to your favorite anime hits with Ani-oke"
    <br />
    <a href="https://ani-oke.netlify.app/">View Demo</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

![HomePage](https://user-images.githubusercontent.com/91375797/211187775-c71affca-5eac-4764-bfb1-a905227b7026.png)

Ani-oke is a webapp that allows users to play anime openings and endings using Spotify's web API. The app also generates romanized lyrics for the selected song using web scraping from various lyrics websites. With Ani-oke, users can sing along to their favorite anime songs, even if they don't know how to read Japanese. The app is perfect for anime fans who want to practice their singing skills or just have some fun with their friends. Simply search for an anime song, and Ani-oke will take care of the rest!

### Built With

- [![React][react.js]][react-url]
- ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
- ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Spotify](https://img.shields.io/badge/Spotify-1ED760?style=for-the-badge&logo=spotify&logoColor=white)
- ![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You will need the following software.

For Node
- npm
  ```sh
  npm install npm@latest -g
  ```
For Flask
- pip
```sh
python -m pip install --upgrade pip.
```
### Installation

_Below are the instructions to setup the project locally , don't forget to Cd to the respective folders mentioned._

1. Create a Spotify Developer Account, and generate the Client Secret and Client ID then Set Redirect URI - http://localhost:3000
2. Clone the repo
   ```sh
   git clone https://github.com/Malay-dev/spotify-x-ani-oke.git
   ```
3. Install NPM packages in the server
   ```sh
   cd server
   npm install
   ```
4. Create a '.env' in server folder and enter your API according to the sample '.env' template
   ```js
   REDIRECT_URI=http://localhost:3000
   CLIENT_ID=ENTER YOUT CLIENT ID
   CLIENT_SECRET=ENTER YOUR CLIENT SECRET
   ```
5. Start the Nodemon server in Server folder
   ```sh
   npm run start:dev
   ```
6. Install required libraries in flask-server
    ```sh
   cd flask-server
   python3 -m venv /path/to/new/virtual/environment
   pip install -r requirements.txt
   ```
7. Start the flask-server
   ```sh
   py app.py
   ```
8. Install NPM packages in client - frontend
   ```sh
   cd client
   npm install
   ```
9. Start the frontend
   ```sh
   npm run start
   ```
**NOTE:** _Song streaming feature will only work if you have premium spotify account._
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Add Readme
- [ ] Add footer
- [ ] Make the site responsive
- [ ] Add playlist feature
- [ ] Improve lyrics generation
- [ ] Improve Song Streaming Service

See the [open issues](https://github.com/Malay-dev/spotify-x-ani-oke/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->


<!-- LICENSE -->

## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Utsav Yadav - [@Yadavutsav3](https://twitter.com/Yadavutsav3)
Malay Kumar - [@void_MalayK](https://twitter.com/void_MalayK)
<p align="center">NOTE: To enjoy the demo link please contact above for required permissions.</p>
Project Link: [https://github.com/Malay-dev/spotify-x-ani-oke](https://github.com/Malay-dev/spotify-x-ani-oke)

<p align="right"><a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

- [Choose an Open Source License](https://choosealicense.com)
- [Img Shields](https://shields.io)
- [Render](https://render.com/)
- [Netlify](https://www.netlify.com/)
- [Spotify Web API](https://developer.spotify.com/)
- [Genius](https://genius.com/)
- [Fonts](https://fonts.google.com/about)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/utsav82/Bollywood-Back.svg?style=for-the-badge
[contributors-url]: https://github.com/utsav82/Bollywood-Back/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/utsav82/Bollywood-Back.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/utsav82/Bollywood-Back
[forks-shield]: https://img.shields.io/github/forks/utsav82/Bollywood-Back.svg?style=for-the-badge
[forks-url]: https://github.com/utsav82/Bollywood-Back/network/members
[license-shield]: https://img.shields.io/github/license/utsav82/Bollywood-Back.svg?style=for-the-badge
[license-url]: https://github.com/utsav82/Bollywood-Back/blob/master/LICENSE.txt
[react.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[react-url]: https://reactjs.org/
[node.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[react-url]: https://reactjs.org/
