---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.IsHigherFibRecurrence, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.IsStandardHigherFib, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.weightedHigherFibSum, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.weightedHigherFibMomentSum, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.higherFibWalk, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.fibQ, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.fibWalkCount, MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.evenFibWalkCount
statement: formalized
---

# Self-convolutions of m-step Fibonacci numbers

17 results, 9 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html).

## The $m$-step Fibonacci recurrence

A sequence $F : \mathbb{Z} \to \mathbb{Q}$ satisfies the
$m$-step Fibonacci recurrence if $F_n = F_{n-1} + F_{n-2} + \dots + F_{n-m}$ for every integer
$n$, that is, $F_n = \sum_{i=0}^{m-1} F_{n-i-1}$. For $m = 0$ this says $F_n = 0$ for all $n$.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.IsHigherFibRecurrence`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#is-higher-fib-recurrence).

## The standard order-$m$ Fibonacci sequence

A sequence $F : \mathbb{Z} \to \mathbb{Q}$ is
the standard order-$m$ Fibonacci sequence if it satisfies the $m$-step Fibonacci recurrence,
$F_i = 0$ for every natural number $i < m - 1$, and $F_{m-1} = 1$, where $m - 1$ is computed in
the integers.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.IsStandardHigherFib`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#is-standard-higher-fib).

## Weighted sum of a sequence

For a sequence $F : \mathbb{Z} \to \mathbb{Q}$, a natural number
$m$, integers $N$ and $l$, and a rational number $q$, $S(m,N,l,q) = \sum_{k=0}^{N} q^k F_{k+l}$;
for $N < 0$ this is the empty sum $0$.

The order $m$ is carried explicitly to match the paper notation, although the sum itself only
uses $F$, $N$, $l$, and $q$.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.weightedHigherFibSum`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#weighted-higher-fib-sum).

## First-moment weighted sum

For a sequence $F : \mathbb{Z} \to \mathbb{Q}$, a natural number
$m$, integers $N$ and $l$, and a rational number $q$, $S_2(m,N,l,q) = \sum_{k=0}^{N} k q^k F_{k+l}$;
for $N < 0$ this is the empty sum $0$. The value does not depend on $m$.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.weightedHigherFibMomentSum`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#weighted-higher-fib-moment-sum).

## Shifted self-convolution

For a sequence $F : \mathbb{Z} \to \mathbb{Q}$ and natural
numbers $m$ and $n$, the shifted self-convolution is
$w_n^{(m)} = \sum_{j=0}^{n} F_{j+m-1} F_{n-j+m-1}$, with the indices computed in the integers.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.higherFibWalk`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#higher-fib-walk).

## Fibonacci numbers at integer indices

For an integer $n$, $F_n$ is the $n$-th Fibonacci
number as a rational number: $F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$ for $n \ge 0$, and
$F_{-n} = (-1)^{n+1} F_n$ for $n > 0$.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.fibQ`, an abbreviation declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#fib-q).

## Fibonacci self-convolution

For $n \ge 0$, $v_n$ is the rational number
$v_n = \sum_{j=0}^{n} F_{j+1} F_{n-j+1}$, where $F_i$ is the $i$-th Fibonacci number
($F_0 = 0$, $F_1 = 1$).

This sum encodes algebraically the number of Fibonacci tiling walks.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.fibWalkCount`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#fib-walk-count).

## Even part of the Fibonacci self-convolution

For $n \ge 0$, $E_n$ is the rational number
$\sum F_{j+1} F_{n-j+1}$, the sum taken over the even integers $j$ with $0 \le j \le n$, where
$F_i$ is the $i$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$).

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.evenFibWalkCount`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#even-fib-walk-count).

## Odd part of the Fibonacci walk count

For a natural number $n$, this is the sum of
$F_{j+1} F_{n-j+1}$ over the odd $j$ with $0 \le j \le n$, where $F_k$ are the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$, $F_{k+2} = F_{k+1} + F_k$). It is the part of
$v_n = \sum_{j=0}^{n} F_{j+1} F_{n-j+1}$ that comes from odd $j$.

Formalized by `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.oddFibWalkCount`, a definition declared in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#odd-fib-walk-count).

## Recurrence for the shifted self-convolution of higher-order Fibonacci numbers

Let
$m \ge 1$ and let $(F_n)_{n \in \mathbb{Z}}$ be a sequence of rational numbers with
$F_n = F_{n-1} + \dots + F_{n-m}$ for every integer $n$, $F_i = 0$ for $0 \le i < m - 1$ and
$F_{m-1} = 1$, and for $n \ge 0$ let $w_n = \sum_{j=0}^{n} F_{j+m-1} F_{n-j+m-1}$. Then for
every integer $n \ge 0$, $(m+1) w_{n+1} - 2m w_n = (n+m+2) F_{n+m} - (n+m) F_{n+m-1}$.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.higherFibWalk_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#higher-fib-walk-recurrence).

## Closed form for weighted sums of an $m$-step Fibonacci sequence

Let $m \ge 1$ and let
$F : \mathbb{Z} \to \mathbb{Q}$ satisfy the $m$-step Fibonacci recurrence
$F_k = F_{k-1} + \dots + F_{k-m}$ for every integer $k$. For every natural number $n$, every
integer $l$ and every rational number $q$ with $q^{m+1} - 2q + 1 \ne 0$, the weighted sum
$S(m,n,l,q) = \sum_{k=0}^{n} q^k F_{k+l}$ equals

$$
\frac{(q-1)\Bigl(q^{n+1}F_{n+l+1} - F_l +
\sum_{i=1}^{m-1}\sum_{j=1}^{i} q^{i+1-j}\bigl(q^{n+1}F_{n+l-j+1} - F_{l-j}\bigr)\Bigr)}
{q^{m+1} - 2q + 1}.
$$

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.weightedHigherFibSum_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#weighted-higher-fib-sum-eq).

## Explicit formula for the shifted self-convolution of higher-order Fibonacci numbers

Let
$m \ge 1$ and let $(F_n)_{n \in \mathbb{Z}}$ be a sequence of rational numbers with
$F_n = F_{n-1} + \dots + F_{n-m}$ for every integer $n$, $F_i = 0$ for $0 \le i < m - 1$ and
$F_{m-1} = 1$. For $n \ge 0$ let $w_n = \sum_{j=0}^{n} F_{j+m-1} F_{n-j+m-1}$; for integers
$N$, $l$ and rational $q$ let $S(N, l, q) = \sum_{k=0}^{N} q^k F_{k+l}$ and
$S_2(N, l, q) = \sum_{k=0}^{N} k q^k F_{k+l}$, both equal to $0$ when $N < 0$. Put
$q = (m+1)/(2m)$. Then for every integer $n \ge 0$,

$$
w_n = \left(\frac{2m}{m+1}\right)^{n} +
\frac{(2m)^{n-1}}{(m+1)^{n}} \bigl((m+2) S(n-1, m, q) + S_2(n-1, m, q) -
m S(n-1, m-1, q) - S_2(n-1, m-1, q)\bigr).
$$

At $n = 0$ the weighted sums have upper limit $-1$ and are empty.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.higherFibWalk_eq_weighted_sums` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#higher-fib-walk-eq-weighted-sums).

## Self-convolution of higher-order Fibonacci numbers

Let $m \ge 1$ and let
$(F_n)_{n \in \mathbb{Z}}$ be a sequence of rational numbers with
$F_n = F_{n-1} + \dots + F_{n-m}$ for every integer $n$, $F_i = 0$ for $0 \le i < m - 1$ and
$F_{m-1} = 1$. For $p \ge 0$ let $w_p = \sum_{j=0}^{p} F_{j+m-1} F_{p-j+m-1}$; for integers
$N$, $l$ and rational $q$ let $S(N, l, q) = \sum_{k=0}^{N} q^k F_{k+l}$ and
$S_2(N, l, q) = \sum_{k=0}^{N} k q^k F_{k+l}$, both equal to $0$ when $N < 0$. Put
$q = (m+1)/(2m)$. Then for every integer $n \ge 2m - 2$, writing $p = n - 2m + 2$,

$$
\sum_{i=0}^{n} F_i F_{n-i} = w_p = \left(\frac{2m}{m+1}\right)^{p} +
\frac{(2m)^{p-1}}{(m+1)^{p}} \bigl((m+2) S(p-1, m, q) + S_2(p-1, m, q) -
m S(p-1, m-1, q) - S_2(p-1, m-1, q)\bigr).
$$

The source states the formula for all $n \ge 0$, but for $m \ge 2$ it fails when
$n < 2m - 2$: at $m = 2$ and $n = 0$ the left side is $0$ and the right side is $9/16$.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.higherFib_selfConvolution_eq_weighted_sums` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#higher-fib-self-convolution-eq-weighted).

## Even and odd parts of the Fibonacci self-convolution agree at odd length

Let $F_n$
denote the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$) and, for $n \ge 0$, let $E_n$ and $O_n$ be
the sums of $F_{j+1} F_{n-j+1}$ over the even and over the odd integers $j$ with
$0 \le j \le n$. For every integer $k \ge 1$, $E_{2k-1} = O_{2k-1}$.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.evenFibWalkCount_odd_length_eq_oddFibWalkCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#even-fib-walk-count-odd-length-eq-odd-fi).

## Even and odd parts of the Fibonacci self-convolution at even length

Let $F_n$ denote
the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$) and, for $n \ge 0$, let $E_n$ and $O_n$ be the
sums of $F_{j+1} F_{n-j+1}$ over the even and over the odd integers $j$ with $0 \le j \le n$.
For every integer $k \ge 1$, $E_{2k} = O_{2k} + F_{2k+2}$.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.evenFibWalkCount_even_length_eq_odd_add_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#even-fib-walk-count-even-length-eq-odd-a).

## Halving the Fibonacci self-convolution at odd length

Let $F_n$ denote the Fibonacci
numbers ($F_0 = 0$, $F_1 = 1$) and, for $n \ge 0$, let $v_n = \sum_{j=0}^{n} F_{j+1} F_{n-j+1}$,
and let $E_n$ and $O_n$ be the sums of the same terms $F_{j+1} F_{n-j+1}$ over the even and over
the odd integers $j$ with $0 \le j \le n$. For every integer $k \ge 1$,
$E_{2k-1} = v_{2k-1}/2$ and $O_{2k-1} = v_{2k-1}/2$.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.fibWalkCounts_odd_length_eq_half` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#fib-walk-counts-odd-length-eq-half).

## Halving the Fibonacci self-convolution at even length

Let $F_n$ denote the Fibonacci
numbers ($F_0 = 0$, $F_1 = 1$) and, for $n \ge 0$, let $v_n = \sum_{j=0}^{n} F_{j+1} F_{n-j+1}$,
and let $E_n$ and $O_n$ be the sums of the same terms $F_{j+1} F_{n-j+1}$ over the even and over
the odd integers $j$ with $0 \le j \le n$. For every integer $k \ge 1$,
$E_{2k} = (v_{2k} + F_{2k+2})/2$ and $O_{2k} = (v_{2k} - F_{2k+2})/2$.

## Sources

- Jan Sedlák and Antonín Slavík, "Walks in Tiled Rectangles and Self-Convolutions of Higher-Order Fibonacci Numbers", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.HigherFibonacciWalksWanted.fibWalkCounts_even_length_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/HigherFibonacciWalksWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html#fib-walk-counts-even-length-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Self-convolutions of m-step Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/self-convolutions-of-m-step-fibonacci-numbers)
