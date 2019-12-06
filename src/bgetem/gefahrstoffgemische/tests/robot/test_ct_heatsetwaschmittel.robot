# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s bgetem.gefahrstoffgemische -t test_heatsetwaschmittel.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src bgetem.gefahrstoffgemische.testing.BGETEM_GEFAHRSTOFFGEMISCHE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/bgetem/gefahrstoffgemische/tests/robot/test_heatsetwaschmittel.robot
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

Scenario: As a site administrator I can add a Heatsetwaschmittel
  Given a logged-in site administrator
    and an add Heatsetwaschmittel form
   When I type 'My Heatsetwaschmittel' into the title field
    and I submit the form
   Then a Heatsetwaschmittel with the title 'My Heatsetwaschmittel' has been created

Scenario: As a site administrator I can view a Heatsetwaschmittel
  Given a logged-in site administrator
    and a Heatsetwaschmittel 'My Heatsetwaschmittel'
   When I go to the Heatsetwaschmittel view
   Then I can see the Heatsetwaschmittel title 'My Heatsetwaschmittel'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Heatsetwaschmittel form
  Go To  ${PLONE_URL}/++add++Heatsetwaschmittel

a Heatsetwaschmittel 'My Heatsetwaschmittel'
  Create content  type=Heatsetwaschmittel  id=my-heatsetwaschmittel  title=My Heatsetwaschmittel

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Heatsetwaschmittel view
  Go To  ${PLONE_URL}/my-heatsetwaschmittel
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Heatsetwaschmittel with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Heatsetwaschmittel title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
