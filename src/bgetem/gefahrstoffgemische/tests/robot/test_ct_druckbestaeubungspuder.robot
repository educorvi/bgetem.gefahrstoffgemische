# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.gefahrstoffgemische -t test_druckbestaeubungspuder.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.gefahrstoffgemische.testing.BGETEM_GEFAHRSTOFFGEMISCHE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/gefahrstoffgemische/tests/robot/test_druckbestaeubungspuder.robot
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

Scenario: As a site administrator I can add a Druckbestaeubungspuder
  Given a logged-in site administrator
    and an add Druckbestaeubungspuder form
   When I type 'My Druckbestaeubungspuder' into the title field
    and I submit the form
   Then a Druckbestaeubungspuder with the title 'My Druckbestaeubungspuder' has been created

Scenario: As a site administrator I can view a Druckbestaeubungspuder
  Given a logged-in site administrator
    and a Druckbestaeubungspuder 'My Druckbestaeubungspuder'
   When I go to the Druckbestaeubungspuder view
   Then I can see the Druckbestaeubungspuder title 'My Druckbestaeubungspuder'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Druckbestaeubungspuder form
  Go To  ${PLONE_URL}/++add++Druckbestaeubungspuder

a Druckbestaeubungspuder 'My Druckbestaeubungspuder'
  Create content  type=Druckbestaeubungspuder  id=my-druckbestaeubungspuder  title=My Druckbestaeubungspuder

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Druckbestaeubungspuder view
  Go To  ${PLONE_URL}/my-druckbestaeubungspuder
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Druckbestaeubungspuder with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Druckbestaeubungspuder title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
