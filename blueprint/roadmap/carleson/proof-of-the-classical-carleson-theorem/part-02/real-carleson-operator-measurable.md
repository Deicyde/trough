---
declaration: lemma
origin: cited
lean: carlesonOperatorReal_measurable
statement: formalized
proof: formalized
---

# real Carleson operator measurable

Let $f$ be a bounded measurable function on ${\mathbb{R}}$. Then $Tf$ as defined in [(9)](../part-01/real-carleson.md) is measurable.

## Depends on

- [Hilbert kernel bound](../part-01/hilbert-kernel-bound.md)

## Proof

Since a countable supremum of measurable functions is measurable, it suffices to show that for every $n\in{\mathbb{Z}}$,

$$
x \mapsto \sup_{r>0}\left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right|
$$

is measurable. So let $n\in{\mathbb{Z}}$. Note that for each $x\in{\mathbb{R}}$, the function

$$
r \mapsto \left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right|
$$

is continuous on $(0,\infty)$ since the integrand is locally bounded on the domain $0<|x-y|<1$ by the assumptions on $f$ and [Hilbert kernel bound](../part-01/hilbert-kernel-bound.md). Thus, for each $x\in{\mathbb{R}}$,

$$
\sup_{r>0}\left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right|
=\sup_{r\in{\mathbb{Q}}_{>0}}\left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right|
$$

The right hand side is again a countable supremum so it remains to show that for every $r\in{\mathbb{Q}}_{>0}$,

$$
x \mapsto \left|\int_{r<|x-y|<1} f(y)\kappa(x-y) e^{iny}\, dy\right| = \left|\int \mathbf{1}_{\{r<|x-\cdot|<1\}}(y) f(y)\kappa(x-y) e^{iny}\, dy\right|
$$

is measurable, which follows from the fact that the integrand is measurable in $(x,y)$.

## Lean

Formalized as [`carlesonOperatorReal_measurable`](https://fpvandoorn.github.io/carleson/docs/find/#doc/carlesonOperatorReal_measurable).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 9122](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L9122)
