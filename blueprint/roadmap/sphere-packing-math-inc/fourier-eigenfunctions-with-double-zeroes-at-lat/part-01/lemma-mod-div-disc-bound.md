---
declaration: lemma
origin: cited
lean: MagicFunction.PolyFourierCoeffBound.DivDiscBoundOfPolyFourierCoeff
statement: formalized
proof: formalized
---

# mod-div-disc-bound

Let $f(z)$ be a holomorphic function with a Fourier expansion

$$
f(z) = \sum_{n \ge n_0} c_f(n) e^{\pi i n z}
$$

with $c_f(n_0) \ne 0$. Assume that $c_f(n)$ has a polynomial growth, i.e. $|c_f(n)| = O(n^k)$ for some $k \in \mathbb{N}$. Then there exists a constant $C_f > 0$ such that

$$
\left|\frac{f(z)}{\Delta(z)}\right| \le C_f e^{-\pi (n_0 - 2) \Im z}
$$

for all $z$ with $\Im z > 1/2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [disc-definition](../../modular-forms/part-01/def-disc-definition.md)

## Proof

By the product formula [(4)](../../modular-forms/part-01/def-disc-definition.md),

$$
\begin{aligned}
\left|\frac{f(z)}{\Delta(z)}\right| &= \left|\frac{\sum_{n \ge n_0} c_f(n) e^{\pi i n z}}{e^{2 \pi i z}\prod_{n \ge 1} (1 - e^{2\pi i n z})^{24}}\right| \\
&= |e^{\pi i (n_0 - 2)z}| \cdot \frac{|\sum_{n \ge n_0} c_f(n) e^{\pi i (n - n_0) z}|}{\prod_{n \ge 1} |1 - e^{2\pi i n z}|^{24}} \\
&\le e^{-\pi (n_0 - 2) \Im z} \cdot \frac{\sum_{n \ge n_0} |c_f(n)| e^{-\pi (n - n_0) \Im z}}{\prod_{n \ge 1} (1 - e^{- 2\pi n \Im z})^{24}} \\
&\le e^{-\pi (n_0 - 2) \Im z} \cdot \frac{\sum_{n \ge n_0} |c_f(n)| e^{-\pi (n - n_0) / 2}}{\prod_{n \ge 1} (1 - e^{-\pi n})^{24}} \\
&= C_f \cdot e^{-\pi (n_0 - 2) \Im z}
\end{aligned}
$$

where

$$
C_f = \frac{\sum_{n \ge n_0} |c_f(n)| e^{-\pi (n - n_0) / 2}}{\prod_{n \ge 1} (1 - e^{-\pi n})^{24}}.
$$

Note that the summation in the numerator converges absolutely because of polynomial growth. The denominator also converges, which is simply $e^{\pi} \cdot \Delta(i/2)$.

## Lean

Formalized as [`MagicFunction.PolyFourierCoeffBound.DivDiscBoundOfPolyFourierCoeff`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/MagicFunction.PolyFourierCoeffBound.DivDiscBoundOfPolyFourierCoeff).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/construct-a-b.tex, line 96](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/construct-a-b.tex#L96)
