# DESCRIPTION

Our project is called STARBASE, a fictional space company that investigates and observes stars. Our idea for this project was to have a way to collect data and showcase it in an unconventional way through a game.
As a new employee, your job is done all in the office. At the end of every day, you are given data from the astronauts, and you have to figure out which star systems they went to. You are given the star's colour, its distance in light years from earth, the magnitude of their brightness and which constellation they are part of. Space explorations are hard, and astronauts return with limited information about the celestial body they visit. So using the information you’re given, you need to go search through the STARDEX to find which stars match the information that the astronaut provides you. 

# INSPIRATION

Our project had a few inspirations. The visual and aesthetic inspiration comes from the game Lethal Company, where we wanted to create a terminal like the one in the game:

<img width="825" height="464" alt="image1" src="https://github.com/user-attachments/assets/092c05bb-4e94-476f-8ef3-2b58e6ee1f3a" />

We actually opened the game and played around to get more ideas from it. Initially, we also wanted to have some of the same mechanics, like a scanning function. In lethal company, you can scan your surroundings, and you'll receive data that tells you what you're looking at. We wanted to create something similar where you could scan whatever star you're looking at, and it will give you information on it, but not all the information is available. But we felt that would be a really hard mechanic and too much to accomplish with the time we had, so we kept the information part, where you're given a dataset, and some of the information in the dataset is redacted. 

Another point of inspiration came from the game Krillion, where you are asked questions and have to give answers. The more niche your answer is, the better. Obviously we did not take the same mechanic, but the question and answer format is what inspired us for the input aspect of our project. 

# PROCESS

We also talked through a lot of different iterations of the game. At first we created a whole story behind STARBASE to give it a little more life, but with time constraints and for the sake of simplicity, we just went with a terminal program. At first, we wanted to use both the space catalog API, as well as the NASA images API. Together, when a user searches for a specific star, we want to have an image of that star displayed on the page from the NASA images API, and have both of them communicate to display something on the page. But with the terminal functionality, we felt that that didn't really fit with the idea. 

Overall, we had a lot of fun creating this project because we went with a theme that unconventionally reflected the reading in a way that isn't necessarily positive or negative. We usually tend to see data retention and usage in a bad way, so it was our way of showing how you can use data in a way that isn't bad.

# RELATION TO THE READINGS

## A Sea of Data: Apophenia and Pattern (Mis-)Recognition

In this reading, Steyerl talks about how we try to find patterns and meaning in large amounts of data, specifically when she discusses apophenia, which is when we start seeing connections or patterns in information that might not even be there.

We connected this reading to STARBASE because the main idea of the game is to identify stars by finding patterns in the information given to the players. For example, players have to look through the STARDEX to find stars that have similar properties to the one assigned to them, compare the information, and try to recognize patterns that will help them figure out which star they're looking for.

In addition, Steyerl discusses the concept of separating signal and noise. Especially in an era where we constantly bombarded with information, whether it is ads, or social media posts, our brains have began to adapt to filter out what information is considered important or as Steyerl discusses, what information is recognized as signal. In our game, this concept of signal versus noise manifests itself in the way players filter through the star data in STARDEX and try to ignore the noise and find the signal which is the star they are searching for to complete their assignment. We originally didn't intend for this outcome with the game but it became apparent that as we played, the other stars became unimportant compared to the star we were actually searching for and that made us realize how much the importance of a piece of data relies in the hands of the people using said data.

## The Point of Collection

In this text, Onuoha discusses how data is affected by the way it is collected. Which means, the information that ends up in a dataset depends on what people choose to collect, how they collect it, and what they decide to include or leave out.

This relates to STARBASE because the game uses information from an external API, and although we didn't create or collect all this data ourselves, we decided which data was worth displaying by filtering and reorganizing it before presenting it to the player.

For instance, we created categories for star colours, distances, and brightness instead of displaying only the raw numerical values that were available in the API. This was done to not only make it easier for users to search for stars in the STARDEX but also make the the data more readable for a regular person who might not be familiar with astronomy terms. This means we're making decisions about how the information is presented and how players are expected to understand it.

# SCREENSHOTS
<img width="472" height="645" alt="image" src="https://github.com/user-attachments/assets/6e985be7-f299-4c04-ba4e-3511c4693800" />

*Figure 1. Screenshot of Spacecatalog API Object. The values framed in red were the ones used to determine the star categories* 

<img width="1669" height="998" alt="Screenshot 2026-11-16 at 3 15 40 PM" src="https://github.com/user-attachments/assets/c481bc32-f22e-44c2-95ca-faa6501538d6" />

*Figure 2. The STARBASE main menu.*

<img width="503" height="120" alt="Screenshot 2026-11-16 at 3 16 02 PM" src="https://github.com/user-attachments/assets/1f3e495f-460a-45df-8728-68d703c3daa9" />

*Figure 3. The STARBASE main menu.*

<img width="572" height="687" alt="Screenshot 2026-11-16 at 3 12 44 PM" src="https://github.com/user-attachments/assets/3d3368e9-31d1-4508-b887-dd38d3034b91" />

*Figure 4. The STARBASE main menu.*

<img width="503" height="460" alt="Screenshot 2026-11-16 at 3 14 59 PM" src="https://github.com/user-attachments/assets/6203dc61-7145-4fc6-889b-8ab52cbc4156" />

*Figure 5. The STARBASE main menu.*

<img width="1668" height="993" alt="Screenshot 2026-11-16 at 3 15 23 PM" src="https://github.com/user-attachments/assets/3ea58926-023a-409d-8e1d-98c6d875997a" />

*Figure 6. The STARBASE main menu.*
