---
declaration: theorem
origin: cited
lean: TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing
statement: formalized
proof: formalized
---

# TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing

A Henselian local ring with separably closed residue field, that is, a strictly Henselian local
ring, has no nonsplit finite étale covers: a faithfully flat finite étale algebra has a point over
the separably closed residue field, which lifts to a section.

```lean
TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing.{u} (R : Type u) [CommRing R]
  [HenselianLocalRing R] [IsSepClosed (IsLocalRing.ResidueField R)] : TauCeti.IsFiniteEtaleSplit R
```

## Depends on

- [TauCeti.IsFiniteEtaleSplit](tauceti-isfiniteetalesplit.md)

## Proof depends on

- [TauCeti.isFiniteEtaleSplit_iff_exists_section](tauceti-isfiniteetalesplit-iff-exists-section.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Etale.html#TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Etale.html#TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing)
- [Source of `TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing` in TauCeti/RingTheory/Henselian/Etale.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Henselian/Etale.lean#L146)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
