---
declaration: theorem
origin: cited
lean: TauCeti.isManifold_symChartedSpace
statement: formalized
proof: formalized
---

# The symmetric power of a complex curve is a complex analytic manifold

For a Hausdorff
one-dimensional complex manifold `α`, the elementary-symmetric charts of `Sym α n` have analytic
transition maps, so `TauCeti.symChartedSpace` makes `Sym α n` an analytic manifold modelled on
`Fin n → ℂ`.

```lean
TauCeti.isManifold_symChartedSpace.{u_1} {α : Type u_1} [TopologicalSpace α] [T2Space α]
  [ChartedSpace ℂ α] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 α] {n : ℕ} :
  IsManifold (modelWithCornersSelf ℂ (Fin n → ℂ)) ⊤ (Sym α n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy's bound on the symmetric power](../../part-03/polynomial/cauchys-bound-on-the-symmetric-power.md)
- [Newton's identities for a multiset](../../../ring-theory/part-01/multivariate-polynomials/newtons-identities-for-a-multiset.md)
- [Vieta's formulas on the symmetric power](../../../ring-theory/part-01/polynomial/vietas-formulas-on-the-symmetric-power.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isManifold_symChartedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SymmetricPower/Manifold.html#TauCeti.isManifold_symChartedSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isManifold_symChartedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SymmetricPower/Manifold.html#TauCeti.isManifold_symChartedSpace)
- [Source of `TauCeti.isManifold_symChartedSpace` in TauCeti/Geometry/Manifold/SymmetricPower/Manifold.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/SymmetricPower/Manifold.lean#L50)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
