# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s pkan.examplecontentfilter -t test_pkan_item.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src pkan.examplecontentfilter.testing.PKAN_EXAMPLECONTENTFILTER_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_pkan_item.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a pkan_item
  Given a logged-in site administrator
    and an add pkan_item form
   When I type 'My PKAN Item' into the title field
    and I submit the form
   Then a pkan_item with the title 'My PKAN Item' has been created

Scenario: As a site administrator I can view a pkan_item
  Given a logged-in site administrator
    and a pkan_item 'My PKAN Item'
   When I go to the pkan_item view
   Then I can see the pkan_item title 'My PKAN Item'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add pkan_item form
  Go To  ${PLONE_URL}/++add++pkan_item

a pkan_item 'My PKAN Item'
  Create content  type=pkan_item  id=my-pkan_item  title=My PKAN Item


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the pkan_item view
  Go To  ${PLONE_URL}/my-pkan_item
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a pkan_item with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the pkan_item title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
