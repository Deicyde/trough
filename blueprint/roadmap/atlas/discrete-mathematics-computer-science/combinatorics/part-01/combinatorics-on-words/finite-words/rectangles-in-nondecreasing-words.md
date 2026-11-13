---
declaration: section
origin: cited
lean: MetaMathlibExt.rectangleCapacity, MetaMathlibExt.rectangleCapacity_example, MetaMathlibExt.nondecreasingRectangleTotal, MetaMathlibExt.nondecreasingRectangleTotal_two_one_two_two, MetaMathlibExt.nondecreasingRectangleTotal_one_by_s, MetaMathlibExt.nondecreasingRectangleTotal_r_by_s
statement: formalized
---

# Rectangles in nondecreasing words

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html).

## Number of $r \times s$ rectangles in a bargraph

Let $w = w_0 w_1 \cdots w_{m-1}$ be a word
of natural numbers, drawn as a bargraph whose column $i$ has height $w_i$. The number of
occurrences of an $r \times s$ rectangle (height $r$, width $s$) in $w$ is the number of pairs
$(i, y)$ of natural numbers with $i < m$, $i + s \le m$ and $y \le w_0 + \cdots + w_{m-1}$ such
that $y + r \le w_{i+j}$ for every $j < s$.

Here $(i, y)$ is the rectangle whose lower left cell is in column $i$ and row $y$, both counted
from $0$. For $s \ge 1$ the conditions $i < m$ and $y \le w_0 + \cdots + w_{m-1}$ follow from the
others; for $s = 0$ the count is $m(w_0 + \cdots + w_{m-1} + 1)$.

## Sources

- Sela Fried and Toufik Mansour, *Counting Rectangles of Size r × s in Nondecreasing and Smirnov Words*, Journal of Integer Sequences 27 (2024), Article 24.8.4, Introduction and Figure 2.

Formalized by `MetaMathlibExt.rectangleCapacity`, a definition declared in [WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html#rectangle-capacity).

## Example: $3 \times 2$ rectangles in the word $345134$

The bargraph of the word $345134$
contains exactly four rectangles of height $3$ and width $2$.

## Sources

- Sela Fried and Toufik Mansour, *Counting Rectangles of Size r × s in Nondecreasing and Smirnov Words*, Journal of Integer Sequences 27 (2024), Article 24.8.4, Figure 2.

Formalized by `MetaMathlibExt.rectangleCapacity_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html#rectangle-capacity-example).

## Total number of $r \times s$ rectangles in nondecreasing words

For natural numbers $k$,
$r$, $s$ and $n$, this is the sum, over all nondecreasing words $w_1 \le w_2 \le \cdots \le w_n$ of
length $n$ over the alphabet $[k] = \{1, \dots, k\}$ (the set $W^{\nearrow}_{n,k}$), of the number
of $r \times s$ rectangles in the bargraph of $w$.

## Sources

- Sela Fried and Toufik Mansour, *Counting Rectangles of Size r × s in Nondecreasing and Smirnov Words*, Journal of Integer Sequences 27 (2024), Article 24.8.4, Corollaries 2 and 6.

Formalized by `MetaMathlibExt.nondecreasingRectangleTotal`, a definition declared in [WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html#nondecreasing-rectangle-total).

## Example: $1 \times 2$ rectangles in nondecreasing words of length $2$

The nondecreasing
words of length $2$ over $[2] = \{1, 2\}$ are $11$, $12$ and $22$, which contain $1$, $1$ and $2$
rectangles of size $1 \times 2$ respectively, so the total number of $1 \times 2$ rectangles over
all nondecreasing words of length $2$ over $[2]$ is $4$.

## Sources

- Sela Fried and Toufik Mansour, *Counting Rectangles of Size r × s in Nondecreasing and Smirnov Words*, Journal of Integer Sequences 27 (2024), Article 24.8.4, Corollary 2.

Formalized by `MetaMathlibExt.nondecreasingRectangleTotal_two_one_two_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html#nondecreasing-rectangle-total-two-one-tw).

## Generating function for $1 \times s$ rectangles in nondecreasing words

Let $k \ge 1$ and
$s \ge 1$, and let $f_k(n)$ be the total number of $1 \times s$ rectangles over all nondecreasing
words of length $n$ over $[k] = \{1, \dots, k\}$. Then, as formal power series over $\mathbb{Z}$,

$$
\Big(\sum_{n \ge 0} f_k(n)\, x^n\Big) (1 - x)^{k+1} =
x^s \sum_{i=0}^{k-1} (-1)^i \binom{i+s-2}{i} \binom{k+s}{s+i+1} x^i,
$$

and for every $n \ge s$,

$$
f_k(n) = \sum_{i=0}^{\min(k-1,\, n-s)} (-1)^i \binom{i+s-2}{i} \binom{k+s}{s+i+1}
\binom{n-s-i+k}{k}.
$$

For $s = 1$ the factor $\binom{i+s-2}{i} = \binom{i-1}{i}$ is $1$ at $i = 0$ and $0$ for $i \ge 1$.

## Sources

- Sela Fried and Toufik Mansour, *Counting Rectangles of Size r × s in Nondecreasing and Smirnov Words*, Journal of Integer Sequences 27 (2024), Article 24.8.4, Corollary 2 (`jis-2024-24.8.4-cor-2`).

Stated but not proved: `MetaMathlibExt.nondecreasingRectangleTotal_one_by_s` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html#nondecreasing-rectangle-total-one-by-s).

## Generating function for $r \times s$ rectangles in nondecreasing words

Let $k \ge 1$,
$r \ge 1$ and $s \ge 1$, let $g_k(n)$ be the total number of $r \times s$ rectangles over all
nondecreasing words of length $n$ over $[k] = \{1, \dots, k\}$, and let $m = \max(k + 1 - r, 0)$.
Then, as formal power series over $\mathbb{Z}$,

$$
\Big(\sum_{n \ge 0} g_k(n)\, x^n\Big) (1 - x)^{k+1} =
x^s \sum_{0 \le i \le k+1-r} (-1)^i \binom{i+s-2}{i} \binom{m+s}{s+i+1} x^i,
$$

where the sum is empty when $r \ge k + 2$, and for every $n \ge s$,

$$
g_k(n) = \sum_{i=0}^{\min(m,\, n-s)} (-1)^i \binom{i+s-2}{i} \binom{m+s}{s+i+1}
\binom{n-s-i+k}{k}.
$$

For $s = 1$ the factor $\binom{i+s-2}{i} = \binom{i-1}{i}$ is $1$ at $i = 0$ and $0$ for $i \ge 1$.

## Sources

- Sela Fried and Toufik Mansour, *Counting Rectangles of Size r × s in Nondecreasing and Smirnov Words*, Journal of Integer Sequences 27 (2024), Article 24.8.4, Corollary 6 (`jis-2024-24.8.4-cor-6`).

Stated but not proved: `MetaMathlibExt.nondecreasingRectangleTotal_r_by_s` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RectangleCapacityNondecreasingWordsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html#nondecreasing-rectangle-total-r-by-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rectangles in nondecreasing words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/rectangles-in-nondecreasing-words)
