---
declaration: theorem
origin: cited
lean: Polynomial.exists_isRoot_addVal_eval_eq
statement: formalized
proof: formalized
---

# Polynomial.exists\_isRoot\_addVal\_eval\_eq

**Hensel's lemma with an estimate** over a Henselian discrete valuation ring. If the order of
`F` at `y₀` exceeds twice the order of its derivative there, then `F` has a root `z` whose
distance to `y₀` has order exactly `addVal (F(y₀)) - addVal (F'(y₀))`. This is the existence
part of Mathlib's `hensels_lemma` in `addVal` spelling; the uniqueness of `z` in that ball is
`Polynomial.existsUnique_isRoot_addVal_lt`.

```lean
Polynomial.exists_isRoot_addVal_eval_eq.{u_1} {A : Type u_1} [CommRing A] [IsDomain A]
  [IsDiscreteValuationRing A] [HenselianLocalRing A] (F : Polynomial A) (y₀ : A)
  (hlt :
    (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) +
        (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) <
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ F)) :
  ∃ z,
    F.IsRoot z ∧
      (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ F) =
        (IsDiscreteValuationRing.addVal A) (Polynomial.eval y₀ (Polynomial.derivative F)) +
          (IsDiscreteValuationRing.addVal A) (z - y₀)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.exists_isRoot_addVal_eval_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Hensel.html#Polynomial.exists_isRoot_addVal_eval_eq).

## Sources

- [Tau Ceti documentation: `Polynomial.exists_isRoot_addVal_eval_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/Hensel.html#Polynomial.exists_isRoot_addVal_eval_eq)
- [Source of `Polynomial.exists_isRoot_addVal_eval_eq` in TauCeti/RingTheory/DiscreteValuationRing/Hensel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DiscreteValuationRing/Hensel.lean#L126)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
