---
declaration: module
origin: cited
lean: ClassicalMechanics.HarmonicOscillator.massMetricVal, ClassicalMechanics.HarmonicOscillator.massMetricVal_apply, ClassicalMechanics.HarmonicOscillator.tangentCoord_ne_zero, ClassicalMechanics.HarmonicOscillator.massMetricVal_pos, ClassicalMechanics.HarmonicOscillator.massMetricVal_isVonNBounded, ClassicalMechanics.HarmonicOscillator.massMetricVal_contMDiff, ClassicalMechanics.HarmonicOscillator.massRiemannianMetric, ClassicalMechanics.HarmonicOscillator.geometricKineticEnergy
statement: formalized
proof: formalized
---

# Geometric kinetic energy of the harmonic oscillator

The module `Physlib.ClassicalMechanics.HarmonicOscillator.Geometric.KineticEnergy`, [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean): 12 declarations, 12 with a docstring.

## i. Overview

> The configuration space of the geometric harmonic oscillator is `ConfigurationSpace`.
> At a configuration `q`, velocities are tangent vectors in
> `TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q`.
>
> The oscillator mass determines a Riemannian metric on `ConfigurationSpace`. At each
> configuration `q`, the metric is the mass-scaled Euclidean inner product on tangent
> vectors, recorded by `massMetricVal S q`.
>
> The kinetic energy associated with this mass metric is
> `geometricKineticEnergy S q v = (1 / 2 : ℝ) * S.massRiemannianMetric.inner q v v`.
> In coordinates this gives the standard expression
> `(1 / 2 : ℝ) * S.m * ⟪tangentCoord q v, tangentCoord q v⟫_ℝ`.

## ii. Key results

> - `massRiemannianMetric` : the mass-scaled Euclidean inner product as a Riemannian metric
>   on `ConfigurationSpace`.
> - `geometricKineticEnergy` : the geometric kinetic-energy function associated to the
>   oscillator mass metric.
> - `massRiemannianMetric_inner_apply` : evaluation of the mass metric in global tangent
>   coordinates.
> - `massRiemannianMetric_pos` : positive definiteness of the mass Riemannian metric.
> - `geometricKineticEnergy_massMetric_eq` : the metric-induced kinetic energy for
>   the oscillator mass metric is the mass-scaled coordinate kinetic energy.

## iv. References

> * Ivo Terek, Introductory Variational Calculus on Manifolds, pages 1-2.
>   [ref: terek\_variational\_manifolds]

## A. Pointwise mass metric

> The pointwise mass metric is the mass-scaled Euclidean inner product in global tangent
> coordinates. Its positivity, boundedness, and smoothness properties are established here
> before assembling the Riemannian metric.

**`ClassicalMechanics.HarmonicOscillator.massMetricVal`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L82).

> The value of the oscillator mass metric at `q`. It is the mass-scaled pullback of the
> Euclidean inner product along `tangentCoord q`, so
> `massMetricVal S q v w = S.m * ⟪tangentCoord q v, tangentCoord q w⟫_ℝ`.

```lean
noncomputable def massMetricVal (S : HarmonicOscillator) (q : ConfigurationSpace) :
    TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q →L[ℝ]
      TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q →L[ℝ] ℝ
```

**`ClassicalMechanics.HarmonicOscillator.massMetricVal_apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L90).

> Applying the mass metric value to two tangent vectors gives the mass-scaled Euclidean
> inner product of their coordinate representatives.

```lean
lemma massMetricVal_apply
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v w : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q) :
    massMetricVal S q v w = S.m * ⟪tangentCoord q v, tangentCoord q w⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.tangentCoord_ne_zero`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L97).

> A nonzero tangent vector has nonzero coordinate representative under `tangentCoord`.

```lean
lemma tangentCoord_ne_zero {q : ConfigurationSpace}
    {v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q}
    (hv : v ≠ 0) : tangentCoord q v ≠ 0
```

**`ClassicalMechanics.HarmonicOscillator.massMetricVal_pos`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L105).

> The oscillator mass metric is positive on nonzero tangent vectors.

```lean
lemma massMetricVal_pos
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q) (hv : v ≠ 0) :
    0 < massMetricVal S q v v
```

**`ClassicalMechanics.HarmonicOscillator.massMetricVal_isVonNBounded`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L113).

> The mass metric unit ball is bounded in the model norm.

```lean
lemma massMetricVal_isVonNBounded
    (S : HarmonicOscillator) (q : ConfigurationSpace) :
    IsVonNBounded ℝ
      {v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q | massMetricVal S q v v < 1}
```

**`ClassicalMechanics.HarmonicOscillator.massMetricVal_contMDiff`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L133).

> The oscillator mass metric is constant in the global tangent-bundle chart.

```lean
lemma massMetricVal_contMDiff (S : HarmonicOscillator) :
    ContMDiff 𝓘(ℝ, EuclideanSpace ℝ (Fin 1))
      (𝓘(ℝ, EuclideanSpace ℝ (Fin 1)).prod
        𝓘(ℝ, EuclideanSpace ℝ (Fin 1) →L[ℝ]
          EuclideanSpace ℝ (Fin 1) →L[ℝ] ℝ)) ω
      (fun q : ConfigurationSpace =>
        TotalSpace.mk'
          (EuclideanSpace ℝ (Fin 1) →L[ℝ] EuclideanSpace ℝ (Fin 1) →L[ℝ] ℝ)
          (E := fun q : ConfigurationSpace =>
            TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q →L[ℝ]
              TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q →L[ℝ] ℝ)
          q (massMetricVal S q))
```

## B. Riemannian mass metric

> The pointwise bilinear forms assemble into a `ContMDiffRiemannianMetric` on the oscillator
> configuration space.

**`ClassicalMechanics.HarmonicOscillator.massRiemannianMetric`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L161).

> The mass-scaled Euclidean inner product as a Riemannian metric on the oscillator
> configuration space.

```lean
noncomputable def massRiemannianMetric (S : HarmonicOscillator) :
    ContMDiffRiemannianMetric 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) ω
      (EuclideanSpace ℝ (Fin 1))
      (TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) : ConfigurationSpace → Type _)
```

## C. Geometric kinetic energy

> The geometric kinetic energy is defined directly from the oscillator's mass Riemannian
> metric.

**`ClassicalMechanics.HarmonicOscillator.geometricKineticEnergy`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L180).

> The defining formula for the oscillator geometric kinetic energy.

```lean
noncomputable def geometricKineticEnergy
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q) : ℝ
```

**`ClassicalMechanics.HarmonicOscillator.geometricKineticEnergy_eq`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L187).

> The geometric kinetic energy is one half the mass Riemannian metric applied to `v`
> twice.

```lean
lemma geometricKineticEnergy_eq
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q) :
    geometricKineticEnergy S q v =
      (1 / 2 : ℝ) * S.massRiemannianMetric.inner q v v
```

## D. Coordinate formula

> The coordinate identities below recover the usual mass-scaled formula for kinetic energy.

**`ClassicalMechanics.HarmonicOscillator.massRiemannianMetric_pos`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L201).

> The oscillator mass Riemannian metric is positive definite.

```lean
lemma massRiemannianMetric_pos
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q)
    (hv : v ≠ 0) :
    0 < S.massRiemannianMetric.inner q v v
```

**`ClassicalMechanics.HarmonicOscillator.massRiemannianMetric_inner_apply`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L210).

> In the global coordinate, the oscillator mass metric is the mass-scaled Euclidean inner
> product of coordinate representatives.

```lean
lemma massRiemannianMetric_inner_apply
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v w : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q) :
    S.massRiemannianMetric.inner q v w =
      S.m * ⟪tangentCoord q v, tangentCoord q w⟫_ℝ
```

**`ClassicalMechanics.HarmonicOscillator.geometricKineticEnergy_massMetric_eq`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean#L219).

> The metric-induced kinetic energy for the mass metric has the standard
> harmonic-oscillator coordinate form.

```lean
lemma geometricKineticEnergy_massMetric_eq
    (S : HarmonicOscillator) (q : ConfigurationSpace)
    (v : TangentSpace 𝓘(ℝ, EuclideanSpace ℝ (Fin 1)) q) :
    geometricKineticEnergy S q v =
      (1 / 2 : ℝ) * S.m * ⟪tangentCoord q v, tangentCoord q v⟫_ℝ
```

## Depends on

- [The Classical Harmonic Oscillator](../basic.md)
- [Configuration space of the harmonic oscillator](basic.md)

## Sources

- [Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HarmonicOscillator/Geometric/KineticEnergy.lean)
