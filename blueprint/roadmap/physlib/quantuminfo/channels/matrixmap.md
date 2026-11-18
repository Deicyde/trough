---
declaration: module
origin: cited
lean: MatrixMap.map_choi_inv, MatrixMap.choi_map_inv, MatrixMap.choi_matrix_inj, MatrixMap.toMatrix_comp, MatrixMap.kron_def, MatrixMap.kron_comp_distrib, MatrixMap.kron_map_of_kron_state, MatrixMap.piProd_comp
statement: formalized
proof: formalized
---

# Linear maps of matrices

The module `QuantumInfo.Channels.MatrixMap`, [QuantumInfo/Channels/MatrixMap.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean): 34 declarations, 18 with a docstring, 8 listed as significant.

> This file works with `MatrixMap`s, that is, linear maps from square matrices to square matrices.
> Although this is just a shorthand for `Matrix A A R →ₗ[R] Matrix B B R`, there are several
> concepts that specifically make sense in this context.
>
>  * `toMatrix` is the rectangular "transfer matrix", where matrix multiplication commutes with map
>    composition.
>  * `choi_matrix` is the square "Choi matrix", see `MatrixMap.choi_PSD_iff_CP_map` for example usage
>  * `kron` is the Kronecker product of matrix maps
>  * `IsTracePreserving` states the trace of the output is always equal to the trace of the input.
>
> We provide simp lemmas for relating these facts, prove basic facts e.g. composition and identity,
> and some facts about `IsTracePreserving` maps.

**`MatrixMap`**, an abbrev, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L30).

> A `MatrixMap` is a linear map between squares matrices of size A to size B, over R.

```lean
abbrev MatrixMap (A B R : Type*) [Semiring R]
```

**`MatrixMap.id`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L42).

> Alias of LinearMap.id, but specifically as a MatrixMap.

```lean
def id : MatrixMap A A R
```

**`MatrixMap.choi_matrix`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L47).

> Choi matrix of a given linear matrix map. Note that this is defined even for things that
> aren't CPTP, it's just rarely talked about in those contexts. This is the inverse of
> `MatrixMap.of_choi_matrix`. Compare with `MatrixMap.toMatrix`, which gives the transfer matrix.

```lean
def choi_matrix (M : MatrixMap A B R) : Matrix (B × A) (B × A) R
```

**`MatrixMap.of_choi_matrix`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L53).

> Given the Choi matrix, generate the corresponding R-linear map between matrices as a
> MatrixMap. This is the inverse of `MatrixMap.choi_matrix`.

```lean
def of_choi_matrix (M : Matrix (B × A) (B × A) R) : MatrixMap A B R
```

**`MatrixMap.map_choi_inv`**, a theorem, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L63). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Proves that `MatrixMap.of_choi_matrix` and `MatrixMap.choi_matrix` inverses.

```lean
theorem map_choi_inv (M : Matrix (B × A) (B × A) R) : choi_matrix (of_choi_matrix M) = M
```

**`MatrixMap.choi_map_inv`**, a theorem, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L70). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Proves that `MatrixMap.choi_matrix` and `MatrixMap.of_choi_matrix` inverses.

```lean
theorem choi_map_inv (M : MatrixMap A B R) : of_choi_matrix (choi_matrix M) = M
```

**`MatrixMap.choi_matrix_inj`**, a theorem, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L86). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The correspondence induced by `MatrixMap.of_choi_matrix` is injective.

```lean
theorem choi_matrix_inj : Function.Injective (@choi_matrix A B R _ _)
```

**`MatrixMap.choi_equiv`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L95).

> The linear equivalence between linear maps of matrices,and Choi matrices.

```lean
def choi_equiv : MatrixMap A B R ≃ₗ[R] Matrix (B × A) (B × A) R
```

**`MatrixMap.toMatrix`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L105).

> The linear equivalence between MatrixMap's and transfer matrices on a larger space.
> Compare with `MatrixMap.choi_matrix`, which gives the Choi matrix instead of the transfer matrix.

```lean
noncomputable def toMatrix [Fintype B] : MatrixMap A B R ≃ₗ[R] Matrix (B × B) (A × A) R
```

**`MatrixMap.toMatrix_comp`**, a theorem, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L109). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Multiplication of transfer matrices, `MatrixMap.toMatrix`, is equivalent to composition of maps.

```lean
theorem toMatrix_comp [Fintype B] [Fintype C] [DecidableEq B] (M₁ : MatrixMap A B R) (M₂ : MatrixMap B C R) : toMatrix (M₂ ∘ₗ M₁) = (toMatrix M₂) * (toMatrix M₁)
```

**`MatrixMap.of_kraus`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L121).

> Construct a matrix map out of families of matrices M N : Σ → Matrix B A R
> indexed by κ via X ↦ ∑ k : κ, (M k) * X * (N k)ᴴ

```lean
def of_kraus (M N : κ → Matrix B A R) : MatrixMap A B R
```

**`MatrixMap.exists_kraus`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L134).

```lean
lemma exists_kraus (Φ : MatrixMap A B R) :
    ∃ r : ℕ, ∃ (M N : Fin r → Matrix B A R), Φ = of_kraus M N
```

**`MatrixMap.submatrix`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L175).

> The `MatrixMap` corresponding to applying a `submatrix` operation on each side.

```lean
def submatrix (f : B → A) : MatrixMap A B R
```

**`MatrixMap.submatrix_id`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L181).

```lean
lemma submatrix_id : submatrix R _root_.id = id A R
```

**`MatrixMap.submatrix_comp`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L185).

```lean
lemma submatrix_comp (f : C → B) (g : B → A) :
    submatrix R f ∘ₗ submatrix R g = submatrix R (g ∘ f)
```

**`MatrixMap.kron`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L199).

> The Kronecker product of MatrixMaps. Defined here using `TensorProduct.map M₁ M₂`, with
> appropriate reindexing operations and `LinearMap.toMatrix`/`Matrix.toLin`. Notation `⊗ₖₘ`.

```lean
noncomputable def kron [CommSemiring R] (M₁ : MatrixMap A B R) (M₂ : MatrixMap C D R) : MatrixMap (A × C) (B × D) R
```

**`MatrixMap.kron_def`**, a theorem, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L214). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The extensional definition of the Kronecker product `MatrixMap.kron`, in terms of the entries of
> its image.

```lean
theorem kron_def [CommSemiring R] (M₁ : MatrixMap A B R) (M₂ : MatrixMap C D R) (M : Matrix (A × C) (A × C) R) :
    (M₁ ⊗ₖₘ M₂) M (b₁, d₁) (b₂, d₂) = ∑ a₁, ∑ a₂, ∑ c₁, ∑ c₂,
      (M₁ (Matrix.single a₁ a₂ 1) b₁ b₂) * (M₂ (Matrix.single c₁ c₂ 1) d₁ d₂) * (M (a₁, c₁) (a₂, c₂))
```

**`MatrixMap.add_kron`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L275).

```lean
lemma add_kron (ML₁ ML₂ : MatrixMap A B R) (MR : MatrixMap C D R) : (ML₁ + ML₂) ⊗ₖₘ MR = ML₁ ⊗ₖₘ MR + ML₂ ⊗ₖₘ MR
```

**`MatrixMap.kron_add`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L278).

```lean
lemma kron_add (ML : MatrixMap A B R) (MR₁ MR₂ : MatrixMap C D R) : ML ⊗ₖₘ (MR₁ + MR₂) = ML ⊗ₖₘ MR₁ + ML ⊗ₖₘ  MR₂
```

**`MatrixMap.smul_kron`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L281).

```lean
lemma smul_kron (r : R) (ML : MatrixMap A B R) (MR : MatrixMap C D R) : (r • ML) ⊗ₖₘ MR = r • (ML ⊗ₖₘ MR)
```

**`MatrixMap.kron_smul`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L284).

```lean
lemma kron_smul (r : R) (ML : MatrixMap A B R) (MR : MatrixMap C D R) : ML ⊗ₖₘ (r • MR) = r • (ML ⊗ₖₘ MR)
```

**`MatrixMap.zero_kron`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L288).

```lean
lemma zero_kron (MR : MatrixMap C D R) : (0 : MatrixMap A B R) ⊗ₖₘ MR = 0
```

**`MatrixMap.kron_zero`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L292).

```lean
lemma kron_zero (ML : MatrixMap A B R) : ML ⊗ₖₘ (0 : MatrixMap C D R) = 0
```

**`MatrixMap.kron_id_id`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L296).

```lean
lemma kron_id_id : (id A R ⊗ₖₘ id B R) = id (A × B) R
```

**`MatrixMap.kron_comp_distrib`**, a theorem, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L303). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For maps L₁, L₂, R₁, and R₂, the product (L₂ ∘ₗ L₁) ⊗ₖₘ (R₂ ∘ₗ R₁) = (L₂ ⊗ₖₘ R₂) ∘ₗ (L₁ ⊗ₖₘ R₁)

```lean
theorem kron_comp_distrib (L₁ : MatrixMap Dl₁ Dl₂ R) (L₂ : MatrixMap Dl₂ Dl₃ R) (R₁ : MatrixMap Dr₁ Dr₂ R)
    (R₂ : MatrixMap Dr₂ Dr₃ R) : (L₂ ∘ₗ L₁) ⊗ₖₘ (R₂ ∘ₗ R₁) = (L₂ ⊗ₖₘ R₂) ∘ₗ (L₁ ⊗ₖₘ R₁)
```

**`MatrixMap.kron_map_of_kron_state`**, a theorem, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L318). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The operational definition of the Kronecker product `MatrixMap.kron`, that it maps a Kronecker
> product of inputs to the Kronecker product of outputs. It is the unique bilinear map doing so.

```lean
theorem kron_map_of_kron_state [CommRing R] (M₁ : MatrixMap A B R) (M₂ : MatrixMap C D R) (MA : Matrix A A R) (MC : Matrix C C R) : (M₁ ⊗ₖₘ M₂) (MA ⊗ₖ MC) = (M₁ MA) ⊗ₖ (M₂ MC)
```

**`MatrixMap.choi_matrix_state_rep`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L351).

```lean
lemma choi_matrix_state_rep {B : Type*} [Fintype B] [Nonempty A] (M : MatrixMap A B ℂ) :
    M.choi_matrix = (↑(Fintype.card (α := A)) : ℂ) • (M ⊗ₖₘ (LinearMap.id : MatrixMap A A ℂ)) (MState.pure (Ket.MES A)).m
```

**`MatrixMap.submatrix_kron_submatrix`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L377).

```lean
lemma submatrix_kron_submatrix [CommSemiring R] (f : B → A) (g : D → C) :
    submatrix R f ⊗ₖₘ submatrix R g = submatrix R (Prod.map f g)
```

**`MatrixMap.submatrix_kron_id`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L383).

```lean
lemma submatrix_kron_id [CommSemiring R] (f : B → A) :
    submatrix R f ⊗ₖₘ id C R = submatrix R (Prod.map f _root_.id)
```

**`MatrixMap.id_kron_submatrix`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L387).

```lean
lemma id_kron_submatrix [CommSemiring R] (f : B → A) :
    id C R ⊗ₖₘ submatrix R f = submatrix R (Prod.map _root_.id f)
```

**`MatrixMap.piProd`**, a def, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L401).

> Finite Pi-type tensor product of MatrixMaps. Defined as `PiTensorProduct.tprod` of the
> underlying Linear maps. Notation `⨂ₜₘ[R] i, f i`, eventually.

```lean
noncomputable def piProd (Λi : ∀ i, MatrixMap (dI i) (dO i) R) : MatrixMap (∀i, dI i) (∀i, dO i) R
```

**`MatrixMap.choi_matrix_piProd`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L412).

```lean
lemma choi_matrix_piProd (Λi : ∀ i, MatrixMap (dI i) (dO i) R) :
    (MatrixMap.piProd Λi).choi_matrix =
      Matrix.reindex
        (Equiv.arrowProdEquivProdArrow ι dO dI)
        (Equiv.arrowProdEquivProdArrow ι dO dI)
        (Matrix.piProd (fun i => (Λi i).choi_matrix))
```

**`MatrixMap.piProd_comp`**, a theorem, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L437). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Composition of `MatrixMap.piProd` maps distributes over the tensor product.

```lean
theorem piProd_comp
  {d₁ d₂ d₃ : ι → Type*}
  [∀ i, Fintype (d₁ i)] [∀ i, DecidableEq (d₁ i)]
  [∀ i, Fintype (d₂ i)] [∀ i, DecidableEq (d₂ i)]
  [∀ i, Fintype (d₃ i)] [∀ i, DecidableEq (d₃ i)]
  (Λ₁ : ∀ i, MatrixMap (d₁ i) (d₂ i) R) (Λ₂ : ∀ i, MatrixMap (d₂ i) (d₃ i) R) :
    piProd (fun i ↦ (Λ₂ i) ∘ₗ (Λ₁ i)) = (piProd Λ₂) ∘ₗ (piProd Λ₁)
```

**`MatrixMap.piProd_id`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean#L447).

```lean
lemma piProd_id :
    piProd (fun i ↦ (LinearMap.id : MatrixMap (dI i) (dI i) R)) = LinearMap.id
```

## Depends on

- [QuantumInfo.States.Mixed.MState](../states/mixed/mstate.md)

## Sources

- [QuantumInfo/Channels/MatrixMap.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/MatrixMap.lean)
