---
declaration: module
origin: cited
lean: QuantumMechanics.FiniteHilbertSpace.val_apply_basisFun, QuantumMechanics.FiniteHilbertSpace.val_apply, QuantumMechanics.FiniteHilbertSpace.onFst, QuantumMechanics.FiniteHilbertSpace.onSnd, QuantumMechanics.FiniteHilbertSpace.onFst_val, QuantumMechanics.FiniteHilbertSpace.onSnd_val, QuantumMechanics.FiniteHilbertSpace.onFst_comp, QuantumMechanics.FiniteHilbertSpace.onSnd_comp
statement: formalized
proof: formalized
---

# Operators on one coordinate of a product of finite targets

The module `PhyslibAlpha.QuantumMechanics.HilbertSpaces.FiniteTarget.Product`, [PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean): 13 declarations, 11 with a docstring.

## i. Overview

> A system whose configurations are pairs `(a, b)` has the Hilbert space `𝓗[α × β]`. An operator
> `A` on `𝓗[α]` acts on the first coordinate alone, `(A Ψ) (a, b) = ∑ a', ⟨a|A|a'⟩ Ψ (a', b)`,
> and leaves the second in place; an operator on `𝓗[β]` acts on the second coordinate in the same
> way. Operators on different coordinates commute, acting twice on one coordinate composes the
> operators, and hermitian operators stay hermitian.

## ii. Key results

> - `onFst`, `onSnd` : an operator acting on one coordinate of `𝓗[α × β]`.
> - `onFst_comp`, `onSnd_comp` : acting twice on the same coordinate.
> - `onFst_comp_onSnd` : operators on different coordinates commute.
> - `onFst_isSymmetric`, `onSnd_isSymmetric` : hermitian operators stay hermitian.

## iv. References

> * None.

## A. Amplitudes

**`QuantumMechanics.FiniteHilbertSpace.val_apply_basisFun`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L58).

> The amplitude `⟨a|A|a'⟩` of an operator is the `a` component of `A |a'⟩`.

```lean
lemma val_apply_basisFun (A : 𝓗[α] →ₗ[ℂ] 𝓗[α]) (a a' : α) :
    (A (basisFun α a')).val a = ⟪basisFun α a, A (basisFun α a')⟫_ℂ
```

**`QuantumMechanics.FiniteHilbertSpace.val_apply`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L63).

> An operator in components: `(A ψ) a = ∑ a', ⟨a|A|a'⟩ ψ a'`.

```lean
lemma val_apply (A : 𝓗[α] →ₗ[ℂ] 𝓗[α]) (ψ : 𝓗[α]) (a : α) :
    (A ψ).val a = ∑ a', (A (basisFun α a')).val a * ψ.val a'
```

## B. Operators on one coordinate

**`QuantumMechanics.FiniteHilbertSpace.onFst`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L80).

> The operator `A` acting on the first coordinate: `(A Ψ) (a, b) = ∑ a', ⟨a|A|a'⟩ Ψ (a', b)`.

```lean
noncomputable def onFst (A : 𝓗[α] →ₗ[ℂ] 𝓗[α]) : 𝓗[α × β] →ₗ[ℂ] 𝓗[α × β]
```

**`QuantumMechanics.FiniteHilbertSpace.onSnd`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L90).

> The operator `B` acting on the second coordinate: `(B Ψ) (a, b) = ∑ b', ⟨b|B|b'⟩ Ψ (a, b')`.

```lean
noncomputable def onSnd (B : 𝓗[β] →ₗ[ℂ] 𝓗[β]) : 𝓗[α × β] →ₗ[ℂ] 𝓗[α × β]
```

**`QuantumMechanics.FiniteHilbertSpace.onFst_val`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L99).

```lean
lemma onFst_val (A : 𝓗[α] →ₗ[ℂ] 𝓗[α]) (Ψ : 𝓗[α × β]) (p : α × β) :
    (onFst A Ψ).val p = ∑ a, (A (basisFun α a)).val p.1 * Ψ.val (a, p.2)
```

**`QuantumMechanics.FiniteHilbertSpace.onSnd_val`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L102).

```lean
lemma onSnd_val (B : 𝓗[β] →ₗ[ℂ] 𝓗[β]) (Ψ : 𝓗[α × β]) (p : α × β) :
    (onSnd B Ψ).val p = ∑ b, (B (basisFun β b)).val p.2 * Ψ.val (p.1, b)
```

## C. Composition

**`QuantumMechanics.FiniteHilbertSpace.onFst_comp`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L112).

> Acting twice on the first coordinate composes the operators.

```lean
lemma onFst_comp (A A' : 𝓗[α] →ₗ[ℂ] 𝓗[α]) :
    onFst (β := β) (A ∘ₗ A') = onFst A ∘ₗ onFst A'
```

**`QuantumMechanics.FiniteHilbertSpace.onSnd_comp`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L121).

> Acting twice on the second coordinate composes the operators.

```lean
lemma onSnd_comp (B B' : 𝓗[β] →ₗ[ℂ] 𝓗[β]) :
    onSnd (α := α) (B ∘ₗ B') = onSnd B ∘ₗ onSnd B'
```

**`QuantumMechanics.FiniteHilbertSpace.onFst_comp_onSnd`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L130).

> Operators on different coordinates commute.

```lean
lemma onFst_comp_onSnd (A : 𝓗[α] →ₗ[ℂ] 𝓗[α]) (B : 𝓗[β] →ₗ[ℂ] 𝓗[β]) :
    onFst A ∘ₗ onSnd B = onSnd B ∘ₗ onFst A
```

## D. Hermiticity

**`QuantumMechanics.FiniteHilbertSpace.inner_eq_sum`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L144).

> The inner product of `𝓗[α × β]` in components.

```lean
lemma inner_eq_sum (Ψ Φ : 𝓗[α × β]) :
    ⟪Ψ, Φ⟫_ℂ = ∑ p, (starRingEnd ℂ) (Ψ.val p) * Φ.val p
```

**`QuantumMechanics.FiniteHilbertSpace.conj_val_apply_basisFun`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L150).

> Hermitian amplitudes: `conj ⟨a'|A|a⟩ = ⟨a|A|a'⟩`.

```lean
lemma conj_val_apply_basisFun {A : 𝓗[α] →ₗ[ℂ] 𝓗[α]} (hA : A.IsSymmetric) (a a' : α) :
    (starRingEnd ℂ) ((A (basisFun α a)).val a') = (A (basisFun α a')).val a
```

**`QuantumMechanics.FiniteHilbertSpace.onFst_isSymmetric`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L155).

> A hermitian operator on the first coordinate is hermitian.

```lean
lemma onFst_isSymmetric {A : 𝓗[α] →ₗ[ℂ] 𝓗[α]} (hA : A.IsSymmetric) :
    (onFst (β := β) A).IsSymmetric
```

**`QuantumMechanics.FiniteHilbertSpace.onSnd_isSymmetric`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean#L168).

> A hermitian operator on the second coordinate is hermitian.

```lean
lemma onSnd_isSymmetric {B : 𝓗[β] →ₗ[ℂ] 𝓗[β]} (hB : B.IsSymmetric) :
    (onSnd (α := α) B).IsSymmetric
```

## Depends on

- [The Hilbert space of a finite target quantum mechanical system](../../../physlib/quantummechanics/hilbertspaces/finitetarget-basic.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Product.lean)
