---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank
statement: formalized
proof: formalized
---

# The Hodge numbers partition the dimension

the Hodge numbers of a weight-`n` Hodge
structure on a finite-dimensional complex vector space sum to its dimension.

```lean
TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank.{u} {W : Type u} [AddCommGroup W]
  [_root_.Module ℂ W] {ω : TauCeti.Hodge.Conjugation W} {n : ℤ}
  (hs : TauCeti.Hodge.HodgeStructureOn W ω n) [FiniteDimensional ℂ W] :
  ∑ᶠ (p : ℤ), hs.hodgeNumber p = Module.finrank ℂ W
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Dimension.html#TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Dimension.html#TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank)
- [Source of `TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank` in TauCeti/Geometry/Hodge/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/Dimension.lean#L95)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
