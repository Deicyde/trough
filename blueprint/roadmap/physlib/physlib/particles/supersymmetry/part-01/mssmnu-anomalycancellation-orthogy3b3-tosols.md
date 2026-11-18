---
declaration: module
origin: cited
lean: MSSMACC.AnomalyFreePerp.LineEqProp, MSSMACC.AnomalyFreePerp.LineEqPropSol, MSSMACC.AnomalyFreePerp.lineEqCoeff, MSSMACC.AnomalyFreePerp.lineEqPropSol_iff_lineEqCoeff_zero, MSSMACC.AnomalyFreePerp.linEqPropSol_iff_proj_linEqProp, MSSMACC.AnomalyFreePerp.InQuadProp, MSSMACC.AnomalyFreePerp.InQuadSolProp, MSSMACC.AnomalyFreePerp.quadCoeff
statement: formalized
proof: formalized
---

# From charges perpendicular to `Y₃` and `B₃` to solutions

The module `Physlib.Particles.SuperSymmetry.MSSMNu.AnomalyCancellation.OrthogY3B3.ToSols`, [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean): 49 declarations (3 instances with no name), 30 with a docstring.

> The main aim of this file is to take charge assignments perpendicular to `Y₃` and `B₃` and
> produce solutions to the anomaly cancellation conditions. In this regard we will define
> a surjective map `toSol` from `MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ` to `MSSMACC.Sols`.
>
> To define `toSols` we define a series of other maps from various subtypes of
> `MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ` to `MSSMACC.Sols`. And show that these maps form a
> surjection on certain subtypes of `MSSMACC.Sols`.

## References

> * The main reference for the material in this file is https://arxiv.org/pdf/2107.07926.pdf.
>   [ref: Allanach:2021yjy]

**`MSSMACC.AnomalyFreePerp.LineEqProp`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L37).

> A condition for the quad line in the plane spanned by R, Y₃ and B₃ to sit in the cubic,
> and for the cube line to sit in the quad.

```lean
def LineEqProp (R : MSSMACC.AnomalyFreePerp) : Prop
```

**An instance with no name**, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L40).

> The proposition `LineEqProp` is decidable.

```lean
instance (R : MSSMACC.AnomalyFreePerp) : Decidable (LineEqProp R)
```

**`MSSMACC.AnomalyFreePerp.LineEqPropSol`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L44).

> A condition on `Sols` which we will show in `linEqPropSol_iff_proj_linEqProp` that is equivalent
> to the condition that the `proj` of the solution satisfies `lineEqProp`.

```lean
def LineEqPropSol (R : MSSMACC.Sols) : Prop
```

**`MSSMACC.AnomalyFreePerp.lineEqCoeff`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L50).

> A rational which appears in `toSolNS` acting on sols, and which being zero is
> equivalent to satisfying `lineEqPropSol`.

```lean
def lineEqCoeff (T : MSSMACC.Sols) : ℚ
```

**`MSSMACC.AnomalyFreePerp.lineEqPropSol_iff_lineEqCoeff_zero`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L52).

```lean
lemma lineEqPropSol_iff_lineEqCoeff_zero (T : MSSMACC.Sols) :
    LineEqPropSol T ↔ lineEqCoeff T = 0
```

**`MSSMACC.AnomalyFreePerp.linEqPropSol_iff_proj_linEqProp`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L63).

```lean
lemma linEqPropSol_iff_proj_linEqProp (R : MSSMACC.Sols) :
    LineEqPropSol R ↔ LineEqProp (proj R.1.1)
```

**`MSSMACC.AnomalyFreePerp.InQuadProp`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L76).

> A condition which is satisfied if the plane spanned by `R`, `Y₃` and `B₃` lies
> entirely in the quadratic surface.

```lean
def InQuadProp (R : MSSMACC.AnomalyFreePerp) : Prop
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L80).

> The proposition `InQuadProp` is decidable.

```lean
instance (R : MSSMACC.AnomalyFreePerp) : Decidable (InQuadProp R)
```

**`MSSMACC.AnomalyFreePerp.InQuadSolProp`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L84).

> A condition which is satisfied if the plane spanned by the solutions `R`, `Y₃` and `B₃`
> lies entirely in the quadratic surface.

```lean
def InQuadSolProp (R : MSSMACC.Sols) : Prop
```

**`MSSMACC.AnomalyFreePerp.quadCoeff`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L89).

> A rational which has two properties. It is zero for a solution `T` if and only if
> that solution satisfies `inQuadSolProp`. It appears in the definition of `inQuadProj`.

```lean
def quadCoeff (T : MSSMACC.Sols) : ℚ
```

**`MSSMACC.AnomalyFreePerp.inQuadSolProp_iff_quadCoeff_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L93).

```lean
lemma inQuadSolProp_iff_quadCoeff_zero (T : MSSMACC.Sols) : InQuadSolProp T ↔ quadCoeff T = 0
```

**`MSSMACC.AnomalyFreePerp.inQuadSolProp_iff_proj_inQuadProp`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L107).

> The conditions `inQuadSolProp R` and `inQuadProp (proj R.1.1)` are equivalent. This is to be
> expected since both `R` and `proj R.1.1` define the same plane with `Y₃` and `B₃`.

```lean
lemma inQuadSolProp_iff_proj_inQuadProp (R : MSSMACC.Sols) :
    InQuadSolProp R ↔ InQuadProp (proj R.1.1)
```

**`MSSMACC.AnomalyFreePerp.InCubeProp`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L120).

> A condition which is satisfied if the plane spanned by `R`, `Y₃` and `B₃` lies
> entirely in the cubic surface.

```lean
def InCubeProp (R : MSSMACC.AnomalyFreePerp) : Prop
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L125).

> The proposition `InCubeProp` is decidable.

```lean
instance (R : MSSMACC.AnomalyFreePerp) : Decidable (InCubeProp R)
```

**`MSSMACC.AnomalyFreePerp.InCubeSolProp`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L129).

> A condition which is satisfied if the plane spanned by the solutions `R`, `Y₃` and `B₃`
> lies entirely in the cubic surface.

```lean
def InCubeSolProp (R : MSSMACC.Sols) : Prop
```

**`MSSMACC.AnomalyFreePerp.cubicCoeff`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L134).

> A rational which has two properties. It is zero for a solution `T` if and only if
> that solution satisfies `inCubeSolProp`. It appears in the definition of `inLineEqProj`.

```lean
def cubicCoeff (T : MSSMACC.Sols) : ℚ
```

**`MSSMACC.AnomalyFreePerp.inCubeSolProp_iff_cubicCoeff_zero`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L138).

```lean
lemma inCubeSolProp_iff_cubicCoeff_zero (T : MSSMACC.Sols) :
    InCubeSolProp T ↔ cubicCoeff T = 0
```

**`MSSMACC.AnomalyFreePerp.inCubeSolProp_iff_proj_inCubeProp`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L151).

```lean
lemma inCubeSolProp_iff_proj_inCubeProp (R : MSSMACC.Sols) :
    InCubeSolProp R ↔ InCubeProp (proj R.1.1)
```

**`MSSMACC.AnomalyFreePerp.InLineEq`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L166).

> Those charge assignments perpendicular to `Y₃` and `B₃` which satisfy the condition
> `lineEqProp`.

```lean
def InLineEq : Type
```

**`MSSMACC.AnomalyFreePerp.InQuad`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L170).

> Those charge assignments perpendicular to `Y₃` and `B₃` which satisfy the conditions
> `lineEqProp` and `inQuadProp`.

```lean
def InQuad : Type
```

**`MSSMACC.AnomalyFreePerp.InQuadCube`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L174).

> Those charge assignments perpendicular to `Y₃` and `B₃` which satisfy the conditions
> `lineEqProp`, `inQuadProp` and `inCubeProp`.

```lean
def InQuadCube : Type
```

**`MSSMACC.AnomalyFreePerp.NotInLineEqSol`**, a def, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L177).

> Those solutions which do not satisfy the condition `lineEqPropSol`.

```lean
def NotInLineEqSol : Type
```

**`MSSMACC.AnomalyFreePerp.InLineEqSol`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L180).

> Those solutions which satisfy the condition `lineEqPropSol` but not `inQuadSolProp`.

```lean
def InLineEqSol : Type
```

**`MSSMACC.AnomalyFreePerp.InQuadSol`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L184).

> Those solutions which satisfy the condition `lineEqPropSol` and `inQuadSolProp` but
> not `inCubeSolProp`.

```lean
def InQuadSol : Type
```

**`MSSMACC.AnomalyFreePerp.InQuadCubeSol`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L188).

> Those solutions which satisfy the conditions `lineEqPropSol`, `inQuadSolProp`
> and `inCubeSolProp`.

```lean
def InQuadCubeSol : Type
```

**`MSSMACC.AnomalyFreePerp.toSolNSQuad`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L192).

> Given an `R` perpendicular to `Y₃` and `B₃` a quadratic solution.

```lean
def toSolNSQuad (R : MSSMACC.AnomalyFreePerp) : MSSMACC.QuadSols
```

**`MSSMACC.AnomalyFreePerp.toSolNSQuad_cube`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L198).

```lean
lemma toSolNSQuad_cube (R : MSSMACC.AnomalyFreePerp) :
    accCube (toSolNSQuad R).val = 0
```

**`MSSMACC.AnomalyFreePerp.toSolNSQuad_eq_planeY₃B₃_on_α`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L205).

```lean
lemma toSolNSQuad_eq_planeY₃B₃_on_α (R : MSSMACC.AnomalyFreePerp) :
    (toSolNSQuad R).1 = planeY₃B₃ R (α₁ R) (α₂ R) (α₃ R)
```

**`MSSMACC.AnomalyFreePerp.toSolNS`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L215).

> Given an `R` perpendicular to `Y₃` and `B₃`, an element of `Sols`. This map is
> not surjective.

```lean
def toSolNS : MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ → MSSMACC.Sols
```

**`MSSMACC.AnomalyFreePerp.toSolNSProj`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L220).

> A map from `Sols` to `MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ` which on elements of
> `notInLineEqSol` will produce a right inverse to `toSolNS`.

```lean
def toSolNSProj (T : MSSMACC.Sols) : MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ
```

**`MSSMACC.AnomalyFreePerp.toSolNS_proj`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L223).

```lean
lemma toSolNS_proj (T : NotInLineEqSol) : toSolNS (toSolNSProj T.val) = T.val
```

**`MSSMACC.AnomalyFreePerp.inLineEqToSol`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L242).

> A solution to the ACCs, given an element of `inLineEq × ℚ × ℚ × ℚ`.

```lean
def inLineEqToSol : InLineEq × ℚ × ℚ × ℚ → MSSMACC.Sols
```

**`MSSMACC.AnomalyFreePerp.inLineEqProj`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L250).

> On elements of `inLineEqSol` a right-inverse to `inLineEqSol`.

```lean
def inLineEqProj (T : InLineEqSol) : InLineEq × ℚ × ℚ × ℚ
```

**`MSSMACC.AnomalyFreePerp.inLineEqTo_smul`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L258).

```lean
lemma inLineEqTo_smul (R : InLineEq) (c₁ c₂ c₃ d : ℚ) :
    inLineEqToSol (R, (d * c₁), (d * c₂), (d * c₃)) = d • inLineEqToSol (R, c₁, c₂, c₃)
```

**`MSSMACC.AnomalyFreePerp.inLineEqToSol_proj`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L266).

```lean
lemma inLineEqToSol_proj (T : InLineEqSol) : inLineEqToSol (inLineEqProj T) = T.val
```

**`MSSMACC.AnomalyFreePerp.inQuadToSol`**, a def, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L286).

> Given an element of `inQuad × ℚ × ℚ × ℚ`, a solution to the ACCs.

```lean
def inQuadToSol : InQuad × ℚ × ℚ × ℚ → MSSMACC.Sols
```

**`MSSMACC.AnomalyFreePerp.inQuadToSol_smul`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L291).

```lean
lemma inQuadToSol_smul (R : InQuad) (c₁ c₂ c₃ d : ℚ) :
    inQuadToSol (R, (d * c₁), (d * c₂), (d * c₃)) = d • inQuadToSol (R, c₁, c₂, c₃)
```

**`MSSMACC.AnomalyFreePerp.inQuadProj`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L299).

> On elements of `inQuadSol` a right-inverse to `inQuadToSol`.

```lean
def inQuadProj (T : InQuadSol) : InQuad × ℚ × ℚ × ℚ
```

**`MSSMACC.AnomalyFreePerp.inQuadToSol_proj`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L310).

```lean
lemma inQuadToSol_proj (T : InQuadSol) : inQuadToSol (inQuadProj T) = T.val
```

**`MSSMACC.AnomalyFreePerp.inQuadCubeToSol`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L327).

> Given a element of `inQuadCube × ℚ × ℚ × ℚ`, a solution to the ACCs.

```lean
def inQuadCubeToSol : InQuadCube × ℚ × ℚ × ℚ → MSSMACC.Sols
```

**`MSSMACC.AnomalyFreePerp.inQuadCubeToSol_smul`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L332).

```lean
lemma inQuadCubeToSol_smul (R : InQuadCube) (c₁ c₂ c₃ d : ℚ) :
    inQuadCubeToSol (R, (d * c₁), (d * c₂), (d * c₃)) = d • inQuadCubeToSol (R, c₁, c₂, c₃)
```

**`MSSMACC.AnomalyFreePerp.inQuadCubeProj`**, a def, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L340).

> On elements of `inQuadCubeSol` a right-inverse to `inQuadCubeToSol`.

```lean
def inQuadCubeProj (T : InQuadCubeSol) : InQuadCube × ℚ × ℚ × ℚ
```

**`MSSMACC.AnomalyFreePerp.inQuadCubeToSol_proj`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L349).

```lean
lemma inQuadCubeToSol_proj (T : InQuadCubeSol) :
    inQuadCubeToSol (inQuadCubeProj T) = T.val
```

**`MSSMACC.AnomalyFreePerp.toSol`**, a def, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L364).

> A solution from an element of `MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ`. We will
> show that this map is a surjection.

```lean
def toSol : MSSMACC.AnomalyFreePerp × ℚ × ℚ × ℚ → MSSMACC.Sols
```

**`MSSMACC.AnomalyFreePerp.toSol_toSolNSProj`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L376).

```lean
lemma toSol_toSolNSProj (T : NotInLineEqSol) :
    ∃ X, toSol X = T.val
```

**`MSSMACC.AnomalyFreePerp.toSol_inLineEq`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L384).

```lean
lemma toSol_inLineEq (T : InLineEqSol) : ∃ X, toSol X = T.val
```

**`MSSMACC.AnomalyFreePerp.toSol_inQuad`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L392).

```lean
lemma toSol_inQuad (T : InQuadSol) : ∃ X, toSol X = T.val
```

**`MSSMACC.AnomalyFreePerp.toSol_inQuadCube`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L401).

```lean
lemma toSol_inQuadCube (T : InQuadCubeSol) : ∃ X, toSol X = T.val
```

**`MSSMACC.AnomalyFreePerp.toSol_surjective`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean#L410).

```lean
lemma toSol_surjective : Function.Surjective toSol
```

## Depends on

- [Plane Y₃ B₃ and an orthogonal third point](mssmnu-anomalycancellation-orthogy3b3-planewithy.md)

## Sources

- [Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/SuperSymmetry/MSSMNu/AnomalyCancellation/OrthogY3B3/ToSols.lean)
