---
declaration: lemma
origin: cited
lean: MIPRE.Verifier.ComputablyPresented, MIPRE.Verifier.boundBudget, MIPRE.Verifier.BoundViolation, MIPRE.Verifier.boundViolationB, MIPRE.Verifier.boundViolationB_iff, MIPRE.Verifier.not_isBounded_iff_exists, MIPRE.Verifier.rePred_not_isBounded, MIPRE.REPred.of_computable_exists, MIPRE.Cost.primrec_natLeB
statement: formalized
proof: formalized
---

# A violated time bound is enumerable

Call a family $a \mapsto \mathsf{V}^a$ of normal form verifiers *computably presented* when the program of its sampler, the program of its decider, and the dimension $s^a(n)$ of its sampler's ambient space are computable in $a$ (and, for the dimension, in $n$). For such a family the set of pairs $(a, \lambda)$ with $\mathsf{V}^a$ *not* $\lambda$-bounded (Definition [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)) is recursively enumerable.

## Depends on

- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)
- [Halting within a cost budget is decidable](../../computability/lem-cost-budget-decidable.md)

## Proof

Every clause of Definition [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md) is universally quantified — over indices $m \geq 2$, and, inside the two time bounds, over the inputs of the sampler and of the decider at $m$ — and the remaining clause $\left\vert {\mathsf{V}} \right\vert \leq \lambda$ is a comparison of two computable numbers. So the negation is an unbounded search for a pair (index, input), and each test is decidable: the dimension clause because the dimension is computable by hypothesis, the two time bounds by Lemma [Halting within a cost budget is decidable](../../computability/lem-cost-budget-decidable.md). The index is carried as a datum and read back by `Data.natOf`, which is a surjection onto $\mathbb{N}$ inverting the encoding on canonical binary data, so nothing is lost and the encoding the time bounds prepend to their input is primitive recursive in the witness.

## Lean

Formalized as [`MIPRE.Verifier.ComputablyPresented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.ComputablyPresented), [`MIPRE.Verifier.boundBudget`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.boundBudget), [`MIPRE.Verifier.BoundViolation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.BoundViolation), [`MIPRE.Verifier.boundViolationB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.boundViolationB), [`MIPRE.Verifier.boundViolationB_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.boundViolationB_iff), [`MIPRE.Verifier.not_isBounded_iff_exists`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.not_isBounded_iff_exists), [`MIPRE.Verifier.rePred_not_isBounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.rePred_not_isBounded), [`MIPRE.REPred.of_computable_exists`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.REPred.of_computable_exists), [`MIPRE.Cost.primrec_natLeB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.primrec_natLeB).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6939](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6939)
