---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.starConjEquiv, SpaceTimeAlgebra.starConjEquiv_apply, SpaceTimeAlgebra.starConjEquiv_symm_apply, SpaceTimeAlgebra.coeff_single_one_mul, SpaceTimeAlgebra.constantCoeffₗ, SpaceTimeAlgebra.constantCoeffₗ_apply, SpaceTimeAlgebra.iteratedPDeriv_pderiv, SpaceTimeAlgebra.iteratedPDeriv_smul
statement: formalized
proof: formalized
---

# Star, derivatives, truncation and the Euler operator on the jet ring

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Basic`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean): 28 declarations, 20 with a docstring.

> The further structure the jet ring of spacetime carries, beyond its ring structure.

## i. Overview

> `Physlib.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Basic` carries `SpaceTimeAlgebra`, the ring of
> formal power series in the spacetime coordinates, which is the ring of jets of a field at a
> point. Four further pieces of structure on it are developed here, each needed to state a
> Lagrangian as an element of a jet algebra.
>
> The star operation is coefficientwise complex conjugation, fixing the formal variables: the
> spacetime coordinates are self-adjoint. It makes the jet ring a `StarRing` and a `StarModule`
> over both `ℝ` and `ℂ`, and `starConjEquiv` identifies the conjugate module of the jet ring with
> the jet ring itself, honestly `ℂ`-linearly, since the conjugate-linearity of `star` cancels
> against the twisted scalar action. That is what identifies the jets of a conjugate field with
> the conjugates of the jets.
>
> The formal partial derivative commutes with the star, and the iterated derivative
> `iteratedPDeriv` is additive, homogeneous and satisfies a Leibniz rule over the antidiagonal of
> the multiset of directions; `constantCoeff_iteratedPDeriv_mul` is the form a component
> computation uses.
>
> The truncation `truncation n` sets the Taylor coefficients of total degree above `n` to zero.
>
> Finally the Euler operator `∑ x^ρ ∂_ρ` detects jets: a jet with vanishing constant coefficient
> killed by the Euler operator is zero, and `coeff_eq_zero_of_coeff_pderiv_eq_zero` is the graded
> form of that statement, where control of the first derivatives below degree `n` controls the
> coefficients up to degree `n`.

## ii. Key results

> - `SpaceTimeAlgebra.coeff_star`, `SpaceTimeAlgebra.star_X` : the star is coefficientwise, and
>   the coordinates are self-adjoint.
> - `SpaceTimeAlgebra.starConjEquiv` : the conjugate module of the jet ring is the jet ring.
> - `SpaceTimeAlgebra.pderiv_star`, `SpaceTimeAlgebra.iteratedPDeriv_mul` : the derivative
>   commutes with the star, and the Leibniz rule for iterated derivatives.
> - `SpaceTimeAlgebra.truncation` : the truncation of a jet.
> - `SpaceTimeAlgebra.eq_zero_of_sum_X_smul_pderiv_eq_zero` : the Euler operator detects jets.
> - `SpaceTimeAlgebra.coeff_eq_zero_of_coeff_pderiv_eq_zero` : its graded form.

## iv. References

> The jet ring itself is in `Physlib.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Basic`.

## A. The star structure on the jet ring

> The star operation on the jet ring is coefficientwise complex conjugation, fixing
> the formal variables. In particular the spacetime coordinates are self-adjoint.

**`SpaceTimeAlgebra.starConjEquiv`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L90).

> **The real structure of the jet ring.** Coefficientwise conjugation is a `ℂ`-linear
> equivalence from the conjugate module of the jet ring back to the jet ring itself. It is
> honestly `ℂ`-linear, not merely semilinear, because the conjugate-linearity of `star`
> cancels against the twisted scalar action of `ConjModule`.
>
> This is what identifies the jets of a conjugate field with the conjugates of the jets:
> `ConjModule (SpaceTimeAlgebra ⊗[ℂ] V)` and `SpaceTimeAlgebra ⊗[ℂ] ConjModule V` differ
> exactly by this equivalence on the jet-ring factor.

```lean
noncomputable def starConjEquiv : ConjModule SpaceTimeAlgebra ≃ₗ[ℂ] SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.starConjEquiv_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L94).

```lean
lemma starConjEquiv_apply (f : ConjModule SpaceTimeAlgebra) :
    starConjEquiv f = star ((conjEquiv (k := ℂ) (M := SpaceTimeAlgebra)).symm f)
```

**`SpaceTimeAlgebra.starConjEquiv_symm_apply`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L98).

```lean
lemma starConjEquiv_symm_apply (f : SpaceTimeAlgebra) :
    starConjEquiv.symm f = conjEquiv (k := ℂ) (M := SpaceTimeAlgebra) (star f)
```

**`SpaceTimeAlgebra.coeff_single_one_mul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L105).

> The first-order Leibniz rule: the degree-one Taylor coefficient, in the
> direction `μ`, of a product of jets. This is the coefficient-level statement
> that the first jet of a product is given by the product rule.

```lean
lemma coeff_single_one_mul (μ : Fin 1 ⊕ Fin 3) (f g : SpaceTimeAlgebra) :
    coeff (Finsupp.single μ 1) (f * g) =
      coeff (Finsupp.single μ 1) f * constantCoeff g +
        constantCoeff f * coeff (Finsupp.single μ 1) g
```

**`SpaceTimeAlgebra.constantCoeffₗ`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L119).

> The constant-coefficient evaluation of a jet, as a `ℂ`-linear map.

```lean
noncomputable def constantCoeffₗ : SpaceTimeAlgebra →ₗ[ℂ] ℂ
```

**`SpaceTimeAlgebra.constantCoeffₗ_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L125).

```lean
lemma constantCoeffₗ_apply (f : SpaceTimeAlgebra) : constantCoeffₗ f = constantCoeff f
```

## B. The formal partial derivative

**`SpaceTimeAlgebra.iteratedPDeriv_pderiv`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L134).

> Iterated formal derivatives commute with a single formal partial derivative.

```lean
lemma iteratedPDeriv_pderiv (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (f : SpaceTimeAlgebra) :
    iteratedPDeriv s (pderiv μ f) = pderiv μ (iteratedPDeriv s f)
```

**`SpaceTimeAlgebra.iteratedPDeriv_smul`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L144).

> Iterated formal derivatives preserve complex scalar multiplication.

```lean
lemma iteratedPDeriv_smul (s : Multiset (Fin 1 ⊕ Fin 3)) (c : ℂ)
    (f : SpaceTimeAlgebra) :
    iteratedPDeriv s (c • f) = c • iteratedPDeriv s f
```

**`SpaceTimeAlgebra.iteratedPDeriv_neg`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L152).

> Iterated formal derivatives commute with negation.

```lean
lemma iteratedPDeriv_neg (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) :
    iteratedPDeriv s (-f) = -iteratedPDeriv s f
```

**`SpaceTimeAlgebra.iteratedPDeriv_zero_apply`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L160).

> The iterated formal derivative of the zero jet vanishes.

```lean
lemma iteratedPDeriv_zero_apply (s : Multiset (Fin 1 ⊕ Fin 3)) :
    iteratedPDeriv s (0 : SpaceTimeAlgebra) = 0
```

**`SpaceTimeAlgebra.iteratedPDeriv_sum`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L167).

> The iterated formal derivative of a finite sum.

```lean
lemma iteratedPDeriv_sum {κ : Type*} (s : Multiset (Fin 1 ⊕ Fin 3)) (t : Finset κ)
    (f : κ → SpaceTimeAlgebra) :
    iteratedPDeriv s (∑ k ∈ t, f k)
      = ∑ k ∈ t, iteratedPDeriv s (f k)
```

**`SpaceTimeAlgebra.iteratedPDeriv_C_of_ne_zero`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L179).

> The iterated derivative of a constant jet vanishes for a nonempty multiset of
> directions.

```lean
lemma iteratedPDeriv_C_of_ne_zero {s : Multiset (Fin 1 ⊕ Fin 3)} (hs : s ≠ 0) (c : ℂ) :
    iteratedPDeriv s (C c : SpaceTimeAlgebra) = 0
```

## C. Truncation of jets

**`SpaceTimeAlgebra.truncation`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L192).

> The `n`-th truncation of a jet: the Taylor coefficients of total degree
> greater than `n` are set to zero.

```lean
noncomputable def truncation (n : ℕ) (f : SpaceTimeAlgebra) : SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.coeff_truncation_of_le`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L196).

```lean
lemma coeff_truncation_of_le {n : ℕ} {m : (Fin 1 ⊕ Fin 3) →₀ ℕ}
    (h : Finsupp.degree m ≤ n) (f : SpaceTimeAlgebra) :
    coeff m (truncation n f) = coeff m f
```

**`SpaceTimeAlgebra.coeff_truncation_of_gt`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L201).

```lean
lemma coeff_truncation_of_gt {n : ℕ} {m : (Fin 1 ⊕ Fin 3) →₀ ℕ}
    (h : n < Finsupp.degree m) (f : SpaceTimeAlgebra) :
    coeff m (truncation n f) = 0
```

**`SpaceTimeAlgebra.truncation_add`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L205).

```lean
lemma truncation_add (n : ℕ) (f g : SpaceTimeAlgebra) :
    truncation n (f + g) = truncation n f + truncation n g
```

**`SpaceTimeAlgebra.truncation_zero`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L215).

```lean
lemma truncation_zero (n : ℕ) : truncation n (0 : SpaceTimeAlgebra) = 0
```

**`SpaceTimeAlgebra.truncation_one`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L224).

> Truncation fixes the identity: a constant series has its only nonzero Taylor
> coefficient in degree zero, which every truncation keeps.

```lean
lemma truncation_one (n : ℕ) : truncation n (1 : SpaceTimeAlgebra) = 1
```

**`SpaceTimeAlgebra.truncation_eq_one_of_coeff`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L233).

> A power series with value `1` and no coefficients in nonzero degree up to `n`
> truncates to `1`.

```lean
lemma truncation_eq_one_of_coeff {n : ℕ} {f : SpaceTimeAlgebra} (h0 : constantCoeff f = 1)
    (hf : ∀ p : (Fin 1 ⊕ Fin 3) →₀ ℕ, p ≠ 0 → Finsupp.degree p ≤ n → coeff p f = 0) :
    SpaceTimeAlgebra.truncation n f = SpaceTimeAlgebra.truncation n (1 : SpaceTimeAlgebra)
```

## D. The Euler operator

**`SpaceTimeAlgebra.coeff_X_smul`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L253).

> The Taylor coefficients of a jet multiplied by a formal coordinate: the
> coefficient shifts down by one in that direction.

```lean
lemma coeff_X_smul (ρ : Fin 1 ⊕ Fin 3) (f : SpaceTimeAlgebra) (p : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    coeff p ((X ρ : SpaceTimeAlgebra) • f) =
      if Finsupp.single ρ 1 ≤ p then coeff (p - Finsupp.single ρ 1) f else 0
```

**`SpaceTimeAlgebra.coeff_sum_X_smul_pderiv`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L262).

> The Euler (radial) operator acts on Taylor coefficients as multiplication by the
> total degree.

```lean
lemma coeff_sum_X_smul_pderiv (f : SpaceTimeAlgebra) (p : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    coeff p (∑ ρ, (X ρ : SpaceTimeAlgebra) • pderiv ρ f) =
      ((Finsupp.degree p : ℕ) : ℂ) * coeff p f
```

**`SpaceTimeAlgebra.eq_zero_of_sum_X_smul_pderiv_eq_zero`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L286).

> The scalar vanishing principle for the Euler operator: a jet vanishing at the base
> point that is killed by the Euler operator is zero.

```lean
lemma eq_zero_of_sum_X_smul_pderiv_eq_zero {f : SpaceTimeAlgebra} (h0 : constantCoeff f = 0)
    (hf : ∑ ρ, (X ρ : SpaceTimeAlgebra) • pderiv ρ f = 0) : f = 0
```

### D.1. The Euler vanishing principle by degree

> The graded form of `eq_zero_of_sum_X_smul_pderiv_eq_zero`: control of the first
> derivatives below degree `n` controls the coefficients up to degree `n`.

**`SpaceTimeAlgebra.coeff_mul_eq_zero_of_lt`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L308).

> A product with a factor whose coefficients vanish below degree `n` has coefficients
> vanishing below degree `n`.

```lean
lemma coeff_mul_eq_zero_of_lt {n : ℕ} {w : SpaceTimeAlgebra}
    (hw : ∀ q : (Fin 1 ⊕ Fin 3) →₀ ℕ, Finsupp.degree q < n → coeff q w = 0) (v : SpaceTimeAlgebra)
    {q : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hq : Finsupp.degree q < n) : coeff q (w * v) = 0
```

**`SpaceTimeAlgebra.coeff_eq_zero_of_coeff_pderiv_eq_zero`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L323).

> The Euler vanishing principle: a power series all of whose first derivatives have
> coefficients vanishing below degree `n` has vanishing coefficients in every nonzero degree
> up to `n`, since `∑_ρ x_ρ ∂_ρ f` has the coefficient of `f` at `p` scaled by the degree
> of `p`.

```lean
lemma coeff_eq_zero_of_coeff_pderiv_eq_zero {n : ℕ} {f : SpaceTimeAlgebra}
    (hf : ∀ (ρ : Fin 1 ⊕ Fin 3) (q : (Fin 1 ⊕ Fin 3) →₀ ℕ), Finsupp.degree q < n →
      coeff q (pderiv ρ f) = 0)
    {p : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hp : p ≠ 0) (hpn : Finsupp.degree p ≤ n) : coeff p f = 0
```

**`SpaceTimeAlgebra.coeff_eq_zero_of_pderiv_eq_mul`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L345).

> A power series satisfying a radial relation `∂_ρ f = x_ρ f`, with the `x_ρ` vanishing
> below degree `n`, has no coefficients in nonzero degree up to `n`.

```lean
lemma coeff_eq_zero_of_pderiv_eq_mul {n : ℕ} {f : SpaceTimeAlgebra}
    {x : (Fin 1 ⊕ Fin 3) → SpaceTimeAlgebra}
    (hd : ∀ ρ, pderiv ρ f = x ρ * f)
    (hx : ∀ (ρ : Fin 1 ⊕ Fin 3) (q : (Fin 1 ⊕ Fin 3) →₀ ℕ), Finsupp.degree q < n →
      coeff q (x ρ) = 0)
    {p : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hp : p ≠ 0) (hpn : Finsupp.degree p ≤ n) : coeff p f = 0
```

**`SpaceTimeAlgebra.C_real_smul`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L354).

```lean
lemma C_real_smul (r : ℝ) (x : ℂ) :
    (MvPowerSeries.C (r • x) : SpaceTimeAlgebra) = r • MvPowerSeries.C x
```

**`SpaceTimeAlgebra.constantCoeff_real_smul`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L359).

> The constant coefficient commutes with real scalars.

```lean
lemma constantCoeff_real_smul (r : ℝ) (f : SpaceTimeAlgebra) :
    MvPowerSeries.constantCoeff (r • f) = r • MvPowerSeries.constantCoeff f
```

**`SpaceTimeAlgebra.pderiv_real_smul`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L364).

> The formal derivatives commute with real scalars.

```lean
lemma pderiv_real_smul (μ : Fin 1 ⊕ Fin 3) (r : ℝ) (f : SpaceTimeAlgebra) :
    MvPowerSeries.pderiv μ (r • f) = r • MvPowerSeries.pderiv μ f
```

## Depends on

- [The conjugate module](../../../physlib/mathematics/modules/conjmodule.md)
- [Complex conjugation in the spacetime algebra](../../../physlib/spaceandtime/spacetime/spacetimealgebra-star.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean)
