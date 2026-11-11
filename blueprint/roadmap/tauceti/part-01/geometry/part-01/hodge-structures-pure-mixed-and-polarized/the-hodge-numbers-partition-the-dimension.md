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
- [Source of `TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank` in TauCeti/Geometry/Hodge/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Dimension.lean#L95)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
