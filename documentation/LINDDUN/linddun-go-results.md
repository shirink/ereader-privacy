# Privacy threat modeling

## What is it?

Privacy threat modeling is a systematic approach to identifying and addressing potential privacy risks in a system or application. It involves analyzing the components, data flows, and potential vulnerabilities to assess how privacy might be compromised. The goal is to proactively design and implement measures to mitigate these threats and enhance overall privacy protection.

## LINDDUN

More information on LINDDUN: [click here](https://linddun.org/)

**Explanation**: In this document, you can find the results of applying LINDDUN GO (+ the privacy trees of LINDDUN PRO) to the information we have gathered so far on the privacy of Kobo Ereaders. Normally, LINDDUN has to be applied in a team setting but I did it alone, which means that it's not 100% correct. However, It shows that there is room for improvement regarding the privacy ecosystem on Kobo Ereaders.

You can find the LINDDUN GO cards on the website. Almost each card has an answer in this document. Some cards are very relevant in our case and some are not. The conclusions I made are based on a limited view of the system.

## Interesting cards

 * L2 - L4  
 * L3  
 * DD2  
 * U1  
 * Nc4  
 * Nc2  

# Cards

## L1

L.1.1

Elicitation questions:
* Yes, deviceID, IP address,...
* Yes, multiple identifiers like mentioned in the answer of the first question
* Yes, All the requests from the device 

Relevant risk? It is relevant, but I think this risk is something that is inherently part of the system. You cannot use a personal device without identifiers

## L2

L.2.2.3

Elicitation questions:
* Yes, each user has different reading habits and device usage habits.
* Not, really if I'm correct

Relevant risk? Yes, Especially data that does not really have clear attributes can be used to distinguish users.

## L3

L.2.1.1

Elicitation questions:
* Yes, the readings habits or titles of sideloaded books
* Yes, general device usage
* I think so, but I'm not sure about this question

Relevant risk? Yes, some requests contain properties that are unique to an individual. However, one could argue about the severity of those properties

## L4

L.2.2.1

Elicitation questions:
* Yes, similar to L2 but more relevant for this section
* Yes, there could be (holidays, reading hours, reading times, timestamp located in requests)

Relevant risk? Yes, very similar to L2. There are a lot of patterns that can be inferred from the collected analytics data.

## L5

Elicitation questions:
* *The answer to these questions are the same as the ones for L3*

Relevant risk? yes, the difference between L5 and L3 is in the fact that this data is definitely stored for some time, as it gets sent as a post request.

## I1

I.1.1

Elicitation questions:
* Not really as far as we know

Relevant risk? In my opinion not really 

## I2

I.2.3

Elicitation questions:
* Yes, but only when a user is authenticated on the device -> not applicable on a personal device in my opinion

Relevant risk? Not really, no tracking data is being sent to Kobo when a user is not authenticated -> users are always 'identified'. Not sure about this answer, I based it off the privacy trees.

## I3

I.2.2

Elicitation questions:
* No
* Yes, Information concerning side loaded books and files.

Relevant risk? Maybe, there is definitely a chance the user accidentally provides identifiable attributes

## I4

I.2.1.2
I.2.1.1

Elicitation questions:
* Yes, serialnumbers, x-kobo-deviceids,...
* Probably, depending on the request

Relevant risk? Although the elicitation questions pass, I'm not completely sure how relevant this is.

## I5

Elicitation questions:
* *The answer to these questions are the same as the ones for I4*

Relevant risk? Same as I4, the difference between I5 and I4 is that the hotspot here is storage, which we don't have a complete view on.

## Nr1

Nr.1.1

Elicitation questions:
* Probably, although I can't think of a situation in which this is relevant
* Depending on what we want to deny.

> maybe connecting to a corporate network?

Relevant risk? Probably not, although you could debate this

## Nr2

Nr.1.2

Elicitation questions:
* No
* Not relevant

Relevant risk? No

## Nr3

Nr.1.2

Elicitation questions:
* Not sure what they mean with this but I think not.
* It depends on the action but it probably does

Relevant risk? Probably not

## Nr4

Elicitation questions:
* *The answer to these questions are the same as the ones for Nr2*

Relevant risk? No

## Nr5

Nr.1.3
Nr.1.4

Elicitation questions:
* Yes, Some events have metadata about the event or even sideloaded books
* Not sure

Relevant risk? Probably not

## D1

D.3

Elicitation questions:
* *This should be tested but doesn't almost every system do this?*

Relevant risk? Probably not

## D2

D.1

Elicitation questions:
* Yes
* Not without knowledge on the system

Relevant risk? Probably not

## D3

D.1

Elicitation questions:
* Yes, opening books, accessing the store,....
* Yes, but some knowledge of the system is required

Relevant risk? Yes, potential sniffers could infer user actions based on network traffic.

## D4

D.3

Elicitation questions:
* Unsure but probably not
* /

Relevant risk? No

## DD1

DD.1

Elicitation questions:
* Yes, information on sideloaded books is not needed by Kobo
* Probably although you could debate about this
* No 

Relevant risk? Yes, Kobo doesn't need to send information regarding sideloaded books. Stopping this would already resolve a lot of problems regarding privacy.

## DD2

DD.2

Elicitation questions:
* I don't think so, but we don't know what the data is used for
* Same as question 1
* No

Relevant risk? Yes, The amount of tracking happening is probably not needed. For example: You can aggregate most of the data (for example: menu accessed x times, brightness always lower than x %)

However, this is debatable 

## DD3

Elicitation questions:
* As we are not sure on what kind of processing is happening, this question is difficult to answer

Relevant risk? Not enough information

## DD4

Elicitation questions:
* As we are not sure on how long data is stored, this question is difficult to answer

Relevant risk? Not enough information

## DD5

Elicitation questions:
* They don't contact 3rd parties beside google analytics

Relevant risk? Not really

## U1

U.1.1

Elicitation questions:
* Yes, the depth of the tracking that is happening is not communicated clearly enough with the user

Relevant risk? Yes, users should be aware of extensive the tracking is

## U2

U.1.2

Elicitation questions:
* There is no way to share personal data of other users

Relevant risk? No

## U3

U.2.1

Elicitation questions:
* No, but this should be studied further to be certain
* /

Relevant risk? Yes, but this should be tested

## U4

U.2.2

Elicitation questions:
* No, but this should be studied further to be certain
* /

Relevant risk? Yes, but this should be checked

## U5

U.2.3

Elicitation questions:
* No, but this should be studied further to be certain
* /

Relevant risk? Yes, but this should be checked

## Nc1

Nc.1.1.3.1

Elicitation questions:
* Not sure, should be checked
* For some of the data processing there seems to be way to withdraw consent
* Not sure what this means

Relevant risk? Yes, but maybe out of the scope of this thesis

## Nc2

Nc.1.1.3.2

Elicitation questions:
* Not sure about this
* Probably but not sure

Relevant risk? Yes, judging by the example given in the privacy threat trees, it is very relevant. However, I'm not sure if it is a risk.

## Nc3

Nc.1.1.3.2

Elicitation questions:
* As there is no automated decisions happening to our knowledge, we cannot answer this card correctly.

Relevant risk? No

## Nc4

Nc.1.1.2

Elicitation questions:
* Unsure, it depends on what exactly is necessary but it could be the case.

Relevant risk? Yes, judging by the card this is a relevant risk. However, more knowledge about the law and system is needed to accurately answer this card.

## Nc5

Nc.1.1.4

Elicitation questions:
* Unsure, it depends on why the data is needed

Relevant risk? Not enough knowledge to answer this

## Nc6

Elicitation questions:
* We cannot answer this card correctly without more knowledge about the underlying system.

Relevant risk? Not enough knowledge to answer this