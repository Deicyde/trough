---
declaration: module
origin: cited
lean: SMRHN.SMNoGrav, SMRHN.SMNoGrav.SU2Sol, SMRHN.SMNoGrav.SU3Sol, SMRHN.SMNoGrav.cubeSol, SMRHN.SMNoGrav.chargeToLinear, SMRHN.SMNoGrav.linearToQuad, SMRHN.SMNoGrav.quadToAF, SMRHN.SMNoGrav.chargeToQuad
statement: formalized
proof: formalized
---

# ACC system for SM with RHN and no gravitational anomaly.

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.NoGrav.Basic`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean): 11 declarations, 8 with a docstring.

> We define the ACC system for the Standard Model with right-handed neutrinos and no gravitational
> anomaly.

**`SMRHN.SMNoGrav`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L26).

> The ACC system for the SM plus RHN with no gravitational anomaly.

```lean
def SMNoGrav (n : ℕ) : ACCSystem
```

**`SMRHN.SMNoGrav.SU2Sol`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L41).

```lean
lemma SU2Sol (S : (SMNoGrav n).LinSols) : accSU2 S.val = 0
```

**`SMRHN.SMNoGrav.SU3Sol`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L43).

```lean
lemma SU3Sol (S : (SMNoGrav n).LinSols) : accSU3 S.val = 0
```

**`SMRHN.SMNoGrav.cubeSol`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L45).

```lean
lemma cubeSol (S : (SMNoGrav n).Sols) : accCube S.val = 0
```

**`SMRHN.SMNoGrav.chargeToLinear`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L49).

> An element of `charges` which satisfies the linear ACCs
> gives us a element of `LinSols`.

```lean
def chargeToLinear (S : (SMNoGrav n).Charges) (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) :
    (SMNoGrav n).LinSols
```

**`SMRHN.SMNoGrav.linearToQuad`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L59).

> An element of `LinSols` which satisfies the quadratic ACCs
> gives us a element of `QuadSols`.

```lean
def linearToQuad (S : (SMNoGrav n).LinSols) : (SMNoGrav n).QuadSols
```

**`SMRHN.SMNoGrav.quadToAF`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L63).

> An element of `QuadSols` which satisfies the quadratic ACCs
> gives us a element of `LinSols`.

```lean
def quadToAF (S : (SMNoGrav n).QuadSols) (hc : accCube S.val = 0) :
    (SMNoGrav n).Sols
```

**`SMRHN.SMNoGrav.chargeToQuad`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L68).

> An element of `charges` which satisfies the linear and quadratic ACCs
> gives us a element of `QuadSols`.

```lean
def chargeToQuad (S : (SMNoGrav n).Charges) (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) :
    (SMNoGrav n).QuadSols
```

**`SMRHN.SMNoGrav.chargeToAF`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L74).

> An element of `charges` which satisfies the linear, quadratic and cubic ACCs
> gives us a element of `Sols`.

```lean
def chargeToAF (S : (SMNoGrav n).Charges) (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0)
    (hc : accCube S = 0) : (SMNoGrav n).Sols
```

**`SMRHN.SMNoGrav.linearToAF`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L80).

> An element of `LinSols` which satisfies the quadratic and cubic ACCs
> gives us a element of `Sols`.

```lean
def linearToAF (S : (SMNoGrav n).LinSols)
    (hc : accCube S.val = 0) : (SMNoGrav n).Sols
```

**`SMRHN.SMNoGrav.perm`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean#L86).

> The permutations acting on the ACC system corresponding to the SM with RHN,
> and no gravitational anomaly.

```lean
def perm (n : ℕ) : ACCSystemGroupAction (SMNoGrav n)
```

## Depends on

- [Permutations of SM charges with RHN.](rhn-anomalycancellation-permutations.md)
- [Group actions on ACC systems.](../../qft/anomalycancellation/groupactions.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/NoGrav/Basic.lean)
