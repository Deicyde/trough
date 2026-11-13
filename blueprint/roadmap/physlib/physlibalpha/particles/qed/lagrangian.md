---
declaration: module
origin: cited
lean: QED.JetAlgebra.diracKineticTerm, QED.JetAlgebra.diracKineticTermBar, QED.JetAlgebra.electronMassTerm, QED.JetAlgebra.diracCurrent, QED.JetAlgebra.diracEquation, QED.JetAlgebra.diracAdjEquation, QED.JetAlgebra.qedMaxwellEquation, QED.JetAlgebra.lagrangian
statement: formalized
proof: formalized
---

# The QED Lagrangian

The module `PhyslibAlpha.Particles.QED.Lagrangian`, [PhyslibAlpha/Particles/QED/Lagrangian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean): 8 declarations, 8 with a docstring.

## i. Overview

> The Lagrangian of quantum electrodynamics as an element of the QED jet
> algebra:
>
> `L = - 1/4 F_{μν} F^{μν} + i ψ̄ γ^μ D_μ ψ - m ψ̄ ψ`,
>
> with `D_μ ψ = ∂_μ ψ + i e A_μ ψ` the covariant derivative of the electron
> (electric charge `-1`) and the γ matrices taken in the chiral (Weyl)
> representation.  Here `ψ̄` denotes the conjugate jet coordinates `ψ†`; the
> `γ⁰` of `ψ̄ = ψ† γ⁰` is kept explicitly in the contraction matrices
> `γ⁰ γ^μ` and `γ⁰`.
>
> This file contains only definitions; the gauge invariance of every term and
> of the full Lagrangian is proved in `PhyslibAlpha.Particles.QED.GaugeInvariance`.

## ii. Key results

> - `JetAlgebra.diracKineticTerm`, `JetAlgebra.diracKineticTermBar` : the Dirac
>   kinetic terms `i ψ̄ γ^μ D_μ ψ` and `-i (D_μ ψ̄) γ⁰ γ^μ ψ`.
> - `JetAlgebra.electronMassTerm` : the Dirac mass term `ψ̄ ψ`.
> - `JetAlgebra.diracCurrent` : the Dirac current `J^μ = ψ̄ γ^μ ψ`.
> - `JetAlgebra.lagrangian` : the QED Lagrangian.

## iv. References

> The fields are defined in `PhyslibAlpha.Particles.QED.Fields`; gauge invariance is proved in
> `PhyslibAlpha.Particles.QED.GaugeInvariance`.

## A. The Dirac kinetic terms and the mass term

**`QED.JetAlgebra.diracKineticTerm`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L65).

> The Dirac kinetic term `i ψ̄ γ^μ D_μ ψ = i ψ†_α (γ⁰ γ^μ)_{αβ} (D_μ ψ)_β`
> of the electron.

```lean
noncomputable def diracKineticTerm (e : ℝ) : JetAlgebra
```

**`QED.JetAlgebra.diracKineticTermBar`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L71).

> The conjugate Dirac kinetic term
> `-i (D_μ ψ̄) γ⁰ γ^μ ψ = -i (D_μ ψ̄)_α (γ⁰ γ^μ)_{αβ} ψ_β`; the hermitian form
> of the kinetic term is the average of `diracKineticTerm` and this term.

```lean
noncomputable def diracKineticTermBar (e : ℝ) : JetAlgebra
```

**`QED.JetAlgebra.electronMassTerm`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L78).

> The Dirac mass term `ψ̄ ψ = ψ†_α (γ⁰)_{αβ} ψ_β` of the electron.  This is
> the dimension-three term available because the electron is a Dirac fermion:
> its two Weyl components have the same electric charge, so the bilinear
> pairing them against the conjugate components is charge neutral.

```lean
noncomputable def electronMassTerm : JetAlgebra
```

**`QED.JetAlgebra.diracCurrent`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L86).

> The Dirac current `J^μ = ψ̄ γ^μ ψ = ψ†_α (γ⁰ γ^μ)_{αβ} ψ_β` of the
> electron: the Noether current of the `U(1)_em` phase symmetry.  Its coupling
> `- e J^μ A_μ` to the photon is the entire interaction of QED — this is the
> jet-algebra counterpart of the current coupling of
> `Physlib.Electromagnetism.Dynamics`; see `PhyslibAlpha.Particles.QED.CurrentCoupling`.

```lean
noncomputable def diracCurrent (μ : Fin 1 ⊕ Fin 3) : JetAlgebra
```

## B. The QED Lagrangian

## C. B'. The equations of motion

> The Euler–Lagrange equations of the QED Lagrangian, as elements of the jet
> algebra whose vanishing expresses the equations of motion.  Deriving them
> *variationally* from `lagrangian` requires a variational calculus on the jet
> algebra, which is future work; here they are definitions, and
> `PhyslibAlpha.Particles.QED.CurrentCoupling` proves the Noether identity that the
> divergence of the Dirac current is a combination of them.

**`QED.JetAlgebra.diracEquation`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L110).

> The Dirac-equation element `γ⁰ (i γ^μ D_μ - m) ψ`, row `α`: its vanishing
> is the interacting Dirac equation.

```lean
noncomputable def diracEquation (e m : ℝ) (α : Fin 2 ⊕ Fin 2) : JetAlgebra
```

**`QED.JetAlgebra.diracAdjEquation`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L116).

> The adjoint Dirac-equation element `i (D_μ ψ̄) γ⁰ γ^μ + m ψ̄ γ⁰`,
> column `β`: its vanishing is the interacting adjoint Dirac equation.

```lean
noncomputable def diracAdjEquation (e m : ℝ) (β : Fin 2 ⊕ Fin 2) : JetAlgebra
```

> …

> …

> …

> …

> …

> …

> …

> …

**`QED.JetAlgebra.qedMaxwellEquation`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L131).

> The QED Maxwell-equation element `∂_μ F^{μν} - e J^ν`: its vanishing is
> the inhomogeneous Maxwell equation sourced by the Dirac current.

```lean
noncomputable def qedMaxwellEquation (e : ℝ) (ν : Fin 1 ⊕ Fin 3) : JetAlgebra
```

**`QED.JetAlgebra.lagrangian`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean#L141).

> The QED Lagrangian
> `L = - 1/4 F_{μν} F^{μν} + i ψ̄ γ^μ D_μ ψ - m ψ̄ ψ`
> with electric coupling `e` and electron mass `m`, as an element of the QED
> jet algebra.  Evaluated on an honest electromagnetic potential, the first
> term is the Maxwell Lagrangian of `Physlib.Electromagnetism`; see
> `PhyslibAlpha.Particles.QED.Evaluation`.

```lean
noncomputable def lagrangian (e m : ℝ) : JetAlgebra
```

## Depends on

- [The fields of quantum electrodynamics](fields.md)

## Sources

- [PhyslibAlpha/Particles/QED/Lagrangian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/Lagrangian.lean)
