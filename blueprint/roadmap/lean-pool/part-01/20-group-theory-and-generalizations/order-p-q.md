---
declaration: theorem
origin: cited
lean: OrderPQ.exists_card_eq_prime_mul_prime_and_not_isCyclic_iff
statement: formalized
proof: formalized
---

# Classification of groups of order p \* q

> Classification of noncyclic finite groups of order p\*q, including the prime-square direct-product case and the p&lt;q semidirect-product normal form.

*Quoted from the card [LeanPool/projects/order-p-q.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/order-p-q.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`OrderPQ.exists_card_eq_prime_mul_prime_and_not_isCyclic_iff`](https://leanpool.github.io/lean-pool/LeanPool/OrderPQ/Main.html#OrderPQ.exists_card_eq_prime_mul_prime_and_not_isCyclic_iff) (theorem; a main declaration), declared in [LeanPool/OrderPQ/Main.lean, line 34](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OrderPQ/Main.lean#L34): “There exists a noncyclic group of order p\*q exactly when p=q, p divides q-1, or q divides p-1.”
- [`OrderPQ.nonempty_mulEquiv_of_card_eq_prime_mul_prime_of_not_isCyclic`](https://leanpool.github.io/lean-pool/LeanPool/OrderPQ/Main.html#OrderPQ.nonempty_mulEquiv_of_card_eq_prime_mul_prime_of_not_isCyclic) (theorem), declared in [LeanPool/OrderPQ/Main.lean, line 50](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OrderPQ/Main.lean#L50): “Any two noncyclic groups of order p\*q are isomorphic.”
- [`OrderPQ.nonempty_mulEquiv_semidirectProduct_of_card_eq_prime_mul_prime`](https://leanpool.github.io/lean-pool/LeanPool/OrderPQ/Main.html#OrderPQ.nonempty_mulEquiv_semidirectProduct_of_card_eq_prime_mul_prime) (theorem), declared in [LeanPool/OrderPQ/Main.lean, line 73](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OrderPQ/Main.lean#L73): “If p&lt;q, every group of order p\*q is isomorphic to a semidirect product of MulZMod q by MulZMod p.”

## Project

- Authors: Scott Harper, Peiran Wu.
- Source: [arXiv:2501.09769](https://arxiv.org/abs/2501.09769).
- Project repository: [wupr/order-p-q](https://github.com/wupr/order-p-q).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 20D20, 20E22, 20D60.
- In Lean Pool: [LeanPool/OrderPQ](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OrderPQ), from the card [LeanPool/projects/order-p-q.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/order-p-q.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/order-p-q.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/order-p-q.yaml)
- [Lean Pool at 2b205bf9: LeanPool/OrderPQ](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/OrderPQ)
