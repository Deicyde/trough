---
declaration: theorem
origin: cited
lean: PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod_pow
statement: formalized
proof: formalized
---

# The Schwarz lemma for restricted series

Let `f` be a power series over a complete
ultrametric normed field `K`, restricted at a radius `c > 0`. Let `Z` be a finite multiset of
points of the closed disc of radius `c` such that `f` vanishes at each `b ∈ Z` to at least the
multiplicity of `b` in `Z`, in the sense that the Hasse derivatives `(D⁽ᵗ⁾ f)(b)` vanish for `t`
below that multiplicity. Then at every point `x` of the closed disc of radius `c` in a complete
normed field extension `L` of `K`,

```text
‖f(x)‖ ≤ ‖f‖_c * ∏_{b ∈ Z} ‖x - b‖ / c,
```

where `‖f‖_c` is the Gauss norm of `f` at `c`.

```lean
PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod.{u_1, u_2} {K : Type u_1} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {c : ℝ} {f : PowerSeries K} [DecidableEq K] {L : Type u_2}
  [NormedField L] [NormedAlgebra K L] [CompleteSpace L] (hf : PowerSeries.IsRestricted c f)
  (hc : 0 < c) {Z : Multiset K} (hZ : ∀ b ∈ Z, ‖b‖ ≤ c)
  (hzero : ∀ b ∈ Z, ∀ t < Multiset.count b Z, ((PowerSeries.hasseDeriv t) f).evalAt b = 0) {x : L}
  (hx : ‖x‖ ≤ c) :
  ‖f.evalAt x‖ ≤
    PowerSeries.gaussNorm norm c f * (Multiset.map (fun b => ‖x - (algebraMap K L) b‖ / c) Z).prod
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Factor theorem for restricted series](factor-theorem-for-restricted-series.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod).

## Other forms

**The Schwarz lemma for distinct zeros with multiplicities.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod_pow).

```lean
PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod_pow.{u_1, u_2} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] {c : ℝ} {f : PowerSeries K} {L : Type u_2}
  [NormedField L] [NormedAlgebra K L] [CompleteSpace L] (hf : PowerSeries.IsRestricted c f)
  (hc : 0 < c) {s : Finset K} {T : K → ℕ} (hs : ∀ b ∈ s, ‖b‖ ≤ c)
  (hzero : ∀ b ∈ s, ∀ t < T b, ((PowerSeries.hasseDeriv t) f).evalAt b = 0) {x : L} (hx : ‖x‖ ≤ c) :
  ‖f.evalAt x‖ ≤ PowerSeries.gaussNorm norm c f * ∏ b ∈ s, (‖x - (algebraMap K L) b‖ / c) ^ T b
```

## Sources

- [Tau Ceti documentation: `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod)
- [Source of `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod` in TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.lean#L135)
