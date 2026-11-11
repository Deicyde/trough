---
declaration: section
origin: cited
lean: MetaMathlibExt.convergentDen, MetaMathlibExt.convergentDen_zero, MetaMathlibExt.convergentDen_one, MetaMathlibExt.convergentDen_add_two, MetaMathlibExt.convergentDen_two, MetaMathlibExt.HasPeriodicCF, MetaMathlibExt.HasPeriodicCF.floor_eq, MetaMathlibExt.sqrt_hasPeriodicCF_exists_iff_of_odd
statement: formalized
---

# Continued fractions of quadratic irrationals

23 results, 7 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html).

## Convergent denominators as continuants

For a sequence of natural numbers
$a_0, a_1, a_2, \dots$, its convergent denominators $q_0, q_1, q_2, \dots$ are the natural
numbers defined by $q_0 = 1$, $q_1 = a_1$ and $q_{i+2} = a_{i+2} q_{i+1} + q_i$ for $i \ge 0$.
They are the denominators of the convergents of $[a_0; a_1, a_2, \dots]$, and $q_i$ is the
continuant $K(a_1, \dots, a_i)$; the term $a_0$ is never used.

The denominators $r_i$ of the paper, those of the convergents of $[a_1; a_2, \dots, a_i]$, are
the convergent denominators of the shifted sequence $(a_{n+1})_{n \ge 0}$ at index $i - 1$, for
$i \ge 1$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, notation of Proposition 2.

Formalized by `MetaMathlibExt.convergentDen`, a definition declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den).

## The convergent denominator $q_0$ equals $1$

For every sequence of natural numbers
$a_0, a_1, a_2, \dots$ with convergent denominators $q_0, q_1, q_2, \dots$, we have $q_0 = 1$.

## Sources

- Jun Ho Lee, INTEGERS 26 (2026), Article A69, notation of Proposition 2.

Formalized by `MetaMathlibExt.convergentDen_zero`, a theorem declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-zero).

## The convergent denominator $q_1$ equals $a_1$

For every sequence of natural numbers
$a_0, a_1, a_2, \dots$ with convergent denominators $q_0, q_1, q_2, \dots$, we have $q_1 = a_1$.

## Sources

- Jun Ho Lee, INTEGERS 26 (2026), Article A69, notation of Proposition 2.

Formalized by `MetaMathlibExt.convergentDen_one`, a theorem declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-one).

## Recurrence for the convergent denominators

For every sequence of natural numbers
$a_0, a_1, a_2, \dots$ with convergent denominators $q_0, q_1, q_2, \dots$ and every natural
number $n$, we have $q_{n+2} = a_{n+2} q_{n+1} + q_n$.

## Sources

- Jun Ho Lee, INTEGERS 26 (2026), Article A69, notation of Proposition 2.

Formalized by `MetaMathlibExt.convergentDen_add_two`, a theorem declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-add-two).

## The convergent denominator $q_2$ equals $a_2 a_1 + 1$

For every sequence of natural
numbers $a_0, a_1, a_2, \dots$ with convergent denominators $q_0, q_1, q_2, \dots$, we have
$q_2 = a_2 a_1 + 1$.

## Sources

- Jun Ho Lee, INTEGERS 26 (2026), Article A69, notation of Proposition 2.

Formalized by `MetaMathlibExt.convergentDen_two`, a theorem declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-two).

## Continued fractions with a prescribed period

For a real number $x$, natural numbers
$a_0$, $l$, $c$ and a sequence of natural numbers $a_1, a_2, \dots$, we write
$x = [a_0; \overline{a_1, \dots, a_{l-1}, c}]$ when the regular continued fraction of $x$ is the
infinite expansion $[a_0; a_1, \dots, a_{l-1}, c, a_1, \dots, a_{l-1}, c, \dots]$: its integer
part is $a_0$, and for every $k \ge 1$ its $k$-th partial quotient exists and equals $c$ when $l$
divides $k$ and $a_{k \bmod l}$ otherwise. The period $l$ need not be minimal.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, the expansions `√d = [a₀; a₁, …, a_{l-1}, 2a₀]` of Theorem 1.

Formalized by `MetaMathlibExt.HasPeriodicCF`, a definition declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#has-periodic-cf).

## The integer part of a periodic continued fraction is the floor

Let $x$ be a real
number and let $a_0$, $l$, $c$ and $a_1, a_2, \dots$ be natural numbers. Suppose that the regular
continued fraction of $x$ has integer part $a_0$ and that, for every $k \ge 1$, its $k$-th
partial quotient is $c$ when $l$ divides $k$ and $a_r$ otherwise, where $r$ is the remainder of
$k$ modulo $l$ (so $r = k$ when $l = 0$). For $l \ge 1$ this says that the continued fraction
is $[a_0; a_1, \dots, a_{l-1}, c, a_1, \dots, a_{l-1}, c, \dots]$. Then $\lfloor x \rfloor = a_0$.

## Sources

- Jun Ho Lee, INTEGERS 26 (2026), Article A69, Theorem 1 (`a₀ = ⌊√d⌋`).

Formalized by `MetaMathlibExt.HasPeriodicCF.floor_eq`, a theorem declared in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#floor-eq).

## Parity criterion for $\sqrt{d}$ with a given symmetric period, odd length

Let $l$ be odd
and let $a_1, \dots, a_{l-1}$ be positive integers with $a_i = a_{l-i}$ for $1 \le i \le l - 1$.
For $0 \le i \le l - 1$ let $q_i = K(a_1, \dots, a_i)$ be the continuant, given by $q_0 = 1$,
$q_1 = a_1$ and $q_{i+2} = a_{i+2} q_{i+1} + q_i$. Then there are a natural number $d$ that is
not a perfect square and a natural number $a_0$ with
$\sqrt{d} = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0}]$ if and only if $q_{l-1}$ is odd.

The paper fixes $d$ in its preamble; here $d$ and $a_0$ are quantified existentially, as in its
Proposition 2.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Theorem 1 (i).

Stated but not proved: `MetaMathlibExt.sqrt_hasPeriodicCF_exists_iff_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#sqrt-has-periodic-cf-exists-iff-of-odd).

## Parity criterion for $\sqrt{d}$ with a given symmetric period, even length

Let $l \ge 2$
be even and let $a_1, \dots, a_{l-1}$ be positive integers with $a_i = a_{l-i}$ for
$1 \le i \le l - 1$. For $0 \le i \le l - 1$ let $q_i = K(a_1, \dots, a_i)$ be the continuant,
given by $q_0 = 1$, $q_1 = a_1$ and $q_{i+2} = a_{i+2} q_{i+1} + q_i$. Then there are a natural
number $d$ that is not a perfect square and a natural number $a_0$ with
$\sqrt{d} = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0}]$ if and only if either $a_{l/2}$ and
$q_{l-1}$ are both odd, or $a_{l/2}$ is even.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Theorem 1 (ii).

Stated but not proved: `MetaMathlibExt.sqrt_hasPeriodicCF_exists_iff_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#sqrt-has-periodic-cf-exists-iff-of-even).

## Splitting the last convergent denominator of a symmetric sequence

Let $l$ be a
natural number and let $a_0, a_1, a_2, \dots$ be natural numbers with convergent denominators
$q_0, q_1, q_2, \dots$, such that $a_i = a_{l-i}$ for $1 \le i < l$. Then for every $i$ with
$1 \le i \le l - 2$,

$$q_{l-1} = q_i q_{l-1-i} + q_{i-1} q_{l-2-i}.$$

The case $i = 0$ of the paper, which uses $q_{-1} = 0$, is omitted.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Proposition 3 (i).

Stated but not proved: `MetaMathlibExt.convergentDen_symm_split` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-symm-split).

## Splitting the shifted continuant of a symmetric sequence

Let $l$ be a natural number
and let $a_1, \dots, a_{l-1}$ be natural numbers with $a_i = a_{l-i}$ for $1 \le i \le l - 1$.
For $j \ge 1$ let $r_j = K(a_2, \dots, a_j)$ be the continuant, given by $r_1 = 1$,
$r_2 = a_2$ and $r_{j+2} = a_{j+2} r_{j+1} + r_j$. Then for every $i$ with $2 \le i \le l - 3$,

$$r_{l-2} = r_i \, r_{l-1-i} + r_{i-1} \, r_{l-2-i}.$$

The cases $i \in \{0, 1, l - 2\}$ of the paper, which need $r_0 = 0$ and $r_{-1} = 1$, are
omitted.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Proposition 3 (ii).

Stated but not proved: `MetaMathlibExt.shifted_convergentDen_symm_split` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#shifted-convergent-den-symm-split).

## Parity of $q_{l-1}$ for a symmetric sequence, even $l$

Let $l \ge 2$ be even and let
$a_0, a_1, a_2, \dots$ be natural numbers with convergent denominators $q_0, q_1, q_2, \dots$,
such that $a_i = a_{l-i}$ for $1 \le i < l$. Then $q_{l-1} \equiv a_{l/2} \, q_{l/2-1} \pmod 2$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Corollary 1 (i).

Stated but not proved: `MetaMathlibExt.convergentDen_parity_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-parity-of-even).

## Parity of the shifted continuant of a symmetric sequence, even length

Let $l \ge 4$ be
even and let $a_1, \dots, a_{l-1}$ be natural numbers with $a_i = a_{l-i}$ for
$1 \le i \le l - 1$. For $j \ge 1$ let $r_j = K(a_2, \dots, a_j)$ be the continuant, given by
$r_1 = 1$, $r_2 = a_2$ and $r_{j+2} = a_{j+2} r_{j+1} + r_j$. Then
$r_{l-2} \equiv a_{l/2} \, r_{l/2-1} \pmod 2$.

The case $l = 2$ of the paper, which needs $r_0 = 0$, is omitted.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Corollary 1 (ii).

Stated but not proved: `MetaMathlibExt.shifted_convergentDen_parity_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#shifted-convergent-den-parity-of-even).

## Parity of $q_{l-1}$ for a symmetric sequence, odd $l$

Let $l \ge 3$ be odd and let
$a_0, a_1, a_2, \dots$ be natural numbers with convergent denominators $q_0, q_1, q_2, \dots$,
such that $a_i = a_{l-i}$ for $1 \le i < l$. Then
$q_{l-1} \equiv q_{(l-1)/2} + q_{(l-3)/2} \pmod 2$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Corollary 2 (i).

Stated but not proved: `MetaMathlibExt.convergentDen_parity_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#convergent-den-parity-of-odd).

## Parity of the shifted continuant of a symmetric sequence, odd length

Let $l \ge 5$ be
odd and let $a_1, \dots, a_{l-1}$ be natural numbers with $a_i = a_{l-i}$ for
$1 \le i \le l - 1$. For $j \ge 1$ let $r_j = K(a_2, \dots, a_j)$ be the continuant, given by
$r_1 = 1$, $r_2 = a_2$ and $r_{j+2} = a_{j+2} r_{j+1} + r_j$. Then
$r_{l-2} \equiv r_{(l-1)/2} + r_{(l-3)/2} \pmod 2$.

The case $l = 3$ of the paper, which needs $r_0 = 0$, is omitted.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Corollary 2 (ii).

Stated but not proved: `MetaMathlibExt.shifted_convergentDen_parity_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#shifted-convergent-den-parity-of-odd).

## Number of unrealizable parity patterns for $\sqrt{d}$, odd length

Let $l \ge 3$ be odd.
Call a parity pattern $(v_1, \dots, v_{(l-1)/2}) \in (\mathbb{Z}/2)^{(l-1)/2}$ realizable if
there are positive integers $a_1, \dots, a_{l-1}$ with $a_i = a_{l-i}$ for $1 \le i \le l - 1$
and $a_j \equiv v_j \pmod 2$ for $1 \le j \le (l-1)/2$, a natural number $d$ that is not a
perfect square and a natural number $a_0$ with
$\sqrt{d} = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0}]$. If $A$ is the number of parity
patterns that are not realizable, then $3A = 2^{(l-1)/2} - (-1)^{(l-1)/2}$.

Writing $A_m$ for $A$ when $l = 2m + 1$, this gives $A_1 = A_2 = 1$ and
$A_m = A_{m-1} + 2A_{m-2}$ for $m \ge 3$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Theorem 3.

Stated but not proved: `MetaMathlibExt.sqrt_periodicCF_obstruction_count_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#sqrt-periodic-cf-obstruction-count-of-od).

## Number of unrealizable parity patterns for $\sqrt{d}$, even length

Let $l \ge 4$ be
even. Call a parity pattern $(v_1, \dots, v_{l/2}) \in (\mathbb{Z}/2)^{l/2}$ realizable if there
are positive integers $a_1, \dots, a_{l-1}$ with $a_i = a_{l-i}$ for $1 \le i \le l - 1$ and
$a_j \equiv v_j \pmod 2$ for $1 \le j \le l/2$, a natural number $d$ that is not a perfect square
and a natural number $a_0$ with $\sqrt{d} = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0}]$. If $B$
is the number of parity patterns that are not realizable, then
$3B = 2^{l/2 - 1} - (-1)^{l/2 - 1}$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Theorem 4.

Stated but not proved: `MetaMathlibExt.sqrt_periodicCF_obstruction_count_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#sqrt-periodic-cf-obstruction-count-of-ev).

## Every parity pattern is realized by $(1 + \sqrt{d})/2$ for odd period length

Let $l$ be
odd. For every parity pattern $(v_1, \dots, v_{(l-1)/2}) \in (\mathbb{Z}/2)^{(l-1)/2}$ there are
positive integers $a_1, \dots, a_{l-1}$ with $a_i = a_{l-i}$ for $1 \le i \le l - 1$ and
$a_j \equiv v_j \pmod 2$ for $1 \le j \le (l-1)/2$, a natural number $d$ that is not a perfect
square and a natural number $a_0$ with
$(1 + \sqrt{d})/2 = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0 - 1}]$. That is, the number $A'_l$
of patterns that are not realized is $0$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Theorem 5.

Stated but not proved: `MetaMathlibExt.half_one_add_sqrt_periodicCF_obstruction_count_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#half-one-add-sqrt-periodic-cf-obstructio).

## Unrealizable parity patterns for $(1 + \sqrt d)/2$ with even $l$

Let $l \ge 2$ be
even. Call a parity pattern $(v_1, \dots, v_{l/2}) \in (\mathbb{Z}/2)^{l/2}$ realizable if there
are positive integers $a_1, \dots, a_{l-1}$ with $a_i = a_{l-i}$ for $1 \le i < l$ and
$a_j \equiv v_j \pmod 2$ for $1 \le j \le l/2$, together with natural numbers $d$ and $a_0$
such that $d \equiv 1 \pmod 4$, $d$ is not a perfect square and the regular continued fraction
of $(1 + \sqrt d)/2$ is

$$[a_0; a_1, \dots, a_{l-1}, 2a_0 - 1, a_1, \dots, a_{l-1}, 2a_0 - 1, \dots].$$

Then the number $B'_l$ of parity patterns that are not realizable is $2^{l/2 - 1}$.

Without the hypothesis $d \equiv 1 \pmod 4$ one would get $B'_2 = 0$, since $d = 15$
realizes $a_1 = 2$.

## Sources

- Jun Ho Lee, *Nonexistence of the Continued Fraction of a Quadratic Irrational Number with a Given Sequence*, INTEGERS 26 (2026), Article A69, Theorem 6.

Stated but not proved: `MetaMathlibExt.half_one_add_sqrt_periodicCF_obstruction_count_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFNonexistenceWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#half-one-add-sqrt-periodic-cf-obstructio-2).

## Parity criterion for $\sqrt{d}$ with a given symmetric period

Let $l \ge 3$ and let
$a_1, \dots, a_{l-1}$ be positive integers with $a_i = a_{l-i}$ for $1 \le i < l$. Let $q_j$ be the
denominator of the $j$-th convergent of $[a_0; a_1, a_2, \dots]$ (so $q_0 = 1$, $q_1 = a_1$ and
$q_{j+2} = a_{j+2} q_{j+1} + q_j$), and let $r_{l-2}$ be the denominator of the $(l-3)$-th
convergent of $[a_1; a_2, a_3, \dots]$. There are natural numbers $d$ and $a_0$ with $d$ not a
perfect square and $\sqrt{d} = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0}]$ if and only if
$q_{l-1}$ is odd, or $q_{l-1}$ and $r_{l-2}$ are even and $q_{l-2}$ is odd.

## Sources

- Jun Ho Lee, *Classification for Existence of the Continued Fraction Expansions of √D and (1 + √D)/2*, INTEGERS 24 (2024), Article A50, Proposition 1.

Stated but not proved: `MetaMathlibExt.sqrt_hasPeriodicCF_exists_iff_parity` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#sqrt-has-periodic-cf-exists-iff-parity).

## Parity criterion for $(1 + \sqrt{d})/2$ with a given symmetric period

Let $l \ge 3$ and
let $a_1, \dots, a_{l-1}$ be positive integers with $a_i = a_{l-i}$ for $1 \le i < l$. Let $q_j$ be
the denominator of the $j$-th convergent of $[a_0; a_1, a_2, \dots]$ (so $q_0 = 1$, $q_1 = a_1$ and
$q_{j+2} = a_{j+2} q_{j+1} + q_j$), and let $r_{l-2}$ be the denominator of the $(l-3)$-th
convergent of $[a_1; a_2, a_3, \dots]$. There are natural numbers $d$ and $a_0$ with
$d \equiv 1 \pmod 4$, $d$ not a perfect square, and
$(1 + \sqrt{d})/2 = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0 - 1}]$ if and only if $q_{l-1}$ is
odd, or $q_{l-2}$ and $r_{l-2}$ are odd and $q_{l-1}$ is even.

The restriction $d \equiv 1 \pmod 4$ is needed: $(1 + \sqrt{2})/2 = [1; \overline{4, 1}]$ fits
$l = 6$ with $(a_1, \dots, a_5) = (4, 1, 4, 1, 4)$, where $q_5 = 140$, $q_4 = 29$ and $r_4 = 6$
violate the criterion.

## Sources

- Jun Ho Lee, *Classification for Existence of the Continued Fraction Expansions of √D and (1 + √D)/2*, INTEGERS 24 (2024), Article A50, Proposition 2.

Stated but not proved: `MetaMathlibExt.half_one_add_sqrt_hasPeriodicCF_exists_iff_parity` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#half-one-add-sqrt-has-periodic-cf-exists).

## Existence of $(1 + \sqrt{d})/2$ with a given symmetric period

Let $l$ be a natural number
and $a_1, \dots, a_{l-1}$ positive integers with $a_i = a_{l-i}$ for $1 \le i < l$. If $l$ is odd,
there are natural numbers $d$ and $a_0$ with $d \equiv 1 \pmod 4$, $d$ not a perfect square, and
$(1 + \sqrt{d})/2 = [a_0; \overline{a_1, \dots, a_{l-1}, 2a_0 - 1}]$. If $l$ is even and positive,
such $d$ and $a_0$ exist if and only if $a_{l/2}$ is odd.

## Sources

- Jun Ho Lee, *Classification for Existence of the Continued Fraction Expansions of √D and (1 + √D)/2*, INTEGERS 24 (2024), Article A50, Theorem 3.

Stated but not proved: `MetaMathlibExt.half_one_add_sqrt_hasPeriodicCF_exists_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#half-one-add-sqrt-has-periodic-cf-exists-2).

## Fundamental unit from the period of $\sqrt{d}$

Let $d \ge 2$ be a squarefree integer, let
$\varepsilon$ be the least real number $u > 1$ of the form $u = (x + y\sqrt{d})/2$ with
$x, y \in \mathbb{Z}$ and $x^2 - d y^2 = \pm 4$ (the fundamental unit of $\mathbb{Q}(\sqrt{d})$),
let $\sqrt{d} = [a_0; a_1, a_2, \dots]$ be the regular continued fraction of $\sqrt{d}$, with
convergents $p_k / q_k$ (so $p_0 = a_0$ and $q_0 = 1$), and let $l$ be the least positive integer
such that $a_{k+l} = a_k$ for all $k \ge 1$. Then $p_{l-1} + q_{l-1}\sqrt{d} = \varepsilon$, or
$p_{l-1} + q_{l-1}\sqrt{d} = \varepsilon^3$ and $d \equiv 5 \pmod 8$.

For squarefree $d$ the numbers $(x + y\sqrt{d})/2$ above are exactly the units of the ring of
integers of $\mathbb{Q}(\sqrt{d})$. The paper's positive squarefree $d$ is restricted to $d \ge 2$,
since $\mathbb{Q}(\sqrt{1})$ is not a quadratic field.

## Sources

- Jun Ho Lee, *Classification for Existence of the Continued Fraction Expansions of √D and (1 + √D)/2*, INTEGERS 24 (2024), Article A50, Theorem 1.

Stated but not proved: `MetaMathlibExt.fundamentalUnit_eq_convergent_or_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticIrrationalCFClassificationWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html#fundamental-unit-eq-convergent-or-cube).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continued fractions of quadratic irrationals](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/continued-fractions-of-quadratic-irrationals)
