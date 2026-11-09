---
declaration: theorem
origin: cited
lean: QuadraticOrder.prime_inert_iff, QuadraticOrder.prime_split_iff
statement: formalized
proof: formalized
---

# Quadratic-order prime classification

> Formalizes foundational algebra for quadratic orders associated to discriminants, including their power basis, norm and discriminant identities, odd-prime splitting/ramification/inertness criteria via Legendre symbols, and root-counting results for quadratic congruences modulo odd prime powers.

*Quoted from the card [LeanPool/projects/singular-moduli.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/singular-moduli.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`QuadraticOrder.prime_inert_iff`](https://leanpool.github.io/lean-pool/LeanPool/SingularModuli/QuadraticOrder/Prime/Inert.html#QuadraticOrder.prime_inert_iff) (theorem; a main declaration), declared in [LeanPool/SingularModuli/QuadraticOrder/Prime/Inert.lean, line 83](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli/QuadraticOrder/Prime/Inert.lean#L83): “Proves that for an odd rational prime p and a valid discriminant d, the ideal (p) is maximal in the quadratic order O_d exactly when the Legendre symbol (d/p) is -1.” Its source, as the card gives it: “C. Geiger, Singular Moduli and the Ideal Class Group, Section 3.2, Proposition 3.2.1.”
- [`QuadraticOrder.prime_ramified_iff`](https://leanpool.github.io/lean-pool/LeanPool/SingularModuli/QuadraticOrder/Prime/Ramified.html#QuadraticOrder.prime_ramified_iff) (theorem), declared in [LeanPool/SingularModuli/QuadraticOrder/Prime/Ramified.lean, line 175](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli/QuadraticOrder/Prime/Ramified.lean#L175): “Proves that for an odd rational prime p and a valid discriminant d, the ideal (p) is not radical in O_d exactly when p divides d.” Its source, as the card gives it: “C. Geiger, Singular Moduli and the Ideal Class Group, Section 3.2, Proposition 3.2.1.”
- [`QuadraticOrder.prime_split_iff`](https://leanpool.github.io/lean-pool/LeanPool/SingularModuli/QuadraticOrder/Prime/Split.html#QuadraticOrder.prime_split_iff) (theorem; a main declaration), declared in [LeanPool/SingularModuli/QuadraticOrder/Prime/Split.lean, line 48](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli/QuadraticOrder/Prime/Split.lean#L48): “Proves that for an odd rational prime p and a valid discriminant d, the ideal (p) is radical but not maximal exactly when the Legendre symbol (d/p) is 1.” Its source, as the card gives it: “C. Geiger, Singular Moduli and the Ideal Class Group, Section 3.2, Proposition 3.2.1.”
- [`QuadraticOrder.cardSqrts_prime_pow_coprime`](https://leanpool.github.io/lean-pool/LeanPool/SingularModuli/QuadraticOrder/RootCounting.html#QuadraticOrder.cardSqrts_prime_pow_coprime) (theorem), declared in [LeanPool/SingularModuli/QuadraticOrder/RootCounting.lean, line 405](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli/QuadraticOrder/RootCounting.lean#L405): “Counts roots of x^2 = c modulo p^n for odd prime p and p not dividing c, giving two roots when the Legendre symbol is 1 and none otherwise.” Its source, as the card gives it: “C. Geiger, Singular Moduli and the Ideal Class Group, Section 3.1.”
- [`QuadraticOrder.cardSqrts_prime_pow_even_val`](https://leanpool.github.io/lean-pool/LeanPool/SingularModuli/QuadraticOrder/RootCounting.html#QuadraticOrder.cardSqrts_prime_pow_even_val) (theorem), declared in [LeanPool/SingularModuli/QuadraticOrder/RootCounting.lean, line 746](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli/QuadraticOrder/RootCounting.lean#L746): “Counts roots of x^2 = p^(2r) u modulo p^n for odd prime p, p not dividing u, and 2r < n, reducing to the coprime case and multiplying by p^r.” Its source, as the card gives it: “C. Geiger, Singular Moduli and the Ideal Class Group, Section 3.1.”
- [`QuadraticOrder.tau_sub_tauConj_sq_of_valid_disc`](https://leanpool.github.io/lean-pool/LeanPool/SingularModuli/QuadraticOrder/Discriminant.html#QuadraticOrder.tau_sub_tauConj_sq_of_valid_disc) (lemma), declared in [LeanPool/SingularModuli/QuadraticOrder/Discriminant.lean, line 62](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli/QuadraticOrder/Discriminant.lean#L62): “Proves the discriminant identity (tau - tauConj)^2 = d for valid quadratic-order discriminants d congruent to 0 or 1 modulo 4.” Its source, as the card gives it: “C. Geiger, Singular Moduli and the Ideal Class Group, Section 2.”

## Project

- Authors: Caleb L. Geiger.
- Source: *Singular Moduli and the Ideal Class Group* by C. Geiger.
- Project repository: [ElodinLaarz/lean-thesis](https://github.com/ElodinLaarz/lean-thesis).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11R11, 11R29, 11A15.
- In Lean Pool: [LeanPool/SingularModuli](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli), from the card [LeanPool/projects/singular-moduli.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/singular-moduli.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/singular-moduli.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/singular-moduli.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SingularModuli](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SingularModuli)
