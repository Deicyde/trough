---
declaration: def
origin: cited
lean: TauCeti.OrientedPDCode.khovanovEnhancedComplexIso
statement: formalized
---

# TauCeti.OrientedPDCode.khovanovEnhancedComplexIso

The tensor and enhanced-state coefficient models are isomorphic as cochain complexes.

```lean
TauCeti.OrientedPDCode.khovanovEnhancedComplexIso.{u} {n : ℕ} (D : TauCeti.OrientedPDCode n)
  (hD : D.IsPlanar) (R : Type u) [CommRing R] (j : ℤ) :
  D.khovanovComplex hD R j ≅ D.khovanovEnhancedComplex hD R j
```

## Depends on

- [TauCeti.OrientedPDCode.khovanovComplex](tauceti-orientedpdcode-khovanovcomplex.md)

## Proof depends on

- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovEnhancedComplexIso`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Computational.html#TauCeti.OrientedPDCode.khovanovEnhancedComplexIso).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovEnhancedComplexIso`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Computational.html#TauCeti.OrientedPDCode.khovanovEnhancedComplexIso)
- [Source of `TauCeti.OrientedPDCode.khovanovEnhancedComplexIso` in TauCeti/KnotTheory/Khovanov/Computational.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Computational.lean#L212)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
