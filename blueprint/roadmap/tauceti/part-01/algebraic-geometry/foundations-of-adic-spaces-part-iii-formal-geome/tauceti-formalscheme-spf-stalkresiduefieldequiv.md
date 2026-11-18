---
declaration: def
origin: cited
lean: TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv
statement: formalized
---

# TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv

The residue field of `Spf A` at an open prime `p` is the fraction field of `A ⧸ p`
(EGA I, Ch. I, 10.1.6).

```lean
TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv.{u} {A : Type u} [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.IsAdicRing A] (p : ↑(TauCeti.FormalScheme.Spf.carrier A)) :
  ↑((TauCeti.FormalScheme.Spf A).residueField p) ≃+* FractionRing (A ⧸ (↑p).asIdeal)
```

## Depends on

- [TauCeti.AdicRing.CompletedAway](tauceti-adicring-completedaway.md)
- [TauCeti.FormalScheme.Spf](tauceti-formalscheme-spf.md)

## Proof depends on

- [TauCeti.FormalScheme.Spf.globalSectionsIso](tauceti-formalscheme-spf-globalsectionsiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.html#TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.html#TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv)
- [Source of `TauCeti.FormalScheme.Spf.stalkResidueFieldEquiv` in TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FormalScheme/Spf/Basic.lean#L202)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
