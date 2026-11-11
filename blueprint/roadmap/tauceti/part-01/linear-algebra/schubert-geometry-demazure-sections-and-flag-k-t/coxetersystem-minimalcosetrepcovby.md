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
- [Source of `CoxeterSystem.MinimalCosetRepCovBy` in TauCeti/GroupTheory/Coxeter/Bruhat.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Coxeter/Bruhat.lean#L605)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchubertGeometry/STATUS.md)
