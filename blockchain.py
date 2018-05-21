genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Saur'

def get_user_choice():
    """Prompt user for function selection (string)"""

    return input('Please enter a command: ')


def get_transaction_value():
    """Prompt user for transaction value (float)"""
    tx_recipient = input('Enter the recipient of the payment: ')
    tx_amount = float(input('Enter the amount to send: '))
    return (tx_recipient, tx_amount)


def get_last_value():
    """ Returns the last index of the blockchain or None"""

    if len(blockchain) < 1:
        return [0]
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Adds transaction value to blockchain

    Arguments:
        :sender: The sender of the payment
        :recipient: The recipient of the payment
        :amount: The amount of the payment (default = 1.0)
    """
    transaction = {   
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join(str([last_block[key] for key in last_block]))
    print(hashed_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def display_blockchain():
    """Loop over blockchain and print blocks to terminal"""

    for block in blockchain:
        print('\nOutputting block:')
        print(block)
    else:
        print('-' * 20)


def display_open_transactions():
    print(open_transactions)

def verify_chain():
    """Check integrity of blockchain vs last transaction"""

    global blockchain
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
    return is_valid


def main():
    """Prompt for input and carry out instructions until user quits"""

    global blockchain
    waiting_for_input = True

    while waiting_for_input:
        print('\nPlease enter a command: ')
        print('1: Make a payment')
        print('2: Mine a new block')
        print('3: Display open transactions')
        print('4: Display the blockchain')
        print('h: Manipulate the blockchain')
        print('q: Quit the application')
        print('-' * 20)

        user_choice = get_user_choice()

        if user_choice == '1':
            tx_data = get_transaction_value()
            recipient, amount = tx_data
            add_transaction(recipient, amount=amount)
        elif user_choice == '2':
            mine_block()
        elif user_choice == '3':
            display_open_transactions()
        elif user_choice == '4':
            display_blockchain()
        elif user_choice == 'h':
            if len(blockchain) >= 1:
                blockchain[0] = [2]
        elif user_choice == 'q':
            waiting_for_input = False
        else:
            print('\n< Invalid input >')

        # if not verify_chain():
        #     display_blockchain()
        #     print('Error: Invalid blockchain!')
        #     break

# Start program
main()

#End program
print('\nUser logged out')

# List Comprehension
mylist = [1,2,3,4,5,6,7,8,9]
ignore_list = [1, 3, 5, 7, 9]

def double_nums(numbers):
    return [number * 2 for number in numbers if number % 2 == 0]


def filter_nums(numbers, ignore):
    return [el for el in mylist if el not in ignore]

double_nums(mylist)
filter_nums(mylist, ignore_list)

# Dict Comprehension
stats = [('name', 'Aeon'), ('age', 39), ('weight', 200)]
dict_stats = {key: value for (key, value) in stats}
dict_stats