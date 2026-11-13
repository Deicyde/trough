---
declaration: section
origin: cited
lean: MetaMathlibExt.octanacciWindow, MetaMathlibExt.octanacciNumber, MetaMathlibExt.nStepFibonacci, MetaMathlibExt.nStepFibonacci_add_two, MetaMathlibExt.nStepFibonacci_zero, MetaMathlibExt.nStepFibonacci_one, MetaMathlibExt.nStepFibonacci_three_five, MetaMathlibExt.dominant_root_bounds_k_generalized_fibonacci
statement: formalized
---

# k-generalized Fibonacci numbers

75 results, 21 proved and 54 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html).

## Octanacci window

The octanacci window is the sequence $(w_n)_{n \ge 0}$ of $8$-tuples of
natural numbers with $w_0 = (1, 1, 2, 4, 8, 16, 32, 64)$ and, if $w_n = (a_1, \dots, a_8)$, then
$w_{n+1} = (a_2, \dots, a_8, a_1 + a_2 + \dots + a_8)$. The octanacci numbers $f_n$ are the first
entries of these tuples, so $w_n = (f_n, f_{n+1}, \dots, f_{n+7})$.

Formalized by `MetaMathlibExt.octanacciWindow`, a definition declared in [MathlibExt/Combinatorics/Enumerative/OctanacciNumber.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/OctanacciNumber.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#octanacci-window).

## Octanacci numbers

The octanacci sequence $(f_n)_{n \ge 0}$ of natural numbers is defined by
$f_0 = f_1 = 1$, $f_n = 2^{n-1}$ for $2 \le n \le 7$, and
$f_n = f_{n-1} + f_{n-2} + \dots + f_{n-8}$ for $n \ge 8$. It begins
$1, 1, 2, 4, 8, 16, 32, 64, 128, 255, \dots$, and its generating function is
$1/(1 - t - t^2 - \dots - t^8)$.

Formalized by `MetaMathlibExt.octanacciNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/OctanacciNumber.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/OctanacciNumber.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#octanacci-number).

## N-step Fibonacci numbers

For a natural number $N$, the $N$-step Fibonacci numbers
$F^{(N)}_n$ ($n \ge 0$), in the convention of Noe and Post, are defined by $F^{(N)}_0 = 0$,
$F^{(N)}_1 = 1$ and, for $n \ge 2$, $F^{(N)}_n = \sum_{i=1}^{N} F^{(N)}_{n-i}$, where a term
whose index $n - i$ is negative counts as $0$. In particular $F^{(0)}_n = 0$ for $n \ge 2$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Section 4.4.

Formalized by `MetaMathlibExt.nStepFibonacci`, a definition declared in [MathlibExt/NumberTheory/NStepFibonacciSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepFibonacciSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#n-step-fibonacci).

## Recurrence for the N-step Fibonacci numbers

For all natural numbers $N$ and $n$, the
$N$-step Fibonacci numbers $F^{(N)}$ satisfy
$F^{(N)}_{n+2} = \sum_{i=0}^{N-1} F^{(N)}_{\max(n+1-i,\,0)}$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Section 4.4.

Formalized by `MetaMathlibExt.nStepFibonacci_add_two`, a theorem declared in [MathlibExt/NumberTheory/NStepFibonacciSequence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepFibonacciSequence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#n-step-fibonacci-add-two).

## Zeroth N-step Fibonacci number

For every natural number $N$, the $N$-step Fibonacci
number $F^{(N)}_0$ equals $0$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Section 4.4.

Formalized by `MetaMathlibExt.nStepFibonacci_zero`, a theorem declared in [MathlibExt/NumberTheory/NStepFibonacciSequence.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepFibonacciSequence.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#n-step-fibonacci-zero).

## First N-step Fibonacci number

For every natural number $N$, the $N$-step Fibonacci
number $F^{(N)}_1$ equals $1$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Section 4.4.

Formalized by `MetaMathlibExt.nStepFibonacci_one`, a theorem declared in [MathlibExt/NumberTheory/NStepFibonacciSequence.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepFibonacciSequence.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#n-step-fibonacci-one).

## The tribonacci number with index 5

The $3$-step Fibonacci number $F^{(3)}_5$ equals $7$.

The tribonacci numbers $F^{(3)}_0, \dots, F^{(3)}_5$ are $0, 1, 1, 2, 4, 7$.

## Sources

- Bowman, *Compositions with an Odd Number of Parts, and Other Congruences*, Journal of Integer Sequences 27 (2024), Article 24.3.6, Section 4.4.

Formalized by `MetaMathlibExt.nStepFibonacci_three_five`, a theorem declared in [MathlibExt/NumberTheory/NStepFibonacciSequence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NStepFibonacciSequence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#n-step-fibonacci-three-five).

## Bounds on the dominant root of the k-generalized Fibonacci polynomial

Let $k$ be a natural
number and let $\alpha > 1$ be a real number with $\alpha^k = \sum_{i=0}^{k-1} \alpha^i$. Then
$2 - 1/k < \alpha < 2$, and if $k \ge 4$, moreover $2 - 1/(3k) < \alpha < 2$.

## Sources

- G. P. B. Dresden and Z. Du, *A Simplified Binet Formula for k-Generalized Fibonacci Numbers*, Journal of Integer Sequences 17 (2014), Article 14.4.7, Lemma `La`, line 350, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Dresden/dresden6.tex>.

Formalized by `MetaMathlibExt.dominant_root_bounds_k_generalized_fibonacci`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/DominantRootBounds.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/DominantRootBounds.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#dominant-root-bounds-k-generalized-fibon).

## Simplified Binet formula for k-generalized Fibonacci numbers from an initial window

Let $k \ge 2$ and let $F : \mathbb{Z} \to \mathbb{Z}$ satisfy $F(n) = 0$ for all integers $n$ with
$2 - k \le n < 1$, $F(1) = 1$, and $F(n) = \sum_{i=0}^{k-1} F(n - 1 - i)$ for all integers
$n > 1$. Let $\alpha$ be a positive real number with $\alpha^k = \sum_{i=0}^{k-1} \alpha^i$, and
put $c = (\alpha - 1)/(2 + (k + 1)(\alpha - 2))$. Then for every integer $n \ge 2 - k$,
$F(n) = \lfloor c\,\alpha^{n-1} + 1/2 \rfloor$.

Proof: We follow Dresden–Du's recurrence and first-crossing route, replacing their appeal to
the non-dominant-root results of Miles (1960) and Miller (1971) with an exact positive weighted
invariant.

## Sources

- G. P. B. Dresden and Z. Du, *A Simplified Binet Formula for k-Generalized Fibonacci Numbers*, Journal of Integer Sequences 17 (2014), Article 14.4.7, Theorem T2, lines 209-218, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Dresden/dresden6.tex>.

Formalized by `MetaMathlibExt.dresden_du_simplified_binet_of_initial_window`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/DresdenDuSimplifiedBinet.lean, line 705](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/DresdenDuSimplifiedBinet.lean#L705). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#dresden-du-simplified-binet-of-initial-w).

## Dresden–Du simplified Binet formula

Let $k \ge 2$ and let $F : \mathbb{Z} \to \mathbb{Z}$
satisfy $F(n) = 0$ for all integers $n < 1$, $F(1) = 1$, and
$F(n) = \sum_{i=0}^{k-1} F(n - 1 - i)$ for all integers $n > 1$. Let $\alpha$ be a positive real
number with $\alpha^k = \sum_{i=0}^{k-1} \alpha^i$, and suppose that every positive real $\beta$
with $\beta^k = \sum_{i=0}^{k-1} \beta^i$ equals $\alpha$. Put
$c = (\alpha - 1)/(2 + (k + 1)(\alpha - 2))$. Then for every integer $n \ge 2 - k$,
$F(n) = \lfloor c\,\alpha^{n-1} + 1/2 \rfloor$.

## Sources

- G. P. B. Dresden and Z. Du, *A Simplified Binet Formula for k-Generalized Fibonacci Numbers*, Journal of Integer Sequences 17 (2014), Article 14.4.7, Theorem T2, lines 209-218, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Dresden/dresden6.tex>.

Formalized by `MetaMathlibExt.dresden_du_simplified_binet`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/DresdenDuSimplifiedBinet.lean, line 759](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/DresdenDuSimplifiedBinet.lean#L759). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#dresden-du-simplified-binet).

## Power-weighted convolution of Fibonacci $m$-step numbers

Let $m \ge 1$ and let
$F \colon \mathbb{N} \to \mathbb{N}$ satisfy $F(0) = 0$, $F(1) = 1$ and
$F(k) = \sum_{j=1}^{m} F(k - j)$ for every $k \ge 2$, where a term $F(k - j)$ with $j > k$ is
read as $F(0) = 0$. Then for every natural number $n$,

$$\sum_{j=0}^{n} 2^j F(n - j) = 2^{n+m-1} - F(n + 1 + m),$$

where the subtraction on the right is taken in $\mathbb{N}$ (truncated at $0$).

The initial conditions are those of the paper's definition of Fibonacci $m$-step numbers
(lines 126–133), whose values at negative indices are $0$. The paper states the theorem for
$m \ge 3$; the cases $m = 1$ and $m = 2$ also hold, so the hypothesis here is $m \ge 1$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci m-Step Numbers," Journal of Integer Sequences 27 (2024), Article 24.8.8, Theorem, lines 453–459, https://cs.uwaterloo.ca/journals/JIS/VOL27/Gryszka/gryszka12.tex

Formalized by `MetaMathlibExt.two_pow_convolution_mstep_fibonacci`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/MStepFibonacciConvolution.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/MStepFibonacciConvolution.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-pow-convolution-mstep-fibonacci).

## Binet asymptotics for weighted generalized Fibonacci sequences, positive-root form

Let $r \ge 2$, let $A_1, \dots, A_r$ and $c_1, \dots, c_r$ be nonnegative real numbers with
$A_r > 0$ and $c_j > 0$ for some $j$, and suppose that the indices $j$ with $A_j > 0$ have
greatest common divisor $1$. Let $a_0, a_1, a_2, \dots$ be the real sequence with
$a_n = c_{n+1}$ for $0 \le n < r$ and $a_n = \sum_{j=1}^{r} A_j a_{n-j}$ for $n \ge r$, and let
$p(x) = x^r - \sum_{j=1}^{r} A_j x^{r-j}$ be its characteristic polynomial. Let $\lambda > 0$
be a root of $p$. Then there is a constant $C > 0$ such that $a_n = C \lambda^n + o(\lambda^n)$
as $n \to \infty$, and $a_{n+1} / a_n \to \lambda$.

Formalized by `MetaMathlibExt.binet_general`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/WeightedFibonacciBinet.lean, line 856](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/WeightedFibonacciBinet.lean#L856). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#binet-general).

## Binet asymptotics for weighted generalized Fibonacci sequences

Let $r \ge 2$, let
$A_1, \dots, A_r$ and $c_1, \dots, c_r$ be nonnegative real numbers with $A_r > 0$ and $c_j > 0$
for some $j$, and suppose that the indices $j$ with $A_j > 0$ have greatest common divisor $1$.
Let $a_0, a_1, a_2, \dots$ be the real sequence with $a_n = c_{n+1}$ for $0 \le n < r$ and
$a_n = \sum_{j=1}^{r} A_j a_{n-j}$ for $n \ge r$, and let $p(x) = x^r - \sum_{j=1}^{r} A_j x^{r-j}$
be its characteristic polynomial. Let $\lambda > 0$ be a root of $p$ that is not a root of the
derivative $p'$, and such that every complex root $z$ of $p$ satisfies $|z| \le \lambda$, with
$|z| = \lambda$ only for $z = \lambda$. Then there is a constant $C > 0$ such that
$a_n = C \lambda^n + o(\lambda^n)$ as $n \to \infty$, and $a_{n+1} / a_n \to \lambda$.

The source indexes the sequence from $1$; the $a_n$ here is the source's $a_{n+1}$, and $A_j$,
$c_j$ are the source's weights and initial values.

## Sources

- Passawan Noppakaew and Thanakorn Prinyasart, "Complete Sequences of Weighted r-Generalized Fibonacci Powers," Journal of Integer Sequences 24 (2021), Article 21.5.4, Proposition, lines 119–126, https://cs.uwaterloo.ca/journals/JIS/VOL24/Prinyasart/prin3.tex. It follows from `binet_general`; the hypotheses `hlam_simple` and `hlam_dom` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.binet`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/WeightedFibonacciBinet.lean, line 944](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/WeightedFibonacciBinet.lean#L944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#binet).

## Initial segments of the Fibonacci $m$-step sequence

For natural numbers $m$ and $n$,
this is the list of integers $[F_0, F_1, \dots, F_n]$, built recursively: the list for $n = 0$
is $[0]$, the list for $n = 1$ is $[0, 1]$, and for $n \ge 2$ the list for $n$ is the list for
$n - 1$ followed by $F_n = \sum_{j=1}^{m} F_{n-j}$, where $F_i = 0$ for $i < 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStepSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-seq).

## Fibonacci $m$-step numbers

For natural numbers $m$ and $n$, the integer $F^{(m)}_n$ is
defined by $F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$ and $F^{(m)}_n = \sum_{j=1}^{m} F^{(m)}_{n-j}$ for
$n \ge 2$, where $F^{(m)}_i = 0$ for $i < 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStep`, a definition declared in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step).

## Jacobsthal numbers

The Jacobsthal numbers are the integers $J_n$ defined by $J_0 = 0$,
$J_1 = 1$ and $J_{n+2} = J_{n+1} + 2 J_n$ for all $n \ge 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.jacobsthalSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#jacobsthal-seq).

## Generating function of the Fibonacci $m$-step numbers

For a natural number $m$,
$F^{(m)}(X)$ is the formal power series $\sum_{n \ge 0} F^{(m)}_n X^n$ with rational
coefficients, where $F^{(m)}_n$ is the $n$-th Fibonacci $m$-step number.

Formalized by `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStepGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-gf).

## Sums over compositions

Given integer sequences $a_0, \dots, a_{r-1}$ and a natural
number $n$, the sum over the compositions $K(r, n)$ of $n$ into $r$ nonnegative parts is the
sum, over all $(k_0, \dots, k_{r-1}) \in \mathbb{N}^r$ with $k_0 + \dots + k_{r-1} = n$, of
$\prod_{i=0}^{r-1} a_i(k_i)$.

Formalized by `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum).

## Truncated convolution of the $m$-step and $(m+1)$-step Fibonacci numbers

Write
$F^{(m)}_n$ for the Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each later
term is the sum of the $m$ terms before it, terms at negative indices being $0$). For all natural
numbers $m \ge 1$ and $n \ge m$,

$$\sum_{j=0}^{n-m} F^{(m)}_j F^{(m+1)}_{n-m-j} = F^{(m+1)}_n - F^{(m)}_n.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fibStep_mul_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-step-mul-succ).

## Convolution of the Fibonacci and tribonacci numbers

Write $F_n$ and $T_n$ for the
Fibonacci and tribonacci numbers, that is, the Fibonacci $m$-step numbers $F^{(m)}_n$ for
$m = 2, 3$ ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each later term is the sum of the $m$ terms
before it, terms at negative indices being $0$). For every natural number $n$,

$$\sum_{j=0}^{n} F_j T_{n-j} = T_{n+2} - F_{n+2}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fib_mul_trib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-mul-trib).

## Convolution of the Fibonacci 3-step and 4-step numbers

Let $T_j$ and $Q_j$ be the
Fibonacci $3$-step and $4$-step numbers, where the Fibonacci $k$-step numbers start $0, 1$ and
each later term is the sum of the $k$ terms before it (terms of negative index being $0$). For
every natural number $n$,

$$\sum_{j=0}^{n} T_j \, Q_{n-j} = Q_{n+3} - T_{n+3}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_trib_mul_tetra` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-trib-mul-tetra).

## Convolution of the Fibonacci 4-step and 5-step numbers

Let $Q_j$ and $P_j$ be the
Fibonacci $4$-step and $5$-step numbers, where the Fibonacci $k$-step numbers start $0, 1$ and
each later term is the sum of the $k$ terms before it (terms of negative index being $0$). For
every natural number $n$,

$$\sum_{j=0}^{n} Q_j \, P_{n-j} = P_{n+4} - Q_{n+4}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_tetra_mul_penta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-tetra-mul-penta).

## Iterated convolution of Fibonacci $m$-step and $(m+p)$-step numbers

Let $F^{(k)}_j$ be
the $j$-th Fibonacci $k$-step number: the sequence starts $F^{(k)}_0 = 0$, $F^{(k)}_1 = 1$, and each
later term is the sum of the $k$ terms before it (terms of negative index being $0$). For all
natural numbers $m$, $p$ and $n$ with $m \ge 1$ and $n \ge m$,

$$\sum_{k=0}^{p-1} \sum_{j=0}^{n-m-k} F^{(m)}_j \, F^{(m+p)}_{n-m-k-j} =
F^{(m+p)}_n - F^{(m)}_n,$$

where an inner sum whose upper limit $n - m - k$ is negative counts as $0$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_sum_fibStep_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-sum-fib-step-mul).

## Convolution of the $m$-step Fibonacci numbers with consecutive sums of the $(m+2)$-step ones

**Convolution of the $m$-step Fibonacci numbers with consecutive sums of the
$(m+2)$-step ones.** Write $F^{(m)}_n$ for the Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$,
$F^{(m)}_1 = 1$, and each later term is the sum of the $m$ terms before it, terms at negative
indices being $0$). For all natural numbers $m \ge 1$ and $n \ge m$,

$$\sum_{j=0}^{n-m-1} F^{(m)}_j \bigl(F^{(m+2)}_{n-m-j} + F^{(m+2)}_{n-m-j-1}\bigr) =
F^{(m+2)}_n - F^{(m)}_n.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 4.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fibStep_mul_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-step-mul-add).

## Double partial sums of Fibonacci step numbers

For natural numbers $p$ and $n$ with
$1 \le p \le n$, the Fibonacci $(p+1)$-step numbers $F^{(p+1)}_j$ satisfy

$$F^{(p+1)}_n - 1 = \sum_{k=0}^{p-1} \sum_{j=0}^{n-2-k} F^{(p+1)}_j,$$

where an inner sum whose upper limit is $-1$ is empty.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStep_sub_one_eq_sum_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-sub-one-eq-sum-sum).

## Partial sums of the Fibonacci $m$-step numbers

For natural numbers $m \ge 2$ and $n$,
the Fibonacci $m$-step numbers $F^{(m)}_k$ satisfy

$$(m-1) \sum_{k=0}^{n} F^{(m)}_k =
F^{(m)}_{n+m} - \sum_{k=1}^{m-2} (m-1-k) F^{(m)}_{n+k} - 1.$$

The source prints this identity divided by $m - 1$ and with coefficients $k$ in place of
$m-1-k$; its proof gives $m-1-k$, and the printed form already fails at $m = 4$, $n = 1$, where
it gives $2/3$ instead of $1$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.mul_sum_fibStep` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#mul-sum-fib-step).

## Convolution of the Fibonacci and tetranacci numbers

Write $F_n$ and $Q_n$ for the
Fibonacci and tetranacci numbers, that is, the Fibonacci $m$-step numbers $F^{(m)}_n$ for
$m = 2, 4$ ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each later term is the sum of the $m$ terms
before it, terms at negative indices being $0$). For every natural number $n$,

$$\sum_{j=0}^{n} F_j Q_{n-j} = Q_{n+1} + Q_{n-1} - F_{n+1},$$

where for $n = 0$ the term $Q_{n-1}$ is $Q_0 = 0$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollaries 9 and 16.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fib_mul_tetra` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-mul-tetra).

## Convolution of the Fibonacci and pentanacci numbers

Write $F_n$ for the Fibonacci numbers
and $P_n$ for the pentanacci numbers (the Fibonacci $m$-step numbers $F^{(m)}_n$ with $m = 2$ and
$m = 5$). For every integer $n \ge 0$,
$2 \sum_{j=0}^{n} F_j P_{n-j} = P_{n+2} + P_{n-1} - F_{n+2}$, where $P_{n-1}$ is read as
$P_0 = 0$ when $n = 0$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_sum_fib_mul_penta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-sum-fib-mul-penta).

## Convolution of the pentanacci and tribonacci numbers

Write $P_n$ for the pentanacci
numbers and $T_n$ for the tribonacci numbers (the Fibonacci $m$-step numbers $F^{(m)}_n$ with
$m = 5$ and $m = 3$). For every integer $n \ge 0$,
$2 \sum_{j=0}^{n} P_j T_{n-j} = P_{n+3} + P_{n+1} + P_{n-1} - T_{n+3} - T_{n+1}$, where
$P_{n-1}$ is read as $P_0 = 0$ when $n = 0$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_sum_penta_mul_trib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-sum-penta-mul-trib).

## Exchange identity for convolutions of $(m-2)$-, $(m-1)$- and $m$-step Fibonacci numbers

Write $F^{(m)}_n$ for the Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each
later term is the sum of the $m$ terms before it, terms at negative indices being $0$). For all
natural numbers $m \ge 3$ and $n \ge 1$,

$$\sum_{j=0}^{n} F^{(m-2)}_j \bigl(F^{(m)}_{n-j} - F^{(m-1)}_{n-j}\bigr) =
\sum_{j=0}^{n-1} F^{(m)}_j \bigl(F^{(m-1)}_{n-1-j} - F^{(m-2)}_{n-1-j}\bigr).$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 10.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fibStep_sub_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-step-sub-eq).

## Difference of the Fibonacci 3-step and 2-step numbers as a convolution

Let $F_j$ and
$T_j$ be the Fibonacci $2$-step and $3$-step numbers, where the Fibonacci $k$-step numbers start
$0, 1$ and each later term is the sum of the $k$ terms before it (terms of negative index being
$0$). For every natural number $n \ge 1$,

$$T_{n+1} - F_{n+1} = \sum_{j=0}^{n-1} T_j \, F_{n-1-j}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.trib_sub_fib_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#trib-sub-fib-eq-sum).

## Convolution of the Fibonacci numbers with tribonacci minus tetranacci

Write $F_n$, $T_n$
and $Q_n$ for the Fibonacci, tribonacci and tetranacci numbers, that is, the Fibonacci $m$-step
numbers $F^{(m)}_n$ for $m = 2, 3, 4$ ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each later term is the
sum of the $m$ terms before it, terms at negative indices being $0$). For every natural number
$n \ge 1$,

$$\sum_{j=0}^{n} F_j (T_{n-j} - Q_{n-j}) = \sum_{j=0}^{n-1} (F_j - T_j) Q_{n-1-j}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fib_mul_sub_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-mul-sub-eq).

## Convolution of the Fibonacci 3-step numbers with differences of 4- and 5-step numbers

Let $T_j$, $Q_j$ and $P_j$ be the Fibonacci $3$-, $4$- and $5$-step numbers, where the Fibonacci
$k$-step numbers start $0, 1$ and each later term is the sum of the $k$ terms before it (terms of
negative index being $0$). For every natural number $n \ge 1$,

$$\sum_{j=0}^{n} T_j \bigl(Q_{n-j} - P_{n-j}\bigr) =
\sum_{j=0}^{n-1} \bigl(T_j - Q_j\bigr) P_{n-1-j}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_trib_mul_sub_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-trib-mul-sub-eq).

## Convolution of the $(m-1)$-step and $m$-step Fibonacci numbers against powers of two

Write $F^{(m)}_n$ for the Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each
later term is the sum of the $m$ terms before it, terms at negative indices being $0$). For all
natural numbers $m \ge 2$ and $n \ge 2$,

$$\sum_{j=0}^{n} F^{(m-1)}_j F^{(m)}_{n-j} =
\sum_{j=0}^{n-2} 2^j \bigl(F^{(m-1)}_{n-1-j} - F^{(m)}_{n-2-j}\bigr).$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fibStep_pred_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-step-pred-mul).

## Convolution of the Fibonacci 3-step and 4-step numbers as a sum weighted by powers of 2

Let $T_j$ and $Q_j$ be the Fibonacci $3$-step and $4$-step numbers, where the Fibonacci $k$-step
numbers start $0, 1$ and each later term is the sum of the $k$ terms before it (terms of negative
index being $0$). For every natural number $n$,

$$\sum_{j=0}^{n+2} T_j \, Q_{n+2-j} = \sum_{j=0}^{n} 2^j \bigl(T_{n+1-j} - Q_{n-j}\bigr).$$

This is the case $m = 4$ of the paper's Theorem 12 with $n$ replaced by $n + 2$. The paper prints
$Q_{n-j}$ in place of $Q_{n+2-j}$ on the left; as printed, the identity fails at $n = 0$, where
the left side is $0$ and the right side is $1$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 13.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_trib_mul_tetra_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-trib-mul-tetra-eq).

## Alternating sum of differences of $2m$-step and $(2m-2)$-step Fibonacci numbers

Write
$F^{(m)}_n$ for the Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each later
term is the sum of the $m$ terms before it, terms at negative indices being $0$). For all natural
numbers $m \ge 2$ and $n \ge 2m - 1$,

$$\sum_{j=0}^{n-1} (-1)^j \bigl(F^{(2m)}_j - F^{(2m-2)}_j\bigr) =
(-1)^{n+1} \sum_{j=0}^{n-2m+1} F^{(2m)}_j F^{(2m-2)}_{n-2m+1-j}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 15.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_neg_one_pow_sub_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-neg-one-pow-sub-even).

## Alternating sums of differences of odd-order Fibonacci step numbers

Let $F^{(k)}_j$ be
the $j$-th Fibonacci $k$-step number: the sequence starts $F^{(k)}_0 = 0$, $F^{(k)}_1 = 1$, and each
later term is the sum of the $k$ terms before it (terms of negative index being $0$). For all
natural numbers $m$ and $n$ with $m \ge 1$ and $n \ge 2m$,

$$\sum_{j=0}^{n-1} (-1)^{j+1} \bigl(F^{(2m+1)}_j - F^{(2m-1)}_j\bigr) =
(-1)^n \sum_{j=0}^{n-2m} F^{(2m+1)}_j \, F^{(2m-1)}_{n-2m-j}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 17.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_neg_one_pow_sub_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-neg-one-pow-sub-odd).

## Alternating sum of the tribonacci numbers

Write $T_n$ for the tribonacci numbers (the
Fibonacci $3$-step numbers $F^{(3)}_n$). For every integer $n \ge 0$,
$2 \sum_{j=0}^{n} (-1)^j T_j = (-1)^n (T_{n+1} - T_{n-1}) - 1$, where $T_{n-1}$ is read as
$T_0 = 0$ when $n = 0$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 18.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_sum_neg_one_pow_trib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-sum-neg-one-pow-trib).

## Convolution of the pentanacci and tribonacci numbers, second closed form

Write $P_n$ for
the pentanacci numbers and $T_n$ for the tribonacci numbers (the Fibonacci $m$-step numbers
$F^{(m)}_n$ with $m = 5$ and $m = 3$). For every integer $n \ge 0$,
$2 \sum_{j=0}^{n} P_j T_{n-j} = -P_{n+7} + 2P_{n+6} - P_{n+5} + 2P_{n+4} + P_{n+3} - T_{n+4} +
T_{n+2}$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 18.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_sum_penta_mul_trib'` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-sum-penta-mul-trib-2).

## Convolution of the $m$-step and $(m-2)$-step Fibonacci numbers via Jacobsthal numbers

Write $F^{(m)}_n$ for the Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each
later term is the sum of the $m$ terms before it, terms at negative indices being $0$), and $J_n$
for the Jacobsthal numbers ($J_0 = 0$, $J_1 = 1$, $J_{n+2} = J_{n+1} + 2 J_n$). For all natural
numbers $m \ge 3$ and $n \ge 2$,

$$\sum_{j=0}^{n} F^{(m)}_j F^{(m-2)}_{n-j} =
J_{n-1} + \sum_{j=0}^{n-2} J_j \bigl(F^{(m-2)}_{n-j} - F^{(m)}_{n-2-j}\bigr).$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 19.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fibStep_mul_sub_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-step-mul-sub-two).

## Convolution of the Jacobsthal and tribonacci numbers

Write $J_n$ for the Jacobsthal
numbers ($J_0 = 0$, $J_1 = 1$, $J_{n+2} = J_{n+1} + 2J_n$) and $T_n$ for the tribonacci numbers
(the Fibonacci $3$-step numbers $F^{(3)}_n$). For every integer $n \ge 0$,
$2 \sum_{j=0}^{n} J_j T_{n-j} = 2J_{n+1} + J_{n+2} - T_{n+3} - T_{n+1}$.

The source prints this identity with a factor $1/2$ on part of the right-hand side; it is stated
here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 20.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_sum_jacobsthal_mul_trib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-sum-jacobsthal-mul-trib).

## Triple convolution of Pell numbers with two consecutive Fibonacci step sequences

Write
$P_k$ for the Pell numbers ($P_0 = 0$, $P_1 = 1$, $P_{k+2} = 2P_{k+1} + P_k$), $F^{(s)}_k$ for
the Fibonacci $s$-step numbers, and $\sum_{K(3,N)}$ for a sum over all
$(k_1, k_2, k_3) \in \mathbb{N}^3$ with $k_1 + k_2 + k_3 = N$. For all natural numbers $m \ge 2$
and $n \ge 1$,

$$
\sum_{K(3, n - 1)} P_{k_1} F^{(m-1)}_{k_2} F^{(m)}_{k_3} =
\sum_{j=0}^{n} F^{(m-1)}_j \left(P_{n-j} - F^{(m)}_{n-j}\right) -
\sum_{j=0}^{n-1} P_j F^{(m)}_{n-1-j}.
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 21.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_pell_fibStep` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-pell-fib-step).

## Convolution of the Pell numbers with the Fibonacci numbers

Let $\mathcal{P}_j$ be the
Pell numbers ($\mathcal{P}_0 = 0$, $\mathcal{P}_1 = 1$,
$\mathcal{P}_{j+2} = 2\mathcal{P}_{j+1} + \mathcal{P}_j$) and $F_j$ the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$, $F_{j+2} = F_{j+1} + F_j$), that is, the Fibonacci $2$-step numbers. For
every natural number $n$,

$$\sum_{j=0}^{n} \mathcal{P}_j \, F_{n-j} = \mathcal{P}_n - F_n.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 22.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_pell_mul_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-pell-mul-fib).

## Pell–Fibonacci–tribonacci triple sum via a Pell–tribonacci convolution

Write $P_k$ for
the Pell numbers ($P_0 = 0$, $P_1 = 1$, $P_{k+2} = 2P_{k+1} + P_k$), $F_k$ and $T_k$ for the
Fibonacci $2$- and $3$-step numbers, and $\sum_{K(3,n)}$ for a sum over all
$(k_1, k_2, k_3) \in \mathbb{N}^3$ with $k_1 + k_2 + k_3 = n$. For every natural number $n$,

$$
\sum_{K(3,n)} P_{k_1} F_{k_2} T_{k_3} = P_{n+1} + F_{n+2} - T_{n+3} - \sum_{j=0}^{n} P_j T_{n-j}.
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 23.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_pell_fib_trib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-pell-fib-trib).

## Closed form for the Pell–Fibonacci–tribonacci triple convolution

Write $\mathcal{P}_n$
for the Pell numbers, $F_n$ for the Fibonacci numbers and $T_n$ for the tribonacci numbers (the
Fibonacci $m$-step numbers $F^{(m)}_n$ with $m = 2$ and $m = 3$). For every integer $n \ge 0$,
$2 \sum \mathcal{P}_{k_1} F_{k_2} T_{k_3} = \mathcal{P}_{n+1} - T_{n+3} - T_{n+2} + 2F_{n+2}$,
where the sum runs over all triples $(k_1, k_2, k_3)$ of nonnegative integers with
$k_1 + k_2 + k_3 = n$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 23.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_compProdSum_pell_fib_trib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-comp-prod-sum-pell-fib-trib).

## A product identity for Fibonacci step generating functions of orders $m$, $m+p$, $m+p+q$

**A product identity for Fibonacci step generating functions of orders $m$, $m+p$,
$m+p+q$.** Let $m, p, q \ge 1$ be natural numbers. For each $k$, let
$F^{(k)} = \sum_{n \ge 0} F^{(k)}_n X^n$ in $\mathbb{Q}[[X]]$ be the ordinary generating function
of the Fibonacci $k$-step numbers $F^{(k)}_n$. Then

$$X^{2m+p} (1-X^p)(1-X^q) F^{(m)} F^{(m+p)} F^{(m+p+q)} =
X^m (1-X)(1-X^p) F^{(m)} F^{(m+p+q)} - (1-X)^2 \left(F^{(m+p)} - F^{(m)}\right).$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 24.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStepGF_triple_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-gf-triple-identity).

## A product identity for three consecutive Fibonacci step generating functions

Let
$m \ge 1$ be a natural number. For each $k$, let $F^{(k)} = \sum_{n \ge 0} F^{(k)}_n X^n$ in
$\mathbb{Q}[[X]]$ be the ordinary generating function of the Fibonacci $k$-step numbers
$F^{(k)}_n$. Then

$$X^{2m+1} F^{(m)} F^{(m+1)} F^{(m+2)} = X^m F^{(m)} F^{(m+2)} - F^{(m+1)} + F^{(m)}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 24.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStepGF_triple_consecutive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-gf-triple-consecutive).

## Generating-function form of the triple convolution with two consecutive step sequences

For a natural number $s$ let $F^{(s)}(X) = \sum_{n \ge 0} F^{(s)}_n X^n$ be the ordinary
generating function, with rational coefficients, of the Fibonacci $s$-step numbers
$F^{(s)}_n$. For all natural numbers $m \ge 1$ and $p \ge 1$, the formal power series over
$\mathbb{Q}$ satisfy

$$
X^m F^{(m)}(X) F^{(m+1)}(X) F^{(p)}(X) = F^{(p)}(X) F^{(m+1)}(X) - F^{(p)}(X) F^{(m)}(X).
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 25.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStepGF_mixed_triple` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-gf-mixed-triple).

## Triple convolution of two consecutive Fibonacci step sequences with a third

Write
$F^{(s)}_k$ for the Fibonacci $s$-step numbers, and write $\sum_{K(3,N)}$ for a sum over all
$(k_1, k_2, k_3) \in \mathbb{N}^3$ with $k_1 + k_2 + k_3 = N$. For all natural numbers $m \ge 1$,
$p \ge 1$ and $n \ge m$,

$$
\sum_{K(3, n - m)} F^{(m)}_{k_1} F^{(m+1)}_{k_2} F^{(p)}_{k_3} =
\sum_{j=0}^{n} F^{(p)}_j F^{(m+1)}_{n-j} - \sum_{j=0}^{n} F^{(p)}_j F^{(m)}_{n-j}.
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 25.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_fibStep_triple` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-fib-step-triple).

## Closed form of the Fibonacci–tribonacci–tetranacci triple sum

Write $F_k$, $T_k$ and
$Q_k$ for the Fibonacci $2$-, $3$- and $4$-step numbers, and write $\sum_{K(3,n)}$ for a sum over
all $(k_1, k_2, k_3) \in \mathbb{N}^3$ with $k_1 + k_2 + k_3 = n$. For every natural number $n$,

$$
\sum_{K(3,n)} F_{k_1} T_{k_2} Q_{k_3} = Q_{n+4} + Q_{n+2} - T_{n+5} + F_{n+3}.
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 26.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_fib_trib_tetra` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 513](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L513). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-fib-trib-tetra).

## Triple convolution of the tribonacci, tetranacci and pentanacci numbers

Write $T_n$,
$Q_n$ and $P_n$ for the Fibonacci $m$-step numbers $F^{(m)}_n$ with $m = 3, 4, 5$ respectively.
For every integer $n \ge 7$,
$2 \sum T_{k_1} Q_{k_2} P_{k_3} = P_n + P_{n-2} + P_{n-4} + T_n - T_{n-2} - 2Q_n$, where the sum
runs over all triples $(k_1, k_2, k_3)$ of nonnegative integers with $k_1 + k_2 + k_3 = n - 7$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 27.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_compProdSum_trib_tetra_penta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-comp-prod-sum-trib-tetra-penta).

## Triple convolution of the Fibonacci 2-, 4- and 5-step numbers

Let $F_j$, $Q_j$ and $P_j$
be the Fibonacci $2$-, $4$- and $5$-step numbers, where the Fibonacci $k$-step numbers start
$0, 1$ and each later term is the sum of the $k$ terms before it (terms of negative index being
$0$). For every natural number $n \ge 5$,

$$2 \sum_{k_1 + k_2 + k_3 = n - 5} F_{k_1} Q_{k_2} P_{k_3}
= -2Q_n - 2Q_{n-2} + P_{n+1} + P_{n-2} - F_{n+1} + 2F_n,$$

where the sum runs over all triples $(k_1, k_2, k_3)$ of natural numbers with
$k_1 + k_2 + k_3 = n - 5$.

The paper prints this identity with a factor $\tfrac{1}{2}$ on part of the right side.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 28.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_compProdSum_fib_tetra_penta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 541](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L541). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-comp-prod-sum-fib-tetra-penta).

## Triple convolution of the Fibonacci 2-, 3- and 5-step numbers

Let $F_j$, $T_j$ and $P_j$
be the Fibonacci $2$-, $3$- and $5$-step numbers, where the Fibonacci $k$-step numbers start
$0, 1$ and each later term is the sum of the $k$ terms before it (terms of negative index being
$0$). For every natural number $n \ge 5$,

$$2 \sum_{k_1 + k_2 + k_3 = n - 5} F_{k_1} T_{k_2} P_{k_3} =
P_n - P_{n-1} + P_{n-2} - T_n - T_{n-2} + F_{n-1},$$

where the sum runs over all triples $(k_1, k_2, k_3)$ of natural numbers with
$k_1 + k_2 + k_3 = n - 5$.

The paper prints this identity with a factor $\tfrac{1}{2}$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 29.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_compProdSum_fib_trib_penta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-comp-prod-sum-fib-trib-penta).

## A product identity for four consecutive Fibonacci step generating functions

Let
$m \ge 1$ be a natural number. For each $k$, let $F^{(k)} = \sum_{n \ge 0} F^{(k)}_n X^n$ in
$\mathbb{Q}[[X]]$ be the ordinary generating function of the Fibonacci $k$-step numbers
$F^{(k)}_n$. Then

$$X^{2m+1} F^{(m)} F^{(m+1)} F^{(m+2)} F^{(m+3)} =
X^m F^{(m)} F^{(m+2)} F^{(m+3)} - F^{(m+1)} F^{(m+3)} + F^{(m)} F^{(m+3)}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 31.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.fibStepGF_quadruple_consecutive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 572](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L572). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-step-gf-quadruple-consecutive).

## Four-fold convolution of the Fibonacci, tribonacci, tetranacci and pentanacci numbers

Write $F_n$, $T_n$, $Q_n$ and $P_n$ for the Fibonacci $m$-step numbers $F^{(m)}_n$ with
$m = 2, 3, 4, 5$ respectively. For every integer $n \ge 5$,
$2 \sum F_{k_1} T_{k_2} Q_{k_3} P_{k_4} = P_{n+4} - P_{n+3} + P_{n+2} + T_{n+3} + T_{n+1} -
F_n - 2Q_{n+3} - 2Q_{n+1}$, where the sum runs over all $4$-tuples $(k_1, k_2, k_3, k_4)$ of
nonnegative integers with $k_1 + k_2 + k_3 + k_4 = n - 5$.

The source prints this identity with a factor $1/2$; it is stated here multiplied by $2$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 32.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.two_mul_compProdSum_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#two-mul-comp-prod-sum-four).

## Convolution of four consecutive Fibonacci step sequences

Write $F^{(s)}_k$ for the
Fibonacci $s$-step numbers, and write $\sum_{K(4,N)}$ for a sum over all
$(k_1, k_2, k_3, k_4) \in \mathbb{N}^4$ with $k_1 + k_2 + k_3 + k_4 = N$. For all natural numbers
$m \ge 1$ and $n \ge 2m + 2$,

$$
\sum_{K(4, n - 2m - 2)} F^{(m)}_{k_1} F^{(m+1)}_{k_2} F^{(m+2)}_{k_3} F^{(m+3)}_{k_4} =
\sum_{j=0}^{n} \left(F^{(m+3)}_j - F^{(m+2)}_j\right) \left(F^{(m+1)}_{n-j} - F^{(m)}_{n-j}\right).
$$

The paper prints the index of the last factor on the left as $k_3$; it is corrected to $k_4$
here.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 34.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_four_consecutive` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-four-consecutive).

## Convolution of an even number of consecutive Fibonacci step sequences

Write $F^{(s)}_k$
for the Fibonacci $s$-step numbers, and write $\sum_{K(r,N)}$ for a sum over all
$(k_1, \dots, k_r) \in \mathbb{N}^r$ with $k_1 + \dots + k_r = N$. For all natural numbers
$\ell \ge 1$, $m \ge 1$ and $n \ge \ell(m + \ell - 1)$,

$$
\sum_{K(2\ell, n - \ell(m + \ell - 1))} \prod_{j=0}^{2\ell-1} F^{(m+j)}_{k_{j+1}} =
\sum_{K(\ell, n)} \prod_{j=0}^{\ell-1} \left(F^{(m+2j+1)}_{k_{j+1}} - F^{(m+2j)}_{k_{j+1}}\right).
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 35.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-even).

## Convolution of an odd number of consecutive Fibonacci step sequences

Write $F^{(s)}_k$
for the Fibonacci $s$-step numbers, and write $\sum_{K(r,N)}$ for a sum over all
$(k_1, \dots, k_r) \in \mathbb{N}^r$ with $k_1 + \dots + k_r = N$. For all natural numbers
$\ell \ge 1$, $m \ge 1$ and $n \ge \ell(m + \ell - 1)$,

$$
\sum_{K(2\ell+1, n - \ell(m + \ell - 1))} \prod_{j=0}^{2\ell} F^{(m+j)}_{k_{j+1}} =
\sum_{K(\ell+1, n)} F^{(m+2\ell)}_{k_{\ell+1}} \prod_{j=0}^{\ell-1}
\left(F^{(m+2j+1)}_{k_{j+1}} - F^{(m+2j)}_{k_{j+1}}\right).
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 35.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-odd).

## Two convolution forms of the Fibonacci–tribonacci–tetranacci triple sum

Write $F_k$,
$T_k$ and $Q_k$ for the Fibonacci $2$-, $3$- and $4$-step numbers, and write $\sum_{K(3,N)}$ for
a sum over all $(k_1, k_2, k_3) \in \mathbb{N}^3$ with $k_1 + k_2 + k_3 = N$. For every natural
number $n \ge 2$,

$$
\sum_{K(3, n - 2)} F_{k_1} T_{k_2} Q_{k_3} = \sum_{j=0}^{n} (T_j - F_j) Q_{n-j} =
\sum_{j=0}^{n+1} F_{n+1-j} (Q_j - T_j).
$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Corollary 36.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.compProdSum_fib_trib_tetra_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 654](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L654). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#comp-prod-sum-fib-trib-tetra-eq).

## Sum of $2m + 2$ consecutive Fibonacci $m$-step numbers

Write $F^{(m)}_n$ for the
Fibonacci $m$-step numbers ($F^{(m)}_0 = 0$, $F^{(m)}_1 = 1$, and each later term is the sum of
the $m$ terms before it, terms at negative indices being $0$). For every natural number $m \ge 2$
and every natural number $n$,

$$\sum_{k=0}^{2m+1} F^{(m)}_{n+k} = 4 F^{(m)}_{n+2m}.$$

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Lemma 39.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.sum_fibStep_window` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#sum-fib-step-window).

## Convolution of the Fibonacci $6$-step numbers with the Fibonacci numbers

Write
$s_n = F^{(6)}_n$ for the Fibonacci $6$-step numbers and $F_n = F^{(2)}_n$ for the Fibonacci
numbers. For every natural number $n \ge 3$,

$$5 \sum_{j=0}^{n} s_j F_{n-j} =
s_{n+3} + s_{n+1} - s_n + 3 s_{n-1} + s_{n-3} - F_{n+3} - F_{n+1}.$$

The source prints this identity divided by $5$.

## Sources

- Robert Frontczak and Karol Gryszka, "General Convolution Sums Involving Fibonacci `m`-Step Numbers", Theorem 41.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.FibStepConvolutionWanted.five_mul_sum_fibStep6_mul_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean, line 683](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/FibStepConvolutionWanted.lean#L683). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#five-mul-sum-fib-step6-mul-fib).

## Truncated binomial sum $G_n^{(k)}$

For an integer $x$ and a natural number $j$ let
$\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$. For natural numbers $k$ and $n$, the rational number
$G_n^{(k)}$ is

$$
G_n^{(k)} = 2^{n-2} \sum_{\ell=0}^{m}
\left(\binom{(k+1)\ell - n}{\ell} - \binom{(k+1)\ell - n}{\ell - 1}\right) 2^{-(k+1)\ell},
$$

where $m = \lfloor (n-1)/(k+1) \rfloor$ for $n \ge 1$ and $m = 0$ for $n = 0$, and the term
$\binom{(k+1)\ell - n}{\ell - 1}$ is taken to be $0$ for $\ell = 0$.

The paper defines $G_n^{(k)}$ only for $n, k \ge 2$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, definition before Proposition 10.

Formalized by `MetaMathlibExt.kFibonacciBinomialTruncation`, a definition declared in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-binomial-truncation).

## Value $G_2^{(2)} = 1$

The truncated binomial sum satisfies $G_2^{(2)} = 1$.

This is the Fibonacci number $F_2$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, definition before Proposition 10.

Formalized by `MetaMathlibExt.kFibonacciBinomialTruncation_two_two`, a theorem declared in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-binomial-truncation-two-two).

## Value $G_4^{(2)} = 3$

The truncated binomial sum satisfies $G_4^{(2)} = 3$.

This is the Fibonacci number $F_4$, and $n = 4$ is the first index for which the sum defining
$G_n^{(2)}$ has two terms.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, definition before Proposition 10.

Formalized by `MetaMathlibExt.kFibonacciBinomialTruncation_two_four`, a theorem declared in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-binomial-truncation-two-four).

## Lagrange inversion formula

Let $f, g : \mathbb{C} \to \mathbb{C}$ be analytic at $z_0$.
There are $\varepsilon > 0$ and $\delta > 0$ such that for every $\alpha \in \mathbb{C}$ with
$|\alpha| < \delta$ the equation $w = z_0 + \alpha f(w)$ has exactly one solution $w$ with
$|w - z_0| < \varepsilon$, and for this solution the series
$\sum_{n \ge 1} \frac{\alpha^n}{n!} \frac{d^{n-1}}{dz^{n-1}} \bigl(f(z)^n g'(z)\bigr)\big|_{z=z_0}$
converges absolutely to $g(w) - g(z_0)$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Theorem 1 (`jis-2024-24.1.1-thm-1`).

Stated but not proved: `MetaMathlibExt.lagrange_inversion_formula_analytic` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#lagrange-inversion-formula-analytic).

## Binomial series for the powers of the dominant $k$-Fibonacci root

Let $k \ge 2$ and let
$\rho_k > 0$ be a real number with $\rho_k^k = 1 + \rho_k + \dots + \rho_k^{k-1}$. For integers $a$
and $j \ge 0$ write $\binom{a}{j} = a(a-1)\cdots(a-j+1)/j!$. Then for every $n \ge 1$ the series
$S = \sum_{\ell \ge 0} \frac{1}{\ell+1} \binom{k(\ell+1)+\ell-n}{\ell} 2^{-(k+1)\ell}$ converges
absolutely and $\rho_k^n = 2^n - n\, 2^{n-k-1} S$.

For $n = 1$ this is the paper's series for $\rho_k$ itself.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Theorem 3 (`jis-2024-24.1.1-thm-3`).

Stated but not proved: `MetaMathlibExt.kFibonacci_root_pow_eq_binomial_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-root-pow-eq-binomial-series).

## Binomial series for the powers of the golden ratio

Let $\varphi = (1 + \sqrt{5})/2$ be
the golden ratio, and for an integer $x$ and a natural number $j$ let
$\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$. For every natural number $n \ge 1$ the series
$S_n = \sum_{\ell \ge 0} \frac{1}{\ell + 1} \binom{3\ell + 2 - n}{\ell} 2^{-3\ell}$ converges
absolutely and $\varphi^n = 2^n - n \, 2^{n-3} S_n$. Moreover, the series
$\sum_{\ell \ge 0} \frac{1}{\ell + 1} \binom{3\ell + 1}{\ell} 2^{-(3\ell + 2)}$ converges
absolutely to $2 - \varphi$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Corollary 5 (`jis-2024-24.1.1-cor-5`).

Stated but not proved: `MetaMathlibExt.goldenRatio_pow_eq_binomial_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#golden-ratio-pow-eq-binomial-series).

## Binomial series summed at the $k$-Fibonacci root

Let $k \ge 2$ be a natural number and
$\rho > 0$ a real number with $\rho^k = 1 + \rho + \cdots + \rho^{k-1}$, and for an integer $x$
and a natural number $j$ let $\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$. Then for every integer
$a$ the series below converges absolutely and

$$
\sum_{\ell \ge 0} \binom{(k+1)\ell + a}{\ell} 2^{-(k+1)\ell} =
\frac{2^{a+1} \rho^{-a}}{(k+1)\rho - 2k}.
$$

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Theorem 6 (`jis-2024-24.1.1-thm-6`).

Stated but not proved: `MetaMathlibExt.hasSum_choose_div_two_pow_kFibonacci_root` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#has-sum-choose-div-two-pow-k-fibonacci-r).

## Difference binomial series at the $k$-Fibonacci root

Let $k \ge 2$ be a natural number
and $\rho > 0$ a real number with $\rho^k = 1 + \rho + \cdots + \rho^{k-1}$, and for an integer
$x$ and a natural number $j$ let $\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$. For every natural number
$n \ne 1$ the series below converges absolutely and

$$
2^{n-2} \sum_{\ell \ge 0} \left(\binom{(k+1)\ell - n}{\ell} - \binom{(k+1)\ell - n}{\ell - 1}\right)
2^{-(k+1)\ell} = \frac{\rho - 1}{(k+1)\rho - 2k} \rho^{n-1},
$$

where the term $\binom{(k+1)\ell - n}{\ell - 1}$ is taken to be $0$ for $\ell = 0$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Theorem 8 (`jis-2024-24.1.1-thm-8`), with `As_n^{(k)}` from equation (8).

Stated but not proved: `MetaMathlibExt.hasSum_binomial_series_kFibonacci_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#has-sum-binomial-series-k-fibonacci-asym).

## $k$-Fibonacci numbers as truncated binomial sums

Let $k \ge 2$ and let
$(F_n)_{n \ge 0}$ be the $k$-Fibonacci sequence, given by $F_0 = \dots = F_{k-2} = 0$,
$F_{k-1} = 1$ and $F_{m+k} = F_m + F_{m+1} + \dots + F_{m+k-1}$ for all $m \ge 0$. For integers
$a$ and $j \ge 0$ write $\binom{a}{j} = a(a-1)\cdots(a-j+1)/j!$, and put $\binom{a}{-1} = 0$.
For $n \ge 2$ let $G_n^{(k)}$ be the truncated binomial sum
$G_n^{(k)} = 2^{n-2} \sum_{\ell=0}^{\lfloor (n-1)/(k+1) \rfloor} \left(\binom{(k+1)\ell-n}{\ell} -
\binom{(k+1)\ell-n}{\ell-1}\right) 2^{-(k+1)\ell}$. Then $F_{n+k-2} = G_n^{(k)}$ for every
$n \ge 2$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Theorem 9 (`jis-2024-24.1.1-thm-9`).

Stated but not proved: `MetaMathlibExt.kFibonacci_eq_kFibonacciBinomialTruncation` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-eq-k-fibonacci-binomial-trun).

## Initial values of the truncated binomial sums

Let $k \ge 2$ be a natural number and let
$G_n^{(k)}$ be the truncated binomial sum. Then $G_n^{(k)} = 2^{n-2}$ for every natural number $n$
with $2 \le n \le k + 1$, and $G_{k+2}^{(k)} = 2^k - 1$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Proposition 10 (`jis-2024-24.1.1-prop-10`).

Stated but not proved: `MetaMathlibExt.kFibonacciBinomialTruncation_initial_values` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-binomial-truncation-initial).

## Recurrence for the truncated binomial sums

Let $G_n^{(k)}$ be the truncated binomial
sum. For all natural numbers $k \ge 2$ and $n \ge 2$,
$G_{n+k+1}^{(k)} = 2 G_{n+k}^{(k)} - G_n^{(k)}$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Proposition 11 (`jis-2024-24.1.1-prop-11`).

Stated but not proved: `MetaMathlibExt.kFibonacciBinomialTruncation_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-binomial-truncation-recurren).

## Binomial-sum formula for the $k$-Fibonacci numbers

Let $k \ge 2$ and let
$(F_n)_{n \ge 0}$ be the $k$-Fibonacci sequence, given by $F_0 = \dots = F_{k-2} = 0$,
$F_{k-1} = 1$ and $F_{m+k} = F_m + F_{m+1} + \dots + F_{m+k-1}$ for all $m \ge 0$. For integers
$a$ and $j \ge 0$ write $\binom{a}{j} = a(a-1)\cdots(a-j+1)/j!$, and put $\binom{a}{-1} = 0$.
Then for every $n \ge k$,

$$F_n = 2^{n-k} \sum_{\ell=0}^{\lfloor (n-k+1)/(k+1) \rfloor} \left(\binom{(k+1)\ell+k-n-2}{\ell} -
\binom{(k+1)\ell+k-n-2}{\ell-1}\right) 2^{-(k+1)\ell}.$$

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Corollary 12 (`jis-2024-24.1.1-cor-12`).

Stated but not proved: `MetaMathlibExt.kFibonacci_eq_binomial_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-eq-binomial-sum).

## Fibonacci numbers as a truncated binomial sum

Let $F_n$ be the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$), and for an integer $x$ and a natural number
$j$ let $\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$. For every natural number $n \ge 2$,

$$
F_n = 2^{n-2} \sum_{\ell=0}^{\lfloor (n-1)/3 \rfloor}
\left(\binom{3\ell - n}{\ell} - \binom{3\ell - n}{\ell - 1}\right) 2^{-3\ell},
$$

where the term $\binom{3\ell - n}{\ell - 1}$ is taken to be $0$ for $\ell = 0$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Corollary 13 (`jis-2024-24.1.1-cor-13`).

Stated but not proved: `MetaMathlibExt.fib_eq_binomial_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#fib-eq-binomial-sum).

## Alternating binomial formula for the $k$-Fibonacci numbers

Let $k \ge 2$ be a natural
number and let $F_n^{(k)}$ be the $k$-Fibonacci numbers: $F_i^{(k)} = 0$ for $i < k - 1$,
$F_{k-1}^{(k)} = 1$ and $F_{m+k}^{(k)} = F_m^{(k)} + F_{m+1}^{(k)} + \cdots + F_{m+k-1}^{(k)}$ for
every $m \ge 0$. For an integer $x$ and a natural number $j$ let
$\binom{x}{j} = x(x-1)\cdots(x-j+1)/j!$. Then for every natural number $n \ge k$,

$$
F_n^{(k)} = 2^{n-k} + \sum_{\ell=1}^{\lfloor (n-k+1)/(k+1) \rfloor} (-1)^\ell
\left(\binom{n - (\ell+1)k + 2}{\ell} - \binom{n - (\ell+1)k}{\ell - 2}\right)
2^{n - (k+1)\ell - k},
$$

where the term $\binom{n - (\ell+1)k}{\ell - 2}$ is taken to be $0$ for $\ell = 1$.

The paper assumes $n \ne 2k - 1$; for $n = 2k - 1$ the sum is empty and both sides equal
$2^{k-1}$.

## Sources

- Bakir Farhi, *Some Applications of the Lagrange Inversion Formula for the k-Fibonacci Numbers*, Journal of Integer Sequences 27 (2024), Article 24.1.1, Corollary 14 (`jis-2024-24.1.1-cor-14`).

Stated but not proved: `MetaMathlibExt.kFibonacci_eq_alternating_binomial_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/KFibonacciLagrangeInversionWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html#k-fibonacci-eq-alternating-binomial-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: k-generalized Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/k-generalized-fibonacci-numbers)
