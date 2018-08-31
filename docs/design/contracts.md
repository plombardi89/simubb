# Player Contracts

A league at creation time can choose to operate with one of two contract models: "classic" (reserve clause) or "modern" (fixed length contracts + free agency). 

## Classic Model

In the classic model players, once signed by a team, are owned by that team until they are released or traded. This model is similar to the classic pre-1975 reserve clause system used by Major League Baseball. A player's salary increase or decrease at the end of a season based on a variety of factors such as season performance, career legacy, randomness, age, and actual vs potential skill. The computation will occur automatically by the simulation engine on behalf of the owner.

## Modern Model

In the modern model teams negotiate fixed length contracts with a player and when a contract expires the player becomes an Unrestricted Free Agent ("UFA"). This model is similar to the modern post-1975 Free Agency system used by Major League Baseball.

A player can enter a contract for any duration of time from 1 to 15 years. A contract is is gauranteed in value for its duration. A team can negotiate a new contract at any point up to the time of Free Agency to a player already under its control.

### Minimum Salary

There is a minimum salary of $250,000 per year. A player cannot make less than $250,000 in a single season.

### Maximum Salary

TBD: Likely needed if leagues have a salary cap to avoid unworkable roster situations.

### Drafted Players and Contracts

Every season there is a New Talent Draft. The League Operations Simulator ("LOS") automatically generates a "fair-value" four year contract that factors age, actual skill, and potential skill (over 4 years). When a player is drafted the team automatically assumes responsibility of the generated contract. The team CANNOT renegotiate the contract in the first season but CAN renegotiate the contract in years 2, 3 or 4, however, the Annual Average Value ("AAV") of the contract CANNOT be less than the AAV of the generated contract.

### Ownership Changes

TBD

