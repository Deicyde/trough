---
declaration: module
origin: cited
lean: CKMMatrix.VAbs_sum_sq_row_eq_one, CKMMatrix.fst_row_normalized_abs, CKMMatrix.snd_row_normalized_abs, CKMMatrix.thd_row_normalized_abs, CKMMatrix.fst_row_normalized_normSq, CKMMatrix.snd_row_normalized_normSq, CKMMatrix.thd_row_normalized_normSq, CKMMatrix.normSq_Vud_plus_normSq_Vus
statement: formalized
proof: formalized
---

# Relations for the CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.Relations`, [Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean): 37 declarations, 7 with a docstring.

> This file contains a collection of relations and properties between the elements of the CKM
> matrix.

**`CKMMatrix.VAbs_sum_sq_row_eq_one`**, a lemma, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L29).

> The absolute value squared of any row of a CKM matrix is `1`, in terms of `Vabs`.

```lean
lemma VAbs_sum_sq_row_eq_one (V : Quotient CKMMatrixSetoid) (i : Fin 3) :
    (VAbs i 0 V) ^ 2 + (VAbs i 1 V) ^ 2 + (VAbs i 2 V) ^ 2 = 1
```

**`CKMMatrix.fst_row_normalized_abs`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L46).

> The absolute value squared of the first row of a CKM matrix is `1`, in terms of `norm`.

```lean
lemma fst_row_normalized_abs (V : CKMMatrix) :
    norm [V]ud ^ 2 + norm [V]us ^ 2 + norm [V]ub ^ 2 = 1
```

**`CKMMatrix.snd_row_normalized_abs`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L51).

> The absolute value squared of the second row of a CKM matrix is `1`, in terms of `norm`.

```lean
lemma snd_row_normalized_abs (V : CKMMatrix) :
    norm [V]cd ^ 2 + norm [V]cs ^ 2 + norm [V]cb ^ 2 = 1
```

**`CKMMatrix.thd_row_normalized_abs`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L56).

> The absolute value squared of the third row of a CKM matrix is `1`, in terms of `norm`.

```lean
lemma thd_row_normalized_abs (V : CKMMatrix) :
    norm [V]td ^ 2 + norm [V]ts ^ 2 + norm [V]tb ^ 2 = 1
```

**`CKMMatrix.fst_row_normalized_normSq`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L61).

> The absolute value squared of the first row of a CKM matrix is `1`, in terms of `nomSq`.

```lean
lemma fst_row_normalized_normSq (V : CKMMatrix) :
    normSq [V]ud + normSq [V]us + normSq [V]ub = 1
```

**`CKMMatrix.snd_row_normalized_normSq`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L67).

> The absolute value squared of the second row of a CKM matrix is `1`, in terms of `nomSq`.

```lean
lemma snd_row_normalized_normSq (V : CKMMatrix) :
    normSq [V]cd + normSq [V]cs + normSq [V]cb = 1
```

**`CKMMatrix.thd_row_normalized_normSq`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L73).

> The absolute value squared of the third row of a CKM matrix is `1`, in terms of `nomSq`.

```lean
lemma thd_row_normalized_normSq (V : CKMMatrix) :
    normSq [V]td + normSq [V]ts + normSq [V]tb = 1
```

**`CKMMatrix.normSq_Vud_plus_normSq_Vus`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L78).

```lean
lemma normSq_Vud_plus_normSq_Vus (V : CKMMatrix) :
    normSq [V]ud + normSq [V]us = 1 - normSq [V]ub
```

**`CKMMatrix.VudAbs_sq_add_VusAbs_sq`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L82).

```lean
lemma VudAbs_sq_add_VusAbs_sq : VudAbs V ^ 2 + VusAbs V ^2 = 1 - VubAbs V ^2
```

**`CKMMatrix.ud_us_ne_zero_iff_ub_ne_one`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L85).

```lean
lemma ud_us_ne_zero_iff_ub_ne_one (V : CKMMatrix) :
    [V]ud ≠ 0 ∨ [V]us ≠ 0 ↔ norm [V]ub ≠ 1
```

**`CKMMatrix.normSq_Vud_plus_normSq_Vus_ne_zero_ℝ`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L102).

```lean
lemma normSq_Vud_plus_normSq_Vus_ne_zero_ℝ {V : CKMMatrix} (hb : [V]ud ≠ 0 ∨ [V]us ≠ 0) :
    normSq [V]ud + normSq [V]us ≠ 0
```

**`CKMMatrix.VAbsub_ne_zero_Vud_Vus_ne_zero`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L118).

```lean
lemma VAbsub_ne_zero_Vud_Vus_ne_zero {V : Quotient CKMMatrixSetoid}
    (hV : VAbs 0 2 V ≠ 1) :(VudAbs V ^ 2 + VusAbs V ^ 2) ≠ 0
```

**`CKMMatrix.VAbsub_ne_zero_sqrt_Vud_Vus_ne_zero`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L128).

```lean
lemma VAbsub_ne_zero_sqrt_Vud_Vus_ne_zero {V : Quotient CKMMatrixSetoid}
    (hV : VAbs 0 2 V ≠ 1) : √(VudAbs V ^ 2 + VusAbs V ^ 2) ≠ 0
```

**`CKMMatrix.normSq_Vud_plus_normSq_Vus_ne_zero_ℂ`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L139).

```lean
lemma normSq_Vud_plus_normSq_Vus_ne_zero_ℂ {V : CKMMatrix} (hb : [V]ud ≠ 0 ∨ [V]us ≠ 0) :
    (normSq [V]ud : ℂ) + normSq [V]us ≠ 0
```

**`CKMMatrix.Vabs_sq_add_ne_zero`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L146).

```lean
lemma Vabs_sq_add_ne_zero {V : CKMMatrix} (hb : [V]ud ≠ 0 ∨ [V]us ≠ 0) :
    ((VudAbs ⟦V⟧ : ℂ) * ↑(VudAbs ⟦V⟧) + ↑(VusAbs ⟦V⟧) * ↑(VusAbs ⟦V⟧)) ≠ 0
```

**`CKMMatrix.fst_row_orthog_snd_row`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L155).

```lean
lemma fst_row_orthog_snd_row (V : CKMMatrix) :
    [V]cd * conj [V]ud + [V]cs * conj [V]us + [V]cb * conj [V]ub = 0
```

**`CKMMatrix.fst_row_orthog_thd_row`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L164).

```lean
lemma fst_row_orthog_thd_row (V : CKMMatrix) :
    [V]td * conj [V]ud + [V]ts * conj [V]us + [V]tb * conj [V]ub = 0
```

**`CKMMatrix.Vcd_mul_conj_Vud`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L173).

```lean
lemma Vcd_mul_conj_Vud (V : CKMMatrix) :
    [V]cd * conj [V]ud = -[V]cs * conj [V]us - [V]cb * conj [V]ub
```

**`CKMMatrix.Vcs_mul_conj_Vus`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L177).

```lean
lemma Vcs_mul_conj_Vus (V : CKMMatrix) :
    [V]cs * conj [V]us = - [V]cd * conj [V]ud - [V]cb * conj [V]ub
```

**`CKMMatrix.VAbs_thd_eq_one_fst_eq_zero`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L183).

```lean
lemma VAbs_thd_eq_one_fst_eq_zero {V : Quotient CKMMatrixSetoid} {i : Fin 3} (hV : VAbs i 2 V = 1) :
    VAbs i 0 V = 0
```

**`CKMMatrix.VAbs_thd_eq_one_snd_eq_zero`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L190).

```lean
lemma VAbs_thd_eq_one_snd_eq_zero {V : Quotient CKMMatrixSetoid} {i : Fin 3} (hV : VAbs i 2 V = 1) :
    VAbs i 1 V = 0
```

**`CKMMatrix.conj_Vtb_cross_product`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L199).

```lean
lemma conj_Vtb_cross_product {V : CKMMatrix} {τ : ℝ}
    (hτ : [V]t = cexp (τ * I) • (conj [V]u ⨯₃ conj [V]c)) :
    conj [V]tb = cexp (- τ * I) * ([V]cs * [V]ud - [V]us * [V]cd)
```

**`CKMMatrix.conj_Vtb_mul_Vud`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L216).

```lean
lemma conj_Vtb_mul_Vud {V : CKMMatrix} {τ : ℝ}
    (hτ : [V]t = cexp (τ * I) • (conj [V]u ⨯₃ conj [V]c)) :
    cexp (τ * I) * conj [V]tb * conj [V]ud =
    [V]cs * (normSq [V]ud + normSq [V]us) + [V]cb * conj [V]ub * [V]us
```

**`CKMMatrix.conj_Vtb_mul_Vus`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L231).

```lean
lemma conj_Vtb_mul_Vus {V : CKMMatrix} {τ : ℝ}
    (hτ : [V]t = cexp (τ * I) • (conj [V]u ⨯₃ conj [V]c)) :
    cexp (τ * I) * conj [V]tb * conj [V]us =
    - ([V]cd * (normSq [V]ud + normSq [V]us) + [V]cb * conj ([V]ub) * [V]ud)
```

**`CKMMatrix.cs_of_ud_us_ub_cb_tb`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L246).

```lean
lemma cs_of_ud_us_ub_cb_tb {V : CKMMatrix} (h : [V]ud ≠ 0 ∨ [V]us ≠ 0)
    {τ : ℝ} (hτ : [V]t = cexp (τ * I) • (conj ([V]u) ⨯₃ conj ([V]c))) :
    [V]cs = (- conj [V]ub * [V]us * [V]cb +
      cexp (τ * I) * conj [V]tb * conj [V]ud) / (normSq [V]ud + normSq [V]us)
```

**`CKMMatrix.cd_of_ud_us_ub_cb_tb`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L255).

```lean
lemma cd_of_ud_us_ub_cb_tb {V : CKMMatrix} (h : [V]ud ≠ 0 ∨ [V]us ≠ 0)
    {τ : ℝ} (hτ : [V]t = cexp (τ * I) • (conj ([V]u) ⨯₃ conj ([V]c))) :
    [V]cd = - (conj [V]ub * [V]ud * [V]cb + cexp (τ * I) * conj [V]tb * conj [V]us) /
      (normSq [V]ud + normSq [V]us)
```

**`CKMMatrix.VAbs_ge_zero`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L268).

```lean
lemma VAbs_ge_zero (i j : Fin 3) (V : Quotient CKMMatrixSetoid) : 0 ≤ VAbs i j V
```

**`CKMMatrix.VAbs_leq_one`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L273).

```lean
lemma VAbs_leq_one (i j : Fin 3) (V : Quotient CKMMatrixSetoid) : VAbs i j V ≤ 1
```

**`CKMMatrix.VAbs_sum_sq_col_eq_one`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L287).

```lean
lemma VAbs_sum_sq_col_eq_one (V : Quotient CKMMatrixSetoid) (i : Fin 3) :
    (VAbs 0 i V) ^ 2 + (VAbs 1 i V) ^ 2 + (VAbs 2 i V) ^ 2 = 1
```

**`CKMMatrix.thd_col_normalized_abs`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L302).

```lean
lemma thd_col_normalized_abs (V : CKMMatrix) :
    norm [V]ub ^ 2 + norm [V]cb ^ 2 + norm [V]tb ^ 2 = 1
```

**`CKMMatrix.thd_col_normalized_normSq`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L308).

```lean
lemma thd_col_normalized_normSq (V : CKMMatrix) :
    normSq [V]ub + normSq [V]cb + normSq [V]tb = 1
```

**`CKMMatrix.cb_eq_zero_of_ud_us_zero`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L314).

```lean
lemma cb_eq_zero_of_ud_us_zero {V : CKMMatrix} (h : [V]ud = 0 ∧ [V]us = 0) :
    [V]cb = 0
```

**`CKMMatrix.cs_of_ud_us_zero`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L327).

```lean
lemma cs_of_ud_us_zero {V : CKMMatrix} (ha : ¬ ([V]ud ≠ 0 ∨ [V]us ≠ 0)) :
    VcsAbs ⟦V⟧ = √(1 - VcdAbs ⟦V⟧ ^ 2)
```

**`CKMMatrix.VcbAbs_sq_add_VtbAbs_sq`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L348).

```lean
lemma VcbAbs_sq_add_VtbAbs_sq (V : Quotient CKMMatrixSetoid) :
    VcbAbs V ^ 2 + VtbAbs V ^ 2 = 1 - VubAbs V ^2
```

**`CKMMatrix.cb_tb_ne_zero_iff_ub_ne_one`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L352).

```lean
lemma cb_tb_ne_zero_iff_ub_ne_one (V : CKMMatrix) :
    [V]cb ≠ 0 ∨ [V]tb ≠ 0 ↔ norm [V]ub ≠ 1
```

**`CKMMatrix.VAbs_fst_col_eq_one_snd_eq_zero`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L375).

```lean
lemma VAbs_fst_col_eq_one_snd_eq_zero {V : Quotient CKMMatrixSetoid} {i : Fin 3}
    (hV : VAbs 0 i V = 1) : VAbs 1 i V = 0
```

**`CKMMatrix.VAbs_fst_col_eq_one_thd_eq_zero`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean#L382).

```lean
lemma VAbs_fst_col_eq_one_thd_eq_zero {V : Quotient CKMMatrixSetoid} {i : Fin 3}
    (hV : VAbs 0 i V = 1) : VAbs 2 i V = 0
```

## Depends on

- [Rows for the CKM Matrix](ckmmatrix-rows.md)

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Relations.lean)
