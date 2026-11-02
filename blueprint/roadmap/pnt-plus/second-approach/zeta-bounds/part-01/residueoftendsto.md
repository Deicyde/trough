---
declaration: theorem
origin: cited
lean: ResidueOfTendsTo
statement: formalized
proof: formalized
---

# ResidueOfTendsTo

If a function $f$ is holomorphic in a neighborhood of $p$ and $\lim_{s\to p} (s-p)f(s) = A$, then $f(s) = \frac{A}{s-p} + O(1)$ near $p$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md)

## Proof

The function $(s - p)\cdot f(s)$ bounded, so by Theorem [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md), there is a holomorphic function, $g$, say, so that $(s-p)f(s) = g(s)$ in a neighborhood of $s=p$, and $g(p)=A$. Now because $g$ is holomorphic, near $s=p$, we have $g(s)=A+O(s-p)$. Then when you divide by $(s-p)$, you get $f(s) = A/(s-p) + O(1)$.

## Lean

Formalized as [`ResidueOfTendsTo`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ResidueOfTendsTo).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
