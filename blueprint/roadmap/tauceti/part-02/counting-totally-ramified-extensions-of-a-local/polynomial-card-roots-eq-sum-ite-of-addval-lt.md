---
declaration: theorem
origin: cited
lean: Polynomial.card_roots_eq_sum_ite_of_addVal_lt
statement: formalized
proof: formalized
---

# Polynomial.card\_roots\_eq\_sum\_ite\_of\_addVal\_lt

Count roots by a finite disjoint family of balls covering them. If the derivative order at
each root is smaller than the ball order, each occupied ball contributes exactly one root.
The derivative bound also excludes repeated rational roots, so no separability hypothesis is
needed.

```lean
Polynomial.card_roots_eq_sum_ite_of_addVal_lt.{u_1} {A : Type u_1} [CommRing A] [IsDomain A]
  [IsDiscreteValuationRing A] (F : Polynomial A) (C : Finset A) {r : ℕ}
  (hcover : ∀ x ∈ F.roots, ∃ c ∈ C, ↑r ≤ (IsDiscreteValuationRing.addVal A) (x - c))
  (hdisj : (↑C).PairwiseDisjoint fun c => {x | ↑r ≤ (IsDiscreteValuationRing.addVal A) (x - c)})
  (hder :
    ∀ x ∈ F.roots,
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval x (Polynomial.derivative F)) < ↑r) :
  F.roots.card =
    ∑ c ∈ C, if ∃ x ∈ F.roots, ↑r ≤ (IsDiscreteValuationRing.addVal A) (x - c) then 1 else 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.card_roots_eq_sum_ite_of_addVal_lt`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/RootPartition.html#Polynomial.card_roots_eq_sum_ite_of_addVal_lt).

## Sources

- [Tau Ceti documentation: `Polynomial.card_roots_eq_sum_ite_of_addVal_lt`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/RootPartition.html#Polynomial.card_roots_eq_sum_ite_of_addVal_lt)
- [Source of `Polynomial.card_roots_eq_sum_ite_of_addVal_lt` in TauCeti/RingTheory/DiscreteValuationRing/RootPartition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DiscreteValuationRing/RootPartition.lean#L77)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
