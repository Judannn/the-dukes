# **The Dukes** <br/>
#### *A murder mystery game.*
<br/>
<br/>

## **Introduction**
This is a murder mystery game where you are dropped into The Dukes house. You are required to figure out who commited the murder by talking to characters and using items.

## **User Documentation**
### Installation Steps
1. Download all files from this Github Repo. <br/>
2. Install colorama to your Python libraries by entering ```pip install colorama``` in your python console.
3. Once colorama is installed within the 'app' folder find 'main.py'
4. You will then run 'main.py' in the python terminal to start up the game.

## Note
This game has been created in Visual Studio Code however issues with Jetbrains have become apparent. <br/>
Edits have been made to allow function in JetBrains however functionality is not as smooth.

### Game play
To play this game you will be required to type inputs and press the <kbd>enter</kbd> key. <br/>
These inputs will be described to you through the game as either interaction options or pre-set inputs, these inputs are described below in the 'User Input Key's section.

### Map
![alt text for screen readers](the_dukes_map.png "Text to show on mouseover")
### Icon Legend
<span style="color:blue">D</span> - Door <br/>
<span style="color:cyan">^</span> - Item <br/>
<span style="color:green">&</span> - NPC <br/>
<span style="color:magenta">@</span> - Player <br/>

### Game Play Input Key's
<kbd>h</kbd> - Opens Help Menu <br/>
<kbd>i</kbd> - Opens Inventory Menu<br/>
<kbd>m</kbd> - Opens Map Menu <br/>
<kbd>0</kbd> or <kbd>1</kbd> or <kbd>2</kbd> or <kbd>3</kbd> - Option Inputs <br/><br/>

## **Developer Documentation**
### Class Diagram
```mermaid
classDiagram
    NPC <|-- Daisy
    NPC <|-- Dog
    NPC <|-- Duke
    NPC <|-- Grandma
    NPC <|-- Luke
    NPC <|-- SherrifRosco

    Item <|-- Battery
    Item <|-- Berries
    Item <|-- DogHair
    Item <|-- Potion
    Item <|-- Concoction
    Item <|-- SilverNecklace
    Item <|-- Water

    Coordinates --* Item
    Coordinates --* Player
    Coordinates --* NPC
    Coordinates --* Door

    InventoryMenu --* Player
    HelpMenu --* Player
    PlayerMap --* Player
    PlayerMap --* Player
    BackPack --* Player

    Door -- Room
    NPC -- Room
    Player -- Room
    Item -- Room

    Player -- Battery
    Player -- Berries
    Player -- DogHair
    Player -- Potion
    Player -- Concoction
    Player -- SilverNecklace
    Player -- Water

    Game -- Player

    NPCReply -- Player
    NPCReply -- NPC
    
    MenuOption -- Player
    MenuOption -- HelpMenu
    MenuOption -- InventoryMenu
    MenuOption -- Game



    class Coordinates{
        +int row
        +int column
    }

    class Door{
        +string graphic_char
        +Coordinates coordinates
        +Room linked_room
        +Door linked_door
        +enter_door()
        +link_door(Door)
    }

    class Game{
        +Player player
        +bool continue_game
        +new_game()
        +game_intro() string
        +run()
        +finish_game()
        +collect_action_options() []
        +has_silver_necklace() bool
        +is_same_coord(first_coordinate, second_coordinate) bool
        +print_console()
        +print_room()
        +print_action_options()
        +print_action_descriptions()
        +print_npc_replies()
        +type_write(print_string, timing)
        +setup(player_name)
    }

    class BackPack{
        +[] _backpack
        +sort()
        +count()
        +list()
        +add(item)
        +remove(item)
        +in_backpack(item) int
    }

    class HelpMenu{
        +open_help()
        +print_menu()
    }

    class InventoryMenu{
        +Player player
        +[] options
        +string description
        +int menu_level
        +setup()
        +open_menu()
        +inventory_action(player_input)
        +collect_item_options()
        +print_menu()
    }

    class Item{
        +string name
        +string graphic_char
        +Coordinates coordinates
        +string description
    }

    class MenuOption{
        +string text
        +object object
    }

    class NPCReply{
        +[] reply_options
        +string reply
        +[] action
        +Item item
        +NPC npc
    }

    class NPC{
        +string name
        +string graphic_char
        +[] item_bag
        +Coordinates coordinates
        +add_item(item)
        +talk(response, player)
    }

    class PlayerMap{
        +[] visited_locations
        +open_map()
        +print_menu()
    }

    class PlayerResponse{
        +string response
        +[] player_items
    }

    class Player{
        +string name
        +[] graphic_char
        +[] item_bag
        +Coordinates coordinates
        +Room current_room
        +bool is_talking
        +[] action_options
        +[] action_descriptions
        +[] npc_replies
        +bool accepted_duke_quest
        +bool drank_concoction
        +bool spoke_to_dog
        +bool spoke_to_luke
        +bool found_murderer
        +InventoryMenu inventory_menu
        +HelpMenu help_menu
        +PlayerMap player_map
        +player_action(player_input)
        +move(key_input)
        +move_up()
        +move_down()
        +move_left()
        +move_right()
        +pick_up_item(Item)
        +talk(NPC, response=None) NPCReply
        +add_action_options(options)
        +add_action_description(action_description)
        +enter_door(door)
        +drink_concoction()
    }

    class Room{
        +string name
        +[] object_list
        +int rows
        +int columns
        +[] room
        +add_object(object)
        +remove_object(object)
        +update_room()
        +room_border()
    }

    class Battery{
        +string name
        +Coordinates coordinates
        +string description
    }

    class Berries{
        +string name
        +Coordinates coordinates
        +string description
    }

    class DogHair{
        +string name
        +Coordinates coordinates
        +string description
    }

    class Potion{
        +string name
        +Coordinates coordinates
        +string description
        +drink(player)
    }

    class Concoction{
        +string name
        +Coordinates coordinates
        +string description
        +drink(player)
    }

    class SilverNecklace{
        +string name
        +Coordinates coordinates
        +string description
    }

    class Water{
        +string name
        +Coordinates coordinates
        +string description
    }

    class Daisy{
        +talk(response, player) NPCReply
    }

    class Dog{
        +talk(response, player) NPCReply
    }

    class Duke{
        +talk(response, player) NPCReply
        +has_all_quest_items(player_items) bool
    }

    class Grandma{
        +talk(response, player) NPCReply
    }

    class Luke{
        +talk(response, player) NPCReply
    }

    class SherrifRosco{
        +talk(response, player) NPCReply
    }
```