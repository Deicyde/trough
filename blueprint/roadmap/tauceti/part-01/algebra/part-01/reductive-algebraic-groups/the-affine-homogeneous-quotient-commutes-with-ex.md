---
declaration: def
origin: cited
lean: TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso
statement: formalized
---

# The affine homogeneous quotient commutes with extension of the base field

For a linearly
reductive closed subgroup `N` of a geometrically reduced affine group `G` of finite type over a
field `k`, and any field extension `K / k`, the fppf homogeneous quotient `G_K/N_K` is represented
by `Spec (K ⊗[k] O(G)^N)`, the scalar extension of the invariant algebra of `N`.

```lean
TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso.{u} {k : Type u} [Field k]
  {H : CommHopfAlgCat k} [Algebra.FiniteType k ↑H] [Algebra.IsGeometricallyReduced k ↑H]
  (I : TauCeti.HopfIdeal k ↑H) (K : Type u) [Field K] [Algebra k K]
  (hlr : TauCeti.Coalgebra.IsLinearlyReductive k (↑H ⧸ I.toIdeal)) :
  (TauCeti.CommHopfAlgCat.baseChange H).fppfHomogeneousQuotient
      (TauCeti.CommHopfAlgCat.baseChangeHopfIdeal I) ≅
    (CategoryTheory.GrothendieckTopology.uliftYoneda.{u + 1, u, u + 1}
          (TauCeti.CommAlgCat.fppfTopology K)).obj
      (Opposite.op ↧(TensorProduct k K ↥I.coinvariants))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's finiteness theorem](../../part-02/other-results/hilberts-finiteness-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/BaseChange.html#TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/BaseChange.html#TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso)
- [Source of `TauCeti.HopfIdeal.fppfHomogeneousQuotientBaseChangeIso` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/BaseChange.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/BaseChange.lean#L69)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
