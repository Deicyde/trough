---
declaration: module
origin: cited
lean: MSSMACC.B₃AsCharge, MSSMACC.B₃, MSSMACC.B₃_val, MSSMACC.doublePoint_B₃_B₃
statement: formalized
proof: formalized
---

# The definition of the solution B₃ and properties thereof

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.B3`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean): 4 declarations, 2 with a docstring.

> We define `B₃` and show that it is a double point of the cubic.

## References

> * The main reference for the material in this file. [ref: Allanach:2021yjy]

**`MSSMACC.B₃AsCharge`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean#L29).

> `B₃` is the charge which is $B-L$ in all families, but with the third
> family of the opposite sign.

```lean
def B₃AsCharge : MSSMACC.Charges
```

**`MSSMACC.B₃`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean#L56).

> `B₃` as a solution.

```lean
def B₃ : MSSMACC.Sols
```

**`MSSMACC.B₃_val`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean#L61).

```lean
lemma B₃_val : B₃.val = B₃AsCharge
```

**`MSSMACC.doublePoint_B₃_B₃`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean#L65).

```lean
lemma doublePoint_B₃_B₃ (R : MSSMACC.LinSols) : cubeTriLin B₃.val B₃.val R.val = 0
```

## Depends on

- [The MSSM with 3 families and RHNs](mssmnu-anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/B3.lean)
