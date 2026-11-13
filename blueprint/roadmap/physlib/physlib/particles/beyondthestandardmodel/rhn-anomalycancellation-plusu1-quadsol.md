---
declaration: module
origin: cited
lean: SMRHN.PlusU1.QuadSol.add_AFL_quad, SMRHN.PlusU1.QuadSol.α₁, SMRHN.PlusU1.QuadSol.α₂, SMRHN.PlusU1.QuadSol.α₂_AFQ, SMRHN.PlusU1.QuadSol.accQuad_α₁_α₂, SMRHN.PlusU1.QuadSol.accQuad_α₁_α₂_zero, SMRHN.PlusU1.QuadSol.genericToQuad, SMRHN.PlusU1.QuadSol.genericToQuad_on_quad
statement: formalized
proof: formalized
---

# Properties of Quad Sols for SM with RHN

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.QuadSol`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean): 19 declarations, 6 with a docstring.

> We give a series of properties held by solutions to the quadratic equation.
>
> In particular given a quad solution we define a map from linear solutions to quadratic solutions
> and show that it is a surjection.

## References

> * The main reference for this is https://arxiv.org/abs/2006.03588. [ref: arxiv\_2006\_03588]

**`SMRHN.PlusU1.QuadSol.add_AFL_quad`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L37).

```lean
lemma add_AFL_quad (S : (PlusU1 n).LinSols) (a b : ℚ) :
    accQuad (a • S.val + b • C.val) =
    a * (a * accQuad S.val + 2 * b * quadBiLin S.val C.val)
```

**`SMRHN.PlusU1.QuadSol.α₁`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L47).

> A helper function for what comes later.

```lean
def α₁ (S : (PlusU1 n).LinSols) : ℚ
```

**`SMRHN.PlusU1.QuadSol.α₂`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L50).

> A helper function for what comes later.

```lean
def α₂ (S : (PlusU1 n).LinSols) : ℚ
```

**`SMRHN.PlusU1.QuadSol.α₂_AFQ`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L52).

```lean
lemma α₂_AFQ (S : (PlusU1 n).QuadSols) : α₂ S.1 = 0
```

**`SMRHN.PlusU1.QuadSol.accQuad_α₁_α₂`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L54).

```lean
lemma accQuad_α₁_α₂ (S : (PlusU1 n).LinSols) :
    accQuad ((α₁ C S) • S + α₂ S • C.1).val = 0
```

**`SMRHN.PlusU1.QuadSol.accQuad_α₁_α₂_zero`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L60).

```lean
lemma accQuad_α₁_α₂_zero (S : (PlusU1 n).LinSols) (h1 : α₁ C S = 0)
    (h2 : α₂ S = 0) (a b : ℚ) : accQuad (a • S + b • C.1).val = 0
```

**`SMRHN.PlusU1.QuadSol.genericToQuad`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L68).

> The construction of a `QuadSol` from a `LinSols` in the generic case.

```lean
def genericToQuad (S : (PlusU1 n).LinSols) :
    (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.QuadSol.genericToQuad_on_quad`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L72).

```lean
lemma genericToQuad_on_quad (S : (PlusU1 n).QuadSols) :
    genericToQuad C S.1 = (α₁ C S.1) • S
```

**`SMRHN.PlusU1.QuadSol.genericToQuad_ne_zero`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L78).

```lean
lemma genericToQuad_ne_zero (S : (PlusU1 n).QuadSols) (h : α₁ C S.1 ≠ 0) :
    (α₁ C S.1)⁻¹ • genericToQuad C S.1 = S
```

**`SMRHN.PlusU1.QuadSol.specialToQuad`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L84).

> The construction of a `QuadSol` from a `LinSols` in the special case when `α₁ C S = 0` and
> `α₂ S = 0`.

```lean
def specialToQuad (S : (PlusU1 n).LinSols) (a b : ℚ) (h1 : α₁ C S = 0)
    (h2 : α₂ S = 0) : (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.QuadSol.special_on_quad`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L88).

```lean
lemma special_on_quad (S : (PlusU1 n).QuadSols) (h1 : α₁ C S.1 = 0) :
    specialToQuad C S.1 1 0 h1 (α₂_AFQ S) = S
```

**`SMRHN.PlusU1.QuadSol.toQuad`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L96).

> The construction of a `QuadSols` from a `LinSols` and two rationals taking account of the
> generic and special cases. This function is a surjection.

```lean
def toQuad : (PlusU1 n).LinSols × ℚ × ℚ → (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.QuadSol.toQuadInv`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L104).

> A function from `QuadSols` to `LinSols × ℚ × ℚ` which is a right inverse to `toQuad`.

```lean
def toQuadInv : (PlusU1 n).QuadSols → (PlusU1 n).LinSols × ℚ × ℚ
```

**`SMRHN.PlusU1.QuadSol.toQuadInv_fst`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L110).

```lean
lemma toQuadInv_fst (S : (PlusU1 n).QuadSols) :
    (toQuadInv C S).1 = S.1
```

**`SMRHN.PlusU1.QuadSol.toQuadInv_α₁_α₂`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L115).

```lean
lemma toQuadInv_α₁_α₂ (S : (PlusU1 n).QuadSols) :
    α₁ C S.1 = 0 ↔ α₁ C (toQuadInv C S).1 = 0 ∧ α₂ (toQuadInv C S).1 = 0
```

**`SMRHN.PlusU1.QuadSol.toQuadInv_special`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L120).

```lean
lemma toQuadInv_special (S : (PlusU1 n).QuadSols) (h : α₁ C S.1 = 0) :
    specialToQuad C (toQuadInv C S).1 (toQuadInv C S).2.1 (toQuadInv C S).2.2
    ((toQuadInv_α₁_α₂ C S).mp h).1 ((toQuadInv_α₁_α₂ C S).mp h).2 = S
```

**`SMRHN.PlusU1.QuadSol.toQuadInv_generic`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L127).

```lean
lemma toQuadInv_generic (S : (PlusU1 n).QuadSols) (h : α₁ C S.1 ≠ 0) :
    (toQuadInv C S).2.1 • genericToQuad C (toQuadInv C S).1 = S
```

**`SMRHN.PlusU1.QuadSol.toQuad_rightInverse`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L133).

```lean
lemma toQuad_rightInverse : Function.RightInverse (@toQuadInv n C) (toQuad C)
```

**`SMRHN.PlusU1.QuadSol.toQuad_surjective`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean#L141).

```lean
lemma toQuad_surjective : Function.Surjective (toQuad C)
```

## Depends on

- [ACC system for SM with RHN](rhn-anomalycancellation-plusu1-basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSol.lean)
