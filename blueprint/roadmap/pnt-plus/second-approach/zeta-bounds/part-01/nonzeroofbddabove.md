---
declaration: theorem
origin: cited
lean: nonZeroOfBddAbove
statement: formalized
proof: formalized
---

# nonZeroOfBddAbove

If a function $f$ has a simple pole at a point $p$ with residue $A \neq 0$, then $f$ is nonzero in a punctured neighborhood of $p$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We know that $f(s) = \frac{A}{s-p} + O(1)$ near $p$, so we can write

$$
f(s) = \left(f(s) - \frac{A}{s-p}\right) + \frac{A}{s-p}.
$$

The first term is bounded, say by $M$, and the second term goes to $\infty$ as $s \to p$. Therefore, there exists a neighborhood $V$ of $p$ such that for all $s \in V \setminus \{p\}$, we have $f(s) \neq 0$.

## Lean

Formalized as [`nonZeroOfBddAbove`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/nonZeroOfBddAbove).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
