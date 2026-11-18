---
declaration: module
origin: cited
lean: S₁₂, S₁₃, S₂₃, θ₁₂, θ₁₃, θ₂₃, C₁₂, C₁₃
statement: formalized
proof: formalized
---

# Standard parameters for the CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.StandardParameterization.StandardParameters`, [Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean): 65 declarations, 16 with a docstring.

> Given a CKM matrix `V` we can extract four real numbers `θ₁₂`, `θ₁₃`, `θ₂₃` and `δ₁₃`.
> These, when used in the standard parameterization return `V` up to equivalence.
>
> This leads to the theorem `standParam.exists_for_CKMatrix` which says that up to equivalence every
> CKM matrix can be written using the standard parameterization.

**`S₁₂`**, a def, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L31).

> Given a CKM matrix `V` the real number corresponding to `sin θ₁₂` in the
> standard parameterization. -

```lean
def S₁₂ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`S₁₃`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L35).

> Given a CKM matrix `V` the real number corresponding to `sin θ₁₃` in the
> standard parameterization. -

```lean
def S₁₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`S₂₃`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L39).

> Given a CKM matrix `V` the real number corresponding to `sin θ₂₃` in the
> standard parameterization. -

```lean
def S₂₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`θ₁₂`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L45).

> Given a CKM matrix `V` the real number corresponding to `θ₁₂` in the
> standard parameterization. -

```lean
def θ₁₂ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`θ₁₃`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L49).

> Given a CKM matrix `V` the real number corresponding to `θ₁₃` in the
> standard parameterization. -

```lean
def θ₁₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`θ₂₃`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L53).

> Given a CKM matrix `V` the real number corresponding to `θ₂₃` in the
> standard parameterization. -

```lean
def θ₂₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`C₁₂`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L57).

> Given a CKM matrix `V` the real number corresponding to `cos θ₁₂` in the
> standard parameterization. -

```lean
def C₁₂ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`C₁₃`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L61).

> Given a CKM matrix `V` the real number corresponding to `cos θ₁₃` in the
> standard parameterization. -

```lean
def C₁₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`C₂₃`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L65).

> Given a CKM matrix `V` the real number corresponding to `sin θ₂₃` in the
> standard parameterization. -

```lean
def C₂₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`δ₁₃`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L69).

> Given a CKM matrix `V` the real number corresponding to the phase `δ₁₃` in the
> standard parameterization. -

```lean
def δ₁₃ (V : Quotient CKMMatrixSetoid) : ℝ
```

**`S₁₂_nonneg`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L75).

> For a CKM matrix `sin θ₁₂` is non-negative.

```lean
lemma S₁₂_nonneg (V : Quotient CKMMatrixSetoid) : 0 ≤ S₁₂ V
```

**`S₁₃_nonneg`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L79).

> For a CKM matrix `sin θ₁₃` is non-negative.

```lean
lemma S₁₃_nonneg (V : Quotient CKMMatrixSetoid) : 0 ≤ S₁₃ V
```

**`S₂₃_nonneg`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L83).

> For a CKM matrix `sin θ₂₃` is non-negative.

```lean
lemma S₂₃_nonneg (V : Quotient CKMMatrixSetoid) : 0 ≤ S₂₃ V
```

**`S₁₂_leq_one`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L90).

> For a CKM matrix `sin θ₁₂` is less than or equal to 1.

```lean
lemma S₁₂_leq_one (V : Quotient CKMMatrixSetoid) : S₁₂ V ≤ 1
```

**`S₁₃_leq_one`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L96).

> For a CKM matrix `sin θ₁₃` is less than or equal to 1.

```lean
lemma S₁₃_leq_one (V : Quotient CKMMatrixSetoid) : S₁₃ V ≤ 1
```

**`S₂₃_leq_one`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L100).

> For a CKM matrix `sin θ₂₃` is less than or equal to 1.

```lean
lemma S₂₃_leq_one (V : Quotient CKMMatrixSetoid) : S₂₃ V ≤ 1
```

**`S₁₂_eq_sin_θ₁₂`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L108).

```lean
lemma S₁₂_eq_sin_θ₁₂ (V : Quotient CKMMatrixSetoid) : Real.sin (θ₁₂ V) = S₁₂ V
```

**`S₁₃_eq_sin_θ₁₃`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L111).

```lean
lemma S₁₃_eq_sin_θ₁₃ (V : Quotient CKMMatrixSetoid) : Real.sin (θ₁₃ V) = S₁₃ V
```

**`S₂₃_eq_sin_θ₂₃`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L114).

```lean
lemma S₂₃_eq_sin_θ₂₃ (V : Quotient CKMMatrixSetoid) : Real.sin (θ₂₃ V) = S₂₃ V
```

**`S₁₂_eq_ℂsin_θ₁₂`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L117).

```lean
lemma S₁₂_eq_ℂsin_θ₁₂ (V : Quotient CKMMatrixSetoid) : Complex.sin (θ₁₂ V) = S₁₂ V
```

**`S₁₃_eq_ℂsin_θ₁₃`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L120).

```lean
lemma S₁₃_eq_ℂsin_θ₁₃ (V : Quotient CKMMatrixSetoid) : Complex.sin (θ₁₃ V) = S₁₃ V
```

**`S₂₃_eq_ℂsin_θ₂₃`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L123).

```lean
lemma S₂₃_eq_ℂsin_θ₂₃ (V : Quotient CKMMatrixSetoid) : Complex.sin (θ₂₃ V) = S₂₃ V
```

**`complexAbs_sin_θ₁₂`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L126).

```lean
lemma complexAbs_sin_θ₁₂ (V : Quotient CKMMatrixSetoid) :
    norm (Complex.sin (θ₁₂ V)) = sin (θ₁₂ V)
```

**`complexAbs_sin_θ₁₃`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L131).

```lean
lemma complexAbs_sin_θ₁₃ (V : Quotient CKMMatrixSetoid) :
    norm (Complex.sin (θ₁₃ V)) = sin (θ₁₃ V)
```

**`complexAbs_sin_θ₂₃`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L136).

```lean
lemma complexAbs_sin_θ₂₃ (V : Quotient CKMMatrixSetoid) :
    norm (Complex.sin (θ₂₃ V)) = sin (θ₂₃ V)
```

**`S₁₂_of_Vub_one`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L141).

```lean
lemma S₁₂_of_Vub_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V = 1) : S₁₂ V = 0
```

**`S₁₃_of_Vub_one`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L144).

```lean
lemma S₁₃_of_Vub_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V = 1) : S₁₃ V = 1
```

**`S₂₃_of_Vub_eq_one`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L146).

```lean
lemma S₂₃_of_Vub_eq_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V = 1) : S₂₃ V = VcdAbs V
```

**`S₂₃_of_Vub_ne_one`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L149).

```lean
lemma S₂₃_of_Vub_ne_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V ≠ 1) :
    S₂₃ V = VcbAbs V / √ (VudAbs V ^ 2 + VusAbs V ^ 2)
```

**`C₁₂_eq_ℂcos_θ₁₂`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L157).

```lean
lemma C₁₂_eq_ℂcos_θ₁₂ (V : Quotient CKMMatrixSetoid) : Complex.cos (θ₁₂ V) = C₁₂ V
```

**`C₁₃_eq_ℂcos_θ₁₃`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L160).

```lean
lemma C₁₃_eq_ℂcos_θ₁₃ (V : Quotient CKMMatrixSetoid) : Complex.cos (θ₁₃ V) = C₁₃ V
```

**`C₂₃_eq_ℂcos_θ₂₃`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L163).

```lean
lemma C₂₃_eq_ℂcos_θ₂₃ (V : Quotient CKMMatrixSetoid) : Complex.cos (θ₂₃ V) = C₂₃ V
```

**`complexAbs_cos_θ₁₂`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L166).

```lean
lemma complexAbs_cos_θ₁₂ (V : Quotient CKMMatrixSetoid) : norm (Complex.cos (θ₁₂ V)) =
    cos (θ₁₂ V)
```

**`complexAbs_cos_θ₁₃`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L171).

```lean
lemma complexAbs_cos_θ₁₃ (V : Quotient CKMMatrixSetoid) : norm (Complex.cos (θ₁₃ V)) =
    cos (θ₁₃ V)
```

**`complexAbs_cos_θ₂₃`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L176).

```lean
lemma complexAbs_cos_θ₂₃ (V : Quotient CKMMatrixSetoid) : norm (Complex.cos (θ₂₃ V)) =
    cos (θ₂₃ V)
```

**`S₁₂_sq_add_C₁₂_sq`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L181).

```lean
lemma S₁₂_sq_add_C₁₂_sq (V : Quotient CKMMatrixSetoid) : S₁₂ V ^ 2 + C₁₂ V ^ 2 = 1
```

**`S₁₃_sq_add_C₁₃_sq`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L184).

```lean
lemma S₁₃_sq_add_C₁₃_sq (V : Quotient CKMMatrixSetoid) : S₁₃ V ^ 2 + C₁₃ V ^ 2 = 1
```

**`S₂₃_sq_add_C₂₃_sq`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L187).

```lean
lemma S₂₃_sq_add_C₂₃_sq (V : Quotient CKMMatrixSetoid) : S₂₃ V ^ 2 + C₂₃ V ^ 2 = 1
```

**`C₁₂_of_Vub_one`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L190).

```lean
lemma C₁₂_of_Vub_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V = 1) : C₁₂ V = 1
```

**`C₁₃_of_Vub_eq_one`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L193).

```lean
lemma C₁₃_of_Vub_eq_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V = 1) : C₁₃ V = 0
```

**`C₁₂_eq_Vud_div_sqrt`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L197).

```lean
lemma C₁₂_eq_Vud_div_sqrt {V : Quotient CKMMatrixSetoid} (ha : VubAbs V ≠ 1) :
    C₁₂ V = VudAbs V / √ (VudAbs V ^ 2 + VusAbs V ^ 2)
```

**`C₁₃_eq_add_sq`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L207).

```lean
lemma C₁₃_eq_add_sq (V : Quotient CKMMatrixSetoid) : C₁₃ V = √ (VudAbs V ^ 2 + VusAbs V ^ 2)
```

**`C₂₃_of_Vub_ne_one`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L210).

```lean
lemma C₂₃_of_Vub_ne_one {V : Quotient CKMMatrixSetoid} (ha : VubAbs V ≠ 1) :
    C₂₃ V = VtbAbs V / √ (VudAbs V ^ 2 + VusAbs V ^ 2)
```

**`VudAbs_eq_C₁₂_mul_C₁₃`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L226).

```lean
lemma VudAbs_eq_C₁₂_mul_C₁₃ (V : Quotient CKMMatrixSetoid) : VudAbs V = C₁₂ V * C₁₃ V
```

**`VusAbs_eq_S₁₂_mul_C₁₃`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L233).

```lean
lemma VusAbs_eq_S₁₂_mul_C₁₃ (V : Quotient CKMMatrixSetoid) : VusAbs V = S₁₂ V * C₁₃ V
```

**`VubAbs_eq_S₁₃`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L240).

```lean
lemma VubAbs_eq_S₁₃ (V : Quotient CKMMatrixSetoid) : VubAbs V = S₁₃ V
```

**`VcbAbs_eq_S₂₃_mul_C₁₃`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L242).

```lean
lemma VcbAbs_eq_S₂₃_mul_C₁₃ (V : Quotient CKMMatrixSetoid) : VcbAbs V = S₂₃ V * C₁₃ V
```

**`VtbAbs_eq_C₂₃_mul_C₁₃`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L249).

```lean
lemma VtbAbs_eq_C₂₃_mul_C₁₃ (V : Quotient CKMMatrixSetoid) : VtbAbs V = C₂₃ V * C₁₃ V
```

**`VubAbs_of_cos_θ₁₃_zero`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L256).

```lean
lemma VubAbs_of_cos_θ₁₃_zero {V : Quotient CKMMatrixSetoid} (h1 : Real.cos (θ₁₃ V) = 0) :
    VubAbs V = 1
```

**`Vs_zero_iff_cos_sin_zero`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L263).

```lean
lemma Vs_zero_iff_cos_sin_zero (V : CKMMatrix) :
    VudAbs ⟦V⟧ = 0 ∨ VubAbs ⟦V⟧ = 0 ∨ VusAbs ⟦V⟧ = 0 ∨ VcbAbs ⟦V⟧ = 0 ∨ VtbAbs ⟦V⟧ = 0
    ↔ Real.cos (θ₁₂ ⟦V⟧) = 0 ∨ Real.cos (θ₁₃ ⟦V⟧) = 0 ∨ Real.cos (θ₂₃ ⟦V⟧) = 0 ∨
      Real.sin (θ₁₂ ⟦V⟧) = 0 ∨ Real.sin (θ₁₃ ⟦V⟧) = 0 ∨ Real.sin (θ₂₃ ⟦V⟧) = 0
```

**`standParam.mulExpδ₁₃_on_param_δ₁₃`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L276).

```lean
lemma mulExpδ₁₃_on_param_δ₁₃ (V : CKMMatrix) (δ₁₃ : ℝ) :
    mulExpδ₁₃ ⟦standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃⟧ =
    sin (θ₁₂ ⟦V⟧) * cos (θ₁₃ ⟦V⟧) ^ 2 * sin (θ₂₃ ⟦V⟧) * sin (θ₁₃ ⟦V⟧)
    * cos (θ₁₂ ⟦V⟧) * cos (θ₂₃ ⟦V⟧) * cexp (I * δ₁₃)
```

**`standParam.mulExpδ₁₃_on_param_eq_zero_iff`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L284).

```lean
lemma mulExpδ₁₃_on_param_eq_zero_iff (V : CKMMatrix) (δ₁₃ : ℝ) :
    mulExpδ₁₃ ⟦standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃⟧ = 0 ↔
      VudAbs ⟦V⟧ = 0 ∨ VubAbs ⟦V⟧ = 0 ∨ VusAbs ⟦V⟧ = 0 ∨ VcbAbs ⟦V⟧ = 0 ∨ VtbAbs ⟦V⟧ = 0
```

**`standParam.mulExpδ₁₃_on_param_abs`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L297).

```lean
lemma mulExpδ₁₃_on_param_abs (V : CKMMatrix) (δ₁₃ : ℝ) :
    norm (mulExpδ₁₃ ⟦standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃⟧) =
    sin (θ₁₂ ⟦V⟧) * cos (θ₁₃ ⟦V⟧) ^ 2 * sin (θ₂₃ ⟦V⟧) * sin (θ₁₃ ⟦V⟧)
    * cos (θ₁₂ ⟦V⟧) * cos (θ₂₃ ⟦V⟧)
```

**`standParam.mulExpδ₁₃_on_param_ne_zero_arg`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L307).

```lean
lemma mulExpδ₁₃_on_param_ne_zero_arg (V : CKMMatrix) (δ₁₃ : ℝ)
    (h1 : mulExpδ₁₃ ⟦standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃⟧ ≠ 0) :
    cexp (arg (mulExpδ₁₃ ⟦standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃⟧) * I) =
    cexp (δ₁₃ * I)
```

**`standParam.on_param_cos_θ₁₃_eq_zero`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L323).

```lean
lemma on_param_cos_θ₁₃_eq_zero {V : CKMMatrix} (δ₁₃ : ℝ) (h : Real.cos (θ₁₃ ⟦V⟧) = 0) :
    standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃ ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.on_param_cos_θ₁₂_eq_zero`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L334).

```lean
lemma on_param_cos_θ₁₂_eq_zero {V : CKMMatrix} (δ₁₃ : ℝ) (h : Real.cos (θ₁₂ ⟦V⟧) = 0) :
    standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃ ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.on_param_cos_θ₂₃_eq_zero`**, a lemma, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L344).

```lean
lemma on_param_cos_θ₂₃_eq_zero {V : CKMMatrix} (δ₁₃ : ℝ) (h : Real.cos (θ₂₃ ⟦V⟧) = 0) :
    standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃ ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.on_param_sin_θ₁₃_eq_zero`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L354).

```lean
lemma on_param_sin_θ₁₃_eq_zero {V : CKMMatrix} (δ₁₃ : ℝ) (h : Real.sin (θ₁₃ ⟦V⟧) = 0) :
    standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃ ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.on_param_sin_θ₁₂_eq_zero`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L363).

```lean
lemma on_param_sin_θ₁₂_eq_zero {V : CKMMatrix} (δ₁₃ : ℝ) (h : Real.sin (θ₁₂ ⟦V⟧) = 0) :
    standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃ ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.on_param_sin_θ₂₃_eq_zero`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L373).

```lean
lemma on_param_sin_θ₂₃_eq_zero {V : CKMMatrix} (δ₁₃ : ℝ) (h : Real.sin (θ₂₃ ⟦V⟧) = 0) :
    standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₁₃ ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.eq_standParam_of_fstRowThdColRealCond`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L382).

```lean
lemma eq_standParam_of_fstRowThdColRealCond {V : CKMMatrix} (hb : [V]ud ≠ 0 ∨ [V]us ≠ 0)
    (hV : FstRowThdColRealCond V) : V = standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) (- arg [V]ub)
```

**`standParam.eq_standParam_of_ubOnePhaseCond`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L437).

```lean
lemma eq_standParam_of_ubOnePhaseCond {V : CKMMatrix} (hV : ubOnePhaseCond V) :
    V = standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) 0
```

**`standParam.exists_δ₁₃`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L493).

```lean
lemma exists_δ₁₃ (V : CKMMatrix) :
    ∃ (δ₃ : ℝ), V ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) δ₃
```

**`standParam.eq_standardParameterization_δ₃`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L517).

```lean
lemma eq_standardParameterization_δ₃ (V : CKMMatrix) :
    V ≈ standParam (θ₁₂ ⟦V⟧) (θ₁₃ ⟦V⟧) (θ₂₃ ⟦V⟧) (δ₁₃ ⟦V⟧)
```

**`standParam.exists_for_CKMatrix`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean#L542).

```lean
lemma exists_for_CKMatrix (V : CKMMatrix) :
    ∃ (θ₁₂ θ₁₃ θ₂₃ δ₁₃ : ℝ), V ≈ standParam θ₁₂ θ₁₃ θ₂₃ δ₁₃
```

## Depends on

- [Phase freedom of the CKM Matrix](ckmmatrix-phasefreedom.md)
- [Standard parameterization for the CKM Matrix](ckmmatrix-standardparameterization-basic.md)

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/StandardParameterization/StandardParameters.lean)
