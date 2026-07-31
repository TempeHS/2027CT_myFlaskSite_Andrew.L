# Website Name

| Field                          | Detail |
| ------------------------------ | ------ |
| **Website Title**              | MediON     |
| **Student Name(s)**            |   Andrew Yong Ly     |
| **Class / Course**             |     Year 9 Computer Technology   |
| **Repository**                 |    2027CT_myFlaskSite_Andrew.L    |
| **Live Site / Codespaces URL** |    https://musical-space-train-gxrvj646wwp29pwv.github.dev/    |
| **Date**                       |  31/7/26      |

> Your website is the main piece of work. This README is short on purpose — it
> points a reader to your **2-minute walkthrough** and gives an honest
> **evaluation of what you delivered**.

---

## 1. Overview

**Purpose:** <!-- One or two sentences: what the site is and why it exists (from your Statement of Intent). --> MediON is a gaming and entertainment website, meant for showcasing some of the biggest and more niche articles that the mainstream media might have missed. This site acts as a source hub for the latest movie and gaming articles of the week, with a short summary on the matter and links that lead to other websites that talk about the matter.

**Target audience:** This website is meant for gaming and movie enthusiasts of all ages, who want to stay up to date with the latest news.

**Technology stack:** Python Flask · Jinja2 templates · Bootstrap (CDN) · custom CSS · pytest

---

## 2. Walkthrough Video (2 minutes)

This is the most important part of your documentation — it shows your website running.

<!--
  Embed a ~2 minute walkthrough. Replace VIDEO_ID with your YouTube video ID:
  [![Website Walkthrough](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

  OR link a screen recording stored in the repository:
  [Watch the Walkthrough](./docs/walkthrough.mp4)
-->

| Field            | Detail |
| ---------------- | ------ |
| **Link / Embed** |        |
| **Duration**     |        |

**Your walkthrough should show:**

- A tour of each page (Home and Contact)
- Your key Bootstrap components working (navbar, carousel, cards, map, form)
- The layout responding when the window is resized (navbar collapsing to a hamburger)

---

## 3. Evaluation — Did You Deliver Your Statement of Intent?

This is the most important written part of your documentation. Evaluate the
website you **delivered** against the **Statement of Intent** you wrote during
planning. Be honest and use evidence — point to a page, a feature or a test.

Overall, I would say that I delivered a sufficient amount from what I stated in my statement of Intent. As previously, I had mentioned how I would create article pages by weekly gaming and movie news; this feature is prominent in my website, as a nav bar is used to showcase how the user can go back into certain weeks in order to view a certain article from prior weeks. In my article pages, there's also a brief summary (~100-200 word description) on the topic. There is also article links at the bottom of each page that redirects the user to more information about the matter.

However, there was some features in which I was not able to succesfully do. An example is making at least 10 article cards per week about the latest movie and gaming news. I was only able to make 9 working pages on the matter, as a few of the pages were not yet completed and had a red square to indicate it.

### 3.1 Your Statement of Intent

What is the website?
MediON is a gaming and entertainment website, meant for game and movie enthusiasts
of all ages. This site will act as a source hub for weekly information, pumping out 10-20 of
the latest gaming & movie news that the previous week offers; serving as a bridge for
curious viewers to easily access heaps of summarised information in only one site.
Similarly to IGN and other media outlets, MediON will consist of only the most reliable
images of a topic, alongside a brief 100-200 word description on the matter, and more links
to trustworthy articles gathered by me. Examples of article headlines, like: "New
Spider-Verse movie release date change!" or "New leaks for an upcoming game releasing
this year!" will be featured on this site.

Why is it needed?
Currently, if a viewer wants to gather information about a certain topic or idea, they look it
up through a search engine like Google. In the process of this, they end up missing other
information in the media space, like a new movie releasing or an indie game coming out.
This kills any possible hype for a release or an event, due to the topic being too small for
word to travel through and reducing the creator’s hype onto their independent
game/movie. Understanding how information from gaming & movie articles move across
the web, from a user's perspective, is the key to understanding what users want and don't
want.

How will it help?
By creating 'MediON', we essentially bridge the gap between small projects (indie games,
small movies), into the mainstream media. This website will not only build-up hype for
different games across different genres and movies, but will also support smaller indie
devs and film studios that might've not been picked up by the larger media outlets.
Ensuring that a wide range of topics across the media is covered weekly, will allow all
kinds of information to expand across every part of the web.

Who is it for?
This website is mainly catered towards interested viewers, wanting to look for more than
just information on their certain game or movie. And wanting to expand their interests from
one game/movie title into even more titles. This will not only nurture the user’s hobby and
interest, but possibly even allow more people to become interested in multiple titles.

Summary and expected impact.
MediON will not only bridge the gap between movie and game enthusiasts, but also
nurture their interests too. With the website hopefully becoming frequently used each
week, with users coming back, due to their sheer interest in the weekly news of the gaming
and movie space. This will not only enhance the viewer’s knowledge of a certain topic, but
also allow them to support themes or titles they choose to. This outcome will be achieved,
through daily modifying, including spending most of my days tweaking the UI layout and
the coding aspect of the site.

### 3.2 What You Delivered

| Page    | Route      | What it delivers |
| ------- | ---------- | ---------------- |
| Home    | `/`        |  A homepage that is the very first thing that the viewer sees. It acts as a hub that leads to the hottest articles of the week, alongside the gaming and movie week articles in the form of article cards.                |
| Contact | `/contact` | A page that allows people to send messages to the creator (me), in the form of putting in their email and sending a message or subject.                 |
| Gaming Week 1 | `/gaming1` | A page that allows viewers to access article pages based on gaming news in the form of article cards, alongside with a mini-nav bar that allows the user to change the week they're viewing.                 |
| Movie Week 1 | `/movie1` | It uses the same design as the Gaming Week 1 page, although it showcases movie article cards and allows the user to go forward or back in weeks.                 |
| Gaming Week 2 | `/gaming2` | A page that is connected through the mini-nav bar of Gaming Week 1, which showcases more article cards based on the specified week (E.G. 27/7/26).                  |
| Movie Week 2 | `/movie2` | Connected through the Movie Week 1's mini-nav bar at the top, which also showcases the specified article pages.                 |
| Game Article 1 | `/gamearticle1` | The game articles have a brief description of a topic, alongside an image and where the image was found. At the very end of the page, there is also links that lead to the same topic but from different websites.             |
| Game Article 2 | `/gamearticle2` |(All have the same function as Movie article 1)                  | (All have the same function as Game Article 1)
| Game Article 3 | `/gamearticle3` |(All have the same function as Movie article 1)                  | (All have the same function as Game Article 1)
| Game Article 4 | `/gamearticle4` |(All have the same function as Movie article 1)                  | (All have the same function as Game Article 1)
| Movie Article 1 | `/moviearticle1` |  The movie articles have a brief description of a topic, alongside an image and where the image was found. At the very end of the page, there is also links that lead to the same topic but from different websites.                 |
| Movie Article 2 | `/moviearticle2` |(All have the same function as Movie article 1)                  | 
| Movie Article 3 | `/moviearticle3` |(All have the same function as Movie article 1)                  | 
| Movie Article 5 | `/moviearticle5` |(All have the same function as Movie article 1)                  |
| Movie Article 6 | `/moviearticle6` |(All have the same function as Movie article 1)                  | 

### 3.3 Evaluation Against Your Intent (2–3 paragraphs)

Overall, I have fulfilled most of my goals as stated in the Statement of Intent but underachieved concerning the quantity. MediON is a weekly destination for gaming and movie news that summarises the information, making it easier for the inquisitive viewer to read. It can be seen in my final website because the second navigation bar on the gaming and movie pages allows one to go through 'week 1' and 'week 2' to get back to previous articles. Every card has an image, a title, and a brief description (the Wolverine trailer and Dewdrop Dynasty are just some examples), with a 'learn more' button at the bottom leading to an external, more detailed resource, which follows my Statement of Intent, which states that MediON should be a bridge, summarising the main points but not substituting the primary sources.

Concerning the overachievement, I have not reached the quantity goal. I intended to have 10-20 articles per week, but I only managed to create 9 cards by the deadline, with a few more left unfinished, which is evident by the red square placeholder instead of a card. It reflects my process pretty much because I spent most of the time fixing structural issues, such as improperly placed div tags, or making minor adjustments to images, buttons, and icons. Therefore, I did not have enough time to research and write more cards to meet the quantity goal. My final website does not fully represent the idea of having heaps of information in one place from the Statement of Intent because, although I have implemented the bridging between MediON and the external resources, there is still not enough variety in topics as I only managed to publish 9 cards. It does not yet show enough potential to bridge the gap between small indies and big companies by featuring both the triple A game Wolverine and the indie Metroidvania Dewdrop Dynasty.

Regarding the audience and impact, MediON has fulfilled the intended impact because, on the website, the Dewdrop Dynasty indie Metroidvania and Wolverine have the same visual presentation, which means that both are prioritised and equally noticeable. This reflects my intent to impact the indie gaming industry by promoting smaller games/studios that bigger companies might ignore. Although I did not reach the quantity goal of 10-20 articles/features, the basic structure is created, so one could easily add more if needed. Thus, in terms of impact, it is fuffiled by being able to make smaller games and movies more noticeable and less dependent on big companies’ coverage. About the audience, I have not fully met the goal because it would take much longer to reach the quantity goal of 10-20. However, I have done everything necessary for the intended effect to take place, as the structure is already there, and a few more articles would impact the indie gaming industry as intended.

### 3.4 Overall Effectiveness (1–2 paragraphs)

> Step back from the detail. Overall, **how effective** is the website at
> achieving its purpose for its target audience? Weigh what works against what
> falls short, and state what you would improve to better meet your intent.

In my opinion, I'd say that my website was pretty effective in delivering and achieving its purpose for the target audience. This is due to how I had added some indie articles, alongside articles with big titles, which is a nice even mix of topics. This allows people to find new content that they have never seen before and possibly find a new game they will want to watch or buy. However, I'd say that I don't have a large amount of article cards for viewers to truly see more of the niche games or movies, as I currently have less than 10 article cards inside my website. This is something I would very much improve on to meet my intent at the start, in order to fully make a bridge between indie content and mainstream content.

---

## 4. Acknowledgements

> List anything you did not make yourself — tutorials, images, fonts, icons and
> libraries. Using content without acknowledgement may constitute academic
> misconduct.

| What you used | Source / Creator | Licence | What you used it for   |
| ------------- | ---------------- | ------- | ---------------------- |
| Bootstrap     | Bootstrap team   | MIT     | Layout and components  |
| Flask         | Pallets Projects | BSD     | Web server and routing |
| Heroicons              | tailwindlabs                 | MIT        | icons on my nav bar                       |
| Lato font (google fonts)              | Łukasz Dziedzic     | SIL open font         | Consistent font throughout the website                       |
| Hero images              | Multiple companies    | Fair Use       | Images for articles                  |

---

> **Student Declaration:** All work submitted is my own except where explicitly acknowledged above.
