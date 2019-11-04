# FloodGate
Welcome to FloodGate, a fully functional, responsive, natural disaster early-warning & detection web app dedicated to enabling communities, first-responders, and local governments in times of crisis.

## Inspiration
Today's world increasingly interacts with natural disasters and climate phenomena, in large part caused by anthropomorphic global warming, For many of us, not only in the US but also around the world, access to definitive pipelines for connections and educational resources is severely lacking, and thus FloodGate provides a streamlined path to help the students, community leaders, and people of the future get a headstart.

## What it does
FloodGate has several functions. The SMS notification system provides persons in need with easy, reliable, and secure access to responders and volunteers, and its intended purpose is to help users identify key events established during the path of a natural disaster so they can make more informed decisions and gain vital contact/rescue information. FloodGate also implements an autonomous, remote, and cheap sensing device, built with multiple contact functionalities and messaging services. This is all compiled into an accessible, user-friendly website which includes resources to heatmaps and real-time models of natural disasters.

## How I built it
### Twilio API (SMS), Google Maps (GCP), Flask, and Ngrok
FloodGate's creation required building and utilizing functional RESTful APIs and packages to create a responsive site. The site is styled via Python's Flask library. The backend server is supported by Ngrok, providing localhost access to webhooks. The SMS ping system is backed entirely by Twilio's Programmable SMS API, providing FloodGate users and first-responders with RESTful, real-time notifications. We also use Firebase's Cloud Firestore database service to host our sensor and SMS data (with SQLite3 as an offline backup) and GCP's Google Maps Platform to display location-based data on interactive maps.

### Arduino, C, Python, Matplotlib, and a whole lot of Solder
The FloodGate sensor is built using an Arduino 101 and Ultrasonic Distance Module HR-S04 using the established Arduino IDE and C. Serial data is handling via Python's PySerial library.

## Challenges I ran into
**FloodGate was my first time making an actual project on Arduino, and I've never used Flask before**. In the process of making the site, I ran into several production issues with Ngrok. Additionally, I encountered difficulties connecting to the development server on several instances, and the Twilio versioning proved challenging for the back-end.

## Accomplishments that I'm proud of
I'm amazed that I was able to complete FloodGate over such a small duration, especially considering my lack of experience with Flask and Arduino. I faced many set-backs with the site interface, so ultimately having a working version of the site pushed into production was extremely fulfilling.

## What I learned
Coming into this project as a Flask novice, I had absolutely no experience with anything related to the Twilio API, and minimal experience with Ngrok servers and design. However, I managed to bridge this gap by constantly pushing myself to learn more about C, poring over documentation, and seeking help when needed on StackOverflow and Google. Ultimately, I needed to think and rethink the overall coding process, and finding that common ground and challenging myself to truly understand code instead of haphazardly copying it from forum pages really allowed me to progress. I was also able to experiment with new technologies such as Cloud Firestore, SQLite3, Ngrok, and others.

## What's next for FloodGate
I hope to expand the site into a fully integrated site complete with enhanced user experiences and design. I'm also actively pushing myself to create an iOS app for FloodGate, which I hope to push into production soon! Stay tuned for more updates!

## Awards
### HackDuke 2019 - Best Use of Twilio Award [MLH]
### HackDuke 2019 - Wolfram Award

Made with ❤ in 2019
