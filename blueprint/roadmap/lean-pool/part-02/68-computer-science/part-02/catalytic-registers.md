---
declaration: theorem
origin: cited
lean: Catalytic.rp_pass_two_iff, Catalytic.four_reg_powering_x13, Catalytic.balancedProdProg_clean
statement: formalized
proof: formalized
---

# Passive catalytic register programs over finite fields and commutative rings

> Characterizes formal polynomial identities computable with two passive catalytic registers and prime-field constants using base-p digit sums. It verifies explicit three-register powering programs, composes them into a four-register construction, and proves exact costs and clean restoration for a balanced multilinear product program with a sufficiently large pool of distinct work registers.

*Quoted from the card [LeanPool/projects/catalytic-registers.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/catalytic-registers.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Catalytic.rp_pass_two_iff`](https://leanpool.github.io/lean-pool/LeanPool/CatalyticRegisters/DigitSumDichotomy.html#Catalytic.rp_pass_two_iff) (theorem; a main declaration), declared in [LeanPool/CatalyticRegisters/DigitSumDichotomy.lean, line 947](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters/DigitSumDichotomy.lean#L947): “For a prime p and input-access budget t ≥ 1, a formal polynomial over the prime field is computable as a formal identity by a clean passive two-register program with prime-field constants exactly when each exponent at least two with nonzero coefficient has base-p digit sum at most min(p − 1, t − 1).”
- [`Catalytic.four_reg_powering_x13`](https://leanpool.github.io/lean-pool/LeanPool/CatalyticRegisters/FourRegisterPowering.html#Catalytic.four_reg_powering_x13) (theorem; a main declaration), declared in [LeanPool/CatalyticRegisters/FourRegisterPowering.lean, line 1174](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters/FourRegisterPowering.lean#L1174): “For N ≥ 1, under the stated invertibility conditions on the certificate coefficient and two factorials, the radix-13 construction computes the Nth power with four registers. Let ℓ be one less than the number of base-13 digits of N. Three times the access count is less than 104 · 8^ℓ.”
- [`Catalytic.balancedProdProg_clean`](https://leanpool.github.io/lean-pool/LeanPool/CatalyticRegisters/BalancedProduct.html#Catalytic.balancedProdProg_clean) (theorem; a main declaration), declared in [LeanPool/CatalyticRegisters/BalancedProduct.lean, line 335](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters/BalancedProduct.lean#L335): “With sign +1, the balanced product program adds the product of 2^k inputs to its target and restores every other register. The work registers must be pairwise distinct and disjoint from the target, with at least k + 1 work registers for k > 0. The pool may be empty at k = 0.”
- [`Catalytic.balancedProdProg_length`](https://leanpool.github.io/lean-pool/LeanPool/CatalyticRegisters/BalancedProduct.html#Catalytic.balancedProdProg_length) (theorem), declared in [LeanPool/CatalyticRegisters/BalancedProduct.lean, line 130](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters/BalancedProduct.lean#L130): “The balanced product program has length balancedOpCount k if k = 0 or the work-register pool has at least k + 1 entries.”
- [`Catalytic.balancedOpCount_formula`](https://leanpool.github.io/lean-pool/LeanPool/CatalyticRegisters/BalancedProduct.html#Catalytic.balancedOpCount_formula) (theorem), declared in [LeanPool/CatalyticRegisters/BalancedProduct.lean, line 108](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters/BalancedProduct.lean#L108): “The exact count balancedOpCount k is (7 · 4^k − 4) / 3 primitives, including input accesses.”

## Project

- Authors: Alexander S. Donahue.
- Source: *Prime-Field Digit-Sum Dichotomy and Improved Three-Register Powering Exponents in Passive Catalytic Register Programs*, [https://github.com/0thernes/catalytic-register-frontiers/blob/c80125c42956ff17e7d6d56c66d94ee9bb57ae33/dist/Donahue_2026_catalytic_register_frontiers.pdf](https://github.com/0thernes/catalytic-register-frontiers/blob/c80125c42956ff17e7d6d56c66d94ee9bb57ae33/dist/Donahue_2026_catalytic_register_frontiers.pdf).
- Project repository: [0thernes/catalytic-register-frontiers](https://github.com/0thernes/catalytic-register-frontiers), at commit [c80125c4](https://github.com/0thernes/catalytic-register-frontiers/tree/c80125c42956ff17e7d6d56c66d94ee9bb57ae33).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 68Q17, 68Q05, 12E20.
- In Lean Pool: [LeanPool/CatalyticRegisters](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters), from the card [LeanPool/projects/catalytic-registers.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/catalytic-registers.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/catalytic-registers.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/catalytic-registers.yaml)
- [Lean Pool at bb99e52c: LeanPool/CatalyticRegisters](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/CatalyticRegisters)
