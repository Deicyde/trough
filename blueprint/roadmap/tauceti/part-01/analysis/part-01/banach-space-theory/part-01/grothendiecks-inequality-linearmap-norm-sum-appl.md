---
declaration: theorem
origin: cited
lean: LinearMap.norm_sum_apply_apply_le_sixteen_mul
statement: formalized
proof: formalized
---

# Grothendieck's inequality (`LinearMap.norm_sum_apply_apply_le_sixteen_mul`)

**Grothendieck's inequality** for bounded bilinear forms on spaces of continuous functions,
over an `RCLike` field with constant `κ_𝕜 = 16`. Let `K` and `L` be compact spaces and
`B` a bilinear form on `C(K, 𝕜) × C(L, 𝕜)` with `‖B f g‖ ≤ C * ‖f‖ * ‖g‖`, such as a continuous
bilinear form with `C = ‖B‖`. If the families `f i` in `C(K, 𝕜)` and `g i` in `C(L, 𝕜)` have
square functions bounded by one, then `‖∑ i, B (f i) (g i)‖ ≤ 16 * C`. Over `ℝ`,
`LinearMap.abs_sum_apply_apply_le_eight_mul` gives the constant `8`.

```lean
LinearMap.norm_sum_apply_apply_le_sixteen_mul.{u_1, u_2, u_3, u_4} {K : Type u_1} {L : Type u_2}
  {𝕜 : Type u_3} {ι : Type u_4} [TopologicalSpace K] [CompactSpace K] [TopologicalSpace L]
  [CompactSpace L] [RCLike 𝕜] [Fintype ι] (B : C(K, 𝕜) →ₗ[𝕜] C(L, 𝕜) →ₗ[𝕜] 𝕜) {C : ℝ} (hC : 0 ≤ C)
  (hB : ∀ (f : C(K, 𝕜)) (g : C(L, 𝕜)), ‖(B f) g‖ ≤ C * ‖f‖ * ‖g‖) {f : ι → C(K, 𝕜)}
  {g : ι → C(L, 𝕜)} (hf : ∀ (x : K), ∑ i, ‖(f i) x‖ ^ 2 ≤ 1)
  (hg : ∀ (y : L), ∑ i, ‖(g i) y‖ ^ 2 ≤ 1) : ‖∑ i, (B (f i)) (g i)‖ ≤ 16 * C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's inequality over an `RCLike` field, with constant `κ_𝕜 = 16`](grothendiecks-inequality-over-an-rclike-field-wi.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.norm_sum_apply_apply_le_sixteen_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.norm_sum_apply_apply_le_sixteen_mul).

## Sources

- [Tau Ceti documentation: `LinearMap.norm_sum_apply_apply_le_sixteen_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.norm_sum_apply_apply_le_sixteen_mul)
- [Source of `LinearMap.norm_sum_apply_apply_le_sixteen_mul` in TauCeti/Topology/ContinuousMap/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/ContinuousMap/Grothendieck.lean#L142)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
