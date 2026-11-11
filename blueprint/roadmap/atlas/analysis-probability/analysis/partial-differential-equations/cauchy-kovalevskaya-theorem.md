---
declaration: section
origin: cited
lean: MathlibExt.Analysis.CauchyKovalevskayaWanted.Analysis.E, MathlibExt.Analysis.CauchyKovalevskayaWanted.Analysis.cauchy_kovalevskaya
statement: formalized
---

# Cauchy–Kovalevskaya theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/cauchy-kovalevskaya-theorem/index.html).

## Model space $\mathbb{R}^d$ of the Cauchy–Kovalevskaya problem

For a natural number $d$,
this is the real Euclidean space $\mathbb{R}^d$ of dimension $d$, with the Euclidean inner product
and norm.

Formalized by `MathlibExt.Analysis.CauchyKovalevskayaWanted.Analysis.E`, an abbreviation declared in [WantedExt/Analysis/CauchyKovalevskayaWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/CauchyKovalevskayaWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/cauchy-kovalevskaya-theorem/index.html#e).

## Cauchy–Kovalevskaya theorem

Let $d$ be a natural number, write $\mathbb{R}^d$ for real
Euclidean $d$-space, and let $F : \mathbb{R}^d \times \mathbb{R} \times \mathbb{R} \to
\mathbb{R}^d$, $f : \mathbb{R}^d \times \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ and
$u_0 : \mathbb{R}^d \to \mathbb{R}$ be real analytic at every point. Then for every
$x_0 \in \mathbb{R}^d$ there are an open set $U \subseteq \mathbb{R}^d \times \mathbb{R}$
containing $(x_0, 0)$ and a function $u : \mathbb{R}^d \times \mathbb{R} \to \mathbb{R}$, real
analytic on $U$, such that $u(x, 0) = u_0(x)$ whenever $(x, 0) \in U$ and

$$\partial_t u(x, t) = F(x, t, u(x, t)) \cdot \nabla_x u(x, t) + f(x, t, u(x, t))$$

for every $(x, t) \in U$, where $\partial_t u$ is the partial derivative of $u$ in $t$ and
$\nabla_x u$ is its gradient in $x$. Moreover, every function
$v : \mathbb{R}^d \times \mathbb{R} \to \mathbb{R}$ that is real analytic on $U$, satisfies
$v(x, 0) = u_0(x)$ whenever $(x, 0) \in U$, and satisfies the same equation at every point of
$U$ agrees with $u$ on $U$.

## Sources

- A.-L. Cauchy (1842) and S. Kovalevskaya (1875). Listed as §32 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `cauchy_kovalevskaya` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.CauchyKovalevskayaWanted.Analysis.cauchy_kovalevskaya` is written with `theorem_wanted` in [WantedExt/Analysis/CauchyKovalevskayaWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/CauchyKovalevskayaWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/cauchy-kovalevskaya-theorem/index.html#cauchy-kovalevskaya).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cauchy–Kovalevskaya theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/cauchy-kovalevskaya-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/partial-differential-equations/cauchy-kovalevskaya-theorem)
