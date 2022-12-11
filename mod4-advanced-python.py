#!/usr/bin/env python
# coding: utf-8

# In[ ]:


social_graph = {
    "@beatricelui": {
        "first_name": "Bea",
        "last_name": "Lui",
        "following": ["@clare", "@tiong", "@marianne"],
    },
    "@clare": {
        "first_name": "Clare",
        "last_name": "Chua",
        "following": ["@beatricelui", "@tiong"],
    },
    "@marianne": {
        "first_name": "Marianne",
        "last_name": "So",
        "following": ["@slare", "@beatricelui", "@kyla", "@frannyc"],
    },
    "@tiong": {
        "first_name": "Vanessa",
        "last_name": "Tiong",
        "following": [
            "@beatricelui",
            "@marianne",
            "@kyla",
        ],
    },
    "@kyla": {
        "first_name": "Kyla",
        "last_name": "Chua",
        "following": [
            "@tiong",
        ],
    },
}


def relationship_status(from_member, to_member, social_graph):
    
    follower = False
    followed = False
    from_member_following = social_graph.get(from_member).get("following")
    to_member_following = social_graph.get(to_member).get("following")

    if to_member in from_member_following:
        follower = True
    if from_member in to_member_following:
        followed = True

    if follower and followed:
        return "friends"
    elif follower and not followed:
        return "follower"
    elif not follower and followed:
        return "followed"
    else:
        return "no relationship"


from_member = str(input("Person 1: "))
to_member = str(input("Person 2: "))

print(relationship_status(from_member, to_member, social_graph))




board1 = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", "O", "X"],
          ]

board2 = [["O", "X", "X"],
          ["X", "O", "X"],
          ["O", "O", "X"],
          ]

board3 = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", "O", "X"],
          ]

board4 = [["X", "O", "X"],
          ["O", "X", "O"],
          ["X", "O", "X"],
          ]

board5 = [["X", "X", "O"],
          ["O", "O", "X"],
          ["X", "O", "X"],
          ]

board6 = [["O", "O", "O"],
          ["O", "X", "O"],
          ["O", "O", "X"],
          ]


def tic_tac_toe(board):
    if all(not row for row in board):
        return "no winner"
    for row in board:
        if all(x == row[0] for x in row):
            return row[0]
    for col in range(len(board)):
        if all(board[i][col] == board[0][col] for i in range(len(board))):
            return board[0][col]
    if all(board[i][i] == board[0][0] for i in range(len(board))):
        return board[0][0]
    if all(board[i][len(board) - i - 1] == board[0][len(board) - 1] for i in range(len(board))):
        return board[0][len(board) - 1]
    return "no winner"

winner = tic_tac_toe(board2)
print(winner)

legs = {
    ("upd", "admu"): {"travel time mins": 15},
    ("admu", "dlsu"): {"travel time mins": 75},
    ("dlsu", "upd"): {"travel time mins": 65},
}


def eta(first_stop, second_stop, route_map):
    return route_map[(first_stop, second_stop)].get("travel time mins")


from_place = str(input("From: "))
to_place = str(input("To: "))
print(eta(from_place, to_place, legs), "mins")


# In[ ]:




