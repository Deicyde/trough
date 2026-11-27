---
declaration: theorem
origin: cited
lean: OrderPQ.exists_card_eq_prime_mul_prime_and_not_isCyclic_iff
statement: formalized
proof: formalized
---

# Classification of groups of order p \* q

> Classification of noncyclic finite groups of order p\*q, including the prime-square direct-product case and the p`<`q semidirect-product normal form.

*Quoted from the card [LeanPool/projects/order-p-q.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/order-p-q.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`OrderPQ.exists_card_eq_prime_mul_prime_and_not_isCyclic_iff`](https://leanpool.github.io/lean-pool/LeanPool/OrderPQ/Main.html#OrderPQ.exists_card_eq_prime_mul_prime_and_not_isCyclic_iff) (theorem; a main declaration), declared in [LeanPool/OrderPQ/Main.lean, line 34](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderPQ/Main.lean#L34): “There exists a noncyclic group of order p\*q exactly when p=q, p divides q-1, or q divides p-1.”
- [`OrderPQ.nonempty_mulEquiv_of_card_eq_prime_mul_prime_of_not_isCyclic`](https://leanpool.github.io/lean-pool/LeanPool/OrderPQ/Main.html#OrderPQ.nonempty_mulEquiv_of_card_eq_prime_mul_prime_of_not_isCyclic) (theorem), declared in [LeanPool/OrderPQ/Main.lean, line 50](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderPQ/Main.lean#L50): “Any two noncyclic groups of order p\*q are isomorphic.”
- [`OrderPQ.nonempty_mulEquiv_semidirectProduct_of_card_eq_prime_mul_prime`](https://leanpool.github.io/lean-pool/LeanPool/OrderPQ/Main.html#OrderPQ.nonempty_mulEquiv_semidirectProduct_of_card_eq_prime_mul_prime) (theorem), declared in [LeanPool/OrderPQ/Main.lean, line 73](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderPQ/Main.lean#L73): “If p`<`q, every group of order p\*q is isomorphic to a semidirect product of MulZMod q by MulZMod p.”

## Project

- Authors: Scott Harper, Peiran Wu.
- Source: [arXiv:2501.09769](https://arxiv.org/abs/2501.09769).
- Project repository: [wupr/order-p-q](https://github.com/wupr/order-p-q).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 20D20, 20E22, 20D60.
- In Lean Pool: [LeanPool/OrderPQ](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderPQ), from the card [LeanPool/projects/order-p-q.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/order-p-q.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/order-p-q.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/order-p-q.yaml)
- [Lean Pool at bb99e52c: LeanPool/OrderPQ](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/OrderPQ)
