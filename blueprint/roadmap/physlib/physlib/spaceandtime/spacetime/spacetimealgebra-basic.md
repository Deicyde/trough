---
declaration: module
origin: cited
lean: SpaceTimeAlgebra, SpaceTimeAlgebra.pderiv_comm, SpaceTimeAlgebra.iteratedPDeriv, SpaceTimeAlgebra.iteratedPDeriv_zero, SpaceTimeAlgebra.iteratedPDeriv_cons, SpaceTimeAlgebra.iteratedPDeriv_singleton, SpaceTimeAlgebra.iteratedPDeriv_add, SpaceTimeAlgebra.constantCoeff_iteratedPDeriv
statement: formalized
proof: formalized
---

# The spacetime algebra

The module `Physlib.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Basic`, [Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean): 20 declarations (1 instance with no name), 13 with a docstring.

## i. Overview

> The spacetime algebra `SpaceTimeAlgebra` is the ring of formal power series with complex
> coefficients in four variables, one for each spacetime direction. The value at the base point of
> an iterated partial derivative of a series is the corresponding coefficient multiplied by a
> factorial. Consequently, a series is determined by these derivative values, and every family of
> values arises from exactly one series. Iterated derivatives of a product obey the all-orders
> Leibniz rule.

## ii. Key results

> - `SpaceTimeAlgebra` : formal power series in the spacetime directions.
> - `SpaceTimeAlgebra.iteratedPDeriv` : iterated formal partial derivatives.
> - `SpaceTimeAlgebra.constantCoeff_iteratedPDeriv` : derivative values are `s!` times coefficients.
> - `SpaceTimeAlgebra.iteratedPDeriv_mul` : the all-orders Leibniz rule.
> - `SpaceTimeAlgebra.ext_of_constantCoeff_iteratedPDeriv` : derivative values determine a series.
> - `SpaceTimeAlgebra.ofDerivValues` : the series with given derivative values.
> - `SpaceTimeAlgebra.ofDerivValues_constantCoeff_iteratedPDeriv` : Taylor's formula.
> - `SpaceTimeAlgebra.derivValuesEquiv` : series and derivative values are linearly equivalent.

## iv. References

> * P. Haukkanen, Formal power series in several variables, Notes on Number Theory and Discrete
>   Mathematics 25 (2019) 44–57, Section 4, Definitions 4.1–4.2 and Theorem 4.1, p. 48.
>   https://doi.org/10.7546/nntdm.2019.25.4.44-57 [ref: haukkanen\_2019\_formal\_power\_series]
> * I. Kolář, P. W. Michor and J. Slovák, Natural Operations in Differential Geometry,
>   Sections 12.5–12.6 and 12.18, for the interpretation of Taylor series as coordinate
>   expressions of jets. https://www.mat.univie.ac.at/~michor/kmsbookh.pdf
>   [ref: kolar\_michor\_slovak\_1993]

## A. The spacetime algebra

> The four spacetime directions are indexed by `Fin 1 ⊕ Fin 3`, with `Sum.inl 0` the time direction
> and `Sum.inr i` the three space directions. The spacetime algebra has one variable `x^μ` for each
> direction `μ`.
>
> These power series are formal, meaning that a series is an arbitrary family of complex
> coefficients, one for each monomial, and no convergence condition is imposed.
>
> The formal variables represent coordinate displacements from a fixed, implicit spacetime point, the
> base point. The constant coefficient represents the field value at that point. In differential
> geometry, the data of all derivatives of a smooth map at a point is called its infinite-order jet
> at that point (a mathematical notion, unrelated to jets in collider physics). In fixed coordinates,
> the infinite-order jet of a smooth complex-valued field at the base point is recorded by the
> series of its Taylor coefficients, which is an element of the spacetime algebra.

**`SpaceTimeAlgebra`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L80).

> Formal power series in the four spacetime directions, with complex coefficients.

```lean
abbrev SpaceTimeAlgebra : Type
```

## B. Iterated formal partial derivatives

### B.1. Commutation of formal partial derivatives

> `pderiv μ` differentiates a series term by term with the power rule in `x^μ`, treating the other
> variables as constants. Formal partial derivatives in different directions commute, so an iterated
> derivative depends only on how many times each direction occurs. We therefore index iterated
> derivatives by a multiset `s` of directions (an unordered list in which repetition is allowed) and
> write `∂^s f` for `iteratedPDeriv s f`. For example, the multiset containing `μ` twice and `ν` once
> gives `∂_μ ∂_μ ∂_ν f`.

**`SpaceTimeAlgebra.pderiv_comm`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L102).

> Formal partial derivatives commute.

```lean
lemma pderiv_comm (μ ν : Fin 1 ⊕ Fin 3) (f : SpaceTimeAlgebra) :
    pderiv μ (pderiv ν f) = pderiv ν (pderiv μ f)
```

**An instance with no name**, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L113).

> Formal partial differentiation can be iterated over a multiset of directions.

```lean
instance : RightCommutative (fun (f : SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3) => pderiv μ f)
```

**`SpaceTimeAlgebra.iteratedPDeriv`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L118).

> The iterated formal partial derivative `∂^s f`, differentiating once along each element of
> `s`.

```lean
noncomputable def iteratedPDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) :
    SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.iteratedPDeriv_zero`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L123).

```lean
lemma iteratedPDeriv_zero (f : SpaceTimeAlgebra) : iteratedPDeriv 0 f = f
```

**`SpaceTimeAlgebra.iteratedPDeriv_cons`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L126).

```lean
lemma iteratedPDeriv_cons (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (f : SpaceTimeAlgebra) :
    iteratedPDeriv (μ ::ₘ s) f = iteratedPDeriv s (pderiv μ f)
```

**`SpaceTimeAlgebra.iteratedPDeriv_singleton`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L132).

```lean
lemma iteratedPDeriv_singleton (μ : Fin 1 ⊕ Fin 3) (f : SpaceTimeAlgebra) :
    iteratedPDeriv {μ} f = pderiv μ f
```

**`SpaceTimeAlgebra.iteratedPDeriv_add`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L135).

```lean
lemma iteratedPDeriv_add (s : Multiset (Fin 1 ⊕ Fin 3)) (f g : SpaceTimeAlgebra) :
    iteratedPDeriv s (f + g) = iteratedPDeriv s f + iteratedPDeriv s g
```

### B.2. Base-point values of iterated derivatives

> For a power series in one variable, the `n`-th derivative at `0` is `n!` times the coefficient of
> `xⁿ`. This section proves the analogue in several variables, on which the rest of the file is
> built. We write `(∂^s f)(0)` for the constant coefficient of `∂^s f`, which is its value at the base
> point where every `x^μ` is zero, and call the family `s ↦ (∂^s f)(0)` the base-point derivative
> values of `f`. A multiset `s` determines the monomial `x^s`, containing each `x^μ` as often as `μ`
> occurs in `s`, and the number `s!`, the product of the factorials of these multiplicities. Applying
> `∂^s` turns `x^s` into the constant `s!`, while every other monomial ends up either zero or without
> a constant term, so `(∂^s f)(0)` is `s!` times the coefficient of `x^s` in `f`.

**`SpaceTimeAlgebra.constantCoeff_iteratedPDeriv`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L157).

> The base-point value of `∂^s f` is `s!` times the coefficient of `x^s` in `f`.

```lean
lemma constantCoeff_iteratedPDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) :
    constantCoeff (iteratedPDeriv s f) =
      ((∏ ν, (s.count ν).factorial : ℕ) : ℂ) * coeff (Multiset.toFinsupp s) f
```

### B.3. The Leibniz rule

> To apply `∂^s` to `f g`, each direction in `s` acts on either `f` or `g`, so `∂^s (f g)` is a sum
> of `(∂^t₁ f) (∂^t₂ g)` over the splits `t₁ + t₂ = s` in `Multiset.antidiagonal s`. Each split
> appears once for every assignment of the elements of `s` that produces it, so repeated directions
> give multiplicities: `∂_μ² (f g) = (∂_μ² f) g + 2 (∂_μ f) (∂_μ g) + f (∂_μ² g)`. The same formula
> holds for base-point derivative values, but not for the Taylor coefficients, which are divided by
> `s!`.

**`SpaceTimeAlgebra.iteratedPDeriv_mul`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L190).

> The all-orders Leibniz rule for iterated formal partial derivatives.

```lean
lemma iteratedPDeriv_mul (s : Multiset (Fin 1 ⊕ Fin 3)) (f g : SpaceTimeAlgebra) :
    iteratedPDeriv s (f * g) =
      (s.antidiagonal.map fun p => iteratedPDeriv p.1 f * iteratedPDeriv p.2 g).sum
```

**`SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_mul`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L201).

> The Leibniz rule for the base-point derivative values of a product.

```lean
lemma constantCoeff_iteratedPDeriv_mul (s : Multiset (Fin 1 ⊕ Fin 3)) (f g : SpaceTimeAlgebra) :
    constantCoeff (iteratedPDeriv s (f * g)) =
      (s.antidiagonal.map fun p =>
        constantCoeff (iteratedPDeriv p.1 f) * constantCoeff (iteratedPDeriv p.2 g)).sum
```

## C. Series with equal derivative values

> Since `s!` is nonzero, the coefficient of `x^s` in `f` is `(∂^s f)(0)` divided by `s!`. Two series
> with the same base-point derivative values therefore have the same coefficients, and so are
> equal. Similarly, a series whose first derivatives all vanish is the constant series given by its
> base-point value.

**`SpaceTimeAlgebra.ext_of_constantCoeff_iteratedPDeriv`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L219).

> Series whose iterated derivatives have the same base-point values are equal.

```lean
lemma ext_of_constantCoeff_iteratedPDeriv {f g : SpaceTimeAlgebra}
    (h : ∀ s, constantCoeff (iteratedPDeriv s f) = constantCoeff (iteratedPDeriv s g)) :
    f = g
```

**`SpaceTimeAlgebra.eq_C_of_pderiv_eq_zero`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L231).

> A series with vanishing first derivatives is constant.

```lean
lemma eq_C_of_pderiv_eq_zero {f : SpaceTimeAlgebra} (hf : ∀ μ, pderiv μ f = 0) :
    f = C (constantCoeff f)
```

## D. Series from derivative values

### D.1. Series with prescribed derivative values

> A family `F` of complex numbers indexed by multisets defines the series `ofDerivValues F`, whose
> coefficient of `x^s` is `F s` divided by `s!`. By B.2, its base-point derivative values are the
> values of `F`. Applied to the base-point derivative values of a series `f`, this construction
> returns `f`, which is Taylor's formula `f = Σ_s (∂^s f)(0) / s! · x^s` (Haukkanen, Theorem 4.1).

**`SpaceTimeAlgebra.ofDerivValues`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L249).

> The series whose base-point derivative values are `F`.

```lean
noncomputable def ofDerivValues (F : Multiset (Fin 1 ⊕ Fin 3) → ℂ) : SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.coeff_ofDerivValues`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L252).

```lean
lemma coeff_ofDerivValues (F : Multiset (Fin 1 ⊕ Fin 3) → ℂ) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    coeff m (ofDerivValues F) =
      ((∏ ν, (m ν).factorial : ℕ) : ℂ)⁻¹ * F (Finsupp.toMultiset m)
```

**`SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_ofDerivValues`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L258).

> The base-point derivative values of `ofDerivValues F` are `F`.

```lean
lemma constantCoeff_iteratedPDeriv_ofDerivValues (F : Multiset (Fin 1 ⊕ Fin 3) → ℂ)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    constantCoeff (iteratedPDeriv s (ofDerivValues F)) = F s
```

**`SpaceTimeAlgebra.ofDerivValues_constantCoeff_iteratedPDeriv`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L267).

> A series is recovered from its base-point derivative values by `ofDerivValues`.

```lean
lemma ofDerivValues_constantCoeff_iteratedPDeriv (f : SpaceTimeAlgebra) :
    ofDerivValues (fun s => constantCoeff (iteratedPDeriv s f)) = f
```

### D.2. The linear equivalence

> The two constructions are mutually inverse and `ℂ`-linear, so together they form the linear
> equivalence `derivValuesEquiv` between the spacetime algebra and `Multiset (Fin 1 ⊕ Fin 3) → ℂ`.

**`SpaceTimeAlgebra.derivValuesEquiv`**, a def, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L281).

> The linear equivalence between series and their base-point derivative values.

```lean
noncomputable def derivValuesEquiv : SpaceTimeAlgebra ≃ₗ[ℂ] (Multiset (Fin 1 ⊕ Fin 3) → ℂ)
```

**`SpaceTimeAlgebra.derivValuesEquiv_apply`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L291).

```lean
lemma derivValuesEquiv_apply (f : SpaceTimeAlgebra) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivValuesEquiv f s = constantCoeff (iteratedPDeriv s f)
```

**`SpaceTimeAlgebra.derivValuesEquiv_symm_apply`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean#L295).

```lean
lemma derivValuesEquiv_symm_apply (F : Multiset (Fin 1 ⊕ Fin 3) → ℂ) :
    derivValuesEquiv.symm F = ofDerivValues F
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Basic.lean)
