import time
from behave import *
from features.pages.PhotosPg import PhotosPg


@when('I click on the more button inside header menu')
def step_impl(context):
    context.home.morebtn_menu()  # Use the existing instance from context


@when('I click on photos text hyperlink')
def step_impl(context):
    context.home.photos_link()  # Use the existing instance from context


@then('I should be navigated to the photos page')
def step_impl(context):
    photos = PhotosPg(context.driver)
    photos.photos_pg_assertion()
