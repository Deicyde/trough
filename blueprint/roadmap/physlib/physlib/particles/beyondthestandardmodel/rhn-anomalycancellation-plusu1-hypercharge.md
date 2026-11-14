---
declaration: module
origin: cited
lean: SMRHN.PlusU1.Y₁, SMRHN.PlusU1.Y, SMRHN.PlusU1.Y.on_quadBiLin, SMRHN.PlusU1.Y.on_quadBiLin_AFL, SMRHN.PlusU1.Y.add_AFL_quad, SMRHN.PlusU1.Y.add_quad, SMRHN.PlusU1.Y.addQuad, SMRHN.PlusU1.Y.addQuad_zero
statement: formalized
proof: formalized
---

# Hypercharge in SM with RHN.

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.HyperCharge`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean): 16 declarations, 4 with a docstring.

> Relevant definitions for the SM hypercharge.

**`SMRHN.PlusU1.Y₁`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L27).

> The hypercharge for 1 family.

```lean
def Y₁ : (PlusU1 1).Sols
```

**`SMRHN.PlusU1.Y`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L51).

> The hypercharge for `n` family.

```lean
def Y (n : ℕ) : (PlusU1 n).Sols
```

**`SMRHN.PlusU1.Y.on_quadBiLin`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L59).

```lean
lemma on_quadBiLin (S : (PlusU1 n).Charges) :
    quadBiLin (Y n).val S = accYY S
```

**`SMRHN.PlusU1.Y.on_quadBiLin_AFL`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L68).

```lean
lemma on_quadBiLin_AFL (S : (PlusU1 n).LinSols) : quadBiLin (Y n).val S.val = 0
```

**`SMRHN.PlusU1.Y.add_AFL_quad`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L72).

```lean
lemma add_AFL_quad (S : (PlusU1 n).LinSols) (a b : ℚ) :
    accQuad (a • S.val + b • (Y n).val) = a ^ 2 * accQuad S.val
```

**`SMRHN.PlusU1.Y.add_quad`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L80).

```lean
lemma add_quad (S : (PlusU1 n).QuadSols) (a b : ℚ) :
    accQuad (a • S.val + b • (Y n).val) = 0
```

**`SMRHN.PlusU1.Y.addQuad`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L85).

> The `QuadSol` obtained by adding hypercharge to a `QuadSol`.

```lean
def addQuad (S : (PlusU1 n).QuadSols) (a b : ℚ) : (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.Y.addQuad_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L88).

```lean
lemma addQuad_zero (S : (PlusU1 n).QuadSols) (a : ℚ) : addQuad S a 0 = a • S
```

**`SMRHN.PlusU1.Y.on_cubeTriLin`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L92).

```lean
lemma on_cubeTriLin (S : (PlusU1 n).Charges) :
    cubeTriLin (Y n).val (Y n).val S = 6 * accYY S
```

**`SMRHN.PlusU1.Y.on_cubeTriLin_AFL`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L100).

```lean
lemma on_cubeTriLin_AFL (S : (PlusU1 n).LinSols) :
    cubeTriLin (Y n).val (Y n).val S.val = 0
```

**`SMRHN.PlusU1.Y.on_cubeTriLin'`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L106).

```lean
lemma on_cubeTriLin' (S : (PlusU1 n).Charges) :
    cubeTriLin (Y n).val S S = 6 * accQuad S
```

**`SMRHN.PlusU1.Y.on_cubeTriLin'_ALQ`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L114).

```lean
lemma on_cubeTriLin'_ALQ (S : (PlusU1 n).QuadSols) :
    cubeTriLin (Y n).val S.val S.val = 0
```

**`SMRHN.PlusU1.Y.add_AFL_cube`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L120).

```lean
lemma add_AFL_cube (S : (PlusU1 n).LinSols) (a b : ℚ) :
    accCube (a • S.val + b • (Y n).val) =
    a ^ 2 * (a * accCube S.val + 3 * b * cubeTriLin S.val S.val (Y n).val)
```

**`SMRHN.PlusU1.Y.add_AFQ_cube`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L132).

```lean
lemma add_AFQ_cube (S : (PlusU1 n).QuadSols) (a b : ℚ) :
    accCube (a • S.val + b • (Y n).val) = a ^ 3 * accCube S.val
```

**`SMRHN.PlusU1.Y.add_AF_cube`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L137).

```lean
lemma add_AF_cube (S : (PlusU1 n).Sols) (a b : ℚ) :
    accCube (a • S.val + b • (Y n).val) = 0
```

**`SMRHN.PlusU1.Y.addCube`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean#L143).

> The `Sol` obtained by adding hypercharge to a `Sol`.

```lean
def addCube (S : (PlusU1 n).Sols) (a b : ℚ) : (PlusU1 n).Sols
```

## Depends on

- [Family Maps for SM with RHN](rhn-anomalycancellation-plusu1-familymaps.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/HyperCharge.lean)
