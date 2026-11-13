---
declaration: module
origin: cited
lean: SMRHN.PlusU1.BL₁, SMRHN.PlusU1.BL, SMRHN.PlusU1.BL.on_quadBiLin, SMRHN.PlusU1.BL.on_quadBiLin_AFL, SMRHN.PlusU1.BL.add_AFL_quad, SMRHN.PlusU1.BL.add_quad, SMRHN.PlusU1.BL.addQuad, SMRHN.PlusU1.BL.addQuad_zero
statement: formalized
proof: formalized
---

# B Minus L in SM with RHN.

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.BMinusL`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean): 11 declarations, 3 with a docstring.

> Relevant definitions for the SM `B-L`.

**`SMRHN.PlusU1.BL₁`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L29).

> $B - L$ in the 1-family case.

```lean
def BL₁ : (PlusU1 1).Sols
```

**`SMRHN.PlusU1.BL`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L53).

> $B - L$ in the $n$-family case.

```lean
def BL (n : ℕ) : (PlusU1 n).Sols
```

**`SMRHN.PlusU1.BL.on_quadBiLin`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L61).

```lean
lemma on_quadBiLin (S : (PlusU1 n).Charges) :
    quadBiLin (BL n).val S = 1/2 * accYY S + 3/2 * accSU2 S - 2 * accSU3 S
```

**`SMRHN.PlusU1.BL.on_quadBiLin_AFL`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L69).

```lean
lemma on_quadBiLin_AFL (S : (PlusU1 n).LinSols) : quadBiLin (BL n).val S.val = 0
```

**`SMRHN.PlusU1.BL.add_AFL_quad`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L74).

```lean
lemma add_AFL_quad (S : (PlusU1 n).LinSols) (a b : ℚ) :
    accQuad (a • S.val + b • (BL n).val) = a ^ 2 * accQuad S.val
```

**`SMRHN.PlusU1.BL.add_quad`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L82).

```lean
lemma add_quad (S : (PlusU1 n).QuadSols) (a b : ℚ) :
    accQuad (a • S.val + b • (BL n).val) = 0
```

**`SMRHN.PlusU1.BL.addQuad`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L88).

> The `QuadSol` obtained by adding $B-L$ to a `QuadSol`.

```lean
def addQuad (S : (PlusU1 n).QuadSols) (a b : ℚ) : (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.BL.addQuad_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L91).

```lean
lemma addQuad_zero (S : (PlusU1 n).QuadSols) (a : ℚ) : addQuad S a 0 = a • S
```

**`SMRHN.PlusU1.BL.on_cubeTriLin`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L96).

```lean
lemma on_cubeTriLin (S : (PlusU1 n).Charges) :
    cubeTriLin (BL n).val (BL n).val S = 9 * accGrav S - 24 * accSU3 S
```

**`SMRHN.PlusU1.BL.on_cubeTriLin_AFL`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L104).

```lean
lemma on_cubeTriLin_AFL (S : (PlusU1 n).LinSols) :
    cubeTriLin (BL n).val (BL n).val S.val = 0
```

**`SMRHN.PlusU1.BL.add_AFL_cube`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean#L110).

```lean
lemma add_AFL_cube (S : (PlusU1 n).LinSols) (a b : ℚ) :
    accCube (a • S.val + b • (BL n).val) =
    a ^ 2 * (a * accCube S.val + 3 * b * cubeTriLin S.val S.val (BL n).val)
```

## Depends on

- [Family Maps for SM with RHN](rhn-anomalycancellation-plusu1-familymaps.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BMinusL.lean)
