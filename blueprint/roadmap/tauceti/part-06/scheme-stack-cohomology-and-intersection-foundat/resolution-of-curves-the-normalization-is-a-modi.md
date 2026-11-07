---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint
statement: formalized
proof: formalized
---

# Resolution of curves: the normalization is a modification

If the normalization of an
integral scheme `Y` in its function field, along `Spec k(Y) ⟶ Y`, is finite over `Y`, then it is a
modification of `Y`: it is proper, and an isomorphism over a dense open of `Y` with dense preimage.
Stacks, Lemma 33.41.1 (0C45) over a field.

```lean
TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint.{u}
  {Y : AlgebraicGeometry.Scheme} [AlgebraicGeometry.IsIntegral Y]
  [AlgebraicGeometry.IsFinite
      (AlgebraicGeometry.Scheme.Hom.fromNormalization (Y.fromSpecStalk (genericPoint ↥Y)))] :
  TauCeti.AlgebraicGeometry.IsModification
    (AlgebraicGeometry.Scheme.Hom.fromNormalization (Y.fromSpecStalk (genericPoint ↥Y)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Normalization/Modification.html#TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Normalization/Modification.html#TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint)
- [Source of `TauCeti.AlgebraicGeometry.isModification_fromNormalization_fromSpecStalk_genericPoint` in TauCeti/AlgebraicGeometry/Normalization/Modification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Normalization/Modification.lean#L54)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
