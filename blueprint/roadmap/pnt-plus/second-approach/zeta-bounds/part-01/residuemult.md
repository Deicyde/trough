---
declaration: theorem
origin: cited
lean: ResidueMult
statement: formalized
proof: formalized
---

# ResidueMult

If $f$ has a simple pole at $p$ with residue $A$, and $g$ is holomorphic near $p$, then the residue of $f \cdot g$ at $p$ is $A \cdot g(p)$. That is, we assume that

$$
f(s) = \frac{A}{s - p} + O(1)
$$

near $p$, and that $g$ is holomorphic near $p$. Then

$$
f(s) \cdot g(s) = \frac{A \cdot g(p)}{s - p} + O(1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Elementary calculation.

$$
f(s) * g(s) - \frac{A * g(p)}{s - p} =
\left(f(s) * g(s) - \frac{A * g(s)}{s - p}\right)
+ \left(\frac{A * g(s) - A * g(p)}{s - p}\right).
$$

The first term is $g(s)(f(s) - \frac{A}{s - p})$, which is bounded near $p$ by the assumption on $f$ and the fact that $g$ is holomorphic near $p$. The second term is $A$ times the log derivative of $g$ at $p$, which is bounded by the assumption that $g$ is holomorphic.

## Lean

Formalized as [`ResidueMult`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ResidueMult).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
