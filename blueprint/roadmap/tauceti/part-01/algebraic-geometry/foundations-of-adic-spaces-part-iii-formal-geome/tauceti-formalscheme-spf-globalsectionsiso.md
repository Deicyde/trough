---
declaration: def
origin: cited
lean: TauCeti.FormalScheme.Spf.globalSectionsIso
statement: formalized
---

# TauCeti.FormalScheme.Spf.globalSectionsIso

If `A` is `I`-adically complete, the global sections of the structure sheaf of `Spf A` are
`A` (EGA I, Ch. I, 10.1.3).

```lean
TauCeti.FormalScheme.Spf.globalSectionsIso.{u} {A : Type u} [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] {I : Ideal A} [IsAdicComplete I A] (hI : IsAdic I) :
  (TauCeti.FormalScheme.Spf.structureSheaf hI).obj.obj (Opposite.op ⊤) ≅ ↧A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalScheme.Spf.globalSectionsIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/StructureSheaf.html#TauCeti.FormalScheme.Spf.globalSectionsIso).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalScheme.Spf.globalSectionsIso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FormalScheme/Spf/StructureSheaf.html#TauCeti.FormalScheme.Spf.globalSectionsIso)
- [Source of `TauCeti.FormalScheme.Spf.globalSectionsIso` in TauCeti/AlgebraicGeometry/FormalScheme/Spf/StructureSheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FormalScheme/Spf/StructureSheaf.lean#L464)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
