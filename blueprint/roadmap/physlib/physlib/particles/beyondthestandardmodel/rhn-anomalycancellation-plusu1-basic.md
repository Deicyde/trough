---
declaration: module
origin: cited
lean: SMRHN.PlusU1, SMRHN.PlusU1.gravSol, SMRHN.PlusU1.SU2Sol, SMRHN.PlusU1.SU3Sol, SMRHN.PlusU1.YYsol, SMRHN.PlusU1.quadSol, SMRHN.PlusU1.cubeSol, SMRHN.PlusU1.chargeToLinear
statement: formalized
proof: formalized
---

# ACC system for SM with RHN

The module `Physlib.Particles.BeyondTheStandardModel.RHN.AnomalyCancellation.PlusU1.Basic`, [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean): 14 declarations, 8 with a docstring.

> We define the ACC system for the Standard Model with right-handed neutrinos.

**`SMRHN.PlusU1`**, a def, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L25).

> The ACC system for the SM plus RHN with an additional U1.

```lean
def PlusU1 (n : ℕ) : ACCSystem
```

**`SMRHN.PlusU1.gravSol`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L45).

```lean
lemma gravSol (S : (PlusU1 n).LinSols) : accGrav S.val = 0
```

**`SMRHN.PlusU1.SU2Sol`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L51).

```lean
lemma SU2Sol (S : (PlusU1 n).LinSols) : accSU2 S.val = 0
```

**`SMRHN.PlusU1.SU3Sol`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L57).

```lean
lemma SU3Sol (S : (PlusU1 n).LinSols) : accSU3 S.val = 0
```

**`SMRHN.PlusU1.YYsol`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L63).

```lean
lemma YYsol (S : (PlusU1 n).LinSols) : accYY S.val = 0
```

**`SMRHN.PlusU1.quadSol`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L69).

```lean
lemma quadSol (S : (PlusU1 n).QuadSols) : accQuad S.val = 0
```

**`SMRHN.PlusU1.cubeSol`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L74).

```lean
lemma cubeSol (S : (PlusU1 n).Sols) : accCube S.val = 0
```

**`SMRHN.PlusU1.chargeToLinear`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L79).

> An element of `charges` which satisfies the linear ACCs
> gives us a element of `LinSols`.

```lean
def chargeToLinear (S : (PlusU1 n).Charges) (hGrav : accGrav S = 0)
    (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) (hYY : accYY S = 0) :
    (PlusU1 n).LinSols
```

**`SMRHN.PlusU1.linearToQuad`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L92).

> An element of `LinSols` which satisfies the quadratic ACCs
> gives us a element of `AnomalyFreeQuad`.

```lean
def linearToQuad (S : (PlusU1 n).LinSols) (hQ : accQuad S.val = 0) :
    (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.quadToAF`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L101).

> An element of `QuadSols` which satisfies the quadratic ACCs
> gives us a element of `Sols`.

```lean
def quadToAF (S : (PlusU1 n).QuadSols) (hc : accCube S.val = 0) :
    (PlusU1 n).Sols
```

**`SMRHN.PlusU1.chargeToQuad`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L106).

> An element of `charges` which satisfies the linear and quadratic ACCs
> gives us a element of `QuadSols`.

```lean
def chargeToQuad (S : (PlusU1 n).Charges) (hGrav : accGrav S = 0)
    (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) (hYY : accYY S = 0) (hQ : accQuad S = 0) :
    (PlusU1 n).QuadSols
```

**`SMRHN.PlusU1.chargeToAF`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L113).

> An element of `charges` which satisfies the linear, quadratic and cubic ACCs
> gives us a element of `Sols`.

```lean
def chargeToAF (S : (PlusU1 n).Charges) (hGrav : accGrav S = 0) (hSU2 : accSU2 S = 0)
    (hSU3 : accSU3 S = 0) (hYY : accYY S = 0) (hQ : accQuad S = 0) (hc : accCube S = 0) :
    (PlusU1 n).Sols
```

**`SMRHN.PlusU1.linearToAF`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L120).

> An element of `LinSols` which satisfies the quadratic and cubic ACCs
> gives us a element of `Sols`.

```lean
def linearToAF (S : (PlusU1 n).LinSols) (hQ : accQuad S.val = 0)
    (hc : accCube S.val = 0) : (PlusU1 n).Sols
```

**`SMRHN.PlusU1.perm`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean#L125).

> The permutations acting on the ACC system corresponding to the SM with RHN.

```lean
def perm (n : ℕ) : ACCSystemGroupAction (PlusU1 n)
```

## Depends on

- [Permutations of SM charges with RHN.](rhn-anomalycancellation-permutations.md)
- [Group actions on ACC systems.](../../qft/anomalycancellation/groupactions.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/RHN/AnomalyCancellation/PlusU1/Basic.lean)
