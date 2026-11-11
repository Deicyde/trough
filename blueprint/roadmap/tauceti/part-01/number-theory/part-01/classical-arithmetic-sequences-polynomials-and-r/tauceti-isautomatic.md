---
declaration: def
origin: cited
lean: TauCeti.IsAutomatic
statement: formalized
---

# TauCeti.IsAutomatic

A sequence `a : ℕ → Δ` is **`k`-automatic** if a deterministic automaton with output, with
finitely many states and input alphabet `Fin k`, outputs `a n` on the base-`k` digits of `n`, read
least significant digit first (Mathlib's `Nat.digits k n`, so `0` is the empty word).

```lean
TauCeti.IsAutomatic.{u} (k : ℕ) [NeZero k] {Δ : Type u} (a : ℕ → Δ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAutomatic`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence.html#TauCeti.IsAutomatic).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAutomatic`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence.html#TauCeti.IsAutomatic)
- [Source of `TauCeti.IsAutomatic` in TauCeti/Computability/AutomaticSequence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/AutomaticSequence.lean#L67)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
