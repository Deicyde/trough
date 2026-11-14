---
declaration: module
origin: cited
lean: CKMMatrix.uRow, CKMMatrix.cRow, CKMMatrix.tRow, CKMMatrix.uRow_normalized, CKMMatrix.cRow_normalized, CKMMatrix.tRow_normalized, CKMMatrix.uRow_cRow_orthog, CKMMatrix.uRow_tRow_orthog
statement: formalized
proof: formalized
---

# Rows for the CKM Matrix

The module `Physlib.Particles.FlavorPhysics.CKMMatrix.Rows`, [Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean): 29 declarations, 16 with a docstring.

> This file contains the definition extracting the rows of the CKM matrix and
> proves some properties between them.
>
> The first row can be extracted as `[V]u` for a CKM matrix `V`.

**`CKMMatrix.uRow`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L32).

> The `u`th row of the CKM matrix.

```lean
def uRow (V : CKMMatrix) : Fin 3 → ℂ
```

**`CKMMatrix.cRow`**, a def, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L38).

> The `c`th row of the CKM matrix.

```lean
def cRow (V : CKMMatrix) : Fin 3 → ℂ
```

**`CKMMatrix.tRow`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L44).

> The `t`th row of the CKM matrix.

```lean
def tRow (V : CKMMatrix) : Fin 3 → ℂ
```

**`CKMMatrix.uRow_normalized`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L50).

> The up-quark row of the CKM matrix is normalized to `1`.

```lean
lemma uRow_normalized (V : CKMMatrix) : conj [V]u ⬝ᵥ [V]u = 1
```

**`CKMMatrix.cRow_normalized`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L58).

> The charm-quark row of the CKM matrix is normalized to `1`.

```lean
lemma cRow_normalized (V : CKMMatrix) : conj [V]c ⬝ᵥ [V]c = 1
```

**`CKMMatrix.tRow_normalized`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L66).

> The top-quark row of the CKM matrix is normalized to `1`.

```lean
lemma tRow_normalized (V : CKMMatrix) : conj [V]t ⬝ᵥ [V]t = 1
```

**`CKMMatrix.uRow_cRow_orthog`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L74).

> The up-quark row of the CKM matrix is orthogonal to the charm-quark row.

```lean
lemma uRow_cRow_orthog (V : CKMMatrix) : conj [V]u ⬝ᵥ [V]c = 0
```

**`CKMMatrix.uRow_tRow_orthog`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L83).

> The up-quark row of the CKM matrix is orthogonal to the top-quark row.

```lean
lemma uRow_tRow_orthog (V : CKMMatrix) : conj [V]u ⬝ᵥ [V]t = 0
```

**`CKMMatrix.cRow_uRow_orthog`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L92).

> The charm-quark row of the CKM matrix is orthogonal to the up-quark row.

```lean
lemma cRow_uRow_orthog (V : CKMMatrix) : conj [V]c ⬝ᵥ [V]u = 0
```

**`CKMMatrix.cRow_tRow_orthog`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L101).

> The charm-quark row of the CKM matrix is orthogonal to the top-quark row.

```lean
lemma cRow_tRow_orthog (V : CKMMatrix) : conj [V]c ⬝ᵥ [V]t = 0
```

**`CKMMatrix.tRow_uRow_orthog`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L110).

> The top-quark row of the CKM matrix is orthogonal to the up-quark row.

```lean
lemma tRow_uRow_orthog (V : CKMMatrix) : conj [V]t ⬝ᵥ [V]u = 0
```

**`CKMMatrix.tRow_cRow_orthog`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L119).

> The top-quark row of the CKM matrix is orthogonal to the charm-quark row.

```lean
lemma tRow_cRow_orthog (V : CKMMatrix) : conj [V]t ⬝ᵥ [V]c = 0
```

**`CKMMatrix.uRow_cross_cRow_conj`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L127).

```lean
lemma uRow_cross_cRow_conj (V : CKMMatrix) : conj (conj [V]u ⨯₃ conj [V]c) = [V]u ⨯₃ [V]c
```

**`CKMMatrix.cRow_cross_tRow_conj`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L133).

```lean
lemma cRow_cross_tRow_conj (V : CKMMatrix) : conj (conj [V]c ⨯₃ conj [V]t) = [V]c ⨯₃ [V]t
```

**`CKMMatrix.uRow_cross_cRow_normalized`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L139).

```lean
lemma uRow_cross_cRow_normalized (V : CKMMatrix) :
    conj (conj [V]u ⨯₃ conj [V]c) ⬝ᵥ (conj [V]u ⨯₃ conj [V]c) = 1
```

**`CKMMatrix.cRow_cross_tRow_normalized`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L146).

```lean
lemma cRow_cross_tRow_normalized (V : CKMMatrix) :
    conj (conj [V]c ⨯₃ conj [V]t) ⬝ᵥ (conj [V]c ⨯₃ conj [V]t) = 1
```

**`CKMMatrix.rows`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L155).

> A map from `Fin 3` to each row of a CKM matrix.

```lean
def rows (V : CKMMatrix) : Fin 3 → Fin 3 → ℂ
```

**`CKMMatrix.rows_linearly_independent`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L162).

> The rows of a CKM matrix are linearly independent.

```lean
lemma rows_linearly_independent (V : CKMMatrix) : LinearIndependent ℂ (rows V)
```

**`CKMMatrix.rowBasis`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L180).

> The rows of a CKM matrix as a basis of `ℂ³`.

```lean
noncomputable def rowBasis (V : CKMMatrix) : Basis (Fin 3) ℂ (Fin 3 → ℂ)
```

**`CKMMatrix.cRow_cross_tRow_eq_uRow`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L185).

```lean
lemma cRow_cross_tRow_eq_uRow (V : CKMMatrix) :
    ∃ (κ : ℝ), [V]u = cexp (κ * I) • (conj [V]c ⨯₃ conj [V]t)
```

**`CKMMatrix.uRow_cross_cRow_eq_tRow`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L228).

```lean
lemma uRow_cross_cRow_eq_tRow (V : CKMMatrix) :
    ∃ (τ : ℝ), [V]t = cexp (τ * I) • (conj ([V]u) ⨯₃ conj ([V]c))
```

**`CKMMatrix.ext_Rows`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L272).

```lean
lemma ext_Rows {U V : CKMMatrix} (hu : [U]u = [V]u) (hc : [U]c = [V]c) (ht : [U]t = [V]t) :
    U = V
```

**`phaseShiftApply.ucCross`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L292).

> The cross product of the conjugate of the `u` and `c` rows of a CKM matrix.

```lean
def ucCross : Fin 3 → ℂ
```

**`phaseShiftApply.ucCross_fst`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L295).

```lean
lemma ucCross_fst (V : CKMMatrix) : (ucCross V a b c d e f) 0 =
    cexp ((- a * I) + (- b * I) + (- e * I) + (- f * I)) * (conj [V]u ⨯₃ conj [V]c) 0
```

**`phaseShiftApply.ucCross_snd`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L303).

```lean
lemma ucCross_snd (V : CKMMatrix) : (ucCross V a b c d e f) 1 =
    cexp ((- a * I) + (- b * I) + (- d * I) + (- f * I)) * (conj [V]u ⨯₃ conj [V]c) 1
```

**`phaseShiftApply.ucCross_thd`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L311).

```lean
lemma ucCross_thd (V : CKMMatrix) : (ucCross V a b c d e f) 2 =
    cexp ((- a * I) + (- b * I) + (- d * I) + (- e * I)) * (conj [V]u ⨯₃ conj [V]c) 2
```

**`phaseShiftApply.uRow_mul`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L319).

```lean
lemma uRow_mul (V : CKMMatrix) (a b c : ℝ) :
    [phaseShiftApply V a b c 0 0 0]u = cexp (a * I) • [V]u
```

**`phaseShiftApply.cRow_mul`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L330).

```lean
lemma cRow_mul (V : CKMMatrix) (a b c : ℝ) :
    [phaseShiftApply V a b c 0 0 0]c = cexp (b * I) • [V]c
```

**`phaseShiftApply.tRow_mul`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean#L341).

```lean
lemma tRow_mul (V : CKMMatrix) (a b c : ℝ) :
    [phaseShiftApply V a b c 0 0 0]t = cexp (c * I) • [V]t
```

## Depends on

- [The CKM Matrix](ckmmatrix-basic.md)

## Sources

- [Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/FlavorPhysics/CKMMatrix/Rows.lean)
