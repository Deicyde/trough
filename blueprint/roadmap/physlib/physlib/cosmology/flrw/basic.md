---
declaration: module
origin: cited
lean: Cosmology.SpatialGeometry, Cosmology.SpatialGeometry.S, Cosmology.SpatialGeometry.mul_sinh_as_div, Cosmology.SpatialGeometry.tendsto_sinh_rx_over_x, Cosmology.SpatialGeometry.limit_S_saddle, Cosmology.SpatialGeometry.mul_sin_as_div, Cosmology.SpatialGeometry.tendsto_sin_rx_over_x, Cosmology.SpatialGeometry.limit_S_sphere
statement: formalized
proof: formalized
---

# The Friedmann-Lemaître-Robertson-Walker metric

The module `Physlib.Cosmology.FLRW.Basic`, [Physlib/Cosmology/FLRW/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean): 37 declarations, 31 with a docstring.

> The spatial geometry of an FLRW model and its curvature parameter, the structures `FLRW` and
> `CosmicFluid`, the density and pressure of the cosmological constant as a fluid and the cosmic
> fluid with the cosmological constant folded in, the tangent-line bound for an FLRW model whose
> scale factor decelerates and the resulting lower bound on its interval of time, the first- and
> second-order Friedmann equations, the proposition `FLRW.FriedmannSolution` that a model and a
> fluid solve them, and the Hubble and deceleration parameters.

**`Cosmology.SpatialGeometry`**, an inductive, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L37).

> The inductive type with three constructors:
> - `Spherical (k : ℝ)`
> - `Flat`
> - `Saddle (k : ℝ)`

```lean
inductive SpatialGeometry : Type where
  | Spherical (k : ℝ) (h : k < 0)
  | Flat
  | Saddle (k : ℝ) (h : k > 0)
```

**`Cosmology.SpatialGeometry.S`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L49).

> For `s` corresponding to
> - `Spherical k`, `S s r = k * sin (r / k)`
> - `Flat`, `S s r = r`,
> - `Saddle k`, `S s r = k * sinh (r / k)`.

```lean
noncomputable def S (s : SpatialGeometry) : ℝ → ℝ
```

**`Cosmology.SpatialGeometry.mul_sinh_as_div`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L58).

> The limit of `S (Saddle k) r` as `k → ∞` is equal to `S (Flat) r`.
> First show that `k * sinh(r / k) = sinh(r / k) / (1 / k)` pointwise.

```lean
lemma mul_sinh_as_div (r k : ℝ) :
    k * Real.sinh (r / k) = Real.sinh (r / k) / (1 / k)
```

**`Cosmology.SpatialGeometry.tendsto_sinh_rx_over_x`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L63).

> First, show that limit of `sinh(r * x) / x` is r at the limit x goes to zero.
> Then the next theorem will address the rewrite using Filter.Tendsto.comp

```lean
lemma tendsto_sinh_rx_over_x (r : ℝ) :
    Tendsto (fun x : ℝ => Real.sinh (r * x) / x) (𝓝[≠] 0) (𝓝 r)
```

**`Cosmology.SpatialGeometry.limit_S_saddle`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L68).

```lean
lemma limit_S_saddle (r : ℝ) :
    Tendsto (fun k : ℝ => k * Real.sinh (r / k)) atTop (𝓝 r)
```

**`Cosmology.SpatialGeometry.mul_sin_as_div`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L77).

> The limit of `S (Sphere k) r` as `k → ∞` is equal to `S (Flat) r`.
> First show that `k * sinh(r / k) = sin(r / k) / (1 / k)` pointwise.

```lean
lemma mul_sin_as_div (r k : ℝ) :
    k * Real.sin (r / k) = Real.sin (r / k) / (1 / k)
```

**`Cosmology.SpatialGeometry.tendsto_sin_rx_over_x`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L82).

> First, show that limit of `sin(r * x) / x` is r at the limit x goes to zero.
> Then the next theorem will address the rewrite using Filter.Tendsto.comp

```lean
lemma tendsto_sin_rx_over_x (r : ℝ) :
    Tendsto (fun x : ℝ => Real.sin (r * x) / x) (𝓝[≠] 0) (𝓝 r)
```

**`Cosmology.SpatialGeometry.limit_S_sphere`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L87).

```lean
lemma limit_S_sphere(r : ℝ) :
    Tendsto (fun k : ℝ => k * Real.sin (r / k)) atTop (𝓝 r)
```

**`Cosmology.SpatialGeometry.curvature`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L101).

> The curvature parameter of the spatial geometry, the constant `k` of the first-order
>   Friedmann equation `FLRW.FriedmannEquation.FirstOrderFriedmann`:
> - `1 / k ^ 2` for `Spherical k`, whose profile `S` is that of a sphere of radius `|k|`,
> - `0` for `Flat`,
> - `-1 / k ^ 2` for `Saddle k`, whose profile `S` is that of a hyperbolic space of curvature
>   radius `|k|`.

```lean
noncomputable def curvature : SpatialGeometry → ℝ
```

**`Cosmology.SpatialGeometry.curvature_flat`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L107).

```lean
lemma curvature_flat : Flat.curvature = 0
```

**`Cosmology.SpatialGeometry.curvature_spherical_pos`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L110).

> The spherical geometry has a positive curvature parameter.

```lean
lemma curvature_spherical_pos (k : ℝ) (h : k < 0) : 0 < (Spherical k h).curvature
```

**`Cosmology.SpatialGeometry.curvature_saddle_neg`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L116).

> The saddle geometry has a negative curvature parameter.

```lean
lemma curvature_saddle_neg (k : ℝ) (h : k > 0) : (Saddle k h).curvature < 0
```

**`Cosmology.FLRW`**, a structure, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L128).

> An FLRW model: the scale factor `a` of the Friedmann-Lemaître-Robertson-Walker metric on an
> open interval `I` of cosmic time, positive and twice differentiable on `I`, together with the
> geometry of the spatial slices. The values of `a` outside `I` carry no meaning. The interval
> lets a model begin at a Big Bang, as the Milne model `FLRW.milne` does on
> `I = {t | 0 < t.val}`.

```lean
structure FLRW where
  /-- The interval of cosmic time on which the model is defined. -/
  I : Set Time
  /-- The interval `I` is open. -/
  isOpen_I : IsOpen I
  /-- The set `I` is an interval. -/
  ordConnected_I : I.OrdConnected
  /-- The scale factor as a function of cosmic time. -/
  a : Time → ℝ
  /-- The scale factor is positive on `I`. -/
  a_pos : ∀ t ∈ I, 0 < a t
  /-- The scale factor is differentiable on `I`. -/
  differentiableOn_a : DifferentiableOn ℝ a I
  /-- The time derivative of the scale factor is differentiable on `I`. -/
  differentiableOn_deriv_a : DifferentiableOn ℝ (∂ₜ a) I
  /-- The geometry of the spatial slices. -/
  geometry : SpatialGeometry
```

**`Cosmology.CosmicFluid`**, a structure, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L150).

> The cosmic fluid filling an FLRW model, described by its total energy density `ρ` and its
> pressure `p`, both functions of cosmic time, as in the first- and second-order Friedmann
> equations `FLRW.FriedmannEquation.FirstOrderFriedmann` and
> `FLRW.FriedmannEquation.SecondOrderFriedmann`.

```lean
structure CosmicFluid where
  /-- The total energy density as a function of cosmic time. -/
  ρ : Time → ℝ
  /-- The pressure as a function of cosmic time. -/
  p : Time → ℝ
```

**`Cosmology.CosmicFluid.empty`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L157).

> The empty cosmic fluid, with zero energy density and zero pressure at all times.

```lean
def CosmicFluid.empty : CosmicFluid
```

**`Cosmology.FLRW.FriedmannEquation.cosmologicalConstantDensity`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L160).

> The density `ρ_Λ = Λ c² / (8 π G)` associated with the cosmological constant.

```lean
noncomputable def FLRW.FriedmannEquation.cosmologicalConstantDensity (Λ G : ℝ)
    (c : SpeedOfLight) : ℝ
```

**`Cosmology.FLRW.FriedmannEquation.cosmologicalConstantPressure`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L165).

> The pressure `p_Λ = - ρ_Λ c²` associated with the cosmological constant.

```lean
noncomputable def FLRW.FriedmannEquation.cosmologicalConstantPressure (Λ G : ℝ)
    (c : SpeedOfLight) : ℝ
```

**`Cosmology.CosmicFluid.addCosmologicalConstant`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L170).

> The cosmic fluid `F` with the cosmological constant folded in as a fluid.

```lean
noncomputable def CosmicFluid.addCosmologicalConstant (F : CosmicFluid) (Λ G : ℝ)
    (c : SpeedOfLight) : CosmicFluid
```

**`Cosmology.FLRW.a_ne_zero`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L183).

```lean
lemma a_ne_zero {t : Time} (ht : t ∈ U.I) : U.a t ≠ 0
```

**`Cosmology.FLRW.differentiableAt_a`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L185).

```lean
lemma differentiableAt_a {t : Time} (ht : t ∈ U.I) : DifferentiableAt ℝ U.a t
```

**`Cosmology.FLRW.differentiableAt_deriv_a`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L188).

```lean
lemma differentiableAt_deriv_a {t : Time} (ht : t ∈ U.I) : DifferentiableAt ℝ (∂ₜ U.a) t
```

## The interval and the tangent-line bound for a decelerating model

> These statements hold for any FLRW model; they do not use the Friedmann equations.

**`Cosmology.FLRW.mk_mem_I_of_mem_Icc`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L206).

> The times between two times of the interval `U.I` of an FLRW model are in `U.I`.

```lean
lemma mk_mem_I_of_mem_Icc (U : FLRW) {σ τ x : ℝ} (hσ : (⟨σ⟩ : Time) ∈ U.I)
    (hτ : (⟨τ⟩ : Time) ∈ U.I) (hx : x ∈ Set.Icc σ τ) : (⟨x⟩ : Time) ∈ U.I
```

**`Cosmology.FLRW.continuousOn_deriv_scaleFactor_mk`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L212).

> Along the time coordinate, the derivative of the scale factor is continuous on any segment
> of the interval `U.I`.

```lean
lemma continuousOn_deriv_scaleFactor_mk (U : FLRW) {σ τ : ℝ} (hσ : (⟨σ⟩ : Time) ∈ U.I)
    (hτ : (⟨τ⟩ : Time) ∈ U.I) : ContinuousOn (fun x : ℝ => ∂ₜ U.a ⟨x⟩) (Set.Icc σ τ)
```

**`Cosmology.FLRW.scaleFactor_le_tangent`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L221).

> If the scale factor decelerates on the interval (`∂ₜ ∂ₜ a ≤ 0` on `U.I`), it lies below its
> tangent line at any time `t₀` of `U.I`: `a t ≤ a t₀ + ∂ₜ a t₀ (t - t₀)` for `t ∈ U.I`. The
> derivative is antitone on the segment between `t` and `t₀`, which lies in `U.I`, and the mean
> value inequality concludes.

```lean
lemma scaleFactor_le_tangent (U : FLRW) (hdec : ∀ s ∈ U.I, ∂ₜ (∂ₜ U.a) s ≤ 0) {t₀ t : Time}
    (ht₀ : t₀ ∈ U.I) (ht : t ∈ U.I) : U.a t ≤ U.a t₀ + ∂ₜ U.a t₀ * (t.val - t₀.val)
```

**`Cosmology.FLRW.lt_of_mem_I_of_decelerating`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L268).

> The Big-Bang bound for an FLRW model: if the scale factor decelerates on `U.I` and the model
> expands at `t₀ ∈ U.I`, every time of `U.I` is later than `t₀ - a t₀ / ∂ₜ a t₀`. Earlier, the
> tangent line, and hence the scale factor, would be non-positive.

```lean
lemma lt_of_mem_I_of_decelerating (U : FLRW) (hdec : ∀ s ∈ U.I, ∂ₜ (∂ₜ U.a) s ≤ 0)
    {t₀ : Time} (ht₀ : t₀ ∈ U.I) (h0 : 0 < ∂ₜ U.a t₀) {t : Time} (ht : t ∈ U.I) :
    t₀.val - U.a t₀ / ∂ₜ U.a t₀ < t.val
```

**`Cosmology.FLRW.bddBelow_I_of_decelerating`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L283).

> Hence the interval of an FLRW model that decelerates on `U.I` and expands at one of its
> times is bounded below.

```lean
lemma bddBelow_I_of_decelerating (U : FLRW) (hdec : ∀ s ∈ U.I, ∂ₜ (∂ₜ U.a) s ≤ 0) {t₀ : Time}
    (ht₀ : t₀ ∈ U.I) (h0 : 0 < ∂ₜ U.a t₀) : BddBelow U.I
```

**`Cosmology.FLRW.FriedmannEquation.FirstOrderFriedmann`**, a def, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L310).

> The first-order Friedmann equation.
>
> - `a : Time → ℝ` is the FLRW scale factor as a function of cosmic time `t`.
> - `ρ : Time → ℝ` is the total energy density as a function of cosmic time `t`.
> - `k : ℝ` is the spatial curvature parameter.
> - `Λ : ℝ` is the cosmological constant.
> - `G : ℝ` is Newton's constant.
> - `c : SpeedOfLight` is the speed of light; take `c = 1` for units in which it is one.
>
> Note: We will leave `c` explicit for generality and accounting purposes.
>
> At time `t` the equation reads:
> `(a'(t) / a(t))^2 = (8πG/3) ρ(t) − k c^2 / a(t)^2 + Λ c^2 / 3`.

```lean
def FirstOrderFriedmann (a ρ : Time → ℝ) (k Λ G : ℝ) (c : SpeedOfLight) (t : Time) : Prop
```

**`Cosmology.FLRW.FriedmannEquation.SecondOrderFriedmann`**, a def, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L333).

> The second-order Friedmann equation.
> Note: Other sources may call this the Raychaudhuri equation.
> We choose not to use that terminology to avoid the Raychaudhuri equation
> related to describing congruences of geodesics in general relativity.
> - `a : Time → ℝ` is the FLRW scale factor as a function of cosmic time `t`.
> - `ρ : Time → ℝ` is the total energy density as a function of cosmic time `t`.
> - `p : Time → ℝ` is the pressure. It is related to `ρ` via `p = w * ρ `
> - `w` is the equation of state. We will introduce this later.
> - `Λ : ℝ` is the cosmological constant.
> - `G : ℝ` is Newton's constant.
> - `c : SpeedOfLight` is the speed of light; take `c = 1` for units in which it is one.
>
> Note: We will leave `c` explicit for generality and accounting purposes.
>
> At time `t` the equation reads:
> `(a''(t) / a (t)) = - (4πG/3) * (ρ(t) + 3 * p(t) / c^2) + Λ * c^2 / 3`.

```lean
def SecondOrderFriedmann (a ρ p : Time → ℝ) (Λ G : ℝ) (c : SpeedOfLight) (t : Time) : Prop
```

**`Cosmology.FLRW.FriedmannEquation.hubbleConstant`**, a def, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L344).

> The hubble constant defined in terms of the scale factor
> as `(dₜ a) / a`.
>
> The notation `H` is used for the `hubbleConstant`.
>
> Semiformal implementation note: Implement also scoped notation.

```lean
noncomputable def hubbleConstant (a : Time → ℝ) (t : Time) : ℝ
```

**`Cosmology.FLRW.FriedmannEquation.hubbleConstant_ne_zero`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L348).

> The Hubble constant is nonzero whenever `∂ₜ a t` and `a t` are both nonzero.

```lean
lemma hubbleConstant_ne_zero {a : Time → ℝ} {t : Time}
    (hd_az : ∂ₜ a t ≠ 0) (haz : a t ≠ 0) :
    hubbleConstant a t ≠ 0
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter`**, a def, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L368).

> The deceleration parameter defined in terms of the scale factor
> as `- (dₜdₜ a) a / (dₜ a)^2`.
>
> The notation `q` is used for the `decelerationParameter`.
>
> Semiformal implementation note: Implement also scoped notation.

```lean
noncomputable def decelerationParameter (a : Time → ℝ) (t : Time) : ℝ
```

**`Cosmology.FLRW.FriedmannEquation.deriv_hubbleConstant`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L373).

> Quotient-rule expression for the time derivative of the Hubble constant:
> `dₜ H = (a'' a - (a')^2) / a^2`.

```lean
lemma deriv_hubbleConstant {a : Time → ℝ} {t : Time}
    (ha : DifferentiableAt ℝ a t) (hd_a : DifferentiableAt ℝ (∂ₜ a) t)
    (haz : a t ≠ 0) :
    ∂ₜ (hubbleConstant a) t =
      (∂ₜ (∂ₜ a) t * a t - (∂ₜ a t) ^ 2) / (a t) ^ 2
```

**`Cosmology.FLRW.FriedmannEquation.decelerationParameter_eq_one_plus_hubbleConstant`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L383).

> The deceleration parameter is equal to `- (1 + (dₜ H)/H^2)`.

```lean
lemma decelerationParameter_eq_one_plus_hubbleConstant
    {a : Time → ℝ} {t : Time}
    (ha : DifferentiableAt ℝ a t) (hd_a : DifferentiableAt ℝ (∂ₜ a) t)
    (haz : a t ≠ 0) (hd_az : ∂ₜ a t ≠ 0) :
    decelerationParameter a t =
      -(1 + ∂ₜ (hubbleConstant a) t / (hubbleConstant a t) ^ 2)
```

**`Cosmology.FLRW.FriedmannEquation.deriv_hubbleConstant_eq_neg_sq_mul`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L394).

> The time derivative of the Hubble constant equals `-H² (1 + q)`.

```lean
lemma deriv_hubbleConstant_eq_neg_sq_mul
    {a : Time → ℝ} {t : Time}
    (ha : DifferentiableAt ℝ a t) (hd_a : DifferentiableAt ℝ (∂ₜ a) t)
    (haz : a t ≠ 0) (hd_az : ∂ₜ a t ≠ 0) :
    ∂ₜ (hubbleConstant a) t =
      -(hubbleConstant a t) ^ 2 * (1 + decelerationParameter a t)
```

**`Cosmology.FLRW.FriedmannEquation.deriv_hubbleConstant_neg_iff`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L406).

> Pointwise: `∂ₜ H t < 0` iff `-1 < q t` (assuming `a` is twice differentiable at `t`
> and both `a t` and `∂ₜ a t` are nonzero).

```lean
lemma deriv_hubbleConstant_neg_iff
    {a : Time → ℝ} {t : Time}
    (ha : DifferentiableAt ℝ a t) (hd_a : DifferentiableAt ℝ (∂ₜ a) t)
    (haz : a t ≠ 0) (hd_az : ∂ₜ a t ≠ 0) :
    ∂ₜ (hubbleConstant a) t < 0 ↔ -1 < decelerationParameter a t
```

**`Cosmology.FLRW.FriedmannEquation.exists_deriv_hubbleConstant_neg_iff`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L419).

> There exists a time at which `∂ₜ H < 0` iff there exists a time with `q > -1`.
>
> (The corresponding informal statement was written with `q < -1`. Since
> `dₜ H = -H² (1 + q)` and `H ≠ 0`, one has `dₜ H < 0 ↔ q > -1`, so the formal
> statement uses the corrected inequality `-1 < q`.)

```lean
lemma exists_deriv_hubbleConstant_neg_iff
    {a : Time → ℝ}
    (ha : ∀ t, DifferentiableAt ℝ a t) (hd_a : ∀ t, DifferentiableAt ℝ (∂ₜ a) t)
    (haz : ∀ t, a t ≠ 0) (hd_az : ∀ t, ∂ₜ a t ≠ 0) :
    (∃ t, ∂ₜ (hubbleConstant a) t < 0) ↔ (∃ t, -1 < decelerationParameter a t)
```

**`Cosmology.FLRW.FriedmannSolution`**, a structure, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean#L438).

> The proposition that the FLRW model `U` filled with the cosmic fluid `F` solves the
> Friedmann equations: the first- and second-order Friedmann equations, with cosmological
> constant `Λ`, Newton's constant `G` and speed of light `c`, hold at every time of the interval
> `U.I`, the curvature parameter being the one of the spatial geometry. The continuity equation
> of the fluid is not part of it: it follows from the two Friedmann equations
> (`FLRW.FriedmannSolution.continuityEquation` in `Physlib.Cosmology.FLRW.MatterContent`).

```lean
structure FriedmannSolution (U : FLRW) (F : CosmicFluid) (Λ G : ℝ) (c : SpeedOfLight) : Prop where
  /-- The first-order Friedmann equation holds on `U.I`. -/
  firstOrder : ∀ t ∈ U.I, FirstOrderFriedmann U.a F.ρ U.geometry.curvature Λ G c t
  /-- The second-order Friedmann equation holds on `U.I`. -/
  secondOrder : ∀ t ∈ U.I, SecondOrderFriedmann U.a F.ρ F.p Λ G c t
```

## Depends on

- [The Speed of Light](../../relativity/speedoflight.md)
- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/Cosmology/FLRW/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Cosmology/FLRW/Basic.lean)
