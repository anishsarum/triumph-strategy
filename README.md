# Triumph - Strategy Game
A 4 player turn-based strategy game made on Python 3 and Pygame, where the aim of the game is for a player to conquer all the land available in the map. 3 different maps with different sizes can be chosen, with the possibility of players to create more if they wish.

## Maps
- Small - 10x10
- Medium - 15x15 (minimum 1080p display required)
- Big - 20x20 (minimum 1440p display required)
- Create your own by editing the map text files.

## Rules
- All Players start with 10 gold each.
- All units have 10hp
- Players earn gold equal to the amount of tiles their unit owns per turn.
- The team's turn is indicated at the bottom.
- Each tile has an outline relative to the team which owns it.
- Select units from the right of the board.
- Then after selecting, click on a tile that your unit owns to place there.
- Each unit has different costs.
- When it's your turn, click on one of your units and click to an adjacent square to move there.
- Number of movement points each unit has indicated at the bottom.
- When your unit is adjacent to an enemy unit it can attack it by clicking on your unit then the enemy unit.
- Ground (infantry and tanks) units are on a separate plane from Air (bomber and fighter) units, cannot attack each other except for the bomber unit.
- Bomber is unique in that it can attack ground units by clicking the same tile it is on, twice.
- Win the game by being the team to own all other tiles, or if the opponents give up.

## Units
- Infantry unit   
  - 2 gold per unit   
   - 1 damage  
   - 1 movement point 
   - good for holding ground
- Tank unit       
  - 20 gold per unit  
  - 5 damage  
  - 5 movement points 
  - good for advancing and conquering new provinces
- Bomber unit     
  - 30 gold per unit  
  - 5 damage  
  - 5 movement points 
  - good for advancing and destroying ground units (1 damage to fighters)
- Fighter unit    
  - 20 gold per unit  
  - 5 damage  
  - 5 movement points 
  - good for destroying bombers
