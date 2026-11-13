---
declaration: module
origin: cited
lean: MSSMACC.planeY₃B₃, MSSMACC.planeY₃B₃_val, MSSMACC.planeY₃B₃_smul, MSSMACC.planeY₃B₃_eq, MSSMACC.planeY₃B₃_val_eq', MSSMACC.planeY₃B₃_quad, MSSMACC.planeY₃B₃_cubic, MSSMACC.lineQuadAFL
statement: formalized
proof: formalized
---

# Plane Y₃ B₃ and an orthogonal third point

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.OrthogY3B3.PlaneWithY3B3`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean): 25 declarations, 7 with a docstring.

> The plane spanned by Y₃, B₃ and third orthogonal point.

## References

> * https://arxiv.org/pdf/2107.07926.pdf. [ref: Allanach:2021yjy]

**`MSSMACC.planeY₃B₃`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L28).

> The plane of linear solutions spanned by `Y₃`, `B₃` and `R`, a point orthogonal
> to `Y₃` and `B₃`.

```lean
def planeY₃B₃ (R : MSSMACC.AnomalyFreePerp) (a b c : ℚ) : MSSMACC.LinSols
```

**`MSSMACC.planeY₃B₃_val`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L31).

```lean
lemma planeY₃B₃_val (R : MSSMACC.AnomalyFreePerp) (a b c : ℚ) :
    (planeY₃B₃ R a b c).val = a • Y₃.val + b • B₃.val + c • R.val
```

**`MSSMACC.planeY₃B₃_smul`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L35).

```lean
lemma planeY₃B₃_smul (R : MSSMACC.AnomalyFreePerp) (a b c d : ℚ) :
    planeY₃B₃ R (d * a) (d * b) (d * c) = d • planeY₃B₃ R a b c
```

**`MSSMACC.planeY₃B₃_eq`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L43).

```lean
lemma planeY₃B₃_eq (R : MSSMACC.AnomalyFreePerp) (a b c : ℚ) (h : a = a' ∧ b = b' ∧ c = c') :
    (planeY₃B₃ R a b c) = (planeY₃B₃ R a' b' c')
```

**`MSSMACC.planeY₃B₃_val_eq'`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L48).

```lean
lemma planeY₃B₃_val_eq' (R : MSSMACC.AnomalyFreePerp) (a b c : ℚ) (hR' : R.val ≠ 0)
    (h : (planeY₃B₃ R a b c).val = (planeY₃B₃ R a' b' c').val) :
    a = a' ∧ b = b' ∧ c = c'
```

**`MSSMACC.planeY₃B₃_quad`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L66).

```lean
lemma planeY₃B₃_quad (R : MSSMACC.AnomalyFreePerp) (a b c : ℚ) :
    accQuad (planeY₃B₃ R a b c).val = c * (2 * a * quadBiLin Y₃.val R.val
    + 2 * b * quadBiLin B₃.val R.val + c * quadBiLin R.val R.val)
```

**`MSSMACC.planeY₃B₃_cubic`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L81).

```lean
lemma planeY₃B₃_cubic (R : MSSMACC.AnomalyFreePerp) (a b c : ℚ) :
    accCube (planeY₃B₃ R a b c).val = c ^ 2 *
    (3 * a * cubeTriLin R.val R.val Y₃.val
    + 3 * b * cubeTriLin R.val R.val B₃.val + c * cubeTriLin R.val R.val R.val)
```

**`MSSMACC.lineQuadAFL`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L100).

> The line in the plane spanned by `Y₃`, `B₃` and `R` which is in the quadratic,
> as `LinSols`.

```lean
def lineQuadAFL (R : MSSMACC.AnomalyFreePerp) (c1 c2 c3 : ℚ) : MSSMACC.LinSols
```

**`MSSMACC.lineQuadAFL_quad`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L105).

```lean
lemma lineQuadAFL_quad (R : MSSMACC.AnomalyFreePerp) (c1 c2 c3 : ℚ) :
    accQuad (lineQuadAFL R c1 c2 c3).val = 0
```

**`MSSMACC.lineQuad`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L113).

> The line in the plane spanned by `Y₃`, `B₃` and `R` which is in the quadratic.

```lean
def lineQuad (R : MSSMACC.AnomalyFreePerp) (c1 c2 c3 : ℚ) : MSSMACC.QuadSols
```

**`MSSMACC.lineQuad_val`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L116).

```lean
lemma lineQuad_val (R : MSSMACC.AnomalyFreePerp) (c1 c2 c3 : ℚ) :
    (lineQuad R c1 c2 c3).val = (planeY₃B₃ R
    (c2 * quadBiLin R.val R.val - 2 * c3 * quadBiLin B₃.val R.val)
    (2 * c3 * quadBiLin Y₃.val R.val - c1 * quadBiLin R.val R.val)
    (2 * c1 * quadBiLin B₃.val R.val - 2 * c2 * quadBiLin Y₃.val R.val)).val
```

**`MSSMACC.lineQuad_smul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L123).

```lean
lemma lineQuad_smul (R : MSSMACC.AnomalyFreePerp) (a b c d : ℚ) :
    lineQuad R (d * a) (d * b) (d * c) = d • lineQuad R a b c
```

**`MSSMACC.α₁`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L132).

> A helper function to simplify following expressions.

```lean
def α₁ (T : MSSMACC.AnomalyFreePerp) : ℚ
```

**`MSSMACC.α₂`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L137).

> A helper function to simplify following expressions.

```lean
def α₂ (T : MSSMACC.AnomalyFreePerp) : ℚ
```

**`MSSMACC.α₃`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L142).

> A helper function to simplify following expressions.

```lean
def α₃ (T : MSSMACC.AnomalyFreePerp) : ℚ
```

**`MSSMACC.lineQuad_cube`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L146).

```lean
lemma lineQuad_cube (R : MSSMACC.AnomalyFreePerp) (c₁ c₂ c₃ : ℚ) :
    accCube (lineQuad R c₁ c₂ c₃).val =
    - 4 * (c₁ * quadBiLin B₃.val R.val - c₂ * quadBiLin Y₃.val R.val) ^ 2 *
    (α₁ R * c₁ + α₂ R * c₂ + α₃ R * c₃)
```

**`MSSMACC.lineCube`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L155).

> The line in the plane spanned by `Y₃`, `B₃` and `R` which is in the cubic.

```lean
def lineCube (R : MSSMACC.AnomalyFreePerp) (a₁ a₂ a₃ : ℚ) :
    MSSMACC.LinSols
```

**`MSSMACC.lineCube_smul`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L162).

```lean
lemma lineCube_smul (R : MSSMACC.AnomalyFreePerp) (a b c d : ℚ) :
    lineCube R (d * a) (d * b) (d * c) = d • lineCube R a b c
```

**`MSSMACC.lineCube_cube`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L170).

```lean
lemma lineCube_cube (R : MSSMACC.AnomalyFreePerp) (a₁ a₂ a₃ : ℚ) :
    accCube (lineCube R a₁ a₂ a₃).val = 0
```

**`MSSMACC.lineCube_quad`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L175).

```lean
lemma lineCube_quad (R : MSSMACC.AnomalyFreePerp) (a₁ a₂ a₃ : ℚ) :
    accQuad (lineCube R a₁ a₂ a₃).val =
    3 * (a₁ * cubeTriLin R.val R.val B₃.val - a₂ * cubeTriLin R.val R.val Y₃.val) *
    (α₁ R * a₁ + α₂ R * a₂ + α₃ R * a₃)
```

**`MSSMACC.α₃_proj`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L184).

```lean
lemma α₃_proj (T : MSSMACC.Sols) : α₃ (proj T.1.1) =
    6 * dot Y₃.val B₃.val ^ 3 *
    (cubeTriLin T.val T.val Y₃.val * quadBiLin B₃.val T.val -
    cubeTriLin T.val T.val B₃.val * quadBiLin Y₃.val T.val)
```

**`MSSMACC.α₂_proj`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L191).

```lean
lemma α₂_proj (T : MSSMACC.Sols) : α₂ (proj T.1.1) =
    - α₃ (proj T.1.1) * (dot Y₃.val T.val - 2 * dot B₃.val T.val)
```

**`MSSMACC.α₁_proj`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L196).

```lean
lemma α₁_proj (T : MSSMACC.Sols) : α₁ (proj T.1.1) =
    - α₃ (proj T.1.1) * (dot B₃.val T.val - dot Y₃.val T.val)
```

**`MSSMACC.α₁_proj_zero`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L202).

```lean
lemma α₁_proj_zero (T : MSSMACC.Sols) (h1 : α₃ (proj T.1.1) = 0) :
    α₁ (proj T.1.1) = 0
```

**`MSSMACC.α₂_proj_zero`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean#L207).

```lean
lemma α₂_proj_zero (T : MSSMACC.Sols) (h1 : α₃ (proj T.1.1) = 0) :
    α₂ (proj T.1.1) = 0
```

## Depends on

- [The type of solutions perpendicular to `Y₃` and `B₃`](mssmnu-anomalycancellation-orthogy3b3-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/PlaneWithY3B3.lean)
