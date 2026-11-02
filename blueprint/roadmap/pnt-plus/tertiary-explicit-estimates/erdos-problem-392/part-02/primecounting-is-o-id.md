---
declaration: lemma
origin: cited
lean: Erdos392.primeCounting_is_o_id
statement: formalized
proof: formalized
---

# primeCounting-is-o-id

$$
\pi(n) = o(n) \quad \text{as } n \to \infty.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Given $\varepsilon > 0$, choose $a \neq 0$ with $\varphi(a)/a < \varepsilon/2$ (using $\prod_{p \leq n}(1 - 1/p) \to 0$). For $n \geq a + 2$,

$$
\pi(n) \leq \frac{\varphi(a)}{a} \cdot n + \varphi(a) + \pi(a+1) + 1.
$$

Since $\varphi(a)/a < \varepsilon/2$, for $n$ large enough the constant terms are absorbed, giving $\pi(n) < \varepsilon n$.

## Lean

Formalized as [`Erdos392.primeCounting_is_o_id`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Erdos392.primeCounting_is_o_id).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Erdos392.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Erdos392.lean)
