---
declaration: module
origin: cited
lean: ClassicalMechanics.SimplePendulum.periodFormula, ClassicalMechanics.SimplePendulum.periodFormula_neg, ClassicalMechanics.SimplePendulum.periodFormula_zero, ClassicalMechanics.SimplePendulum.continuousOn_periodFormula, ClassicalMechanics.SimplePendulum.continuousAt_periodFormula_zero, ClassicalMechanics.SimplePendulum.periodFormula_tendsto_smallAnglePeriod, ClassicalMechanics.SimplePendulum.periodFormula_mono, ClassicalMechanics.SimplePendulum.periodFormula_strictMono
statement: formalized
proof: formalized
---

# The period formula of the simple gravity pendulum

The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.PeriodFormula`, [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean): 14 declarations, 14 with a docstring.

## i. Overview

> Beyond the small-angle approximation the period of the simple gravity pendulum depends on the
> amplitude of the swing. Released from rest at the angle `θ₀`, with `0 < θ₀ < π`, the pendulum
> librates about the bottom of its swing, and the classical calculation (Landau & Lifshitz, §11,
> Problem 1) integrates the energy first integral by quadrature: the quarter period is the time
> of descent from `θ₀` to the bottom, the substitution `sin (θ/2) = sin (θ₀/2) sin φ` turns the
> resulting integral into a complete elliptic integral of the first kind, and the period is
>
> `T = 4 √(ℓ/g) K(sin ½θ₀)`,
>
> with `K` Legendre's complete elliptic integral of the first kind in the modulus convention. In
> the parameter convention of `Real.completeEllipticK`, where the parameter is the square
> `m = k²` of the modulus, the same formula reads `4 √(ℓ/g) completeEllipticK (sin² (θ₀/2))`.
>
> This module records that formula as `SimplePendulum.periodFormula` and proves what follows
> for it from the theory of `completeEllipticK` alone: it is even in the amplitude, at zero
> amplitude it is the small-angle period `2π √(ℓ/g)`, it is continuous on `(-π, π)` and tends to
> the small-angle period as the amplitude tends to zero, it is never below the small-angle
> period, it is strictly increasing in the amplitude on `[0, π)`, and it is at most
> `2π √(ℓ/g) / cos (θ₀/2)`. The formula is therefore not constant in the amplitude — the
> classical statement that the pendulum is not isochronous, once the identification below is
> proved — and the upper bound quantifies how it grows as the amplitude approaches the inverted
> position.
>
> …

## ii. Key results

> - `SimplePendulum.periodFormula` is the classical formula `4 √(ℓ/g) K(sin² (θ₀/2))` for the
>   period of libration with amplitude `θ₀`; for `|θ₀| < π` its parameter `sin² (θ₀/2)` lies
>   below `1` (`Real.sin_half_sq_lt_one`), so it is evaluated on the domain of
>   `completeEllipticK`.
> - `SimplePendulum.periodFormula_neg`: the formula is even in the amplitude.
> - `SimplePendulum.periodFormula_zero`: at zero amplitude the formula is the small-angle
>   period, `periodFormula 0 = smallAnglePeriod`.
> - `SimplePendulum.continuousOn_periodFormula` and
>   `SimplePendulum.continuousAt_periodFormula_zero`: the formula is continuous on `(-π, π)`,
>   in particular at `0`.
> - `SimplePendulum.periodFormula_tendsto_smallAnglePeriod`: the formula tends to the
>   small-angle period as the amplitude tends to zero.
> - `SimplePendulum.periodFormula_mono` and `SimplePendulum.periodFormula_strictMono`, with the
>   bundled `SimplePendulum.monotoneOn_periodFormula` and
>   `SimplePendulum.strictMonoOn_periodFormula`: on `[0, π)` the formula is increasing, and
>   strictly increasing, in the amplitude.
> - `SimplePendulum.smallAnglePeriod_le_periodFormula` and `SimplePendulum.periodFormula_pos`:
>   the formula is at least the small-angle period, in particular positive, whenever
>   `sin² (θ₀/2) < 1`.
> - `SimplePendulum.periodFormula_le` and `SimplePendulum.periodFormula_le'`: for `|θ₀| < π` the
>   formula is at most `2π √(ℓ/g) / cos (θ₀/2) = smallAnglePeriod / cos (θ₀/2)`.

## iv. References

> * Landau & Lifshitz, Mechanics, 3rd ed., §11, Problem 1: `T = 4 √(l/g) K(sin ½φ₀)`, in the modulus
>   convention `K(k) = ∫ φ in 0..π/2, (1 - k² sin² φ)^(-1/2)`. [ref: landau\_mechanics]
> * M. Abramowitz, I. A. Stegun, Handbook of Mathematical Functions, 17.3.1 (the parameter convention
>   `K(m)`, `m = k²`, used by `Real.completeEllipticK`). [ref: abramowitz\_stegun\_1964]
> * The module `Physlib.Mathematics.SpecialFunctions.EllipticIntegral`, for `completeEllipticK` and
>   its theory on the domain `m < 1`.
> * The module `Physlib.ClassicalMechanics.Pendulum.SimplePendulum.SmallAngle`, for the small-angle
>   period `smallAnglePeriod = 2π √(ℓ/g)`.

## A. The period formula, its continuity and its small-angle limit

> The classical formula for the period of libration as a function of the amplitude, its evenness
> and its domain, and its behaviour at small amplitudes: it is continuous on the libration range
> `(-π, π)`, at zero amplitude it is exactly the small-angle period, and it tends to the
> small-angle period as the amplitude tends to zero. These are facts about the elliptic integral
> on its domain and at the parameter `0`, where `K 0 = π/2`.

### A.1. The formula, its domain and its evenness

> The formula `4 √(ℓ/g) K(sin² (θ₀/2))` is defined for every real `θ₀`, and is even in `θ₀`; for
> libration amplitudes `|θ₀| < π` the parameter `sin² (θ₀/2)` is below `1`
> (`Real.sin_half_sq_lt_one`), so the elliptic integral is evaluated on its domain. At `θ₀ = ±π`
> the parameter is `1`, where Legendre's `K` diverges — the pendulum released from rest at the
> inverted position never returns — while the Lean value of `completeEllipticK` at `m = 1` is a
> junk value (see the module docstring of `Physlib.Mathematics.SpecialFunctions.EllipticIntegral`),
> so nothing is claimed there.

**`ClassicalMechanics.SimplePendulum.periodFormula`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L137).

```lean
noncomputable def periodFormula (θ₀ : ℝ) : ℝ
```

**`ClassicalMechanics.SimplePendulum.periodFormula_neg`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L165).

> The period formula is even in the amplitude, `periodFormula (-θ₀) = periodFormula θ₀`: its
> parameter `sin² (θ₀/2)` is even in `θ₀`.

```lean
lemma periodFormula_neg (θ₀ : ℝ) : S.periodFormula (-θ₀) = S.periodFormula θ₀
```

### A.2. Continuity and the small-angle limit

> At zero amplitude the parameter of the elliptic integral is `0`, where `K 0 = π/2`, and the
> formula collapses to `4 √(ℓ/g) · π/2 = 2π √(ℓ/g)`: the small-angle period. Since `K` is
> continuous on its domain and the parameter `sin² (θ₀/2)` is continuous in the amplitude and
> stays below `1` for `|θ₀| < π`, the formula is continuous on `(-π, π)`; in particular it tends
> to the small-angle period as the amplitude tends to zero — the sense in which the small-angle
> theory of `SimplePendulum.SmallAngle` is the limit of the classical formula.

**`ClassicalMechanics.SimplePendulum.periodFormula_zero`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L184).

> At zero amplitude the period formula is the small-angle period: `K 0 = π/2` turns
> `4 √(ℓ/g) K 0` into `2π √(ℓ/g)`.

```lean
lemma periodFormula_zero : S.periodFormula 0 = S.smallAnglePeriod
```

**`ClassicalMechanics.SimplePendulum.continuousOn_periodFormula`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L192).

> The period formula is continuous on the libration range `(-π, π)`: `completeEllipticK` is
> continuous at every parameter `m < 1`, and the parameter `sin² (θ₀/2)` is continuous in `θ₀`
> and below `1` for `|θ₀| < π`.

```lean
lemma continuousOn_periodFormula : ContinuousOn S.periodFormula (Set.Ioo (-Real.pi) Real.pi)
```

**`ClassicalMechanics.SimplePendulum.continuousAt_periodFormula_zero`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L200).

> The period formula is continuous at zero amplitude, an interior point of `(-π, π)`.

```lean
lemma continuousAt_periodFormula_zero : ContinuousAt S.periodFormula 0
```

**`ClassicalMechanics.SimplePendulum.periodFormula_tendsto_smallAnglePeriod`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L206).

> The period formula tends to the small-angle period as the amplitude tends to zero: it is
> continuous at `0`, where its value is the small-angle period.

```lean
lemma periodFormula_tendsto_smallAnglePeriod :
    Filter.Tendsto S.periodFormula (nhds 0) (nhds S.smallAnglePeriod)
```

## B. Monotonicity and bounds in the amplitude

> The dependence of the period formula on the amplitude is inherited from the dependence of
> `completeEllipticK` on its parameter: on `[0, π)` the parameter `sin² (θ₀/2)` is strictly
> increasing in `θ₀` and stays below `1`, and `K` is strictly increasing on `(-∞, 1)`, so the
> formula is strictly increasing in the amplitude. The bounds `π/2 ≤ K m ≤ (π/2) (1 - m)^(-1/2)`
> on `[0, 1)` sandwich the formula between the small-angle period and
> `2π √(ℓ/g) / cos (θ₀/2)`.

### B.1. Monotonicity in the amplitude

> For `0 ≤ θ₁ ≤ θ₂ < π` the half-angles lie in `[0, π/2)`, where the sine is nonnegative and
> increasing, so `sin² (θ₁/2) ≤ sin² (θ₂/2) < 1`, and the monotonicity of `K` on its domain does
> the rest. The strict version uses the strict monotonicity of the sine on the same interval and
> of `K`. Both are restated as bundled `MonotoneOn` and `StrictMonoOn` facts on `[0, π)`.

**`ClassicalMechanics.SimplePendulum.periodFormula_mono`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L239).

```lean
lemma periodFormula_mono {θ₁ θ₂ : ℝ} (h0 : 0 ≤ θ₁) (h12 : θ₁ ≤ θ₂) (hπ : θ₂ < Real.pi) :
    S.periodFormula θ₁ ≤ S.periodFormula θ₂
```

**`ClassicalMechanics.SimplePendulum.periodFormula_strictMono`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L253).

> The period formula is strictly increasing in the amplitude on `[0, π)`: for
> `0 ≤ θ₁ < θ₂ < π`, `periodFormula θ₁ < periodFormula θ₂`.

```lean
lemma periodFormula_strictMono {θ₁ θ₂ : ℝ} (h0 : 0 ≤ θ₁) (h12 : θ₁ < θ₂) (hπ : θ₂ < Real.pi) :
    S.periodFormula θ₁ < S.periodFormula θ₂
```

**`ClassicalMechanics.SimplePendulum.monotoneOn_periodFormula`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L269).

> The period formula is monotone on `[0, π)`, as a bundled `MonotoneOn` statement.

```lean
lemma monotoneOn_periodFormula : MonotoneOn S.periodFormula (Set.Ico 0 Real.pi)
```

**`ClassicalMechanics.SimplePendulum.strictMonoOn_periodFormula`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L274).

> The period formula is strictly increasing on `[0, π)`, as a bundled `StrictMonoOn`
> statement.

```lean
lemma strictMonoOn_periodFormula : StrictMonoOn S.periodFormula (Set.Ico 0 Real.pi)
```

### B.2. Bounds

> The lower bound `π/2 ≤ K m` on `[0, 1)` says that the period formula is never below the
> small-angle period: the formula is least at zero amplitude, and in particular positive. The
> upper bound `K m ≤ (π/2) (1 - m)^(-1/2)`, with `1 - sin² (θ₀/2) = cos² (θ₀/2)`, bounds the
> formula by `2π √(ℓ/g) / cos (θ₀/2)` for `|θ₀| < π`: the formula is at most the small-angle
> period divided by the cosine of the half-amplitude, a quantity that grows without bound as the
> amplitude approaches the inverted position.

**`ClassicalMechanics.SimplePendulum.smallAnglePeriod_le_periodFormula`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L292).

> The period formula is at least the small-angle period: for `sin² (θ₀/2) < 1`,
> `smallAnglePeriod ≤ periodFormula θ₀`, since `π/2 ≤ K m` on `[0, 1)`.

```lean
lemma smallAnglePeriod_le_periodFormula {θ₀ : ℝ} (h : Real.sin (θ₀ / 2) ^ 2 < 1) :
    S.smallAnglePeriod ≤ S.periodFormula θ₀
```

**`ClassicalMechanics.SimplePendulum.periodFormula_pos`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L303).

> The period formula is positive for `sin² (θ₀/2) < 1`: it is at least the small-angle
> period, which is positive.

```lean
lemma periodFormula_pos {θ₀ : ℝ} (h : Real.sin (θ₀ / 2) ^ 2 < 1) : 0 < S.periodFormula θ₀
```

**`ClassicalMechanics.SimplePendulum.periodFormula_le`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L309).

> The period formula is at most `2π √(ℓ/g) / cos (θ₀/2)` for `|θ₀| < π`: the bound
> `K m ≤ (π/2) (1 - m)^(-1/2)` at `m = sin² (θ₀/2)`, where `1 - sin² (θ₀/2) = cos² (θ₀/2)`
> and `cos (θ₀/2) > 0`.

```lean
lemma periodFormula_le {θ₀ : ℝ} (h : |θ₀| < Real.pi) :
    S.periodFormula θ₀ ≤ 2 * Real.pi * √(S.ℓ / S.g) / Real.cos (θ₀ / 2)
```

**`ClassicalMechanics.SimplePendulum.periodFormula_le'`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean#L331).

> The period formula is at most the small-angle period divided by `cos (θ₀/2)`, for
> `|θ₀| < π`: `periodFormula_le` with `2π √(ℓ/g) = smallAnglePeriod`. Together with
> `smallAnglePeriod_le_periodFormula` this sandwiches the formula,
> `smallAnglePeriod ≤ periodFormula θ₀ ≤ smallAnglePeriod / cos (θ₀/2)`; the lower bound holds
> under the more general hypothesis `sin² (θ₀/2) < 1`, which `|θ₀| < π` implies
> (`Real.sin_half_sq_lt_one`).

```lean
lemma periodFormula_le' {θ₀ : ℝ} (h : |θ₀| < Real.pi) :
    S.periodFormula θ₀ ≤ S.smallAnglePeriod / Real.cos (θ₀ / 2)
```

## Depends on

- [Small-angle motion of the simple gravity pendulum](smallangle.md)
- [The complete elliptic integral of the first kind](../../../mathematics/specialfunctions/ellipticintegral.md)

## Proof depends on

- [Strict bounds on the square of the sine](../../../mathematics/formathlib/trigonometry-sinsq.md)

## Sources

- [Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/Pendulum/SimplePendulum/PeriodFormula.lean)
