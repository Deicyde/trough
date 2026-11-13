---
declaration: section
origin: cited
lean: MetaMathlibExt.genLeonardo, MetaMathlibExt.genLeonardo_two, MetaMathlibExt.genLeonardo_eq_leonardoPK_one, MetaMathlibExt.genLeonardoCompanion, MetaMathlibExt.genLeonardoCompanion_one, MetaMathlibExt.genLeonardo_mul_companion, MetaMathlibExt.genLeonardo_cross, MetaMathlibExt.genLeonardo_sq_sub_sq
statement: formalized
---

# Leonardo numbers

22 results, 4 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html).

## Generalized Leonardo numbers

For an integer $k$, the generalized Leonardo numbers
$L_{k,0}, L_{k,1}, L_{k,2}, \ldots$ are the integers defined by $L_{k,0} = L_{k,1} = 1$ and
$L_{k,n+2} = L_{k,n+1} + L_{k,n} + k$ for all $n \ge 0$.

The paper takes $k$ positive; here $k$ may be any integer.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly 62.3 (2024), introduction.

Formalized by `MetaMathlibExt.genLeonardo`, a definition declared in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo).

## Generalized Leonardo number of index two

For every integer $k$, the generalized
Leonardo number $L_{k,2}$ equals $2 + k$.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024).

Formalized by `MetaMathlibExt.genLeonardo_two`, a theorem declared in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-two).

## Generalized Leonardo numbers as Leonardo $p$-numbers with $p = 1$

For all natural numbers
$k$ and $n$, the generalized Leonardo number $L_{k,n}$ equals the generalized Leonardo $p$-number
$\mathcal{L}_{1,k}(n)$; both sequences start with $1, 1$ and satisfy the recurrence
$a_{n+2} = a_{n+1} + a_n + k$.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly 62.3 (2024), introduction; Kusrini, Putra, and Kuhapatanakul, *On Generalized Leonardo p-Numbers*, Journal of Integer Sequences 27 (2024), Article 24.4.6.

Stated but not proved: `MetaMathlibExt.genLeonardo_eq_leonardoPK_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-eq-leonardo-pk-one).

## Dual generalized Leonardo numbers

For an integer $k$, let $L_{k,n}$ denote the generalized
Leonardo numbers. The dual generalized Leonardo numbers $M_{k,n}$, for natural numbers $n$, are
defined by $M_{k,0} = 1 - k$ and $M_{k,n+1} = L_{k,n} + L_{k,n+2}$, so that
$M_{k,n} = L_{k,n-1} + L_{k,n+1}$ for $n \ge 1$.

This agrees with the paper's Definition 2.1, which sets $M_{k,0} = 1 - k$, $M_{k,1} = k + 3$, and
$M_{k,n+1} = M_{k,n} + M_{k,n-1} + 2k$ for $n \ge 1$.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly 62.3 (2024), Definition 2.1 and identity (2.1).

Formalized by `MetaMathlibExt.genLeonardoCompanion`, a definition declared in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-companion).

## The dual generalized Leonardo number of index one

For every integer $k$, the dual
generalized Leonardo number $M_{k,1}$ equals $3 + k$.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024).

Formalized by `MetaMathlibExt.genLeonardoCompanion_one`, a theorem declared in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-companion-one).

## Product of a generalized Leonardo number and its dual

Let $k$ be an integer, and let
$L_{k,n}$ and $M_{k,n}$ denote the generalized Leonardo numbers and the dual generalized Leonardo
numbers. For every natural number $n$,

$$L_{k,n} M_{k,n} = (k+1) L_{k,2n+1} - k L_{k,n+3} + k\,(2k+1).$$

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 2.2.

Stated but not proved: `MetaMathlibExt.genLeonardo_mul_companion` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-mul-companion).

## Cross-product identity for generalized Leonardo numbers

Let $k$ be an integer, and let
$L_{k,n}$ and $M_{k,n}$ denote the generalized Leonardo numbers and the dual generalized Leonardo
numbers. For every natural number $n \ge 1$,

$$L_{k,n} M_{k,n+1} - L_{k,n+1} M_{k,n-1} = (k+1) L_{k,2n} - k L_{k,n} + k.$$

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 2.3.

Stated but not proved: `MetaMathlibExt.genLeonardo_cross` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-cross).

## Square-difference identity for generalized Leonardo numbers

For every integer $k$ and
every natural number $n \ge 1$, the generalized Leonardo numbers $L_{k,n}$ and the dual
generalized Leonardo numbers $M_{k,n}$ satisfy

$$M_{k,n}^2 - L_{k,n}^2 = 4 L_{k,n-1} L_{k,n+1} + 2k L_{k,n} + k^2.$$

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 2.4.

Stated but not proved: `MetaMathlibExt.genLeonardo_sq_sub_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-sq-sub-sq).

## Shift identity for generalized Leonardo numbers

Let $k$ be an integer and let $L_{k,n}$
denote the generalized Leonardo numbers. For all natural numbers $m$, $n$, $t$ with
$1 \le t \le n$ and $n + 1 \le m + t$,

$$L_{k,m} L_{k,n} - L_{k,m+t} L_{k,n-t}
= (-1)^{n-t+1} (L_{k,m+t-n-1} + k)(L_{k,t-1} + k) -
k\,(L_{k,m} + L_{k,n} - L_{k,m+t} - L_{k,n-t}).$$

The paper also allows $t = 0$, reading $L_{k,-1}$ by extending the sequence to negative indices.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 2.5.

Stated but not proved: `MetaMathlibExt.genLeonardo_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-shift).

## Sum-and-difference square identities for generalized Leonardo numbers

For every
integer $k$ and all natural numbers $m$, $n$ with $1 \le n < m$, the generalized Leonardo
numbers $L_{k,n}$ satisfy

$$L_{k,m+n}^2 - L_{k,m-n}^2 =
(L_{k,2m+1} + k)(L_{k,2n-1} + k) - 2k (L_{k,m+n} - L_{k,m-n})$$

and

$$L_{k,m+n}^2 + L_{k,m-n-1}^2 =
(L_{k,2m} + k)(L_{k,2n} + k) - 2k (L_{k,m+n} + L_{k,m-n-1}) - 2k^2.$$

In the second identity the last term inside the parentheses is $L_{k,m-n-1}$. The paper as
printed shows $L_{k,m-n}$ there, which is false: at $k = 1$, $m = 3$, $n = 1$ the printed
identity reads $82 = 78$. The reading used here agrees with the paper's outline derivation.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 2.6.

Stated but not proved: `MetaMathlibExt.genLeonardo_sq_sum_diff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-sq-sum-diff).

## Binomial convolution identities for generalized Leonardo numbers

Let $k$ be an integer,
and let $L_{k,n}$ and $M_{k,n}$ denote the generalized Leonardo numbers and the dual generalized
Leonardo numbers. For all natural numbers $n$ and $r$,

$$\sum_{i=0}^{n} \binom{n}{i} L_{k,i+r} = L_{k,2n+r} - k\,(2^n - 1)$$

and

$$\sum_{i=0}^{n} \binom{n}{i} M_{k,i+r} = M_{k,2n+r} - 2k\,(2^n - 1).$$

Parts (iii) and (iv) of the paper's Theorem 3.1, alternating sums involving the index
$L_{k,n-r-2}$, are false as printed: at $k = 1$, $n = 3$, $r = 1$, with the sequence extended to
negative indices by the recurrence, the left side is $2$ and the printed right side is $-2$.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 3.1 (i),(ii).

Stated but not proved: `MetaMathlibExt.genLeonardo_binomial_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-binomial-sum).

## Even-order binomial identities for generalized Leonardo numbers

Let $k$ be an integer,
and let $L_{k,n}$ and $M_{k,n}$ denote the generalized Leonardo numbers and the dual generalized
Leonardo numbers. For all natural numbers $m$ and $r$,

$$\sum_{i=0}^{2m} \binom{2m}{i} L_{k,2i+r} = 5^m L_{k,2m+r} + k\,(5^m - 2^{2m})$$

and

$$\sum_{i=0}^{2m} \binom{2m}{i} M_{k,2i+r} = 5^m M_{k,2m+r} + 2k\,(5^m - 2^{2m}).$$

The paper's Theorem 3.2 also states identities of odd order $n$; as printed they are false (at
$k = n = 1$, $r = 0$ the first odd identity reads $4 = 6$).

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 3.2, even case.

Stated but not proved: `MetaMathlibExt.genLeonardo_binomial_sum_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-binomial-sum-two-mul).

## Alternating binomial identities for generalized Leonardo numbers

Let $k$ be an integer,
and let $L_{k,n}$ and $M_{k,n}$ denote the generalized Leonardo numbers and the dual generalized
Leonardo numbers. For all natural numbers $n \ge 1$ and $r$,

$$\sum_{i=0}^{n} \binom{n}{i} (-1)^{n-i} L_{k,2i+r} = L_{k,n+r} + k$$

and

$$\sum_{i=0}^{n} \binom{n}{i} (-1)^{n-i} M_{k,2i+r} = M_{k,n+r} + 2k.$$

The hypothesis $n \ge 1$ is needed: for $n = 0$ the two sums equal $L_{k,r}$ and $M_{k,r}$.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 3.3.

Stated but not proved: `MetaMathlibExt.genLeonardo_binomial_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-binomial-alternating).

## Binomial identities with steps three and four for generalized Leonardo numbers

Let $k$ be
an integer, and let $L_{k,n}$ and $M_{k,n}$ denote the generalized Leonardo numbers and the dual
generalized Leonardo numbers. For all natural numbers $n$ and $r$,

$$\sum_{i=0}^{n} \binom{n}{i} L_{k,3i+r} = 2^n L_{k,2n+r},$$



$$\sum_{i=0}^{n} \binom{n}{i} M_{k,3i+r} = 2^n M_{k,2n+r},$$



$$\sum_{i=0}^{n} \binom{n}{i} L_{k,4i+r} = 3^n L_{k,2n+r} + k\,(3^n - 2^n),$$

and

$$\sum_{i=0}^{n} \binom{n}{i} M_{k,4i+r} = 3^n M_{k,2n+r} + 2k\,(3^n - 2^n).$$

Part (iv) of the paper's Theorem 3.4 prints the last term of the fourth identity as
$k\,(3^n - 2^n)$, which is false at $k = n = 1$, $r = 0$; the coefficient $2k$ is the correct one,
as in parts (ii) of Theorems 3.1–3.3.

## Sources

- Kuhapatanakul, *Note on the Generalized Leonardo Numbers*, Fibonacci Quarterly (2024), Theorem 3.4.

Stated but not proved: `MetaMathlibExt.genLeonardo_binomial_steps` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenLeonardoWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenLeonardoWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-binomial-steps).

## Log-concavity propagates along a linear recurrence

Let $k \ge 2$ be an integer, let
$c_1, \dots, c_k$ be real numbers with $c_j \ge 0$ for $2 \le j \le k$, and let
$(z_n)_{n \ge 0}$ be a sequence of positive real numbers with

$$z_n = c_1 z_{n-1} - \sum_{j=2}^{k} c_j z_{n-j} \quad (n \ge k).$$

If $z_{i-1} z_{i+1} \le z_i^2$ for $1 \le i < k$, then $z_{n-1} z_{n+1} \le z_n^2$ for every
$n \ge 1$; that is, the whole sequence is log-concave.

The paper assumes that the block $z_0, \dots, z_{k+1}$ is log-concave, which adds the
inequality for $i = k$, and that $c_1 > 0$. Both follow from the other hypotheses: the
recurrence at $n = k + 1$ propagates the inequality for $i = k$ from those for $i < k$, and
the recurrence at $n = k$ forces $c_1 > 0$.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Lemma 1 (quoted from the paper's reference [17]).

Stated but not proved: `MetaMathlibExt.logConcave_of_linearRecurrence_of_initial_logConcave` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#log-concave-of-linear-recurrence-of-init).

## Log-convexity propagates along a linear recurrence

Let $k \ge 2$ be an integer, let
$c_1, \dots, c_k$ be real numbers with $c_j \ge 0$ for $2 \le j \le k$, and let
$(z_n)_{n \ge 0}$ be a sequence of positive real numbers with

$$z_n = c_1 z_{n-1} - \sum_{j=2}^{k} c_j z_{n-j} \quad (n \ge k).$$

If $z_i^2 \le z_{i-1} z_{i+1}$ for $1 \le i < k$, then $z_n^2 \le z_{n-1} z_{n+1}$ for every
$n \ge 1$; that is, the whole sequence is log-convex.

The paper assumes that the block $z_0, \dots, z_{k+1}$ is log-convex, which adds the
inequality for $i = k$, and that $c_1 > 0$. Both follow from the other hypotheses: the
recurrence propagates the inequality for $i = k$, and the recurrence at $n = k$ forces
$c_1 > 0$.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Lemma 1, log-convex reading (quoted from the paper's reference [17]).

Stated but not proved: `MetaMathlibExt.logConvex_of_linearRecurrence_of_initial_logConvex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#log-convex-of-linear-recurrence-of-initi).

## Log-balancedness of reciprocals along a three-term recurrence

Let $c_1$ and $c_2$ be
real numbers with $c_2 \ge 0$, and let $(z_n)_{n \ge 0}$ be a sequence of positive real numbers
with $z_{n+1} = c_1 z_n - c_2 z_{n-2}$ for every $n \ge 2$. Write $w_n = 1/z_n$ and
$x_n = z_{n+1}/z_n$, and let $n_0 \ge 0$ be an integer. Suppose that for $n = n_0 + 1$ and
$n = n_0 + 2$

$$w_n^2 \le w_{n-1} w_{n+1} \quad \text{and} \quad
\frac{w_{n-1}}{(n-1)!} \cdot \frac{w_{n+1}}{(n+1)!} \le \left(\frac{w_n}{n!}\right)^2,$$

and that $c_1 x_n x_{n+1} \ge 3 c_2$ for every $n \ge n_0$. Then both inequalities hold for
every $n \ge n_0 + 1$; that is, the sequence $(1/z_n)_{n \ge n_0}$ is log-balanced (Došlić).

The paper also assumes $c_1 > 0$; this follows from positivity, the recurrence and $c_2 \ge 0$.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Lemma 2.

Stated but not proved: `MetaMathlibExt.inv_logBalanced_of_recurrence_of_initial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#inv-log-balanced-of-recurrence-of-initia).

## Log-balancedness of the reciprocals of generalized Leonardo numbers

Let $k \ge 1$ be an
integer and let $L_{k,n}$ be the generalized Leonardo numbers. Then the sequence
$(1/L_{k,n})_{n \ge 3}$ is log-balanced (Došlić): for every integer $n \ge 4$,

$$\left(\frac{1}{L_{k,n}}\right)^2 \le \frac{1}{L_{k,n-1}} \cdot \frac{1}{L_{k,n+1}}$$

and

$$\frac{1}{L_{k,n-1} \, (n-1)!} \cdot \frac{1}{L_{k,n+1} \, (n+1)!} \le
\left(\frac{1}{L_{k,n} \, n!}\right)^2.$$

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Theorem 1.

Stated but not proved: `MetaMathlibExt.inv_genLeonardo_logBalanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#inv-gen-leonardo-log-balanced).

## Log-convexity of the n-th roots of generalized Leonardo numbers

Let $k \ge 1$ be an
integer and let $L_{k,n}$ be the generalized Leonardo numbers. Then the sequence
$(L_{k,n}^{1/n})_{n \ge 9}$ is log-convex:
$(L_{k,n}^{1/n})^2 \le L_{k,n-1}^{1/(n-1)} L_{k,n+1}^{1/(n+1)}$ for every integer $n \ge 10$.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Theorem 3.

Stated but not proved: `MetaMathlibExt.genLeonardo_rpow_inv_logConvex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-rpow-inv-log-convex).

## Log-concavity of partial sums of generalized Leonardo numbers

Let $k \ge 1$ be an
integer, let $L_{k,n}$ be the generalized Leonardo numbers, and let
$R_n = \sum_{i=0}^{n} L_{k,i}$. Then $R_{n-1} R_{n+1} \le R_n^2$ for every integer $n \ge 2$.

The inequality fails at $n = 1$: there $R_0 = 1$, $R_1 = 2$ and $R_2 = k + 4$, so
$R_1^2 - R_0 R_2 = -k < 0$. The paper states it for every $n \ge 1$, although its identity
$R_n^2 - R_{n-1} R_{n+1} = (k+1)^2 (F_n + (-1)^n) + k(k+1)(n F_n - 2 F_{n+1}) + k^2$, with
$F_n$ the Fibonacci numbers, gives the same value $-k$ at $n = 1$.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Theorem 2.

Stated but not proved: `MetaMathlibExt.genLeonardo_partialSum_logConcave` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-partial-sum-log-concave).

## Log-balancedness of the n-th roots of generalized Leonardo numbers

Let $k \ge 1$ be an
integer, let $L_{k,n}$ be the generalized Leonardo numbers, and let $n_k$ be an integer with
$n_k \ge 9$ and $n_k \ge (1 + \sqrt{64k - 7})/4$. Then for every integer $n \ge n_k + 1$,

$$\left(L_{k,n}^{1/n}\right)^2 \le L_{k,n-1}^{1/(n-1)} L_{k,n+1}^{1/(n+1)}$$

and

$$\frac{L_{k,n-1}^{1/(n-1)}}{(n-1)!} \cdot \frac{L_{k,n+1}^{1/(n+1)}}{(n+1)!} \le
\left(\frac{L_{k,n}^{1/n}}{n!}\right)^2;$$

that is, the sequence $(L_{k,n}^{1/n})_{n \ge n_k}$ is log-balanced (Došlić): it is log-convex
and its quotient by $n!$ is log-concave.

The paper asserts only that some $n_k \ge \max\{9, (1 + \sqrt{64k - 7})/4\}$ with this property
exists; the statement above gives the threshold its proof establishes (log-concavity of
$L_{k,n}^{1/n}/n!$ once $n \ge (1 + \sqrt{64k - 7})/4$, log-convexity of $L_{k,n}^{1/n}$ from
$n = 9$ on).

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Theorem 4.

Stated but not proved: `MetaMathlibExt.genLeonardo_rpow_inv_logBalanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-rpow-inv-log-balanced).

## Log-convexity of the self-powers of generalized Leonardo numbers

Let $k \ge 1$ be an
integer and let $L_{k,n}$ be the generalized Leonardo numbers. Then the sequence
$(L_{k,n}^n)_{n \ge 3}$ is log-convex: $L_{k,n}^{2n} \le L_{k,n-1}^{n-1} L_{k,n+1}^{n+1}$ for
every integer $n \ge 4$.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to the Generalized Leonardo Numbers*, INTEGERS 24 (2024), Article A82, Theorem 5.

Stated but not proved: `MetaMathlibExt.genLeonardo_pow_self_logConvex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GeneralizedLeonardoLogBehaviorWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html#gen-leonardo-pow-self-log-convex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Leonardo numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/leonardo-numbers)
