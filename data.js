const LESSONS = [
  {
    "id": 1,
    "title": "Tom Gets Up",
    "article_text": "Tom opens his eyes. It is morning. He gets up. He eats bread and drinks milk. Then he walks to school. He sees his friend Ann. They go to class together. Tom likes school. He feels happy.",
    "sentences": [
      {
        "id": 1,
        "en": "Tom opens his eyes.",
        "zh": "汤姆睁开眼睛。",
        "words": [
          {
            "word": "open",
            "def": "打开",
            "ipa": "/ˈəʊpən/",
            "eng_def": "to move something so that it is not closed",
            "pos": "verb"
          },
          {
            "word": "eye",
            "def": "眼睛",
            "ipa": "/aɪ/",
            "eng_def": "the part of the body that you use to see",
            "pos": "noun"
          },
          {
            "word": "Tom",
            "def": "汤姆（人名）",
            "ipa": "/tɒm/",
            "eng_def": "a name for a boy",
            "pos": "noun"
          },
          {
            "word": "his",
            "def": "他的",
            "ipa": "/hɪz/",
            "eng_def": "belonging to him",
            "pos": "pron"
          }
        ]
      },
      {
        "id": 2,
        "en": "It is morning.",
        "zh": "现在是早上。",
        "words": [
          {
            "word": "morning",
            "def": "早上",
            "ipa": "/ˈmɔːnɪŋ/",
            "eng_def": "the early part of the day",
            "pos": "noun"
          },
          {
            "word": "it",
            "def": "它",
            "ipa": "/ɪt/",
            "eng_def": "used to refer to a thing or animal",
            "pos": "pron"
          },
          {
            "word": "is",
            "def": "是",
            "ipa": "/ɪz/",
            "eng_def": "third person singular of 'be'",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 3,
        "en": "He gets up.",
        "zh": "他起床了。",
        "words": [
          {
            "word": "get",
            "def": "得到；变得",
            "ipa": "/ɡet/",
            "eng_def": "to receive or have something",
            "pos": "verb"
          },
          {
            "word": "he",
            "def": "他",
            "ipa": "/hiː/",
            "eng_def": "the male person previously mentioned",
            "pos": "pron"
          }
        ]
      },
      {
        "id": 4,
        "en": "He eats bread and drinks milk.",
        "zh": "他吃面包，喝牛奶。",
        "words": [
          {
            "word": "eat",
            "def": "吃",
            "ipa": "/iːt/",
            "eng_def": "to take food into your body",
            "pos": "verb"
          },
          {
            "word": "drink",
            "def": "喝",
            "ipa": "/drɪŋk/",
            "eng_def": "to take water or other liquid into your body",
            "pos": "verb"
          },
          {
            "word": "he",
            "def": "他",
            "ipa": "/hiː/",
            "eng_def": "the male person previously mentioned",
            "pos": "pron"
          },
          {
            "word": "and",
            "def": "和；并且",
            "ipa": "/ænd/",
            "eng_def": "used to connect words or phrases",
            "pos": "conj"
          }
        ]
      },
      {
        "id": 5,
        "en": "Then he walks to school.",
        "zh": "然后他走路去学校。",
        "words": [
          {
            "word": "walk",
            "def": "走路",
            "ipa": "/wɔːk/",
            "eng_def": "to move on your feet",
            "pos": "verb"
          },
          {
            "word": "school",
            "def": "学校",
            "ipa": "/skuːl/",
            "eng_def": "a place where children go to learn",
            "pos": "noun"
          },
          {
            "word": "then",
            "def": "然后",
            "ipa": "/ðen/",
            "eng_def": "at that time; next",
            "pos": "adv"
          },
          {
            "word": "he",
            "def": "他",
            "ipa": "/hiː/",
            "eng_def": "the male person previously mentioned",
            "pos": "pron"
          },
          {
            "word": "to",
            "def": "到；去；给",
            "ipa": "/tuː/",
            "eng_def": "used to show direction or purpose",
            "pos": "prep"
          }
        ]
      },
      {
        "id": 6,
        "en": "He sees his friend Ann.",
        "zh": "他看到了他的朋友安。",
        "words": [
          {
            "word": "see",
            "def": "看见",
            "ipa": "/siː/",
            "eng_def": "to use your eyes to know something",
            "pos": "verb"
          },
          {
            "word": "he",
            "def": "他",
            "ipa": "/hiː/",
            "eng_def": "the male person previously mentioned",
            "pos": "pron"
          },
          {
            "word": "friend",
            "def": "朋友",
            "ipa": "/frend/",
            "eng_def": "a person you like and know well",
            "pos": "noun"
          },
          {
            "word": "Ann",
            "def": "安（人名）",
            "ipa": "/æn/",
            "eng_def": "a name for a girl",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 7,
        "en": "They go to class together.",
        "zh": "他们一起去上课。",
        "words": [
          {
            "word": "class",
            "def": "课；班级",
            "ipa": "/klɑːs/",
            "eng_def": "a group of students who learn together",
            "pos": "noun"
          },
          {
            "word": "they",
            "def": "他们；她们；它们",
            "ipa": "/ðeɪ/",
            "eng_def": "used to refer to two or more people",
            "pos": "pron"
          },
          {
            "word": "go",
            "def": "去",
            "ipa": "/ɡəʊ/",
            "eng_def": "to move or travel somewhere",
            "pos": "verb"
          },
          {
            "word": "to",
            "def": "到；去；给",
            "ipa": "/tuː/",
            "eng_def": "used to show direction or purpose",
            "pos": "prep"
          },
          {
            "word": "together",
            "def": "一起",
            "ipa": "/təˈɡeðə(r)/",
            "eng_def": "with each other",
            "pos": "adv"
          }
        ]
      },
      {
        "id": 8,
        "en": "Tom likes school.",
        "zh": "汤姆喜欢学校。",
        "words": [
          {
            "word": "Tom",
            "def": "汤姆（人名）",
            "ipa": "/tɒm/",
            "eng_def": "a name for a boy",
            "pos": "noun"
          },
          {
            "word": "like",
            "def": "喜欢",
            "ipa": "/laɪk/",
            "eng_def": "to find pleasant or enjoyable",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 9,
        "en": "He feels happy.",
        "zh": "他觉得很开心。",
        "words": [
          {
            "word": "he",
            "def": "他",
            "ipa": "/hiː/",
            "eng_def": "the male person previously mentioned",
            "pos": "pron"
          },
          {
            "word": "feel",
            "def": "感觉",
            "ipa": "/fiːl/",
            "eng_def": "to experience an emotion or sensation",
            "pos": "verb"
          },
          {
            "word": "happy",
            "def": "快乐的；开心的",
            "ipa": "/ˈhæpi/",
            "eng_def": "feeling pleasure or contentment",
            "pos": "adj"
          }
        ]
      }
    ],
    "questions": [
      {
        "question": "What does Tom do first in the morning?",
        "options": [
          "Get up",
          "Open his eyes",
          "Eat bread",
          "Go to school"
        ],
        "answer": "Open his eyes"
      },
      {
        "question": "What does Tom eat and drink for breakfast?",
        "options": [
          "Rice",
          "Bread and milk",
          "Eggs",
          "Fruit"
        ],
        "answer": "Bread and milk"
      },
      {
        "question": "How does Tom go to school?",
        "options": [
          "Take a car",
          "Ride a bike",
          "Walk",
          "Take a bus"
        ],
        "answer": "Walk"
      },
      {
        "question": "Who does Tom see at school?",
        "options": [
          "Teacher",
          "His friend Ann",
          "His mom",
          "Classmates"
        ],
        "answer": "His friend Ann"
      },
      {
        "question": "How does Tom feel about school?",
        "options": [
          "Doesn't like it",
          "Very happy",
          "Very tired",
          "Very bored"
        ],
        "answer": "Very happy"
      }
    ],
    "audio_full": "audio/lesson_01/full.mp3"
  },
  {
    "id": 2,
    "title": "At the Park",
    "article_text": "Tom and his mother go to the park. The park has many trees and birds. Tom sees a dog. The dog runs fast. Tom wants to play with the dog. But the dog goes home. Tom is sad. Then Tom sees water in a small lake. He looks at the water. A bird drinks the water. Tom feels happy. He says, \"This is a good time.\"",
    "sentences": [
      {
        "id": 1,
        "en": "Tom and his mother go to the park.",
        "zh": "汤姆和他妈妈去公园。",
        "words": [
          {
            "word": "park",
            "def": "公园",
            "ipa": "/pɑːk/",
            "eng_def": "a green area where people play and rest",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 2,
        "en": "The park has many trees and birds.",
        "zh": "公园里有很多树和鸟。",
        "words": [
          {
            "word": "tree",
            "def": "树",
            "ipa": "/triː/",
            "eng_def": "a tall plant with a long body made of wood",
            "pos": "noun"
          },
          {
            "word": "bird",
            "def": "鸟",
            "ipa": "/bɜːd/",
            "eng_def": "an animal with wings that can fly",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 3,
        "en": "Tom sees a dog.",
        "zh": "汤姆看到一只狗。",
        "words": [
          {
            "word": "dog",
            "def": "狗",
            "ipa": "/dɒɡ/",
            "eng_def": "an animal that many people keep at home",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 4,
        "en": "The dog runs fast.",
        "zh": "那只狗跑得很快。",
        "words": [
          {
            "word": "run",
            "def": "跑",
            "ipa": "/rʌn/",
            "eng_def": "to move your feet very fast",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 5,
        "en": "Tom wants to play with the dog.",
        "zh": "汤姆想跟那只狗玩。",
        "words": [
          {
            "word": "play",
            "def": "玩",
            "ipa": "/pleɪ/",
            "eng_def": "to do things for fun",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 6,
        "en": "But the dog goes home.",
        "zh": "但是那只狗回家了。",
        "words": [
          {
            "word": "home",
            "def": "家",
            "ipa": "/həʊm/",
            "eng_def": "the place where you live with your family",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 7,
        "en": "Tom is sad.",
        "zh": "汤姆很难过。",
        "words": []
      },
      {
        "id": 8,
        "en": "Then Tom sees water in a small lake.",
        "zh": "然后汤姆看到一个小湖里有水。",
        "words": [
          {
            "word": "water",
            "def": "水",
            "ipa": "/ˈwɔːtə(r)/",
            "eng_def": "the clear drink without color or taste",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 9,
        "en": "He looks at the water.",
        "zh": "他看着水。",
        "words": []
      },
      {
        "id": 10,
        "en": "A bird drinks the water.",
        "zh": "一只鸟在喝水。",
        "words": []
      },
      {
        "id": 11,
        "en": "Tom feels happy.",
        "zh": "汤姆觉得开心。",
        "words": [
          {
            "word": "happy",
            "def": "开心的",
            "ipa": "/ˈhæpi/",
            "eng_def": "feeling good",
            "pos": "adj"
          }
        ]
      },
      {
        "id": 12,
        "en": "He says, \"This is a good time.\"",
        "zh": "他说：“这是个好时光。”",
        "words": [
          {
            "word": "time",
            "def": "时间；时光",
            "ipa": "/taɪm/",
            "eng_def": "the thing we measure in hours, days, and years",
            "pos": "noun"
          }
        ]
      }
    ],
    "questions": [
      {
        "question": "Where does Tom go?",
        "options": [
          "Park",
          "School",
          "Home",
          "Lake"
        ],
        "answer": "Park"
      },
      {
        "question": "What does Tom see at the park?",
        "options": [
          "A cat",
          "A dog",
          "A car",
          "A book"
        ],
        "answer": "A dog"
      },
      {
        "question": "What does the dog do?",
        "options": [
          "It played with Tom",
          "It ran fast",
          "It ate food",
          "It slept"
        ],
        "answer": "It ran fast"
      },
      {
        "question": "Why is Tom happy at the end?",
        "options": [
          "He played with the dog",
          "He saw a bird drink water",
          "He went home",
          "He ate food"
        ],
        "answer": "He saw a bird drink water"
      },
      {
        "question": "What kind of time does Tom think this is?",
        "options": [
          "Bad time",
          "Good time",
          "Long time",
          "Short time"
        ],
        "answer": "Good time"
      }
    ],
    "audio_full": "audio/lesson_02/full.mp3"
  },
  {
    "id": 3,
    "title": "A New Friend",
    "article_text": "Tom is at the park. He sees a new boy. The boy has a ball. Tom asks, \"What is your name?\" The boy says, \"My name is Ben.\" They play a game with the ball. They laugh a lot. Tom gives Ben a drink. Ben says, \"You are a good friend.\" They stay at the park. They play on the side. Tom is happy to have a new friend.",
    "sentences": [
      {
        "id": 1,
        "en": "Tom is at the park.",
        "zh": "汤姆在公园里。",
        "words": []
      },
      {
        "id": 2,
        "en": "He sees a new boy.",
        "zh": "他看到一个新来的男孩。",
        "words": [
          {
            "word": "new",
            "def": "新的",
            "ipa": "/njuː/",
            "eng_def": "not old; just made or found",
            "pos": "adj"
          }
        ]
      },
      {
        "id": 3,
        "en": "The boy has a ball.",
        "zh": "那个男孩有一个球。",
        "words": [
          {
            "word": "boy",
            "def": "男孩",
            "ipa": "/bɔɪ/",
            "eng_def": "a young male person",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 4,
        "en": "Tom asks, \"What is your name?\"",
        "zh": "汤姆问：“你叫什么名字？”",
        "words": [
          {
            "word": "asks",
            "def": "问",
            "eng_def": "to say something to get an answer",
            "ipa": "/ɑːsks/",
            "pos": "verb"
          },
          {
            "word": "name",
            "def": "名字",
            "ipa": "/neɪm/",
            "eng_def": "the word that people call you",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 5,
        "en": "The boy says, \"My name is Ben.\"",
        "zh": "那个男孩说：“我叫本。”",
        "words": [
          {
            "word": "name",
            "def": "名字",
            "ipa": "/neɪm/",
            "eng_def": "the word that people call you",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 6,
        "en": "They play a game with the ball.",
        "zh": "他们一起玩球。",
        "words": [
          {
            "word": "game",
            "def": "游戏",
            "ipa": "/ɡeɪm/",
            "eng_def": "a fun activity with rules",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 7,
        "en": "They laugh a lot.",
        "zh": "他们笑得很开心。",
        "words": [
          {
            "word": "laugh",
            "def": "笑",
            "ipa": "/lɑːf/",
            "eng_def": "to make a sound because something is funny",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 8,
        "en": "Tom gives Ben a drink.",
        "zh": "汤姆给了本一杯水。",
        "words": [
          {
            "word": "gives",
            "def": "给",
            "ipa": "/ɡɪvz/",
            "eng_def": "to put something in another person's hand",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 9,
        "en": "Ben says, \"You are a good friend.\"",
        "zh": "本说：“你是个好朋友。”",
        "words": [
          {
            "word": "friend",
            "def": "朋友",
            "ipa": "/frend/",
            "eng_def": "a person you know and like",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 10,
        "en": "They stay at the park.",
        "zh": "他们待在公园里。",
        "words": [
          {
            "word": "stay",
            "def": "待、停留",
            "ipa": "/steɪ/",
            "eng_def": "to not leave; to be in the same place",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 11,
        "en": "They play on the side.",
        "zh": "他们在旁边玩。",
        "words": [
          {
            "word": "side",
            "def": "旁边、一边",
            "ipa": "/saɪd/",
            "eng_def": "the area to the right or left of something",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 12,
        "en": "Tom is happy to have a new friend.",
        "zh": "汤姆很高兴有了一个新朋友。",
        "words": [
          {
            "word": "new",
            "def": "新的",
            "ipa": "/njuː/",
            "eng_def": "not old; just made or found",
            "pos": "adj"
          },
          {
            "word": "friend",
            "def": "朋友",
            "ipa": "/frend/",
            "eng_def": "a person you know and like",
            "pos": "noun"
          }
        ]
      }
    ],
    "questions": [
      {
        "question": "Where is Tom?",
        "options": [
          "At school",
          "At the park",
          "At home",
          "At the store"
        ],
        "answer": "At the park"
      },
      {
        "question": "Who does Tom see?",
        "options": [
          "A new girl",
          "A new boy",
          "An old man",
          "A dog"
        ],
        "answer": "A new boy"
      },
      {
        "question": "What is the new boy's name?",
        "options": [
          "Tom",
          "Max",
          "Ben",
          "Kim"
        ],
        "answer": "Ben"
      },
      {
        "question": "What do they do together?",
        "options": [
          "Played a game",
          "Read a book",
          "Watched TV",
          "Ate lunch"
        ],
        "answer": "Played a game"
      },
      {
        "question": "How does Tom feel at the end?",
        "options": [
          "Sad",
          "Angry",
          "Happy",
          "Tired"
        ],
        "answer": "Happy"
      }
    ],
    "audio_full": "audio/lesson_03/full.mp3"
  },
  {
    "id": 4,
    "title": "Helping Mom",
    "article_text": "Tom comes home from school. He sees his mother in the kitchen. She looks tired. Tom wants to help. He puts his hand on her arm. \"Let me help you, Mother,\" he says. Tom cleans the table. He puts the food away. His mom smiles. \"You are a good boy,\" she says. Tom feels happy. He loves helping his mother.",
    "sentences": [
      {
        "id": 1,
        "en": "Tom comes home from school.",
        "zh": "汤姆放学回到家。",
        "words": [
          {
            "word": "home",
            "def": "家",
            "ipa": "/həʊm/",
            "eng_def": "the place where you live with your family",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 2,
        "en": "He sees his mother in the kitchen.",
        "zh": "他看到妈妈在厨房里。",
        "words": []
      },
      {
        "id": 3,
        "en": "She looks tired.",
        "zh": "她看起来很累。",
        "words": []
      },
      {
        "id": 4,
        "en": "Tom wants to help.",
        "zh": "汤姆想帮忙。",
        "words": [
          {
            "word": "help",
            "def": "帮忙",
            "ipa": "/help/",
            "eng_def": "to do something so the work is easier for another person",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 5,
        "en": "He puts his hand on her arm.",
        "zh": "他把手放在妈妈的胳膊上。",
        "words": [
          {
            "word": "hand",
            "def": "手",
            "ipa": "/hænd/",
            "eng_def": "the body part at the end of your arm",
            "pos": "noun"
          },
          {
            "word": "put",
            "def": "放",
            "ipa": "/pʊt/",
            "eng_def": "to move something to a place",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 6,
        "en": "\"Let me help you, Mother,\" he says.",
        "zh": "他说：“妈妈，让我帮你吧。”",
        "words": []
      },
      {
        "id": 7,
        "en": "Tom cleans the table.",
        "zh": "汤姆擦了桌子。",
        "words": [
          {
            "word": "clean",
            "def": "擦干净",
            "ipa": "/kliːn/",
            "eng_def": "to remove dirt; not dirty",
            "pos": "verb"
          },
          {
            "word": "table",
            "def": "桌子",
            "ipa": "/ˈteɪbl/",
            "eng_def": "a piece of furniture with a flat top",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 8,
        "en": "He puts the food away.",
        "zh": "他把食物收好。",
        "words": [
          {
            "word": "food",
            "def": "食物",
            "ipa": "/fuːd/",
            "eng_def": "the things that people and animals eat",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 9,
        "en": "His mom smiles.",
        "zh": "妈妈笑了。",
        "words": []
      },
      {
        "id": 10,
        "en": "\"You are a good boy,\" she says.",
        "zh": "她说：“你真是个好孩子。”",
        "words": [
          {
            "word": "good",
            "def": "好的",
            "ipa": "/ɡʊd/",
            "eng_def": "of a high quality; not bad",
            "pos": "adj"
          }
        ]
      },
      {
        "id": 11,
        "en": "Tom feels happy.",
        "zh": "汤姆觉得很开心。",
        "words": []
      },
      {
        "id": 12,
        "en": "He loves helping his mother.",
        "zh": "他喜欢帮妈妈的忙。",
        "words": [
          {
            "word": "love",
            "def": "爱，喜欢",
            "ipa": "/lʌv/",
            "eng_def": "to like someone or something very much",
            "pos": "verb"
          }
        ]
      }
    ],
    "questions": [
      {
        "question": "Where does Tom go after school?",
        "options": [
          "School",
          "Friend's house",
          "Home",
          "Store"
        ],
        "answer": "Home"
      },
      {
        "question": "How does mom look?",
        "options": [
          "Happy",
          "Tired",
          "Angry",
          "Sad"
        ],
        "answer": "Tired"
      },
      {
        "question": "What does Tom do to help his mom?",
        "options": [
          "Cook food",
          "Clean the table and put food away",
          "Wash clothes",
          "Sweep the floor"
        ],
        "answer": "Clean the table and put food away"
      },
      {
        "question": "What does mom say to Tom?",
        "options": [
          "You are a good boy",
          "Go play",
          "Don't bother me",
          "Go do homework"
        ],
        "answer": "You are a good boy"
      },
      {
        "question": "How does Tom feel?",
        "options": [
          "Tired",
          "Hungry",
          "Happy",
          "Sleepy"
        ],
        "answer": "Happy"
      }
    ],
    "audio_full": "audio/lesson_04/full.mp3"
  },
  {
    "id": 5,
    "title": "A Rainy Day",
    "article_text": "Tom looks out the window. It is rain. He wants to go out. But he can't. The rain is too strong. So Tom stays home. He finds a book. He reads a good story. After that, he goes to bed. He rests his eyes. It is a nice day inside.",
    "sentences": [
      {
        "id": 1,
        "en": "Tom looks out the window.",
        "zh": "汤姆往窗外看。",
        "words": [
          {
            "word": "window",
            "def": "窗户",
            "ipa": "/ˈwɪndəʊ/",
            "eng_def": "an opening in a wall with glass",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 2,
        "en": "It is rain.",
        "zh": "下雨了。",
        "words": [
          {
            "word": "rain",
            "def": "雨",
            "ipa": "/reɪn/",
            "eng_def": "water that falls from the sky",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 3,
        "en": "He wants to go out.",
        "zh": "他想出去。",
        "words": []
      },
      {
        "id": 4,
        "en": "But he can't.",
        "zh": "但他出不去。",
        "words": []
      },
      {
        "id": 5,
        "en": "The rain is too strong.",
        "zh": "雨太大了。",
        "words": [
          {
            "word": "rain",
            "def": "雨",
            "ipa": "/reɪn/",
            "eng_def": "water that falls from the sky",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 6,
        "en": "So Tom stays home.",
        "zh": "所以汤姆待在家里。",
        "words": []
      },
      {
        "id": 7,
        "en": "He finds a book.",
        "zh": "他找到一本书。",
        "words": [
          {
            "word": "book",
            "def": "书",
            "ipa": "/bʊk/",
            "eng_def": "pages with words that you read",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 8,
        "en": "He reads a good story.",
        "zh": "他读了一个好故事。",
        "words": [
          {
            "word": "read",
            "def": "读",
            "ipa": "/riːd/",
            "eng_def": "to look at words and understand them",
            "pos": "verb"
          },
          {
            "word": "story",
            "def": "故事",
            "ipa": "/ˈstɔːri/",
            "eng_def": "words that tell about events",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 9,
        "en": "After that, he goes to bed.",
        "zh": "之后，他去睡觉了。",
        "words": [
          {
            "word": "bed",
            "def": "床",
            "ipa": "/bed/",
            "eng_def": "a piece of furniture that you sleep on",
            "pos": "noun"
          }
        ]
      },
      {
        "id": 10,
        "en": "He rests his eyes.",
        "zh": "他让眼睛歇一歇。",
        "words": [
          {
            "word": "rest",
            "def": "休息",
            "ipa": "/rest/",
            "eng_def": "to stop work so your body can feel better",
            "pos": "verb"
          }
        ]
      },
      {
        "id": 11,
        "en": "It is a nice day inside.",
        "zh": "待在屋里也挺好的一天。",
        "words": []
      }
    ],
    "questions": [
      {
        "question": "Why can't Tom go outside?",
        "options": [
          "He is tired.",
          "The rain is too strong.",
          "He likes to stay home.",
          "He has no shoes."
        ],
        "answer": "The rain is too strong."
      },
      {
        "question": "What does Tom do at home?",
        "options": [
          "He watched TV.",
          "He read a book.",
          "He played with a toy.",
          "He cooked food."
        ],
        "answer": "He read a book."
      },
      {
        "question": "Where does Tom go at the end of the story?",
        "options": [
          "He went to school.",
          "He went outside.",
          "He went to bed.",
          "He went to the park."
        ],
        "answer": "He went to bed."
      },
      {
        "question": "How does Tom feel about this day?",
        "options": [
          "It is bad.",
          "It is nice inside.",
          "It is boring.",
          "It is too long."
        ],
        "answer": "It is nice inside."
      }
    ],
    "audio_full": "audio/lesson_05/full.mp3"
  }
];
