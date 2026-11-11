---
declaration: theorem
origin: cited
lean: PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod_pow, PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod
statement: formalized
proof: formalized
---

# The Schwarz lemma for Hasse derivatives

Let `f` be a power series over a complete
ultrametric normed field `K`, restricted at a radius `c > 0`, and let `s` be a finite set of points
of the closed disc of radius `c` at each of which the Hasse derivatives `(D⁽ᵗ⁾ f)(b)` vanish for
`t < T b`. Then for every `k` and every point `x` of the closed disc of radius `c` in a complete
normed field extension `L` of `K`,

```text
‖(D⁽ᵏ⁾ f)(x)‖ ≤ c⁻ᵏ * ‖f‖_c * ∏_{b ∈ s} (‖x - b‖ / c) ^ (T b - k).
```

For `k = 0` this is `PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod_pow`.

```lean
PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow.{u_1, u_2} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] {c : ℝ} {f : PowerSeries K} {L : Type u_2}
  [NormedField L] [NormedAlgebra K L] [CompleteSpace L] (hf : PowerSeries.IsRestricted c f)
  (hc : 0 < c) {s : Finset K} {T : K → ℕ} (hs : ∀ b ∈ s, ‖b‖ ≤ c)
  (hzero : ∀ b ∈ s, ∀ t < T b, ((PowerSeries.hasseDeriv t) f).evalAt b = 0) (k : ℕ) {x : L}
  (hx : ‖x‖ ≤ c) :
  ‖((PowerSeries.hasseDeriv k) f).evalAt x‖ ≤
    c⁻¹ ^ k * PowerSeries.gaussNorm norm c f * ∏ b ∈ s, (‖x - (algebraMap K L) b‖ / c) ^ (T b - k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Factor theorem for restricted series](factor-theorem-for-restricted-series.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow).

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

**The Schwarz lemma for restricted series.** Formalized in Tau Ceti as [`PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.norm_evalAt_le_gaussNorm_mul_prod).

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

## Sources

- [Tau Ceti documentation: `PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow)
- [Source of `PowerSeries.IsRestricted.norm_evalAt_hasseDeriv_le_gaussNorm_mul_prod_pow` in TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.lean#L211)
