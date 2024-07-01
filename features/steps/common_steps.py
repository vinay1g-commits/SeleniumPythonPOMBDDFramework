# common_steps.py
from behave import *
from features.pages.HomePg import HomePg


@given('I am on the home page')
def step_impl(context):
    context.home = HomePg(context.driver)
    context.home.homepgtitle()
