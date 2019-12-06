# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.gefahrstoffgemische -t test_gefahrstoffgemisch.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.gefahrstoffgemische.testing.BGETEM_GEFAHRSTOFFGEMISCHE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/gefahrstoffgemische/tests/robot/test_gefahrstoffgemisch.robot
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

Scenario: As a site administrator I can add a Gefahrstoffgemisch
  Given a logged-in site administrator
    and an add Gefahrstoffgemisch form
   When I type 'My Gefahrstoffgemisch' into the title field
    and I submit the form
   Then a Gefahrstoffgemisch with the title 'My Gefahrstoffgemisch' has been created

Scenario: As a site administrator I can view a Gefahrstoffgemisch
  Given a logged-in site administrator
    and a Gefahrstoffgemisch 'My Gefahrstoffgemisch'
   When I go to the Gefahrstoffgemisch view
   Then I can see the Gefahrstoffgemisch title 'My Gefahrstoffgemisch'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Gefahrstoffgemisch form
  Go To  ${PLONE_URL}/++add++Gefahrstoffgemisch

a Gefahrstoffgemisch 'My Gefahrstoffgemisch'
  Create content  type=Gefahrstoffgemisch  id=my-gefahrstoffgemisch  title=My Gefahrstoffgemisch

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Gefahrstoffgemisch view
  Go To  ${PLONE_URL}/my-gefahrstoffgemisch
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Gefahrstoffgemisch with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Gefahrstoffgemisch title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
