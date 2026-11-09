---
declaration: structure
origin: cited
lean: CoxeterSystem.MinimalCosetRepCovBy
statement: formalized
---

# CoxeterSystem.MinimalCosetRepCovBy

`y` is **covered by** `x` in the Bruhat order of the parabolic quotient `W / W_J`, modelled on
the minimal coset representatives: both are minimal coset representatives, `y < x`, and no minimal
coset representative lies strictly between them.

```lean
CoxeterSystem.MinimalCosetRepCovBy.{u_1, u_2} {B : Type u_1} {W : Type u_2} [Group W]
  {M : CoxeterMatrix B} (cs : CoxeterSystem M W) (J : Set B) (y x : W) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CoxeterSystem.MinimalCosetRepCovBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Bruhat.html#CoxeterSystem.MinimalCosetRepCovBy).

## Sources

- [Tau Ceti documentation: `CoxeterSystem.MinimalCosetRepCovBy`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Bruhat.html#CoxeterSystem.MinimalCosetRepCovBy)
- [Source of `CoxeterSystem.MinimalCosetRepCovBy` in TauCeti/GroupTheory/Coxeter/Bruhat.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Coxeter/Bruhat.lean#L585)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
