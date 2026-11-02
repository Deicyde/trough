---
declaration: theorem
origin: cited
lean: pi_asymp
statement: formalized
proof: formalized
---

# pi-asymp

There exists a function $c(x)$ such that $c(x) = o(1)$ as $x \to \infty$ and

$$
\pi(x) = (1 + c(x)) \int_2^x \frac{dt}{\log t}
$$

for all $x$ large enough.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [chebyshev-asymptotic](chebyshev-asymptotic.md)

## Proof

We have the identity

$$
\pi(x) = \frac{1}{\log x} \sum_{p \leq x} \log p
+ \int_2^x (\sum_{p \leq t} \log p) \frac{dt}{t \log^2 t}
$$

as can be proven by interchanging the sum and integral and using the fundamental theorem of calculus. For any $\varepsilon$, we know from Theorem chebyshev\_asymptotic that there is $x_\varepsilon$ such that $\sum_{p \leq t} \log p = t + O(\varepsilon t)$ for $t \geq x_\varepsilon$, hence for $x \geq x_\varepsilon$

$$
\pi(x) = \frac{1}{\log x} (x + O(\varepsilon x))
+ \int_{x_\varepsilon}^x (t + O(\varepsilon t)) \frac{dt}{t \log^2 t} + O_\varepsilon(1)
$$

where the $O_\varepsilon(1)$ term can depend on $x_\varepsilon$ but is independent of $x$. One can evaluate this after an integration by parts as

$$
\pi(x) = (1+O(\varepsilon)) \int_{x_\varepsilon}^x \frac{dt}{\log t} + O_\varepsilon(1)
$$

$$
= (1+O(\varepsilon)) \int_{2}^x \frac{dt}{\log t}
$$

for $x$ large enough, giving the claim.

## Lean

Formalized as [`pi_asymp`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/pi_asymp).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
