from web3 import Web3 

web3 = Web3(Web3.HTTPProvider('')) # - web3 API should be taken from https://infuria.io

from_account = '' 
to_account = ''

private_key = '' # - https://support.metamask.io/hc/en-us/articles/360015289632-How-to-export-an-account-s-private-key#:~:text=Click%20on%20the%20account%20button,on%20'Show%20private%20key'.

address_1 = web3.toChecksumAddress(from_account)
address_2 = web3.toChecksumAddress(to_account)

nonce = web3.eth.getTransactionCount(address_1)

tx = {
    'nonce': nonce,
    'to': address_2, 
    'value': web3.toWei(0.05, 'ether'), # - Amount of transfering ETH
    'gas': 40000,
    'gasPrice': web3.toWei(10, 'gwei') # - https://etherscan.io/gastracker
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_transaction = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

Hash = print('Hash of transaction: ', web3.toHex(tx_transaction)) # - Hash of transaction to track a transfer on https://etherscan.com