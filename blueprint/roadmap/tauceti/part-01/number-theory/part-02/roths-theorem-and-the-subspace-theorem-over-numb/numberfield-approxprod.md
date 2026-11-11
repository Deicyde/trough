---
declaration: def
origin: cited
lean: NumberField.approxProd
statement: formalized
---

# NumberField.approxProd

The approximation product of a point `x : ι → K` with respect to linear forms `L v i` with
coefficients in `F` at the places of `K` in `Sinf` and `Sfin`, each measured by an absolute value
`w v` of `F`: the product over `v ∈ Sinf` of `(∏ i, w v (L v i x) / ⨆ j, v (x j)) ^ mult v`, times
the product over `v ∈ Sfin` of `∏ i, w v (L v i x) / ⨆ j, v (x j)`, where `x` is mapped into `F`.

The data `w` and `L` are indexed by the underlying absolute value of a place, and their values off
`Sinf ∪ Sfin` play no role.

```lean
NumberField.approxProd.{u_1, u_2, u_3} {K : Type u_1} {F : Type u_2} {ι : Type u_3} [Field K]
  [Field F] [Algebra K F] [Fintype ι] [NumberField K] (Sinf : Finset (NumberField.InfinitePlace K))
  (Sfin : Finset (NumberField.FinitePlace K)) (w : AbsoluteValue K ℝ → AbsoluteValue F ℝ)
  (L : AbsoluteValue K ℝ → ι → Module.Dual F (ι → F)) (x : ι → K) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.approxProd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproxProd.html#NumberField.approxProd).

## Sources

- [Tau Ceti documentation: `NumberField.approxProd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproxProd.html#NumberField.approxProd)
- [Source of `NumberField.approxProd` in TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproxProd.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Subspace/ApproxProd.lean#L106)
- [Tau Ceti roadmap status: Roth's theorem and the Subspace Theorem over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SubspaceTheorem/STATUS.md)
