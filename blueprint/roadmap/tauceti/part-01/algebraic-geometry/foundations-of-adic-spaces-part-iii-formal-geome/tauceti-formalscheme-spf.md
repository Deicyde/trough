---
declaration: def
origin: cited
lean: TauCeti.FormalScheme.Spf
statement: formalized
---

# TauCeti.FormalScheme.Spf

The **formal spectrum** `Spf A` of an adic ring `A` of finite ideal type, as a locally ringed
space (EGA I, Ch. I, 10.1.2): its points are the open prime ideals of `A`, and its structure sheaf
is `lim_n O_{Spec (A ⧸ I ^ (n + 1))}` for the chosen ideal of definition `I`.

The body is exposed so that the underlying space and the structure sheaf are definitionally
`TauCeti.FormalScheme.Spf.carrier A` and `TauCeti.FormalScheme.Spf.structureSheaf`, whose API then
applies to `Spf A` directly.

```lean
TauCeti.FormalScheme.Spf.{u} (A : Type u) [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
  [TauCeti.IsAdicRing A] : AlgebraicGeometry.LocallyRingedSpace
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.AdicRing.CompletedAway](tauceti-adicring-completedaway.md)
- [TauCeti.FormalScheme.Spf.globalSectionsIso](tauceti-formalscheme-spf-globalsectionsiso.md)
- [TauCeti.FormalScheme.Spf.structureSheafIso](tauceti-formalscheme-spf-structuresheafiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalScheme.Spf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.html#TauCeti.FormalScheme.Spf).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalScheme.Spf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.html#TauCeti.FormalScheme.Spf)
- [Source of `TauCeti.FormalScheme.Spf` in TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.lean#L172)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
