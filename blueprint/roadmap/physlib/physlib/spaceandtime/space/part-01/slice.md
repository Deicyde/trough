---
declaration: module
origin: cited
lean: Space.slice, Space.slice_symm_apply, Space.slice_symm_apply_self, Space.slice_symm_apply_succAbove, Space.slice_symm_measurableEmbedding, Space.norm_slice_symm_eq, Space.abs_right_le_norm_slice_symm, Space.norm_left_le_norm_slice_symm
statement: formalized
proof: formalized
---

# Slices of space

The module `Physlib.SpaceAndTime.Space.Slice`, [Physlib/SpaceAndTime/Space/Slice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean): 15 declarations, 1 with a docstring.

## i. Overview

> In this module we will define the equivalence between `Space d.succ` and `ℝ × Space d` which
> extracts the `i`th coordinate on `Space d.succ`.

## ii. Key results

> - `slice` : The continuous linear equivalence between `Space d.succ` and `ℝ × Space d` extracting
>   the `i`th coordinate.

## iv. References

> * https://leanprover.zulipchat.com/#narrow/channel/479953-Physlib/topic/API.20around.20.60Space.20.28d1.20.2B.20d2.29.60.20to.20.60Space.20d1.20x.20Space.20d2.60/with/556754634.

## A. Slicing spaces

**`Space.slice`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L57).

> The linear equivalence between `Space d.succ` and `ℝ × Space d`
> extracting the `i`th coordinate.

```lean
def slice {d} (i : Fin d.succ) : Space d.succ ≃L[ℝ] ℝ × Space d
```

### A.1. Basic applications of the slicing map

**`Space.slice_symm_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L101).

```lean
lemma slice_symm_apply {d : ℕ} (i : Fin d.succ) (r : ℝ) (x : Space d) :
    (slice i).symm (r, x) = fun j =>
      Fin.insertNthEquiv (fun _ => ℝ) i (r, x) j
```

**`Space.slice_symm_apply_self`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L106).

```lean
lemma slice_symm_apply_self {d : ℕ} (i : Fin d.succ) (r : ℝ) (x : Space d) :
    (slice i).symm (r, x) i = r
```

**`Space.slice_symm_apply_succAbove`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L111).

```lean
lemma slice_symm_apply_succAbove {d : ℕ} (i : Fin d.succ) (r : ℝ) (x : Space d) (j : Fin d) :
    (slice i).symm (r, x) (Fin.succAbove i j) = x j
```

### A.2. Slice as a measurable embedding

**`Space.slice_symm_measurableEmbedding`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L121).

```lean
lemma slice_symm_measurableEmbedding {d : ℕ} (i : Fin d.succ) :
    MeasurableEmbedding (slice i).symm
```

### A.3. The norm of the slice map

**`Space.norm_slice_symm_eq`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L143).

```lean
lemma norm_slice_symm_eq {d : ℕ} (i : Fin d.succ) (r : ℝ) (x : Space d) :
    ‖(slice i).symm (r, x)‖ = √(‖r‖ ^ 2 + ‖x‖ ^ 2)
```

**`Space.abs_right_le_norm_slice_symm`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L152).

```lean
lemma abs_right_le_norm_slice_symm {d : ℕ} (i : Fin d.succ) (r : ℝ) (x : Space d) :
    |r| ≤ ‖(slice i).symm (r, x)‖
```

**`Space.norm_left_le_norm_slice_symm`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L159).

```lean
lemma norm_left_le_norm_slice_symm {d : ℕ} (i : Fin d.succ) (r : ℝ) (x : Space d) :
    ‖x‖ ≤ ‖(slice i).symm (r, x)‖
```

### A.4. Derivative of the slice map

**`Space.fderiv_slice_symm`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L173).

```lean
lemma fderiv_slice_symm {d : ℕ} (i : Fin d.succ) (p1 : ℝ × Space d) :
    fderiv ℝ (slice i).symm p1 = (slice i).symm
```

**`Space.fderiv_slice_symm_left_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L177).

```lean
lemma fderiv_slice_symm_left_apply {d : ℕ} (i : Fin d.succ) (x : Space d) (r1 r2 : ℝ) :
    (fderiv ℝ (fun r => (slice i).symm (r, x))) r1 r2 = (slice i).symm (r2, 0)
```

**`Space.fderiv_slice_symm_right_apply`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L187).

```lean
lemma fderiv_slice_symm_right_apply {d : ℕ} (i : Fin d.succ) (r : ℝ)
    (x1 x2 : Space d) :
    (fderiv ℝ (fun x => (slice i).symm (r, x))) x1 x2 = (slice i).symm (0, x2)
```

**`Space.fderiv_fun_slice_symm_right_apply`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L197).

```lean
lemma fderiv_fun_slice_symm_right_apply {d : ℕ} (i : Fin d.succ) (r : ℝ)
    (x1 x2 : Space d) (f : Space d.succ → F) (hf : DifferentiableAt ℝ f ((slice i).symm (r, x1))) :
    (fderiv ℝ (fun x => f ((slice i).symm (r, x)))) x1 x2 =
    fderiv ℝ f ((slice i).symm (r, x1)) ((slice i).symm (0, x2))
```

**`Space.fderiv_fun_slice_symm_left_apply`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L206).

```lean
lemma fderiv_fun_slice_symm_left_apply {d : ℕ} (i : Fin d.succ) (r1 r2 : ℝ)
    (x : Space d) (f : Space d.succ → F) (hf : DifferentiableAt ℝ f ((slice i).symm (r1, x))) :
    (fderiv ℝ (fun r => f ((slice i).symm (r, x)))) r1 r2 =
    fderiv ℝ f ((slice i).symm (r1, x)) ((slice i).symm (r2, 0))
```

### A.5. Basis in terms of slices

**`Space.basis_self_eq_slice`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L221).

```lean
lemma basis_self_eq_slice {d : ℕ} (i : Fin d.succ) :
    basis i = (slice i).symm (1, 0)
```

**`Space.basis_succAbove_eq_slice`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean#L228).

```lean
lemma basis_succAbove_eq_slice {d : ℕ} (i : Fin d.succ) (j : Fin d) :
    basis (Fin.succAbove i j) = (slice i).symm (0, basis j)
```

## Depends on

- [The structure of a module on Space](module.md)

## Sources

- [Physlib/SpaceAndTime/Space/Slice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Slice.lean)
