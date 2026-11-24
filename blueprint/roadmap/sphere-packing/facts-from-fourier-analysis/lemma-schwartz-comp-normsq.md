---
declaration: lemma
origin: cited
lean: schwartzMap_multidimensional_of_schwartzMap_real
statement: formalized
proof: formalized
---

# schwartz-comp-normsq

Let $f \in \mathcal{S}(\mathbb{R}, \mathbb{C})$ be a Schwartz function. Then, for every $d \in \mathbb{N}$, the radial function

$$
f_d : \mathbb{R}^d \to \mathbb{C}, \quad f_d(x) := f(\|x\|^2)
$$

is a Schwartz function.

## Depends on

- [Schwartz-Space](def-schwartz-space.md)

## Proof

Precomposition with a function of temperate growth that grows at least polynomially maps Schwartz functions to Schwartz functions. The function $x \mapsto \|x\|^2$ has temperate growth and satisfies the required lower bound $\|x\| \le 1 + \|x\|^2$, so the composition $f \circ \|\cdot\|^2$ is Schwartz.

## Lean

Formalized as [`schwartzMap_multidimensional_of_schwartzMap_real`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/schwartzMap_multidimensional_of_schwartzMap_real).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/fourier-analysis.tex, line 146](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L146)
