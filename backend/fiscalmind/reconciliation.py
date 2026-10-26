"""Geração de sugestões; não confirma nem grava conciliações."""
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Entry:
    company_id: str
    entry_id: str
    amount_cents: int
    date: date

    def __post_init__(self):
        if not self.company_id or not self.entry_id:
            raise ValueError("company_id e entry_id são obrigatórios")
        if type(self.amount_cents) is not int or self.amount_cents <= 0:
            raise ValueError("amount_cents deve ser inteiro positivo")
        if type(self.date) is not date:
            raise ValueError("date deve ser uma data")


@dataclass(frozen=True)
class Suggestion:
    document_id: str
    transaction_id: str
    days_apart: int
    reason: str


def suggest(document: Entry, transactions: list[Entry], max_days: int = 7) -> list[Suggestion]:
    """Mesma empresa e valor exato; data em até max_days. Nunca confirma."""
    if type(max_days) is not int or max_days < 0:
        raise ValueError("max_days deve ser inteiro não negativo")
    results = []
    for transaction in transactions:
        days = abs((transaction.date - document.date).days)
        if (transaction.company_id == document.company_id
                and transaction.amount_cents == document.amount_cents
                and days <= max_days):
            results.append(Suggestion(document.entry_id, transaction.entry_id, days,
                                      f"Mesmo valor; datas com diferença de {days} dia(s)."))
    return sorted(results, key=lambda item: (item.days_apart, item.transaction_id))
