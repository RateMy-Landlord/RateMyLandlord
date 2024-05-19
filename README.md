# RateMyLandlord
## How to setup?
### How to generate the database?
```
1. python3 manage.py makemigrations

(If the code fails to generate migrations folder then try...)
python3 manage.py makemigrations landlords
python3 manage.py makemigrations reviews


2. python3 manage.py migrate
```

### How to create administrator user
```
(Create admin user for admin access in /admin url)
python3 manage.py createsuperuser
```

### How to deploy?
```
python3 manage.py runserver 0.0.0.0:<port number to host>
```

## Inspiration

The sheer brilliance of our landlord-dominated rental market! Their unfettered ability to concoct rules at whim and treat tenants like mere mortals has truly been the wind beneath our sarcastic wings.

## What it does

Our website allows tenants to rate their landlords to help other tenants make an informed choice while renting a place.

## How we built it

The Django framework served as the backbone to our project, as it's MVC architecture and built-in templating system allowed for efficient data handling and development. We also utilized the CSS framework Bulma, to provide a streamlined design to our website with minimal effort.

## Challenges we ran into

Our front end developer is good at React but had no idea on how to exploit Django Framework. So, he had to go through bunch of tutorials in order to figure it out.

## Accomplishments that we're proud of

We are proud of deploying Django girls platform for full stack development for the very first time.

## What we learned

We learnt the importance of framework, they make our life easier when coding for bigger projects.

## What's next for Rate my Landlord

We are planning to add more functionalities to it such as verifying a tenant's identity and his reasoning behind low rating before posting a review for the landlord.

## Hackathon Submission
- https://devpost.com/software/rate-my-landlord-hp2g7l?ref_content=my-projects-tab&ref_feature=my_projects