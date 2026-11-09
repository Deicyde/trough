---
declaration: structure
origin: cited
lean: ComputableℝSeq, Computableℝ, IsComputable
statement: formalized
---

# Verified interval-Cauchy real arithmetic

> Represents real numbers as Cauchy sequences of nested rational intervals quotiented into a field, with executable interval ring arithmetic, proven-convergent rational bounds for sqrt, exp, and pi, and an IsComputable typeclass that packages such approximations to drive classical (noncomputable) comparison instances, after O'Connor's certified exact real computation.

*Quoted from the card [LeanPool/projects/computablereal.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/computablereal.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ComputableℝSeq`](https://leanpool.github.io/lean-pool/LeanPool/ComputableReal/ComputableRSeq.html#Computable%E2%84%9DSeq) (structure; a main declaration), declared in [LeanPool/ComputableReal/ComputableRSeq.lean, line 132](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal/ComputableRSeq.lean#L132): “A sequence of converging rational lower and upper bounds representing a single real number.”
- [`Computableℝ`](https://leanpool.github.io/lean-pool/LeanPool/ComputableReal/ComputableReal.html#Computable%E2%84%9D) (def; a main declaration), declared in [LeanPool/ComputableReal/ComputableReal.lean, line 27](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal/ComputableReal.lean#L27): “The quotient of interval-Cauchy sequences by equality of value, an ordered field whose ring operations are executable interval arithmetic.”
- [`IsComputable`](https://leanpool.github.io/lean-pool/LeanPool/ComputableReal/IsComputable.html#IsComputable) (class; a main declaration), declared in [LeanPool/ComputableReal/IsComputable.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal/IsComputable.lean#L38): “A typeclass packaging an explicit interval-Cauchy approximation of a real number, used to drive its classical comparison instances.”
- [`Computableℝ.instField`](https://leanpool.github.io/lean-pool/LeanPool/ComputableReal/ComputableReal.html#Computable%E2%84%9D.instField) (instance), declared in [LeanPool/ComputableReal/ComputableReal.lean, line 251](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal/ComputableReal.lean#L251): “The field instance on the quotient; inversion extracts a sign witness classically and is noncomputable.”
- [`ComputableℝSeq.Sqrt.sqrtq`](https://leanpool.github.io/lean-pool/LeanPool/ComputableReal/SpecialFunctions/Sqrt.html#Computable%E2%84%9DSeq.Sqrt.sqrtq) (def), declared in [LeanPool/ComputableReal/SpecialFunctions/Sqrt.lean, line 136](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal/SpecialFunctions/Sqrt.lean#L136): “Computes converging rational interval bounds for the square root of a rational interval.”

## Project

- Authors: Alex Meiburg.
- Source: [doi:10.1007/978-3-540-71067-7_21](https://doi.org/10.1007/978-3-540-71067-7_21), [arXiv:0805.2438](https://arxiv.org/abs/0805.2438).
- Project repository: [Timeroot/computableReal](https://github.com/Timeroot/computableReal).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 65G40, 68V20.
- In Lean Pool: [LeanPool/ComputableReal](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal), from the card [LeanPool/projects/computablereal.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/computablereal.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/computablereal.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/computablereal.yaml)
- [Lean Pool at 2b205bf9: LeanPool/ComputableReal](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/ComputableReal)
