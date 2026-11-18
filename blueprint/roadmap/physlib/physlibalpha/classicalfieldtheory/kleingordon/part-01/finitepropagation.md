---
declaration: module
origin: cited
lean: KleinGordon.energyDensity, KleinGordon.EnergyFields, KleinGordon.EnergyFields.e, KleinGordon.EnergyFields.e', KleinGordon.EnergyFields.hasDerivAt_e, KleinGordon.energy_integrand_nonneg, KleinGordon.WeightFields, KleinGordon.EnergyFields.continuous_e
statement: formalized
proof: formalized
---

# Finite propagation speed

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.FinitePropagation`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean): 32 declarations, 19 with a docstring.

> The weighted local energy decreases.

## i. Overview

> The weighted local energy decreases. The retarded solution vanishes outside the causal future of the
> source.

## ii. Key results

> - `energyDensity` : The energy density `‖v‖² + ∑ᵢ ‖pᵢ‖² + μ ‖u‖²`.
> - `EnergyFields` : Fields with the pointwise derivatives needed for the energy identity of the
>   Klein–Gordon equation, in the basis vectors `b i`.
> - `e` : The energy density of the fields.
> - `e'` : The time derivative of the energy density.
> - `WeightFields` : A weight for the energy: smooth, compactly supported in space uniformly in time,
>   decreasing in time, with a spatial gradient bounded by its time derivative.
> - `flux` : The Lie derivative of the energy flux `⟪v, pᵢ⟫` along `b i`.
> - `energyDeriv` : The time derivative of the weighted energy density.
> - `coneWeight` : The cone weight `N (c - τ - ψ x)` as a weight for the energy estimate.

## iv. References

> None.

## A. The weighted local energy

> - `energyDensity` : The energy density `‖v‖² + ∑ᵢ ‖pᵢ‖² + μ ‖u‖²`.
> - `EnergyFields` : Fields with the pointwise derivatives needed for the energy identity of the
>   Klein–Gordon equation, in the basis vectors `b i`.
> - `e` : The energy density of the fields.
> - `e'` : The time derivative of the energy density.
> - `WeightFields` : A weight for the energy: smooth, compactly supported in space uniformly in time,
>   decreasing in time, with a spatial gradient bounded by its time derivative.
> - `flux` : The Lie derivative of the energy flux `⟪v, pᵢ⟫` along `b i`.
> - `energyDeriv` : The time derivative of the weighted energy density.
>
> Lemmas: `hasDerivAt_e`, `energy_integrand_nonneg`, `continuous_e`, `continuous_e'`,
> `hasLineDerivAt_flux`, `e'_eq`, `continuous_energyDeriv`, `hasCompactSupport_of_vanishing`,
> `hasDerivAt_energy`, `integral_energyDeriv` and more.

## B. The cone weight

> - `coneWeight` : The cone weight `N (c - τ - ψ x)` as a weight for the energy estimate.
>
> Lemmas: `continuous_coneArg`.

## C. Finite propagation speed for the homogeneous Klein–Gordon evolution

> - `evolveFields` : The evolved field of the Cauchy data `(f0, f1)` as fields for the energy
>   estimate, in the orthonormal basis `stdOrthonormalBasis`.
>
> Lemmas: `evolveU_zero_time`, `evolveV_zero_time`, `sineEvolution_apply_eq_zero`,
> `functional_sineEvolution`, `sineEvolution_apply_eq_zero'`.

## D. Causal support of the retarded solution

> Lemmas: `sineEvolution_slice_eq_zero`, `solution_eq_zero_of_not_mem_causalFuture`,
> `tsupport_solution_subset`, `advancedSolution_eq_zero_of_not_mem_causalPast`,
> `tsupport_advancedSolution_subset`.

**`KleinGordon.energyDensity`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L100).

> The energy density `‖v‖² + ∑ᵢ ‖pᵢ‖² + μ ‖u‖²`.

```lean
def energyDensity {ι : Type*} [Fintype ι] (μ : ℝ) (u v : ℂ) (p : ι → ℂ) : ℝ
```

**`KleinGordon.EnergyFields`**, a structure, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L106).

> Fields with the pointwise derivatives needed for the energy identity of the Klein–Gordon
> equation, in the basis vectors `b i`. The field is `u` with velocity `v`, the spatial derivatives
> are `p i`, the time derivatives of those are `q i`, and the second spatial derivatives are `s i`.

```lean
structure EnergyFields {ι : Type*} [Fintype ι] (μ : ℝ) (b : ι → E) where
  /-- The field. -/
  u : ℝ → E → ℂ
  /-- The velocity. -/
  v : ℝ → E → ℂ
  /-- The derivative of the field along `b i`. -/
  p : ι → ℝ → E → ℂ
  /-- The derivative of the velocity along `b i`. -/
  q : ι → ℝ → E → ℂ
  /-- The second derivative of the field along `b i`. -/
  s : ι → ℝ → E → ℂ
  hu : ∀ τ x, HasDerivAt (fun r => u r x) (v τ x) τ
  hv : ∀ τ x, HasDerivAt (fun r => v r x) (∑ i, s i τ x - μ • u τ x) τ
  hp : ∀ i τ x, HasDerivAt (fun r => p i r x) (q i τ x) τ
  hpx : ∀ i τ x, HasLineDerivAt ℝ (p i τ) (s i τ x) x (b i)
  hvx : ∀ i τ x, HasLineDerivAt ℝ (v τ) (q i τ x) x (b i)
  cu : Continuous fun z : ℝ × E => u z.1 z.2
  cv : Continuous fun z : ℝ × E => v z.1 z.2
  cp : ∀ i, Continuous fun z : ℝ × E => p i z.1 z.2
  cq : ∀ i, Continuous fun z : ℝ × E => q i z.1 z.2
  cs : ∀ i, Continuous fun z : ℝ × E => s i z.1 z.2
```

**`KleinGordon.EnergyFields.e`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L139).

> The energy density of the fields.

```lean
def e (τ : ℝ) (x : E) : ℝ
```

**`KleinGordon.EnergyFields.e'`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L143).

> The time derivative of the energy density.

```lean
def e' (τ : ℝ) (x : E) : ℝ
```

**`KleinGordon.EnergyFields.hasDerivAt_e`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L148).

```lean
lemma hasDerivAt_e (τ : ℝ) (x : E) : HasDerivAt (fun r => D.e r x) (D.e' τ x) τ
```

**`KleinGordon.energy_integrand_nonneg`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L167).

> The pointwise inequality behind the monotonicity of the weighted energy.

```lean
lemma energy_integrand_nonneg {ι : Type*} [Fintype ι] (m V : ℝ) (hm : 0 ≤ m)
    (wg P G : ι → ℝ) (hP : ∀ i, 0 ≤ P i) (hG : ∀ i, |G i| ≤ V * P i)
    (hgrad : ∑ i, wg i ^ 2 ≤ m ^ 2) :
    0 ≤ m * (V ^ 2 + ∑ i, P i ^ 2) + 2 * ∑ i, wg i * G i
```

**`KleinGordon.WeightFields`**, a structure, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L202).

> A weight for the energy: smooth, compactly supported in space uniformly in time, decreasing in
> time, with a spatial gradient bounded by its time derivative.

```lean
structure WeightFields {ι : Type*} [Fintype ι] (b : ι → E) where
  /-- The weight. -/
  w : ℝ → E → ℝ
  /-- Its time derivative. -/
  wτ : ℝ → E → ℝ
  /-- Its derivative along `b i`. -/
  wg : ι → ℝ → E → ℝ
  hw : ∀ τ x, HasDerivAt (fun r => w r x) (wτ τ x) τ
  hwx : ∀ i τ x, HasLineDerivAt ℝ (w τ) (wg i τ x) x (b i)
  cw : Continuous fun z : ℝ × E => w z.1 z.2
  cwτ : Continuous fun z : ℝ × E => wτ z.1 z.2
  cwg : ∀ i, Continuous fun z : ℝ × E => wg i z.1 z.2
  /-- The radius of the common spatial support. -/
  R : ℝ
  hR : ∀ τ x, -1 ≤ τ → R < ‖x‖ → w τ x = 0 ∧ wτ τ x = 0 ∧ ∀ i, wg i τ x = 0
  sign : ∀ τ x, wτ τ x ≤ 0
  grad : ∀ τ x, ∑ i, wg i τ x ^ 2 ≤ wτ τ x ^ 2
```

**`KleinGordon.EnergyFields.continuous_e`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L231).

```lean
lemma continuous_e : Continuous fun z : ℝ × E => D.e z.1 z.2
```

**`KleinGordon.EnergyFields.continuous_e'`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L238).

```lean
lemma continuous_e' : Continuous fun z : ℝ × E => D.e' z.1 z.2
```

**`KleinGordon.EnergyFields.flux`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L249).

> The Lie derivative of the energy flux `⟪v, pᵢ⟫` along `b i`.

```lean
def flux (i : ι) (τ : ℝ) (x : E) : ℝ
```

**`KleinGordon.EnergyFields.hasLineDerivAt_flux`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L252).

```lean
lemma hasLineDerivAt_flux (i : ι) (τ : ℝ) (x : E) :
    HasLineDerivAt ℝ (D.flux i τ) (inner ℝ (D.q i τ x) (D.p i τ x) + inner ℝ (D.v τ x) (D.s i τ x))
      x (b i)
```

**`KleinGordon.EnergyFields.e'_eq`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L260).

```lean
lemma e'_eq (τ : ℝ) (x : E) : D.e' τ x =
    2 * ∑ i, (inner ℝ (D.q i τ x) (D.p i τ x) + inner ℝ (D.v τ x) (D.s i τ x))
```

**`KleinGordon.EnergyFields.energyDeriv`**, a def, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L276).

> The time derivative of the weighted energy density.

```lean
def energyDeriv (τ : ℝ) (x : E) : ℝ
```

**`KleinGordon.EnergyFields.continuous_energyDeriv`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L279).

```lean
lemma continuous_energyDeriv : Continuous fun z : ℝ × E => D.energyDeriv W z.1 z.2
```

**`KleinGordon.EnergyFields.hasCompactSupport_of_vanishing`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L283).

```lean
lemma hasCompactSupport_of_vanishing (g : E → ℝ) (hg : ∀ x, W.R < ‖x‖ → g x = 0) :
    HasCompactSupport g
```

**`KleinGordon.EnergyFields.hasDerivAt_energy`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L287).

```lean
lemma hasDerivAt_energy {τ0 : ℝ} (hτ0 : 0 ≤ τ0) :
    HasDerivAt (fun τ => ∫ x, W.w τ x * D.e τ x) (∫ x, D.energyDeriv W τ0 x) τ0
```

**`KleinGordon.EnergyFields.integral_energyDeriv`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L328).

```lean
lemma integral_energyDeriv {τ0 : ℝ} (hτ0 : 0 ≤ τ0) :
    ∫ x, D.energyDeriv W τ0 x =
      ∫ x, (W.wτ τ0 x * D.e τ0 x - 2 * ∑ i, W.wg i τ0 x * D.flux i τ0 x)
```

**`KleinGordon.EnergyFields.integral_energyDeriv_nonpos`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L393).

```lean
lemma integral_energyDeriv_nonpos (hμ : 0 ≤ μ) {τ0 : ℝ} (hτ0 : 0 ≤ τ0) : ∫ x, D.energyDeriv W τ0 x ≤
    0
```

**`KleinGordon.EnergyFields.antitoneOn_energy`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L409).

> The weighted energy is non-increasing in time, for nonnegative times.

```lean
lemma antitoneOn_energy (hμ : 0 ≤ μ) :
    AntitoneOn (fun τ => ∫ x, W.w τ x * D.e τ x) (Set.Ici 0)
```

**`KleinGordon.continuous_coneArg`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L430).

```lean
lemma continuous_coneArg (ε c : ℝ) (x₀ : E) :
    Continuous fun z : ℝ × E => c - z.1 - smoothDist ε x₀ z.2
```

**`KleinGordon.coneWeight`**, a def, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L435).

> The cone weight `N (c - τ - ψ x)` as a weight for the energy estimate.

```lean
def coneWeight {ε : ℝ} (hε : 0 < ε) (x₀ : E) (c : ℝ) :
    WeightFields (fun i : Fin (Module.finrank ℝ E) => stdOrthonormalBasis ℝ E i)
```

**`KleinGordon.evolveFields`**, a def, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L502).

> The evolved field of the Cauchy data `(f0, f1)` as fields for the energy estimate, in the
> orthonormal basis `stdOrthonormalBasis`.

```lean
def evolveFields {μ : ℝ} (hμ : 0 ≤ μ) (f0 f1 : 𝓢(E, ℂ)) :
    EnergyFields μ (fun i : Fin (Module.finrank ℝ E) => stdOrthonormalBasis ℝ E i)
```

**`KleinGordon.evolveU_zero_time`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L534).

```lean
lemma evolveU_zero_time (μ : ℝ) (a b : 𝓢(E, ℂ)) : evolveU μ 0 a b = a
```

**`KleinGordon.evolveV_zero_time`**, a lemma, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L537).

```lean
lemma evolveV_zero_time (μ : ℝ) (a b : 𝓢(E, ℂ)) : evolveV μ 0 a b = b
```

**`KleinGordon.sineEvolution_apply_eq_zero`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L542).

> **Finite propagation speed.** If the initial velocity `g` vanishes on the ball of radius
> `r + δ` about `x₀` then the sine evolution over the time `r ≥ 0` vanishes at `x₀`.

```lean
lemma sineEvolution_apply_eq_zero {μ : ℝ} (hμ : 0 ≤ μ) (g : 𝓢(E, ℂ)) (x₀ : E) {r δ : ℝ}
    (hr : 0 ≤ r) (hδ : 0 < δ) (hg : ∀ y, g y ≠ 0 → r + δ ≤ ‖y - x₀‖) :
    sineEvolution ℂ r μ g x₀ = 0
```

**`KleinGordon.functional_sineEvolution`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L633).

> A continuous linear functional commutes with the sine evolution.

```lean
lemma functional_sineEvolution {μ : ℝ} (hμ : 0 ≤ μ) (ℓ : F →L[ℂ] ℂ) (r : ℝ) (g : 𝓢(E, F)) (x : E) :
    ℓ (sineEvolution F r μ g x) =
      sineEvolution ℂ r μ (SchwartzMap.postcompCLM (𝕜 := ℂ) (E := E) ℓ g) x
```

**`KleinGordon.sineEvolution_apply_eq_zero'`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L646).

> **Finite propagation speed for vector-valued data.**

```lean
lemma sineEvolution_apply_eq_zero' {μ : ℝ} (hμ : 0 ≤ μ) (g : 𝓢(E, F)) (x₀ : E) {r δ : ℝ}
    (hr : 0 ≤ r) (hδ : 0 < δ) (hg : ∀ y, g y ≠ 0 → r + δ ≤ ‖y - x₀‖) :
    sineEvolution F r μ g x₀ = 0
```

**`KleinGordon.sineEvolution_slice_eq_zero`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L662).

> Each slice of the source propagates only inside the light cone.

```lean
lemma sineEvolution_slice_eq_zero {μ : ℝ} (hμ : 0 ≤ μ) {s t : ℝ} (hst : s ≤ t) {x₀ : E}
    (hfut : ∀ y, (s, y) ∈ tsupport f → t - s < ‖y - x₀‖) :
    sineEvolution F (t - s) μ (slice F f s) x₀ = 0
```

**`KleinGordon.solution_eq_zero_of_not_mem_causalFuture`**, a lemma, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L687).

> **Causal support.** The retarded solution vanishes outside the causal future of the support of
> the source.

```lean
lemma solution_eq_zero_of_not_mem_causalFuture {μ : ℝ} (hμ : 0 ≤ μ) {t : ℝ} {x₀ : E}
    (h : (t, x₀) ∉ causalFuture (tsupport f)) : solution F f μ t x₀ = 0
```

**`KleinGordon.tsupport_solution_subset`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L698).

> The topological support of the retarded field lies in the source's causal future.

```lean
lemma tsupport_solution_subset {μ : ℝ} (hμ : 0 ≤ μ) :
    tsupport (fun p : ℝ × E => solution F f μ p.1 p.2) ⊆ causalFuture (tsupport f)
```

**`KleinGordon.advancedSolution_eq_zero_of_not_mem_causalPast`**, a lemma, [line 706](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L706).

> **Causal support of the advanced solution.**

```lean
lemma advancedSolution_eq_zero_of_not_mem_causalPast {μ : ℝ} (hμ : 0 ≤ μ) {t : ℝ} {x₀ : E}
    (h : (t, x₀) ∉ causalPast (tsupport f)) : advancedSolution F f μ t x₀ = 0
```

**`KleinGordon.tsupport_advancedSolution_subset`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean#L716).

> The topological support of the advanced field lies in the source's causal past.

```lean
lemma tsupport_advancedSolution_subset {μ : ℝ} (hμ : 0 ≤ μ) :
    tsupport (fun p : ℝ × E => advancedSolution F f μ p.1 p.2) ⊆ causalPast (tsupport f)
```

## Depends on

- [The retarded and advanced solution](retardedsolution.md)
- [A smooth substitute for the distance](../../../mathematics/part-01/calculus/smoothdistance.md)
- [Light cones in time and space](../../../relativity/causality/lightcone.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/FinitePropagation.lean)
