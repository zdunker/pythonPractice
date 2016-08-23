import threading
from test.fork_wait import NUM_THREADS

class BankAccount():
  def __init__(self, initial_money=0, owner='Anonymous'):
    self.money = initial_money
    self.owner = owner
    # We will keep each write access to money in an history file
    # In order to understand what Python does with your money
    self.history_file = open('./%s.txt' % (owner,), 'w')

  def execute_deposit(self, amount, by='A customer'):

    self.history_file.write('Customer %s is adding %s to bank account of %s containing %s\n' % (by, amount, self.owner, self.money) )
    self.money += amount
    self.history_file.write('Account money after %s deposit: %s\n' % (by, self.money) )

  def __del__(self):
    self.history_file.close()

 

my_account = BankAccount(1000, "WorldCompanyBigBoss")
my_account.execute_deposit(100, "First customer")
my_account.execute_deposit(200, "Second customer")

for i in range(10):
    t = threading.Thread(target=BankAccount.execute_deposit, args=(my_account,4999,'ZDunker'))
    t.start()
