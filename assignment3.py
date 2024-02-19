def minimax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_terminal(position):
        return get_static_evaluation(position)
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Alpha-Beta Pruning
        return maxEval
    else:
        minEval = float('inf')
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha-Beta Pruning
        return minEval

# Helper functions
def is_terminal(position):
    # Assuming terminal nodes have no children
    return not get_children(position)

def get_static_evaluation(position):
    # This function would return the static evaluation of a position.
    # For the given problem, it would return the terminal node values.
    return position['value']

def get_children(position):
    # This function would return the children of a node in the tree.
    # For the given problem, it would return the connected lower nodes.
    return position['children']

# Construct the tree as a nested dictionary
tree = {
    'value': None,
    'children': [
        {
            'value': None,
            'children': [
                {'value': 4, 'children': []},  # D
                {'value': 6, 'children': []}   # E
            ]
        },
        {
            'value': None,
            'children': [
                {'value': -3, 'children': []},  # F
                {'value': 7, 'children': []}    # G
            ]
        }
    ]
}

# Assuming the root is at depth 3 and it's the maximizer's turn
best_value = minimax(tree, 3, float('-inf'), float('inf'), True)
print("The best value for the maximizer is:", best_value)

# Define the tree structure based on the given problem
tree = {
    'value': None,
    'children': [
        {
            'value': None,
            'children': [
                {'value': -1, 'children': []},  # H
                {'value': 4, 'children': []}    # I
            ]
        },  # D
        {
            'value': None,
            'children': [
                {'value': 2, 'children': []},  # J
                {'value': 6, 'children': []}   # K
            ]
        },  # E
        {
            'value': None,
            'children': [
                {'value': -3, 'children': []},  # L
                {'value': -5, 'children': []}   # M
            ]
        },  # F
        {
            'value': None,
            'children': [
                {'value': 0, 'children': []},  # N
                {'value': 7, 'children': []}   # O
            ]
        }   # G
    ]
}

# Alpha-Beta Pruning Algorithm
def alpha_beta_pruning(node, alpha, beta, maximizing_player):
    if 'children' not in node or not node['children']:
        return node['value']

    if maximizing_player:
        value = float('-inf')
        for child in node['children']:
            value = max(value, alpha_beta_pruning(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break  # Beta cut-off
        return value
    else:
        value = float('inf')
        for child in node['children']:
            value = min(value, alpha_beta_pruning(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                break  # Alpha cut-off
        return value

# Apply the alpha-beta pruning algorithm on the root node
best_value = alpha_beta_pruning(tree, float('-inf'), float('inf'), True)
print("The best value for the maximizer (A) is:", best_value)