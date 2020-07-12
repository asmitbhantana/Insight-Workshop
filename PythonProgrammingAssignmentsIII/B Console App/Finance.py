class Finance:

    def __init__(self):
        self.accounts = {}

    def create_account(self, name, isStudent=False):
        try:
            self.accounts[name]
            print("Account Already Exist with the same name!")
            return False
        except KeyError:
            self.accounts[name] = {}
            self.accounts[name]['balance'] = 0
            if isStudent:
                self.accounts[name]['balance'] = 2000
            self.accounts[name]["from"] = {}
            print("Created account with name", name)
            return self

    def delete_account(self, name):
        try:
            del self.accounts[name]
        except Exception as e:
            return e

    def get_account_balance(self, name):
        try:
            return self.accounts[name]['balance']
        except Exception as e:
            return e


    def transfer_money(self, balance, t_from, t_to):
        try:
            if self.accounts[t_from][balance] >= balance:
                self.accounts[t_from][balance] -= balance
                self.accounts[t_to][balance] += balance
                try:
                    # sender exists
                    self.accounts[t_to]["from"][t_from]
                    self.accounts[t_to]["from"][t_from] += balance
                except KeyError:
                    # sender doesn't exist
                    self.accounts[t_to]["from"][t_from] = {}
                    self.accounts[t_to]["from"][t_from] = balance
                print(f"{balance} Transfer Success from {t_from} to {t_to}")
                return True
            print("Not sufficient balance!")
            return False
        except Exception as e:
            return e

    def get_transferred_amount(self, t_from, t_to):
        balance = 0
        try:
            balance = self.accounts[t_to]["from"][t_from]
            print("Found some transactions")
        except Exception:
            print("Cannot find any related transactions")
        return balance
