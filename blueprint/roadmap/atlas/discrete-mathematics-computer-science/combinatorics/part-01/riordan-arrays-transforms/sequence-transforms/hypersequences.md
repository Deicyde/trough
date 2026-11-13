---
declaration: section
origin: cited
lean: MetaMathlibExt.hypersequence, MetaMathlibExt.hypersequence_succ, MetaMathlibExt.hypersequence_one_zero, MetaMathlibExt.hyperFibonacci_eq_hypersequence, MetaMathlibExt.alternatingBinomialPowerSum, MetaMathlibExt.alternatingBinomialPowerSum_one_one_one_one, MetaMathlibExt.hypersequence_eq_sum_choose, MetaMathlibExt.hypersequence_succ_succ
statement: formalized
---

# Hypersequences

44 results, 11 proved and 33 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html).

## Hypersequence

Let $(a_n)_{n \ge 0}$ be a sequence in an additive commutative monoid.
Its hypersequence of generation $r$, written $a^{(r)}_n$, is defined by recursion on $r$:
$a^{(0)}_n = a_n$ and $a^{(r+1)}_n = \sum_{k=0}^{n} a^{(r)}_k$ for all natural numbers $r$ and
$n$. Thus each generation is the sequence of partial sums of the previous one.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Section 1, Equation (1.1).

Formalized by `MetaMathlibExt.hypersequence`, a definition declared in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hypersequence).

## Each hypersequence generation sums the previous one

Let $(a_n)$ be a sequence in an
additive commutative monoid and let $a^{(r)}_n$ denote its hypersequence of generation $r$. For
all natural numbers $r$ and $n$, $a^{(r+1)}_n = \sum_{k=0}^{n} a^{(r)}_k$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Section 1, Equation (1.1).

Formalized by `MetaMathlibExt.hypersequence_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hypersequence-succ).

## First hypersequence at index zero

Let $(a_n)$ be a sequence in an additive commutative
monoid and let $a^{(1)}_n$ denote its hypersequence of generation $1$. Then $a^{(1)}_0 = a_0$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Section 1, Equation (1.1).

Formalized by `MetaMathlibExt.hypersequence_one_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hypersequence-one-zero).

## Hyperfibonacci numbers are the hypersequences of the Fibonacci numbers

Let $F_k$ denote
the $k$th Fibonacci number. For all natural numbers $r$ and $n$, the hyperfibonacci number
$F^{(r)}_n$ equals the $r$th hypersequence of the Fibonacci sequence at $n$, that is,
$F^{(r)}_n = a^{(r)}_n$ for $a_k = F_k$, where $a^{(0)}_n = a_n$ and
$a^{(r+1)}_n = \sum_{k=0}^{n} a^{(r)}_k$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Example 3 (hyperfibonacci numbers).

Formalized by `MetaMathlibExt.hyperFibonacci_eq_hypersequence`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyper-fibonacci-eq-hypersequence).

## Alternating binomial power sum

For natural numbers $\ell, m$ and complex numbers $x, y$,

$$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell,$$

with the convention $0^0 = 1$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Section 3, Equation (3.9).

Formalized by `MetaMathlibExt.alternatingBinomialPowerSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#alternating-binomial-power-sum).

## A value of the alternating binomial power sum

The alternating binomial power sum
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell$ satisfies
$p_{1,1}(1, 1) = 1 - 2 = -1$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Section 3, Equation (3.9).

Formalized by `MetaMathlibExt.alternatingBinomialPowerSum_one_one_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#alternating-binomial-power-sum-one-one-o).

## Hypersequences as binomial sums

Let $(a_n)$ be a sequence of complex numbers and let
$a^{(r)}_n$ denote its hypersequence of generation $r$. For every $r \ge 1$ and every natural
number $n$,

$$a^{(r)}_n = \sum_{k=0}^{n} \binom{n+r-1-k}{r-1} a_k = \sum_{k=0}^{n} \binom{r+k-1}{k} a_{n-k}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 1, Equation (2.1).

Stated but not proved: `MetaMathlibExt.hypersequence_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hypersequence-eq-sum-choose).

## Recurrence between consecutive hypersequence generations

Let $(a_n)$ be a sequence of
complex numbers and let $a^{(r)}_n$ denote its hypersequence of generation $r$. For all natural
numbers $r$ and $n$, $a^{(r+1)}_{n+1} = a^{(r+1)}_n + a^{(r)}_{n+1}$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 2, Equation (2.2).

Stated but not proved: `MetaMathlibExt.hypersequence_succ_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hypersequence-succ-succ).

## Hyperfibonacci numbers in terms of Fibonacci numbers

Let $F_k$ denote the $k$th Fibonacci
number and $F^{(r)}_n$ the hyperfibonacci numbers, given by $F^{(0)}_n = F_n$ and
$F^{(r+1)}_n = \sum_{k=0}^{n} F^{(r)}_k$. For all natural numbers $r$ and $n$,

$$F^{(r)}_n = F_{n+2r} - \sum_{k=0}^{r-1} \binom{n + k - 1}{k} F_{2(r-k)}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 3, Equation (2.8).

Stated but not proved: `MetaMathlibExt.hyperFibonacci_eq_fib_sub_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyper-fibonacci-eq-fib-sub-sum).

## Fibonacci numbers as binomially weighted sums

Let $F_k$ denote the $k$th Fibonacci
number. For every natural number $r \ge 1$ and every natural number $n$,

$$F_{n+2r} = \sum_{k=0}^{n} \binom{n + r - 1 - k}{r - 1} F_k +
\sum_{k=0}^{r-1} \binom{n + k - 1}{k} F_{2(r-k)}$$

and

$$F_{n+2r} = \sum_{k=0}^{n} \binom{r + k - 1}{k} F_{n-k} +
\sum_{k=0}^{r-1} \binom{n + k - 1}{k} F_{2(r-k)}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Corollary 1.

Stated but not proved: `MetaMathlibExt.fib_add_two_mul_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#fib-add-two-mul-eq-sum-choose).

## Recurrence for the hyperfibonacci numbers

Let $F^{(r)}_n$ denote the hyperfibonacci
numbers. For all natural numbers $r$ and $n$, $F^{(r)}_0 = 0$, $F^{(r)}_1 = 1$, and
$F^{(r+1)}_{n+2} = F^{(r+1)}_{n+1} + F^{(r+1)}_n + \binom{n+r+1}{r}$.

Equivalently, for $r \ge 1$, $F^{(r)}_{n+2} = F^{(r)}_{n+1} + F^{(r)}_n + \binom{n+r}{r-1}$, the
form in which Parisse quotes this result of Cristea, Martinjak and Urbiha.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 4, Equation (2.9).

Stated but not proved: `MetaMathlibExt.hyperFibonacci_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyper-fibonacci-recurrence).

## Hyperlucas numbers in terms of Lucas numbers

Let $L_n$ denote the Lucas numbers and
let $L^{(r)}_n$ denote the hyperlucas numbers, the hypersequence of generation $r$ of $(L_n)$.
For all natural numbers $r$ and $n$, in the integers,

$$L^{(r)}_n = L_{n+2r} - \sum_{k=0}^{r-1} \binom{n+k}{k} L_{2(r-k)-1}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 5, Equation (2.12).

Stated but not proved: `MetaMathlibExt.hyperLucas_eq_lucas_sub_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyper-lucas-eq-lucas-sub-sum).

## Lucas numbers as binomial sums

Let $L_n$ denote the Lucas numbers. For every $r \ge 1$
and every natural number $n$,

$$L_{n+2r} = \sum_{k=0}^{n} \binom{n+r-1-k}{r-1} L_k +
\sum_{k=0}^{r-1} \binom{n+k}{k} L_{2(r-k)-1}$$

and

$$L_{n+2r} = \sum_{k=0}^{n} \binom{r+k-1}{k} L_{n-k} +
\sum_{k=0}^{r-1} \binom{n+k}{k} L_{2(r-k)-1}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Corollary 2.

Stated but not proved: `MetaMathlibExt.lucas_add_two_mul_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#lucas-add-two-mul-eq-sum-choose).

## Recurrence for the hyperlucas numbers

Let $L^{(r)}_n$ denote the hyperlucas numbers,
the hypersequence of generation $r$ of the Lucas numbers. For all natural numbers $r$ and $n$,
$L^{(r)}_0 = 2$, $L^{(r)}_1 = 2r + 1$, and, in the rational numbers,

$$L^{(r+1)}_{n+2} = L^{(r+1)}_{n+1} + L^{(r+1)}_n + \frac{n + 2(r+1)}{n+2} \binom{n+r+1}{r}.$$

Equivalently, for $r \ge 1$,

$$L^{(r)}_{n+2} = L^{(r)}_{n+1} + L^{(r)}_n + \frac{n+2r}{n+2} \binom{n+r}{r-1}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 6, Equation (2.13).

Stated but not proved: `MetaMathlibExt.hyperLucas_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyper-lucas-recurrence).

## Abel summation by parts

Let $a$ and $b$ be sequences of complex numbers and let
$a^{(1)}_k = \sum_{i=0}^{k} a_i$ be the first hypersequence (the partial sums) of $a$. Then for
every natural number $n$,

$$\sum_{k=0}^{n} a_k b_k = a^{(1)}_n b_{n+1} + \sum_{k=0}^{n} a^{(1)}_k (b_k - b_{k+1}).$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 7.

Stated but not proved: `MetaMathlibExt.sum_mul_eq_hypersequence_one_mul_add_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-mul-eq-hypersequence-one-mul-add-sum).

## Recurrence for power-weighted sums of hypersequences

Let $a$ be a sequence of complex
numbers, let $a^{(r)}_k$ denote its hypersequence of generation $r$, and for natural numbers
$\ell$, $r$ and $n$ let $t^{(r)}_\ell(n) = \sum_{k=0}^{n} k^\ell a^{(r)}_k$, with the convention
$0^0 = 1$. Then for all natural numbers $\ell$, $r$ and $n$,

$$t^{(r)}_\ell(n) = (n + 1)^\ell a^{(r+1)}_n - \sum_{j=0}^{\ell-1} \binom{\ell}{j} t^{(r+1)}_j(n),$$

where the sum over $j$ is empty when $\ell = 0$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 8, Equation (3.5).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_hypersequence_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-pow-mul-hypersequence-recurrence).

## Power-weighted sums of hypersequences

Let $a$ be a sequence of complex numbers, let
$a^{(r)}_n$ denote its hypersequence of generation $r$, let
$p_{\ell,m}(x, y) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (ix + y)^\ell$ be the alternating binomial
power sum, and let $S(j, m)$ denote the Stirling numbers of the second kind. Then for all
natural numbers $\ell$, $n$ and $r$, with the convention $0^0 = 1$,

$$\sum_{k=0}^{n} k^\ell a^{(r)}_k = \sum_{m=0}^{\ell} p_{\ell,m}(1, n + 1)\, a^{(r+m+1)}_n$$

and

$$\sum_{k=0}^{n} k^\ell a^{(r)}_k = \sum_{j=0}^{\ell} \binom{\ell}{j}
\Bigl(\sum_{m=0}^{j} (-1)^m\, m!\, S(j, m)\, a^{(r+m+1)}_n\Bigr) (n + 1)^{\ell-j}.$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 9, Equations (3.7) and (3.8).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_hypersequence_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-pow-mul-hypersequence-eq).

## Power-weighted sums of a sequence via its hypersequences

Let $a$ be a sequence of complex
numbers, let $a^{(r)}_n$ denote its hypersequence of generation $r$, let
$p_{\ell,m}(x, y) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (ix + y)^\ell$ be the alternating binomial
power sum, and let $S(j, m)$ denote the Stirling numbers of the second kind. Then for all
natural numbers $\ell$ and $n$, with the convention $0^0 = 1$,

$$\sum_{k=0}^{n} k^\ell a_k = \sum_{m=0}^{\ell} p_{\ell,m}(1, n + 1)\, a^{(m+1)}_n$$

and

$$\sum_{k=0}^{n} k^\ell a_k = \sum_{j=0}^{\ell} \binom{\ell}{j}
\Bigl(\sum_{m=0}^{j} (-1)^m\, m!\, S(j, m)\, a^{(m+1)}_n\Bigr) (n + 1)^{\ell-j}.$$

This is the case $r = 0$ of the corresponding identity for $\sum_{k=0}^{n} k^\ell a^{(r)}_k$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Corollary 3.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-pow-mul-eq).

## Boyadzhiev's and Katsuura's formulas for alternating binomial power sums

Let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell$ and let $S(j, m)$ denote the
Stirling numbers of the second kind. For all complex numbers $x, y$ and natural numbers
$\ell, m$:
(i) (Boyadzhiev) $p_{\ell,m}(x, y) = \sum_{j=m}^{\ell} \binom{\ell}{j} (-1)^m m!\, S(j, m)\,
x^j y^{\ell-j}$, where the sum is empty (hence $0$) when $\ell < m$;
(ii) (Katsuura) if $\ell < m$ then $p_{\ell,m}(x, y) = 0$, and $p_{m,m}(x, y) = (-1)^m x^m m!$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Proposition 1.

Stated but not proved: `MetaMathlibExt.alternatingBinomialPowerSum_eq_sum_stirlingSecond` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#alternating-binomial-power-sum-eq-sum-st).

## Special values of alternating binomial power sums

Let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell$, with $0^0 = 1$, and let
$S(j, m)$ denote the Stirling numbers of the second kind. For all complex numbers $x, y$ and
natural numbers $\ell, m$:
(i) $p_{\ell,m}(x, x) = (-1)^m m!\, S(\ell + 1, m + 1)\, x^\ell$, and in particular
$p_{\ell,m}(1, 1) = (-1)^m m!\, S(\ell + 1, m + 1)$;
(ii) $p_{\ell,m}(0, y) = 0^m y^\ell$;
(iii) $p_{\ell,m}(x, 0) = (-1)^m m!\, S(\ell, m)\, x^\ell$, and in particular
$p_{m+1,m}(1, 0) = (-1)^m m! \binom{m+1}{2}$;
(iv) $p_{\ell,m}(-1, m) = m!\, S(\ell, m)$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Proposition 2 (i)–(iv).

Stated but not proved: `MetaMathlibExt.alternatingBinomialPowerSum_special_values` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#alternating-binomial-power-sum-special-v).

## Small cases of alternating binomial power sums

Let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell$, with $0^0 = 1$. For all
complex numbers $x, y$ and natural numbers $\ell, m$:
(i) $p_{\ell,0}(x, y) = y^\ell$;
(ii) $p_{\ell,1}(x, y) = y^\ell - (x + y)^\ell$;
(iii) $p_{\ell,2}(x, y) = y^\ell - 2(x + y)^\ell + (2x + y)^\ell$;
(iv) if $\ell \ge 1$, then
$p_{\ell,\ell-1}(x, y) = (-1)^{\ell-1} \ell!\, x^{\ell-1} \left(y + \frac{\ell - 1}{2} x\right)$;
(v) $p_{\ell,\ell}(x, y) = (-1)^\ell \ell!\, x^\ell$;
(vi) $p_{0,m}(x, y) = 0^m$;
(vii) $\sum_{m=0}^{\ell} p_{\ell,m}(x, y) = (y - x)^\ell$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Proposition 3.

Stated but not proved: `MetaMathlibExt.alternatingBinomialPowerSum_small_cases` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#alternating-binomial-power-sum-small-cas).

## Recurrences for alternating binomial power sums

Let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell$. For all complex numbers
$x, y$ and natural numbers $\ell, m$ (sums over an empty range are $0$, and $m - 1$ means $0$ when
$m = 0$):
(i) $p_{\ell,m+1}(x, y) = p_{\ell,m}(x, y) - p_{\ell,m}(x, x + y)$;
(ii) $p_{\ell,m}(x, x + y) = \sum_{j=m}^{\ell} \binom{\ell}{j} p_{j,m}(x, y)\, x^{\ell-j}$;
(iii) $p_{\ell,m+1}(x, y) = -\sum_{j=m}^{\ell-1} \binom{\ell}{j} p_{j,m}(x, y)\, x^{\ell-j}$;
(iv) $p_{\ell+1,m}(x, y) = y\, p_{\ell,m}(x, y) - m x\, p_{\ell,m-1}(x, x + y)$;
(v) $p_{\ell+1,m+1}(x, y) = ((m + 1) x + y)\, p_{\ell,m+1}(x, y) -
(m + 1) x\, p_{\ell,m}(x, y)$;
(vi) if $\ell \ge 1$, the complex derivative of $z \mapsto p_{\ell,m}(x, z)$ at $z = y$ is
$\ell\, p_{\ell-1,m}(x, y)$;
(vii) if $\ell \ge 1$, then
$p_{\ell,m}(x, y) = (m x + y)\, p_{\ell-1,m}(x, y) - m x\, p_{\ell-1,m-1}(x, y)$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Proposition 4.

Stated but not proved: `MetaMathlibExt.alternatingBinomialPowerSum_recurrences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#alternating-binomial-power-sum-recurrenc).

## Derivative and recurrence of the shifted alternating binomial power sums

Let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (kx + y)^\ell$ and, for a complex number
$n$, let $c_{\ell,m}(n) = p_{\ell,m}(1, n + 1)$. For natural numbers $\ell, m \ge 1$ and every
complex number $n$, the complex derivative of $c_{\ell,m}$ at $n$ is $\ell\, c_{\ell-1,m}(n)$, and
$c_{\ell,m}(n) = (m + n + 1)\, c_{\ell-1,m}(n) - m\, c_{\ell-1,m-1}(n)$.

The variable $n$ is complex here because the paper differentiates in $n$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Corollary 4, Equation (3.38).

Stated but not proved: `MetaMathlibExt.carlitzSum_deriv_and_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#carlitz-sum-deriv-and-recurrence).

## Sums of $m$th powers via Stirling numbers of the second kind

For all natural numbers
$n$ and $m$,

$$\sum_{k=1}^{n} k^m = \sum_{k=0}^{m} (-1)^{m-k}\, k!\, \binom{n + k}{k + 1}\, S(m, k),$$

where $S(m, k)$ denotes the Stirling numbers of the second kind.

The paper takes $n \ge 1$; for $n = 0$ both sides vanish, so that case is included.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Corollary 5, Equation (4.4).

Stated but not proved: `MetaMathlibExt.sum_pow_eq_sum_stirlingSecond` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-pow-eq-sum-stirling-second).

## Alternating binomial expansion of a shifted binomial coefficient

For all natural numbers
$m$, $n$ and $k$,

$$\binom{n+m-k-1}{m} = \sum_{j=0}^{k} (-1)^j \binom{k}{j} \binom{n+m-j-1}{m-j},$$

where, for an integer $x$ and a natural number $i$, $\binom{x}{i} = x(x-1)\cdots(x-i+1)/i!$ is
the generalized binomial coefficient, and the term $\binom{n+m-j-1}{m-j}$ is taken to be $0$
when $j > m$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Lemma 1, Equation (4.10).

Stated but not proved: `MetaMathlibExt.ringChoose_sub_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#ring-choose-sub-eq-sum).

## Powers of $k + 1$ via Stirling numbers of the second kind

For all natural numbers $k$
and $\ell$,

$$(k + 1)^\ell = \sum_{j=0}^{k} \binom{k}{j}\, j!\, S(\ell + 1, j + 1),$$

where $S(i, j)$ denotes the Stirling numbers of the second kind.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Lemma 2, Equation (4.11).

Stated but not proved: `MetaMathlibExt.succ_pow_eq_sum_stirlingSecond` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#succ-pow-eq-sum-stirling-second).

## Power-weighted sums of Fibonacci numbers

Let $F_k$ denote the Fibonacci numbers and let
$p_{\ell,m}(x, y) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (ix + y)^\ell$ be the alternating binomial
power sum. Then for all natural numbers $\ell$ and $n$, with the convention $0^0 = 1$,

$$\sum_{k=0}^{n} k^\ell F_k = \sum_{m=0}^{\ell} p_{\ell,m}(1, n + 1)\, F_{n+2(m+1)} -
\sum_{m=0}^{\ell} p_{\ell,m}(1, 1)\, F_{2(m+1)}.$$

The paper's conjecture on the constant term, stated after this theorem, is not included.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 10, Equation (4.7).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_fib_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-pow-mul-fib-eq).

## Power-weighted sums of Lucas numbers

Let $L_k$ denote the Lucas numbers, so $L_0 = 2$,
$L_1 = 1$ and $L_{k+2} = L_{k+1} + L_k$, and let
$p_{\ell,m}(x, y) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (ix + y)^\ell$ be the alternating binomial
power sum. Then for all natural numbers $\ell$ and $n$, with the convention $0^0 = 1$,

$$\sum_{k=0}^{n} k^\ell L_k = \sum_{m=0}^{\ell} p_{\ell,m}(1, n + 1)\, L_{n+2(m+1)} -
\sum_{m=0}^{\ell} p_{\ell,m}(1, 1)\, L_{2(m+1)} + L_0 \cdot 0^\ell.$$

The paper's conjecture on the constant term, stated after this theorem, is not included.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums*, INTEGERS 24 (2024), Article A70, Theorem 11, Equation (4.9).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_lucas_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceWeightedSumsWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-pow-mul-lucas-eq).

## Recurrence, closed form and row sums of $e_{j,k}(n)$

Let $n \in \mathbb{N}$ and let
$e_{j,k}(n)$ be the elementary symmetric polynomial of degree $k$ in $n + 1, \dots, n + j$.
Write $[j, \ell]$ for the unsigned Stirling numbers of the first kind and
$x^{\overline{j}} = x (x + 1) \cdots (x + j - 1)$ for the rising factorial. Then
$e_{0,k}(n) = \delta_{0,k}$ for all $k$;
$e_{j+1,k+1}(n) = e_{j,k+1}(n) + (n + j + 1) \, e_{j,k}(n)$ for all $j, k \in \mathbb{N}$;
$e_{j,k}(n) = \sum_{\ell=0}^{k} \binom{j-k+\ell}{\ell} [j, j-k+\ell] \, (n + 1)^\ell$ for all
$k \le j$; and for all $j$, $\sum_{k=0}^{j} e_{j,k}(n) = (n + 2)^{\overline{j}}$ and
$\sum_{k=0}^{j} (-1)^k e_{j,k}(n) = (-1)^j n^{\overline{j}}$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Proposition 1.

Stated but not proved: `MetaMathlibExt.hyperseq_esymm_recurrence_closed_form_row_sums` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-esymm-recurrence-closed-form-ro).

## Elementary symmetric functions of the first integers via Stirling numbers

For
$j, k \in \mathbb{N}$ let $e_{j,k}$ be the elementary symmetric polynomial of degree $k$ evaluated
at $1, 2, \dots, j$ (the source's $e_{j,k}(0)$), and let $c(j, i)$ be the unsigned Stirling number
of the first kind. Then $e_{0,k} = 1$ if $k = 0$ and $e_{0,k} = 0$ otherwise; for all $j, k$,
$e_{j+1,k+1} = e_{j,k+1} + (j + 1)\, e_{j,k}$; and for all $k \le j$,

$$e_{j,k} = \sum_{\ell=0}^{k} \binom{j-k+\ell}{\ell}\, c(j, j-k+\ell) = c(j + 1, j + 1 - k).$$

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Corollary 3.

Stated but not proved: `MetaMathlibExt.hyperseq_esymm_zero_recurrence_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-esymm-zero-recurrence-stirling).

## Parisse's matrix $B(n)$

For an integer $n$ and $j, k \in \mathbb{N}$, let $e_{j,i}(n)$ be
the elementary symmetric polynomial of degree $i$ in $n + 1, \dots, n + j$. The entry
$b_{j,k}(n)$ of $B(n)$ is $(-1)^k e_{j,j-k}(n)$ for $k \le j$ and $0$ for $k > j$; it is an
integer.

The source also uses this for $n \in \mathbb{Z}$ (Proposition 3, after Remark 1), which is why
$n$ ranges over the integers.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Section 2, Equation (2.5).

Formalized by `MetaMathlibExt.hyperseqB`, a definition declared in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-b).

## Row one of Parisse's matrix $B(n)$

For every integer $n$, the entries $b_{j,k}(n)$ of
$B(n)$ satisfy $b_{1,0}(n) = n + 1$ and $b_{1,1}(n) = -1$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Section 2, display of `B(n)`.

Formalized by `MetaMathlibExt.hyperseqB_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-b-one).

## Row three of Parisse's matrix $B(1)$

The entries $b_{3,0}(1), b_{3,1}(1), b_{3,2}(1),
b_{3,3}(1)$ of $B(1)$ are $24, -26, 9, -1$.

This matches the source's display of row three of $B(n)$,
$(n + 1)(n + 2)(n + 3), -(3n^2 + 12n + 11), 3n + 6, -1$, at $n = 1$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Section 2, display of `B(n)`.

Formalized by `MetaMathlibExt.hyperseqB_row_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-b-row-three).

## Mitrinović's numbers

For complex numbers $a$ and $b$, Mitrinović's numbers
$R^k_j(a, b)$, $j, k \in \mathbb{N}$ (lower index $j$, upper index $k$), are defined by
$R^k_0(a, b) = 1$ if $k = 0$ and $R^k_0(a, b) = 0$ otherwise, and, for all $j, k$, by
$R^0_{j+1}(a, b) = -(a + b j)\, R^0_j(a, b)$ and
$R^{k+1}_{j+1}(a, b) = R^k_j(a, b) - (a + b j)\, R^{k+1}_j(a, b)$.

With $R = 0$ at negative indices this is the recurrence (4.2),
$R^k_j(a, b) = R^{k-1}_{j-1}(a, b) - (a - b + b j)\, R^k_{j-1}(a, b)$ for $j \ge 1$. The start
value is the source's Corollary 5 at $a = 0$ and its solution (4.3) at $j = 0$ for every $a$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Section 4, Equation (4.2).

Formalized by `MetaMathlibExt.mitrinovicR`, a definition declared in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#mitrinovic-r).

## Mitrinović's numbers with lower index one

For all complex numbers $a, b$, Mitrinović's
numbers satisfy $R^0_1(a, b) = -a$ and $R^1_1(a, b) = 1$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Section 4, Equation (4.2).

Formalized by `MetaMathlibExt.mitrinovicR_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#mitrinovic-r-one).

## Hypersequences through elementary symmetric polynomials

Let $a$ be a sequence of complex
numbers and let $j, n \in \mathbb{N}$. Write $a^{(r)}_n$ for the hypersequence of generation $r$
of $a$, write $e_{j,k}(n)$ for the elementary symmetric polynomial of degree $k$ in
$n + 1, \dots, n + j$, and put $t_i(n) = \sum_{k=0}^{n} k^i a_k$, with $0^0 = 1$. Then
$j! \, a^{(j+1)}_n = (-1)^j \sum_{k=0}^{j} (-1)^k e_{j,k}(n) \, t_{j-k}(n)$ and
$j! \, a^{(j+1)}_n = \sum_{k=0}^{j} (-1)^k e_{j,j-k}(n) \, t_k(n)$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Theorem 1, Equation (2.1).

Stated but not proved: `MetaMathlibExt.factorial_mul_hypersequence_eq_sum_esymm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#factorial-mul-hypersequence-eq-sum-esymm).

## The inverse of Parisse's matrix $C(n)$

Let $n \in \mathbb{N}$. Let $e_{j,i}(n)$ be the
elementary symmetric polynomial of degree $i$ in $n + 1, \dots, n + j$, let
$b_{j,k}(n) = (-1)^k e_{j,j-k}(n)$ for $k \le j$ and $b_{j,k}(n) = 0$ for $k > j$, let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k x + y)^\ell$ for complex $x, y$, and let
$c_{\ell,m}(n) = p_{\ell,m}(1, n + 1) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k + n + 1)^\ell$.
Then for all $j, m \in \mathbb{N}$, with $\delta_{j,m}$ the Kronecker delta,
$\sum_{k=0}^{j} \frac{b_{j,k}(n)}{j!} \, c_{k,m}(n) = \delta_{j,m}$ and
$\sum_{k=0}^{j} c_{j,k}(n) \, \frac{b_{k,m}(n)}{k!} = \delta_{j,m}$.

In matrix form, with $B(n) = (b_{j,k}(n))$, $C(n) = (c_{\ell,m}(n))$ and $D$ the diagonal matrix
of the factorials $j!$, this says $C(n)^{-1} = D^{-1} B(n)$; both matrices are lower triangular,
so each entry of the two products is the finite sum above.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Theorem 2.

Stated but not proved: `MetaMathlibExt.hyperseqC_inv_eq_hyperseqB_div_factorial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-c-inv-eq-hyperseq-b-div-factori).

## The inverse of Parisse's matrix $B(n)$

Let $n \in \mathbb{N}$. Let $e_{j,i}(n)$ be the
elementary symmetric polynomial of degree $i$ in $n + 1, \dots, n + j$, let
$b_{j,k}(n) = (-1)^k e_{j,j-k}(n)$ for $k \le j$ and $b_{j,k}(n) = 0$ for $k > j$, let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k x + y)^\ell$ for complex $x, y$, and let
$c_{\ell,m}(n) = p_{\ell,m}(1, n + 1) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k + n + 1)^\ell$.
Then for all $j, m \in \mathbb{N}$, with $\delta_{j,m}$ the Kronecker delta,
$\sum_{k=0}^{j} b_{j,k}(n) \, \frac{c_{k,m}(n)}{m!} = \delta_{j,m}$ and
$\sum_{k=0}^{j} \frac{c_{j,k}(n)}{k!} \, b_{k,m}(n) = \delta_{j,m}$.

In matrix form, with $B(n) = (b_{j,k}(n))$, $C(n) = (c_{\ell,m}(n))$ and $D$ the diagonal matrix
of the factorials $j!$, this says $B(n)^{-1} = C(n) D^{-1}$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Corollary 1, Equation (2.9).

Stated but not proved: `MetaMathlibExt.hyperseqB_inv_eq_hyperseqC_div_factorial` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-b-inv-eq-hyperseq-c-div-factori).

## The product of Parisse's matrices B(n) and C(n)

For $n, j, m \in \mathbb{N}$ let
$b_{j,i}(n) = (-1)^i e_{j-i}(n + 1, \dots, n + j)$ for $i \le j$ be the entries of Parisse's
matrix $B(n)$, where $e_d$ is the elementary symmetric polynomial of degree $d$, and let
$c_{i,m}(n) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k + n + 1)^i$ be the entries
of $C(n)$. Then $\sum_{i=0}^{j} b_{j,i}(n)\, c_{i,m}(n)$ equals $j!$ if $j = m$ and $0$ otherwise.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Corollary 2.

Stated but not proved: `MetaMathlibExt.sum_hyperseqB_mul_hyperseqC` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#sum-hyperseq-b-mul-hyperseq-c).

## Recurrence, closed form and row sums of Parisse's $b_{j,k}(n)$

Let $n \in \mathbb{N}$ and
let $b_{j,k}(n)$ be the entries of Parisse's matrix $B(n)$. Write $[j, \ell]$ for the unsigned
Stirling numbers of the first kind and $x^{\overline{j}} = x (x + 1) \cdots (x + j - 1)$ for the
rising factorial. Then $b_{0,k}(n) = \delta_{0,k}$ for all $k$; for all $j, k \in \mathbb{N}$,
$b_{j+1,0}(n) = (n + j + 1) \, b_{j,0}(n)$ and
$b_{j+1,k+1}(n) = (n + j + 1) \, b_{j,k+1}(n) - b_{j,k}(n)$;
$b_{j,k}(n) = (-1)^k \sum_{\ell=k}^{j} \binom{\ell}{k} [j, \ell] \, (n + 1)^{\ell-k}$ for all
$j, k$ (an empty sum for $k > j$); and for all $j$,
$\sum_{k=0}^{j} b_{j,k}(n) = n^{\overline{j}}$ and
$\sum_{k=0}^{j} (-1)^k b_{j,k}(n) = (n + 2)^{\overline{j}}$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Proposition 2.

Stated but not proved: `MetaMathlibExt.hyperseqB_recurrence_closed_form_row_sums` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-b-recurrence-closed-form-row-su).

## Parisse's $b_{j,k}(0)$ and Stirling numbers of the first kind

Let $b_{j,k}(0)$ be the
entries of Parisse's matrix $B(0)$ and write $[j, \ell]$ for the unsigned Stirling numbers of the
first kind. Then $b_{0,k}(0) = \delta_{0,k}$ for all $k$; for all $j, k \in \mathbb{N}$,
$b_{j+1,0}(0) = (j + 1) \, b_{j,0}(0)$ and $b_{j+1,k+1}(0) = (j + 1) \, b_{j,k+1}(0) - b_{j,k}(0)$;
and for all $j, k \in \mathbb{N}$,
$b_{j,k}(0) = (-1)^k \sum_{\ell=k}^{j} \binom{\ell}{k} [j, \ell] = (-1)^k [j + 1, k + 1]$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Corollary 4.

Stated but not proved: `MetaMathlibExt.hyperseqB_zero_recurrence_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-b-zero-recurrence-stirling).

## Parisse's coefficients at $n$ from their values at $-1$

Let $n \in \mathbb{Z}$. For
$j, k \in \mathbb{N}$ let $e_{j,k}(n)$ be the elementary symmetric polynomial of degree $k$ in
$n + 1, \dots, n + j$, let $b_{j,k}(n) = (-1)^k e_{j,j-k}(n)$ for $k \le j$ and $b_{j,k}(n) = 0$
for $k > j$, let
$p_{\ell,m}(x, y) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k x + y)^\ell$ for complex $x, y$, with
$0^0 = 1$, and let
$c_{\ell,m}(n) = p_{\ell,m}(1, n + 1) = \sum_{k=0}^{m} (-1)^k \binom{m}{k} (k + n + 1)^\ell$. Then
$e_{j,k}(n) = \sum_{i=0}^{k} \binom{j - k + i}{i} (n + 1)^i e_{j,k-i}(-1)$ for all $k \le j$,
$b_{j,k}(n) = \sum_{i=k}^{j} (-1)^{i-k} \binom{i}{k} (n + 1)^{i-k} b_{j,i}(-1)$ for all $j, k$,
and $c_{\ell,m}(n) = \sum_{i=m}^{\ell} \binom{\ell}{i} (n + 1)^{\ell-i} c_{i,m}(-1)$ for all
$\ell, m \in \mathbb{N}$.

The first identity is stated only for $k \le j$; for $k > j$ the source's upper index
$j - k + i$ of the binomial coefficient can be negative.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Proposition 3.

Stated but not proved: `MetaMathlibExt.hyperseq_entries_eq_sum_at_neg_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#hyperseq-entries-eq-sum-at-neg-one).

## Mitrinović's numbers at $a = 0$

For every complex number $b$, Mitrinović's numbers
$R^k_j(0, b)$ satisfy the following. First, for every $k \in \mathbb{N}$, $R^k_0(0, b) = 1$ if
$k = 0$ and $R^k_0(0, b) = 0$ otherwise. Second, for all $j, k \in \mathbb{N}$,
$R^{k+1}_{j+1}(0, b) = R^k_j(0, b) + (b - b(j + 1))\, R^{k+1}_j(0, b)$. Third, for all
$j, k \in \mathbb{N}$, $R^k_j(0, b) = (-b)^{j-k} c(j, k)$, where $c(j, k)$ is the unsigned
Stirling number of the first kind, which is $0$ for $k > j$, and the exponent $j - k$ is read as
$0$ when $k > j$.

The source prints the last factor of the recurrence as $R^k_{j-1}(a, b)$; it is
$R^k_{j-1}(0, b)$, the case $a = 0$ of (4.2). The source's hypothesis $b \ne 0$ is dropped: at
$b = 0$ both sides of the closed form are $\delta_{j,k}$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Corollary 5.

Stated but not proved: `MetaMathlibExt.mitrinovicR_zero_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#mitrinovic-r-zero-eq).

## Binomial expansion of Mitrinović's numbers in the first parameter

For all complex
numbers $a, b$ and all $j, k \in \mathbb{N}$, Mitrinović's numbers satisfy

$$R^k_j(a, b) = \sum_{\ell=0}^{j-k} (-1)^\ell \binom{k+\ell}{\ell} a^\ell R^{k+\ell}_j(0, b),$$

where the upper limit $j - k$ is read as $0$ when $k > j$ (both sides are then $0$).

The source's hypothesis $b \ne 0$ is not needed: the identity also holds at $b = 0$.

## Sources

- Daniele Parisse, *On Hypersequences of an Arbitrary Sequence and Their Weighted Sums II*, INTEGERS 26 (2026), Article A36, Proposition 4, Equation (4.6).

Stated but not proved: `MetaMathlibExt.mitrinovicR_eq_sum_mitrinovicR_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/HypersequenceElementarySymmetricWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html#mitrinovic-r-eq-sum-mitrinovic-r-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypersequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/hypersequences)
