---
declaration: module
origin: cited
lean: QED.JetAlgebra.A_mul_diracCurrent, QED.JetAlgebra.diracKineticTerm_eq_free_add_current, QED.JetAlgebra.gaugeAction_diracCurrent, QED.JetAlgebra.current_conservation
statement: formalized
proof: formalized
---

# The current coupling of quantum electrodynamics

The module `PhyslibAlpha.Particles.QED.CurrentCoupling`, [PhyslibAlpha/Particles/QED/CurrentCoupling.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/CurrentCoupling.lean): 4 declarations, 4 with a docstring.

## i. Overview

> The interaction of QED is *minimal coupling to the Dirac current*: expanding
> the covariant derivative inside the Dirac kinetic term,
>
> `i ψ̄ γ^μ D_μ ψ = i ψ̄ γ^μ ∂_μ ψ - e J^μ A_μ`  with  `J^μ = ψ̄ γ^μ ψ`.
>
> This is the jet-algebra counterpart of the current coupling `J^μ A_μ` of
> `Physlib.Electromagnetism.Dynamics.Lagrangian`: the photon couples to matter
> only through a conserved current contracted with the potential, with the
> electron supplying `J^μ = ψ̄ γ^μ ψ`.
>
> The current is gauge invariant (`gaugeAction_diracCurrent`) — the electron
> and its conjugate carry opposite charges, so the phases cancel — which is
> what makes it a physically meaningful source for the photon.
>
> This file contains no definitions, only theorems about the fields of
> `PhyslibAlpha.Particles.QED.Fields` and the Lagrangian of `PhyslibAlpha.Particles.QED.Lagrangian`.

## ii. Key results

> - `JetAlgebra.diracKineticTerm_eq_free_add_current` : **minimal coupling** —
>   the Dirac kinetic term is the free kinetic term plus `- e J^μ A_μ`.
> - `JetAlgebra.gaugeAction_diracCurrent` : the Dirac current is gauge
>   invariant.

## iv. References

> The current is defined in `PhyslibAlpha.Particles.QED.Lagrangian`; the concrete
> electromagnetic current coupling is
> `Physlib.Electromagnetism.Dynamics.Lagrangian`.

> …

## A. The minimal-coupling decomposition of the kinetic term

> The photon coordinates commute with the fermion coordinates
> (`PhyslibAlpha.Particles.QED.FermionStatistics`), so the interaction inside the kinetic term
> reorganises into the potential times the Dirac current.

**`QED.JetAlgebra.A_mul_diracCurrent`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/CurrentCoupling.lean#L76).

> The photon potential times the Dirac current, written through the fermion
> bilinears.

```lean
lemma A_mul_diracCurrent (μ : Fin 1 ⊕ Fin 3) :
    A 0 μ * diracCurrent μ =
      ∑ α, ∑ β, kineticGamma μ α β • (A 0 μ * (barψ 0 α * ψ 0 β))
```

**`QED.JetAlgebra.diracKineticTerm_eq_free_add_current`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/CurrentCoupling.lean#L90).

> **Minimal coupling**: the Dirac kinetic term with coupling `e` is the free
> Dirac kinetic term plus the current coupling `- e J^μ A_μ`.  All of the
> interaction of QED is the photon contracted with the Dirac current, the
> jet-algebra counterpart of the current coupling of
> `Physlib.Electromagnetism.Dynamics`.

```lean
lemma diracKineticTerm_eq_free_add_current (e : ℝ) :
    diracKineticTerm e = diracKineticTerm 0 +
      (-e : ℂ) • ∑ μ, A 0 μ * diracCurrent μ
```

## B. Gauge invariance of the Dirac current

**`QED.JetAlgebra.gaugeAction_diracCurrent`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/CurrentCoupling.lean#L128).

> **The Dirac current is gauge invariant**: the electron and its conjugate
> carry opposite charges, so the phases cancel by unitarity.  This is what
> makes `J^μ` a physically meaningful source for the photon.

```lean
lemma gaugeAction_diracCurrent {e : ℝ} (g : GaugeJet e) (μ : Fin 1 ⊕ Fin 3) :
    gaugeAction g (diracCurrent μ) = diracCurrent μ
```

## C. Noether: conservation of the Dirac current on-shell

**`QED.JetAlgebra.current_conservation`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/CurrentCoupling.lean#L151).

> **Noether's identity for the Dirac current**: the divergence of the
> current is a combination of the Dirac-equation elements,
> `i ∂_μ J^μ = ψ̄ ⬝ (Dirac eq) + (adjoint Dirac eq) ⬝ ψ`.
> On solutions of the Dirac equations the current is conserved,
> `∂_μ J^μ = 0` — for every coupling `e` and mass `m`: the gauge interaction
> and the mass drop out of the divergence identically.

```lean
lemma current_conservation (e m : ℝ) :
    Complex.I • ∑ μ, jetDeriv μ (diracCurrent μ) =
      ∑ α, barψ 0 α * diracEquation e m α +
        ∑ β, diracAdjEquation e m β * ψ 0 β
```

## Depends on

- [The QED Lagrangian](lagrangian.md)

## Proof depends on

- [Spin-statistics of the QED fields](fermionstatistics.md)
- [Properties of the field strength](fieldstrength.md)

## Sources

- [PhyslibAlpha/Particles/QED/CurrentCoupling.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/CurrentCoupling.lean)
