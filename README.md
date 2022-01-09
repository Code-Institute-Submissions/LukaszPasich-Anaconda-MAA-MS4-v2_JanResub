# _Anaconda_ Martial Arts Academy

_Anaconda_ Martial Arts Academy is a local school of martial arts located in Dublin 15, that teaches a combination of disciplines necessary to become a Mixed Martial Artist.
The goal of the academy however is not to train competition ready athletes but to help their members to get active and fit and receive all benefits of martial arts training, including building self-esteem and confidence.
The classes tought in the academy are: Brazilian Jiu-Jitsu, Kickboxing and Boxing and also Mixed Martial Arts for the more advanced students.
Members can practice one chosen discipline or get involved with the whole MMA suite of disciplines.
The school accepts new members across all ages (in BJJ classes, kids can start as early as the age of 4) and various skill levels from Beginners to Advanced.
As 'Anaconda' academy is growing in members, they would like to automatise the process of signing up for memberships to and they would like to add a small e-commerce on their website to sell their branded merchandise.

<img src="static/images/ms4-readme-overview.jpg" alt="Anaconda MAA website overview">

# Link to live project - [CLICK HERE](https://anacondamaa2.herokuapp.com/)

<br>

#### Contents
1. [UX](#ux)
	- [Strategy](#strategy)
		- [User Goals](#user-goals)
		- [Stakeholder Goals](#stakeholder-goals)
		- [User Stories](#user-stories)
	- [Scope](#scope)
		- [Features included](#features-included)
		- [Features to implement in the future](#features-to-implement-in-the-future)
	- [Structure](#structure)
		- [Sitemap](#sitemap)
		- [Database Schema](#database-schema)
	- [Skeleton](#skeleton)
		- [Wireframes (low fidelity wireframes)](#wireframes-(low-fidelity))
		- [Prototype (high fidelity wireframes)](#prototype-(high-fidelity))
	- [Surface](#surface)
2. [Technologies](#technologies)
	- [Tools](#tools)
	- [Libraries](#libraries)
	- [Languages](#languages)
3. [Testing](#testing)
	- [Automated Testing](#automated-testing)
	- [UX Testing](#ux-testing)
	- [Manual Testing](#manual-testing)
	- [Bugs](#bugs)
4. [Deployment](#deployment)
	- [Forking GitHub Repository](#forking-github-repository)
	- [Making a Local Clone](#making-a-local-clone)
	- [Heroku Deployment](#heroku-deployment)
5. [Credits](#credits)
	- [Content](#content)
	- [Media](#media)
	- [Code](#code)
    - [Resources](#resources)
	- [Acknowledgements](#acknowledgements)
6. [Contact](#contact)

---
---
<br>

## UX

### Strategy

<br>

#### User Goals
- Find out information about the academy, it's procedures, different classes provided and instructors teaching the classes.
- Find out information about different age groups and skill levels that classes are divided into and timetable for classes.
- Find out membership prices.
- Sign up for membership. 
- Find information on how to get in touch with the school and start the training.
- Buy training equipment on the website

#### Stakeholder Goals
- Attract new members to join the academy and retain existing members.
- Provide comprehensive information about the academy and classes provided.
- Increase online presence as a tool of advertising and promotion.
- Process membership sign ups on the website.
- Sell Anaconda branded merchandise.
- Process online payments easily and without a hassle.
- Be able to easily update information on the website.

#### User Stories
- Link to User Stories - [CLICK HERE](https://docs.google.com/spreadsheets/d/1CIi1zBifp5aBSsgi96vp9oLkrAsZ-a9Hyv3Tw9sNon4/edit?usp=sharing)

<br>
<br>

### Scope

<br>

####  Features included:
1. Navigation bar

	The navigation bar features logo on the left-hand side and navigation links on the right-hand side.

	Navigation bar elements:
	- Logo - always links back to the _Home_ page
	- About - links to _About_ page
	- Classes - links to _Classes_ page
	- Shop - links to the e-commerce _Shop_ page
	- Contact - links to _Contact_ page
	- Account - has hidden on click dropdown menu with links:
		- Sign up - visible for non-logged in user
		- Login - visible for non-logged in user
		- My Profile - visible for logged in user
		- Logout - visible for logged in user
		- Products - visible for admin user

	- Join now - links to page with all membership options
	- Bag total - displays current shopping bag value
	
	Navigation links have _underline from center_ hover effect taken from Hover.css website.
	There is no effect for active navigation link, the headline of the header banner is sufficient to indicate the page that the user is in.

	The Navigation bar's position is fixed to allow for quick navigation between pages.
	
	On mobile devices the logo collapses into hamburger menu.
	
<br>

2. Footer

	The footer contains following information:
	- Logo	
	- Contact details - academy's location, phone number and email address
	- Opening times
	- Navigation links - stacked in a column, same navigation links as in navigation bar
	- Social media links - links to Twitter, Pinterest, Facebook, Instagram and Youtube will have to be linked later to the academy's' actual pages in the respective channels.

<br>

3. Home page

	The _Home_ page features a main banner with headline and call to action button to join the Academy. Below the banner is the quick overview of disciplines that the Academy offers classes in: Brazilian Jiu-Jitsu, Kickboxing and Boxing, and an invitation to read more about them on the _About_ page.

<br>

4. About page

	The _About_ page, features the main banner on top and below contains couple of paragraphs about Anaconda Martial Arts Academy followed by a small section devoted to each of the martial arts disciplines taught in the school and ending with information about the instructors.

	Each of the martial arts sections has __'Join Our Academy'__ call to action button and an additional link to _Coaches_ section, each of the instructors sections has in turn link back to information about the discipline they are teaching.

<br>

5. Classes page

	The _Classes_ page, apart from the main banner, features two sections (Kids & Teens Classes and Adults Classes) explaining division of classes into different age and skill level groups. There is also __'Join Our Academy'__ call to action button and an additional link to the Class Timetable with each section. The Class Timetable is the last section on this page.

<br>

6. Contact page

	The _Contact_ page contains Contact Form to send email to the academy.

<br>

7. Contact Form

	Contact form contains below fields (* fields are required):
	- Name *
	- Email address *
	- Phone number
	- The message *

<br>

8. Membership page

	The _Membership_ page is accessed via __Join Now__ button in the navbar or __Join Our Academy__ call to action button anywhere else in the website. The page has 4 boxes representing different membership options, one of them is a distinctive looking offer of a free introductory class. Each box has a __Get Started__ button that links to _Contact_ page at the moment, expecting visitors to get in touch with the academy through contact channels given on that page in order to sign up and pay for membership.

<br>

9. Account - Sign up page

	The _Sign up_ page is accessible from the navbar _Account_ dropdown menu, if no user is currently signed in. The page contains the sign up form with the following fields (* fields are required):
	- Email address *
	- Email address confirmation *
	- Username *
	- Password *
	- Password confirmation *

	On submitting the form (Sign up) the user is taken to _Verify your email_ page, with the toast 'Alert!' being displayed informing user that the email has been sent to the submited email address with the link to verify the user's email address.
	
<br>

10. Account - Login page

	The _Login_ page is accessible from the navbar _Account_ dropdown menu, if no user is currently signed in. The page contains the sign up form with the following fields (* fields are required):

	- Username *
	- Password *
	- Remember me (tickbox)

	On submitting the form (Sign in), the user is taken to the _Home_ page and a 'Success!' toast is displayed to confirm the successful login. Furthermore, a user icon is displayed above the _Account_ link in the navbar, indicating that a user is currently signed in.

<br>

11. Account - Logout page

	The _Logout_ page is accessible from the navbar _Account_ dropdown menu, if user is currently signed in. On successful sign out the 'Success!' toast is displayed and the user is taken to the _Home_ page.

<br>

12. Account - Profile page

	The _My Profile_ page is accessible from the navbar _Account_ dropdown menu, if user is currently signed in. The page contains the form with user's delivery details and the history of purchases made on the website.

	Delivery Information form has fields:
	- Phone number
	- Street Address 1
	- Street Address 2
	- Town or City
	- County, State or Locality
	- Postal Code
	- Country (dropdown)

	On submitting this form, the 'Success!' toast pops up and the page reloads with the information updated.

	Order history contains the following information:
	- Order number - links to the order confirmation originally generated, with more details of the order (a toast 'Alert!' informs user that this is the past order)
	- Order date
	- Items purchased
	- Order total

<br>

12. Account - Add Products page

	The _Add Product_ page allows admin user to add new products to the database and is accessible from the navbar _Account_ dropdown menu, only by admin user who is currently signed in. The page contains the form with the following product details to fill in (* fields are required):
	- Category (Choose from dropdown)
	- SKU
	- Name *
	- Description
	- Price *
	- Rating
	- Image URL (opens select from your computer web browser box)

	On submitting this form, the 'Success!' toast pops - the new product has been added to the database and the admin user is redirected to the _Product View_ page with the preview of the newly added product.

<br>

13. Account - Add Membership page

	The _Add Membership_ page allows admin user to add new memberships to the database and is accessible from the navbar _Account_ dropdown menu, only by admin user who is currently signed in. The page contains the form with the following product details to fill in (* fields are required):
	- Discipline (Choose from dropdown)
	- Membership no.
	- Name *
	- Small name
	- All classes checkbox
	- Price *
	- Pay interval

	On submitting this form, the 'Success!' toast pops - the new membership has been added to the database and the admin user is redirected to the _Membership_ page.

<br>

14. Account - Add Class page

	The _Add Class_ page allows admin user to add new class to the database and is accessible from the navbar _Account_ dropdown menu, only by admin user who is currently signed in. The page contains the form with the following product details to fill in (* fields are required):
	- Class Name *
	- Class Time *
	- Class Type
	- Class Level

	On submitting this form, the 'Success!' toast pops - the new vlass has been added to the database and the admin user is redirected to the _Classes_ page.

<br>

15. Shop page

	Displays all products in the website's database on a responsive grid. Each product is represented by a box containing below details:
	
	- Image
	- Category
	- Name
	- Price
	- Rating
	- Edit button (available only to admin user)
	- Delete button (available only to admin user)

	Clicking on one of the products takes user to the individual _Product View_ page.

	There are tabs with different categories above the products allowing user to select all products or only products in the chosen category.

	---
	__NOTE:__

	More categories and more products should be added to complete the full offer.
	___

<br>

16. Product search bar

	Product search bar appears on the _Shop_ page. It allows for searching for products based on the keyword(s) entered into the search bar (keywords searched in the category, name and description of the products).
	An 'Error!' toast pops up if search is performed with no search criteria entered or the search criteria was not found.

<br>

17. Sort by...

	_Sort by_ box appears on the _Shop_ page. It allows for sorting of the current selection of the products on the page (can be all products or products filtered by keyword or category).
	
	Current sorting criteria are:
	- Price (low to high, high to low)
	- Rating (low to high, high to low)
	- Name (A-Z, Z-A)
	- Category (A-Z, Z-A)

<br>

18. Product View page

	Individual _Product View_ page is accessed from the _Shop_ page after clicking on any product. This page contains similar details to the _Shop_ page with some expansions:
	- Image (bigger than on the _Shop_ page)
	- Category
	- Name
	- Price
	- Rating
	- Description
	- Quantity Selector
	- Edit button (available only to admin user)
	- Delete button (available only to admin user)

	_Add to Bag_ button ads the currently viewed product and it's selected quantity to the shopping bag. The 'Success!' toast with full current details of the shopping bag is displayed.

<br>

19. Edit Product page

	The _Edit Product_ page is available only to admin user and allows admin user to edit existing products and update these edits in database. Editing the product is available from the _Shop_ page or _Product View_ page. The page contains the same form as the _Add Product_ page, with all the fields populated with current product information.

	When accesing the _Edit Product_ page an 'Alert!' toast pops up to remind the user that this action will change product information.

	On submitting this form (Update product), the 'Success!' toast pops - the product has been updated in the database and the admin user is redirected to the _Product View_ page with the preview of the updated product.

<br>

20. _Delete Product_ functionality

	_Delete Product_ functionality is available only to admin user and allows admin user to delete existing product from the database.
	Deleting the product is available from the _Shop_ page or _Product View_ page.
	
	---
	__WARNING!__
	
	Currently there is no confirmation of deleting the product required, so once the _Delete_ button is clicked on, the product is instantly erased from database. This will need to be corrected at the soonest opportunity.

	---

	On successful _Delete_ a 'Success!' toast pops up.

<br>

21. Edit Membership page

	The _Edit Membership_ page is available only to admin user and allows admin user to edit existing memberships and update these edits in database. Editing the membership is available from the _Membership_ page. The page contains the same form as the _Add Membership_ page, with all the fields populated with current membesrhip information.

	When accesing the _Edit Membership_ page an 'Alert!' toast pops up to remind the user that this action will change membership information.

	On submitting this form (Update Membership), the 'Success!' toast pops - the membership has been updated in the database and the admin user is redirected to the _Membership_ page.

<br>

22. _Delete Membership_ functionality

	_Delete Membership_ functionality is available only to admin user and allows admin user to delete existing membership from the database.
	Deleting the membership is available from the _Membership' page.
	
	---
	__WARNING!__
	
	Currently there is no confirmation of deleting the membership required, so once the _Delete_ button is clicked on, the membership is instantly erased from database. This will need to be corrected at the soonest opportunity.

	---

	On successful _Delete_ a 'Success!' toast pops up.

<br>

21. Edit Class page

	The _Edit Class_ page is available only to admin user and allows admin user to edit existing class and update these edits in database. Editing the class is available from the _Classes_ page. The page contains the same form as the _Add Class_ page, with all the fields populated with current class information.

	When accesing the _Edit Class_ page an 'Alert!' toast pops up to remind the user that this action will change class information.

	On submitting this form (Update Class), the 'Success!' toast pops - the class has been updated in the database and the admin user is redirected to the _Classes_ page.

<br>

23. _Delete Class_ functionality

	_Delete Class_ functionality is available only to admin user and allows admin user to delete existing class from the database.
	Deleting the class is available from the _Classes' page.
	
	---
	__WARNING!__
	
	Currently there is no confirmation of deleting the class required, so once the _Delete_ button is clicked on, the class is instantly erased from database. This will need to be corrected at the soonest opportunity.

	---

	On successful _Delete_ a 'Success!' toast pops up.

<br>

24. _Shopping Bag_ page and functionality

	_Shopping Bag_ page contains the list of products that have been added to the bag in the single continued session (not ended with payment). The products are subtotalled individually and the grand total is calculated at the bottom of the page. 

	_Shopping Bag_ page can be accessed via the link in the navbar - the current euro value of the bag link - and it can be also accessed by clicking on _Go to secure checkout_ button on the 'SUCCESS!' toast, which always appears on the occasion of adding product to the _Shopping Bag_ or updating the quantity. 

	---
	__NOTE!__

	There is 10% Delivery charge calculated on orders under 50EUR, this hasn't been communicated very well, I decided to communicate more strongly 10% Discount for Academy members, but connecting memberships to users didn't happen at the end. It should be a featured considered at the next round of website updates.  

	---

<br>

25. _Checkout_ page and functionality

	_Checkout_ page is the last step before confirming the payment in the Anaconda academy shop. The page contains the summary overview of the shopping bag with the grand total and a form with personal, delivery and payment details.

	The form contains below fields (* fields are required):
	- Full name *
	- Email *
	- Phone number *
	- Street address 1 *
	- Street address 2 *
	- Town or City *
	- County, State or Locality
	- Postal code
	- Country * (select from dropdown menu)
	- Credit Card number *
	- Save delivery info to my profile (checkbox)

	On submitting the form (Complete Order), the payment is being processed through Stripe, the 'Success!' toast pops up and the user is taken to the _Thank You_ page with full details order confirmation.

<br>

26. Order confirmation _Thank You_ page

	This page contains full order summary of the order just processed.
	- Order info:
		- Order number
		- Order date
	- Order details
	- Delivering to info:
		- Full name
		- Phone number
		- Street address 1
		- Street address 2
		- Town or City
		- County, State or Locality
		- Postal code
		- Country
	- Billing info:
		- Order total
		- Delivery
		- Grand total

<br>

27. _Stripe_ payment functionality

	_Stripe_ is setup for processing the payment on the website. Webhooks are connected to ensure that the order is accounted for at the point of clicking on _Complete Order_ button on _Checkout_ page and is going to be processed even if the connection with website is broken suddenly.

<br>

28. Toasts

	Toasts are connected to _messages_ in views and they pass on the messages of success, info, warnings and errors.
	
	Check the full list of toasts in the [Manual testing section](README_testing.md#manual-testing).

<br>



<br>
<br>

#### Features to implement in the future
- Online Membership Signup & Payment feature.
- Connect Memberships to Users.
- Connect 10% discount in the shop to users with academy membership.
- Add more products and categories to the shop.
- Connect Order Confirmation email.
- Add confirmation or cancel delete (defensive design) to _Delete Product_ button.
- Connect the contact form to some emailing service (EmailJS etc...)
- Add Google maps with a marker on contact page.
- Add members testimonials page.
- Online Free Trial Class booking - a feature allowing users to pick the class date and time in the online calendar and have the class automatically booked, with confirmation email automatically sent to user.
- 400 Errors handling

<br>

[Back to top](#contents)


---
<br>

### Structure

#### Sitemap

- [Sitemap CLICK HERE](https://indd.adobe.com/view/07136e64-5fa7-4427-a982-9158331285cf)


#### Database Schema

- [Database structure CLICK HERE](https://indd.adobe.com/view/2c4b9a28-36dc-4bf4-b1b9-85fc3c0fbf71)

<br>

[Back to top](#contents)

---
<br>

### Skeleton

<br>

#### Wireframes (low fidelity)
Wireframes created for 4 screen/ device sizes: desktop, tablet-landscape, tablet-portrait and phone.
- [Wireframes for all pages AVAILABLE HERE](https://indd.adobe.com/view/d9db8027-1cdd-4de5-86b2-efcc73aef2eb)

	---
	__NOTE__

	Ultimately, I didn't have time/skills to implement the membership purchase functionality that is presented in the wireframes. 

	---

<br>

#### Prototype (high fidelity)
Prototype for desktop only created.
- [Prototype - desktop version of the website AVAILABLE HERE](https://xd.adobe.com/view/3225eceb-21c6-4e20-9318-36ec8daf1735-6776/)

	---
	__NOTE__

	Ultimately, I didn't have time and skills to implement the membership purchase functionality that is presented in the wireframes. 

	---

<br>

[Back to top](#contents)

---
<br>

### Surface

<br>

-	The Name - Why Anaconda?

	The martial art of Brazilian Jiu-Jitsu - one of the staples of the academy - is in essence the skill of grappling, holding and taking down the opponent to then force them into submission via joint lock or chokehold.
	This very much resembles the actions of a constrictor snake and one of the submissions in BJJ is even called an _Anaconda Choke_. As grappling has become one of the key weapons in Mixed Martial Artist's arsenal, Brazilian Jiu-Jitsu became near synonymous with MMA and that's why I thought it was a good name for this Martial Arts Academy.

<br>

- Logo

	With the logo I was trying to emulate the classic idea of the Martial Arts Club badge which seems to have always evolved around some related image or an Asian symbol enclosed in a circle (or lately popular octagon), with the club name and all the necessary text wrapped around that circle.

	Reference images:

	<img src="assets/images_readme/ms1-readme-ux-logoref.jpg" alt="Anaconda MAA website logo reference">

	Anaconda MAA final logo:

	<img src="assets/images_readme/ms1-readme-ux-logo.jpg" alt="Anaconda MAA logo">

<br>

- Colours

	Principally white, red and black colour palette.
	With black and white representing the concept of dualism, describing how seemingly opposite or contrary forces may actually be complementary, interconnected, and interdependent in the natural world, and the red colour being universally seen as a sign of both life and aggression - the 3 colours have always been used in martial arts themes.

	In my research of the competitor's websites, I discovered that these were the prevalent colours on all of those websites and the similar colour theme would also be possibly expected by the website user/ visitor. Meeting this expectation adds credibility to the brand, company and the website. 


	<img src="assets/images_readme/ms1-readme-ux-colours.jpg" alt="Anaconda MAA website colours">

<br>

- Typography

	Raleway: Semi-Bold, Bold and Extra Bold - for headlines and sub-headlines.

	_Raleway_ because it is a nice and clean display typeface and also geometric sans-serif fonts (as _Raleway_ being geometric inspired) tend to have more neutral feel about them.
	As Anaconda MAA aims at attracting a diverse audience, I didn't want to use font with too strong personality, because I wanted to convey an 'everybody is welcome' academy's approach to attracting it's new members.

	Roboto: Regular - for body text.

	_Roboto_ has forms that are largely geometric, but at the same time, the font features friendly and open curves - it is an excellent body text font and a good compliment to Raleway.
	Allowing letters to be settled into their natural width and with slab-serifs clearly defining the text baseline _Roboto_ creates an easy and more natural reading rhythm.


	Both fonts and also their combination has been tried and is well established and widely popular on the web.

<br>

- Images - Why black and white photography?

	Black and white photography removes any distraction of color and helps the viewer focus on other aspects of the photo, such as the subject, the textures, shapes and patterns, and the composition.
	It can convey remarkable purity of emotion and action and therefore works perfect for martial arts.


[Back to top](#contents)

---
---

<br>

## Technologies
### Tools
- [GitHub](https://github.com) was an IDE used for the project.
- [GitPod](https://gitpod.io/workspaces/) was used for version control.
- [Heroku](https://heroku.com) was used for website deployment.
- [Stripe](https://stripe.com/ie) was used for processing online payments.
- [Amazon Web Services](https://signin.aws.amazon.com/) S3 Bucket service was used for collecting and storing websites static files, including images.
- [EmailJS](https://www.emailjs.com/) was used for sending emails to Academy via contact form on Contact page.
- [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) was used to generate django key to enable automatic deploys to Heroku
- [Adobe Indesign](https://balsamiq.com) was used to create low fidelity wireframes.
- [Adobe XD](https://www.adobe.com/ie/products/xd.html) was used to build the high fidelity prototypes.
- [Adobe Illustrator](https://www.adobe.com/ie/products/illustrator.html) was used to create logo.
- [Adobe Photoshop](https://www.adobe.com/ie/products/photoshop.html) was used to edit, crop and save images.

### Libraries and frameworks
- [Django](https://www.djangoproject.com/) - a high-level Python framework was used to develop the website. It provided framework for easy implementation and use of data models, views and URL's, templates, forms, authentication and provided admin function.
- [jQuery](https://jquery.com/) - a JavaScript library, was used for a number of front-end interaction solutions.
- [Bootstrap](https://getbootstrap.com/) library was used to style the website and make it responsive.
- [Google Fonts](https://fonts.google.com) was used to link the "Raleway" and "Roboto" fonts.
- [Font Awesome](https://fontawesome.com) was used for icons.

### Languages
- HTML5
- CSS3
- JavaScript
- Python

<br>

[Back to top](#contents)

---
---

<br>

## Testing 

<br>

### Automated Testing

- Automated testing full section [CLICK HERE](README_testing.md#automated-testing)

### UX Testing

- UX testing full section [CLICK HERE](README_testing.md#ux-testing)

### Manual Testing

- Manual testing full section[CLICk HERE](README_testing.md#manual-testing)

### Bugs

- Bugs fixed full section [CLICk HERE](README_testing.md#bugs-fixed)
- Bugs not fixed full section [CLICk HERE](README_testing.md#bugs-not-fixed)

<br>

[Back to top](#contents)

---
---

<br>

## Deployment

<br>

### Forking GitHub Repository
(A copy of the original repository on your GitHub account)

1. Log in to GitHub and locate this [GitHub Repository](https://github.com/LukaszPasich/Anaconda-MAA-MS4-v2)
2. Locate the "Fork" button in the top right-hand side of the page and click on it.
3. You now have a copy of the original repository in your GitHub account.

<br>

### Making a Local Clone
1. Log in to GitHub and locate this [GitHub Repository](https://github.com/LukaszPasich/Anaconda-MAA-MS4-v2)
2. Under the repository name, click on "Code" button.
3. In the Clone/ Download unfolded tab click on HTTPS (to clone with HTTPS).
4. Click on the 'clipboard' icon to copy the URL of your project.
5. Open your IDE, open terminal.
6. Change the current working directory to the location where you want the cloned directory.
7. In the terminal type <code>git clone</code>, and then paste the URL you copied earlier.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
8. Press _ENTER_ to create your local clone.

	__Note:__ It is important that you create an env.py file to save your __environment variables__, the web app will not function without these variables:
	
<br>

### Heroku Deployment

1. Log in to [Heroku](https://www.heroku.com).
2. From the Dashboard, click on the _New_ button in the top-right corner and then select "Create new app".
3. Insert your app name.
4. Select the most appropriate region for your location.
5. Click the "Create app" button.
6. In the _Resources_ tab search for Add-on "Heroku Postgres", click on it and 'Provision' it using the Free plan (or another plan of your choice).
7. In Gitpod CLI install 2 more dependencies:

	```
	pip3 install dj.database.url
	pip3 install psycopg2-binary 
	```
8. Freeze the requirements:

	```
	pip3 freeze > requirements.txt
	```	
9. In the app's settings.py file:

	```
	import dj_database_url
	```	
	... then comment out the default DATABASES settings in the settings.py file and replace it with:
	```
	DATABASES = {
		'default': dj_database_url.parse(database_URL_from_Heroku) 
	}
	```	
	... you can get database_URL_from_Heroku in your app's _Settings_ tab (Reveal Cofig Vars - value for the DATABASE_URL key) or by typing <code>heroku config</code> in Heroku CLI.
10. With the new postgres database connected, migrations need to be run again, in CLI type in:

	```
	python3 manage.py migrate
	```	

11. Import all the data, type in CLI:

	```
	python3 manage.py loaddata db
	```	
	... where db is the name of the json file with fixtures. If there are multiple fixture files and some of them depend on other files, they should be loaded AFTER the files they depend on have been loaded.

12. Create superuser:

	```
	python3 manage.py createsuperuser
	```	
	... create username, enter email address and create password.

13. In settings.py delete current Heroku DATABASES config, uncomment previously commented out DATABASES config (you can safely push your code now and the postgres database url is not going to end up in version control) and put it in an _if statement_:
	```
	if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
	else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
	```	

14. Instal gunicorn (acts as a webserver), in CLI:
	```
	pip3 install gunicorn
	```	
	...then freeze requirements:
	```
	pip3 freeze > requirements.txt
	```

15. Create Procfile at project level, inside the file type in on the first line:
	```
	web: gunicorn your_app_name.wsgi:application
	```
	... your_app_name is the name of the project - the name of the folder where settings.py file is.

16. Login to Heroku - in CLI: heroku login (or heroku login -i and give email and password of the superuser).


17. Temporarily disable collect static by typing in CLI:
	```
	heroku config: set DISABLE_COLLECTSTATIC=1 --app name_of_the_app
	```
	... name_of_the_app in heroku.


18. Add the hostname of heroku app to allowed hosts in settings.py:
	```
	ALLOWED_HOSTS = ['app_name_in_heroku.herokuapp.com', 'localhost']
	```

19. Commit changes and push to GitHub.

20. Push to Heroku, in CLI type in:
	```
	git push heroku main
	```
	... if the app was created on the website (fatal: 'heroku' does not appear to be a git repository), heroku git remote may need to be initialized:
	```
	heroku git:remote -a app_name_in_heroku 
	```
	... and then type again in CLI: git push heroku main

21. After few seconds at the end of the load up, the heroku link to the app will be ready.

22. To set for automatic deploy when pushed, go to Heroku _Deploy_ tab:
- click _Connect to Github_
- enter the name of the app in search bar (name of the GitHub repositoiry) - click "Search"
- click "Connect" to the repository
- below, click "Enable Automatic Deploys" - whenever code is pushed to GitHub now, it will automatically be pushed to Heroku as well.

23. Go to [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) and generate a new key - copy the key.
Go to Heroku _Settings_ tab, _Reveal Config Vars_ and add a new _Config Var_ with key: SECRET_KEY, and value: paste the key from Django Secret Key Generator.

24. In settings.py replace SECRET_KEY with the call to get it from environment:
	```
	SECRET_KEY = os.environ.get('SECRET_KEY', '')
	```

25. In settings.py set DEBUG to be True only if there's a variable DEVELOPMENT in the environment. 
	```
	DEBUG = 'DEVELOPMENT' in os.environ
	```

---
__NOTE!__

Remember to set environment variables in Heroku:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DATABASE_URL
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET
- USE_AWS

---

<br>

[Back to top](#contents)

---
---

<br>

## Credits
### Content
The textual content was influenced by or taken from the websites:
- [JS Brazilian Jiu-Jitsu](https://www.jsbjj.ie "JS Brazilian Jiu-Jitsu")
- [Evolve Daily blog](https://evolve-mma.com/blog/4-reasons-boxing-will-make-you-obsessed-to-working-out/ "Evolve Daily blog")
- [Club Solutions Magazine](https://clubsolutionsmagazine.com/2018/11/7-reasons-kickboxing-classes-schedule/ "Club Solutions Magazine")
- [Satori BJJ Dublin](https://www.satoribjj.com "Satori BJJ Dublin")
- [Royal Grappling Academy](https://rga.ie "Royal Grappling Academy")
- [www.venum.com](https://www.venum.com "www.venum.com")

### Media
- Home page main banner - by Nathan Dumlao, downloaded from [www.unsplash.com](https://unsplash.com/photos/DT3bb-KDAus "www.unsplash.com")
- Home page BJJ white image - by Nathan Dumlao, downloaded from [www.unsplash.com](https://unsplash.com/photos/NdCixEBtTf0 "www.unsplash.com")
- Home page kickboxing white image - bu Justin Ng, downloaded from [www.unsplash.com](https://unsplash.com/photos/45tcVh0M3kw "www.unsplash.com")
- Home page kickboxing icon - by Miguel Angel, downloaded from [www.vecteezy.com](https://www.vecteezy.com/vector-art/93089-woman-and-man-fighting-silhouettes "www.vecteezy.com")
- Home page boxing white image - by Anastase Maragos, downloaded from [www.unsplash.com](https://unsplash.com/photos/ZUBNPRZsQvk "www.unsplash.com")
- Home page boxing icon - by yoosillyone, downloaded from [www.vecteezy.com](https://www.vecteezy.com/vector-art/166423-muay-thai-silhouette "www.vecteezy.com")
- About page main banner - by Nathan Dumlao, downloaded from [www.unsplash.com](https://unsplash.com/photos/NdCixEBtTf0 "www.unsplash.com")
- About page boxing bag image - by Milo Bunnik, downloaded from [www.unsplash.com](https://unsplash.com/photos/lp9GQiQNHqc "www.unsplash.com")
- About page BJJ image - by Nathan Dumlao, downloaded from [www.unsplash.com](https://unsplash.com/photos/YmNIHXdTfPg "www.unsplash.com")
- About page kickboxing image - by cottonbro, downloaded from [www.pexels.com](https://www.pexels.com/photo/woman-in-black-shirt-and-black-shorts-carrying-black-leather-shoulder-bag-4754146/ "www.pexels.com")
- About page boxing image - by Logan Weaver, downloaded from [www.unsplash.com](https://unsplash.com/photos/9D_rUDe7xvA "www.unsplash.com")
- About page BJJ coach image - by Jahir Martinez, downloaded from [www.unsplash.com](https://unsplash.com/photos/cVLOqm8sSXc "www.unsplash.com")
- About page kickboxing coach image - by Michael Uebler, downloaded from [www.unsplash.com](https://unsplash.com/photos/EwnkEPhVym4 "www.unsplash.com")
- About page boxing coach image - by John Fornander, downloaded from [www.unsplash.com](https://unsplash.com/photos/r79IYSMpu_M "www.unsplash.com")
- Classes page main banner - by Nathan Dumlao, downloaded from [www.unsplash.com](https://unsplash.com/photos/AsCCBr7J-XM "www.unsplash.com")
- Classes page kids & teens classes image - by Microgen, downloaded from [www.stock.adobe.com](https://stock.adobe.com/ie/images/martial-arts-training-class-for-children/176854174 "Adobe Stock")
- Classes page adults classes image - by Nathan Dumlao, downloaded from [www.unsplash.com](https://unsplash.com/photos/YQg2wxJAINQ "www.unsplash.com")
- Shop page main banner - by Gantas Vaičiulėnas, downloaded from [www.unsplash.com](https://unsplash.com/photos/rvAcZMqFIkY "www.unsplash.com")
- Contact page main banner - by Thao Le Hoang, downloaded from [www.unsplash.com](https://unsplash.com/photos/XeBk0qF77_4 "www.unsplash.com")

### Code
- The whole website relied very heavily on the 'Boutique Ado' tutorial from Code Institute !!  <br>
It would be impossible to give credit for every piece of code.

- Navigation links hover effect (underline from center) styling - code found on Hover.css website [https://ianlunn.github.io/Hover/#effects](https://ianlunn.github.io/Hover/#effects)
- _Home_ page - overlay hover effect on 3 images (BJJ, Kickboxing and Boxing) styling - code found on [www.w3schools.com](https://www.w3schools.com/howto/howto_css_image_overlay_title.asp)
- _Coaches_ page - zoom effect on hover over coaches images styling - code found on [www.w3bits.com](https://w3bits.com/css-image-hover-zoom/)

### Resources
- [www.w3schools.com](https://www.w3schools.com)
- [www.stackoverflow.com](https://stackoverflow.com)
- [www.developer.mozilla.org](https://developer.mozilla.org/en-US/)
- [Django documentation](https://www.djangoproject.com)
- [Code Institute course content](https://codeinstitute.net/)

### Acknowledgements
- Thank you to my mentor __Nishant Kumar__ for his guidance, support and continuous helpful feedback throughout this project.
- Tutor Support at Code Institute and the Slack Community for a solution to any question at any time.

<br>

[Back to top](#contents)

---
---

<br>

## Contact
For any queries related to this project, you can contact me at:

lukas (dot) zed81 (at) gmail (dot) com.

<br>

[Back to top](#contents)

---
---
---

<br>

### THANK YOU FOR TAKING TIME TO VIEW THIS PROJECT!
