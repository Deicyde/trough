---
declaration: def
origin: cited
lean: FormalGroup.logIso
statement: formalized
---

# FormalGroup.logIso

The normalized logarithm is a strict isomorphism from `F` to the additive formal group,
with the formal exponential as its inverse.

```lean
FormalGroup.logIso.{u_1} {R : Type u_1} [CommRing R] (F : FormalGroup R) [Algebra ℚ R] :
  TauCeti.FormalGroupIso F FormalGroup.𝔾ₐ
```

## Depends on

- [TauCeti.FormalGroupHom](tauceti-formalgrouphom.md)
- [TauCeti.FormalGroupIso](tauceti-formalgroupiso.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.logIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Logarithm/Basic.html#FormalGroup.logIso).

## Sources

- [Tau Ceti documentation: `FormalGroup.logIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Logarithm/Basic.html#FormalGroup.logIso)
- [Source of `FormalGroup.logIso` in TauCeti/RingTheory/FormalGroup/Logarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/Logarithm/Basic.lean#L558)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
