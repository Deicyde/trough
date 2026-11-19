---
declaration: theorem
origin: cited
lean: TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder
statement: formalized
proof: formalized
---

# The asymptotic expansion of the composition symbol

For every `N`,
`a # b = ∑_{k < N} sharpTerm a b k + sharpRemainder a b hb N`, where `sharpTerm a b k` is the
term `((-i)^k / k!) ∑_{|w| = k} ∂_ξ^w a ∘ ∂_x^w b` of order `m' + m - k` and the remainder is a
symbol of order `m' + m - N`.

```lean
TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder.{u_1, u_2, u_3} {n : ℕ} {m m' : ℝ}
  {V : Type u_1} {W : Type u_2} {U : Type u_3} [NormedAddCommGroup V] [NormedSpace ℂ V]
  [NormedAddCommGroup W] [NormedSpace ℂ W] [NormedAddCommGroup U] [NormedSpace ℂ U]
  {a : TauCeti.Symbol n W U m'} {b : TauCeti.Symbol n V W m} [CompleteSpace W] [CompleteSpace U]
  (hb : b.HasCompactSpatialSupport) (N : ℕ) :
  a.sharp b hb =
    ∑ k ∈ Finset.range N, (TauCeti.Symbol.inclusion ⋯) (a.sharpTerm b k) +
      (TauCeti.Symbol.inclusion ⋯) (a.sharpRemainder b hb N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../part-04/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Expansion.html#TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder).

## Sources

- [Tau Ceti documentation: `TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Expansion.html#TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder)
- [Source of `TauCeti.Symbol.sharp_eq_sum_sharpTerm_add_sharpRemainder` in TauCeti/Analysis/Pseudodifferential/Composition/Expansion.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/Composition/Expansion.lean#L730)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)
