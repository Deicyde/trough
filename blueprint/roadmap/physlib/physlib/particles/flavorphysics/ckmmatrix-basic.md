---
declaration: module
origin: cited
lean: phaseShiftMatrix, phaseShiftMatrix_one, phaseShiftMatrix_star, phaseShiftMatrix_mul, phaseShift, phaseShift_coe_matrix, PhaseShiftRelation, phaseShiftRelation_refl
statement: formalized
proof: formalized
---

# The CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.Basic`, [Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean): 45 declarations, 44 with a docstring.

> The definition of the type of CKM matrices as unitary $3×3$-matrices.
>
> An equivalence relation on CKM matrices is defined, where two matrices are equivalent if they are
> related by phase shifts.
>
> The notation `[V]ud` etc can be used for the elements of a CKM matrix, and
> `[V]ud|us` etc for the ratios of elements.

**`phaseShiftMatrix`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L32).

> Given three real numbers `a b c` the complex matrix with `exp (I * a)` etc on the
> leading diagonal.

```lean
def phaseShiftMatrix (a b c : ℝ) : Matrix (Fin 3) (Fin 3) ℂ
```

**`phaseShiftMatrix_one`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L36).

> The phase shift matrix for zero-phases is the identity.

```lean
lemma phaseShiftMatrix_one : phaseShiftMatrix 0 0 0 = 1
```

**`phaseShiftMatrix_star`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L43).

> The conjugate transpose of the phase shift matrix is the phase-shift matrix
> with negated phases.

```lean
lemma phaseShiftMatrix_star (a b c : ℝ) :
    (phaseShiftMatrix a b c)ᴴ = phaseShiftMatrix (- a) (- b) (- c)
```

**`phaseShiftMatrix_mul`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L52).

> The multiple of two phase shift matrices is equal to the phase shift matrix with
> added phases.

```lean
lemma phaseShiftMatrix_mul (a b c d e f : ℝ) :
    phaseShiftMatrix a b c * phaseShiftMatrix d e f = phaseShiftMatrix (a + d) (b + e) (c + f)
```

**`phaseShift`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L62).

> Given three real numbers `a b c` the unitary matrix with `exp (I * a)` etc on the
> leading diagonal.

```lean
def phaseShift (a b c : ℝ) : unitaryGroup (Fin 3) ℂ
```

**`phaseShift_coe_matrix`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L72).

> The underlying matrix of the phase-shift element of the unitary group is the
> phase-shift matrix.

```lean
lemma phaseShift_coe_matrix (a b c : ℝ) : ↑(phaseShift a b c) = phaseShiftMatrix a b c
```

**`PhaseShiftRelation`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L76).

> The relation on unitary matrices (CKM matrices) satisfied if two unitary matrices
> are related by phase shifts of quarks.

```lean
def PhaseShiftRelation (U V : unitaryGroup (Fin 3) ℂ) : Prop
```

**`phaseShiftRelation_refl`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L80).

> The relation `PhaseShiftRelation` is reflective.

```lean
lemma phaseShiftRelation_refl (U : unitaryGroup (Fin 3) ℂ) : PhaseShiftRelation U U
```

**`phaseShiftRelation_symm`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L86).

> The relation `PhaseShiftRelation` is symmetric.

```lean
lemma phaseShiftRelation_symm {U V : unitaryGroup (Fin 3) ℂ} :
    PhaseShiftRelation U V → PhaseShiftRelation V U
```

**`phaseShiftRelation_trans`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L95).

> The relation `PhaseShiftRelation` is transitive.

```lean
lemma phaseShiftRelation_trans {U V W : unitaryGroup (Fin 3) ℂ} :
    PhaseShiftRelation U V → PhaseShiftRelation V W → PhaseShiftRelation U W
```

**`phaseShiftRelation_equiv`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L104).

> The relation `PhaseShiftRelation` is an equivalence relation.

```lean
lemma phaseShiftRelation_equiv : Equivalence PhaseShiftRelation
```

**`CKMMatrix`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L110).

> The type of CKM matrices.

```lean
def CKMMatrix : Type
```

**`CKMMatrix_ext`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L113).

> Two CKM matrices are equal if their underlying unitary matrices are equal.

```lean
lemma CKMMatrix_ext {U V : CKMMatrix} (h : U.val = V.val) : U = V
```

**`CKMMatrixSetoid`**, an instance, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L143).

> The setoid of CKM matrices defined by phase shifts of fermions.

```lean
instance CKMMatrixSetoid : Setoid CKMMatrix
```

**`phaseShiftApply`**, a def, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L147).

> The matrix obtained from `V` by shifting the phases of the fermions.

```lean
def phaseShiftApply (V : CKMMatrix) (a b c d e f : ℝ) : CKMMatrix
```

**`phaseShiftApply.equiv`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L153).

> A CKM matrix is equivalent to a phase-shift of itself.

```lean
lemma equiv (V : CKMMatrix) (a b c d e f : ℝ) :
    V ≈ phaseShiftApply V a b c d e f
```

**`phaseShiftApply.ud`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L160).

> The `ud` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma ud (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 0 0 = cexp (a * I + d * I) * V.1 0 0
```

**`phaseShiftApply.us`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L169).

> The `us` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma us (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 0 1 = cexp (a * I + e * I) * V.1 0 1
```

**`phaseShiftApply.ub`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L178).

> The `ub` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma ub (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 0 2 = cexp (a * I + f * I) * V.1 0 2
```

**`phaseShiftApply.cd`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L187).

> The `cd` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma cd (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 1 0= cexp (b * I + d * I) * V.1 1 0
```

**`phaseShiftApply.cs`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L196).

> The `cs` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma cs (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 1 1 = cexp (b * I + e * I) * V.1 1 1
```

**`phaseShiftApply.cb`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L205).

> The `cb` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma cb (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 1 2 = cexp (b * I + f * I) * V.1 1 2
```

**`phaseShiftApply.td`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L214).

> The `td` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma td (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 2 0= cexp (c * I + d * I) * V.1 2 0
```

**`phaseShiftApply.ts`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L223).

> The `ts` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma ts (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 2 1 = cexp (c * I + e * I) * V.1 2 1
```

**`phaseShiftApply.tb`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L232).

> The `tb` component of the CKM matrix obtained after applying a phase shift.

```lean
lemma tb (V : CKMMatrix) (a b c d e f : ℝ) :
    (phaseShiftApply V a b c d e f).1 2 2 = cexp (c * I + f * I) * V.1 2 2
```

**`VAbs'`**, a def, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L243).

> The absolute value of the `(i,j)`th element of `V`.

```lean
def VAbs' (V : unitaryGroup (Fin 3) ℂ) (i j : Fin 3) : ℝ
```

**`VAbs'_equiv`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L248).

> If two CKM matrices are equivalent (under phase shifts), then their absolute values
> are the same.

```lean
lemma VAbs'_equiv (i j : Fin 3) (V U : CKMMatrix) (h : V ≈ U) :
    VAbs' V i j = VAbs' U i j
```

**`VAbs`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L257).

> The absolute value of the `(i,j)`th any representative of `⟦V⟧`.

```lean
def VAbs (i j : Fin 3) : Quotient CKMMatrixSetoid → ℝ
```

**`VudAbs`**, an abbrev, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L263).

> The absolute value of the `ud`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VudAbs
```

**`VusAbs`**, an abbrev, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L268).

> The absolute value of the `us`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VusAbs
```

**`VubAbs`**, an abbrev, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L273).

> The absolute value of the `ub`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VubAbs
```

**`VcdAbs`**, an abbrev, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L278).

> The absolute value of the `cd`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VcdAbs
```

**`VcsAbs`**, an abbrev, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L283).

> The absolute value of the `cs`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VcsAbs
```

**`VcbAbs`**, an abbrev, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L288).

> The absolute value of the `cb`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VcbAbs
```

**`VtdAbs`**, an abbrev, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L293).

> The absolute value of the `td`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VtdAbs
```

**`VtsAbs`**, an abbrev, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L298).

> The absolute value of the `ts`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VtsAbs
```

**`VtbAbs`**, an abbrev, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L303).

> The absolute value of the `tb`th element of a representative of an equivalence class of
> CKM matrices.

```lean
abbrev VtbAbs
```

**`CKMMatrix.Rubud`**, a def, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L311).

> The ratio of the `ub` and `ud` elements of a CKM matrix.

```lean
def Rubud (V : CKMMatrix) : ℂ
```

**`CKMMatrix.Rusud`**, a def, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L317).

> The ratio of the `us` and `ud` elements of a CKM matrix.

```lean
def Rusud (V : CKMMatrix) : ℂ
```

**`CKMMatrix.Rudus`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L323).

> The ratio of the `ud` and `us` elements of a CKM matrix.

```lean
def Rudus (V : CKMMatrix) : ℂ
```

**`CKMMatrix.Rubus`**, a def, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L329).

> The ratio of the `ub` and `us` elements of a CKM matrix.

```lean
def Rubus (V : CKMMatrix) : ℂ
```

**`CKMMatrix.Rcdcb`**, a def, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L335).

> The ratio of the `cd` and `cb` elements of a CKM matrix.

```lean
def Rcdcb (V : CKMMatrix) : ℂ
```

**`CKMMatrix.Rcdcb_mul_cb`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L340).

```lean
lemma Rcdcb_mul_cb {V : CKMMatrix} (h : [V]cb ≠ 0) : [V]cd = Rcdcb V * [V]cb
```

**`CKMMatrix.Rcscb`**, a def, [line 344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L344).

> The ratio of the `cs` and `cb` elements of a CKM matrix.

```lean
def Rcscb (V : CKMMatrix) : ℂ
```

**`CKMMatrix.Rcscb_mul_cb`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean#L351).

> Multiplying the ratio of the `cs` by `cb` element of a CKM matrix by the `cb` element
> returns the `cs` element, as long as the `cb` element is non-zero.

```lean
lemma Rcscb_mul_cb {V : CKMMatrix} (h : [V]cb ≠ 0) : [V]cs = Rcscb V * [V]cb
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Basic.lean)
