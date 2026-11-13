---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.Pure.evalPCoeff, TensorSpecies.Tensor.Pure.evalPCoeff_update_self, TensorSpecies.Tensor.Pure.evalPCoeff_update_succAbove, TensorSpecies.Tensor.Pure.evalPCoeff_basisVector, TensorSpecies.Tensor.Pure.evalP, TensorSpecies.Tensor.Pure.evalP_update_add, TensorSpecies.Tensor.Pure.evalP_update_smul, TensorSpecies.Tensor.Pure.evalPMultilinear
statement: formalized
proof: formalized
---

# Evaluation of tensor indices

The module `Physlib.Relativity.Tensors.Evaluation`, [Physlib/Relativity/Tensors/Evaluation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean): 22 declarations, 13 with a docstring.

> ## The evaluation coefficient.

**`TensorSpecies.Tensor.Pure.evalPCoeff`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L41).

> Given a `i : Fin (n + 1)`, a `b : basisIdx (c i)` and a pure tensor
> `p : Pure S c`, `evalPCoeff i b p` is the `b`th component of `p i`.

```lean
noncomputable def evalPCoeff (i : Fin (n + 1)) (φ : basisIdx (c i)) (p : Pure S c) : k
```

**`TensorSpecies.Tensor.Pure.evalPCoeff_update_self`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L45).

```lean
lemma evalPCoeff_update_self (i : Fin (n + 1)) [inst : DecidableEq (Fin (n + 1))]
    (φ : basisIdx (c i)) (p : Pure S c)
    (x : V (c i)) :
    evalPCoeff i φ (p.update i x) = (b (c i)).repr x φ
```

**`TensorSpecies.Tensor.Pure.evalPCoeff_update_succAbove`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L52).

```lean
lemma evalPCoeff_update_succAbove (i : Fin (n + 1)) [inst : DecidableEq (Fin (n + 1))]
    (j : Fin n)
    (φ : basisIdx (c i)) (p : Pure S c)
    (x : V (c (i.succAbove j))) :
    evalPCoeff i φ (p.update (i.succAbove j) x) = evalPCoeff i φ p
```

**`TensorSpecies.Tensor.Pure.evalPCoeff_basisVector`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L59).

```lean
lemma evalPCoeff_basisVector (i : Fin (n + 1)) (φ : basisIdx (c i)) (b' : ComponentIdx (S := S) c) :
    evalPCoeff i φ (Pure.basisVector c b') = if b' i = φ then (1 : k) else 0
```

## Evaluation for a pure tensor.

**`TensorSpecies.Tensor.Pure.evalP`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L72).

> Given a `i : Fin (n + 1)`, a `φ : basisIdx (c i)` and a pure tensor
> `p : Pure S c`, `evalP i φ p` is the tensor formed by evaluating the `i`th index
> of `p` at `φ`.

```lean
noncomputable def evalP (i : Fin (n + 1)) (φ : basisIdx (c i)) (p : Pure S c) :
  Tensor S (c ∘ i.succAbove)
```

**`TensorSpecies.Tensor.Pure.evalP_update_add`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L76).

```lean
lemma evalP_update_add [inst : DecidableEq (Fin (n + 1))] (i j : Fin (n + 1))
    (φ : basisIdx (c i)) (p : Pure S c)
    (x y: V (c j)) :
    evalP i φ (p.update j (x + y)) =
    evalP i φ (p.update j x) + evalP i φ (p.update j y)
```

**`TensorSpecies.Tensor.Pure.evalP_update_smul`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L87).

```lean
lemma evalP_update_smul [inst : DecidableEq (Fin (n + 1))] (i j : Fin (n + 1))
    (φ : basisIdx (c i)) (p : Pure S c)
    (r : k)
    (x : V (c j)) :
    evalP i φ (p.update j (r • x)) =
    r • evalP i φ (p.update j x)
```

## Evaluation for a pure tensor as multilinear map.

**`TensorSpecies.Tensor.Pure.evalPMultilinear`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L105).

> The multi-linear map formed by evaluation of an index of pure tensors.

```lean
noncomputable def evalPMultilinear {n : ℕ} {c : Fin (n + 1)→ C}
    (i : Fin (n + 1)) (φ : basisIdx (c i)) :
    MultilinearMap k (fun i => V (c i))
      (S.Tensor (c ∘ i.succAbove))
```

**`TensorSpecies.Tensor.evalT`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L125).

> Evaluation of a tensor at a given index and basis element.

```lean
noncomputable def evalT {n : ℕ} {c : Fin (n + 1) → C} (i : Fin (n + 1))
      (φ : basisIdx (c i)) :
    Tensor S c →ₗ[k] Tensor S (c ∘ i.succAbove)
```

**`TensorSpecies.Tensor.evalT_pure`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L131).

```lean
lemma evalT_pure {n : ℕ} {c : Fin (n + 1) → C} (i : Fin (n + 1))
    (φ : basisIdx (c i)) (p : Pure S c) :
    evalT i φ p.toTensor = Pure.evalP i φ p
```

**`TensorSpecies.Tensor.evalT_basis`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L138).

```lean
lemma evalT_basis {n : ℕ} {c : Fin (n + 1) → C} (i : Fin (n + 1))
    (b : ComponentIdx c) (x : basisIdx (c i)) :
    evalT i x (basis (S := S) c b) = if b i = x then basis (c ∘ i.succAbove)
      (fun j => b (i.succAbove j)) else 0
```

## The commutation of evaluation with permutations.

**`TensorSpecies.Tensor.evalT_permT`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L157).

> Commuting evaluation with permutations.

```lean
lemma evalT_permT {n m : ℕ} {c : Fin (n + 1) → C} {c' : Fin (m + 1) → C}
    {σ : Fin (n + 1) → Fin (m + 1)}
    (h : IsReindexing c' c  σ) (i : Fin (n + 1)) (x : basisIdx (c i)) (t : Tensor S c') :
    evalT i x (permT _ h t) = permT _ (h.succAbove i)
      (evalT (σ i) (basisIdxCongr (by simp [h.2]) x) t)
```

## The commutation of evaluation with evaluation.

**`TensorSpecies.Tensor.evalT_evalT_basis`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L192).

> Commutation of two evaluations on a tensor basis vector.

```lean
lemma evalT_evalT_basis {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (k1 : Fin (n + 1 + 1)) (k2 : Fin (n + 1)) (φ1 : basisIdx (c k1))
    (φ2 : basisIdx ((c ∘ k1.succAbove) k2)) (ψ : ComponentIdx (S := S) c) :
    evalT k2 φ2 (evalT k1 φ1 (basis (S := S) c ψ)) =
      permT id (IsReindexing.succAbove_succAbove_comm k1 k2)
        (evalT (k2.predAbove k1)
          (basisIdxCongr
            (congrArg c (Fin.succAbove_succAbove_predAbove k1 k2).symm) φ1)
          (evalT (k1.succAbove k2) φ2 (basis (S := S) c ψ)))
```

**`TensorSpecies.Tensor.evalT_evalT`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L230).

> Evaluating two tensor indices commutes, up to the canonical reindexing
> identifying the two possible orders in which the indices are removed.

```lean
lemma evalT_evalT {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (k1 : Fin (n + 1 + 1)) (k2 : Fin (n + 1)) (φ1 : basisIdx (c k1))
    (φ2 : basisIdx ((c ∘ k1.succAbove) k2)) (t : Tensor S c) :
    evalT k2 φ2 (evalT k1 φ1 t) =
      permT id (IsReindexing.succAbove_succAbove_comm k1 k2)
        (evalT (k2.predAbove k1)
          (basisIdxCongr
            (congrArg c (Fin.succAbove_succAbove_predAbove k1 k2).symm) φ1)
          (evalT (k1.succAbove k2) φ2 t))
```

## The commutation of evaluation with contraction.

**`TensorSpecies.Tensor.contrT_evalT`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L255).

> Commuting evaluation with contraction. Evaluating index `k` and then contracting the
> pair `i j` equals contracting the corresponding pair `k.succAbove i`, `k.succAbove j` and
> then evaluating the residual index, up to the identity reindexing
> `IsReindexing.succAbove_succSuccAbove_comm`.

```lean
lemma contrT_evalT {n : ℕ} {c : Fin (n + 1 + 1 + 1) → C}
    (k : Fin (n + 1 + 1 + 1)) (i j : Fin (n + 1 + 1)) (φ : basisIdx (c k))
    (hij : i ≠ j ∧ S.τ ((c ∘ k.succAbove) i) = (c ∘ k.succAbove) j) (t : Tensor S c) :
    contrT n i j hij (evalT k φ t) =
    permT id (.succAbove_succSuccAbove_comm k i j hij.1)
      (evalT (Fin.predPredAbove (k.succAbove i) (k.succAbove j) (by simp [hij.1]) k (by simp))
        (basisIdxCongr (by simp) φ)
        (contrT (n + 1) (k.succAbove i) (k.succAbove j) ⟨by simp [hij.1], hij.2⟩ t))
```

## The commutation of evaluation with products.

**`TensorSpecies.Tensor.evalT_prodT_right`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L313).

> Evaluating an index in the right factor of a tensor product commutes with forming the
> product, up to the identity reindexing which identifies the two ways of removing that
> index from the appended color list.

```lean
lemma evalT_prodT_right {n n1 : ℕ} {c : Fin n → C} {c1 : Fin (n1 + 1) → C}
    (i : Fin (n1 + 1)) (x : basisIdx (c1 i)) (t : Tensor S c) (t1 : Tensor S c1) :
    prodT t (evalT i x t1) =
    permT id (IsReindexing.append_succAbove_natAdd (n := n) (n1 := n1) i)
      (evalT (Fin.natAdd (m := n1 + 1) n i) (basisIdxCongr (by simp) x) (prodT t t1))
```

## Other properties of evaluation

**`TensorSpecies.Tensor.evalT_basis_single`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L384).

> Evaluating the single-index basis tensor `basis ![c] (single.symm b)` at the index `x`
> yields the field element `1` if `b = x` (transported across `![c] 0 = c`) and `0` otherwise:
> evaluation of a one-index basis tensor is the Kronecker delta.

```lean
lemma evalT_basis_single {c : C} (b : basisIdx c) (x : basisIdx (![c] 0)) :
    (evalT 0 x (basis (S := S) ![c] (ComponentIdx.single.symm b))).toScalar =
    if basisIdxCongr (by simp) b =  x then 1 else 0
```

**`TensorSpecies.Tensor.eq_sum_evalT_of_single_tensor_basis`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L396).

> Basis expansion of a one-index tensor: every `t : Tensor S ![c]` is the sum over basis
> indices `i` of its evaluation coefficient `toScalar (evalT 0 i t)` times the corresponding
> basis tensor.

```lean
lemma eq_sum_evalT_of_single_tensor_basis {c : C} (t : Tensor S ![c]) :
    t = ∑ i, toScalar (evalT 0 i t) • basis ![c] (ComponentIdx.single.symm
      (basisIdxCongr (by simp) i))
```

**`TensorSpecies.Tensor.eq_sum_evalT`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L413).

> Reconstruction of a tensor from the evaluations of its last index: every `t : Tensor S c`
> is the sum over basis indices `i` of the evaluation `evalT (Fin.last n) i t` tensored with
> the basis covector `basis ![c (Fin.last n)] (single.symm i)`, with the appended index
> permuted back into the last slot.

```lean
lemma eq_sum_evalT {n : ℕ} {c : Fin (n + 1) → C} (t : Tensor S c) :
    t = ∑ i, permT id (IsReindexing.append_succ_last c) (prodT (evalT (Fin.last n) i t)
      (basis ![c (Fin.last n)] (ComponentIdx.single.symm i)))
```

**`TensorSpecies.Tensor.eq_sum_evalT_zero`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L447).

> Reconstruction of a tensor from the evaluations of its first index: every `t : Tensor S c`
> is the sum over basis indices `i` of the basis covector `basis ![c 0] (single.symm i)` tensored
> with the evaluation `evalT 0 i t`, with the prepended index permuted back into the first slot.
> This is the first-index analogue of `eq_sum_evalT`.

```lean
lemma eq_sum_evalT_zero {n : ℕ} {c : Fin (n + 1) → C} (t : Tensor S c) :
    t = ∑ i, permT _ (IsReindexing.append_of_first c)
    (prodT (basis ![c 0] (ComponentIdx.single.symm i)) (evalT 0 i t))
```

**`TensorSpecies.Tensor.ext_of_evalT`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L480).

```lean
lemma ext_of_evalT {n : ℕ} {c : Fin (n + 1) → C} (t1 t2 : Tensor S c)
    (h : ∀ i φ, evalT i φ t1 = evalT i φ t2) :
    t1 = t2
```

**`TensorSpecies.Tensor.ext_of_evalT_index`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean#L488).

```lean
lemma ext_of_evalT_index {n : ℕ} {c : Fin (n + 1) → C} {t1 t2 : Tensor S c}
    (i : Fin (n + 1)) (h : ∀ φ, evalT i φ t1 = evalT i φ t2) :
    t1 = t2
```

## Depends on

- [Component indices for one-index tensors](../part-02/componentidx-single.md)
- [Contractions on tensors](../part-02/contraction-basic.md)
- [The product of tensors](product.md)

## Proof depends on

- [Contractions on basis tensors](../part-02/contraction-basis.md)

## Sources

- [Physlib/Relativity/Tensors/Evaluation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Evaluation.lean)
