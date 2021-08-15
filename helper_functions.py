from itertools import permutations
import numpy as np

def card_generator(li_values=[0, 1, 2, 3], length=3):
    """generate cards given a list of values and the length of tuple."""
    cards = list(permutations(li_values, length))

    return cards

def map_rule_to_action(card, rule):
    action = card[rule]
    return action

def map_action_to_rule(card, action):
    try:
        rule = card.index(action)
    except ValueError:
        rule = 3 #odd response

    return rule

def create_rule_series(total_time):
    rule_series = []
    rules = [0, 1, 2]
    last_rule = None  # To begin with

    while len(rule_series) < total_time:

        available_rules = [x for x in rules if x != last_rule]
        current_rule = np.random.choice(available_rules)
        current_rep = np.random.randint(2, 6)
        rule_series += [current_rule] * current_rep
        last_rule = current_rule

    rule_series = rule_series[:total_time]

    return rule_series
