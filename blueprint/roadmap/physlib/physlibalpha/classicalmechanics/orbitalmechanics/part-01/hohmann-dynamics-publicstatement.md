---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.hohmann_transfer, ClassicalMechanics.HohmannTransfer.exists_hohmann_transfer
statement: formalized
proof: formalized
---

# Existence of an outward Hohmann transfer

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.PublicStatement`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/PublicStatement.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/PublicStatement.lean): 2 declarations, 2 with a docstring.

> Two positive ordered radii admit a tangential two-impulse transfer.

## i. Overview

> The explicit ellipse joins two prograde circles at its apses. The statement exposes the time
> derivatives, Newtonian equations, velocity jump norms, and transfer time in terms of the input
> data.

## ii. Key results

> - `exists_hohmann_transfer` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Existence and physical transfer identities

**`ClassicalMechanics.HohmannTransfer.hohmann_transfer`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/PublicStatement.lean#L43).

> The explicit outward transfer satisfies the Newtonian equations and burn identities.

```lean
lemma hohmann_transfer (p : Parameters) :
    0 < p.transferTime ∧
    (∀ t, deriv (deriv (position p)) t =
      -(p.mu/‖position p t‖^3) • position p t) ∧
    (∀ t, p.r₁ ≤ ‖position p t‖ ∧ ‖position p t‖ ≤ p.r₂) ∧
    position p 0 = pack p.r₁ 0 ∧
    position p p.transferTime = pack (-p.r₂) 0 ∧
    deriv (position p) 0 = pack 0 (periSpeed p) ∧
    deriv (position p) p.transferTime = pack 0 (-apoSpeed p) ∧
    incoming p 0 = position p 0 ∧
    position p p.transferTime = outgoing p p.transferTime ∧
    (∀ t, deriv (deriv (incoming p)) t =
      -(p.mu/‖incoming p t‖^3) • incoming p t) ∧
    (∀ t, deriv (deriv (outgoing p)) t =
      -(p.mu/‖outgoing p t‖^3) • outgoing p t) ∧
    ‖deriv (position p) 0-deriv (incoming p) 0‖ = deltaV₁ p ∧
    ‖deriv (outgoing p) p.transferTime-deriv (position p) p.transferTime‖ = deltaV₂ p ∧
    0 < deltaV₁ p ∧ 0 < deltaV₂ p ∧
    deltaV₁ p = Real.sqrt (p.mu/p.r₁)*(Real.sqrt (2*p.r₂/(p.r₁+p.r₂))-1) ∧
    deltaV₂ p = Real.sqrt (p.mu/p.r₂)*(1-Real.sqrt (2*p.r₁/(p.r₁+p.r₂))) ∧
    p.transferTime = Real.pi*Real.sqrt (p.a^3/p.mu) ∧
    (∀ t, specificEnergy p.mu (position p t) (deriv (position p) t) = -p.mu/(2*p.a)) ∧
    (∀ t, cross (position p t) (deriv (position p) t) = p.a*p.b*p.n)
```

**`ClassicalMechanics.HohmannTransfer.exists_hohmann_transfer`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/PublicStatement.lean#L79).

> Existence without asking the reader to trust a project-defined orbit predicate.
> All geometric and motion hypotheses are consequences, not input fields.

```lean
lemma exists_hohmann_transfer (mu r₁ r₂ : ℝ)
    (hmu : 0 < mu) (hr₁ : 0 < r₁) (horder : r₁ < r₂) :
    ∃ (q v c₁ c₂ : ℝ → ℂ) (τ d₁ d₂ : ℝ),
      0 < τ ∧ 0 < d₁ ∧ 0 < d₂ ∧
      (∀ t, HasDerivAt q (v t) t) ∧
      (∀ t, HasDerivAt v (-(mu/‖q t‖^3) • q t) t) ∧
      (∀ t, deriv (deriv q) t = -(mu/‖q t‖^3) • q t) ∧
      (∀ t, r₁ ≤ ‖q t‖ ∧ ‖q t‖ ≤ r₂) ∧
      q 0 = pack r₁ 0 ∧ q τ = pack (-r₂) 0 ∧
      (∀ t, ‖c₁ t‖ = r₁) ∧ (∀ t, ‖c₂ t‖ = r₂) ∧
      (∀ t, deriv (deriv c₁) t = -(mu/‖c₁ t‖^3) • c₁ t) ∧
      (∀ t, deriv (deriv c₂) t = -(mu/‖c₂ t‖^3) • c₂ t) ∧
      c₁ 0 = q 0 ∧ q τ = c₂ τ ∧
      v 0-deriv c₁ 0 = pack 0 d₁ ∧
      deriv c₂ τ-v τ = pack 0 (-d₂) ∧
      ‖v 0-deriv c₁ 0‖ = d₁ ∧ ‖deriv c₂ τ-v τ‖ = d₂ ∧
      d₁ = Real.sqrt (mu/r₁)*(Real.sqrt (2*r₂/(r₁+r₂))-1) ∧
      d₂ = Real.sqrt (mu/r₂)*(1-Real.sqrt (2*r₁/(r₁+r₂))) ∧
      τ = Real.pi*Real.sqrt (((r₁+r₂)/2)^3/mu)
```

## Depends on

- [Mechanical invariants of the Hohmann ellipse](hohmann-dynamics-invariants.md)
- [Joining the Hohmann coast to circular orbits](hohmann-dynamics-transfer.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/PublicStatement.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/PublicStatement.lean)
