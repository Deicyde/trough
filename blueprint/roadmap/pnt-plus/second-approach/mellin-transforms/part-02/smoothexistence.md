---
declaration: theorem
origin: cited
lean: SmoothExistence
statement: formalized
proof: formalized
---

# SmoothExistence

There exists a smooth (once differentiable would be enough), nonnegative “bumpfunction” $\nu$, supported in $[1/2,2]$ with total mass one:

$$
\int_0^\infty \nu(x)\frac{dx}{x} = 1.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Same idea as Urysohn-type argument.

## Lean

Formalized as [`SmoothExistence`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothExistence).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/SmoothExistence.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/SmoothExistence.lean)
