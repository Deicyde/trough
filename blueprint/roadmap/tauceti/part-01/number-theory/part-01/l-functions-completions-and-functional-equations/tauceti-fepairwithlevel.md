---
declaration: structure
origin: cited
lean: TauCeti.FEPairWithLevel
statement: formalized
---

# TauCeti.FEPairWithLevel

A functional-equation pair with a level. The fields are those of Mathlib's `WeakFEPair`:
functions `f` and `g` locally integrable on `(0, ∞)`, equal to the constants `f₀` and `g₀` at `∞` up
to an error decaying faster than every power, a weight `k > 0` and a root number `ε ≠ 0`. The
transformation law is taken at a level `N > 0`: `f (1 / (N t)) = ε t ^ k g t`. At `N = 1` it is
Mathlib's law. Only the values of `f` and `g` on `(0, ∞)` enter the laws, so both are required to
vanish elsewhere.

```lean
TauCeti.FEPairWithLevel.{u_1} (E : Type u_1) [NormedAddCommGroup E] [NormedSpace ℂ E] : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FEPairWithLevel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/FEPairWithLevel.html#TauCeti.FEPairWithLevel).

## Sources

- [Tau Ceti documentation: `TauCeti.FEPairWithLevel`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/FEPairWithLevel.html#TauCeti.FEPairWithLevel)
- [Source of `TauCeti.FEPairWithLevel` in TauCeti/NumberTheory/LSeries/FEPairWithLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/FEPairWithLevel.lean#L82)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
