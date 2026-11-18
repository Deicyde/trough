---
declaration: theorem
origin: cited
lean: LinearMap.abs_sum_apply_apply_le_eight_mul
statement: formalized
proof: formalized
---

# Grothendieck's inequality (`LinearMap.abs_sum_apply_apply_le_eight_mul`)

**Grothendieck's inequality** for bounded real bilinear forms on spaces of continuous
functions, with constant `κ_ℝ = 8`. Let `K` and `L` be compact spaces and `B` a bilinear
form on `C(K, ℝ) × C(L, ℝ)` with `|B f g| ≤ C * ‖f‖ * ‖g‖`. If `∑ i, f i x ^ 2 ≤ 1` and
`∑ i, g i y ^ 2 ≤ 1` everywhere, then `|∑ i, B (f i) (g i)| ≤ 8 * C`.

```lean
LinearMap.abs_sum_apply_apply_le_eight_mul.{u_1, u_2, u_4} {K : Type u_1} {L : Type u_2}
  {ι : Type u_4} [TopologicalSpace K] [CompactSpace K] [TopologicalSpace L] [CompactSpace L]
  [Fintype ι] (B : C(K, ℝ) →ₗ[ℝ] C(L, ℝ) →ₗ[ℝ] ℝ) {C : ℝ} (hC : 0 ≤ C)
  (hB : ∀ (f : C(K, ℝ)) (g : C(L, ℝ)), |(B f) g| ≤ C * ‖f‖ * ‖g‖) {f : ι → C(K, ℝ)}
  {g : ι → C(L, ℝ)} (hf : ∀ (x : K), ∑ i, (f i) x ^ 2 ≤ 1) (hg : ∀ (y : L), ∑ i, (g i) y ^ 2 ≤ 1) :
  |∑ i, (B (f i)) (g i)| ≤ 8 * C
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Grothendieck's inequality over the reals, with constant `κ_ℝ = 8`](grothendiecks-inequality-over-the-reals-with-con.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.abs_sum_apply_apply_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.abs_sum_apply_apply_le_eight_mul).

## Sources

- [Tau Ceti documentation: `LinearMap.abs_sum_apply_apply_le_eight_mul`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Grothendieck.html#LinearMap.abs_sum_apply_apply_le_eight_mul)
- [Source of `LinearMap.abs_sum_apply_apply_le_eight_mul` in TauCeti/Topology/ContinuousMap/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/ContinuousMap/Grothendieck.lean#L156)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
