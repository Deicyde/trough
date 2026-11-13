---
declaration: module
origin: cited
lean: PureU1.Sorted, PureU1.sort, PureU1.sort_sorted, PureU1.sort_perm, PureU1.sort_apply, PureU1.sort_zero, PureU1.sort_projection, PureU1.sortAFL
statement: formalized
proof: formalized
---

# Sort for Pure U(1) charges

The module `Physlib.QFT.QED.AnomalyCancellation.Sorts`, [Physlib/QFT/QED/AnomalyCancellation/Sorts.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean): 10 declarations, 3 with a docstring.

> We define the sort function for Pure U(1) charges, and prove some basic properties.

**`PureU1.Sorted`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L28).

> A charge is sorted if for all `i ≤ j`, then `S i ≤ S j`.

```lean
def Sorted {n : ℕ} (S : (PureU1 n).Charges) : Prop
```

**`PureU1.sort`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L33).

> Given a charge assignment `S`, the corresponding sorted charge assignment.

```lean
def sort {n : ℕ} (S : (PureU1 n).Charges) : (PureU1 n).Charges
```

**`PureU1.sort_sorted`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L36).

```lean
lemma sort_sorted {n : ℕ} (S : (PureU1 n).Charges) : Sorted (sort S)
```

**`PureU1.sort_perm`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L41).

```lean
lemma sort_perm {n : ℕ} (S : (PureU1 n).Charges) (M :(FamilyPermutations n).group) :
    sort ((FamilyPermutations n).rep M S) = sort S
```

**`PureU1.sort_apply`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L45).

```lean
lemma sort_apply {n : ℕ} (S : (PureU1 n).Charges) (j : Fin n) :
    sort S j = S ((Tuple.sort S) j)
```

**`PureU1.sort_zero`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L50).

```lean
lemma sort_zero {n : ℕ} (S : (PureU1 n).Charges) (hS : sort S = 0) : S = 0
```

**`PureU1.sort_projection`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L62).

```lean
lemma sort_projection {n : ℕ} (S : (PureU1 n).Charges) : sort (sort S) = sort S
```

**`PureU1.sortAFL`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L66).

> The sort function acting on `LinSols`.

```lean
def sortAFL {n : ℕ} (S : (PureU1 n).LinSols) : (PureU1 n).LinSols
```

**`PureU1.sortAFL_val`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L69).

```lean
lemma sortAFL_val {n : ℕ} (S : (PureU1 n).LinSols) : (sortAFL S).val = sort S.val
```

**`PureU1.sortAFL_zero`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean#L72).

```lean
lemma sortAFL_zero {n : ℕ} (S : (PureU1 n).LinSols) (hS : sortAFL S = 0) : S = 0
```

## Depends on

- [Permutations of Pure U(1) ACC](anomalycancellation-permutations.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Sorts.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Sorts.lean)
