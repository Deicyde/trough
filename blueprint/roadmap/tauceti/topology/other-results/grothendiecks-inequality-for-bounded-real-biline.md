---
declaration: theorem
origin: cited
lean: LinearMap.abs_sum_apply_apply_le_eight_mul, LinearMap.norm_sum_apply_apply_le_sixteen_mul
statement: formalized
proof: formalized
---

# Grothendieck's inequality for bounded real bilinear forms on spaces of continuous functions, with constant `κ_ℝ = 8`

Let `K` and `L` be compact normal spaces and `B` a bilinear
form on `C(K, ℝ) × C(L, ℝ)` with `|B f g| ≤ C * ‖f‖ * ‖g‖`. If `∑ i, f i x ^ 2 ≤ 1` and
`∑ i, g i y ^ 2 ≤ 1` everywhere, then `|∑ i, B (f i) (g i)| ≤ 8 * C`.

```lean
LinearMap.abs_sum_apply_apply_le_eight_mul.{u_1, u_2, u_4} {K : Type u_1} {L : Type u_2}
  {ι : Type u_4} [TopologicalSpace K] [CompactSpace K] [TopologicalSpace L] [CompactSpace L]
  [Fintype ι] [NormalSpace K] [NormalSpace L] (B : C(K, ℝ) →ₗ[ℝ] C(L, ℝ) →ₗ[ℝ] ℝ) {C : ℝ}
  (hC : 0 ≤ C) (hB : ∀ (f : C(K, ℝ)) (g : C(L, ℝ)), |(B f) g| ≤ C * ‖f‖ * ‖g‖) {f : ι → C(K, ℝ)}
  {g : ι → C(L, ℝ)} (hf : ∀ (x : K), ∑ i, (f i) x ^ 2 ≤ 1) (hg : ∀ (y : L), ∑ i, (g i) y ^ 2 ≤ 1) :
  |∑ i, (B (f i)) (g i)| ≤ 8 * C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's inequality over the reals, with constant `κ_ℝ = 8`](../../analysis/part-02/matrix/grothendiecks-inequality-over-the-reals-with-con.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.abs_sum_apply_apply_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.abs_sum_apply_apply_le_eight_mul).

## Other forms

**Grothendieck's inequality for bounded bilinear forms on spaces of continuous functions, over an `RCLike` field with constant `κ_𝕜 = 16`.** Formalized in Tau Ceti as [`LinearMap.norm_sum_apply_apply_le_sixteen_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.norm_sum_apply_apply_le_sixteen_mul).

```lean
LinearMap.norm_sum_apply_apply_le_sixteen_mul.{u_1, u_2, u_3, u_4} {K : Type u_1} {L : Type u_2}
  {𝕜 : Type u_3} {ι : Type u_4} [TopologicalSpace K] [CompactSpace K] [TopologicalSpace L]
  [CompactSpace L] [RCLike 𝕜] [Fintype ι] [NormalSpace K] [NormalSpace L]
  (B : C(K, 𝕜) →ₗ[𝕜] C(L, 𝕜) →ₗ[𝕜] 𝕜) {C : ℝ} (hC : 0 ≤ C)
  (hB : ∀ (f : C(K, 𝕜)) (g : C(L, 𝕜)), ‖(B f) g‖ ≤ C * ‖f‖ * ‖g‖) {f : ι → C(K, 𝕜)}
  {g : ι → C(L, 𝕜)} (hf : ∀ (x : K), ∑ i, ‖(f i) x‖ ^ 2 ≤ 1)
  (hg : ∀ (y : L), ∑ i, ‖(g i) y‖ ^ 2 ≤ 1) : ‖∑ i, (B (f i)) (g i)‖ ≤ 16 * C
```

## Sources

- [Tau Ceti documentation: `LinearMap.abs_sum_apply_apply_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.abs_sum_apply_apply_le_eight_mul)
- [Source of `LinearMap.abs_sum_apply_apply_le_eight_mul` in TauCeti/Topology/ContinuousMap/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/ContinuousMap/Grothendieck.lean#L165)
