---
declaration: section
origin: cited
lean: MetaMathlibExt.catalan_transform_pair, MetaMathlibExt.IsCFiniteSequence, MetaMathlibExt.hadamard_fibonacci_product, MetaMathlibExt.generating_function_term_extraction
statement: formalized
proof: formalized
---

# Sequence transforms and generating functions: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/index.html).

Operators on integer sequences and coefficient extraction: binomial, multiple and falling k-binomial transforms, INVERT and Catalan transforms, hypersequences, convolutions, C-finite sequences, and recovering terms from generating-function values.

## Barry's Catalan transform and its inverse

Let $a, b \colon \mathbb{N} \to \mathbb{Q}$ be
sequences such that, for every $n \ge 0$,

$$b_n = \sum_{j=0}^{n} \sum_{k=0}^{n} \frac{2k+1}{n+k+1} (-1)^{k-j}
\binom{2n}{n-k} \binom{k}{j} a_j.$$

Then for every $n \ge 1$ both

$$b_n = \sum_{k=0}^{n} \frac{k}{2n-k} \binom{2n-k}{n-k} a_k$$

and

$$b_n = \sum_{k=0}^{n} \frac{k}{n} \binom{2n-k-1}{n-k} a_k$$

hold, and for every $n \ge 0$ both

$$a_n = \sum_{k=0}^{\lfloor n/2 \rfloor} (-1)^k \binom{n-k}{k} b_{n-k}$$

and

$$a_n = \sum_{k=0}^{n} (-1)^{n-k} \binom{k}{n-k} b_k$$

hold.

In the hypothesis, the terms with $j > k$ vanish because $\binom{k}{j} = 0$ there.

## Sources

- Paul Barry, "A Catalan Transform and Related Transformations on Integer Sequences", Journal of Integer Sequences 8 (2005), Article 05.4.5, proposition lines 302--311, <https://cs.uwaterloo.ca/journals/JIS/VOL8/Barry/barry84.tex>.

Formalized by `MetaMathlibExt.catalan_transform_pair`, a theorem declared in [MathlibExt/Combinatorics/CatalanTransformPair.lean, line 777](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/CatalanTransformPair.lean#L777). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/index.html#catalan-transform-pair).

## C-finite polynomial sequences

Let $\sigma$ be a type indexing variables, and write
$\mathbb{Z}[\sigma]$ for the multivariate polynomials with integer coefficients in the variables
$\sigma$. A sequence $a_0, a_1, a_2, \dots$ in $\mathbb{Z}[\sigma]$ is C-finite when there exist
natural numbers $k$ and $N$ and polynomials $p_1, \dots, p_k \in \mathbb{Z}[\sigma]$ such that
for every $n \ge N$

$$
a_{n+k+1} = \sum_{i=1}^{k} p_i \, a_{n+i}.
$$

Formalized by `MetaMathlibExt.IsCFiniteSequence`, a definition declared in [MathlibExt/Combinatorics/Enumerative/CFiniteSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CFiniteSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/index.html#is-cfinite-sequence).

## Hadamard product of two Fibonacci-type series

Let $R$ be a commutative ring, let
$a, b \in R$, and let $n \ge 2$ be a natural number. For each $k$, let $f_k$ be the coefficient of
$x^k$ in $1/(1 - ax - x^2)$ and $g_k$ the coefficient of $x^k$ in $1/(1 - bx - x^n)$, the
inverses taken in $R[[x]]$. Then the Hadamard product $\sum_{k \ge 0} f_k g_k x^k$ equals

$$
\frac{1 - f_{n-2}\, x^n}{1 - ab\, x - b^2 x^2 - (f_n + f_{n-2})\, x^n -
(2b f_{n-1} - ab f_{n-2})\, x^{n+1} + (-1)^n x^{2n}}
$$

in $R[[x]]$, where the denominator has constant coefficient $1$ and so is invertible.

## Sources

- Jong Hyun Kim, "Hadamard Products and Tilings", Journal of Integer Sequences 12 (2009), Article 09.7.4, Theorem `eq:61`, lines 430-437, <https://cs.uwaterloo.ca/journals/JIS/VOL12/Kim/kim18.tex>.

Formalized by `MetaMathlibExt.hadamard_fibonacci_product`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/HadamardFibonacciProduct.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/PowerSeries/HadamardFibonacciProduct.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/index.html#hadamard-fibonacci-product).

## Recovering a sequence term from its generating function

Let $t_0, t_1, t_2, \dots$ be
natural numbers and let $c$, $m$, $N$ be natural numbers with $c \ge 2$ and $2 \le m \le N$.
Suppose that the real series $\sum_{k \ge 0} t_k \, (c^{-N})^k$ is summable and that
$t_j < c^{j-2}$ for every $j \ge m$. Then

$$t_N = \Bigl\lfloor c^{N^2} \sum_{k \ge 0} t_k \, (c^{-N})^k \Bigr\rfloor \bmod c^N.$$

## Sources

- M. Prunescu and J. M. Shunia, "On Modular Representations of C-Recursive Integer Sequences", Journal of Integer Sequences 28 (2025), Article 25.5.3, Theorem `ThmExtraction1`, source lines 169–173, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Prunescu/prunescu3.tex>. The paper attributes the result to Prunescu and Sauras-Altuzarra. Only the first representation (for `N ≥ m ≥ 2` with `t j < c ^ (j - 2)`) is recorded, not the `c ≥ 8` variant for all `n ≥ 1`.

Formalized by `MetaMathlibExt.generating_function_term_extraction`, a theorem declared in [MathlibExt/Combinatorics/Sequences/GeneratingFunctionTermExtraction.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Sequences/GeneratingFunctionTermExtraction.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/index.html#generating-function-term-extraction).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sequence transforms and generating functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/sequence-transforms)
