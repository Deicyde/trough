---
declaration: def
origin: cited
lean: TauCeti.GeneralLinear.standardWeight
statement: formalized
---

# TauCeti.GeneralLinear.standardWeight

The weight starting at zero and dropping by one at exactly the adjacent indices
outside `J`. Thus `J` records the simple roots retained in the Levi blocks.

```lean
TauCeti.GeneralLinear.standardWeight {n : ℕ} (J : Finset (Fin n)) (i : Fin (n + 1)) : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GeneralLinear.standardWeight`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/BlockWeight.html#TauCeti.GeneralLinear.standardWeight).

## Sources

- [Tau Ceti documentation: `TauCeti.GeneralLinear.standardWeight`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/BlockWeight.html#TauCeti.GeneralLinear.standardWeight)
- [Source of `TauCeti.GeneralLinear.standardWeight` in TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/BlockWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/Weight/Parabolic/BlockWeight.lean#L59)
- [Tau Ceti roadmap status: Classification of parabolic subgroups and projective homogeneous spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FlagVarieties/STATUS.md)
