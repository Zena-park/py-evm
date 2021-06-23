from eth_keys import keys
from eth_utils import decode_hex
from eth_typing import Address

from eth.consensus.pow import mine_pow_nonce
from eth import constants, chains
##from eth.vm.forks.byzantium import ByzantiumVM
from eth.vm.forks.simple import SimpleVM

from eth.db.backends.memory import MemoryDB


GENESIS_PARAMS = {
    'parent_hash': constants.GENESIS_PARENT_HASH,
    'uncles_hash': constants.EMPTY_UNCLE_HASH,
    'coinbase': constants.ZERO_ADDRESS,
    'transaction_root': constants.BLANK_ROOT_HASH,
    'receipt_root': constants.BLANK_ROOT_HASH,
    'difficulty': 1,
    'block_number': constants.GENESIS_BLOCK_NUMBER,
    'gas_limit': constants.GENESIS_GAS_LIMIT,
    'timestamp': 1514764800,
    'extra_data': constants.GENESIS_EXTRA_DATA,
    'nonce': constants.GENESIS_NONCE
}

SENDER_PRIVATE_KEY = keys.PrivateKey(
  decode_hex('0x45a915e4d060149eb4365960e6a7a45f334393093061116b197e3240065ff2d8')
)

SENDER = Address(SENDER_PRIVATE_KEY.public_key.to_canonical_address())

RECEIVER = Address(b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\x02')

GENESIS_STATE = {
    SENDER: {
        "balance" : 10**20,
        "nonce" : 0,
        "code" : b'0x6080604052600436106100fc576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063158ef93e146101015780633bebf51914610130578063622bda58146101a757806362eb5d98146101fe578063844ada9414610241578063857184d1146102c457806392d0d1531461031b5780639b4e735f14610346578063b7b0422d146103c9578063bcac9736146103f6578063c35082a91461045b578063d1c0c042146104d2578063d3aceae214610537578063e1e158a51461058e578063e842a64b146105b9578063f340fa0114610614578063f3fef3a314610662578063f8b2cb4f146106c7575b600080fd5b34801561010d57600080fd5b5061011661071e565b604051808215151515815260200191505060405180910390f35b34801561013c57600080fd5b50610191600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610731565b6040518082815260200191505060405180910390f35b3480156101b357600080fd5b506101e8600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610756565b6040518082815260200191505060405180910390f35b34801561020a57600080fd5b5061023f600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061076e565b005b34801561024d57600080fd5b50610282600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506107f4565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156102d057600080fd5b50610305600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610827565b6040518082815260200191505060405180910390f35b34801561032757600080fd5b50610330610870565b6040518082815260200191505060405180910390f35b34801561035257600080fd5b50610387600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610876565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156103d557600080fd5b506103f4600480360381019080803590602001909291905050506108de565b005b34801561040257600080fd5b50610441600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019092919050505061091f565b604051808215151515815260200191505060405180910390f35b34801561046757600080fd5b506104bc600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610a61565b6040518082815260200191505060405180910390f35b3480156104de57600080fd5b5061051d600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610ae8565b604051808215151515815260200191505060405180910390f35b34801561054357600080fd5b50610578600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610b8e565b6040518082815260200191505060405180910390f35b34801561059a57600080fd5b506105a3610ba6565b6040518082815260200191505060405180910390f35b3480156105c557600080fd5b506105fa600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610bac565b604051808215151515815260200191505060405180910390f35b610648600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610d62565b604051808215151515815260200191505060405180910390f35b34801561066e57600080fd5b506106ad600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919080359060200190929190505050610f92565b604051808215151515815260200191505060405180910390f35b3480156106d357600080fd5b50610708600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506111f9565b6040518082815260200191505060405180910390f35b600560009054906101000a900460ff1681565b6003602052816000526040600020602052806000526040600020600091509150505481565b60026020528060005260406000206000915090505481565b600260008273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054600160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555050565b60006020528060005260406000206000915054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b60045481565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b600560009054906101000a900460ff161515156108fa57600080fd5b806006819055506001600560006101000a81548160ff02191690831515021790555050565b600080600080600260008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549250600160008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549150818583011115156109b957600080fd5b848201905082811115610a0f5782600160008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610a54565b80600160008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505b6001935050505092915050565b6000600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905092915050565b600080600160008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905080838203101515610b3d57600080fd5b828103600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550600191505092915050565b60016020528060005260406000206000915090505481565b60065481565b6000806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050826000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055507f5884d7e3ec123de8e772bcf576c18dcdad75b056c4314f999ed966693419c692338285604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001935050505060405180910390a16001915050919050565b60008060006006543410151515610d7857600080fd5b600260008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549150600360003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054905081348301111515610e4957600080fd5b80348201111515610e5957600080fd5b348201600260008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550348101600360003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508373ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8752a472e571a816aea92eec8dae9baf628e840f4929fbcc2d155e6233ff68a7346040518082815260200191505060405180910390a3600192505050919050565b6000806000600260008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549150600360003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490508184830310151561106857600080fd5b8084820310151561107857600080fd5b838203600260008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550838103600360003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055503373ffffffffffffffffffffffffffffffffffffffff166108fc859081150290604051600060405180830381858888f19350505050158015611187573d6000803e3d6000fd5b508473ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f2717ead6b9200dd235aad468c9809ea400fe33ac69b5bfaa6d3e90fc922b6398866040518082815260200191505060405180910390a360019250505092915050565b6000600160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490509190505600a165627a7a7230582007692e4dbb478be658c92d6b85e63623d7d77a59daf4f5b52e0425531dbe946a0029',
        "storage" : {}
    }
}

klass = chains.base.MiningChain.configure(
    __name__='TestChain',
    vm_configuration=(
        (constants.GENESIS_BLOCK_NUMBER, SimpleVM),
    ))

chain = klass.from_genesis(MemoryDB(), GENESIS_PARAMS, GENESIS_STATE)



######### Tx1 ###########################
# nonce = vm.get_transaction_nonce(SENDER)
vm = chain.get_vm()
nonce = vm.state.account_db.get_nonce(SENDER)

tx1 = vm.create_unsigned_transaction(
    nonce=nonce,
    gas_price=0,
    gas=100000,
    to=RECEIVER,
    value=0,
    data=b'',
)

signed_tx1 = tx1.as_signed_transaction(SENDER_PRIVATE_KEY)

chain.apply_transaction(signed_tx1)

# We have to finalize the block first in order to be able read the
# attributes that are important for the PoW algorithm
block = chain.get_vm().finalize_block(chain.get_block())

# based on mining_hash, block number and difficulty we can perform
# the actual Proof of Work (PoW) mechanism to mine the correct
# nonce and mix_hash for this block
nonce, mix_hash = mine_pow_nonce(
    block.number,
    block.header.mining_hash,
    block.header.difficulty)

block = chain.mine_block(mix_hash=mix_hash, nonce=nonce)

print("BLOCK1 SENDER BALANCE : {}".format(vm.state.account_db.get_balance(SENDER)))
print("BLOCK1 RECEIVER BALANCE : {}".format(vm.state.account_db.get_balance(RECEIVER)))

######### Tx2 ###########################
# nonce = vm.get_transaction_nonce(SENDER)
vm = chain.get_vm()
nonce = vm.state.account_db.get_nonce(SENDER)

tx2 = vm.create_unsigned_transaction(
    nonce=nonce,
    gas_price=0,
    gas=100000,
    to=RECEIVER,
    value=10**18,
    data=b'',
)

signed_tx2 = tx2.as_signed_transaction(SENDER_PRIVATE_KEY)

chain.apply_transaction(signed_tx2)

# We have to finalize the block first in order to be able read the
# attributes that are important for the PoW algorithm
block = chain.get_vm().finalize_block(chain.get_block())

# based on mining_hash, block number and difficulty we can perform
# the actual Proof of Work (PoW) mechanism to mine the correct
# nonce and mix_hash for this block
nonce, mix_hash = mine_pow_nonce(
    block.number,
    block.header.mining_hash,
    block.header.difficulty)

block = chain.mine_block(mix_hash=mix_hash, nonce=nonce)
vm = chain.get_vm()

print("BLOCK2 SENDER BALANCE : {}".format(vm.state.account_db.get_balance(SENDER)))
print("BLOCK2 RECEIVER BALANCE : {}".format(vm.state.account_db.get_balance(RECEIVER)))
print("GET CODE : {}".format(vm.state.account_db.get_code(SENDER)))