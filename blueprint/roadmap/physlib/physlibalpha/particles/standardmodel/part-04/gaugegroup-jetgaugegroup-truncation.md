---
declaration: module
origin: cited
lean: StandardModel.JetGaugeGroupI.truncation, StandardModel.JetGaugeGroupI.truncation_one, StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_eq_zero_of_mem_truncationKer, StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_toSU3Matrix_eq_zero_of_mem_truncationKer, StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_toSU2Matrix_eq_zero_of_mem_truncationKer, StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_toU1Value_eq_zero_of_mem_truncationKer, StandardModel.JetGaugeGroupI.truncation_eq_one_of_mem_truncationKer
statement: formalized
proof: formalized
---

# Truncation of the jet gauge group

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.JetGaugeGroup.Truncation`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean): 7 declarations, 7 with a docstring.

## i. Overview

> Truncating a jet of gauge transformations at order `n` sets to zero, in every matrix
> entry, the Taylor coefficients of total degree above `n`. This `truncation n` is a plain
> function into the matrix data, not a homomorphism into `JetGaugeGroupI`: deleting the
> coefficients above order `n` breaks unitarity and multiplicativity at the orders between
> `n + 1` and `2n`.
>
> The homomorphic notion of a jet *trivial to order `n`* is the truncation filtration of the
> local-gauge-data package, `localGaugeData.truncationKer n`, defined in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Truncation` through the value and
> the Maurer–Cartan form of the jet alone. This file compares the two notions: a jet trivial to
> order `n` in that sense truncates to the identity, `truncation_eq_one_of_mem_truncationKer`.
> The argument is the Euler vanishing principle by degree on power series,
> `SpaceTimeAlgebra.coeff_eq_zero_of_pderiv_eq_mul`, applied to the radial relation
> `∂_ρ U = −i ω_ρ(U) U` between a jet and its Maurer–Cartan form.

## ii. Key results

> - `JetGaugeGroupI.truncation` : the `n`-th truncation of a jet.
> - `JetGaugeGroupI.truncation_eq_one_of_mem_truncationKer` : jets trivial to order `n`
>   truncate to the identity.

## iv. References

> * None.

## A. The truncation

**`StandardModel.JetGaugeGroupI.truncation`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L64).

> The `n`-th truncation of a jet of a gauge transformation: componentwise, all Taylor
> coefficients of total degree greater than `n` are set to zero.

```lean
noncomputable def truncation (n : ℕ) (U : JetGaugeGroupI) :
    Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra × Matrix (Fin 2)
        (Fin 2) SpaceTimeAlgebra × SpaceTimeAlgebra
```

**`StandardModel.JetGaugeGroupI.truncation_one`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L72).

> Truncation of the identity jet is the identity value triple.

```lean
lemma truncation_one (n : ℕ) : truncation n (1 : JetGaugeGroupI) = 1
```

## B. The comparison with the Maurer–Cartan filtration

**`StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_eq_zero_of_mem_truncationKer`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L89).

> The base-point Taylor data of the Maurer–Cartan form of a jet trivial to order `n`,
> read as power-series coefficients of a scalar component `f` of the jet gauge algebra
> through a scalar `ψ` of the gauge algebra computing evaluated iterated derivatives: they
> vanish below degree `n`.

```lean
lemma coeff_maurerCartanForm_eq_zero_of_mem_truncationKer (ψ : GaugeAlgebra → ℂ)
    (hψ : ψ 0 = 0) (f : JetGaugeAlgebra → SpaceTimeAlgebra)
    (hf : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra),
      ψ (JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv s a)) =
        constantCoeff (SpaceTimeAlgebra.iteratedPDeriv s (f a)))
    {U : JetGaugeGroupI} {n : ℕ} (hU : U ∈ localGaugeData.truncationKer n) (ρ : Fin 1 ⊕ Fin 3)
    {m : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hm : Finsupp.degree m < n) :
    coeff m (f (maurerCartanForm U ρ)) = 0
```

**`StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_toSU3Matrix_eq_zero_of_mem_truncationKer`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L109).

> The `su(3)` entries of `coeff_maurerCartanForm_eq_zero_of_mem_truncationKer`.

```lean
lemma coeff_maurerCartanForm_toSU3Matrix_eq_zero_of_mem_truncationKer {U : JetGaugeGroupI}
    {n : ℕ} (hU : U ∈ localGaugeData.truncationKer n) (ρ : Fin 1 ⊕ Fin 3)
    {m : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hm : Finsupp.degree m < n) (i j : Fin 3) :
    coeff m ((maurerCartanForm U ρ).toSU3Matrix i j) = 0
```

**`StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_toSU2Matrix_eq_zero_of_mem_truncationKer`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L119).

> The `su(2)` entries of `coeff_maurerCartanForm_eq_zero_of_mem_truncationKer`.

```lean
lemma coeff_maurerCartanForm_toSU2Matrix_eq_zero_of_mem_truncationKer {U : JetGaugeGroupI}
    {n : ℕ} (hU : U ∈ localGaugeData.truncationKer n) (ρ : Fin 1 ⊕ Fin 3)
    {m : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hm : Finsupp.degree m < n) (i j : Fin 2) :
    coeff m ((maurerCartanForm U ρ).toSU2Matrix i j) = 0
```

**`StandardModel.JetGaugeGroupI.coeff_maurerCartanForm_toU1Value_eq_zero_of_mem_truncationKer`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L129).

> The `u(1)` value of `coeff_maurerCartanForm_eq_zero_of_mem_truncationKer`.

```lean
lemma coeff_maurerCartanForm_toU1Value_eq_zero_of_mem_truncationKer {U : JetGaugeGroupI}
    {n : ℕ} (hU : U ∈ localGaugeData.truncationKer n) (ρ : Fin 1 ⊕ Fin 3)
    {m : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hm : Finsupp.degree m < n) :
    coeff m (maurerCartanForm U ρ).toU1Value = 0
```

**`StandardModel.JetGaugeGroupI.truncation_eq_one_of_mem_truncationKer`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean#L141).

> Maurer–Cartan triangularity for the Standard Model: a jet trivial to order `n` in the
> sense of the Maurer–Cartan filtration truncates to the identity at order `n`. On each
> factor the radial relation `∂_ρ U = −i ω_ρ(U) U` and the Euler vanishing principle
> propagate the vanishing of the Maurer–Cartan coefficients below degree `n` to the
> vanishing of the coefficients of `U` in nonzero degree up to `n`.

```lean
lemma truncation_eq_one_of_mem_truncationKer {U : JetGaugeGroupI} {n : ℕ}
    (hU : U ∈ localGaugeData.truncationKer n) : truncation n U = 1
```

## Depends on

- [The Standard Model gauge group as local gauge data](gaugegroup-localgaugedata.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/JetGaugeGroup/Truncation.lean)
