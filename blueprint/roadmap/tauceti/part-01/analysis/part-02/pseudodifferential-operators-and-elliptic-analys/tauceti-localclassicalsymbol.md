---
declaration: structure
origin: cited
lean: TauCeti.LocalClassicalSymbol
statement: formalized
---

# TauCeti.LocalClassicalSymbol

A classical symbol of order `m` on `U × ℝⁿ`, for an open set `U ⊆ ℝⁿ` of positions: a symbol
`a` of order `m` on `U` together with homogeneous terms `a_{m-j}` of degree `m - j` on `U` for
`j = 0, 1, 2, …`, such that for some frequency cutoff `χ` and every `N`, the remainder
`a - ∑_{j<N} χ(ξ) a_{m-j}` is a symbol of order `m - N` on `U`. The expansion then holds for every
cutoff (`TauCeti.LocalClassicalSymbol.exists_remainder`), and the terms are determined by the
symbol (`TauCeti.LocalClassicalSymbol.ext`).

```lean
TauCeti.LocalClassicalSymbol.{u_1, u_2} {n : ℕ}
  (U : TopologicalSpace.Opens (TauCeti.CoordinateSpace n)) (V : Type u_1) (W : Type u_2)
  [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup W] [NormedSpace ℂ W] (m : ℝ) :
  Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalClassicalSymbol`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/LocalSymbol/Classical.html#TauCeti.LocalClassicalSymbol).

## Sources

- [Tau Ceti documentation: `TauCeti.LocalClassicalSymbol`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/LocalSymbol/Classical.html#TauCeti.LocalClassicalSymbol)
- [Source of `TauCeti.LocalClassicalSymbol` in TauCeti/Analysis/Pseudodifferential/LocalSymbol/Classical.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/LocalSymbol/Classical.lean#L66)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
