---
declaration: section
origin: cited
lean: MetaMathlibExt.IsDyckHeightAtMostTwo, MetaMathlibExt.dyckHeightTwoBlockWord, MetaMathlibExt.boolRuns, MetaMathlibExt.boolRuns_example, MetaMathlibExt.runFollowingValleys, MetaMathlibExt.IsTildeRationalRuns, MetaMathlibExt.IsQBonacciRuns, MetaMathlibExt.isQBonacciRuns_examples
statement: formalized
---

# Rational Dyck paths

13 results, 11 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html).

## Dyck words of height at most $2$

A Dyck word has height at most $2$ when no prefix of it
has more than two more up steps $U$ than down steps $D$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Section 2.

Formalized by `MetaMathlibExt.IsDyckHeightAtMostTwo`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#is-dyck-height-at-most-two).

## Block word of a Dyck path of height at most $2$

For a Dyck word
$P = P_0 P_1 \cdots P_{2n-1}$ of semilength $n$, with steps indexed from $0$, the block word of
$P$ is the Boolean word of length $n - 1$ (empty when $n = 0$) whose entry $i$, for
$0 \le i < n - 1$, is true exactly when $P_{2i+1} = U$.

When $P$ has height at most $2$ and $n \ge 1$, it factorizes as $P = U X_1 \cdots X_{n-1} D$
with each $X_{i+1} = P_{2i+1} P_{2i+2}$ a $1$-peak $UD$ or a $0$-valley $DU$, so entry $i$ is
true for a $1$-peak and false for a $0$-valley.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Section 3, factorization (1).

Formalized by `MetaMathlibExt.dyckHeightTwoBlockWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#dyck-height-two-block-word).

## Maximal runs of a Boolean word

The run decomposition of a Boolean word is the list,
from left to right, of its maximal runs of equal consecutive letters, each recorded as the pair
(letter, length of the run).

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Section 3 (blocks of maximal length of consecutive `1`-peaks and `0`-valleys).

Formalized by `MetaMathlibExt.boolRuns`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#bool-runs).

## Maximal runs of the word $1001100$

Writing $1$ for true and $0$ for false, the maximal
runs of the Boolean word $1001100$, listed from left to right as pairs (letter, length), are
$(1, 1), (0, 2), (1, 2), (0, 2)$.

This word is the block word of the source's example path $U\,(UD)\,(DU)^2\,(UD)^2\,(DU)^2\,D$.
In the source's factorization $U\,(UD)^{p_1}\,(DU)^{v_1}\,(UD)^{p_2}\,(DU)^{v_2}\,D$ of that path
into maximal blocks of $1$-peaks $UD$ and $0$-valleys $DU$, the block lengths are $p_1 = 1$,
$v_1 = 2$, $p_2 = 2$, $v_2 = 2$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Section 3, Example.

Formalized by `MetaMathlibExt.boolRuns_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#bool-runs-example).

## Valleys following a run

Let $R = ((b_0, m_0), \dots, (b_{k-1}, m_{k-1}))$ be a list of
pairs of a Boolean letter and a natural number, read as the maximal runs of a block word in which
the letter $\mathrm{false}$ stands for a $0$-valley $DU$. For $i \in \mathbb{N}$, the number of
$0$-valleys immediately after run $i$ is $m_{i+1}$ if $i + 1 < k$ and $b_{i+1} = \mathrm{false}$,
and $0$ otherwise.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Section 3 (`vᵢ` after `pᵢ`).

Formalized by `MetaMathlibExt.runFollowingValleys`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#run-following-valleys).

## The rational Dyck path run condition

Let $r, s \in \mathbb{N}$ and let $R$ be a list of
runs, each a pair (letter, length) with a Boolean letter. For the run at position $i$, let $v_i$
be the length of the run at position $i + 1$ if that run exists and has letter false, and
$v_i = 0$ otherwise. Then $R$ satisfies the rational run condition for $q = r/s$ when every run
of letter true, say of length $p$ at position $i$, has $p \le r$ and $p s \le r v_i$.

Applied to the maximal runs of the block word of a Dyck path, this says that every block of $p$
consecutive $1$-peaks has $p \le r$ and is followed by $v$ consecutive $0$-valleys with
$p s \le r v$, that is, $v \ge \lceil p s / r \rceil$ when $r \ge 1$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Definition 3.

Formalized by `MetaMathlibExt.IsTildeRationalRuns`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#is-tilde-rational-runs).

## The $Q$-bonacci run condition

Let $r, s \in \mathbb{N}$ and let $R$ be a list of runs,
each a pair (letter, length) with a Boolean letter. For the run at position $i$, let $v_i$ be the
length of the run at position $i + 1$ if that run exists and has letter false, and $v_i = 0$
otherwise. Then $R$ satisfies the $Q$-bonacci run condition for $q = r/s$ when every run of
letter true, say of length $p$ at position $i$, has $p \le r$ and also $p s \le r v_i$, except
that $p s \le r v_i$ may fail when both this run is the last run of letter true in $R$ and
either $p = r$ or $v_i = 0$.

Applied to the maximal runs of the block word of a Dyck path, the runs of letter true are the
blocks of $p$ consecutive $1$-peaks and $v_i$ counts the $0$-valleys that follow them: every
block but the last needs $p s \le r v_i$, and the last block, of $p_k$ peaks followed by $v_k$
valleys, needs it only when $p_k < r$ and $v_k \ne 0$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Definition 4.

Formalized by `MetaMathlibExt.IsQBonacciRuns`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#is-qbonacci-runs).

## Examples of the $Q$-bonacci run condition for $q = 4/5$

Writing $1$ for true and $0$ for
false, for $r = 4$ and $s = 5$ the maximal runs of the Boolean word $1001100$ do not satisfy the
$Q$-bonacci run condition, while the maximal runs of $100111100$ and of $100111$ do.

These are the block words of the source's paths $U\,(UD)\,(DU)^2\,(UD)^2\,(DU)^2\,D$, which is
not in the set $Q^{4/5}$ of $Q$-bonacci paths for $q = 4/5$, and
$U\,(UD)\,(DU)^2\,(UD)^4\,(DU)^2\,D$ and $U\,(UD)\,(DU)^2\,(UD)^3\,D$, which are. Writing each
path as $U\,(UD)^{p_1}\,(DU)^{v_1}\,(UD)^{p_2}\,(DU)^{v_2}\,D$ with maximal blocks, the second
has last block $p_2 = 4 = r$ and the third has $p_2 = 3 < r$ and $v_2 = 0$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Example after Definition 4.

Formalized by `MetaMathlibExt.isQBonacciRuns_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#is-qbonacci-runs-examples).

## The path sets $\tilde R_n^{r/s}$

For natural numbers $r$, $s$ and $n$,
$\tilde R_n^{r/s}$ is the finite set of Dyck paths of semilength $n$ and height at most $2$
that satisfy the following run condition. For $n \ge 1$ such a path factors as
$U X_1 \cdots X_{n-1} D$ with each $X_i$ either a $1$-peak $UD$ or a $0$-valley $DU$, and its
block word $X_1 \cdots X_{n-1}$ (empty for $n = 0$) splits into maximal runs of equal blocks.
Every run of $p$ consecutive $1$-peaks must have $p \le r$ and $p s \le r v$, where $v$ is the
length of the run of $0$-valleys immediately after it ($v = 0$ if no run follows it).

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Definition 3.

Formalized by `MetaMathlibExt.tildeRationalDyckPaths`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#tilde-rational-dyck-paths).

## The $Q$-bonacci paths $Q_n^{r/s}$

For natural numbers $r$, $s$ and $n$, $Q_n^{r/s}$ is
the finite set of Dyck paths of semilength $n$ and height at most $2$ that satisfy the following
run condition. For $n \ge 1$ such a path factors as $U X_1 \cdots X_{n-1} D$ with each $X_i$
either a $1$-peak $UD$ or a $0$-valley $DU$, and its block word $X_1 \cdots X_{n-1}$ (empty for
$n = 0$) splits into maximal runs of equal blocks. Every run of $p$ consecutive $1$-peaks must
have $p \le r$, and also $p s \le r v$, where $v$ is the length of the run of $0$-valleys
immediately after it ($v = 0$ if no run follows it); for the last run of $1$-peaks, the
inequality $p s \le r v$ is required only when $p < r$ and $v \ne 0$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Definition 4.

Formalized by `MetaMathlibExt.qBonacciDyckPaths`, a definition declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#q-bonacci-dyck-paths).

## Path counts for $q = 3/2$

Let $r = 3$ and $s = 2$. The set $Q_4^{3/2}$ of $Q$-bonacci
paths of semilength $4$, that is, the Dyck paths of semilength $4$ and height at most $2$ whose
block word's maximal runs satisfy the $Q$-bonacci run condition, has $7$ elements, while the set
$\tilde R_5^{3/2}$ of Dyck paths of semilength $5$ and height at most $2$ whose block word's
maximal runs satisfy the rational run condition has $6$ elements.

Here $t = \lfloor (s - 1)/r \rfloor = 0$ and $s \ne t r + 1$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Definitions 3 and 4.

Formalized by `MetaMathlibExt.card_qBonacciDyckPaths_three_two_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#card-q-bonacci-dyck-paths-three-two-four).

## $Q$-bonacci and rational-run paths are in bijection when $s = t r + 1$

Let $r \ge 1$
and $t$ be natural numbers and $s = t r + 1$. Then for every $n \ge 0$ the set $Q_n^{r/s}$ of
$Q$-bonacci paths of semilength $n$ is in bijection with the set $\tilde R_{n+t+1}^{r/s}$ of Dyck
paths of semilength $n + t + 1$ and height at most $2$ whose block word's maximal runs satisfy
the rational run condition for $q = r/s$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Proposition 6 (`jis-2025-25.3.2-prop-6`).

Stated but not proved: `MetaMathlibExt.nonempty_equiv_qBonacci_tildeRational` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#nonempty-equiv-q-bonacci-tilde-rational).

## $Q$-bonacci and rational-run paths correspond exactly when $s \equiv 1 \pmod r$

Let
$r, s \ge 1$ be coprime natural numbers and let $t = \lfloor (s - 1)/r \rfloor$, so that
$t r + 1 \le s \le (t + 1) r$. For $m \in \mathbb{N}$ write $Q_m^{r/s}$ for the set of $Q$-bonacci
paths of semilength $m$ and $\tilde R_m^{r/s}$ for the set of Dyck paths of semilength $m$ and
height at most $2$ whose block word's maximal runs satisfy the rational run condition for
$q = r/s$. Then $\tilde R_{n+t+1}^{r/s}$ and $Q_n^{r/s}$ are in bijection for every $n \ge 0$ if
and only if $s = t r + 1$.

## Sources

- Barcucci, Bernini, Bilotta, and Pinzani, *Rational Dyck Paths*, Journal of Integer Sequences 28 (2025), Article 25.3.2, Proposition 7 (`jis-2025-25.3.2-prop-7`).

Stated but not proved: `MetaMathlibExt.forall_nonempty_equiv_qBonacci_tildeRational_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RationalDyckPathsWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html#forall-nonempty-equiv-q-bonacci-tilde-ra).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rational Dyck paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/rational-dyck-paths)
