---
declaration: section
origin: cited
lean: MetaMathlibExt.card_lift_padicVal_gt_one_le_one, MetaMathlibExt.card_padicVal_gt_one_le_natDegree, MetaMathlibExt.card_lift_padicVal_eq_one, MetaMathlibExt.card_common_lift_padicVal_of_gradients_independent, MetaMathlibExt.card_padicVal_eq_one_mod_sq_eq, MetaMathlibExt.card_lift_padicVal_eq_one_of_singular, MetaMathlibExt.card_common_lift_padicVal_of_gradients_dependent, MetaMathlibExt.valuationCurvePoints
statement: formalized
---

# Points of valuation one of two-variable polynomials

22 results, 12 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html).

## At most one lift has valuation above one

Let $p$ be a prime, $g \in \mathbb{Z}[x]$ and
$r$ an integer with $0 \le r < p$ such that $g(r)$ and $g'(r)$ are not both divisible by $p$.
Then at most one $k \in \{0, \dots, p - 1\}$ satisfies $p^2 \mid g(r + kp)$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Proposition 1.

Stated but not proved: `MetaMathlibExt.card_lift_padicVal_gt_one_le_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-lift-padic-val-gt-one-le-one).

## Few residues modulo $p^2$ with valuation above one

Let $g \in \mathbb{Z}[x]$ be a
non-zero polynomial of degree $d$ with non-zero discriminant. Then there is a natural number $P$
such that for every prime $p \ge P$, at most $d$ integers $x$ with $0 \le x < p^2$ satisfy
$p^2 \mid g(x)$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Corollary 1.

Stated but not proved: `MetaMathlibExt.card_padicVal_gt_one_le_natDegree` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-padic-val-gt-one-le-nat-degree).

## Lifts of a nonsingular point with valuation one

Let $p$ be a prime, let
$f \in \mathbb{Z}[x, y]$ have partial derivatives $f_x$ and $f_y$, and let $r, s$ be integers in
$\{0, \dots, p - 1\}$ with $p \mid f(r, s)$ such that $f_x(r, s)$ and $f_y(r, s)$ are not both
divisible by $p$. Then exactly $p(p - 1)$ of the pairs $(k, l)$ with $0 \le k, l < p$ satisfy
$p \mid f(r + kp, s + lp)$ and $p^2 \nmid f(r + kp, s + lp)$, that is,
$\nu_p(f(r + kp, s + lp)) = 1$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Proposition 2.

Stated but not proved: `MetaMathlibExt.card_lift_padicVal_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-lift-padic-val-eq-one).

## Common lifts of two points with independent gradients

Let $p$ be a prime, let
$f \in \mathbb{Z}[x, y]$ have partial derivatives $f_x$ and $f_y$, and let $(r_1, s_1)$ and
$(r_2, s_2)$ be pairs of integers in $\{0, \dots, p - 1\}$ with $p \mid f(r_i, s_i)$ for
$i = 1, 2$ and

$$
p \nmid f_x(r_1, s_1) f_y(r_2, s_2) - f_y(r_1, s_1) f_x(r_2, s_2).
$$

Write $F_i(k, l) = f(r_i + kp, s_i + lp)$. Among the pairs $(k, l)$ with $0 \le k, l < p$,
exactly $(p - 1)^2$ have $p \mid F_i(k, l)$ and $p^2 \nmid F_i(k, l)$ for both $i$, exactly
$p - 1$ have $p^2 \mid F_1(k, l)$, $p \mid F_2(k, l)$ and $p^2 \nmid F_2(k, l)$, and exactly
one has $p^2 \mid F_1(k, l)$ and $p^2 \mid F_2(k, l)$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Proposition 3.

Stated but not proved: `MetaMathlibExt.card_common_lift_padicVal_of_gradients_independent` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-common-lift-padic-val-of-gradients).

## Number of points of valuation one modulo $p^2$

Let $p$ be a prime and let
$f \in \mathbb{Z}[x, y]$ have partial derivatives $f_x$ and $f_y$. Suppose that for all integers
$r, s \in \{0, \dots, p - 1\}$ with $p \mid f(r, s)$, the integers $f_x(r, s)$ and $f_y(r, s)$
are not both divisible by $p$. Let $m$ be the number of pairs $(r, s)$ with $0 \le r, s < p$ and
$p \mid f(r, s)$. Then the number of pairs $(x, y)$ with $0 \le x, y < p^2$, $p \mid f(x, y)$
and $p^2 \nmid f(x, y)$ is $m p (p - 1)$.

Without the hypothesis on $f_x$ and $f_y$ the count fails: for $f = x^2 - y^2$ and $p = 3$ one
has $m = 5$, but only $24$ pairs, not $30$, have valuation $1$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Corollary 2.

Stated but not proved: `MetaMathlibExt.card_padicVal_eq_one_mod_sq_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-padic-val-eq-one-mod-sq-eq).

## Lifts of a singular point with valuation one

Let $p$ be a prime, let
$f \in \mathbb{Z}[x, y]$ have partial derivatives $f_x$ and $f_y$, and let $r, s$ be integers in
$\{0, \dots, p - 1\}$ such that $p$ divides $f(r, s)$, $f_x(r, s)$ and $f_y(r, s)$. Then the
number of pairs $(k, l)$ with $0 \le k, l < p$, $p \mid f(r + kp, s + lp)$ and
$p^2 \nmid f(r + kp, s + lp)$ is $0$ if $p^2 \mid f(r, s)$, and $p^2$ otherwise.

The cited statement prints the two cases swapped. By the paper's eq. (7) every lift
$f(r + kp, s + lp)$ is congruent to $f(r, s)$ modulo $p^2$. The printed version fails for
$f = x^2 + y^2 + 3$, $p = 3$, $(r, s) = (0, 0)$: $f(0, 0) = 3$ is not divisible by $9$, and all
$9$ lifts have valuation $1$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Corollary 3.

Stated but not proved: `MetaMathlibExt.card_lift_padicVal_eq_one_of_singular` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-lift-padic-val-eq-one-of-singular).

## Common lifts of two points with dependent gradients

Let $p$ be a prime, let
$f \in \mathbb{Z}[x, y]$ have partial derivatives $f_x$ and $f_y$, and let $(r_1, s_1)$ and
$(r_2, s_2)$ be pairs of integers in $\{0, \dots, p - 1\}$ with $p \mid f(r_i, s_i)$ for
$i = 1, 2$. Write $a_i = f_x(r_i, s_i)$, $b_i = f_y(r_i, s_i)$ and $c_i = f(r_i, s_i)/p$.
Suppose that for each $i$ the integers $a_i$ and $b_i$ are not both divisible by $p$, and that
$p \mid a_1 b_2 - b_1 a_2$. Write $F_i(k, l) = f(r_i + kp, s_i + lp)$, and among the pairs
$(k, l)$ with $0 \le k, l < p$ let $n_1$ be the number with $p \mid F_i(k, l)$ and
$p^2 \nmid F_i(k, l)$ for both $i$, let $n_2$ be the number with $p^2 \mid F_1(k, l)$,
$p \mid F_2(k, l)$ and $p^2 \nmid F_2(k, l)$, and let $n_3$ be the number with
$p^2 \mid F_1(k, l)$ and $p^2 \mid F_2(k, l)$. If $p$ divides both $a_1 c_2 - c_1 a_2$ and
$b_1 c_2 - c_1 b_2$ (the matrix with rows $(a_i, b_i, c_i)$ has rank $1$ modulo $p$), then
$n_1 = p(p - 1)$, $n_2 = 0$ and $n_3 = p$. Otherwise (rank $2$) $n_1 = p(p - 2)$, $n_2 = p$
and $n_3 = 0$.

The source assumes only that $f$ has no zero modulo $p^2$ at which $f_x \equiv f_y \equiv 0
\pmod p$ and that one column is non-zero. The counts need both gradients $(a_i, b_i)$ non-zero
modulo $p$, which the paper's Case 2 uses. Without this they fail for $f = -x^2 + y^2 - x - 1$,
$p = 3$, $(r_1, s_1) = (0, 1)$, $(r_2, s_2) = (1, 0)$: the gradient vanishes at $(1, 0)$, the
rank is $2$, and $(n_1, n_2, n_3) = (6, 3, 0)$ rather than $(3, 3, 0)$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Proposition 4.

Stated but not proved: `MetaMathlibExt.card_common_lift_padicVal_of_gradients_dependent` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#card-common-lift-padic-val-of-gradients-2).

## Points of $C_f(\mathbb{F}_p)$

For $f \in \mathbb{Z}[x, y]$ and a natural number $p$,
$C_f(\mathbb{F}_p)$ is the set of pairs $(r, s)$ of natural numbers with $r, s < p$ such that $p$
divides $f(r, s)$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1 (definition of `C_f(𝔽_p)` and `m = |C_f(𝔽_p)|`).

Formalized by `MetaMathlibExt.valuationCurvePoints`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-curve-points).

## $C_f(\mathbb{F}_p)$ has at most $p^2$ points

For every $f \in \mathbb{Z}[x, y]$ and
every natural number $p$, the set $C_f(\mathbb{F}_p)$ of pairs $(r, s)$ of natural numbers with
$r, s < p$ such that $p$ divides $f(r, s)$ has at most $p^2$ elements.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1 (definition of `C_f(𝔽_p)`).

Formalized by `MetaMathlibExt.valuationCurvePoints_card_le`, a theorem declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-curve-points-card-le).

## Valuation row of a point

For $f \in \mathbb{Z}[x, y]$ with partial derivatives $f_x$ and
$f_y$, a natural number $p$ and a pair $(r, s)$ of natural numbers, the valuation row at $(r, s)$
is the vector $(f_x(r, s), f_y(r, s), q)$ reduced modulo $p$, an element of
$(\mathbb{Z}/p\mathbb{Z})^3$, where $q$ is $f(r, s)/p$ rounded down ($q = 0$ when $p = 0$).
These are the rows of the matrix in the paper's eq. (2); when $p$ divides $f(r, s)$, the
division by $p$ is exact.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1, eq. (2).

Formalized by `MetaMathlibExt.valuationRow`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-row).

## Distinct $k$-tuples of points of $C_f(\mathbb{F}_p)$

For $f \in \mathbb{Z}[x, y]$ and
natural numbers $p$ and $k$, let $C_f(\mathbb{F}_p)$ be the set of pairs $(r, s)$ of natural
numbers with $r, s < p$ such that $p$ divides $f(r, s)$. The distinct $k$-tuples of points of
$C_f(\mathbb{F}_p)$ are the $k$-tuples $(P_1, \dots, P_k)$ with every $P_i$ in $C_f(\mathbb{F}_p)$
and $P_i \ne P_j$ for $i \ne j$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1 (definition of `m_k(f, p)`) and Section 3 (sums over `l₁ ≠ l₂ ≠ ⋯ ≠ l_k`).

Formalized by `MetaMathlibExt.valuationDistinctTuples`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-distinct-tuples).

## Rank-two tuple count $m_k(f, p)$

For $f \in \mathbb{Z}[x, y]$ and natural numbers $p$
and $k$, let $C_f(\mathbb{F}_p)$ be the set of pairs $(r, s)$ of natural numbers with $r, s < p$
such that $p$ divides $f(r, s)$. Then $m_k(f, p)$ is the number of $k$-tuples
$P = (P_1, \dots, P_k)$ of pairwise distinct points of $C_f(\mathbb{F}_p)$ such that the
$k \times 3$ matrix $B_k(P)$ over $\mathbb{Z}/p\mathbb{Z}$ whose $i$-th row is the valuation row
at $P_i$ has rank $2$ and the $k \times 2$ submatrix of its first two columns also has
rank $2$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1 (definition of `m_k(f, p)` after eq. (2)).

Formalized by `MetaMathlibExt.valuationRankTwoTupleCount`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-rank-two-tuple-count).

## The rank-two tuple count vanishes for $k = 1$

For every $f \in \mathbb{Z}[x, y]$ and
every prime $p$, the rank-two tuple count $m_1(f, p)$ is $0$: a matrix with a single row has rank
at most $1$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1 ("For `k = 1`, we observe that `m_k(f, p) = 0` trivially").

Formalized by `MetaMathlibExt.valuationRankTwoTupleCount_one`, a theorem declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-rank-two-tuple-count-one).

## Rank-one tuple count $o_k(f, p)$

For $f \in \mathbb{Z}[x, y]$ and natural numbers $p$
and $k$, let $C_f(\mathbb{F}_p)$ be the set of pairs $(r, s)$ of natural numbers with $r, s < p$
such that $p$ divides $f(r, s)$. Then $o_k(f, p)$ is the number of $k$-tuples
$P = (P_1, \dots, P_k)$ of pairwise distinct points of $C_f(\mathbb{F}_p)$ such that the
$k \times 3$ matrix $B_k(P)$ over $\mathbb{Z}/p\mathbb{Z}$ whose $i$-th row is the valuation row
at $P_i$ has rank $1$ and the first two columns of $B_k(P)$ are not both zero.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 3 (definition of `o_k(f, p)` before Proposition 6).

Formalized by `MetaMathlibExt.valuationRankOneTupleCount`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-rank-one-tuple-count).

## Common lift count

Let $f \in \mathbb{Z}[x, y]$, let $p$ and $k$ be natural numbers and
let $P = ((r_1, s_1), \dots, (r_k, s_k))$ be a $k$-tuple of pairs of natural numbers. The common
lift count of $P$ is the number of pairs $(a, b)$ of natural numbers with $a, b < p$ such that
$p^2$ divides $f(r_i + ap, s_i + bp)$ for every $i$.

For a prime $p$ this says that every lift $(r_i + ap, s_i + bp)$ has $p$-adic valuation of $f$
greater than $1$ (a zero value counts as valuation greater than $1$); divided by $p^2$, the count
is the probability of this event for a uniformly random $(a, b) \in \mathbb{F}_p^2$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 3 (definition of the indicator random variables `Y_{x,y}`).

Formalized by `MetaMathlibExt.valuationCommonLiftCount`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-common-lift-count).

## The common lift count is at most $p^2$

For every $f \in \mathbb{Z}[x, y]$, all natural
numbers $p$ and $k$ and every $k$-tuple $P$ of pairs of natural numbers, the common lift count of
$P$ is at most $p^2$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 3 (definition of the indicator random variables `Y_{x,y}`).

Formalized by `MetaMathlibExt.valuationCommonLiftCount_le`, a theorem declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-common-lift-count-le).

## Count of points of high valuation in a square

For a polynomial $f \in \mathbb{Z}[x, y]$
and natural numbers $p$, $k$ and $l$, $X(k, l)$ is the number of points $(x, y)$ of the square
$\{kp, \dots, kp + p - 1\} \times \{lp, \dots, lp + p - 1\}$ with $p^2 \mid f(x, y)$. For a
prime $p$ this is the condition $\nu_p(f(x, y)) > 1$, where points with $f(x, y) = 0$ count.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1, eq. (1).

Formalized by `MetaMathlibExt.valuationSquareCount`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-square-count).

## Trivial bound for the square count

For every polynomial $f \in \mathbb{Z}[x, y]$ and all
natural numbers $p$, $k$ and $l$, the number $X(k, l)$ of points $(x, y)$ of the square
$\{kp, \dots, kp + p - 1\} \times \{lp, \dots, lp + p - 1\}$ with $p^2 \mid f(x, y)$ is at most
$p^2$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1, eq. (1).

Formalized by `MetaMathlibExt.valuationSquareCount_le`, a theorem declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-square-count-le).

## Rajkumar–Shubham Conjecture 1

For $f \in \mathbb{Z}[x, y]$, the proposition that for
every $k \ge 2$, $m_k(f, p)/p^2 \to 1$ as $p \to \infty$ through the primes, where $m_k(f, p)$ is
the rank-two tuple count.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Section 1, Conjecture 1, eq. (3).

Formalized by `MetaMathlibExt.ValuationConjectureOne`, a definition declared in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#valuation-conjecture-one).

## Sum of expectations over distinct tuples of points

Let $p$ be a prime, let
$f \in \mathbb{Z}[x, y]$ have partial derivatives $f_x$ and $f_y$, and let $C_f(\mathbb{F}_p)$
be the set of pairs of integers $0 \le r, s < p$ with $p \mid f(r, s)$. Suppose that no
$(r, s) \in C_f(\mathbb{F}_p)$ has $p \mid f_x(r, s)$ and $p \mid f_y(r, s)$, and let $k \ge 1$.
For a $k$-tuple $P$ of points of $C_f(\mathbb{F}_p)$, let $N(P)$ be the number of pairs
$(a, b)$ with $0 \le a, b < p$ such that $p^2 \mid f(r + ap, s + bp)$ for every point $(r, s)$
of $P$. Then

$$
\sum_P \frac{N(P)}{p^2} = \frac{m_k(f, p)}{p^2} + \frac{o_k(f, p)}{p},
$$

where $P$ runs over the $k$-tuples of pairwise distinct points of $C_f(\mathbb{F}_p)$. Here
$m_k(f, p)$ is the number of such $P$ whose matrix $B_k(P)$, with rows
$(f_x(r, s), f_y(r, s), f(r, s)/p)$ modulo $p$ at the points of $P$, has rank $2$ and whose first
two columns have rank $2$, and $o_k(f, p)$ is the number of such $P$ for which $B_k(P)$ has rank
$1$ and its first two columns are not both zero.

In the paper's notation the left side is $\sum_{l_1 \ne \dots \ne l_k} E[Y_{l_1} \cdots Y_{l_k}]$
(eq. (15)). The hypothesis is the paper's standing assumption of Section 3 at this $p$; its
proof uses it to rule out rank $0$.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Proposition 6, eq. (15).

Stated but not proved: `MetaMathlibExt.sum_expectation_distinct_tuples_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#sum-expectation-distinct-tuples-eq).

## Sums of expectations over distinct tuples tend to one

Let $f \in \mathbb{Z}[x, y]$ have
partial derivatives $f_x$ and $f_y$, and for a prime $p$ let $C_f(\mathbb{F}_p)$ be the set of
pairs of integers $0 \le r, s < p$ with $p \mid f(r, s)$. Suppose that there is a natural number
$P_0$ such that for every prime $p \ge P_0$ and all integers $x, y$, the integers $f(x, y)$,
$f_x(x, y)$ and $f_y(x, y)$ are not all divisible by $p$; that $|C_f(\mathbb{F}_p)|/p \to 1$ as
$p \to \infty$ through the primes; and that Conjecture 1 holds for $f$. For a tuple $P$ of points
of $C_f(\mathbb{F}_p)$, let $N(P)$ be the number of pairs $(a, b)$ with $0 \le a, b < p$ such that
$p^2 \mid f(r + ap, s + bp)$ for every point $(r, s)$ of $P$. Then for every $k \ge 1$,
$\sum_P N(P)/p^2 \to 1$ as $p \to \infty$ through the primes, where $P$ runs over the $k$-tuples
of pairwise distinct points of $C_f(\mathbb{F}_p)$.

In the paper's notation the sum is $\sum_{l_1 \ne \dots \ne l_k} E[Y_{l_1} \cdots Y_{l_k}]$.
The paper's proof takes $|C_f(\mathbb{F}_p)|/p \to 1$ from the Hasse–Weil bounds, which need an
irreducibility hypothesis the paper does not state; it is assumed directly here.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Corollary 5, under the standing assumption of Section 3.

Stated but not proved: `MetaMathlibExt.tendsto_sum_expectation_distinct_tuples` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#tendsto-sum-expectation-distinct-tuples).

## Poisson limit for points of valuation $> 1$

Let $f \in \mathbb{Z}[x, y]$ have partial
derivatives $f_x$ and $f_y$, and for a prime $p$ let $C_f(\mathbb{F}_p)$ be the set of pairs of
integers $0 \le r, s < p$ with $p \mid f(r, s)$. Suppose that there is a natural number $P_0$
such that for every prime $p \ge P_0$ and all integers $x, y$, the integers $f(x, y)$,
$f_x(x, y)$ and $f_y(x, y)$ are not all divisible by $p$; that $|C_f(\mathbb{F}_p)|/p \to 1$ as
$p \to \infty$ through the primes; and that Conjecture 1 holds for $f$. For $0 \le k, l < p$ let
$X(k, l)$ be the number of points $(x, y)$ of the square
$\{kp, \dots, kp + p - 1\} \times \{lp, \dots, lp + p - 1\}$ with $p^2 \mid f(x, y)$. Then for
every $j \ge 0$,

$$
\frac{\#\{(k, l) : 0 \le k, l < p,\ X(k, l) = j\}}{p^2} \to \frac{e^{-1}}{j!}
$$

as $p \to \infty$ through the primes. That is, for $(k, l)$ uniformly random in
$\{0, \dots, p - 1\}^2$, $X(k, l)$ converges in distribution to a Poisson variable with
parameter $1$ (for $\mathbb{N}$-valued variables, pointwise convergence of the mass functions is
convergence in distribution).

The hypothesis $|C_f(\mathbb{F}_p)|/p \to 1$ is the Hasse–Weil input of the paper's proof,
assumed directly, as in the companion statement about sums over distinct tuples.

## Sources

- Krishnan Rajkumar and Shubham, *On the Distribution of Points of Valuation 1 for a Polynomial in Two Variables*, INTEGERS 26 (2026), Article A82, Theorem 1.

Stated but not proved: `MetaMathlibExt.tendsto_valuationSquareCount_poisson` is written with `theorem_wanted` in [WantedExt/NumberTheory/ValuationOnePointsWanted.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ValuationOnePointsWanted.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html#tendsto-valuation-square-count-poisson).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Points of valuation one of two-variable polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/p-adic-numbers/points-of-valuation-one-of-two-variable-polynomi)
