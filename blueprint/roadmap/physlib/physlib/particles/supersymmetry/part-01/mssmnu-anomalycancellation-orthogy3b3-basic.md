---
declaration: module
origin: cited
lean: MSSMACC.AnomalyFreePerp, MSSMACC.proj, MSSMACC.proj_val, MSSMACC.Y₃_plus_B₃_plus_proj, MSSMACC.quad_Y₃_proj, MSSMACC.quad_B₃_proj, MSSMACC.quad_self_proj, MSSMACC.quad_proj
statement: formalized
proof: formalized
---

# The type of solutions perpendicular to `Y₃` and `B₃`

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.OrthogY3B3.Basic`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean): 12 declarations, 2 with a docstring.

> We define the type of solutions which are orthogonal to `Y₃` and `B₃` and prove some basic lemmas
> about them.

## References

> * The main reference for the material in this file is https://arxiv.org/pdf/2107.07926.pdf.
>   [ref: Allanach:2021yjy]

**`MSSMACC.AnomalyFreePerp`**, a structure, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L29).

> The type of linear solutions orthogonal to $Y_3$ and $B_3$.

```lean
structure AnomalyFreePerp extends MSSMACC.LinSols where
  perpY₃ : dot Y₃.val val = 0
  perpB₃ : dot B₃.val val = 0
```

**`MSSMACC.proj`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L36).

> The projection of an object in `MSSMACC.AnomalyFreeLinear` onto the subspace
> orthogonal to `Y₃` and`B₃`.

```lean
def proj (T : MSSMACC.LinSols) : MSSMACC.AnomalyFreePerp
```

**`MSSMACC.proj_val`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L56).

```lean
lemma proj_val (T : MSSMACC.LinSols) :
    (proj T).val = (dot B₃.val T.val - dot Y₃.val T.val) • Y₃.val +
    (dot Y₃.val T.val - 2 * dot B₃.val T.val) • B₃.val +
    dot Y₃.val B₃.val • T.val
```

**`MSSMACC.Y₃_plus_B₃_plus_proj`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L62).

```lean
lemma Y₃_plus_B₃_plus_proj (T : MSSMACC.LinSols) (a b c : ℚ) :
    a • Y₃.val + b • B₃.val + c • (proj T).val =
    (a + c * (dot B₃.val T.val - dot Y₃.val T.val)) • Y₃.val
    + (b + c * (dot Y₃.val T.val - 2 * dot B₃.val T.val)) • B₃.val
    + (dot Y₃.val B₃.val * c) • T.val
```

**`MSSMACC.quad_Y₃_proj`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L72).

```lean
lemma quad_Y₃_proj (T : MSSMACC.LinSols) :
    quadBiLin Y₃.val (proj T).val = dot Y₃.val B₃.val * quadBiLin Y₃.val T.val
```

**`MSSMACC.quad_B₃_proj`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L82).

```lean
lemma quad_B₃_proj (T : MSSMACC.LinSols) :
    quadBiLin B₃.val (proj T).val = dot Y₃.val B₃.val * quadBiLin B₃.val T.val
```

**`MSSMACC.quad_self_proj`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L92).

```lean
lemma quad_self_proj (T : MSSMACC.Sols) :
    quadBiLin T.val (proj T.1.1).val =
    (dot B₃.val T.val - dot Y₃.val T.val) * quadBiLin Y₃.val T.val +
    (dot Y₃.val T.val - 2 * dot B₃.val T.val) * quadBiLin B₃.val T.val
```

**`MSSMACC.quad_proj`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L106).

```lean
lemma quad_proj (T : MSSMACC.Sols) :
    quadBiLin (proj T.1.1).val (proj T.1.1).val = 2 * dot Y₃.val B₃.val *
    ((dot B₃.val T.val - dot Y₃.val T.val) * quadBiLin Y₃.val T.val +
    (dot Y₃.val T.val - 2 * dot B₃.val T.val) * quadBiLin B₃.val T.val)
```

**`MSSMACC.cube_proj_proj_Y₃`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L117).

```lean
lemma cube_proj_proj_Y₃ (T : MSSMACC.LinSols) :
    cubeTriLin (proj T).val (proj T).val Y₃.val =
    (dot Y₃.val B₃.val)^2 * cubeTriLin T.val T.val Y₃.val
```

**`MSSMACC.cube_proj_proj_B₃`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L143).

```lean
lemma cube_proj_proj_B₃ (T : MSSMACC.LinSols) :
    cubeTriLin (proj T).val (proj T).val B₃.val =
    (dot Y₃.val B₃.val)^2 * cubeTriLin T.val T.val B₃.val
```

**`MSSMACC.cube_proj_proj_self`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L160).

```lean
lemma cube_proj_proj_self (T : MSSMACC.Sols) :
    cubeTriLin (proj T.1.1).val (proj T.1.1).val T.val =
    2 * dot Y₃.val B₃.val *
    ((dot B₃.val T.val - dot Y₃.val T.val) * cubeTriLin T.val T.val Y₃.val +
    (dot Y₃.val T.val - 2 * dot B₃.val T.val) * cubeTriLin T.val T.val B₃.val)
```

**`MSSMACC.cube_proj`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean#L180).

```lean
lemma cube_proj (T : MSSMACC.Sols) :
    cubeTriLin (proj T.1.1).val (proj T.1.1).val (proj T.1.1).val =
    3 * dot Y₃.val B₃.val ^ 2 *
    ((dot B₃.val T.val - dot Y₃.val T.val) * cubeTriLin T.val T.val Y₃.val +
        (dot Y₃.val T.val - 2 * dot B₃.val T.val) * cubeTriLin T.val T.val B₃.val)
```

## Depends on

- [The definition of the solution B₃ and properties thereof](mssmnu-anomalycancellation-b3.md)
- [The definition of the solution Y₃ and properties thereof](mssmnu-anomalycancellation-y3.md)

## Proof depends on

- [The line through B₃ and Y₃](mssmnu-anomalycancellation-liney3b3.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/Basic.lean)
