---
declaration: module
origin: cited
lean: QuantumMechanics.RectangularBarrier.probabilityCurrent, QuantumMechanics.RectangularBarrier.IsStationaryWave, QuantumMechanics.RectangularBarrier.probabilityCurrent_eq, QuantumMechanics.RectangularBarrier.planeWave, QuantumMechanics.RectangularBarrier.probabilityCurrent_two_plane_waves, QuantumMechanics.RectangularBarrier.incident_norm_sq_eq, QuantumMechanics.RectangularBarrier.reflection_add_transmission_eq_one
statement: formalized
proof: formalized
---

# Stationary probability current at a rectangular barrier

The module `PhyslibAlpha.QuantumMechanics.RectangularBarrier.ProbabilityCurrent`, [PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean): 7 declarations, 7 with a docstring; 6 private, not shown.

> Conservation of the one-dimensional current across both barrier interfaces.

## i. Overview

> A stationary wave is represented by a function of the real spatial coordinate.
> For a real potential, the Schrödinger equation makes the derivative of the
> probability current vanish within each region. Continuity of the wave and its
> first derivative gives the same current on both sides of each interface.
> For a wave incident from the left, the common exterior wave number lets us
> express this conservation as a balance of the squared amplitudes.

## ii. Key results

> - `RectangularBarrier.probabilityCurrent_eq` gives equality of the current at any
>   two positions for a classical stationary wave of the barrier.
> - `RectangularBarrier.reflection_add_transmission_eq_one` gives the normalized
>   flux balance for a stationary wave with the stated exterior plane-wave forms.

## iv. References

> * None.

## A. Probability current and stationary waves

**`QuantumMechanics.RectangularBarrier.probabilityCurrent`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L60).

> The probability current along the real spatial coordinate, with the
> particle mass of the rectangular barrier and the reduced Planck constant.

```lean
def probabilityCurrent (Q : RectangularBarrier) (ψ : ℝ → ℂ) (x : ℝ) : ℝ
```

**`QuantumMechanics.RectangularBarrier.IsStationaryWave`**, a structure, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L66).

> A globally continuously differentiable stationary wave of energy `E`.
> The second derivative obeys the Schrödinger equation on each open region
> delimited by the two edges of the barrier.

```lean
structure IsStationaryWave (Q : RectangularBarrier) (E : ℝ) (ψ : ℝ → ℂ) : Prop where
  contDiff : ContDiff ℝ 1 ψ
  equation : ∀ x : ℝ, x ≠ Q.lower → x ≠ Q.upper →
    HasDerivAt (deriv ψ)
      ((2 * Q.m * (Q.potentialFunction ⟨fun _ => x⟩ - E) / (ℏ : ℝ) ^ 2) • ψ x) x
```

## B. Conservation across the interfaces

**`QuantumMechanics.RectangularBarrier.probabilityCurrent_eq`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L99).

> For a stationary wave of a rectangular barrier, the probability current
> is independent of position, including at both interfaces.

```lean
lemma probabilityCurrent_eq {Q : RectangularBarrier} {E : ℝ} {ψ : ℝ → ℂ}
    (hψ : Q.IsStationaryWave E ψ) (x y : ℝ) :
    Q.probabilityCurrent ψ x = Q.probabilityCurrent ψ y
```

## C. Exterior plane waves and flux balance

**`QuantumMechanics.RectangularBarrier.planeWave`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L135).

> The plane wave with wave number `k` at position `x`.

```lean
def planeWave (k x : ℝ) : ℂ
```

**`QuantumMechanics.RectangularBarrier.probabilityCurrent_two_plane_waves`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L155).

> The current of two counterpropagating plane waves is the difference of their currents.

```lean
lemma probabilityCurrent_two_plane_waves (Q : RectangularBarrier) (k : ℝ) (A B : ℂ) (x : ℝ) :
    Q.probabilityCurrent (fun y => A * planeWave k y + B * planeWave (-k) y) x =
      ((ℏ : ℝ) / Q.m * k) * (‖A‖ ^ 2 - ‖B‖ ^ 2)
```

**`QuantumMechanics.RectangularBarrier.incident_norm_sq_eq`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L176).

> For a stationary wave with a left incident wave and no right incident wave, the incident
> squared amplitude equals the sum of the reflected and transmitted squared amplitudes.

```lean
lemma incident_norm_sq_eq (hψ : Q.IsStationaryWave E ψ) (hk : 0 < k)
    (hLeft : EqOn ψ (fun x => A * planeWave k x + B * planeWave (-k) x) (Iio Q.lower))
    (hRight : EqOn ψ (fun x => C * planeWave k x) (Ioi Q.upper)) :
    ‖A‖ ^ 2 = ‖B‖ ^ 2 + ‖C‖ ^ 2
```

**`QuantumMechanics.RectangularBarrier.reflection_add_transmission_eq_one`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L197).

> The reflection and transmission coefficients for a nonzero incident wave sum to one.

```lean
lemma reflection_add_transmission_eq_one (hψ : Q.IsStationaryWave E ψ) (hk : 0 < k) (hA : A ≠ 0)
    (hLeft : EqOn ψ (fun x => A * planeWave k x + B * planeWave (-k) x) (Iio Q.lower))
    (hRight : EqOn ψ (fun x => C * planeWave k x) (Ioi Q.upper)) :
    ‖B‖ ^ 2 / ‖A‖ ^ 2 + ‖C‖ ^ 2 / ‖A‖ ^ 2 = 1
```

## Depends on

- [The rectangular potential barrier](../../../physlib/quantummechanics/rectangularbarrier/basic.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean)
