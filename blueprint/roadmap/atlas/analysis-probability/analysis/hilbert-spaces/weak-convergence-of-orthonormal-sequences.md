---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_inner_cofinite_zero, MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_apply_cofinite_zero, MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_inner_atTop_zero, MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_apply_atTop_zero, MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.not_tendsto_atTop_zero
statement: formalized
proof: formalized
---

# Weak convergence of orthonormal sequences

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html).

## Fourier coefficients along an orthonormal family tend to `0`

Let $H$ be an inner product
space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(v_i)_{i \in \iota}$ be an orthonormal
family in $H$ and let $x \in H$. Then the inner products $\langle v_i, x \rangle$ tend to $0$
along the cofinite filter on $\iota$: for every $\varepsilon > 0$,
$|\langle v_i, x \rangle| < \varepsilon$ for all but finitely many $i$.

Bessel's inequality makes their squared absolute values summable, and the terms of a summable
family tend to $0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_inner_cofinite_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html#tendsto-inner-cofinite-zero).

## An orthonormal family tends weakly to `0`

Let $H$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(v_i)_{i \in \iota}$ be an orthonormal family in
$H$ and let $f : H \to \mathbb{K}$ be a continuous linear functional. Then $f(v_i)$ tends to $0$
along the cofinite filter on $\iota$: for every $\varepsilon > 0$, $|f(v_i)| < \varepsilon$ for
all but finitely many $i$.

By the Riesz representation theorem, $f$ is the inner product with a fixed vector, so this
follows from the corresponding statement for Fourier coefficients.

Formalized by `MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_apply_cofinite_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html#tendsto-apply-cofinite-zero).

## Fourier coefficients along an orthonormal sequence tend to `0`

Let $H$ be an inner
product space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(v_n)_{n \in \mathbb{N}}$ be
an orthonormal sequence in $H$ and let $x \in H$. Then $\langle v_n, x \rangle \to 0$ as
$n \to \infty$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_inner_atTop_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html#tendsto-inner-at-top-zero).

## An orthonormal sequence tends weakly to `0`

Let $H$ be a Hilbert space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(v_n)_{n \in \mathbb{N}}$ be an orthonormal
sequence in $H$. Then for every continuous linear functional $f : H \to \mathbb{K}$, we have
$f(v_n) \to 0$ as $n \to \infty$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.tendsto_apply_atTop_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html#tendsto-apply-at-top-zero).

## An orthonormal sequence does not converge strongly to `0`

Let $H$ be an inner product
space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ and let $(v_n)_{n \in \mathbb{N}}$ be an
orthonormal sequence in $H$. Then $v_n$ does not tend to $0$ in norm as $n \to \infty$.

Weak convergence does not upgrade to norm convergence here: every term of an orthonormal sequence
has norm $1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.OrthonormalWeakConvergence.not_tendsto_atTop_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/OrthonormalWeakConvergence.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html#not-tendsto-at-top-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weak convergence of orthonormal sequences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/hilbert-spaces/weak-convergence-of-orthonormal-sequences)
