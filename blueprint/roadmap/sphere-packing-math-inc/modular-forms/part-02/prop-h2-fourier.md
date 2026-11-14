---
declaration: proposition
origin: cited
lean: H₂
statement: formalized
proof: formalized
---

# H2-fourier

$H_2$ admits a Fourier series of the form

$$
H_2(z) = \sum_{n \ge 1} c_{H_2}(n) e^{\pi i n z}
$$

for some $c_{H_2}(n) \in \mathbb{R}_{\ge 0}$, with $c_{H_2}(1) = 16$ and $c_{H_2}(n) = O(n^k)$ for some $k \in \mathbb{N}$.

## Depends on

- [H2-H3-H4](def-h2-h3-h4.md)

## Proof

We have

$$
\begin{aligned}
H_2(z) &= \Theta_2(z)^4 \\
&= \left(\sum_{n \in \mathbb{Z}} e^{\pi i (n + \frac{1}{2})^{2} z}\right)^{4} \\
&= \left(2\sum_{n \ge 0} e^{\pi i (n + \frac{1}{2})^{2} z}\right)^{4} \\
&= \left(2 e^{\pi i z / 4} + 2 \sum_{n \ge 1} e^{\pi i (n^2 + n + \frac{1}{4}) z}\right)^{4} \\
&= 16 e^{\pi i z}\left(1 + \sum_{n \ge 1} e^{\pi i (n^2 + n)z}\right)^{4} \\
&= 16 e^{\pi i z} + \sum_{n \ge 2} c_{H_2}(n) e^{\pi i n z} \\
&= \sum_{n \ge 1} c_{H_2}(n) e^{\pi i n z}.
\end{aligned}
$$

## Lean

Formalized as [`H₂`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₂).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 428](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L428)
