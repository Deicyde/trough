---
declaration: module
origin: cited
lean: QED.Photon.JetAlgebra.deriv_coPotential, QED.Photon.JetAlgebra.evalPotential_fieldStrength_zero_apply, QED.Photon.JetAlgebra.evalPotential_fieldStrength_zero, QED.Photon.JetAlgebra.evalPotential_maxwellTerm, QED.Photon.JetAlgebra.electricField_eq_evalPotential_fieldStrength, QED.Photon.JetAlgebra.magneticField_eq_evalPotential_fieldStrength, QED.Photon.JetAlgebra.evalPotential_neg_quarter_maxwellTerm, QED.Photon.JetAlgebra.contDiff_coPotential
statement: formalized
proof: formalized
---

# Evaluation of the photon jet algebra on a potential

The module `PhyslibAlpha.Particles.QED.Evaluation`, [PhyslibAlpha/Particles/QED/Evaluation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean): 18 declarations, 13 with a docstring.

## i. Overview

> The theorems tying the formal photon jet algebra of QED to the honest
> electromagnetism of `Physlib.Electromagnetism`, through the evaluation map
> `Photon.JetAlgebra.evalPotential` of `PhyslibAlpha.Particles.QED.Basic`:
>
> * evaluated on any differentiable potential, the formal field strength is the
>   field strength of the potential with both indices lowered;
> * evaluated on any differentiable potential, the formal Maxwell term
>   `F_{μν} F^{μν}` is `-4 μ₀` times `ElectromagneticPotential.kineticTerm`;
> * the evaluation is compatible with concrete gauge transformations
>   `A ↦ A + ∂χ`, matching the formal gauge invariance of
>   `PhyslibAlpha.Particles.QED.GaugeInvariance` on the concrete side.
>
> Only the photon sector evaluates: fermionic jet coordinates would have to be
> evaluated on anticommuting (Grassmann-valued) fields, which have no
> realisation as honest functions on spacetime.
>
> This file contains no definitions, only theorems.

## ii. Key results

> - `Photon.JetAlgebra.evalPotential_fieldStrength_zero` : the formal field
>   strength evaluates to the field strength.
> - `Photon.JetAlgebra.evalPotential_maxwellTerm` : **the formal Maxwell term
>   is the Maxwell Lagrangian**.
> - `Photon.JetAlgebra.electricField_eq_evalPotential_fieldStrength`,
>   `Photon.JetAlgebra.magneticField_eq_evalPotential_fieldStrength` : the
>   time–space and space–space components of the evaluated formal field
>   strength are the electric and magnetic fields.
> - `Photon.JetAlgebra.evalPotential_neg_quarter_maxwellTerm` : the Maxwell
>   part of the QED Lagrangian is `μ₀` times the electromagnetic kinetic term.
> - `Photon.JetAlgebra.evalPotential_fieldStrength_gaugeTransform`,
>   `Photon.JetAlgebra.evalPotential_maxwellTerm_gaugeTransform` :
>   compatibility with concrete gauge transformations.
> - `Photon.JetAlgebra.evalPotential_maxwell_homogeneous` : **the homogeneous
>   Maxwell equations**, as the evaluation of the formal Bianchi identity.
> - `Photon.JetAlgebra.evalPotential_fieldStrength_lorentzAction` :
>   compatibility of the formal and concrete Lorentz actions.

## iv. References

> The evaluation map is defined in `PhyslibAlpha.Particles.QED.Basic`; the concrete side is
> `Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean` and
> `Physlib/Electromagnetism/Dynamics/KineticTerm.lean`.

## A. Evaluation of the field strength

**`QED.Photon.JetAlgebra.deriv_coPotential`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L93).

> The derivative of a covariant component.  Differentiability is needed to move
> the constant `η_{νν}` through the derivative.

```lean
lemma deriv_coPotential (A : ElectromagneticPotential 3) (hA : Differentiable ℝ A)
    (μ ν : Fin 1 ⊕ Fin 3) (x : SpaceTime 3) :
    ∂_ μ (coPotential A ν) x = η ν ν * ∂_ μ A x ν
```

**`QED.Photon.JetAlgebra.evalPotential_fieldStrength_zero_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L102).

```lean
lemma evalPotential_fieldStrength_zero_apply (A : ElectromagneticPotential 3)
    (hA : Differentiable ℝ A) (μ ν : Fin 1 ⊕ Fin 3) (x : SpaceTime 3) :
    evalPotential A (fieldStrength 0 μ ν) x = η ν ν * ∂_ μ A x ν - η μ μ * ∂_ ν A x μ
```

**`QED.Photon.JetAlgebra.evalPotential_fieldStrength_zero`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L111).

> The formal field strength evaluates to the field strength of the potential
> with both indices lowered, `F_{μν} = η_{μμ} η_{νν} F^{μν}`.

```lean
lemma evalPotential_fieldStrength_zero (A : ElectromagneticPotential 3)
    (hA : Differentiable ℝ A) (μ ν : Fin 1 ⊕ Fin 3) (x : SpaceTime 3) :
    evalPotential A (fieldStrength 0 μ ν) x =
      η μ μ * η ν ν * toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ
```

## B. The Maxwell term is the Maxwell Lagrangian

**`QED.Photon.JetAlgebra.evalPotential_maxwellTerm`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L131).

> **The formal Maxwell term is the Maxwell Lagrangian.**  Evaluated on any
> differentiable electromagnetic potential, the gauge-invariant jet polynomial
> `F_{μν} F^{μν}` is `-4 μ₀` times the kinetic term
> `- 1/(4 μ₀) F_{μν} F^{μν}` of `Physlib.Electromagnetism`.

```lean
lemma evalPotential_maxwellTerm (𝓕 : FreeSpace) (A : ElectromagneticPotential 3)
    (hA : Differentiable ℝ A) (x : SpaceTime 3) :
    evalPotential A maxwellTerm x = -(4 * 𝓕.μ₀) * A.kineticTerm 𝓕 x
```

## C. B'. The electric and magnetic fields from the jet algebra

> Splitting spacetime into time and space through `toTimeAndSpace`, the
> time–space components of the evaluated formal field strength are the electric
> field and the space–space components the magnetic field of
> `Physlib.Electromagnetism`.

**`QED.Photon.JetAlgebra.electricField_eq_evalPotential_fieldStrength`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L171).

> The electric field is (the speed of light times) the evaluated time–space
> components of the formal field strength: `E_i = c ∂_0 A_i - c ∂_i A_0`
> with lowered indices.

```lean
lemma electricField_eq_evalPotential_fieldStrength (c : SpeedOfLight)
    (A : ElectromagneticPotential 3) (hA : Differentiable ℝ A) (t : Time)
    (x : Space) (i : Fin 3) :
    A.electricField c t x i =
      c * evalPotential A (fieldStrength 0 (Sum.inl 0) (Sum.inr i))
        ((toTimeAndSpace c).symm (t, x))
```

**`QED.Photon.JetAlgebra.magneticField_eq_evalPotential_fieldStrength`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L184).

> The magnetic field is the evaluated space–space components of the formal
> field strength, `B_i = - F_{(i+1)(i+2)}` with lowered indices.

```lean
lemma magneticField_eq_evalPotential_fieldStrength (c : SpeedOfLight)
    (A : ElectromagneticPotential 3) (hA : Differentiable ℝ A) (t : Time)
    (x : Space) (i : Fin 3) :
    A.magneticField c t x i =
      - evalPotential A (fieldStrength 0 (Sum.inr (i + 1)) (Sum.inr (i + 2)))
        ((toTimeAndSpace c).symm (t, x))
```

## D. B''. The Maxwell part of the QED Lagrangian

**`QED.Photon.JetAlgebra.evalPotential_neg_quarter_maxwellTerm`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L204).

> The Maxwell part `- 1/4 F_{μν} F^{μν}` of the QED Lagrangian evaluates to
> `μ₀` times the electromagnetic kinetic term of
> `Physlib.Electromagnetism.Dynamics`: the two Lagrangians agree up to the
> choice of units absorbed into the field normalisation.

```lean
lemma evalPotential_neg_quarter_maxwellTerm (𝓕 : FreeSpace)
    (A : ElectromagneticPotential 3) (hA : Differentiable ℝ A) (x : SpaceTime 3) :
    evalPotential A ((-(1 : ℝ)/4) • maxwellTerm) x = 𝓕.μ₀ * A.kineticTerm 𝓕 x
```

## E. First-order jets and the homogeneous Maxwell equations

> Evaluation intertwines the first-order jet of the field strength with the
> honest spacetime derivative — for a `C²` potential the sorted iterated
> derivative is symmetric by Clairaut's theorem — and hence the formal Bianchi
> identity of `PhyslibAlpha.Particles.QED.FieldStrength` evaluates to **the homogeneous
> Maxwell equations** in covariant form.

**`QED.Photon.JetAlgebra.contDiff_coPotential`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L224).

```lean
lemma contDiff_coPotential {A : ElectromagneticPotential 3} (hA : ContDiff ℝ 2 A)
    (ν : Fin 1 ⊕ Fin 3) : ContDiff ℝ 2 (coPotential A ν)
```

**`QED.Photon.JetAlgebra.derivMultiset_pair`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L232).

> The iterated derivative along a pair of directions, in either order: for a
> `C²` function the canonical sorted order is immaterial by Clairaut's
> theorem.

```lean
lemma derivMultiset_pair (a b : Fin 1 ⊕ Fin 3) (f : SpaceTime 3 → ℝ)
    (hf : ContDiff ℝ 2 f) :
    derivMultiset {a, b} f = ∂_ a (∂_ b f)
```

**`QED.Photon.JetAlgebra.deriv_sub_eq`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L259).

```lean
lemma deriv_sub_eq {f g : SpaceTime 3 → ℝ} (lam : Fin 1 ⊕ Fin 3)
    (hf : Differentiable ℝ f) (hg : Differentiable ℝ g) :
    ∂_ lam (f - g) = ∂_ lam f - ∂_ lam g
```

**`QED.Photon.JetAlgebra.evalPotential_fieldStrength_singleton`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L269).

> Evaluation intertwines the first-order jet with the spacetime derivative:
> the evaluated `∂_lam F_{μν}` is the derivative of the evaluated `F_{μν}`.

```lean
lemma evalPotential_fieldStrength_singleton (A : ElectromagneticPotential 3)
    (hA : ContDiff ℝ 2 A) (lam μ ν : Fin 1 ⊕ Fin 3) :
    evalPotential A (fieldStrength {lam} μ ν) =
      ∂_ lam (evalPotential A (fieldStrength 0 μ ν))
```

**`QED.Photon.JetAlgebra.evalPotential_maxwell_homogeneous`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L291).

> **The homogeneous Maxwell equations** in covariant form,
> `∂_lam F_{μν} + ∂_μ F_{ν lam} + ∂_ν F_{lam μ} = 0`, as the evaluation of the
> formal Bianchi identity of `PhyslibAlpha.Particles.QED.FieldStrength`: Faraday's law and
> the absence of magnetic monopoles are its time–space–space and
> space–space–space components.

```lean
lemma evalPotential_maxwell_homogeneous (A : ElectromagneticPotential 3)
    (hA : ContDiff ℝ 2 A) (lam μ ν : Fin 1 ⊕ Fin 3) :
    ∂_ lam (evalPotential A (fieldStrength 0 μ ν)) +
      ∂_ μ (evalPotential A (fieldStrength 0 ν lam)) +
      ∂_ ν (evalPotential A (fieldStrength 0 lam μ)) = 0
```

## F. D'. The inhomogeneous Maxwell equations and the action principle

> The concrete side (`Physlib.Electromagnetism.Dynamics.IsExtrema`) proves
> variationally that a potential extremises the electromagnetic action exactly
> when `∂_μ F^{μν} = μ₀ J^ν`.  The left-hand side is the evaluation of the
> formal Maxwell operator of `PhyslibAlpha.Particles.QED.Fields`, so the action
> principle can be read entirely through the jet algebra.

**`QED.Photon.JetAlgebra.deriv_const_mul_apply`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L316).

```lean
lemma deriv_const_mul_apply (c : ℝ) {f : SpaceTime 3 → ℝ} (ρ : Fin 1 ⊕ Fin 3)
    (hf : Differentiable ℝ f) (x : SpaceTime 3) :
    ∂_ ρ (fun y => c * f y) x = c * ∂_ ρ f x
```

**`QED.Photon.JetAlgebra.isExtrema_iff_evalPotential_maxwellOperator`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L326).

> **The action principle through the jet algebra**: an electromagnetic
> potential extremises the Maxwell action with source `J` exactly when the
> evaluated formal Maxwell operator equals `μ₀ J` — the inhomogeneous Maxwell
> equations `∂_μ F^{μν} = μ₀ J^ν`.

```lean
lemma isExtrema_iff_evalPotential_maxwellOperator (𝓕 : FreeSpace)
    (A : ElectromagneticPotential 3) (hA : ContDiff ℝ ∞ A)
    (J : LorentzCurrentDensity 3) (hJ : ContDiff ℝ ∞ J) :
    ElectromagneticPotential.IsExtrema 𝓕 A J ↔
      ∀ x ν, evalPotential A (maxwellOperator ν) x = 𝓕.μ₀ * J x ν
```

## G. Compatibility with concrete Lorentz transformations

> The formal Lorentz action of `PhyslibAlpha.Particles.QED.Basic` is matched by the concrete
> action `(Λ • A) x = Λ • A (Λ⁻¹ • x)` of `Physlib.Electromagnetism`:
> evaluating the field strength on the transformed potential is evaluating the
> Lorentz-transformed jet on the original potential at the transformed point.

**`QED.Photon.JetAlgebra.evalPotential_fieldStrength_lorentzAction`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L382).

> **Compatibility of the formal and concrete Lorentz actions**: the
> evaluation of the field strength on `Λ • A` at `x` is the evaluation of its
> formal Lorentz transform on `A` at `Λ⁻¹ • x`, matching the equivariance
> `Physlib.Electromagnetism.Kinematics.FieldStrength.toFieldStrength_equivariant`
> on the concrete side.

```lean
lemma evalPotential_fieldStrength_lorentzAction (Λ : LorentzGroup 3)
    (A : ElectromagneticPotential 3) (hA : Differentiable ℝ A)
    (μ ν : Fin 1 ⊕ Fin 3) (x : SpaceTime 3) :
    evalPotential (Λ • A) (fieldStrength 0 μ ν) x =
      evalPotential A (lorentzAction Λ (fieldStrength 0 μ ν)) (Λ⁻¹ • x)
```

## H. Compatibility with concrete gauge transformations

> The formal gauge invariance of `PhyslibAlpha.Particles.QED.GaugeInvariance` is matched on
> the concrete side: the evaluation of the field strength, and hence of the
> Maxwell term, is unchanged when the potential is replaced by `A + ∂χ`.

**`QED.Photon.JetAlgebra.differentiable_gaugeTransform`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L414).

```lean
lemma differentiable_gaugeTransform {A : ElectromagneticPotential 3} {χ : SpaceTime 3 → ℝ}
    (hA : Differentiable ℝ A) (hχ : ContDiff ℝ 2 χ) :
    Differentiable ℝ (ElectromagneticPotential.gaugeTransform χ A)
```

**`QED.Photon.JetAlgebra.evalPotential_fieldStrength_gaugeTransform`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L422).

> The evaluated field strength is invariant under the concrete gauge
> transformation `A ↦ A + ∂χ`, matching the formal gauge invariance
> `Physlib.Particles.QED.GaugeInvariance.Photon.JetAlgebra.gaugeAction_fieldStrength`.

```lean
lemma evalPotential_fieldStrength_gaugeTransform (A : ElectromagneticPotential 3)
    (χ : SpaceTime 3 → ℝ) (hA : Differentiable ℝ A) (hχ : ContDiff ℝ 2 χ)
    (μ ν : Fin 1 ⊕ Fin 3) (x : SpaceTime 3) :
    evalPotential (ElectromagneticPotential.gaugeTransform χ A) (fieldStrength 0 μ ν) x =
      evalPotential A (fieldStrength 0 μ ν) x
```

**`QED.Photon.JetAlgebra.evalPotential_maxwellTerm_gaugeTransform`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean#L432).

> The Maxwell Lagrangian is gauge invariant, as read off from the jet algebra.

```lean
lemma evalPotential_maxwellTerm_gaugeTransform (A : ElectromagneticPotential 3)
    (χ : SpaceTime 3 → ℝ) (hA : Differentiable ℝ A) (hχ : ContDiff ℝ 2 χ)
    (x : SpaceTime 3) :
    evalPotential (ElectromagneticPotential.gaugeTransform χ A) maxwellTerm x =
      evalPotential A maxwellTerm x
```

## Depends on

- [Extrema of the Lagrangian density](../../../physlib/electromagnetism/dynamics/isextrema.md)
- [Gauge Transformations of the Electromagnetic Potential](../../../physlib/electromagnetism/kinematics/gaugetransformation.md)
- [The fields of quantum electrodynamics](fields.md)

## Proof depends on

- [Properties of the field strength](fieldstrength.md)
- [Lorentz invariance of quantum electrodynamics](lorentzinvariance.md)

## Sources

- [PhyslibAlpha/Particles/QED/Evaluation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Evaluation.lean)
