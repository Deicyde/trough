---
declaration: module
origin: cited
lean: SpaceTimeDerivAlgebraℂ.basis_apply_symmetricAlgebra, SpaceTimeDerivAlgebraℂ.basis_nil, SpaceTimeDerivAlgebraℂ.deriv, SpaceTimeDerivAlgebraℂ.deriv_basis, SpaceTimeDerivAlgebraℂ.deriv_basis_multiset, SpaceTimeDerivAlgebraℂ.deriv_apply_eq_mul, SpaceTimeDerivAlgebraℂ.eval, SpaceTimeDerivAlgebraℂ.eval_basis
statement: formalized
proof: formalized
---

# Derivative algebras

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean): 58 declarations (1 instance with no name), 54 with a docstring.

> The algebras of derivative symbols `∂_s` in spacetime, their pairing with jets and their
> Lorentz action.

## i. Overview

> A Lagrangian density is built out of fields and their derivatives `∂_μ ∂_ν ⋯ φ`. The symbols
> `∂_s`, one for each multiset `s` of spacetime directions, span the symmetric algebra
> `SpaceTimeDerivAlgebraℂ` of the dual of complex covectors (defined in Physlib), and its real
> form `SpaceTimeDerivAlgebraℝ`. This file gives them the structure that the gauge-theory field
> algebras are built on.
>
> - The basis `basis s = ∂_s`, and the derivative operator `deriv μ`, which appends `μ` to `s`.
> - The pairing `eval` of a symbol with a jet `f`, under which `∂_s` reads off the base-point
>   value of `∂_s f` and `deriv μ` is the transpose of the formal partial derivative.
> - The action `jetRingAction χ` of a jet `χ`, the transpose of multiplication by `χ`. It is the
>   all-orders Leibniz rule, and is how a jet of gauge transformations acts on the derivatives of
>   a matter field.
> - The Lorentz action `repLorentzGroup`, through the dual covector representation.
> - The derivative-degree scaling `gradeScale t`, multiplying `∂_s` by `t ^ |s|`, and its
>   polynomial form `gradePoly`, which separates an element into its pieces of fixed degree.

## ii. Key results

> - `SpaceTimeDerivAlgebraℂ.basis_apply_symmetricAlgebra` : the basis vector at `s` is the
>   monomial of the symmetric algebra of dual symbols.
> - `SpaceTimeDerivAlgebraℂ.eval_basis_eq_constantCoeff_iteratedPDeriv` : the pairing of `∂_s`
>   with a jet `f` is the base-point value of `∂_s f`.
> - `SpaceTimeDerivAlgebraℂ.jetRingAction_basis_multiset` : the action of a jet on `∂_s` is the
>   Leibniz convolution of its base-point derivatives.
> - `SpaceTimeDerivAlgebraℂ.jetRingAction_mul` : the action of the jet ring is multiplicative.
> - `SpaceTimeDerivAlgebraℂ.repLorentzGroup`, `SpaceTimeDerivAlgebraℝ.repLorentzGroup` : the
>   Lorentz action on the derivative symbols.
> - `SpaceTimeDerivAlgebraℂ.gradePoly_eval_one`, `SpaceTimeDerivAlgebraℝ.gradePoly_eval_one` :
>   the pieces of fixed derivative degree add up to the element.

## iv. References

> * None.

## A. The complex derivative algebra

### A.1. The basis indexed by multisets

**`SpaceTimeDerivAlgebraℂ.basis_apply_symmetricAlgebra`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L92).

> The basis vector at a multiset of derivative indices is the corresponding basis monomial
> of the symmetric algebra of dual symbols. This is `basis_apply` of
> `Physlib.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra.Basic` in the symmetric-algebra form,
> rather than through `SymmetricAlgebra.equivMvPolynomial`.

```lean
lemma basis_apply_symmetricAlgebra (s : Multiset (Fin 1 ⊕ Fin 3)) :
    basis s =
      Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra (Multiset.toFinsupp s)
```

**`SpaceTimeDerivAlgebraℂ.basis_nil`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L100).

> The basis vector at the empty multiset is the unit of the algebra. The
> zeroth-order symbol carries no derivatives.

```lean
lemma basis_nil :
    basis ({} : Multiset (Fin 1 ⊕ Fin 3)) = 1
```

### A.2. The derivative operator

**`SpaceTimeDerivAlgebraℂ.deriv`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L118).

> The derivative of an element in `SpaceTimeDerivAlgebraℂ` taking e.g.
> `∂_s` to `∂_μ ∂_s`.

```lean
noncomputable def deriv (μ : Fin 1 ⊕ Fin 3) : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.deriv_basis`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L123).

> The derivative operator on a basis monomial of the symmetric algebra.

```lean
lemma deriv_basis (μ : Fin 1 ⊕ Fin 3) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    deriv μ (Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra m) =
      Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra (m + Finsupp.single μ 1)
```

**`SpaceTimeDerivAlgebraℂ.deriv_basis_multiset`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L130).

> The derivative operator on the multiset basis, appending the derivative
> index to the multiset.

```lean
lemma deriv_basis_multiset (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    deriv μ (basis s) = basis (s + {μ})
```

**`SpaceTimeDerivAlgebraℂ.deriv_apply_eq_mul`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L138).

> The derivative operator is right multiplication by the first-order derivative
> symbol.

```lean
lemma deriv_apply_eq_mul (μ : Fin 1 ⊕ Fin 3) (a : SpaceTimeDerivAlgebraℂ) :
    deriv μ a = a * basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))
```

### A.3. Evaluating on the Jet ring

**An instance with no name**, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L154).

> Differentiating a jet along a multiset of directions is well defined. The partial
> derivatives commute, so the fold over a multiset does not depend on the order.

```lean
instance : RightCommutative
    (fun (f : SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3) => MvPowerSeries.pderiv μ f)
```

**`SpaceTimeDerivAlgebraℂ.eval`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L159).

> The evaluation map taking a function `f : SpaceTimeAlgebra` to `∂_μ f`.

```lean
noncomputable def eval : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeAlgebra →ₗ[ℂ] ℂ
```

**`SpaceTimeDerivAlgebraℂ.eval_basis`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L167).

> The pairing of a basis monomial with a jet is its Taylor coefficient times the
> factorials of the multiplicities.

```lean
lemma eval_basis (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) (f : SpaceTimeAlgebra) :
    eval (Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra m) f =
      (∏ μ, (m μ)! : ℕ) • MvPowerSeries.coeff m f
```

**`SpaceTimeDerivAlgebraℂ.eval_monomial`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L174).

> The pairing of a symbol with a monomial jet reads off one coordinate of the symbol.

```lean
lemma eval_monomial (p : SpaceTimeDerivAlgebraℂ) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    eval p (MvPowerSeries.monomial m 1) =
      ((∏ μ, (m μ)! : ℕ) : ℂ) *
        Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra.repr p m
```

**`SpaceTimeDerivAlgebraℂ.eval_injective`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L193).

> A derivative symbol is determined by its pairings with jets.

```lean
lemma eval_injective {p q : SpaceTimeDerivAlgebraℂ}
    (h : ∀ f, eval p f = eval q f) : p = q
```

**`SpaceTimeDerivAlgebraℂ.eval_deriv`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L205).

> Adjointness. The shift of derivative symbols is the transpose of the formal
> partial derivative under the divided-power pairing.

```lean
lemma eval_deriv (ν : Fin 1 ⊕ Fin 3) (p : SpaceTimeDerivAlgebraℂ) (f : SpaceTimeAlgebra) :
    eval (deriv ν p) f = eval p (MvPowerSeries.pderiv ν f)
```

**`SpaceTimeDerivAlgebraℂ.eval_one`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L230).

> The pairing of the unit derivative symbol with a jet is its value at the base
> point, the empty derivative multiset reads off the constant term.

```lean
lemma eval_one (f : SpaceTimeAlgebra) :
    eval (1 : SpaceTimeDerivAlgebraℂ) f = MvPowerSeries.constantCoeff f
```

**`SpaceTimeDerivAlgebraℂ.eval_basis_eq_constantCoeff_iteratedPDeriv`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L240).

> Iterating adjointness. The pairing of the basis monomial `∂_s` with a jet is the
> constant term of the iterated formal partial derivative `∂_s f`. This is the concrete
> description of the divided-power pairing that `eval_deriv` encodes one derivative at a
> time.

```lean
lemma eval_basis_eq_constantCoeff_iteratedPDeriv (s : Multiset (Fin 1 ⊕ Fin 3))
    (f : SpaceTimeAlgebra) :
    eval (basis s) f =
      MvPowerSeries.constantCoeff (SpaceTimeAlgebra.iteratedPDeriv s f)
```

### A.4. The action of the Jet ring

**`SpaceTimeDerivAlgebraℂ.jetRingAction`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L263).

> The action of `χ` on the derivatives, this takes `∂_μ ·` to `∂_μ (χ ·)`,
> expanded out explicitly.

```lean
noncomputable def jetRingAction (χ : SpaceTimeAlgebra) :
    SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_basis`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L271).

> The action of a jet on a basis monomial of the symmetric algebra.

```lean
lemma jetRingAction_basis (χ : SpaceTimeAlgebra) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    jetRingAction χ (Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra m) =
      ∑ p ∈ Finset.antidiagonal m,
        ((∏ μ, (m μ).descFactorial (p.1 μ) : ℕ) : ℂ) • MvPowerSeries.coeff p.1 χ •
          Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra p.2
```

**`SpaceTimeDerivAlgebraℂ.eval_jetRingAction`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L279).

> The action of a jet is the transpose of multiplication by it.

```lean
lemma eval_jetRingAction (χ f : SpaceTimeAlgebra) (p : SpaceTimeDerivAlgebraℂ) :
    eval (jetRingAction χ p) f = eval p (χ * f)
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_basis_multiset`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L316).

> The action of a jet on a derivative monomial, in multiset form. `∂_s` is sent to the
> all-orders Leibniz convolution, each splitting `s = s₁ + s₂` of the derivative multiset
> contributing the base-point Taylor coefficient `(∂_{s₁} χ)(0)` against the lower monomial
> `∂_{s₂}`.
>
> This is `jetRingAction_basis` with the `Nat.choose` bookkeeping traded for the
> divided-power pairing. Both sides are compared through `eval`, where the identity is the
> Leibniz rule `SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_mul` at the base point. It is the form
> in which the transformation law of a matter field is stated.

```lean
lemma jetRingAction_basis_multiset (χ : SpaceTimeAlgebra) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    jetRingAction χ (basis s) =
      (s.antidiagonal.map fun p =>
        MvPowerSeries.constantCoeff
            (SpaceTimeAlgebra.iteratedPDeriv p.1 χ) • basis p.2).sum
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_C`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L338).

> Constant jets act on the derivative symbols by their value. `C c` has no
> derivative coordinates.

```lean
lemma jetRingAction_C (c : ℂ) :
    jetRingAction (MvPowerSeries.C c) = c • LinearMap.id
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_one`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L348).

> The unit jet acts trivially.

```lean
lemma jetRingAction_one : jetRingAction (1 : SpaceTimeAlgebra) = LinearMap.id
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_mul`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L355).

> The derivative action is multiplicative. It is the transpose of multiplication
> in the commutative jet ring. This makes `χ ↦ χ(∂)` a monoid homomorphism and
> hence yields representations of the jet gauge group on polynomial jet spaces.

```lean
lemma jetRingAction_mul (χ ψ : SpaceTimeAlgebra) :
    jetRingAction (χ * ψ) = jetRingAction χ ∘ₗ jetRingAction ψ
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_zero`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L364).

> The zero jet acts as zero.

```lean
lemma jetRingAction_zero : jetRingAction (0 : SpaceTimeAlgebra) = 0
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_add`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L371).

> The action of the jet ring is additive.

```lean
lemma jetRingAction_add (χ ψ : SpaceTimeAlgebra) :
    jetRingAction (χ + ψ) = jetRingAction χ + jetRingAction ψ
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_apply_one`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L380).

> The derivative action on the zeroth-order (field) symbol. It is scaled by the
> value of the jet at the base point.

```lean
lemma jetRingAction_apply_one (χ : SpaceTimeAlgebra) :
    jetRingAction χ (1 : SpaceTimeDerivAlgebraℂ) =
      MvPowerSeries.constantCoeff χ • 1
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_deriv`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L397).

> The commutation of the jet-ring action with the derivative operator. Acting by
> `χ` after differentiating equals differentiating after acting, plus the action
> of the derivative `∂_ν χ`. This is the operator form of the Leibniz rule
> `∂_ν (χ f) = χ ∂_ν f + (∂_ν χ) f` under the divided-power pairing.

```lean
lemma jetRingAction_deriv (χ : SpaceTimeAlgebra) (ν : Fin 1 ⊕ Fin 3) (a : SpaceTimeDerivAlgebraℂ) :
    jetRingAction χ (deriv ν a) =
      deriv ν (jetRingAction χ a) + jetRingAction (MvPowerSeries.pderiv ν χ) a
```

### A.5. The action of the Lorentz group

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L415).

> The representation of the Lorentz group `SL(2,ℂ)` on the algebra of derivative
> symbols, extending the dual covector representation multiplicatively.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_apply_one`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L438).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) : repLorentzGroup Λ 1 = 1
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_apply_mul`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L442).

> The Lorentz action on the derivative symbols is multiplicative.

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (a b : SpaceTimeDerivAlgebraℂ) :
    repLorentzGroup Λ (a * b) = repLorentzGroup Λ a * repLorentzGroup Λ b
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_apply_ι`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L448).

> The Lorentz action on a generator.

```lean
lemma repLorentzGroup_apply_ι (Λ : SL(2,ℂ)) (x : Module.Dual ℂ Lorentz.ComplexCoVector) :
    repLorentzGroup Λ (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector) x) =
      SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector)
        (Lorentz.ComplexCoVector.SL2CRep.dual Λ x)
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_deriv`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L457).

> The Lorentz action on a derivative. The derivative symbol transforms as a
> covector, mixing the spacetime directions by the components of `Λ` in the dual
> covector representation.

```lean
lemma repLorentzGroup_deriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : SpaceTimeDerivAlgebraℂ) :
    repLorentzGroup Λ (deriv μ a) =
      ∑ ν, (Lorentz.ComplexCoVector.SL2CRep.dual Λ (Lorentz.ComplexCoVector.basis.dualBasis μ))
        (Lorentz.ComplexCoVector.basis ν) • deriv ν (repLorentzGroup Λ a)
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_basis_singleton`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L477).

> The Lorentz action on the singleton derivative monomial. The derivative
> slot transforms by the columns of the Lorentz matrix.

```lean
lemma repLorentzGroup_basis_singleton (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    repLorentzGroup Λ (basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))) =
      ∑ ν, (((Lorentz.SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) •
        basis ({ν} : Multiset (Fin 1 ⊕ Fin 3))
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_basis_ofFn`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L488).

> The Lorentz action on the derivative monomial of an ordered tuple of directions. Every
> slot mixes by the columns of the Lorentz matrix, one factor per slot.

```lean
lemma repLorentzGroup_basis_ofFn (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    repLorentzGroup Λ (basis (List.ofFn l)) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (∏ i, (((Lorentz.SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) • basis (List.ofFn p)
```

### A.6. The derivative-degree scaling

**`SpaceTimeDerivAlgebraℂ.gradeScale`**, a def, [line 520](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L520).

> The derivative-degree scaling on the algebra of derivative symbols, the
> algebra map multiplying each generator by `t`, hence each degree-`n` monomial
> by `t ^ n`.

```lean
noncomputable def gradeScale (t : ℂ) : SpaceTimeDerivAlgebraℂ →ₐ[ℂ] SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.gradeScale_ι`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L524).

```lean
lemma gradeScale_ι (t : ℂ) (x : Module.Dual ℂ Lorentz.ComplexCoVector) :
    gradeScale t (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector) x) =
      t • SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector) x
```

**`SpaceTimeDerivAlgebraℂ.gradeScale_basis`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L531).

> The degree scaling multiplies the basis monomial at `s` by `t ^ |s|`.

```lean
lemma gradeScale_basis (t : ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradeScale t (basis s) = t ^ s.card • basis s
```

**`SpaceTimeDerivAlgebraℂ.gradeScale_repLorentzGroup`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L544).

> The degree scaling commutes with the Lorentz action, since the Lorentz action
> preserves the derivative degree.

```lean
lemma gradeScale_repLorentzGroup (t : ℂ) (Λ : SL(2,ℂ)) (a : SpaceTimeDerivAlgebraℂ) :
    gradeScale t (repLorentzGroup Λ a) = repLorentzGroup Λ (gradeScale t a)
```

### A.7. The derivative-degree polynomial

> The degree scaling of the previous section records the derivative degree in a scalar. The
> same construction with the scalar replaced by a formal variable records it in a polynomial:
> `gradePoly` is the linear map sending the basis monomial `∂_s` to `X ^ |s| ∂_s`, so the
> coefficient of `X ^ n` in `gradePoly a` is the part of `a` of derivative degree `n`.

**`SpaceTimeDerivAlgebraℂ.gradePoly`**, a def, [line 569](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L569).

> The derivative-degree polynomial on the algebra of derivative symbols, the linear map
> sending the basis monomial `∂_s` to `X ^ |s|` times itself. It is `gradeScale` with the
> scalar replaced by the formal variable `X`.

```lean
noncomputable def gradePoly : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] Polynomial SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.gradePoly_basis`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L574).

> The derivative-degree polynomial of a basis monomial is the monomial of degree `|s|`.

```lean
lemma gradePoly_basis (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradePoly (basis s) = Polynomial.monomial (Multiset.card s) (basis s)
```

**`SpaceTimeDerivAlgebraℂ.eval_algebraMap_gradePoly`**, a lemma, [line 580](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L580).

> Evaluating the derivative-degree polynomial at a scalar is the derivative-degree
> scaling by that scalar, so the two descriptions of the grading agree.

```lean
lemma eval_algebraMap_gradePoly (t : ℂ) (a : SpaceTimeDerivAlgebraℂ) :
    (gradePoly a).eval (algebraMap ℂ SpaceTimeDerivAlgebraℂ t) = gradeScale t a
```

**`SpaceTimeDerivAlgebraℂ.gradePoly_eval_one`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L596).

> Setting the formal variable to one recovers the original element, as the pieces of a
> graded decomposition sum to the element.

```lean
lemma gradePoly_eval_one (a : SpaceTimeDerivAlgebraℂ) : (gradePoly a).eval 1 = a
```

## B. The real derivative algebra

**`SpaceTimeDerivAlgebraℝ`**, an abbrev, [line 613](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L613).

> The ℝ-algebra of derivative symbols in spacetime.

```lean
abbrev SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup`**, a def, [line 620](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L620).

> The representation of the Lorentz group `SL(2,ℂ)` on the algebra of derivative
> symbols, extending the dual covector representation multiplicatively.

```lean
noncomputable def repLorentzGroup : Representation ℝ SL(2,ℂ) SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_apply_ι`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L644).

> The Lorentz action on a generator of the real derivative algebra.

```lean
lemma repLorentzGroup_apply_ι (Λ : SL(2,ℂ)) (x : Module.Dual ℝ Lorentz.CoVector) :
    repLorentzGroup Λ (SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector) x) =
      SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector)
        (Lorentz.CoVector.sl2Rep.dual Λ x)
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_apply_mul`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L652).

> The real derivative-algebra representation is multiplicative. It is the lift of a linear
> map to the symmetric algebra.

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ))
    (a b : SpaceTimeDerivAlgebraℝ) :
    SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ (a * b) =
      SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ a * SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ b
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_apply_one`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L659).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ 1 = 1
```

**`SpaceTimeDerivAlgebraℝ.gradeScale`**, a def, [line 665](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L665).

> The derivative-degree scaling on the real algebra of derivative symbols,
> the algebra map multiplying each generator by `t`.

```lean
noncomputable def gradeScale (t : ℝ) : SpaceTimeDerivAlgebraℝ →ₐ[ℝ] SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.gradeScale_ι`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L669).

```lean
lemma gradeScale_ι (t : ℝ) (x : Module.Dual ℝ Lorentz.CoVector) :
    gradeScale t (SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector) x) =
      t • SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector) x
```

**`SpaceTimeDerivAlgebraℝ.gradeScale_repLorentzGroup`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L677).

> The degree scaling commutes with the Lorentz action on the real derivative
> symbols.

```lean
lemma gradeScale_repLorentzGroup (t : ℝ) (Λ : SL(2,ℂ)) (a : SpaceTimeDerivAlgebraℝ) :
    gradeScale t (repLorentzGroup Λ a) = repLorentzGroup Λ (gradeScale t a)
```

## C. The multiset basis of `SpaceTimeDerivAlgebraℝ`

**`SpaceTimeDerivAlgebraℝ.basisMultiset`**, a def, [line 698](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L698).

> The basis of the symmetric algebra of dual real jet slots, indexed by multisets of
> spacetime indices.

```lean
noncomputable def basisMultiset :
    Basis (Multiset (Fin 1 ⊕ Fin 3)) ℝ (SymmetricAlgebra ℝ (Module.Dual ℝ Lorentz.CoVector))
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_apply`**, a lemma, [line 704](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L704).

> The multiset basis of the dual derivative symbols, as a basis vector of the
> symmetric algebra at the corresponding multi-index.

```lean
lemma basisMultiset_apply (s : Multiset (Fin 1 ⊕ Fin 3)) :
    basisMultiset s =
      Lorentz.CoVector.basis.dualBasis.symmetricAlgebra (Multiset.toFinsupp s)
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_mul`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L712).

> The multiset basis vectors of the real dual derivative slots multiply by adding the
> multisets.

```lean
lemma basisMultiset_mul (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    basisMultiset s * basisMultiset t =
      basisMultiset (s + t)
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_nil`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L727).

> The multiset basis of the real dual derivative slots at the empty multiset is the
> unit.

```lean
lemma basisMultiset_nil :
    basisMultiset (0 : Multiset (Fin 1 ⊕ Fin 3)) = 1
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_singleton`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L745).

> The multiset basis of the real dual derivative slots at a singleton index.

```lean
lemma basisMultiset_singleton (μ : Fin 1 ⊕ Fin 3) :
    basisMultiset ({μ} : Multiset (Fin 1 ⊕ Fin 3)) =
      SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector)
        (Lorentz.CoVector.basis.dualBasis μ)
```

## D. The derivative-degree polynomial on the real derivative algebra

**`SpaceTimeDerivAlgebraℝ.gradeScale_basisMultiset`**, a lemma, [line 764](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L764).

> The degree scaling multiplies the real basis monomial at `s` by `t ^ |s|`.

```lean
lemma gradeScale_basisMultiset (t : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradeScale t (basisMultiset s) = t ^ Multiset.card s • basisMultiset s
```

**`SpaceTimeDerivAlgebraℝ.gradePoly`**, a def, [line 777](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L777).

> The derivative-degree polynomial on the real algebra of derivative symbols, the linear
> map sending the basis monomial `∂_s` to `X ^ |s|` times itself.

```lean
noncomputable def gradePoly : SpaceTimeDerivAlgebraℝ →ₗ[ℝ] Polynomial SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.gradePoly_basisMultiset`**, a lemma, [line 783](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L783).

> The derivative-degree polynomial of a real basis monomial is the monomial of degree
> `|s|`.

```lean
lemma gradePoly_basisMultiset (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradePoly (basisMultiset s) =
      Polynomial.monomial (Multiset.card s) (basisMultiset s)
```

**`SpaceTimeDerivAlgebraℝ.eval_algebraMap_gradePoly`**, a lemma, [line 790](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L790).

> Evaluating the real derivative-degree polynomial at a scalar is the derivative-degree
> scaling by that scalar.

```lean
lemma eval_algebraMap_gradePoly (t : ℝ) (a : SpaceTimeDerivAlgebraℝ) :
    (gradePoly a).eval (algebraMap ℝ SpaceTimeDerivAlgebraℝ t) = gradeScale t a
```

**`SpaceTimeDerivAlgebraℝ.gradePoly_eval_one`**, a lemma, [line 806](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L806).

> Setting the formal variable to one recovers the original element of the real
> derivative algebra.

```lean
lemma gradePoly_eval_one (a : SpaceTimeDerivAlgebraℝ) : (gradePoly a).eval 1 = a
```

## Depends on

- [The spacetime derivative algebra](../../../physlib/spaceandtime/spacetime/spacetimederivalgebra-basic.md)
- [Functoriality of the symmetric algebra](../../mathematics/part-01/symmetricalgebra.md)
- [The representation of `SL(2, ℂ)` on real Lorentz covectors](../../relativity/tensors/realtensor-covector-representation.md)

## Proof depends on

- [Peeling the first slot off a sum over tuples](../../mathematics/part-02/formathlib/fin.md)
- [The dual of the complex covector representation](../../relativity/tensors/complextensor-vector-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean)
