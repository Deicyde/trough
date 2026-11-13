---
declaration: section
origin: cited
lean: MetaMathlibExt.overpartitionCount, MetaMathlibExt.nonOverlinedCount, MetaMathlibExt.leastGapOverpartition, MetaMathlibExt.D3, MetaMathlibExt.sigmaMexOverpartition, MetaMathlibExt.overpartitionCount_zero, MetaMathlibExt.D3_zero, MetaMathlibExt.D3_one
statement: formalized
---

# Minimal excludant of overpartitions

18 results, 9 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html).

## Number of overpartitions

For a natural number $n$, $\overline{p}(n)$ is the number of
overpartitions of $n$, that is, of pairs consisting of a partition $p$ of $n$ and a set of
overlined part sizes, each of which occurs as a part of $p$. For example, $\overline{p}(3) = 8$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Section 1.

Formalized by `MetaMathlibExt.overpartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#overpartition-count).

## Number of non-overlined copies of a part size

For an overpartition $O$ of $n$ and a natural
number $a$, the number of non-overlined parts of size $a$ in $O$ is the multiplicity of $a$ in the
underlying partition of $O$, minus $1$ if $a$ is overlined in $O$ and minus $0$ otherwise.

This matches the convention that only the first occurrence of a part size may be overlined: an
overpartition records each overlined size once.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definition of `mex̄_r`.

Formalized by `MetaMathlibExt.nonOverlinedCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#non-overlined-count).

## Minimal excludant of an overpartition with a multiplicity bound

For natural numbers $r \ge 1$
and $n$ and an overpartition $O$ of $n$, $\overline{\mathrm{mex}}_r(O)$ is the least positive
integer $k$ that occurs fewer than $r$ times among the non-overlined parts of $O$. Such a $k$
exists, since $n + 1$ is not a part of $O$. For $r = 0$, which the paper does not use, the value
is $0$ by convention.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definition of `mex̄_r`.

Formalized by `MetaMathlibExt.leastGapOverpartition`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#least-gap-overpartition).

## Three-colored distinct-part partitions

For a natural number $n$, $D_3(n)$ is the number of
triples $(A, B, C)$ of subsets of $\{1, \dots, n\}$ such that the sum of the elements of $A$, the
sum of the elements of $B$ and the sum of the elements of $C$ add up to $n$. Here $A$, $B$, $C$
are the parts of the three colors of a partition of $n$ whose parts of each color are distinct.

A size may occur in several colors but at most once in each, as in the product
$\prod_{m \ge 1} (1 + q^m)^3$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definition of `D_3(n)`.

Formalized by `MetaMathlibExt.D3`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#d3).

## Sums of minimal excludants over overpartitions

For natural numbers $r$ and $n$,
$\sigma_r\overline{\mathrm{mex}}(n)$ is the sum, over all overpartitions $\pi$ of $n$, of
$\overline{\mathrm{mex}}_r(\pi)$, the least positive integer occurring fewer than $r$ times
among the non-overlined parts of $\pi$; for $r = 0$ the value $\overline{\mathrm{mex}}_0(\pi)$
is $0$ by convention, so $\sigma_0\overline{\mathrm{mex}}(n) = 0$. We write
$\sigma\overline{\mathrm{mex}}(n) = \sigma_1\overline{\mathrm{mex}}(n)$.

By direct enumeration, $\sigma\overline{\mathrm{mex}}(n) = 1, 3, 6, 13, 24$ for $n = 0, \dots, 4$,
and $\sigma_2\overline{\mathrm{mex}}(2) = 5$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definitions of `σmex̄` and `σ_r mex̄`.

Formalized by `MetaMathlibExt.sigmaMexOverpartition`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition).

## The number of overpartitions of zero

The number $\overline{p}(0)$ of overpartitions of
$0$ equals $1$: the empty overpartition is the only one.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Section 1 (`p̄(0) = 1`).

Formalized by `MetaMathlibExt.overpartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#overpartition-count-zero).

## Three-colored distinct-part partitions of $0$

The number $D_3(0)$ of partitions of $0$ into
parts of three colors, with the parts of each color distinct, equals $1$: the empty partition is
the only one.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definition of `D_3(n)`.

Formalized by `MetaMathlibExt.D3_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#d3-zero).

## Three-colored distinct-part partitions of $1$

The number $D_3(1)$ of partitions of $1$ into
parts of three colors, with the parts of each color distinct, equals $3$: the single part $1$
takes one of the three colors.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definition of `D_3(n)`.

Formalized by `MetaMathlibExt.D3_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#d3-one).

## Three-colored distinct-part partitions of $2$

The number $D_3(2)$ of partitions of $2$ into
parts of three colors, with the parts of each color distinct, equals $6$: the single part $2$ in
one of three colors, or two parts $1$ in two different colors.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Definition of `D_3(n)`.

Formalized by `MetaMathlibExt.D3_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#d3-two).

## The overpartition mex sum counts three-colored distinct-part partitions

For an
overpartition $\pi$, let $\overline{\mathrm{mex}}(\pi)$ be the least positive integer that does
not occur among the non-overlined parts of $\pi$, and let $\sigma\overline{\mathrm{mex}}(n)$ be
the sum of $\overline{\mathrm{mex}}(\pi)$ over all overpartitions $\pi$ of $n$. For every
positive integer $n$, $\sigma\overline{\mathrm{mex}}(n) = D_3(n)$, the number of partitions of
$n$ into distinct parts in three colors: the number of triples $(A, B, C)$ of subsets of
$\{1, \dots, n\}$ whose three element sums add up to $n$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Theorem 2.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_eq_D3` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-eq-d3).

## Asymptotic formula for the overpartition mex sum

Let $\sigma\overline{\mathrm{mex}}(n)$ be
the sum, over all overpartitions $\pi$ of $n$, of $\overline{\mathrm{mex}}(\pi)$, the least
positive integer that does not occur among the non-overlined parts of $\pi$. Then
$\sigma\overline{\mathrm{mex}}(n) \sim e^{\pi\sqrt{n}} / (8 n^{3/4})$ as $n \to \infty$, that is,
the ratio of the two sides tends to $1$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Theorem 3.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_asymptotic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-asymptotic).

## Parity of the overpartition mex sum

For an overpartition $\pi$, let
$\overline{\mathrm{mex}}(\pi)$ be the least positive integer that does not occur among the
non-overlined parts of $\pi$, and let $\sigma\overline{\mathrm{mex}}(n)$ be the sum of
$\overline{\mathrm{mex}}(\pi)$ over all overpartitions $\pi$ of $n$. For every positive integer
$n$, $\sigma\overline{\mathrm{mex}}(n)$ is odd if $n = j(j+1)/2$ is a triangular number for some
natural number $j$, and even otherwise.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Theorem 4.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_parity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-parity).

## Generating function of the overpartition r-mex sums

Let $r$ be a positive integer and $q$
a complex number with $|q| < 1$. Write $(a;q)_\infty = \prod_{j \ge 0} (1 - a q^j)$, and let
$\sigma_r\overline{\mathrm{mex}}(n)$ be the sum over all overpartitions $\pi$ of $n$ of
$\overline{\mathrm{mex}}_r(\pi)$, the least positive integer occurring fewer than $r$ times among
the non-overlined parts of $\pi$. Then

$$
\sum_{n \ge 0} \sigma_r\overline{\mathrm{mex}}(n)\, q^n =
\frac{(-q;q)_\infty\,(q^{2r};q^{2r})_\infty}{(q;q)_\infty\,(q^r;q^{2r})_\infty}.
$$

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Theorem 6.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_generating_function` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-generating-funct).

## Asymptotic formula for the overpartition r-mex sums

Let $r$ be a positive integer and let
$\sigma_r\overline{\mathrm{mex}}(n)$ be the sum over all overpartitions $\pi$ of $n$ of
$\overline{\mathrm{mex}}_r(\pi)$, the least positive integer occurring fewer than $r$ times among
the non-overlined parts of $\pi$. Then
$\sigma_r\overline{\mathrm{mex}}(n) \sim e^{\pi\sqrt{n}} / (8 \sqrt{r}\, n^{3/4})$ as
$n \to \infty$, that is, the ratio of the two sides tends to $1$.

The denominator $8\sqrt{r}$ follows the published version of the paper; arXiv v1 prints $8r$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Theorem 7.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_r_asymptotic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-r-asymptotic).

## Density of overpartition r-mex sums divisible by powers of two

Let $m$, $e$ and $k$ be
natural numbers with $k \ge 1$, let $r = 2^m 3^e$, and let
$\sigma_r\overline{\mathrm{mex}}(n)$ be the sum over all overpartitions $\pi$ of $n$ of
$\overline{\mathrm{mex}}_r(\pi)$, the least positive integer occurring fewer than $r$ times among
the non-overlined parts of $\pi$. Then the natural numbers $n$ with
$2^k \mid \sigma_r\overline{\mathrm{mex}}(n)$ have natural density $1$: the number of such $n$
with $n \le X$, divided by $X$, tends to $1$ as $X \to \infty$.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Theorem 8.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_power_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-power-density).

## Ingham's Tauberian theorem

Let $a : \mathbb{N} \to \mathbb{R}$ be nonnegative and weakly
increasing, let $A : \mathbb{C} \to \mathbb{C}$ be a function, and let $\alpha$, $\beta$, $C$
be real numbers with $C > 0$. Suppose that for every complex $q$ with $|q| < 1$ the series
$\sum_{n \ge 0} a(n) q^n$ is summable with sum $A(q)$, and that for every complex $q$ with
$|q| > 1$ it is not summable. Suppose also that $A(e^{-t}) \sim \alpha t^\beta e^{C/t}$ as
$t \to 0^+$ through positive reals, and that for every $\Delta > 0$,
$A(e^{-z}) = O(|z|^\beta e^{C/|z|})$ as $z \to 0$ within the cone
$\{z \in \mathbb{C} : \mathrm{Re}\, z > 0,\ |\mathrm{Im}\, z| \le \Delta\, \mathrm{Re}\, z\}$.
Then, as $n \to \infty$,

$$a(n) \sim \frac{\alpha}{2\sqrt{\pi}} C^{(2\beta + 1)/4} n^{-(2\beta + 3)/4} e^{2\sqrt{Cn}}.$$

Nothing is assumed about the series on the circle $|q| = 1$, since radius of convergence one
permits either behavior there.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Proposition 9.

Stated but not proved: `MetaMathlibExt.ingham_tauberian` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#ingham-tauberian).

## The r-mex sum of overpartitions as a sum of overpartition counts

Let $n$ and $r$ be
natural numbers with $r \ge 1$, let $\overline{p}(m)$ be the number of overpartitions of $m$, let
$T_k = k(k+1)/2$ be the $k$-th triangular number, and let $\sigma_r\overline{\mathrm{mex}}(n)$ be
the sum over all overpartitions $\pi$ of $n$ of $\overline{\mathrm{mex}}_r(\pi)$, the least
positive integer occurring fewer than $r$ times among the non-overlined parts of $\pi$. Then

$$\sigma_r\overline{\mathrm{mex}}(n) = \sum_{k \ge 0,\; rT_k \le n} \overline{p}(n - rT_k).$$

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Proposition 10.

Stated but not proved: `MetaMathlibExt.sigmaMexOverpartition_eq_sum_shifted_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#sigma-mex-overpartition-eq-sum-shifted-c).

## Eta-quotient congruence for sums of overpartition minimal excludants

Let $r \ge 1$ and
$k \ge 1$ be integers, and for $n \ge 0$ let $\sigma_r \overline{\mathrm{mex}}(n)$ be the sum, over
all overpartitions of $n$, of the least positive integer occurring fewer than $r$ times among the
non-overlined parts. Then there are integers $c_0, c_1, c_2, \dots$ such that for every complex $q$
with $|q| < 1$, writing $f_d = (q^d; q^d)_\infty = \prod_{m \ge 1} (1 - q^{dm})$,

$$q^{3r} \frac{f_{48} f_{24r}^{2^k - 1}}{f_{24}^2 f_{48r}^{2^{k-1} - 2}} = \sum_{j \ge 0} c_j q^j,$$

and for every $j \ge 0$ we have $c_j \equiv \sigma_r \overline{\mathrm{mex}}(n) \pmod{2^k}$ when
$j = 24n + 3r$ with $n \ge 0$, and $c_j \equiv 0 \pmod{2^k}$ otherwise.

The exponent $2^{k-1} - 2$ is an integer; at $k = 1$ it equals $-1$, so $f_{48r}$ then appears
in the numerator.

## Sources

- Victor Manuel R. Aricheta, Judy Ann L. Donato, *A Minimal Excludant over Overpartitions*, Journal of Integer Sequences 27 (2024), Article 24.7.1, Proposition 16.

Stated but not proved: `MetaMathlibExt.etaQuotient_sigmaMexOverpartition_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/OverpartitionMexWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html#eta-quotient-sigma-mex-overpartition-mod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimal excludant of overpartitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/integer-partitions/counting-partitions/minimal-excludant-of-overpartitions)
