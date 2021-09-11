#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "46CBB5F5-77CD-452B-BED5-FA7ADF0454AD",
  "name": "Small Adventure",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631388494884,
  "passages": [
    {
      "name": "Adventurer Intro",
      "tags": "",
      "id": "1",
      "text": "You've never had much to do in your little village, and you're sick of it. You have a thirst for adventure that you need to satisfy, no matter what anyone says. Today is the day you venture out into the rest of the world, so you pack your sword and head to the border of your village. (Type: CONTINUE)\n[[CONTINUE->Two paths]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Two paths",
          "original": "[[CONTINUE->Two paths]]"
        }
      ],
      "hooks": [],
      "cleanText": "You've never had much to do in your little village, and you're sick of it. You have a thirst for adventure that you need to satisfy, no matter what anyone says. Today is the day you venture out into the rest of the world, so you pack your sword and head to the border of your village. (Type: CONTINUE)"
    },
    {
      "name": "Forest Path",
      "tags": "",
      "id": "2",
      "text": "You begin to trot along the forest path but soon encounter a bear blocking your way. (Type: TRY TO FIGHT or TRY TO BEFRIEND)\n[[TRY TO FIGHT->Rest in Peace (fight)]]\n[[TRY TO BEFRIEND->New Friend!]]",
      "links": [
        {
          "linkText": "TRY TO FIGHT",
          "passageName": "Rest in Peace (fight)",
          "original": "[[TRY TO FIGHT->Rest in Peace (fight)]]"
        },
        {
          "linkText": "TRY TO BEFRIEND",
          "passageName": "New Friend!",
          "original": "[[TRY TO BEFRIEND->New Friend!]]"
        }
      ],
      "hooks": [],
      "cleanText": "You begin to trot along the forest path but soon encounter a bear blocking your way. (Type: TRY TO FIGHT or TRY TO BEFRIEND)"
    },
    {
      "name": "Gravel Path",
      "tags": "",
      "id": "3",
      "text": "You enter the gravel path and the further down you go, the more vast the field around you seems to feel. (Type: CONTINUE)\n[[CONTINUE->PROCEED]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "PROCEED",
          "original": "[[CONTINUE->PROCEED]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter the gravel path and the further down you go, the more vast the field around you seems to feel. (Type: CONTINUE)"
    },
    {
      "name": "Rest in Peace (fight)",
      "tags": "",
      "id": "4",
      "text": "You tried, but ultimately whatever you were up against succeeded. (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "You tried, but ultimately whatever you were up against succeeded. (Type: QUIT)"
    },
    {
      "name": "New Friend!",
      "tags": "",
      "id": "5",
      "score": 10,
      "text": "Turns out he's nice. You've made a new friend, he joins you on your adventure. (Type: CONTINUE)\n[[CONTINUE]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "CONTINUE",
          "original": "[[CONTINUE]]"
        }
      ],
      "hooks": [],
      "cleanText": "Turns out he's nice. You've made a new friend, he joins you on your adventure. (Type: CONTINUE)"
    },
    {
      "name": "CONTINUE",
      "tags": "",
      "id": "6",
      "text": "You and your new friend encounter a fork in the road. You want to go to the left, but he seems to want to go to the right. If only you spoke his language. (Type: TRUST YOUR GUT or FOLLOW THE BEAR)\n[[TRUST YOUR GUT->Rest in peace (lost)]]\n[[FOLLOW THE BEAR->River]]",
      "links": [
        {
          "linkText": "TRUST YOUR GUT",
          "passageName": "Rest in peace (lost)",
          "original": "[[TRUST YOUR GUT->Rest in peace (lost)]]"
        },
        {
          "linkText": "FOLLOW THE BEAR",
          "passageName": "River",
          "original": "[[FOLLOW THE BEAR->River]]"
        }
      ],
      "hooks": [],
      "cleanText": "You and your new friend encounter a fork in the road. You want to go to the left, but he seems to want to go to the right. If only you spoke his language. (Type: TRUST YOUR GUT or FOLLOW THE BEAR)"
    },
    {
      "name": "Rest in peace (lost)",
      "tags": "",
      "id": "7",
      "text": "You attempted to find your own way, but ultimately got lost forever. (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "You attempted to find your own way, but ultimately got lost forever. (Type: QUIT)"
    },
    {
      "name": "River",
      "tags": "",
      "id": "8",
      "text": "The bear leads you to a nearby river. He runs in ahead of you and catches a fish, then comes back and offers it to you. (Type: ACCEPT FISH or REJECT FISH)\n[[ACCEPT FISH->Fish]]\n[[REJECT FISH->Bear Offense]]",
      "links": [
        {
          "linkText": "ACCEPT FISH",
          "passageName": "Fish",
          "original": "[[ACCEPT FISH->Fish]]"
        },
        {
          "linkText": "REJECT FISH",
          "passageName": "Bear Offense",
          "original": "[[REJECT FISH->Bear Offense]]"
        }
      ],
      "hooks": [],
      "cleanText": "The bear leads you to a nearby river. He runs in ahead of you and catches a fish, then comes back and offers it to you. (Type: ACCEPT FISH or REJECT FISH)"
    },
    {
      "name": "PROCEED",
      "tags": "",
      "id": "9",
      "text": "To your left you encounter a bush with berries. They look quite similar to blueberries and really appetizing right now. (Type: EAT THEM or DON'T EAT THEM or PUT IN INVENTORY)\n[[EAT THEM->Delicious!]]\n[[DON'T EAT THEM->Thief]]\n[[PUT IN INVENTORY->Proceed pt2 (berries)]]",
      "links": [
        {
          "linkText": "EAT THEM",
          "passageName": "Delicious!",
          "original": "[[EAT THEM->Delicious!]]"
        },
        {
          "linkText": "DON'T EAT THEM",
          "passageName": "Thief",
          "original": "[[DON'T EAT THEM->Thief]]"
        },
        {
          "linkText": "PUT IN INVENTORY",
          "passageName": "Proceed pt2 (berries)",
          "original": "[[PUT IN INVENTORY->Proceed pt2 (berries)]]"
        }
      ],
      "hooks": [],
      "cleanText": "To your left you encounter a bush with berries. They look quite similar to blueberries and really appetizing right now. (Type: EAT THEM or DON'T EAT THEM or PUT IN INVENTORY)"
    },
    {
      "name": "Delicious!",
      "tags": "",
      "id": "10",
      "score":10,
      "text": "They dry your mouth out a bit, but they're delicious. That was an adventurous choice! (Type: CONTINUE)\n[[CONTINUE->Thief]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Thief",
          "original": "[[CONTINUE->Thief]]"
        }
      ],
      "hooks": [],
      "cleanText": "They dry your mouth out a bit, but they're delicious. That was an adventurous choice! (Type: CONTINUE)"
    },
    {
      "name": "Thief",
      "tags": "",
      "id": "11",
      "text": "You continue past the berry push and all is well until you hear a strange rustling in the grass just a few feet ahead of you. It's a theif! And he wants everything you've got! (Type: FIGHT HIM or TRY TO RUN OR TALK YOUR WAY OUT)\n[[FIGHT HIM->Lucky win]]\n[[TRY TO RUN->Escape]]\n[[TALK YOUR WAY OUT->Rest in Peace (fight)]]",
      "links": [
        {
          "linkText": "FIGHT HIM",
          "passageName": "Lucky win",
          "original": "[[FIGHT HIM->Lucky win]]"
        },
        {
          "linkText": "TRY TO RUN",
          "passageName": "Escape",
          "original": "[[TRY TO RUN->Escape]]"
        },
        {
          "linkText": "TALK YOUR WAY OUT",
          "passageName": "Rest in Peace (fight)",
          "original": "[[TALK YOUR WAY OUT->Rest in Peace (fight)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You continue past the berry push and all is well until you hear a strange rustling in the grass just a few feet ahead of you. It's a theif! And he wants everything you've got! (Type: FIGHT HIM or TRY TO RUN OR TALK YOUR WAY OUT)"
    },
    {
      "name": "Lucky win",
      "tags": "",
      "id": "12",
      "score":20,
      "text": "Despite this being your first battle, you somehow hurt him enough to scare him away. What a lucky win! (Type: CONTINUE)\n[[CONTINUE->Treasure ending (luck)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Treasure ending (luck)",
          "original": "[[CONTINUE->Treasure ending (luck)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Despite this being your first battle, you somehow hurt him enough to scare him away. What a lucky win! (Type: CONTINUE)"
    },
    {
      "name": "Escape",
      "tags": "",
      "id": "13",
      "text": "You run into the tall grass as fast as you can, but in your panic you lost the path. You turn back in the direction you think you came from, but can find nothing but grass. After searching for what feels like hours, you find yourself quite tired. You then stumble across an ominous cabin nestled in an opening in the field, and it might be your only hope of making it out. (Type: ENTER CABIN or KEEP SEARCHING FOR PATH)\n[[ENTER CABIN->Cabin]]\n[[KEEP SEARCHING FOR PATH->Rest in peace (lost)]]",
      "links": [
        {
          "linkText": "ENTER CABIN",
          "passageName": "Cabin",
          "original": "[[ENTER CABIN->Cabin]]"
        },
        {
          "linkText": "KEEP SEARCHING FOR PATH",
          "passageName": "Rest in peace (lost)",
          "original": "[[KEEP SEARCHING FOR PATH->Rest in peace (lost)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You run into the tall grass as fast as you can, but in your panic you lost the path. You turn back in the direction you think you came from, but can find nothing but grass. After searching for what feels like hours, you find yourself quite tired. You then stumble across an ominous cabin nestled in an opening in the field, and it might be your only hope of making it out. (Type: ENTER CABIN or KEEP SEARCHING FOR PATH)"
    },
    {
      "name": "Cabin",
      "tags": "",
      "id": "14",
      "text": "You approach the door of the cabin and give it a gentle knock. Just moments later a woman with a large pointy black hat and a long black robe answers the door and invites you inside for a meal. (Type: ACCEPT INVITATION or RUN AWAY)\n[[ACCEPT INVITATION->Rest in peace (eaten)]] \n[[RUN AWAY->Rest in peace (lost)]]",
      "links": [
        {
          "linkText": "ACCEPT INVITATION",
          "passageName": "Rest in peace (eaten)",
          "original": "[[ACCEPT INVITATION->Rest in peace (eaten)]]"
        },
        {
          "linkText": "RUN AWAY",
          "passageName": "Rest in peace (lost)",
          "original": "[[RUN AWAY->Rest in peace (lost)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the door of the cabin and give it a gentle knock. Just moments later a woman with a large pointy black hat and a long black robe answers the door and invites you inside for a meal. (Type: ACCEPT INVITATION or RUN AWAY)"
    },
    {
      "name": "Proceed pt2 (berries)",
      "tags": "",
      "id": "15",
      "text": "You continue past the berry push all is well until you hear a strange rustling in the grass just a few feet ahead of you. (Type: CONTINUE)\n[[CONTINUE->Theif(berries)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Theif(berries)",
          "original": "[[CONTINUE->Theif(berries)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You continue past the berry push all is well until you hear a strange rustling in the grass just a few feet ahead of you. (Type: CONTINUE)"
    },
    {
      "name": "Theif(berries)",
      "tags": "",
      "id": "16",
      "text": "It's a theif! And he wants everything you've got! (Type: FIGHT HIM or TRY TO RUN or TALK YOUR WAY OUT)\n[[FIGHT HIM->Lucky win(berries)]]\n[[TRY TO RUN->Escape(berries)]]\n[[TALK YOUR WAY OUT->Rest in Peace (fight)]]",
      "links": [
        {
          "linkText": "FIGHT HIM",
          "passageName": "Lucky win(berries)",
          "original": "[[FIGHT HIM->Lucky win(berries)]]"
        },
        {
          "linkText": "TRY TO RUN",
          "passageName": "Escape(berries)",
          "original": "[[TRY TO RUN->Escape(berries)]]"
        },
        {
          "linkText": "TALK YOUR WAY OUT",
          "passageName": "Rest in Peace (fight)",
          "original": "[[TALK YOUR WAY OUT->Rest in Peace (fight)]]"
        }
      ],
      "hooks": [],
      "cleanText": "It's a theif! And he wants everything you've got! (Type: FIGHT HIM or TRY TO RUN or TALK YOUR WAY OUT)"
    },
    {
      "name": "Lucky win(berries)",
      "tags": "",
      "id": "17",
      "score":20,
      "text": "Despite this being your first battle, you somehow hurt him enough to scare him away. What a lucky win! (Type: CONTINUE)\n[[CONTINUE->Treasure Ending(berries)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Treasure Ending(berries)",
          "original": "[[CONTINUE->Treasure Ending(berries)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Despite this being your first battle, you somehow hurt him enough to scare him away. What a lucky win! (Type: CONTINUE)"
    },
    {
      "name": "Escape(berries)",
      "tags": "",
      "id": "18",
      "text": "You run into the tall grass as fast as you can, but in your panic you lost the path. You turn back in the direction you think you came from, but can find nothing but grass. Eventually you stumble across an ominous cabin nestled in an opening in the field, and it might be your only hope of making it out. (Type: ENTER CABIN or TRY TO FIND PATH)\n[[ENTER CABIN->Cabin(berries)]]\n[[TRY TO FIND PATH->Rest in peace (lost)]]",
      "links": [
        {
          "linkText": "ENTER CABIN",
          "passageName": "Cabin(berries)",
          "original": "[[ENTER CABIN->Cabin(berries)]]"
        },
        {
          "linkText": "TRY TO FIND PATH",
          "passageName": "Rest in peace (lost)",
          "original": "[[TRY TO FIND PATH->Rest in peace (lost)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You run into the tall grass as fast as you can, but in your panic you lost the path. You turn back in the direction you think you came from, but can find nothing but grass. Eventually you stumble across an ominous cabin nestled in an opening in the field, and it might be your only hope of making it out. (Type: ENTER CABIN or TRY TO FIND PATH)"
    },
    {
      "name": "Cabin(berries)",
      "tags": "",
      "id": "19",
      "text": "You approach the door of the cabin and give it a gentle knock. Just moments later a woman with a large pointy black hat and a long black robe answers the door and invites you inside for a meal. (Type: ACCEPT INVITATION or RUN AWAY or FIGHT HER)\n[[ACCEPT INVITATION->Inside House]] \n[[RUN AWAY->Rest in peace (lost)]] \n[[FIGHT HER->Witch Battle(berries)]]",
      "links": [
        {
          "linkText": "ACCEPT INVITATION",
          "passageName": "Inside House",
          "original": "[[ACCEPT INVITATION->Inside House]]"
        },
        {
          "linkText": "RUN AWAY",
          "passageName": "Rest in peace (lost)",
          "original": "[[RUN AWAY->Rest in peace (lost)]]"
        },
        {
          "linkText": "FIGHT HER",
          "passageName": "Witch Battle(berries)",
          "original": "[[FIGHT HER->Witch Battle(berries)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the door of the cabin and give it a gentle knock. Just moments later a woman with a large pointy black hat and a long black robe answers the door and invites you inside for a meal. (Type: ACCEPT INVITATION or RUN AWAY or FIGHT HER)"
    },
    {
      "name": "Rest in peace (eaten)",
      "tags": "",
      "id": "20",
      "text": "Unfortunately she cooked you up and ate you. Turns out she wasn't offering to make you a meal, she wanted to make you her meal. Didn't you read Hansel and Gretel? (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "Unfortunately she cooked you up and ate you. Turns out she wasn't offering to make you a meal, she wanted to make you her meal. Didn't you read Hansel and Gretel? (Type: QUIT)"
    },
    {
      "name": "Inside House",
      "tags": "",
      "id": "21",
      "text": "She welcomes you in with hungry eyes and you see a plethora of candles, spices, and an assortment of animal parts. You also see a dining table beside a large cauldron over a fire- she seems to be cooking. (Type: OFFER BERRIES or FIGHT HER or SIT AT THE TABLE)\n[[OFFER BERRIES->Ending (Delicious Meal)]]\n[[FIGHT HER->Witch Battle(berries)]] \n[[SIT AT THE TABLE->Rest in peace (eaten)]]",
      "links": [
        {
          "linkText": "OFFER BERRIES",
          "passageName": "Ending (Delicious Meal)",
          "original": "[[OFFER BERRIES->Ending (Delicious Meal)]]"
        },
        {
          "linkText": "FIGHT HER",
          "passageName": "Witch Battle(berries)",
          "original": "[[FIGHT HER->Witch Battle(berries)]]"
        },
        {
          "linkText": "SIT AT THE TABLE",
          "passageName": "Rest in peace (eaten)",
          "original": "[[SIT AT THE TABLE->Rest in peace (eaten)]]"
        }
      ],
      "hooks": [],
      "cleanText": "She welcomes you in with hungry eyes and you see a plethora of candles, spices, and an assortment of animal parts. You also see a dining table beside a large cauldron over a fire- she seems to be cooking. (Type: OFFER BERRIES or FIGHT HER or SIT AT THE TABLE)"
    },
    {
      "name": "Witch Battle(berries)",
      "tags": "",
      "id": "22",
      "text": "You don't trust this woman and trying to find the path again doesn't feel like a viable option. (Type: USE SWORD or USE BERRIES)\n[[USE SWORD->Victory (curse)]]\n[[USE BERRIES->throw berry]]",
      "links": [
        {
          "linkText": "USE SWORD",
          "passageName": "Victory (curse)",
          "original": "[[USE SWORD->Victory (curse)]]"
        },
        {
          "linkText": "USE BERRIES",
          "passageName": "throw berry",
          "original": "[[USE BERRIES->throw berry]]"
        }
      ],
      "hooks": [],
      "cleanText": "You don't trust this woman and trying to find the path again doesn't feel like a viable option. (Type: USE SWORD or USE BERRIES)"
    },
    {
      "name": "Ending (Delicious Meal)",
      "tags": "",
      "id": "23",
      "score":100,
      "text": "In shock she says, \"Is that aronia?! I've been looking everywhere for those! I need them for a recipe I've been working on.\" She takes your aronia and cooks you the most delicious fruit tart you've ever had. She then flies you back home being sure to supply you with another tart. Congratulations! You've found the treasure of a delicious pastry baked with love! (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "In shock she says, \"Is that aronia?! I've been looking everywhere for those! I need them for a recipe I've been working on.\" She takes your aronia and cooks you the most delicious fruit tart you've ever had. She then flies you back home being sure to supply you with another tart. Congratulations! You've found the treasure of a delicious pastry baked with love! (Type: QUIT)"
    },
    {
      "name": "throw berry",
      "tags": "",
      "id": "24",
      "text": "What did you think that would accomplish? I've got some bad news. (Type: CONTINUE)\n[[CONTINUE->Rest in Peace (fight)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Rest in Peace (fight)",
          "original": "[[CONTINUE->Rest in Peace (fight)]]"
        }
      ],
      "hooks": [],
      "cleanText": "What did you think that would accomplish? I've got some bad news. (Type: CONTINUE)"
    },
    {
      "name": "Victory (curse)",
      "tags": "",
      "id": "25",
      "text": "You engage in battle! She throws a vial at your feet and the liquid inside covers your legs. You run at the woman with your sword drawn and manage to hurt her just enough provide a distraction. You escape the cabin with your life. (Type: CONTINUE)\n[[CONTINUE->Treasure Ending (Curse)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Treasure Ending (Curse)",
          "original": "[[CONTINUE->Treasure Ending (Curse)]]"
        }
      ],
      "hooks": [],
      "cleanText": "You engage in battle! She throws a vial at your feet and the liquid inside covers your legs. You run at the woman with your sword drawn and manage to hurt her just enough provide a distraction. You escape the cabin with your life. (Type: CONTINUE)"
    },
    {
      "name": "Treasure Ending (Curse)",
      "tags": "",
      "id": "26",
      "text": "Damaging the woman in the cabin seems to have changed your surroundings outside. What was once an endless field with tall grass has now become a peaceful meadow and you can see the horizon again. In the distance you can now see a wonderfully shining object. Could this be the treasure? (Type: CONTINUE)\n[[CONTINUE->Poison Ending]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Poison Ending",
          "original": "[[CONTINUE->Poison Ending]]"
        }
      ],
      "hooks": [],
      "cleanText": "Damaging the woman in the cabin seems to have changed your surroundings outside. What was once an endless field with tall grass has now become a peaceful meadow and you can see the horizon again. In the distance you can now see a wonderfully shining object. Could this be the treasure? (Type: CONTINUE)"
    },
    {
      "name": "Fish",
      "tags": "",
      "id": "27",
      "score":10,
      "text": "You accept his gift and take a bite. It's not good, but it was nice of you to take it. (Type: CONTINUE)\n[[CONTINUE->Forest Exit]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Forest Exit",
          "original": "[[CONTINUE->Forest Exit]]"
        }
      ],
      "hooks": [],
      "cleanText": "You accept his gift and take a bite. It's not good, but it was nice of you to take it. (Type: CONTINUE)"
    },
    {
      "name": "Bear Offense",
      "tags": "",
      "id": "28",
      "text": "Oh no. He seems to be very offended by this. (Type: CONTINUE)\n[[CONTINUE->Rest in Peace (bear)]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Rest in Peace (bear)",
          "original": "[[CONTINUE->Rest in Peace (bear)]]"
        }
      ],
      "hooks": [],
      "cleanText": "Oh no. He seems to be very offended by this. (Type: CONTINUE)"
    },
    {
      "name": "Rest in Peace (bear)",
      "tags": "",
      "id": "29",
      "text": "Rejecting a bear's fish is a great offense in their culture. The bear kills you in his rage. (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "Rejecting a bear's fish is a great offense in their culture. The bear kills you in his rage. (Type: QUIT)"
    },
    {
      "name": "Forest Exit",
      "tags": "",
      "id": "30",
      "text": "The bear then leads you to a clearning in the forest and you see a bright shining object that must be the treasure, but your friend seems sad to see you go. (Type: CLAIM THE TREASURE or STAY WITH HIM)\n[[CLAIM THE TREASURE->Treasure ending]]\n[[STAY WITH HIM->Friendship ending]]",
      "links": [
        {
          "linkText": "CLAIM THE TREASURE",
          "passageName": "Treasure ending",
          "original": "[[CLAIM THE TREASURE->Treasure ending]]"
        },
        {
          "linkText": "STAY WITH HIM",
          "passageName": "Friendship ending",
          "original": "[[STAY WITH HIM->Friendship ending]]"
        }
      ],
      "hooks": [],
      "cleanText": "The bear then leads you to a clearning in the forest and you see a bright shining object that must be the treasure, but your friend seems sad to see you go. (Type: CLAIM THE TREASURE or STAY WITH HIM)"
    },
    {
      "name": "Treasure ending (luck)",
      "tags": "",
      "id": "31",
      "score":500,
      "text": "It seems that your luck hasn't run out just yet! Miraculously, you encounter no other obstacles along the way! You find your way to the end of the gravel path and see a bright shining light just up ahead. As you make your way to it, you see golden figurine encrusted with jewels and know that this must be the treasure you had once heard about. The people back in the village won't believe this! (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "It seems that your luck hasn't run out just yet! Miraculously, you encounter no other obstacles along the way! You find your way to the end of the gravel path and see a bright shining light just up ahead. As you make your way to it, you see golden figurine encrusted with jewels and know that this must be the treasure you had once heard about. The people back in the village won't believe this! (Type: QUIT)"
    },
    {
      "name": "Friendship ending",
      "tags": "",
      "id": "32",
      "score":300,
      "text": "I guess the real prize wasn't the treasure, but the friend you made along the way. (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "I guess the real prize wasn't the treasure, but the friend you made along the way. (Type: QUIT)"
    },
    {
      "name": "Two paths",
      "tags": "",
      "id": "33",
      "text": "Ahead of you are two paths. One surrounded by a thick wood on either side and one a gravel road with tall grass all around. You've heard a tale of a vast treasure down one of the two, but you can't seem to remember which one. (Type: FOREST PATH or GRAVEL PATH)\n[[FOREST PATH->Forest Path]]\n[[GRAVEL PATH->Gravel Path]]",
      "links": [
        {
          "linkText": "FOREST PATH",
          "passageName": "Forest Path",
          "original": "[[FOREST PATH->Forest Path]]"
        },
        {
          "linkText": "GRAVEL PATH",
          "passageName": "Gravel Path",
          "original": "[[GRAVEL PATH->Gravel Path]]"
        }
      ],
      "hooks": [],
      "cleanText": "Ahead of you are two paths. One surrounded by a thick wood on either side and one a gravel road with tall grass all around. You've heard a tale of a vast treasure down one of the two, but you can't seem to remember which one. (Type: FOREST PATH or GRAVEL PATH)"
    },
    {
      "name": "Treasure Ending(berries)",
      "tags": "",
      "id": "34",
      "score":500,
      "text": "It seems that your luck hasn't run out just yet! Miraculously, you encounter no other obstacles and you have some berries to enjoy along the way! You find your way to the end of the gravel path and see a bright shining light just up ahead. As you make your way to it, you see golden figurine encrusted with jewels and know that this must be the treasure you had once heard about. The people back in the village won't believe this! (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "It seems that your luck hasn't run out just yet! Miraculously, you encounter no other obstacles and you have some berries to enjoy along the way! You find your way to the end of the gravel path and see a bright shining light just up ahead. As you make your way to it, you see golden figurine encrusted with jewels and know that this must be the treasure you had once heard about. The people back in the village won't believe this! (Type: QUIT)"
    },
    {
      "name": "Poison Ending",
      "tags": "",
      "id": "35",
      "text": "You make your way to this shining light, hopeful that it is the treasure you long for. You try to run, but find that your legs can't keep up. In fact all of you seems to be slowing down now. Just before you can reach the shine, you collapse onto the ground. It seem that the vial the witch threw at you must've been some kind of poison. Now unable to move, you lay here and watch the sky as you close your eyes one last time. (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "You make your way to this shining light, hopeful that it is the treasure you long for. You try to run, but find that your legs can't keep up. In fact all of you seems to be slowing down now. Just before you can reach the shine, you collapse onto the ground. It seem that the vial the witch threw at you must've been some kind of poison. Now unable to move, you lay here and watch the sky as you close your eyes one last time. (Type: QUIT)"
    },
    {
      "name": "Treasure ending",
      "tags": "",
      "id": "36",
      "score":500,
      "text": "The treasure is a bright golden figurine encrusted with jewels and you know that this must be the treasure you had once heard about. The people back in the village won't believe this! (Type: QUIT)",
      "links": [],
      "hooks": [],
      "cleanText": "The treasure is a bright golden figurine encrusted with jewels and you know that this must be the treasure you had once heard about. The people back in the village won't believe this! (Type: QUIT)"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Adventurer Intro"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves = moves + 1
	if "score" in current_location:
		score = score + current_location["score"]
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing! Want to try again?")