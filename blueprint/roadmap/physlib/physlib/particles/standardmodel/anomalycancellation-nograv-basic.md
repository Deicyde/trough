---
declaration: module
origin: cited
lean: SM.SMNoGrav, SM.SMNoGrav.SU2Sol, SM.SMNoGrav.SU3Sol, SM.SMNoGrav.cubeSol, SM.SMNoGrav.chargeToLinear, SM.SMNoGrav.linearToQuad, SM.SMNoGrav.quadToAF, SM.SMNoGrav.chargeToQuad
statement: formalized
proof: formalized
---

# Anomaly Cancellation in the Standard Model without Gravity

The module `Physlib.Particles.StandardModel.AnomalyCancellation.NoGrav.Basic`, [Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean): 10 declarations, 10 with a docstring.

> This file defines the system of anomaly equations for the SM without RHN, and
> without the gravitational ACC.

**`SM.SMNoGrav`**, a def, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L26).

> The ACC system for the standard model without RHN and without the gravitational ACC.

```lean
def SMNoGrav (n : ℕ) : ACCSystem
```

**`SM.SMNoGrav.SU2Sol`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L45).

> The charges in `(SMNoGrav n).LinSols` satisfy the `SU(2)` anomaly-equation.

```lean
lemma SU2Sol (S : (SMNoGrav n).LinSols) : accSU2 S.val = 0
```

**`SM.SMNoGrav.SU3Sol`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L52).

> The charges in `(SMNoGrav n).LinSols` satisfy the `SU(3)` anomaly-equation.

```lean
lemma SU3Sol (S : (SMNoGrav n).LinSols) : accSU3 S.val = 0
```

**`SM.SMNoGrav.cubeSol`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L58).

> The charges in `(SMNoGrav n).Sols` satisfy the cubic anomaly-equation.

```lean
lemma cubeSol (S : (SMNoGrav n).Sols) : accCube S.val = 0
```

**`SM.SMNoGrav.chargeToLinear`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L62).

> An element of `charges` which satisfies the linear ACCs
> gives us a element of `AnomalyFreeLinear`.

```lean
def chargeToLinear (S : (SMNoGrav n).Charges) (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) :
    (SMNoGrav n).LinSols
```

**`SM.SMNoGrav.linearToQuad`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L72).

> An element of `AnomalyFreeLinear` which satisfies the quadratic ACCs
> gives us a element of `AnomalyFreeQuad`.

```lean
def linearToQuad (S : (SMNoGrav n).LinSols) : (SMNoGrav n).QuadSols
```

**`SM.SMNoGrav.quadToAF`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L79).

> An element of `AnomalyFreeQuad` which satisfies the quadratic ACCs
> gives us a element of `AnomalyFree`.

```lean
def quadToAF (S : (SMNoGrav n).QuadSols) (hc : accCube S.val = 0) :
    (SMNoGrav n).Sols
```

**`SM.SMNoGrav.chargeToQuad`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L84).

> An element of `charges` which satisfies the linear and quadratic ACCs
> gives us a element of `AnomalyFreeQuad`.

```lean
def chargeToQuad (S : (SMNoGrav n).Charges) (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0) :
    (SMNoGrav n).QuadSols
```

**`SM.SMNoGrav.chargeToAF`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L90).

> An element of `charges` which satisfies the linear, quadratic and cubic ACCs
> gives us a element of `AnomalyFree`.

```lean
def chargeToAF (S : (SMNoGrav n).Charges) (hSU2 : accSU2 S = 0) (hSU3 : accSU3 S = 0)
    (hc : accCube S = 0) : (SMNoGrav n).Sols
```

**`SM.SMNoGrav.linearToAF`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean#L96).

> An element of `AnomalyFreeLinear` which satisfies the quadratic and cubic ACCs
> gives us a element of `AnomalyFree`.

```lean
def linearToAF (S : (SMNoGrav n).LinSols)
    (hc : accCube S.val = 0) : (SMNoGrav n).Sols
```

## Depends on

- [Anomaly cancellation conditions for the n-family SM.](anomalycancellation-basic.md)

## Sources

- [Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/Basic.lean)
