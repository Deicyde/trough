---
catalog: module
lean: Fin.dfoldrM_loop_zero, Fin.dfoldrM_loop_succ, Fin.dfoldrM_loop, Fin.dfoldrM_zero, Fin.dfoldrM_succ, Fin.dfoldrM_eq_foldrM, Fin.dfoldr_eq_dfoldrM, Fin.dfoldr_zero, Fin.dfoldr_succ, Fin.dfoldr_succ_last, Fin.dfoldr_eq_foldr, Fin.dfoldlM_loop_lt, Fin.dfoldlM_loop_eq, Fin.dfoldlM_zero, Fin.dfoldlM_loop, Fin.dfoldlM_succ, Fin.dfoldlM_eq_foldlM, Fin.dfoldl_zero, Fin.dfoldl_succ, Fin.dfoldl_succ_last, Fin.dfoldl_eq_dfoldlM, Fin.dfoldl_eq_foldl, Fin.foldl_eq_foldl_finRange, Fin.foldr_eq_foldr_finRange
statement: formalized
proof: formalized
---

# Fold

`Batteries.Data.Fin.Fold`, in [Batteries/Data/Fin/Fold.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean), by François G. Dorais, Quang Dao.

> ### dfoldrM

`Fin.dfoldrM_loop_zero` (theorem, [line 16](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L16))

```lean
theorem dfoldrM_loop_zero [Monad m] (f : (i : Fin n) → α i.succ → m (α i.castSucc)) (x) :
    dfoldrM.loop n α f 0 h x = pure x
```

`Fin.dfoldrM_loop_succ` (theorem, [line 19](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L19))

```lean
theorem dfoldrM_loop_succ [Monad m] (f : (i : Fin n) → α i.succ → m (α i.castSucc)) (x) :
    dfoldrM.loop n α f (i+1) h x = f ⟨i, by omega⟩ x >>= dfoldrM.loop n α f i (by omega)
```

`Fin.dfoldrM_loop` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L24))

```lean
theorem dfoldrM_loop [Monad m] [LawfulMonad m] (f : (i : Fin (n+1)) → α i.succ → m (α i.castSucc))
    (x) : dfoldrM.loop (n+1) α f (i+1) h x =
      dfoldrM.loop n (α ∘ succ) (f ·.succ) i (by omega) x >>= f 0
```

`Fin.dfoldrM_zero` (theorem, [line 36](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L36))

```lean
theorem dfoldrM_zero [Monad m] (f : (i : Fin 0) → α i.succ → m (α i.castSucc)) (x) :
    dfoldrM 0 α f x = pure x
```

`Fin.dfoldrM_succ` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L39))

```lean
theorem dfoldrM_succ [Monad m] [LawfulMonad m] (f : (i : Fin (n+1)) → α i.succ → m (α i.castSucc))
    (x) : dfoldrM (n+1) α f x = dfoldrM n (α ∘ succ) (f ·.succ) x >>= f 0
```

`Fin.dfoldrM_eq_foldrM` (theorem, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L42))

```lean
theorem dfoldrM_eq_foldrM [Monad m] [LawfulMonad m] (f : (i : Fin n) → α → m α) (x) :
    dfoldrM n (fun _ => α) f x = foldrM n f x
```

`Fin.dfoldr_eq_dfoldrM` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L48))

```lean
theorem dfoldr_eq_dfoldrM (f : (i : Fin n) → α i.succ → α i.castSucc) (x) :
    dfoldr n α f x = dfoldrM (m:=Id) n α f x
```

> ### dfoldr

`Fin.dfoldr_zero` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L53))

```lean
theorem dfoldr_zero (f : (i : Fin 0) → α i.succ → α i.castSucc) (x) :
    dfoldr 0 α f x = x
```

`Fin.dfoldr_succ` (theorem, [line 56](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L56))

```lean
theorem dfoldr_succ (f : (i : Fin (n+1)) → α i.succ → α i.castSucc) (x) :
    dfoldr (n+1) α f x = f 0 (dfoldr n (α ∘ succ) (f ·.succ) x)
```

`Fin.dfoldr_succ_last` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L60))

```lean
theorem dfoldr_succ_last {n : Nat} {α : Fin (n+2) → Sort _}
    (f : (i : Fin (n+1)) → α i.succ → α i.castSucc) (x : α (last (n+1))) :
      dfoldr (n+1) α f x = dfoldr n (α ∘ castSucc) (f ·.castSucc) (f (last n) x)
```

`Fin.dfoldr_eq_foldr` (theorem, [line 67](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L67))

```lean
theorem dfoldr_eq_foldr (f : (i : Fin n) → α → α) (x) :
    dfoldr n (fun _ => α) f x = foldr n f x
```

> ### dfoldlM

`Fin.dfoldlM_loop_lt` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L75))

```lean
theorem dfoldlM_loop_lt [Monad m] (f : ∀ (i : Fin n), α i.castSucc → m (α i.succ)) (h : i < n) (x) :
    dfoldlM.loop n α f i (Nat.lt_add_right 1 h) x =
      (f ⟨i, h⟩ x) >>= (dfoldlM.loop n α f (i+1) (Nat.add_lt_add_right h 1))
```

`Fin.dfoldlM_loop_eq` (theorem, [line 80](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L80))

```lean
theorem dfoldlM_loop_eq [Monad m] (f : ∀ (i : Fin n), α i.castSucc → m (α i.succ)) (x) :
    dfoldlM.loop n α f n (Nat.le_refl _) x = pure x
```

`Fin.dfoldlM_zero` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L85))

```lean
theorem dfoldlM_zero [Monad m] (f : (i : Fin 0) → α i.castSucc → m (α i.succ)) (x) :
    dfoldlM 0 α f x = pure x
```

`Fin.dfoldlM_loop` (theorem, [line 88](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L88))

```lean
theorem dfoldlM_loop [Monad m] (f : (i : Fin (n+1)) → α i.castSucc → m (α i.succ)) (h : i < n+1)
    (x) : dfoldlM.loop (n+1) α f i (Nat.lt_add_right 1 h) x =
      f ⟨i, h⟩ x >>= (dfoldlM.loop n (α ∘ succ) (f ·.succ ·) i h .)
```

`Fin.dfoldlM_succ` (theorem, [line 101](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L101))

```lean
theorem dfoldlM_succ [Monad m] (f : (i : Fin (n+1)) → α i.castSucc → m (α i.succ)) (x) :
    dfoldlM (n+1) α f x = f 0 x >>= (dfoldlM n (α ∘ succ) (f ·.succ ·) .)
```

`Fin.dfoldlM_eq_foldlM` (theorem, [line 105](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L105))

```lean
theorem dfoldlM_eq_foldlM [Monad m] (f : (i : Fin n) → α → m α) (x : α) :
    dfoldlM n (fun _ => α) f x = foldlM n (fun x i => f i x) x
```

> ### dfoldl

`Fin.dfoldl_zero` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L115))

```lean
theorem dfoldl_zero (f : (i : Fin 0) → α i.castSucc → α i.succ) (x) :
    dfoldl 0 α f x = x
```

`Fin.dfoldl_succ` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L118))

```lean
theorem dfoldl_succ (f : (i : Fin (n+1)) → α i.castSucc → α i.succ) (x) :
    dfoldl (n+1) α f x = dfoldl n (α ∘ succ) (f ·.succ ·) (f 0 x)
```

`Fin.dfoldl_succ_last` (theorem, [line 122](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L122))

```lean
theorem dfoldl_succ_last (f : (i : Fin (n+1)) → α i.castSucc → α i.succ) (x) :
    dfoldl (n+1) α f x = f (last n) (dfoldl n (α ∘ castSucc) (f ·.castSucc ·) x)
```

`Fin.dfoldl_eq_dfoldlM` (theorem, [line 129](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L129))

```lean
theorem dfoldl_eq_dfoldlM (f : (i : Fin n) → α i.castSucc → α i.succ) (x) :
    dfoldl n α f x = dfoldlM (m := Id) n α f x
```

`Fin.dfoldl_eq_foldl` (theorem, [line 132](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L132))

```lean
theorem dfoldl_eq_foldl (f : Fin n → α → α) (x : α) :
    dfoldl n (fun _ => α) f x = foldl n (fun x i => f i x) x
```

> ### `Fin.fold{l/r}{M}` equals `List.fold{l/r}{M}`

`Fin.foldl_eq_foldl_finRange` (theorem, [line 142](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L142))

```lean
theorem foldl_eq_foldl_finRange (f : α → Fin n → α) (x) :
    foldl n f x = (List.finRange n).foldl f x
```

`Fin.foldr_eq_foldr_finRange` (theorem, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean#L148))

```lean
theorem foldr_eq_foldr_finRange (f : Fin n → α → α) (x) :
    foldr n f x = (List.finRange n).foldr f x
```

## Depends on

- [Fin/Basic](basic.md)

## Sources

- [Batteries/Data/Fin/Fold.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Fold.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Fin.Fold.json)
