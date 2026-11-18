---
declaration: module
origin: cited
lean: Fin.succSuccAbove, Fin.succSuccAbove_val, Fin.succSuccAbove_self_apply, Fin.succSuccAbove_eq_succAbove_succAbove, Fin.succSuccAbove_eq_predAbove, Fin.succSuccAbove_injective, Fin.succSuccAbove_eq_iff_eq, Fin.succSuccAbove_leq_iff_leq
statement: formalized
proof: formalized
---

# Defining succSuccAbove

The module `Physlib.Relativity.Tensors.Contraction.SuccSuccAbove`, [Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean): 43 declarations, 6 with a docstring.

> In Mathlib there is the `Fin.succAbove` function which gives an embedding of `Fin n` into
> `Fin (n + 1)` by leaving a hole at a specified index. We will need a version of this which
> gives an embedding of `Fin n` into `Fin (n + 1 + 1)` by leaving holes at
> two specified indices. We call this `succSuccAbove`.
>
> We will also need an explicit inverse of this map from
> `Fin (n + 1 + 1)` to `Fin n` which is defined on the complement of the two specified indices.
> This is similar to `Fin.predAbove` (although not exactly the same),
> for this reason we call it `predPredAbove`.

## Implementation

> In previous versions of Physlib the function which is now called `succSuccAbove`
> was previously called `dropPairEmb` and the function which is now called `predPredAbove` was
> previously called `dropPairEmbPre`.

## Defining succSuccAbove

> The definition below is deliberately explicit. Later lemmas identify it with
> `Finset.orderEmbOfFin` and `Finset.orderIsoOfFin`, giving a bridge to the Mathlib
> API while keeping this form convenient for computation and goals solved by
> `decide`.

**`Fin.succSuccAbove`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L52).

> The embedding of `Fin n` into `Fin (n + 1 + 1)` which leaves a hole
> at `i` and `j`.

```lean
def succSuccAbove (i j : Fin (n + 1 + 1)) (m : Fin n) : Fin (n + 1 + 1)
```

**`Fin.succSuccAbove_val`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L62).

```lean
lemma succSuccAbove_val (i j : Fin (n + 1 + 1)) (m : Fin n) :
    (succSuccAbove i j m).val = if m.1 < i.1 ∧ m.1 < j.1 then m.1
    else if m.1 + 1 < i.1 ∧ j.1 ≤ m.1 then m.1 + 1
    else if i.1 ≤ m.1 ∧ m.1 + 1 < j.1 then m.1 + 1
    else m.1 + 2
```

**`Fin.succSuccAbove_self_apply`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L70).

```lean
lemma succSuccAbove_self_apply (i : Fin (n + 1 + 1)) (m : Fin n) :
    succSuccAbove i i m = if m.1 < i.1 then ⟨m.1, by omega⟩ else ⟨m.1 + 2, by omega⟩
```

**`Fin.succSuccAbove_eq_succAbove_succAbove`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L75).

```lean
lemma succSuccAbove_eq_succAbove_succAbove (i : Fin (n + 1 + 1)) (j : Fin (n + 1)) :
    succSuccAbove i (i.succAbove j) = i.succAbove ∘ j.succAbove
```

**`Fin.succSuccAbove_eq_predAbove`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L81).

```lean
lemma succSuccAbove_eq_predAbove {i j : Fin (n + 1 + 1)} (hij : i ≠ j) :
    succSuccAbove i j = fun x => i.succAbove (((Fin.predAbove 0 i).predAbove j).succAbove x)
```

**`Fin.succSuccAbove_injective`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L99).

```lean
lemma succSuccAbove_injective {n : ℕ}
    (i j : Fin (n + 1 + 1)) : Function.Injective (succSuccAbove i j)
```

**`Fin.succSuccAbove_eq_iff_eq`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L106).

```lean
lemma succSuccAbove_eq_iff_eq {n : ℕ}
    (i j : Fin (n + 1 + 1)) (m1 m2 : Fin n) :
    succSuccAbove i j m1 = succSuccAbove i j m2 ↔ m1 = m2
```

**`Fin.succSuccAbove_leq_iff_leq`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L112).

```lean
lemma succSuccAbove_leq_iff_leq {n : ℕ}
    (i j : Fin (n + 1 + 1)) (m1 m2 : Fin n) :
    succSuccAbove i j m1 ≤ succSuccAbove i j m2 ↔ m1 ≤ m2
```

**`Fin.succSuccAbove_lt_iff_lt`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L119).

```lean
lemma succSuccAbove_lt_iff_lt {n : ℕ}
    (i j : Fin (n + 1 + 1)) (m1 m2 : Fin n) :
    succSuccAbove i j m1 < succSuccAbove i j m2 ↔ m1 < m2
```

**`Fin.succSuccAbove_monotone`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L126).

```lean
lemma succSuccAbove_monotone {n : ℕ} (i j : Fin (n + 1 + 1)) :
    Monotone (succSuccAbove i j)
```

**`Fin.succSuccAbove_strictMono`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L131).

```lean
lemma succSuccAbove_strictMono {n : ℕ} (i j : Fin (n + 1 + 1)) :
    StrictMono (succSuccAbove i j)
```

**`Fin.succSuccAbove_range`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L136).

```lean
lemma succSuccAbove_range {i j : Fin (n + 1 + 1)} (hij : i ≠ j) :
    Set.range (succSuccAbove i j) = {i, j}ᶜ
```

**`Fin.succSuccAbove_eq_orderEmbOfFin`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L154).

```lean
lemma succSuccAbove_eq_orderEmbOfFin {n : ℕ}
    (i j : Fin (n + 1 + 1)) (hij : i ≠ j) :
    succSuccAbove i j = Finset.orderEmbOfFin {i, j}ᶜ
    (by rw [Finset.card_compl]; simp [Finset.card_pair hij])
```

**`Fin.succSuccAbove_symm`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L163).

```lean
lemma succSuccAbove_symm (i j : Fin (n + 1 + 1)) :
    succSuccAbove i j = succSuccAbove j i
```

**`Fin.apply_succSuccAbove_symm`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L171).

```lean
lemma apply_succSuccAbove_symm {c : Fin (n + 1 + 1) → C} (i j : Fin (n + 1 + 1))
    (k : Fin n) : c (succSuccAbove i j k) = c (succSuccAbove j i k)
```

**`Fin.succSuccAbove_apply_eq_orderIsoOfFin`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L175).

```lean
lemma succSuccAbove_apply_eq_orderIsoOfFin {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (m : Fin n) :
    (succSuccAbove i j) m = (Finset.orderIsoOfFin {i, j}ᶜ
      (by rw [Finset.card_compl]; simp [Finset.card_pair hij])) m
```

**`Fin.succSuccAbove_image_compl`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L180).

```lean
lemma succSuccAbove_image_compl {i j : Fin (n + 1 + 1)} (hij : i ≠ j)
    (X : Set (Fin n)) :
    (succSuccAbove i j) '' Xᶜ = ({i, j} ∪ succSuccAbove i j '' X)ᶜ
```

**`Fin.fst_ne_succSuccAbove_pre`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L188).

```lean
lemma fst_ne_succSuccAbove_pre (i j : Fin (n + 1 + 1)) (m : Fin n) :
    ¬ i = succSuccAbove i j m
```

**`Fin.succSuccAbove_ne_fst`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L194).

```lean
lemma succSuccAbove_ne_fst (i j : Fin (n + 1 + 1)) (m : Fin n) :
    ¬ succSuccAbove i j m = i
```

**`Fin.snd_ne_succSuccAbove_pre`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L200).

```lean
lemma snd_ne_succSuccAbove_pre (i j : Fin (n + 1 + 1)) (m : Fin n) :
    ¬ j = (succSuccAbove i j) m
```

**`Fin.succSuccAbove_ne_snd`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L206).

```lean
lemma succSuccAbove_ne_snd (i j : Fin (n + 1 + 1)) (m : Fin n) :
    ¬ succSuccAbove i j m = j
```

**`Fin.eq_or_exists_succSuccAbove`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L211).

```lean
lemma eq_or_exists_succSuccAbove(i j : Fin (n + 1 + 1)) (hij : i ≠ j) (m : Fin (n + 1 + 1)) :
    m = i ∨ m = j ∨ ∃ m', m = succSuccAbove i j m'
```

**`Fin.succSuccAbove_apply_lt_lt`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L221).

```lean
lemma succSuccAbove_apply_lt_lt {n : ℕ}
    (i j : Fin (n + 1 + 1)) (m : Fin n) (hi : m.val < i.val) (hj : m.val < j.val) :
    succSuccAbove i j m = m.castSucc.castSucc
```

**`Fin.succSuccAbove_natAdd_apply_castAdd`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L227).

```lean
lemma succSuccAbove_natAdd_apply_castAdd {n n1 : ℕ}
    (i j : Fin (n + 1 + 1)) (m : Fin n1) :
    (succSuccAbove (n := n1 + n) (Fin.natAdd n1 i) (Fin.natAdd n1 j))
    (Fin.castAdd n m) = Fin.castAdd (n + 1 + 1) (m)
```

**`Fin.succSuccAbove_castAdd_natAdd_apply_castAdd`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L238).

> Reinserting a left-block survivor `a` after removing the `i`-th slot of the left block and the
> `j`-th slot of the right block of `Fin ((nA + 1) + (nB + 1))`, the removal read at the contracted
> length `(nA + nB) + 1 + 1`. Unlike `succSuccAbove_natAdd_apply_castAdd` the two holes straddle the
> two blocks, so the statement carries the reshaping `Fin.cast`s.

```lean
lemma succSuccAbove_castAdd_natAdd_apply_castAdd {nA nB : ℕ} (i : Fin (nA + 1)) (j : Fin (nB + 1))
    (a : Fin nA) :
    Fin.cast (show (nA + nB) + 1 + 1 = (nA + 1) + (nB + 1) by omega)
        ((Fin.cast (show (nA + 1) + (nB + 1) = (nA + nB) + 1 + 1 by omega)
            (Fin.castAdd (nB + 1) i)).succSuccAbove
          (Fin.cast (show (nA + 1) + (nB + 1) = (nA + nB) + 1 + 1 by omega)
            (Fin.natAdd (nA + 1) j)) (Fin.castAdd nB a))
      = Fin.castAdd (nB + 1) (i.succAbove a)
```

**`Fin.succSuccAbove_castAdd_natAdd_apply_natAdd`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L253).

> Reinserting a right-block survivor, the mirror of
> `Fin.succSuccAbove_castAdd_natAdd_apply_castAdd`.

```lean
lemma succSuccAbove_castAdd_natAdd_apply_natAdd {nA nB : ℕ} (i : Fin (nA + 1)) (j : Fin (nB + 1))
    (a : Fin nB) :
    Fin.cast (show (nA + nB) + 1 + 1 = (nA + 1) + (nB + 1) by omega)
        ((Fin.cast (show (nA + 1) + (nB + 1) = (nA + nB) + 1 + 1 by omega)
            (Fin.castAdd (nB + 1) i)).succSuccAbove
          (Fin.cast (show (nA + 1) + (nB + 1) = (nA + nB) + 1 + 1 by omega)
            (Fin.natAdd (nA + 1) j)) (Fin.natAdd nA a))
      = Fin.natAdd (nA + 1) (j.succAbove a)
```

**`Fin.succSuccAbove_natAdd_image_range_castAdd`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L266).

```lean
lemma succSuccAbove_natAdd_image_range_castAdd {n n1 : ℕ}
    (i j : Fin (n + 1 + 1)) :
    (succSuccAbove (n := n1 + n) (Fin.natAdd n1 i) (Fin.natAdd n1 j)) ''
    (Set.range (Fin.castAdd (m := n) (n := n1))) = {i | i.1 < n1}
```

**`Fin.succSuccAbove_comm_natAdd`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L280).

```lean
lemma succSuccAbove_comm_natAdd {n n1 : ℕ}
    (i j : Fin (n + 1 + 1)) (m : Fin n) :
    succSuccAbove (n := n1 + n) (Fin.natAdd n1 i) (Fin.natAdd n1 j) (Fin.natAdd n1 m)
    = Fin.natAdd (n1) (succSuccAbove i j m)
```

## predPredAbove

**`Fin.predPredAbove`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L295).

> The preimage of `m` under `succSuccAbove i j hij` given that `m` is not equal
> to `i` or `j`.

```lean
def predPredAbove (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (m : Fin (n + 1 + 1))
    (hm : m ≠ i ∧ m ≠ j) : Fin n
```

**`Fin.predPredAbove_val`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L306).

```lean
lemma predPredAbove_val (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (m : Fin (n + 1 + 1))
    (hm : m ≠ i ∧ m ≠ j) :
    (predPredAbove i j hij m hm).val = if m.1 < i.1 ∧ m.1 < j.1 then m.1
    else if m.1 - 1 < i.1 ∧ j.1 ≤ m.1 then m.1 - 1
    else if i.1 - 1 ≤ m.1 ∧ m.1 < j.1 then m.1 - 1
    else m.1 - 2
```

**`Fin.succSuccAbove_predPredAbove`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L316).

```lean
lemma succSuccAbove_predPredAbove (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (m : Fin (n + 1 + 1))
    (hm : m ≠ i ∧ m ≠ j) :
    succSuccAbove i j (predPredAbove i j hij m hm) = m
```

**`Fin.predPredAbove_eq_orderIsoOfFin`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L322).

```lean
lemma predPredAbove_eq_orderIsoOfFin (i j : Fin (n + 1 + 1)) (hij : i ≠ j) (m : Fin (n + 1 + 1))
    (hm : m ≠ i ∧ m ≠ j) :
    predPredAbove i j hij m hm =
    (Finset.orderIsoOfFin {i, j}ᶜ (by rw [Finset.card_compl]; simp [Finset.card_pair hij])).symm
    ⟨m, by simp [hm]⟩
```

**`Fin.predPredAbove_injective`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L332).

```lean
lemma predPredAbove_injective (i j : Fin (n + 1 + 1)) (hij : i ≠ j)
    (m1 m2 : Fin (n + 1 + 1)) (hm1 : m1 ≠ i ∧ m1 ≠ j) (hm2 : m2 ≠ i ∧ m2 ≠ j) :
    predPredAbove i j hij m1 hm1 = predPredAbove i j hij m2 hm2 ↔ m1 = m2
```

**`Fin.predPredAbove_surjective`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L338).

```lean
lemma predPredAbove_surjective (i j : Fin (n + 1 + 1)) (hij : i ≠ j)
    (m : Fin n) : ∃ m' : Fin (n + 1 + 1), ∃ (h : m' ≠ i ∧ m' ≠ j),
    predPredAbove i j hij m' h = m
```

**`Fin.predPredAbove_succSuccAbove`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L345).

```lean
lemma predPredAbove_succSuccAbove (i j : Fin (n + 1 + 1)) (hij : i ≠ j)
    (m : Fin n) :
    predPredAbove i j hij (succSuccAbove i j m) (by simp) = m
```

## Commutativity of succSuccAbove

**`Fin.succSuccAbove_comm`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L356).

```lean
lemma succSuccAbove_comm (i1 j1 : Fin (n + 1 + 1 + 1 + 1)) (i2 j2 : Fin (n + 1 + 1))
    (hij1 : i1 ≠ j1) (hij2 : i2 ≠ j2) :
    let i2' := (succSuccAbove i1 j1 i2);
    let j2' := (succSuccAbove i1 j1 j2);
    have hi2j2' : i2' ≠ j2' := by simp [i2', j2', hij2];
    let i1' := (predPredAbove i2' j2' hi2j2' i1 (by simp [i2', j2']));
    let j1' := (predPredAbove i2' j2' hi2j2' j1 (by simp [i2', j2']));
    succSuccAbove i1 j1 ∘ succSuccAbove i2 j2 =
    succSuccAbove i2' j2' ∘ succSuccAbove i1' j1'
```

**`Fin.succSuccAbove_comm_apply`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L369).

```lean
lemma succSuccAbove_comm_apply (i1 j1 : Fin (n + 1 + 1 + 1 + 1)) (i2 j2 : Fin (n + 1 + 1))
    (hij1 : i1 ≠ j1) (hij2 : i2 ≠ j2) (m : Fin n) :
    let i2' := (succSuccAbove i1 j1 i2);
    let j2' := (succSuccAbove i1 j1 j2);
    have hi2j2' : i2' ≠ j2' := by simp [i2', j2', hij2];
    let i1' := (predPredAbove i2' j2' hi2j2' i1 (by simp [i2', j2']));
    let j1' := (predPredAbove i2' j2' hi2j2' j1 (by simp [i2', j2']));
    succSuccAbove i2' j2' (succSuccAbove i1' j1' m) =
    succSuccAbove i1 j1 (succSuccAbove i2 j2 m)
```

## funPredPredAbove

**`Fin.funPredPredAbove`**, a def, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L392).

> Given a bijection `Fin (n1 + 1 + 1) → Fin (n + 1 + 1))` and a pair `i j : Fin (n1 + 1 + 1)`,
> then `funPredPredAbove i j _ σ _ : Fin n1 → Fin n` corresponds to the induced bijection
> formed by dropping `i` and `j` in the source and their image in the target.

```lean
def funPredPredAbove {n n1 : ℕ} (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j)
    (σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1)) (hσ : Function.Bijective σ)
    (m : Fin n1) : Fin n
```

**`Fin.funPredPredAbove_injective`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L399).

```lean
lemma funPredPredAbove_injective {n n1 : ℕ} (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j)
    (σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1)) (hσ : Function.Bijective σ) :
    Function.Injective (funPredPredAbove i j hij σ hσ)
```

**`Fin.funPredPredAbove_surjective`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L405).

```lean
lemma funPredPredAbove_surjective {n n1 : ℕ} (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j)
    (σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1)) (hσ : Function.Bijective σ) :
    Function.Surjective (funPredPredAbove i j hij σ hσ)
```

**`Fin.funPredPredAbove_bijective`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L420).

```lean
lemma funPredPredAbove_bijective {n n1 : ℕ} (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j)
    (σ : Fin (n1 + 1 + 1) → Fin (n + 1 + 1)) (hσ : Function.Bijective σ) :
    Function.Bijective (funPredPredAbove i j hij σ hσ)
```

**`Fin.funPredPredAbove_id`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L428).

```lean
lemma funPredPredAbove_id { n1 : ℕ} (i j : Fin (n1 + 1 + 1)) (hij : i ≠ j) :
    funPredPredAbove i j hij id (Function.bijective_id) = id
```

**`Fin.succSuccAbove_succAbove_comm_apply`**, a lemma, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean#L434).

> Pointwise form of commuting deletion of one slot with deletion of a pair.

```lean
lemma succSuccAbove_succAbove_comm_apply {n : ℕ} (i j : Fin (n + 1 + 1 + 1))
    (k : Fin (n + 1)) (m : Fin n) :
    (i.succSuccAbove j k).succAbove
        (((Fin.predAbove 0 (i.succSuccAbove j k)).predAbove i).succSuccAbove
          ((Fin.predAbove 0 (i.succSuccAbove j k)).predAbove j) m) =
      i.succSuccAbove j (k.succAbove m)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/SuccSuccAbove.lean)
