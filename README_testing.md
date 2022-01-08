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





[Back to top](#contents)

---

<br>

### Bugs
#### Bugs Fixed

#### Bugs not Fixed

<br>

[Back to top](#contents)