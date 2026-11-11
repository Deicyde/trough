---
declaration: section
origin: cited
lean: MetaMathlibExt.IsConcatTwoRepdigitsBase, MetaMathlibExt.isConcatTwoRepdigitsBase_examples, MetaMathlibExt.narayanaCowsSequence_isConcatTwoRepdigitsBase_iff, MetaMathlibExt.narayanaCowsSequence_concat_log_bounds
statement: formalized
---

# Narayana numbers as concatenations of repdigits

5 results, 2 proved, 2 stated but not proved and 1 without a declaration, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html).

## Concatenations of two repdigits in a general base

A natural number $n$ is a
concatenation of two repdigits in base $b$ if there are digits $a_1, a_2$ with
$1 \le a_1 \le b - 1$, $0 \le a_2 \le b - 1$ and $a_1 \ne a_2$, and block lengths $l, m \ge 1$,
such that $(b - 1) n = a_1 (b^l - 1) b^m + a_2 (b^m - 1)$. The digit conditions force
$b \ge 2$, and the equation says that the base-$b$ expansion of $n$ is $l$ copies of $a_1$
followed by $m$ copies of $a_2$.

Because of the condition $a_1 \ne a_2$, a repdigit such as $4 = (11)_3$ is not a concatenation
of two repdigits in base $3$. For $b = 10$ this is the notion of a concatenation of two decimal
repdigits.

## Sources

- Prasanta Kumar Ray and Kisan Bhoi, *Narayana Numbers Which Are Concatenations of Two Base b Repdigits*, INTEGERS 24 (2024), Article A20, Section 1 (Equation (1)).

Formalized by `MetaMathlibExt.IsConcatTwoRepdigitsBase`, a definition declared in [WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html#is-concat-two-repdigits-base).

## Examples of two-repdigit concatenations in bases 2 and 5

The number $4$ is a
concatenation of two repdigits in base $2$, since $4 = (100)_2$, and the number $406$ is a
concatenation of two repdigits in base $5$, since $406 = (3111)_5$.

## Sources

- Prasanta Kumar Ray and Kisan Bhoi, *Narayana Numbers Which Are Concatenations of Two Base b Repdigits*, INTEGERS 24 (2024), Article A20, Theorem 1.

Formalized by `MetaMathlibExt.isConcatTwoRepdigitsBase_examples`, a theorem declared in [WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html#is-concat-two-repdigits-base-examples).

## Narayana numbers that concatenate two repdigits in bases 2 to 9

Let $(N_n)$ be
Narayana's cows sequence and let $2 \le b \le 9$. Then $N_n$ is a concatenation of two repdigits
in base $b$ if and only if $(n, b)$ is one of the following $43$ pairs: $n = 4$ and $b = 2$;
$n = 5$ and $b = 3$; $n = 6$ and $b \in \{2, 4\}$; $n = 7$ and $b \in \{2, 3, 4, 6\}$; $n = 8$
and $b \in \{3, 4, 5, 6, 7, 9\}$; $n = 9$ and $b \in \{4, 5, 6, 7, 8, 9\}$; $n = 10$ and
$b \in \{5, 6, 7, 8, 9\}$; $n = 11$ and $b \in \{2, 7, 8, 9\}$; $n = 12$ and
$b \in \{3, 4, 7, 8, 9\}$; $n = 13$ and $b \in \{2, 4, 5, 7, 8\}$; $n = 14$ and $b = 6$;
$n = 17$ and $b \in \{7, 9\}$; $n = 18$ and $b = 5$.

The corresponding values and expansions are $N_4 = 2 = (10)_2$, $N_5 = 3 = (10)_3$,
$N_6 = 4 = (100)_2 = (10)_4$, $N_7 = 6 = (110)_2 = (20)_3 = (12)_4 = (10)_6$,
$N_8 = 9 = (100)_3 = (21)_4 = (14)_5 = (13)_6 = (12)_7 = (10)_9$,
$N_9 = 13 = (31)_4 = (23)_5 = (21)_6 = (16)_7 = (15)_8 = (14)_9$,
$N_{10} = 19 = (34)_5 = (31)_6 = (25)_7 = (23)_8 = (21)_9$,
$N_{11} = 28 = (11100)_2 = (40)_7 = (34)_8 = (31)_9$,
$N_{12} = 41 = (1112)_3 = (221)_4 = (56)_7 = (51)_8 = (45)_9$,
$N_{13} = 60 = (111100)_2 = (330)_4 = (220)_5 = (114)_7 = (74)_8$, $N_{14} = 88 = (224)_6$,
$N_{17} = 277 = (544)_7 = (337)_9$ and $N_{18} = 406 = (3111)_5$.

## Sources

- Prasanta Kumar Ray and Kisan Bhoi, *Narayana Numbers Which Are Concatenations of Two Base b Repdigits*, INTEGERS 24 (2024), Article A20, Theorem 1.

Stated but not proved: `MetaMathlibExt.narayanaCowsSequence_isConcatTwoRepdigitsBase_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html#narayana-cows-sequence-is-concat-two-rep).

## Guzmán Sánchez–Luca lemma: $L < 2^r H (\log H)^r$

Lemma 3 (Guzmán Sánchez and Luca): for real `r ≥ 1` and `H` with `H > (4r²)^r` and
`H > L / (log L)^r`, we have `L < 2^r H (log H)^r`. The hypothesis `H > 0` is implied by
`H > (4r²)^r` and is dropped.

## Sources

- Prasanta Kumar Ray and Kisan Bhoi, *Narayana Numbers Which Are Concatenations of Two Base b Repdigits*, INTEGERS 24 (2024), Article A20, Lemma 3.

The vault records no Lean declaration for it. [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html#lt-two-rpow-mul-mul-log-rpow).

## Logarithmic bounds for Narayana numbers that concatenate two repdigits

Let $(N_n)$ be
Narayana's cows sequence and let $\alpha$ be a real number with $\alpha^3 = \alpha^2 + 1$ (so
$\alpha \approx 1.46557$ is the unique real root of $x^3 - x^2 - 1$). Let $b \ge 2$, $n \ge 1$
and $l, m \ge 1$ be natural numbers, and let $a_1, a_2$ be digits with $1 \le a_1 \le b - 1$,
$0 \le a_2 \le b - 1$ and $a_1 \ne a_2$. If $(b - 1) N_n = a_1 (b^l - 1) b^m + a_2 (b^m - 1)$,
that is, the base-$b$ expansion of $N_n$ is $l$ copies of $a_1$ followed by $m$ copies of
$a_2$, then $(l + m - 1) \log b + \log \alpha < n \log \alpha < (l + m) \log b + 1$.

## Sources

- Prasanta Kumar Ray and Kisan Bhoi, *Narayana Numbers Which Are Concatenations of Two Base b Repdigits*, INTEGERS 24 (2024), Article A20, Lemma 1.

Stated but not proved: `MetaMathlibExt.narayanaCowsSequence_concat_log_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NarayanaConcatRepdigitsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html#narayana-cows-sequence-concat-log-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Narayana numbers as concatenations of repdigits](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/narayana-numbers-as-concatenations-of-repdigits)
