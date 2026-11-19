---
declaration: theorem
origin: cited
lean: Submodule.subspaceHeight_inf_mul_sup_le
statement: formalized
proof: formalized
---

# Struppeck–Vaaler submodularity of absolute Euclidean subspace heights

No disjointness, complementarity or positive-dimension hypothesis is required.

```lean
Submodule.subspaceHeight_inf_mul_sup_le.{u_1, u_2} {K : Type u_1} {ι : Type u_2} [Field K]
  [NumberField K] [LinearOrder ι] [Finite ι] (U W : Submodule K (ι → K)) :
  (U ⊓ W).subspaceHeight * (U ⊔ W).subspaceHeight ≤ U.subspaceHeight * W.subspaceHeight
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Binet formula](../../../linear-algebra/part-02/other-results/the-cauchy-binet-formula.md)
- [Koteljanskii's inequality for overlapping blocks](../../../analysis/part-03/matrix/koteljanskiis-inequality-for-overlapping-blocks.md)
- [Ultrametric Hadamard bound, row form](../../../linear-algebra/part-01/polynomial-interpolation-and-arithmetic-determin/ultrametric-hadamard-bound-row-form.md)

## Lean

Formalized in Tau Ceti as [`Submodule.subspaceHeight_inf_mul_sup_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/Subspace/Submodularity.html#Submodule.subspaceHeight_inf_mul_sup_le).

## Sources

- [Tau Ceti documentation: `Submodule.subspaceHeight_inf_mul_sup_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Arakelov/Subspace/Submodularity.html#Submodule.subspaceHeight_inf_mul_sup_le)
- [Source of `Submodule.subspaceHeight_inf_mul_sup_le` in TauCeti/NumberTheory/Height/Arakelov/Subspace/Submodularity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Height/Arakelov/Subspace/Submodularity.lean#L150)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
