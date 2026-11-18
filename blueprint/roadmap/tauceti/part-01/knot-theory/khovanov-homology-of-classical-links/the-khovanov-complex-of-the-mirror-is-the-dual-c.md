---
declaration: def
origin: cited
lean: TauCeti.OrientedPDCode.khovanovComplexMirrorIso
statement: formalized
---

# The Khovanov complex of the mirror is the dual complex

For a planar oriented code `D`,
the normalized Khovanov complex of `D.mirror` in quantum degree `j` is isomorphic to the dual
`Hom(C(D)_{-j}, R)` of the normalized Khovanov complex of `D` in quantum degree `-j`, the
`R`-linear Hom complex into `R` placed in degree `0`. In cochain degree `i` it pairs the states of
the mirror with `|S| - n₋(D.mirror) = i` with the complementary states of `D`, of cochain
degree `-i`, by the Frobenius pairing of their circle tensors, up to a sign depending on the state
and the degree (`TauCeti.OrientedPDCode.khovanovComplexMirrorIso_hom_f_apply` and
`TauCeti.OrientedPDCode.khovanovComplexMirrorIso_inv_f_apply`). Any planarity proof `hD'` for the
mirror may be used.

```lean
TauCeti.OrientedPDCode.khovanovComplexMirrorIso.{u} {n : ℕ} (D : TauCeti.OrientedPDCode n)
  (hD : D.IsPlanar) (R : Type u) [CommRing R] (j : ℤ) (hD' : D.mirror.IsPlanar) :
  D.mirror.khovanovComplex hD' R j ≅
    CochainComplex.linearHomComplex R (D.khovanovComplex hD R (-j))
      ((CochainComplex.singleFunctor (ModuleCat R) 0).obj ↧R)
```

## Depends on

- [TauCeti.OrientedPDCode.khovanovComplex](tauceti-orientedpdcode-khovanovcomplex.md)
- [The totalization of a dual cube is a dual complex](the-totalization-of-a-dual-cube-is-a-dual-comple.md)

## Proof depends on

- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedPDCode.khovanovComplexMirrorIso`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Mirror.html#TauCeti.OrientedPDCode.khovanovComplexMirrorIso).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedPDCode.khovanovComplexMirrorIso`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Mirror.html#TauCeti.OrientedPDCode.khovanovComplexMirrorIso)
- [Source of `TauCeti.OrientedPDCode.khovanovComplexMirrorIso` in TauCeti/KnotTheory/Khovanov/Mirror.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Mirror.lean#L89)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
