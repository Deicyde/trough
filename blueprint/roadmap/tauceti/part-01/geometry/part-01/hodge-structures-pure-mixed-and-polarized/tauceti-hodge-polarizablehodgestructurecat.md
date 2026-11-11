---
declaration: structure
origin: cited
lean: TauCeti.Hodge.PolarizableHodgeStructureCat
statement: formalized
---

# TauCeti.Hodge.PolarizableHodgeStructureCat

The category of finite-dimensional polarizable rational Hodge structures of weight `n`, with
integral, rational, and complex models in `Type u`.

The integral model is a finitely generated free lattice and determines the conjugation on the
complexification. The rational model is the carrier on which morphisms are defined. Polarizability
is retained only as a property, so no particular polarizing form is part of an object.

```lean
TauCeti.Hodge.PolarizableHodgeStructureCat.{u} (n : ℤ) : Type (u + 1)
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.PolarizableHodgeStructureCat`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Category.html#TauCeti.Hodge.PolarizableHodgeStructureCat).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.PolarizableHodgeStructureCat`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Category.html#TauCeti.Hodge.PolarizableHodgeStructureCat)
- [Source of `TauCeti.Hodge.PolarizableHodgeStructureCat` in TauCeti/Geometry/Hodge/Category.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Category.lean#L54)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
