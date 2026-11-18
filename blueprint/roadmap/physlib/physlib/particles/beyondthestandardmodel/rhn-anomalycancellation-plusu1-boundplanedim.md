---
declaration: module
origin: cited
lean: SMRHN.PlusU1.ExistsPlane, SMRHN.PlusU1.exists_plane_exists_basis, SMRHN.PlusU1.plane_exists_dim_le_7
statement: formalized
proof: formalized
---

# Bound on plane dimension

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.BoundPlaneDim`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean): 3 declarations, 1 with a docstring.

> We place an upper bound on the dimension of a plane of charges on which every point is a solution.
> The upper bound is 7, proven in the theorem `plane_exists_dim_le_7`.

**`SMRHN.PlusU1.ExistsPlane`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean#L28).

> A proposition which is true if for a given `n`, a plane of charges of dimension `n` exists
> in which each point is a solution.

```lean
def ExistsPlane (n : ℕ) : Prop
```

**`SMRHN.PlusU1.exists_plane_exists_basis`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean#L32).

```lean
lemma exists_plane_exists_basis {n : ℕ} (hE : ExistsPlane n) :
    ∃ (B : Fin 11 ⊕ Fin n → (PlusU1 3).Charges), LinearIndependent ℚ B
```

**`SMRHN.PlusU1.plane_exists_dim_le_7`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean#L51).

```lean
lemma plane_exists_dim_le_7 {n : ℕ} (hn : ExistsPlane n) : n ≤ 7
```

## Depends on

- [ACC system for SM with RHN](rhn-anomalycancellation-plusu1-basic.md)

## Proof depends on

- [Plane of non-solutions](rhn-anomalycancellation-plusu1-planenonsols.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/BoundPlaneDim.lean)
