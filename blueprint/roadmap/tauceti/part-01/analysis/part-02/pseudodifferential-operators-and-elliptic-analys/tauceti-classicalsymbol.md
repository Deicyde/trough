---
declaration: structure
origin: cited
lean: TauCeti.ClassicalSymbol
statement: formalized
---

# TauCeti.ClassicalSymbol

A classical symbol of order `m` on `ℝⁿ`: a symbol `a` of order `m` together with homogeneous
terms `a_{m-j}` of degree `m - j` for `j = 0, 1, 2, …`, such that for some frequency cutoff `χ` and
every `N`, the remainder `a - ∑_{j<N} χ(ξ) a_{m-j}` is a symbol of order `m - N`. The expansion
then holds for every cutoff (`TauCeti.ClassicalSymbol.exists_remainder`), and the terms are
determined by the symbol (`TauCeti.ClassicalSymbol.ext`).

```lean
TauCeti.ClassicalSymbol.{u_1, u_2} (n : ℕ) (V : Type u_1) (W : Type u_2) [NormedAddCommGroup V]
  [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W] (m : ℝ) : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassicalSymbol`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Symbol/Classical.html#TauCeti.ClassicalSymbol).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassicalSymbol`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Symbol/Classical.html#TauCeti.ClassicalSymbol)
- [Source of `TauCeti.ClassicalSymbol` in TauCeti/Analysis/Pseudodifferential/Symbol/Classical.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/Symbol/Classical.lean#L122)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
