---
declaration: section
origin: cited
lean: MetaMathlibExt.card_hurwitz_norm_eq, MetaMathlibExt.card_hurwitz_norm_le_asymptotic, MetaMathlibExt.density_hurwitz_norm_valuations_in, MetaMathlibExt.density_hurwitz_norm_in_rankin_greedy, MetaMathlibExt.upperDensity_hurwitz_norm_in_interval_union, MetaMathlibExt.disjoint_progressions_hurwitz_card, MetaMathlibExt.upperDensity_le_of_hurwitz_gpFree, MetaMathlibExt.sSup_upperDensity_hurwitz_gpFree_bounds
statement: formalized
---

# Geometric-progression-free sets of Hurwitz quaternions

13 results, 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html).

## Number of Hurwitz quaternions of a given norm

A Hurwitz quaternion is a quaternion
$q = x_0 + x_1 i + x_2 j + x_3 k$ whose rational coordinates $x_0, x_1, x_2, x_3$ are either all
integers or all halves of odd integers, and its norm is
$\mathrm{Nm}(q) = x_0^2 + x_1^2 + x_2^2 + x_3^2$. For every positive integer $N$, the number of
Hurwitz quaternions of norm $N$ is $24 \sum_{d \mid N,\ d \text{ odd}} d$, that is, $24$ times
the sum of the odd divisors of $N$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Lemma 1.

Stated but not proved: `MetaMathlibExt.card_hurwitz_norm_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#card-hurwitz-norm-eq).

## Counting Hurwitz quaternions of bounded norm

A Hurwitz quaternion is a quaternion whose
four rational coordinates are either all integers or all halves of odd integers; its norm is the
sum of the squares of its coordinates. For a natural number $N$ let $S(N)$ be the set of nonzero
Hurwitz quaternions of norm at most $N$.

(a) There is a real constant $C$ such that $\bigl| |S(N)| - \pi^2 N^2 \bigr| \le C N \log N$ for
every natural number $N \ge 2$.

(b) For every positive integer $M$ there is a real constant $C$ such that, for every natural
number $N \ge 2$, the number $c_M(N)$ of Hurwitz quaternions whose norm is a positive integer
$n \le N$ coprime to $M$ satisfies

$$\Bigl| c_M(N) - \pi^2 N^2 \cdot \frac{\varphi(2M)}{M}
\prod_{p \mid M} \Bigl(1 - \frac{1}{p^2}\Bigr) \Bigr| \le C N \log N,$$

where $\varphi$ is Euler's totient function and the product runs over the primes $p$ dividing $M$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Lemma 2.

Stated but not proved: `MetaMathlibExt.card_hurwitz_norm_le_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#card-hurwitz-norm-le-asymptotic).

## Density of Hurwitz quaternions whose norm has prescribed prime exponents

A Hurwitz
quaternion is a quaternion whose four rational coordinates are either all integers or all halves
of odd integers; its norm is the sum of the squares of its coordinates. For a natural number $N$
let $S(N)$ be the set of nonzero Hurwitz quaternions of norm at most $N$. Let $A$ be a set of
natural numbers, let $G$ be the set of positive integers $n$ such that for every prime $p$ the
exponent $\nu_p(n)$ of $p$ in $n$ lies in $A$, and let $H_G$ be the set of Hurwitz quaternions
whose norm lies in $G$. Then the ratio $|H_G \cap S(N)| / |S(N)|$ tends, as $N \to \infty$, to

$$\frac{6}{\pi^2} \Bigl( \sum_{k \in A} 2^{-2k} \Bigr)
\prod_{p > 2} \Bigl( \sum_{k \in A} p^{-k} - \frac{1}{p} \sum_{k \in A} p^{-2k} \Bigr),$$

the product running over the odd primes $p$. Here $6/\pi^2 = 1/\zeta(2)$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Theorem 5.

Stated but not proved: `MetaMathlibExt.density_hurwitz_norm_valuations_in` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#density-hurwitz-norm-valuations-in).

## Density of Hurwitz quaternions with norm in Rankin's greedy set

A Hurwitz quaternion is a
quaternion whose four rational coordinates are either all integers or all halves of odd integers;
its norm is the sum of the squares of its coordinates. For a natural number $N$ let $S(N)$ be the
set of nonzero Hurwitz quaternions of norm at most $N$. Let $G$ be the set of positive integers
$n$ such that, for every prime $p$, the base-$3$ digits of the exponent $\nu_p(n)$ of $p$ in $n$
include no $2$ (this is Rankin's greedy set of positive integers avoiding 3-term geometric
progressions), and let $H_G$ be the set of Hurwitz quaternions whose norm lies in $G$. With
$f(x) = \prod_{i \ge 0} \bigl(1 + x^{-3^i}\bigr)$, the ratio $|H_G \cap S(N)| / |S(N)|$ tends,
as $N \to \infty$, to

$$\frac{6}{\pi^2} \, f(4) \prod_{p > 2} \Bigl( f(p) - \frac{f(p^2)}{p} \Bigr),$$

the product running over the odd primes $p$.

The paper writes this constant as $(f(2^2)/\zeta(2)) \prod_{p > 2} (f(p) - f(p^2)/p)$, using
$1/\zeta(2) = 6/\pi^2$, and gives its value as approximately $0.782643$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Theorem 7 (restated as the unnumbered theorem of the introduction).

Stated but not proved: `MetaMathlibExt.density_hurwitz_norm_in_rankin_greedy` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#density-hurwitz-norm-in-rankin-greedy).

## Upper density of Hurwitz quaternions with norms in a lacunary union of intervals

Let
$Q_{\mathrm{Hur}}$ be the set of Hurwitz quaternions, the rational quaternions whose four
coordinates are all integers or all lie in $\mathbb{Z} + \tfrac12$, and let $\mathrm{Nm}(q)$ be
the sum of the squares of the coordinates of $q$. For $N \in \mathbb{N}$ let $S(N)$ be the set of
nonzero $q \in Q_{\mathrm{Hur}}$ with $\mathrm{Nm}(q) \le N$, and define the upper density of a
set $A$ of quaternions as $\limsup_{N \to \infty} |A \cap S(N)| / |S(N)|$. For a natural number
$M$ let $T_M$ be the set of positive integers in $(M/48, M/45] \cup (M/40, M/36] \cup
(M/32, M/27] \cup (M/24, M/12] \cup (M/9, M/8] \cup (M/4, M]$, and let
$\mathcal{S} = \bigcup_{i \ge 1} T_{N_i}$ with $N_i = 48^{2^i}$. Then the set of
$q \in Q_{\mathrm{Hur}}$ with $\mathrm{Nm}(q) \in \mathcal{S}$ has upper density
$17665627/18662400$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Lemma 10 (the set `𝒮` from Section 4.1).

Stated but not proved: `MetaMathlibExt.upperDensity_hurwitz_norm_in_interval_union` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#upper-density-hurwitz-norm-in-interval-u).

## Many disjoint geometric progressions among Hurwitz quaternions

A Hurwitz quaternion is a
quaternion whose four rational coordinates are either all integers or all halves of odd integers;
its norm is the sum of the squares of its coordinates. For a natural number $N$ let $S(N)$ be the
set of nonzero Hurwitz quaternions of norm at most $N$. Fix a Hurwitz quaternion $R$ of norm $2$,
and for a natural number $N$ let $E(N)$ be the set of triples $(bR^{3n}, bR^{3n+1}, bR^{3n+2})$,
where $n$ is a natural number and $b$ is a Hurwitz quaternion whose norm is an odd integer at
most $N / 2^{3n+2}$. Then for every $N$, every triple in $E(N)$ has the form $(a, aR, aR^2)$ with
all three entries in $S(N)$, and two distinct triples in $E(N)$ have no entry in common.
Moreover there is a real constant $C$ such that

$$\Bigl| |E(N)| - \frac{\pi^2 N^2}{21} \Bigr| \le C N (\log N)^2$$

for every natural number $N \ge 2$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Lemma 12.

Stated but not proved: `MetaMathlibExt.disjoint_progressions_hurwitz_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#disjoint-progressions-hurwitz-card).

## Upper bound for geometric-progression-free Hurwitz sets

Let $Q_{\mathrm{Hur}}$ be the
set of Hurwitz quaternions, the rational quaternions whose four coordinates are all integers or
all lie in $\mathbb{Z} + \tfrac12$, and let $\mathrm{Nm}(q)$ be the sum of the squares of the
coordinates of $q$. For $N \in \mathbb{N}$ let $S(N)$ be the set of nonzero
$q \in Q_{\mathrm{Hur}}$ with $\mathrm{Nm}(q) \le N$. Let $A \subseteq Q_{\mathrm{Hur}}$ be free
of 3-term geometric progressions: there are no $a, r \in Q_{\mathrm{Hur}}$ with $a \ne 0$,
$r \ne 0$ and $\mathrm{Nm}(r) \ne 1$ such that $a$, $ar$ and $ar^2$ all lie in $A$. Then the
upper density $\limsup_{N \to \infty} |A \cap S(N)| / |S(N)|$ of $A$ is at most $20/21$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Lemma 13.

Stated but not proved: `MetaMathlibExt.upperDensity_le_of_hurwitz_gpFree` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#upper-density-le-of-hurwitz-gp-free).

## Bounds on the supremum of upper densities of geometric-progression-free Hurwitz sets

Let
$Q_{\mathrm{Hur}}$ be the set of Hurwitz quaternions, the rational quaternions whose four
coordinates are all integers or all lie in $\mathbb{Z} + \tfrac12$, and let $\mathrm{Nm}(q)$ be
the sum of the squares of the coordinates of $q$. For $N \in \mathbb{N}$ let $S(N)$ be the set of
nonzero $q \in Q_{\mathrm{Hur}}$ with $\mathrm{Nm}(q) \le N$, and define the upper density of a
set $A$ of quaternions as $\limsup_{N \to \infty} |A \cap S(N)| / |S(N)|$. Call
$A \subseteq Q_{\mathrm{Hur}}$ free of 3-term geometric progressions if there are no
$a, r \in Q_{\mathrm{Hur}}$ with $a \ne 0$, $r \ne 0$ and $\mathrm{Nm}(r) \ne 1$ such that $a$,
$ar$ and $ar^2$ all lie in $A$. Let $\bar m_{\mathrm{Hur}}$ be the supremum of the upper
densities of such sets. Then $17665627/18662400 \le \bar m_{\mathrm{Hur}} \le 20/21$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Theorem 14 (restated as the unnumbered theorem of the introduction).

Stated but not proved: `MetaMathlibExt.sSup_upperDensity_hurwitz_gpFree_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#s-sup-upper-density-hurwitz-gp-free-boun).

## Squarefree norms and the lower density of the quaternion greedy set

A Hurwitz quaternion is
a quaternion whose four rational coordinates are either all integers or all halves of odd integers;
the norm $\mathrm{Nm}(q)$ of a quaternion $q$ is the sum of the squares of its coordinates. For a
natural number $N$ let $S(N)$ be the set of nonzero Hurwitz quaternions of norm at most $N$. Let
$\mathcal{G}$ be a set of quaternions such that a quaternion $q$ lies in $\mathcal{G}$ if and only
if $q$ is a nonzero Hurwitz quaternion and there are no $a \in \mathcal{G}$ and Hurwitz quaternion
$r \ne 0$ with norm $\mathrm{Nm}(r) \ne 1$, $ar \in \mathcal{G}$ and $q = ar^2$ (this recursion on
the norm characterizes the quaternion greedy set). Then $\mathcal{G}$ contains every Hurwitz
quaternion whose norm is a squarefree natural number, and

$$\liminf_{N \to \infty} \frac{|\mathcal{G} \cap S(N)|}{|S(N)|} \ge \frac{60}{7 \pi^2 \zeta(3)},$$

where $\zeta(3) = \sum_{n \ge 1} n^{-3}$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Proposition 17.

Stated but not proved: `MetaMathlibExt.quaternionGreedy_squarefree_norm_and_lowerDensity` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#quaternion-greedy-squarefree-norm-and-lo).

## The quaternion greedy set is not determined by norms

A Hurwitz quaternion is a quaternion
whose four rational coordinates are either all integers or all halves of odd integers; the norm
$\mathrm{Nm}(q)$ of a quaternion $q$ is the sum of the squares of its coordinates. Let
$\mathcal{G}$ be a set of quaternions such that a quaternion $q$ lies in $\mathcal{G}$ if and only
if $q$ is a nonzero Hurwitz quaternion and there are no $a \in \mathcal{G}$ and Hurwitz quaternion
$r \ne 0$ with norm $\mathrm{Nm}(r) \ne 1$, $ar \in \mathcal{G}$ and $q = ar^2$ (this recursion on
the norm characterizes the quaternion greedy set). Then for every set $G$ of positive integers,
$\mathcal{G}$ is not the set of Hurwitz quaternions whose norm lies in $G$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Proposition 18.

Stated but not proved: `MetaMathlibExt.quaternionGreedy_ne_norm_preimage` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#quaternion-greedy-ne-norm-preimage).

## The quaternion greedy set and the norm preimage of Rankin's set differ infinitely

A
Hurwitz quaternion is a quaternion whose four rational coordinates are either all integers or all
halves of odd integers; the norm $\mathrm{Nm}(q)$ of a quaternion $q$ is the sum of the squares of
its coordinates. Let $\mathcal{G}$ be a set of quaternions such that a quaternion $q$ lies in
$\mathcal{G}$ if and only if $q$ is a nonzero Hurwitz quaternion and there are no
$a \in \mathcal{G}$ and Hurwitz quaternion $r \ne 0$ with norm $\mathrm{Nm}(r) \ne 1$,
$ar \in \mathcal{G}$ and $q = ar^2$ (this recursion on the norm characterizes the quaternion
greedy set). Let $G^*_3$ be Rankin's greedy set, the set of positive integers $n$ such that for
every prime $p$ the base-$3$ digits of the exponent of $p$ in $n$ include no digit $2$, and let
$S(G^*_3)$ be the set of Hurwitz quaternions whose norm lies in $G^*_3$. Then both
$\mathcal{G} \setminus S(G^*_3)$ and $S(G^*_3) \setminus \mathcal{G}$ are infinite.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Proposition 19.

Stated but not proved: `MetaMathlibExt.quaternionGreedy_diff_rankin_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#quaternion-greedy-diff-rankin-infinite).

## Hurwitz quaternions of square norm that are not a unit times a square

A Hurwitz
quaternion is a quaternion whose four rational coordinates are either all integers or all halves
of odd integers; its norm is the sum of the squares of its coordinates, and a Hurwitz unit is a
Hurwitz quaternion of norm $1$. Let $r$ be a positive integer that is not a sum of three squares
of integers, or that is divisible by an odd integer greater than $24$. Then some Hurwitz
quaternion $Q$ of norm $r^2$ cannot be written as $Q = UR^2$ with $U$ a Hurwitz unit and $R$ a
Hurwitz quaternion of norm $r$. If $r$ is not a sum of three squares of integers, then $Q = r$,
viewed as a quaternion with zero imaginary part, is such a quaternion.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Proposition 20.

Stated but not proved: `MetaMathlibExt.exists_hurwitz_norm_sq_not_unit_mul_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#exists-hurwitz-norm-sq-not-unit-mul-sq).

## Quaternions of prime-square norm separating the greedy set from Rankin's set

A Hurwitz
quaternion is a quaternion whose four rational coordinates are either all integers or all halves
of odd integers; its norm $\mathrm{Nm}(q)$ is the sum of the squares of its coordinates, and a
Hurwitz unit is a Hurwitz quaternion of norm $1$. Let $\mathcal{G}$ be a set of quaternions such
that a quaternion $q$ lies in $\mathcal{G}$ if and only if $q$ is a nonzero Hurwitz quaternion
and there are no $a \in \mathcal{G}$ and Hurwitz quaternion $r \ne 0$ with $\mathrm{Nm}(r) \ne 1$,
$ar \in \mathcal{G}$ and $q = ar^2$ (this recursion on the norm characterizes the quaternion
greedy set). Let $G^*_3$ be Rankin's greedy set, the set of positive integers $n$ such that for
every prime $\ell$ the base-$3$ digits of the exponent of $\ell$ in $n$ include no digit $2$, and
let $S(G^*_3)$ be the set of Hurwitz quaternions whose norm lies in $G^*_3$. Let $p$ be a prime
and $Q$ a Hurwitz quaternion of norm $p^2$ that cannot be written as $Q = UR^2$ with $U$ a
Hurwitz unit and $R$ a Hurwitz quaternion of norm $p$. Then
$Q \in \mathcal{G} \setminus S(G^*_3)$ and $Q^2 \in S(G^*_3) \setminus \mathcal{G}$.

## Sources

- Asada, Fang, Fourakis, Manski, McNew, Miller, Moreland, Yamin, and Zhang, *Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions*, J. Integer Seq. 27 (2024), Article 24.7.7, Proposition 21.

Stated but not proved: `MetaMathlibExt.quaternionGreedy_mem_of_not_unit_mul_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzGeometricProgressionFreeWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html#quaternion-greedy-mem-of-not-unit-mul-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geometric-progression-free sets of Hurwitz quaternions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/geometric-progression-free-sets-of-hurwitz-quate)
