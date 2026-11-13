---
declaration: section
origin: cited
lean: MetaMathlibExt.booleanVectorComplement, MetaMathlibExt.booleanFunctionDual, MetaMathlibExt.IsSelfDualMonotone, MetaMathlibExt.booleanVectorComplement_complement, MetaMathlibExt.booleanFunctionDual_dual, MetaMathlibExt.selfDualMonotone_proj, MetaMathlibExt.booleanCubeConcat, MetaMathlibExt.booleanCubeConcat_false
statement: formalized
---

# Self-dual monotone Boolean functions

25 results, 8 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html).

## Complement of a Boolean vector

The complement of a Boolean vector $x \in \{0,1\}^n$ is
the vector $\bar x \in \{0,1\}^n$ obtained by negating every coordinate: $\bar x_i = \lnot x_i$
for every $i < n$.

## Sources

- JIS VOL28/Pawelski, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Pawelski/pawelski22.tex>, lines 72–81.

Formalized by `MetaMathlibExt.booleanVectorComplement`, a definition declared in [MathlibExt/Order/BooleanFunction/SelfDual.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanFunction/SelfDual.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-vector-complement).

## Dual of a Boolean function

For a Boolean function $f \colon \{0,1\}^n \to \{0,1\}$, its
dual is the Boolean function $f^\star \colon \{0,1\}^n \to \{0,1\}$ given by
$f^\star(x) = \lnot f(\bar x)$, where $\bar x$ is the coordinatewise complement of $x$.

Formalized by `MetaMathlibExt.booleanFunctionDual`, a definition declared in [MathlibExt/Order/BooleanFunction/SelfDual.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanFunction/SelfDual.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-function-dual).

## Self-dual monotone Boolean functions

A Boolean function $f \colon \{0,1\}^n \to \{0,1\}$
is self-dual monotone when it is monotone, that is, $f(x) \le f(y)$ for all $x, y \in \{0,1\}^n$
with $x_i \le y_i$ for every $i < n$, and it equals its dual, that is, $f = f^\star$, where
$f^\star(x) = \lnot f(\bar x)$ and $\bar x$ is the coordinatewise complement of $x$.

Formalized by `MetaMathlibExt.IsSelfDualMonotone`, a definition declared in [MathlibExt/Order/BooleanFunction/SelfDual.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanFunction/SelfDual.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#is-self-dual-monotone).

## Complementation of Boolean vectors is an involution

For every $n$ and every Boolean
vector $x \in \{0,1\}^n$, writing $\bar x$ for the coordinatewise complement of $x$, we have
$\bar{\bar x} = x$.

Formalized by `MetaMathlibExt.booleanVectorComplement_complement`, a theorem declared in [MathlibExt/Order/BooleanFunction/SelfDual.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanFunction/SelfDual.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-vector-complement-complement).

## Duality of Boolean functions is an involution

For every $n$ and every Boolean function
$f \colon \{0,1\}^n \to \{0,1\}$, writing $f^\star$ for the dual of $f$, we have
$(f^\star)^\star = f$.

Formalized by `MetaMathlibExt.booleanFunctionDual_dual`, a theorem declared in [MathlibExt/Order/BooleanFunction/SelfDual.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanFunction/SelfDual.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-function-dual-dual).

## Coordinate projections are self-dual monotone

For every $n$ and every index $i < n$, the
projection $x \mapsto x_i$ on $\{0,1\}^n$ is a self-dual monotone Boolean function.

Formalized by `MetaMathlibExt.selfDualMonotone_proj`, a theorem declared in [MathlibExt/Order/BooleanFunction/SelfDual.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Order/BooleanFunction/SelfDual.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#self-dual-monotone-proj).

## Concatenation of a list of Boolean functions

Let $n$ and $k$ be natural numbers and let
$W = (W_0, W_1, \dots, W_{m-1})$ be a finite list of Boolean functions on $n$ variables. The
concatenation $W_0 \cdot W_1 \cdots W_{m-1}$ on $n + k$ variables is the Boolean function that
sends $(x_0, \dots, x_{n-1}, y_0, \dots, y_{k-1})$ to $W_i(x_0, \dots, x_{n-1})$, where
$i = \sum_{j < k} y_j 2^j$ is the number whose binary digits are the last $k$ variables (true
counted as $1$ and false as $0$), and to false when $i \ge m$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, the concatenation representation of `D_n^{B^k}` before Theorem 10.

Formalized by `MetaMathlibExt.booleanCubeConcat`, a definition declared in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-cube-concat).

## Concatenation at the all-false input

For natural numbers $n$ and $k$ and a finite list
$W = (W_0, \dots, W_{m-1})$ of Boolean functions on $n$ variables, the concatenation of $W$ on
$n + k$ variables takes the value $W_0(\mathrm{false}, \dots, \mathrm{false})$ at the all-false
input when $W$ is nonempty, and the value false when $W$ is empty.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, the concatenation representation of `D_n^{B^k}` before Theorem 10.

Formalized by `MetaMathlibExt.booleanCubeConcat_false`, a theorem declared in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-cube-concat-false).

## Currying monotone Boolean functions (Lemma 1)

For a natural number $m$, let $D_m$ be the
poset of monotone Boolean functions $\{0,1\}^m \to \{0,1\}$, where $0 < 1$, inputs are ordered
coordinatewise and functions are ordered pointwise. Then for all natural numbers $n$ and $k$,
$D_{n+k}$ is order-isomorphic to the poset of monotone maps $\{0,1\}^k \to D_n$, ordered
pointwise.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 1 (`jis-2025-25.6.5-lem-1`).

Stated but not proved: `MetaMathlibExt.monotoneBooleanFunction_orderIso_curry` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#monotone-boolean-function-order-iso-curr).

## Duality reverses order and exchanges joins and meets

Let $f$ and $g$ be monotone
Boolean functions on $n$ variables, ordered pointwise, with duals $f^*$ and $g^*$. If $f \le g$
then $g^* \le f^*$. Moreover $(f \lor g)^* = f^* \land g^*$ and $(f \land g)^* = f^* \lor g^*$,
where $\lor$ and $\land$ are pointwise disjunction and conjunction.

Part 1 of the paper's lemma, $f^{**} = f$, holds for every Boolean function.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 2 (`jis-2025-25.6.5-lem-2`).

Stated but not proved: `MetaMathlibExt.booleanFunctionDual_antitone_sup_inf` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-function-dual-antitone-sup-inf).

## Permuting variables preserves monotonicity, duals and self-duality

Let $f$ be a Boolean
function on $n$ variables, let $\pi$ be a permutation of the $n$ coordinates, and let $f^\pi$
be the function $x \mapsto f(x \circ \pi)$. If $f$ is monotone, then $f^\pi$ is monotone and
$(f^*)^\pi = (f^\pi)^*$, where $f^*$ is the dual of $f$. If $f$ is self-dual monotone, then so
is $f^\pi$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 5 (`jis-2025-25.6.5-lem-5`).

Stated but not proved: `MetaMathlibExt.booleanFunction_perm_monotone_dual_selfDual` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#boolean-function-perm-monotone-dual-self).

## Counting self-dual monotone functions on $n + 1$ variables

For every $n \ge 0$, the
number of self-dual monotone Boolean functions on $n + 1$ variables equals the number of
monotone Boolean functions $b$ on $n$ variables with $b \le b^*$, where $b^*$ is the dual of $b$
and functions are ordered pointwise. Moreover, for a permutation $\pi$ of the $n$ coordinates
write $b^\pi$ for the function $x \mapsto b(x \circ \pi)$, and let $R$ be any finite set of
monotone Boolean functions on $n$ variables such that for every monotone $f$ there is exactly
one $b \in R$ with $f = b^\pi$ for some permutation $\pi$. Then the number of self-dual
monotone Boolean functions on $n + 1$ variables equals $\sum_{b \in R,\ b \le b^*} \gamma(b)$,
where $\gamma(b)$ is the number of distinct functions $b^\pi$ as $\pi$ ranges over all
permutations.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Theorem 6 (`jis-2025-25.6.5-thm-6`).

Stated but not proved: `MetaMathlibExt.card_selfDualMonotone_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#card-self-dual-monotone-succ).

## Upper bound for self-dual monotone functions on $n + 1$ variables

For every $n \ge 0$,
the number of self-dual monotone Boolean functions on $n + 1$ variables is at most the number
of monotone Boolean functions on $n$ variables.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Corollary 7 (`jis-2025-25.6.5-cor-7`).

Stated but not proved: `MetaMathlibExt.card_selfDualMonotone_succ_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#card-self-dual-monotone-succ-le).

## Weights of monotone Boolean functions and their duals (Lemma 8)

Order $\{0,1\}$ by
$0 < 1$, inputs in $\{0,1\}^n$ coordinatewise and Boolean functions on $\{0,1\}^n$ pointwise. For
such a function $f$, let $f^*(x) = \lnot f(\bar x)$ be its dual, where $\bar x$ is the
coordinatewise complement of $x$, and let $\ell(f)$ be the number of $x \in \{0,1\}^n$ with
$f(x) = 1$. Let $b$ be a monotone Boolean function on $\{0,1\}^n$. Then: if $b \le b^*$, then
$2\ell(b) \le 2^n$; if $2\ell(b) = 2^n$ and $b \le b^*$, then $b = b^*$; if $b = b^*$, then
$2\ell(b) = 2^n$; and $\ell(b^*) = 2^n - \ell(b)$. Moreover, the number of monotone Boolean
functions $f$ on $\{0,1\}^n$ with $2\ell(f) < 2^n$ equals the number of those with
$2\ell(f) > 2^n$.

For $n \ge 1$ the comparisons of $2\ell$ with $2^n$ are the paper's comparisons of $\ell$ with
$2^{n-1}$; written this way the statement also covers $n = 0$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 8 (`jis-2025-25.6.5-lem-8`).

Stated but not proved: `MetaMathlibExt.monotoneBooleanFunction_weight_dual` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#monotone-boolean-function-weight-dual).

## Recursion for self-dual monotone functions from $n$ to $n + 1$ variables

Let $n \ge 1$,
let $\lambda_m$ be the number of self-dual monotone Boolean functions on $m$ variables, and let
$d_n$ be the number of monotone Boolean functions on $n$ variables. For a Boolean function $b$
on $n$ variables let $b^*$ be its dual and $\ell(b)$ the number of inputs at which $b$ is true,
order functions pointwise, and for a permutation $\pi$ of the $n$ coordinates write $b^\pi$ for
the function $x \mapsto b(x \circ \pi)$. Let $R$ be any finite set of monotone Boolean
functions on $n$ variables such that for every monotone $f$ there is exactly one $b \in R$ with
$f = b^\pi$ for some permutation $\pi$, and let $\gamma(b)$ be the number of distinct functions
$b^\pi$ as $\pi$ ranges over all permutations. Then

$$
\lambda_{n+1} = \lambda_n + \sum_{b \in R,\ \ell(b) < 2^{n-1},\ b \le b^*} \gamma(b),
$$

and $2 \lambda_{n+1} \le d_n + \lambda_n$.

The bound is the paper's $\lambda_{n+1} \le (d_n + \lambda_n) / 2$ with the division cleared.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Theorem 9 (`jis-2025-25.6.5-thm-9`).

Stated but not proved: `MetaMathlibExt.card_selfDualMonotone_succ_eq_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#card-self-dual-monotone-succ-eq-add).

## Counting self-dual monotone functions on $n + 2$ variables

Let $n \ge 0$ and let
$\lambda_{n+2}$ be the number of self-dual monotone Boolean functions on $n + 2$ variables. For
a monotone Boolean function $b$ on $n$ variables let $r(b)$ be the number of monotone Boolean
functions $z$ on $n$ variables with $b \lor b^* \le z$, where $b^*$ is the dual of $b$, $\lor$
is pointwise disjunction and functions are ordered pointwise. Then $\lambda_{n+2}$ is the sum
of $r(b)$ over all monotone Boolean functions $b$ on $n$ variables. Moreover, for a permutation
$\pi$ of the $n$ coordinates write $b^\pi$ for the function $x \mapsto b(x \circ \pi)$, and let
$R$ be any finite set of monotone Boolean functions on $n$ variables such that for every
monotone $f$ there is exactly one $b \in R$ with $f = b^\pi$ for some permutation $\pi$. Then
$\lambda_{n+2} = \sum_{b \in R} \gamma(b) \, r(b)$, where $\gamma(b)$ is the number of distinct
functions $b^\pi$ as $\pi$ ranges over all permutations.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Theorem 10 (`jis-2025-25.6.5-thm-10`).

Stated but not proved: `MetaMathlibExt.card_selfDualMonotone_add_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#card-self-dual-monotone-add-two).

## Dedekind numbers bound self-dual counts from below (Corollary 11)

For a natural number
$n$, let $d_n$ be the number of monotone Boolean functions $\{0,1\}^n \to \{0,1\}$ (for the
coordinatewise order with $0 < 1$) and let $\lambda_{n+2}$ be the number of self-dual monotone
Boolean functions $\{0,1\}^{n+2} \to \{0,1\}$, that is, monotone functions $f$ with
$f(\bar x) = \lnot f(x)$ for every $x$, where $\bar x$ is the coordinatewise complement of $x$.
Then $d_n \le \lambda_{n+2}$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Corollary 11 (`jis-2025-25.6.5-cor-11`).

Stated but not proved: `MetaMathlibExt.le_card_selfDualMonotone_add_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#le-card-self-dual-monotone-add-two).

## Self-dual monotone functions on $n+4$ variables as concatenations (Theorem 12)

Order
$\{0,1\}$ by $0 < 1$, inputs coordinatewise and Boolean functions pointwise, with $\vee$ the
pointwise maximum. Let $D_n$ be the set of monotone Boolean functions on $\{0,1\}^n$, and let
$f^*(x) = \lnot f(\bar x)$ be the dual of $f$, where $\bar x$ is the coordinatewise complement of
$x$; a Boolean function $F$ is self-dual monotone if it is monotone and $F^* = F$. The
concatenation $W_0 \cdot W_1 \cdots W_{15}$ of Boolean functions on $\{0,1\}^n$ is the Boolean
function on $\{0,1\}^{n+4}$ sending $(x, y_0, y_1, y_2, y_3)$, with $x \in \{0,1\}^n$, to
$W_i(x)$, where $i = y_0 + 2y_1 + 4y_2 + 8y_3$. Let $a, b, c, d, e, f, g, h \in D_n$ satisfy
$a \vee b \vee c \vee a^* \vee b^* \vee c^* \le h$, $a \vee b \vee c \le d \le h$,
$a \vee b^* \vee c^* \le e \le h$, $b \vee a^* \vee c^* \le f \le h$ and
$c \vee a^* \vee b^* \le g \le h$. Then the concatenation

$$h^* \cdot g^* \cdot f^* \cdot a \cdot e^* \cdot b \cdot c \cdot d \cdot
d^* \cdot c^* \cdot b^* \cdot e \cdot a^* \cdot f \cdot g \cdot h$$

is a self-dual monotone Boolean function on $\{0,1\}^{n+4}$. Conversely, every self-dual
monotone Boolean function on $\{0,1\}^{n+4}$ equals this concatenation for some
$a, b, c, d, e, f, g, h \in D_n$ satisfying these inequalities.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Theorem 12 (`jis-2025-25.6.5-thm-12`).

Stated but not proved: `MetaMathlibExt.selfDualMonotone_add_four_iff_concat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#self-dual-monotone-add-four-iff-concat).

## Counting self-dual monotone functions on $n + 4$ variables

Let $D_n$ be the set of
monotone Boolean functions on $n$ variables, ordered pointwise, with $\lor$ the pointwise
disjunction and $f^*$ the dual of $f$. For $x, h \in D_n$ let $\mathrm{re}(x, h)$ be the number
of $z \in D_n$ with $x \le z \le h$. Then the number of self-dual monotone Boolean functions on
$n + 4$ variables equals

$$
\sum_{a, b, c \in D_n} \ \sum_{h \in D_n,\ h \ge a \lor b \lor c \lor a^* \lor b^* \lor c^*}
\mathrm{re}(a \lor b \lor c, h) \, \mathrm{re}(a \lor b^* \lor c^*, h) \,
\mathrm{re}(b \lor a^* \lor c^*, h) \, \mathrm{re}(c \lor a^* \lor b^*, h).
$$

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Theorem 13 (`jis-2025-25.6.5-thm-13`).

Stated but not proved: `MetaMathlibExt.card_selfDualMonotone_add_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#card-self-dual-monotone-add-four).

## Self-dual monotone functions on $n+4$ variables, interval form (Theorem 14)

Order
$\{0,1\}$ by $0 < 1$, inputs coordinatewise and Boolean functions pointwise, with $\vee$ the
pointwise maximum. Let $D_n$ be the set of monotone Boolean functions on $\{0,1\}^n$, and let
$f^*(x) = \lnot f(\bar x)$ be the dual of $f$, where $\bar x$ is the coordinatewise complement of
$x$; a Boolean function $F$ is self-dual monotone if it is monotone and $F^* = F$. The
concatenation $W_0 \cdot W_1 \cdots W_{15}$ of Boolean functions on $\{0,1\}^n$ is the Boolean
function on $\{0,1\}^{n+4}$ sending $(x, y_0, y_1, y_2, y_3)$, with $x \in \{0,1\}^n$, to
$W_i(x)$, where $i = y_0 + 2y_1 + 4y_2 + 8y_3$. Let $a, b, c, d, e, f, g, h \in D_n$ satisfy
$h^* \le h$, $h^* \le a \le h$, $h^* \le b \le h$, $h^* \le c \le h$,
$a \vee b \vee c \le d \le h$, $a \vee b^* \vee c^* \le e \le h$,
$b \vee a^* \vee c^* \le f \le h$ and $c \vee a^* \vee b^* \le g \le h$. Then the concatenation

$$h^* \cdot g^* \cdot f^* \cdot a \cdot e^* \cdot b \cdot c \cdot d \cdot
d^* \cdot c^* \cdot b^* \cdot e \cdot a^* \cdot f \cdot g \cdot h$$

is a self-dual monotone Boolean function on $\{0,1\}^{n+4}$. Conversely, every self-dual
monotone Boolean function on $\{0,1\}^{n+4}$ equals this concatenation for some
$a, b, c, d, e, f, g, h \in D_n$ satisfying these inequalities.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Theorem 14 (`jis-2025-25.6.5-thm-14`).

Stated but not proved: `MetaMathlibExt.selfDualMonotone_add_four_iff_concat_of_dual_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#self-dual-monotone-add-four-iff-concat-o).

## Maximal intersecting families split complementary pairs (Lemma 3, L2)

Let $n \ge 1$ and
let $\mathcal U$ be a maximal intersecting family of subsets of $X = \{0, \dots, n-1\}$: any two
members of $\mathcal U$, not necessarily distinct, have nonempty intersection, and no family of
subsets of $X$ strictly containing $\mathcal U$ has this property. Then for every
$A \subseteq X$, $A \in \mathcal U$ if and only if $X \setminus A \notin \mathcal U$.

The hypothesis $n \ge 1$ is needed: for $n = 0$ the empty family is the maximal intersecting
family, and it contains neither $\emptyset$ nor its complement $\emptyset$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 3 (`jis-2025-25.6.5-lem-3`).

Stated but not proved: `MetaMathlibExt.maximal_intersecting_mem_iff_compl_notMem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#maximal-intersecting-mem-iff-compl-not-m).

## A criterion for maximal intersecting families (Lemma 4)

Let $n$ be a natural number and
let $\mathcal U$ be a family of subsets of $X = \{0, \dots, n-1\}$ such that $\mathcal U$ is an
upper set (if $A \in \mathcal U$ and $A \subseteq B \subseteq X$ then $B \in \mathcal U$) and,
for every $A \subseteq X$, $A \in \mathcal U$ if and only if $X \setminus A \notin \mathcal U$.
Then $\mathcal U$ is a maximal intersecting family: any two members of $\mathcal U$, not
necessarily distinct, have nonempty intersection, and no family of subsets of $X$ strictly
containing $\mathcal U$ has this property.

The paper's hypothesis $n \ge 1$ is not needed: for $n = 0$ the complement of $\emptyset$ is
$\emptyset$, so no family satisfies the second condition.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 4 (`jis-2025-25.6.5-lem-4`).

Stated but not proved: `MetaMathlibExt.maximal_intersecting_of_isUpperSet_of_mem_iff_compl_notMem` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#maximal-intersecting-of-is-upper-set-of).

## Permutations with only even cycles fix no self-dual monotone function (Lemma 15)

Let
$\pi$ be a permutation of $\{0, \dots, n-1\}$ all of whose cycles have even length, that is,
every point has an orbit of even size under $\pi$. Let $f : \{0,1\}^n \to \{0,1\}$ be self-dual
monotone, that is, monotone for the coordinatewise order with $0 < 1$ and such that
$f(\bar x) = \lnot f(x)$ for every $x$, where $\bar x$ is the coordinatewise complement of $x$.
Then $f$ is not fixed by $\pi$: the function $x \mapsto f(x \circ \pi)$, where
$(x \circ \pi)_i = x_{\pi(i)}$, differs from $f$.

The paper also assumes that $n$ is even; this follows from the condition on the cycles.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 15 (`jis-2025-25.6.5-lem-15`).

Stated but not proved: `MetaMathlibExt.selfDualMonotone_not_fixed_of_even_minimalPeriod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#self-dual-monotone-not-fixed-of-even-min).

## Permutations of eight variables fixing no self-dual monotone function (Corollary 16)

Let $\pi$ be one of the permutations $(0\,1\,2\,3\,4\,5\,6\,7)$, $(0\,1)(2\,3\,4\,5\,6\,7)$,
$(0\,1\,2\,3)(4\,5\,6\,7)$, $(0\,1)(2\,3)(4\,5\,6\,7)$ and $(0\,1)(2\,3)(4\,5)(6\,7)$ of
$\{0, \dots, 7\}$, in cycle notation. Let $f : \{0,1\}^8 \to \{0,1\}$ be self-dual monotone,
that is, monotone for the coordinatewise order with $0 < 1$ and such that
$f(\bar x) = \lnot f(x)$ for every $x$, where $\bar x$ is the coordinatewise complement of $x$.
Then $f$ is not fixed by $\pi$: the function $x \mapsto f(x \circ \pi)$, where
$(x \circ \pi)_i = x_{\pi(i)}$, differs from $f$.

In the paper the points are numbered $1, \dots, 8$, so these permutations are $(12345678)$,
$(12)(345678)$, $(1234)(5678)$, $(12)(34)(5678)$ and $(12)(34)(56)(78)$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Corollary 16 (`jis-2025-25.6.5-cor-16`).

Stated but not proved: `MetaMathlibExt.selfDualMonotone_eight_not_fixed` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#self-dual-monotone-eight-not-fixed).

## For odd $n$, every permutation fixes a self-dual monotone function

Let $n$ be odd and
let $\pi$ be a permutation of the $n$ coordinates. Then there is a self-dual monotone Boolean
function $f$ on $n$ variables with $f(x \circ \pi) = f(x)$ for every input $x$.

## Sources

- Bartłomiej Pawelski and Andrzej Szepietowski, *Counting Self-Dual Monotone Boolean Functions*, Journal of Integer Sequences 28 (2025), Article 25.6.5, Lemma 17 (`jis-2025-25.6.5-lem-17`).

Stated but not proved: `MetaMathlibExt.exists_selfDualMonotone_fixed_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/SelfDualMonotoneBooleanWanted.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html#exists-self-dual-monotone-fixed-of-odd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Self-dual monotone Boolean functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/self-dual-monotone-boolean-functions)
