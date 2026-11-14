---
declaration: module
origin: cited
lean: QuantumMechanics.FiniteHilbertSpace.prodVec, QuantumMechanics.FiniteHilbertSpace.prodVec_val, QuantumMechanics.FiniteHilbertSpace.inner_prodVec, QuantumMechanics.FiniteHilbertSpace.norm_prodVec, QuantumMechanics.FiniteHilbertSpace.norm_prodVec_eq_one, QuantumMechanics.FiniteHilbertSpace.prodVec_sub_left, QuantumMechanics.FiniteHilbertSpace.prodVec_sub_right, QuantumMechanics.FiniteHilbertSpace.prodVec_smul_left
statement: formalized
proof: formalized
---

# Product states of a product of finite targets

The module `PhyslibAlpha.QuantumMechanics.HilbertSpaces.FiniteTarget.ProductState`, [PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean): 30 declarations, 19 with a docstring.

## i. Overview

> The product state `(ψ ⊗ φ) (a, b) = ψ a φ b` of two unit vectors describes two uncorrelated
> coordinates. An observable acting on one coordinate only sees that coordinate: its mean, its
> variance, its covariance with another such observable and their centered Gram defect are those
> of the factor state.
>
> More generally, a family of vectors `v i` on `𝓗[α]`, indexed by a finite type `ι`, has the
> product vector `(⊗ i, v i) k = ∏ i, v i (k i)` on `𝓗[ι → α]`, describing independently prepared
> copies of a system; inner products and norms of product vectors are products.

## ii. Key results

> - `prodVec` : the product vector `ψ ⊗ φ`, of norm `‖ψ‖ ‖φ‖` by `norm_prodVec`.
> - `onFst_prodVec`, `onSnd_prodVec` : `(A ⊗ 1) (ψ ⊗ φ) = A ψ ⊗ φ` and `(1 ⊗ B) (ψ ⊗ φ) = ψ ⊗ B φ`.
> - `onFstObservable`, `onSndObservable` : an observable acting on one coordinate.
> - `variance_onFstObservable`, `covariance_onFstObservable`,
>   `centeredGramDefect_onFstObservable` : the statistics of the first coordinate.
> - `variance_onSndObservable`, `covariance_onSndObservable`,
>   `centeredGramDefect_onSndObservable` : the statistics of the second coordinate.
> - `covariance_onFstObservable_onSndObservable` : the two coordinates are uncorrelated.
> - `piProdVec` : the product vector `⊗ i, v i` of a finite family.
> - `inner_piProdVec`, `norm_piProdVec`, `norm_piProdVec_eq_one` : `⟪⊗ v, ⊗ w⟫ = ∏ i, ⟪v i, w i⟫`,
>   `‖⊗ v‖ = ∏ i, ‖v i‖`, and a product of unit vectors is a unit vector.

## iv. References

> * None.

## A. Product vectors

**`QuantumMechanics.FiniteHilbertSpace.prodVec`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L74).

> The product vector `(ψ ⊗ φ) (a, b) = ψ a φ b`.

```lean
noncomputable def prodVec (ψ : 𝓗[α]) (φ : 𝓗[β]) : 𝓗[α × β]
```

**`QuantumMechanics.FiniteHilbertSpace.prodVec_val`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L77).

```lean
lemma prodVec_val (ψ : 𝓗[α]) (φ : 𝓗[β]) (p : α × β) :
    (prodVec ψ φ).val p = ψ.val p.1 * φ.val p.2
```

**`QuantumMechanics.FiniteHilbertSpace.inner_prodVec`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L81).

> `⟪ψ ⊗ φ, ψ' ⊗ φ'⟫ = ⟪ψ, ψ'⟫ ⟪φ, φ'⟫`.

```lean
lemma inner_prodVec (ψ ψ' : 𝓗[α]) (φ φ' : 𝓗[β]) :
    ⟪prodVec ψ φ, prodVec ψ' φ'⟫_ℂ = ⟪ψ, ψ'⟫_ℂ * ⟪φ, φ'⟫_ℂ
```

**`QuantumMechanics.FiniteHilbertSpace.norm_prodVec`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L90).

> `‖ψ ⊗ φ‖ = ‖ψ‖ ‖φ‖`.

```lean
lemma norm_prodVec (ψ : 𝓗[α]) (φ : 𝓗[β]) : ‖prodVec ψ φ‖ = ‖ψ‖ * ‖φ‖
```

**`QuantumMechanics.FiniteHilbertSpace.norm_prodVec_eq_one`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L97).

> The product of two unit vectors is a unit vector.

```lean
lemma norm_prodVec_eq_one {ψ : 𝓗[α]} {φ : 𝓗[β]} (hψ : ‖ψ‖ = 1) (hφ : ‖φ‖ = 1) :
    ‖prodVec ψ φ‖ = 1
```

**`QuantumMechanics.FiniteHilbertSpace.prodVec_sub_left`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L101).

```lean
lemma prodVec_sub_left (ψ ψ' : 𝓗[α]) (φ : 𝓗[β]) :
    prodVec (ψ - ψ') φ = prodVec ψ φ - prodVec ψ' φ
```

**`QuantumMechanics.FiniteHilbertSpace.prodVec_sub_right`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L106).

```lean
lemma prodVec_sub_right (ψ : 𝓗[α]) (φ φ' : 𝓗[β]) :
    prodVec ψ (φ - φ') = prodVec ψ φ - prodVec ψ φ'
```

**`QuantumMechanics.FiniteHilbertSpace.prodVec_smul_left`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L111).

```lean
lemma prodVec_smul_left (r : ℝ) (ψ : 𝓗[α]) (φ : 𝓗[β]) :
    prodVec (r • ψ) φ = r • prodVec ψ φ
```

**`QuantumMechanics.FiniteHilbertSpace.prodVec_smul_right`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L116).

```lean
lemma prodVec_smul_right (r : ℝ) (ψ : 𝓗[α]) (φ : 𝓗[β]) :
    prodVec ψ (r • φ) = r • prodVec ψ φ
```

**`QuantumMechanics.FiniteHilbertSpace.onFst_prodVec`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L122).

> `(A ⊗ 1) (ψ ⊗ φ) = A ψ ⊗ φ`.

```lean
lemma onFst_prodVec (A : 𝓗[α] →ₗ[ℂ] 𝓗[α]) (ψ : 𝓗[α]) (φ : 𝓗[β]) :
    onFst A (prodVec ψ φ) = prodVec (A ψ) φ
```

**`QuantumMechanics.FiniteHilbertSpace.onSnd_prodVec`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L129).

> `(1 ⊗ B) (ψ ⊗ φ) = ψ ⊗ B φ`.

```lean
lemma onSnd_prodVec (B : 𝓗[β] →ₗ[ℂ] 𝓗[β]) (ψ : 𝓗[α]) (φ : 𝓗[β]) :
    onSnd B (prodVec ψ φ) = prodVec ψ (B φ)
```

## B. Observables on one coordinate

**`QuantumMechanics.FiniteHilbertSpace.onFstObservable`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L142).

> An observable of the first coordinate as an observable of `𝓗[α × β]`.

```lean
noncomputable def onFstObservable (a : Observable (𝓗[α] →L[ℂ] 𝓗[α])) :
    Observable (𝓗[α × β] →L[ℂ] 𝓗[α × β])
```

**`QuantumMechanics.FiniteHilbertSpace.onSndObservable`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L149).

> An observable of the second coordinate as an observable of `𝓗[α × β]`.

```lean
noncomputable def onSndObservable (b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    Observable (𝓗[α × β] →L[ℂ] 𝓗[α × β])
```

## C. Statistics of the first coordinate

**`QuantumMechanics.FiniteHilbertSpace.expectation_onFstObservable`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L164).

> The mean of the first coordinate is that of `ψ`.

```lean
lemma expectation_onFstObservable (a : Observable (𝓗[α] →L[ℂ] 𝓗[α])) :
    (ofVec (norm_prodVec_eq_one hψ hφ))⟨onFstObservable a⟩ = (ofVec hψ)⟨a⟩
```

**`QuantumMechanics.FiniteHilbertSpace.fluctuation_onFstObservable`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L175).

> The fluctuation of the first coordinate is that of `ψ`, tensored with `φ`.

```lean
lemma fluctuation_onFstObservable (a : Observable (𝓗[α] →L[ℂ] 𝓗[α])) :
    (onFstObservable (β := β) a : 𝓗[α × β] →L[ℂ] 𝓗[α × β]) (prodVec ψ φ) -
        (ofVec (norm_prodVec_eq_one hψ hφ))⟨onFstObservable a⟩ • prodVec ψ φ =
      prodVec ((a : 𝓗[α] →L[ℂ] 𝓗[α]) ψ - (ofVec hψ)⟨a⟩ • ψ) φ
```

**`QuantumMechanics.FiniteHilbertSpace.variance_onFstObservable`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L182).

```lean
lemma variance_onFstObservable (a : Observable (𝓗[α] →L[ℂ] 𝓗[α])) :
    variance (ofVec (norm_prodVec_eq_one hψ hφ)) (onFstObservable a) = variance (ofVec hψ) a
```

**`QuantumMechanics.FiniteHilbertSpace.covariance_onFstObservable`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L186).

```lean
lemma covariance_onFstObservable (a b : Observable (𝓗[α] →L[ℂ] 𝓗[α])) :
    covariance (ofVec (norm_prodVec_eq_one hψ hφ)) (onFstObservable a) (onFstObservable b) =
      covariance (ofVec hψ) a b
```

**`QuantumMechanics.FiniteHilbertSpace.centeredGramDefect_onFstObservable`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L195).

```lean
lemma centeredGramDefect_onFstObservable (a b : Observable (𝓗[α] →L[ℂ] 𝓗[α])) :
    centeredGramDefect (ofVec (norm_prodVec_eq_one hψ hφ)) (onFstObservable a)
      (onFstObservable b) = centeredGramDefect (ofVec hψ) a b
```

## D. Statistics of the second coordinate

**`QuantumMechanics.FiniteHilbertSpace.expectation_onSndObservable`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L210).

> The mean of the second coordinate is that of `φ`.

```lean
lemma expectation_onSndObservable (b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    (ofVec (norm_prodVec_eq_one hψ hφ))⟨onSndObservable b⟩ = (ofVec hφ)⟨b⟩
```

**`QuantumMechanics.FiniteHilbertSpace.fluctuation_onSndObservable`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L221).

> The fluctuation of the second coordinate is `ψ` tensored with that of `φ`.

```lean
lemma fluctuation_onSndObservable (b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    (onSndObservable (α := α) b : 𝓗[α × β] →L[ℂ] 𝓗[α × β]) (prodVec ψ φ) -
        (ofVec (norm_prodVec_eq_one hψ hφ))⟨onSndObservable b⟩ • prodVec ψ φ =
      prodVec ψ ((b : 𝓗[β] →L[ℂ] 𝓗[β]) φ - (ofVec hφ)⟨b⟩ • φ)
```

**`QuantumMechanics.FiniteHilbertSpace.variance_onSndObservable`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L228).

```lean
lemma variance_onSndObservable (b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    variance (ofVec (norm_prodVec_eq_one hψ hφ)) (onSndObservable b) = variance (ofVec hφ) b
```

**`QuantumMechanics.FiniteHilbertSpace.covariance_onSndObservable`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L232).

```lean
lemma covariance_onSndObservable (a b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    covariance (ofVec (norm_prodVec_eq_one hψ hφ)) (onSndObservable a) (onSndObservable b) =
      covariance (ofVec hφ) a b
```

**`QuantumMechanics.FiniteHilbertSpace.centeredGramDefect_onSndObservable`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L241).

```lean
lemma centeredGramDefect_onSndObservable (a b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    centeredGramDefect (ofVec (norm_prodVec_eq_one hψ hφ)) (onSndObservable a)
      (onSndObservable b) = centeredGramDefect (ofVec hφ) a b
```

## E. Different coordinates are uncorrelated

**`QuantumMechanics.FiniteHilbertSpace.inner_fluctuation`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L256).

> The fluctuation vector of an observable is orthogonal to the state.

```lean
lemma inner_fluctuation {γ : Type*} [Fintype γ] [DecidableEq γ] {χ : 𝓗[γ]} (hχ : ‖χ‖ = 1)
    (c : Observable (𝓗[γ] →L[ℂ] 𝓗[γ])) :
    ⟪χ, (c : 𝓗[γ] →L[ℂ] 𝓗[γ]) χ - (ofVec hχ)⟨c⟩ • χ⟫_ℂ = 0
```

**`QuantumMechanics.FiniteHilbertSpace.covariance_onFstObservable_onSndObservable`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L267).

> In a product state, an observable of the first coordinate and one of the second are
> uncorrelated.

```lean
lemma covariance_onFstObservable_onSndObservable (a : Observable (𝓗[α] →L[ℂ] 𝓗[α]))
    (b : Observable (𝓗[β] →L[ℂ] 𝓗[β])) :
    covariance (ofVec (norm_prodVec_eq_one hψ hφ)) (onFstObservable a) (onSndObservable b) = 0
```

## F. Product vectors of finite families

**`QuantumMechanics.FiniteHilbertSpace.piProdVec`**, a def, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L286).

> The product vector `(⊗ i, v i) k = ∏ i, v i (k i)` of a finite family of vectors,
> describing independently prepared copies of a system.

```lean
noncomputable def piProdVec (v : ι → 𝓗[α]) : 𝓗[ι → α]
```

**`QuantumMechanics.FiniteHilbertSpace.piProdVec_val`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L290).

> The components of a product vector are the products of the components.

```lean
lemma piProdVec_val (v : ι → 𝓗[α]) (k : ι → α) :
    (piProdVec v).val k = ∏ i, (v i).val (k i)
```

**`QuantumMechanics.FiniteHilbertSpace.inner_piProdVec`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L294).

> `⟪⊗ v, ⊗ w⟫ = ∏ i, ⟪v i, w i⟫`.

```lean
lemma inner_piProdVec (v w : ι → 𝓗[α]) :
    ⟪piProdVec v, piProdVec w⟫_ℂ = ∏ i, ⟪v i, w i⟫_ℂ
```

**`QuantumMechanics.FiniteHilbertSpace.norm_piProdVec`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L301).

> `‖⊗ v‖ = ∏ i, ‖v i‖`.

```lean
lemma norm_piProdVec (v : ι → 𝓗[α]) : ‖piProdVec v‖ = ∏ i, ‖v i‖
```

**`QuantumMechanics.FiniteHilbertSpace.norm_piProdVec_eq_one`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean#L309).

> The product of unit vectors is a unit vector.

```lean
lemma norm_piProdVec_eq_one {v : ι → 𝓗[α]} (hv : ∀ i, ‖v i‖ = 1) : ‖piProdVec v‖ = 1
```

## Depends on

- [Uncertainty relations](../../probabilistictheory/cstaralgebra/uncertainty.md)
- [Vector states](../../probabilistictheory/hilbertspace/part-01/state-vector.md)
- [Operators on the Hilbert space of a finite target system](finitetarget-operators.md)
- [Operators on one coordinate of a product of finite targets](finitetarget-product.md)

## Proof depends on

- [Uncertainty in vector states](../../probabilistictheory/hilbertspace/part-01/state-vectoruncertainty.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/ProductState.lean)
