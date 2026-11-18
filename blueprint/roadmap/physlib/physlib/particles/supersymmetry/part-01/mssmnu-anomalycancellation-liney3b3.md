---
declaration: module
origin: cited
lean: MSSMACC.lineY₃B₃Charges, MSSMACC.lineY₃B₃Charges_val, MSSMACC.lineY₃B₃Charges_quad, MSSMACC.lineY₃B₃Charges_cubic, MSSMACC.lineY₃B₃, MSSMACC.lineY₃B₃_val, MSSMACC.doublePoint_Y₃_B₃, MSSMACC.lineY₃B₃_doublePoint
statement: formalized
proof: formalized
---

# The line through B₃ and Y₃

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.LineY3B3`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean): 8 declarations, 2 with a docstring.

> We give properties of lines through `B₃` and `Y₃`. We show that every point on this line
> is a solution to the quadratic `lineY₃B₃Charges_quad` and a double point of the cubic
> `lineY₃B₃_doublePoint`.

## References

> * The main reference for the material in this file. [ref: Allanach:2021yjy]

**`MSSMACC.lineY₃B₃Charges`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L30).

> The line through $Y_3$ and $B_3$ as `LinSols`.

```lean
def lineY₃B₃Charges (a b : ℚ) : MSSMACC.LinSols
```

**`MSSMACC.lineY₃B₃Charges_val`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L32).

```lean
lemma lineY₃B₃Charges_val (a b : ℚ) :
    (lineY₃B₃Charges a b).val = a • Y₃.1.1.val + b • B₃.1.1.val
```

**`MSSMACC.lineY₃B₃Charges_quad`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L36).

```lean
lemma lineY₃B₃Charges_quad (a b : ℚ) : accQuad (lineY₃B₃Charges a b).val = 0
```

**`MSSMACC.lineY₃B₃Charges_cubic`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L44).

```lean
lemma lineY₃B₃Charges_cubic (a b : ℚ) : accCube (lineY₃B₃Charges a b).val = 0
```

**`MSSMACC.lineY₃B₃`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L54).

> The line through $Y_3$ and $B_3$ as `Sols`.

```lean
def lineY₃B₃ (a b : ℚ) : MSSMACC.Sols
```

**`MSSMACC.lineY₃B₃_val`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L57).

```lean
lemma lineY₃B₃_val (a b : ℚ) : (lineY₃B₃ a b).val = a • Y₃.val + b • B₃.val
```

**`MSSMACC.doublePoint_Y₃_B₃`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L61).

```lean
lemma doublePoint_Y₃_B₃ (R : MSSMACC.LinSols) :
    cubeTriLin Y₃.val B₃.val R.val = 0
```

**`MSSMACC.lineY₃B₃_doublePoint`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean#L81).

```lean
lemma lineY₃B₃_doublePoint (R : MSSMACC.LinSols) (a b : ℚ) :
    cubeTriLin (lineY₃B₃ a b).val (lineY₃B₃ a b).val R.val = 0
```

## Depends on

- [The definition of the solution B₃ and properties thereof](mssmnu-anomalycancellation-b3.md)
- [The definition of the solution Y₃ and properties thereof](mssmnu-anomalycancellation-y3.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/LineY3B3.lean)
