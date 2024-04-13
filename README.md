## Personal Website

### A portfolio website with an about section, downloadable resume, technical skills summary, education & work history, links to recent projects, and contact info.

Technologies used: 
- HTML
- CSS (grid & flexbox)
- JavaScript
- Swiper
- Flask
- Flask-Mail
- WTForms for CSRF protection
- Flask-Compress to speed up load times

### Features:
  - Open-source code 
  - JavaScript to collapse and toggle elements
  - Swiper to add slides for projects
  - Light/dark mode remembered by each user's localStorage
  - Responsive web design
    
### Setup on your local machine:
  - First clone this git on your local machine `git clone https://github.com/AnishSarkar22/Personal-Portfolio.git`
  - Install virtual environment `python3 -m venv .venv`
  - Run the virtual environment `. .venv/bin/activate`
  - Install the dependencies `pip install -r requirements.txt` in the virtual environment
  - Run app `flask run`
  - The app should run at http://127.0.0.1:5000
