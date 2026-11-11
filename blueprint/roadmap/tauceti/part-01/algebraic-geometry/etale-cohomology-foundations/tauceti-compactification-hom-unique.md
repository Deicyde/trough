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
- [Source of `TauCeti.Compactification.hom_unique` in TauCeti/AlgebraicGeometry/Compactification/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Compactification/Uniqueness.lean#L43)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
