---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.SchurL1.l1_norm_eq_tsum, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.summable_bounded_mul_l1, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.l1DualOfBounded, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.norm_l1DualOfBounded_le, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.tsum_split3, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.summable_norm_shift, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.tail_tsum_norm, MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schurBlockOf
statement: formalized
proof: formalized
---

# Schur's theorem on weak convergence in ℓ¹

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html).

## The $\ell^1$ norm is the sum of the coordinate norms

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. Every $x \in \ell^1(\mathbb{N}, \mathbb{K})$ satisfies
$\|x\| = \sum_{i=0}^{\infty} |x_i|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.l1_norm_eq_tsum`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#l1-norm-eq-tsum).

## The pairing of $\ell^1$ with sequences bounded by $1$ is summable

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$. If $y : \mathbb{N} \to \mathbb{K}$ satisfies $\|y_i\| \le 1$ for
every $i$ and $x \in \ell^1(\mathbb{N}, \mathbb{K})$, then the series $\sum_i y_i x_i$ is
summable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.summable_bounded_mul_l1`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#summable-bounded-mul-l1).

## Pairing $\ell^1$ with a sequence bounded by one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $(y_i)_{i \in \mathbb{N}}$ be a sequence in $\mathbb{K}$ with
$|y_i| \le 1$ for every $i$. The pairing with $y$ is the continuous linear functional
$\ell^1(\mathbb{N}, \mathbb{K}) \to \mathbb{K}$ given by $x \mapsto \sum_{i=0}^{\infty} y_i x_i$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.l1DualOfBounded`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#l1-dual-of-bounded).

## Pairing with a sequence bounded by one has norm at most one

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $(y_i)_{i \in \mathbb{N}}$ be a sequence in $\mathbb{K}$
with $|y_i| \le 1$ for every $i$. The continuous linear functional
$x \mapsto \sum_{i=0}^{\infty} y_i x_i$ on $\ell^1(\mathbb{N}, \mathbb{K})$ has operator norm at
most $1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.norm_l1DualOfBounded_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#norm-l1-dual-of-bounded-le).

## Splitting a series into a head, a middle block and a tail

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$, let $h : \mathbb{N} \to \mathbb{K}$ be summable and let $a \le b$ be natural
numbers. Then $\sum_{i=0}^{\infty} h(i)$ equals
$\sum_{i < a} h(i) + \sum_{a \le i < b} h(i) + \sum_{j=0}^{\infty} h(j + b)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.tsum_split3`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#tsum-split3).

## Tails of an $\ell^1$ sequence are absolutely summable

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every $x \in \ell^1(\mathbb{N}, \mathbb{K})$ and every $b \in \mathbb{N}$, the
series $\sum_{j=0}^{\infty} \|x_{j+b}\|$ is summable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.summable_norm_shift`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#summable-norm-shift).

## Tail of the norm series of an $\ell^1$ sequence

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every $x \in \ell^1(\mathbb{N}, \mathbb{K})$ and every $b \in \mathbb{N}$,
$\sum_{j=0}^{\infty} \|x_{j+b}\| = \|x\| - \sum_{i < b} \|x_i\|$, where $\|x\|$ is the $\ell^1$
norm of $x$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.tail_tsum_norm`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#tail-tsum-norm).

## Block index for a cutoff sequence

Let $M : \mathbb{N} \to \mathbb{N}$ be such that
every $i \in \mathbb{N}$ satisfies $i < M(k + 1)$ for some $k$. The block index of
$i \in \mathbb{N}$ is the least $k$ with $i < M(k + 1)$.

When $M$ is monotone and $M(0) = 0$, the block index of $i$ is the unique $k$ with
$M(k) \le i < M(k + 1)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schurBlockOf`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-block-of).

## An index lies in the block it is assigned to

Let $M : \mathbb{N} \to \mathbb{N}$ satisfy
$M(0) = 0$, and suppose every $i \in \mathbb{N}$ satisfies $i < M(j + 1)$ for some $j$. For
every $i \in \mathbb{N}$, if $k$ is the block index of $i$ (the least $k$ with
$i < M(k + 1)$), then $M(k) \le i < M(k + 1)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schurBlockOf_mem`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-block-of-mem).

## Indices in block $k$ have block index $k$

Let $M : \mathbb{N} \to \mathbb{N}$ be
monotone, and suppose every $i \in \mathbb{N}$ satisfies $i < M(j + 1)$ for some $j$. For all
$k, i \in \mathbb{N}$ with $M(k) \le i < M(k + 1)$, the block index of $i$ (the least $j$ with
$i < M(j + 1)$) is $k$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schurBlockOf_eq`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-block-of-eq).

## Conjugate-sign sequence of a block decomposition

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $(x_n)$ be a sequence in $\ell^1(\mathbb{N}, \mathbb{K})$, let
$n' : \mathbb{N} \to \mathbb{N}$, and let $M : \mathbb{N} \to \mathbb{N}$ be such that every
$i \in \mathbb{N}$ satisfies $i < M(j + 1)$ for some $j$. For $i \in \mathbb{N}$, let $k$ be
the block index of $i$ (the least $k$ with $i < M(k + 1)$) and let $v = x_{n'(k)}(i)$. The
$i$-th term $\sigma_i$ of the conjugate-sign sequence is $0$ if $v = 0$, and
$\overline{v} / |v|$ otherwise.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schurSignSeq`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-sign-seq).

## The conjugate-sign sequence is bounded by one

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $(x_n)$ be a sequence in $\ell^1(\mathbb{N}, \mathbb{K})$, let
$n' : \mathbb{N} \to \mathbb{N}$, and let $M : \mathbb{N} \to \mathbb{N}$ be such that every
$i \in \mathbb{N}$ satisfies $i < M(j + 1)$ for some $j$. Every term $\sigma_i$ of the
conjugate-sign sequence of $(x_n)$, $n'$ and $M$ satisfies $|\sigma_i| \le 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.norm_schurSignSeq_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#norm-schur-sign-seq-le).

## On block $k$, the conjugate signs recover absolute values

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $(x_n)$ be a sequence in $\ell^1(\mathbb{N}, \mathbb{K})$,
let $n' : \mathbb{N} \to \mathbb{N}$, and let $M : \mathbb{N} \to \mathbb{N}$ be monotone and
such that every $i \in \mathbb{N}$ satisfies $i < M(j + 1)$ for some $j$. Let $\sigma$ be the
conjugate-sign sequence of $(x_n)$, $n'$ and $M$. For all $k, i \in \mathbb{N}$ with
$M(k) \le i < M(k + 1)$, we have $\sigma_i \, x_{n'(k)}(i) = |x_{n'(k)}(i)|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schurSignSeq_mul`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-sign-seq-mul).

## Schur's theorem

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let $(x_n)$ be a sequence
in $\ell^1(\mathbb{N}, \mathbb{K})$ and let $x_0 \in \ell^1(\mathbb{N}, \mathbb{K})$. If
$F(x_n) \to F(x_0)$ for every continuous linear functional $F$ on $\ell^1(\mathbb{N}, \mathbb{K})$,
that is, if $(x_n)$ converges weakly to $x_0$, then $x_n \to x_0$ in the $\ell^1$ norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schur_tendsto_of_weak_tendsto`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-tendsto-of-weak-tendsto).

## Schur's theorem, norm form

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, let
$(x_n)$ be a sequence in $\ell^1(\mathbb{N}, \mathbb{K})$, and let
$x \in \ell^1(\mathbb{N}, \mathbb{K})$. If $F(x_n) \to F(x)$ as $n \to \infty$ for every
continuous linear functional $F : \ell^1(\mathbb{N}, \mathbb{K}) \to \mathbb{K}$, then
$\|x_n - x\| \to 0$ as $n \to \infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurL1.schur_tendsto_norm_sub_of_weak_tendsto`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurL1.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html#schur-tendsto-norm-sub-of-weak-tendsto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur's theorem on weak convergence in ℓ¹](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/schur-s-theorem-on-weak-convergence-in)
