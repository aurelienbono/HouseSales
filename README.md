
About
=====
## HOUSESALES

YdobonAi is a real estate company that focuses on selling houses.
RealAgents sells a variety of types of house in one metropolitan area.
Some houses sell slowly and sometimes require lowering the price in order to find a buyer.
In order to stay competitive, YdobonAi would like to optimize the listing prices of the houses it is trying to sell.
They want to do this by predicting the sale price of a house given its characteristics.
If they can predict the sale price in advance, they can decrease the time to sale..

Installation
============
- Create virtualenv - `virtualenv venv`

- Enter it `source venv/bin/activate`

- Install required packages `pip install -r requirements.txt`

- Run it: `python app.py runserver`

- Run it: `python manage.py makemigrations`

- Run it: `python manage.py migrate`

- For more - reference Django documentation


Route
=====
`/` is the project homepage <br>
`/predict` allows users to predict the price of an apartment based on the characteristics of the project<br>
`/resultat`  allows users to observe the prediction result<br>


