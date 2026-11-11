---
declaration: section
origin: cited
lean: hasDerivWithinAt_of_tendstoUniformlyOn_Icc, hasDerivAt_of_tendstoUniformlyOn_Icc
statement: formalized
proof: formalized
---

# Interchange of limits and derivatives

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/interchange-of-limits-and-derivatives/index.html).

## Interchange of limits and derivatives on a closed interval

Let $a < b$ be real
numbers, and let $f_n, f_n' : \mathbb{R} \to \mathbb{R}$ for $n \in \mathbb{N}$ and
$g, g' : \mathbb{R} \to \mathbb{R}$ be functions. Suppose that for every $n$ and every
$x \in [a, b]$, $f_n$ is differentiable at $x$ (two-sided, also at the endpoints) with
derivative $f_n'(x)$; that each $f_n'$ is continuous on $[a, b]$; that $f_n' \to g'$
uniformly on $[a, b]$; and that $f_n(x) \to g(x)$ for every $x \in [a, b]$. Then for every
$x \in [a, b]$, $g$ has derivative $g'(x)$ at $x$ within $[a, b]$ (a one-sided derivative at
the endpoints), and $g'$ is continuous on $[a, b]$.

Formalized by `hasDerivWithinAt_of_tendstoUniformlyOn_Icc`, a theorem declared in [MathlibExt/Analysis/Calculus/UniformLimitDerivative.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/UniformLimitDerivative.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/interchange-of-limits-and-derivatives/index.html#has-deriv-within-at-of-tendsto-uniformly).

## Interchange of limits and derivatives at interior points

Let $a < b$ be real numbers,
and let $f_n, f_n' : \mathbb{R} \to \mathbb{R}$ for $n \in \mathbb{N}$ and
$g, g' : \mathbb{R} \to \mathbb{R}$ be functions. Suppose that for every $n$ and every
$x \in [a, b]$, $f_n$ is differentiable at $x$ (two-sided, also at the endpoints) with
derivative $f_n'(x)$; that each $f_n'$ is continuous on $[a, b]$; that $f_n' \to g'$
uniformly on $[a, b]$; and that $f_n(x) \to g(x)$ for every $x \in [a, b]$. Then $g$ is
differentiable at every $x \in (a, b)$ with derivative $g'(x)$.

Formalized by `hasDerivAt_of_tendstoUniformlyOn_Icc`, a theorem declared in [MathlibExt/Analysis/Calculus/UniformLimitDerivative.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/UniformLimitDerivative.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/interchange-of-limits-and-derivatives/index.html#has-deriv-at-of-tendsto-uniformly-on-icc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Interchange of limits and derivatives](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/interchange-of-limits-and-derivatives/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/differential-calculus/interchange-of-limits-and-derivatives)
