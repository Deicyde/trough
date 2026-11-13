---
declaration: section
origin: cited
lean: StochasticMatrix, StochasticMatrix.matPow, StochasticMatrix.IsIrreducible, StochasticMatrix.Distribution, StochasticMatrix.IsStationary, StochasticMatrix.DetailedBalance, StochasticMatrix.IsReversible, StochasticMatrix.KolmogorovCycleCondition
statement: formalized
proof: formalized
---

# Kolmogorov's criterion for reversibility

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html).

## Stochastic matrix

For a natural number $M$, a stochastic matrix of size $M + 1$ is a
square matrix $P = (P_{ij})$ indexed by the states $\{0, 1, \dots, M\}$, with real entries
$P_{ij} \ge 0$ for all states $i, j$, whose rows sum to $1$: $\sum_j P_{ij} = 1$ for every $i$.
It is the transition matrix of a Markov chain on these $M + 1$ states.

Formalized by `StochasticMatrix`, a structure declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#stochastic-matrix).

## Matrix powers of a stochastic matrix

For a stochastic matrix $P$ on the finite state
space $\{0, 1, \dots, M\}$ and $n \in \mathbb{N}$, the $n$-th matrix power $P^n$ is defined by
$P^0 = I$, the identity matrix, and $(P^{n+1})_{ij} = \sum_k P(i, k) (P^n)_{kj}$. The entry
$(P^n)_{ij}$ is the probability of moving from state $i$ to state $j$ in exactly $n$ steps.

Formalized by `StochasticMatrix.matPow`, a definition declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#mat-pow).

## Irreducible stochastic matrix

Let $P$ be a stochastic matrix on the finite state space
$\{0, 1, \dots, M\}$ and write $P^n$ for its $n$-th matrix power. Then $P$ is irreducible if for
all states $i$ and $j$ there is an $n \ge 1$ with $(P^n)_{ij} > 0$; that is, every state can be
reached from every state, itself included, in a positive number of steps.

Formalized by `StochasticMatrix.IsIrreducible`, a definition declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#is-irreducible).

## Probability distribution on a finite state space

A probability distribution on the
finite state space $\{0, 1, \dots, M\}$ is a function $\pi$ from the states to $\mathbb{R}$
with $\pi(i) \ge 0$ for every state $i$ and $\sum_i \pi(i) = 1$.

Formalized by `StochasticMatrix.Distribution`, a structure declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#distribution).

## Stationary distribution

A probability distribution $\pi$ on the finite state space
$\{0, 1, \dots, M\}$ is stationary for a stochastic matrix $P$ on the same states if
$\pi P = \pi$, that is, $\sum_i \pi(i) P(i, j) = \pi(j)$ for every state $j$.

Formalized by `StochasticMatrix.IsStationary`, a definition declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#is-stationary).

## Detailed balance

A probability distribution $\pi$ and a stochastic matrix $P$ on the
finite state space $\{0, 1, \dots, M\}$ satisfy the detailed balance (reversibility) equations
when $\pi(i) P(i, j) = \pi(j) P(j, i)$ for all states $i$ and $j$.

Formalized by `StochasticMatrix.DetailedBalance`, a definition declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#detailed-balance).

## Reversible stochastic matrix

A stochastic matrix $P$ on the finite state space
$\{0, 1, \dots, M\}$ is reversible if there is a probability distribution $\pi$ on the states
that is stationary for $P$ and satisfies the detailed balance equations
$\pi(i) P(i, j) = \pi(j) P(j, i)$ for all states $i, j$.

Formalized by `StochasticMatrix.IsReversible`, a definition declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#is-reversible).

## Kolmogorov's cycle condition

A stochastic matrix $P$ on the finite state space
$\{0, 1, \dots, M\}$ satisfies Kolmogorov's cycle condition when (1) for all states $x, y$,
$P(x, y) > 0$ implies $P(y, x) > 0$; and (2) for every $n \ge 0$ and every loop of states
$x_0, x_1, \dots, x_n$ with $x_n = x_0$ and $\prod_{i=0}^{n-1} P(x_{i+1}, x_i) > 0$, we have
$\prod_{i=0}^{n-1} P(x_i, x_{i+1}) = \prod_{i=0}^{n-1} P(x_{i+1}, x_i)$.

Formalized by `StochasticMatrix.KolmogorovCycleCondition`, a structure declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#kolmogorov-cycle-condition).

## Detailed balance implies stationarity

Let $P$ be a stochastic matrix on the finite state
space $\{0, 1, \dots, M\}$ and let $\pi$ be a probability distribution on the same states. If
$\pi$ and $P$ satisfy the detailed balance equations $\pi(i) P(i, j) = \pi(j) P(j, i)$ for all
states $i, j$, then $\pi$ is stationary for $P$: $\sum_i \pi(i) P(i, j) = \pi(j)$ for every
state $j$.

Formalized by `StochasticMatrix.detailedBalance_isStationary`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#detailed-balance-is-stationary).

## Powers of a stochastic matrix are nonnegative

Every entry of every power of a stochastic matrix is nonnegative.

Formalized by `StochasticMatrix.matPow_nonneg`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#mat-pow-nonneg).

## Detailed balance distributions of irreducible chains are positive

Let $P$ be an
irreducible stochastic matrix on the finite state space $\{0, 1, \dots, M\}$. If a probability
distribution $\pi$ satisfies the detailed balance equations $\pi(i) P(i, j) = \pi(j) P(j, i)$
for all states $i, j$, then $\pi(i) > 0$ for every state $i$.

Formalized by `StochasticMatrix.distribution_pos_of_irreducible_detailedBalance`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#distribution-pos-of-irreducible-detailed).

## Kolmogorov's cycle theorem, necessity half

Let $P$ be an irreducible stochastic matrix
on the finite state space $\{0, 1, \dots, M\}$. If $P$ is reversible, that is, some probability
distribution $\pi$ is stationary for $P$ and satisfies the detailed balance equations
$\pi(i) P(i, j) = \pi(j) P(j, i)$ for all states $i, j$, then $P$ satisfies Kolmogorov's cycle
condition: (1) for all states $x, y$, $P(x, y) > 0$ implies $P(y, x) > 0$; and (2) for every
$n \ge 0$ and every loop of states $x_0, x_1, \dots, x_n$ with $x_n = x_0$ and
$\prod_{i=0}^{n-1} P(x_{i+1}, x_i) > 0$, we have
$\prod_{i=0}^{n-1} P(x_i, x_{i+1}) = \prod_{i=0}^{n-1} P(x_{i+1}, x_i)$.

Formalized by `StochasticMatrix.kolmogorov_cycle_necessity`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleNecessity.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleNecessity.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#kolmogorov-cycle-necessity).

## Forward path product

For a stochastic matrix $P$ and a path of states
$x_0, x_1, \dots, x_k$, the path product is the real number
$\prod_{i=0}^{k-1} P(x_i, x_{i+1})$, the product of the forward transition probabilities along
the path. For the empty path and for a path consisting of a single state it is $1$.

Formalized by `StochasticMatrix.listPathProduct`, a definition declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-path-product).

## Path products are nonnegative

Let $P$ be a stochastic matrix on the states
$\{0, \dots, M\}$. For every path (finite list of states), the product of the forward transition
probabilities $P(x, y)$ over consecutive states $x, y$ along the path is nonnegative.

Formalized by `StochasticMatrix.listPathProduct_nonneg`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-path-product-nonneg).

## Ratio product along a path

For a stochastic matrix $P$ and a path of states
$x_0, x_1, \dots, x_k$, the ratio product is the real number
$\prod_{i=0}^{k-1} \frac{P(x_i, x_{i+1})}{P(x_{i+1}, x_i)}$, where a quotient with
denominator $0$ is taken to be $0$. For the empty path and for a path consisting of a single
state it is $1$.

This is the quantity that defines the "cycle weight" used to construct a reversible measure
from Kolmogorov's cycle condition.

Formalized by `StochasticMatrix.listRatioProduct`, a definition declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product).

## The ratio product is nonnegative

For a stochastic matrix $P$, the ratio product along
every path of states is nonnegative.

Formalized by `StochasticMatrix.listRatioProduct_nonneg`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-nonneg).

## Positive paths have positive ratio product

Let $P$ be a stochastic matrix such that
$P(x, y) > 0$ implies $P(y, x) > 0$ for all states $x$ and $y$. If the forward path product
along a path of states is positive, then the ratio product along that path is positive.

Formalized by `StochasticMatrix.listRatioProduct_pos_of_listPathProduct_pos`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-pos-of-list-path-prod).

## Paths from positive matrix powers

Let $P$ be a stochastic matrix on the states
$\{0, \dots, M\}$. If $n > 0$ and the $(i, j)$ entry of the $n$-th matrix power $P^n$ is positive,
then there is a path from $i$ to $j$ (a finite list of states starting at $i$ and ending at $j$)
along which the product of the transition probabilities $P(x, y)$ over consecutive states $x, y$
is positive.

Formalized by `StochasticMatrix.exists_path_of_matPow_pos`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#exists-path-of-mat-pow-pos).

## Irreducible chains have positive paths

Let $P$ be an irreducible stochastic matrix on the
states $\{0, \dots, M\}$. For any two states $i, j$ there is a path from $i$ to $j$ (a finite list
of states starting at $i$ and ending at $j$) along which the product of the transition
probabilities $P(x, y)$ over consecutive states $x, y$ is strictly positive.

Formalized by `StochasticMatrix.IsIrreducible.exists_path`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#exists-path).

## First step of the ratio product

Let $P$ be a stochastic matrix, $n$ a natural number
and $c_0, c_1, \dots, c_{n+1}$ states. Then the ratio product along $c_0, c_1, \dots, c_{n+1}$
equals $\frac{P(c_0, c_1)}{P(c_1, c_0)}$ times the ratio product along $c_1, \dots, c_{n+1}$,
where a quotient with denominator $0$ is taken to be $0$.

Formalized by `StochasticMatrix.listRatioProduct_cons_ofFn`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-cons-of-fn).

## The ratio product as a finite product

Let $P$ be a stochastic matrix, $n$ a natural
number and $c_0, c_1, \dots, c_n$ states. Then the ratio product along $c_0, c_1, \dots, c_n$
equals $\prod_{i=0}^{n-1} \frac{P(c_i, c_{i+1})}{P(c_{i+1}, c_i)}$, where a quotient with
denominator $0$ is taken to be $0$.

Formalized by `StochasticMatrix.listRatioProduct_ofFn`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-of-fn).

## The ratio product around a loop is one

Let $P$ be a stochastic matrix satisfying
Kolmogorov's cycle condition, and let $x_0, x_1, \dots, x_n$ be a path of states with
$n \ge 1$ and $x_0 = x_n$ such that $P(x_{i+1}, x_i) > 0$ for every $i < n$. Then the ratio
product along $x_0, x_1, \dots, x_n$ equals $1$.

Formalized by `StochasticMatrix.listRatioProduct_cycle_eq_one`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-cycle-eq-one).

## Cycle weight

Let $P$ be an irreducible stochastic matrix on the states
$\{0, \dots, M\}$ and fix a reference state $i_0$. The cycle weight of a state $j$ relative to
$i_0$ is the product of the ratios $P(x, y) / P(y, x)$ over consecutive states $x, y$ along a
path (a finite list of states) from $i_0$ to $j$ whose product of transition probabilities
$P(x, y)$ over consecutive states is positive, where a ratio with $P(y, x) = 0$ counts as $0$;
such a path exists by irreducibility, and one is fixed by choice.

For chains satisfying Kolmogorov's cycle condition this value does not depend on the chosen path,
and the weights give a reversible measure.

Formalized by `StochasticMatrix.cycleWeight`, a definition declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#cycle-weight).

## Ratio product of joined paths

Let $P$ be a stochastic matrix and let $x_0, \dots, x_k$
and $y_0, \dots, y_l$ be paths of states with $x_k = y_0$. Then the ratio product along the
joined path $x_0, \dots, x_k, y_1, \dots, y_l$ equals the ratio product along
$x_0, \dots, x_k$ times the ratio product along $y_0, \dots, y_l$.

Formalized by `StochasticMatrix.listRatioProduct_append`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-append).

## Positive path products have positive steps

Let $P$ be a stochastic matrix on the states
$\{0, \dots, M\}$, and let $l$ be a path (a finite list of states) whose $i$-th state, counting
from $0$, is $l_i$. If the product of the transition probabilities $P(x, y)$ over consecutive
states $x, y$ along $l$ is positive, then $P(l_i, l_{i+1}) > 0$ for every $i$ such that $i + 1$
is less than the length of $l$.

Formalized by `StochasticMatrix.listPathProduct_pos_implies_transitions`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-path-product-pos-implies-transition).

## Joining positive paths

Let $P$ be a stochastic matrix on the states $\{0, \dots, M\}$,
and let $l_1, l_2$ be nonempty paths (finite lists of states) such that the last state of $l_1$
is the first state of $l_2$. If the products of the transition probabilities $P(x, y)$ over
consecutive states $x, y$ along $l_1$ and along $l_2$ are both positive, then so is the product
along the path that follows $l_1$ and then $l_2$ with its first state removed.

Formalized by `StochasticMatrix.listPathProduct_append_pos`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-path-product-append-pos).

## Path independence of cycle weight

Let $P$ be an irreducible stochastic matrix on the
states $\{0, \dots, M\}$ satisfying Kolmogorov's cycle condition, and let $i_0, j$ be states. If
two paths (finite lists of states) both start at $i_0$, end at $j$, and have positive product of
the transition probabilities $P(x, y)$ over consecutive states $x, y$, then the products of the
ratios $P(x, y) / P(y, x)$ over consecutive states $x, y$ along the two paths are equal.

This is the key step that makes the cycle weight well-defined and ultimately produces a
reversible measure.

Formalized by `StochasticMatrix.cycleWeight_path_independent`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#cycle-weight-path-independent).

## Ratio product after appending a state

Let $P$ be a stochastic matrix,
$x_0, \dots, x_k$ a path of states and $j$ a state. Then the ratio product along
$x_0, \dots, x_k, j$ equals the ratio product along $x_0, \dots, x_k$ times
$\frac{P(x_k, j)}{P(j, x_k)}$, where a quotient with denominator $0$ is taken to be $0$.

Formalized by `StochasticMatrix.listRatioProduct_snoc`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#list-ratio-product-snoc).

## Cycle weights along a positive transition

Let $P$ be an irreducible stochastic matrix on
the states $\{0, \dots, M\}$ satisfying Kolmogorov's cycle condition, fix a reference state
$i_0$, and write $w(j)$ for the cycle weight of a state $j$ relative to $i_0$. If $i, j$ are
states with $P(i, j) > 0$, then $w(i) \cdot P(i, j) / P(j, i) = w(j)$.

Formalized by `StochasticMatrix.cycleWeight_extend`, a lemma declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#cycle-weight-extend).

## Detailed balance for cycle weights

Let $P$ be an irreducible stochastic matrix on the
states $\{0, \dots, M\}$ satisfying Kolmogorov's cycle condition, fix a reference state $i_0$,
and write $w(j)$ for the cycle weight of a state $j$ relative to $i_0$. Then for all states
$i, j$ we have $w(i) \cdot P(i, j) = w(j) \cdot P(j, i)$.

Formalized by `StochasticMatrix.cycleWeight_detailed_balance`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#cycle-weight-detailed-balance).

## Kolmogorov's cycle theorem, sufficiency

For an irreducible finite
Markov chain satisfying the cycle condition, there exists a reversible
measure: a distribution satisfying the detailed balance equations (and
hence stationary).

Formalized by `StochasticMatrix.kolmogorov_cycle_sufficiency`, a theorem declared in [MathlibExt/Probability/KolmogorovCycleSufficiency.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/KolmogorovCycleSufficiency.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html#kolmogorov-cycle-sufficiency).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolmogorov's criterion for reversibility](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/markov-chains/kolmogorov-s-criterion-for-reversibility)
