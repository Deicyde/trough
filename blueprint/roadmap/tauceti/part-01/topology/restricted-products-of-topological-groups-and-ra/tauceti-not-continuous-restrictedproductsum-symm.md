---
declaration: theorem
origin: cited
lean: TauCeti.not_continuous_restrictedProductSum_symm
statement: formalized
proof: formalized
---

# TauCeti.not_continuous_restrictedProductSum_symm

The inverse of the splitting `restrictedProductSum` of a restricted product over a sum of index
types is not continuous in general: for `Πʳ k : ℕ ⊕ ℕ, [Multiplicative ℚ, ⊥]`, with the trivial,
non-open, reference subgroup at every index, it is a discontinuous bijection. The openness
hypothesis of `continuous_restrictedProductSum_symm` therefore cannot be dropped.

```lean
TauCeti.not_continuous_restrictedProductSum_symm :
  ¬Continuous ⇑(TauCeti.restrictedProductSum (fun x => ⊥) ⋯ ⋯).symm
```

## Depends on

- [TauCeti.restrictedProductSum](tauceti-restrictedproductsum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_continuous_restrictedProductSum_symm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.html#TauCeti.not_continuous_restrictedProductSum_symm).

## Sources

- [Tau Ceti documentation: `TauCeti.not_continuous_restrictedProductSum_symm`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.html#TauCeti.not_continuous_restrictedProductSum_symm)
- [Source of `TauCeti.not_continuous_restrictedProductSum_symm` in TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/RestrictedProduct/NotContinuousMul.lean#L266)
- [Tau Ceti roadmap status: Restricted products of topological groups and rational diagonals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RestrictedProducts/STATUS.md)
