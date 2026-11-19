---
declaration: def
origin: cited
lean: TauCeti.FormalScheme.Spf.restrictBasicOpenIso
statement: formalized
---

# The basic open set `D(f)` of `Spf A` is `Spf A_{f}`

the restriction of the locally ringed
space `Spf A` to `D(f)` is isomorphic to the formal spectrum of the completed localisation
`A_{f}` (EGA I, Ch. I, 10.1.4).

```lean
TauCeti.FormalScheme.Spf.restrictBasicOpenIso.{u} {A : Type u} [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.IsAdicRing A] (f : A) :
  (TauCeti.FormalScheme.Spf A).restrict ⋯ ≅
    TauCeti.FormalScheme.Spf (TauCeti.AdicRing.CompletedAway A f)
```

## Depends on

- [TauCeti.AdicRing.CompletedAway](tauceti-adicring-completedaway.md)
- [TauCeti.FormalScheme.Spf](tauceti-formalscheme-spf.md)

## Proof depends on

- [TauCeti.FormalScheme.Spf.globalSectionsIso](tauceti-formalscheme-spf-globalsectionsiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalScheme.Spf.restrictBasicOpenIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Restrict.html#TauCeti.FormalScheme.Spf.restrictBasicOpenIso).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalScheme.Spf.restrictBasicOpenIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Restrict.html#TauCeti.FormalScheme.Spf.restrictBasicOpenIso)
- [Source of `TauCeti.FormalScheme.Spf.restrictBasicOpenIso` in TauCeti/AlgebraicGeometry/FormalScheme/Spf/Restrict.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Restrict.lean#L235)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
