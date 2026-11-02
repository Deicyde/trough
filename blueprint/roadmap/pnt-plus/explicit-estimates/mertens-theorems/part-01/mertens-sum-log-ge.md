---
declaration: corollary
origin: cited
lean: Mertens.sum_log_ge
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1305
---

# Partial sum of logarithm lower bound

For any $x \geq 1$, one has

$$
\sum_{n \leq x} \log n \geq x \log x - 2 x.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have

$$
\begin{aligned}
\sum_{n \leq x} \log n &= \sum_{2 \leq n \leq \lfloor x \rfloor} \log n \\
&\geq \sum_{2 \leq n \leq \lfloor x \rfloor} \int_{n-1}^n \log t \, dt \\
&= \int_1^{\lfloor x \rfloor} \log t \, dt \\
&\geq \int_1^x \log t\ dt - \log x \\
&= x \log x - x - \log x \\
&\geq x \log x - 2 x.
\end{aligned}
$$

Here we use the monotonicity of $\log n$ (and its vanishing at $n=1$) and the crude bound $\log x \leq x$. Note: the tools at Mathlib.Analysis.SumIntegralComparisons may be useful.

## Lean

Formalized as [`Mertens.sum_log_ge`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.sum_log_ge).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
