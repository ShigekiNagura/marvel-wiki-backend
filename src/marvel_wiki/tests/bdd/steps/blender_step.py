from behave import given, then, when
from hamcrest import assert_that, equal_to

from marvel_wiki.use_case.blender import Blender


@given('I put "{things}" in a blender')
def step_given_things_into_blender(context, things):
    context.blender = Blender()
    context.blender.add(things)


@when("I switch the blender on")
def step_when_switch_blender_on(context):
    context.blender.switch_on()


@then('It should transform into "{other_thing}"')
def step_then_should_transfer_into(context, other_thing):
    assert_that(context.blender.result, equal_to(other_thing))
