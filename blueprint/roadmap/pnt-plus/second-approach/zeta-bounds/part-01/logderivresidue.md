---
declaration: theorem
origin: cited
lean: logDerivResidue
statement: formalized
proof: formalized
---

# logDerivResidue

If $f$ is holomorphic in a neighborhood of $p$, and there is a simple pole at $p$, then $f'/ f$ has a simple pole at $p$ with residue $-1$:

$$
\frac{f'(s)}{f(s)} = \frac{-1}{s - p} + O(1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md)

## Proof

Using Theorem [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md), there is a function $g$ holomorphic near $p$, for which $f(s) = A/(s-p) + g(s) = h(s)/ (s-p)$. Here $h(s):= A + g(s)(s-p)$ which is nonzero in a neighborhood of $p$ (since $h$ goes to $A$ which is nonzero). Then $f'(s) = (h'(s)(s-p) - h(s))/(s-p)^2$, and we can compute the quotient:

$$
\frac{f'(s)}{f(s)}+1/(s-p) = \frac{h'(s)(s-p) - h(s)}{h(s)} \cdot \frac{1}{(s-p)}+1/(s-p)
=
\frac{h'(s)}{h(s)}.
$$

Since $h$ is nonvanishing near $p$, this remains bounded in a neighborhood of $p$.

## Lean

Formalized as [`logDerivResidue`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/logDerivResidue).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
