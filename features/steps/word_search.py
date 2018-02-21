from behave import *

from src.word_search import WordSearch

use_step_matcher("parse")


@given('a "{word}" to find')
def step_impl(context, word):
    context.word = word


@when("I search")
def step_impl(context):
    word_search = WordSearch()
    context.result = word_search.search(context.word)


@then("I find the word horizontally")
def step_impl(context):
    assert context.result == "SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)"
