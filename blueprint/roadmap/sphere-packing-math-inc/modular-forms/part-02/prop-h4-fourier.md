---
declaration: proposition
origin: cited
lean: H₄
statement: formalized
proof: formalized
---

# H4-fourier

$H_4$ admits a Fourier series of the form

$$
H_4(z) = \sum_{n \ge 0} c_{H_4}(n) e^{\pi i n z}
$$

for some $c_{H_4}(n) \in \mathbb{R}$ with $c_{H_4}(0) = 1$ and $c_{H_4}(n) = O(n^k)$ for some $k \in \mathbb{N}$. Especially, $H_4$ is not cuspidal.

## Depends on

- [H2-H3-H4](def-h2-h3-h4.md)

## Lean

Formalized as [`H₄`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₄).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 463](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L463)
