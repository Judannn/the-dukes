# The Dukes

`A murder mystery game.`<br/>
`This is a single player, adventure text-based game`<br/>
<br/><br/>
Basic Mark down, this can be removed<br/>
# Main heading
## Second level heading
### Third level heading
**Bold** <br/>
***Bold and Italic***
- [ ] Lists
- bullets <br/>
[python:download](https://www.python.org/downloads/) Hyperlinks
> text in a box
> 
`> Another type of text box`

## Introduction




## User Documentation
#### Overview and rules


#### Game play


## Developer Documentation
### Files and resources

### User Requirements Specification

#### Class Diagram

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

    Door -- Room
    NPC -- Room
    Player -- Room
    Item -- Room



    Game -- Player



    

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