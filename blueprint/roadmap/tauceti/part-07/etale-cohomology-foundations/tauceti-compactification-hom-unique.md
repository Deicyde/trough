---
declaration: theorem
origin: cited
lean: TauCeti.Compactification.hom_unique
statement: formalized
proof: formalized
---

# TauCeti.Compactification.hom_unique

Maps from a compactification with schematically dense interior to any fixed
compactification are unique. No density assumption on the target is needed.

```lean
TauCeti.Compactification.hom_unique.{u} {X S : AlgebraicGeometry.Scheme} {f : X ⟶ S}
  {C D : TauCeti.Compactification f} [AlgebraicGeometry.IsSchemeTheoreticallyDominant C.j]
  (h k : C ⟶ D) : h = k
```

## Depends on

- [TauCeti.Compactification](tauceti-compactification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Compactification.hom_unique`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Uniqueness.html#TauCeti.Compactification.hom_unique).

## Sources

- [Tau Ceti documentation: `TauCeti.Compactification.hom_unique`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/Uniqueness.html#TauCeti.Compactification.hom_unique)
- [Source of `TauCeti.Compactification.hom_unique` in TauCeti/AlgebraicGeometry/Compactification/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Compactification/Uniqueness.lean#L43)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
