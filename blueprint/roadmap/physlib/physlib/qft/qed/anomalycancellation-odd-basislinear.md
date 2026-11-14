---
declaration: module
origin: cited
lean: PureU1.VectorLikeOddPlane.odd_shift_eq, PureU1.VectorLikeOddPlane.oddFst, PureU1.VectorLikeOddPlane.oddSnd, PureU1.VectorLikeOddPlane.oddMid, PureU1.VectorLikeOddPlane.sum_odd, PureU1.VectorLikeOddPlane.oddShiftFst, PureU1.VectorLikeOddPlane.oddShiftSnd, PureU1.VectorLikeOddPlane.oddShiftZero
statement: formalized
proof: formalized
---

# Splitting the linear solutions in the odd case into two ACC-satisfying planes

The module `Physlib.QFT.QED.AnomalyCancellation.Odd.BasisLinear`, [Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean): 87 declarations, 23 with a docstring.

## i. Overview

> We split the linear solutions of `PureU1 (2 * n + 1)` into two planes,
> where every point in either plane satisfies both the linear and cubic anomaly cancellation
> conditions.

## ii. Key results

> - `Unshifted.planeLinSols` : The inclusion of the unshifted plane into linear solutions
> - `Unshifted.planeCharges_accCube` : The statement that charges from the unshifted plane
>   satisfy the cubic ACC
> - `Shifted.planeLinSols` : The inclusion of the shifted plane.
> - `Shifted.planeCharges_accCube` : The statement that charges from the shifted plane
>   satisfy the cubic ACC
> - `span_basis` : Every linear solution is the sum of a point from each plane.

## iv. References

> * https://arxiv.org/pdf/1912.04804.pdf. [ref: arxiv\_1912\_04804]

## A. Splitting the charges up into groups

> We have `2 * n + 1` charges, which we split up in the following ways:
>
> `| evenFst j (0 to n) | evenSnd j (n.succ to n + n.succ)|`
>
> ```
> | evenShiftZero (0) | evenShiftFst j (1 to n) |
>   evenShiftSnd j (n.succ to 2 * n) | evenShiftLast (2 * n.succ - 1) |
> ```

### A.1. The symmetric split: Spltting the charges up via `(n + 1) + 1`

**`PureU1.VectorLikeOddPlane.odd_shift_eq`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L110).

```lean
lemma odd_shift_eq (n : ℕ) : (1 + n) + n = 2 * n +1
```

**`PureU1.VectorLikeOddPlane.oddFst`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L115).

> The inclusion of `Fin n` into `Fin ((n + 1) + n)` via the first `n`.
> This is then casted to `Fin (2 * n + 1)`.

```lean
def oddFst (j : Fin n) : Fin (2 * n + 1)
```

**`PureU1.VectorLikeOddPlane.oddSnd`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L120).

> The inclusion of `Fin n` into `Fin ((n + 1) + n)` via the second `n`.
> This is then casted to `Fin (2 * n + 1)`.

```lean
def oddSnd (j : Fin n) : Fin (2 * n + 1)
```

**`PureU1.VectorLikeOddPlane.oddMid`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L125).

> The element representing `1` in `Fin ((n + 1) + n)`.
> This is then casted to `Fin (2 * n + 1)`.

```lean
def oddMid : Fin (2 * n + 1)
```

**`PureU1.VectorLikeOddPlane.sum_odd`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L128).

```lean
lemma sum_odd (S : Fin (2 * n + 1) → ℚ) :
    ∑ i, S i = S oddMid + ∑ i : Fin n, ((S ∘ oddFst) i + (S ∘ oddSnd) i)
```

### A.2. The shifted split: Spltting the charges up via `1 + n + n`

**`PureU1.VectorLikeOddPlane.oddShiftFst`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L147).

> The inclusion of `Fin n` into `Fin (1 + n + n)` via the first `n`.
> This is then casted to `Fin (2 * n + 1)`.

```lean
def oddShiftFst (j : Fin n) : Fin (2 * n + 1)
```

**`PureU1.VectorLikeOddPlane.oddShiftSnd`**, a def, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L152).

> The inclusion of `Fin n` into `Fin (1 + n + n)` via the second `n`.
> This is then casted to `Fin (2 * n + 1)`.

```lean
def oddShiftSnd (j : Fin n) : Fin (2 * n + 1)
```

**`PureU1.VectorLikeOddPlane.oddShiftZero`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L157).

> The element representing the `1` in `Fin (1 + n + n)`.
> This is then casted to `Fin (2 * n + 1)`.

```lean
def oddShiftZero : Fin (2 * n + 1)
```

**`PureU1.VectorLikeOddPlane.sum_oddShift`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L160).

```lean
lemma sum_oddShift (S : Fin (2 * n + 1) → ℚ) :
    ∑ i, S i = S oddShiftZero + ∑ i : Fin n, ((S ∘ oddShiftFst) i + (S ∘ oddShiftSnd) i)
```

### A.3. The shifted shifted split: Spltting the charges up via `((1+n)+1) + n.succ`

**`PureU1.VectorLikeOddPlane.odd_shift_shift_eq`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L175).

```lean
lemma odd_shift_shift_eq (n : ℕ) : ((1+n)+1) + n.succ = 2 * n.succ + 1
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftZero`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L180).

> The element representing the first `1` in `Fin (1 + n + 1 + n.succ)` casted
> to `Fin (2 * n.succ + 1)`.

```lean
def oddShiftShiftZero : Fin (2 * n.succ + 1)
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftFst`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L185).

> The inclusion of `Fin n` into `Fin (1 + n + 1 + n.succ)` via the first `n` and casted
> to `Fin (2 * n.succ + 1)`.

```lean
def oddShiftShiftFst (j : Fin n) : Fin (2 * n.succ + 1)
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftMid`**, a def, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L190).

> The element representing the second `1` in `Fin (1 + n + 1 + n.succ)` casted
> to `2 * n.succ + 1`.

```lean
def oddShiftShiftMid : Fin (2 * n.succ + 1)
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftSnd`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L195).

> The inclusion of `Fin n.succ` into `Fin (1 + n + 1 + n.succ)` via the `n.succ` and casted
> to `Fin (2 * n.succ + 1)`.

```lean
def oddShiftShiftSnd (j : Fin n.succ) : Fin (2 * n.succ + 1)
```

### A.4. Relating the splittings together

**`PureU1.VectorLikeOddPlane.oddShiftShiftZero_eq_oddFst_zero`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L203).

```lean
lemma oddShiftShiftZero_eq_oddFst_zero : @oddShiftShiftZero n = oddFst 0
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftZero_eq_oddShiftZero`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L206).

```lean
lemma oddShiftShiftZero_eq_oddShiftZero : @oddShiftShiftZero n = oddShiftZero
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftFst_eq_oddFst_succ`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L208).

```lean
lemma oddShiftShiftFst_eq_oddFst_succ (j : Fin n) :
    oddShiftShiftFst j = oddFst j.succ
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftFst_eq_oddShiftFst_castSucc`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L214).

```lean
lemma oddShiftShiftFst_eq_oddShiftFst_castSucc (j : Fin n) :
    oddShiftShiftFst j = oddShiftFst j.castSucc
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftMid_eq_oddMid`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L218).

```lean
lemma oddShiftShiftMid_eq_oddMid : @oddShiftShiftMid n = oddMid
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftMid_eq_oddShiftFst_last`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L223).

```lean
lemma oddShiftShiftMid_eq_oddShiftFst_last : oddShiftShiftMid = oddShiftFst (Fin.last n)
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftSnd_eq_oddSnd`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L226).

```lean
lemma oddShiftShiftSnd_eq_oddSnd (j : Fin n.succ) : oddShiftShiftSnd j = oddSnd j
```

**`PureU1.VectorLikeOddPlane.oddShiftShiftSnd_eq_oddShiftSnd`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L231).

```lean
lemma oddShiftShiftSnd_eq_oddShiftSnd (j : Fin n.succ) : oddShiftShiftSnd j = oddShiftSnd j
```

**`PureU1.VectorLikeOddPlane.oddSnd_eq_oddShiftSnd`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L235).

```lean
lemma oddSnd_eq_oddShiftSnd (j : Fin n) : oddSnd j = oddShiftSnd j
```

**`PureU1.VectorLikeOddPlane.oddShiftZero_eq_oddFst`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L239).

```lean
lemma oddShiftZero_eq_oddFst : oddShiftZero = oddFst (0 : Fin n.succ)
```

**`PureU1.VectorLikeOddPlane.oddShiftFst_castSucc_eq_oddFst_succ`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L242).

```lean
lemma oddShiftFst_castSucc_eq_oddFst_succ (j : Fin n) :
    oddShiftFst j.castSucc = oddFst j.succ
```

**`PureU1.VectorLikeOddPlane.oddShiftFst_last_eq_oddMid`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L248).

```lean
lemma oddShiftFst_last_eq_oddMid : oddShiftFst (Fin.last n) = oddMid
```

**`PureU1.VectorLikeOddPlane.oddShiftSnd_eq_oddSnd`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L253).

```lean
lemma oddShiftSnd_eq_oddSnd (j : Fin n) : oddShiftSnd j = oddSnd j
```

## B. The unshifted plane

### B.1. The basis vectors of the unshifted plane as charges

**`PureU1.VectorLikeOddPlane.Unshifted.basisAsCharges`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L275).

> The unshifted part of the basis as charge assignments.

```lean
def basisAsCharges (j : Fin n) : (PureU1 (2 * n + 1)).Charges
```

### B.2. Components of the basis vectors as charges

**`PureU1.VectorLikeOddPlane.Unshifted.basis_on_oddFst_self`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L292).

```lean
lemma basis_on_oddFst_self (j : Fin n) : basisAsCharges j (oddFst j) = 1
```

**`PureU1.VectorLikeOddPlane.Unshifted.basis_on_oddFst_other`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L296).

```lean
lemma basis_on_oddFst_other {k j : Fin n} (h : k ≠ j) :
    basisAsCharges k (oddFst j) = 0
```

**`PureU1.VectorLikeOddPlane.Unshifted.basis_on_other`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L308).

```lean
lemma basis_on_other {k : Fin n} {j : Fin (2 * n + 1)} (h1 : j ≠ oddFst k) (h2 : j ≠ oddSnd k) :
    basisAsCharges k j = 0
```

**`PureU1.VectorLikeOddPlane.Unshifted.basis_oddSnd_eq_minus_oddFst`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L313).

```lean
lemma basis_oddSnd_eq_minus_oddFst (j i : Fin n) :
    basisAsCharges j (oddSnd i) = - basisAsCharges j (oddFst i)
```

**`PureU1.VectorLikeOddPlane.Unshifted.basis_on_oddSnd_self`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L319).

```lean
lemma basis_on_oddSnd_self (j : Fin n) : basisAsCharges j (oddSnd j) = - 1
```

**`PureU1.VectorLikeOddPlane.Unshifted.basis_on_oddSnd_other`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L322).

```lean
lemma basis_on_oddSnd_other {k j : Fin n} (h : k ≠ j) : basisAsCharges k (oddSnd j) = 0
```

**`PureU1.VectorLikeOddPlane.Unshifted.basis_on_oddMid`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L327).

```lean
lemma basis_on_oddMid (j : Fin n) : basisAsCharges j oddMid = 0
```

### B.3. The basis vectors satisfy the linear ACCs

**`PureU1.VectorLikeOddPlane.Unshifted.basis_linearACC`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L343).

```lean
lemma basis_linearACC (j : Fin n) : (accGrav (2 * n + 1)) (basisAsCharges j) = 0
```

### B.4. The basis vectors as `LinSols`

**`PureU1.VectorLikeOddPlane.Unshifted.basis`**, a def, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L355).

> The unshifted part of the basis as `LinSols`.

```lean
def basis (j : Fin n) : (PureU1 (2 * n + 1)).LinSols
```

### B.5. The inclusion of the unshifted plane into charges

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges`**, a def, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L368).

> A point in the span of the unshifted part of the basis as a charge.

```lean
def planeCharges (f : Fin n → ℚ) : (PureU1 (2 * n + 1)).Charges
```

### B.6. Components of the unshifted plane

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges_oddFst`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L376).

```lean
lemma planeCharges_oddFst (f : Fin n → ℚ) (j : Fin n) : planeCharges f (oddFst j) = f j
```

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges_oddSnd`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L384).

```lean
lemma planeCharges_oddSnd (f : Fin n → ℚ) (j : Fin n) : planeCharges f (oddSnd j) = - f j
```

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges_oddMid`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L392).

```lean
lemma planeCharges_oddMid (f : Fin n → ℚ) : planeCharges f oddMid = 0
```

### B.7. Points on the unshifted plane satisfies the ACCs

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges_linearACC`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L403).

```lean
lemma planeCharges_linearACC (f : Fin n → ℚ) : (accGrav (2 * n + 1)) (planeCharges f) = 0
```

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges_accCube`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L408).

```lean
lemma planeCharges_accCube (f : Fin n → ℚ) : accCube (2 * n +1) (planeCharges f) = 0
```

### B.8. Kernel of the inclusion into charges

**`PureU1.VectorLikeOddPlane.Unshifted.planeCharges_zero`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L421).

```lean
lemma planeCharges_zero (f : Fin n → ℚ) (h : planeCharges f = 0) : ∀ i, f i = 0
```

**`PureU1.VectorLikeOddPlane.Unshifted.planeLinSols`**, a def, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L425).

> A point in the span of the unshifted part of the basis.

```lean
def planeLinSols (f : Fin n → ℚ) : (PureU1 (2 * n + 1)).LinSols
```

**`PureU1.VectorLikeOddPlane.Unshifted.planeLinSols_val`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L428).

```lean
lemma planeLinSols_val (f : Fin n → ℚ) : (planeLinSols f).val = planeCharges f
```

### B.9. The basis vectors are linearly independent

**`PureU1.VectorLikeOddPlane.Unshifted.basis_linear_independent`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L440).

```lean
lemma basis_linear_independent : LinearIndependent ℚ (@basis n)
```

## C. The shifted plane

### C.1. The basis vectors of the shifted plane as charges

**`PureU1.VectorLikeOddPlane.Shifted.basisAsCharges`**, a def, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L464).

> The shifted part of the basis as charge assignments.

```lean
def basisAsCharges (j : Fin n) : (PureU1 (2 * n + 1)).Charges
```

### C.2. Components of the basis vectors as charges

**`PureU1.VectorLikeOddPlane.Shifted.basis_on_oddShiftFst_self`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L481).

```lean
lemma basis_on_oddShiftFst_self (j : Fin n) : basisAsCharges j (oddShiftFst j) = 1
```

**`PureU1.VectorLikeOddPlane.Shifted.basis_on_oddShiftFst_other`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L485).

```lean
lemma basis_on_oddShiftFst_other {k j : Fin n} (h : k ≠ j) :
    basisAsCharges k (oddShiftFst j) = 0
```

**`PureU1.VectorLikeOddPlane.Shifted.basis_on_other`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L497).

```lean
lemma basis_on_other {k : Fin n} {j : Fin (2 * n + 1)}
    (h1 : j ≠ oddShiftFst k) (h2 : j ≠ oddShiftSnd k) :
    basisAsCharges k j = 0
```

**`PureU1.VectorLikeOddPlane.Shifted.basis_oddShiftSnd_eq_minus_oddShiftFst`**, a lemma, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L503).

```lean
lemma basis_oddShiftSnd_eq_minus_oddShiftFst (j i : Fin n) :
    basisAsCharges j (oddShiftSnd i) = - basisAsCharges j (oddShiftFst i)
```

**`PureU1.VectorLikeOddPlane.Shifted.basis_on_oddShiftSnd_self`**, a lemma, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L509).

```lean
lemma basis_on_oddShiftSnd_self (j : Fin n) : basisAsCharges j (oddShiftSnd j) = - 1
```

**`PureU1.VectorLikeOddPlane.Shifted.basis_on_oddShiftSnd_other`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L512).

```lean
lemma basis_on_oddShiftSnd_other {k j : Fin n} (h : k ≠ j) :
    basisAsCharges k (oddShiftSnd j) = 0
```

**`PureU1.VectorLikeOddPlane.Shifted.basis_on_oddShiftZero`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L518).

```lean
lemma basis_on_oddShiftZero (j : Fin n) : basisAsCharges j oddShiftZero = 0
```

### C.3. The basis vectors satisfy the linear ACCs

**`PureU1.VectorLikeOddPlane.Shifted.basis_linearACC`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L534).

```lean
lemma basis_linearACC (j : Fin n) : (accGrav (2 * n + 1)) (basisAsCharges j) = 0
```

### C.4. The basis vectors as `LinSols`

**`PureU1.VectorLikeOddPlane.Shifted.basis`**, a def, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L546).

> The shifted part of the basis as `LinSols`.

```lean
def basis (j : Fin n) : (PureU1 (2 * n + 1)).LinSols
```

### C.5. Permutations equal adding basis vectors

**`PureU1.VectorLikeOddPlane.Shifted.swap_as_add`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L561).

> Swapping the elements oddShiftFst j and oddShiftSnd j is equivalent to adding a vector
> basisAsCharges j.

```lean
lemma swap_as_add {S S' : (PureU1 (2 * n + 1)).LinSols} (j : Fin n)
    (hS : ((FamilyPermutations (2 * n + 1)).linSolRep
    (Equiv.swap (oddShiftFst j) (oddShiftSnd j))) S = S') :
    S'.val = S.val + (S.val (oddShiftSnd j) - S.val (oddShiftFst j)) • basisAsCharges j
```

### C.6. The inclusion of the shifted plane into charges

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges`**, a def, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L585).

> A point in the span of the shifted part of the basis as a charge.

```lean
def planeCharges (f : Fin n → ℚ) : (PureU1 (2 * n + 1)).Charges
```

### C.7. Components of the shifted plane

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges_oddShiftFst`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L593).

```lean
lemma planeCharges_oddShiftFst (f : Fin n → ℚ) (j : Fin n) :
    planeCharges f (oddShiftFst j) = f j
```

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges_oddShiftSnd`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L602).

```lean
lemma planeCharges_oddShiftSnd (f : Fin n → ℚ) (j : Fin n) :
    planeCharges f (oddShiftSnd j) = - f j
```

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges_oddShiftZero`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L611).

```lean
lemma planeCharges_oddShiftZero (f : Fin n → ℚ) : planeCharges f oddShiftZero = 0
```

### C.8. Points on the shifted plane satisfies the ACCs

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges_linearACC`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L622).

```lean
lemma planeCharges_linearACC (f : Fin n → ℚ) : (accGrav (2 * n + 1)) (planeCharges f) = 0
```

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges_accCube`**, a lemma, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L627).

```lean
lemma planeCharges_accCube (f : Fin n → ℚ) : accCube (2 * n +1) (planeCharges f) = 0
```

### C.9. Kernel of the inclusion into charges

**`PureU1.VectorLikeOddPlane.Shifted.planeCharges_zero`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L640).

```lean
lemma planeCharges_zero (f : Fin n → ℚ) (h : planeCharges f = 0) : ∀ i, f i = 0
```

### C.10. The inclusion of the shifted plane into LinSols

**`PureU1.VectorLikeOddPlane.Shifted.planeLinSols`**, a def, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L650).

> A point in the span of the shifted part of the basis.

```lean
def planeLinSols (f : Fin n → ℚ) : (PureU1 (2 * n + 1)).LinSols
```

**`PureU1.VectorLikeOddPlane.Shifted.planeLinSols_val`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L653).

```lean
lemma planeLinSols_val (f : Fin n → ℚ) : (planeLinSols f).val = planeCharges f
```

### C.11. The basis vectors are linearly independent

**`PureU1.VectorLikeOddPlane.Shifted.basis_linear_independent`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L665).

```lean
lemma basis_linear_independent : LinearIndependent ℚ (@basis n)
```

## D. The mixed cubic ACC from points in both planes

**`PureU1.VectorLikeOddPlane.P_P_P!_accCube`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L680).

```lean
lemma P_P_P!_accCube (g : Fin n → ℚ) (j : Fin n) :
    accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
      (Shifted.basisAsCharges j)
    = (Unshifted.planeCharges g (oddShiftFst j))^2 - (g j)^2
```

## E. The combined Unshifted.basis

### E.1. The combined Unshifted.basis as `LinSols`

**`PureU1.VectorLikeOddPlane.basisa`**, a def, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L708).

> The whole Unshifted.basis as `LinSols`.

```lean
def basisa : Fin n ⊕ Fin n → (PureU1 (2 * n + 1)).LinSols
```

### E.2. The inclusion of the span of the combined Unshifted.basis into charges

**`PureU1.VectorLikeOddPlane.Pa`**, a def, [line 720](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L720).

> A point in the span of the Unshifted.basis as a charge.

```lean
def Pa (f : Fin n → ℚ) (g : Fin n → ℚ) : (PureU1 (2 * n + 1)).Charges
```

### E.3. Components of the inclusion

**`PureU1.VectorLikeOddPlane.Pa_oddShiftShiftZero`**, a lemma, [line 730](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L730).

```lean
lemma Pa_oddShiftShiftZero (f g : Fin n.succ → ℚ) : Pa f g oddShiftShiftZero = f 0
```

**`PureU1.VectorLikeOddPlane.Pa_oddShiftShiftFst`**, a lemma, [line 739](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L739).

```lean
lemma Pa_oddShiftShiftFst (f g : Fin n.succ → ℚ) (j : Fin n) :
    Pa f g (oddShiftShiftFst j) = f j.succ + g j.castSucc
```

**`PureU1.VectorLikeOddPlane.Pa_oddShiftShiftMid`**, a lemma, [line 749](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L749).

```lean
lemma Pa_oddShiftShiftMid (f g : Fin n.succ → ℚ) : Pa f g oddShiftShiftMid = g (Fin.last n)
```

**`PureU1.VectorLikeOddPlane.Pa_oddShiftShiftSnd`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L758).

```lean
lemma Pa_oddShiftShiftSnd (f g : Fin n.succ → ℚ) (j : Fin n.succ) :
    Pa f g (oddShiftShiftSnd j) = - f j - g j
```

### E.4. Kernel of the inclusion into charges

**`PureU1.VectorLikeOddPlane.Pa_zero`**, a lemma, [line 773](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L773).

```lean
lemma Pa_zero (f g : Fin n.succ → ℚ) (h : Pa f g = 0) :
    ∀ i, f i = 0
```

**`PureU1.VectorLikeOddPlane.Pa_zero!`**, a lemma, [line 794](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L794).

```lean
lemma Pa_zero! (f g : Fin n.succ → ℚ) (h : Pa f g = 0) :
    ∀ i, g i = 0
```

### E.5. The inclusion of the span of the combined Unshifted.basis into LinSols

**`PureU1.VectorLikeOddPlane.Pa'`**, a def, [line 808](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L808).

> A point in the span of the whole Unshifted.basis.

```lean
def Pa' (f : (Fin n) ⊕ (Fin n) → ℚ) : (PureU1 (2 * n + 1)).LinSols
```

**`PureU1.VectorLikeOddPlane.Pa'_P'_P!'`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L811).

```lean
lemma Pa'_P'_P!' (f : (Fin n) ⊕ (Fin n) → ℚ) :
    Pa' f = Unshifted.planeLinSols (f ∘ Sum.inl) + Shifted.planeLinSols (f ∘ Sum.inr)
```

### E.6. The combined Unshifted.basis vectors are linearly independent

**`PureU1.VectorLikeOddPlane.basisa_linear_independent`**, a lemma, [line 821](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L821).

```lean
lemma basisa_linear_independent : LinearIndependent ℚ (@basisa n.succ)
```

### E.7. Injectivity of the inclusion into linear solutions

**`PureU1.VectorLikeOddPlane.Pa'_eq`**, a lemma, [line 843](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L843).

```lean
lemma Pa'_eq (f f' : (Fin n.succ) ⊕ (Fin n.succ) → ℚ) : Pa' f = Pa' f' ↔ f = f'
```

**`PureU1.VectorLikeOddPlane.Pa'_elim_eq_iff`**, a lemma, [line 856](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L856).

```lean
lemma Pa'_elim_eq_iff (g g' : Fin n.succ → ℚ) (f f' : Fin n.succ → ℚ) :
    Pa' (Sum.elim g f) = Pa' (Sum.elim g' f') ↔ Pa g f = Pa g' f'
```

**`PureU1.VectorLikeOddPlane.Pa_eq`**, a lemma, [line 867](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L867).

```lean
lemma Pa_eq (g g' : Fin n.succ → ℚ) (f f' : Fin n.succ → ℚ) :
    Pa g f = Pa g' f' ↔ g = g' ∧ f = f'
```

### E.8. Cardinality of the Unshifted.basis

**`PureU1.VectorLikeOddPlane.basisa_card`**, a lemma, [line 879](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L879).

```lean
lemma basisa_card : Fintype.card ((Fin n.succ) ⊕ (Fin n.succ)) =
    Module.finrank ℚ (PureU1 (2 * n.succ + 1)).LinSols
```

### E.9. The Unshifted.basis vectors as a Unshifted.basis

**`PureU1.VectorLikeOddPlane.basisaAsBasis`**, a def, [line 891](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L891).

> The Unshifted.basis formed out of our basisa vectors.

```lean
noncomputable def basisaAsBasis :
    Basis (Fin n.succ ⊕ Fin n.succ) ℚ (PureU1 (2 * n.succ + 1)).LinSols
```

## F. Every Lienar solution is the sum of a point from each plane

**`PureU1.VectorLikeOddPlane.span_basis`**, a lemma, [line 901](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L901).

```lean
lemma span_basis (S : (PureU1 (2 * n.succ + 1)).LinSols) :
    ∃ (g f : Fin n.succ → ℚ), S.val = Unshifted.planeCharges g + Shifted.planeCharges f
```

### F.1. Relation under permutations

**`PureU1.VectorLikeOddPlane.span_basis_swap!`**, a lemma, [line 920](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean#L920).

```lean
lemma span_basis_swap! {S : (PureU1 (2 * n.succ + 1)).LinSols} (j : Fin n.succ)
    (hS : ((FamilyPermutations (2 * n.succ + 1)).linSolRep
    (Equiv.swap (oddShiftFst j) (oddShiftSnd j))) S = S') (g f : Fin n.succ → ℚ)
    (hS1 : S.val = Unshifted.planeCharges g + Shifted.planeCharges f) : ∃ (g' f' : Fin n.succ → ℚ),
    S'.val = Unshifted.planeCharges g' + Shifted.planeCharges f' ∧
    Shifted.planeCharges f' = Shifted.planeCharges f +
    (S.val (oddShiftSnd j) - S.val (oddShiftFst j)) • Shifted.basisAsCharges j ∧ g' = g
```

## Depends on

- [Vector like charges](anomalycancellation-vectorlike.md)

## Proof depends on

- [Basis of `LinSols`](anomalycancellation-basislinear.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Odd/BasisLinear.lean)
