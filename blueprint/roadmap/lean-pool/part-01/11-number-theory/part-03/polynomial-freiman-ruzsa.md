---
declaration: theorem
origin: cited
lean: Marton.pfr_conjecture
statement: formalized
proof: formalized
---

# The polynomial Freiman–Ruzsa conjecture

> Formalizes Marton's polynomial Freiman–Ruzsa conjecture by the entropy method, including the characteristic-two bounds with exponents twelve and nine, the bounded-torsion theorem with an explicit exponent, and quantitative consequences for affine dimension and approximate homomorphisms. The supporting development builds entropic Ruzsa distance, multidistance, conditional entropy, and additive-energy machinery. This optimized import reuses the pooled Zhang–Yeung entropy and kernel library in place of duplicate upstream modules while preserving all six closed headline statements.

*Quoted from the card [LeanPool/projects/polynomial-freiman-ruzsa.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/polynomial-freiman-ruzsa.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Marton.pfr_conjecture`](https://leanpool.github.io/lean-pool/LeanPool/PFR/Solution.html#Marton.pfr_conjecture) (theorem; a main declaration), declared in [LeanPool/PFR/Solution.lean, line 43](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR/Solution.lean#L43): “A nonempty finite set A of doubling at most K in an abelian group of exponent two is covered by fewer than 2 K^12 cosets of a finite subgroup no larger than A.”
- [`Marton.pfr_conjecture_nine`](https://leanpool.github.io/lean-pool/LeanPool/PFR/Solution.html#Marton.pfr_conjecture_nine) (theorem), declared in [LeanPool/PFR/Solution.lean, line 59](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR/Solution.lean#L59): “Strengthens the characteristic-two covering theorem to fewer than 2 K^9 cosets of a finite subgroup no larger than A.”
- [`Marton.torsion_pfr_conjecture`](https://leanpool.github.io/lean-pool/LeanPool/PFR/Solution.html#Marton.torsion_pfr_conjecture) (theorem), declared in [LeanPool/PFR/Solution.lean, line 99](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR/Solution.lean#L99): “In an abelian group of exponent m at least two, a nonempty finite set of doubling at most K is covered by fewer than m K^(256 m^3 + 1) cosets of a subgroup no larger than A.”
- [`Marton.weak_pfr_int`](https://leanpool.github.io/lean-pool/LeanPool/PFR/Solution.html#Marton.weak_pfr_int) (theorem), declared in [LeanPool/PFR/Solution.lean, line 109](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR/Solution.lean#L109): “A nonempty finite set of doubling at most K in a finite-rank free abelian group has a subset of relative size at least K^(-34) and affine dimension at most (80 / log 2) log K.”
- [`Marton.homomorphism_pfr`](https://leanpool.github.io/lean-pool/LeanPool/PFR/Solution.html#Marton.homomorphism_pfr) (theorem), declared in [LeanPool/PFR/Solution.lean, line 149](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR/Solution.lean#L149): “A map between finite abelian groups of exponent two whose additive defects lie in S differs from a homomorphism by a map taking at most |S|^10 values.”
- [`Marton.approx_hom_pfr`](https://leanpool.github.io/lean-pool/LeanPool/PFR/Solution.html#Marton.approx_hom_pfr) (theorem), declared in [LeanPool/PFR/Solution.lean, line 179](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR/Solution.lean#L179): “A map between finite abelian groups of exponent two that is additive on at least a 1/K fraction of pairs agrees with a homomorphism on at least (|G| / (2^144 K^122) - 1) / 2 points.”

## Project

- Authors: PFR contributors.
- Contributors: Aaron Anderson, Mantas Bakšys, Jonas Bayer, Mauricio Collares, Rémy Degenne, Yaël Dillies, Bhavik Mehta, Ella Yu, Ben Eltschig, Sébastien Gouëzel, Kalle Kytölä, Rob Lewis, Paul Lezeau, Lorenzo Luccioli, Heather Macbeth, Patrick Massot, Arend Mellendijk, Kyle Miller, Pietro Monticone, Kim Morrison, Oliver Nash, Utensil Song, Terence Tao, Floris van Doorn, Sky Wilshaw, Lawrence Wu.
- Source: *Marton's conjecture (the polynomial Freiman–Ruzsa conjecture)* by W. T. Gowers, Ben Green, Freddie Manners, Terence Tao, [arXiv:2311.05762](https://arxiv.org/abs/2311.05762).
- Project repository: [teorth/pfr](https://github.com/teorth/pfr), at commit [07839bdd](https://github.com/teorth/pfr/tree/07839bddb1395c8808fa47db821ce2e4fff9362e).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11B30, 11P70, 20K01, 94A17.
- In Lean Pool: [LeanPool/PFR](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR), from the card [LeanPool/projects/polynomial-freiman-ruzsa.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/polynomial-freiman-ruzsa.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/polynomial-freiman-ruzsa.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/polynomial-freiman-ruzsa.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PFR](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PFR)
