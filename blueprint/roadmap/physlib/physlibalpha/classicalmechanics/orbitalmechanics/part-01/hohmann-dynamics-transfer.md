---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.incoming, ClassicalMechanics.HohmannTransfer.outgoingPhase, ClassicalMechanics.HohmannTransfer.outgoing, ClassicalMechanics.HohmannTransfer.flight, ClassicalMechanics.HohmannTransfer.incoming_deriv, ClassicalMechanics.HohmannTransfer.outgoing_deriv, ClassicalMechanics.HohmannTransfer.incoming_newton, ClassicalMechanics.HohmannTransfer.outgoing_newton
statement: formalized
proof: formalized
---

# Joining the Hohmann coast to circular orbits

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Transfer`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean): 21 declarations, 4 with a docstring.

> The incoming circle, transfer ellipse and outgoing circle share the burn positions.

## i. Overview

> Each coast is defined on all real times. The flight uses them on successive intervals, with the
> positions matched at the two impulses and velocities allowed to jump.

## ii. Key results

> - `junction_velocity_jumps` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Coast arcs and their junctions

**`ClassicalMechanics.HohmannTransfer.incoming`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L43).

> The inner circular coast before the departure impulse.

```lean
def incoming (p : Parameters) (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.outgoingPhase`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L45).

> The phase that places the outer circular orbit at the arrival apsis.

```lean
def outgoingPhase (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.outgoing`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L47).

> The outer circular coast after the arrival impulse.

```lean
def outgoing (p : Parameters) (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.flight`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L50).

> The position throughout the two circular coasts and the transfer coast.

```lean
def flight (p : Parameters) (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.incoming_deriv`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L53).

```lean
lemma incoming_deriv (p : Parameters) (t : ℝ) :
    deriv (incoming p) t = circularVelocity p.mu p.r₁ 0 t
```

**`ClassicalMechanics.HohmannTransfer.outgoing_deriv`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L56).

```lean
lemma outgoing_deriv (p : Parameters) (t : ℝ) :
    deriv (outgoing p) t = circularVelocity p.mu p.r₂ (outgoingPhase p) t
```

**`ClassicalMechanics.HohmannTransfer.incoming_newton`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L59).

```lean
lemma incoming_newton (p : Parameters) (t : ℝ) :
    deriv (deriv (incoming p)) t = -(p.mu/‖incoming p t‖^3) • incoming p t
```

**`ClassicalMechanics.HohmannTransfer.outgoing_newton`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L62).

```lean
lemma outgoing_newton (p : Parameters) (t : ℝ) :
    deriv (deriv (outgoing p)) t = -(p.mu/‖outgoing p t‖^3) • outgoing p t
```

**`ClassicalMechanics.HohmannTransfer.incoming_radius`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L65).

```lean
lemma incoming_radius (p : Parameters) (t : ℝ) : ‖incoming p t‖ = p.r₁
```

**`ClassicalMechanics.HohmannTransfer.outgoing_radius`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L67).

```lean
lemma outgoing_radius (p : Parameters) (t : ℝ) : ‖outgoing p t‖ = p.r₂
```

**`ClassicalMechanics.HohmannTransfer.incoming_zero`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L69).

```lean
lemma incoming_zero (p : Parameters) : incoming p 0 = pack p.r₁ 0
```

**`ClassicalMechanics.HohmannTransfer.outgoing_angle`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L71).

```lean
lemma outgoing_angle (p : Parameters) :
    circularRate p.mu p.r₂*p.transferTime + outgoingPhase p = Real.pi
```

**`ClassicalMechanics.HohmannTransfer.outgoing_arrival`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L75).

```lean
lemma outgoing_arrival (p : Parameters) :
    outgoing p p.transferTime = pack (-p.r₂) 0
```

**`ClassicalMechanics.HohmannTransfer.incoming_velocity_zero`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L78).

```lean
lemma incoming_velocity_zero (p : Parameters) :
    deriv (incoming p) 0 = pack 0 (circularSpeed p.mu p.r₁)
```

**`ClassicalMechanics.HohmannTransfer.outgoing_velocity_arrival`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L82).

```lean
lemma outgoing_velocity_arrival (p : Parameters) :
    deriv (outgoing p) p.transferTime = pack 0 (-circularSpeed p.mu p.r₂)
```

**`ClassicalMechanics.HohmannTransfer.junction_positions`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L87).

```lean
lemma junction_positions (p : Parameters) :
    incoming p 0 = position p 0 ∧
      position p p.transferTime = outgoing p p.transferTime
```

**`ClassicalMechanics.HohmannTransfer.junction_velocity_jumps`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L90).

```lean
lemma junction_velocity_jumps (p : Parameters) :
    deriv (position p) 0 - deriv (incoming p) 0 = entryImpulse p ∧
    deriv (outgoing p) p.transferTime - deriv (position p) p.transferTime = exitImpulse p
```

**`ClassicalMechanics.HohmannTransfer.flight_before`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L95).

```lean
lemma flight_before (p : Parameters) {t : ℝ} (ht : t < 0) :
    flight p t = incoming p t
```

**`ClassicalMechanics.HohmannTransfer.flight_transfer`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L97).

```lean
lemma flight_transfer (p : Parameters) {t : ℝ} (ht : t ∈ Set.Icc 0 p.transferTime) :
    flight p t = position p t
```

**`ClassicalMechanics.HohmannTransfer.flight_after`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L99).

```lean
lemma flight_after (p : Parameters) {t : ℝ} (ht : p.transferTime < t) :
    flight p t = outgoing p t
```

**`ClassicalMechanics.HohmannTransfer.apsidal_parameters_unique`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean#L103).

```lean
lemma apsidal_parameters_unique (p : Parameters) {A E : ℝ}
    (_hA : 0 < A) (h₁ : A*(1-E)=p.r₁) (h₂ : A*(1+E)=p.r₂) :
    A = p.a ∧ E = p.e
```

## Depends on

- [The two Hohmann velocity impulses](hohmann-dynamics-impulses.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Transfer.lean)
