
def test_data_loader():
    
    player = Person("John", 25)
    player.abilities = PersonAbilities()

    player.abilities.add_ability("strength", 10)
    player.abilities.add_ability("intelligence", 8)
    player.abilities.add_ability("charisma", 5)

    print(player.abilities.get_ability("strength"))  # Output: 10

    player.abilities.modify_ability("strength", 2)  # Improve strength
