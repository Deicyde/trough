---
declaration: structure
origin: cited
lean: TauCeti.Hodge.HodgeStructureOn
statement: formalized
---

# TauCeti.Hodge.HodgeStructureOn

A pure Hodge structure of weight `n` on a complex vector space with conjugation `ω`.

The decreasing filtration `F` is bounded and `n`-opposed to its conjugate: for every `p`,
`F p` is complementary to the conjugate of `F (n + 1 - p)`.

```lean
TauCeti.Hodge.HodgeStructureOn.{u} (W : Type u) [AddCommGroup W] [_root_.Module ℂ W]
  (ω : TauCeti.Hodge.Conjugation W) (n : ℤ) : Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.HodgeStructureOn`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Structure.html#TauCeti.Hodge.HodgeStructureOn).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.HodgeStructureOn`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Structure.html#TauCeti.Hodge.HodgeStructureOn)
- [Source of `TauCeti.Hodge.HodgeStructureOn` in TauCeti/Geometry/Hodge/Structure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/Structure.lean#L57)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
