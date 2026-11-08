---
declaration: class
origin: cited
lean: QuasiBorelSpace, OmegaQuasiBorelSpace, QuasiBorelSpace.ProbabilityMeasure
statement: formalized
---

# Quasi-Borel Spaces

> Formalizes quasi-Borel spaces and quasi-Borel pre-domains, a category for higher-order probability theory.

*Quoted from the card [LeanPool/projects/quasi-borel-spaces.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quasi-borel-spaces.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`QuasiBorelSpace`](https://leanpool.github.io/lean-pool/LeanPool/QuasiBorelSpaces/Defs.html#QuasiBorelSpace) (class; a main declaration), declared in [LeanPool/QuasiBorelSpaces/Defs.lean, line 31](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuasiBorelSpaces/Defs.lean#L31): “Defines a quasi-Borel space as a type with a set of random variables closed under constants, measurable precomposition, and gluing.”
- [`QuasiBorelSpace.IsHom`](https://leanpool.github.io/lean-pool/LeanPool/QuasiBorelSpaces/Defs.html#QuasiBorelSpace.IsHom) (inductive), declared in [LeanPool/QuasiBorelSpaces/Defs.lean, line 64](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuasiBorelSpaces/Defs.lean#L64): “Defines morphisms of quasi-Borel spaces as maps that preserve random variables under precomposition.”
- [`OmegaQuasiBorelSpace`](https://leanpool.github.io/lean-pool/LeanPool/QuasiBorelSpaces/OmegaQuasiBorelSpace.html#OmegaQuasiBorelSpace) (class; a main declaration), declared in [LeanPool/QuasiBorelSpaces/OmegaQuasiBorelSpace.lean, line 45](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuasiBorelSpaces/OmegaQuasiBorelSpace.lean#L45): “Combines the quasi-Borel and ω-complete partial order structures with the compatibility axiom of Vakar-Kammar-Staton.”
- [`QuasiBorelSpace.ProbabilityMeasure`](https://leanpool.github.io/lean-pool/LeanPool/QuasiBorelSpaces/ProbabilityMeasure.html#QuasiBorelSpace.ProbabilityMeasure) (structure; a main declaration), declared in [LeanPool/QuasiBorelSpaces/ProbabilityMeasure.lean, line 39](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuasiBorelSpaces/ProbabilityMeasure.lean#L39): “Defines the probability-measure monad on quasi-Borel spaces by quotienting pre-probability measures by integral equivalence.”

## Project

- Authors: Anthony Vandikas, Kiarash Sotoudeh.
- Source: [doi:10.1109/LICS.2017.8005137](https://doi.org/10.1109/LICS.2017.8005137), [arXiv:1701.02547](https://arxiv.org/abs/1701.02547).
- Project repository: [YellPika/quasi-borel-spaces](https://github.com/YellPika/quasi-borel-spaces).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0, keeping its copyright line: “Copyright (c) 2025 Anthony Vandikas, Kiarash Sotoudeh”.
- MSC2020: 60A05, 18C50, 68Q55.
- In Lean Pool: [LeanPool/QuasiBorelSpaces](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuasiBorelSpaces), from the card [LeanPool/projects/quasi-borel-spaces.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quasi-borel-spaces.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/quasi-borel-spaces.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quasi-borel-spaces.yaml)
- [Lean Pool at 2b205bf9: LeanPool/QuasiBorelSpaces](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuasiBorelSpaces)
