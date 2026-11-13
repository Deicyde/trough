---
declaration: module
origin: cited
lean: FluidDynamics.CauchyFlow.matrixDiv_stress_eq_neg_grad_pressure_of_is_inviscid, FluidDynamics.CauchyFlow.IsInviscid, FluidDynamics.CauchyFlow.matrixDiv_inviscid_pressure_stress
statement: formalized
proof: formalized
---

# Inviscid stress laws for Cauchy flows

The module `Physlib.FluidDynamics.CauchyFlow.Inviscid`, [Physlib/FluidDynamics/CauchyFlow/Inviscid.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Inviscid.lean): 3 declarations, 3 with a docstring, 1 listed as significant.

## i. Overview

> This module defines the inviscid stress law for `CauchyFlow` and the corresponding
> matrix-divergence identity for pressure stress.

## ii. Key results

> - `CauchyFlow.IsInviscid` : Predicate saying the Cauchy stress is the inviscid pressure stress.
> - `CauchyFlow.matrixDiv_stress_eq_neg_grad_pressure_of_is_inviscid` : The inviscid stress
>   contributes the usual pressure-gradient force term.

## iv. References

> * None.

## A. Inviscid stress law

**`FluidDynamics.CauchyFlow.IsInviscid`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Inviscid.lean#L54).

> A Cauchy flow is inviscid with pressure `p` when its stress is the isotropic pressure stress
> `-p I`.
>
> In this formulation, inviscid means that the Cauchy stress has no viscous or shear contribution.
> It does not rule out body forces; those are carried separately by `CauchyFlow.specificBodyForce`.

```lean
def IsInviscid (d : ℕ) (flow : CauchyFlow d) (pressure : ScalarField d) : Prop
```

**`FluidDynamics.CauchyFlow.matrixDiv_inviscid_pressure_stress`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Inviscid.lean#L58).

> The matrix divergence of the inviscid pressure stress `-p I` is `-grad p`.

```lean
lemma matrixDiv_inviscid_pressure_stress (d : ℕ) (pressureAtTime : Space d → ℝ) :
    matrixDiv d (fun x => (-(pressureAtTime x)) • (1 : Matrix (Fin d) (Fin d) ℝ)) =
      -∇ pressureAtTime
```

**`FluidDynamics.CauchyFlow.matrixDiv_stress_eq_neg_grad_pressure_of_is_inviscid`**, a theorem, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Inviscid.lean#L73). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> In an inviscid Cauchy flow, the stress-divergence force is the usual
> negative pressure-gradient term.

```lean
theorem matrixDiv_stress_eq_neg_grad_pressure_of_is_inviscid
    (d : ℕ) (flow : CauchyFlow d) (pressure : ScalarField d)
    (hInviscid : IsInviscid d flow pressure) :
    ∀ t, matrixDiv d (flow.stress t) = -∇ (pressure t)
```

## Depends on

- [Basic API for Cauchy flows](basic.md)
- [Matrix divergence on Space](../../spaceandtime/space/part-01/derivatives-matrixdiv.md)

## Sources

- [Physlib/FluidDynamics/CauchyFlow/Inviscid.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/FluidDynamics/CauchyFlow/Inviscid.lean)
