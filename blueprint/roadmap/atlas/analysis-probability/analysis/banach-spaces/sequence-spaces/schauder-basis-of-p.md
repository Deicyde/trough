---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis, MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpSchauderBasis, MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis_coord_apply, MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis_apply, MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis_proj_apply, MathlibExt.Analysis.Normed.Lp.SchauderBasis.norm_lpSchauderBasis_proj_apply_le, MathlibExt.Analysis.Normed.Lp.SchauderBasis.norm_lpSchauderBasis_proj_le, MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpSchauderBasis_coord_apply
statement: formalized
proof: formalized
---

# Schauder basis of ℓ^p

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html).

## The unit vectors form an unconditional Schauder basis of ℓᵖ

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $1 \le p < \infty$ and let $\iota$ be a type. This is the
unconditional Schauder basis of $\ell^p(\iota, \mathbb{K})$ whose $i$-th basis vector is the unit
vector $e_i$, equal to $1$ at $i$ and to $0$ elsewhere, and whose $i$-th coordinate functional is
the evaluation $x \mapsto x_i$. In particular every $x \in \ell^p(\iota, \mathbb{K})$ is the
limit in norm of the finite partial sums $\sum_{i \in A} x_i e_i$ along the finite sets
$A \subseteq \iota$ directed by inclusion.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis`, a definition declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-unconditional-schauder-basis).

## The unit vectors form a Schauder basis of ℓᵖ

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $1 \le p < \infty$. This is the Schauder basis of
$\ell^p(\mathbb{N}, \mathbb{K})$ whose $i$-th basis vector is the unit vector $e_i$, equal to $1$ at
$i$ and to $0$ elsewhere, and whose $i$-th coordinate functional is the evaluation $x \mapsto x_i$.
In particular every $x \in \ell^p(\mathbb{N}, \mathbb{K})$ is the limit in norm of its partial sums
$\sum_{i < n} x_i e_i$ as $n \to \infty$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpSchauderBasis`, a definition declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-schauder-basis).

## Coordinate functionals of the unconditional ℓᵖ basis

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $1 \le p < \infty$ and let $\iota$ be a type. For every $i \in \iota$ and every
$x \in \ell^p(\iota, \mathbb{K})$, the $i$-th coordinate functional of the unconditional Schauder
basis of $\ell^p(\iota, \mathbb{K})$ by unit vectors sends $x$ to its entry $x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis_coord_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-unconditional-schauder-basis-coord-ap).

## Basis vectors of the unconditional ℓᵖ basis

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $1 \le p < \infty$ and let $\iota$ be a type. For every $i \in \iota$, the
$i$-th basis vector of the unconditional Schauder basis of $\ell^p(\iota, \mathbb{K})$ by unit
vectors is the unit vector $e_i$, the family equal to $1$ at $i$ and to $0$ elsewhere.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-unconditional-schauder-basis-apply).

## Finite-set projections of the unconditional ℓᵖ basis

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $1 \le p < \infty$ and let $\iota$ be a type. For every finite set
$A \subseteq \iota$ and every $x \in \ell^p(\iota, \mathbb{K})$, the projection $P_A$ of the
unconditional Schauder basis of $\ell^p(\iota, \mathbb{K})$ by unit vectors onto the basis vectors
indexed by $A$ satisfies $P_A x = \sum_{i \in A} x_i e_i$, where $e_i$ is the unit vector equal
to $1$ at $i$ and to $0$ elsewhere.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpUnconditionalSchauderBasis_proj_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-unconditional-schauder-basis-proj-app).

## Basis projections of $\ell^p$ are contractive

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $\iota$ be an index set and let $1 \le p < \infty$. Let $e_i$ ($i \in \iota$) be
the unit vectors, which form an unconditional Schauder basis of $\ell^p(\iota, \mathbb{K})$. For
every finite set $A \subseteq \iota$ and every $x \in \ell^p(\iota, \mathbb{K})$, the basis
projection $P_A x = \sum_{i \in A} x_i e_i$ satisfies $\|P_A x\|_p \le \|x\|_p$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.norm_lpSchauderBasis_proj_apply_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#norm-lp-schauder-basis-proj-apply-le).

## The $\ell^p$ basis projections have operator norm at most $1$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $\iota$ be an index set and let $1 \le p < \infty$. Let $e_i$
($i \in \iota$) be the unit vectors, which form an unconditional Schauder basis of
$\ell^p(\iota, \mathbb{K})$. For every finite set $A \subseteq \iota$, the basis projection
$P_A$, the bounded linear operator on $\ell^p(\iota, \mathbb{K})$ given by
$P_A x = \sum_{i \in A} x_i e_i$, has operator norm $\|P_A\| \le 1$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.norm_lpSchauderBasis_proj_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#norm-lp-schauder-basis-proj-le).

## Coordinate functionals of the ℓᵖ Schauder basis

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $1 \le p < \infty$. For every $i \in \mathbb{N}$ and every
$x \in \ell^p(\mathbb{N}, \mathbb{K})$, the $i$-th coordinate functional of the Schauder basis of
$\ell^p(\mathbb{N}, \mathbb{K})$ by unit vectors sends $x$ to its $i$-th entry $x_i$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpSchauderBasis_coord_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-schauder-basis-coord-apply).

## Basis vectors of the ℓᵖ Schauder basis

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $1 \le p < \infty$. For every $i \in \mathbb{N}$, the $i$-th basis vector of the Schauder
basis of $\ell^p(\mathbb{N}, \mathbb{K})$ by unit vectors is the unit vector $e_i$, the sequence
equal to $1$ at $i$ and to $0$ elsewhere.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpSchauderBasis_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-schauder-basis-apply).

## The ℓᵖ partial-sum projections are truncations

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $1 \le p < \infty$. For every $n \in \mathbb{N}$ and every
$x \in \ell^p(\mathbb{N}, \mathbb{K})$, the $n$-th partial-sum projection $P_n$ of the Schauder
basis of $\ell^p(\mathbb{N}, \mathbb{K})$ by unit vectors satisfies $P_n x = \sum_{i < n} x_i e_i$,
where $e_i$ is the unit vector equal to $1$ at $i$ and to $0$ elsewhere; that is, $P_n x$ is the
truncation of $x$ to its first $n$ coordinates.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.lpSchauderBasis_proj_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#lp-schauder-basis-proj-apply).

## The ℓᵖ partial-sum projections are contractions

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$ and let $1 \le p < \infty$. For every $n \in \mathbb{N}$ and every
$x \in \ell^p(\mathbb{N}, \mathbb{K})$, the $n$-th partial-sum projection $P_n$ of the Schauder
basis of $\ell^p(\mathbb{N}, \mathbb{K})$ by unit vectors satisfies $\|P_n x\| \le \|x\|$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.norm_lpSchauderBasis_classical_proj_apply_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#norm-lp-schauder-basis-classical-proj-ap).

## The ℓᵖ partial-sum projections have norm at most one

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$ and let $1 \le p < \infty$. For every $n \in \mathbb{N}$, the $n$-th partial-sum
projection of the Schauder basis of $\ell^p(\mathbb{N}, \mathbb{K})$ by unit vectors has operator
norm at most $1$.

Formalized by `MathlibExt.Analysis.Normed.Lp.SchauderBasis.norm_lpSchauderBasis_classical_proj_le`, a theorem declared in [MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Lp/SchauderBasis.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html#norm-lp-schauder-basis-classical-proj-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schauder basis of ℓ^p](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/schauder-basis-of-p)
