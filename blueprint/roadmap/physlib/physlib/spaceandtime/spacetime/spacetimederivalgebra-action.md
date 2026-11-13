---
declaration: module
origin: cited
lean: SpaceTimeDerivAlgebraℂ.seriesAction, SpaceTimeDerivAlgebraℂ.seriesAction_basis, SpaceTimeDerivAlgebraℂ.pairing_seriesAction, SpaceTimeDerivAlgebraℂ.seriesAction_C, SpaceTimeDerivAlgebraℂ.seriesAction_apply_one, SpaceTimeDerivAlgebraℂ.seriesAction_basis_singleton, SpaceTimeDerivAlgebraℂ.seriesAction_mul_basis_singleton
statement: formalized
proof: formalized
---

# The action of spacetime series on derivative symbols

The module `Physlib.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra.Action`, [Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean): 7 declarations, 7 with a docstring.

> The action of formal power series in spacetime coordinates on polynomials in derivatives.

## i. Overview

> Multiplying a field component `φ` by a spacetime-dependent function `χ`, such as a matrix element
> of a local gauge transformation, changes its derivatives by the product rule. At a point `x₀`,
> `∂_μ (χ φ)(x₀) = χ(x₀) ∂_μ φ(x₀) + (∂_μ χ)(x₀) φ(x₀)`, so a first derivative of `χ φ` is a
> combination of derivatives of `φ`, and the same holds for any derivative symbol `P`. The symbol
> `seriesAction χ P` records this combination, applying `P` after multiplying by `χ`. We define the
> action on monomials by the product rule, and it respects sums and products of series, so
> `seriesAction` is a ring homomorphism from the spacetime algebra to the linear endomorphisms of
> the derivative algebra.
>
> In the statements `χ` is a series, the Taylor series of the function at `x₀`, and we use the
> notation of `SpaceTimeDerivAlgebraℂ` throughout.

## ii. Key results

> - `SpaceTimeDerivAlgebraℂ.seriesAction` : the action of series on derivative symbols.
> - `SpaceTimeDerivAlgebraℂ.pairing_seriesAction` : the action applies `P` after multiplying by `χ`.
> - `SpaceTimeDerivAlgebraℂ.seriesAction_basis_singleton` : the product rule for first-order
>   symbols.
> - `SpaceTimeDerivAlgebraℂ.seriesAction_mul_basis_singleton` : the action commutes with
>   multiplication by `∂_μ` up to the action of `pderiv μ χ`.

## iv. References

> * None.

## A. The action of a series

### A.1. The action on monomials

> The action of `χ` sends each monomial `∂^s` to its Leibniz expansion with `χ`, a finite sum of
> symbols, which pairs with `f` as `∂^s` pairs with `χ f` by `pairing_constr_leibniz`.

**`SpaceTimeDerivAlgebraℂ.seriesAction`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L70).

> The action of series on derivative symbols, defined on monomials by the product rule.

```lean
noncomputable def seriesAction : SpaceTimeAlgebra →+* Module.End ℂ SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.seriesAction_basis`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L81).

> The action of `χ` on a monomial `∂^s` is its Leibniz expansion.

```lean
lemma seriesAction_basis (χ : SpaceTimeAlgebra) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    seriesAction χ ∂^[s] =
      (s.antidiagonal.map fun t => constantCoeff (iteratedPDeriv t.1 χ) • ∂^[t.2]).sum
```

### A.2. Multiplication before differentiation

> Pairing a symbol with a series applies it and takes the value at `x₀`, so
> `pairing (seriesAction χ P) f = pairing P (χ * f)` says that `seriesAction χ P` applies `P` after
> multiplying by `χ`. In particular the constant series `C c` acts as multiplication by `c`.

**`SpaceTimeDerivAlgebraℂ.pairing_seriesAction`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L97).

> The action of `χ` multiplies by `χ` before applying the symbol.

```lean
lemma pairing_seriesAction (χ : SpaceTimeAlgebra) (p : SpaceTimeDerivAlgebraℂ)
    (f : SpaceTimeAlgebra) :
    pairing (seriesAction χ p) f = pairing p (χ * f)
```

**`SpaceTimeDerivAlgebraℂ.seriesAction_C`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L104).

> The constant series `C c` acts as scalar multiplication by `c`.

```lean
lemma seriesAction_C (c : ℂ) : seriesAction (C c) = c • LinearMap.id
```

## B. Low-order symbols and derivatives

### B.1. The unit and first-order symbols

> A series `χ` acts on the unit symbol by `χ(x₀)`, and sends `∂_μ` to `χ(x₀) ∂_μ + (∂_μ χ)(x₀)`,
> which is the product rule at the base point.

**`SpaceTimeDerivAlgebraℂ.seriesAction_apply_one`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L121).

> A series acts on the unit symbol by its base-point value.

```lean
lemma seriesAction_apply_one (χ : SpaceTimeAlgebra) :
    seriesAction χ 1 = constantCoeff χ • 1
```

**`SpaceTimeDerivAlgebraℂ.seriesAction_basis_singleton`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L127).

> A series `χ` sends `∂_μ` to `χ(x₀) ∂_μ + (∂_μ χ)(x₀)`, the product rule.

```lean
lemma seriesAction_basis_singleton (χ : SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3) :
    seriesAction χ ∂[μ] = constantCoeff χ • ∂[μ] + constantCoeff (pderiv μ χ) • 1
```

### B.2. Multiplication by a derivative symbol

> Appending `∂_μ` to a symbol amounts to differentiating the series it pairs with, by
> `pairing_mul_basis_singleton`, so the product rule for `∂_μ (χ f)` relates the action of `χ` to
> multiplication by `∂_μ`.

**`SpaceTimeDerivAlgebraℂ.seriesAction_mul_basis_singleton`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean#L144).

> The action commutes with multiplication by `∂_μ` up to the action of `pderiv μ χ`.

```lean
lemma seriesAction_mul_basis_singleton (χ : SpaceTimeAlgebra) (p : SpaceTimeDerivAlgebraℂ)
    (μ : Fin 1 ⊕ Fin 3) :
    seriesAction χ (p * ∂[μ]) = seriesAction χ p * ∂[μ] + seriesAction (pderiv μ χ) p
```

## Depends on

- [The spacetime derivative algebra](spacetimederivalgebra-basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra/Action.lean)
