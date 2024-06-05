# Test Descriptions

## Introduction

This file contains information regarding tests performed on the device and observed results after performing these tests. Most of these tests have corresponding traffic files.

## Tests

### General Device usage test

In this test, the device was used in a specific manner (for example: We execute an an action 10 times and see what event was also launched 10 times). We then compare the actions we did with the resulting traffic to see what event/request is associated with what action. This test was one of the first tests ever executed but it holds little value now as the subsequent tests have a better way of indicating specific events thanks to the brightness trick explained later.

**Steps**

* Clicked home widget 10 times 
* Clicked my books 10 times 
* Clicked discover 10 times 
* Clicked more 10 times 
* Clicked my wishlist 10 times (wishlist and then back) 
* Clicked my articles 10 times (my articles and then back) 
* Clicked activity 10 times (and then back)
* Clicked settings 10 times 
* Clicked brightness 10 times 
* Changed brightness and natural light 10 times and clicked auto 
* Clicked wifi 10 times 
* Clicked settings: 
	* Clicked accounts 10 times 
		* Clicked kobo plus 
		* Clicked redeem
		* Clicked parental controls 
		* Clicked pocket sign in
		* Clicked adobe authorization 
	* Clicked date and time 10 times 
	* Clicked language and dictionaries 
	* Clicked wifi connection 10 times 
	* Clicked sync 10 times 
	* Clicked energy and privacy 10 times 
	* Clicked reading settings 10 times
	* Clicked manage download 10 times 
	* Clicked device info 10 times 
	* Clicked about 10 times 
* Clicked discover x
	* Switched 10 times between tabs 
	* Clicked search and searched "George RR Martin"
	* Changed search option 
	* Clicked search and search "dune"
	* Clicked recommended 
		* Clicked related reads
	* Clicked kobo originals
	* Clicked trending now
	* Scrolled down

**Results**

see `user-test-part-1.har` for the traffic and the `kobo-traffic-info.md` file

### User Bypass test

In this test, the user registration bypass hack has been used to test what the device does when there is no user.

**Preparation**

* Executed the user bypass hack
* Added the certificate to the device using telnet and USB connections

**Steps**

* Execute the user bypass hack again
* Added 2 files to the device: 1 epub and 1 pdf
* Reading books, browsing around on the device, ...

**Results**

* No analytics get sent
* Nothing remarkable happens
* Almost no communication
* Good way to prevent tracking
* see `no-user-test.har` for the traffic

### Existing User test

In this test, an existing user was registered on a new device.

**Preparation**

* Added the certificate to the device using telnet and USB connections

**Steps**

* Register an existing user

**Result**

* A lot of new requests being sent not seen before
* passwords being sent unencrypted
* NOTE: De traffic file for this test contains requests from another device so the results are a bit scrambled. All plaintext passwords have also been redacted.
* see `second-user-scrambled-no-password.har` for the traffic

### Book usage test

In this test, we used the fact that we can see the brightness being changed to our advantage. We change the brightness to a specific level every time we execute an action. This makes sure that we can determine what requests correspond to specific actions and makes it easier to follow along.

The goal is to analyze events that have to do with using/reading books and actions related to this.

**Steps**

* Set brightness to 24
* Clicked my books
	* Set brightness to 0
	* Switched tabs 4 times (changed brightness to 26 and 0 between tabs)
	* Set brightness to 24
	* Click books tab
	* In books tab: changed the filter and sort options
	* Set brightness to 0
	* Clicked the search icon top left
	* Change search location
	* Go back
* Set to brightness to 27
* Clicked home
* Set to brightness to 0
* Opened a book and read a page: side loaded
* Set to brightness to 34
* Opened a book and read a page: Kobo store
* Set to brightness to 0
* Opened a pdf and read a page
* **Crashed ---> device restarted itself**
* Set to brightness to 35
* Opened a book: Sideloaded
	* Read a page
	* Set to brightness to 0
	* Clicked 3 dots 10 times
	* Set brightness to 35
	* Clicked reading settings 10 times
		* Clicked advanced reading settings
	* Clicked the advanced font settings
	* Set brightness to 0
	* Clicked 3 dots and view details 
	* Clicked dictionary
	* Clicked hints and tips
	* Set brightness to 37
	* Searched a word in dictionary on page 40 -> word searched: khal
	* Searched a word in dictionary on page 40 -> word searched: night
	* Made a note on page 40
	* Made another note on page 41
	* Clicked the bar above and under when clicking in the middle of a book
	* Closed the book
	* Set brightness to 0
* Clicked recommended in home page
* Set brightness to 43
* Turned off and restarted the device

**Results**

see `reading-test-result.har` for the traffic and the `kobo-traffic-info.md` file

### Store usage test

The goal is to analyze events that have to do with using/browsing the store and actions related to this.

**Steps**

* Set brightness to 0 
* Click discover 
* Clicked wifi widget 
* Set brightness to 2 
* Click kobo plus tab 
* Set brightness to 0 
* Click ebooks tab 
* Set brightness to 3 
* Click recommended 
* Set brightness to 0 
* Clicked related reads tab 
* Set brightness to 3 
* Click just for you tab 
* Set brightness to 0 
* Click go back 
* Set brightness to 5 
* Click kobo originals 
* Set brightness to 0 
* Go back 
* Set brightness to 3 
* Click trending now
* Set bbrightnessr to 0
* Scroll down
* Set brightness to 3
* Go back
* Set brightness to 0

**Results**

see `discover-tab-test.har` for the traffic and the `kobo-traffic-info.md` file

### Privacy settings test

Kobo contains a webpage on which you can change your privacy options ([https://www.kobo.com/privacy](https://www.kobo.com/privacy)). This test determines if these settings affect the tracking that is happening on the device.

**Steps**

We first use the device normally with the Privacy Tracking Settings enabled:

* Timestamp first request: Thu, 15 Feb 2024 18:47:55 GMT
* Performance / Analysis setting: ON
* Observed result:
	* google analytics sent
	* analytics/event sent
	* Changed brightness to 82 -> was found in the event requests
	

We now disable the Privacy Tracking settings and use the device for 20 minutes:

* Timestamp request when turning OFF analytics and syncing: Thu, 15 Feb 2024 19:03:13 GMT
* Performance / Analysis setting: OFF
* Observed result:
	* no google analytics sent
	* no analytics request sent
	* Changed brightness to 44
	* Changed brightness to 80
	
After one hour we enabled the Privacy Tracking settings again:

* Timestamp request when turning ON analytics and syncing: Thu, 15 Feb 2024 19:23:42 GMT
* Performance / Analysis setting: ON
* Observed result:
	* google analytics sent
	* analytics request sent
	* Changed brightness to 21: The old brightness was 80, and there never was an event changing from 82 -> 44 and from 44 -> 80, meaning that those events didn't get sent.

**Results**

It is possible to disable all tracking on the device. see `privacy-settings-test.har` for the traffic and `privacy-permissions-test.har` to see the difference in privacy permissions.

### Book type test

In this test, we load multiple file types on the device to see which ones get recognized and to see what kind of metadata gets sent

**Preparation**

* Added the following filetypes on the device:
	* PDF
	* Microsoft Word
	* Images
	* Epub

**Steps**

* Opened the available files to trigger the corresponding requests that sent metadata

**Results**

* Beside the Microsoft Word file, every other filetype can be used on the device
* see `book-type-metadata-test.har` for the traffic and the overview file for more information

### Beta feature test

Beta features are features that you can use on your e-reader but Kobo does not provide support for it. This test is to show what the effect on the traffic is of using these functions.

**Steps**

* Set brightness to 56 
* Open the web browser
* Search the following: dog
* Go back
* Set brightness to 23
* Make a sketch
* Go back
* Sync the device to trigger analytic event requests

**Results**

* Sketches are saved on the device
* see `beta-feature-test.har` for the traffic and the overview file for more information

### Tracking ID test

This test was used to show the different tracking ids used by the two devices tested.

**Steps**

* Used device 1
* Used device 2
* Capture and compare traffic

**Results**

* Each device has unique identifiers and the user has unique identifiers
* see `tracking-id-check.har` for the traffic and the overview file for more information

### Misc traffic tests

These were small tests used to confirm specific findings or just interesting traffic that was captured on the device. There are no specific steps followed for these tests. The following is a list of the traffic files and their meaning:

* `content-compare-1.har`: Shows the requests for different content types.
* `e-reader-1-example-requests.har`: Contains requests for a specific e-reader.
* `privacy-settings-not-working.har`: Test in which the privacy settings are not working. Requests are being sent when the tracking should be disabled.
* `used-browser-random.har`: Test in which the experimental browser was used on the device. Nothing interesting happens in the data collection traffic.
* `test-no-user-1.har`: Traffic with similar results to the User Bypass test. Used to confirm the findings.
* `device-1-synced-notes-test.har`: Traffic to check if notes are synced. Nothing interesting happens in the data collection traffic.

Remaining traffic files not named in this document have no specific meaning and contains captured traffic with no real importance.


