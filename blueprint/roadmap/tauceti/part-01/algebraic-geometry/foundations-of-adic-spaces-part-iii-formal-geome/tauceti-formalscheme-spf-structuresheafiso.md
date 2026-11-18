---
declaration: def
origin: cited
lean: TauCeti.FormalScheme.Spf.structureSheafIso
statement: formalized
---

# TauCeti.FormalScheme.Spf.structureSheafIso

For ideals of definition `I` and `J` of `A`, the canonical isomorphism between the structure
sheaves of `Spf A` built from `I` and from `J`. Both are sheaves on the same space, the open primes
of `A`, and the isomorphism commutes with the projections to the thickenings `O_K` for every
ideal of definition `K` (`structureSheafIso_hom_comp_toQuotientSheaf`) and with the
identifications of the global sections with `A`
(`globalSectionsIso_inv_comp_structureSheafIso_hom`). Thus `Spf A` depends only on the topology
of `A` (EGA I, Ch. I, 10.1.1).

```lean
TauCeti.FormalScheme.Spf.structureSheafIso.{u} {A : Type u} [CommRing A] [TopologicalSpace A]
  {I J : Ideal A} [IsTopologicalRing A] (hI : IsAdic I) (hJ : IsAdic J) :
  TauCeti.FormalScheme.Spf.structureSheaf hI ≅ TauCeti.FormalScheme.Spf.structureSheaf hJ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalScheme.Spf.structureSheafIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/IdealIndependence.html#TauCeti.FormalScheme.Spf.structureSheafIso).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalScheme.Spf.structureSheafIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/IdealIndependence.html#TauCeti.FormalScheme.Spf.structureSheafIso)
- [Source of `TauCeti.FormalScheme.Spf.structureSheafIso` in TauCeti/AlgebraicGeometry/FormalScheme/Spf/IdealIndependence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FormalScheme/Spf/IdealIndependence.lean#L82)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
