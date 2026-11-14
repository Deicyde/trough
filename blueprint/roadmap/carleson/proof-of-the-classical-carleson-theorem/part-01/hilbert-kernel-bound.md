---
declaration: lemma
origin: cited
lean: Hilbert_kernel_bound
statement: formalized
proof: formalized
---

# Hilbert kernel bound

For $x,y\in {\mathbb{R}}$ with $x\neq y$ we have

$$
|\kappa(x-y)|\le 2^2(2|x-y|)^{-1}\, .\qquad\text{(18)}
$$

## Depends on

- [lower secant bound](lower-secant-bound.md)

## Proof

Fix $x\neq y$. If $\kappa(x-y)$ is zero, then (18) is evident. Assume $\kappa(x-y)$ is not zero, then $0<|x-y|<1$. We have

$$
|\kappa(x-y)|=\left|\frac {1-|x-y|}{1-e^{i(x-y)}}\right|\, .\qquad\text{(19)}
$$

We estimate with [lower secant bound](lower-secant-bound.md)

$$
|\kappa(x-y)|\le \frac {1}{|1-e^{i(x-y)}|}\le \frac 2{|x-y|}\, .\qquad\text{(20)}
$$

This proves (18) in the given case and completes the proof of the lemma.

## Lean

Formalized as [`Hilbert_kernel_bound`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Hilbert_kernel_bound).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8427](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8427)
