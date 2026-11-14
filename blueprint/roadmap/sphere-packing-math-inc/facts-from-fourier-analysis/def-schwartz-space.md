---
declaration: definition
origin: cited
lean: SchwartzMap
statement: formalized
---

# Schwartz-Space

A $C^\infty$ function $f:\mathbb{R}^d\to\mathbb{C}$ is called a *Schwartz function* if it decays to zero as $\|x\|\to\infty$ faster then any inverse power of $\|x\|$, and the same holds for all partial derivatives of $f$, ie, if for all $k, n \in \mathbb{N}$, there exists a constant $C \in \mathbb{R}$ such that for all $x \in \mathbb{R}^d$, $\left\lVert x \right\rVert^k \cdot \left\lVert f^{(n)}(x) \right\rVert \leq C$, where $f^{(n)}$ denotes the $n$-th derivative of $f$ considered along with the appropriate operator norm. The set of all Schwartz functions from $\mathbb{R}^d$ to $\mathbb{C}$ is called the *Schwartz space*. It is an $\mathbb{R}$-vector space.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`SchwartzMap`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/SchwartzMap).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/fourier-analysis.tex, line 28](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/fourier-analysis.tex#L28)
