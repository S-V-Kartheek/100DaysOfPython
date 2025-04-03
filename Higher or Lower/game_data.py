data = [
    # Social Media Platforms
    {'name': 'Instagram', 'follower_count': 685, 'description': 'Social media platform', 'country': 'United States'},

    # Footballers
    {'name': 'Cristiano Ronaldo', 'follower_count': 649, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Lionel Messi', 'follower_count': 505, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Neymar Jr.', 'follower_count': 228, 'description': 'Footballer', 'country': 'Brazil'},

    # Indian Cricketers
    {'name': 'Virat Kohli', 'follower_count': 270, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Sachin Tendulkar', 'follower_count': 45, 'description': 'Cricket legend', 'country': 'India'},
    {'name': 'MS Dhoni', 'follower_count': 45, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Rohit Sharma', 'follower_count': 30, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'KL Rahul', 'follower_count': 18, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Hardik Pandya', 'follower_count': 25, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Ravindra Jadeja', 'follower_count': 10, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Shubman Gill', 'follower_count': 12, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Rishabh Pant', 'follower_count': 11, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Suryakumar Yadav', 'follower_count': 8, 'description': 'Cricketer', 'country': 'India'},

    # Indian Athletes
    {'name': 'Neeraj Chopra', 'follower_count': 7, 'description': 'Javelin Thrower', 'country': 'India'},
    {'name': 'PV Sindhu', 'follower_count': 5, 'description': 'Badminton Player', 'country': 'India'},
    {'name': 'Saina Nehwal', 'follower_count': 4, 'description': 'Badminton Player', 'country': 'India'},
    {'name': 'Mary Kom', 'follower_count': 3, 'description': 'Boxer', 'country': 'India'},

    # CEOs (India & Global)
    {'name': 'Elon Musk', 'follower_count': 320, 'description': 'CEO of Tesla, SpaceX', 'country': 'United States'},
    {'name': 'Sundar Pichai', 'follower_count': 2, 'description': 'CEO of Google', 'country': 'India'},
    {'name': 'Satya Nadella', 'follower_count': 1.5, 'description': 'CEO of Microsoft', 'country': 'India'},
    {'name': 'Mukesh Ambani', 'follower_count': 1, 'description': 'Chairman of Reliance Industries',
     'country': 'India'},
    {'name': 'Narayana Murthy', 'follower_count': 0.5, 'description': 'Co-founder of Infosys', 'country': 'India'},
    {'name': 'Ratan Tata', 'follower_count': 10, 'description': 'Former Chairman of Tata Group', 'country': 'India'},

    # Bollywood & Indian Celebrities
    {'name': 'Shah Rukh Khan', 'follower_count': 47, 'description': 'Actor', 'country': 'India'},
    {'name': 'Salman Khan', 'follower_count': 55, 'description': 'Actor', 'country': 'India'},
    {'name': 'Amitabh Bachchan', 'follower_count': 35, 'description': 'Actor', 'country': 'India'},
    {'name': 'Alia Bhatt', 'follower_count': 80, 'description': 'Actress', 'country': 'India'},
    {'name': 'Deepika Padukone', 'follower_count': 75, 'description': 'Actress', 'country': 'India'},
    {'name': 'Priyanka Chopra', 'follower_count': 90, 'description': 'Actress', 'country': 'India'},

    # YouTube Stars (Global & Indian)
    {'name': 'MrBeast', 'follower_count': 160, 'description': 'YouTuber', 'country': 'United States'},
    {'name': 'PewDiePie', 'follower_count': 110, 'description': 'YouTuber', 'country': 'Sweden'},
    {'name': 'CarryMinati', 'follower_count': 40, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Ashish Chanchlani', 'follower_count': 30, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Bhuvan Bam', 'follower_count': 25, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Gaurav Taneja (Flying Beast)', 'follower_count': 12, 'description': 'YouTuber', 'country': 'India'},

    # Companies with High Followers
    {'name': 'Nike', 'follower_count': 330, 'description': 'Sports brand', 'country': 'United States'},
    {'name': 'Adidas', 'follower_count': 120, 'description': 'Sports brand', 'country': 'Germany'},
    {'name': 'Samsung', 'follower_count': 80, 'description': 'Tech brand', 'country': 'South Korea'},
    {'name': 'Apple', 'follower_count': 110, 'description': 'Tech brand', 'country': 'United States'},
    {'name': 'Reliance Jio', 'follower_count': 20, 'description': 'Telecom', 'country': 'India'},
    {'name': 'Tata Motors', 'follower_count': 10, 'description': 'Automobile company', 'country': 'India'},

    # Global Celebrities
    {'name': 'Selena Gomez', 'follower_count': 422, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Ariana Grande', 'follower_count': 377, 'description': 'Musician and actress', 'country': 'United States'},
    {'name': 'Dwayne Johnson', 'follower_count': 395, 'description': 'Actor and wrestler', 'country': 'United States'},
    {'name': 'Beyoncé', 'follower_count': 313, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Taylor Swift', 'follower_count': 283, 'description': 'Musician', 'country': 'United States'},
    {'name': 'Rihanna', 'follower_count': 180, 'description': 'Musician and businesswoman', 'country': 'Barbados'},

    # Additional Influential Figures
    {'name': 'Narendra Modi', 'follower_count': 80, 'description': 'Prime Minister of India', 'country': 'India'},
    {'name': 'Barack Obama', 'follower_count': 100, 'description': 'Former US President', 'country': 'United States'},
    {'name': 'Bill Gates', 'follower_count': 50, 'description': 'Founder of Microsoft', 'country': 'United States'},
    {'name': 'Jeff Bezos', 'follower_count': 20, 'description': 'Founder of Amazon', 'country': 'United States'}
]
