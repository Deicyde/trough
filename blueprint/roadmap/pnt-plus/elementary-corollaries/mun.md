---
declaration: proposition
origin: cited
lean: sum_mobius_div_self_le
statement: formalized
proof: formalized
---

# mun

We have $|\sum_{n \leq x} \frac{\mu(n)}{n}| \leq 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

From Möbius inversion $1_{n=1} = \sum_{d|n} \mu(d)$ and summing we have

$$
1 = \sum_{d \leq x} \mu(d) \lfloor \frac{x}{d} \rfloor
$$

for any $x \geq 1$. Since $\lfloor \frac{x}{d} \rfloor = \frac{x}{d} - \epsilon_d$ with $0 \leq \epsilon_d < 1$ and $\epsilon_x = 0$, we conclude that

$$
1 ≥ x \sum_{d \leq x} \frac{\mu(d)}{d} - (x - 1)
$$

and the claim follows.

## Lean

Formalized as [`sum_mobius_div_self_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/sum_mobius_div_self_le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
