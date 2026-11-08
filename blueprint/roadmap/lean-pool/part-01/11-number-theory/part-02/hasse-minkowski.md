---
declaration: theorem
origin: cited
lean: HasseMinkowski.hasseMinkowski, HasseMinkowski.meyer
statement: formalized
proof: formalized
---

# The Hasse–Minkowski theorem over ℚ

> Proves the local–global principle for quadratic forms over the rationals: a form is isotropic over ℚ exactly when it is isotropic over ℝ and over every p-adic completion, together with Meyer's theorem that an indefinite rational form in at least five variables is isotropic. The development builds the Hilbert symbol at every place of ℚ with Serre's explicit formulas (including the 2-adic case), proves Hilbert reciprocity and the existence theorem for prescribed local symbols, the Hasse invariant and the rank-two and rank-three local representability criteria, Legendre's ternary descent, and the rank-four and rank-≥5 inductions.

*Quoted from the card [LeanPool/projects/hasse-minkowski.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hasse-minkowski.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`HasseMinkowski.hasseMinkowski`](https://leanpool.github.io/lean-pool/LeanPool/HasseMinkowski/Main.html#HasseMinkowski.hasseMinkowski) (theorem; a main declaration), declared in [LeanPool/HasseMinkowski/Main.lean, line 197](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HasseMinkowski/Main.lean#L197): “A quadratic form over ℚ is isotropic if and only if it is isotropic over ℝ and over every p-adic completion ℚ\_[p] (the Hasse–Minkowski local–global principle, in isotropy form).”
- [`HasseMinkowski.meyer`](https://leanpool.github.io/lean-pool/LeanPool/HasseMinkowski/Main.html#HasseMinkowski.meyer) (theorem; a main declaration), declared in [LeanPool/HasseMinkowski/Main.lean, line 202](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HasseMinkowski/Main.lean#L202): “Every indefinite quadratic form over ℚ in at least five variables is isotropic (Meyer's theorem).”

## Project

- Authors: jayyswan, Nirvana Coppola, María Inés de Frutos-Fernández.
- Source: *The Hasse–Minkowski theorem over ℚ*.
- Project repository: [jayyswan/hasse-minkowski](https://github.com/jayyswan/hasse-minkowski), at commit [47f0e9b5](https://github.com/jayyswan/hasse-minkowski/tree/47f0e9b5cba6e6354b882bc5856a11962ba61f4a).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 11E12, 11E08, 11E88.
- In Lean Pool: [LeanPool/HasseMinkowski](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HasseMinkowski), from the card [LeanPool/projects/hasse-minkowski.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hasse-minkowski.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/hasse-minkowski.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/hasse-minkowski.yaml)
- [Lean Pool at 2b205bf9: LeanPool/HasseMinkowski](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/HasseMinkowski)
