---
declaration: abbrev
origin: cited
lean: TauCeti.DynkinType.chevalleyGroupScheme
statement: formalized
---

# The simply connected Chevalley group scheme `G_sc(t)` over `ℤ`

the group scheme of the
full-weight Chevalley datum, the smallest closed subgroup scheme of `GLₙ` containing the
divided-power exponential root subgroups of the numbered Chevalley generators on the full-weight
lattice and the split torus acting on its weight basis through the weights.

This is an abbreviation, like the group scheme of a Chevalley datum it specializes, so that the
inclusion into `GLₙ`, the torus and the points of that construction apply to it without
transport.

```lean
TauCeti.DynkinType.chevalleyGroupScheme (t : TauCeti.DynkinType) (ht : t.Valid) :
  CategoryTheory.Grp (CategoryTheory.Over (AlgebraicGeometry.Spec ↧ℤ))
```

## Depends on

- [The weights of the full-weight lattice span the weight lattice](the-weights-of-the-full-weight-lattice-span-the.md)

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The full-weight module is faithful](the-full-weight-module-is-faithful.md)
- [The rank-one Kostant straightening formula](../../algebra/part-01/nilpotent-orbits-springer-resolution-and-subregu/the-rank-one-kostant-straightening-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.chevalleyGroupScheme`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.html#TauCeti.DynkinType.chevalleyGroupScheme).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.chevalleyGroupScheme`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.html#TauCeti.DynkinType.chevalleyGroupScheme)
- [Source of `TauCeti.DynkinType.chevalleyGroupScheme` in TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Chevalley/SimplyConnected.lean#L152)
- [Tau Ceti roadmap status: Chevalley groups and the Chevalley–Demazure group schemes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ChevalleyGroups/STATUS.md)
