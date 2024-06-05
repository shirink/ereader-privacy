# Privacy settings

When the user changes the privacy settings, the "PrivacyPermissions" in their profile change. The profile of a user can be found on the following endpoint: `https://storeapi.kobo.com/v1/user/profile`. The "*PrivacyPermissions*" field is a list of permissions regarding the privacy settings. Each option in the privacy settings account page from Kobo corresponds to one or more privacy permissions.

The following shows what permissions are enabled when settings change:

## Option 1 Off

**Option Name:** Personalized Recommendations  
**Option Examples:**  
* Personalized book recommendations (Emails and Lists)

**Resulting PrivacyPermissions:**

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
        

## Option 2 Off

**Option Name:** Performance/Analytics  
**Option Examples:**  
* Click tracking
* A/B testing
* Product usage analytics

**Resulting PrivacyPermissions:**


        "feature.recommendation",
        "analytics.tracking",
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
        
## Option 3 Off

**Option Name:** Third Party Analytics & Personalization  
**Option Examples:**  
* Pixel tracking
* Ad retargeting
* Social tracking

**Resulting PrivacyPermissions:**

        "feature.recommendation",
        "analytics.user",
        "analytics.platform.features",
        "analytics.catalog",
        "analytics.platform.crashreporting",
        "analytics.platform.AB",
        "readingstats.social",
        "analytics.tracking.campaigns",
        "analytics.tracking.googleAnalytics",
        "analytics.tracking.googleTagManager",
        "analytics.tracking.maxymiser",
        "analytics.tracking.crashlytics",
        "analytics.tracking.hotjar",
        "analytics.tracking.firebase"
        

## No settings off

**Resulting PrivacyPermissions:**

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
