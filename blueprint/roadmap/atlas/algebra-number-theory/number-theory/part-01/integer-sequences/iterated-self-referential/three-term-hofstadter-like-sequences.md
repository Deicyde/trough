---
declaration: section
origin: cited
lean: MetaMathlibExt.threeTermHofstadterLookup, MetaMathlibExt.threeTermHofstadterNext, MetaMathlibExt.threeTermHofstadterExtend, MetaMathlibExt.threeTermHofstadterPrefix, MetaMathlibExt.threeTermHofstadterTerm, MetaMathlibExt.ThreeTermHofstadterEndsAfter, MetaMathlibExt.threeTermHofstadterTerm_of_le_length, MetaMathlibExt.threeTermHofstadterTerm_zero
statement: formalized
---

# Three-term Hofstadter-like sequences

19 results, 10 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html).

## Value of a partially computed sequence at an index

Given computed terms
$B(1), \dots, B(m)$, a choice of whether the sequence is padded, and an integer $j$, the value
at index $j$ is $B(j)$ when $1 \le j \le m$, is $0$ when $j \le 0$ and the sequence is padded,
and is undefined otherwise (for $j \le 0$ in the unpadded case, and for $j > m$).

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1 (initial-condition and sequence-death conventions).

Formalized by `MetaMathlibExt.threeTermHofstadterLookup`, a definition declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-lookup).

## Next term of the three-term Hofstadter-like recurrence

Given computed terms
$B(1), \dots, B(m)$, padded with $0$ at nonpositive indices or not, the next term is
$B(m + 1) = B(m + 1 - B(m)) + B(m + 1 - B(m - 1)) + B(m + 1 - B(m - 2))$. It is undefined
when one of the values it uses, $B(m)$, $B(m - 1)$, $B(m - 2)$ or one of the three summands,
sits at an undefined index: a nonpositive index in the unpadded case, or an index above $m$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterNext`, a definition declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-next).

## Computing further terms of a three-term Hofstadter-like sequence

Given terms
$B(1), \dots, B(m)$, padded with $0$ at nonpositive indices or not, and a natural number $k$,
this is the list $B(1), \dots, B(m + k)$ obtained by computing $B(m + 1), \dots, B(m + k)$ one
after another from $B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3))$. It is undefined if
one of these terms cannot be computed because the formula refers to an undefined index (a
nonpositive index in the unpadded case, or an index not yet computed).

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterExtend`, a definition declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-extend).

## Initial segment of a three-term Hofstadter-like sequence

Let $x_1, \dots, x_m$ be
integers ($m \ge 0$) and let $B$ be the padded or the unpadded three-term Hofstadter-like sequence
with initial conditions $x_1, \dots, x_m$: $B(i) = x_i$ for $1 \le i \le m$, the padded sequence
has $B(i) = 0$ for every $i \le 0$ while the unpadded one is undefined there, and for $n > m$

$$B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3)),$$

which is defined only when every value of $B$ on the right-hand side is defined and the indices
$n - B(n-1)$, $n - B(n-2)$, $n - B(n-3)$ are less than $n$. For a natural number $k$, the
initial segment is the list $B(1), \dots, B(m + k)$, the initial conditions followed by the next
$k$ terms; it is undefined when one of $B(m + 1), \dots, B(m + k)$ is undefined.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterPrefix`, a definition declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-prefix).

## Three-term Hofstadter-like sequence

Let $x_1, \dots, x_m$ be integers ($m \ge 0$), the
initial conditions, and choose whether the sequence is padded. The sequence $B$ has $B(i) = x_i$
for $1 \le i \le m$; the padded sequence has $B(i) = 0$ for every integer $i \le 0$, while the
unpadded one is undefined at every $i \le 0$. For $n > m$,

$$B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3)),$$

which is defined only when every value of $B$ on the right-hand side is defined and the indices
$n - B(n-1)$, $n - B(n-2)$, $n - B(n-3)$ are less than $n$; once a term is undefined, the
sequence stops and every later term is undefined. The term at a natural number index $j$ is
$B(j)$ when this is defined and undefined otherwise; in particular the term at index $0$ is $0$
for the padded sequence and undefined for the unpadded one.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterTerm`, a definition declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-term).

## Exact length of a three-term Hofstadter-like sequence

Take integer initial conditions
$B(1), \dots, B(m)$, and either pad the sequence with $B(n) = 0$ for every $n \le 0$ or leave it
unpadded. Continue it by $B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3))$ for $n > m$,
where a term cannot be computed if this formula refers to an undefined index: a nonpositive
index in the unpadded case, or an index not yet computed. For a natural number $T$, the
sequence has exactly $T$ terms when $T \ge m$, the terms $B(1), \dots, B(T)$ can all be
computed, and $B(T + 1)$ cannot.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1 ("dies after `n - 1` terms"; "ends" in the padded case).

Formalized by `MetaMathlibExt.ThreeTermHofstadterEndsAfter`, a definition declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-ends-after).

## The initial conditions are the first terms

Let $x_1, \dots, x_m$ be integers and let $j$
be a natural number with $j \le m$. For the padded or the unpadded three-term Hofstadter-like
sequence with initial conditions $x_1, \dots, x_m$, the term at index $j$ equals the lookup of
index $j$ in $x_1, \dots, x_m$: it is $x_j$ if $j \ge 1$, and if $j = 0$ it is $0$ for the
padded sequence and undefined for the unpadded one.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterTerm_of_le_length`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-term-of-le-length).

## Index zero of the sequence started at 5

For the three-term Hofstadter-like sequence with
the single initial condition $5$, the term at index $0$ is defined and equals $0$ when the
sequence is padded, and it is undefined when the sequence is unpadded.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterTerm_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-term-zero).

## Sixth and seventh terms of the sequence started at 1, 2, 3, 4, 5

For the unpadded
three-term Hofstadter-like sequence $B$ with initial conditions $1, 2, 3, 4, 5$, the terms $B(6)$
and $B(7)$ are defined, with $B(6) = B(1) + B(2) + B(3) = 6$ and $B(7) = B(1) + B(2) + B(3) = 6$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Section 1.

Formalized by `MetaMathlibExt.threeTermHofstadterTerm_bSequence_six_seven`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-term-b-sequence-si).

## The sequence from $1, 2, 3$ dies after four terms

Run the recurrence
$B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3))$ from the initial conditions
$B(1) = 1$, $B(2) = 2$, $B(3) = 3$ without padding, so that a term whose recurrence refers to a
nonpositive index, or to an index not yet computed, cannot be computed. Then the sequence has
exactly four terms: $B(4)$ can be computed and $B(5)$ cannot.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, proof of Theorem 1 (`B_3(4) = 6`).

Formalized by `MetaMathlibExt.threeTermHofstadterEndsAfter_one_two_three`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-ends-after-one-two).

## Death of the unpadded sequence from $1, \dots, N$ for $N = 3$, $4$ or $N \ge 10$

Let
$N$ be a natural number with $N = 3$, $N = 4$ or $N \ge 10$, and let $B_N$ be the sequence with
initial conditions $B_N(i) = i$ for $1 \le i \le N$, continued without padding by the recurrence
$B_N(n) = B_N(n - B_N(n-1)) + B_N(n - B_N(n-2)) + B_N(n - B_N(n-3))$. Then $B_N$ dies: there is
a natural number $T$ such that $B_N(1), \dots, B_N(T)$ can be computed and $B_N(T + 1)$ cannot,
because the recurrence refers to a nonpositive index or to an index not yet computed.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Theorem 1 (`jis-2024-24.7.4-thm-1`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_linear_dies` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-linear-dies).

## Length of the unpadded sequence from $1, \dots, N$

For every natural number $N \ge 14$,
the sequence $B_N$ with initial conditions $B_N(i) = i$ for $1 \le i \le N$, continued without
padding by the recurrence $B_N(n) = B_N(n - B_N(n-1)) + B_N(n - B_N(n-2)) + B_N(n - B_N(n-3))$,
has exactly $N + 24$ terms: $B_N(1), \dots, B_N(N + 24)$ can be computed and $B_N(N + 25)$
cannot, because the recurrence refers to a nonpositive index or to an index not yet computed.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Theorem 1 (`jis-2024-24.7.4-thm-1`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_linear_length` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-linear-length).

## Period-seven pattern of the padded sequence from $1, \dots, N$

Let $N \ge 72$ be a
natural number, and let $B$ be the sequence with $B(n) = 0$ for $n \le 0$ and $B(i) = i$ for
$1 \le i \le N$, continued by the recurrence $B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3))$.
Let $\nu = -1, -2, -2, -2, 2, 1, 0$ according as $N \equiv 0, 1, 2, 3, 4, 5, 6 \pmod 7$. Then
for all natural numbers $k \ge 1$ and $r < 7$ with $N + 67 \le N + 7k + r \le 2N + \nu$, the
term $B(N + 7k + r)$ can be computed, and it equals $7k + 2$, $N + 7k + 2$, $N + 7k + 4$, $7$,
$2N + 2k + 45$, $2N + k - 7$ or $N - 2$ according as $r = 0, 1, 2, 3, 4, 5$ or $6$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Theorem 2 (`jis-2024-24.7.4-thm-2`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_padded_linear_period_seven` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-padded-linear-peri).

## Length of the padded sequence from $1, \dots, N$

Let $N$ be a natural number, and let
$t = 196, 2087, 3201, 4315, 200, 32478, 118$ and $e = 27, 254, 524, 560, 20, 4547, 9$
according as $N \equiv 0, 1, 2, 3, 4, 5, 6 \pmod 7$. Let $B$ be the sequence with $B(n) = 0$
for $n \le 0$ and $B(i) = i$ for $1 \le i \le N$, continued by the recurrence
$B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3))$. If $N \ge t$, then $B$ ends after
exactly $2N + e$ terms: $B(1), \dots, B(2N + e)$ can be computed and $B(2N + e + 1)$ cannot,
because the recurrence refers to an index not yet computed.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Theorem 2 (`jis-2024-24.7.4-thm-2`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_padded_linear_endsAfter` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-padded-linear-ends).

## Seven-cycle lemma for the three-term Hofstadter-like recurrence

Let $K$, $c$ and
$\gamma$ be natural numbers with $K \ge 7$, $c \ge 1$, $\gamma \le 6$ and $7c + \gamma \le K$, and
put $L = K - 7c - \gamma$ and $M = K + L + 5$. For a tuple $(t_0, \dots, t_6)$ write
$(t_0, \dots, t_6)_\gamma$ for its entry $t_\gamma$. Let $\lambda$ and $\mu$ be integers with
$\lambda \ge -2c + (2, 1, 4, 3, 2, 1, 0)_\gamma$ and $\mu \ge -c + (0, 0, 3, 2, 1, 0, -1)_\gamma$,
and put $\nu = (-2, -2, 2, 1, 0, -1, -2)_\gamma$. Let $a_1, \dots, a_L$ be arbitrary integers and
let $B$ be the padded three-term Hofstadter-like sequence with initial conditions
$1, 2, \dots, K, 6, a_1, \dots, a_L, 2K + \lambda - 2, 2K + \mu - 1, K - 2$. Then for every
integer $k$ and every $r \in \{0, 1, \dots, 6\}$ with $M - 3 \le M + 7k + r \le 2K + \nu$, the
term $B(M + 7k + r)$ is defined, and these terms are $B(M + 7k) = L + 7k + 7$,
$B(M + 7k + 1) = M + 7k + 2$, $B(M + 7k + 2) = M + 7k + 4$, $B(M + 7k + 3) = 7$,
$B(M + 7k + 4) = 2K + 2k + \lambda$, $B(M + 7k + 5) = 2K + k + \mu$ and $B(M + 7k + 6) = K - 2$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Lemma 3 (`jis-2024-24.7.4-lem-3`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_sevenCycle` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-seven-cycle).

## Two-cycle lemma for the three-term Hofstadter-like recurrence

Let $K \ge 1$ be a natural
number, let $M$ be an integer with $M \ge K + 5$, let $a_1, \dots, a_K$ be arbitrary integers,
and let $B$ be the padded three-term Hofstadter-like sequence with initial conditions
$a_1, \dots, a_K, 2, M, 2$. Then for every natural number $k$ the term $B(K + 2k + 1)$ is defined
and equals $2$, and for every $k \ge 1$ the term $B(K + 2k)$ is defined and equals $2^{k-1} M$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Lemma 4, citing the author's thesis, Proposition 9.9 (`jis-2024-24.7.4-lem-4`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_twoCycle` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-two-cycle).

## Five-cycle lemma for the three-term Hofstadter-like recurrence

Let $K \ge 3$ be a
natural number, $\mu \ge 1$ an integer, and $a_4, \dots, a_K$ arbitrary integers. Let $B$ be
the sequence given by $B(n) = B(n - B(n-1)) + B(n - B(n-2)) + B(n - B(n-3))$, padded with
$B(n) = 0$ for $n \le 0$, with initial conditions
$1, 2, 3, a_4, \dots, a_K, K + \mu, 3, K + 3, K + \mu + 1, 5$ at the indices $1, \dots, K + 5$.
Then for all natural numbers $k$ and $r < 5$ with
$K + 1 \le K + 5k + r \le K + \lfloor (5\mu - 15)/2 \rfloor$, the term $B(K + 5k + r)$ can be
computed, and it equals $5$, $K + 3k + \mu$, $3$, $K + 5k + 3$ or $K + 3k + \mu + 1$ according
as $r = 0, 1, 2, 3$ or $4$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Lemma 5, citing the author's thesis, Proposition 9.10 (`jis-2024-24.7.4-lem-5`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_fiveCycle` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-five-cycle).

## Second sixteen-cycle lemma for the three-term Hofstadter-like recurrence

Let $K \ge 1$
be a natural number and let $\lambda$, $\mu_1$, $\mu_2$, $\gamma_1$, $\gamma_2$, $\gamma_3$ be
integers with $\lambda > 31 + K$ and $\mu_1, \mu_2, \gamma_1, \gamma_2, \gamma_3 > \lambda$. Let
$a_1, \dots, a_K$ be arbitrary integers and let $B$ be the padded three-term Hofstadter-like
sequence with initial conditions $a_1, \dots, a_K, 16, \mu_2, 7, \gamma_2, \lambda, 16, \lambda,
16, \mu_1, 10, \gamma_3, \mu_2, 7, \lambda, 16, \gamma_1$. Then for all natural numbers $k$ and
$r \le 15$ with $K + 1 \le K + 16k + r \le \lambda$, the term $B(K + 16k + r)$ is defined, and
these terms are $B(K + 16k) = \mu_1 2^k + \gamma_1 - 2\mu_1$, $B(K + 16k + 1) = 16$,
$B(K + 16k + 2) = \mu_2 2^k$, $B(K + 16k + 3) = 7$, $B(K + 16k + 4) = 7k + \gamma_2$,
$B(K + 16k + 5) = \lambda$, $B(K + 16k + 6) = 16$, $B(K + 16k + 7) = \lambda$,
$B(K + 16k + 8) = 16$, $B(K + 16k + 9) = \mu_1 2^k$, $B(K + 16k + 10) = 10$,
$B(K + 16k + 11) = 16k + \gamma_3$, $B(K + 16k + 12) = \mu_2 2^k$, $B(K + 16k + 13) = 7$,
$B(K + 16k + 14) = \lambda$ and $B(K + 16k + 15) = 16$.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Lemma 7, citing the author's thesis, Proposition 9.16 (`jis-2024-24.7.4-lem-7`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_sixteenCycle_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-sixteen-cycle-two).

## First sixteen-cycle lemma for the three-term Hofstadter-like recurrence

Let $K \ge 1$ be
a natural number and let $\lambda$, $\mu_1$, $\mu_2$, $\gamma$ be integers with $\lambda > 31 + K$
and $\mu_1, \mu_2, \gamma > \lambda$. Let $a_1, \dots, a_K$ be arbitrary integers and let $B$ be
the padded three-term Hofstadter-like sequence with initial conditions
$a_1, \dots, a_K, \lambda, 7, \mu_2, 16, \mu_2, 16, \mu_1, \lambda, 7, \mu_2, 16, 2\mu_2, 16,
\mu_2, 25, \gamma, \lambda, 7$. Then for all natural numbers $k$ and $r \le 15$ with
$K + 1 \le K + 16k + r \le \lambda$, the term $B(K + 16k + r)$ is defined, and these terms are
$B(K + 16k) = \mu_1 2^{k-1} + \gamma - \mu_1$, $B(K + 16k + 1) = \lambda$, $B(K + 16k + 2) = 7$,
$B(K + 16k + 3) = \mu_2 2^k$, $B(K + 16k + 4) = 16$, $B(K + 16k + 5) = \mu_2 2^k$,
$B(K + 16k + 6) = 16$, $B(K + 16k + 7) = \mu_1 2^k$, $B(K + 16k + 8) = \lambda$,
$B(K + 16k + 9) = 7$, $B(K + 16k + 10) = \mu_2 2^k$, $B(K + 16k + 11) = 16$,
$B(K + 16k + 12) = \mu_2 2^{k+1}$, $B(K + 16k + 13) = 16$, $B(K + 16k + 14) = \mu_2 2^k$ and
$B(K + 16k + 15) = 25$.

Corrected: the paper prints $B(K + 16k + 12) = \mu_2 2^k$, which contradicts its own initial
value $B(K + 12) = 2\mu_2$; the exponent $k + 1$ matches the initial conditions and every later
term.

## Sources

- Nathan Fox, *The Behavior of a Three-Term Hofstadter-Like Recurrence with Linear Initial Conditions*, Journal of Integer Sequences 27 (2024), Article 24.7.4, Lemma 6, citing the author's thesis, Proposition 9.13 (`jis-2024-24.7.4-lem-6`).

Stated but not proved: `MetaMathlibExt.threeTermHofstadter_sixteenCycle_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Recurrences/ThreeTermHofstadterWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html#three-term-hofstadter-sixteen-cycle-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Three-term Hofstadter-like sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/three-term-hofstadter-like-sequences)
