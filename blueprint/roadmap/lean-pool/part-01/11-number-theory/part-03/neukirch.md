---
declaration: theorem
origin: cited
lean: NumberField.ramificationIdx_mul_inertiaDegOfIsGalois
statement: formalized
proof: formalized
---

# Neukirch's Algebraic Number Theory: Hilbert ramification theory

> Formalizes Hilbert's ramification theory for Galois extensions of number fields, including the fundamental identity and the decomposition and inertia groups, ported from the jjdishere/neukirch project.

*Quoted from the card [LeanPool/projects/neukirch.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/neukirch.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`NumberField.ramificationIdx_mul_inertiaDegOfIsGalois`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/HilbertRamificationTheory.html#NumberField.ramificationIdx_mul_inertiaDegOfIsGalois) (theorem; a main declaration), declared in [LeanPool/Neukirch/HilbertRamificationTheory.lean, line 753](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/HilbertRamificationTheory.lean#L753): “Proves the fundamental identity g·e·f = [L : K] for a Galois extension of number fields.”
- [`NumberField.finrank_eq_ramificationIdx_mul_inertiaDeg`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/HilbertRamificationTheory.html#NumberField.finrank_eq_ramificationIdx_mul_inertiaDeg) (theorem), declared in [LeanPool/Neukirch/HilbertRamificationTheory.lean, line 1145](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/HilbertRamificationTheory.lean#L1145): “Shows that when P is the unique prime over p, the degree [L : K] equals the ramification index times the inertia degree.”
- [`NumberField.IsMaximal_conjugates`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/HilbertRamificationTheory.html#NumberField.IsMaximal_conjugates) (theorem), declared in [LeanPool/Neukirch/HilbertRamificationTheory.lean, line 566](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/HilbertRamificationTheory.lean#L566): “Proves the Galois group acts transitively on the primes lying over a fixed prime.”
- [`NumberField.DecompositionGroup_card_eq_ramificationIdx_mul_inertiaDeg`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/HilbertRamificationTheory.html#NumberField.DecompositionGroup_card_eq_ramificationIdx_mul_inertiaDeg) (theorem), declared in [LeanPool/Neukirch/HilbertRamificationTheory.lean, line 821](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/HilbertRamificationTheory.lean#L821): “Computes the order of the decomposition group as the product of the ramification index and inertia degree.”
- [`NumberField.InertiaFieldAutEquivResidueFieldAut`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/HilbertRamificationTheory.html#NumberField.InertiaFieldAutEquivResidueFieldAut) (def), declared in [LeanPool/Neukirch/HilbertRamificationTheory.lean, line 1133](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/HilbertRamificationTheory.lean#L1133): “Identifies the Galois group of the inertia field over K with the Galois group of the residue field extension.”
- [`NumberField.InertiaGroup_card_eq_ramificationIdx`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/HilbertRamificationTheory.html#NumberField.InertiaGroup_card_eq_ramificationIdx) (theorem), declared in [LeanPool/Neukirch/HilbertRamificationTheory.lean, line 1293](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/HilbertRamificationTheory.lean#L1293): “Computes the order of the inertia group as the ramification index of p in L.”
- [`Ideal.ramificationIdx_algebra_tower_of_eq`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/ExtensionOfDedekindDomains.html#Ideal.ramificationIdx_algebra_tower_of_eq) (theorem), declared in [LeanPool/Neukirch/ExtensionOfDedekindDomains.lean, line 34](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/ExtensionOfDedekindDomains.lean#L34): “Proves multiplicativity of the ramification index in a tower of Dedekind domains.”
- [`Ideal.inertiaDeg_algebra_tower_of_eq`](https://leanpool.github.io/lean-pool/LeanPool/Neukirch/ExtensionOfDedekindDomains.html#Ideal.inertiaDeg_algebra_tower_of_eq) (theorem), declared in [LeanPool/Neukirch/ExtensionOfDedekindDomains.lean, line 65](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch/ExtensionOfDedekindDomains.lean#L65): “Proves multiplicativity of the inertia degree in a tower of Dedekind domains.”

## Project

- Authors: Hu Yongle.
- Source: [doi:10.1007/978-3-662-03983-0](https://doi.org/10.1007/978-3-662-03983-0).
- Project repository: [jjdishere/neukirch](https://github.com/jjdishere/neukirch).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11R32, 11S15, 13B25.
- In Lean Pool: [LeanPool/Neukirch](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch), from the card [LeanPool/projects/neukirch.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/neukirch.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/neukirch.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/neukirch.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Neukirch](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Neukirch)
