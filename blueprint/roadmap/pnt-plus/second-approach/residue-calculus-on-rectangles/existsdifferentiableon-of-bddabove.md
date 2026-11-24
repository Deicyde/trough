---
declaration: theorem
origin: cited
lean: existsDifferentiableOn_of_bddAbove
statement: formalized
proof: formalized
---

# existsDifferentiableOn-of-bddAbove

If $f$ is differentiable on a set $s$ except at $c\in s$, and $f$ is bounded above on $s\setminus\{c\}$, then there exists a differentiable function $g$ on $s$ such that $f$ and $g$ agree on $s\setminus\{c\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is the Riemann Removable Singularity Theorem, slightly rephrased from what's in Mathlib. (We don't care what the function $g$ is, just that it's holomorphic.)

## Lean

Formalized as [`existsDifferentiableOn_of_bddAbove`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/existsDifferentiableOn_of_bddAbove).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean)
