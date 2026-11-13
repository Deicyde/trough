---
declaration: module
origin: cited
lean: PureU1.ConstAbsProp, PureU1.ConstAbs, PureU1.constAbs_perm, PureU1.constAbs_sort, PureU1.ConstAbsSorted, PureU1.ConstAbsSorted.lt_eq, PureU1.ConstAbsSorted.val_le_zero, PureU1.ConstAbsSorted.gt_eq
statement: formalized
proof: formalized
---

# Charges assignments with constant abs

The module `Physlib.QFT.QED.AnomalyCancellation.ConstAbs`, [Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean): 32 declarations, 5 with a docstring.

> We look at charge assignments in which all charges have the same absolute value.

**`PureU1.ConstAbsProp`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L27).

> The condition for two rationals to have the same square (equivalent to same abs).

```lean
def ConstAbsProp : ℚ × ℚ → Prop
```

**`PureU1.ConstAbs`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L31).

> The condition on a charge assignment `S` to have constant absolute value among charges.

```lean
def ConstAbs (S : (PureU1 n).Charges) : Prop
```

**`PureU1.constAbs_perm`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L34).

```lean
lemma constAbs_perm (S : (PureU1 n).Charges) (M :(FamilyPermutations n).group) :
    ConstAbs ((FamilyPermutations n).rep M S) ↔ ConstAbs S
```

**`PureU1.constAbs_sort`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L44).

```lean
lemma constAbs_sort {S : (PureU1 n).Charges} (CA : ConstAbs S) : ConstAbs (sort S)
```

**`PureU1.ConstAbsSorted`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L49).

> The condition for a set of charges to be `sorted`, and have `constAbs`

```lean
def ConstAbsSorted (S : (PureU1 n).Charges) : Prop
```

**`PureU1.ConstAbsSorted.lt_eq`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L58).

```lean
lemma lt_eq {k i : Fin n.succ} (hk : S k ≤ 0) (hik : i ≤ k) : S i = S k
```

**`PureU1.ConstAbsSorted.val_le_zero`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L67).

```lean
lemma val_le_zero {i : Fin n.succ} (hi : S i ≤ 0) : S i = S (0 : Fin n.succ)
```

**`PureU1.ConstAbsSorted.gt_eq`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L73).

```lean
lemma gt_eq {k i: Fin n.succ} (hk : 0 ≤ S k) (hik : k ≤ i) : S i = S k
```

**`PureU1.ConstAbsSorted.zero_gt`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L82).

```lean
lemma zero_gt (h0 : 0 ≤ S (0 : Fin n.succ)) (i : Fin n.succ) : S (0 : Fin n.succ) = S i
```

**`PureU1.ConstAbsSorted.opposite_signs_eq_neg`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L87).

```lean
lemma opposite_signs_eq_neg {i j : Fin n.succ} (hi : S i ≤ 0) (hj : 0 ≤ S j) : S i = - S j
```

**`PureU1.ConstAbsSorted.is_zero`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L96).

```lean
lemma is_zero (h0 : S (0 : Fin n.succ) = 0) : S = 0
```

**`PureU1.ConstAbsSorted.Boundary`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L107).

> A boundary of `S : (PureU1 n.succ).charges` (assumed sorted, constAbs and non-zero)
> is defined as a element of `k ∈ Fin n` such that `S k.castSucc` and `S k.succ` are different signs.

```lean
def Boundary (S : (PureU1 n.succ).Charges) (k : Fin n) : Prop
```

**`PureU1.ConstAbsSorted.boundary_castSucc`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L110).

```lean
lemma boundary_castSucc {k : Fin n} (hk : Boundary S k) : S k.castSucc = S (0 : Fin n.succ)
```

**`PureU1.ConstAbsSorted.boundary_succ`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L114).

```lean
lemma boundary_succ {k : Fin n} (hk : Boundary S k) : S k.succ = - S (0 : Fin n.succ)
```

**`PureU1.ConstAbsSorted.boundary_split`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L119).

```lean
lemma boundary_split (k : Fin n) : k.succ.val + (n.succ - k.succ.val) = n.succ
```

**`PureU1.ConstAbsSorted.boundary_accGrav'`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L123).

```lean
lemma boundary_accGrav' (k : Fin n) : accGrav n.succ S =
    ∑ i : Fin (k.succ.val + (n.succ - k.succ.val)), S (Fin.cast (boundary_split k) i)
```

**`PureU1.ConstAbsSorted.boundary_accGrav''`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L133).

```lean
lemma boundary_accGrav'' (k : Fin n) (hk : Boundary S k) :
    accGrav n.succ S = (2 * ↑↑k + 1 - ↑n) * S (0 : Fin n.succ)
```

**`PureU1.ConstAbsSorted.HasBoundary`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L151).

> A `S ∈ charges` has a boundary if there exists a `k ∈ Fin n` which is a boundary.

```lean
def HasBoundary (S : (PureU1 n.succ).Charges) : Prop
```

**`PureU1.ConstAbsSorted.not_hasBoundary_zero_le`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L155).

```lean
lemma not_hasBoundary_zero_le (hnot : ¬ (HasBoundary S)) (h0 : S (0 : Fin n.succ) < 0) :
    ∀ i, S (0 : Fin n.succ) = S i
```

**`PureU1.ConstAbsSorted.not_hasBoundry_zero`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L168).

```lean
lemma not_hasBoundry_zero (hnot : ¬ (HasBoundary S)) (i : Fin n.succ) :
    S (0 : Fin n.succ) = S i
```

**`PureU1.ConstAbsSorted.not_hasBoundary_grav`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L176).

```lean
lemma not_hasBoundary_grav (hnot : ¬ (HasBoundary S)) :
    accGrav n.succ S = n.succ * S (0 : Fin n.succ)
```

**`PureU1.ConstAbsSorted.AFL_hasBoundary`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L181).

```lean
lemma AFL_hasBoundary (h : A.val (0 : Fin n.succ) ≠ 0) : HasBoundary A.val
```

**`PureU1.ConstAbsSorted.AFL_odd_noBoundary`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L191).

```lean
lemma AFL_odd_noBoundary {A : (PureU1 (2 * n + 1)).LinSols} (h : ConstAbsSorted A.val)
    (hA : A.val (0 : Fin (2*n +1)) ≠ 0) : ¬ HasBoundary A.val
```

**`PureU1.ConstAbsSorted.AFL_odd_zero`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L205).

```lean
lemma AFL_odd_zero {A : (PureU1 (2 * n + 1)).LinSols} (h : ConstAbsSorted A.val) :
    A.val (0 : Fin (2 * n + 1)) = 0
```

**`PureU1.ConstAbsSorted.AFL_odd`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L210).

```lean
lemma AFL_odd (A : (PureU1 (2 * n + 1)).LinSols) (h : ConstAbsSorted A.val) :
    A = 0
```

**`PureU1.ConstAbsSorted.AFL_even_Boundary`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L215).

```lean
lemma AFL_even_Boundary {A : (PureU1 (2 * n.succ)).LinSols} (h : ConstAbsSorted A.val)
    (hA : A.val (0 : Fin (2 * n.succ)) ≠ 0) {k : Fin (2 * n + 1)} (hk : Boundary A.val k) :
    k.val = n
```

**`PureU1.ConstAbsSorted.AFL_even_below'`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L228).

```lean
lemma AFL_even_below' {A : (PureU1 (2 * n.succ)).LinSols} (h : ConstAbsSorted A.val)
    (hA : A.val (0 : Fin (2 * n.succ)) ≠ 0) (i : Fin n.succ) :
    A.val (Fin.cast (split_equal n.succ) (Fin.castAdd n.succ i)) = A.val (0 : Fin (2*n.succ))
```

**`PureU1.ConstAbsSorted.AFL_even_below`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L239).

```lean
lemma AFL_even_below (A : (PureU1 (2 * n.succ)).LinSols) (h : ConstAbsSorted A.val)
    (i : Fin n.succ) :
    A.val (Fin.cast (split_equal n.succ) (Fin.castAdd n.succ i))
    = A.val (0 : Fin (2*n.succ))
```

**`PureU1.ConstAbsSorted.AFL_even_above'`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L249).

```lean
lemma AFL_even_above' {A : (PureU1 (2 * n.succ)).LinSols} (h : ConstAbsSorted A.val)
    (hA : A.val (0 : Fin (2*n.succ)) ≠ 0) (i : Fin n.succ) :
    A.val (Fin.cast (split_equal n.succ) (Fin.natAdd n.succ i)) =
    - A.val (0 : Fin (2*n.succ))
```

**`PureU1.ConstAbsSorted.AFL_even_above`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L261).

```lean
lemma AFL_even_above (A : (PureU1 (2 * n.succ)).LinSols) (h : ConstAbsSorted A.val)
    (i : Fin n.succ) :
    A.val (Fin.cast (split_equal n.succ) (Fin.natAdd n.succ i)) =
    - A.val (0 : Fin (2 * n.succ))
```

**`PureU1.ConstAbs.boundary_value_odd`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L276).

```lean
lemma boundary_value_odd (S : (PureU1 (2 * n + 1)).LinSols) (hs : ConstAbs S.val) :
    S = 0
```

**`PureU1.ConstAbs.boundary_value_even`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean#L281).

```lean
lemma boundary_value_even (S : (PureU1 (2 * n.succ)).LinSols) (hs : ConstAbs S.val) :
    VectorLikeEven S.val
```

## Depends on

- [Vector like charges](anomalycancellation-vectorlike.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/ConstAbs.lean)
