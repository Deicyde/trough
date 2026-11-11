---
declaration: theorem
origin: cited
lean: TauCeti.tsupport_quantizeSchwartzValue_subset_iff
statement: formalized
proof: formalized
---

# Output support

Let `K` be a closed set of positions, and let every frequency slice
`ξ ↦ a(x, ξ)` with `x ∉ K` be continuous with polynomial growth. Then `Op(a) u` is supported in
`K` for every compactly supported Schwartz function `u` if and only if `a(x, ξ) = 0` for every
`x ∉ K` and every frequency `ξ`.

```lean
TauCeti.tsupport_quantizeSchwartzValue_subset_iff.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {V : Type u_2} {W : Type u_3} [NormedAddCommGroup V] [NormedSpace ℂ V]
  [CompleteSpace V] [NormedAddCommGroup W] [NormedSpace ℂ W] [CompleteSpace W]
  {a : E × E → V →L[ℂ] W} {K : Set E} (hK : IsClosed K) (ha : ∀ x ∉ K, Continuous fun ξ => a (x, ξ))
  (hC : ∀ x ∉ K, ∃ C m, ∀ (ξ : E), ‖a (x, ξ)‖ ≤ C * (1 + ‖ξ‖ ^ 2) ^ (m / 2)) :
  (∀ (u : SchwartzMap E V),
      HasCompactSupport ⇑u → tsupport (TauCeti.quantizeSchwartzValue a u) ⊆ K) ↔
    ∀ x ∉ K, ∀ (ξ : E), a (x, ξ) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tsupport_quantizeSchwartzValue_subset_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/OutputSupport.html#TauCeti.tsupport_quantizeSchwartzValue_subset_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.tsupport_quantizeSchwartzValue_subset_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/OutputSupport.html#TauCeti.tsupport_quantizeSchwartzValue_subset_iff)
- [Source of `TauCeti.tsupport_quantizeSchwartzValue_subset_iff` in TauCeti/Analysis/Pseudodifferential/OutputSupport.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/OutputSupport.lean#L126)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
