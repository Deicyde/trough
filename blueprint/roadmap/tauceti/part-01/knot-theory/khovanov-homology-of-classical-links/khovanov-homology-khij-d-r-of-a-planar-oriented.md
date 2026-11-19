---
declaration: abbrev
origin: cited
lean: TauCeti.OrientedPDCode.khovanovHomology
statement: formalized
---

# Khovanov homology `Khⁱʲ(D; R)` of a planar oriented code `D`

the cohomology in cochain
degree `i` of the quantum component `j` of the normalized Khovanov complex.

```lean
TauCeti.OrientedPDCode.khovanovHomology.{u} {n : ℕ} (D : TauCeti.OrientedPDCode n) (hD : D.IsPlanar)
  (R : Type u) [CommRing R] (i j : ℤ) : ModuleCat R
```

## Depends on

- [TauCeti.OrientedPDCode.khovanovComplex](tauceti-orientedpdcode-khovanovcomplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovHomology`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Homology.html#TauCeti.OrientedPDCode.khovanovHomology).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovHomology`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Homology.html#TauCeti.OrientedPDCode.khovanovHomology)
- [Source of `TauCeti.OrientedPDCode.khovanovHomology` in TauCeti/KnotTheory/Khovanov/Homology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Homology.lean#L46)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
