---
declaration: def
origin: cited
lean: TauCeti.OrientedPDCode.khovanovComplex
statement: formalized
---

# TauCeti.OrientedPDCode.khovanovComplex

The normalized Khovanov complex of a planar oriented diagram. Quantum degree `j` uses
bracket degree `j - n₊ + 2n₋`, and cochain degree `i` uses cube height `i + n₋`.
Restriction translates indices while preserving the original signed saddle differential.

```lean
TauCeti.OrientedPDCode.khovanovComplex.{u} {n : ℕ} (D : TauCeti.OrientedPDCode n) (hD : D.IsPlanar)
  (R : Type u) [CommRing R] : CategoryTheory.GradedObject ℤ (CochainComplex (ModuleCat R) ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Complex.html#TauCeti.OrientedPDCode.khovanovComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Complex.html#TauCeti.OrientedPDCode.khovanovComplex)
- [Source of `TauCeti.OrientedPDCode.khovanovComplex` in TauCeti/KnotTheory/Khovanov/Complex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Complex.lean#L50)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
