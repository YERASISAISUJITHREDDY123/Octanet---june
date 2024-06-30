import time

def main():
    print('Please insert your card')
    time.sleep(1)
    
    password = 5543
    balance = 10000
    transaction_history = []
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            pin = int(input('Enter your PIN: '))
        except ValueError:
            print('Invalid input.Please enter a numeric PIN.')
            attempts += 1
            if attempts == max_attempts:
                print('Maximum attempts reached. Your card is blocked.')
            continue
        
        if pin == password:
            while True:
                print('\n1. Check Balance')
                print('2. Withdraw')
                print('3. Dposit')
                print('4. Transaction History')
                print('5. Transfer')
                print('6. Quit')
                
                try:
                    option = int(input('PLease enter your choice: '))
                except ValueError:
                    print('Please enter a valid option.')
                    continue
                
                if option == 1:
                    print(f'Your current balance is {balance}.')
                elif option == 2:
                    try:
                        withdraw_amt = int(input('Please enter withdraw amount: '))
                    except ValueError:
                        print('Invalid input. Please enter numeric amount: ')
                        continue
                    
                    if withdraw_amt > balance:
                        print('Insufficient balance.')
                    else:
                        balance -= withdraw_amt
                        transaction_history.append(f'Withdraw: {withdraw_amt}')
                        print(f'{withdraw_amt} is debited from your account.')
                        print(f'Your updated balance is {balance}.')
                elif option == 3:
                    try:
                        deposit_amt = int(input('Please enter deposit amount: '))
                    except ValueError:
                        print('Invalid input. Please enter a numeric amount.')
                        continue
                    
                    balance += deposit_amt
                    transaction_history.append(f'Deposited: {deposit_amt}')
                    print(f'{deposit_amt} is credited to your account.')
                    print(f'Your updated value is {balance}.')
                elif option == 4:
                    print('Transaction History:')
                    if not transaction_history:
                        print('No transactions yet.')
                    else:
                        for transaction in transaction_history:
                            print(transaction)
                elif option == 5:
                    try:
                        transfer_amt = int(input('Please enter transfer amount: '))
                        transfer_acc = input('Please enter account number to transfer to: ')
                    except ValueError:
                        print('Invalid input. Please enter numeric amount: ')
                        continue
                    
                    if transfer_amt > balance:
                        print('Insufficient balance.')
                    else:
                        balance -= transfer_amt
                        transaction_history.append(f'Transferred: {transfer_amt} to account {transfer_acc}')
                        print(f'{transfer_amt} is transferred to account {transfer_acc}.')
                        print(f'Your updated balance is {balance}.')
                elif option == 6:
                    print('Thank you for using our service.')
                    break
                else:
                    print('Invalid option. Please try again.')
        else:
            print('Your entered the wrong PIN.')
            attempts += 1
            if attempts == max_attempts:
                print('Maximun attempts reached. Your card is blocked.')
                break
            
if __name__== "__main__":
    main()          