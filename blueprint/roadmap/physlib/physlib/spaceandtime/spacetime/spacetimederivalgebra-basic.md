---
declaration: module
origin: cited
lean: SpaceTimeDerivAlgebraℂ, SpaceTimeDerivAlgebraℂ.basis, SpaceTimeDerivAlgebraℂ.basis_apply, SpaceTimeDerivAlgebraℂ.basis_zero, SpaceTimeDerivAlgebraℂ.basis_singleton, SpaceTimeDerivAlgebraℂ.basis_mul, SpaceTimeDerivAlgebraℂ.pairing, SpaceTimeDerivAlgebraℂ.pairing_basis
statement: formalized
proof: formalized
---

# The spacetime derivative algebra

The module `Physlib.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra.Basic`, [Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean): 15 declarations, 15 with a docstring.

> The algebra of derivative symbols on spacetime, which evaluate on the spacetime algebra.

## i. Overview

> In field theory, local quantities are built from a field and finitely many of its derivatives at
> a point. A linear combination of such derivatives is the value `(P φ)(x₀)` of a linear
> differential operator `P` with constant coefficients, and such an operator is a polynomial in the
> partial derivatives `∂_μ`. These polynomials, which we call derivative symbols, form the algebra
> `SpaceTimeDerivAlgebraℂ`. The value `(P φ)(x₀)` is determined by the derivatives of `φ` at `x₀`,
> which its Taylor series `taylorSeries x₀ φ` records as an element of the spacetime algebra. We
> therefore pair a symbol `P` with any series `f` by applying `P` to `f` and taking the value at the
> base point, so that pairing with `taylorSeries x₀ φ` gives `(P φ)(x₀)`.
>
> Throughout we use the notation of `SpaceTimeAlgebra`, whose elements we call series. For a
> multiset `s` of directions,
>
> - `x^s` is the monomial in which each `x^μ` occurs as often as `μ` occurs in `s`;
> - `∂^s f` is the iterated derivative of a series `f`, and `(∂^s f)(x₀)` is its value at the base
>   point `x₀`;
> - `s!` is the product of the factorials of the multiplicities in `s`;
> - `∂^s` is the derivative symbol of `∂^s f`, written `∂^[s]` in Lean.

## ii. Key results

> - `SpaceTimeDerivAlgebraℂ` : the algebra of derivative symbols.
> - `SpaceTimeDerivAlgebraℂ.basis` : the monomial basis indexed by multisets of directions.
> - `SpaceTimeDerivAlgebraℂ.basis_mul` : monomials multiply by adding multisets.
> - `SpaceTimeDerivAlgebraℂ.pairing` : applies a symbol to a series and evaluates at the base
>   point.
> - `SpaceTimeDerivAlgebraℂ.pairing_basis` : `∂^s` pairs with `f` to the value `(∂^s f)(x₀)`.
> - `SpaceTimeDerivAlgebraℂ.pairing_injective` : the pairing separates derivative symbols.
> - `SpaceTimeDerivAlgebraℂ.pairing_mul_basis_singleton` : multiplying by `∂_μ` differentiates the
>   series.

## iv. References

> * None.

## A. The derivative algebra

> The partial derivatives of a smooth field commute, so these polynomials are in commuting symbols
> `∂_μ`. Each symbol involves finitely many derivatives (whereas the Taylor series of a field keeps
> all of them). Formally, the derivative algebra is the symmetric algebra on
> `Module.Dual ℂ Lorentz.ComplexCoVector`, the dual of the complex covector module, with `∂_μ` the
> dual basis vector in direction `μ` and time coordinate `x⁰ = ct`.

**`SpaceTimeDerivAlgebraℂ`**, an abbrev, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L80).

> The algebra of derivative symbols on spacetime, the polynomials in four commuting symbols
> `∂_μ`.

```lean
abbrev SpaceTimeDerivAlgebraℂ : Type
```

### A.1. The monomial basis

> The order of the monomial `∂^s` is the size of `s`, and multiplying monomials adds their
> multisets. The basis is Mathlib's `Module.Basis.symmetricAlgebra`, reindexed by multisets.

**`SpaceTimeDerivAlgebraℂ.basis`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L96).

> The monomial basis of the derivative algebra, in which `basis s` is the monomial `∂^s`.

```lean
noncomputable def basis : Module.Basis (Multiset (Fin 1 ⊕ Fin 3)) ℂ SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.basis_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L107).

> The monomial `∂^s` is the polynomial monomial whose exponents are the multiplicities in
> `s`.

```lean
lemma basis_apply (s : Multiset (Fin 1 ⊕ Fin 3)) :
    ∂^[s] = (SymmetricAlgebra.equivMvPolynomial Lorentz.ComplexCoVector.basis.dualBasis).symm
      (MvPolynomial.monomial (Multiset.toFinsupp s) 1)
```

**`SpaceTimeDerivAlgebraℂ.basis_zero`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L115).

> The empty monomial is the unit.

```lean
lemma basis_zero : ∂^[0] = 1
```

**`SpaceTimeDerivAlgebraℂ.basis_singleton`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L120).

> The monomial of a single direction `μ` is the derivative symbol `∂_μ`.

```lean
lemma basis_singleton (μ : Fin 1 ⊕ Fin 3) :
    ∂[μ] = SymmetricAlgebra.ι ℂ _ (Lorentz.ComplexCoVector.basis.dualBasis μ)
```

**`SpaceTimeDerivAlgebraℂ.basis_mul`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L126).

> Monomials multiply by adding multisets, `∂^s ∂^t = ∂^(s + t)`.

```lean
lemma basis_mul (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    ∂^[s] * ∂^[t] = ∂^[s + t]
```

## B. Pairing symbols with series

> The monomial `∂^s` pairs with a series `f` to `(∂^s f)(x₀)`, and the pairing extends linearly in
> the symbol (in commutative algebra this is the apolarity pairing, with power series in place of
> polynomials). On the Taylor series of a field it gives `(∂^s φ)(x₀)`, by
> `constantCoeff_iteratedPDeriv_taylorSeries`.

**`SpaceTimeDerivAlgebraℂ.pairing`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L144).

> The pairing of a symbol `P` with a series `f`, given by the value of `P f` at the base
> point.

```lean
noncomputable def pairing : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeAlgebra →ₗ[ℂ] ℂ
```

### B.1. Pairing with monomials

> Since `(∂^s f)(x₀)` is `s!` times the coefficient of `x^s` in `f` (`constantCoeff_iteratedPDeriv`),
> the symbol `∂_μ²` paired with the series `(x^μ)²` gives `2`, while the coefficient of `(x^μ)²` is
> `1`.

**`SpaceTimeDerivAlgebraℂ.pairing_basis`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L158).

> The monomial `∂^s` pairs with `f` to the base-point value `(∂^s f)(x₀)`.

```lean
lemma pairing_basis (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTimeAlgebra) :
    pairing ∂^[s] f = constantCoeff (iteratedPDeriv s f)
```

**`SpaceTimeDerivAlgebraℂ.pairing_one`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L164).

> The unit symbol pairs with `f` to its base-point value `f(x₀)`.

```lean
lemma pairing_one (f : SpaceTimeAlgebra) : pairing 1 f = constantCoeff f
```

**`SpaceTimeDerivAlgebraℂ.pairing_monomial`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L169).

> Pairing a symbol with the series `x^s` gives `s!` times the coefficient of `∂^s` in the
> symbol.

```lean
lemma pairing_monomial (p : SpaceTimeDerivAlgebraℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    pairing p (monomial (Multiset.toFinsupp s) 1) =
      ((∏ ν, (s.count ν).factorial : ℕ) : ℂ) * basis.repr p s
```

### B.2. Injectivity of the pairing

> The same computation on the monomials `x^s` recovers every coefficient of a symbol, so distinct
> symbols take different values on some series.

**`SpaceTimeDerivAlgebraℂ.pairing_injective`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L191).

> The pairing separates derivative symbols.

```lean
lemma pairing_injective : Function.Injective pairing
```

**`SpaceTimeDerivAlgebraℂ.ext_of_pairing_eq`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L199).

> Symbols that pair equally with every series are equal.

```lean
lemma ext_of_pairing_eq {p q : SpaceTimeDerivAlgebraℂ} (h : ∀ f, pairing p f = pairing q f) :
    p = q
```

### B.3. Multiplication by a derivative symbol

> Appending `∂_μ` to a symbol amounts to differentiating the series along `μ`, and on
> `taylorSeries x₀ φ` to differentiating the field, by `taylorSeries_deriv`.

**`SpaceTimeDerivAlgebraℂ.pairing_mul_basis_singleton`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L213).

> Multiplying a symbol by `∂_μ` corresponds to applying `pderiv μ` to the series.

```lean
lemma pairing_mul_basis_singleton (p : SpaceTimeDerivAlgebraℂ) (μ : Fin 1 ⊕ Fin 3)
    (f : SpaceTimeAlgebra) :
    pairing (p * ∂[μ]) f = pairing p (pderiv μ f)
```

### B.4. Pairing with a product

> Pairing `∂^s` with a product `χ f` gives `(∂^s (χ f))(x₀)`, which the Leibniz rule
> `constantCoeff_iteratedPDeriv_mul` expands as a sum of terms `(∂^t₁ χ)(x₀) (∂^t₂ f)(x₀)` with
> `t₁ + t₂ = s`. Replacing each `(∂^t₂ f)(x₀)` by the symbol `∂^t₂`, and extending linearly to all
> symbols, gives a symbol that pairs with `f` as the original pairs with `χ f`.

**`SpaceTimeDerivAlgebraℂ.pairing_basis_mul`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L235).

> Pairing `∂^s` with a product `χ f` expands by the Leibniz rule.

```lean
lemma pairing_basis_mul (s : Multiset (Fin 1 ⊕ Fin 3)) (χ f : SpaceTimeAlgebra) :
    pairing ∂^[s] (χ * f) =
      (s.antidiagonal.map fun t =>
        constantCoeff (iteratedPDeriv t.1 χ) * pairing ∂^[t.2] f).sum
```

**`SpaceTimeDerivAlgebraℂ.pairing_constr_leibniz`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean#L243).

> Replacing each monomial `∂^s` of `p` by its Leibniz expansion with `χ` gives a symbol that
> pairs with `f` as `p` pairs with `χ f`.

```lean
lemma pairing_constr_leibniz (χ : SpaceTimeAlgebra) (p : SpaceTimeDerivAlgebraℂ)
    (f : SpaceTimeAlgebra) :
    pairing (basis.constr ℂ (fun s => (s.antidiagonal.map fun t =>
      constantCoeff (iteratedPDeriv t.1 χ) • ∂^[t.2]).sum) p) f = pairing p (χ * f)
```

## Depends on

- [Complex Lorentz vectors](../../relativity/tensors/part-02/complextensor-vector-basic.md)
- [The spacetime algebra](spacetimealgebra-basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Basic.lean)
