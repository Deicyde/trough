---
declaration: section
origin: cited
lean: MetaMathlibExt.sum_choose_mul_fib_odd_eq_choose_add_sum, MetaMathlibExt.fib_two_mul_eq_sum_sum_choose_mul_fib_odd, MetaMathlibExt.wordCapacity, MetaMathlibExt.wordArea, MetaMathlibExt.wordCapacity_figure_one, MetaMathlibExt.catalanWords, MetaMathlibExt.smoothWords, MetaMathlibExt.mem_catalanWords_iff
statement: formalized
---

# Capacity of Catalan words

62 results, 31 proved and 31 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html).

## A recursion for binomial sums of odd-indexed Fibonacci numbers

Let $F_k$ be the Fibonacci
numbers, with the convention $F_{-1} = 1$. For all integers $n \ge 1$ and $2 \le i \le n + 1$,

$$\sum_{m=0}^{n-i+1} \binom{n-m-1}{i-2} F_{2m-1} =
\binom{n-1}{i-2} + \sum_{j=i}^{n} \sum_{m=0}^{n-j} \binom{n-m-2}{j-2} F_{2m-1}$$

(Mansour and Shattuck's Lemma 5, identity (21)). All differences in the binomial coefficients and
in the summation bounds are nonnegative.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 5.

Stated but not proved: `MetaMathlibExt.sum_choose_mul_fib_odd_eq_choose_add_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#sum-choose-mul-fib-odd-eq-choose-add-sum).

## A double-sum identity for even-indexed Fibonacci numbers

Let $F_k$ be the Fibonacci
numbers, with $F_0 = 0$, $F_1 = 1$ and $F_{k+2} = F_{k+1} + F_k$, and set $F_{-1} = 1$. For every
natural number $n \ge 1$,

$$F_{2n} = \sum_{j=1}^{n} \sum_{m=0}^{n-j} \binom{n-m-1}{j-1} F_{2m-1}.$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 5.

Stated but not proved: `MetaMathlibExt.fib_two_mul_eq_sum_sum_choose_mul_fib_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#fib-two-mul-eq-sum-sum-choose-mul-fib-od).

## Capacity of a word

The capacity of a word $w = w_1 \cdots w_n$ of natural numbers,
viewed as a bargraph, is

$$\mathrm{cap}(w) = \sum_{i=1}^{n}
\max\Bigl(0, \min\bigl(\max_{j < i} w_j, \max_{j > i} w_j\bigr) - w_i\Bigr),$$

the number of cells of water held above the columns, where an empty maximum is $0$. In particular
the first and last columns hold no water.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, definition of capacity.

Formalized by `MetaMathlibExt.wordCapacity`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#word-capacity).

## Area of a word

The area of a word $w = w_1 \cdots w_n$ of natural numbers is the sum
$w_1 + \cdots + w_n$ of its letters, the area of its bargraph.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of the area statistic.

Formalized by `MetaMathlibExt.wordArea`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#word-area).

## Capacity of the word $122341123212323$

The word
$w = 1\,2\,2\,3\,4\,1\,1\,2\,3\,2\,1\,2\,3\,2\,3$ of length $15$ has capacity $10$ (Mansour and
Shattuck's Figure 1).

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, Figure 1.

Formalized by `MetaMathlibExt.wordCapacity_figure_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#word-capacity-figure-one).

## Catalan words

For a natural number $n$, the set $\mathcal{A}_n$ of Catalan words of length
$n$ consists of the words $w = w_1 w_2 \cdots w_n$ of positive integers with $w_1 = 1$ and
$w_{i+1} \le w_i + 1$ for $1 \le i < n$; for $n = 0$ it contains only the empty word.

Every letter of a Catalan word of length $n$ is at most $n$, so $\mathcal{A}_n$ is finite.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, definition of Catalan words.

Formalized by `MetaMathlibExt.catalanWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-words).

## Smooth words

For $n \ge 0$, the set $\mathcal{R}_n$ of smooth words of length $n$ consists
of the words $w = w_1 \cdots w_n$ of positive integers with $w_1 = 1$ (when $n \ge 1$) and
$|w_{i+1} - w_i| \le 1$ for $1 \le i < n$.

The letters of a smooth word of length $n$ are at most $n$, so $\mathcal{R}_n$ is finite.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, definition of smooth words.

Formalized by `MetaMathlibExt.smoothWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-words).

## Characterization of Catalan words

For a natural number $n$, let $\mathcal{A}_n$ be the
set of Catalan words of length $n$, defined as the words $w = w_1 \cdots w_n$ with letters in
$\{1, \dots, n\}$ such that $w_1 = 1$ when $n \ge 1$ and $w_{k+1} \le w_k + 1$ for $1 \le k < n$.
A word $w = w_1 \cdots w_n$ of natural numbers belongs to $\mathcal{A}_n$ if and only if
$w_k \ge 1$ for every $k$, $w_1 = 1$ when $n \ge 1$, and $w_{k+1} \le w_k + 1$ for $1 \le k < n$.
In particular, the bound $w_k \le n$ on the letters is automatic.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, definition of Catalan words.

Formalized by `MetaMathlibExt.mem_catalanWords_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#mem-catalan-words-iff).

## Characterization of smooth words

For a natural number $n$, let $\mathcal{R}_n$ be the
set of smooth words of length $n$, defined as the words $w = w_1 \cdots w_n$ with letters in
$\{1, \dots, n\}$ such that $w_1 = 1$ when $n \ge 1$, and $w_{k+1} \le w_k + 1$ and
$w_k \le w_{k+1} + 1$ for $1 \le k < n$. A word $w = w_1 \cdots w_n$ of natural numbers belongs
to $\mathcal{R}_n$ if and only if $w_k \ge 1$ for every $k$, $w_1 = 1$ when $n \ge 1$, and
$w_{k+1} \le w_k + 1$ and $w_k \le w_{k+1} + 1$ for $1 \le k < n$. In particular, the bound
$w_k \le n$ on the letters is automatic.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, definition of smooth words.

Formalized by `MetaMathlibExt.mem_smoothWords_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#mem-smooth-words-iff).

## Restricted smooth words

For $n \ge 0$, the set $\mathcal{R}^{\ast}_n$ of restricted smooth
words of length $n$ consists of the smooth words of length $n$ in which no two adjacent letters
are both equal to $1$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 4, definition of restricted smooth words.

Formalized by `MetaMathlibExt.restrictedSmoothWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-words).

## Words ending in a given letter

Given a finite set $S$ of words $w = w_1 \cdots w_n$
of length $n$ with letters in $\mathbb{N}$ and a natural number $k$, this is the set of words
in $S$ whose last letter $w_n$ is $k$. When $n = 0$ this set is empty.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `𝒜_{n,i}`.

Formalized by `MetaMathlibExt.wordsEndingIn`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#words-ending-in).

## Words with all letters at most a bound

Given a finite set $S$ of words of length $n$
with letters in $\mathbb{N}$ and a natural number $k$, this is the set of words in $S$ all of
whose letters are at most $k$. Applied to the words of $S$ whose last letter is $k$, it gives
those whose largest letter is $k$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `ℬ_{n,i}`.

Formalized by `MetaMathlibExt.wordsBoundedBy`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#words-bounded-by).

## Capacity distribution

For a finite set $S$ of words of length $n$ with letters in the
natural numbers, the capacity distribution of $S$ is the polynomial
$\sum_{w \in S} q^{\operatorname{cap}(w)}$ in $\mathbb{Z}[q]$, where $\operatorname{cap}(w)$ is the
capacity of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `a(n, i; q)`.

Formalized by `MetaMathlibExt.capacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#capacity-dist).

## Area distribution

For a finite set $S$ of words of length $n$ with letters in the
natural numbers, the area distribution of $S$ is the polynomial
$\sum_{w \in S} q^{\operatorname{area}(w)}$ in $\mathbb{Z}[q]$, where the area of a word is the
sum of its letters.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `c(m, j, ℓ; q)`.

Formalized by `MetaMathlibExt.areaDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#area-dist).

## Capacity distribution of Catalan words with a given last letter

For natural numbers $n$
and $i$, $a(n, i; q) \in \mathbb{Z}[q]$ is the capacity distribution of the Catalan words of
length $n$ whose last letter is $i$: the sum of $q^{\mathrm{cap}(w)}$ over all such words $w$,
where $\mathrm{cap}(w)$ is the capacity of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `a(n, i; q)`.

Formalized by `MetaMathlibExt.catalanCapacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-capacity-dist).

## Capacity distribution of Catalan words ending in their largest letter

For natural
numbers $n$ and $i$, $b(n, i; q) \in \mathbb{Z}[q]$ is the sum of $q^{\mathrm{cap}(w)}$, where
$\mathrm{cap}(w)$ is the capacity of $w$, over the Catalan words $w$ of length $n$ whose last
letter is $i$ and all of whose letters are at most $i$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `b(n, i; q)`.

Formalized by `MetaMathlibExt.catalanMaxEndCapacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-max-end-capacity-dist).

## Capacity distribution of smooth words by last letter

For $n, i \ge 0$, $r(n, i; q)$ is the
polynomial $\sum_w q^{\operatorname{cap}(w)} \in \mathbb{Z}[q]$, where $w$ runs over the smooth
words of length $n$ whose last letter is $i$ and $\operatorname{cap}(w)$ is the capacity of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 3, definition of `r(n, i; q)`.

Formalized by `MetaMathlibExt.smoothCapacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-capacity-dist).

## Capacity distribution of smooth words ending in their largest letter

For $n, i \ge 0$,
$s(n, i; q)$ is the polynomial $\sum_w q^{\operatorname{cap}(w)} \in \mathbb{Z}[q]$, where $w$ runs
over the smooth words of length $n$ whose last letter is $i$ and all of whose letters are at most
$i$, and $\operatorname{cap}(w)$ is the capacity of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 3, definition of `s(n, i; q)`.

Formalized by `MetaMathlibExt.smoothMaxEndCapacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-max-end-capacity-dist).

## Capacity distribution of restricted smooth words with a given last letter

For natural
numbers $n$ and $i$, $r^*(n, i; q)$ is the polynomial $\sum_w q^{\mathrm{cap}(w)}$ in
$\mathbb{Z}[q]$, where $w$ ranges over the restricted smooth words of length $n$ (smooth words
with no two adjacent letters equal to $1$) whose last letter is $i$, and $\mathrm{cap}(w)$ is the
capacity of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 4, definition of `r*(n, i; q)`.

Formalized by `MetaMathlibExt.restrictedSmoothCapacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-capacity-dist).

## Capacity distribution of restricted smooth words ending in their largest letter

For
natural numbers $n$ and $i$, $s^*(n, i; q)$ is the polynomial $\sum_w q^{\mathrm{cap}(w)}$ in
$\mathbb{Z}[q]$, where $w$ ranges over the restricted smooth words of length $n$ (smooth words
with no two adjacent letters equal to $1$) whose last letter is $i$ and all of whose letters are
at most $i$, and $\mathrm{cap}(w)$ is the capacity of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 4, definition of `s*(n, i; q)`.

Formalized by `MetaMathlibExt.restrictedSmoothMaxEndCapacityDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-max-end-capacity-dist).

## Words with unit-bounded rises ending in their maximum

For natural numbers $m$ and $j$,
$\mathcal{C}_{m,j}$ is the set of words $w = w_1 \cdots w_m$ of length $m$ with letters in
$\{1, \dots, j\}$ such that $w_{k+1} \le w_k + 1$ for $1 \le k < m$ and whose last letter $w_m$
is $j$. It is empty when $m = 0$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `𝒞_{m,j}`.

Formalized by `MetaMathlibExt.catalanGrowthWords`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-growth-words).

## Area distribution of words with unit-bounded rises, by first letter

For natural numbers
$m$, $j$ and $\ell$, let $\mathcal{C}_{m,j}$ be the set of words of length $m$ with letters in
$\{1, \dots, j\}$, each letter at most one more than the letter before it, and last letter $j$.
Then $c(m, j, \ell; q) \in \mathbb{Z}[q]$ is the area distribution of the words in
$\mathcal{C}_{m,j}$ whose first letter is $\ell$: the sum of $q^{\mathrm{area}(w)}$ over these
words $w$, where $\mathrm{area}(w)$ is the sum of the letters of $w$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `c(m, j, ℓ; q)`.

Formalized by `MetaMathlibExt.catalanGrowthAreaDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-growth-area-dist).

## Area distribution of smooth words from $j$ to $j$

For natural numbers $m$ and $j$, let
$\mathcal{T}_{m,j}$ be the set of words $w = w_1 \cdots w_m$ with letters in $\{1, \dots, j\}$
such that $w_1 = w_m = j$ and $|w_{i+1} - w_i| \le 1$ for $1 \le i < m$; in particular
$\mathcal{T}_{0,j}$ is empty. The area distribution of $\mathcal{T}_{m,j}$ is the polynomial
$t(m, j; q) = \sum_{w \in \mathcal{T}_{m,j}} q^{w_1 + \cdots + w_m}$ in $\mathbb{Z}[q]$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 3, definition of `𝒯_{m,j}` and `t(m, j; q)`.

Formalized by `MetaMathlibExt.smoothPlateauAreaDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-plateau-area-dist).

## Capacity distribution at $q = 1$

For every finite set $S$ of words of length $n$ with
letters in the natural numbers, the capacity distribution of $S$ evaluated at $q = 1$ equals the
number of words in $S$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `a(n, i; q)`.

Formalized by `MetaMathlibExt.capacityDist_eval_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#capacity-dist-eval-one).

## Area distribution at $q = 1$

For every finite set $S$ of words of length $n$ with
letters in the natural numbers, the area distribution of $S$ evaluated at $q = 1$ equals the
number of words in $S$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 2, definition of `c(m, j, ℓ; q)`.

Formalized by `MetaMathlibExt.areaDist_eval_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#area-dist-eval-one).

## Catalan and smooth words of length four

There are $14$ Catalan words of length $4$,
$13$ smooth words of length $4$, and $7$ restricted smooth words of length $4$. Here $14$ is the
Catalan number $C_4$, $13 = C_4 - 1$, and $7$ is the central trinomial coefficient $G_3$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 1, examples.

Formalized by `MetaMathlibExt.card_catalanWords_four_smoothWords_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#card-catalan-words-four-smooth-words-fou).

## Recurrence for the area distribution by first letter

For natural numbers $m$, $j$ and
$\ell$, let $c(m, j, \ell; q) \in \mathbb{Z}[q]$ be the area distribution of the words of length
$m$ with letters in $\{1, \dots, j\}$, each letter at most one more than the letter before it,
that begin with $\ell$ and end with $j$. For all natural numbers $m \ge 2$ and $j$, $\ell$ with
$1 \le \ell \le j$,

$$c(m, j, \ell; q) = q^{\ell} \sum_{i=1}^{\ell+1} c(m-1, j, i; q),$$

and $c(1, j, \ell; q)$ equals $q^{\ell}$ if $j = \ell$ and $0$ otherwise.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 1.

Stated but not proved: `MetaMathlibExt.catalanGrowthAreaDist_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-growth-area-dist-succ).

## Denominator polynomials for the area of words with unit-bounded rises

The polynomials
$d_j(x; q)$, viewed as formal power series in $x$ over $\mathbb{Z}[q]$, are defined by $d_0 = 1$,
$d_1 = 1 - xq$, $d_2 = 1 - xq - xq^2$ and
$d_j = (1 - xq^j)\, d_{j-1} - x^2 q^{2j-1} d_{j-3}$ for $j \ge 3$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 3, recurrence (4).

Formalized by `MetaMathlibExt.catalanGrowthDen`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-growth-den).

## The area denominators have constant term one

For every $j \ge 0$, the power series
$d_j(x; q)$ in $x$ over $\mathbb{Z}[q]$ defined by $d_0 = 1$, $d_1 = 1 - xq$, $d_2 = 1 - xq - xq^2$
and $d_j = (1 - xq^j) d_{j-1} - x^2 q^{2j-1} d_{j-3}$ for $j \ge 3$ has constant term $1$.

Consequently every $d_j(x; q)$ is invertible as a power series in $x$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 3, recurrence (4).

Formalized by `MetaMathlibExt.constantCoeff_catalanGrowthDen`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#constant-coeff-catalan-growth-den).

## Area generating function of words with unit-bounded rises, by first letter

For natural
numbers $i$ and $j$ with $1 \le i \le j$ and for $n \ge 0$, let $c(n, j, i; q) \in \mathbb{Z}[q]$
be the area distribution of the words of length $n$ with letters in $\{1, \dots, j\}$, each letter
at most one more than the letter before it, that begin with $i$ and end with $j$: the sum of
$q^{\mathrm{area}(w)}$ over these words $w$, where $\mathrm{area}(w)$ is the sum of the letters
of $w$. Let $d_0, d_1, \dots$ be the power series in $x$ over $\mathbb{Z}[q]$ defined by
$d_0 = 1$, $d_1 = 1 - xq$, $d_2 = 1 - xq - xq^2$ and
$d_k = (1 - xq^k)\, d_{k-1} - x^2 q^{2k-1} d_{k-3}$ for $k \ge 3$; each $d_k$ has constant term
$1$, so it is invertible. Then, as formal power series in $x$ over $\mathbb{Z}[q]$,

$$\sum_{n \ge 0} c(n, j, i; q)\, x^n =
x^{j-i+1} q^{\binom{j+1}{2} - \binom{i}{2}}\, \frac{d_{i-1}(x; q)}{d_j(x; q)}.$$

The term for $n = 0$ is zero, since there are no words of length $0$ that end with $j$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 3.

Stated but not proved: `MetaMathlibExt.catalanGrowthAreaDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-growth-area-dist-gen-fun).

## Area generating function of words with unit-bounded rises ending in their maximum

For
natural numbers $n$ and $j$, let $\mathcal{C}_{n,j}$ be the set of words $w = w_1 \cdots w_n$ with
letters in $\{1, \dots, j\}$, each letter at most one more than the letter before it, and last
letter $j$, and let $c(n, j; q) \in \mathbb{Z}[q]$ be the sum of $q^{w_1 + \cdots + w_n}$ over
$w \in \mathcal{C}_{n,j}$. Let the formal power series $d_k(x; q)$ in $x$ over $\mathbb{Z}[q]$ be
defined by $d_0 = 1$, $d_1 = 1 - xq$, $d_2 = 1 - xq - xq^2$ and
$d_k = (1 - xq^k)\, d_{k-1} - x^2 q^{2k-1} d_{k-3}$ for $k \ge 3$. For every natural number
$j \ge 1$, in formal power series in $x$ over $\mathbb{Z}[q]$,

$$\sum_{n \ge 0} c(n, j; q)\, x^n =
\frac{1}{d_j(x; q)} \sum_{i=1}^{j} x^{j-i+1} q^{\binom{j+1}{2} - \binom{i}{2}} d_{i-1}(x; q).$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 3.

Stated but not proved: `MetaMathlibExt.catalanGrowthWords_areaDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-growth-words-area-dist-gen-fun).

## Dilating and inverting a power series

For a natural number $j$ and a power series
$f(x; q) = \sum_{n \ge 0} f_n(q) x^n$ in $x$ over $\mathbb{Z}[q]$, the power series
$f(q^j x; 1/q)$ in $x$ over the Laurent polynomial ring $\mathbb{Z}[q, q^{-1}]$ is
$\sum_{n \ge 0} q^{jn} f_n(q^{-1}) x^n$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 4.

Formalized by `MetaMathlibExt.dilateInvertSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 355](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L355). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#dilate-invert-series).

## Dilating and inverting a power series preserves constant term one

For every natural
number $j$ and every power series $f(x; q)$ in $x$ over $\mathbb{Z}[q]$ with constant term $1$,
the power series $f(q^j x; 1/q)$ in $x$ over $\mathbb{Z}[q, q^{-1}]$ also has constant term $1$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 4.

Formalized by `MetaMathlibExt.constantCoeff_dilateInvertSeries`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#constant-coeff-dilate-invert-series).

## Generating function for the capacity of Catalan words ending in their largest letter

For
natural numbers $n$ and $i$, let $b(n, i; q)$ be the capacity distribution of the Catalan words of
length $n$ that end in $i$ and have all letters at most $i$, viewed in $\mathbb{Z}[q, q^{-1}]$.
Let the formal power series $d_k(x; q)$ in $x$ over $\mathbb{Z}[q]$ be defined by $d_0 = 1$,
$d_1 = 1 - xq$, $d_2 = 1 - xq - xq^2$ and $d_k = (1 - xq^k)\, d_{k-1} - x^2 q^{2k-1} d_{k-3}$ for
$k \ge 3$. For a natural number $j$ and a power series $f(x; q)$ over $\mathbb{Z}[q]$ write
$f(q^j x; 1/q)$ for the series over $\mathbb{Z}[q, q^{-1}]$ whose coefficient of $x^n$ is
$q^{jn}$ times the coefficient of $x^n$ in $f$ with $q$ replaced by $q^{-1}$. For every natural
number $i \ge 1$, in formal power series in $x$ over $\mathbb{Z}[q, q^{-1}]$,

$$\sum_{n \ge 0} b(n, i; q)\, x^n = x^i \prod_{j=1}^{i} \Bigl(1 - x -
\frac{x}{d_{j-1}(q^j x; 1/q)} \sum_{m=1}^{j-1} x^{j-m} q^{j(j-m) + \binom{m}{2} - \binom{j}{2}}
d_{m-1}(q^j x; 1/q)\Bigr)^{-1}.$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 4.

Stated but not proved: `MetaMathlibExt.catalanMaxEndCapacityDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-max-end-capacity-dist-gen-fun).

## Recurrence for the capacity distribution on Catalan words

Write $a(n, i)$ for the
capacity distribution of the Catalan words of length $n$ ending in $i$, $b(n, i)$ for that of
those Catalan words of length $n$ ending in $i$ whose largest letter is $i$, and $c(m, j)$ for the
area distribution of the set $\mathcal{C}_{m,j}$ of words of length $m$ over $\{1, \dots, j\}$
ending in $j$ in which each letter is at most one more than the letter before it. For
$1 < i < n$, in the Laurent polynomial ring $\mathbb{Z}[q, q^{-1}]$,

$$
a(n,i) = b(n-1,i-1) + \sum_{j=i}^{n-1} a(n-1,j) +
\sum_{m=1}^{n-i-1} \sum_{j=i}^{n-m-1} q^{mi} \, a(n-m-1,j) \, c(m,i-1;1/q),
$$

where $c(m, i-1; 1/q)$ is the image of $c(m, i-1)$ under $q \mapsto q^{-1}$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 2.

Stated but not proved: `MetaMathlibExt.catalanCapacityDist_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-capacity-dist-recurrence).

## Recurrence for the capacity of Catalan words ending in their largest letter

For natural
numbers $n$ and $i$, let $b(n, i; q)$ be the capacity distribution of the Catalan words of length
$n$ that end in $i$ and have all letters at most $i$. For natural numbers $m$ and $k$, let
$c(m, k; q) \in \mathbb{Z}[q]$ be the area distribution of the words of length $m$ with letters
in $\{1, \dots, k\}$, each letter at most one more than the letter before it, and last letter
$k$, and let $c(m, k; 1/q)$ be its image under $q \mapsto q^{-1}$. For all natural numbers $n$
and $i$ with $1 < i < n$, in $\mathbb{Z}[q, q^{-1}]$,

$$b(n, i; q) = b(n-1, i; q) + b(n-1, i-1; q) +
\sum_{m=1}^{n-i-1} q^{mi}\, b(n-m-1, i; q)\, c(m, i-1; 1/q).$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 2.

Stated but not proved: `MetaMathlibExt.catalanMaxEndCapacityDist_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-max-end-capacity-dist-recurrence).

## Boundary values of the capacity distributions on Catalan words

Write $a(n, i)$ for the
capacity distribution of the Catalan words of length $n$ ending in $i$, $b(n, i)$ for that of
those Catalan words of length $n$ ending in $i$ whose largest letter is $i$, and $a(n)$ for the
capacity distribution of all Catalan words of length $n$. For every $n \ge 1$,
$a(n, n) = b(n, 1) = b(n, n) = 1$, and if $n \ge 2$ then $a(n, 1) = a(n - 1)$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 2.

Stated but not proved: `MetaMathlibExt.catalanCapacityDist_boundary` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-capacity-dist-boundary).

## Generating function of Catalan words by last letter

Let $C(x) = \sum_{n \ge 0} C_n x^n$
be the generating function of the Catalan numbers $C_n$. For every $i \ge 1$, let $a_{n,i}$ be the
number of Catalan words of length $n$ whose last letter is $i$. Then, as formal power series with
integer coefficients, $\sum_{n \ge 0} a_{n,i} x^n = x^i C(x)^i$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Corollary 3.

Stated but not proved: `MetaMathlibExt.catalanWordsEndingIn_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-words-ending-in-gen-fun).

## Maximum capacity of Catalan words

For every natural number $m$, the degree of the capacity
distribution $\sum_{w \in \mathcal{A}_n} q^{\operatorname{cap}(w)}$ of the set $\mathcal{A}_n$ of
Catalan words of length $n$, that is, the largest capacity of a Catalan word of length $n$, is
$3\binom{m}{2}$ for $n = 3m$, $m(3m-1)/2$ for $n = 3m + 1$ and $m(3m+1)/2$ for $n = 3m + 2$. The
case $m = 0$ is included.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 2.

Stated but not proved: `MetaMathlibExt.catalanWords_capacity_natDegree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 442](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L442). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-words-capacity-nat-degree).

## Number of Catalan words of maximum capacity

For every $n \ge 4$, let $\mathcal{A}_n$ be
the set of Catalan words of length $n$. The leading coefficient of the capacity distribution
$\sum_{w \in \mathcal{A}_n} q^{\operatorname{cap}(w)}$ is $2$ if $3$ divides $n$ and $1$
otherwise; equivalently, exactly two Catalan words of length $n$ have the largest capacity when
$3 \mid n$, and exactly one does otherwise.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Corollary 4.

Stated but not proved: `MetaMathlibExt.catalanWords_capacity_leadingCoeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-words-capacity-leading-coeff).

## Subleading coefficient of the capacity distribution of Catalan words

For every $n \ge 4$,
let $\mathcal{A}_n$ be the set of Catalan words of length $n$, let $\alpha$ be the degree of its
capacity distribution $\sum_{w \in \mathcal{A}_n} q^{\operatorname{cap}(w)}$, and let $d_n$ be the
coefficient of $q^{\alpha - 1}$ in it. Then $d_4 = 13$, $d_5 = 7$, $d_6 = 8$, and for $n \ge 7$,
$d_n = 2m$ if $n = 3m$, $d_n = m + 1$ if $n = 3m + 1$ and $d_n = m + 2$ if $n = 3m + 2$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Corollary 4.

Stated but not proved: `MetaMathlibExt.catalanWords_capacity_subleading_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 461](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L461). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-words-capacity-subleading-coeff).

## Zero-capacity Catalan words with a given last letter

For $2 \le i \le n$, let
$a(n, i; q)$ be the capacity distribution of the Catalan words of length $n$ ending in $i$, so that
$a(n, i; 0)$ is the number of those words with capacity $0$. Then

$$
a(n, i; 0) = \sum_{m=0}^{n-i} \binom{n-m-2}{i-2} F_{2m-1},
$$

where $F_k$ is the $k$-th Fibonacci number ($F_1 = F_2 = 1$) and $F_{-1} = 1$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 3.

Stated but not proved: `MetaMathlibExt.catalanCapacityDist_eval_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-capacity-dist-eval-zero).

## Catalan words of capacity zero

Let $F_k$ be the Fibonacci numbers, with $F_0 = 0$ and
$F_1 = 1$. For $n \ge 1$, let $a(n, 1; q)$ be the capacity distribution on Catalan words of length
$n$ ending in $1$, and let $a(n; q) = \sum_{w \in \mathcal{A}_n} q^{\operatorname{cap}(w)}$ be the
capacity distribution on the set $\mathcal{A}_n$ of all Catalan words of length $n$. Then
$a(n, 1; 0)$, the number of Catalan words of length $n$ ending in $1$ with capacity $0$, is $1$ if
$n = 1$ and $F_{2n-3}$ if $n \ge 2$, and $a(n; 0)$, the number of Catalan words of length $n$ with
capacity $0$, is $F_{2n-1}$.

The value $1$ for $n = 1$ is $F_{2n-3}$ under the convention $F_{-1} = 1$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 3.

Stated but not proved: `MetaMathlibExt.catalanWords_zero_capacity_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#catalan-words-zero-capacity-count).

## Recurrence for the area distribution of smooth words from $j$ to $j$

Let $t(m, j; q)$ be
the area distribution of the words of length $m$ over $\{1, \dots, j\}$ that begin and end with $j$
and whose consecutive letters differ by at most $1$. For all $m \ge 2$ and $j \ge 2$,

$$t(m, j; q) = q^j\, t(m-1, j; q) + q^j \sum_{\ell=1}^{m-2} t(\ell, j-1; q)\, t(m-\ell-1, j; q),$$

and for every $k \ge 1$, $t(k, 1; q) = t(1, k; q) = q^k$ (Mansour and Shattuck's Lemma 6).

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 6.

Stated but not proved: `MetaMathlibExt.smoothPlateauAreaDist_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-plateau-area-dist-recurrence).

## Area polynomial of restricted smooth words between two top letters

For natural numbers
$m$ and $j$, let $\mathcal{T}^*_{m,j}$ be the set of words $w = w_1 \cdots w_m$ over
$\{1, \dots, j\}$ with $w_1 = w_m = j$, $w_{k+1} \le w_k + 1$ and $w_k \le w_{k+1} + 1$ for
$1 \le k < m$, and no two adjacent letters both equal to $1$ (so $\mathcal{T}^*_{0,j}$ is empty).
Then $t^*(m, j; q)$ is the polynomial $\sum_{w \in \mathcal{T}^*_{m,j}} q^{w_1 + \cdots + w_m}$ in
$\mathbb{Z}[q]$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Section 4, definition of `t*(m, j; q)`.

Formalized by `MetaMathlibExt.restrictedSmoothPlateauAreaDist`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-plateau-area-dist).

## Continued-fraction denominators

Given a power series $B$ in $x$ over $\mathbb{Z}[q]$,
define power series $K_k$ in $x$ over $\mathbb{Z}[q]$ by $K_0 = 1$, $K_1 = B$ and, for $k \ge 2$,
$K_k = 1 - q^k x - q^{2k-1} x^2 K_{k-1}^{-1}$. Here $K_{k-1}^{-1}$ is the formal inverse of
$K_{k-1}$ computed with constant term $1$. It is the true inverse whenever $K_{k-1}$ has constant
term $1$, which always holds for $k \ge 3$, and for $k = 2$ when $B$ has constant term $1$.
Lemma 8 takes $B = 1 - qx$ and Lemma 10 takes $B = 1$; the value $K_0$ is unused.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemmas 8 and 10.

Formalized by `MetaMathlibExt.capacityContinuedFractionDen`, a definition declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#capacity-continued-fraction-den).

## Continued-fraction denominators have constant term one

Let $B$ be a power series in $x$
over $\mathbb{Z}[q]$ with constant term $1$, and define power series $K_k$ in $x$ over
$\mathbb{Z}[q]$ by $K_0 = 1$, $K_1 = B$ and $K_k = 1 - q^k x - q^{2k-1} x^2 / K_{k-1}$ for
$k \ge 2$. Then $K_k$ has constant term $1$ for every $k \ge 0$.

Consequently every $K_k$ is invertible as a power series in $x$, and the inverses of $K_{k-1}$
used to define $K_k$ are genuine inverses.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemmas 8 and 10.

Formalized by `MetaMathlibExt.constantCoeff_capacityContinuedFractionDen`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#constant-coeff-capacity-continued-fracti).

## Continued fraction for smooth words from $j$ to $j$ by area

Let $t(m, j; q)$ be the area
distribution of the words of length $m$ over $\{1, \dots, j\}$ that begin and end with $j$ and whose
consecutive letters differ by at most $1$. Define power series $K_k$ in $x$ over $\mathbb{Z}[q]$ by
$K_1 = 1 - qx$ and $K_k = 1 - q^k x - q^{2k-1} x^2 / K_{k-1}$ for $k \ge 2$; each $K_k$ has constant
term $1$. Then for every $j \ge 1$, in $\mathbb{Z}[q][[x]]$,

$$\sum_{m \ge 0} t(m, j; q)\, x^m = \frac{q^j x}{K_j}.$$

This is Mansour and Shattuck's Lemma 8: $q^j x / K_j$ is the finite continued fraction
$q^j x / (1 - q^j x - q^{2j-1} x^2 / (1 - q^{j-1} x - \cdots / (1 - q^2 x - q^3 x^2 / (1 - qx))))$,
and for $j = 1$ it is $qx / (1 - qx)$. The term $m = 0$ vanishes.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 8.

Stated but not proved: `MetaMathlibExt.smoothPlateauAreaDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-plateau-area-dist-gen-fun).

## Continued fraction for the area series of restricted smooth words

For $j \ge 1$, let
$t^*(m, j; q) = \sum_w q^{w_1 + \cdots + w_m}$, the sum over the words $w = w_1 \cdots w_m$ over
$\{1, \dots, j\}$ with $w_1 = w_m = j$ (there are none for $m = 0$), consecutive letters
differing by at most $1$ and no two adjacent letters equal to $1$, and let
$T^*_j(x; q) = \sum_{m \ge 0} t^*(m, j; q)\, x^m$. Define power series $K_k$ in $x$ over
$\mathbb{Z}[q]$ by $K_1 = 1$ and $K_k = 1 - q^k x - q^{2k-1} x^2 / K_{k-1}$ for $k \ge 2$ (each
$K_k$ has constant term $1$, so the divisions are defined). Then

$$T^*_j(x; q) = \frac{q^j x}{K_j}.$$

For example, $T^*_1 = qx$ and $T^*_2 = q^2 x / (1 - q^2 x - q^3 x^2)$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 10.

Stated but not proved: `MetaMathlibExt.restrictedSmoothPlateauAreaDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-plateau-area-dist-gen).

## Recurrence for the capacity distribution of smooth words by last letter

Let $r(n, i; q)$
be the capacity distribution of the smooth words of length $n$ ending in $i$, let $s(n, i; q)$ be
that of those smooth words of length $n$ ending in $i$ whose largest letter is $i$, and let
$t(m, j; q)$ be the area distribution (the area of a word is the sum of its letters) of the words
of length $m$ over $\{1, \dots, j\}$ that begin and end with $j$ and whose adjacent letters
differ by at most $1$. For $1 < i < n$, in the ring $\mathbb{Z}[q, q^{-1}]$ of Laurent
polynomials,

$$
r(n, i; q) = r(n - 1, i; q) + r(n - 1, i + 1; q) + s(n - 1, i - 1; q) +
\sum_{m=1}^{n-i-1} q^{mi}\, r(n - m - 1, i; q)\, t(m, i - 1; 1/q).
$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 7.

Stated but not proved: `MetaMathlibExt.smoothCapacityDist_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 568](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-capacity-dist-recurrence).

## Recurrence for the capacity distribution of smooth words ending in their largest letter

Let $s(n, i; q)$ be the capacity distribution of the smooth words of length $n$ that end in $i$ and
have largest letter $i$, and let $t(m, j; q)$ be the area distribution (the area of a word is the
sum of its letters) of the words of length $m$ over $\{1, \dots, j\}$ that begin and end with $j$
and whose adjacent letters differ by at most $1$. For $1 < i < n$, in the ring
$\mathbb{Z}[q, q^{-1}]$ of Laurent polynomials,

$$
s(n, i; q) = s(n - 1, i; q) + s(n - 1, i - 1; q) +
\sum_{m=1}^{n-i-1} q^{mi}\, s(n - m - 1, i; q)\, t(m, i - 1; 1/q).
$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 7.

Stated but not proved: `MetaMathlibExt.smoothMaxEndCapacityDist_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-max-end-capacity-dist-recurrence).

## Boundary values of the capacity distributions of smooth words

For letters $i$, let
$r(n, i; q)$ be the capacity distribution of the smooth words of length $n$ ending in $i$, and
$s(n, i; q)$ that of those smooth words of length $n$ ending in $i$ whose largest letter is $i$.
For $n \ge 1$, $r(n, n; q) = s(n, n; q) = s(n, 1; q) = 1$, and if $n \ge 2$ then
$r(n, 1; q) = r(n - 1, 1; q) + r(n - 1, 2; q)$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 7.

Stated but not proved: `MetaMathlibExt.smoothCapacityDist_boundary` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-capacity-dist-boundary).

## Generating function of smooth words ending in their largest letter

For $i \ge 1$, let
$s(n, i; q)$ be the capacity distribution of the smooth words of length $n$ that end in $i$ and
have largest letter $i$, and let $t(m, j; q)$ be the area distribution (the area of a word is the
sum of its letters) of the words of length $m$ over $\{1, \dots, j\}$ that begin and end with $j$
and whose adjacent letters differ by at most $1$. In the ring of formal power series in $x$ over
the Laurent polynomials $\mathbb{Z}[q, q^{-1}]$,

$$
\sum_{n \ge 0} s(n, i; q)\, x^n = x^i \prod_{j=0}^{i-1}
\Bigl(1 - x - x \sum_{m \ge 0} q^{(j+1)m}\, t(m, j; 1/q)\, x^m\Bigr)^{-1}.
$$

The factor for $j = 0$ is $(1 - x)^{-1}$, since $t(m, 0; q) = 0$ for every $m$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 9.

Stated but not proved: `MetaMathlibExt.smoothMaxEndCapacityDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-max-end-capacity-dist-gen-fun).

## Generating function for restricted smooth words ending in their largest letter

For
$i \ge 1$, let $s^*(n, i; q)$ be the capacity distribution of the restricted smooth words of
length $n$ that end in $i$ and all of whose letters are at most $i$. For $j \ge 1$, let
$t^*(m, j; q) = \sum_w q^{w_1 + \cdots + w_m}$, the sum over the words $w = w_1 \cdots w_m$ over
$\{1, \dots, j\}$ with $w_1 = w_m = j$ (there are none for $m = 0$), consecutive letters
differing by at most $1$ and no two adjacent letters equal to $1$, and let
$T^*_j(q^{j+1} x; 1/q) = \sum_{m \ge 0} q^{(j+1)m}\, t^*(m, j; 1/q)\, x^m$. Then, in the ring of
formal power series in $x$ over $\mathbb{Z}[q, q^{-1}]$,

$$
\sum_{n \ge 0} s^*(n, i; q)\, x^n =
x^i \prod_{j=1}^{i-1} \frac{1}{1 - x - x\, T^*_j(q^{j+1} x; 1/q)},
$$

where each denominator has constant term $1$ and so is invertible.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Lemma 11.

Stated but not proved: `MetaMathlibExt.restrictedSmoothMaxEndCapacityDist_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-max-end-capacity-dist-2).

## Maximum capacity of smooth words

A smooth word is a word of positive integers with first
letter $1$ whose consecutive letters differ by at most $1$. Let
$r(n; q) = \sum_w q^{\mathrm{cap}(w)}$, summed over the smooth words $w$ of length $n$, where
$\mathrm{cap}(w)$ is the capacity of $w$. For all $m \ge 1$ and $0 \le p \le 3$, the degree of
$r(4m + p; q)$ in $q$ is $m(2m + p - 1)$. Since $r(n; q)$ is a nonzero polynomial with
nonnegative coefficients, this degree is the maximum capacity of a smooth word of length
$4m + p$ (Mansour and Shattuck's Theorem 5).

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 5.

Stated but not proved: `MetaMathlibExt.smoothWords_capacity_natDegree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 631](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L631). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-words-capacity-nat-degree).

## Zero-capacity smooth words with a given last letter

For $2 \le i \le n$, the number of
smooth words of length $n$ ending in $i$ with capacity $0$, that is, the value at $q = 0$ of their
capacity distribution $r(n, i; q)$, equals $\sum_{j=i-2}^{n-2} \binom{n-2}{j}$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 6.

Stated but not proved: `MetaMathlibExt.smoothCapacityDist_eval_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-capacity-dist-eval-zero).

## Number of smooth words of capacity zero

Let $r(n, i; q)$ be the capacity distribution of
the smooth words of length $n$ ending in $i$ and $r(n; q)$ that of all smooth words of length $n$,
so that $r(n, i; 0)$ and $r(n; 0)$ count the smooth words of capacity $0$. Then $r(1, 1; 0) = 1$
and $r(n, 1; 0) = 2^{n-2}$ for every $n \ge 2$; moreover $r(1; 0) = 1$, $r(2; 0) = 2$ and
$r(n; 0) = (n + 2) \cdot 2^{n-3}$ for every $n \ge 3$ (Mansour and Shattuck's Theorem 6, totals).

The paper states the formula for $r(n; 0)$ for $n \ge 2$; at $n = 2$ it reads $4 \cdot 2^{-1} = 2$,
so that case is stated separately.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 6.

Stated but not proved: `MetaMathlibExt.smoothWords_zero_capacity_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 649](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L649). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#smooth-words-zero-capacity-count).

## Maximum capacity of restricted smooth words

Let $m \ge 0$ and $0 \le p \le 7$ with
$n = 8m + p \ge 1$. The degree of the capacity distribution of the restricted smooth words of
length $n$, that is, the largest capacity of a restricted smooth word of length $n$, equals
$8m^2 + (2p - 3)m + e_p$, where $e_p = 0$ for $p \le 3$, $e_4 = 1$ and $e_p = 2^{p-5}$ for
$5 \le p \le 7$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 9.

Stated but not proved: `MetaMathlibExt.restrictedSmoothWords_capacity_natDegree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-words-capacity-nat-deg).

## Number of restricted smooth words of maximum capacity

Let $n = 8m + p \ge 1$ with
natural numbers $m$ and $p \le 7$, and let $c_n$ be the leading coefficient of the capacity
distribution $\sum_{w} q^{\mathrm{cap}(w)}$ over the restricted smooth words $w$ of length $n$
(smooth words with no two adjacent letters equal to $1$), that is, the number of restricted
smooth words of length $n$ with maximum capacity. If $m = 0$, then $c_1, \dots, c_7$ are
$1, 1, 3, 1, 5, 2, 1$. If $m \ge 1$, then $c_n = m + 1$ for $p \in \{0, 3\}$, $c_n = m + 3$ for
$p = 5$, $c_n = m + 2$ for $p = 6$ and $c_n = 1$ for $p \in \{1, 2, 4, 7\}$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 9.

Stated but not proved: `MetaMathlibExt.restrictedSmoothWords_capacity_leadingCoeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-words-capacity-leading).

## Zero-capacity restricted smooth words with a given last letter

For natural numbers $n$
and $i$ with $3 \le i \le n$, let $r^*(n, i; q)$ be the capacity distribution of the restricted
smooth words of length $n$ ending in $i$. Its value at $q = 0$, which is the number of such words
of capacity $0$, is

$$r^*(n, i; 0) = \sum_{j=i-3}^{n-3} \binom{n-3}{j}.$$

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 10.

Stated but not proved: `MetaMathlibExt.restrictedSmoothCapacityDist_eval_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-capacity-dist-eval-zer).

## Zero-capacity restricted smooth words

For $n \ge 1$ and a letter $i$, let $r^{\ast}(n, i)$
be the number of restricted smooth words of length $n$ ending in $i$ that have capacity $0$, and
let $r^{\ast}(n)$ be the number of restricted smooth words of length $n$ with capacity $0$; these
are the values at $q = 0$ of the corresponding capacity distributions. Then $r^{\ast}(n, 1) = 1$
for $n \in \{1, 3\}$, $r^{\ast}(2, 1) = 0$ and $r^{\ast}(n, 1) = 2^{n-4}$ for $n \ge 4$;
$r^{\ast}(2, 2) = 1$ and $r^{\ast}(n, 2) = 2^{n-3}$ for $n \ge 3$; and $r^{\ast}(n) = 1$ for
$n \le 2$, $r^{\ast}(3) = 3$ and $r^{\ast}(n) = (n + 2)\, 2^{n-4}$ for $n \ge 4$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 10.

Stated but not proved: `MetaMathlibExt.restrictedSmoothWords_zero_capacity_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#restricted-smooth-words-zero-capacity-co).

## Restricted smooth words are counted by grand Motzkin numbers

For every $n \ge 1$, the
number of restricted smooth words of length $n$ is the grand Motzkin number $G_{n-1}$, that is,
the central trinomial coefficient: the coefficient of $X^{n-1}$ in $(1 + X + X^2)^{n-1}$.

## Sources

- Toufik Mansour and Mark Shattuck, *Enumeration of Catalan and Smooth Words According to Capacity*, INTEGERS 25 (2025), Article A5, Theorem 11.

Stated but not proved: `MetaMathlibExt.card_restrictedSmoothWords` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean, line 712](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CatalanWordsCapacityWanted.lean#L712). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html#card-restricted-smooth-words).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Capacity of Catalan words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/capacity-of-catalan-words)
