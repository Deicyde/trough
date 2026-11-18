---
declaration: module
origin: cited
lean: MSSMACC.Y₃AsCharge, MSSMACC.Y₃, MSSMACC.Y₃_val, MSSMACC.doublePoint_Y₃_Y₃
statement: formalized
proof: formalized
---

# The definition of the solution Y₃ and properties thereof

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.Y3`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean): 4 declarations, 2 with a docstring.

> We define $Y_3$ and show that it is a double point of the cubic.

## References

> * The main reference for the material in this file is https://arxiv.org/pdf/2107.07926.pdf.
>   [ref: Allanach:2021yjy]

**`MSSMACC.Y₃AsCharge`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean#L30).

> $Y_3$ is the charge which is hypercharge in all families, but with the third
> family of the opposite sign.

```lean
def Y₃AsCharge : MSSMACC.Charges
```

**`MSSMACC.Y₃`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean#L57).

> $Y_3$ as a solution.

```lean
def Y₃ : MSSMACC.Sols
```

**`MSSMACC.Y₃_val`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean#L62).

```lean
lemma Y₃_val : Y₃.val = Y₃AsCharge
```

**`MSSMACC.doublePoint_Y₃_Y₃`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean#L66).

```lean
lemma doublePoint_Y₃_Y₃ (R : MSSMACC.LinSols) :
    cubeTriLin Y₃.val Y₃.val R.val = 0
```

## Depends on

- [The MSSM with 3 families and RHNs](mssmnu-anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/Y3.lean)
