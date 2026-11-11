---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple
statement: formalized
proof: formalized
---

# Categorical semisimplicity of polarizable rational Hodge structures

Every object is
isomorphic to a finite biproduct of simple objects induced by rational Hodge substructures.

```lean
TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple.{u'} {n : ℤ}
  (X : TauCeti.Hodge.PolarizableHodgeStructureCat n) :
  ∃ s,
    (∀ U ∈ s, CategoryTheory.Simple (X.ofSubstructure U)) ∧
      Nonempty ((⨁ fun U => X.ofSubstructure ↑U) ≅ X)
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)
- [TauCeti.Hodge.PolarizableHodgeStructureCat](tauceti-hodge-polarizablehodgestructurecat.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [Strictness of a morphism of mixed Hodge structures for the Hodge filtration](strictness-of-a-morphism-of-mixed-hodge-structur.md)
- [TauCeti.Hodge.Polarization.Q](tauceti-hodge-polarization-q.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Semisimple.html#TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Semisimple.html#TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple)
- [Source of `TauCeti.Hodge.PolarizableHodgeStructureCat.exists_iso_biproduct_simple` in TauCeti/Geometry/Hodge/Semisimple.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Semisimple.lean#L378)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
