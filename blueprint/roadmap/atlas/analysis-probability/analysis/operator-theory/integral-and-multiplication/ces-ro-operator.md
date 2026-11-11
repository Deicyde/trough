---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.CesaroSpace, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroMean, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaro_den_ne_zero, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaro_den, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroMean_le, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.summable_norm_sq_cesaroMean, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.memℓp_cesaroMean, MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroLinearMap
statement: formalized
proof: formalized
---

# Cesàro operator

37 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html).

## The sequence space $\ell^2(\mathbb{N}, \mathbb{K})$

For $\mathbb{K}$ equal to $\mathbb{R}$
or $\mathbb{C}$, this is the space $\ell^2(\mathbb{N}, \mathbb{K})$ of square-summable sequences
$x : \mathbb{N} \to \mathbb{K}$, with the norm $\|x\| = \left(\sum_{n} |x(n)|^2\right)^{1/2}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.CesaroSpace`, an abbreviation declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-space).

## Cesàro means of a sequence

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. For a
sequence $x : \mathbb{N} \to \mathbb{K}$ and $n \in \mathbb{N}$, the $n$-th Cesàro mean of $x$ is
the average of its first $n + 1$ terms, $\frac{1}{n+1} \sum_{k=0}^{n} x(k)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroMean`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-mean).

## The Cesàro denominator $n + 1$ is nonzero

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
For every natural number $n$, the element $n + 1$ of $\mathbb{K}$ is nonzero.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaro_den_ne_zero`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-den-ne-zero).

## Norm of the Cesàro denominator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. For every
natural number $n$, the element $n + 1$ of $\mathbb{K}$ (the denominator of the $n$-th Cesàro
mean) has norm equal to the real number $n + 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaro_den`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-den).

## A Cesàro mean is bounded by the mean of the norms

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $x : \mathbb{N} \to \mathbb{K}$ be any sequence and let $n$ be a natural
number. Then $\|\frac{1}{n+1} \sum_{k=0}^{n} x_k\| \le \frac{1}{n+1} \sum_{k=0}^{n} \|x_k\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroMean_le`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-mean-le).

## Cesàro means of square-summable sequences are square-summable

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the Cesàro means
$\sigma_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$ satisfy: the series $\sum_n |\sigma_n|^2$ converges.

This follows from Hardy's inequality at $p = 2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.summable_norm_sq_cesaroMean`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#summable-norm-sq-cesaro-mean).

## Cesàro means preserve square-summability

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
If $x \in \ell^2(\mathbb{N}, \mathbb{K})$, then the sequence of its Cesàro means
$n \mapsto \frac{1}{n+1} \sum_{k=0}^{n} x_k$ also lies in $\ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.memℓp_cesaroMean`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#mem-p-cesaro-mean).

## The Cesàro operator as a linear map

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The Cesàro operator is the $\mathbb{K}$-linear map $C$ from $\ell^2(\mathbb{N}, \mathbb{K})$ to
itself that sends a sequence $x$ to its sequence of Cesàro means,
$(Cx)(n) = \frac{1}{n+1} \sum_{k=0}^{n} x(k)$ for $n \in \mathbb{N}$.

That $Cx$ is again square-summable follows from Hardy's inequality.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroLinearMap`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-linear-map).

## The Cesàro operator is bounded by 2

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and
let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$, viewed as a linear map, given
by $(Cx)_n = \frac{1}{n+1} \sum_{k=0}^{n} x_k$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$,
$\|Cx\| \le 2 \|x\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroLinearMap_le`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-linear-map-le).

## Cesàro operator on square-summable sequences

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. The Cesàro operator $C$ is the continuous linear map from
$\ell^2(\mathbb{N}, \mathbb{K})$ to itself that sends a sequence $x$ to its sequence of
averages, $(Cx)_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$. It is obtained from the Cesàro linear
map with the bound $\|Cx\| \le 2 \|x\|$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm).

## Formula for the Cesàro operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let
$C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $n \in \mathbb{N}$,
$(Cx)_n = \bigl(\sum_{k=0}^{n} x_k\bigr)/(n + 1)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-apply).

## Partial sums from Cesàro means

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and let
$C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $n \in \mathbb{N}$,
$\sum_{k=0}^{n} x(k) = (n+1)\,(Cx)(n)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaro_sum_eq`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-sum-eq).

## The Cesàro operator agrees with the Cesàro linear map

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$. For every $x \in \ell^2(\mathbb{N}, \mathbb{K})$, the Cesàro operator, as a
continuous linear map on $\ell^2(\mathbb{N}, \mathbb{K})$, takes the same value at $x$ as the
Cesàro linear map, the same averaging map considered only as a linear map.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_eq`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-eq).

## The Cesàro operator has norm at most 2

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The Cesàro operator $C$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = \frac{1}{n+1} \sum_{k=0}^{n} x_k$, has operator norm $\|C\| \le 2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroCLM_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-clm-le).

## The first standard basis vector of $\ell^2$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. The vector $e_0 \in \ell^2(\mathbb{N}, \mathbb{K})$ is the sequence with $e_0(0) = 1$
and $e_0(n) = 0$ for every $n \ge 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroE0`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-e0).

## Coordinates of the first standard basis vector of $\ell^2$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $e_0 \in \ell^2(\mathbb{N}, \mathbb{K})$ be the first standard
basis vector. For every $n \in \mathbb{N}$, $e_0(n) = 1$ if $n = 0$ and $e_0(n) = 0$ otherwise.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroE0_apply`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-e0-apply).

## The first basis vector is a unit vector

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The first standard basis vector $e_0 = (1, 0, 0, \dots)$ of $\ell^2(\mathbb{N}, \mathbb{K})$
has norm $\|e_0\| = 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroE0`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-e0).

## The Cesàro operator has norm at least one

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The Cesàro operator $C$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$, has operator norm $\|C\| \ge 1$.

This is seen on the first basis vector $e_0$, for which $\|e_0\| = 1$ and $(C e_0)_0 = 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.one_le_norm_cesaroCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#one-le-norm-cesaro-clm).

## One step of inverting the Cesàro operator

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, and let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$. For every
$x \in \ell^2(\mathbb{N}, \mathbb{K})$ and every $n \in \mathbb{N}$,
$x(n+1) = (n+2)\,(Cx)(n+1) - (n+1)\,(Cx)(n)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaro_preimage_succ`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-preimage-succ).

## The Cesàro operator is injective

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
Cesàro operator $C$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = (x_0 + \dots + x_n)/(n + 1)$, is injective.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_injective`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-injective).

## The alternating harmonic sequence in $\ell^2$

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. The sequence $y$ with $y(n) = (-1)^n / (n + 1)$ for $n \in \mathbb{N}$ is
square-summable, and it is regarded as an element of $\ell^2(\mathbb{N}, \mathbb{K})$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroNonRange`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-non-range).

## Coordinates of the alternating harmonic sequence in $\ell^2$

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $y$ be the alternating harmonic sequence, viewed as an
element of $\ell^2(\mathbb{N}, \mathbb{K})$. For every $n \in \mathbb{N}$,
$y(n) = (-1)^n / (n + 1)$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroNonRange_apply`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-non-range-apply).

## The Cesàro operator is not surjective

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The sequence $y \in \ell^2(\mathbb{N}, \mathbb{K})$ with $y_n = (-1)^n/(n + 1)$ is not in the
range of the Cesàro operator $C$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$. In particular $C$ is not surjective.

A preimage $x$ would have to satisfy $x_{n+1} = -2(-1)^n$ for all $n$, so it would not be
square-summable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.notMem_range_cesaroCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#not-mem-range-cesaro-clm).

## The Cesàro operator on standard basis vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$, let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$, and for
$n \in \mathbb{N}$ let $e_n$ be the standard basis vector with $1$ in coordinate $n$ and $0$
elsewhere. For all $n, k \in \mathbb{N}$, $(C e_n)_k = 1/(k + 1)$ if $n \le k$, and
$(C e_n)_k = 0$ if $k < n$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_single_apply`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-single-apply).

## Adjoint of the Cesàro operator

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$, and
let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = (x_0 + \dots + x_n)/(n + 1)$. For every $y \in \ell^2(\mathbb{N}, \mathbb{K})$ and
every $n \in \mathbb{N}$, the adjoint $C^*$ of $C$ satisfies

$$(C^* y)_n = \sum_{k=0}^{\infty} \frac{y_{n+k}}{n + k + 1}.$$

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaro_adjoint_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-adjoint-apply).

## The adjoint of the Cesàro operator fixes the first basis vector

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$,
and let $e_0 = (1, 0, 0, \dots)$ be the first standard basis vector. Then $C^* e_0 = e_0$, where
$C^*$ is the adjoint of $C$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaro_adjoint_single_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-adjoint-single-zero).

## Second coordinate of the Cesàro operator at the first basis vector

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$,
and let $e_0 = (1, 0, 0, \dots)$ be the first standard basis vector. With coordinates indexed
from $0$, $(C e_0)_1 = 1/2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_e0_apply_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-e0-apply-one).

## The Cesàro operator is not self-adjoint

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$.
The Cesàro operator $C$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$, is not self-adjoint.

Indeed, its adjoint fixes the first basis vector $e_0$, while $(C e_0)_1 = 1/2$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.not_isSelfAdjoint_cesaroCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#not-is-self-adjoint-cesaro-clm).

## Cesàro test vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $e_i$ be the
$i$-th standard basis vector of $\ell^2(\mathbb{N}, \mathbb{K})$. For a natural number $N$, the
test vector $t_N = \sum_{i < N} \frac{1}{\sqrt{N}} e_i$ has coordinate $1/\sqrt{N}$ at each
$j < N$ and $0$ at each $j \ge N$; in particular $t_0 = 0$.

These vectors are used to show that the Cesàro operator is not compact.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroTest`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-test).

## Coordinates of the Cesàro test vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$
and let $N$ and $j$ be natural numbers. The $j$-th coordinate of the Cesàro test vector
$t_N \in \ell^2(\mathbb{N}, \mathbb{K})$ is $1/\sqrt{N}$ if $j < N$, and $0$ if $j \ge N$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroTest_apply`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-test-apply).

## Norm of the Cesàro test-vector coefficient

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every natural number $N$, the norm of $(\sqrt{N})^{-1}$, computed in
$\mathbb{K}$, equals the real number $(\sqrt{N})^{-1}$; for $N = 0$ both sides are $0$, with the
convention $0^{-1} = 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroTest_sqrt`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-test-sqrt).

## The Cesàro test vectors are unit vectors

Let $\mathbb{K}$ be $\mathbb{R}$ or
$\mathbb{C}$. For every natural number $N \ge 1$, the test vector
$t_N \in \ell^2(\mathbb{N}, \mathbb{K})$, equal to $1/\sqrt{N}$ at the coordinates
$0, \dots, N - 1$ and to $0$ elsewhere, has norm $\|t_N\| = 1$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.norm_cesaroTest`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#norm-cesaro-test).

## The Cesàro operator on a test vector, within its support

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $C$ be the Cesàro operator on
$\ell^2(\mathbb{N}, \mathbb{K})$. For $N \in \mathbb{N}$ let $t_N$ be the test vector whose
first $N$ coordinates equal $1/\sqrt{N}$ and whose other coordinates are $0$. For all
$n, N \in \mathbb{N}$ with $n < N$, $(C t_N)_n = 1/\sqrt{N}$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_test_apply_lt`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-test-apply-lt).

## The Cesàro operator on a test vector, past its support

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, and let $C$ be the Cesàro operator on
$\ell^2(\mathbb{N}, \mathbb{K})$. For $N \in \mathbb{N}$ let $t_N$ be the test vector whose
first $N$ coordinates equal $(\sqrt{N})^{-1}$ and whose other coordinates are $0$. For all
$N, n \in \mathbb{N}$ with $N \le n$, $(C t_N)_n = N (\sqrt{N})^{-1}/(n + 1)$, where
$(\sqrt{0})^{-1}$ is read as $0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.cesaroCLM_test_apply_ge`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#cesaro-clm-test-apply-ge).

## Lower bound for the Cesàro operator on the test vectors

Let $\mathbb{K}$ be $\mathbb{R}$
or $\mathbb{C}$, let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$ and let $t_N$
be the $N$-th Cesàro test vector. For every natural number $N \ge 1$, $\|C t_N\|^2 \ge 5/4$.

The first $N$ coordinates of $C t_N$ contribute $1$ to $\|C t_N\|^2$, and the next $N$
contribute at least $1/4$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.five_div_four_le_norm_sq_cesaro_test`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#five-div-four-le-norm-sq-cesaro-test).

## The Cesàro images of the test vectors tend to zero coordinatewise

Let $\mathbb{K}$ be
$\mathbb{R}$ or $\mathbb{C}$, let $C$ be the Cesàro operator on $\ell^2(\mathbb{N}, \mathbb{K})$,
$(Cx)_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$, and for $N \ge 1$ let $t_N$ be the vector equal to
$1/\sqrt{N}$ at the coordinates $0, \dots, N - 1$ and to $0$ elsewhere. Then for every fixed
coordinate $n$, $(C t_{N+1})_n \to 0$ as $N \to \infty$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.tendsto_cesaro_test_coord_zero`, a lemma declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#tendsto-cesaro-test-coord-zero).

## The Cesàro operator is not compact

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$. The
Cesàro operator $C$ on $\ell^2(\mathbb{N}, \mathbb{K})$, given by
$(Cx)_n = (x_0 + x_1 + \dots + x_n)/(n + 1)$, is not a compact operator.

For $N \ge 1$ let $t_N$ be the unit vector equal to $1/\sqrt{N}$ at the coordinates
$0, \dots, N - 1$ and to $0$ elsewhere. Then $\|C t_N\|^2 \ge 5/4$ for every $N$, while each
coordinate of $C t_N$ tends to $0$ as $N \to \infty$, so no subsequence of $(C t_N)$ converges
in norm.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CesaroOperator.not_isCompactOperator_cesaroCLM`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CesaroOperator.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html#not-is-compact-operator-cesaro-clm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cesàro operator](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/ces-ro-operator)
