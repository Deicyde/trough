---
declaration: module
origin: cited
lean: SMRHN.SM, SMRHN.SM.gravSol, SMRHN.SM.SU2Sol, SMRHN.SM.SU3Sol, SMRHN.SM.cubeSol, SMRHN.SM.chargeToLinear, SMRHN.SM.linearToQuad, SMRHN.SM.quadToAF
statement: formalized
proof: formalized
---

# ACC system for SM with RHN (without hypercharge).

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.Ordinary.Basic`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean): 12 declarations, 8 with a docstring.

> We define the ACC system for the Standard Model (without hypercharge) with right-handed neutrinos.

**`SMRHN.SM`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L25).

> The ACC system for the SM plus RHN.

```lean
def SM (n : ℕ) : ACCSystem
```

**`SMRHN.SM.gravSol`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L41).

```lean
lemma gravSol (S : (SM n).LinSols) : accGrav S.val = 0
```

**`SMRHN.SM.SU2Sol`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L43).

```lean
lemma SU2Sol (S : (SM n).LinSols) : accSU2 S.val = 0
```

**`SMRHN.SM.SU3Sol`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L45).

```lean
lemma SU3Sol (S : (SM n).LinSols) : accSU3 S.val = 0
```

**`SMRHN.SM.cubeSol`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L47).

```lean
lemma cubeSol (S : (SM n).Sols) : accCube S.val = 0
```

**`SMRHN.SM.chargeToLinear`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L51).

> An element of `charges` which satisfies the linear ACCs
> gives us a element of `LinSols`.

```lean
def chargeToLinear (S : (SM n).Charges) (hGrav : accGrav S = 0)
    (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) : (SM n).LinSols
```

**`SMRHN.SM.linearToQuad`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L62).

> An element of `LinSols` which satisfies the quadratic ACCs
> gives us a element of `QuadSols`.

```lean
def linearToQuad (S : (SM n).LinSols) : (SM n).QuadSols
```

**`SMRHN.SM.quadToAF`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L67).

> An element of `QuadSols` which satisfies the quadratic ACCs
> gives us a element of `Sols`.

```lean
def quadToAF (S : (SM n).QuadSols) (hc : accCube S.val = 0) :
    (SM n).Sols
```

**`SMRHN.SM.chargeToQuad`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L72).

> An element of `charges` which satisfies the linear and quadratic ACCs
> gives us a element of `QuadSols`.

```lean
def chargeToQuad (S : (SM n).Charges) (hGrav : accGrav S = 0)
    (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) :
    (SM n).QuadSols
```

**`SMRHN.SM.chargeToAF`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L79).

> An element of `charges` which satisfies the linear, quadratic and cubic ACCs
> gives us a element of `Sols`.

```lean
def chargeToAF (S : (SM n).Charges) (hGrav : accGrav S = 0) (hSU2 : accSU2 S = 0)
    (hSU3 : accSU3 S = 0) (hc : accCube S = 0) : (SM n).Sols
```

**`SMRHN.SM.linearToAF`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L85).

> An element of `LinSols` which satisfies the quadratic and cubic ACCs
> gives us a element of `Sols`.

```lean
def linearToAF (S : (SM n).LinSols)
    (hc : accCube S.val = 0) : (SM n).Sols
```

**`SMRHN.SM.perm`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean#L90).

> The permutations acting on the ACC system corresponding to the SM with RHN.

```lean
def perm (n : ℕ) : ACCSystemGroupAction (SM n)
```

## Depends on

- [Permutations of SM charges with RHN.](rhn-anomalycancellation-permutations.md)
- [Group actions on ACC systems.](../../qft/anomalycancellation/groupactions.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/Ordinary/Basic.lean)
