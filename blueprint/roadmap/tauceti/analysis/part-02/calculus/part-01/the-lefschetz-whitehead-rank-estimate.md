---
declaration: theorem
origin: cited
lean: HasFDerivAt.finrank_range_lt_of_infinite, HasFDerivAt.finrank_range_lt_of_infinite_of_norm_eq
statement: formalized
proof: formalized
---

# The Lefschetz–Whitehead rank estimate

Let `g` and `h` be differentiable at `x`, with
`h x` outside the range of the derivative `h'` of `h`. If the swept map
`(y, t) ↦ g y + t • h y` has rank at most `p` at `(x, t)` for infinitely many `t`, for instance
for every `t` near `0`, then `h` has rank less than `p` at `x`.

```lean
HasFDerivAt.finrank_range_lt_of_infinite.{u_1, u_2, u_3} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {F : Type u_3} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {g h : E → F} {g' h' : E →L[𝕜] F} {x : E} [FiniteDimensional 𝕜 F]
  (hh : HasFDerivAt h h' x) (hg : HasFDerivAt g g' x) (hx : h x ∉ (↑h').range) {p : ℕ}
  (hp :
    {t |
        Module.finrank 𝕜 ↥(↑(fderiv 𝕜 (fun q => g q.1 + q.2 • h q.1) (x, t))).range ≤ p}.Infinite) :
  Module.finrank 𝕜 ↥(↑h').range < p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasFDerivAt.finrank_range_lt_of_infinite`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/RankDrop.html#HasFDerivAt.finrank_range_lt_of_infinite).

## Other forms

**The Lefschetz–Whitehead rank estimate for unit directions.** Formalized in Tau Ceti as [`HasFDerivAt.finrank_range_lt_of_infinite_of_norm_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/RankDrop.html#HasFDerivAt.finrank_range_lt_of_infinite_of_norm_eq).

```lean
HasFDerivAt.finrank_range_lt_of_infinite_of_norm_eq.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {F : Type u_2} [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  [FiniteDimensional ℝ F] {g h : E → F} {g' h' : E →L[ℝ] F} {x : E} (hh : HasFDerivAt h h' x)
  (hg : HasFDerivAt g g' x) (hn : ∀ᶠ (y : E) in nhds x, ‖h y‖ = ‖h x‖) (h0 : h x ≠ 0) {p : ℕ}
  (hp :
    {t |
        Module.finrank ℝ ↥(↑(fderiv ℝ (fun q => g q.1 + q.2 • h q.1) (x, t))).range ≤ p}.Infinite) :
  Module.finrank ℝ ↥(↑h').range < p
```

## Sources

- [Tau Ceti documentation: `HasFDerivAt.finrank_range_lt_of_infinite`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/RankDrop.html#HasFDerivAt.finrank_range_lt_of_infinite)
- [Source of `HasFDerivAt.finrank_range_lt_of_infinite` in TauCeti/Analysis/Calculus/FDeriv/RankDrop.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/FDeriv/RankDrop.lean#L69)
