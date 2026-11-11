---
declaration: section
origin: cited
lean: MetaMathlibExt.farey_interval_mediant_telescoping, MetaMathlibExt.farey_interval_subset_reciprocal_interval, MetaMathlibExt.hasSum_farey_subintervals_reciprocal_interval, MetaMathlibExt.euler_mascheroni_eq_hata_farey_sum, MetaMathlibExt.fareyGeneration, MetaMathlibExt.fareyGeneration_one_two, MetaMathlibExt.fareyGeneration_succ, MetaMathlibExt.fareyGeneration_length_le
statement: formalized
---

# Hata's Farey formula for Euler's constant

9 results, 3 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html).

## Mediant telescoping identity for Farey intervals

For an interval $[x/y, z/w]$ write
$f([x/y, z/w]) = (xw + yz)/(xyzw)$. Let $a, b, c, d$ be natural numbers with $a > 0$, $d > 0$
and $bc = ad + 1$. Then, computing in the real numbers, the value of $f$ on $[a/b, c/d]$ minus
its values on the two halves $[a/b, (a + c)/(b + d)]$ and $[(a + c)/(b + d), c/d]$ cut at the
mediant equals

$$
\frac{(bc - ad)^2}{abcd(a + c)(b + d)} = \frac{1}{abcd(a + c)(b + d)}.
$$

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Lemma 1.

Stated but not proved: `MetaMathlibExt.farey_interval_mediant_telescoping` is written with `theorem_wanted` in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#farey-interval-mediant-telescoping).

## Farey intervals lie in reciprocal intervals

Let $a, b, c, d$ be natural numbers with
$a > 0$, $c \le d$ and $bc = ad + 1$, so that $[a/b, c/d] \subseteq [0, 1]$ is a Farey interval
with positive left endpoint. Then there is a natural number $n \ge 1$ with $1/(n + 1) \le a/b$
and $c/d \le 1/n$, that is, $[a/b, c/d] \subseteq [1/(n + 1), 1/n]$.

The source's set $F \setminus F^*$ is rendered as these intervals: $F^*$ consists of the
intervals $[0/1, 1/n]$, the ones excluded in the source's proof of this corollary.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Corollary 2.

Stated but not proved: `MetaMathlibExt.farey_interval_subset_reciprocal_interval` is written with `theorem_wanted` in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#farey-interval-subset-reciprocal-interva).

## Sum over the Farey intervals inside a reciprocal interval

Let $n \ge 1$ and
$J_n = [1/(n + 1), 1/n]$. The family $1/(abcd(a + c)(b + d))$, indexed by the quadruples
$(a, b, c, d)$ of natural numbers with $bc = ad + 1$, $b \le (n + 1)a$ and $nc \le d$ (that is,
by the Farey intervals $[a/b, c/d] \subseteq J_n$, including $J_n$ itself), is summable with sum

$$
\frac{1}{n} + \frac{1}{n + 1} - 2 \log \frac{n + 1}{n}.
$$

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Lemma 3.

Stated but not proved: `MetaMathlibExt.hasSum_farey_subintervals_reciprocal_interval` is written with `theorem_wanted` in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#has-sum-farey-subintervals-reciprocal-in).

## Hata's formula for Euler's constant

Let $S$ be the set of quadruples $(a, b, c, d)$ of
natural numbers with $bc = ad + 1$, $a > 0$ and $c \le d$; these are the Farey intervals
$[a/b, c/d] \subseteq [0, 1]$ with positive left endpoint. The family
$1/(abcd(a + c)(b + d))$, indexed by $(a, b, c, d) \in S$, is summable, and Euler's constant
$\gamma$ satisfies

$$
\gamma = \frac{1}{2} + \frac{1}{2} \sum_{(a, b, c, d) \in S} \frac{1}{abcd(a + c)(b + d)}.
$$

The set $S$ is the source's $F \setminus F^*$, where $F^*$ consists of the intervals $[0/1, 1/n]$.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Theorem 1, attributed there to Hata.

Stated but not proved: `MetaMathlibExt.euler_mascheroni_eq_hata_farey_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#euler-mascheroni-eq-hata-farey-sum).

## Stern-Brocot generations

The $n$-th Stern-Brocot generation $F_n$ is a finite set of
intervals $[a/b, c/d]$, each stored as the quadruple $(a, b, c, d)$ of natural numbers. It is
defined by $F_0 = \{[0/1, 1/1]\}$, and $F_{n+1}$ is obtained by replacing each
$[a/b, c/d] \in F_n$ with its two mediant halves $[a/b, (a + c)/(b + d)]$ and
$[(a + c)/(b + d), c/d]$.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Section 2 (before Corollary 1).

Formalized by `MetaMathlibExt.fareyGeneration`, a definition declared in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#farey-generation).

## The first two Stern-Brocot generations

Writing $[a/b, c/d]$ for the quadruple
$(a, b, c, d)$, the first two Stern-Brocot generations are $F_1 = \{[0/1, 1/2], [1/2, 1/1]\}$
and $F_2 = \{[0/1, 1/3], [1/3, 1/2], [1/2, 2/3], [2/3, 1/1]\}$.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Section 2 (before Corollary 1).

Formalized by `MetaMathlibExt.fareyGeneration_one_two`, a theorem declared in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#farey-generation-one-two).

## Recurrence for the Stern-Brocot generations

For every natural number $n$, the
generation $F_{n+1}$ is the union, over all intervals $[a/b, c/d] \in F_n$, of the two mediant
halves $[a/b, (a + c)/(b + d)]$ and $[(a + c)/(b + d), c/d]$, where each interval $[x/y, z/w]$
is stored as the quadruple $(x, y, z, w)$.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Section 2 (before Corollary 1).

Formalized by `MetaMathlibExt.fareyGeneration_succ`, a theorem declared in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#farey-generation-succ).

## Length bound for the Stern-Brocot generations

For every natural number $n$, every
interval $[a/b, c/d]$ of the $n$-th Stern-Brocot generation $F_n$, that is, every quadruple
$(a, b, c, d) \in F_n$, satisfies $c/d - a/b \le 1/(n + 1)$.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Corollary 1.

Stated but not proved: `MetaMathlibExt.fareyGeneration_length_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#farey-generation-length-le).

## Riemann-sum bound for Farey partitions

Let $a, b, c, d, m$ be natural numbers with
$a > 0$, $bc = ad + 1$, $c \le d$ and $m \ge 2$. Let $A, B : \mathbb{N} \to \mathbb{N}$ satisfy
$A(1) = a$, $B(1) = b$, $A(m) = c$, $B(m) = d$ and $B(k) A(k+1) = A(k) B(k+1) + 1$ for
$1 \le k \le m - 1$, and let $\delta$ be a real number with $1/(B(k) B(k+1)) \le \delta$ for
$1 \le k \le m - 1$. Then

$$
\left| \sum_{k=1}^{m-1} \frac{A(k) B(k+1) + B(k) A(k+1)}{A(k) B(k) A(k+1) B(k+1)} -
\int_{a/b}^{c/d} \frac{2}{t} \, dt \right| \le
\left( \frac{c}{d} - \frac{a}{b} \right) \frac{b^2}{a^2} \, \delta.
$$

In words: the fractions $A(k)/B(k)$ cut the Farey interval $[a/b, c/d]$ into consecutive Farey
intervals, the $k$-th summand is $f([A(k)/B(k), A(k+1)/B(k+1)])$ with
$f([x/y, z/w]) = (xw + yz)/(xyzw)$, and $\delta$ stands for any upper bound of
$\max_k 1/(B(k) B(k+1))$.

## Sources

- Nikita Kalinin, *A Short Telescoping Proof of Hata's Formula for the Euler-Mascheroni Constant*, INTEGERS 25 (2025), Article A90, Lemma 2, inequality (2).

Stated but not proved: `MetaMathlibExt.abs_sum_farey_partition_sub_integral_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HataEulerMascheroniFareyWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html#abs-sum-farey-partition-sub-integral-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hata's Farey formula for Euler's constant](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/hata-s-farey-formula-for-euler-s-constant)
