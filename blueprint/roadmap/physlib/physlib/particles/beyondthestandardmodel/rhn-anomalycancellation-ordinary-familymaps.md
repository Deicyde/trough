---
declaration: module
origin: cited
lean: SMRHN.SM.familyUniversalLinear, SMRHN.SM.familyUniversalQuad, SMRHN.SM.familyUniversalAF
statement: formalized
proof: formalized
---

# Family Maps for SM with RHN (no hypercharge)

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.Ordinary.FamilyMaps`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean): 3 declarations, 3 with a docstring.

> We give some properties of the family maps for the SM with RHN, in particular, we
> define family universal maps in the case of `LinSols`, `QuadSols`, and `Sols`.

**`SMRHN.SM.familyUniversalLinear`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean#L30).

> The family universal maps on `LinSols`.

```lean
def familyUniversalLinear (n : ℕ) :
    (SM 1).LinSols →ₗ[ℚ] (SM n).LinSols
```

**`SMRHN.SM.familyUniversalQuad`**, a def, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean#L41).

> The family universal maps on `QuadSols`.

```lean
def familyUniversalQuad (n : ℕ) :
    (SM 1).QuadSols → (SM n).QuadSols
```

**`SMRHN.SM.familyUniversalAF`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean#L50).

> The family universal maps on `Sols`.

```lean
def familyUniversalAF (n : ℕ) :
    (SM 1).Sols → (SM n).Sols
```

## Depends on

- [Family maps for the Standard Model for RHN ACCs](rhn-anomalycancellation-familymaps.md)
- [ACC system for SM with RHN (without hypercharge).](rhn-anomalycancellation-ordinary-basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/FamilyMaps.lean)
