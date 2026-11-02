---
declaration: proposition
origin: cited
lean: lambda_pnt
statement: formalized
proof: formalized
---

# lambda-pnt

We have $\sum_{n \leq x} \lambda(n) = o(x)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [WeakPNT](../first-approach-wiener-ikehara-tauberian-theorem/weak-pnt/weakpnt.md)
- [Möbius form of prime number theorem](mu-pnt.md)
- [mun](mun.md)

## Proof

From the identity

$$
\lambda(n) = \sum_{d^2|n} \mu(n/d^2)
$$

and summing, we have

$$
\sum_{n \leq x} \lambda(n) = \sum_{d \leq \sqrt{x}} \sum_{n \leq x/d^2} \mu(n).
$$

For any $\varepsilon>0$, we have from Proposition [Möbius form of prime number theorem](mu-pnt.md) that

$$
\sum_{n \leq x/d^2} \mu(n) = O(\varepsilon x/d^2) + O_\varepsilon(1)
$$

and hence on summing in $d$

$$
\sum_{n \leq x} \lambda(n) = O(\varepsilon x) + O_\varepsilon(x^{1/2}).
$$

Sending $\varepsilon \to 0$ we obtain the claim.

## Lean

Formalized as [`lambda_pnt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/lambda_pnt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
