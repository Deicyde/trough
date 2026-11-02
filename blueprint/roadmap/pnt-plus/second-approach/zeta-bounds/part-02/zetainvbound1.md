---
declaration: lemma
origin: cited
lean: ZetaInvBound1
statement: formalized
proof: formalized
---

# ZetaInvBound1

For all $\sigma>1$,

$$
1/|\zeta(\sigma+it)| \le |\zeta(\sigma)|^{3/4}|\zeta(\sigma+2it)|^{1/4}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The identity

$$
1 \le |\zeta(\sigma)|^3 |\zeta(\sigma+it)|^4 |\zeta(\sigma+2it)|
$$

for $\sigma>1$ is already proved by Michael Stoll in the EulerProducts PNT file.

## Lean

Formalized as [`ZetaInvBound1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaInvBound1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
