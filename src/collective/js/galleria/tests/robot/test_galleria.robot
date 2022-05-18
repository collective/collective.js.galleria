*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As anonymous I want to be able to see galleria
  [Documentation]  Test that the example gallery is working.
  Given galleria page
   Then I can see the gallery

Scenario: As anonymous I want to be able to change gallery item
  [Documentation]  Test change gallery item.
  Given galleria page
   When I change the item
   Then the visible image is changed


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

galleria page
  Go To  ${PLONE_URL}/collective.js.galleria.test
  Wait Until Element Is Visible  css=.galleria-container


# --- WHEN -------------------------------------------------------------------

I change the item
  Click Element  css=.galleria-image-nav-right
  Wait Until Element Is Not Visible  css=img[src="https://picsum.photos/id/1055/800/500.jpg"]


# --- THEN -------------------------------------------------------------------

I can see the gallery
  Wait Until Element Is Visible  css=img[src="https://picsum.photos/id/1055/800/500.jpg"]

the visible image is changed
  Wait Until Element Is Visible  css=img[src="https://picsum.photos/id/268/800/500.jpg"]
