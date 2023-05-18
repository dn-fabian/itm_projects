from sample_data import social_graph, board5, legs1

def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph.get(from_member, {}).get("following", []):
        return "follower"
    elif from_member in social_graph.get(to_member, {}).get("following", []):
        return "followed by"
    elif (
        from_member in social_graph.get(to_member, {}).get("following", []) and
        to_member in social_graph.get(from_member, {}).get("following", [])
    ):
        return "friends"
    else:
        return "no relationship"
# Test Case
# print(relationship_status('@joaquin', '@bongolpoc', social_graph))

def tic_tac_toe(board):
    size = len(board)

    # Check rows
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    # Check columns
    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if len(set(column)) == 1:
            return column[0]

    # Check diagonals
    diagonal1 = [board[i][i] for i in range(size)]
    if len(set(diagonal1)) == 1:
        return diagonal1[0]

    diagonal2 = [board[i][size - 1 - i] for i in range(size)]
    if len(set(diagonal2)) == 1:
        return diagonal2[0]

    return "NO WINNER"

# Test Case
# print(tic_tac_toe(board5))

def eta(first_stop, second_stop, route_map):
    # Check if there is a direct leg from first_stop to second_stop
    if (first_stop, second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]

    # Find a path from first_stop to second_stop using multiple legs
    for leg in route_map:
        if leg[0] == first_stop:
            intermediate_stop = leg[1]
            travel_time = route_map[leg]["travel_time_mins"]
            if intermediate_stop == second_stop:
                return travel_time
            else:
                remaining_time = eta(intermediate_stop, second_stop, route_map)
                if remaining_time != -1:
                    return travel_time + remaining_time

    return -1

# Test Case
# print(eta('upd', 'dlsu', legs1))