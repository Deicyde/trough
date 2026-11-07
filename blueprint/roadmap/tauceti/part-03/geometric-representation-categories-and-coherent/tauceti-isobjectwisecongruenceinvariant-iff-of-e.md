---
declaration: theorem
origin: cited
lean: TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence
statement: formalized
proof: formalized
---

# TauCeti.isObjectwiseCongruenceInvariant\_iff\_of\_equivalence

Objectwise congruence invariance is independent of an equivariant presentation of
the category. Only the forward functor of the equivalence needs a specified lineator.

```lean
TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence.{u_1, v_1, u_2, v_2, u_3} {H : Type u_1}
  [Group H] {K : ℕ → Subgroup H} {C : Type u_2} [CategoryTheory.Category.{v_1, u_2} C]
  [CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete H) C] {D : Type u_3}
  [CategoryTheory.Category.{v_2, u_3} D]
  [CategoryTheory.MonoidalCategory.MonoidalLeftAction (CategoryTheory.Discrete H) D] (e : C ≌ D)
  [e.functor.LeftLinear (CategoryTheory.Discrete H)] :
  TauCeti.IsObjectwiseCongruenceInvariant K C ↔ TauCeti.IsObjectwiseCongruenceInvariant K D
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/Congruence.html#TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence).

## Sources

- [Tau Ceti documentation: `TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Action/Congruence.html#TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence)
- [Source of `TauCeti.isObjectwiseCongruenceInvariant_iff_of_equivalence` in TauCeti/CategoryTheory/Monoidal/Action/Congruence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Monoidal/Action/Congruence.lean#L119)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
