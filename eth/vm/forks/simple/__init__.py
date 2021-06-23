from typing import (
    Type,
)

from eth.abc import (
    BlockHeaderAPI,
    ComputationAPI,
    ReceiptAPI,
    SignedTransactionAPI,
    StateAPI,
)
from eth.rlp.blocks import BaseBlock
from eth.vm.forks import (
    BerlinVM,
)
from eth.vm.forks.byzantium.constants import (
    EIP658_TRANSACTION_STATUS_CODE_FAILURE,
    EIP658_TRANSACTION_STATUS_CODE_SUCCESS,
)
from eth.vm.state import BaseState

from .blocks import SimpleBlock
from .headers import (
    compute_simple_difficulty,
    configure_simple_header,
    create_simple_header_from_parent,
)
from .state import SimpleState


def finalize_gas_used(transaction: SignedTransactionAPI, computation: ComputationAPI) -> int:
    gas_remaining = computation.get_gas_remaining()
    consumed_gas = transaction.gas - gas_remaining

    gross_refund = computation.get_gas_refund()
    max_refund = consumed_gas // 2
    gas_refund = min(gross_refund, max_refund)

    return consumed_gas - gas_refund


class SimpleVM(BerlinVM):
    # fork name
    fork = 'simple'

    # classes
    block_class: Type[BaseBlock] = SimpleBlock
    _state_class: Type[BaseState] = SimpleState

    # Methods
    create_header_from_parent = staticmethod(create_simple_header_from_parent)  # type: ignore
    compute_difficulty = staticmethod(compute_simple_difficulty)    # type: ignore
    configure_header = configure_simple_header

    @staticmethod
    def make_receipt(
            base_header: BlockHeaderAPI,
            transaction: SignedTransactionAPI,
            computation: ComputationAPI,
            state: StateAPI) -> ReceiptAPI:

        gas_used = base_header.gas_used + finalize_gas_used(transaction, computation)

        if computation.is_error:
            status_code = EIP658_TRANSACTION_STATUS_CODE_FAILURE
        else:
            status_code = EIP658_TRANSACTION_STATUS_CODE_SUCCESS

        return transaction.make_receipt(status_code, gas_used, computation.get_log_entries())
