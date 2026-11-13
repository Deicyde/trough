---
declaration: section
origin: cited
lean: MetaMathlibExt.extendedContinuantFwd, MetaMathlibExt.extendedContinuantBwd, MetaMathlibExt.extendedContinuant, MetaMathlibExt.extendedContinuant_neg_two, MetaMathlibExt.extendedContinuant_neg_one, MetaMathlibExt.extendedContinuant_zero, MetaMathlibExt.extendedContinuant_recurrence, MetaMathlibExt.extendedContinuant_neg_three_to_six
statement: formalized
---

# Extended continuants and bi-infinite continued fractions

21 results, 8 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html).

## Forward branch of the extended continuant

For an integer sequence
$x : \mathbb{Z} \to \mathbb{Z}$ and an integer $b$, the forward branch with start index $b$ is the
sequence $(F_n)_{n \ge 0}$ of integers defined by $F_0 = 0$, $F_1 = 1$ and
$F_{n+2} = x_{b+n} F_{n+1} + F_n$. Its value $F_n$ is the extended continuant $K_{n-2}(x)_b$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Definition 3 (right-adjusting recurrence).

Formalized by `MetaMathlibExt.extendedContinuantFwd`, a definition declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-fwd).

## Backward branch of the extended continuant

For an integer sequence
$x : \mathbb{Z} \to \mathbb{Z}$ and an integer $b$, the backward branch with start index $b$ is
the sequence $(B_m)_{m \ge 0}$ of integers defined by $B_0 = 1$, $B_1 = 0$ and
$B_{m+2} = -x_{b-1-m} B_{m+1} + B_m$. Its value $B_m$ is the extended continuant
$K_{-1-m}(x)_b$ of negative order $-1-m$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Definition 4 (right-adjusting recurrence).

Formalized by `MetaMathlibExt.extendedContinuantBwd`, a definition declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-bwd).

## Extended continuants

Let $x : \mathbb{Z} \to \mathbb{Z}$ be a bi-infinite integer sequence
and $b$ an integer. The extended continuant $K_a(x)_b$ of order $a \in \mathbb{Z}$ with start index
$b$ (the paper's $K_a(x)_b^{a+b}$) is the integer defined by $K_{-2}(x)_b = 0$, $K_{-1}(x)_b = 1$,
the forward recurrence $K_a(x)_b = x_{b+a} K_{a-1}(x)_b + K_{a-2}(x)_b$ for $a \ge 0$, and the
backward recurrence $K_a(x)_b = K_{a+2}(x)_b - x_{b+a+2} K_{a+1}(x)_b$ for $a \le -3$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Definitions 3 and 4.

Formalized by `MetaMathlibExt.extendedContinuant`, a definition declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant).

## Extended continuants of order $-2$ vanish

For every bi-infinite integer sequence
$x : \mathbb{Z} \to \mathbb{Z}$ and every integer $b$, the extended continuant of order $-2$ with
start index $b$ is zero: $K_{-2}(x)_b = 0$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Definitions 3 and 4.

Formalized by `MetaMathlibExt.extendedContinuant_neg_two`, a theorem declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-neg-two).

## Extended continuant of order $-1$

For every integer sequence
$x : \mathbb{Z} \to \mathbb{Z}$ and every integer $b$, the extended continuant of $x$ of order
$-1$ with start index $b$ equals $1$, that is, $K_{-1}(x)_b = 1$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Definitions 3 and 4.

Formalized by `MetaMathlibExt.extendedContinuant_neg_one`, a theorem declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-neg-one).

## The extended continuant of order $0$ is a single term

For every bi-infinite integer
sequence $x : \mathbb{Z} \to \mathbb{Z}$ and every integer $b$, the extended continuant of order $0$
with start index $b$ is $K_0(x)_b = x_b$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Section 3.4 and Equation (13).

Formalized by `MetaMathlibExt.extendedContinuant_zero`, a theorem declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-zero).

## Recurrence for extended continuants

For every bi-infinite integer sequence
$x : \mathbb{Z} \to \mathbb{Z}$ and all integers $a$ and $b$, the extended continuants $K_a(x)_b$
of order $a$ with start index $b$ satisfy
$K_a(x)_b = x_{b+a} K_{a-1}(x)_b + K_{a-2}(x)_b$.

For $a \le -1$ this is the paper's backward recurrence of Definition 4.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Definitions 3 and 4 (RA versions).

Formalized by `MetaMathlibExt.extendedContinuant_recurrence`, a theorem declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-recurrence).

## Extended continuants of orders $-3$ to $-6$

Let $x : \mathbb{Z} \to \mathbb{Z}$ be an
integer sequence and write $K_a(x)_b$ for its extended continuant of order $a$ with start index
$b$. For every integer $h$, $K_{-3}(x)_h = 1$, $K_{-4}(x)_h = -x_{h-2}$,
$K_{-5}(x)_h = 1 + x_{h-3} x_{h-2}$ and
$K_{-6}(x)_h = -(x_{h-4} + x_{h-2} + x_{h-4} x_{h-3} x_{h-2})$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Lemma 1.

Formalized by `MetaMathlibExt.extendedContinuant_neg_three_to_six`, a theorem declared in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-neg-three-to-six).

## Westbound matrix product of extended continuants

Let $x : \mathbb{Z} \to \mathbb{Z}$ be a
bi-infinite integer sequence, write $K_a(x)_b$ for the extended continuant of order $a$ with start
index $b$, and put $M_i = \begin{pmatrix} 0 & 1 \\ 1 & -x_{-i} \end{pmatrix}$. Then for every
integer $n \ge 1$,

$$
M_n M_{n-1} \cdots M_1 =
\begin{pmatrix} K_{-n-1}(x)_0 & K_{-n-2}(x)_1 \\ K_{-n-2}(x)_0 & K_{-n-3}(x)_1 \end{pmatrix}.
$$

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Proposition 1.

Stated but not proved: `MetaMathlibExt.extendedContinuant_westbound_matrix_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-westbound-matrix-pro).

## Reflection formula for the order of extended continuants

Let
$x : \mathbb{Z} \to \mathbb{Z}$ be an integer sequence and write $K_a(x)_b$ for its extended
continuant of order $a$ with start index $b$. For all integers $h$ and $n$,

$$K_{-n}(x)_h = (-1)^{n+1} K_{n-4}(x)_{h-n+2}.$$

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 1.

Stated but not proved: `MetaMathlibExt.extendedContinuant_neg_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-neg-order).

## Bennett's continuant identity for nonnegative indices

Let $x : \mathbb{Z} \to \mathbb{Z}$
be an integer sequence and write $K_a(x)_b$ for its extended continuant of order $a$ with start
index $b$. For all nonnegative integers $k$, $\ell$, $m$, $n$,

$$(-1)^{k+\ell} K_{n-k-2}(x)_k K_{m-\ell-2}(x)_\ell +
(-1)^{\ell+m} K_{n-\ell-2}(x)_\ell K_{k-m-2}(x)_m +
(-1)^{m+k} K_{n-m-2}(x)_m K_{\ell-k-2}(x)_k = 0.$$

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 2 (after G. T. Bennett, 1939).

Stated but not proved: `MetaMathlibExt.extendedContinuant_bennett_nat` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-bennett-nat).

## Bennett's continuant identity for all integer indices

Let $x : \mathbb{Z} \to \mathbb{Z}$
be an integer sequence and write $K_a(x)_b$ for its extended continuant of order $a$ with start
index $b$. For all integers $k$, $\ell$, $m$, $n$,

$$(-1)^{k+\ell} K_{n-k-2}(x)_k K_{m-\ell-2}(x)_\ell +
(-1)^{\ell+m} K_{n-\ell-2}(x)_\ell K_{k-m-2}(x)_m +
(-1)^{m+k} K_{n-m-2}(x)_m K_{\ell-k-2}(x)_k = 0.$$

This extends Bennett's identity from nonnegative to arbitrary integer indices.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 3.

Stated but not proved: `MetaMathlibExt.extendedContinuant_bennett` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-bennett).

## Euler's continuant identity for extended continuants

Let $x : \mathbb{Z} \to \mathbb{Z}$
be an integer sequence and write $K_a(x)_b$ for its extended continuant of order $a$ with start
index $b$. For all integers $h$, $k$, $\ell$, $m$,

$$K_{\ell+m}(x)_h K_{k-1}(x)_{\ell+h+1} - K_{m-1}(x)_{\ell+h+1} K_{k+\ell}(x)_h =
(-1)^k K_{m-k-2}(x)_{k+\ell+h+2} K_{\ell-1}(x)_h.$$

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Corollary 1.

Stated but not proved: `MetaMathlibExt.extendedContinuant_euler` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-euler).

## Determinant identity for extended continuants

Let $x : \mathbb{Z} \to \mathbb{Z}$ be an
integer sequence and write $K_a(x)_b$ for its extended continuant of order $a$ with start index
$b$. For every integer $n$,

$$K_n(x)_0 K_{n-2}(x)_1 - K_{n-1}(x)_1 K_{n-1}(x)_0 = (-1)^{n+1}.$$

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Corollary 2.

Stated but not proved: `MetaMathlibExt.extendedContinuant_det` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#extended-continuant-det).

## No silent sequences of even order

Let $\sigma \ge 0$ be an even integer and write
$K_a(x)_b$ for the extended continuant of order $a$ with start index $b$. For all bi-infinite
integer sequences $x, z : \mathbb{Z} \to \mathbb{Z}$ it is not the case that
$K_{-i-\sigma-1}(x)_0 = K_i(z)_0$ and $K_{-i-\sigma-2}(x)_1 = K_{i-1}(z)_1$ for every natural
number $i$.

In the paper's terms: for even $\sigma$ no bi-infinite sequence $x$ is $\sigma$-silent, that is,
there is no sequence $z$ such that for every $i \ge 0$ the raw westbound convergent
$k_{-i-\sigma-1} = K_{-i-\sigma-1}(x)_0 / K_{-i-\sigma-2}(x)_1$ of $x$ is strictly equivalent
(equal numerators and equal denominators) to the raw convergent $d_i = K_i(z)_0 / K_{i-1}(z)_1$
of $z$. The BpCF conditions are not needed.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 4.

Stated but not proved: `MetaMathlibExt.not_silent_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#not-silent-of-even).

## Terms of a $1$-silent sequence

Let $x, y, z : \mathbb{Z} \to \mathbb{Z}$ be bi-infinite
integer sequences and write $K_a(x)_b$ for the extended continuant of order $a$ with start index
$b$. Suppose that for every natural number $i$, $K_i(x)_0 = K_i(y)_0$,
$K_{i-1}(x)_1 = K_{i-1}(y)_1$, $K_{-i-2}(x)_0 = K_i(z)_0$ and $K_{-i-3}(x)_1 = K_{i-1}(z)_1$.
Then $x_n = y_n$ for every $n \ge 0$, $x_{-n} = -z_n$ for every $n \ge 1$, and $z_0 = 0$.

In the paper's terms the hypotheses say that the raw convergents $k_i = K_i(x)_0 / K_{i-1}(x)_1$
of $x$ are strictly equivalent (equal numerators and equal denominators) to the raw convergents
$c_i$ of $y$, and $k_{-i-2}$ to the raw convergents $d_i$ of $z$, for all $i \ge 0$. The
conclusion $z_0 = 0$ matches the paper's $0 < \bar\alpha < 1$ for the EA-generated SCF of the
irrational $\bar\alpha$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 5.

Stated but not proved: `MetaMathlibExt.oneSilent_terms` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#one-silent-terms).

## Terms of 3-silent sequences

Let $x, y, z : \mathbb{Z} \to \mathbb{Z}$ be bi-infinite
integer sequences, and write $K_a(x)_b$ for the extended continuant of $x$ of order $a$ with start
index $b$. Suppose that for every natural number $i$ we have $K_i(x)_0 = K_i(y)_0$,
$K_{i-1}(x)_1 = K_{i-1}(y)_1$, $K_{-i-4}(x)_0 = K_i(z)_0$ and
$K_{-i-5}(x)_1 = K_{i-1}(z)_1$, and that $x_{-1} = 0$. Then $x_n = y_n$ for every $n \ge 0$, and
$x_{-n} = -z_{n-2}$ for every $n \ge 2$.

In the paper's terms, the hypotheses say that the raw convergents
$k_n = K_n(x)_0 / K_{n-1}(x)_1$ of $x$ satisfy $k_i \doteq c_i$ and $k_{-i-4} \doteq d_i$ for all
$i \ge 0$, where $c_i$ and $d_i$ are the corresponding raw convergents of $y$ and $z$ and $\doteq$
is equality of numerators and of denominators; the periodicity and limit conditions of a
bi-infinite periodic continued fraction are not assumed.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 6 and its proof (option 2, `x_{-1} = 0`).

Stated but not proved: `MetaMathlibExt.threeSilent_terms` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#three-silent-terms).

## Terms of a $\sigma$-silent sequence for odd $\sigma \ge 5$

Let $\sigma \ge 5$ be an odd
integer, let $x, y, z : \mathbb{Z} \to \mathbb{Z}$ be bi-infinite integer sequences, and write
$K_a(x)_b$ for the extended continuant of order $a$ with start index $b$. Suppose that for every
natural number $i$, $K_i(x)_0 = K_i(y)_0$, $K_{i-1}(x)_1 = K_{i-1}(y)_1$,
$K_{-i-\sigma-1}(x)_0 = K_i(z)_0$ and $K_{-i-\sigma-2}(x)_1 = K_{i-1}(z)_1$. Then $x_n = y_n$ for
every $n \ge 0$,
$x_{-\sigma+2} x_{-\sigma+1} = -1 + K_{\sigma-6}(x)_{-\sigma+4} + z_0 K_{\sigma-5}(x)_{-\sigma+4}$,
$x_{-\sigma+1} = -K_{\sigma-5}(x)_{-\sigma+3} - z_0 K_{\sigma-4}(x)_{-\sigma+3}$,
$x_{-\sigma} = -K_{\sigma-3}(x)_{-\sigma+2} - z_1$, and $x_{-n} = -z_{n-\sigma+1}$ for every integer
$n \ge \sigma + 1$.

The paper states the second formula as a quotient for $x_{-\sigma+2}$; here it is multiplied out.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Theorem 7.

Stated but not proved: `MetaMathlibExt.oddSilent_terms` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#odd-silent-terms).

## Silent-term formulas on table (33), case $\sigma \equiv 1 \pmod 6$

Let $\sigma \ge 7$ be
an integer with $\sigma \equiv 1 \pmod 6$, let $c_1 \ne c_2$ be integers, and let
$x : \mathbb{Z} \to \mathbb{Z}$ be a bi-infinite integer sequence with $x_{-3} = x_0 + c_1$,
$x_{-2} = 1$, $x_{-1} = -1$ and, for all integers $4 \le m \le \sigma - 3$, $x_{-m} = -1$ if
$m \equiv 1 \pmod 3$ and $x_{-m} = 1$ otherwise. Write $K_a(x)_b$ for the extended continuant of
order $a$ with start index $b$, and put $z_0 = x_0 + c_2$ and
$w = -K_{\sigma-5}(x)_{-\sigma+3} - z_0 K_{\sigma-4}(x)_{-\sigma+3}$. Then $w \ne 0$ and
$-1 + K_{\sigma-6}(x)_{-\sigma+4} + z_0 K_{\sigma-5}(x)_{-\sigma+4} = w$.

So formula (29) of Theorem 7, with $z_0 = x_0 + c_2$, gives $x_{-\sigma+1} = w \ne 0$ and
$x_{-\sigma+2} = 1$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Proposition 3 (case `σ ≡ 1 mod 6`).

Stated but not proved: `MetaMathlibExt.silentTerms_table_one_mod_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#silent-terms-table-one-mod-six).

## Silent-term formulas on table (33), case $\sigma \equiv 5 \pmod 6$

Let $\sigma \ge 7$ be
an integer with $\sigma \equiv 5 \pmod 6$, let $c_1 \ne c_2$ be integers, and let
$x : \mathbb{Z} \to \mathbb{Z}$ be a bi-infinite integer sequence with $x_{-3} = x_0 + c_1$,
$x_{-2} = 1$, $x_{-1} = -1$ and, for all integers $4 \le m \le \sigma - 3$, $x_{-m} = -1$ if
$m \equiv 2 \pmod 3$ and $x_{-m} = 1$ otherwise. Write $K_a(x)_b$ for the extended continuant of
order $a$ with start index $b$, and put $z_0 = x_0 + c_2$ and
$w = -K_{\sigma-5}(x)_{-\sigma+3} - z_0 K_{\sigma-4}(x)_{-\sigma+3}$. Then $w \ne 0$ and
$-1 + K_{\sigma-6}(x)_{-\sigma+4} + z_0 K_{\sigma-5}(x)_{-\sigma+4} = (1 + c_2 - c_1) w$.

So formula (29) of Theorem 7, with $z_0 = x_0 + c_2$, gives $x_{-\sigma+1} = w \ne 0$ and
$x_{-\sigma+2} = 1 + c_2 - c_1$.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Proposition 3 (case `σ ≡ 5 mod 6`).

Stated but not proved: `MetaMathlibExt.silentTerms_table_five_mod_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#silent-terms-table-five-mod-six).

## The conjugate continued fraction is not purely periodic

Let $P$, $Q$ and $D$ be integers
with $D > 0$ not a perfect square and $Q > 0$, and let $\bar\alpha = (P - \sqrt{D})/Q$. Then the
simple continued fraction $[a_0; a_1, a_2, \dots]$ of $\bar\alpha$, which is infinite because
$\bar\alpha$ is irrational, is not purely periodic: there is no integer $s \ge 1$ with
$a_{n+s} = a_n$ for all $n \ge 0$. Here $a_0 = \lfloor \bar\alpha \rfloor$ is included.

## Sources

- Dixon J. Jones, *Extended Continuants and Bi-infinite Periodic Continued Fractions*, INTEGERS 26 (2026), Article A73, Lemma 3.

Stated but not proved: `MetaMathlibExt.conjugate_continuedFraction_not_purelyPeriodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/ExtendedContinuantWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ExtendedContinuantWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html#conjugate-continued-fraction-not-purely).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extended continuants and bi-infinite continued fractions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/extended-continuants-and-bi-infinite-continued-f)
