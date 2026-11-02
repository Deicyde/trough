---
declaration: proposition
origin: cited
lean: mu_pnt_alt
statement: formalized
proof: formalized
---

# Alternate Möbius form of prime number theorem

We have $\sum_{n \leq x} \mu(n)/n = o(1)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Möbius form of prime number theorem](mu-pnt.md)

## Proof

As in the proof of Theorem [mun](mun.md), we have

$$
1 = \sum_{d \leq x} \mu(d) \lfloor \frac{x}{d} \rfloor
$$

$$
= x \sum_{d \leq x} \frac{\mu(d)}{d} - \sum_{d \leq x} \mu(d) \{ \frac{x}{d} \}
$$

so it will suffice to show that

$$
\sum_{d \leq x} \mu(d) \{ \frac{x}{d} \} = o(x).
$$

Let $N$ be a natural number. It suffices to show that

$$
\sum_{d \leq x} \mu(d) \{ \frac{x}{d} \} = O(x/N).
$$

if $x$ is large enough depending on $N$. We can split the left-hand side as the sum of

$$
\sum_{d \leq x/N} \mu(d) \{ \frac{x}{d} \}
$$

and

$$
\sum_{j=1}^{N-1} \sum_{x/(j+1) < d \leq x/j} \mu(d) (x/d - j).
$$

The first term is clearly $O(x/N)$. For the second term, we can use Theorem [Möbius form of prime number theorem](mu-pnt.md) and summation by parts (using the fact that $x/d-j$ is monotone and bounded) to find that

$$
\sum_{x/(j+1) < d \leq x/j} \mu(d) (x/d - j) = o(x)
$$

for any given $j$, so in particular

$$
\sum_{x/(j+1) < d \leq x/j} \mu(d) (x/d - j) = O(x/N^2)
$$

for all $j=1,\dots,N-1$ if $x$ is large enough depending on $N$. Summing all the bounds, we obtain the claim.

## Lean

Formalized as [`mu_pnt_alt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/mu_pnt_alt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
