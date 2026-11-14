---
declaration: module
origin: cited
lean: SMRHN.SM.PlaneSeven.B₀, SMRHN.SM.PlaneSeven.B₀_cubic, SMRHN.SM.PlaneSeven.B₁, SMRHN.SM.PlaneSeven.B₁_cubic, SMRHN.SM.PlaneSeven.B₂, SMRHN.SM.PlaneSeven.B₂_cubic, SMRHN.SM.PlaneSeven.B₃, SMRHN.SM.PlaneSeven.B₃_cubic
statement: formalized
proof: formalized
---

# Dimension 7 plane

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.Ordinary.DimSevenPlane`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean): 29 declarations, 8 with a docstring.

> We work here in the three family case.
> We give an example of a 7 dimensional plane on which every point satisfies the ACCs.
>
> The main result of this file is `seven_dim_plane_exists` which states that there exists a
> 7 dimensional plane of charges on which every point satisfies the ACCs.

**`SMRHN.SM.PlaneSeven.B₀`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L30).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₀ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₀_cubic`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L37).

```lean
lemma B₀_cubic (S T : (SM 3).Charges) : cubeTriLin B₀ S T =
    6 * (S (0 : Fin 18) * T (0 : Fin 18) - S (1 : Fin 18) * T (1 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B₁`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L44).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₁ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₁_cubic`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L51).

```lean
lemma B₁_cubic (S T : (SM 3).Charges) : cubeTriLin B₁ S T =
    3 * (S (3 : Fin 18) * T (3 : Fin 18) - S (4 : Fin 18) * T (4 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B₂`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L58).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₂ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₂_cubic`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L65).

```lean
lemma B₂_cubic (S T : (SM 3).Charges) : cubeTriLin B₂ S T =
    3 * (S (6 : Fin 18) * T (6 : Fin 18) - S (7 : Fin 18) * T (7 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B₃`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L72).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₃ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₃_cubic`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L79).

```lean
lemma B₃_cubic (S T : (SM 3).Charges) : cubeTriLin B₃ S T =
    2 * (S (9 : Fin 18) * T (9 : Fin 18) - S (10 : Fin 18) * T (10 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B₄`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L86).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₄ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₄_cubic`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L93).

```lean
lemma B₄_cubic (S T : (SM 3).Charges) : cubeTriLin B₄ S T =
    (S (12 : Fin 18) * T (12 : Fin 18) - S (13 : Fin 18) * T (13 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B₅`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L100).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₅ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₅_cubic`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L107).

```lean
lemma B₅_cubic (S T : (SM 3).Charges) : cubeTriLin B₅ S T =
    (S (15 : Fin 18) * T (15 : Fin 18) - S (16 : Fin 18) * T (16 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B₆`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L114).

> A charge assignment forming one of the basis elements of the plane.

```lean
def B₆ : (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₆_cubic`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L121).

```lean
lemma B₆_cubic (S T : (SM 3).Charges) : cubeTriLin B₆ S T =
    3 * (S (5 : Fin 18) * T (5 : Fin 18) - S (8 : Fin 18) * T (8 : Fin 18))
```

**`SMRHN.SM.PlaneSeven.B`**, an abbrev, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L131).

> The charge assignments forming a basis of the plane.

```lean
abbrev B : Fin 7 → (SM 3).Charges
```

**`SMRHN.SM.PlaneSeven.B₀_Bi_cubic`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L141).

```lean
lemma B₀_Bi_cubic {i : Fin 7} (hi : 0 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 0) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.B₁_Bi_cubic`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L148).

```lean
lemma B₁_Bi_cubic {i : Fin 7} (hi : 1 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 1) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.B₂_Bi_cubic`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L155).

```lean
lemma B₂_Bi_cubic {i : Fin 7} (hi : 2 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 2) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.B₃_Bi_cubic`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L162).

```lean
lemma B₃_Bi_cubic {i : Fin 7} (hi : 3 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 3) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.B₄_Bi_cubic`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L169).

```lean
lemma B₄_Bi_cubic {i : Fin 7} (hi : 4 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 4) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.B₅_Bi_cubic`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L176).

```lean
lemma B₅_Bi_cubic {i : Fin 7} (hi : 5 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 5) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.B₆_Bi_cubic`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L183).

```lean
lemma B₆_Bi_cubic {i : Fin 7} (hi : 6 ≠ i) (S : (SM 3).Charges) :
    cubeTriLin (B 6) (B i) S = 0
```

**`SMRHN.SM.PlaneSeven.Bi_Bj_ne_cubic`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L190).

```lean
lemma Bi_Bj_ne_cubic {i j : Fin 7} (h : i ≠ j) (S : (SM 3).Charges) :
    cubeTriLin (B i) (B j) S = 0
```

**`SMRHN.SM.PlaneSeven.Bi_Bi_Bj_cubic`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L202).

```lean
lemma Bi_Bi_Bj_cubic (i j : Fin 7) :
    cubeTriLin (B i) (B i) (B j) = 0
```

**`SMRHN.SM.PlaneSeven.Bi_Bj_Bk_cubic`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L209).

```lean
lemma Bi_Bj_Bk_cubic (i j k : Fin 7) :
    cubeTriLin (B i) (B j) (B k) = 0
```

**`SMRHN.SM.PlaneSeven.B_in_accCube`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L216).

```lean
lemma B_in_accCube (f : Fin 7 → ℚ) : accCube (∑ i, f i • B i) = 0
```

**`SMRHN.SM.PlaneSeven.B_sum_is_sol`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L224).

```lean
lemma B_sum_is_sol (f : Fin 7 → ℚ) : (SM 3).IsSolution (∑ i, f i • B i)
```

**`SMRHN.SM.PlaneSeven.basis_linear_independent`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L240).

```lean
lemma basis_linear_independent : LinearIndependent ℚ B
```

**`SMRHN.SM.seven_dim_plane_exists`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean#L260).

```lean
lemma seven_dim_plane_exists : ∃ (B : Fin 7 → (SM 3).Charges),
    LinearIndependent ℚ B ∧ ∀ (f : Fin 7 → ℚ), (SM 3).IsSolution (∑ i, f i • B i)
```

## Depends on

- [ACC system for SM with RHN (without hypercharge).](rhn-anomalycancellation-ordinary-basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/DimSevenPlane.lean)
