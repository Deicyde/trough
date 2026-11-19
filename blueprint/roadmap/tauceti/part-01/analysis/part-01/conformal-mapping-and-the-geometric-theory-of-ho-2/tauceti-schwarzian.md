---
declaration: def
origin: cited
lean: TauCeti.schwarzian
statement: formalized
---

# TauCeti.schwarzian

The **Schwarzian derivative** `S(f) = f''' / f' - (3 / 2) * (f'' / f') ^ 2`, written over the
common denominator `2 * f' ^ 2`.  It is totalized: at a point where `f' = 0` it is zero, and it
carries no geometric meaning there.

```lean
TauCeti.schwarzian (f : ℂ → ℂ) (x : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.schwarzian`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarzian.html#TauCeti.schwarzian).

## Sources

- [Tau Ceti documentation: `TauCeti.schwarzian`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Schwarzian.html#TauCeti.schwarzian)
- [Source of `TauCeti.schwarzian` in TauCeti/Analysis/Complex/Conformal/Schwarzian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/Schwarzian.lean#L64)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ConformalMappingPartII/STATUS.md)
