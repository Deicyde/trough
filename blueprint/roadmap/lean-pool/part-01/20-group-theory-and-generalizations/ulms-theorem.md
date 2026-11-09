---
declaration: theorem
origin: cited
lean: UlmsTheorem.ulm_theorem
statement: formalized
proof: formalized
---

# Ulm's theorem for countable reduced abelian p-groups

> Formalizes Ulm's classification theorem for countable reduced abelian p-groups in arbitrary Lean universes. The development constructs the transfinite Ulm filtration and invariants, proves their invariance under additive equivalence, establishes Kaplansky's one-generator extension lemma, and completes the countable back-and-forth classification. A finite-group regression distinguishes Z/4 x Z/4 from Z/2 x Z/8 at the zeroth Ulm invariant.

*Quoted from the card [LeanPool/projects/ulms-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ulms-theorem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`UlmsTheorem.ulm_theorem`](https://leanpool.github.io/lean-pool/LeanPool/UlmsTheorem/Ulm/Theorem.html#UlmsTheorem.ulm_theorem) (theorem; a main declaration), declared in [LeanPool/UlmsTheorem/Ulm/Theorem.lean, line 53](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/UlmsTheorem/Ulm/Theorem.lean#L53): “For any prime p and any two countable reduced abelian p-groups in the same arbitrary Lean universe, the groups are additively isomorphic if and only if all of their classical Ulm invariants, indexed by universe-zero ordinals, agree.”
- [`UlmsTheorem.iso_of_ulm_invariants`](https://leanpool.github.io/lean-pool/LeanPool/UlmsTheorem/Ulm/Theorem.html#UlmsTheorem.iso_of_ulm_invariants) (theorem), declared in [LeanPool/UlmsTheorem/Ulm/Theorem.lean, line 43](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/UlmsTheorem/Ulm/Theorem.lean#L43): “Equal Ulm invariants at every universe-zero ordinal imply an additive equivalence between countable reduced abelian p-groups, via finite height-preserving partial isomorphisms and a back-and-forth limit.”
- [`UlmsTheorem.ulmInvariant_iso_invariant`](https://leanpool.github.io/lean-pool/LeanPool/UlmsTheorem/Ulm/Invariance.html#UlmsTheorem.ulmInvariant_iso_invariant) (theorem), declared in [LeanPool/UlmsTheorem/Ulm/Invariance.lean, line 177](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/UlmsTheorem/Ulm/Invariance.lean#L177): “An additive equivalence preserves every classical Ulm invariant.”
- [`UlmsTheorem.UlmDifferentialRegression.no_iso_44_28`](https://leanpool.github.io/lean-pool/LeanPool/UlmsTheorem/Regression.html#UlmsTheorem.UlmDifferentialRegression.no_iso_44_28) (theorem), declared in [LeanPool/UlmsTheorem/Regression.lean, line 147](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/UlmsTheorem/Regression.lean#L147): “The groups Z/4 x Z/4 and Z/2 x Z/8 are not additively isomorphic; the proof exercises the classification theorem and independently detects their different zeroth Ulm invariants.”

## Project

- Authors: Elan Roth.
- Source: *Ulm's theorem for countable reduced abelian p-groups* by Elan Roth.
- Project repository: [elanroth/UlmsTheorem](https://github.com/elanroth/UlmsTheorem), at commit [3bb8a10a](https://github.com/elanroth/UlmsTheorem/tree/3bb8a10ae12eb957a0f05db248d3becaf6a7e222).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 20K10.
- In Lean Pool: [LeanPool/UlmsTheorem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/UlmsTheorem), from the card [LeanPool/projects/ulms-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ulms-theorem.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/ulms-theorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ulms-theorem.yaml)
- [Lean Pool at 2b205bf9: LeanPool/UlmsTheorem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/UlmsTheorem)
