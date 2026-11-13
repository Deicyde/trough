---
declaration: module
origin: cited
lean: Electromagnetism.TempDistElectromagneticPotential, Electromagnetism.TempDistElectromagneticPotential.ofScalarPotential, Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotential, Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotentialFunction, Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotentialFunction_of_isDistBounded, Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotentialFunction_eq_zero_of_not_isDistBounded, Electromagnetism.TempDistElectromagneticPotential.ofVectorPotential, Electromagnetism.TempDistElectromagneticPotential.ofStaticVectorPotential
statement: formalized
proof: formalized
---

# The Electromagnetic Potential

The module `Physlib.Electromagnetism.TemperedDistributional.Basic`, [Physlib/Electromagnetism/TemperedDistributional/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean): 11 declarations, 6 with a docstring.

## i. Overview

> The electromagnetic potential `A^μ` is the fundamental objects in
> electromagnetism. Mathematically it is related to a connection
> on a `U(1)`-bundle.
>
> We define the electromagnetic potential as a distribution from
> spacetime to contravariant Lorentz vectors.

## ii. Key results

> - `TempDistElectromagneticPotential` : the type of electromagnetic potentials as distributions.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]
> * https://ph.qmul.ac.uk/sites/default/files/EMT10new.pdf. [ref: qmul\_emt10\_notes]

## A. The electromagnetic potential as a distribution

**`Electromagnetism.TempDistElectromagneticPotential`**, an abbrev, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L55).

> The electromagnetic potential as a distribution and as a tensor `A^μ`.

```lean
noncomputable abbrev TempDistElectromagneticPotential (d : ℕ := 3)
```

### A.1. Constructors

**`Electromagnetism.TempDistElectromagneticPotential.ofScalarPotential`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L74).

> The creation of an electromagnetic potential from a scalar potential.

```lean
noncomputable def ofScalarPotential {d} (c : SpeedOfLight) :
    ((Time × Space d) →d[ℝ] ℝ) →ₗ[ℝ] TempDistElectromagneticPotential d
```

**`Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotential`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L88).

> The creation of an electromagnetic potential from a static scalar potential.

```lean
noncomputable def ofStaticScalarPotential {d} (c : SpeedOfLight) :
    ((Space d) →d[ℝ] ℝ) →ₗ[ℝ] TempDistElectromagneticPotential d
```

**`Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotentialFunction`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L96).

> The creation of an electromagnetic potential from a static scalar-potential function.
>
> If the function is distribution-bounded, it is first promoted to a distribution using
> `Space.distOfFunction`. Otherwise the constructor returns zero.

```lean
noncomputable def ofStaticScalarPotentialFunction {d} (c : SpeedOfLight)
    (φ : Space d → ℝ) : TempDistElectromagneticPotential d
```

**`Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotentialFunction_of_isDistBounded`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L103).

```lean
lemma ofStaticScalarPotentialFunction_of_isDistBounded {d} (c : SpeedOfLight)
    (φ : Space d → ℝ) (hφ : Space.IsDistBounded φ) :
    ofStaticScalarPotentialFunction c φ =
      ofStaticScalarPotential c (Space.distOfFunction φ hφ)
```

**`Electromagnetism.TempDistElectromagneticPotential.ofStaticScalarPotentialFunction_eq_zero_of_not_isDistBounded`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L111).

```lean
lemma ofStaticScalarPotentialFunction_eq_zero_of_not_isDistBounded {d}
    (c : SpeedOfLight) (φ : Space d → ℝ) (hφ : ¬ Space.IsDistBounded φ) :
    ofStaticScalarPotentialFunction c φ = 0
```

**`Electromagnetism.TempDistElectromagneticPotential.ofVectorPotential`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L118).

> The creation of an electromagnetic potential from a vector potential.

```lean
noncomputable def ofVectorPotential {d} (c : SpeedOfLight) :
    ((Time × Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) →ₗ[ℝ]
    TempDistElectromagneticPotential d
```

**`Electromagnetism.TempDistElectromagneticPotential.ofStaticVectorPotential`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L130).

> The creation of an electromagnetic potential from a static vector potential.

```lean
noncomputable def ofStaticVectorPotential {d} (c : SpeedOfLight) :
    ((Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) →ₗ[ℝ] TempDistElectromagneticPotential d
```

### A.2. The derivative of the electromagnetic potential as a distribution

**`Electromagnetism.TempDistElectromagneticPotential.distTensorDeriv_eq_sum_sum`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L143).

```lean
lemma distTensorDeriv_eq_sum_sum {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    distTensorDeriv A ε =∑ μ, ∑ ν, (SpaceTime.distDeriv μ A ε ν) •
      Lorentz.CoVector.basis μ ⊗ₜ[ℝ] Lorentz.Vector.basis ν
```

### A.3. The derivative in terms of the basis

**`Electromagnetism.TempDistElectromagneticPotential.distTensorDeriv_basis_repr_apply`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L164).

```lean
lemma distTensorDeriv_basis_repr_apply {d} {μν : (Fin 1 ⊕ Fin d) × (Fin 1 ⊕ Fin d)}
    (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) :
    (Lorentz.CoVector.basis.tensorProduct Lorentz.Vector.basis).repr (distTensorDeriv A ε) μν =
    distDeriv μν.1 A ε μν.2
```

**`Electromagnetism.TempDistElectromagneticPotential.toTensor_distTensorDeriv_basis_repr_apply`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean#L183).

```lean
lemma toTensor_distTensorDeriv_basis_repr_apply {d} (A : TempDistElectromagneticPotential d)
    (ε : 𝓢(SpaceTime d, ℝ)) (b : ComponentIdx (S := realLorentzTensor d)
      (Fin.append ![Color.down] ![Color.up])) :
    (Tensor.basis _).repr (Tensorial.toTensor (distTensorDeriv A ε)) b =
    distDeriv (b 0) A ε (b 1)
```

## Depends on

- [Time slice](../../spaceandtime/spacetime/timeslice.md)
- [Distributions which are constant in time](../../spaceandtime/timeandspace/constanttimedist.md)

## Sources

- [Physlib/Electromagnetism/TemperedDistributional/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/TemperedDistributional/Basic.lean)
