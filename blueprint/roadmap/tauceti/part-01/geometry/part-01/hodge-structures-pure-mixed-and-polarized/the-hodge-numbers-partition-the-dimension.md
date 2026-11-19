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
- [Source of `TauCeti.Hodge.HodgeStructureOn.finsum_hodgeNumber_eq_finrank` in TauCeti/Geometry/Hodge/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Hodge/Dimension.lean#L93)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HodgeStructures/STATUS.md)
