---
declaration: module
origin: cited
lean: SMRHN.PlusU1.QuadSolToSol.α₁, SMRHN.PlusU1.QuadSolToSol.α₂, SMRHN.PlusU1.QuadSolToSol.cube_α₁_α₂_zero, SMRHN.PlusU1.QuadSolToSol.α₂_AF, SMRHN.PlusU1.QuadSolToSol.BL_add_α₁_α₂_cube, SMRHN.PlusU1.QuadSolToSol.BL_add_α₁_α₂_AF, SMRHN.PlusU1.QuadSolToSol.generic, SMRHN.PlusU1.QuadSolToSol.generic_on_AF
statement: formalized
proof: formalized
---

# Solutions from quad solutions

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.QuadSolToSol`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean): 20 declarations, 6 with a docstring.

> We use $B-L$ to form a surjective map from quad solutions to solutions.

## References

> * The main reference for this material is https://arxiv.org/abs/2006.03588. [ref: arxiv\_2006\_03588]

**`SMRHN.PlusU1.QuadSolToSol.α₁`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L32).

> A helper function for what follows.

```lean
def α₁ (S : (PlusU1 n).QuadSols) : ℚ
```

**`SMRHN.PlusU1.QuadSolToSol.α₂`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L35).

> A helper function for what follows.

```lean
def α₂ (S : (PlusU1 n).QuadSols) : ℚ
```

**`SMRHN.PlusU1.QuadSolToSol.cube_α₁_α₂_zero`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L37).

```lean
lemma cube_α₁_α₂_zero (S : (PlusU1 n).QuadSols) (a b : ℚ) (h1 : α₁ S = 0) (h2 : α₂ S = 0) :
    accCube (BL.addQuad S a b).val = 0
```

**`SMRHN.PlusU1.QuadSolToSol.α₂_AF`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L42).

```lean
lemma α₂_AF (S : (PlusU1 n).Sols) : α₂ S.toQuadSols = 0
```

**`SMRHN.PlusU1.QuadSolToSol.BL_add_α₁_α₂_cube`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L44).

```lean
lemma BL_add_α₁_α₂_cube (S : (PlusU1 n).QuadSols) :
    accCube (BL.addQuad S (α₁ S) (α₂ S)).val = 0
```

**`SMRHN.PlusU1.QuadSolToSol.BL_add_α₁_α₂_AF`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L53).

```lean
lemma BL_add_α₁_α₂_AF (S : (PlusU1 n).Sols) :
    BL.addQuad S.1 (α₁ S.1) (α₂ S.1) = (α₁ S.1) • S.1
```

**`SMRHN.PlusU1.QuadSolToSol.generic`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L58).

> The construction of a `Sol` from a `QuadSol` in the generic case.

```lean
def generic (S : (PlusU1 n).QuadSols) : (PlusU1 n).Sols
```

**`SMRHN.PlusU1.QuadSolToSol.generic_on_AF`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L61).

```lean
lemma generic_on_AF (S : (PlusU1 n).Sols) : generic S.1 = (α₁ S.1) • S
```

**`SMRHN.PlusU1.QuadSolToSol.generic_on_AF_α₁_ne_zero`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L67).

```lean
lemma generic_on_AF_α₁_ne_zero (S : (PlusU1 n).Sols) (h : α₁ S.1 ≠ 0) :
    (α₁ S.1)⁻¹ • generic S.1 = S
```

**`SMRHN.PlusU1.QuadSolToSol.special`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L72).

> The construction of a `Sol` from a `QuadSol` in the case when `α₁ S = 0` and `α₂ S = 0`.

```lean
def special (S : (PlusU1 n).QuadSols) (a b : ℚ) (h1 : α₁ S = 0) (h2 : α₂ S = 0) :
    (PlusU1 n).Sols
```

**`SMRHN.PlusU1.QuadSolToSol.special_on_AF`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L76).

```lean
lemma special_on_AF (S : (PlusU1 n).Sols) (h1 : α₁ S.1 = 0) :
    special S.1 1 0 h1 (α₂_AF S) = S
```

**`SMRHN.PlusU1.quadSolToSol`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L88).

> A map from `QuadSols × ℚ × ℚ` to `Sols` taking account of the special and generic cases.
> We will show that this map is a surjection.

```lean
def quadSolToSol {n : ℕ} : (PlusU1 n).QuadSols × ℚ × ℚ → (PlusU1 n).Sols
```

**`SMRHN.PlusU1.quadSolToSolInv`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L96).

> A map from `Sols` to `QuadSols × ℚ × ℚ` which forms a right-inverse to `quadSolToSol`, as
> shown in `quadSolToSolInv_rightInverse`.

```lean
def quadSolToSolInv {n : ℕ} : (PlusU1 n).Sols → (PlusU1 n).QuadSols × ℚ × ℚ
```

**`SMRHN.PlusU1.quadSolToSolInv_1`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L103).

```lean
lemma quadSolToSolInv_1 (S : (PlusU1 n).Sols) :
    (quadSolToSolInv S).1 = S.1
```

**`SMRHN.PlusU1.quadSolToSolInv_α₁_α₂_zero`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L109).

```lean
lemma quadSolToSolInv_α₁_α₂_zero (S : (PlusU1 n).Sols) (h : α₁ S.1 = 0) :
    α₁ (quadSolToSolInv S).1 = 0 ∧ α₂ (quadSolToSolInv S).1 = 0
```

**`SMRHN.PlusU1.quadSolToSolInv_α₁_α₂_ne_zero`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L114).

```lean
lemma quadSolToSolInv_α₁_α₂_ne_zero (S : (PlusU1 n).Sols) (h : α₁ S.1 ≠ 0) :
    ¬ (α₁ (quadSolToSolInv S).1 = 0 ∧ α₂ (quadSolToSolInv S).1 = 0)
```

**`SMRHN.PlusU1.quadSolToSolInv_special`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L120).

```lean
lemma quadSolToSolInv_special (S : (PlusU1 n).Sols) (h : α₁ S.1 = 0) :
    special (quadSolToSolInv S).1 (quadSolToSolInv S).2.1 (quadSolToSolInv S).2.2
    (quadSolToSolInv_α₁_α₂_zero S h).1 (quadSolToSolInv_α₁_α₂_zero S h).2 = S
```

**`SMRHN.PlusU1.quadSolToSolInv_generic`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L128).

```lean
lemma quadSolToSolInv_generic (S : (PlusU1 n).Sols) (h : α₁ S.1 ≠ 0) :
    (quadSolToSolInv S).2.1 • generic (quadSolToSolInv S).1 = S
```

**`SMRHN.PlusU1.quadSolToSolInv_rightInverse`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L134).

```lean
lemma quadSolToSolInv_rightInverse : Function.RightInverse (@quadSolToSolInv n) quadSolToSol
```

**`SMRHN.PlusU1.quadSolToSol_surjective`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean#L142).

```lean
lemma quadSolToSol_surjective : Function.Surjective (@quadSolToSol n)
```

## Depends on

- [B Minus L in SM with RHN.](rhn-anomalycancellation-plusu1-bminusl.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/QuadSolToSol.lean)
