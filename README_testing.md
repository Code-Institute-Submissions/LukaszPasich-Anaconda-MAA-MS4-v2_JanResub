<br>

#### Contents
[Testing](#testing)
- [Automated Testing](#automated-testing)
- [UX Testing](#ux-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
    - [Bugs Fixed](#bugs-fixed)
    - [Bugs not Fixed](#bugs-not-fixed)

<br>

[Back to main README file](README.md#contents)

---
---

## Testing

<br>

### Automated Testing

- [W3C Markup Validator](https://validator.w3.org/) was used for HTML validation:
	- _Home page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Flanding) - Errors: 0
	- _About page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fget_recipes) - Errors: 0
	- _Classes page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Ffull_recipe) - Errors: 0
	- _Add Class page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fmy_recipes) - Errors: 0
	- _Edit Class page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fedit_recipe) - Errors: 0
	- _Shop page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fedit_recipe) - Errors: 0
	- _Product Details page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fedit_recipe) - Errors: 0
	- _Add Product page_ validator result [HERE](https://validator.w3.org/nu/?doc=http%3A%2F%2Fcookable.herokuapp.com%2Fedit_recipe) - Errors: 0
	- _Edit Product page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fsignup) - Errors: 0
	- _Shopping Bag page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fsignup) - Errors: 0
	- _Checkout page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Flogin) - Errors: 0
	- _Checkout Success page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontact) - Errors: 0
	- _Contact page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontacta) - Errors: 0
    - _Memberships page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontacta) - Errors: 0
    - _Add Membership page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontacta) - Errors: 0
    - _Edit Membership page_ validator result [HERE](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcookable.herokuapp.com%2Fcontacta) - Errors: 0
    - _Profile page_ validator (via direct input, as page password protected) result - Errors: 0
    - _Login page (allauth)_ validator (via direct input, as page password protected) result - Errors: 0
    - _Logout page (allauth)_ validator (via direct input, as page password protected) result - Errors: 0
    - Sign Up page (allauth)_ validator (via direct input, as page password protected) result - Errors: 0
    - _Confirm Your Email page (allauth)_ validator (via direct input, as page password protected) result - Errors: 0

&nbsp;

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used for CSS validation:
	- CSS validation result [HERE](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcookable.herokuapp.com%2Fstatic%2Fstyle%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - Errors: 0

&nbsp;

- [JSHint](https://jshint.com/) was used for JavaScript validation (New JavaScript features (ES6) and jQuery were selected in configuration):
    - script.js - JavaScript validation - Errors: 0
	- sendEmail.js - JavaScript validation - Errors: 0

&nbsp;

- [Web Accessibility](https://www.webaccessibility.com) was used to validate website's accessibility:
	- _Home page_ website accessibility score: 100%
	- _Recipes page_ website accessibility score: 100%
	- _Full recipe page_ website accessibility score: 100%
	- _My recipes page_ - password protected, could not be assessed
	- _Edit recipe page_ - password protected, could not be assessed
	- _Add recipe page_ - password protected, could not be assessed
	- _Categories page_ - password protected, could not be assessed
	- _Edit category page_ - password protected, could not be assessed
	- _Add category page_ - password protected, could not be assessed
	- _Sign up page_ website accessibility score: 100%
	- _Log in page_ website accessibility score: 100%
	- _Contact page_ website accessibility score: 98%
	- _Error 404 page_ website accessibility score: 100%

&nbsp;

    
- [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) was used to test responsiveness of the website:
	- _Home page_ - mobile friendly
	- _Recipes page_ - mobile friendly
	- _Full recipe page_ - mobile friendly
	- _My recipes page_ - password protected, could not be assessed
	- _Edit recipe page_ - password protected, could not be assessed
	- _Add recipe page_ - password protected, could not be assessed
	- _Categories page_ - password protected, could not be assessed
	- _Edit category page_ - password protected, could not be assessed
	- _Add category page_ - password protected, could not be assessed
	- _Sign up page_ - mobile friendly
	- _Log in page_ - mobile friendly
	- _Contact page_ - mobile friendly
	- _Error 404 page_ - mobile friendly

&nbsp;
	
- Python code was verified through GitPod's linter, showing only 1 error:
```	
"env" imported but unused
```

<br>

[Back to top](#contents)

---

<br>


### UX Testing

<br>

[Back to top](#contents)

---

<br>

### Manual Testing

#### Manual Testing Contents
- [1. Navbar Desktop](#navbar-desktop)
- [2. Navbar Mobile](#navbar-mobile)
- [3. Footer](#footer)
- [4. Home Page](#home-page)
- [5. About Page](#about-page)
- [6. Classes Page](#classes-page)
- [7. Shop Page](#shop-page)
- [8. Contact Page](#contact-page)
- [9. Membership Page](#membership-page)
- [10. Sign Up Page](#sign-up-page)
- [11. Sign In Page](#sign-in-page)
- [12. Add Product](#add-product-page)
- [13. Add Membership](#add-membership-page)
- [14. Add Class](#add-class-page)
- [15. My Profile Page](#my-profile-page)
- [16. Sign Out Page](#sign-out-page)

<br>

1. #### Navbar Desktop

Unregistered user:

- TEST 1.1 - _Anaconda MAA_ logo links to the _Home_ page - YES
- TEST 1.2 - _About_ link goes to _About_ page - YES
- TEST 1.3 - _Classes_ link goes to _Classes_ page - YES
- TEST 1.4 - _Shop_ link goes to _Shop_ page - YES
- TEST 1.5 - _Contact_ link goes to _Contact_ page - YES
- TEST 1.6 - "Shopping bag amount in Euros" link goes to _Shopping Bag_ page - YES
- TEST 1.7 - _Join Now_ link goes to _Membership_ page - YES
- TEST 1.8 - _Account_ button submenu shows only _Login_ and _Sign up_ links to non-registered (not logged in) users - YES
- TEST 1.9 - _Sign up_ link under _Accounts_ button (not logged in user) links to _Sign Up_ page - YES
- TEST 1.10 - _Login_ link under _Accounts_ button (not logged in user) links to _Sign In_ page - YES

<br>

Registered user:

- TEST 1.11 - _Account_ button submenu shows only _My Profile_ and _Logout_ links to registered (and logged in) users - YES
- TEST 1.12 - User icon appears above _Account_ button when user is logged in and disappears when user logged out - YES
- TEST 1.13 - "Shopping bag amount in Euros" link stays white when _Shopping Bag_ is empty and becomes blue when there is at least one item in the _Shopping Bag_ - YES
- TEST 1.14 - "Shopping bag amount in Euros" link value always reflects the actual total value of the _Shopping Bag_ - YES
    - TEST 1.15 - _My Profile_ link under _Accounts_ button (registered user) links to _My Profile_ page - YES
    - TEST 1.16 - _Logout_ link under _Accounts_ button (registered user) links to _Sign Out_ page - YES

<br>

Admin user:

- TEST 1.17 - _Account_ button submenu shows _Products_, _Memberships_, _Classes_, _My Profile_ and _Logout_ links to (logged in) admin users - YES
- TEST 1.18 - _Products_ link under _Accounts_ button (admin user) links to _Add Product_ page - YES
- TEST 1.19 - _Memberships_ link under _Accounts_ button (admin user) links to _Add Membership_ page - YES
- TEST 1.20 - _Classes_ link under _Accounts_ button (admin user) links to _Add Class_ page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

2. #### Navbar Mobile

Unregistered user:
- TEST 2.1 - _Anaconda MAA_ logo links to the _Home_ page - YES
- TEST 2.2 - 'Hamburger' button unfolds/folds the navigation links - YES
- TEST 2.3 - _About_ link goes to _About_ page - YES
- TEST 2.4 - _Classes_ link goes to _Classes_ page - YES
- TEST 2.5 - _Shop_ link goes to _Shop_ page - YES
- TEST 2.6 - _Contact_ link goes to _Contact_ page - YES
- TEST 2.7 - _Join Now_ link goes to _Membership_ page - YES
- TEST 2.8 - "Shopping bag amount in Euros" link goes to _Shopping Bag_ page - YES
- TEST 2.9 - _Account_ button submenu shows only _Login_ and _Sign up_ links to non-registered (not logged in) users - YES
- TEST 2.10 - _Sign up_ link under _Accounts_ button (not logged in user) links to _Sign Up_ page - YES
- TEST 2.11 - _Login_ link under _Accounts_ button (not logged in user) links to _Sign In_ page - YES

<br>

Registered user:

- TEST 2.12 - _Account_ button submenu shows only _My Profile_ and _Logout_ links to registered (and logged in) users - YES
- TEST 2.13 - User icon appears above _Account_ button when user is logged in and disappears when user logs out - YES
- TEST 2.14 - "Shopping bag amount in Euros" link stays white when _Shopping Bag_ is empty and becomes blue when there is at least one item in the _Shopping Bag_ - YES
- TEST 2.15 - "Shopping bag amount in Euros" link value always reflects the actual total value of the _Shopping Bag_ - YES
    - TEST 2.16 - _My Profile_ link under _Accounts_ button (registered user) links to _My Profile_ page - YES
    - TEST 2.17 - _Logout_ link under _Accounts_ button (registered user) links to _Sign Out_ page - YES

<br>

Admin user:

- TEST 2.18 - _Account_ button submenu shows _Products_, _Memberships_, _Classes_, _My Profile_ and _Logout_ links to (logged in) admin users - YES
- TEST 2.19 - _Products_ link under _Accounts_ button (admin user) links to _Add Product_ page - YES
- TEST 2.20 - _Memberships_ link under _Accounts_ button (admin user) links to _Add Membership_ page - YES
- TEST 2.21 - _Classes_ link under _Accounts_ button (admin user) links to _Add Class_ page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

3. #### Footer:

- TEST 3.1 - _Home_ link goes to _Home_ page - YES
- TEST 3.2 - _About_ link goes to _About_ page - YES
- TEST 3.3 - _Classes_ link goes to _Classes_ page - YES
- TEST 3.4 - _Shop_ link goes to _Shop_ page - YES
- TEST 3.5 - _Contact_ link goes to _Contact_ page - YES
- TEST 3.6 - _Join Now_ link goes to _Membership_ page - YES
- TEST 3.7 - _Twitter_ icon opens _Twitter_ home page in new tab - YES
- TEST 3.8 - _Pinterest_ icon opens _Pinterest_ home page in new tab - YES
- TEST 3.9 - _Facebook_ icon opens _Facebook_ home page in new tab - YES
- TEST 3.10 - _Instagram_ icon opens _Instagram_ home page in new tab - YES
    - TEST 3.11 - _Youtube_ icon opens _Youtube_ home page in new tab - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

4. #### Home Page:

- TEST 4.1 - _Join Our Academy_ button on main banner links to _Membership_ page - YES
- TEST 4.2 - _Brazilian Jiu-Jitsu_ image links to _Why Brazilian Jiu-Jitsu?_ section in _About_ page - YES
- TEST 4.3 - _Read more_ link under Brazilian Jiu-Jitsu image links to _Why Brazilian Jiu-Jitsu?_ section in _About_ page - YES
- TEST 4.4 - _Kickboxing_ image links to _Why Kickboxing?_ section in _About_ page - YES
- TEST 4.5 - _Read more_ link under Kickboxing image links to _Why Kickboxing?_ section in _About_ page - YES
- TEST 4.6 - _Boxing_ image links to _Why Boxing?_ section in _About_ page - YES
- TEST 4.7 - _Read more_ link under Boxing image links to _Why Boxing?_ section in _About_ page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

5. #### About Page:

- TEST 5.1 - _Join Our Academy_ button in _Why Brazilian Jiu-Jitsu?_ section links to _Membership_ page - YES
- TEST 5.2 - _About our coaches..._ button in _Why Brazilian Jiu-Jitsu?_ section links to _Meet Our Instructors_ section on the same page - YES
- TEST 5.3 - _Join Our Academy_ button in _Why Kickboxing?_ section links to _Membership_ page - YES
- TEST 5.4 - _About our coaches..._ button in _Why Kickboxing?_ section links to _Meet Our Instructors_ section on the same page - YES
- TEST 5.5 - _Join Our Academy_ button in _Why Boxing ?_ section links to _Membership_ page - YES
- TEST 5.6 - _About our coaches..._ button in _Why Boxing?_ section links to _Meet Our Instructors_ section on the same page - YES
- TEST 5.7 - _Brazilian Jiu-Jitsu_ link in _Meet Our Instructors_ section links to _Why Brazilian Jiu-Jitsu?_ section on the same page - YES
- TEST 5.8 - _About Brazilian Jiu-Jitsu?_ link in _Meet Our Instructors_ section links to _Why Brazilian Jiu-Jitsu?_ section on the same page - YES
- TEST 5.9 - _Kickboxing_ link in _Meet Our Instructors_ section links to _Why Kickboxing?_ section on the same page - YES
- TEST 5.10 - _About Kickboxing..._ link in _Meet Our Instructors_ section links to _Why Kickboxing?_ section on the same page - YES
- TEST 5.11 - _Boxing_ link in _Meet Our Instructors_ section links to _Why Boxing?_ section on the same page - YES
- TEST 5.12 - _About Boxing..._ link in _Meet Our Instructors_ section links to _Why Boxing?_ section on the same page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

6. #### Classes Page:

- TEST 6.1 - _See timetable..._ link in _Kids & Teens Classes_ section links to _Class Timetable_ section on the same page - YES
- TEST 6.2 - _Join Our Academy_ button in _Kids & Teens Classes_ section links to _Membership_ page - YES
- TEST 6.3 - _See timetable..._ link in _Adults Classes_ section links to _Class Timetable_ section on the same page - YES
- TEST 6.4 - _Join Our Academy_ button in _Adults Classes_ section links to _Membership_ page - YES

<br>

Admin user:
- TEST 6.5 - _Edit_ and _Delete_ buttons appear in each class box in _Class Timetable_ section when admin user is logged in - YES
- TEST 6.6 - _Edit_ button in each class box in _Class Timetable_ section links to the _Edit Class_ page populated with the corresponding class details - YES
- TEST 6.6 - _Delete_ button in each class box in _Class Timetable_ section deletes the respective class - relevant 'toast' is displayed - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

7. #### Shop Page:

- TEST 7.1 - _'Search our site'_ box empty entry reloads the page with all products - relevant 'toast' is displayed - YES
- TEST 7.2 - _'Search our site'_ search that does not appear in the database reloads the page with no products - relevant 'toast' is displayed - YES
- TEST 7.3 - _'Search our site'_ search that does appear in the database reloads the page with all products meeting the search criteria entered - relevant 'toast' is displayed - YES
- TEST 7.4 - _'Sort by Price (low to high)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.5 - _'Sort by Price (high to low)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.6 - _'Sort by Rating (low to high)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.7 - _'Sort by Rating (high to low)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.8 - _'Sort by Name (A-Z)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.9 - _'Sort by Name (Z-A)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.10 - _'Sort by Category (A-Z)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.11 - _'Sort by Category (Z-A)'_ reloads the page with current selection of products in the correct order - YES
- TEST 7.12 - Current count of products loaded works correctly - YES
- TEST 7.13 - Current count of products loaded _Products Home_ link reloads page with all products - YES
- TEST 7.14 - Clicking on the 'All' tab above the products displays all products - YES
- TEST 7.15 - Clicking on the _'Boxing Bags'_ tab above the products displays all products in the 'Boxing Bags' category - YES
- TEST 7.16 - Clicking on the _'Protective'_ tab above the products displays all products in the 'Protective' category - YES
- TEST 7.17 - Each product image links to the respective _Product Detail_ page - YES
- TEST 7.18 - _Join Our Academy_ button at the bottom of the page links to _Membership_ page - YES

<br>

Admin user:
- TEST 7.16 - _Edit_ and _Delete_ buttons appear underneath each product when admin user is logged in - YES
- TEST 7.17 - _Edit_ button underneath each product links to the _Edit Product_ page populated with the corresponding product details - YES
- TEST 7.18 - _Delete_ button underneath each product deletes the respective product - relevant 'toast' is displayed - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

8. #### Contact Page:

- TEST 8.1 - _Contact Form_ does not validate on 'Submit' if _'Name'_ field is empty - YES
- TEST 8.2 - _Contact Form_ does not validate on 'Submit' if _'E-mail'_ field is empty - YES
- TEST 8.3 - _Contact Form_ does not validate on 'Submit' if _'E-mail'_ entry does not follow the email format (@ missing) - YES
- TEST 8.4 - _Contact Form_ does not validate on 'Submit' if _'Message'_ field is empty - YES
- TEST 8.5 - _Contact Form_ is sent successfully if form valid - relevant 'toast' is displayed - YES
- TEST 8.6 - Message from _Contact Form_ is sent to default email - EmailJS connected correctly - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

9. #### Membership Page

- TEST 9.1 - _Get Started_ button links to _Contact Page_ - YES
- TEST 9.2 - _See Timetables here_ link goes to _Class Timetable_ of _Classes Page_ - YES


<br>

Admin user:
- TEST 9.3 - _Edit_ and _Delete_ buttons appear underneath each membership box when admin user is logged in - YES
- TEST 9.5 - _Edit_ button underneath each membership links to the _Edit Membership_ page populated with the corresponding membership details - YES
- TEST 9.6 - _Delete_ button underneath each membership box deletes the respective membership - relevant 'toast' is displayed - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

10. #### Sign Up Page

- TEST 10.1 - _Already have an account?_ link goes to _Sign In_ page - YES
- TEST 10.2 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if any of the fields is empty - YES
- TEST 10.3 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if _'E-mail address'_ entry does not follow the email format (@ missing) - YES
- TEST 10.4 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if _'E-mail address'_ and 'E-mail address confirmation' entries are not the same - YES
- TEST 10.5 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if _'Password'_ entry is too common (ex.password) or too short - YES
- TEST 10.6 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if _'Password'_ and 'Password (again)' entries are not the same - YES
- TEST 10.7 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if user with the same email address is already registered - YES
- TEST 10.8 - _Sign Up Form_ does not validate on 'Submit' ('Sign Up') if user with the same username is already registered - YES
- TEST 10.9 - On 'Submit' ('Sign Up') of the validated _Sign Up Form_ the user is redirected to the _Verify Your E-mail Address_ page - relevant 'toast' is displayed - YES
- TEST 10.10 - On 'Submit' ('Sign Up') of the validated _Sign Up Form_ the link to verify e-mail is sent to the submited e-mail address - YES
- TEST 10.11 - Verify email address link sent to email works correctly and redirects user to _Confirm E-mail Address_ page - YES
- TEST 10.12 - Confirming email address on _Confirm E-mail Address_ page takes user to _Sig In_ page - YES
- TEST 10.13 - Confirming email address on _Confirm E-mail Address_ page creates a new user in the database - YES
- TEST 10.14 - _Back to Login_ button links to _Sign In_ page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

11. #### Sign In Page

- TEST 11.1 - _If you don't have account yet..._ link goes to _Sign Up_ page - YES
- TEST 11.2 - _Sign In Form_ displays Allauth message: 'The username and/or password you specified are not correct.' on 'Submit' ('Sign In'), if either _'Username'_ or _'Password'_ field entries don't match any user saved in the database - YES
- TEST 11.3 - On 'Submit' ('Sign In') of the validated and correct _Sign In Form_ the user is saved in the session cookie and redirected to the _Home_ page - YES
- TEST 11.4 - _Home_ button links to _Home_ page - YES
- TEST 11.5 - _Forgot Password_ link goes to _Password Reset_ page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

12. #### Add Product Page

Admin user:

- TEST 12.1 - _Add Product Form_ does not validate on 'Submit' ('Add Product') if _'Name'_ field is empty - YES
- TEST 12.2 - _Add Product Form_ does not validate on 'Submit' ('Add Product') if _'Desccription'_ field is empty - YES
- TEST 12.3 - _Add Product Form_ does not validate on 'Submit' ('Add Product') if _'Price'_ field is empty - YES
- TEST 12.4 - _Add Product Form_ does not validate on 'Submit' ('Add Product') if _'Price'_ field entry has different format than digits, max digits: 6, max decimal places: 2 - YES
- TEST 12.5 - _Select Image_ button allows user to select an image (from own device) and attach it to the product - YES
- TEST 12.6 - On 'Submit' ('Add Product') of the _Add Product Form_ without image attached to the product, a default placeholder image ('no image') is attached - YES
- TEST 12.7 - 'Cancel' button links to the _Shop_ page - YES
- TEST 12.8 - On 'Submit' ('Add Product')of the validated _Add Product Form_ a new product is added to the database - YES
- TEST 12.9 - On 'Submit' ('Add Product') of the validated _Add Product Form_, the user is redirected to the _Product Details_ page of the newly added product with all information displayed correctly - relevant 'toast' is displayed - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

13. #### Add Membership Page

- TEST 13.1 - _Add Membership Form_ does not validate on 'Submit' ('Add Membership') if _'Name'_ field is empty - YES
- TEST 13.2 - _Add Membership Form_ does not validate on 'Submit' ('Add Membership') if _'Price'_ field is empty - YES
- TEST 13.3 - _Add Membership Form_ does not validate on 'Submit' ('Add Membership') if _'Price'_ field entry has different format than digits, max digits: 3 - YES
- TEST 13.4 - 'Cancel' button links to the _Membership_ page - YES
- TEST 13.5 - On 'Submit' ('Add Membership') of the validated _Add Membership Form_ a new membership is added to the database - YES
- TEST 13.6 - On 'Submit' ('Add Membership') of the validated _Add Membership Form_, the user is redirected to the _Membership_ page with the new membership rendered on the page - relevant 'toast' is displayed - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

14. #### Add Class Page

- TEST 14.1 - _Add Class Form_ does not validate on 'Submit' ('Add Class') if _'Class Name'_ field is empty - YES
- TEST 14.2 - _Add Class Form_ does not validate on 'Submit' ('Add Class') if _'Class Time'_ field is empty - YES
- TEST 14.3 - 'Cancel' button links to the _Classes_ page - YES
- TEST 14.4 - On 'Submit' ('Add Class') of the validated _Add Class Form_ a new Class is added to the database - YES
- TEST 14.5 - On 'Submit' ('Add Class') of the validated _Add Class Form_, the user is redirected to the _Classes_ page with the new class rendered on the page (if the total of all classes in database is equal to or less than 48) - relevant 'toast' is displayed - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

15. #### My Profile Page

- TEST 15.1 - _Order History_ section lists all orders in the database for current user - YES
- TEST 15.2 - _'Order Number'_ link takes user to the respective order's details (_Thank You_ page) originaly generated for the order - YES


- TEST 15.2 - _Update Information_ button links to _Home_ page - YES

- TEST 15.2 - _Update Information_ button links to _Home_ page - YES

<br>

[Back to Manual Testing Contents](#manual-testing-contents)

<br>

16. #### Sign out Page

- TEST 16.1 - _Sign Out_ removes user from the session button and redirects to _Home_ page - relevant 'toast' is displayed - YES
- TEST 16.2 - _Cancel_ button links to _Home_ page - YES

[Back to top](#contents)

---

<br>

### Bugs
#### Bugs Fixed

#### Bugs not Fixed

<br>

[Back to top](#contents)