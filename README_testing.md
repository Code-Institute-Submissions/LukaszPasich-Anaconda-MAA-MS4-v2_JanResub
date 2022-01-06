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

<br>

[Back to top](#contents)

---

<br>

### Bugs
#### Bugs Fixed

#### Bugs not Fixed

<br>

[Back to top](#contents)