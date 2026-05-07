# dataset/dataset_qa.py
# Dataset di domande e risposte basato su news.txt
# Usato per valutare RAG vs no-RAG in modo quantitativo

QA_DATASET = [

    # -- Article 1: Pope Leo vs Trump --
    {
        "question": "What did Pope Leo say about war?",
        "answer":   "as a pastor, i cannot be in favour of war",
        "article":  1
    },
    {
        "question": "What did Trump call Pope Leo on social media?",
        "answer":   "weak on crime",
        "article":  1
    },
    {
        "question": "Who is going to visit the Vatican this week?",
        "answer":   "marco rubio",
        "article":  1
    },

    # -- Article 2: Trump assassination attempt --
    {
        "question": "What is the name of the man who allegedly tried to assassinate Trump?",
        "answer":   "cole tomas allen",
        "article":  2
    },
    {
        "question": "Where did the alleged assassination attempt take place?",
        "answer":   "washington hilton",
        "article":  2
    },
    {
        "question": "What weapons was the suspect carrying?",
        "answer":   "semi-automatic handgun, pump-action shotgun and three knives",
        "article":  2
    },

    # -- Article 3: Project Freedom --
    {
        "question": "What is Project Freedom?",
        "answer":   "us initiative to help guide ships stranded by iran closure of the strait of hormuz",
        "article":  3
    },
    {
        "question": "How many mariners are trapped in the Gulf?",
        "answer":   "22500",
        "article":  3
    },
    {
        "question": "Which shipping company confirmed one of its vessels exited the Gulf?",
        "answer":   "maersk",
        "article":  3
    },

    # -- Article 4: Ships crossing the Strait --
    {
        "question": "How many vessels crossed the Strait of Hormuz since the blockade started?",
        "answer":   "15",
        "article":  4
    },
    {
        "question": "How many ships passed through the strait each day before the conflict?",
        "answer":   "138",
        "article":  4
    },
    {
        "question": "What is spoofing in the context of ship tracking?",
        "answer":   "ships turning their trackers off or transmitting a false position",
        "article":  4
    },

    # -- Article 5: Airlines cut flights --
    {
        "question": "How many flights were cut globally in May?",
        "answer":   "13,000",
        "article":  5
    },
    {
        "question": "What was the price of jet fuel in late February?",
        "answer":   "831",
        "article":  5
    },
    {
        "question": "What was the highest price of jet fuel in early April?",
        "answer":   "1838",
        "article":  5
    },

    # -- Article 6: Jet fuel shortage --
    {
        "question": "How many days of jet fuel supply does Europe have left?",
        "answer":   "30",
        "article":  6
    },
    {
        "question": "At how many days of supply would airports start running out of fuel?",
        "answer":   "23",
        "article":  6
    },
    {
        "question": "What percentage of UK jet fuel comes from imports?",
        "answer":   "65",
        "article":  6
    },

    # -- Article 7: Gulf aviation --
    {
        "question": "How many passengers went through Dubai International Airport in 2024?",
        "answer":   "92 million",
        "article":  7
    },
    {
        "question": "What percentage of global capacity do Gulf carriers account for?",
        "answer":   "9.5",
        "article":  7
    },
    {
        "question": "How many services to the Middle East have been cancelled since the conflict started?",
        "answer":   "30,000",
        "article":  7
    },
]