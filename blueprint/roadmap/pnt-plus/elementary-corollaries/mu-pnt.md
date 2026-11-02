---
declaration: proposition
origin: cited
lean: mu_pnt
statement: formalized
proof: formalized
---

# Möbius form of prime number theorem

We have $\sum_{n \leq x} \mu(n) = o(x)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [WeakPNT](../first-approach-wiener-ikehara-tauberian-theorem/weak-pnt/weakpnt.md)
- [mun](mun.md)

## Proof

From the Dirichlet convolution identity

$$
\mu(n) \log n = - \sum_{d|n} \mu(d) \Lambda(n/d)
$$

and summing we obtain

$$
\sum_{n \leq x} \mu(n) \log n = - \sum_{d \leq x} \mu(d) \sum_{m \leq x/d} \Lambda(m).
$$

For any $\varepsilon>0$, we have from the prime number theorem that

$$
\sum_{m \leq x/d} \Lambda(m) = x/d + O(\varepsilon x/d) + O_\varepsilon(1)
$$

(divide into cases depending on whether $x/d$ is large or small compared to $\varepsilon$). We conclude that

$$
\sum_{n \leq x} \mu(n) \log n
= - x \sum_{d \leq x} \frac{\mu(d)}{d} + O(\varepsilon x \log x) + O_\varepsilon(x).
$$

Applying [Proposition mun](mun.md) we conclude that

$$
\sum_{n \leq x} \mu(n) \log n = O(\varepsilon x \log x) + O_\varepsilon(x).
$$

and hence

$$
\sum_{n \leq x} \mu(n) \log x
= O(\varepsilon x \log x) + O_\varepsilon(x) + O( \sum_{n \leq x} (\log x - \log n) ).
$$

From Stirling's formula one has

$$
\sum_{n \leq x} (\log x - \log n) = O(x)
$$

thus

$$
\sum_{n \leq x} \mu(n) \log x = O(\varepsilon x \log x) + O_\varepsilon(x)
$$

and thus

$$
\sum_{n \leq x} \mu(n) = O(\varepsilon x) + O_\varepsilon(\frac{x}{\log x}).
$$

Sending $\varepsilon \to 0$ we obtain the claim.

## Lean

Formalized as [`mu_pnt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/mu_pnt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
