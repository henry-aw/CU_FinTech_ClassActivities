# Ethereum Account Functions

################################################################################

# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3.auto.infura.kovan import w3
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
################################################################################

# Create a function called `generate_account` that automates the Ethereum
# account creation process
def generate_account():
    """Create a digital wallet and Ethereum account from a mnemonic seed phrase."""
    # Access the mnemonic phrase from the `.env` file
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet object instance
    wallet = Wallet(mnemonic)

    # Derive Ethereum private key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    # Return the account from the function
    return account


# @TODO
# Create a function called `get_balance` that calls the Kovan testnet, converts the wei balance of the account to ether, and returns the value of ether






# @TODO
# Create a function called `send_transaction` that creates a raw transaction, signs it, and sends it over the Kovan testnet. Return the confirmation hash from the transaction
