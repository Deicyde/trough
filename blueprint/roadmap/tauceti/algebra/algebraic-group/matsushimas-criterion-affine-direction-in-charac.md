---
declaration: theorem
origin: cited
lean: TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive, TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_of_reductive
statement: formalized
proof: formalized
---

# Matsushima's criterion, affine direction, in characteristic zero

For a reductive closed
subgroup `N` of an affine group `G` of finite type over a field of characteristic zero,
restriction to the invariant functions identifies the fppf homogeneous quotient `G/N` with the
sheaf of points of `Spec O(G)^N`.

```lean
TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive.{u} {k : Type u}
  [Field k] [CharZero k] {H : TauCeti.FiniteTypeCommHopfAlgCat k} (I : TauCeti.HopfIdeal k ↑H.obj)
  (hred : TauCeti.reductiveCommHopfAlgProperty k (H.quotient I)) :
  CategoryTheory.IsIso I.fppfHomogeneousQuotientToCoinvariantsPoints
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartier's theorem](cartiers-theorem.md)
- [Hilbert's finiteness theorem](../other-results/hilberts-finiteness-theorem.md)
- [Kolchin's common fixed vector theorem](../../linear-algebra/other-results/kolchins-common-fixed-vector-theorem.md)
- [The Lie--Kolchin theorem](the-lie-kolchin-theorem.md)
- [Weyl's complete reducibility theorem](../lie/part-02/weyls-complete-reducibility-theorem.md)
- [Weyl's theorem as a decomposition](../lie/part-02/weyls-theorem-as-a-decomposition.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Coinvariants.html#TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive).

## Other forms

**Matsushima's criterion for a closed immersion, in characteristic zero.** Formalized in Tau Ceti as [`TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_of_reductive`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Coinvariants.html#TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_of_reductive).

```lean
TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_of_reductive.{u}
  {k : Type u} [Field k] [CharZero k] {H K : TauCeti.FiniteTypeCommHopfAlgCat k} (f : H ⟶ K)
  (hf : Function.Surjective ⇑(CommHopfAlgCat.Hom.hom f.hom))
  (hK : TauCeti.reductiveCommHopfAlgProperty k K) :
  CategoryTheory.IsIso
    (TauCeti.HopfIdeal.ker
        (CommHopfAlgCat.Hom.hom f.hom)).fppfHomogeneousQuotientToCoinvariantsPoints
```

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Coinvariants.html#TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive)
- [Source of `TauCeti.HopfIdeal.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_of_reductive` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Coinvariants.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/Coinvariants.lean#L251)
