Test project for possible Django 1.9 bug
========================================

This project defines two apps containing three models:

app1
 - ConcreteModel
 - AbstractModel (abstract with a foreign key to ConcreteModel)

app2
 - DerivedModel (derived from app1.AbstractModel)


Running makemigrations for app1 works fine. Running it for app2 however gives the following error:

   app2.DerivedModel.foreign_key: (fields.E300) Field defines a relation with model 'ConcreteModel', which is either not installed, or is abstract.
