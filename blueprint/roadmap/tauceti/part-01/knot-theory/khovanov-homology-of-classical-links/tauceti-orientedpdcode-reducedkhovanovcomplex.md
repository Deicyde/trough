---
declaration: def
origin: cited
lean: TauCeti.OrientedPDCode.reducedKhovanovComplex
statement: formalized
---

# TauCeti.OrientedPDCode.reducedKhovanovComplex

The reduced Khovanov complex at a mark, with the quantum normalization
`C_red_j = image(X : C_{j+1} → C_{j-1})`. In particular the reduced unknot lies in quantum degree
zero. The image is taken in the native abelian category of cochain complexes.

```lean
TauCeti.OrientedPDCode.reducedKhovanovComplex.{u} {n : ℕ} (D : TauCeti.OrientedPDCode n)
  (p : D.Mark) (hD : D.IsPlanar) (R : Type u) [CommRing R] :
  CategoryTheory.GradedObject ℤ (CochainComplex (ModuleCat R) ℤ)
```

## Depends on

- [TauCeti.OrientedPDCode.khovanovComplex](tauceti-orientedpdcode-khovanovcomplex.md)

## Proof depends on

- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.reducedKhovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Reduced.html#TauCeti.OrientedPDCode.reducedKhovanovComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.reducedKhovanovComplex`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Reduced.html#TauCeti.OrientedPDCode.reducedKhovanovComplex)
- [Source of `TauCeti.OrientedPDCode.reducedKhovanovComplex` in TauCeti/KnotTheory/Khovanov/Reduced.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Reduced.lean#L126)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
