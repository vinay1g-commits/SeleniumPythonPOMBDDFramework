from behave import *
from features.pages.SearchPg import SearchPg


@when('I click on the search button')
def step_impl(context):
    context.home.clickingsrchbtn()  # Use the existing instance from context


@when('I enter the search query "{query}"')
def step_impl(context, query):
    context.home.searching(query)  # Pass the query to the method


@then('I should see the search results')
def step_impl(context):
    search = SearchPg(context.driver)
    search.searchpgassertion()
