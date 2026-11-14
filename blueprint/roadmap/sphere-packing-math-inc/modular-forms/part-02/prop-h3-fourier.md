---
declaration: proposition
origin: cited
lean: H₃
statement: formalized
proof: formalized
---

# H3-fourier

$H_3$ admits a Fourier series of the form

$$
H_3(z) = \sum_{n \ge 0} c_{H_3}(n) e^{\pi i n z}
$$

for some $c_{H_3}(n) \in \mathbb{R}_{\ge 0}$ with $c_{H_3}(0) = 1$ and $c_{H_3}(n) = O(n^k)$ for some $k \in \mathbb{N}$. Especially, $H_3$ is not cuspidal.

## Depends on

- [H2-H3-H4](def-h2-h3-h4.md)

## Proof

We have

$$
H_3(z) = \Theta_3(z)^{4} = \left(\sum_{n \in \mathbb{Z}} e^{\pi i n^2 z}\right)^{4} = \left(1 + 2 \sum_{n \ge 1} e^{\pi i n^2 z}\right)^{4} = 1 + O(e^{\pi i z}).
$$

## Lean

Formalized as [`H₃`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₃).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 448](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L448)
