---
declaration: definition
origin: cited
lean: SchwartzMap
statement: formalized
---

# Schwartz-Space

A $C^\infty$ function $f:\mathbb{R}^d\to\mathbb{C}$ is called a *Schwartz function* if it decays to zero as $\|x\|\to\infty$ faster then any inverse power of $\|x\|$, and the same holds for all partial derivatives of $f$, ie, if for all $k \in \mathbb{N}$ and $n \in \mathbb{N}^d$, there exists a constant $C \in \mathbb{R}$ such that for all $x \in \mathbb{R}^d$, $\left\lVert x \right\rVert^k \cdot \left\lvert f^{(n)}(x) \right\rvert \leq C$, where $f^{(n)}$ denotes the $n$-th partial derivative of $f$. The set of all Schwartz functions from $\mathbb{R}^d$ to $\mathbb{C}$ is called the *Schwartz space*. It is an $\mathbb{R}$-vector space.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`SchwartzMap`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SchwartzMap).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/fourier-analysis.tex, line 34](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/072d555d14b4265f3c996ad195925dc00f47f563/blueprint/src/subsections/fourier-analysis.tex#L34)
