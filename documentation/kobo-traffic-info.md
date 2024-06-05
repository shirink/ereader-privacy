# Kobo traffic information

This file contains all information about traffic between Kobo Ereaders and Kobo servers.

## Kobo API

This sections contains traffic about the following host: `https://storeapi.kobo.com`

### Analytics

**URL:** `https://storeapi.kobo.com/v1/analytics/event`

**Description:** requests to this domain are always `POST` requests. The content being sent is of the type `application/json` (JSON file). The json file is structured as follows:

```
{
    "AffiliateName": "Kobo",
    "ApplicationVersion": "4.38.21908",
    "Events": [
        {
            "Attributes": {
                "origin": "MyBooks",
                "viewType": "Home"
            },
            "ClientApplicationVersion": "4.38.21908",
            "EventType": "Home",
            "Id": "15fca920-cd4d-4976-b64e-40c4919ad848",
            "Metrics": {},
            "TestGroups": {},
            "Timestamp": "2023-11-18T18:31:43Z"
        },
        ...
    ],
    "PlatformId": "00000000-0000-0000-0000-000000000376",
    "SerialNumber": "N249880244973"
}

```

The first and last two fields seem to stay the same because they are device specific. The `Events` array contains different events corresponding to different actions on the device. Each event is structured as follows:

```
{
    "Attributes": {
        "origin": "MyBooks",
        "viewType": "Home"
    },
    "ClientApplicationVersion": "4.38.21908",
    "EventType": "Home",
    "Id": "15fca920-cd4d-4976-b64e-40c4919ad848",
    "Metrics": {},
    "TestGroups": {},
    "Timestamp": "2023-11-18T18:31:43Z"
}
```

For now, the different EventTypes are: 

```
AppStart, AccessWishlist, Wishlist, UserMetadataUpdate, TasteProfilePromo, Search, HomeWidgetClicked, AppSettings, OpenContent, SearchOpened, LeaveContent, MyBooks, Stats, OpenReadingSettingsMenu, ListViewed, More, DictionaryLookup, BookProgress, WifiSettings, LibraryTabSelected, StatusBarOption, Home, NewWifiNetwork, Pocket, AutoColorToggled, BrightnessAdjusted, KoboPlusNonSubscriberPopup, KoboPlusPromo, DigitalCardRedemption, PocketSignIn, ReadingSettings, SubscriptionItems, SearchExecuted, Help, ReadingListBooks ,AccessLibrary, FilterSelected, ChangeSort, ItemDetail, StoreBookClicked, OpenHintsAndTips, CreateNote, WifiToggle
```

All events have a specific `Id` and `Timestamp`. The `Attributes`, `Metrics` and `TestGroups` fields are all variable depending on the event. The `ClientApplicationVersion` field seems to be the same for each event.

**Meaning of common subfields**

Attributes:
* Origin: judging from its occurence, it shows where the user 'came' from (indicating where the user was previously before executing the action)
* viewType: the type of view the user is getting. This field often gives more info on what exactly the user is seeing. For example: When the user clicks 'Discover', the EventType is 'Home' (not really clear) but the ViewType is `Store/Home`, which is more accurate.

**AppStart**

Description: Launched when the user boots the device.

**AccessWishlist**

Description: Event for when the user accesses the wishlist, usually followed by a WishList event. `Attributes` contains a `ViewType` field.

**Wishlist**

Description: Launched when the user is in the `Wishlist` window. Usually it follows an `AccessWishlist` event.

**UserMetadataUpdate**

Description: Often launched when the user starts the device. It contains metrics and attributes. `Attributes` contains user account information and device information. `Metrics` contains general information about the library.

Example of Attributes:

 * `AccountType`: "Adult",
 * `Affiliate`: "Kobo",
 * `CustomerType`: "RMR",
 * `DeviceModel`: "Kobo Clara HD",
 * `ExternalSDTotal`: "0",
 * `ExternalSDUsed`: "0",
 * `HasSubscription`: "false",
 * `InternalTotal`: "7014",
 * `InternalUsed`: "78",
 * `KoboSuperPointsBalance`: "0",
 * `KoboSuperPointsStatus`: "",
 * `LastReadingFont`: "default",
 * `OSVersion`: "4.1.15",
 * `SDCardStatus`: "No",
 * `StorageSize`: "7014"
 
Example of Metrics:

 * `DownloadedLibrarySize`: 6,
 * `LibrarySize`: 6,
 * `NumberOfBorrowedBooks`: 0,
 * `NumberOfDownloadedBorrowedBooks`: 0,
 * `NumberOfDownloadedFreeBooks`: 0,
 * `NumberOfDownloadedPaidBooks`: 1,
 * `NumberOfDownloadedPreviews`: 0,
 * `NumberOfDownloadedSubscribedBooks`: 0,
 * `NumberOfFixedLayoutBooks`: 0,
 * `NumberOfFreeBooks`: 0,
 * `NumberOfItemsOnCurrentReads`: 3,
 * `NumberOfPaidBooks`: 1,
 * `NumberOfPreviews`: 0,
 * `NumberOfReflowableBooks`: 6,
 * `NumberOfShelves`: 0,
 * `NumberOfSideloadedBooks`: 5,
 * `NumberOfSubscribedBooks`: 0

**TasteProfilePromo**

Description: Launched when the user accesses his recommended reads. `Attributes` contains a origin field (where the user came from).

**Search**

Description: This event gets launched when the user changes search settings (e.g, the search location) or when the user selected a place to search when opening the search window. `Attributes` contains 1 field:

* `Source`: Location to search

**HomeWidgetClicked**

Description: It contains one attribute called `action`. HomeWidgetClicked is caused when the user clicks on a widget from the `Home` tab. Example widgets are `CurrentRead` and `MyBooks`.

**AppSettings**

Description: Launched when the user accesses the settings from the `More` tab. `Attributes` contain an `Origin` and `viewType` field.

**OpenContent**

Description: Launched when the user has clicked a book in the `Home` tab. Usually follows a `HomeWidgetClicked` event but not always. `Attributes` contain information about the book being loaded. Example for a sideloaded book:

* `ContentFormat`: "application/epub+zip",  
* `ContentType`: "application/epub+zip",  
* `Monetization`: "Sideloaded",
* `Origin`: "Sideloaded",  
* `ViewType`: "ReadingView",  
* `author`: "George R. R. Martin",  
* `isbn`: "978-0-553-89784-5",  
* `progress`: "4",  
* `title`: "A Game of Thrones"  

Example for Kobo book:

* `ContentFormat`: "application/x-kobo-epub+zip",
* `ContentType`: "application/x-kobo-epub+zip",
* `Monetization`: "Paid",
* `Origin`: "Kobo Store",
* `StartFile`: "OEBPS/Text/Section0007.xhtml",
* `StartSpan`: "kobo.4.3",
* `ViewType`: "ReadingView",
* `progress`: "6",
* `volumeid`: "a4f64986-da66-4ae6-a8fa-09dd8b5ca0c3"

**SearchOpened**

Description: Launched when the user opens the search bar or search window. No `Attributes` or `Metrics`.

**LeaveContent**

Description: Launched when the user stops reading a book. `Attributes` contains information about the book and `Metrics` contains information about the reading session. Example for a sideloaded book:

`Attributes`:

 * `ContentFormat`: "application/epub+zip",
 * `ContentType`: "application/epub+zip",
 * `Monetization`: "Sideloaded",
 * `Origin`: "Sideloaded",
 * `ViewType`: "",
 * `author`: "George R. R. Martin",
 * `isbn`: "978-0-553-89784-5",
 * `progress`: "4",
 * `title`: "A Game of Thrones"

`Metrics`:

 * `IdleTime`: 80,
 * `PagesTurned`: 1,
 * `SecondsRead`: 147

**MyBooks**

Description: Launched when the user accesses the `MyBooks` tab. `Attributes` contain an `origin` field and `viewType` field. `Origin` denotes where the user came from when accessing the `MyBooks` tab

**Stats**

Description: Launched when the user accesses the 'Activity' option in the `More` tab. `Attributes` contain an `Origin` field and `ViewType` field.

**OpenReadingSettingsMenu**

Description: Launched when the users accesses the `ReadingSettingsMenu` while reading a book. `Attributes` contains an `action` field (meaning what action led to opening this menu). This action is usually followed by a `LeaveContent` event. Sometimes, `Attributes` contains a `Screen` field that shows what is show to the user (for example `font_settings`).

**ListViewed**

Description: Launched when the users views a list in the storefront. `Attributes` contains a field `ListType`.

**More**

Description: Launched when the user accesses the `More` tab. `Attributes` contain an `origin` field and `viewType` field.

**DictionaryLookup**

Description: Launched when the users looks something up in the dictionary while reading. `Attributes` contain the fields `Dictionary` and `Word`.

**BookProgress**

Description: Launched when the users has made progress while reading a book. `Attributes` contains the fields `progress` and `volumeid`.

**WifiSettings**

Description: Launched when the user clicks the Wifi `StatusBarOption`.

**LibraryTabSelected**

Description: Launched when the user changes tabs in the `MyBooks` or `Discover` tab. `Attributes` contain a field called `tab`. It shows which tab the user clicked.

**StatusBarOption**

Description: Launched when the user clicks an option from the upper status bar. `Attributes` contains a `Action` field. Example actions are:
* Light: When the user clicks the background light option 
* Wifi: When the user clicks the wifi option. If this is the case, this event is usually followed by a `WifiSettings` event.

**Home**

Description: Launched when the user accesses the `Discover` or `Home` tab. `Attributes` contain an `origin` field and `viewType` field. The viewtype specifies if the accessed tab is the `Discover` or `Home` tab.

**NewWifiNetwork**

Description: unsure if this launched when the users connects to a new network - TODO

**Pocket**

Description: Launched when the user accesses the `My Articles` option in the `More` tab. `Attributes` contain an `origin` field and `viewType` field.

**AutoColorToggled**

Description: Launched when the user toggles the automatic night light option in the `Light` statusbar option. `Attributes` contains a `Enabled` field. This field shows the resulting status after executing the option (`On` or `Off`).

**BrightnessAdjusted**

Description: Launched when the user changes the brightness and leaves the `Light` option tab. `Attributes` contain a `Method` field (probably means with what method the brightness has changed). `Metrics` contains two field: one for the original brightness and one for the new brightness. They are called `NewBrightness` and `OldBrightness`. 

**KoboPlusNonSubscriberPopup**

Description: Launched when the user clicks `Kobo Plus` in `More > Settings > Accounts`. `Attributes` contain a `Type` field (which denotes what kind of subscriber the user is) and an `action` field (TODO -> ?).

**KoboPlusPromo**

Description: Launched when the user clicks `Kobo Plus` in `More > Settings > Accounts`.`Attributes` contain an `Origin` field.

**DigitalCardRedemption**

Description: Launched when the user clicks `Redeem` in `More > Settings > Redeem (Redeem a Digital Card)`.

**PocketSignIn**

Description: Launched when the user clicks `Sign in` in `More > Settings > Pocket (Sign in)`.

**ReadingSettings**

Description: Launched when the user clicks the `Reading settings` option in the `More` tab or the user accesses the reading settings while reading a book. If the user goes back to the book, then this event is followed by an `OpenContent` event.

**SubscriptionItems**

Description: Launched when the user is shown subscription items (not sure if this is the case when the user clicks discorver OR when the users clicks a library tab). `Attributes` contains a `ViewType` entry.

**SearchExecuted**

Description: Launched when the user executes a search in the store. `Attributes` contains a `Origin`, `Source` and `IsDefault`.

Example `Attributes`:

* "IsDefault": "true",
* "Origin": "Store",
* "Source": "Store"


**ReadingListBooks**

Description: Launched when the user accesses the `Kobo Originals` tab. `Attributes` contains a `ListName` entry.

**Help**

Description: Launched when the user accesses the `Help` option in the `More` tab. `Attributes` contain an `origin` field and `viewType` field. 

**AccessLibrary**

Description: Launched when the user accesses specific tabs in the MyBooks tab. When a tab has to "show" books to the user, then this event gets launched. `Attributes` contain a `ViewType` entry that shows how the library is shown to the user.

**FilterSelected**

Description: Launched when the user chooses to filter the current selection on the screen. `Attributes` contains 2 entries:

* `Screen`: Shows what type of output is currently filtered (for example: `Library`)
* `Type`: On what the current selection is filtered

**ChangeSort**

Description: Launched when the user changes the sorting of the current listed items on the screen. `Attributes` contains 4 entries:

* `Action`: Action that made the event happen
* `Option`: On what we sort currently
* `SortType`: Not sure
* `ViewType`: The view that is currently shown to the user

**ItemDetail**

Description: Launched when the user views the details of a book while reading. `Attributes` contains the following:

 * `ContentType`: "Book",
 * `Origin`: "Library",
 * `Ownership`: "Sideloaded",
 * `Screen`: "ItemDetail",
 * `isInSubscription`: "No",
 * `volumeid`: "file:///mnt/onboard/books/A game of thrones -- Martin, George R. R. -- A game of thrones 1, 2011 -- Random House Publishing Group -- 2c2480353292ac9eaaa4a468f92d1094 -- Anna’s Archive.epub"

**StoreBookClicked**

Description: Launched when the user views the details of a book in the store.

**OpenHintsAndTips**

Description: Launched when the user opens `Hints and Tips`

**CreateNote**

Description: Launched when the users creates a note.

**WifiToggle**

Description: Launched when the user toggles the wifi. `Attributes` contains one entry: `WifiState`. This field shows the resulting Wifi status after executing the option (`On` or `Off`).

### Library

**URL:** `https://storeapi.kobo.com/v1/library`

### User

**URL:** `https://storeapi.kobo.com/v1/user`

**Description:** Requests to this domain seem to be GET requests. When the user accesses its profile information in the settings tab of the device, a request is sent to `https://storeapi.kobo.com/v1/user/profile`. The response contains the following JSON object:

```
{
    "AffiliateName": "Kobo",
    "AudiobooksEnabled": true,
    "CountryCode": "BE",
    "Geo": "BE",
    "HasPurchased": false,
    "HasPurchasedAudiobook": false,
    "HasPurchasedBook": false,
    "IsChildAccount": false,
    "IsEligibleForOrangeDeal": false,
    "IsLibraryMigrated": false,
    "IsOneStore": false,
    "IsOrangeAffiliated": false,
    "IsoCultureCode": "en-US",
    "PartnerId": "00000000-0000-0000-0000-000000000001",
    "PlatformId": "00000000-0000-0000-0000-000000000376",
    "PrivacyPermissions": [
        "feature.recommendation",
        "analytics.user",
        "analytics.platform.features",
        "analytics.catalog",
        "analytics.platform.crashreporting",
        "analytics.platform.AB",
        "readingstats.social",
        "analytics.tracking.campaigns",
        "analytics.tracking",
        "analytics.tracking.googleAnalytics",
        "analytics.tracking.googleTagManager",
        "analytics.tracking.maxymiser",
        "analytics.tracking.crashlytics",
        "analytics.tracking.hotjar",
        "analytics.tracking.firebase",
        "analytics.tracking.googleadwords",
        "analytics.tracking.facebookConnect",
        "analytics.tracking.googlePlusPlatform",
        "analytics.tracking.twitterButton",
        "analytics.tracking.adjust",
        "analytics.tracking.facebook",
        "analytics.tracking.criteo",
        "analytics.tracking.bing",
        "analytics.tracking.talkable",
        "analytics.tracking.pinterest",
        "analytics.tracking.rakutenLinkshare",
        "analytics.tracking.awin",
        "analytics.tracking.branch",
        "analytics.tracking.button",
        "analytics.tracking.rakutenAdvertising",
        "analytics.tracking.linkedIn",
        "analytics.tracking.drop",
        "analytics.tracking.iChannel",
        "analytics.tracking.responsys",
        "analytics.tracking.eBay",
        "analytics.tracking.oAUTH_WalmartHybrid",
        "analytics.tracking.teads",
        "analytics.tracking.onetag",
        "analytics.tracking.rtbHouse",
        "analytics.tracking.cision",
        "analytics.tracking.xandr",
        "analytics.tracking.adform",
        "analytics.tracking.attentiveMessaging",
        "analytics.tracking.quantcast"
    ],
    "SafeSearch": false,
    "StoreFront": "BE",
    "VipMembershipPurchased": false
}
```

### Products

**URL:** `https://storeapi.kobo.com/v1/products`

## Google analytics

This sections contains traffic about the following host: `https://ssl.google-analytics.com`. A lot of requests are being sent to this domain. A request looks as follows:

https://ssl.google-analytics.com/collect?v=1&tid=UA-6177406-38&cid=650d02c6-8b07-4790-890b-59b974762395&av=4.38.21908&an=nickel&sr=1072x1448&ul=en-us&t=screenview&cd=/WifiSettings

And is always paired with a similar request:

https://ssl.google-analytics.com/g/collect?v=2&tid=G-HKVPYM8786&cid=650d02c6-8b07-4790-890b-59b974762395&uid=44c43121-fd78-4295-93bf-bd47516e00d9&av=4.38.21908&an=nickel&_et=1&_z=ccd.v9b&sr=1072x1448&ul=en-us&en=page_view&dt=/WifiSettings

researching gives the following information:

* `G-HKVPYM8786` is a google tag id
* `UA-6177406-38` is a tracking id
* `650d02c6-8b07-4790-890b-59b974762395` is a client id.

The first request is always followed by a HTTP 204 code: Request is a success, but the client doesn't need to navigate to another page.


### Updated information on google analytics

Request analyzed:  
  
```https://ssl.google-analytics.com/collect?v=1&tid=UA-6177406-38&cid=650d02c6-8b07-4790-890b-59b974762395&av=4.38.21908&an=nickel&sr=1072x1448&ul=en-us&cd60&cd64=application/epub+zip&cd65=Sideloaded&cd72=application/epub+zip&t=event&ec=ReadingExperience&ea=LeaveContent&el=application/epub+zip```

```https://ssl.google-analytics.com/g/collect?v=2&tid=G-HKVPYM8786&cid=650d02c6-8b07-4790-890b-59b974762395&uid=44c43121-fd78-4295-93bf-bd47516e00d9&av=4.38.21908&an=nickel&_et=1&_z=ccd.v9b&sr=1072x1448&ul=en-us&ep.book_format=EPUB&ep.book_id=file:///mnt/onboard/books/A%20game%20of%20thrones%20--%20Martin,%20George%20R.%20R.%20--%20A%20game%20of%20thrones%201,%202011%20--%20Random%20House%20Publishing%20Group%20--%202c2480353292ac9eaaa4a468f92d1094%20--%20Anna%E2%80%99s%20Archive.epub&en=leave_content&ec=ReadingExperience```



1. **First Event:**
   - Endpoint: `https://ssl.google-analytics.com/collect`
   - Parameters: 
     - `v=1`: Version 1 of the Measurement Protocol.
     - `tid=UA-6177406-38`: Tracking ID for the Google Analytics property.
     - `cid=650d02c6-8b07-4790-890b-59b974762395`: Client ID.
     - `av=4.38.21908`: Application version.
     - `an=nickel`: Application name.
     - `sr=1072x1448`: Screen resolution.
     - `ul=en-us`: User language.
     - `cd60`: Custom dimension with an unspecified value.
     - `cd64=application/epub+zip`: Custom dimension specifying the book format as "application/epub+zip".
     - `cd65=Sideloaded`: Custom dimension indicating the source of the content as "Sideloaded".
     - `cd72=application/epub+zip`: Custom dimension specifying the book format again.
     - `t=event`: Hit type is an event.
     - `ec=ReadingExperience`: Event category.
     - `ea=LeaveContent`: Event action.
     - `el=application/epub+zip`: Event label.

2. **Second Event:**
   - Endpoint: `https://ssl.google-analytics.com/g/collect`
   - Parameters:
     - `v=2`: Version 2 of the Measurement Protocol.
     - `tid=G-HKVPYM8786`: Tracking ID for a different Google Analytics property.
     - `cid=650d02c6-8b07-4790-890b-59b974762395`: Client ID.
     - `uid=44c43121-fd78-4295-93bf-bd47516e00d9`: User ID.
     - `av=4.38.21908`: Application version.
     - `an=nickel`: Application name.
     - `_et=1`: Indicates an event hit (Engangement time).
     - `_z=ccd.v9b`: A parameter related to data collection -> unsure
     - `sr=1072x1448`: Screen resolution.
     - `ul=en-us`: User language.
     - `ep.book_format=EPUB`: parameter specifying the book format as "EPUB".
     - `ep.book_id`: parameter specifying the book ID.
     - `en=leave_content`: Event name.
     - `ec=ReadingExperience`: Event category.

**Comparison:**

- **Endpoint:** The endpoints differ, indicating that the events are sent to different Google Analytics properties.
- **Version:** The first event uses Version 1 of the Measurement Protocol, while the second event uses Google Analytics 4 protocol.
- **Custom Dimensions:** Both events utilize custom dimensions to provide additional context, such as book format and source of content.
- **Event Action and Label:** Despite slight differences in parameter names, both events capture the action of leaving content, specifically related to reading experiences.

> Interesting note: Version 1 measurement protocol will be fased out and obsolete in July 2024 

### Why the 1x1 GIF Response

https://stackoverflow.com/questions/6638504/why-serve-1x1-pixel-gif-web-bugs-data-at-all

### Sources google analytics

https://www.analyticsmarket.com/blog/how-google-analytics-collects-data/

https://support.google.com/analytics/answer/9964640?hl=en#zippy=%2Cin-this-article

https://developers.google.com/analytics/devguides/collection/protocol/ga4

https://developers.google.com/analytics/devguides/collection/protocol/v1

https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters