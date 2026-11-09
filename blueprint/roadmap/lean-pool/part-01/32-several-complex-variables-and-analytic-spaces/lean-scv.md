---
declaration: theorem
origin: cited
lean: SeveralComplexVariables.analyticOnNhd_of_separately_analytic_locally_bounded
statement: formalized
proof: formalized
---

# Classical several complex variables

> Formalizes Cauchy and Taylor theory, Hartogs phenomena, removable singularities, analytic sets and germs, Weierstrass theory, holomorphic convexity, Cartan–Thullen and Bochner tube theorems, plurisubharmonic functions, Levi convexity, and elementary Runge-domain theory. Weierstrass preparation and coordinate-origin germ Noetherianity overlap LocalComplexGeometry; this development also supplies germ unique factorization and global extension and convexity results.

*Quoted from the card [LeanPool/projects/lean-scv.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-scv.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SCV.cauchy_formula_polydisc`](https://leanpool.github.io/lean-pool/LeanPool/SeveralComplexVariables/Solution.html#SCV.cauchy_formula_polydisc) (theorem), declared in [LeanPool/SeveralComplexVariables/Solution.lean, line 99](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SeveralComplexVariables/Solution.lean#L99): “Holomorphic functions on a polydisc satisfy the iterated Cauchy integral formula.”
- [`SeveralComplexVariables.analyticOnNhd_of_separately_analytic_locally_bounded`](https://leanpool.github.io/lean-pool/LeanPool/SeveralComplexVariables/SeveralComplexVariables/LocallyBounded.html#SeveralComplexVariables.analyticOnNhd_of_separately_analytic_locally_bounded) (theorem; a main declaration), declared in [LeanPool/SeveralComplexVariables/SeveralComplexVariables/LocallyBounded.lean, line 146](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SeveralComplexVariables/SeveralComplexVariables/LocallyBounded.lean#L146): “On an open subset of a finite complex coordinate space, a Banach-valued separately analytic map that is locally bounded is jointly analytic.” Its source, as the card gives it: “Boas (2013), Section 2.7, Theorem 7 (the classical two-variable scalar case).”
- [`SCV.identity_theorem`](https://leanpool.github.io/lean-pool/LeanPool/SeveralComplexVariables/Solution.html#SCV.identity_theorem) (theorem), declared in [LeanPool/SeveralComplexVariables/Solution.lean, line 130](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SeveralComplexVariables/Solution.lean#L130): “Holomorphic functions on a connected domain that agree on a nonempty open subset agree throughout the domain.”

## Project

- Authors: Bastiaan J Braams.
- Project repository: [bjbraams/lean-scv](https://github.com/bjbraams/lean-scv), at commit [caef1ae7](https://github.com/bjbraams/lean-scv/tree/caef1ae776ff79933718312357980d46628d3702).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 32A10, 32D05, 32E10.
- In Lean Pool: [LeanPool/SeveralComplexVariables](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SeveralComplexVariables), from the card [LeanPool/projects/lean-scv.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-scv.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lean-scv.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lean-scv.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SeveralComplexVariables](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SeveralComplexVariables)
