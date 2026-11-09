---
declaration: theorem
origin: cited
lean: ESS.essSmooth, ESS.ladyzhenskayaProdiSerrin, ESS.serrinCriterion
statement: formalized
proof: formalized
---

# Escauriaza–Seregin–Šverák and Ladyzhenskaya–Prodi–Serrin regularity

> Endpoint and Serrin regularity criteria for three-dimensional incompressible Navier–Stokes Leray–Hopf solutions: bounded L-infinity-in-time L3 velocity implies L5 integrability, uniqueness, and a smooth representative on positive times including the final time. Includes local endpoint regularity, both Carleman inequalities, spatial unique continuation, and half-space backward uniqueness. Retains the complete ESS production formalization.

*Quoted from the card [LeanPool/projects/escauriaza-seregin-sverak.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/escauriaza-seregin-sverak.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 10 main results, each with its informal statement quoted from the card. The scan finds 10 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ESS.essSmooth`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/EssSmooth.html#ESS.essSmooth) (theorem; a main declaration), declared in [LeanPool/EscauriazaSereginSverak/Statements/EssSmooth.lean, line 39](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/EssSmooth.lean#L39): “A Leray–Hopf solution whose spatial L3 mass is essentially bounded in time belongs to space-time L5, is unique among Leray–Hopf solutions with the same initial datum, and has an almost-everywhere equal smooth representative on all positive times through the final time.”
- [`ESS.ladyzhenskayaProdiSerrin`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/LadyzhenskayaProdiSerrin.html#ESS.ladyzhenskayaProdiSerrin) (theorem; a main declaration), declared in [LeanPool/EscauriazaSereginSverak/Statements/LadyzhenskayaProdiSerrin.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/LadyzhenskayaProdiSerrin.lean#L40): “A Leray–Hopf solution satisfying the critical Serrin mixed-norm condition with spatial exponent greater than three, including the L2-in-time L-infinity-in-space endpoint, is unique and has a smooth representative on positive times through the final time.”
- [`ESS.serrinCriterion`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/SerrinCriterion.html#ESS.serrinCriterion) (theorem; a main declaration), declared in [LeanPool/EscauriazaSereginSverak/Statements/SerrinCriterion.lean, line 36](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/SerrinCriterion.lean#L36): “The endpoint L-infinity-in-time L3 criterion and the Serrin criteria for all spatial exponents greater than three jointly imply uniqueness and existence of a smooth representative up to the final time.”
- [`ESS.essLocal`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/EssLocal.html#ESS.essLocal) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/EssLocal.lean, line 30](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/EssLocal.lean#L30): “A weak Navier–Stokes solution on the unit cylinder with finite energy, L3/2 pressure, and velocity essentially bounded in time in spatial L3 has an almost-everywhere equal parabolically Holder representative on the closure of the half cylinder.”
- [`ESS.essGlobal`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/EssGlobal.html#ESS.essGlobal) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/EssGlobal.lean, line 29](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/EssGlobal.lean#L29): “A Leray–Hopf solution whose spatial L3 mass is essentially bounded in time has no singular point at an interior positive time.”
- [`ESS.essL5Unique`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/EssL5Unique.html#ESS.essL5Unique) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/EssL5Unique.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/EssL5Unique.lean#L28): “A Leray–Hopf solution whose spatial L3 mass is essentially bounded in time belongs to space-time L5 and is unique among Leray–Hopf solutions with its initial datum.”
- [`ESS.uniqueContinuation`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/UniqueContinuation.html#ESS.uniqueContinuation) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/UniqueContinuation.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/UniqueContinuation.lean#L38): “A vector field with explicit weak space-time derivatives obeying a parabolic differential inequality has unique continuation across a spatial boundary under the stated decay and boundary hypotheses.”
- [`ESS.backwardUniqueness`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/BackwardUniqueness.html#ESS.backwardUniqueness) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/BackwardUniqueness.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/BackwardUniqueness.lean#L38): “A vector field on a three-dimensional half-space satisfying the heat differential inequality, growth bound, and zero initial trace vanishes.”
- [`ESS.carlemanGaussian`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/CarlemanGaussian.html#ESS.carlemanGaussian) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/CarlemanGaussian.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/CarlemanGaussian.lean#L38): “The Gaussian Carleman inequality bounds weighted field and gradient energies by the weighted heat-operator energy under its support hypotheses.”
- [`ESS.carlemanHalfSpace`](https://leanpool.github.io/lean-pool/LeanPool/EscauriazaSereginSverak/Statements/CarlemanHalfSpace.html#ESS.carlemanHalfSpace) (theorem), declared in [LeanPool/EscauriazaSereginSverak/Statements/CarlemanHalfSpace.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak/Statements/CarlemanHalfSpace.lean#L38): “The half-space Carleman inequality bounds weighted field and gradient energies by the weighted heat-operator energy under its support hypotheses.”

## Project

- Authors: Scott Armstrong.
- Project repository: [scottnarmstrong/EscauriazaSereginSverak](https://github.com/scottnarmstrong/EscauriazaSereginSverak), at commit [ae1a0e46](https://github.com/scottnarmstrong/EscauriazaSereginSverak/tree/ae1a0e46086b9b16179dea76b41da10b01845151).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35Q30, 35B65, 35B60.
- In Lean Pool: [LeanPool/EscauriazaSereginSverak](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak), from the card [LeanPool/projects/escauriaza-seregin-sverak.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/escauriaza-seregin-sverak.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/escauriaza-seregin-sverak.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/escauriaza-seregin-sverak.yaml)
- [Lean Pool at 2b205bf9: LeanPool/EscauriazaSereginSverak](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EscauriazaSereginSverak)
