---
declaration: module
origin: cited
lean: SMRHN.PlusU1.familyUniversalLinear, SMRHN.PlusU1.familyUniversalQuad, SMRHN.PlusU1.familyUniversalAF
statement: formalized
proof: formalized
---

# Family Maps for SM with RHN

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.FamilyMaps`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean): 3 declarations, 3 with a docstring.

> We give some properties of the family maps for the SM with RHN, in particular, we
> define family universal maps in the case of `LinSols`, `QuadSols`, and `Sols`.

**`SMRHN.PlusU1.familyUniversalLinear`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean#L30).

> The family universal maps on `LinSols`.

```lean
def familyUniversalLinear (n : ℕ) :
    (PlusU1 1).LinSols →ₗ[ℚ] (PlusU1 n).LinSols
```

**`SMRHN.PlusU1.familyUniversalQuad`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean#L42).

> The family universal maps on `QuadSols`.

```lean
def familyUniversalQuad (n : ℕ) :
    (PlusU1 1).QuadSols → (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.familyUniversalAF`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean#L53).

> The family universal maps on `Sols`.

```lean
def familyUniversalAF (n : ℕ) :
    (PlusU1 1).Sols → (PlusU1 n).Sols
```

## Depends on

- [Family maps for the Standard Model for RHN ACCs](rhn-anomalycancellation-familymaps.md)
- [ACC system for SM with RHN](rhn-anomalycancellation-plusu1-basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/FamilyMaps.lean)
