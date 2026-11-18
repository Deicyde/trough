---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillatorWithDim, ClassicalMechanics.HarmonicOscillatorWithDim.toHarmonicOscillator, ClassicalMechanics.HarmonicOscillatorWithDim.positionNormSq, ClassicalMechanics.HarmonicOscillatorWithDim.positionNormSq_val, ClassicalMechanics.HarmonicOscillatorWithDim.potentialEnergy, ClassicalMechanics.HarmonicOscillatorWithDim.potentialEnergy_val, ClassicalMechanics.HarmonicOscillatorWithDim.potentialEnergy_eq_transport, ClassicalMechanics.HarmonicOscillatorWithDim.hasFDerivAt_potentialEnergy
statement: formalized
proof: formalized
---

# A. A harmonic oscillator with dimension-tagged parameters

The module `Physlib.ClassicalMechanics.HarmonicOscillator.WithDim`, [Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean): 9 declarations, 8 with a docstring.

> This module applies `WithDim` to the existing harmonic-oscillator model. The mass and spring
> constant themselves carry their physical dimensions, and the potential energy is assembled from
> dimension-tagged quantities. Its output dimension is therefore checked by the type of the
> expression rather than attached only after evaluating a numerical function.
>
> The explicit map `toHarmonicOscillator` connects the tagged model to the existing numerical model.
> The analytic results then reuse the general `WithDim` transport API and the existing numerical
> potential energy. The derivative remains an ordinary continuous linear map between the tagged
> coordinate spaces; a derivative whose value itself carries the quotient of output and input
> dimensions remains separate follow-up work.

## A.1. Dimension-tagged oscillator data

**`ClassicalMechanics.HarmonicOscillatorWithDim`**, a structure, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L41).

> A harmonic oscillator whose physical parameters carry their dimensions.
>
> The spring constant has dimension `M T⁻²`, so multiplying it by a squared length produces
> the energy dimension `M L² T⁻²`.

```lean
structure HarmonicOscillatorWithDim where
  /-- The oscillator mass. -/
  m : WithDim M𝓭 ℝ
  /-- The spring constant, with dimension `M T⁻²`. -/
  k : WithDim (M𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ
  /-- The mass is positive. -/
  m_pos : 0 < m
  /-- The spring constant is positive. -/
  k_pos : 0 < k
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.toHarmonicOscillator`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L54).

> Forget the dimension tags on the parameters to recover the existing numerical model.

```lean
def toHarmonicOscillator (S : HarmonicOscillatorWithDim) : HarmonicOscillator
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.positionNormSq`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L61).

> The squared norm of a length-tagged position, carrying dimension `L²`.

```lean
noncomputable def positionNormSq
    (x : WithDim L𝓭 (EuclideanSpace ℝ (Fin 1))) : WithDim (L𝓭 * L𝓭) ℝ
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.positionNormSq_val`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L66).

```lean
lemma positionNormSq_val (x : WithDim L𝓭 (EuclideanSpace ℝ (Fin 1))) :
    (positionNormSq x).val = ⟪x.val, x.val⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.potentialEnergy`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L70).

> The potential energy `1/2 k x²`, with its energy dimension checked by the tagged expression.

```lean
noncomputable def potentialEnergy (S : HarmonicOscillatorWithDim) :
    WithDim L𝓭 (EuclideanSpace ℝ (Fin 1)) →
      WithDim (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹) ℝ
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.potentialEnergy_val`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L77).

> In numerical coordinates, the tagged potential energy is the existing oscillator potential.

```lean
lemma potentialEnergy_val (S : HarmonicOscillatorWithDim)
    (x : WithDim L𝓭 (EuclideanSpace ℝ (Fin 1))) :
    (S.potentialEnergy x).val = S.toHarmonicOscillator.potentialEnergy x.val
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.potentialEnergy_eq_transport`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L84).

> The typed potential energy is the explicit coordinate transport of the existing model.

```lean
lemma potentialEnergy_eq_transport (S : HarmonicOscillatorWithDim) :
    S.potentialEnergy =
      WithDim.transport L𝓭 (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹)
        S.toHarmonicOscillator.potentialEnergy
```

## A.2. Analytic reuse

**`ClassicalMechanics.HarmonicOscillatorWithDim.hasFDerivAt_potentialEnergy`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L97).

> The tagged potential energy is differentiable with the transported numerical derivative.

```lean
lemma hasFDerivAt_potentialEnergy (S : HarmonicOscillatorWithDim)
    (x : WithDim L𝓭 (EuclideanSpace ℝ (Fin 1))) :
    HasFDerivAt S.potentialEnergy
      (WithDim.transportLinearMap L𝓭 (M𝓭 * L𝓭 * L𝓭 * T𝓭⁻¹ * T𝓭⁻¹)
        (fderiv ℝ S.toHarmonicOscillator.potentialEnergy x.val)) x
```

**`ClassicalMechanics.HarmonicOscillatorWithDim.continuous_potentialEnergy`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean#L110).

> The dimension-tagged potential energy is continuous.

```lean
lemma continuous_potentialEnergy (S : HarmonicOscillatorWithDim) :
    Continuous S.potentialEnergy
```

## Depends on

- [The Classical Harmonic Oscillator](basic.md)
- [A. Analysis of dimension-tagged quantities](../../units/withdim/analysis.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/WithDim.lean)
