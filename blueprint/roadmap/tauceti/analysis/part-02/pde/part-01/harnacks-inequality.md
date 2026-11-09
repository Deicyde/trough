---
declaration: theorem
origin: cited
lean: IsCompact.harnack_inequality, InnerProductSpace.HarmonicOnNhd.harnack_inequality, InnerProductSpace.HarmonicContOnCl.harnack_inequality_of_nonneg_on_sphere
statement: formalized
proof: formalized
---

# Harnack's inequality

Let `K` be a compact subset of a preconnected open set `U`. There
is a constant `C`, depending only on `K` and `U`, such that every function `u` harmonic and
nonnegative on `U` satisfies `u x ≤ C * u y` for all `x, y ∈ K`; that is,
`sup_K u ≤ C * inf_K u`.

```lean
IsCompact.harnack_inequality.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] {K U : Set E} (hK : IsCompact K) (hU : IsOpen U) (hUc : IsPreconnected U)
  (hKU : K ⊆ U) :
  ∃ C,
    0 ≤ C ∧
      ∀ (u : E → ℝ),
        InnerProductSpace.HarmonicOnNhd u U → (∀ z ∈ U, 0 ≤ u z) → ∀ x ∈ K, ∀ y ∈ K, u x ≤ C * u y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The centered Harnack inequality on a planar disk](the-centered-harnack-inequality-on-a-planar-disk.md)
- [The local Harnack inequality](the-local-harnack-inequality.md)

## Lean

Formalized in Tau Ceti as [`IsCompact.harnack_inequality`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Basic.html#IsCompact.harnack_inequality).

## Other forms

**Harnack's inequality on a smaller closed disk.** Formalized in Tau Ceti as [`InnerProductSpace.HarmonicOnNhd.harnack_inequality`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Planar.html#InnerProductSpace.HarmonicOnNhd.harnack_inequality).

```lean
InnerProductSpace.HarmonicOnNhd.harnack_inequality {f : ℂ → ℝ} {c : ℂ} {R : ℝ}
  (hf : InnerProductSpace.HarmonicOnNhd f (Metric.ball c R))
  (hnonneg : ∀ z ∈ Metric.ball c R, 0 ≤ f z) {r : ℝ} (hrR : r < R) {x y : ℂ}
  (hx : x ∈ Metric.closedBall c r) (hy : y ∈ Metric.closedBall c r) :
  f x ≤ ((R + r) / (R - r)) ^ 2 * f y
```

**Harnack's inequality on a smaller closed disk, from boundary nonnegativity.** Formalized in Tau Ceti as [`InnerProductSpace.HarmonicContOnCl.harnack_inequality_of_nonneg_on_sphere`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Planar.html#InnerProductSpace.HarmonicContOnCl.harnack_inequality_of_nonneg_on_sphere).

```lean
InnerProductSpace.HarmonicContOnCl.harnack_inequality_of_nonneg_on_sphere {f : ℂ → ℝ} {c : ℂ}
  {R : ℝ} (hf : InnerProductSpace.HarmonicContOnCl f (Metric.ball c R))
  (hnonneg : ∀ z ∈ Metric.sphere c R, 0 ≤ f z) {r : ℝ} (hrR : r < R) {x y : ℂ}
  (hx : x ∈ Metric.closedBall c r) (hy : y ∈ Metric.closedBall c r) :
  f x ≤ ((R + r) / (R - r)) ^ 2 * f y
```

## Sources

- [Tau Ceti documentation: `IsCompact.harnack_inequality`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Basic.html#IsCompact.harnack_inequality)
- [Source of `IsCompact.harnack_inequality` in TauCeti/Analysis/PDE/Harnack/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Harnack/Basic.lean#L174)
