---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.LeonardoPWanted.leonardoPKSeq, MathlibExt.NumberTheory.LeonardoPWanted.leonardoPK, MathlibExt.NumberTheory.LeonardoPWanted.hSeqForward, MathlibExt.NumberTheory.LeonardoPWanted.hSeqBackward, MathlibExt.NumberTheory.LeonardoPWanted.hSeqZ, MathlibExt.NumberTheory.LeonardoPWanted.seqAZ, MathlibExt.NumberTheory.LeonardoPWanted.seqBZ, MathlibExt.NumberTheory.LeonardoPWanted.companionQ
statement: formalized
---

# Leonardo p-numbers

79 results, 42 proved and 37 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html).

## Initial values of the generalized Leonardo $p$-numbers

For natural numbers $p$, $k$
and $n$, this is the list of integers $(\mathcal{L}_{p,k}(0), \mathcal{L}_{p,k}(1), \dots,
\mathcal{L}_{p,k}(n))$ of length $n + 1$, where $\mathcal{L}_{p,k}(i) = 1$ for $0 \le i \le p$
and $\mathcal{L}_{p,k}(i) = \mathcal{L}_{p,k}(i-1) + \mathcal{L}_{p,k}(i-p-1) + k$ for $i > p$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.leonardoPKSeq`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pkseq).

## Generalized Leonardo $p$-numbers

For natural numbers $p$ and $k$, the generalized
Leonardo $p$-numbers are the integers $\mathcal{L}_{p,k}(n)$, $n \in \mathbb{N}$, given by
$\mathcal{L}_{p,k}(n) = 1$ for $0 \le n \le p$ and
$\mathcal{L}_{p,k}(n) = \mathcal{L}_{p,k}(n-1) + \mathcal{L}_{p,k}(n-p-1) + k$ for $n > p$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.leonardoPK`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pk).

## Forward evaluation of the $H(p)$ recurrence

For a natural number $p$, a function
$s : \mathbb{Z} \to \mathbb{Z}$ and $n \in \mathbb{N}$, this is the list of the $2p + n + 1$
values at $-p, -p+1, \dots, p+n$ (the entry at position $i$ is the value at $i - p$) of the
sequence $H$ that equals $s$ on $[-p, p]$ and continues by the $H(p)$ recurrence
$H(t) = H(t-1) + H(t-p) - H(t-2p-1)$ for $t > p$. Each step appends one value to the previous
list, so evaluation takes polynomial time.

For $p = 0$, where this rule is circular, every appended value is $0$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.hSeqForward`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#h-seq-forward).

## Backward evaluation of the $H(p)$ recurrence

For a natural number $p$, a function
$s : \mathbb{Z} \to \mathbb{Z}$ and $n \in \mathbb{N}$, this is the list of the values at
$-p-n, \dots, p$ of the sequence $H$ that equals $s$ on $[-p, p]$ and continues to the left by
$H(t) = H(t+2p) + H(t+p+1) - H(t+2p+1)$ for $t < -p$, which is the $H(p)$ recurrence
$H(u) = H(u-1) + H(u-p) - H(u-2p-1)$ at $u = t+2p+1$ solved for $H(t)$. Each step prepends one
value to the previous list.

For $p = 0$, where this rule is circular, every prepended value equals $s(0)$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.hSeqBackward`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#h-seq-backward).

## Two-sided extension of initial values by the $H(p)$ recurrence

For a natural number
$p \ge 1$ and a function $s : \mathbb{Z} \to \mathbb{Z}$, this is the unique function
$H : \mathbb{Z} \to \mathbb{Z}$ that agrees with $s$ on $[-p, p]$ and satisfies
$H(t) = H(t-1) + H(t-p) - H(t-2p-1)$ for every integer $t$: its values at $t > p$ are computed
forward and its values at $t < -p$ backward from this recurrence. For $p = 0$ its value is $s(0)$
at every $t \le 0$ and $0$ at every $t > 0$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.hSeqZ`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#h-seq-z).

## The sequence $A_p$

For a natural number $p \ge 1$, $A_p : \mathbb{Z} \to \mathbb{Z}$ is
the unique sequence with $A_p(n) = 0$ for $-p \le n \le 0$ and $A_p(n) = 1$ for $1 \le n \le p$
that satisfies $A_p(n) = A_p(n-1) + A_p(n-p) - A_p(n-2p-1)$ for every integer $n$. For $p = 0$
it is the zero sequence.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.seqAZ`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#seq-az).

## The two-sided sequence $B_p$

For a natural number $p \ge 1$, the sequence $B_p$ of
integers indexed by $\mathbb{Z}$ is the unique solution of the recurrence
$B_p(n) = B_p(n-1) + B_p(n-p) - B_p(n-2p-1)$ for every integer $n$ (the defining recurrence of
the paper's class $H(p)$) with initial values $B_p(n) = 1$ for $1 \le n \le p$,
$B_p(-p+1) = 1$, and $B_p(n) = 0$ for the other integers $n$ with $-p \le n \le 0$.

The definition also accepts $p = 0$, where the recurrence is trivial and the construction has no
mathematical meaning.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.seqBZ`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#seq-bz).

## The companion matrix $Q_p$

For a natural number $p$, $Q_p$ is the $(2p+1) \times (2p+1)$
integer matrix with rows and columns indexed by $0, 1, \dots, 2p$ whose entry $(2p, 0)$ is $-1$,
whose other entries $(0, 0)$, $(p-1, 0)$ and $(i, i+1)$ for $0 \le i < 2p$ are $1$, and whose
remaining entries are $0$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.companionQ`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#companion-q).

## Entry formula for the powers of $Q_p$

For natural numbers $p$ and $n$ and indices
$a, b \in \{0, 1, \dots, 2p\}$, the value is the integer $A_p(n + 1 - b)$ if $a = 0$, the integer
$B_p(n - p + 1 + a - b)$ if $1 \le a \le p - 1$, and the integer $-A_p(n - 2p + a - b)$ otherwise,
where $A_p$ and $B_p$ are the two-sided auxiliary sequences of the generalized Leonardo
$p$-numbers.

This is the formula of Theorem 9 of the source for the $(a, b)$ entry of $Q_p^n$, where $p \ge 2$
and $Q_p$ is the $(2p+1) \times (2p+1)$ companion matrix of the source, with the index direction
along the $B_p$ rows corrected (the source's display reverses it after the first entry).

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.qPowEntry`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#q-pow-entry).

## The Hankel matrix $R_{p,m}$

For a natural number $p$, a sequence
$H : \mathbb{Z} \to \mathbb{Z}$ and a natural number $m$, $R_{p,m}$ is the $(2p+1) \times (2p+1)$
integer matrix, with rows and columns indexed by $0, 1, \dots, 2p$, whose $(a, b)$ entry is
$H(m - a - b)$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.rMatrix`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#r-matrix).

## Generalized Leonardo $p$-numbers in terms of Fibonacci $p$-numbers

For all natural
numbers $p$, $k$ and $n$ with $p \ge 1$ and $k \ge 1$, the generalized Leonardo $p$-number
$\mathcal{L}_{p,k}(n)$ and the Fibonacci $p$-number $F_p(n+1)$ satisfy
$\mathcal{L}_{p,k}(n) = (k+1)F_p(n+1) - k$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.leonardoPK_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pk-eq).

## Partial sums of the generalized Leonardo $p$-numbers

Let $p \ge 1$ and $k \ge 1$ be
natural numbers, and let $\mathcal{L}_{p,k}$ denote the generalized Leonardo $p$-numbers
($\mathcal{L}_{p,k}(j) = 1$ for $0 \le j \le p$ and
$\mathcal{L}_{p,k}(j) = \mathcal{L}_{p,k}(j-1) + \mathcal{L}_{p,k}(j-p-1) + k$ for $j > p$).
Then for every natural number $n$,
$\sum_{i=0}^{n} \mathcal{L}_{p,k}(i) = \mathcal{L}_{p,k}(n+p+1) - k(n+1) - 1$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.sum_leonardoPK` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-leonardo-pk).

## Stride sums of the generalized Leonardo $p$-numbers

Let $p \ge 1$ and $k \ge 1$ be
natural numbers, and let $\mathcal{L}_{p,k}$ denote the generalized Leonardo $p$-numbers
($\mathcal{L}_{p,k}(j) = 1$ for $0 \le j \le p$ and
$\mathcal{L}_{p,k}(j) = \mathcal{L}_{p,k}(j-1) + \mathcal{L}_{p,k}(j-p-1) + k$ for $j > p$).
Then for all natural numbers $m \le p$ and $n$, the sum
$S = \sum_{i=0}^{n} \mathcal{L}_{p,k}((p+1)i + m)$ satisfies
$S = \mathcal{L}_{p,k}((p+1)n + m + 1) - kn$ if $m < p$, and
$S = \mathcal{L}_{p,k}((p+1)(n+1)) - k(n+1) - 1$ if $m = p$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.sum_leonardoPK_stride` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-leonardo-pk-stride).

## Fibonacci $p$-numbers as differences of $A_p$

For all natural numbers $p \ge 1$ and
$n \ge 1$, the Fibonacci $p$-number $F_p(n)$ equals $A_p(n) - A_p(n-p)$. Here
$A_p : \mathbb{Z} \to \mathbb{Z}$ is the sequence with $A_p(t) = 0$ for $-p \le t \le 0$,
$A_p(t) = 1$ for $1 \le t \le p$, and $A_p(t) = A_p(t-1) + A_p(t-p) - A_p(t-2p-1)$ for every
integer $t$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 5.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.fibonacciP_eq_seqAZ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#fibonacci-p-eq-seq-az-sub).

## The sequence $A_p$ as a sum of Fibonacci $p$-numbers

For natural numbers $p$, $j$ and $m$
with $j < p$, the auxiliary sequence $A_p$ and the Fibonacci $p$-numbers $F_p$ satisfy
$A_p(mp + j) = \sum_{i=0}^{m} F_p(ip + j)$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Corollary 6.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.seqAZ_eq_sum_fibonacciP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#seq-az-eq-sum-fibonacci-p).

## Recurrence for the sequence $A_p$

For natural numbers $p \ge 2$ and $n \ge 1$, the
auxiliary sequence $A_p$ satisfies $A_p(n) = A_p(n-1) + A_p(n-p-1) + 1$ if
$n \equiv 1 \pmod p$, and $A_p(n) = A_p(n-1) + A_p(n-p-1)$ otherwise.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Proposition 7.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.seqAZ_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#seq-az-recurrence).

## Recurrence for the sequence $B_p$

For natural numbers $p \ge 2$ and $n \ge 1$, the
auxiliary sequence $B_p$ satisfies $B_p(n) = B_p(n-1) + B_p(n-p-1) + \varepsilon$, where
$\varepsilon = 1$ if $n \equiv 1 \pmod p$, $\varepsilon = -1$ if $n \equiv 2 \pmod p$, and
$\varepsilon = 0$ otherwise. For $p = 2$ this means $\varepsilon = 1$ for odd $n$ and
$\varepsilon = -1$ for even $n$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Proposition 7.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.seqBZ_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#seq-bz-recurrence).

## Relation between the sequences $A_p$ and $B_p$

For natural numbers $p \ge 2$ and $n$,
the auxiliary sequences $A_p$ and $B_p$ satisfy $A_p(n) = B_p(n+1) - 1$ if $p$ divides $n$, and
$A_p(n) = B_p(n+1)$ otherwise.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Proposition 8.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.seqAZ_eq_seqBZ` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#seq-az-eq-seq-bz).

## Entries of the powers of the companion matrix $Q_p$

Let $p \ge 2$ and $n$ be natural
numbers, and index the rows and columns of the $(2p+1) \times (2p+1)$ companion matrix $Q_p$ by
$0, 1, \dots, 2p$. Then for all indices $a$ and $b$, the entry $(a, b)$ of $Q_p^n$ equals
$A_p(n + 1 - b)$ if $a = 0$, equals $B_p(n - p + 1 + a - b)$ if $1 \le a \le p - 1$, and equals
$-A_p(n - (2p - a) - b)$ if $p \le a \le 2p$. Here $A_p, B_p : \mathbb{Z} \to \mathbb{Z}$ are the
sequences satisfying $S(t) = S(t-1) + S(t-p) - S(t-2p-1)$ for every integer $t$, with
$A_p(t) = 1$ for $1 \le t \le p$ and $A_p(t) = 0$ for $-p \le t \le 0$, and with $B_p(t) = 1$ for
$1 \le t \le p$ and for $t = -p+1$ and $B_p(t) = 0$ for the other $-p \le t \le 0$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 9.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.companionQ_pow_apply` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#companion-q-pow-apply).

## Powers of $Q_p$ shift the Hankel matrices $R_{p,m}$

Let $p \ge 2$ be a natural number and
let $H : \mathbb{Z} \to \mathbb{Z}$ satisfy $H(t) = H(t-1) + H(t-p) - H(t-2p-1)$ for every
integer $t$. For a natural number $m$, let $R_{p,m}$ be the $(2p+1) \times (2p+1)$ integer matrix
whose $(a, b)$ entry is $H(m - a - b)$ for $0 \le a, b \le 2p$, and let $Q_p$ be the
$(2p+1) \times (2p+1)$ companion matrix with entries $1$ at $(0, 0)$, at $(p-1, 0)$ and on the
superdiagonal, $-1$ at $(2p, 0)$, and $0$ elsewhere. Then $R_{p,m} Q_p^n = R_{p,m+n}$ for all
natural numbers $m \ge 1$ and $n$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 10.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.rMatrix_mul_companionQ_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#r-matrix-mul-companion-q-pow).

## Convolution identity for sequences in $H(p)$

Let $p \ge 2$ be a natural number and let
$\mathcal{H} : \mathbb{Z} \to \mathbb{Z}$ be a sequence in $H(p)$, that is,
$\mathcal{H}(t) = \mathcal{H}(t-1) + \mathcal{H}(t-p) - \mathcal{H}(t-2p-1)$ for every integer
$t$. Then for all natural numbers $m \ge 1$ and $n \ge 1$,

$$
\mathcal{H}(m+n) = \mathcal{H}(m)A_p(n+1) + \sum_{i=1}^{p-1} \mathcal{H}(m-i)B_p(n-p+i+1) -
\sum_{i=0}^{p} \mathcal{H}(m-p-i)A_p(n-p+i),
$$

where $A_p, B_p : \mathbb{Z} \to \mathbb{Z}$ are the sequences in $H(p)$ with $A_p(t) = 1$ for
$1 \le t \le p$ and $A_p(t) = 0$ for $-p \le t \le 0$, and with $B_p(t) = 1$ for $1 \le t \le p$
and for $t = -p+1$ and $B_p(t) = 0$ for the other $-p \le t \le 0$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Corollary 11.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.h_add_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#h-add-eq).

## Sums of $p+1$ consecutive Fibonacci $p$-numbers

Let $p \ge 1$ and $n \ge 1$ be natural
numbers and let $k$ be a natural number. Let $F_p$ denote the Fibonacci $p$-numbers
($F_p(0) = 0$, $F_p(m) = 1$ for $1 \le m \le p$, and $F_p(m) = F_p(m-1) + F_p(m-p-1)$ for
$m > p$), and let $\mathcal{L}_{p,k}$ denote the generalized Leonardo $p$-numbers
($\mathcal{L}_{p,k}(m) = 1$ for $0 \le m \le p$ and
$\mathcal{L}_{p,k}(m) = \mathcal{L}_{p,k}(m-1) + \mathcal{L}_{p,k}(m-p-1) + k$ for $m > p$).
Then $(k+1) \sum_{i=0}^{p} F_p(n+i) = \mathcal{L}_{p,k}(n+2p-1) + k$.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Lemma 12.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.succ_mul_sum_fibonacciP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#succ-mul-sum-fibonacci-p).

## Generalized Leonardo $p$-numbers at integer arguments

For natural numbers $p$ and $k$
and an integer $z$, the value is the generalized Leonardo $p$-number $\mathcal{L}_{p,k}(z)$ if
$z \ge 0$, and $-k$ if $z < 0$.

For $-p \le z \le -1$ these are the values $\mathcal{L}_{p,k}(z) = -k$ obtained by running the
recurrence $\mathcal{L}_{p,k}(n) = \mathcal{L}_{p,k}(n-1) + \mathcal{L}_{p,k}(n-p-1) + k$
backwards; below $-p$ they need not be, but Theorem 13 of the source only uses arguments
$z \ge -p$.

Formalized by `MathlibExt.NumberTheory.LeonardoPWanted.leonardoPKZ`, a definition declared in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pkz).

## Honsberger-type identity for generalized Leonardo $p$-numbers

Let $p$, $k$, $m$ and $n$
be natural numbers with $p, k, m, n \ge 1$. Write $\mathcal{L}$ for the generalized Leonardo
$p$-numbers $\mathcal{L}_{p,k}$, extended to negative integers by $\mathcal{L}(t) = -k$ for
$t < 0$. Then

$$
\mathcal{L}(m)\mathcal{L}(n+1) + \sum_{i=1}^{p} \mathcal{L}(m-i)\mathcal{L}(n-p+i) =
(k+1)\mathcal{L}(m+n+1) - k\bigl(\mathcal{L}(m+p) + \mathcal{L}(n+p+1)\bigr) + pk^2 + k.
$$

The arguments that occur are at least $-p$, and on $[-p, -1]$ the value $-k$ is the one forced by
the recurrence $\mathcal{L}(t) = \mathcal{L}(t-1) + \mathcal{L}(t-p-1) + k$ read backwards. The
paper prints the summation index as $j$ in $\mathcal{L}(m-j)$; it is corrected to $i$ here.

## Sources

- "On Generalized Leonardo `p`-Numbers", Journal of Integer Sequences 27 (2024), Article 24.4.6, Theorem 13.

Stated but not proved: `MathlibExt.NumberTheory.LeonardoPWanted.leonardoPK_honsberger` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pk-honsberger).

## Lucas-type recurrence lists

Let $\alpha$ be a type with a zero, a one and an addition, let
$p$ be a natural number and let $a_0, c \in \alpha$. Define $a_i = 1$ for $1 \le i \le p$ and
$a_n = a_{n-1} + a_{n-p-1} + c$ for $n > p$. For every natural number $n$, the Lucas-type list
with parameters $p$, $a_0$, $c$ ending at index $n$ is $[a_0, a_1, \dots, a_n]$.

The list is built by appending one value per step, so each earlier value is computed once and
evaluation is quadratic in $n$, not exponential as with the naive two-branch recursion. The
Lucas and Lucas-Leonardo $p$-numbers are the cases $c = 0$ and $c = p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Section 1, display (5).

Formalized by `MetaMathlibExt.lucasTypeSeq`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-type-seq).

## Length of a Lucas-type list

For every type $\alpha$ with a zero, a one and an addition,
every natural number $p$, all $a_0, c \in \alpha$ and every natural number $n$, the Lucas-type
list with parameters $p$, $a_0$, $c$ ending at index $n$ has exactly $n + 1$ entries.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasTypeSeq_length`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-type-seq-length).

## Entries of a Lucas-type list do not depend on its length

Let $\alpha$ be a type with a
zero, a one and an addition, let $p$ be a natural number and let $a_0, c \in \alpha$. For natural
numbers $i \le n$, the entry at index $i$ of the Lucas-type list with parameters $p$, $a_0$, $c$
ending at index $n$ equals the entry at index $i$ of the Lucas-type list ending at index $i$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasTypeSeq_getD`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-type-seq-get-d).

## Last entry of a Lucas-type list

Let $\alpha$ be a type with a zero, a one and an
addition, let $p$ be a natural number and let $a_0, c \in \alpha$. Write $S_m$ for the Lucas-type
list with parameters $p$, $a_0$, $c$ ending at index $m$, and $S_m[i]$ for its entry at index $i$.
Then for every natural number $n$, $S_{n+1}[n+1] = 1$ if $n + 1 \le p$, and otherwise
$S_{n+1}[n+1] = S_n[n] + S_{n-p}[n-p] + c$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasTypeSeq_getD_succ`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-type-seq-get-d-succ).

## Lucas $p$-numbers

For a natural number $p$, the Lucas $p$-numbers are the natural numbers
$L_{p,n}$ given by $L_{p,0} = p + 1$, $L_{p,i} = 1$ for $1 \le i \le p$, and
$L_{p,n} = L_{p,n-1} + L_{p,n-p-1}$ for $n > p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Section 1 (after (6)).

Formalized by `MetaMathlibExt.lucasP`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-p).

## Initial Lucas $p$-number

For every natural number $p$, the Lucas $p$-number $L_{p,0}$
equals $p + 1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasP_zero`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-p-zero).

## Lucas $p$-numbers at indices $1$ to $p$

For every natural number $p$ and every $n$ with
$1 \le n \le p$, the Lucas $p$-number $L_{p,n}$ equals $1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasP_of_le`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-p-of-le).

## Recurrence for the Lucas $p$-numbers

For every natural number $p$, write $L_{p,n}$ for
the Lucas $p$-numbers. Then $L_{p,n} = L_{p,n-1} + L_{p,n-p-1}$ for every $n > p$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasP_of_lt`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-p-of-lt).

## Lucas-Leonardo $p$-numbers

For a natural number $p$, the Lucas-Leonardo $p$-numbers are
the integers $R_{p,n}$ given by $R_{p,0} = p^2 + p + 1$, $R_{p,i} = 1$ for $1 \le i \le p$, and
$R_{p,n} = R_{p,n-1} + R_{p,n-p-1} + p$ for $n > p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Section 1, display (5).

Formalized by `MetaMathlibExt.lucasLeonardoP`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-p).

## Initial Lucas-Leonardo $p$-number

For every natural number $p$, the Lucas-Leonardo
$p$-number $R_{p,0}$ equals $p^2 + p + 1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, display (5).

Formalized by `MetaMathlibExt.lucasLeonardoP_zero`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-p-zero).

## Lucas-Leonardo $p$-numbers at indices $1$ to $p$

For every natural number $p$ and every
$n$ with $1 \le n \le p$, the Lucas-Leonardo $p$-number $R_{p,n}$ equals $1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, display (5).

Formalized by `MetaMathlibExt.lucasLeonardoP_of_le`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-p-of-le).

## Recurrence for the Lucas-Leonardo $p$-numbers

For every natural number $p$, write
$R_{p,n}$ for the Lucas-Leonardo $p$-numbers. Then $R_{p,n} = R_{p,n-1} + R_{p,n-p-1} + p$ for
every $n > p$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, display (5).

Formalized by `MetaMathlibExt.lucasLeonardoP_of_lt`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-p-of-lt).

## First values of the Lucas and Lucas-Leonardo $1$-numbers

The Lucas $1$-numbers
$L_{1,0}, \dots, L_{1,5}$ are $2, 1, 3, 4, 7, 11$, and the Lucas-Leonardo $1$-numbers
$R_{1,0}, \dots, R_{1,5}$ are $3, 1, 5, 7, 13, 21$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 1.

Formalized by `MetaMathlibExt.lucasP_lucasLeonardoP_one_values`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-p-lucas-leonardo-p-one-values).

## Incomplete Leonardo p-numbers

For natural numbers $p$, $n$ and $k$, the incomplete
Leonardo $p$-number is the integer

$$
\mathcal{L}_{p,n}(k) = (p + 1) \sum_{i=0}^{k} \binom{\max(n - pi, 0)}{i} - p.
$$

On the paper's range $0 \le k \le \lfloor n/(p+1) \rfloor$ the maximum is always $n - pi$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, display (4).

Formalized by `MetaMathlibExt.incompleteLeonardoP`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#incomplete-leonardo-p).

## Incomplete Leonardo p-numbers at zero

For all natural numbers $p$ and $n$, the
incomplete Leonardo $p$-number $\mathcal{L}_{p,n}(0)$ equals $1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, display (4).

Formalized by `MetaMathlibExt.incompleteLeonardoP_zero`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#incomplete-leonardo-p-zero).

## Incomplete Lucas-Leonardo p-numbers

For natural numbers $p$, $n$ and $k$, the
incomplete Lucas-Leonardo $p$-number is the rational number

$$
R_{p,n}(k) = (p + 1) \sum_{i=0}^{k} \frac{n}{m_i} \binom{m_i}{i} - p, \qquad m_i = \max(n - pi, 0),
$$

where a summand with $m_i = 0$ is taken to be $0$. On the paper's range
$0 \le k \le \lfloor n/(p+1) \rfloor$ with $n \ge 1$, every $m_i$ is positive.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, display (8).

Formalized by `MetaMathlibExt.incompleteLucasLeonardoP`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#incomplete-lucas-leonardo-p).

## Incomplete Lucas-Leonardo p-numbers at zero

For every natural number $p$ and every
natural number $n \ge 1$, the incomplete Lucas-Leonardo $p$-number $R_{p,n}(0)$ equals $1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, display (8).

Formalized by `MetaMathlibExt.incompleteLucasLeonardoP_zero`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#incomplete-lucas-leonardo-p-zero).

## Hyper Leonardo $p$-numbers

For natural numbers $p$, $n$ and $k$, the hyper Leonardo
$p$-number is the integer

$$\mathcal{L}^{(k)}_{p,n} = (p + 1) \sum_{i=0}^{\lfloor n/(p+1) \rfloor}
\binom{n + k - pi}{i + k} - p \binom{n + k}{k}.$$

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, display (12) (quoting Belaggoun and Belbachir).

Formalized by `MetaMathlibExt.hyperLeonardoP`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-leonardo-p).

## Hyper Leonardo $p$-numbers at $n = 0$

For all natural numbers $p$ and $k$, the hyper
Leonardo $p$-number $\mathcal{L}^{(k)}_{p,0}$ equals $1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, display (12) and Proposition 10.

Formalized by `MetaMathlibExt.hyperLeonardoP_zero_left`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-leonardo-p-zero-left).

## Hyper Lucas-Leonardo p-numbers

For natural numbers $p$, $n$ and $k$, the hyper
Lucas-Leonardo $p$-number $R^{(k)}_{p,n}$ is the rational number defined by
$R^{(0)}_{p,n} = R_{p,n}$, the Lucas-Leonardo $p$-number; $R^{(k)}_{p,0} = p^2 + p + 1$ for
$k \ge 1$; and, for $n \ge 1$ and $k \ge 1$,

$$
R^{(k)}_{p,n} = (p + 1) \sum_{i=0}^{\lfloor n/(p+1) \rfloor} \frac{n + (p+1)k}{n + k - pi}
\binom{n + k - pi}{i + k} - p \binom{n + k}{k}.
$$

For $p = 2$ this reproduces the values listed in the paper. For $p = 1$ the listed values $122$
(for $R^{(1)}_{1,7}$), $101, 186, 308$ (for $R^{(2)}_{1,5}, R^{(2)}_{1,6}, R^{(2)}_{1,7}$) and
$220, 406, 714$ (for $R^{(3)}_{1,5}, R^{(3)}_{1,6}, R^{(3)}_{1,7}$) are misprints: the definition
gives $142$; $111, 196, 338$; and $230, 426, 764$, the values that the recurrence
$R^{(k)}_{1,n} = R^{(k)}_{1,n-1} + R^{(k-1)}_{1,n}$ produces from the paper's own earlier
entries.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Definition 2.

Formalized by `MetaMathlibExt.hyperLucasLeonardoP`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-lucas-leonardo-p).

## Hyper Lucas–Leonardo $p$-numbers at $n = 0$

For all natural numbers $p$ and $k$, the
hyper Lucas–Leonardo $p$-number $R^{(k)}_{p,0}$ equals $p^2 + p + 1$.

For $k = 0$ this is the initial value $R_{p,0} = p^2 + p + 1$ of the Lucas–Leonardo $p$-numbers.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Definition 2.

Formalized by `MetaMathlibExt.hyperLucasLeonardoP_zero_left`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-lucas-leonardo-p-zero-left).

## Hyper Lucas-Leonardo p-numbers of order zero

For all natural numbers $p$ and $n$, the
hyper Lucas-Leonardo $p$-number of order $0$ equals the Lucas-Leonardo $p$-number:
$R^{(0)}_{p,n} = R_{p,n}$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Definition 2.

Formalized by `MetaMathlibExt.hyperLucasLeonardoP_zero_right`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-lucas-leonardo-p-zero-right).

## Leonardo $p$-tilings

For natural numbers $p$ and $n$, the tiling set $K_{p,n}$ consists
of the linear tilings of an $n$-board by squares (length $1$), $p$-minos (length $p + 1$) and at
most one $p$-tile, which comes in one of $p$ colors, has length at least $p + 1$, and can only be
the initial piece. A tiling is recorded as its initial $p$-tile, given by its color and length,
if there is one, followed by the sequence of the remaining pieces read from left to right, each a
square or a $p$-mino; the lengths of all pieces sum to $n$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Definition 1 and the set `K_{p,n}` before Proposition 1.

Formalized by `MetaMathlibExt.leonardoPTilings`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-ptilings).

## The all-squares tiling is a Leonardo $p$-tiling

For all natural numbers $p$ and $n$, the
linear tiling of an $n$-board by $n$ squares, with no $p$-tile, lies in the tiling set $K_{p,n}$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 2.

Formalized by `MetaMathlibExt.replicate_mem_leonardoPTilings`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#replicate-mem-leonardo-ptilings).

## First tile of a bracelet

For a natural number $p$, a first tile records the tile of a
bracelet that covers cell $1$ of the circular board, together with its phase (which cell of the
tile covers cell $1$). It is one of: a curved square, in phase $1$; a curved $p$-mino of length
$p + 1$ in phase $r + 1$ for some $0 \le r \le p$; a curved $p$-tile of length $p + 1$ in color
$c$ for some $0 \le c < p$ and phase $r + 1$ for some $0 \le r \le p$; or a curved $p$-tile of
length $l$ in color $c$ for some $0 \le c < p$ and some natural number $l$, starting at cell $1$
(phase $1$).

The restriction $l \ge p + 2$ on the last kind is not part of this type; the bracelet sets
impose it.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Section 3.

Formalized by `MetaMathlibExt.BraceletFirstTile`, an inductive type declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#bracelet-first-tile).

## Length of the first tile of a bracelet

For a natural number $p$, the length of the first
tile of a bracelet is $1$ for a curved square, $p + 1$ for a curved $p$-mino in any phase,
$p + 1$ for a curved $p$-tile of length $p + 1$ in any color and phase, and $l$ for a curved
$p$-tile of length $l$ (in any color) starting at cell $1$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 3.

Formalized by `MetaMathlibExt.BraceletFirstTile.length`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#length).

## Lucas–Leonardo bracelets

For natural numbers $p$ and $n$, the bracelet set $B_{p,n}$
consists of the tilings of a circular $n$-board by curved squares (length $1$), curved $p$-minos
(length $p + 1$) and at most one curved $p$-tile, which comes in one of $p$ colors and has either
length $p + 1$, in any of its $p + 1$ phases, or length $l \ge p + 2$, starting at cell $1$; a
$p$-tile, if present, is the first tile. A bracelet is recorded as its first tile, the one
covering cell $1$, together with its phase, followed by the sequence of the remaining pieces read
clockwise, each a curved square or a curved $p$-mino; the lengths of all pieces sum to $n$. In
particular $B_{p,0}$ is empty.

The source sets $|B_{p,0}| = p^2 + p + 1$ by convention; that value is not modelled here.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Section 3, the set `B_{p,n}` before Proposition 12.

Formalized by `MetaMathlibExt.lucasLeonardoBracelets`, a definition declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-bracelets).

## The all-squares bracelet is a Lucas–Leonardo bracelet

For every natural number $p$ and
every natural number $n \ge 1$, the bracelet whose first tile is a curved square covering cell $1$
and whose remaining $n - 1$ pieces are all curved squares lies in the bracelet set $B_{p,n}$.

## Sources

- Belkhir and Tan, INTEGERS 25 (2025), Article A57, Section 3.

Formalized by `MetaMathlibExt.square_replicate_mem_lucasLeonardoBracelets`, a theorem declared in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#square-replicate-mem-lucas-leonardo-brac).

## Counting Leonardo $p$-tilings

For all natural numbers $p \ge 1$ and $n$, let $K_{p,n}$ be
the set of linear tilings of an $n$-board by squares (length $1$), $p$-minos (length $p + 1$) and
at most one $p$-tile, which comes in one of $p$ colors, has length at least $p + 1$ and can only
be the initial piece. Then the number of tilings in $K_{p,n}$ equals the Leonardo $p$-number
$\mathcal{L}_{p,n}$, the generalized Leonardo $p$-number $\mathcal{L}_{p,k}(n)$ at $k = p$:
$\mathcal{L}_{p,n} = 1$ for $n \le p$ and
$\mathcal{L}_{p,n} = \mathcal{L}_{p,n-1} + \mathcal{L}_{p,n-p-1} + p$ for $n > p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 1.

Stated but not proved: `MetaMathlibExt.card_leonardoPTilings` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#card-leonardo-ptilings).

## Homogeneous recurrence for the Leonardo $p$-numbers

Let $p \ge 1$ and write
$\mathcal{L}_{p,n}$ for the Leonardo $p$-number $\mathcal{L}_{p,p}(n)$, the generalized Leonardo
$p$-number with $k = p$. Then $\mathcal{L}_{p,n} = \mathcal{L}_{p,n-1} + \mathcal{L}_{p,n-p} -
\mathcal{L}_{p,n-2p-1}$ for every $n \ge 2p + 1$, $\mathcal{L}_{p,i} = 1$ for every $i \le p$,
and $\mathcal{L}_{p,p+j} = (j + 1) + jp$ for every $j$ with $1 \le j \le p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 2.

Stated but not proved: `MetaMathlibExt.leonardoPK_self_homogeneous` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pk-self-homogeneous).

## Recurrence for incomplete Leonardo p-numbers

For natural numbers $p \ge 1$, $n > p$ and
$k \le \lfloor n/(p+1) \rfloor$, the incomplete Leonardo $p$-numbers $\mathcal{L}_{p,m}(j)$
satisfy

$$
\mathcal{L}_{p,n}(k + 1) = \mathcal{L}_{p,n-1}(k + 1) + \mathcal{L}_{p,n-p-1}(k) + p.
$$

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 6.

Stated but not proved: `MetaMathlibExt.incompleteLeonardoP_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#incomplete-leonardo-p-succ).

## Binomial sum identity for incomplete Leonardo p-numbers

For natural numbers $p \ge 1$,
$n$, $r$ and $k$ with $n \ge p + r$ and $k \le \lfloor (n - p - r)/(p + 1) \rfloor$, the
incomplete Leonardo $p$-numbers $\mathcal{L}_{p,m}(j)$ satisfy

$$
\sum_{i=0}^{r} \binom{r}{i} \mathcal{L}_{p,n+pi}(k + i) + (2^r - 1) p =
\mathcal{L}_{p,n+(p+1)r}(k + r).
$$

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 7.

Stated but not proved: `MetaMathlibExt.sum_choose_mul_incompleteLeonardoP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-choose-mul-incomplete-leonardo-p).

## Partial sums of incomplete Leonardo p-numbers

For natural numbers $p \ge 1$, $n$, $k$ and
$r$ with $n \ge (p + 1)(k + 1)$, the incomplete Leonardo $p$-numbers $\mathcal{L}_{p,m}(j)$
satisfy

$$
\sum_{i=0}^{r-1} \mathcal{L}_{p,n-p+i}(k) + rp =
\mathcal{L}_{p,n+r}(k + 1) - \mathcal{L}_{p,n}(k + 1),
$$

where the sum is empty when $r = 0$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 8.

Stated but not proved: `MetaMathlibExt.sum_incompleteLeonardoP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-incomplete-leonardo-p).

## Binomial addition formula for hyper Leonardo $p$-numbers

For natural numbers $p \ge 1$,
$n \ge 1$, $m \ge 1$ and $k \ge m$, the hyper Leonardo $p$-numbers satisfy

$$\mathcal{L}^{(k)}_{p,n+m} = \sum_{i=0}^{m} \binom{m}{i} \mathcal{L}^{(k-i)}_{p,n+i}.$$

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 9.

Stated but not proved: `MetaMathlibExt.hyperLeonardoP_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-leonardo-p-add).

## Recurrence for the hyper Leonardo $p$-numbers

Let $p \ge 1$ be a natural number. For all
natural numbers $n \ge 1$ and $k \ge 1$, the hyper Leonardo $p$-numbers satisfy
$\mathcal{L}^{(k)}_{p,n} = \mathcal{L}^{(k)}_{p,n-1} + \mathcal{L}^{(k-1)}_{p,n}$, and for every
natural number $n$, $\mathcal{L}^{(0)}_{p,n} = \mathcal{L}_{p,n}$, where $\mathcal{L}_{p,n}$ is the
Leonardo $p$-number: $\mathcal{L}_{p,n} = 1$ for $n \le p$ and
$\mathcal{L}_{p,n} = \mathcal{L}_{p,n-1} + \mathcal{L}_{p,n-p-1} + p$ for $n > p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 10.

Stated but not proved: `MetaMathlibExt.hyperLeonardoP_rec` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-leonardo-p-rec).

## Leonardo p-numbers split into incomplete and hyper parts

For natural numbers $p \ge 1$,
$n > p$ and $k \ge 1$, let $N = n + (p + 1)k$. Then

$$
\mathcal{L}_{p,N} = \mathcal{L}_{p,N}(k - 1) + \mathcal{L}^{(k)}_{p,n} + p \binom{n + k}{k},
$$

where $\mathcal{L}_{p,N}$ is the Leonardo $p$-number (the generalized Leonardo $p$-numbers with
additive constant $p$: $\mathcal{L}_{p,m} = 1$ for $m \le p$ and
$\mathcal{L}_{p,m} = \mathcal{L}_{p,m-1} + \mathcal{L}_{p,m-p-1} + p$ for $m > p$),
$\mathcal{L}_{p,N}(k - 1)$ is the incomplete Leonardo $p$-number and $\mathcal{L}^{(k)}_{p,n}$ is
the hyper Leonardo $p$-number.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 11.

Stated but not proved: `MetaMathlibExt.leonardoPK_eq_incomplete_add_hyper` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#leonardo-pk-eq-incomplete-add-hyper).

## Counting Lucas–Leonardo bracelets

For all natural numbers $p \ge 1$ and $n \ge 1$, let
$B_{p,n}$ be the set of tilings of a circular $n$-board by curved squares (length $1$), curved
$p$-minos (length $p + 1$) and at most one curved $p$-tile in one of $p$ colors, which if present
is the tile covering cell $1$ and either has length $p + 1$, in any of its $p + 1$ phases, or has
length at least $p + 2$ and starts at cell $1$. Then the number of bracelets in $B_{p,n}$ equals
the Lucas–Leonardo $p$-number $R_{p,n}$, given by $R_{p,0} = p^2 + p + 1$, $R_{p,i} = 1$ for
$1 \le i \le p$ and $R_{p,n} = R_{p,n-1} + R_{p,n-p-1} + p$ for $n > p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 12.

Stated but not proved: `MetaMathlibExt.card_lucasLeonardoBracelets` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#card-lucas-leonardo-bracelets).

## Lucas-Leonardo $p$-numbers from Lucas $p$-numbers

For every $p \ge 1$ and every
natural number $n$, the Lucas-Leonardo $p$-number $R_{p,n}$ and the Lucas $p$-number $L_{p,n}$
satisfy $R_{p,n} = (p + 1) L_{p,n} - p$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 13.

Stated but not proved: `MetaMathlibExt.lucasLeonardoP_eq_lucasP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-p-eq-lucas-p).

## Lucas-Leonardo $p$-numbers from Leonardo $p$-numbers

Let $p \ge 1$, let $R_{p,n}$ denote
the Lucas-Leonardo $p$-numbers, and let $\mathcal{L}_{p,n}$ denote the Leonardo $p$-numbers
$\mathcal{L}_{p,p}(n)$ (the generalized Leonardo $p$-numbers with $k = p$), extended to $n = -1$
by $\mathcal{L}_{p,-1} = -p$. Then $R_{p,n} = (p + 1) \mathcal{L}_{p,n} - p \mathcal{L}_{p,n-1}$
for every natural number $n$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 14.

Stated but not proved: `MetaMathlibExt.lucasLeonardoP_eq_leonardoPK` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#lucas-leonardo-p-eq-leonardo-pk).

## Sum of the Lucas-Leonardo p-numbers

For every natural number $p \ge 1$ and every natural
number $n$, the Lucas-Leonardo $p$-numbers $R_{p,m}$ satisfy
$\sum_{i=0}^{n} R_{p,i} = R_{p,n+p+1} - p(n + 1) - 1$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 15.

Stated but not proved: `MetaMathlibExt.sum_lucasLeonardoP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-lucas-leonardo-p).

## Sum of the Lucas-Leonardo p-numbers at multiples of $p + 1$

For every natural number
$p \ge 1$ and every natural number $n$, the Lucas-Leonardo $p$-numbers $R_{p,m}$ satisfy
$\sum_{i=0}^{n} R_{p,(p+1)i} = R_{p,(p+1)n+1} - p(n - p - 1)$, an identity of integers.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 16.

Stated but not proved: `MetaMathlibExt.sum_lucasLeonardoP_stride` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-lucas-leonardo-p-stride).

## Recurrence for incomplete Lucas-Leonardo p-numbers

For natural numbers $p \ge 1$,
$n > p + 1$ and $k \le \lfloor n/(p+1) \rfloor$, the incomplete Lucas-Leonardo $p$-numbers
$R_{p,m}(j)$ satisfy

$$
R_{p,n}(k + 1) = R_{p,n-1}(k + 1) + R_{p,n-p-1}(k) + p.
$$

At $n = p + 1$ the term $R_{p,0}(k)$ would contain the undefined summand
$\frac{0}{0} \binom{0}{0}$, so that case is excluded.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 17.

Stated but not proved: `MetaMathlibExt.incompleteLucasLeonardoP_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#incomplete-lucas-leonardo-p-succ).

## Binomial sum identity for incomplete Lucas-Leonardo p-numbers

For natural numbers
$p \ge 1$, $n$, $r$ and $k$ with $n \ge p + r$ and $k \le \lfloor (n - p - r)/(p + 1) \rfloor$,
the incomplete Lucas-Leonardo $p$-numbers $R_{p,m}(j)$ satisfy, as rational numbers,

$$
\sum_{i=0}^{r} \binom{r}{i} R_{p,n+pi}(k + i) + (2^r - 1) p = R_{p,n+(p+1)r}(k + r).
$$

The paper prints the range as $0 \le n \le \lfloor (n - p - r)/(p + 1) \rfloor$; the first $n$
is read as $k$, as in Proposition 7.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 18.

Stated but not proved: `MetaMathlibExt.sum_choose_mul_incompleteLucasLeonardoP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#sum-choose-mul-incomplete-lucas-leonardo).

## Hyper Lucas–Leonardo numbers from incomplete ones

For natural numbers $p \ge 1$, $n > p$
and $k \ge 1$, write $R_{p,m}$ for the Lucas–Leonardo $p$-numbers and $R_{p,m}(j)$ for the
incomplete Lucas–Leonardo $p$-numbers. Then the hyper Lucas–Leonardo $p$-number $R^{(k)}_{p,n}$
satisfies

$$R^{(k)}_{p,n} = R_{p,n+(p+1)k} - R_{p,n+(p+1)k}(k - 1) - p \binom{n + k}{k}.$$

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 19.

Stated but not proved: `MetaMathlibExt.hyperLucasLeonardoP_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-lucas-leonardo-p-eq).

## Hyper Lucas–Leonardo numbers from hyper Leonardo numbers

For natural numbers $p \ge 1$,
$n > p$ and $k \ge 1$, the hyper Lucas–Leonardo $p$-number $R^{(k)}_{p,n}$ and the hyper
Leonardo $p$-numbers $\mathcal{L}^{(k)}_{p,n}$ satisfy

$$R^{(k)}_{p,n} = (p + 1) \mathcal{L}^{(k)}_{p,n} - p \mathcal{L}^{(k)}_{p,n-1} +
p^2 \binom{n + k - 1}{k - 1}.$$

The paper prints the binomial as $\binom{n + k - 1}{k}$, which is false: at $p = 1$, $n = 2$,
$k = 1$ one has $R^{(1)}_{1,2} = 9$ while the printed right side is $10$. The paper's own proof
ends with $p^2 \binom{n + k - 1}{k - 1}$.

## Sources

- Amine Belkhir and Elif Tan, *Combinatorial Insights into Leonardo `p`-Numbers and Lucas-Leonardo `p`-Numbers*, INTEGERS 25 (2025), Article A57, Proposition 20.

Stated but not proved: `MetaMathlibExt.hyperLucasLeonardoP_eq_hyperLeonardoP` is written with `theorem_wanted` in [WantedExt/NumberTheory/LeonardoPTilingsWanted.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LeonardoPTilingsWanted.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#hyper-lucas-leonardo-p-eq-hyper-leonardo).

## Supergeneralized Leonardo p-numbers

For natural numbers $p$ and $k$ and a real sequence
$x = (x_n)_{n \in \mathbb{N}}$, the supergeneralized Leonardo $p$-numbers are the real numbers
$\mathcal{L}_{p,k,x}(n)$, $n \in \mathbb{N}$, given by $\mathcal{L}_{p,k,x}(n) = x_n$ for
$n \le p$ and $\mathcal{L}_{p,k,x}(n) = \mathcal{L}_{p,k,x}(n-1) + \mathcal{L}_{p,k,x}(n-p-1) + k$
for $n > p$. Only the initial values $x_0, \dots, x_p$ are used.

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Definition 1.

Formalized by `MetaMathlibExt.superLeonardoP`, a definition declared in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p).

## Initial values of the supergeneralized Leonardo p-numbers

For all natural numbers $p$,
$k$ and $n$ with $n \le p$ and every real sequence $x$, the supergeneralized Leonardo $p$-number
$\mathcal{L}_{p,k,x}(n)$ equals $x_n$.

## Sources

- Schütz and Kelly, Journal of Integer Sequences 28 (2025), Article 25.8.2, Definition 1.

Formalized by `MetaMathlibExt.superLeonardoP_of_le`, a theorem declared in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-of-le).

## Recurrence for the supergeneralized Leonardo p-numbers

For all natural numbers $p$, $k$
and $n$ with $n > p$ and every real sequence $x$, the supergeneralized Leonardo $p$-numbers
$\mathcal{L}_{p,k,x}$ satisfy
$\mathcal{L}_{p,k,x}(n) = \mathcal{L}_{p,k,x}(n-1) + \mathcal{L}_{p,k,x}(n-p-1) + k$.

## Sources

- Schütz and Kelly, Journal of Integer Sequences 28 (2025), Article 25.8.2, Definition 1.

Formalized by `MetaMathlibExt.superLeonardoP_of_lt`, a theorem declared in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-of-lt).

## Reduction of supergeneralized Leonardo p-numbers to the homogeneous case

Let $p \ge 1$
and $k$ be natural numbers, $x$ a real sequence, $y$ the real sequence $y_i = i + 1$, and write
$\mathcal{L}_{p,k,x}(n)$ for the supergeneralized Leonardo $p$-numbers. For every natural number
$n$, $\mathcal{L}_{p,k,x}(n) = \mathcal{L}_{p,0,x}(n)$ if $n \le p$, and
$\mathcal{L}_{p,k,x}(n) = \mathcal{L}_{p,0,x}(n) + \mathcal{L}_{p,1,y}(n-(p+1)) \cdot k$ if $n > p$.

The paper writes the correction term as $\max\{0, \mathcal{L}_{p,1,y}(n-(p+1))\} \cdot k$ with
$y = (1, \dots, p + 1)$ and sets $\mathcal{L} \le 0$ at negative indices, so the correction term
is $0$ for $n \le p$; for $n > p$ the $\max$ is redundant since $\mathcal{L}_{p,1,y}$ is positive.

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Theorem 3.

Stated but not proved: `MetaMathlibExt.superLeonardoP_eq_add_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-eq-add-mul).

## Homogeneous supergeneralized Leonardo p-numbers via Fibonacci p-numbers

For all
natural numbers $p \ge 1$ and $n$ and every real sequence $x$, the supergeneralized Leonardo
$p$-numbers $\mathcal{L}_{p,0,x}$ with $k = 0$ satisfy $\mathcal{L}_{p,0,x}(n) = x_n$ if
$n \le p$, and if $n > p$, with $F_p$ denoting the Fibonacci $p$-numbers,

$$\mathcal{L}_{p,0,x}(n) = F_p(n-p+1)\,x_p + \sum_{i=0}^{\min(p-1,\,n-p-1)} F_p(n-p-i)\,x_i.$$

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Theorem 4.

Stated but not proved: `MetaMathlibExt.superLeonardoP_zero_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-zero-eq).

## Binomial sum for supergeneralized Leonardo p-numbers with linear initial values

Let
$p \ge 1$ be a natural number and $y$ the real sequence $y_i = i + 1$, so that the initial values
are $y_0, \dots, y_p = 1, \dots, p + 1$. For every natural number $n$, the supergeneralized
Leonardo $p$-numbers $\mathcal{L}_{p,1,y}$ with $k = 1$ and initial values $y$ satisfy

$$\mathcal{L}_{p,1,y}(n) = \sum_{i=0}^{\lfloor (n+1)/(p+1) \rfloor} \binom{n+1-pi}{i+1}.$$

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Theorem 5.

Stated but not proved: `MetaMathlibExt.superLeonardoP_one_succ_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-one-succ-eq-sum-choose).

## Schütz–Kelly binomial sum identity

For all natural numbers $J$, $n$ and $p$,

$$1 + \sum_{i=0}^{J} \binom{\max(n-pi,\,0)}{i+1} + \sum_{i=0}^{J-1} \binom{\max(n-pi-p,\,0)}{i+1} =
\sum_{i=0}^{J} \binom{\max(n-pi,\,0)+1}{i+1}.$$

Truncating the upper indices at $0$ makes a negative upper index give $\binom{0}{i+1} = 0$,
matching the paper's binomials. The identity is stated for all natural $J$, $n$, $p$, which
includes the value $0$ beyond the paper's positive range.

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Lemma 6.

Stated but not proved: `MetaMathlibExt.one_add_sum_choose_add_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#one-add-sum-choose-add-sum-choose).

## Supergeneralized Leonardo p-numbers via Fibonacci p-numbers

For all natural numbers
$p \ge 1$, $k$ and $n$ with $n > p$ and every real sequence $x$, the supergeneralized Leonardo
$p$-numbers $\mathcal{L}_{p,k,x}$ and the Fibonacci $p$-numbers $F_p$ satisfy

$$\mathcal{L}_{p,k,x}(n) = F_p(n-p+1)\,x_p + \sum_{i=0}^{\min(p-1,\,n-p-1)} F_p(n-p-i)\,x_i +
\max\Big\{0, \sum_{j=0}^{\lfloor (n-p)/(p+1) \rfloor} \binom{n-p-pj}{j+1}\Big\} \cdot k.$$

This is Corollary 7 of the paper with the factor $k$ restored. The printed corollary omits the
factor $k$ on the last term (and reuses $k$ as the summation index); without it the identity
fails, e.g. at $p = 1$, $k = 2$, $n = 2$, $x = (1, 1)$: $\mathcal{L}_{p,k,x}(n) = 4$ but the
printed right side is $3$. The factor is the one in Theorem 3, of which the corollary is stated
to be an immediate combination with Theorems 4 and 5.

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Corollary 7.

Stated but not proved: `MetaMathlibExt.superLeonardoP_eq_fibonacciP_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-eq-fibonacci-p-sum).

## Binomial sum formula for Fibonacci p-numbers

For all natural numbers $p \ge 1$ and $n$,
the Fibonacci $p$-numbers $F_p$ satisfy

$$F_p(n+1) = \sum_{i=0}^{\lfloor n/(p+1) \rfloor} \binom{n-ip}{i}.$$

The paper (Theorem 8, quoting Kuhapatanakul) also gives the form
$F_p(n) = \sum_{i=0}^{\lfloor (n-1)/(p+1) \rfloor} \binom{n-1-ip}{i}$, which is the same identity
with $n$ shifted by one. The paper allows all natural $p$, but at $p = 0$ the sequence is
identically zero ($F_0(1) = F_0(0) + F_0(0) = 0$) while the sum at $n = 0$ is
$\binom{0}{0} = 1$, so $p \ge 1$ is assumed.

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Theorem 8 (Kuhapatanakul).

Stated but not proved: `MetaMathlibExt.fibonacciP_succ_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#fibonacci-p-succ-eq-sum-choose).

## Explicit formula for the supergeneralized Leonardo p-numbers

For all natural numbers
$p \ge 1$, $k$ and $n$ with $n > p$ and every real sequence $x$, the supergeneralized Leonardo
$p$-numbers $\mathcal{L}_{p,k,x}$ satisfy

$$\mathcal{L}_{p,k,x}(n) =
\Big(\sum_{i=0}^{\lfloor (n-p)/(p+1) \rfloor} \binom{n-p-ip}{i}\Big) x_p +
\sum_{i=0}^{\min(p-1,\,n-p-1)} \Big(\sum_{j=0}^{\lfloor (n-p-i-1)/(p+1) \rfloor}
\binom{n-p-i-1-jp}{j}\Big) x_i +
\max\Big\{0, \sum_{j=0}^{\lfloor (n-p)/(p+1) \rfloor} \binom{n-p-pj}{j+1}\Big\} \cdot k.$$

This is Theorem 9 of the paper with the factor $k$ restored: as in Corollary 7, the printed
theorem omits the factor $k$ on the last term and is false without it (same counterexample:
$p = 1$, $k = 2$, $n = 2$, $x = (1, 1)$ gives $4$ versus $3$).

## Sources

- Clemens Schütz and Kristian Kelly, *An Explicit Formula for Supergeneralized Leonardo `p`-numbers*, Journal of Integer Sequences 28 (2025), Article 25.8.2, Theorem 9.

Stated but not proved: `MetaMathlibExt.superLeonardoP_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperLeonardoPWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SuperLeonardoPWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html#super-leonardo-p-eq-sum-choose).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Leonardo p-numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/leonardo-p-numbers)
