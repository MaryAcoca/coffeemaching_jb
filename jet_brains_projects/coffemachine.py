# cup_amount = int(input())
# print('For', cup_amount, 'cups of coffee you will need:')
# print( cup_amount * 200, 'ml of water')
# print(cup_amount * 50, 'ml of milk')
# print(cup_amount * 15, 'g of coffee beans')

# water = int(input('Write how many ml of water the coffee machine has:'))
# milk = int(input('Write how many ml of milk the coffee machine has:'))
# coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))
# cups = int(input('Write how many cups of coffee you will need:'))

# if water >= 200 and milk >= 50 and coffee >= 15:
#    amount_water = water//200
#    amount_milk = milk//50
#    amount_coffee = coffee//15
#    amount_cups = min(amount_water, amount_milk, amount_coffee)
#    if amount_cups == cups:
#        print('Yes, I can make that amount of coffee')
#    elif amount_cups > cups:
#        more_cups = amount_cups - cups
#        print('Yes, I can make that amount of coffee (and even', more_cups, 'more than that)')
#    else:
#        print('No, I can make only', amount_cups, 'cups of coffee')


class CoffeMachine():
    money = 550
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
  
    def user_buy(self):
        if coffee_choice == '1':
            if CoffeMachine.water >= 250 and CoffeMachine.disposable_cups >= 1 and CoffeMachine.coffee_beans >= 16:
                 print('I have enough resources, making you a coffee!')
                 CoffeMachine.water -= 250
                 CoffeMachine.coffee_beans -= 16
                 CoffeMachine.disposable_cups -= 1
                 CoffeMachine.money += 4
            elif CoffeMachine.water < 250:
             print('Sorry, not enough water!')
            elif CoffeMachine.disposable_cups < 1:
             print('Sorry, not enough cups!')
            elif CoffeMachine.coffee_beans < 16:
             print('Sorry, not enough coffee beans!')
        elif coffee_choice == '2':
            if CoffeMachine.water >= 350 and CoffeMachine.milk >= 75 and CoffeMachine.disposable_cups >= 1 and CoffeMachine.coffee_beans >= 20:
                print('I have enough resources, making you a coffee!')
                CoffeMachine.water -= 350
                CoffeMachine.milk -= 75
                CoffeMachine.coffee_beans -= 20
                CoffeMachine.disposable_cups -= 1
                CoffeMachine.money += 7
            elif CoffeMachine.water < 350:
                print('Sorry, not enough water!')
            elif disposable_cups < 1:
                print('Sorry, not enough cups!')
            elif CoffeMachine.coffee_beans < 20:
                print('Sorry, not enough coffee beans!')
            elif CoffeMachine.milk < 75:
                print('Sorry, not enough milk!')
        elif coffee_choice == '3':
            if CoffeMachine.water >= 200 and CoffeMachine.milk >= 100 and CoffeMachine.disposable_cups >= 1 and CoffeMachine.coffee_beans >= 12:
                print('I have enough resources, making you a coffee!')
                CoffeMachine.water -= 200
                CoffeMachine.milk -= 100
                CoffeMachine.coffee_beans -= 12
                CoffeMachine.disposable_cups -= 1
                CoffeMachine.money += 6
            elif CoffeMachine.water < 200:
                print('Sorry, not enough water!')
            elif CoffeMachine.disposable_cups < 1:
                CoffeMachine.print('Sorry, not enough cups!')
            elif CoffeMachine.coffee_beans < 12:
                print('Sorry, not enough coffee beans!')
            elif CoffeMachine.milk < 100:
                print('Sorry, not enough milk!')

    def user_fill(self):
        user_fill_water = int(input('Write how many ml of water do you want to add:'))
        CoffeMachine.water += user_fill_water
        user_fill_milk = int(input('Write how many ml of milk do you want to add:'))
        CoffeMachine.milk += user_fill_milk
        user_fill_coffee_beans = int(input('Write how many grams of coffee beans do you want to add:'))
        CoffeMachine.coffee_beans += user_fill_coffee_beans
        user_fill_disposable_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        CoffeMachine.disposable_cups += user_fill_disposable_cups

    def user_take(self):
        print('I gave you', self.money)
        CoffeMachine.money -= CoffeMachine.money
        
    def machine_state(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(self.money, "of money")




while True:
    user_action = (input('Write action (buy, fill, take, remaining, exit):'))
    if user_action == 'buy':
        coffee_choice = (input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:'))
        if coffee_choice == 'back':
            continue
        else:
            CoffeMachine().user_buy()
    elif user_action == 'fill':
        CoffeMachine().user_fill()
    elif user_action == 'take':
        CoffeMachine().user_take()
    elif user_action == 'remaining':
        CoffeMachine().machine_state()
    elif user_action == 'exit':
        break
