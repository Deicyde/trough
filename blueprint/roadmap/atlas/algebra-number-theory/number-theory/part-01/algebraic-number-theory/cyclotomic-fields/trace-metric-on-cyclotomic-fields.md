---
declaration: section
origin: cited
lean: MetaMathlibExt.cyclotomicTraceNormSq, MetaMathlibExt.cyclotomicTraceNorm, MetaMathlibExt.cyclotomicTraceDist, MetaMathlibExt.cyclotomicLatticePoint, MetaMathlibExt.cyclotomicBox, MetaMathlibExt.cyclotomicDistMoment, MetaMathlibExt.cyclotomicTraceNormSq_zero, MetaMathlibExt.cyclotomicTraceNormSq_neg
statement: formalized
---

# Trace metric on cyclotomic fields

27 results, 14 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html).

## Squared trace norm on a cyclotomic field

Let $p$ be a positive integer, let $K$ be a
$p$-th cyclotomic extension of $\mathbb{Q}$, and let $\omega$ be the chosen primitive $p$-th root
of unity in $K$. The squared trace norm of $\alpha \in K$ is the rational number

$$\lVert \alpha \rVert^2 = \sum_{j=1}^{p-1} \mathrm{Tr}_{K/\mathbb{Q}}(\alpha \omega^j)^2.$$

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 1 (Definition 2.1 of arXiv:2410.22687).

Formalized by `MetaMathlibExt.cyclotomicTraceNormSq`, a definition declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-norm-sq).

## Trace norm on a cyclotomic field

Let $p$ be a positive integer, let $K$ be a $p$-th
cyclotomic extension of $\mathbb{Q}$, and let $\omega$ be the chosen primitive $p$-th root of
unity in $K$. The trace norm of $\alpha \in K$ is the real number

$$\|\alpha\| = \sqrt{\sum_{j=1}^{p-1} \mathrm{Tr}_{K/\mathbb{Q}}(\alpha \omega^j)^2},$$

the Euclidean length of the vector
$(\mathrm{Tr}_{K/\mathbb{Q}}(\alpha \omega^j))_{1 \le j \le p-1}$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 1 (Definition 2.1 of arXiv:2410.22687).

Formalized by `MetaMathlibExt.cyclotomicTraceNorm`, a definition declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-norm).

## Trace metric on a cyclotomic field

Let $p$ be a positive integer and let $K$ be a $p$-th
cyclotomic extension of $\mathbb{Q}$. The trace distance between $\alpha, \beta \in K$ is the real
number $d(\alpha, \beta) = \lVert \alpha - \beta \rVert$, where $\lVert \cdot \rVert$ is the trace
norm on $K$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 2 (Definition 2.2 of arXiv:2410.22687).

Formalized by `MetaMathlibExt.cyclotomicTraceDist`, a definition declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-dist).

## Lattice points of a cyclotomic field

Let $p$ be a positive integer, let $K$ be a $p$-th
cyclotomic extension of $\mathbb{Q}$, and let $\omega$ be the chosen primitive $p$-th root of
unity in $K$. For integers $a_1, \dots, a_{p-1}$, the lattice point with coefficients
$a_1, \dots, a_{p-1}$ is the element $a_1 \omega + a_2 \omega^2 + \cdots + a_{p-1} \omega^{p-1}$
of $K$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 1 (the box `B(p, N)`).

Formalized by `MetaMathlibExt.cyclotomicLatticePoint`, a definition declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-lattice-point).

## The cyclotomic box

For natural numbers $p$ and $N$, the box $B(p, N)$ is the finite set
of integer vectors $a = (a_1, \dots, a_{p-1}) \in \mathbb{Z}^{p-1}$ with $-N \le a_i \le N$ for
every $i$.

The vector $a$ stands for the point $a_1 \omega + \dots + a_{p-1} \omega^{p-1}$ of the $p$-th
cyclotomic field $\mathbb{Q}(\omega)$, where $\omega$ is a primitive $p$-th root of unity.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 1 (the box `B(p, N)`).

Formalized by `MetaMathlibExt.cyclotomicBox`, a definition declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-box).

## Moments of the trace distance on the cyclotomic box

Let $p \ge 1$, $N$ and $k$ be natural
numbers, and let $K$ be a field generated over $\mathbb{Q}$ by a primitive $p$-th root of unity,
with fixed primitive $p$-th root of unity $\omega \in K$. Let $d$ be the trace metric on $K$, given
by $d(\alpha, \beta) \ge 0$ and
$d(\alpha, \beta)^2 = \sum_{j=1}^{p-1} \mathrm{Tr}_{K/\mathbb{Q}}((\alpha - \beta) \omega^j)^2$.
Let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$ with $-N \le a_i \le N$
for all $i$, and write $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$. The $k$-th moment
of $d$ over $B(p, N)$ is the real number

$$
M_k(p, N) = \frac{1}{\lvert B(p, N) \rvert^2} \sum_{a \in B(p, N)} \sum_{b \in B(p, N)}
d(\alpha_a, \alpha_b)^k.
$$

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 6 (Definition 6.1 of arXiv:2410.22687).

Formalized by `MetaMathlibExt.cyclotomicDistMoment`, a definition declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-dist-moment).

## Squared trace norm of zero

Let $p$ be a positive integer and let $K$ be a $p$-th
cyclotomic extension of $\mathbb{Q}$. The squared trace norm of $0 \in K$ is $0$, that is,
$\lVert 0 \rVert^2 = 0$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 1.

Formalized by `MetaMathlibExt.cyclotomicTraceNormSq_zero`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-norm-sq-zero).

## The squared trace norm is invariant under negation

Let $p$ be a positive integer and
let $K$ be a $p$-th cyclotomic extension of $\mathbb{Q}$. For every $\alpha \in K$, the squared
trace norm satisfies $\lVert -\alpha \rVert^2 = \lVert \alpha \rVert^2$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 1.

Formalized by `MetaMathlibExt.cyclotomicTraceNormSq_neg`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-norm-sq-neg).

## Trace distance from a point to itself

Let $p$ be a positive integer and let $K$ be a
$p$-th cyclotomic extension of $\mathbb{Q}$. For every $\alpha \in K$, the trace distance satisfies
$d(\alpha, \alpha) = 0$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 2.

Formalized by `MetaMathlibExt.cyclotomicTraceDist_self`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-dist-self).

## Symmetry of the trace metric

Let $p$ be a positive integer and let $K$ be a $p$-th
cyclotomic extension of $\mathbb{Q}$. For all $\alpha, \beta \in K$, the trace distance satisfies
$d(\alpha, \beta) = d(\beta, \alpha)$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Definition 2.

Formalized by `MetaMathlibExt.cyclotomicTraceDist_comm`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-dist-comm).

## The zero coefficient vector gives the zero lattice point

Let $p \ge 1$ be a natural
number and let $K$ be a field generated over $\mathbb{Q}$ by a primitive $p$-th root of unity, with
fixed primitive $p$-th root of unity $\omega \in K$. For an integer vector
$a = (a_1, \dots, a_{p-1})$ write $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$. Then
$\alpha_0 = 0$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 1 (the box `B(p, N)`).

Formalized by `MetaMathlibExt.cyclotomicLatticePoint_zero`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-lattice-point-zero).

## The cyclotomic box of radius zero

Let $p$ be a natural number and, for a natural number
$N$, let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$ with
$-N \le a_i \le N$ for all $i$. Then $B(p, 0) = \{0\}$: the zero vector is the only element of the
box of radius $0$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 1 (the box `B(p, N)`).

Formalized by `MetaMathlibExt.cyclotomicBox_zero`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-box-zero).

## The zero vector lies in every box

For all natural numbers $p$ and $N$, the zero vector
lies in the box $B(p, N)$, the set of integer vectors $(a_1, \dots, a_{p-1})$ with
$|a_i| \le N$ for all $i$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 1 (the box `B(p, N)`).

Formalized by `MetaMathlibExt.zero_mem_cyclotomicBox`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#zero-mem-cyclotomic-box).

## The zeroth moment of the trace distance is one

Let $p \ge 1$ and $N$ be natural numbers,
and let $K$ be a field generated over $\mathbb{Q}$ by a primitive $p$-th root of unity, with fixed
primitive $p$-th root of unity $\omega \in K$. Let $d$ be the trace metric on $K$, given by
$d(\alpha, \beta) \ge 0$ and
$d(\alpha, \beta)^2 = \sum_{j=1}^{p-1} \mathrm{Tr}_{K/\mathbb{Q}}((\alpha - \beta) \omega^j)^2$.
Let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$ with $-N \le a_i \le N$
for all $i$, write $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$, and let
$M_k(p, N) = \lvert B(p, N) \rvert^{-2} \sum_{a, b \in B(p, N)} d(\alpha_a, \alpha_b)^k$ be the
$k$-th moment of $d$ over $B(p, N)$. Then $M_0(p, N) = 1$, with the convention $0^0 = 1$ for
coinciding points.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Section 6 (Definition 6.1 of arXiv:2410.22687).

Formalized by `MetaMathlibExt.cyclotomicDistMoment_zero`, a theorem declared in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-dist-moment-zero).

## Galois invariance of the trace metric

Let $p$ be a prime and let $K$ be a $p$-th
cyclotomic extension of $\mathbb{Q}$. For every $\mathbb{Q}$-algebra automorphism $\sigma$ of $K$
and all $\alpha, \beta \in K$, the trace distance satisfies
$d(\sigma \alpha, \sigma \beta) = d(\alpha, \beta)$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Proposition 1.

Stated but not proved: `MetaMathlibExt.cyclotomicTraceDist_algEquiv` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-dist-alg-equiv).

## The trace norm is a norm

Let $p$ be a prime and let $K$ be a $p$-th cyclotomic extension
of $\mathbb{Q}$, viewed as a $\mathbb{Q}$-vector space. The trace norm $\lVert \cdot \rVert$ on $K$
is a norm: for all $\alpha, \beta \in K$ and $q \in \mathbb{Q}$, we have
$\lVert \alpha \rVert = 0$ if and only if $\alpha = 0$,
$\lVert \alpha + \beta \rVert \le \lVert \alpha \rVert + \lVert \beta \rVert$, and
$\lVert q \alpha \rVert = |q| \, \lVert \alpha \rVert$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Theorem 2.

Stated but not proved: `MetaMathlibExt.cyclotomicTraceNorm_isNorm` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-norm-is-norm).

## Krasner-type lemma for the cyclotomic trace metric

Let $p$ be a prime and let $K$ be a
field generated over $\mathbb{Q}$ by a primitive $p$-th root of unity, with fixed primitive $p$-th
root of unity $\omega \in K$. Write $d(\alpha, \beta) = \lVert \alpha - \beta \rVert$ for the trace
metric on $K$, where $\lVert \gamma \rVert \ge 0$ and
$\lVert \gamma \rVert^2 = \sum_{j=1}^{p-1} \operatorname{Tr}_{K/\mathbb{Q}}(\gamma \omega^j)^2$.
Let $\alpha, \beta \in K$ and suppose that $d(\alpha, \beta) < d(\alpha, \sigma(\alpha)) / 2$ for
every automorphism $\sigma$ of $K$ over $\mathbb{Q}$ with $\sigma(\alpha) \ne \alpha$. Then
$\mathbb{Q}(\alpha) \subseteq \mathbb{Q}(\beta)$ as subfields of $K$.

Since $K / \mathbb{Q}$ is Galois, the elements $\sigma(\alpha) \ne \alpha$ are exactly the
conjugates of $\alpha$ over $\mathbb{Q}$ other than $\alpha$ itself.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Theorem 4.

Stated but not proved: `MetaMathlibExt.adjoin_le_adjoin_of_cyclotomicTraceDist_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#adjoin-le-adjoin-of-cyclotomic-trace-dis).

## Primitive elements α + nβ in a prime cyclotomic field

Let $p$ be a prime and let $K$
be a $p$-th cyclotomic extension of $\mathbb{Q}$. For all $\alpha, \beta \in K$ there is a
natural number $n_0$ such that, for every natural number $n \ge n_0$, the subfields
$\mathbb{Q}(\alpha + n\beta)$ and $\mathbb{Q}(\alpha, \beta)$ of $K$ are equal.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Corollary 1.

Stated but not proved: `MetaMathlibExt.eventually_adjoin_add_nsmul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#eventually-adjoin-add-nsmul-eq).

## Squared trace norm in coordinates

Let $p$ be a prime, let $K$ be a $p$-th cyclotomic
extension of $\mathbb{Q}$, let $\omega$ be the chosen primitive $p$-th root of unity in $K$, and
let $\mathrm{Tr}$ be the trace from $K$ to $\mathbb{Q}$. For rational numbers
$a_1, \dots, a_{p-1}$, put $\alpha = a_1 \omega + a_2 \omega^2 + \cdots + a_{p-1} \omega^{p-1}$
and $\lVert \alpha \rVert_E^2 = a_1^2 + a_2^2 + \cdots + a_{p-1}^2$. Then the squared trace
norm of $\alpha$ satisfies

$$\lVert \alpha \rVert^2 = p^2 \lVert \alpha \rVert_E^2 - (p + 1) \mathrm{Tr}(\alpha)^2,$$

and $\lVert \alpha \rVert_E^2 \le \lVert \alpha \rVert^2$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 1.

Stated but not proved: `MetaMathlibExt.cyclotomicTraceNormSq_eq_and_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-trace-norm-sq-eq-and-ge).

## Diameter of the cyclotomic box

Let $p$ be an odd prime, let $N$ be a natural number, and
let $K$ be a field generated over $\mathbb{Q}$ by a primitive $p$-th root of unity, with fixed
primitive $p$-th root of unity $\omega \in K$. Let $d(\alpha, \beta) = \lVert \alpha - \beta \rVert$
be the trace metric on $K$, where $\lVert \gamma \rVert \ge 0$ and
$\lVert \gamma \rVert^2 = \sum_{j=1}^{p-1} \operatorname{Tr}_{K/\mathbb{Q}}(\gamma \omega^j)^2$.
Let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$ with $-N \le a_i \le N$
for all $i$, and write $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$. Then
$d(\alpha_a, \alpha_b) \le 2 N p \sqrt{p - 1}$ for all $a, b \in B(p, N)$, and this bound is
attained: $d(\alpha, -\alpha) = 2 N p \sqrt{p - 1}$ for
$\alpha = N \omega - N \omega^2 + \dots + N \omega^{p-2} - N \omega^{p-1}$, the point whose
coefficient of $\omega^i$ is $(-1)^{i-1} N$.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 2.

Stated but not proved: `MetaMathlibExt.cyclotomicBox_diam` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-box-diam).

## Power sums over a symmetric interval

For natural numbers $N$ and $r$, let
$S_r(N) = \sum_{a=-N}^{N} a^r$, the sum over the integers $a$ with $-N \le a \le N$. Then
$S_r(N) = 0$ for every odd $r$, and

$$S_2(N) = \frac{N(N+1)(2N+1)}{3}, \qquad S_4(N) = \frac{N(N+1)(2N+1)(3N^2+3N-1)}{15}.$$

The paper takes $N \ge 1$; here $N = 0$ is allowed.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 3.

Stated but not proved: `MetaMathlibExt.symmetric_power_sums` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#symmetric-power-sums).

## Second moment of the trace distance on the cyclotomic box

Let $p$ be a prime, let $N$ be
a natural number, and let $K$ be a field generated over $\mathbb{Q}$ by a primitive $p$-th root of
unity, with fixed primitive $p$-th root of unity $\omega \in K$. Let $M_2(p, N)$ be the second
moment of the trace metric $d$ of $K$ over the box $B(p, N)$: the average of
$d(\alpha_a, \alpha_b)^2$ over all pairs $(a, b)$ of integer vectors in $\mathbb{Z}^{p-1}$ whose
coordinates lie in $[-N, N]$, where $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$ and
$d(\alpha, \beta)^2 = \sum_{j=1}^{p-1} \mathrm{Tr}_{K/\mathbb{Q}}((\alpha - \beta) \omega^j)^2$.
Then $M_2(p, N) = \frac{2}{3} (p^3 - 2 p^2 + 1) N (N + 1)$.

The asymptotic form $M_2(p, N) = \frac{2}{3} p^3 N^2 + O(p^2 N^2 + p^3 N)$ follows from this
exact formula.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 4.

Stated but not proved: `MetaMathlibExt.cyclotomicDistMoment_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-dist-moment-two).

## Fourth-power sum of coordinate differences over a box

Let $p$ be a prime and $N$ a
natural number, and let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$
with $|a_i| \le N$ for all $i$. Then

$$\sum_{i=1}^{p-1} \sum_{j=1}^{p-1} \sum_{a, b \in B(p, N)} (a_i - b_i)^2 (a_j - b_j)^2 =
(2N+1)^{2(p-1)} \cdot \tfrac{2}{45} N (N+1) (p-1) (10N^2 p + 4N^2 + 10Np + 4N - 3).$$

This corrects the paper's printed right side, which omits the factor $(2N+1)^{2(p-1)}$: for
$p = 3$ and $N = 1$ the sum is $936$, while the printed right side is $104/9$. The paper's own
proof carries the factors $(2N+1)^{2p-4}$ and $(2N+1)^{2p-6}$ in its pieces (10) and (11), and
combining them gives the value above; the printed formula is the sum divided by
$|B(p, N)|^2 = (2N+1)^{2(p-1)}$. The paper takes $p$ an odd prime; here only $p$ prime is
assumed.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 5.

Stated but not proved: `MetaMathlibExt.sum_sq_sub_mul_sq_sub_box` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#sum-sq-sub-mul-sq-sub-box).

## Fourth moment of the trace distance on the cyclotomic box

Let $p$ be a prime, let $N$ be
a natural number, and let $K$ be a field generated over $\mathbb{Q}$ by a primitive $p$-th root of
unity, with fixed primitive $p$-th root of unity $\omega \in K$. Let $M_4(p, N)$ be the fourth
moment of the trace metric $d$ of $K$ over the box $B(p, N)$: the average of
$d(\alpha_a, \alpha_b)^4$ over all pairs $(a, b)$ of integer vectors in $\mathbb{Z}^{p-1}$ whose
coordinates lie in $[-N, N]$, where $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$ and
$d(\alpha, \beta)^2 = \sum_{j=1}^{p-1} \mathrm{Tr}_{K/\mathbb{Q}}((\alpha - \beta) \omega^j)^2$.
Then

$$
M_4(p, N) = \frac{2}{45} N (N + 1) (p - 1) \bigl( (2 N^2 + 2 N)
(5 p^5 - 8 p^4 + p^3 + 8 p^2 - 21 p - 18) - 3 (p^2 - p - 1)^2 \bigr).
$$

The asymptotic form $M_4(p, N) = \frac{4}{9} p^6 N^4 + O(p^5 N^4 + p^6 N^3)$ follows from this
exact formula.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 6.

Stated but not proved: `MetaMathlibExt.cyclotomicDistMoment_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-dist-moment-four).

## Variance bound for squared trace distances in the box

There is a real number $C$
such that the following holds for every prime $p$, every integer $N \ge 1$ and every $p$-th
cyclotomic extension $K$ of $\mathbb{Q}$. Let $\omega$ be the chosen primitive $p$-th root of
unity in $K$, let $d$ be the trace distance on $K$, and let $B(p, N)$ be the set of integer
vectors $a = (a_1, \dots, a_{p-1})$ with $|a_i| \le N$ for all $i$, where $a$ stands for the
point $a_1 \omega + \dots + a_{p-1} \omega^{p-1}$ of $K$. Then

$$R(p, N) = \frac{1}{|B(p, N)|^2} \sum_{\alpha, \beta \in B(p, N)}
\left( d(\alpha, \beta)^2 - \tfrac{2}{3} p^3 N^2 \right)^2 \le
C \left( p^5 N^4 + p^6 N^3 \right).$$

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Lemma 7.

Stated but not proved: `MetaMathlibExt.exists_cyclotomicDist_variance_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#exists-cyclotomic-dist-variance-le).

## Almost all pairs in the cyclotomic box are nearly equidistant

For every real
$\varepsilon > 0$ there is a natural number $A$ with the following property. Let $p$ be a prime
and $N$ a natural number with $p > A$ and $N > A$, and let $K$ be a field generated over
$\mathbb{Q}$ by a primitive $p$-th root of unity, with fixed primitive $p$-th root of unity
$\omega \in K$. Let $d(\alpha, \beta) = \lVert \alpha - \beta \rVert$ be the trace metric on $K$,
where $\lVert \gamma \rVert \ge 0$ and
$\lVert \gamma \rVert^2 = \sum_{j=1}^{p-1} \operatorname{Tr}_{K/\mathbb{Q}}(\gamma \omega^j)^2$.
Let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$ with $-N \le a_i \le N$
for all $i$, and write $\alpha_a = a_1 \omega + \dots + a_{p-1} \omega^{p-1}$. Then fewer than
$\varepsilon \lvert B(p, N) \rvert^2$ pairs $(a, b) \in B(p, N)^2$ satisfy

$$
\left| \frac{d(\alpha_a, \alpha_b)}{2 N p \sqrt{p - 1}} - \frac{1}{\sqrt{6}} \right| > \varepsilon.
$$

The constant $A$ depends only on $\varepsilon$; it is not claimed to be effectively computable.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Theorem 1.

Stated but not proved: `MetaMathlibExt.cyclotomicBox_almost_equidistant` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#cyclotomic-box-almost-equidistant).

## Concentration of trace distances in the box, quantitative form

There is a real
number $C$ such that the following holds for every real $\varepsilon > 0$, every prime $p$,
every integer $N \ge 1$ and every $p$-th cyclotomic extension $K$ of $\mathbb{Q}$. Let $\omega$
be the chosen primitive $p$-th root of unity in $K$, let $d$ be the trace distance on $K$, and
let $B(p, N)$ be the set of integer vectors $a = (a_1, \dots, a_{p-1})$ with $|a_i| \le N$ for
all $i$, where $a$ stands for the point $a_1 \omega + \dots + a_{p-1} \omega^{p-1}$ of $K$.
Among all pairs $(\alpha, \beta) \in B(p, N)^2$, the proportion of pairs with

$$\left| \frac{d(\alpha, \beta)}{2 N p^{3/2}} - \frac{1}{\sqrt{6}} \right| > \varepsilon$$

is at most $C \varepsilon^{-2} (1/p + 1/N)$.

The paper takes $p$ odd; here $p = 2$ is allowed. The paper also shows that $C$ is
effectively computable; only its existence is stated here.

## Sources

- Saettone, Zaharescu and Zhang, *On a Special Metric in Cyclotomic Fields*, INTEGERS 25 (2025), Article A10, Theorem 5.

Stated but not proved: `MetaMathlibExt.exists_cyclotomicBox_deviation_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicTraceMetricWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html#exists-cyclotomic-box-deviation-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Trace metric on cyclotomic fields](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/trace-metric-on-cyclotomic-fields)
