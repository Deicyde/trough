---
declaration: module
origin: cited
lean: PureU1.VectorLikeEvenPlane.evenFst, PureU1.VectorLikeEvenPlane.evenSnd, PureU1.VectorLikeEvenPlane.ext_even, PureU1.VectorLikeEvenPlane.sum_even, PureU1.VectorLikeEvenPlane.n_cond₂, PureU1.VectorLikeEvenPlane.evenShiftFst, PureU1.VectorLikeEvenPlane.evenShiftSnd, PureU1.VectorLikeEvenPlane.evenShiftZero
statement: formalized
proof: formalized
---

# Splitting the linear solutions in the even case into two ACC-satisfying planes

The module `Physlib.QFT.QED.AnomalyCancellation.Even.BasisLinear`, [Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean): 80 declarations, 19 with a docstring.

## i. Overview

> We split the linear solutions of `PureU1 (2 * n.succ)` into two planes,
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

> We have `2 * n.succ` charges, which we split up in the following ways:
>
> `| evenFst j (0 to n) | evenSnd j (n.succ to n + n.succ)|`
>
> ```
> | evenShiftZero (0) | evenShiftFst j (1 to n) |
>   evenShiftSnd j (n.succ to 2 * n) | evenShiftLast (2 * n.succ - 1) |
> ```

### A.1. The even split: Spltting the charges up via `n.succ + n.succ`

**`PureU1.VectorLikeEvenPlane.evenFst`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L115).

> The inclusion of `Fin n.succ` into `Fin (n.succ + n.succ)` via the first `n.succ`,
> casted into `Fin (2 * n.succ)`.

```lean
def evenFst (j : Fin n.succ) : Fin (2 * n.succ)
```

**`PureU1.VectorLikeEvenPlane.evenSnd`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L120).

> The inclusion of `Fin n.succ` into `Fin (n.succ + n.succ)` via the second `n.succ`,
> casted into `Fin (2 * n.succ)`.

```lean
def evenSnd (j : Fin n.succ) : Fin (2 * n.succ)
```

**`PureU1.VectorLikeEvenPlane.ext_even`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L123).

```lean
lemma ext_even (S T : Fin (2 * n.succ) → ℚ) (h1 : ∀ i, S (evenFst i) = T (evenFst i))
    (h2 : ∀ i, S (evenSnd i) = T (evenSnd i)) : S = T
```

**`PureU1.VectorLikeEvenPlane.sum_even`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L133).

```lean
lemma sum_even (S : Fin (2 * n.succ) → ℚ) :
    ∑ i, S i = ∑ i : Fin n.succ, ((S ∘ evenFst) i + (S ∘ evenSnd) i)
```

### A.2. The shifted even split: Spltting the charges up via `1 + (n + n + 1)`

**`PureU1.VectorLikeEvenPlane.n_cond₂`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L145).

```lean
lemma n_cond₂ (n : ℕ) : 1 + ((n + n) + 1) = 2 * n.succ
```

**`PureU1.VectorLikeEvenPlane.evenShiftFst`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L150).

> The inclusion of `Fin n` into `Fin (1 + (n + n + 1))` via the first `n`,
> casted into `Fin (2 * n.succ)`.

```lean
def evenShiftFst (j : Fin n) : Fin (2 * n.succ)
```

**`PureU1.VectorLikeEvenPlane.evenShiftSnd`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L155).

> The inclusion of `Fin n` into `Fin (1 + (n + n + 1))` via the second `n`,
> casted into `Fin (2 * n.succ)`.

```lean
def evenShiftSnd (j : Fin n) : Fin (2 * n.succ)
```

**`PureU1.VectorLikeEvenPlane.evenShiftZero`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L160).

> The element of `Fin (1 + (n + n + 1))` corresponding to the first `1`,
> casted into `Fin (2 * n.succ)`.

```lean
def evenShiftZero : Fin (2 * n.succ)
```

**`PureU1.VectorLikeEvenPlane.evenShiftLast`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L164).

> The element of `Fin (1 + (n + n + 1))` corresponding to the second `1`,
> casted into `Fin (2 * n.succ)`.

```lean
def evenShiftLast : Fin (2 * n.succ)
```

**`PureU1.VectorLikeEvenPlane.sum_evenShift`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L166).

```lean
lemma sum_evenShift (S : Fin (2 * n.succ) → ℚ) :
    ∑ i, S i = S evenShiftZero + S evenShiftLast +
    ∑ i : Fin n, ((S ∘ evenShiftFst) i + (S ∘ evenShiftSnd) i)
```

### A.3. Lemmas relating the two splittings

**`PureU1.VectorLikeEvenPlane.evenShiftZero_eq_evenFst_zero`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L184).

```lean
lemma evenShiftZero_eq_evenFst_zero : @evenShiftZero n = evenFst 0
```

**`PureU1.VectorLikeEvenPlane.evenShiftLast_eq_evenSnd_last`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L186).

```lean
lemma evenShiftLast_eq_evenSnd_last: @evenShiftLast n = evenSnd (Fin.last n)
```

**`PureU1.VectorLikeEvenPlane.evenShiftFst_eq_evenFst_succ`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L192).

```lean
lemma evenShiftFst_eq_evenFst_succ (j : Fin n) : evenShiftFst j = evenFst j.succ
```

**`PureU1.VectorLikeEvenPlane.evenShiftSnd_eq_evenSnd_castSucc`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L197).

```lean
lemma evenShiftSnd_eq_evenSnd_castSucc (j : Fin n) : evenShiftSnd j = evenSnd j.castSucc
```

## B. The unshifted plane

### B.1. The basis vectors of the unshifted plane as charges

**`PureU1.VectorLikeEvenPlane.Unshifted.basisAsCharges`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L218).

> The unshifted part of the basis as charges.

```lean
def basisAsCharges (j : Fin n.succ) : (PureU1 (2 * n.succ)).Charges
```

### B.2. Components of the basis vectors

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_on_evenFst_self`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L235).

```lean
lemma basis_on_evenFst_self (j : Fin n.succ) : basisAsCharges j (evenFst j) = 1
```

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_on_evenFst_other`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L239).

```lean
lemma basis_on_evenFst_other {k j : Fin n.succ} (h : k ≠ j) :
    basisAsCharges k (evenFst j) = 0
```

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_on_other`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L258).

```lean
lemma basis_on_other {k : Fin n.succ} {j : Fin (2 * n.succ)} (h1 : j ≠ evenFst k)
    (h2 : j ≠ evenSnd k) : basisAsCharges k j = 0
```

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_evenSnd_eq_neg_evenFst`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L263).

```lean
lemma basis_evenSnd_eq_neg_evenFst (j i : Fin n.succ) :
    basisAsCharges j (evenSnd i) = - basisAsCharges j (evenFst i)
```

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_on_evenSnd_self`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L281).

```lean
lemma basis_on_evenSnd_self (j : Fin n.succ) : basisAsCharges j (evenSnd j) = - 1
```

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_on_evenSnd_other`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L284).

```lean
lemma basis_on_evenSnd_other {k j : Fin n.succ} (h : k ≠ j) : basisAsCharges k (evenSnd j) = 0
```

### B.3. The basis vectors satisfy the linear ACCs

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_linearACC`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L295).

```lean
lemma basis_linearACC (j : Fin n.succ) : (accGrav (2 * n.succ)) (basisAsCharges j) = 0
```

### B.4. The basis vectors satisfy the cubic ACC

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_accCube`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L303).

```lean
lemma basis_accCube (j : Fin n.succ) :
    accCube (2 * n.succ) (basisAsCharges j) = 0
```

### B.5. The basis vectors as linear solutions

**`PureU1.VectorLikeEvenPlane.Unshifted.basis`**, a def, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L318).

> The unshifted part of the basis as `LinSols`.

```lean
def basis (j : Fin n.succ) : (PureU1 (2 * n.succ)).LinSols
```

### B.6. The inclusion of the unshifted plane into charges

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges`**, a def, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L331).

> A point in the span of the unshifted part of the basis as a charge.

```lean
def planeCharges (f : Fin n.succ → ℚ) : (PureU1 (2 * n.succ)).Charges
```

### B.7. Components of the inclusion into charges

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges_evenFst`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L339).

```lean
lemma planeCharges_evenFst (f : Fin n.succ → ℚ) (j : Fin n.succ) :
    planeCharges f (evenFst j) = f j
```

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges_evenSnd`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L347).

```lean
lemma planeCharges_evenSnd (f : Fin n.succ → ℚ) (j : Fin n.succ) :
    planeCharges f (evenSnd j) = - f j
```

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges_evenSnd_evenFst`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L356).

```lean
lemma planeCharges_evenSnd_evenFst (f : Fin n.succ → ℚ) :
    planeCharges f ∘ evenSnd = - planeCharges f ∘ evenFst
```

### B.8. The inclusion into charges satisfies the linear and cubic ACCs

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges_linearACC`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L368).

```lean
lemma planeCharges_linearACC (f : Fin n.succ → ℚ) :
    (accGrav (2 * n.succ)) (planeCharges f) = 0
```

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges_accCube`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L373).

```lean
lemma planeCharges_accCube (f : Fin n.succ → ℚ) : accCube (2 * n.succ) (planeCharges f) = 0
```

### B.9. Kernel of the inclusion into charges

**`PureU1.VectorLikeEvenPlane.Unshifted.planeCharges_zero`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L385).

```lean
lemma planeCharges_zero (f : Fin n.succ → ℚ) (h : planeCharges f = 0) : ∀ i, f i = 0
```

### B.10. The inclusion of the plane into linear solutions

**`PureU1.VectorLikeEvenPlane.Unshifted.planeLinSols`**, a def, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L395).

> A point in the span of the unshifted part of the basis.

```lean
def planeLinSols (f : Fin n.succ → ℚ) : (PureU1 (2 * n.succ)).LinSols
```

**`PureU1.VectorLikeEvenPlane.Unshifted.planeLinSols_val`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L398).

```lean
lemma planeLinSols_val (f : Fin n.succ → ℚ) : (planeLinSols f).val = planeCharges f
```

### B.11. The basis vectors are linearly independent

**`PureU1.VectorLikeEvenPlane.Unshifted.basis_linear_independent`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L410).

```lean
lemma basis_linear_independent : LinearIndependent ℚ (@basis n)
```

### B.12. Every vector-like even solution is in the span of the basis of the unshifted plane

**`PureU1.VectorLikeEvenPlane.Unshifted.vectorLikeEven_in_span`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L422).

```lean
lemma vectorLikeEven_in_span (S : (PureU1 (2 * n.succ)).LinSols)
    (hS : VectorLikeEven S.val) : ∃ (M : (FamilyPermutations (2 * n.succ)).group),
      (FamilyPermutations (2 * n.succ)).linSolRep M S ∈ Submodule.span ℚ (Set.range basis)
```

## C. The shifted plane

**`PureU1.VectorLikeEvenPlane.Shifted.basisAsCharges`**, a def, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L459).

> The shifted part of the basis as charges.

```lean
def basisAsCharges (j : Fin n) : (PureU1 (2 * n.succ)).Charges
```

### C.2. Components of the vectors

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_evenShiftFst_self`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L475).

```lean
lemma basis_on_evenShiftFst_self (j : Fin n) : basisAsCharges j (evenShiftFst j) = 1
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_other`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L479).

```lean
lemma basis_on_other {k : Fin n} {j : Fin (2 * n.succ)} (h1 : j ≠ evenShiftFst k)
    (h2 : j ≠ evenShiftSnd k) : basisAsCharges k j = 0
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_evenShiftFst_other`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L483).

```lean
lemma basis_on_evenShiftFst_other {k j : Fin n} (h : k ≠ j) :
    basisAsCharges k (evenShiftFst j) = 0
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_evenShiftSnd_eq_neg_evenShiftFst`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L492).

```lean
lemma basis_evenShiftSnd_eq_neg_evenShiftFst (j i : Fin n) :
    basisAsCharges j (evenShiftSnd i) = - basisAsCharges j (evenShiftFst i)
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_evenShiftSnd_self`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L513).

```lean
lemma basis_on_evenShiftSnd_self (j : Fin n) : basisAsCharges j (evenShiftSnd j) = - 1
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_evenShiftSnd_other`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L516).

```lean
lemma basis_on_evenShiftSnd_other {k j : Fin n} (h : k ≠ j) :
    basisAsCharges k (evenShiftSnd j) = 0
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_evenShiftZero`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L521).

```lean
lemma basis_on_evenShiftZero (j : Fin n) : basisAsCharges j evenShiftZero = 0
```

**`PureU1.VectorLikeEvenPlane.Shifted.basis_on_evenShiftLast`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L527).

```lean
lemma basis_on_evenShiftLast (j : Fin n) : basisAsCharges j evenShiftLast = 0
```

### C.3. The vectors satisfy the linear ACCs

**`PureU1.VectorLikeEvenPlane.Shifted.basis_linearACC`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L540).

```lean
lemma basis_linearACC (j : Fin n) : (accGrav (2 * n.succ)) (basisAsCharges j) = 0
```

### C.4. The vectors satisfy the cubic ACC

**`PureU1.VectorLikeEvenPlane.Shifted.basis_accCube`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L551).

```lean
lemma basis_accCube (j : Fin n) :
    accCube (2 * n.succ) (basisAsCharges j) = 0
```

### C.6. The vectors as linear solutions

**`PureU1.VectorLikeEvenPlane.Shifted.basis`**, a def, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L569).

> The shifted part of the basis as `LinSols`.

```lean
def basis (j : Fin n) : (PureU1 (2 * n.succ)).LinSols
```

### C.7. The inclusion of the shifted plane into charges

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges`**, a def, [line 582](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L582).

> A point in the span of the shifted part of the basis as a charge.

```lean
def planeCharges (f : Fin n → ℚ) : (PureU1 (2 * n.succ)).Charges
```

### C.8. Components of the inclusion into charges

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_evenShiftFst`**, a lemma, [line 590](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L590).

```lean
lemma planeCharges_evenShiftFst (f : Fin n → ℚ) (j : Fin n) :
    planeCharges f (evenShiftFst j) = f j
```

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_evenShiftSnd`**, a lemma, [line 598](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L598).

```lean
lemma planeCharges_evenShiftSnd (f : Fin n → ℚ) (j : Fin n) :
    planeCharges f (evenShiftSnd j) = - f j
```

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_evenShiftZero`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L607).

```lean
lemma planeCharges_evenShiftZero (f : Fin n → ℚ) : planeCharges f (evenShiftZero) = 0
```

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_evenShiftLast`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L611).

```lean
lemma planeCharges_evenShiftLast (f : Fin n → ℚ) : planeCharges f evenShiftLast = 0
```

### C.9. The inclusion into charges satisfies the cubic ACC

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_accCube`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L621).

```lean
lemma planeCharges_accCube (f : Fin n → ℚ) : accCube (2 * n.succ) (planeCharges f) = 0
```

### C.10. Kernel of the inclusion into charges

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_zero`**, a lemma, [line 635](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L635).

```lean
lemma planeCharges_zero (f : Fin n → ℚ) (h : planeCharges f = 0) : ∀ i, f i = 0
```

### C.11. The inclusion of the shifted plane into the span of the basis

**`PureU1.VectorLikeEvenPlane.Shifted.planeCharges_in_span`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L644).

```lean
lemma planeCharges_in_span (f : Fin n → ℚ) :
    planeCharges f ∈ Submodule.span ℚ (Set.range basisAsCharges)
```

### C.12. The inclusion of the plane into linear solutions

**`PureU1.VectorLikeEvenPlane.Shifted.planeLinSols`**, a def, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L655).

> A point in the span of the shifted part of the basis.

```lean
def planeLinSols (f : Fin n → ℚ) : (PureU1 (2 * n.succ)).LinSols
```

**`PureU1.VectorLikeEvenPlane.Shifted.planeLinSols_val`**, a lemma, [line 658](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L658).

```lean
lemma planeLinSols_val (f : Fin n → ℚ) : (planeLinSols f).val = planeCharges f
```

### C.13. The basis vectors are linearly independent

**`PureU1.VectorLikeEvenPlane.Shifted.basis_linear_independent`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L670).

```lean
lemma basis_linear_independent : LinearIndependent ℚ (@basis n)
```

### C.14. Properties of the basis vectors relating to the span

**`PureU1.VectorLikeEvenPlane.Shifted.smul_basisAsCharges_in_span`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L682).

```lean
lemma smul_basisAsCharges_in_span (S : (PureU1 (2 * n.succ)).LinSols) (j : Fin n) :
    (S.val (evenShiftSnd j) - S.val (evenShiftFst j)) • basisAsCharges j ∈
    Submodule.span ℚ (Set.range basisAsCharges)
```

### C.15. Permutations as additions of basis vectors

**`PureU1.VectorLikeEvenPlane.Shifted.swap_as_add`**, a lemma, [line 696](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L696).

> Swapping the elements evenShiftFst j and evenShiftSnd j is equivalent to
> adding a vector basisAsCharges j.

```lean
lemma swap_as_add {S S' : (PureU1 (2 * n.succ)).LinSols} (j : Fin n)
    (hS : ((FamilyPermutations (2 * n.succ)).linSolRep
    (Equiv.swap (evenShiftFst j) (evenShiftSnd j))) S = S') :
    S'.val = S.val + (S.val (evenShiftSnd j) - S.val (evenShiftFst j)) • basisAsCharges j
```

## D. Mixed cubic ACCs involving points from both planes

**`PureU1.VectorLikeEvenPlane.unshifted_unshifted_shifted_accCube`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L722).

```lean
lemma unshifted_unshifted_shifted_accCube (g : Fin n.succ → ℚ) (j : Fin n) :
    accCubeTriLinSymm (Unshifted.planeCharges g) (Unshifted.planeCharges g)
      (Shifted.basisAsCharges j)
    = g (j.succ) ^ 2 - g (j.castSucc) ^ 2
```

**`PureU1.VectorLikeEvenPlane.shifted_shifted_unshifted_accCube`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L740).

```lean
lemma shifted_shifted_unshifted_accCube (g : Fin n → ℚ) (j : Fin n.succ) :
    accCubeTriLinSymm (Shifted.planeCharges g) (Shifted.planeCharges g) (Unshifted.basisAsCharges j)
    = (Shifted.planeCharges g (evenFst j))^2 - (Shifted.planeCharges g (evenSnd j))^2
```

## E. The combined basis

### E.1. As a map into linear solutions

**`PureU1.VectorLikeEvenPlane.basisa`**, a def, [line 765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L765).

> The whole basis as `LinSols`.

```lean
def basisa : (Fin n.succ) ⊕ (Fin n) → (PureU1 (2 * n.succ)).LinSols
```

### E.2. Inclusion of the span of the basis into charges

**`PureU1.VectorLikeEvenPlane.Pa`**, a def, [line 777](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L777).

> A point in the span of the basis as a charge.

```lean
def Pa (f : Fin n.succ → ℚ) (g : Fin n → ℚ) : (PureU1 (2 * n.succ)).Charges
```

### E.3. Components of the inclusion into charges

**`PureU1.VectorLikeEvenPlane.Pa_evenShiftFst`**, a lemma, [line 787](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L787).

```lean
lemma Pa_evenShiftFst (f : Fin n.succ → ℚ) (g : Fin n → ℚ) (j : Fin n) :
    Pa f g (evenShiftFst j) = f j.succ + g j
```

**`PureU1.VectorLikeEvenPlane.Pa_evenShiftSnd`**, a lemma, [line 795](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L795).

```lean
lemma Pa_evenShiftSnd (f : Fin n.succ → ℚ) (g : Fin n → ℚ) (j : Fin n) :
    Pa f g (evenShiftSnd j) = - f j.castSucc - g j
```

**`PureU1.VectorLikeEvenPlane.Pa_evenShitZero`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L804).

```lean
lemma Pa_evenShitZero (f : Fin n.succ → ℚ) (g : Fin n → ℚ) : Pa f g (evenShiftZero) = f 0
```

**`PureU1.VectorLikeEvenPlane.Pa_evenShiftLast`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L811).

```lean
lemma Pa_evenShiftLast (f : Fin n.succ → ℚ) (g : Fin n → ℚ) :
    Pa f g (evenShiftLast) = - f (Fin.last n)
```

### E.4. Kernel of the inclusion into charges

**`PureU1.VectorLikeEvenPlane.Pa_zero`**, a lemma, [line 824](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L824).

```lean
lemma Pa_zero (f : Fin n.succ → ℚ) (g : Fin n → ℚ) (h : Pa f g = 0) :
    ∀ i, f i = 0
```

**`PureU1.VectorLikeEvenPlane.Pa_zero!`**, a lemma, [line 847](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L847).

```lean
lemma Pa_zero! (f : Fin n.succ → ℚ) (g : Fin n → ℚ) (h : Pa f g = 0) :
    ∀ i, g i = 0
```

### E.5. The inclusion of the span of the basis into linear solutions

**`PureU1.VectorLikeEvenPlane.Pa'`**, a def, [line 860](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L860).

> A point in the span of the whole basis.

```lean
def Pa' (f : (Fin n.succ) ⊕ (Fin n) → ℚ) : (PureU1 (2 * n.succ)).LinSols
```

**`PureU1.VectorLikeEvenPlane.Pa'_P'_P!'`**, a lemma, [line 863](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L863).

```lean
lemma Pa'_P'_P!' (f : (Fin n.succ) ⊕ (Fin n) → ℚ) :
    Pa' f = Unshifted.planeLinSols (f ∘ Sum.inl) + Shifted.planeLinSols (f ∘ Sum.inr)
```

### E.6. The combined basis vectors are linearly independent

**`PureU1.VectorLikeEvenPlane.basisa_linear_independent`**, a lemma, [line 873](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L873).

```lean
lemma basisa_linear_independent : LinearIndependent ℚ (@basisa n)
```

### E.7. Injectivity of the inclusion into linear solutions

**`PureU1.VectorLikeEvenPlane.Pa'_eq`**, a lemma, [line 892](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L892).

```lean
lemma Pa'_eq (f f' : (Fin n.succ) ⊕ (Fin n) → ℚ) : Pa' f = Pa' f' ↔ f = f'
```

**`PureU1.VectorLikeEvenPlane.Pa'_elim_eq_iff`**, a lemma, [line 905](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L905).

```lean
lemma Pa'_elim_eq_iff (g g' : Fin n.succ → ℚ) (f f' : Fin n → ℚ) :
    Pa' (Sum.elim g f) = Pa' (Sum.elim g' f') ↔ Pa g f = Pa g' f'
```

**`PureU1.VectorLikeEvenPlane.Pa_eq`**, a lemma, [line 916](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L916).

```lean
lemma Pa_eq (g g' : Fin n.succ → ℚ) (f f' : Fin n → ℚ) :
    Pa g f = Pa g' f' ↔ g = g' ∧ f = f'
```

### E.8. Cardinality of the basis

**`PureU1.VectorLikeEvenPlane.basisa_card`**, a lemma, [line 927](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L927).

```lean
lemma basisa_card : Fintype.card ((Fin n.succ) ⊕ (Fin n)) =
    Module.finrank ℚ (PureU1 (2 * n.succ)).LinSols
```

### E.9. The basis vectors as a basis

**`PureU1.VectorLikeEvenPlane.basisaAsBasis`**, a def, [line 940](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L940).

> The basis formed out of our `basisa` vectors.

```lean
noncomputable def basisaAsBasis :
    Basis (Fin (succ n) ⊕ Fin n) ℚ (PureU1 (2 * succ n)).LinSols
```

## F. Every Lienar solution is the sum of a point from each plane

**`PureU1.VectorLikeEvenPlane.span_basis`**, a lemma, [line 950](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L950).

```lean
lemma span_basis (S : (PureU1 (2 * n.succ)).LinSols) :
    ∃ (g : Fin n.succ → ℚ) (f : Fin n → ℚ),
      S.val = Unshifted.planeCharges g + Shifted.planeCharges f
```

### F.1. Relation under permutations

**`PureU1.VectorLikeEvenPlane.span_basis_swap!`**, a lemma, [line 970](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean#L970).

```lean
lemma span_basis_swap! {S : (PureU1 (2 * n.succ)).LinSols} (j : Fin n)
    (hS : ((FamilyPermutations (2 * n.succ)).linSolRep
    (Equiv.swap (evenShiftFst j) (evenShiftSnd j))) S = S') (g : Fin n.succ → ℚ) (f : Fin n → ℚ)
    (h : S.val = Unshifted.planeCharges g + Shifted.planeCharges f) :
    ∃ (g' : Fin n.succ → ℚ) (f' : Fin n → ℚ),
      S'.val = Unshifted.planeCharges g' + Shifted.planeCharges f' ∧
      Shifted.planeCharges f' = Shifted.planeCharges f +
      (S.val (evenShiftSnd j) - S.val (evenShiftFst j)) • Shifted.basisAsCharges j ∧ g' = g
```

## Depends on

- [Vector like charges](anomalycancellation-vectorlike.md)

## Proof depends on

- [Anomaly cancellation conditions for the n-family SM.](../../particles/standardmodel/anomalycancellation-basic.md)
- [Basis of `LinSols`](anomalycancellation-basislinear.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/Even/BasisLinear.lean)
