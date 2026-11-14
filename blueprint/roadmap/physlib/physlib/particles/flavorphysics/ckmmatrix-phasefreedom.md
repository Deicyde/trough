---
declaration: module
origin: cited
lean: CKMMatrix.shift_ud_phase_zero, CKMMatrix.shift_us_phase_zero, CKMMatrix.shift_ub_phase_zero, CKMMatrix.shift_cs_phase_zero, CKMMatrix.shift_cb_phase_zero, CKMMatrix.shift_tb_phase_zero, CKMMatrix.shift_cd_phase_pi, CKMMatrix.shift_cross_product_phase_zero
statement: formalized
proof: formalized
---

# Phase freedom of the CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.PhaseFreedom`, [Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean): 16 declarations, 2 with a docstring.

> The CKM matrix is only defined up to an equivalence. This leads to a freedom
> to shift the phases of the matrices elements of the CKM matrix.
>
> In this file we define two sets of conditions on the CKM matrices
> `fstRowThdColRealCond` which we show can be satisfied by any CKM matrix up to equivalence
> and `ubOnePhaseCond` which we show can be satisfied by any CKM matrix up to equivalence as long as
> the ub element as absolute value 1.

**`CKMMatrix.shift_ud_phase_zero`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L32).

```lean
lemma shift_ud_phase_zero (V : CKMMatrix) (h1 : u + d = - arg [V]ud) :
    [phaseShiftApply V u c t d s b]ud = VudAbs ⟦V⟧
```

**`CKMMatrix.shift_us_phase_zero`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L43).

```lean
lemma shift_us_phase_zero {V : CKMMatrix} (h1 : u + s = - arg [V]us) :
    [phaseShiftApply V u c t d s b]us = VusAbs ⟦V⟧
```

**`CKMMatrix.shift_ub_phase_zero`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L54).

```lean
lemma shift_ub_phase_zero {V : CKMMatrix} (h1 : u + b = - arg [V]ub) :
    [phaseShiftApply V u c t d s b]ub = VubAbs ⟦V⟧
```

**`CKMMatrix.shift_cs_phase_zero`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L65).

```lean
lemma shift_cs_phase_zero {V : CKMMatrix} (h1 : c + s = - arg [V]cs) :
    [phaseShiftApply V u c t d s b]cs = VcsAbs ⟦V⟧
```

**`CKMMatrix.shift_cb_phase_zero`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L76).

```lean
lemma shift_cb_phase_zero {V : CKMMatrix} (h1 : c + b = - arg [V]cb) :
    [phaseShiftApply V u c t d s b]cb = VcbAbs ⟦V⟧
```

**`CKMMatrix.shift_tb_phase_zero`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L87).

```lean
lemma shift_tb_phase_zero {V : CKMMatrix} (h1 : t + b = - arg [V]tb) :
    [phaseShiftApply V u c t d s b]tb = VtbAbs ⟦V⟧
```

**`CKMMatrix.shift_cd_phase_pi`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L98).

```lean
lemma shift_cd_phase_pi {V : CKMMatrix} (h1 : c + d = Real.pi - arg [V]cd) :
    [phaseShiftApply V u c t d s b]cd = - VcdAbs ⟦V⟧
```

**`CKMMatrix.shift_cross_product_phase_zero`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L111).

```lean
lemma shift_cross_product_phase_zero {V : CKMMatrix} {τ : ℝ}
    (hτ : cexp (τ * I) • (conj [V]u ⨯₃ conj [V]c) = [V]t) (h1 : τ = - u - c - t - d - s - b) :
    [phaseShiftApply V u c t d s b]t =
    conj [phaseShiftApply V u c t d s b]u ⨯₃ conj [phaseShiftApply V u c t d s b]c
```

**`CKMMatrix.FstRowThdColRealCond`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L159).

> A proposition which is satisfied by a CKM matrix if its `ud`, `us`, `cb` and `tb` elements
> are positive and real, and there is no phase difference between the `t`th-row and
> the cross product of the conjugates of the `u`th and `c`th rows.

```lean
def FstRowThdColRealCond (U : CKMMatrix) : Prop
```

**`CKMMatrix.ubOnePhaseCond`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L167).

> A proposition which is satisfied by a CKM matrix `ub` is one, `ud`, `us` and `cb` are zero,
>   there is no phase difference between the `t`th-row and
> the cross product of the conjugates of the `u`th and `c`th rows, and the `cd`th and `cs`th
> elements are real and related in a set way.

```lean
def ubOnePhaseCond (U : CKMMatrix) : Prop
```

**`CKMMatrix.fstRowThdColRealCond_shift_solution`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L171).

```lean
lemma fstRowThdColRealCond_shift_solution {V : CKMMatrix} (h1 : a + d = - arg [V]ud)
    (h2 : a + e = - arg [V]us) (h3 : b + f = - arg [V]cb)
    (h4 : c + f = - arg [V]tb) (h5 : τ = - a - b - c - d - e - f) :
    b = - τ + arg [V]ud + arg [V]us + arg [V]tb + a ∧
    c = - τ + arg [V]cb + arg [V]ud + arg [V]us + a ∧
    d = - arg [V]ud - a ∧
    e = - arg [V]us - a ∧
    f = τ - arg [V]ud - arg [V]us - arg [V]cb - arg [V]tb - a
```

**`CKMMatrix.ubOnePhaseCond_shift_solution`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L201).

```lean
lemma ubOnePhaseCond_shift_solution {V : CKMMatrix} (h1 : a + f = - arg [V]ub)
    (h2 : 0 = - a - b - c - d - e - f)
    (h3 : b + d = Real.pi - arg [V]cd) (h5 : b + e = - arg [V]cs) :
    c = - Real.pi + arg [V]cd + arg [V]cs + arg [V]ub + b ∧
    d = Real.pi - arg [V]cd - b ∧
    e = - arg [V]cs - b ∧
    f = - arg [V]ub - a
```

**`CKMMatrix.fstRowThdColRealCond_holds_up_to_equiv`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L223).

```lean
lemma fstRowThdColRealCond_holds_up_to_equiv (V : CKMMatrix) :
    ∃ (U : CKMMatrix), V ≈ U ∧ FstRowThdColRealCond U
```

**`CKMMatrix.ubOnePhaseCond_hold_up_to_equiv_of_ub_one`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L259).

```lean
lemma ubOnePhaseCond_hold_up_to_equiv_of_ub_one {V : CKMMatrix} (hb : ¬ ([V]ud ≠ 0 ∨ [V]us ≠ 0))
    (hV : FstRowThdColRealCond V) :
    ∃ (U : CKMMatrix), V ≈ U ∧ ubOnePhaseCond U
```

**`CKMMatrix.cd_of_fstRowThdColRealCond`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L317).

```lean
lemma cd_of_fstRowThdColRealCond {V : CKMMatrix} (hb : [V]ud ≠ 0 ∨ [V]us ≠ 0)
    (hV : FstRowThdColRealCond V) :
    [V]cd = (- VtbAbs ⟦V⟧ * VusAbs ⟦V⟧ / (VudAbs ⟦V⟧ ^2 + VusAbs ⟦V⟧ ^2)) +
    (- VubAbs ⟦V⟧ * VudAbs ⟦V⟧ * VcbAbs ⟦V⟧ / (VudAbs ⟦V⟧ ^2 + VusAbs ⟦V⟧ ^2))
    * cexp (- arg [V]ub * I)
```

**`CKMMatrix.cs_of_fstRowThdColRealCond`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean#L338).

```lean
lemma cs_of_fstRowThdColRealCond {V : CKMMatrix} (hb : [V]ud ≠ 0 ∨ [V]us ≠ 0)
    (hV : FstRowThdColRealCond V) :
    [V]cs = (VtbAbs ⟦V⟧ * VudAbs ⟦V⟧ / (VudAbs ⟦V⟧ ^2 + VusAbs ⟦V⟧ ^2))
    + (- VubAbs ⟦V⟧ * VusAbs ⟦V⟧ * VcbAbs ⟦V⟧/ (VudAbs ⟦V⟧ ^2 + VusAbs ⟦V⟧ ^2))
    * cexp (- arg [V]ub * I)
```

## Depends on

- [Rows for the CKM Matrix](ckmmatrix-rows.md)

## Proof depends on

- [Relations for the CKM Matrix](ckmmatrix-relations.md)

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/PhaseFreedom.lean)
