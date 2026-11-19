---
declaration: module
origin: cited
lean: QuantumMechanics.RectangularBarrier.probabilityCurrent, QuantumMechanics.RectangularBarrier.IsStationaryWave, QuantumMechanics.RectangularBarrier.probabilityCurrent_eq
statement: formalized
proof: formalized
---

# Stationary probability current at a rectangular barrier

The module `PhyslibAlpha.QuantumMechanics.RectangularBarrier.ProbabilityCurrent`, [PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean): 3 declarations, 3 with a docstring; 2 private, not shown.

> Conservation of the one-dimensional current across both barrier interfaces.

## i. Overview

> A stationary wave is represented by a function of the real spatial coordinate.
> For a real potential, the Schrödinger equation makes the derivative of the
> probability current vanish within each region. Continuity of the wave and its
> first derivative gives the same current on both sides of each interface.

## ii. Key results

> - `RectangularBarrier.probabilityCurrent_eq` gives equality of the current at any
>   two positions for a classical stationary wave of the barrier.

## iv. References

> * None.

## A. Probability current and stationary waves

**`QuantumMechanics.RectangularBarrier.probabilityCurrent`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L54).

> The probability current along the real spatial coordinate, with the
> particle mass of the rectangular barrier and the reduced Planck constant.

```lean
def probabilityCurrent (Q : RectangularBarrier) (ψ : ℝ → ℂ) (x : ℝ) : ℝ
```

**`QuantumMechanics.RectangularBarrier.IsStationaryWave`**, a structure, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L60).

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

**`QuantumMechanics.RectangularBarrier.probabilityCurrent_eq`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean#L93).

> For a stationary wave of a rectangular barrier, the probability current
> is independent of position, including at both interfaces.

```lean
lemma probabilityCurrent_eq {Q : RectangularBarrier} {E : ℝ} {ψ : ℝ → ℂ}
    (hψ : Q.IsStationaryWave E ψ) (x y : ℝ) :
    Q.probabilityCurrent ψ x = Q.probabilityCurrent ψ y
```

## Depends on

- [The rectangular potential barrier](../../../physlib/quantummechanics/rectangularbarrier/basic.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/QuantumMechanics/RectangularBarrier/ProbabilityCurrent.lean)
