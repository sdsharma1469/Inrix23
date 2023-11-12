# Inspiration 
Urban Utopia is fueled by the pressing challenges small businesses face in the United States, where over 50% of the 30.7 million enterprises succumb within their initial year (Oberlo). The Commercial Leasing industry's robust $244.3 billion revenue in 2022 underscores our potential impact on businesses in search of the ideal space. Emphasizing the pivotal role of location and business insights, our platform transcends traditional considerations. What distinguishes Urban Utopia are its distinctive features, powered by INREX APIs like speed segmenting and trade area trips. These tools enable users to dynamically assess area popularity and navigate the ever-changing landscape of parking availability—an indispensable factor for businesses. In a world where trends evolve daily, Urban Utopia equips users with real-time insights, ensuring each plot purchase is a strategic investment in a flourishing and dynamic community. Urban Utopia is more than a land listings website; it's a tool for urban pioneers seeking the perfect space. Whether you're envisioning business, or community project, let Urban Utopia guide you through the exciting journey of discovering and claiming your ideal urban plot.

# What It Does
Our platform meticulously curates a list of plot options in the specified area, each accompanied by insightful descriptions encompassing size, price, and unique features. Each plot option is accompanied by a detailed report, providing vital information such as parking availability, area popularity, and general details like price, size, and address. Users can leverage this information to make the most optimal decision about their life-changing investment. 

# How We Built It
Urban Utopia's backend is built with Flask and Python. We leveraged the Off-Street and On-Street Parking APIs for real-time data on available parking spaces near listed plots. We also used the Segment Speed API to provide insights into average car speeds and traffic congestion near the location. In addition to that, we used the Trade Area Trips API to get the number of trips that end in the area. These two APIs helped us analyze the popularity of the area. All of the data from these APIs along with some other details is then formatted into a user-friendly report. On the frontend, we use HTML, CSS, and JavaScript to build a practical and responsive website. 

# Challenges We Faced
1) Learning how to use and implement APIs.


2) Connecting the front end to the backend.
    Particularly calling the APIs in the front end after implementing it in the back end.

# Achievements
As a group of sophomore participants diving into our first hackathon, we're excited about successfully bringing our idea to life. Working with the INRIX APIs was a learning curve that provided us with practical insights. Navigating these APIs provided valuable insights into handling and manipulating real-time data. Overcoming challenges not only contributed to the project's success but also equipped us with skills we can carry forward. On the front end, we take pride in our design, ensuring it resonates with the main theme of our project.

# What We Learned 
Understanding and implementing Flask API
Integrating Front end and Back end 
Learnt and implemented Proxy API and Implementing API into websites 
Persevered in bypassing CORS
Parsing through large data 
Making the user experience more friendly  (Front end)

# What’s Next 
Looking ahead, Urban Utopia envisions scaling the project and fostering continuous development to offer an even more robust experience for users. A key strategy involves the incorporation of an expansive Real Estate API, amplifying plot options and diversifying choices for users. Furthermore, the roadmap includes leveraging machine learning to delve deeper into the decision-making process, analyzing additional features that influence plot selection. By harnessing advanced algorithms, we aim to provide users with nuanced insights, enhancing their ability to make informed decisions based on a comprehensive understanding of factors that impact the urban plot landscape. We could also add a map to the final report, adding a visual element and enhancing user experience.
