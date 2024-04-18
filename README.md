# Nada's Kitchen

Nada's Kitchen is a fictional catering business located Dublin, Ireland. The app is a kitchen app that takes customer orders 48 hours in advance. The app is designed to allow customers to view the food menu and place orders online. It also provides customers with a simple, easy to use ordering system that connects to their registered profile.
The live link can be found here: [Live Site - Nada's Kitchen](https://nadas-cuisine-ca42fb816afa.herokuapp.com/)

![Mock Up](static/img/am-i-responsive.JPG)

## Table of Contents
- [Sizzle and Steak](#nada's-kitchen)
    - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
    - [The-Strategy-Plane](#the-strategy-plane)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
        - [Milestones](#milestones)
        - [Issues](#issues)
    - [The-Scope-Plane](#the-scope-plane)
    - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)


# User-Experience-Design

## The-Strategy-Plane

### Site-Goals

The site is aimed to help customers make quick orders from the UI without the need to call the catering company, while enabling the business staff to add menu items from the backend and an enhanced capability to delete a menuitem from the UI. 

The site enables customers to create, view and update their login profiles to aid customer contact and delivery addresses.  

### Agile Planning

This project was developed using agile methodologies by delivering small features in incremental sprints. 
There were 3 sprints in total.

The project enabled issues, prioritized under the labels, Must have, should have, could have and won't have. Labels were assigned to sprints and story pointed according to complexity. "Must have" stories were completed first, "should haves" and then finally "could haves". It was done this way to ensure that all core requirements were completed first, however, the sprints were completed concurrently due to granular requirements that may have been placed on hold until a complete solution was developed.

The Kanban board was created using github projects and can be located [here](https://github.com/users/jjsemaan/projects/4) and can be viewed to see more information on the project cards. All issues have a full set of acceptance criteria in order to define the functionality that marks that issue as complete.

![Kanban image](static/img/kanban.JPG)

#### Milestones

The project had 6 main milestones:

**Milestone 1 - Base Setup**

The base setup milestone is for all issues needed for the base set up of the application. Without the base setup, the app would not be possible so it was the first milestone to be delivered as all other features depend on the completion of the base setup.

**Milestone 2 - Menu Page**

The menu pages milestone was used for the food menu page and for other small pages. Instead of creating milestones for tiny features, these small deliverables were all added here.

**Milestone 3 - Authentication**

The authentication milestone is for all issues related to the registration, login and authorisation of views. This milestone provides critical functionality and value as without it the customer would not be able to make orders securely.

**Milestone 4 - Order**

The order milestone is used for the development of user models that enable CRUD functionality in the site.

**Milestone 5 - Flash Messages**

The flash messages milestone is used in the development of views that enable notifications by either levereging Django built-in messaging or via JavaScript.

**Milestone 6 - Documentation**

The flash messages milestone is used in the development of views that enable notifications by either levereging Django built-in messaging or via JavaScript.

#### Issues

The following issues (by sprint) were completed over a period of four weeks:

**Sprint 1**

As a developer, I need to set up the project and run Django in the browser so that the project is ready for implementation.

As a developer, I need to setup and deploy my project on Heroku to make sure that it is progressing as expected.

As a developer, I need to create a database to enable CRUD functionality.

As a developer, I need to create the base.html to to be reused by other pages.

**Sprint 2**

As a developer, I need to create a user intuitive homepage to facilitate UX.

As a developer, I need to create an About page to inform the users about the site.

As a developer, I need to create a food menu page for the customer's UX.

As a developer, I need to create a food menu for the customer to enable connection to ordering food.

As a developer, I need to create user registration in order to authenticate customers.

As a developer, I could give the user the ability to change their password when logged in.

As a developer, I need to extend the user profile to include **user delivery address and phone number" by adding CRUD functionality so that the customer is capable of updating their profile if need be.

As a developer, I need to style my authentication forms so that they are more intuitive and neat.

As a developer, I need to create an order confirmation page so that the customer can review their order prior to payment.

**Sprint 3**

As a developer I need to add flash messages on my website to acknowledge button actions.

As a developer I need to add a date picker so that the customer can select their preferred delivery date.

As a developer I need to create a README file to provide guided lines to app users.

## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 280px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality (from UI) Create, Read, Update for User Profiles and full CRUD for admin from back end in addition to Admin Delete functionality (from UI). 
* Restricted role based features
* Home and About page with business information

## The-Structure-Plane

### Features

**Navigation Menu**

 The Navigation contains links for Home, Bookings, Menus and has auth options.

The following navigation items are available on all pages:
  * Home            -> index.html           - Visible to all.
  * About Us        -> about.html           - Visible to all.
  * Orders          -> order.html           - Visible upon login authentication. This is the food menu.
  * Order Details   -> orderconfirm.html    - Visible once Place Order button is clicked.
  * Profile         -> profile.html         - Visible to all logged-in customers.
  * Profile Update  -> profile-update.html  - Visible to all logged-in customers to update their details.
  * Login           -> login.html           - Visible to logged out users
  * Register        -> register.html        - Visible to logged out users
  * Change Password -> change-password.html - Visible to logged-in users

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

![Navbar](static/img/navbar.JPG)


Implementation:

**Home Page**

The home page contains a background image of a chef standing in her kitchen with a slogan and an Order button in the foreground. This will immediately make it evident to the user, what the purpose of the website is.

The order button provides access to the food menu and is restricted to logged-in users. 

**Footer**

A footer has been added to the bottom of the site with copyright credits.

![Home Image](static/img/home-page.JPG)

**Login Page**

A Login page restricts access to the food and ordering menu.

![Loging Page](static/img/login-page.JPG)

**Food Menu Ordering Page**

A food menu page ordering page was implemented to allow customers to make orders and request particular delivery dates from the UI. The Delete anchor beside each item is accessible only to admins. 

![Food Menu 1 of 2](static/img/food-menu.JPG)
![Food Menu 2 of 2](static/img/place-order.JPG)
