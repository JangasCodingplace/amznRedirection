# Readme - EN

## Project
The goal is to create an Amazon Deeplink application.

Our customers enter their Amazon partner countries in our application. The link is stored on our systems and the customers receive a new link which they can distribute via social media. 
When users click on this link, they are redirected to the Amazon product page via our service.
If this is done via a mobile device (iPhone, Android mobile, iPad, Android tablet), the user should be redirected to the product page in the mobile app.
If he has not installed the app, he should be redirected to the product page on the web.
**The user should not be redirected to the Appstore or Playstore**

You can log in for a demo:
**URL:** https://link-to-app.de/admin/
**User:** demo
**Password:** hallo12345

**The user name is Case Sensitive**


## Project Requirements
The application is programmed on the server side in Python Django. In the frontend only HTML / CSS & JS should be used. **No jQuery**!

The code is not functional. There are only relevant snippets. There are basically all possibilities that are given in PHP, R or other languages. You can set & evaluate cookies on the server side.

A competent consultation is also a good assistance.


## Trys & Fails
- Redirection via iFrame is outdated and won't work!
- Android Link via direct serverside Redirection is not working. But here is my Try: 
```
intent://#Intent;package=com.amazon.mShop.android.shopping;scheme=com.amazon.mobile.shopping.web://{{PRODUCT_LINK}};S.browser_fallback_url={{https://PRODUCT_WEB_URL}}/;end
```
For modern Androids the Playstore was opened

Other Trys are in iOS Versions. The current Android Version is simular to iOS Version 1
