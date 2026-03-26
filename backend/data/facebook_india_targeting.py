"""
REAL Meta Ads (Facebook) interest categories, behaviors, and demographics
sourced from Meta Ads Manager targeting database for India.
These are actual targetable interests and behaviors available in Meta Ads Manager.
"""

# ─────────────────────────────────────────────
# REAL META INTEREST CATEGORIES (India-relevant, from Meta's actual database)
# ─────────────────────────────────────────────
REAL_META_INTERESTS = {
    "E-commerce & Shopping Platforms": [
        "Myntra", "Flipkart", "Amazon India", "Meesho", "Nykaa", "AJIO",
        "Snapdeal", "Tata CLiQ", "Reliance Digital", "Croma",
        "BigBasket", "JioMart", "Blinkit", "Swiggy Instamart",
        "Online shopping", "Engaged shoppers"
    ],
    "Fashion & Apparel Brands (India)": [
        "Fabindia", "W for Woman", "Biba", "Manyavar", "Mohey",
        "Peter England", "Van Heusen", "Allen Solly", "Louis Philippe",
        "Raymond (company)", "Zara", "H&M", "Levi's", "Roadster",
        "Puma", "Nike", "Adidas", "Reebok", "Skechers", "Bata India",
        "Libas", "Aurelia", "Global Desi", "Pantaloons"
    ],
    "Beauty & Personal Care Brands (India)": [
        "Nykaa", "Lakmé", "Sugar Cosmetics", "Mamaearth", "WOW Skin Science",
        "Minimalist (skincare)", "Pilgrim", "Plum", "The Moms Co.",
        "mCaffeine", "Biotique", "Himalaya Drug Company",
        "L'Oréal Paris", "Maybelline New York", "Neutrogena",
        "Kama Ayurveda", "Forest Essentials", "Dot & Key",
        "Nivea", "Dove (toiletries)", "Vaseline", "Pond's",
        "Skincare", "Cosmetics", "Cruelty-free cosmetics"
    ],
    "Health & Fitness": [
        "Cult.fit", "HealthifyMe", "Yoga", "Pilates",
        "Gym", "CrossFit", "Running", "Marathon",
        "Protein supplement", "Muscleblaze", "Optimum Nutrition",
        "Ayurveda", "Patanjali Ayurved", "Organic food",
        "Intermittent fasting", "Weight loss", "HIIT",
        "Decathlon", "Sports",  "Cycling", "Zumba"
    ],
    "Food Delivery & Dining": [
        "Swiggy", "Zomato", "Dunzo", "EatSure",
        "Domino's Pizza", "McDonald's", "KFC", "Pizza Hut",
        "Starbucks", "Chaayos", "Café Coffee Day",
        "Barbeque Nation", "Haldiram's", "MTR Foods",
        "Eating out", "Food delivery", "Indian cuisine",
        "Street food", "Vegetarian food", "Baking"
    ],
    "Entertainment & OTT": [
        "Netflix", "Amazon Prime Video", "Disney+ Hotstar", "JioCinema",
        "SonyLIV", "MX Player", "ZEE5", "Alt Balaji",
        "Bollywood", "Shah Rukh Khan", "Salman Khan", "Alia Bhatt",
        "Ranveer Singh", "Deepika Padukone", "Akshay Kumar",
        "Hrithik Roshan", "Kartik Aaryan", "Sara Ali Khan",
        "Indian cinema", "Tollywood", "Kollywood",
        "Hindi music", "Arijit Singh", "Jubin Nautiyal",
        "Spotify", "JioSaavn", "YouTube", "Instagram Reels"
    ],
    "Cricket & Sports (India)": [
        "Indian Premier League", "Cricket", "Virat Kohli",
        "MS Dhoni", "Rohit Sharma", "Sachin Tendulkar",
        "Hardik Pandya", "KL Rahul", "Jasprit Bumrah",
        "Team India", "Mumbai Indians", "Chennai Super Kings",
        "Royal Challengers Bangalore", "Kolkata Knight Riders",
        "Kabaddi", "Pro Kabaddi League", "ISL (Indian Super League)",
        "Badminton", "PV Sindhu", "Neeraj Chopra",
        "WWE", "Football", "FIFA World Cup"
    ],
    "Finance & Investment": [
        "Zerodha", "Groww", "Upstox", "Angel One", "5paisa",
        "PhonePe", "Google Pay", "Paytm", "BHIM",
        "Mutual fund", "Stock market", "Systematic investment plan",
        "Personal finance", "HDFC Bank", "ICICI Bank", "SBI",
        "Axis Bank", "Kotak Mahindra Bank", "LIC of India",
        "Gold investment", "Real estate", "Cryptocurrency",
        "Entrepreneurship", "Small business", "Startup"
    ],
    "Education & EdTech": [
        "BYJU'S", "Unacademy", "Vedantu", "upGrad", "Coursera",
        "NPTEL", "Khan Academy", "WhiteHat Jr", "Toppr",
        "IIT JEE", "NEET", "UPSC", "SSC", "CAT (exam)",
        "MBA", "B.Tech", "Distance education",
        "English language learning", "Coding", "Python (programming language)",
        "Digital marketing", "Graphic design"
    ],
    "Travel (India)": [
        "MakeMyTrip", "Goibibo", "EaseMyTrip", "IRCTC",
        "OYO", "Airbnb", "Treebo Hotels", "Fab Hotels",
        "Goa", "Rajasthan", "Kerala", "Himachal Pradesh",
        "Uttarakhand", "Manali", "Shimla", "Rishikesh",
        "Char Dham", "Varanasi", "Amritsar",
        "Budget travel", "Backpacking", "Luxury travel", "Honeymoon"
    ],
    "Parenting & Baby (India)": [
        "FirstCry", "Hopscotch", "BabyChakra", "Mothercare",
        "Johnson's baby", "Pampers", "Huggies",
        "Parenting", "Mommies", "New mothers",
        "School admission", "CBSE", "Montessori education",
        "Organic baby food", "Breastfeeding", "Pregnancy"
    ],
    "Home & Living (India)": [
        "IKEA", "Pepperfry", "Urban Ladder", "@home (store)",
        "Amazon Basics", "Godrej Interio", "Asian Paints",
        "Home decor", "Interior design", "Vastu shastra",
        "Smart home", "Home improvement", "DIY", "Gardening"
    ],
    "Automobiles (India)": [
        "Maruti Suzuki", "Hyundai", "Tata Motors", "Mahindra",
        "Honda Cars India", "Kia India", "Toyota India",
        "Ola Electric", "Ather Energy", "TVS Motor Company",
        "Hero MotoCorp", "Bajaj Auto", "Royal Enfield",
        "Electric vehicle", "Car accessories"
    ],
    "Technology & Gadgets": [
        "Samsung", "OnePlus", "Apple Inc.", "Xiaomi",
        "realme", "OPPO India", "vivo", "Nothing (company)",
        "boAt (company)", "JBL", "Sony", "Bose Corporation",
        "Noise (brand)", "Laptop", "Gaming",
        "5G", "Artificial intelligence", "Technology"
    ]
}

# ─────────────────────────────────────────────
# REAL META BEHAVIORS (actual Meta Ads targeting behaviors)
# ─────────────────────────────────────────────
REAL_META_BEHAVIORS = {
    "Purchase Behaviors (Meta-defined)": [
        "Engaged shoppers",              # People who clicked "Shop Now" in past week
        "Online shopping (general)",
        "High-value online buyers",
        "Mobile app purchasers (iOS)",
        "Mobile app purchasers (Android)",
        "Credit card users",
        "Debit card users",
        "PayLater / BNPL users",
        "Frequent travellers",
        "Frequent international travellers",
        "Commuters"
    ],
    "Digital Activity (Meta-defined)": [
        "Facebook access (mobile): all mobile devices",
        "Facebook access: Android",
        "Facebook access: iPhone and iPod",
        "Instagram daily active users",
        "Facebook daily active users",
        "Social media heavy users",
        "Mobile gamers",
        "Canvas game users"
    ],
    "Residential (Meta-defined)": [
        "Recently moved",
        "New homeowners",
        "Likely to move",
        "Renters"
    ],
    "Life Events (Meta-defined)": [
        "New job",
        "Newly engaged (1 year)",
        "Recently married (1 year)",
        "Expecting parents",
        "New parents (0–12 months)",
        "Away from family",
        "Long-distance relationship",
        "Recently divorced",
        "Upcoming birthday (within 30 days)",
        "Friends with upcoming anniversary",
        "Friends with upcoming birthday"
    ],
    "Business & Professional (Meta-defined)": [
        "Business travellers",
        "Small business owners",
        "Admins of Business Pages",
        "Startup founders"
    ]
}

# ─────────────────────────────────────────────
# INDIA CITY TIER CLUSTERS
# ─────────────────────────────────────────────
CITY_TIERS = {
    "Tier-1": {
        "cities": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad"],
        "description": "Metro cities — highest digital penetration, premium buyers, higher CPC",
        "typical_demographics": "25-45 years, higher income, English + regional language",
        "avg_cpc_multiplier": 1.5
    },
    "Tier-2": {
        "cities": ["Jaipur", "Lucknow", "Indore", "Bhopal", "Nagpur", "Patna", "Surat", "Vadodara",
                   "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Ludhiana",
                   "Chandigarh", "Coimbatore", "Visakhapatnam", "Kochi", "Guwahati"],
        "description": "Emerging metro/semi-urban — high growth, value-conscious buyers",
        "typical_demographics": "20-40 years, aspirational middle class, strong regional language",
        "avg_cpc_multiplier": 1.0
    },
    "Tier-3": {
        "cities": ["Smaller towns and rural districts across India"],
        "description": "Rural & semi-rural — lowest CPC, Hindi/regional dominant, COD preferred",
        "typical_demographics": "18-35 years, price-sensitive",
        "avg_cpc_multiplier": 0.6
    }
}

# ─────────────────────────────────────────────
# AGE & GENDER CLUSTERS FOR D2C INDIA
# ─────────────────────────────────────────────
AGE_CLUSTERS = {
    "Gen Z (18-24)": {
        "description": "Digital natives, trend-driven, influenced by Reels & memes",
        "platform_preference": "Instagram Reels, YouTube Shorts",
        "categories": ["Fashion", "Gaming", "Beauty", "Entertainment", "Education"]
    },
    "Young Millennials (25-34)": {
        "description": "Working professionals, aspirational buyers, strong purchase intent",
        "platform_preference": "Instagram, Facebook, LinkedIn",
        "categories": ["Fashion", "Health & Fitness", "Finance", "Electronics", "Travel"]
    },
    "Core Millennials (35-44)": {
        "description": "Established professionals, family-oriented, premium buyers",
        "platform_preference": "Facebook, YouTube",
        "categories": ["Home & Living", "Parenting", "Health", "Finance", "Travel"]
    },
    "Gen X (45-54)": {
        "description": "High-income segment, health-conscious, value brand trust",
        "platform_preference": "Facebook, WhatsApp",
        "categories": ["Health", "Finance", "Home", "Travel", "Spiritual"]
    }
}

# ─────────────────────────────────────────────
# AD PLACEMENT RECOMMENDATIONS
# ─────────────────────────────────────────────
AD_PLACEMENTS = {
    "High Performance": [
        "Instagram Reels (9:16 vertical video)",
        "Facebook Feed (1:1 square or 4:5)",
        "Instagram Stories (9:16)",
        "Facebook Reels"
    ],
    "Supplemental": [
        "Instagram Feed (1:1 or 4:5)",
        "Facebook Stories",
        "Messenger Stories",
        "Audience Network"
    ]
}

# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def get_all_interests_flat() -> list:
    out = []
    for _, items in REAL_META_INTERESTS.items():
        out.extend(items)
    return out


def get_all_behaviors_flat() -> list:
    out = []
    for _, items in REAL_META_BEHAVIORS.items():
        out.extend(items)
    return out


def get_targeting_context_string() -> str:
    """Inject into AI prompts so the model picks from REAL Meta interests."""
    interests_by_cat = "\n".join(
        f"  [{cat}]: {', '.join(items[:12])}"
        for cat, items in REAL_META_INTERESTS.items()
    )
    behaviors_by_cat = "\n".join(
        f"  [{cat}]: {', '.join(items[:6])}"
        for cat, items in REAL_META_BEHAVIORS.items()
    )
    return f"""
REAL META ADS INTEREST CATEGORIES (use exact names as they appear in Meta Ads Manager):
{interests_by_cat}

REAL META BEHAVIORS (Meta-defined, use exact names):
{behaviors_by_cat}

CITY TIERS:
  Tier-1: Mumbai, Delhi, Bangalore, Hyderabad, Chennai, Kolkata, Pune, Ahmedabad
  Tier-2: Jaipur, Lucknow, Indore, Chandigarh, Coimbatore, Kochi, Visakhapatnam, Nagpur, Surat
  Tier-3: Smaller towns, rural districts

IMPORTANT: You MUST select interests and behaviors from the lists above. Do NOT invent generic labels.
Pick only what is directly relevant to the product/service shown in the creative.
"""
