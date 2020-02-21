import sys
import random
import os
import ascii_art

# This is our first 'function'.  Functions can be called from any other point in our code, which makes them very
# reusable. Using functions often simplifies our code. This function check which type of computer we are on and calls
# the correct clear screen command.
def clear_screen():
    if os.name == "posix":
        os.system('clear')  # Assume on MacOS System
    else:
        os.system('cls')  # Assume on Windows System


intro_msg_1 = "Thank You Goblin Warrior for coming to save our town from raiding goblins!"
intro_msg_2 = "You came just in time.  The Goblin Horde has just arrived..."

goblin_count_msg_1 = "There stands "
goblin_count = random.randint(10, 20)
goblin_count_msg_2 = " snarling and spitting goblins before you."

health_stat = 100

hut_count_msg_1 = "There are "
hut_count = random.randint(10, 30)
hut_count_msg_2 = " huts in the village to defend."

your_move_msg = "What will you do: (A)ttack, (H)ide, Review (S)tats, or (Q)uit? "

pre_bar = "+-----------------------"
post_bar = "----------------------+"

attack_msg_1 = "  You swing your mighty sword through the goblin horde, killing "
attack_msg_2 = " goblin(s)!"

heal_msg_1 = "  You duck into a nearby hut, taking a moment to bandage up yourself.  You heal "
heal_msg_2 = "%"

goblin_burn_msg_1 = "  The goblins take advantage of your disappearance and torch "
goblin_burn_msg_2 = " hut(s)!"

goblin_attack_msg_1 = "  The goblins claw and bite you! taking your health down by "
goblin_attack_msg_2 = "%!"

quit_msg_1 = "  You throw down your sword, sobbing into your hands as you flee the goblins!!!\n"
quit_msg_2 = "  The villagers homes are destroyed and they are forced to move out as the goblins take over the town."

slain_msg = "  You are slain! The goblins run over your body and rush into the town, burning and destroying everything!"
village_burned_msg = "  The goblins have burnt down the entire village! The villagers are forced to move out as the " \
                     "goblins take over the town! You failed!!! "
victory_msg_1 = "  You defeated all the goblins! The villagers carry you on their backs and proclaim you their king of " \
                "the land! "
victory_msg_2 = "  You are given free reign and a castle! Congratulations, Goblin Warrior!"

clear_screen()
print(ascii_art.goblin_warrior_title)
print(intro_msg_1)
print(intro_msg_2)
print("")
print(goblin_count_msg_1 + str(goblin_count) + goblin_count_msg_2)
print(hut_count_msg_1 + str(hut_count) + hut_count_msg_2)
while health_stat > 0 and goblin_count > 0 and hut_count > 0:
    print("")
    nextMove = raw_input(your_move_msg)
    clear_screen()
    # Attacking kills goblins, but you also take damage
    if nextMove == "A" or nextMove == "a":
        print(pre_bar + " You Attack! " + post_bar)
        # Attack the Goblins
        clobbered_goblins = random.randint(0, 5)
        # If we kill more goblins than exist, set clobbered to remaining
        if clobbered_goblins > goblin_count:
            clobbered_goblins = goblin_count
        goblin_count = goblin_count - clobbered_goblins
        print(attack_msg_1 + str(clobbered_goblins) + attack_msg_2)
        # Goblins Attack You
        goblin_damage = random.randint(0, 3) * goblin_count
        health_stat = health_stat - goblin_damage
        print(goblin_attack_msg_1 + str(goblin_damage) + goblin_attack_msg_2)
        print(pre_bar + " You Attack! " + post_bar)

    # Hiding allows you to heal, but also allows the goblins to burn huts.
    if nextMove == "H" or nextMove == "h":
        print(pre_bar + " You Hide! " + post_bar)
        # Hide and Heal
        healing = random.randint(2, 15)
        # If we heal more than 100%, then just heal to 100%
        if (healing + health_stat) > 100:
            healing = 100 - health_stat
        health_stat = health_stat + healing
        print(heal_msg_1 + str(healing) + heal_msg_2)
        # Goblins Burn Huts
        goblin_damage = random.randint(0, 5)
        hut_count = hut_count - goblin_damage
        print(goblin_burn_msg_1 + str(goblin_damage) + goblin_burn_msg_2)
        print(pre_bar + " You Hide! " + post_bar)

    # Check your stats to see how you are doing.
    if nextMove == "S" or nextMove == "s":
        print(pre_bar + " Stats " + post_bar)
        print("    Health  : " + str(health_stat) + "%")
        print("    Goblins : " + str(goblin_count))
        print("    Huts    : " + str(hut_count))
        print(pre_bar + " Stats " + post_bar)

    if nextMove == "Q" or nextMove == "q":
        print(pre_bar + " You Quit! " + post_bar)
        sys.exit(quit_msg_1 + quit_msg_2)

print("")
# If your health falls below 0, you die
if health_stat <= 0:
    print(ascii_art.grim_reaper)
    print(slain_msg)
# If hut count falls below 0, the village is destroyed
if hut_count <= 0:
    print(ascii_art.monkey)
    print(village_burned_msg)
# If goblin count goes below 0, you win!
if goblin_count <= 0:
    print(ascii_art.castle)
    print(victory_msg_1)
    print(victory_msg_2)
