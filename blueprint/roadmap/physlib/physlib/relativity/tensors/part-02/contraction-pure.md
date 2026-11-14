---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.Pure.dropPair, TensorSpecies.Tensor.Pure.dropPair_equivariant, TensorSpecies.Tensor.Pure.dropPair_symm, TensorSpecies.Tensor.Pure.dropPair_comm, TensorSpecies.Tensor.Pure.dropPair_update_fst, TensorSpecies.Tensor.Pure.dropPair_update_snd, TensorSpecies.Tensor.Pure.dropPair_update_succSuccAbove, TensorSpecies.Tensor.Pure.dropPair_permP
statement: formalized
proof: formalized
---

# Contractions on pure tensors

The module `Physlib.Relativity.Tensors.Contraction.Pure`, [Physlib/Relativity/Tensors/Contraction/Pure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean): 28 declarations, 7 with a docstring.

## Pure.contrPCoeff

## dropPair

**`TensorSpecies.Tensor.Pure.dropPair`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L46).

> Given `i j : Fin (n + 1 + 1)`, `c : Fin (n + 1 + 1) → C` and a pure tensor `p : Pure S c`,
> `dropPair i j _ p` is the tensor formed by dropping the `i`th and `j`th parts of `p`.

```lean
def dropPair (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (p : Pure S c) :
    Pure S (c ∘ succSuccAbove i j)
```

**`TensorSpecies.Tensor.Pure.dropPair_equivariant`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L51).

```lean
lemma dropPair_equivariant {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (p : Pure S c) (g : G) :
    dropPair i j hij (g • p) = g • dropPair i j hij p
```

**`TensorSpecies.Tensor.Pure.dropPair_symm`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L58).

```lean
lemma dropPair_symm (i j : Fin (n + 1 + 1)) (hij : i ≠ j)
    (p : Pure S c) : dropPair i j hij p =
    permP id (by simp) (dropPair j i hij.symm p)
```

**`TensorSpecies.Tensor.Pure.dropPair_comm`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L66).

```lean
lemma dropPair_comm {n : ℕ} {c : Fin (n + 1 + 1 + 1 + 1) → C}
    (i1 j1 : Fin (n + 1 + 1 + 1 + 1)) (i2 j2 : Fin (n + 1 + 1))
    (hij1 : i1 ≠ j1) (hij2 : i2 ≠ j2) (p : Pure S c) :
    let i2' := (succSuccAbove i1 j1 i2);
    let j2' := (succSuccAbove i1 j1 j2);
    have hi2j2' : i2' ≠ j2' := by simp [i2', j2', hij2];
    let i1' := (predPredAbove i2' j2' hi2j2' i1 (by simp [i2', j2']));
    let j1' := (predPredAbove i2' j2' hi2j2' j1 (by simp [i2', j2']));
    dropPair i2 j2 hij2 (dropPair i1 j1 hij1 p) =
    permP id (IsReindexing.succSuccAbove_comm i1 j1 i2 j2 hij1 hij2)
    ((dropPair i1' j1' (by simp [i1', j1', hij1]) (dropPair i2' j2' hi2j2' p)))
```

**`TensorSpecies.Tensor.Pure.dropPair_update_fst`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L85).

```lean
lemma dropPair_update_fst {n : ℕ} [inst : DecidableEq (Fin (n + 1 +1))] {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (p : Pure S c)
    (x : V (c i)) :
    dropPair i j hij (p.update i x) = dropPair i j hij p
```

**`TensorSpecies.Tensor.Pure.dropPair_update_snd`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L95).

```lean
lemma dropPair_update_snd {n : ℕ} [inst : DecidableEq (Fin (n + 1 +1))] {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (p : Pure S c)
    (x : V (c j)) :
    dropPair i j hij (p.update j x) = dropPair i j hij p
```

**`TensorSpecies.Tensor.Pure.dropPair_update_succSuccAbove`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L104).

```lean
lemma dropPair_update_succSuccAbove {n : ℕ} [inst : DecidableEq (Fin (n + 1 +1))]
    {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (p : Pure S c)
    (m : Fin n)
    (x : V (c (succSuccAbove i j m))) :
    dropPair i j hij (p.update (succSuccAbove i j m) x) =
    (dropPair i j hij p).update m x
```

**`TensorSpecies.Tensor.Pure.dropPair_permP`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L124).

```lean
lemma dropPair_permP {n n1 : ℕ} {c : Fin (n + 1 + 1) → C}
    {c1 : Fin (n1 + 1 + 1) → C} (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j)
    (σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1)) (hσ : IsReindexing c c1 σ) (p : Pure S c) :
    dropPair i j hij (permP σ hσ p) = permP _ (hσ.succSuccAbove i j hij)
    (dropPair (σ i) (σ j) (by simp [hσ.1.injective.eq_iff, hij]) p)
```

**`TensorSpecies.Tensor.Pure.permP_dropPair_dropPair_congr`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L140).

> Two `permP`–`dropPair`–`dropPair` towers over a common pure tensor agree once their composite
> slot maps agree pointwise. Comparing two orders of dropping two pairs of slots this way keeps
> every slot map an opaque variable, so the comparison closes by unification rather than by
> `whnf`-reducing the color and index-map composites.

```lean
lemma permP_dropPair_dropPair_congr {nP nOut : ℕ}
    {c : Fin (nP + 1 + 1 + 1 + 1) → C} {cOut : Fin nOut → C} (p : Pure S c)
    (aL bL : Fin (nP + 1 + 1 + 1 + 1)) (habL : aL ≠ bL)
    (a2L b2L : Fin (nP + 1 + 1)) (hab2L : a2L ≠ b2L)
    (σ1L : Fin nOut → Fin nP)
    (h1L : IsReindexing ((c ∘ Fin.succSuccAbove aL bL) ∘ Fin.succSuccAbove a2L b2L) cOut σ1L)
    (aR bR : Fin (nP + 1 + 1 + 1 + 1)) (habR : aR ≠ bR)
    (a2R b2R : Fin (nP + 1 + 1)) (hab2R : a2R ≠ b2R)
    (σ1R : Fin nOut → Fin nP)
    (h1R : IsReindexing ((c ∘ Fin.succSuccAbove aR bR) ∘ Fin.succSuccAbove a2R b2R) cOut σ1R)
    (hslot : ∀ m : Fin nOut,
      Fin.succSuccAbove aL bL (Fin.succSuccAbove a2L b2L (σ1L m)) =
      Fin.succSuccAbove aR bR (Fin.succSuccAbove a2R b2R (σ1R m))) :
    permP σ1L h1L (dropPair a2L b2L hab2L (dropPair aL bL habL p)) =
    permP σ1R h1R (dropPair a2R b2R hab2R (dropPair aR bR habR p))
```

**`TensorSpecies.Tensor.Pure.permP_dropPair_permP_congr`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L163).

> Two `permP`–`dropPair`–`permP` towers over a common pure tensor agree once their composite
> slot maps agree pointwise. The one-contraction, inner-relabelled sibling of
> `permP_dropPair_dropPair_congr`.

```lean
lemma permP_dropPair_permP_congr {nP nOut mL mR : ℕ}
    {c : Fin nP → C} {cL : Fin (mL + 1 + 1) → C} {cR : Fin (mR + 1 + 1) → C}
    {cOut : Fin nOut → C} (p : Pure S c)
    (σ0L : Fin (mL + 1 + 1) → Fin nP) (h0L : IsReindexing c cL σ0L)
    (aL bL : Fin (mL + 1 + 1)) (habL : aL ≠ bL)
    (σ1L : Fin nOut → Fin mL)
    (h1L : IsReindexing (cL ∘ Fin.succSuccAbove aL bL) cOut σ1L)
    (σ0R : Fin (mR + 1 + 1) → Fin nP) (h0R : IsReindexing c cR σ0R)
    (aR bR : Fin (mR + 1 + 1)) (habR : aR ≠ bR)
    (σ1R : Fin nOut → Fin mR)
    (h1R : IsReindexing (cR ∘ Fin.succSuccAbove aR bR) cOut σ1R)
    (hslot : ∀ m : Fin nOut,
      σ0L (Fin.succSuccAbove aL bL (σ1L m)) = σ0R (Fin.succSuccAbove aR bR (σ1R m))) :
    permP σ1L h1L (dropPair aL bL habL (permP σ0L h0L p)) =
    permP σ1R h1R (dropPair aR bR habR (permP σ0R h0R p))
```

## Contraction coefficient

**`TensorSpecies.Tensor.Pure.contrPCoeff`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L199).

> Given a pure tensor `p : Pure S c` and a `i j : Fin n`
> corresponding to dual colors in `c`, `contrPCoeff i j _ p` is the
> element of the underlying ring `k` formed by contracting `p i` and `p j`.

```lean
noncomputable def contrPCoeff {n : ℕ} {c : Fin n → C}
    (i j : Fin n) (hij : i ≠ j ∧ S.τ (c i) = c j) (p : Pure S c) : k
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_congr`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L205).

> `contrPCoeff` is insensitive to its proof arguments once the two contracted slots agree. Lets a
> coefficient comparison rewrite the slots without a `congr` search through the proof fields.

```lean
lemma contrPCoeff_congr {n : ℕ} {c : Fin n → C} (p : Pure S c)
    {i i' j j' : Fin n} (hi : i = i') (hj : j = j')
    {hij : i ≠ j ∧ S.τ (c i) = c j} {hij' : i' ≠ j' ∧ S.τ (c i') = c j'} :
    p.contrPCoeff i j hij = p.contrPCoeff i' j' hij'
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_permP`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L216).

```lean
lemma contrPCoeff_permP {n n1 : ℕ} {c : Fin n → C}
    {c1 : Fin n1 → C} (i j : Fin n1) (hij : i ≠ j ∧ S.τ (c1 i) = c1 j)
    (σ : Fin n1 → Fin n) (hσ : IsReindexing c c1 σ) (p : Pure S c) :
    contrPCoeff i j hij (permP σ hσ p) =
    contrPCoeff (σ i) (σ j) (by simp [hσ.1.injective.eq_iff, hij, hσ.2]) p
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_update_succSuccAbove`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L232).

```lean
lemma contrPCoeff_update_succSuccAbove {n : ℕ} [inst : DecidableEq (Fin (n + 1 +1))]
    {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j) (m : Fin n)
    (p : Pure S c) (x : V (c (succSuccAbove i j m))) :
    contrPCoeff i j hij (p.update (succSuccAbove i j m) x) =
    contrPCoeff i j hij p
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_update_fst_add`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L245).

```lean
lemma contrPCoeff_update_fst_add {n : ℕ} [inst : DecidableEq (Fin n)] {c : Fin n → C}
    (i j : Fin n) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (x y : V (c i)) :
    contrPCoeff i j hij (p.update i (x + y)) =
    contrPCoeff i j hij (p.update i x) + contrPCoeff i j hij (p.update i y)
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_update_snd_add`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L255).

```lean
lemma contrPCoeff_update_snd_add {n : ℕ} [inst : DecidableEq (Fin n)] {c : Fin n → C}
    (i j : Fin n) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (x y : V (c j)) :
    contrPCoeff i j hij (p.update j (x + y)) =
    contrPCoeff i j hij (p.update j x) + contrPCoeff i j hij (p.update j y)
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_update_fst_smul`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L265).

```lean
lemma contrPCoeff_update_fst_smul {n : ℕ} [inst : DecidableEq (Fin n)] {c : Fin n → C}
    (i j : Fin n) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (r : k) (x : V (c i)) :
    contrPCoeff i j hij (p.update i (r • x)) =
    r * contrPCoeff i j hij (p.update i x)
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_update_snd_smul`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L276).

```lean
lemma contrPCoeff_update_snd_smul {n : ℕ} [inst : DecidableEq (Fin n)] {c : Fin n → C}
    (i j : Fin n) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (r : k) (x : V (c j)) :
    contrPCoeff i j hij (p.update j (r • x)) =
    r * contrPCoeff i j hij (p.update j x)
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_dropPair`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L286).

```lean
lemma contrPCoeff_dropPair {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (a b : Fin (n + 1 + 1)) (hab : a ≠ b)
    (i j : Fin n) (hij : i ≠ j ∧ S.τ (c (succSuccAbove a b i)) = (c (succSuccAbove a b j)))
    (p : Pure S c) : (p.dropPair a b hab).contrPCoeff i j hij =
    p.contrPCoeff (succSuccAbove a b i) (succSuccAbove a b j)
      (by simpa using hij)
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_symm`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L293).

```lean
lemma contrPCoeff_symm {n : ℕ} {c : Fin n → C} {i j : Fin n} {hij : i ≠ j ∧ S.τ (c i) = c j}
    {p : Pure S c} :
    p.contrPCoeff i j hij = p.contrPCoeff j i ⟨hij.1.symm, by simp [← hij.2]⟩
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_mul_dropPair`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L305).

```lean
lemma contrPCoeff_mul_dropPair {n : ℕ} {c : Fin (n + 1 + 1 + 1 + 1) → C}
    (i1 j1 : Fin (n + 1 + 1 + 1 + 1)) (i2 j2 : Fin (n + 1 + 1))
    (hij1 : i1 ≠ j1 ∧ S.τ (c i1) = (c j1))
    (hij2 : i2 ≠ j2 ∧ S.τ (c (succSuccAbove i1 j1 i2)) = (c (succSuccAbove i1 j1 j2)))
    (p : Pure S c) :
    let i2' := (succSuccAbove i1 j1 i2);
    let j2' := (succSuccAbove i1 j1 j2);
    have hi2j2' : i2' ≠ j2' := by simp [i2', j2', hij2];
    let i1' := (predPredAbove i2' j2' hi2j2' i1 (by simp [i2', j2']));
    let j1' := (predPredAbove i2' j2' hi2j2' j1 (by simp [i2', j2']));
    (p.contrPCoeff i1 j1 hij1) * (dropPair i1 j1 hij1.1 p).contrPCoeff i2 j2 hij2 =
    (p.contrPCoeff i2' j2' (by simp [i2', j2', hij2])) *
    (dropPair i2' j2' (by simp [i2', j2', hij2]) p).contrPCoeff i1' j1'
      (by simp [i1', j1', hij1])
```

**`TensorSpecies.Tensor.Pure.contrPCoeff_invariant`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L323).

```lean
lemma contrPCoeff_invariant {n : ℕ} {c : Fin n → C} {i j : Fin n}
    {hij : i ≠ j ∧ S.τ (c i) = c j} {p : Pure S c}
    (g : G) : (g • p).contrPCoeff i j hij = p.contrPCoeff i j hij
```

## Contractions

**`TensorSpecies.Tensor.Pure.contrP`**, a def, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L347).

> For `c : Fin (n + 1 + 1) → C`, `i j : Fin (n + 1 + 1)` with dual color, and a pure tensor
> `p : Pure S c`, `contrP i j _ p` is the tensor (not pure due to the `n = 0` case)
> formed by contracting the `i`th index of `p`
> with the `j`th index.

```lean
noncomputable def contrP {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j) (p : Pure S c) :
    S.Tensor (c ∘ succSuccAbove i j)
```

**`TensorSpecies.Tensor.Pure.contrP_update_add`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L353).

```lean
lemma contrP_update_add {n : ℕ} [inst : DecidableEq (Fin (n + 1 +1))] {c : Fin (n + 1 + 1) → C}
    (i j m : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (x y : V (c m)) :
    contrP i j hij (p.update m (x + y)) =
    contrP i j hij (p.update m x) + contrP i j hij (p.update m y)
```

**`TensorSpecies.Tensor.Pure.contrP_update_smul`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L364).

```lean
lemma contrP_update_smul {n : ℕ} [inst : DecidableEq (Fin (n + 1 +1))] {c : Fin (n + 1 + 1) → C}
    (i j m : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j)
    (p : Pure S c) (r : k) (x : V (c m)) :
    contrP i j hij (p.update m (r • x)) =
    r • contrP i j hij (p.update m x)
```

**`TensorSpecies.Tensor.Pure.contrP_equivariant`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L375).

```lean
lemma contrP_equivariant {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j) (p : Pure S c) (g : G) :
    contrP i j hij (g • p) = g • contrP i j hij p
```

**`TensorSpecies.Tensor.Pure.contrP_symm`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L380).

```lean
lemma contrP_symm {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} {hij : i ≠ j ∧ S.τ (c i) = c j} {p : Pure S c} :
    contrP i j hij p = permT id (by simp)
    (contrP j i ⟨hij.1.symm, by simp [← hij.2]⟩ p)
```

## contrP as a multilinear map

**`TensorSpecies.Tensor.Pure.contrPMultilinear`**, a def, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean#L394).

> The multi-linear map formed by contracting a pair of indices of pure tensors.

```lean
noncomputable def contrPMultilinear {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j ∧ S.τ (c i) = c j) :
    MultilinearMap k (fun i => V (c i))
      (S.Tensor (c ∘ succSuccAbove i j))
```

## Depends on

- [Tensors](../part-01/basic.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/Pure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/Pure.lean)
