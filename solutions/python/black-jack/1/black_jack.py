def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    val_one = value_of_card(card_one)
    val_two = value_of_card(card_two)

    if val_one > val_two:
        return card_one
    if val_two > val_one:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""
    # If hand already contains an Ace, its value is 11 for calculation
    val_one = 11 if card_one == 'A' else value_of_card(card_one)
    val_two = 11 if card_two == 'A' else value_of_card(card_two)

    # An upcoming Ace is worth 11 if total score stays <= 21, otherwise 1
    if val_one + val_two + 11 <= 21:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack' (Ace + 10-point card)."""
    ten_point_cards = ('10', 'J', 'Q', 'K')
    return (card_one == 'A' and card_two in ten_point_cards) or \
           (card_two == 'A' and card_one in ten_point_cards)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet (total is 9, 10, or 11)."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)