---
declaration: module
origin: cited
lean: QED.Photon.JetAlgebra.gaugeAction_comp, QED.Photon.JetAlgebra.gaugeAction_zero, QED.Photon.JetAlgebra.gaugeAction_fieldStrength, QED.Photon.JetAlgebra.gaugeAction_maxwellTerm, QED.Electron.JetAlgebra.gaugeAction_trivial, QED.JetAlgebra.gaugeAction_trivial, QED.Electron.JetAlgebra.gaugeAction_mul, QED.JetAlgebra.gaugeActionPhoton_comp
statement: formalized
proof: formalized
---

# Gauge invariance of quantum electrodynamics

The module `PhyslibAlpha.Particles.QED.GaugeInvariance`, [PhyslibAlpha/Particles/QED/GaugeInvariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean): 24 declarations, 11 with a docstring.

## i. Overview

> The gauge-theoretic theorems of QED, culminating in the gauge invariance of
> the QED Lagrangian, `gaugeAction_lagrangian`.  The chain of results
> decomposes exactly as in the physics texts:
>
> * on the photon jet algebra the gauge transformations form a group acting by
>   affine shifts (`Photon.JetAlgebra.gaugeAction_comp`), and the field
>   strength and the Maxwell term are invariant because the shift of `∂_s A_μ`
>   is symmetric in the derivative indices — Clairaut's theorem is built into
>   the multiset indexing (`Photon.JetAlgebra.gaugeAction_fieldStrength`);
> * the electron coordinates rotate by the phase and its conjugate, and the
>   trivial gauge jet acts trivially (`Electron.JetAlgebra.gaugeAction_trivial`);
> * the covariant derivative is covariant, `D_μ ψ ↦ ū D_μ ψ`, because the
>   photon shift `∂_μ χ` cancels the derivative `∂_μ ū = -i e (∂_μ χ) ū` of
>   the phase (`gaugeAction_covDψ`);
> * every charge-neutral fermion bilinear is invariant because the phases of
>   the electron and its conjugate cancel by unitarity
>   (`gaugeAction_mul_phase_cancel`);
> * the Lagrangian, being built from invariant pieces, is invariant
>   (`gaugeAction_lagrangian`).
>
> This file contains no definitions, only theorems about the jet algebras of
> `PhyslibAlpha.Particles.QED.Basic`, the fields of `PhyslibAlpha.Particles.QED.Fields`
> and the Lagrangian of
> `PhyslibAlpha.Particles.QED.Lagrangian`.

## ii. Key results

> - `Photon.JetAlgebra.gaugeAction_comp`, `Photon.JetAlgebra.gaugeAction_zero` :
>   the photon gauge transformations form a group acting on the photon jet
>   algebra.
> - `Photon.JetAlgebra.gaugeAction_fieldStrength`,
>   `Photon.JetAlgebra.gaugeAction_maxwellTerm` : gauge invariance of the field
>   strength and the Maxwell term.
> - `Electron.JetAlgebra.gaugeAction_trivial`, `JetAlgebra.gaugeAction_trivial` :
>   the trivial gauge jet acts trivially.
> - `JetAlgebra.gaugeAction_A`, `JetAlgebra.gaugeAction_ψ_zero`,
>   `JetAlgebra.gaugeAction_ψ_singleton` (and the `barψ` versions) : the action
>   on the jet coordinates of QED.
> - `JetAlgebra.gaugeAction_covDψ`, `JetAlgebra.gaugeAction_covDbarψ` : gauge
>   covariance of the covariant derivatives.
> - `JetAlgebra.gaugeAction_diracKineticTerm`,
>   `JetAlgebra.gaugeAction_electronMassTerm` : gauge invariance of the terms
>   of the Lagrangian.
> - `JetAlgebra.gaugeAction_lagrangian` : **gauge invariance of the QED
>   Lagrangian**.

## iv. References

> The jet algebras and gauge actions are defined in `PhyslibAlpha.Particles.QED.Basic`, the
> fields in `PhyslibAlpha.Particles.QED.Fields` and the Lagrangian in
> `PhyslibAlpha.Particles.QED.Lagrangian`.

## A. The gauge group acting on the photon jet algebra

**`QED.Photon.JetAlgebra.gaugeAction_comp`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L101).

> Photon gauge jets compose by addition: the gauge transformations form a
> group acting on the photon jet algebra.

```lean
lemma gaugeAction_comp (c₁ c₂ : GaugeJet) :
    (gaugeAction c₁).comp (gaugeAction c₂) = gaugeAction (c₁ + c₂)
```

**`QED.Photon.JetAlgebra.gaugeAction_zero`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L112).

```lean
lemma gaugeAction_zero : gaugeAction 0 = AlgHom.id ℝ JetAlgebra
```

### A.1. Gauge invariance of the field strength and the Maxwell term

> The field strength is gauge invariant, and the reason is exactly that
> multiset addition is commutative: the two shifts are `∂_s ∂_μ ∂_ν χ` and
> `∂_s ∂_ν ∂_μ χ`, indexed by `s + {μ} + {ν}` and `s + {ν} + {μ}`.  Clairaut's
> lemma is built into the indexing.

**`QED.Photon.JetAlgebra.gaugeAction_fieldStrength`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L130).

```lean
lemma gaugeAction_fieldStrength (c : GaugeJet) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ ν : Fin 1 ⊕ Fin 3) :
    gaugeAction c (fieldStrength s μ ν) = fieldStrength s μ ν
```

**`QED.Photon.JetAlgebra.gaugeAction_maxwellTerm`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L139).

```lean
lemma gaugeAction_maxwellTerm (c : GaugeJet) : gaugeAction c maxwellTerm = maxwellTerm
```

## B. The trivial gauge jet acts trivially

> The key combinatorial fact: in the Leibniz sum over the antidiagonal of `t`,
> the splitting `(0, t)` occurs exactly once, so an indicator supported at the
> zero multiset picks out the identity.

**`QED.Electron.JetAlgebra.gaugeAction_trivial`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L166).

> The trivial gauge jet acts trivially on the electron jet algebra: the
> gauge action is unital.

```lean
lemma gaugeAction_trivial (e : ℝ) :
    gaugeAction (GaugeJet.trivial e) = AlgHom.id ℂ JetAlgebra
```

**`QED.JetAlgebra.gaugeAction_trivial`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L202).

> The trivial gauge jet acts trivially on the QED jet algebra: the gauge
> action is unital.

```lean
lemma gaugeAction_trivial (e : ℝ) :
    gaugeAction (GaugeJet.trivial e) = AlgHom.id ℂ JetAlgebra
```

**`QED.Electron.JetAlgebra.gaugeAction_mul`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L212).

> The electron gauge actions compose through the monoid of gauge jets.

```lean
lemma _root_.QED.Electron.JetAlgebra.gaugeAction_mul {e : ℝ} (g₁ g₂ : GaugeJet e) :
    (Electron.JetAlgebra.gaugeAction g₁).comp (Electron.JetAlgebra.gaugeAction g₂) =
      Electron.JetAlgebra.gaugeAction (g₁ * g₂)
```

**`QED.JetAlgebra.gaugeActionPhoton_comp`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L277).

> The complexified photon gauge actions compose by addition of the gauge
> jets.

```lean
lemma gaugeActionPhoton_comp (c₁ c₂ : Photon.JetAlgebra.GaugeJet) :
    (gaugeActionPhoton c₁).comp (gaugeActionPhoton c₂) =
      gaugeActionPhoton (c₁ + c₂)
```

**`QED.JetAlgebra.gaugeAction_mul`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L286).

> **The gauge actions compose through the monoid of gauge jets**: the QED
> gauge action is a monoid action on the jet algebra.

```lean
lemma gaugeAction_mul {e : ℝ} (g₁ g₂ : GaugeJet e) :
    (gaugeAction g₁).comp (gaugeAction g₂) = gaugeAction (g₁ * g₂)
```

**`QED.JetAlgebra.gaugeAction_mul_apply`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L292).

```lean
lemma gaugeAction_mul_apply {e : ℝ} (g₁ g₂ : GaugeJet e) (x : JetAlgebra) :
    gaugeAction (g₁ * g₂) x = gaugeAction g₁ (gaugeAction g₂ x)
```

## C. The action on the jet coordinates of QED

### C.1. The photon coordinates

> The photon coordinate shifts by a *constant* of the jet algebra, the jet
> `∂_s ∂_μ χ` of the gauge function; in the full algebra the constant is the
> scalar multiple `(∂_s ∂_μ χ) • 1`.

**`QED.JetAlgebra.gaugeAction_A`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L310).

> The gauge action on the photon jet coordinate: the affine shift
> `∂_s A_μ ↦ ∂_s A_μ + ∂_s ∂_μ χ`.

```lean
lemma gaugeAction_A {e : ℝ} (g : GaugeJet e) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) :
    gaugeAction g (A s μ) = A s μ + (g.χjet (s + {μ}) : ℂ) • 1
```

### C.2. The electron coordinates

> The electron (charge `-1`) rotates by the conjugate phase, its conjugate
> (charge `+1`) by the phase; on first-order jets the Leibniz rule feeds the
> first derivative of the phase into the zeroth-order coordinate.

**`QED.JetAlgebra.gaugeAction_ψ_zero`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L329).

```lean
lemma gaugeAction_ψ_zero {e : ℝ} (g : GaugeJet e) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ψ 0 α) = star (g.phase 0) • ψ 0 α
```

**`QED.JetAlgebra.gaugeAction_barψ_zero`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L336).

```lean
lemma gaugeAction_barψ_zero {e : ℝ} (g : GaugeJet e) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (barψ 0 α) = g.phase 0 • barψ 0 α
```

**`QED.JetAlgebra.gaugeAction_ψ_singleton`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L342).

```lean
lemma gaugeAction_ψ_singleton {e : ℝ} (g : GaugeJet e) (μ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ψ {μ} α) =
      star (g.phase 0) • ψ {μ} α + star (g.phase {μ}) • ψ 0 α
```

**`QED.JetAlgebra.gaugeAction_barψ_singleton`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L351).

```lean
lemma gaugeAction_barψ_singleton {e : ℝ} (g : GaugeJet e) (μ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (barψ {μ} α) =
      g.phase 0 • barψ {μ} α + g.phase {μ} • barψ 0 α
```

### C.3. The field strength and the Maxwell term

> Both invariances are inherited from the photon jet algebra, where the proof
> is the commutativity of multiset addition.

**`QED.JetAlgebra.gaugeAction_fieldStrength`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L370).

```lean
lemma gaugeAction_fieldStrength {e : ℝ} (g : GaugeJet e)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    gaugeAction g (fieldStrength s μ ν) = fieldStrength s μ ν
```

**`QED.JetAlgebra.gaugeAction_maxwellTerm`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L378).

```lean
lemma gaugeAction_maxwellTerm {e : ℝ} (g : GaugeJet e) :
    gaugeAction g maxwellTerm = maxwellTerm
```

## D. Gauge covariance of the covariant derivatives

> Under a gauge transformation the photon coordinate shifts by `∂_μ χ` while
> the first-order electron coordinate picks up the derivative
> `∂_μ ū = -i e (∂_μ χ) ū` of the phase by the Leibniz rule; the two
> contributions cancel and the covariant derivative rotates like the field
> itself.

**`QED.JetAlgebra.gaugeAction_covDψ`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L399).

> **Gauge covariance of the covariant derivative**: `D_μ ψ` rotates by the
> conjugate phase, exactly like `ψ` itself.  The shift of the photon
> coordinate cancels the derivative of the phase.

```lean
lemma gaugeAction_covDψ {e : ℝ} (g : GaugeJet e) (μ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (covDψ e μ α) = star (g.phase 0) • covDψ e μ α
```

**`QED.JetAlgebra.gaugeAction_covDbarψ`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L411).

> Gauge covariance of the conjugate covariant derivative: `D_μ ψ̄` rotates
> by the phase, exactly like `ψ̄` itself.

```lean
lemma gaugeAction_covDbarψ {e : ℝ} (g : GaugeJet e) (μ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (covDbarψ e μ α) = g.phase 0 • covDbarψ e μ α
```

## E. Gauge invariance of the Lagrangian

### E.1. Cancellation of the phases in fermion bilinears

**`QED.JetAlgebra.gaugeAction_mul_phase_cancel`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L433).

> A product of a factor rotating by the phase and a factor rotating by the
> conjugate phase is gauge invariant: the phases cancel by unitarity.  This is
> the reason every charge-neutral fermion bilinear of QED is gauge
> invariant.

```lean
lemma gaugeAction_mul_phase_cancel {e : ℝ} (g : GaugeJet e) {x y : JetAlgebra}
    (hx : gaugeAction g x = g.phase 0 • x)
    (hy : gaugeAction g y = star (g.phase 0) • y) :
    gaugeAction g (x * y) = x * y
```

### E.2. Invariance of each term

**`QED.JetAlgebra.gaugeAction_diracKineticTerm`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L446).

```lean
lemma gaugeAction_diracKineticTerm {e : ℝ} (g : GaugeJet e) :
    gaugeAction g (diracKineticTerm e) = diracKineticTerm e
```

**`QED.JetAlgebra.gaugeAction_diracKineticTermBar`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L460).

```lean
lemma gaugeAction_diracKineticTermBar {e : ℝ} (g : GaugeJet e) :
    gaugeAction g (diracKineticTermBar e) = diracKineticTermBar e
```

**`QED.JetAlgebra.gaugeAction_electronMassTerm`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L474).

```lean
lemma gaugeAction_electronMassTerm {e : ℝ} (g : GaugeJet e) :
    gaugeAction g electronMassTerm = electronMassTerm
```

### E.3. Invariance of the QED Lagrangian

**`QED.JetAlgebra.gaugeAction_lagrangian`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean#L494).

> **Gauge invariance of the QED Lagrangian.**  The Maxwell term is invariant
> by the symmetry of the photon shift in its derivative indices, the kinetic
> term by the covariance of the covariant derivative, and the mass term by the
> unitarity of the phase.

```lean
lemma gaugeAction_lagrangian {e : ℝ} (g : GaugeJet e) (m : ℝ) :
    gaugeAction g (lagrangian e m) = lagrangian e m
```

## Depends on

- [The QED Lagrangian](lagrangian.md)

## Sources

- [PhyslibAlpha/Particles/QED/GaugeInvariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/GaugeInvariance.lean)
