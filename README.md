# Thesis e-readers

This repository is for my thesis: Am I Leaking While I am Reading?
Analyzing the Collection and Sharing of User Data on Kobo E-Readers

It contains the following:

* documentation: Contains explanation files regarding results. The file `intercepting-approach.md` contains the steps to intercept traffic on Kobo e-readers.
* traffic files: Traffic files in mitm-proxy format and HAR format
* event analyzer: Script to work with JSON files sent to `https://storeapi.kobo.com/v1/analytics/event`

## Potential Related Work (Will be periodically updated)

* [Amazon Echo Dot or the Reverberating Secrets of IoT Devices](https://dl.acm.org/doi/10.1145/3448300.3467820)
  * This paper talks about the security risks of physical hack of a device: back-quote from Abstract: _"Wi-Fi credentials, the physical location of (previous) owners, and cyber-physical devices (e.g., cameras, door locks). We show that such information, including all previous passwords and tokens, remains on the flash memory, even after a factory reset."_
* [Tracking, Profiling, and Ad Targeting in the Alexa Echo Smart Speaker Ecosystem](https://dl.acm.org/doi/10.1145/3618257.3624803)
  * Interesting thing about this paper, is that instead of looking for trackers in the traffic, they tried to verify whether there is a change in advertisement a user gets based on their interaction with smart voice assistant (cf Ref "[ 24, 59, 60 ] "). It's a nice black box method of searching for tracking (vs. intercepting the traffic)
* [Buddy’s wearable is not your buddy: privacy implications of pet wearables]()
* [Transparency in the consumer Internet of Things](https://iot-transparency.org/Transparency%20in%20the%20consumer%20Internet%20of%20Things_files/iot-transparency.pdf)
  * Very interesting report from Oxford university, similar to e-reader research. Analyzed several popular CIoT devices and also exercised data access right (can be replicated in ereader thesis).
* On HAR:
  * [TrackHAR](https://github.com/tweaselORG/TrackHAR) A library for searching for tracking in HAR files. A quick look, and it seems that it's main advantage is that it already does some of the possible decodings that might happen (like checking for base64 encoded values and it decode them)
