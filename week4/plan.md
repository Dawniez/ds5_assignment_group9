# Blackjack Game Plan

## Prompt

**Role:** You are an experienced Python developer and software architect.

**Goal:** Create a detailed step-by-step plan to build a text-based 
Blackjack game in Python. The plan should cover all the components 
needed to build the game from scratch.

**Constraints:**
- The game uses one standard 52-card deck (ranks 2-10, J, Q, K, A 
  with suits C, D, H, S)
- Cards are drawn without replacement and the deck is shuffled each round
- Aces count as 11 but demote to 1 if the hand exceeds 21
- The player sees both their cards and one dealer card before each decision
- The player can only input H (hit) or S (stand) — invalid input 
  should re-prompt
- The dealer draws until reaching 17 or higher
- Print full hands of both players at the end with the outcome 
  (You won/Dealer won)
- Do not write actual code, only provide the plan

## Plan

### Step 1: Set up the deck
- Create a list of all 52 cards (ranks × suits)
- Represent each card consistently as a rank and suit pair, such as `(A, S)`
- Build a shuffle function
- Remove each card from the deck when it is drawn so cards cannot repeat

### Step 2: Card values
- 2-10 = face value
- J, Q, K = 10
- Ace = 11 or 1

### Step 3: Hand value calculator
- Sum all card values
- If total > 21 and the hand contains an Ace counted as 11, demote that Ace to 1
- Repeat ace demotion when a hand contains multiple Aces
- Return the best possible total, with 21 preferred over a lower total

### Step 4: Deal initial cards
- Give player 2 cards face up
- Give dealer 2 cards, one face up one face down

### Step 5: Player turn
- Print player's cards, running total and dealer's up card
- Ask for H or S input
- Convert input to uppercase so both `H`/`h` and `S`/`s` are accepted
- If invalid input, re-prompt until the player enters H or S
- If H: draw card, recalculate hand, check for bust
- If bust: player loses immediately
- If S: move to dealer turn

### Step 6: Dealer turn
- Reveal hidden card
- Dealer draws until total is 17 or higher
- If dealer busts: player wins

### Step 7: Determine winner
- Compare totals if neither busted
- Higher total wins
- If equal: dealer wins
- Decide how an opening Blackjack is treated; unless a special rule is added, treat it as a normal total of 21

### Step 8: Print final result
- Show full hands of both players
- Print "You won" or "Dealer won"

## Testing Plan

- Confirm that a new deck contains exactly 52 unique cards.
- Confirm that drawing a card reduces the deck size by one and adds the card to the hand.
- Test number cards, face cards, and Aces individually.
- Test a hand with one Ace that must change from 11 to 1.
- Test a hand with multiple Aces that requires more than one demotion.
- Test invalid player input and confirm that the program asks again.
- Test a player bust, a dealer bust, and a player who stands below 21.
- Test totals where the player wins, the dealer wins, and both totals are equal.
- Confirm that the final output reveals both complete hands.

## Implementation Notes

- Keep deck creation, card scoring, turns, winner selection, and output as separate functions.
- Use a main game function to control one complete round.
- Start the game only from the main entry point so individual functions can be tested independently.
- Do not add multiple rounds, betting, insurance, or splitting unless the assignment requirements are expanded.