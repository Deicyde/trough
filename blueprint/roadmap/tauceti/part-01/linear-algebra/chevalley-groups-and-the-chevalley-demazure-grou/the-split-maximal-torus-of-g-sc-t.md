---
declaration: def
origin: cited
lean: TauCeti.DynkinType.chevalleyTorus
statement: formalized
---

# The split maximal torus of `G_sc(t)`

the split torus over `ℤ` with character lattice the
full weight lattice `Fin t.rank → ℤ`, in fundamental-weight coordinates, acting on each vector of
the weight basis through its weight.

```lean
TauCeti.DynkinType.chevalleyTorus (t : TauCeti.DynkinType) (ht : t.Valid) :
  TauCeti.SplitTorus.groupScheme ℤ (Fin t.rank) ⟶ t.chevalleyGroupScheme ht
```

## Depends on

- [The simply connected Chevalley group scheme `G_sc(t)` over `ℤ`](the-simply-connected-chevalley-group-scheme-g-sc.md)
- [The weights of the full-weight lattice span the weight lattice](the-weights-of-the-full-weight-lattice-span-the.md)

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The full-weight module is faithful](the-full-weight-module-is-faithful.md)
- [The rank-one Kostant straightening formula](../../algebra/part-01/nilpotent-orbits-springer-resolution-and-subregu/the-rank-one-kostant-straightening-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.chevalleyTorus`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.html#TauCeti.DynkinType.chevalleyTorus).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.chevalleyTorus`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.html#TauCeti.DynkinType.chevalleyTorus)
- [Source of `TauCeti.DynkinType.chevalleyTorus` in TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.lean#L222)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
