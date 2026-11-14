---
declaration: module
origin: cited
lean: StandardModel.LeptonSinglet.gaugeAlgebraAction, StandardModel.LeptonSinglet.gaugeAlgebraAction_apply, StandardModel.LeptonSinglet.jetPhase, StandardModel.LeptonSinglet.jetPhase_eq, StandardModel.LeptonSinglet.repJetGaugeGroupI_eq_jetPhase, StandardModel.LeptonSinglet.repCoeff_eq, StandardModel.LeptonSinglet.repCoeff_zero_of_eval_eq_one, StandardModel.LeptonSinglet.jetPhase_pderiv
statement: formalized
proof: formalized
---

# The gauge-algebra action on the charged-lepton singlet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonSinglet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean): 10 declarations, 10 with a docstring; 3 private, not shown.

## i. Overview

> The charged-lepton singlet carries the `(1, 1)_{-6}` representation of the gauge group,
> so the infinitesimal action of the gauge algebra is scalar: multiplication by
> `i` times `-6` times the `u(1)` value of the algebra element. This file defines that
> action and proves it is the infinitesimal action underlying the jet gauge action, in
> the sense of `LocalGaugeData.IsInfinitesimalActionOf`.
>
> Because the singlet has no colour or weak index, the jet gauge action is multiplication
> of the jet-ring factor by the hypercharge phase `(star u) ^ 6`, and both laws of
> `IsInfinitesimalActionOf` reduce to scalar identities about the base-point Taylor
> coefficients of that phase: the derivative identity `∂ ((star u) ^ 6) =
> -(i (-6) ω) (star u) ^ 6` against the `u(1)` value of the Maurer–Cartan form, and the
> trivial `u(1)` adjoint equivariance.

## ii. Key results

> - `gaugeAlgebraAction` : the infinitesimal `(1, 1)_{-6}` action of the gauge algebra.
> - `jetPhase` : the hypercharge phase `(star u) ^ 6` of the jet gauge action.
> - `repCoeff_eq` : the base-point Taylor coefficients of the jet gauge action are the
>   base-point Taylor coefficients of the hypercharge phase.
> - `jetPhase_pderiv` : the derivative identity for the hypercharge phase.
> - `isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal action
>   underlying the jet gauge action.

## iv. References

> * None.

## A. The infinitesimal action of the gauge algebra

> The `(1, 1)_{-6}` representation acts through the `u(1)` factor alone, so its
> derivative is scalar multiplication by `i (-6)` times the `u(1)` value.

**`StandardModel.LeptonSinglet.gaugeAlgebraAction`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L75).

> **The infinitesimal action of the gauge algebra on the charged-lepton singlet**:
> the derivative of the `(1, 1)_{-6}` action of the gauge group — scalar
> multiplication by `i` times `-6` times the `u(1)` value, real-linear in the algebra
> slot and complex-linear in the value slot — the form consumed by
> `LocalGaugeData.IsInfinitesimalActionOf`.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] LeptonSinglet →ₗ[ℂ] LeptonSinglet
```

**`StandardModel.LeptonSinglet.gaugeAlgebraAction_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L95).

> The gauge-algebra action on the charged-lepton singlet is scalar multiplication
> by `i` times `-6` times the `u(1)` value.

```lean
lemma gaugeAlgebraAction_apply (c : GaugeAlgebra) :
    gaugeAlgebraAction c
      = (Complex.I * (-(6 : ℂ) * c.toU1Value))
        • (LinearMap.id : LeptonSinglet →ₗ[ℂ] LeptonSinglet)
```

## B. The hypercharge phase of the jet gauge action

> The jet gauge action multiplies the jet-ring factor by the hypercharge power series
> `(star u) ^ 6`: the scalar analogue of the colour matrix of a coloured species.

**`StandardModel.LeptonSinglet.jetPhase`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L112).

> The `SpaceTimeAlgebra`-valued hypercharge phase of the jet gauge action on the
> charged-lepton singlet: the `-6` hypercharge power series `(star u) ^ 6` of the
> gauge jet.

```lean
noncomputable def jetPhase (U : JetGaugeGroupI) : SpaceTimeAlgebra
```

**`StandardModel.LeptonSinglet.jetPhase_eq`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L116).

> The hypercharge phase, unfolded.

```lean
lemma jetPhase_eq (U : JetGaugeGroupI) :
    jetPhase U = (star ((U.2.2 : unitary SpaceTimeAlgebra) : SpaceTimeAlgebra)) ^ 6
```

**`StandardModel.LeptonSinglet.repJetGaugeGroupI_eq_jetPhase`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L121).

> The jet gauge action on the charged-lepton singlet is multiplication of the
> jet-ring factor by the hypercharge phase.

```lean
lemma repJetGaugeGroupI_eq_jetPhase (U : JetGaugeGroupI) :
    repJetGaugeGroupI U
      = LinearMap.rTensor LeptonSinglet (LinearMap.mulLeft ℂ (jetPhase U))
```

## C. The Taylor coefficients of the jet gauge action

**`StandardModel.LeptonSinglet.repCoeff_eq`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L165).

> **The base-point Taylor coefficients of the jet gauge action** on the
> charged-lepton singlet are scalar: multiplication by the base-point Taylor
> coefficients of the hypercharge phase.

```lean
lemma repCoeff_eq (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U x
      = constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x (jetPhase U))
        • (LinearMap.id : LeptonSinglet →ₗ[ℂ] LeptonSinglet)
```

**`StandardModel.LeptonSinglet.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L179).

> At the base point, a gauge jet with trivial value acts trivially: the zeroth
> Taylor coefficient of the jet gauge action is the identity.

```lean
lemma repCoeff_zero_of_eval_eq_one {U : JetGaugeGroupI} (hU : U.eval = 1) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U 0 = LinearMap.id
```

## D. The derivative identity for the hypercharge phase

**`StandardModel.LeptonSinglet.jetPhase_pderiv`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L196).

> **The derivative identity** for the hypercharge phase of the jet gauge action: the
> formal derivative of the phase is minus `i` times `-6` times the `u(1)` value of the
> Maurer–Cartan form, times the phase.

```lean
lemma jetPhase_pderiv (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    pderiv μ (jetPhase U)
      = -(((Complex.I * (-(6 : ℂ))) • (maurerCartanForm U μ).toU1Value)
          * jetPhase U)
```

## E. The infinitesimal action underlies the jet gauge action

> Both laws of `LocalGaugeData.IsInfinitesimalActionOf` reduce through `repCoeff_eq` to
> scalar identities: the Maurer–Cartan Leibniz law is the all-orders product rule at the
> base point applied to the derivative identity, and the adjoint intertwining collapses
> because the adjoint action on the `u(1)` component is trivial.

**`StandardModel.LeptonSinglet.isInfinitesimalActionOf`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L250).

> **The `(1, 1)_{-6}` action of the gauge algebra is the infinitesimal action
> underlying the jet gauge action on the charged-lepton singlet**: its base-point
> Taylor coefficients obey the Maurer–Cartan Leibniz law and intertwine the action
> with the adjoint transports.

```lean
lemma isInfinitesimalActionOf :
    localGaugeData.IsInfinitesimalActionOf gaugeAlgebraAction repJetGaugeGroupI
```

## F. The gauge action commutes with the Lorentz action

**`StandardModel.LeptonSinglet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean#L323).

> The infinitesimal gauge action on the charged-lepton singlet is a scalar, so it
> commutes with the Lorentz action.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : LeptonSinglet) :
    LeptonSinglet.gaugeAlgebraAction c (LeptonSinglet.repLorentzGroup Λ v) =
      LeptonSinglet.repLorentzGroup Λ (LeptonSinglet.gaugeAlgebraAction c v)
```

## Depends on

- [Charged-lepton singlets (PhyslibAlpha)](fermions-leptonsinglet-basic.md)
- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonSinglet/GaugeAlgebraAction.lean)
