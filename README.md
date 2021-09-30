# Gear List ⛺️ 🗻

**Author**: Skyler Johnson

**Repo**: [Link to GiHub Repository](https://github.com/SkylerJohnson102020/gear-list)

**Version**: 2.5.1

## Overview

Gear List is written in Django/Python using TailwindCSS, ElephantSQL, and Docker. 

Gear List is an informational blog for users to store information, ratings, checklists, and other helpful information about backpacking gear from personal experience with the item. It's always great talking shop about gear when you're on a backpacking trip, but it's much more useful to know these tips and recommendations BEFORE going into the wilderness. Gear List is here to help with recommendations from users, ratings on gear items, and even a customizable checklist for the user to use while packing to ensure no item is left behind. (We've all been there.) This is a helpful tool to help you prepare for your next trip!

- Django Documentation - [Documentation](https://docs.djangoproject.com/en/3.2/)
- TailwindCSS Documentation - [Documentation](https://tailwindcss.com/docs)
- Django-Tailwind GitHub Repository - [GitHub](https://github.com/timonweb/django-tailwind)
- Django-Tailwind Documentation - [Documentation](https://django-tailwind.readthedocs.io/en/latest/index.html)
- Docker Documentation - [Documentation](https://docs.docker.com/)

## User Stories

1. I want the ability to keep notes or a blog about my hiking gear. [X]

2. I want the ability to login and save information on a database. []

3. I want the ability to see other user reviews and gear information.[]

4. I want the ability to rate my gear and be able to see ratings of other user gear.[]

5. I want the ability to keep a quick list that acts as a checklist to see on my phone when I am packing my gear for a trip. I want the ability to check off my items as I go. []

## Primary Feature Tasks

[X] Documentation  
[X] CRUD  
[X] Migrate Django naming  
[X] Django-Tailwind Integration  
[] Styling  
[] Login/Logout  
[] Database migration  
[] Docker

## Change Log

06-23-2021 - Initialized repo, Django setup, made first migration, templates, etc. Need to update tests and change snacks to gear. Version 1.0.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/c1c7696d4bf8fbeabdc9341a87571e0e123674ee)

06-23-2021 - Added README. Version 1.0.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/2724d3f7cd82cca465e01ff24a1cb79f39c97f5b)

09-09-2021 1:55pm - Changed name to Gear List. Started documentation and updated list items. Version 2.1.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/b076e3ea5294e0a520b71c19360125ae6ffcb8f1)

09-09-2021 2:02pm - Documentation updated. Version 2.1.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/a6c8b4e34a58dbd2b3adebfeba2d5b1a4cbce31e)

09-09-2021 2:29pm - Templates updated. Version 2.2.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/bc6726a5a29bfbf53483a02915f6baacf7232963)

09-09-2021 2:53pm - Navigation Updated. Added about view, url, and template. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/bc6e92a8355d205688212d96061eaaf4cf7af80b)

09-09-2021 6:02pm - Django-Tailwind integration successful. Need to begin styling. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/e85b6977d9c417a55feec493673af6ba9f85119f)

09-09-2021 6:09pm - Added resource links to overview in documentation. Added previous pull request link to documentation. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/e85b6977d9c417a55feec493673af6ba9f85119f)

09-09-2021 6:20pm - Added previous pull request link to documentation. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/afe06479b408a719ef208906b89e7afb6b6998e2)

09-09-2021 6:28pm - Edits to documentation. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/3cfedda716f26a2b0b9e1dcbf3d5047cdfb8c07c)

09-09-2021 6:42pm - Added .env to project folder, installed django-environ, added .gitignore. Need to work on securing the site. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/98eb7d28e6a3779f37deb1ae46f7fc52c3180b8a)

09-21-2021 7:29pm - Security info now secure including DEBUG, ALLOWED_HOSTS, and SECURITY_KEY. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/d9560f46dbf635aa9af2d457ee76644e96a3ac08)

09-21-2021 8:03pm - Moved templates into theme folder, need to get styling linked with browser_sync. Version 2.3.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/7237e629cc6ea6387c8fda67b76dd3f72729b743)

09-22-2021 4:03pm - Changed naming from snacks to gear. Encountering a server error. Version 2.4.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/957bf4710bfdeed768f5bec4e64b49eec3ede06c)

09-22-2021 4:03pm - Created a quarantine branch. Version 2.4.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/ea149d0afa722f095d6f241ff2f2b3699ca3ca80)

09-22-2021 5:45pm - Found error, Gear/Gears name change successful. Keeping QUARANTINE branch as a precaution. Merging into main. Will be working with some foundational styling. Will be migrating to ElephantSQL and deploying using Docker and Heroku. Version 2.5.0 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/d035726c88bcc1c3f8605af9f79cd78b2986930f)

09-22-2021 5:45pm - Started with simple styling of templates. Work in progress. Version 2.6.1 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/3013debe26d10639f41298eb115157f17122cf47)

09-23-2021 8:23pm - Updated documentation with user stories and primary feature tasks. Version 2.7.1 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/79c869200eb304cf7014ebb7a8f2efaff305a822)

09-23-2021 8:23pm - More infomation in Overview of documentation. Updated About page and did some very light styling. Light styling to the navigation bar as well. Version 2.8.1 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/dcb35d500732bb03cd29422360dce0b04681475e)

09-28-2021 2:35pm - Login now added and wired up. Need to add to nav bar and change views. Version 2.9.1 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/ac5c16e610b4c72dc71f92c66adfbdbbf07174d2)

09-29-2021 6:51pm - Added auth to base.html. Username is showing in nav bar. Need to add logout and sign up. Version 2.10.1 [Pull Request](https://github.com/SkylerJohnson102020/gear-list/commit/54bd7259ed5ec56a0104cbb183342cca21b971cb)

09-30-2021 6:51pm - Login and sign up pages added. Added accounts app. Redirects working properly. Nav bar fixed with auth. Need to add auth to list view. Version 2.11.1 [Pull Request]()

