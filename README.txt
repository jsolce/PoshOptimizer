This is a optimizer for a Posh order that I wrote for my fiance.

The basic logic goes:

	Intake order
	Order descending by price
	Group into sets of 6 (buy 5, get 6th free)
	Using only groups, determine the party level
	Assign hostess rewards by using credit if over 50% of price,
		else use a 1/2 off item
	Print the final order total