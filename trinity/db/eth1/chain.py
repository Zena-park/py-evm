from abc import abstractmethod
from typing import (
    Dict,
    Iterable,
    List,
    Sequence,
    Type,
)

from eth_typing import Hash32

from eth.abc import (
    BlockAPI,
    BlockHeaderAPI,
    ReceiptAPI,
    SignedTransactionAPI,
)
from eth.db.chain import ChainDB

from trinity._utils.asyncio import async_thread_method
from trinity.db.eth1.header import BaseAsyncHeaderDB


class BaseAsyncChainDB(BaseAsyncHeaderDB, ChainDB):
    """
    Abstract base class for the async counterpart to ``ChainDatabaseAPI``.
    """

    @abstractmethod
    async def coro_exists(self, key: bytes) -> bool:
        ...

    @abstractmethod
    async def coro_get(self, key: bytes) -> bytes:
        ...

    @abstractmethod
    async def coro_persist_block(self, block: BlockAPI) -> None:
        ...

    @abstractmethod
    async def coro_persist_uncles(self, uncles: Sequence[BlockHeaderAPI]) -> Hash32:
        ...

    @abstractmethod
    async def coro_persist_trie_data_dict(self, trie_data_dict: Dict[Hash32, bytes]) -> None:
        ...

    @abstractmethod
    async def coro_get_block_transactions(
            self,
            header: BlockHeaderAPI,
            transaction_class: Type[SignedTransactionAPI]) -> Iterable[SignedTransactionAPI]:
        ...

    @abstractmethod
    async def coro_get_block_uncles(self, uncles_hash: Hash32) -> List[BlockHeaderAPI]:
        ...

    @abstractmethod
    async def coro_get_receipts(
            self, header: BlockHeaderAPI, receipt_class: Type[ReceiptAPI]) -> List[ReceiptAPI]:
        ...


class AsyncChainDB(BaseAsyncChainDB):
    coro_exists = async_thread_method(BaseAsyncChainDB.exists)
    coro_get = async_thread_method(BaseAsyncChainDB.get)
    coro_get_block_header_by_hash = async_thread_method(BaseAsyncChainDB.get_block_header_by_hash)
    coro_get_canonical_head = async_thread_method(BaseAsyncChainDB.get_canonical_head)
    coro_get_score = async_thread_method(BaseAsyncChainDB.get_score)
    coro_header_exists = async_thread_method(BaseAsyncChainDB.header_exists)
    coro_get_canonical_block_hash = async_thread_method(BaseAsyncChainDB.get_canonical_block_hash)
    coro_get_canonical_block_header_by_number = async_thread_method(BaseAsyncChainDB.get_canonical_block_header_by_number)  # noqa: E501
    coro_persist_header = async_thread_method(BaseAsyncChainDB.persist_header)
    coro_persist_header_chain = async_thread_method(BaseAsyncChainDB.persist_header_chain)
    coro_persist_block = async_thread_method(BaseAsyncChainDB.persist_block)
    coro_persist_header_chain = async_thread_method(BaseAsyncChainDB.persist_header_chain)
    coro_persist_uncles = async_thread_method(BaseAsyncChainDB.persist_uncles)
    coro_persist_trie_data_dict = async_thread_method(BaseAsyncChainDB.persist_trie_data_dict)
    coro_get_block_transactions = async_thread_method(BaseAsyncChainDB.get_block_transactions)
    coro_get_block_uncles = async_thread_method(BaseAsyncChainDB.get_block_uncles)
    coro_get_receipts = async_thread_method(BaseAsyncChainDB.get_receipts)
