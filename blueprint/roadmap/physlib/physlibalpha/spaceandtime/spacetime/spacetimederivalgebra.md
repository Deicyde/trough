---
declaration: module
origin: cited
lean: SpaceTimeDerivAlgebraℂ.basis_apply_symmetricAlgebra, SpaceTimeDerivAlgebraℂ.basis_nil, SpaceTimeDerivAlgebraℂ.deriv, SpaceTimeDerivAlgebraℂ.deriv_basis, SpaceTimeDerivAlgebraℂ.deriv_comm_apply, SpaceTimeDerivAlgebraℂ.deriv_basis_multiset, SpaceTimeDerivAlgebraℂ.deriv_apply_eq_mul, MvPowerSeries.pderiv_comm
statement: formalized
proof: formalized
---

# Derivative algebras

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean): 63 declarations (1 instance with no name), 48 with a docstring.

## i. Overview

## ii. Key results

> - `SpaceTimeDerivAlgebraℂ` : the ℂ-algebra of derivative symbols in spacetime
> - `basis` : the basis of the algebra of derivative symbols, indexed by multisets of spacetime
>   indices: the multiset `s` labels the monomial `∂_s`
> - `basis_apply_symmetricAlgebra` : the basis vector at a multiset of derivative indices is the
>   monomial of the symmetric algebra of dual symbols
> - `basis_nil` : the basis vector at the empty multiset is the unit of the algebra: the zeroth-order
>   symbol carries no derivatives

## iv. References

> * None.

## A. The complex derivative algebra

### A.1. The basis indexed by multisets

**`SpaceTimeDerivAlgebraℂ.basis_apply_symmetricAlgebra`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L69).

> The basis vector at a multiset of derivative indices is the corresponding basis monomial
> of the symmetric algebra of dual symbols. This is `basis_apply` of
> `Physlib.SpaceAndTime.SpaceTime.SpaceTimeDerivAlgebra.Basic` in the symmetric-algebra form,
> rather than through `SymmetricAlgebra.equivMvPolynomial`.

```lean
lemma basis_apply_symmetricAlgebra (s : Multiset (Fin 1 ⊕ Fin 3)) :
    basis s =
      Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra (Multiset.toFinsupp s)
```

**`SpaceTimeDerivAlgebraℂ.basis_nil`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L77).

> The basis vector at the empty multiset is the unit of the algebra: the
> zeroth-order symbol carries no derivatives.

```lean
lemma basis_nil :
    basis ({} : Multiset (Fin 1 ⊕ Fin 3)) = 1
```

### A.2. The derivative operator

**`SpaceTimeDerivAlgebraℂ.deriv`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L95).

> The derivative of an element in `SpaceTimeDerivAlgebraℂ` taking e.g.
> `∂_s` to `∂_μ ∂_s`.

```lean
noncomputable def deriv (μ : Fin 1 ⊕ Fin 3) : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.deriv_basis`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L99).

```lean
lemma deriv_basis (μ : Fin 1 ⊕ Fin 3) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    deriv μ (Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra m) =
      Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra (m + Finsupp.single μ 1)
```

**`SpaceTimeDerivAlgebraℂ.deriv_comm_apply`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L104).

```lean
lemma deriv_comm_apply (μ ν : Fin 1 ⊕ Fin 3) (x : SpaceTimeDerivAlgebraℂ) :
    deriv μ (deriv ν x) = deriv ν (deriv μ x)
```

**`SpaceTimeDerivAlgebraℂ.deriv_basis_multiset`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L114).

> The derivative operator on the multiset basis: appending the derivative
> index to the multiset.

```lean
lemma deriv_basis_multiset (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    deriv μ (basis s) = basis (s + {μ})
```

**`SpaceTimeDerivAlgebraℂ.deriv_apply_eq_mul`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L122).

> The derivative operator is right multiplication by the first-order derivative
> symbol.

```lean
lemma deriv_apply_eq_mul (μ : Fin 1 ⊕ Fin 3) (a : SpaceTimeDerivAlgebraℂ) :
    deriv μ a = a * basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))
```

### A.3. Evaluating on the Jet ring

**`MvPowerSeries.pderiv_comm`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L138).

> Formal partial derivatives of a multivariate power series commute: each is given on
> coefficients by a shift and a multiplication, and the two shifts commute.

```lean
lemma _root_.MvPowerSeries.pderiv_comm {σ R : Type*} [CommSemiring R] (i j : σ)
    (f : MvPowerSeries σ R) :
    MvPowerSeries.pderiv i (MvPowerSeries.pderiv j f) =
      MvPowerSeries.pderiv j (MvPowerSeries.pderiv i f)
```

**An instance with no name**, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L154).

> Differentiating a jet along a multiset of directions is well defined: the partial
> derivatives commute, so the fold over a multiset does not depend on the order.

```lean
instance : RightCommutative
    (fun (f : SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3) => MvPowerSeries.pderiv μ f)
```

**`SpaceTimeDerivAlgebraℂ.eval`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L159).

> The evaluation map taking a function `f : SpaceTimeAlgebra` to `∂_μ f`.

```lean
noncomputable def eval : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeAlgebra →ₗ[ℂ] ℂ
```

**`SpaceTimeDerivAlgebraℂ.eval_basis`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L165).

```lean
lemma eval_basis (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) (f : SpaceTimeAlgebra) :
    eval (Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra m) f =
      (∏ μ, (m μ)! : ℕ) • MvPowerSeries.coeff m f
```

**`SpaceTimeDerivAlgebraℂ.eval_monomial`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L171).

```lean
lemma eval_monomial (p : SpaceTimeDerivAlgebraℂ) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    eval p (MvPowerSeries.monomial m 1) =
      ((∏ μ, (m μ)! : ℕ) : ℂ) *
        Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra.repr p m
```

**`SpaceTimeDerivAlgebraℂ.eval_injective`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L189).

```lean
lemma eval_injective {p q : SpaceTimeDerivAlgebraℂ}
    (h : ∀ f, eval p f = eval q f) : p = q
```

**`SpaceTimeDerivAlgebraℂ.eval_deriv`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L201).

> Adjointness: the shift of derivative symbols is the transpose of the formal
> partial derivative under the divided-power pairing.

```lean
lemma eval_deriv (ν : Fin 1 ⊕ Fin 3) (p : SpaceTimeDerivAlgebraℂ) (f : SpaceTimeAlgebra) :
    eval (deriv ν p) f = eval p (MvPowerSeries.pderiv ν f)
```

**`SpaceTimeDerivAlgebraℂ.eval_one`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L226).

> The pairing of the unit derivative symbol with a jet is its value at the base
> point: the empty derivative multiset reads off the constant term.

```lean
lemma eval_one (f : SpaceTimeAlgebra) :
    eval (1 : SpaceTimeDerivAlgebraℂ) f = MvPowerSeries.constantCoeff f
```

**`SpaceTimeDerivAlgebraℂ.eval_basis_eq_constantCoeff_iteratedPDeriv`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L236).

> Iterating adjointness: the pairing of the basis monomial `∂_s` with a jet is the
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

**`SpaceTimeDerivAlgebraℂ.jetRingAction`**, a def, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L259).

> The action of `χ` on the derivatives, this takes `∂_μ ·` to `∂_μ (χ ·)`,
> expanded out explicitly.

```lean
noncomputable def jetRingAction (χ : SpaceTimeAlgebra) :
    SpaceTimeDerivAlgebraℂ →ₗ[ℂ] SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_basis`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L266).

```lean
lemma jetRingAction_basis (χ : SpaceTimeAlgebra) (m : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    jetRingAction χ (Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra m) =
      ∑ p ∈ Finset.antidiagonal m,
        ((∏ μ, (m μ).descFactorial (p.1 μ) : ℕ) : ℂ) • MvPowerSeries.coeff p.1 χ •
          Lorentz.ComplexCoVector.basis.dualBasis.symmetricAlgebra p.2
```

**`SpaceTimeDerivAlgebraℂ.eval_jetRingAction`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L273).

```lean
lemma eval_jetRingAction (χ f : SpaceTimeAlgebra) (p : SpaceTimeDerivAlgebraℂ) :
    eval (jetRingAction χ p) f = eval p (χ * f)
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_basis_multiset`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L310).

> The action of a jet on a derivative monomial, in multiset form: `∂_s` is sent to the
> all-orders Leibniz convolution, each splitting `s = s₁ + s₂` of the derivative multiset
> contributing the base-point Taylor coefficient `(∂_{s₁} χ)(0)` against the lower monomial
> `∂_{s₂}`.
>
> This is `jetRingAction_basis` with the `Nat.choose` bookkeeping traded for the
> divided-power pairing: both sides are compared through `eval`, where the identity is the
> Leibniz rule `SpaceTimeAlgebra.constantCoeff_iteratedPDeriv_mul` at the base point. It is the form
> in which the transformation law of a matter field is stated.

```lean
lemma jetRingAction_basis_multiset (χ : SpaceTimeAlgebra) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    jetRingAction χ (basis s) =
      (s.antidiagonal.map fun p =>
        MvPowerSeries.constantCoeff
            (SpaceTimeAlgebra.iteratedPDeriv p.1 χ) • basis p.2).sum
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_C`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L332).

> Constant jets act on the derivative symbols by their value: `C c` has no
> derivative coordinates.

```lean
lemma jetRingAction_C (c : ℂ) :
    jetRingAction (MvPowerSeries.C c) = c • LinearMap.id
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_one`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L341).

```lean
lemma jetRingAction_one : jetRingAction (1 : SpaceTimeAlgebra) = LinearMap.id
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_mul`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L348).

> The derivative action is multiplicative: it is the transpose of multiplication
> in the commutative jet ring. This makes `χ ↦ χ(∂)` a monoid homomorphism and
> hence yields representations of the jet gauge group on polynomial jet spaces.

```lean
lemma jetRingAction_mul (χ ψ : SpaceTimeAlgebra) :
    jetRingAction (χ * ψ) = jetRingAction χ ∘ₗ jetRingAction ψ
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_zero`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L357).

```lean
lemma jetRingAction_zero : jetRingAction (0 : SpaceTimeAlgebra) = 0
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_add`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L363).

```lean
lemma jetRingAction_add (χ ψ : SpaceTimeAlgebra) :
    jetRingAction (χ + ψ) = jetRingAction χ + jetRingAction ψ
```

**`SpaceTimeDerivAlgebraℂ.jetRingActionHom`**, a def, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L372).

> The derivative action as a ring homomorphism from the jet ring to the
> endomorphisms of the algebra of derivative symbols: the module structure of the
> jet ring on its graded dual.

```lean
noncomputable def jetRingActionHom : SpaceTimeAlgebra →+* Module.End ℂ SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_comm`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L380).

> The actions of two jets commute: the jet ring is commutative.

```lean
lemma jetRingAction_comm (χ ψ : SpaceTimeAlgebra) (a : SpaceTimeDerivAlgebraℂ) :
    jetRingAction χ (jetRingAction ψ a) = jetRingAction ψ (jetRingAction χ a)
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_apply_one`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L388).

> The derivative action on the zeroth-order (field) symbol: it is scaled by the
> value of the jet at the base point.

```lean
lemma jetRingAction_apply_one (χ : SpaceTimeAlgebra) :
    jetRingAction χ (1 : SpaceTimeDerivAlgebraℂ) =
      MvPowerSeries.constantCoeff χ • 1
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_apply_ι`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L405).

> The derivative action on a first-order derivative symbol implements the Leibniz
> rule: `∂_μ ↦ χ(0) ∂_μ + (∂_μχ)(0) 1`. The value of the jet multiplies the
> first-derivative symbol, and its first derivative feeds the zeroth-order
> symbol.

```lean
lemma jetRingAction_apply_ι (χ : SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3) :
    jetRingAction χ (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector)
        (Lorentz.ComplexCoVector.basis.dualBasis μ)) =
      MvPowerSeries.constantCoeff χ •
        SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector)
          (Lorentz.ComplexCoVector.basis.dualBasis μ) +
        MvPowerSeries.coeff (Finsupp.single μ 1) χ • 1
```

**`SpaceTimeDerivAlgebraℂ.jetRingAction_deriv`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L445).

> The commutation of the jet-ring action with the derivative operator: acting by
> `χ` after differentiating equals differentiating after acting, plus the action
> of the derivative `∂_ν χ`. This is the operator form of the Leibniz rule
> `∂_ν (χ f) = χ ∂_ν f + (∂_ν χ) f` under the divided-power pairing.

```lean
lemma jetRingAction_deriv (χ : SpaceTimeAlgebra) (ν : Fin 1 ⊕ Fin 3) (a : SpaceTimeDerivAlgebraℂ) :
    jetRingAction χ (deriv ν a) =
      deriv ν (jetRingAction χ a) + jetRingAction (MvPowerSeries.pderiv ν χ) a
```

### A.5. The action of the Lorentz group

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup`**, a def, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L463).

> The representation of the Lorentz group `SL(2,ℂ)` on the algebra of derivative
> symbols, extending the dual covector representation multiplicatively.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_apply_one`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L486).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) : repLorentzGroup Λ 1 = 1
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_apply_mul`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L489).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (a b : SpaceTimeDerivAlgebraℂ) :
    repLorentzGroup Λ (a * b) = repLorentzGroup Λ a * repLorentzGroup Λ b
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_apply_ι`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L495).

> The Lorentz action on a generator.

```lean
lemma repLorentzGroup_apply_ι (Λ : SL(2,ℂ)) (x : Module.Dual ℂ Lorentz.ComplexCoVector) :
    repLorentzGroup Λ (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector) x) =
      SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector)
        (Lorentz.ComplexCoVector.SL2CRep.dual Λ x)
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_deriv`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L504).

> The Lorentz action on a derivative: the derivative symbol transforms as a
> covector, mixing the spacetime directions by the components of `Λ` in the dual
> covector representation.

```lean
lemma repLorentzGroup_deriv (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : SpaceTimeDerivAlgebraℂ) :
    repLorentzGroup Λ (deriv μ a) =
      ∑ ν, (Lorentz.ComplexCoVector.SL2CRep.dual Λ (Lorentz.ComplexCoVector.basis.dualBasis μ))
        (Lorentz.ComplexCoVector.basis ν) • deriv ν (repLorentzGroup Λ a)
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_basis_singleton`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L524).

> The Lorentz action on the singleton derivative monomial: the derivative
> slot transforms by the columns of the Lorentz matrix.

```lean
lemma repLorentzGroup_basis_singleton (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) :
    repLorentzGroup Λ (basis ({μ} : Multiset (Fin 1 ⊕ Fin 3))) =
      ∑ ν, (((Lorentz.SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) •
        basis ({ν} : Multiset (Fin 1 ⊕ Fin 3))
```

**`SpaceTimeDerivAlgebraℂ.repLorentzGroup_basis_ofFn`**, a lemma, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L535).

> The Lorentz action on the derivative monomial of an ordered tuple of directions: every
> slot mixes by the columns of the Lorentz matrix, one factor per slot.

```lean
lemma repLorentzGroup_basis_ofFn (Λ : SL(2,ℂ)) {n : ℕ} (l : Fin n → (Fin 1 ⊕ Fin 3)) :
    repLorentzGroup Λ (basis (List.ofFn l)) =
      ∑ p : Fin n → (Fin 1 ⊕ Fin 3),
        (∏ i, (((Lorentz.SL2C.toLorentzGroup Λ).1 (p i) (l i) : ℝ) : ℂ)) • basis (List.ofFn p)
```

### A.6. The derivative-degree scaling

**`SpaceTimeDerivAlgebraℂ.gradeScale`**, a def, [line 567](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L567).

> The derivative-degree scaling on the algebra of derivative symbols: the
> algebra map multiplying each generator by `t`, hence each degree-`n` monomial
> by `t ^ n`.

```lean
noncomputable def gradeScale (t : ℂ) : SpaceTimeDerivAlgebraℂ →ₐ[ℂ] SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.gradeScale_ι`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L571).

```lean
lemma gradeScale_ι (t : ℂ) (x : Module.Dual ℂ Lorentz.ComplexCoVector) :
    gradeScale t (SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector) x) =
      t • SymmetricAlgebra.ι ℂ (Module.Dual ℂ Lorentz.ComplexCoVector) x
```

**`SpaceTimeDerivAlgebraℂ.gradeScale_basis`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L578).

> The degree scaling multiplies the basis monomial at `s` by `t ^ |s|`.

```lean
lemma gradeScale_basis (t : ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradeScale t (basis s) = t ^ s.card • basis s
```

**`SpaceTimeDerivAlgebraℂ.gradeScale_repLorentzGroup`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L591).

> The degree scaling commutes with the Lorentz action: the Lorentz action
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

**`SpaceTimeDerivAlgebraℂ.gradePoly`**, a def, [line 616](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L616).

> The derivative-degree polynomial on the algebra of derivative symbols: the linear map
> sending the basis monomial `∂_s` to `X ^ |s|` times itself. It is `gradeScale` with the
> scalar replaced by the formal variable `X`.

```lean
noncomputable def gradePoly : SpaceTimeDerivAlgebraℂ →ₗ[ℂ] Polynomial SpaceTimeDerivAlgebraℂ
```

**`SpaceTimeDerivAlgebraℂ.gradePoly_basis`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L621).

> The derivative-degree polynomial of a basis monomial is the monomial of degree `|s|`.

```lean
lemma gradePoly_basis (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradePoly (basis s) = Polynomial.monomial (Multiset.card s) (basis s)
```

**`SpaceTimeDerivAlgebraℂ.eval_algebraMap_gradePoly`**, a lemma, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L627).

> Evaluating the derivative-degree polynomial at a scalar is the derivative-degree
> scaling by that scalar: the two descriptions of the grading agree.

```lean
lemma eval_algebraMap_gradePoly (t : ℂ) (a : SpaceTimeDerivAlgebraℂ) :
    (gradePoly a).eval (algebraMap ℂ SpaceTimeDerivAlgebraℂ t) = gradeScale t a
```

**`SpaceTimeDerivAlgebraℂ.gradePoly_eval_one`**, a lemma, [line 643](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L643).

> Setting the formal variable to one recovers the original element: the pieces of a
> graded decomposition sum to the element.

```lean
lemma gradePoly_eval_one (a : SpaceTimeDerivAlgebraℂ) : (gradePoly a).eval 1 = a
```

## B. The real derivative algebra

**`SpaceTimeDerivAlgebraℝ`**, an abbrev, [line 660](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L660).

> The ℝ-algebra of derivative symbols in spacetime.

```lean
abbrev SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup`**, a def, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L667).

> The representation of the Lorentz group `SL(2,ℂ)` on the algebra of derivative
> symbols, extending the dual covector representation multiplicatively.

```lean
noncomputable def repLorentzGroup : Representation ℝ SL(2,ℂ) SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_apply_ι`**, a lemma, [line 691](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L691).

> The Lorentz action on a generator of the real derivative algebra.

```lean
lemma repLorentzGroup_apply_ι (Λ : SL(2,ℂ)) (x : Module.Dual ℝ Lorentz.CoVector) :
    repLorentzGroup Λ (SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector) x) =
      SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector)
        (Lorentz.CoVector.sl2Rep.dual Λ x)
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_apply_mul`**, a lemma, [line 699](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L699).

> The real derivative-algebra representation is multiplicative: it is the lift of a linear
> map to the symmetric algebra.

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ))
    (a b : SpaceTimeDerivAlgebraℝ) :
    SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ (a * b) =
      SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ a * SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ b
```

**`SpaceTimeDerivAlgebraℝ.repLorentzGroup_apply_one`**, a lemma, [line 706](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L706).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    SpaceTimeDerivAlgebraℝ.repLorentzGroup Λ 1 = 1
```

**`SpaceTimeDerivAlgebraℝ.gradeScale`**, a def, [line 712](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L712).

> The derivative-degree scaling on the real algebra of derivative symbols:
> the algebra map multiplying each generator by `t`.

```lean
noncomputable def gradeScale (t : ℝ) : SpaceTimeDerivAlgebraℝ →ₐ[ℝ] SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.gradeScale_ι`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L716).

```lean
lemma gradeScale_ι (t : ℝ) (x : Module.Dual ℝ Lorentz.CoVector) :
    gradeScale t (SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector) x) =
      t • SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector) x
```

**`SpaceTimeDerivAlgebraℝ.gradeScale_repLorentzGroup`**, a lemma, [line 724](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L724).

> The degree scaling commutes with the Lorentz action on the real derivative
> symbols.

```lean
lemma gradeScale_repLorentzGroup (t : ℝ) (Λ : SL(2,ℂ)) (a : SpaceTimeDerivAlgebraℝ) :
    gradeScale t (repLorentzGroup Λ a) = repLorentzGroup Λ (gradeScale t a)
```

## C. The multiset basis of `SpaceTimeDerivAlgebraℝ`

**`SpaceTimeDerivAlgebraℝ.basisMultiset`**, a def, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L745).

> The basis of the symmetric algebra of dual real jet slots, indexed by multisets of
> spacetime indices.

```lean
noncomputable def basisMultiset :
    Basis (Multiset (Fin 1 ⊕ Fin 3)) ℝ (SymmetricAlgebra ℝ (Module.Dual ℝ Lorentz.CoVector))
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_apply`**, a lemma, [line 751](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L751).

> The multiset basis of the dual derivative symbols, as a basis vector of the
> symmetric algebra at the corresponding multi-index.

```lean
lemma basisMultiset_apply (s : Multiset (Fin 1 ⊕ Fin 3)) :
    basisMultiset s =
      Lorentz.CoVector.basis.dualBasis.symmetricAlgebra (Multiset.toFinsupp s)
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_mul`**, a lemma, [line 759](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L759).

> The multiset basis vectors of the real dual derivative slots multiply by adding the
> multisets.

```lean
lemma basisMultiset_mul (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    basisMultiset s * basisMultiset t =
      basisMultiset (s + t)
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_nil`**, a lemma, [line 774](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L774).

> The multiset basis of the real dual derivative slots at the empty multiset is the
> unit.

```lean
lemma basisMultiset_nil :
    basisMultiset (0 : Multiset (Fin 1 ⊕ Fin 3)) = 1
```

**`SpaceTimeDerivAlgebraℝ.basisMultiset_singleton`**, a lemma, [line 792](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L792).

> The multiset basis of the real dual derivative slots at a singleton index.

```lean
lemma basisMultiset_singleton (μ : Fin 1 ⊕ Fin 3) :
    basisMultiset ({μ} : Multiset (Fin 1 ⊕ Fin 3)) =
      SymmetricAlgebra.ι ℝ (Module.Dual ℝ Lorentz.CoVector)
        (Lorentz.CoVector.basis.dualBasis μ)
```

## D. The derivative-degree polynomial on the real derivative algebra

**`SpaceTimeDerivAlgebraℝ.gradeScale_basisMultiset`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L811).

> The degree scaling multiplies the real basis monomial at `s` by `t ^ |s|`.

```lean
lemma gradeScale_basisMultiset (t : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradeScale t (basisMultiset s) = t ^ Multiset.card s • basisMultiset s
```

**`SpaceTimeDerivAlgebraℝ.gradePoly`**, a def, [line 824](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L824).

> The derivative-degree polynomial on the real algebra of derivative symbols: the linear
> map sending the basis monomial `∂_s` to `X ^ |s|` times itself.

```lean
noncomputable def gradePoly : SpaceTimeDerivAlgebraℝ →ₗ[ℝ] Polynomial SpaceTimeDerivAlgebraℝ
```

**`SpaceTimeDerivAlgebraℝ.gradePoly_basisMultiset`**, a lemma, [line 830](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L830).

> The derivative-degree polynomial of a real basis monomial is the monomial of degree
> `|s|`.

```lean
lemma gradePoly_basisMultiset (s : Multiset (Fin 1 ⊕ Fin 3)) :
    gradePoly (basisMultiset s) =
      Polynomial.monomial (Multiset.card s) (basisMultiset s)
```

**`SpaceTimeDerivAlgebraℝ.eval_algebraMap_gradePoly`**, a lemma, [line 837](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L837).

> Evaluating the real derivative-degree polynomial at a scalar is the derivative-degree
> scaling by that scalar.

```lean
lemma eval_algebraMap_gradePoly (t : ℝ) (a : SpaceTimeDerivAlgebraℝ) :
    (gradePoly a).eval (algebraMap ℝ SpaceTimeDerivAlgebraℝ t) = gradeScale t a
```

**`SpaceTimeDerivAlgebraℝ.gradePoly_eval_one`**, a lemma, [line 853](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean#L853).

> Setting the formal variable to one recovers the original element of the real
> derivative algebra.

```lean
lemma gradePoly_eval_one (a : SpaceTimeDerivAlgebraℝ) : (gradePoly a).eval 1 = a
```

## Depends on

- [The spacetime derivative algebra](../../../physlib/spaceandtime/spacetime/spacetimederivalgebra-basic.md)
- [The representation of `SL(2, ℂ)` on real Lorentz covectors](../../relativity/tensors/realtensor-covector-representation.md)

## Proof depends on

- [Peeling the first slot off a sum over tuples](../../mathematics/part-02/formathlib/fin.md)
- [The dual of the complex covector representation](../../relativity/tensors/complextensor-vector-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeDerivAlgebra.lean)
