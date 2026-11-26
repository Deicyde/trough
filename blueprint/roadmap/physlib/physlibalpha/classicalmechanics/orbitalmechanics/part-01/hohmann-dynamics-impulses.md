---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.deltaV₁, ClassicalMechanics.HohmannTransfer.deltaV₂, ClassicalMechanics.HohmannTransfer.totalDeltaV, ClassicalMechanics.HohmannTransfer.entryImpulse, ClassicalMechanics.HohmannTransfer.exitImpulse, ClassicalMechanics.HohmannTransfer.peri_excess_sq, ClassicalMechanics.HohmannTransfer.apo_deficit_sq, ClassicalMechanics.HohmannTransfer.deltaV₁_pos
statement: formalized
proof: formalized
---

# The two Hohmann velocity impulses

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Impulses`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean): 20 declarations, 5 with a docstring.

> The velocity jumps match the transfer ellipse to the circles.

## i. Overview

> The two velocity jumps are tangential. Their magnitudes are the speed excess at departure and the
> speed deficit at arrival. At the opposite apsis the prograde direction is the negative imaginary
> axis.

## ii. Key results

> - `totalDeltaV_eq_sum_norms` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Vector jumps and their magnitudes

**`ClassicalMechanics.HohmannTransfer.deltaV₁`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L44).

> The magnitude of the departure velocity impulse.

```lean
def deltaV₁ (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.deltaV₂`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L46).

> The magnitude of the arrival velocity impulse.

```lean
def deltaV₂ (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.totalDeltaV`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L48).

> The sum of the departure and arrival impulse magnitudes.

```lean
def totalDeltaV (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.entryImpulse`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L50).

> The change in velocity from the inner circle to the ellipse.

```lean
def entryImpulse (p : Parameters) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.exitImpulse`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L53).

> The change in velocity from the ellipse to the outer circle.

```lean
def exitImpulse (p : Parameters) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.peri_excess_sq`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L56).

```lean
lemma peri_excess_sq (p : Parameters) :
    periSpeed p ^ 2 - circularSpeed p.mu p.r₁ ^ 2 =
      p.mu*(p.r₂-p.r₁)/(p.r₁*(p.r₁+p.r₂))
```

**`ClassicalMechanics.HohmannTransfer.apo_deficit_sq`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L62).

```lean
lemma apo_deficit_sq (p : Parameters) :
    circularSpeed p.mu p.r₂ ^ 2 - apoSpeed p ^ 2 =
      p.mu*(p.r₂-p.r₁)/(p.r₂*(p.r₁+p.r₂))
```

**`ClassicalMechanics.HohmannTransfer.deltaV₁_pos`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L68).

```lean
lemma deltaV₁_pos (p : Parameters) : 0 < deltaV₁ p
```

**`ClassicalMechanics.HohmannTransfer.deltaV₂_pos`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L76).

```lean
lemma deltaV₂_pos (p : Parameters) : 0 < deltaV₂ p
```

**`ClassicalMechanics.HohmannTransfer.totalDeltaV_pos`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L84).

```lean
lemma totalDeltaV_pos (p : Parameters) : 0 < totalDeltaV p
```

**`ClassicalMechanics.HohmannTransfer.periSpeed_factorized`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L86).

```lean
lemma periSpeed_factorized (p : Parameters) :
    periSpeed p = circularSpeed p.mu p.r₁ * Real.sqrt (2*p.r₂/(p.r₁+p.r₂))
```

**`ClassicalMechanics.HohmannTransfer.apoSpeed_factorized`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L100).

```lean
lemma apoSpeed_factorized (p : Parameters) :
    apoSpeed p = circularSpeed p.mu p.r₂ * Real.sqrt (2*p.r₁/(p.r₁+p.r₂))
```

**`ClassicalMechanics.HohmannTransfer.deltaV₁_formula`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L114).

```lean
lemma deltaV₁_formula (p : Parameters) :
    deltaV₁ p = Real.sqrt (p.mu/p.r₁) *
      (Real.sqrt (2*p.r₂/(p.r₁+p.r₂))-1)
```

**`ClassicalMechanics.HohmannTransfer.deltaV₂_formula`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L120).

```lean
lemma deltaV₂_formula (p : Parameters) :
    deltaV₂ p = Real.sqrt (p.mu/p.r₂) *
      (1-Real.sqrt (2*p.r₁/(p.r₁+p.r₂)))
```

**`ClassicalMechanics.HohmannTransfer.entryImpulse_eq`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L126).

```lean
lemma entryImpulse_eq (p : Parameters) : entryImpulse p = pack 0 (deltaV₁ p)
```

**`ClassicalMechanics.HohmannTransfer.exitImpulse_eq`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L129).

```lean
lemma exitImpulse_eq (p : Parameters) : exitImpulse p = pack 0 (-deltaV₂ p)
```

**`ClassicalMechanics.HohmannTransfer.entryImpulse_norm`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L135).

```lean
lemma entryImpulse_norm (p : Parameters) : ‖entryImpulse p‖ = deltaV₁ p
```

**`ClassicalMechanics.HohmannTransfer.exitImpulse_norm`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L137).

```lean
lemma exitImpulse_norm (p : Parameters) : ‖exitImpulse p‖ = deltaV₂ p
```

**`ClassicalMechanics.HohmannTransfer.totalDeltaV_eq_sum_norms`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L139).

```lean
lemma totalDeltaV_eq_sum_norms (p : Parameters) :
    totalDeltaV p = ‖entryImpulse p‖ + ‖exitImpulse p‖
```

**`ClassicalMechanics.HohmannTransfer.impulses_tangential`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean#L143).

```lean
lemma impulses_tangential (p : Parameters) :
    (position p 0).re * (entryImpulse p).re +
      (position p 0).im * (entryImpulse p).im = 0 ∧
    (position p p.transferTime).re * (exitImpulse p).re +
      (position p p.transferTime).im * (exitImpulse p).im = 0
```

## Depends on

- [Circular orbits for the Hohmann transfer](hohmann-dynamics-circular.md)
- [Apsidal speeds on the Hohmann ellipse](hohmann-dynamics-endpoints.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Impulses.lean)
