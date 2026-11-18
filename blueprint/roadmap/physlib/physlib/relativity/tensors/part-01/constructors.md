---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.Pure.fromSingleP, TensorSpecies.Tensor.fromSingleT, TensorSpecies.Tensor.fromSingleT_symm_pure, TensorSpecies.Tensor.fromSingleT_eq_pureT, TensorSpecies.Tensor.actionT_fromSingleT, TensorSpecies.Tensor.fromSingleT_map, TensorSpecies.Tensor.contrT_fromSingleT_fromSingleT, TensorSpecies.Tensor.fromPairT
statement: formalized
proof: formalized
---

# Constructors of tensors.

The module `Physlib.Relativity.Tensors.Constructors`, [Physlib/Relativity/Tensors/Constructors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean): 41 declarations, 15 with a docstring.

> There are a number of ways to construct explicit tensors.

## Tensors with a single index.

**`TensorSpecies.Tensor.Pure.fromSingleP`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L39).

> The equivalence between `V c` and `Pure S ![c]`.

```lean
noncomputable def Pure.fromSingleP {c : C} : V c ≃ₗ[k] Pure S ![c]
```

**`TensorSpecies.Tensor.fromSingleT`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L57).

> The equivalence between `V c` and `S.Tensor ![c]`.

```lean
noncomputable def fromSingleT {c : C} : V c ≃ₗ[k] S.Tensor ![c]
```

**`TensorSpecies.Tensor.fromSingleT_symm_pure`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L60).

```lean
lemma fromSingleT_symm_pure {c : C} (p : Pure S ![c]) :
    fromSingleT.symm p.toTensor = Pure.fromSingleP.symm p
```

**`TensorSpecies.Tensor.fromSingleT_eq_pureT`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L64).

```lean
lemma fromSingleT_eq_pureT {c : C} (x : V c) :
    fromSingleT (S := S) x = Pure.toTensor (fun 0 => x : Pure S ![c])
```

**`TensorSpecies.Tensor.actionT_fromSingleT`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L71).

```lean
lemma actionT_fromSingleT {c : C} (x : V c) (g : G) :
    g • fromSingleT (S := S) x = fromSingleT (rep c g x)
```

**`TensorSpecies.Tensor.fromSingleT_map`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L79).

```lean
lemma fromSingleT_map {c c1 : C}
    (h : c = c1) (x : V c) :
    fromSingleT (LinearEquiv.cast (R := k) h x) =
    permT id (by simp [h]) (fromSingleT (S := S) x)
```

**`TensorSpecies.Tensor.contrT_fromSingleT_fromSingleT`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L89).

```lean
lemma contrT_fromSingleT_fromSingleT {c : C} (x : V c)
    (y : V (S.τ c)) :
    contrT (S := S) 0 0 1 (by simp; rfl) (prodT (fromSingleT x) (fromSingleT y)) =
    (S.contr c) (x ⊗ₜ[k] y) • (Pure.toTensor default)
```

## Tensors with two indices.

## fromPairT

**`TensorSpecies.Tensor.fromPairT`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L117).

> The construction of a tensor with two indices from the tensor product
> `V c1 ⊗[k] V c2 ` defined
> categorically.

```lean
noncomputable def fromPairT {c1 c2 : C} :
    V c1 ⊗[k] V c2 →ₗ[k] S.Tensor ![c1, c2]
```

**`TensorSpecies.Tensor.fromPairT_tmul`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L126).

```lean
lemma fromPairT_tmul {c1 c2 : C} (x : V c1)
    (y : V c2) : fromPairT (x ⊗ₜ[k] y) =
    permT id (And.intro Function.bijective_id (fun i => by fin_cases i <;> rfl))
    (prodT (fromSingleT (S := S) x) (fromSingleT y))
```

**`TensorSpecies.Tensor.fromPairT_eq_pure`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L133).

```lean
lemma fromPairT_eq_pure {c1 c2 : C} (x : V c1) (y : V c2) :
    fromPairT (S := S) (x ⊗ₜ[k] y) = Pure.toTensor (fun | 0 => x | 1 => y)
```

**`TensorSpecies.Tensor.actionT_fromPairT`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L141).

```lean
lemma actionT_fromPairT {c1 c2 : C}
    (x : V c1 ⊗[k]V c2)
    (g : G) :
    g • fromPairT (S := S) x = fromPairT (TensorProduct.map (rep c1 g)
      (rep c2 g) x)
```

**`TensorSpecies.Tensor.fromPairT_map_right`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L155).

```lean
lemma fromPairT_map_right {c1 c2 c2' : C} (h :c2 = c2')
    (x : V c1 ⊗[k] V c2) :
    fromPairT (TensorProduct.map LinearMap.id
      (LinearEquiv.cast (R := k) (M := V) h) x : _ ⊗[k] V c2') =
    permT id (by simp [h]) (fromPairT (S := S) x)
```

**`TensorSpecies.Tensor.fromPairT_comm`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L172).

```lean
lemma fromPairT_comm {c1 c2 : C}
    (x : V c1 ⊗[k] V c2) :
    fromPairT (TensorProduct.comm k _ _ x) =
    permT ![1, 0] (And.intro (by decide) (fun i => by fin_cases i <;> simp))
    (fromPairT (S := S) x)
```

### Contraction of fromPairT with fromSingleT

**`TensorSpecies.Tensor.fromSingleTContrFromPairT`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L194).

> The contraction of tensors with one index with one with two indices defined categorically.

```lean
noncomputable def fromSingleTContrFromPairT {c c2 : C}
    (x : V c) (y : V (S.τ c) ⊗[k] V c2) : S.Tensor ![c2]
```

**`TensorSpecies.Tensor.fromSingleTContrFromPairT_tmul`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L202).

```lean
lemma fromSingleTContrFromPairT_tmul {c c2 : C}
    (x : V c) (y1 : V (S.τ c)) (y2 : V c2) :
    fromSingleTContrFromPairT x (y1 ⊗ₜ[k] y2) =
    S.contr c (x ⊗ₜ[k] y1) • fromSingleT y2
```

**`TensorSpecies.Tensor.fromSingleT_contr_fromPairT_tmul`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L209).

```lean
lemma fromSingleT_contr_fromPairT_tmul {c c2 : C}
    (x : V c) (y1 : V (S.τ c)) (y2 : V c2) :
    contrT 1 0 1 (by simp; rfl)
      (prodT (fromSingleT x) (fromPairT (y1 ⊗ₜ[k] y2))) =
    permT id (by simp; rfl) (fromSingleTContrFromPairT x (y1 ⊗ₜ[k] y2))
```

**`TensorSpecies.Tensor.contrT_fromSingleT_fromPairT`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L258).

```lean
lemma contrT_fromSingleT_fromPairT {c c2 : C}
    (x : V c)
    (y : V (S.τ c) ⊗[k] V c2) :
    contrT 1 0 1 (by simp; rfl)
      (prodT (fromSingleT x) (fromPairT y)) =
    permT id (by simp; rfl) (fromSingleTContrFromPairT x y)
```

### Contraction of fromPairT with fromPairT

**`TensorSpecies.Tensor.fromPairTContr`**, a def, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L278).

> The contraction of tensors with two indices defined categorically.

```lean
noncomputable def fromPairTContr {c c1 c2 : C}(x : V c1 ⊗[k] V c) (y : V (S.τ c) ⊗[k] V c2) :
    S.Tensor ![c1, c2]
```

**`TensorSpecies.Tensor.fromPairTContr_tmul_tmul`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L291).

```lean
lemma fromPairTContr_tmul_tmul {c c1 c2 : C} (x1 : V c1) (x2 : V c) (y1 : V (S.τ c))
    (y2 : V c2) : fromPairTContr (x1 ⊗ₜ[k] x2) (y1 ⊗ₜ[k] y2) =
    (S.contr c) (x2 ⊗ₜ[k] y1) • fromPairT (x1 ⊗ₜ[k] y2)
```

**`TensorSpecies.Tensor.fromPairT_contr_fromPairT_eq_fromPairTContr_tmul`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L296).

```lean
lemma fromPairT_contr_fromPairT_eq_fromPairTContr_tmul (c c1 c2 : C)
    (x1 : V c1) (x2 : V c) (y1 : V (S.τ c))
    (y2 : V c2) :
    contrT 2 1 2 (by simp; rfl) (prodT (fromPairT (x1 ⊗ₜ[k] x2)) (fromPairT (y1 ⊗ₜ[k] y2))) =
    permT id (by simp; exact ⟨rfl, rfl⟩)
    (fromPairTContr (x1 ⊗ₜ[k] x2) (y1 ⊗ₜ[k] y2))
```

**`TensorSpecies.Tensor.fromPairT_contr_fromPairT_eq_fromPairTContr`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L308).

```lean
lemma fromPairT_contr_fromPairT_eq_fromPairTContr (c c1 c2 : C)
    (x : V c1 ⊗[k] V c)
    (y : V (S.τ c) ⊗[k] V c2) :
    contrT 2 1 2 (by simp; rfl)
      (prodT (fromPairT x) (fromPairT y)) =
    permT id (by simp; exact ⟨rfl, rfl⟩) (fromPairTContr x y)
```

**`TensorSpecies.Tensor.fromPairT_basis_repr`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L331).

```lean
lemma fromPairT_basis_repr {c c1 : C}
    (x : V c ⊗[k] V c1)
    (φ : ComponentIdx ![c, c1]) :
    (basis ![c, c1]).repr (fromPairT (S := S) x) φ =
    (Basis.tensorProduct (b c) (b c1)).repr x (φ 0, φ 1)
```

**`TensorSpecies.Tensor.fromPairT_apply_basis_repr`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L353).

```lean
lemma fromPairT_apply_basis_repr {c c1 : C}
    (b0 : basisIdx c) (b1 : basisIdx c1) :
    fromPairT (S := S) (b c b0 ⊗ₜ[k] b c1 b1) =
    Tensor.basis ![c, c1] (fun | 0 => b0 | 1 => b1)
```

## fromConstPair

**`TensorSpecies.Tensor.fromConstPair`**, a def, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L380).

> A constant two tensor (e.g. metric and unit).

```lean
noncomputable def fromConstPair {c1 c2 : C}
      (v : (Representation.trivial k G k).IntertwiningMap ((rep c1).tprod (rep c2))) :
    S.Tensor ![c1, c2]
```

**`TensorSpecies.Tensor.actionT_fromConstPair`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L386).

> Tensors formed by `fromConstPair` are invariant under the group action.

```lean
lemma actionT_fromConstPair {c1 c2 : C}
    (v : (Representation.trivial k G k).IntertwiningMap ((rep c1).tprod (rep c2)))
    (g : G) : g • fromConstPair (S := S) v = fromConstPair v
```

## fromMatrixT

**`TensorSpecies.Tensor.fromMatrixT`**, a def, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L400).

> Rank-two tensors and their component matrices, as a linear equivalence: `fromMatrixT c0 c1 M`
> is the tensor with component matrix `M`.

```lean
noncomputable def fromMatrixT (c0 c1 : C) :
    Matrix (basisIdx c0) (basisIdx c1) k ≃ₗ[k] S.Tensor ![c0, c1]
```

**`TensorSpecies.Tensor.fromMatrixT_basis_repr`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L421).

```lean
lemma fromMatrixT_basis_repr (c0 c1 : C) (M : Matrix (basisIdx c0) (basisIdx c1) k)
    (φ : ComponentIdx ![c0, c1]) :
    (basis ![c0, c1]).repr (fromMatrixT (S := S) c0 c1 M) φ = M (φ 0) (φ 1)
```

**`TensorSpecies.Tensor.toMatrix`**, a def, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L429).

> The component matrix of a rank-two tensor: the `(x, y)` entry is
> `repr t (ComponentIdx.pair.symm (x, y))`.

```lean
noncomputable def toMatrix {cs : Fin 2 → C} (t : S.Tensor cs) :
    Matrix (basisIdx (cs 0)) (basisIdx (cs 1)) k
```

**`TensorSpecies.Tensor.toMatrix_apply`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L434).

```lean
lemma toMatrix_apply {cs : Fin 2 → C} (t : S.Tensor cs)
    (x : basisIdx (cs 0)) (y : basisIdx (cs 1)) :
    toMatrix t x y = (basis cs).repr t (ComponentIdx.pair.symm (x, y))
```

**`TensorSpecies.Tensor.toMatrix_apply_cons`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L441).

> `toMatrix_apply` at a `cons` colour list `![c0, c1]`, where the labels are named by the
> colours.

```lean
lemma toMatrix_apply_cons {c0 c1 : C} (t : S.Tensor ![c0, c1])
    (x : basisIdx c0) (y : basisIdx c1) :
    toMatrix t x y = (basis ![c0, c1]).repr t (ComponentIdx.pair.symm (x, y))
```

**`TensorSpecies.Tensor.toMatrix_fromMatrixT`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L446).

```lean
lemma toMatrix_fromMatrixT (c0 c1 : C) (M : Matrix (basisIdx c0) (basisIdx c1) k) :
    toMatrix (fromMatrixT (S := S) c0 c1 M) = M
```

**`TensorSpecies.Tensor.fromMatrixT_toMatrix`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L451).

```lean
lemma fromMatrixT_toMatrix {c0 c1 : C} (t : S.Tensor ![c0, c1]) :
    fromMatrixT (S := S) c0 c1 (toMatrix t) = t
```

**`TensorSpecies.Tensor.toMatrix_injective`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L456).

> Rank-two tensors with equal component matrices are equal.

```lean
lemma toMatrix_injective {cs : Fin 2 → C} :
    Function.Injective (toMatrix (S := S) (cs := cs))
```

**`TensorSpecies.Tensor.toMatrix_permT_swap`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L466).

> Swapping the two slots of a rank-two tensor transposes its component matrix.

```lean
lemma toMatrix_permT_swap {c c1 : Fin 2 → C} (h0 : c 1 = c1 0) (h1 : c 0 = c1 1)
    (t : S.Tensor c) :
    toMatrix (permT ![1, 0] (IsReindexing.swap_of_eq h0 h1) t) =
      (toMatrix t).transpose.submatrix (basisIdxCongr h0.symm) (basisIdxCongr h1.symm)
```

## fromTripleT

**`TensorSpecies.Tensor.fromTripleT`**, a def, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L489).

> The construction of a tensor with two indices from the tensor product
> `V c1 ⊗[k] V c2 ` defined
> categorically.

```lean
noncomputable def fromTripleT {c1 c2 c3 : C} :
    V c1 ⊗[k] (V c2 ⊗[k] V c3) →ₗ[k] S.Tensor ![c1, c2, c3]
```

**`TensorSpecies.Tensor.fromTripleT_tmul`**, a lemma, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L504).

```lean
lemma fromTripleT_tmul {c1 c2 c3 : C} (x : V c1)
    (y : V c2) (z : V c3) :
    fromTripleT (x ⊗ₜ[k] (y ⊗ₜ[k] z)) =
    permT id (And.intro Function.bijective_id (fun i => by fin_cases i <;> rfl))
      (prodT (fromSingleT (S := S) x) (prodT (fromSingleT y) (fromSingleT z)))
```

**`TensorSpecies.Tensor.actionT_fromTripleT`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L512).

```lean
lemma actionT_fromTripleT {c1 c2 c3 : C}
    (x : V c1 ⊗[k] (V c2 ⊗[k] V c3)) (g : G) :
    g • fromTripleT (S := S) x = fromTripleT (TensorProduct.map (rep c1 g)
      (TensorProduct.map (rep c2 g) (rep c3 g)) x)
```

**`TensorSpecies.Tensor.fromTripleT_basis_repr`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L528).

```lean
lemma fromTripleT_basis_repr {c c1 c2 : C}
    (x : V c ⊗[k] (V c1 ⊗[k] V c2))
    (φ : ComponentIdx ![c, c1, c2]) :
    (basis ![c, c1, c2]).repr (fromTripleT (S := S) x) φ =
    (Basis.tensorProduct (b c) (Basis.tensorProduct (b c1) (b c2))).repr x
    (φ 0, φ 1, φ 2)
```

**`TensorSpecies.Tensor.fromTripleT_apply_basis`**, a lemma, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L560).

```lean
lemma fromTripleT_apply_basis {c c1 c2 : C}
    (b0 : basisIdx c) (b1 : basisIdx c1)
    (b2 : basisIdx c2) :
    fromTripleT (S := S) (b c b0 ⊗ₜ[k] (b c1 b1 ⊗ₜ[k] b c2 b2)) =
    Tensor.basis ![c, c1, c2] (fun | 0 => b0 | 1 => b1 | 2 => b2)
```

## fromConstTriple

**`TensorSpecies.Tensor.fromConstTriple`**, a def, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L593).

> A constant three tensor (e.g. the Pauli matrices).

```lean
noncomputable def fromConstTriple {c1 c2 c3 : C}
    (v : (Representation.trivial k G k).IntertwiningMap
      ((rep c1).tprod ((rep c2).tprod (rep c3)))) :
  S.Tensor ![c1, c2, c3]
```

**`TensorSpecies.Tensor.actionT_fromConstTriple`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean#L600).

> Tensors formed by `fromConstPair` are invariant under the group action.

```lean
lemma actionT_fromConstTriple {c1 c2 c3 : C}
    (v : (Representation.trivial k G k).IntertwiningMap ((rep c1).tprod ((rep c2).tprod (rep c3))))
    (g : G) : g • fromConstTriple (S := S) v = fromConstTriple v
```

## Depends on

- [Component indices for two-index tensors](../part-02/componentidx-pair.md)
- [Contractions on tensors](../part-02/contraction-basic.md)
- [The product of tensors](product.md)

## Proof depends on

- [The interaction of contractions and products](../part-02/contraction-products.md)

## Sources

- [Physlib/Relativity/Tensors/Constructors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Constructors.lean)
