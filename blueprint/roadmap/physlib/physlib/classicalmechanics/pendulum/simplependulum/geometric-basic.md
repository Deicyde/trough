---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.ConfigurationSpace, ClassicalMechanics.SimplePendulum.ConfigurationSpace.ext, ClassicalMechanics.SimplePendulum.ConfigurationSpace.angleEquiv, ClassicalMechanics.SimplePendulum.ConfigurationSpace.instTopologicalSpace, ClassicalMechanics.SimplePendulum.ConfigurationSpace.angleHomeomorph, ClassicalMechanics.SimplePendulum.ConfigurationSpace.toCircle, ClassicalMechanics.SimplePendulum.ConfigurationSpace.circleHomeomorph, ClassicalMechanics.SimplePendulum.ConfigurationSpace.circleHomeomorph_apply
statement: formalized
proof: formalized
---

# Configuration space of the simple pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.Geometric.Basic`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean): 47 declarations, 47 with a docstring.

## i. Overview

> A simple pendulum is a bob fixed to one end of a rigid massless rod of length `ℓ`, the other end
> of which is pinned at a pivot, swinging in a vertical plane under gravity. Its position is fixed by
> the angle of the rod from the downward vertical, and two angles that differ by a full turn describe
> the same position. The configuration space is therefore a circle.
>
> We record a configuration by its angle modulo `2π`, i.e. by an element of `Real.Angle`, as the
> sliding pendulum does (`Physlib.ClassicalMechanics.Pendulum.SlidingPendulum`). The circle carries
> the structure of a compact analytic one-dimensional manifold; we obtain it by identifying the
> configuration space with Mathlib's unit circle `Circle` and pulling back its charts. The smooth
> identification of the configuration space with `Circle` (the analogue of the harmonic oscillator's
> `valDiffeomorph`) is deferred to a later module. The real-valued angle that is used to
> write down the dynamics is a lift of the configuration along the covering map
> `ℝ → ConfigurationSpace`; it is not a chart, and two lifts differing by `2π n` describe the same
> configuration. Finally the position of the bob in the plane is recorded by `toSpace ℓ`, which sends
> the configuration at angle `θ` to `(ℓ sin θ, -ℓ cos θ)`: the pivot is the origin and the second axis
> points upwards.

## ii. Key results

> - `ConfigurationSpace` : the configuration space of the planar simple pendulum.
> - `ConfigurationSpace.circleHomeomorph` : its identification with the unit circle, with inverse
>   `ConfigurationSpace.ofCircle` (`toCircle_ofCircle`, `ofCircle_toCircle`).
> - `ConfigurationSpace.instChartedSpace`, `ConfigurationSpace.instIsManifold` : the analytic
>   manifold structure, pulled back from `Circle` (`chartAt_source`, `chartAt_target`).
> - `ConfigurationSpace.ofAngle` : the angular lift `ℝ → ConfigurationSpace`, periodic with period
>   `2π`, continuous, surjective, analytic, and a covering map (`isCoveringMap_ofAngle`).
> - `ConfigurationSpace.toSpace` : the position of the bob in `Space 2`, with
>   `toSpace_ofAngle` and the rod-length constraint `toSpace_norm`; for `ℓ ≠ 0` it is a closed
>   embedding (`toSpace_isClosedEmbedding`).

## iv. References

> * Landau & Lifshitz, Mechanics, 3rd ed., §5, Problems 1–3 (pendulum configurations).
>   [ref: landau\_mechanics]
> * Mathlib, `Mathlib.Geometry.Manifold.Instances.Sphere` (the manifold structure on `Circle`).

## A. The configuration space type

> A configuration is the angle of the rod from the downward vertical, taken modulo a full turn.

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace`**, a structure, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L81).

> The configuration space of the planar simple pendulum: the angle of the rod from the downward
> vertical, modulo `2π`.

```lean
structure ConfigurationSpace where
  /-- The angle of the rod from the downward vertical, modulo `2π`. -/
  angle : Real.Angle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ext`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L89).

> Two configurations are equal precisely when their angles are equal.

```lean
lemma ext {p q : ConfigurationSpace} (h : p.angle = q.angle) : p = q
```

## B. Topology and identification with the unit circle

> The topology is that of `Real.Angle`; composing with Mathlib's identification of `Real.Angle`
> (the additive circle of period `2π`) with the unit circle `Circle ⊆ ℂ` gives a homeomorphism
> `ConfigurationSpace ≃ₜ Circle`, through which the circle's compactness and Hausdorff property
> transfer.

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.angleEquiv`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L104).

> The identification of the configuration space with `Real.Angle`.

```lean
def angleEquiv : ConfigurationSpace ≃ Real.Angle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.instTopologicalSpace`**, an instance, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L111).

> The topology of the configuration space, induced from `Real.Angle`.

```lean
instance instTopologicalSpace : TopologicalSpace ConfigurationSpace
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.angleHomeomorph`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L115).

> The identification with `Real.Angle` as a homeomorphism.

```lean
def angleHomeomorph : ConfigurationSpace ≃ₜ Real.Angle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toCircle`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L121).

> The point of the unit circle `e^{iθ}` corresponding to a configuration at angle `θ`.

```lean
def toCircle (q : ConfigurationSpace) : Circle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.circleHomeomorph`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L124).

> The identification of the configuration space with the unit circle.

```lean
def circleHomeomorph : ConfigurationSpace ≃ₜ Circle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.circleHomeomorph_apply`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L132).

> The identification with the unit circle is given by `ConfigurationSpace.toCircle`.

```lean
lemma circleHomeomorph_apply (q : ConfigurationSpace) : circleHomeomorph q = q.toCircle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofCircle`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L135).

> The configuration corresponding to a point of the unit circle.

```lean
def ofCircle : Circle → ConfigurationSpace
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toCircle_ofCircle`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L140).

> The point of the unit circle of the configuration attached to a point of the unit circle is
> that point.

```lean
lemma toCircle_ofCircle (z : Circle) : (ofCircle z).toCircle = z
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofCircle_toCircle`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L146).

> The configuration attached to the point of the unit circle of a configuration is that
> configuration.

```lean
lemma ofCircle_toCircle (q : ConfigurationSpace) : ofCircle q.toCircle = q
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.instT2Space`**, an instance, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L150).

> The configuration space is Hausdorff, being homeomorphic to the unit circle.

```lean
instance instT2Space : T2Space ConfigurationSpace
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.instCompactSpace`**, an instance, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L153).

> The configuration space is compact, being homeomorphic to the unit circle.

```lean
instance instCompactSpace : CompactSpace ConfigurationSpace
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.instSecondCountableTopology`**, an instance, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L156).

> The configuration space is second countable, being homeomorphic to the unit circle.

```lean
instance instSecondCountableTopology : SecondCountableTopology ConfigurationSpace
```

## C. Manifold structure

> The unit circle is an analytic one-dimensional manifold modelled on `EuclideanSpace ℝ (Fin 1)`
> (Mathlib, via stereographic projection). We pull its atlas back along `circleHomeomorph`: a chart
> of the configuration space is the identification with the circle followed by a chart of the circle.
> Since the identification cancels in every change of charts, the changes of charts are exactly those
> of the circle, hence analytic.

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.instChartedSpace`**, an instance, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L173).

> The charts of the configuration space: the identification with the unit circle followed by a
> chart of the circle.

```lean
instance instChartedSpace : ChartedSpace (EuclideanSpace ℝ (Fin 1)) ConfigurationSpace
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.chartAt_eq`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L183).

> The chart at a configuration is the identification with the unit circle followed by the chart
> of the circle at the corresponding point.

```lean
lemma chartAt_eq (q : ConfigurationSpace) :
    chartAt (EuclideanSpace ℝ (Fin 1)) q =
      circleHomeomorph.toOpenPartialHomeomorph.trans
        (chartAt (EuclideanSpace ℝ (Fin 1)) q.toCircle)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.chartAt_source`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L190).

> The domain of the chart at a configuration is the preimage under the identification with the
> unit circle of the domain of the chart of the circle at the corresponding point.

```lean
lemma chartAt_source (q : ConfigurationSpace) :
    (chartAt (EuclideanSpace ℝ (Fin 1)) q).source =
      circleHomeomorph ⁻¹' (chartAt (EuclideanSpace ℝ (Fin 1)) q.toCircle).source
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.chartAt_target`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L198).

> The codomain of the chart at a configuration is the codomain of the chart of the circle at the
> corresponding point.

```lean
lemma chartAt_target (q : ConfigurationSpace) :
    (chartAt (EuclideanSpace ℝ (Fin 1)) q).target =
      (chartAt (EuclideanSpace ℝ (Fin 1)) q.toCircle).target
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.instIsManifold`**, an instance, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L206).

> The configuration space is an analytic manifold: every change of charts is a change of charts
> of the unit circle.

```lean
instance instIsManifold : IsManifold (𝓡 1) ω ConfigurationSpace
```

## D. The angular lift

> `ofAngle θ` is the configuration at angle `θ` from the downward vertical. It is the quotient map
> `ℝ → ℝ / 2πℤ`, a covering map of the circle: it is continuous, surjective and `2π`-periodic, and
> two angles give the same configuration exactly when they differ by a whole number of turns. The
> dynamics of the pendulum are written for a real-valued lift of the angle; this section is what
> makes different lifts describe the same configuration. In the charts pulled back from the circle
> is `Circle.exp`, so it is analytic.

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofAngle`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L237).

> The configuration at angle `θ` (measured from the downward vertical).

```lean
def ofAngle (θ : ℝ) : ConfigurationSpace
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofAngle_angle`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L241).

> The angle of the configuration at angle `θ` is `θ` modulo `2π`.

```lean
lemma ofAngle_angle (θ : ℝ) : (ofAngle θ).angle = θ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofAngle_add_two_pi`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L244).

> Adding a full turn to the angle leaves the configuration unchanged.

```lean
lemma ofAngle_add_two_pi (θ : ℝ) : ofAngle (θ + 2 * Real.pi) = ofAngle θ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofAngle_periodic`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L249).

> The angular lift is periodic with period `2π`.

```lean
lemma ofAngle_periodic : Function.Periodic ofAngle (2 * Real.pi)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofAngle_eq_iff`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L253).

> Two angles describe the same configuration exactly when they differ by a whole number of
> turns.

```lean
lemma ofAngle_eq_iff (θ₁ θ₂ : ℝ) :
    ofAngle θ₁ = ofAngle θ₂ ↔ ∃ n : ℤ, θ₂ = θ₁ + n * (2 * Real.pi)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofAngle_surjective`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L265).

> Every configuration is the configuration at some real angle: the lift is surjective.

```lean
lemma ofAngle_surjective : Function.Surjective ofAngle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.continuous_ofAngle`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L272).

> The angular lift is continuous.

```lean
lemma continuous_ofAngle : Continuous ofAngle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.isCoveringMap_ofAngle`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L276).

> The angular lift is a covering map.

```lean
lemma isCoveringMap_ofAngle : IsCoveringMap ofAngle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toCircle_ofAngle`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L284).

> The configuration at angle `θ` corresponds to the point `e^{iθ}` of the unit circle.

```lean
lemma toCircle_ofAngle (θ : ℝ) : (ofAngle θ).toCircle = Circle.exp θ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.ofCircle_circleExp`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L288).

> The configuration of a point `e^{iθ}` of the unit circle is `ofAngle θ`.

```lean
lemma ofCircle_circleExp (θ : ℝ) : ofCircle (Circle.exp θ) = ofAngle θ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.contMDiff_ofAngle`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L293).

> The angular lift is analytic: read in the charts pulled back from the circle it is
> `Circle.exp`.

```lean
lemma contMDiff_ofAngle : ContMDiff 𝓘(ℝ, ℝ) (𝓡 1) ω ofAngle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.cos`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L304).

> The cosine of the angle of a configuration.

```lean
def cos (q : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.sin`**, a def, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L307).

> The sine of the angle of a configuration.

```lean
def sin (q : ConfigurationSpace) : ℝ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.cos_angle`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L310).

> The cosine of a configuration is the cosine of its angle.

```lean
lemma cos_angle (q : ConfigurationSpace) : q.cos = Real.Angle.cos q.angle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.sin_angle`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L313).

> The sine of a configuration is the sine of its angle.

```lean
lemma sin_angle (q : ConfigurationSpace) : q.sin = Real.Angle.sin q.angle
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.cos_ofAngle`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L317).

> The cosine of the configuration at angle `θ` is `cos θ`.

```lean
lemma cos_ofAngle (θ : ℝ) : (ofAngle θ).cos = Real.cos θ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.sin_ofAngle`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L321).

> The sine of the configuration at angle `θ` is `sin θ`.

```lean
lemma sin_ofAngle (θ : ℝ) : (ofAngle θ).sin = Real.sin θ
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.cos_sq_add_sin_sq`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L324).

> The Pythagorean identity for the angle of a configuration.

```lean
lemma cos_sq_add_sin_sq (q : ConfigurationSpace) : q.cos ^ 2 + q.sin ^ 2 = 1
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.continuous_cos`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L329).

> The cosine of the angle depends continuously on the configuration.

```lean
lemma continuous_cos : Continuous (cos : ConfigurationSpace → ℝ)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.continuous_sin`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L334).

> The sine of the angle depends continuously on the configuration.

```lean
lemma continuous_sin : Continuous (sin : ConfigurationSpace → ℝ)
```

## E. Map to physical space

> The pivot is the origin of the plane `Space 2`, the first coordinate is horizontal and the second
> points upwards. A rod of length `ℓ` at angle `θ` from the downward vertical places the bob at
> `(ℓ sin θ, -ℓ cos θ)`; at `θ = 0` the bob hangs straight down at `(0, -ℓ)`. The bob lies on the
> circle of radius `|ℓ|` about the pivot — the rod-length constraint — and for `ℓ ≠ 0` the map is
> injective, so the configuration is determined by the position.

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace`**, a def, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L351).

> The position of the bob in the plane, for a rod of length `ℓ`. `ℓ` is not assumed positive; the
> bob is at distance `|ℓ|` from the pivot.

```lean
def toSpace (ℓ : ℝ) (q : ConfigurationSpace) : Space 2
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace_apply_zero`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L355).

> The horizontal coordinate of the bob, `ℓ * q.sin`.

```lean
lemma toSpace_apply_zero (ℓ : ℝ) (q : ConfigurationSpace) :
    toSpace ℓ q 0 = ℓ * q.sin
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace_apply_one`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L360).

> The vertical coordinate of the bob, `-(ℓ * q.cos)`.

```lean
lemma toSpace_apply_one (ℓ : ℝ) (q : ConfigurationSpace) :
    toSpace ℓ q 1 = -(ℓ * q.cos)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace_ofAngle`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L365).

> The position of the bob for the configuration at angle `θ`.

```lean
lemma toSpace_ofAngle (ℓ θ : ℝ) :
    toSpace ℓ (ofAngle θ) = ⟨![ℓ * Real.sin θ, -ℓ * Real.cos θ]⟩
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace_norm`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L371).

> The rod-length constraint: the bob is at distance `|ℓ|` from the pivot.

```lean
lemma toSpace_norm (ℓ : ℝ) (q : ConfigurationSpace) : ‖toSpace ℓ q‖ = |ℓ|
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.continuous_toSpace`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L379).

> The position of the bob depends continuously on the configuration.

```lean
lemma continuous_toSpace (ℓ : ℝ) : Continuous (toSpace ℓ)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace_injective`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L384).

> For a rod of nonzero length the configuration is determined by the position of the bob.

```lean
lemma toSpace_injective {ℓ : ℝ} (hℓ : ℓ ≠ 0) : Function.Injective (toSpace ℓ)
```

**`ClassicalMechanics.SimplePendulum.ConfigurationSpace.toSpace_isClosedEmbedding`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean#L398).

> For `ℓ ≠ 0` the position map is a closed embedding of the configuration circle.

```lean
lemma toSpace_isClosedEmbedding {ℓ : ℝ} (hℓ : ℓ ≠ 0) : Topology.IsClosedEmbedding (toSpace ℓ)
```

## Depends on

- [The structure of a module on Space](../../../spaceandtime/space/part-01/module.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/Geometric/Basic.lean)
