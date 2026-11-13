---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_zero_sum_cross_number_le_one, MetaMathlibExt.ZMod.exists_zero_sum_cross_number_le_one, MetaMathlibExt.IsGoodSequence, MetaMathlibExt.goodSequenceProb, MetaMathlibExt.goodSequenceProb_zero, MetaMathlibExt.halfGoodThreshold, MetaMathlibExt.halfGoodThreshold_eq_one_of_card_le_two, MetaMathlibExt.IsThresholdFunction
statement: formalized
---

# Zero-sum subsequences of small cross number

22 results, 15 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html).

## Zero-sum subsequences of cross number at most one (Geroldinger; Elledge–Hurlbert)

Let
$\Gamma$ be a finite abelian group of order $|\Gamma|$. Every sequence $g_1, \dots, g_{|\Gamma|}$
of $|\Gamma|$ elements of $\Gamma$ has a nonempty zero-sum subsequence with cross number at most
one: there is a nonempty set $S \subseteq \{1, \dots, |\Gamma|\}$ of indices with
$\sum_{i \in S} g_i = 0$ and $\sum_{i \in S} 1/\operatorname{ord}(g_i) \le 1$, where
$\operatorname{ord}(g_i)$ is the order of $g_i$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Theorem 3.

Stated but not proved: `MetaMathlibExt.exists_zero_sum_cross_number_le_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#exists-zero-sum-cross-number-le-one).

## Lemke–Kleitman theorem

For every positive integer $n$, every sequence
$g_1, \dots, g_n$ of $n$ elements of $\mathbb{Z}/n\mathbb{Z}$ has a nonempty zero-sum
subsequence with cross number at most one: there is a nonempty set $S \subseteq \{1, \dots, n\}$
of indices with $\sum_{i \in S} g_i = 0$ and $\sum_{i \in S} 1/\operatorname{ord}(g_i) \le 1$,
where $\operatorname{ord}(g_i)$ is the additive order of $g_i$. The theorem is due to Lemke and
Kleitman and to Chung.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Theorem 2.

Stated but not proved: `MetaMathlibExt.ZMod.exists_zero_sum_cross_number_le_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#exists-zero-sum-cross-number-le-one-2).

## Good sequences in a finite abelian group

Let $\Gamma$ be a finite abelian group, written
additively, and let $g = (g_1, \dots, g_t)$ be a sequence of $t$ elements of $\Gamma$. The
sequence $g$ is *good* if there is a nonempty set $S \subseteq \{1, \dots, t\}$ of indices with
$\sum_{i \in S} g_i = 0$ whose cross number $\sum_{i \in S} 1/|g_i|$ is at most $1$, where
$|g_i|$ is the order of $g_i$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 1 (definition of good sequences).

Formalized by `MetaMathlibExt.IsGoodSequence`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#is-good-sequence).

## Probability that a random sequence is good

Let $\Gamma$ be a finite abelian group and
$t \ge 0$ an integer. A sequence $g_1, \dots, g_t$ in $\Gamma$ is good if some nonempty set
$S \subseteq \{1, \dots, t\}$ of indices has $\sum_{i \in S} g_i = 0$ and
$\sum_{i \in S} 1/\operatorname{ord}(g_i) \le 1$, where $\operatorname{ord}(g_i)$ is the order
of $g_i$. The good-sequence probability of $\Gamma$ at length $t$ is the number of good sequences
of length $t$ in $\Gamma$ divided by $|\Gamma|^t$, that is, the probability that a uniformly
random sequence of length $t$ in $\Gamma$ is good.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 1.1 (the event `E_Γ(t)`).

Formalized by `MetaMathlibExt.goodSequenceProb`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#good-sequence-prob).

## Good-sequence probability at length zero

For every finite abelian group $\Gamma$, the
probability that a uniformly random sequence of length $0$ in $\Gamma$ is good equals $0$: the
empty sequence has no nonempty zero-sum subsequence, so it is not good.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, characteristic lemma of the Section 1.1 definition.

Formalized by `MetaMathlibExt.goodSequenceProb_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#good-sequence-prob-zero).

## Half-good threshold

For a finite abelian group $\Gamma$, $P_{1/2}(\Gamma)$ is the least
$t \ge 0$ such that a uniformly random sequence of $t$ elements of $\Gamma$ is good (has a
nonempty zero-sum subsequence with cross number at most one) with probability at least $1/2$,
that is, such that at least half of the $|\Gamma|^t$ sequences of length $t$ are good. If no
such $t$ exists, $P_{1/2}(\Gamma)$ is defined to be $0$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 1.1 (definition of `P_{1/2}(Γ)`).

Formalized by `MetaMathlibExt.halfGoodThreshold`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#half-good-threshold).

## Half-good threshold of a group of order at most two

If $\Gamma$ is a finite abelian
group with at most two elements, then its half-good threshold $P_{1/2}(\Gamma)$ equals $1$.

The empty sequence is not good, while the one-term sequence $(0)$ is good, so a uniformly random
sequence of length one is good with probability at least $1/|\Gamma| \ge 1/2$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, characteristic lemma of the Section 1.1 definition of `P_{1/2}(Γ)`.

Formalized by `MetaMathlibExt.halfGoodThreshold_eq_one_of_card_le_two`, a theorem declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#half-good-threshold-eq-one-of-card-le-tw).

## Threshold functions

Let $P : \mathbb{N} \times \mathbb{N} \to \mathbb{R}$, where
$P(k, s)$ is read as the probability of an event in the $k$-th space when $s$ random elements
are chosen. A function $t : \mathbb{N} \to \mathbb{R}$ is a *threshold function* for $P$ if
$t(k) > 0$ for all sufficiently large $k$ and, for every function $f : \mathbb{N} \to \mathbb{N}$,
$P(k, f(k)) \to 1$ as $k \to \infty$ whenever $t = o(f)$, and $P(k, f(k)) \to 0$ as
$k \to \infty$ whenever $f = o(t)$.

The source's thresholds are positive functions; since little-o ignores sign, without the
positivity condition $-t$ would be a threshold function whenever $t$ is.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 1.1 (definition of a threshold and of `τ(G)`).

Formalized by `MetaMathlibExt.IsThresholdFunction`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#is-threshold-function).

## Positive multiples of threshold functions

Let $P : \mathbb{N} \times \mathbb{N} \to
\mathbb{R}$ and $t : \mathbb{N} \to \mathbb{R}$. If $t$ is a threshold function for $P$ and
$c > 0$ is a real number, then $k \mapsto c \, t(k)$ is also a threshold function for $P$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, characteristic lemma of the Section 1.1 definition of a threshold.

Formalized by `MetaMathlibExt.IsThresholdFunction.const_mul`, a theorem declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#const-mul).

## Lagarias–Saks pebbling step

Let $G$ be a simple graph on a vertex set $V$, and let $w$
assign a natural-number cost $w(uv)$ to each unordered pair of vertices $\{u, v\}$. For
configurations $C, C' : V \to \mathbb{N}$, there is a pebbling step from $C$ to $C'$ if there
is an edge $uv$ of $G$ with $0 < w(uv) \le C(u)$ such that $C'$ is obtained from $C$ by
removing $w(uv)$ pebbles from $u$ and adding one pebble to $v$.

Each edge has one cost, used in both directions. The source's costs are positive, and the step
requires $w(uv) > 0$, so a zero cost never creates a pebble for free.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 2.2 (pebbling step).

Formalized by `MetaMathlibExt.PebblingStep`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#pebbling-step).

## Solvable pebbling configurations

Let $G$ be a simple graph on a vertex set $V$ with
natural-number edge costs $w$. A configuration $C : V \to \mathbb{N}$ of pebbles is *solvable*
if for every target vertex $r$ there is a finite, possibly empty, sequence of pebbling steps on
$G$ with costs $w$ leading from $C$ to a configuration with at least one pebble on $r$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Sections 2.2 and 3.1 (`r`-solvability, for every target).

Formalized by `MetaMathlibExt.PebblingSolvable`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#pebbling-solvable).

## Configurations covering every vertex are solvable

Let $G$ be a simple graph with
natural-number edge costs $w$. Every pebbling configuration $C$ on $G$ with $C(r) \ge 1$ for
every vertex $r$ is solvable with respect to $G$ and $w$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, characteristic lemma of the Section 2.2 definition.

Formalized by `MetaMathlibExt.pebblingSolvable_of_forall_pos`, a theorem declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#pebbling-solvable-of-forall-pos).

## Probability that a random pebbling configuration is solvable

Let $G$ be a simple graph on
a finite vertex set $V$ with $n$ vertices, let $w$ assign a natural-number cost to each unordered
pair of vertices, and let $t \ge 0$ be an integer. A configuration of $t$ pebbles is a function
$C : V \to \mathbb{N}$ with $\sum_{v \in V} C(v) = t$. The value is the number of configurations
of $t$ pebbles that are solvable with respect to $G$ and $w$, divided by the number of all
configurations of $t$ pebbles; that is, the probability that a configuration of $t$ pebbles
chosen uniformly at random is solvable. If there are no configurations of $t$ pebbles ($V$ empty
and $t > 0$), the value is $0$.

For $n \ge 1$ there are $\binom{n + t - 1}{t}$ configurations of $t$ pebbles (the space
$D_{G,t}$ of the source).

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 3.1 (configuration model).

Formalized by `MetaMathlibExt.solvableConfigurationProb`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#solvable-configuration-prob).

## The solvability probability is at most one

For every simple graph $G$ on a finite
vertex set with natural-number edge costs $w$ and every $t \ge 0$, the probability that a
uniformly random configuration of $t$ pebbles on $G$ is solvable is at most $1$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, characteristic lemma of the Section 3.1 definition.

Formalized by `MetaMathlibExt.solvableConfigurationProb_le_one`, a theorem declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#solvable-configuration-prob-le-one).

## Grid graph

For natural numbers $d$ and $k$, the $d$-dimensional grid
$P_k^d = \square_{i\lt d} P_k$ is the simple graph on $\{0, \dots, k-1\}^d$ in which $x$ and $y$
are adjacent when there is a coordinate $i$ with $x_j = y_j$ for all $j \ne i$ and
$|x_i - y_i| = 1$. For $k = 2$ this is the $d$-cube $Q_d$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 2.1 (grids and cubes).

Formalized by `MetaMathlibExt.gridGraph`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#grid-graph).

## Grid edge costs

Let $d$ and $k$ be natural numbers and let $w_0, \dots, w_{d-1}$ be
natural numbers. The grid cost with cost $w_i$ in coordinate $i$ assigns to each unordered pair
$\{x, y\}$ of points of $\{0, \dots, k-1\}^d$ the sum of the $w_i$ over the coordinates $i$ with
$x_i \ne y_i$. On an edge of the grid exactly one coordinate differs, so an edge in coordinate
$i$ costs $w_i$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Section 3.2 (cost `wᵢ` in coordinate `i`).

Formalized by `MetaMathlibExt.gridCost`, a definition declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#grid-cost).

## Grid cost of a pair differing in one coordinate

Let $d$ and $k$ be natural numbers, let
$w_0, \dots, w_{d-1}$ be natural numbers, let $x, y \in \{0, \dots, k-1\}^d$, and let
$i \in \{0, \dots, d-1\}$. If $x_i \ne y_i$ and $x_j = y_j$ for every $j \ne i$, then the grid
cost of the pair $\{x, y\}$ with cost $w_j$ in coordinate $j$ is $w_i$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, characteristic lemma of the Section 3.2 grid costs.

Formalized by `MetaMathlibExt.gridCost_eq_of_eq_off`, a theorem declared in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#grid-cost-eq-of-eq-off).

## Threshold version of Geroldinger's theorem

Let $d \ge 0$, let $p_1, \dots, p_d$ be
primes, not necessarily distinct, and for each $k$ let
$\Gamma_k = \prod_{i=1}^d \mathbb{Z}/p_i^k\mathbb{Z}$, and let $P_{1/2}(\Gamma_k)$ be its
half-good threshold. Write $\lg = \log_2$. Then there is a real constant $C$ such that for all
sufficiently large $k$,

$$
P_{1/2}(\Gamma_k) \le k^d \exp\left(\left(\frac{(d+1)! \prod_{i=1}^d \lg p_i}{2}
\lg k\right)^{1/(d+1)} - \frac{d}{d+1} \lg \lg k + C\right).
$$

This is an upper bound only, as in the journal record (the source's final comments say the bound
need not be an equality). The case $d = 0$, where $\Gamma_k$ is trivial, is included.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Theorem 4.

Stated but not proved: `MetaMathlibExt.halfGoodThreshold_pi_zmod_prime_pow_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#half-good-threshold-pi-zmod-prime-pow-le).

## Bushaw–Kettle pebbling threshold for grids

Let $d \ge 1$ and let $w_0, \dots, w_{d-1}$
be natural numbers with $w_i \ge 2$ for every $i$. For each $k$ give the grid $P_k^d$ on
$\{0, \dots, k-1\}^d$ the cost $w_i$ on every edge in coordinate $i$, and let
$t : \mathbb{N} \to \mathbb{R}$ be a threshold function, as $k \to \infty$, for the probability
that a uniformly random configuration of $s$ pebbles on $P_k^d$ is solvable. Write $\lg = \log_2$
and

$$
A(k) = \left(\frac{(d+1)! \prod_{i\lt d} \lg w_i}{2} \lg k\right)^{1/(d+1)} -
\frac{d}{d+1} \lg \lg k.
$$

Then there is a real constant $C$ such that for all sufficiently large $k$,

$$
k^d e^{A(k) - C} \le t(k) \le k^d e^{A(k) + C},
$$

that is, with $n = k^d$, $t(k) = n \exp[A(k) + O(1)]$.

The hypothesis $w_i \ge 2$ is not part of the quoted statement: with all costs equal to $1$
every nonempty configuration is solvable, so the thresholds are bounded while the right side
tends to infinity. Likewise $d \ge 1$ excludes $d = 0$, where the grid is a single vertex.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Theorem 9 (quoting Bushaw and Kettle).

Stated but not proved: `MetaMathlibExt.gridGraph_pebbling_threshold_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#grid-graph-pebbling-threshold-eq).

## Pebbling threshold bounds for the cubes (Czygrinow–Wagner, Alon)

For $d \ge 0$ let
$Q_d$ be the $d$-cube, the grid graph on $\{0, 1\}^d$, with cost $2$ on every edge, and let
$t : \mathbb{N} \to \mathbb{R}$ be a threshold function, as $d \to \infty$, for the probability
that a uniformly random configuration of $s$ pebbles on $Q_d$ is solvable. Write $n = 2^d$ and
$\lg = \log_2$. Then for every real $\varepsilon > 0$, as $d \to \infty$,
$n^{1-\varepsilon} = O(t(d))$ and $t(d) = O\big(n / (\lg \lg n)^{1-\varepsilon}\big)$, that is,
$t \in \Omega(n^{1-\varepsilon}) \cap O\big(n / (\lg \lg n)^{1-\varepsilon}\big)$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Theorem 10.

Stated but not proved: `MetaMathlibExt.cube_pebbling_threshold_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#cube-pebbling-threshold-bounds).

## Threshold for good sequences in $\mathbb{Z}_2^d$

Write $\lg = \log_2$. Let $t$ be a
threshold function, in $d$, for the probability that a uniformly random sequence of $s$ elements
of $\mathbb{Z}_2^d$ is good, and write $n = 2^d$. Then for every $\varepsilon > 0$,
$t(d) = O\left(n / (\lg \lg n)^{1-\varepsilon}\right)$ as $d \to \infty$.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Theorem 11.

Stated but not proved: `MetaMathlibExt.zmod_two_pi_good_threshold_isBigO` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#zmod-two-pi-good-threshold-is-big-o).

## Threshold for good sequences in $\mathbb{Z}/35^k\mathbb{Z}$

Write $\lg = \log_2$. Let $t$
be a threshold function, in $k$, for the probability that a uniformly random sequence of $s$
elements of $\mathbb{Z}/35^k\mathbb{Z}$ is good. Then there is a real constant $C$ such that for
all sufficiently large $k$,

$$t(k) \le k^2 \exp\left((3 \lg 5 \lg 7 \lg k)^{1/3} - \tfrac{2}{3} \lg \lg k + C\right).$$

The source writes the prefactor as $n$; here $n = k^2$, the factor $k^d$ of the source's
Theorem 4 at $d = 2$, since $\mathbb{Z}/35^k\mathbb{Z} \cong \mathbb{Z}/5^k\mathbb{Z} \times
\mathbb{Z}/7^k\mathbb{Z}$. The constant $C$ depends on $t$: thresholds are only determined up to
constant factors, so no single $C$ serves every threshold.

## Sources

- Neal Bushaw and Glenn Hurlbert, *Thresholds for Zero-Sums with Small Cross Numbers in Abelian Groups*, INTEGERS 24 (2024), Article A93, Corollary 2.

Stated but not proved: `MetaMathlibExt.zmod_thirtyFive_pow_good_threshold_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/SmallCrossNumberZeroSumWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html#zmod-thirty-five-pow-good-threshold-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zero-sum subsequences of small cross number](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/zero-sum-subset-sums/zero-sum-subsequences-of-small-cross-number)
