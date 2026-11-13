---
declaration: section
origin: cited
lean: MetaMathlibExt.happy_six_min, MetaMathlibExt.negBaseSqDigitSumAux, MetaMathlibExt.negBaseSqDigitSum, MetaMathlibExt.negBaseSqDigitSum_zero, MetaMathlibExt.negBaseSqDigitSum_of_digit, MetaMathlibExt.negBaseSqDigitSum_samples, MetaMathlibExt.IsNegBaseHappy, MetaMathlibExt.isNegBaseHappy_one
statement: formalized
---

# Happy numbers

20 results, 11 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html).

## Smallest run of six consecutive happy numbers

A natural number is happy when repeatedly
replacing it by the sum of the squares of its decimal digits reaches $1$ after finitely many
steps. Let $N_0 = 7899999999999959999999996$. The six consecutive integers
$N_0, N_0 + 1, \dots, N_0 + 5$ are all happy, and every natural number $m$ such that
$m, m + 1, \dots, m + 5$ are all happy satisfies $m \ge N_0$.

## Sources

- Robert Styer, "Smallest Examples of Strings of Consecutive Happy Numbers," Journal of Integer Sequences 13 (2010), Article 10.6.3, Proposition, lines 135–136, https://cs.uwaterloo.ca/journals/JIS/VOL13/Styer/styer5.tex

Formalized by `MetaMathlibExt.happy_six_min`, a theorem declared in [MathlibExt/NumberTheory/Digits/HappySixMin.lean, line 1106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/HappySixMin.lean#L1106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#happy-six-min).

## Truncated digit-square sum in a negative base

For an integer $b$, define $T_b(f, a)$ for a
natural number $f$ and an integer $a$ by recursion on $f$: $T_b(0, a) = 0$, $T_b(f + 1, 0) = 0$,
and for $a \ne 0$, $T_b(f + 1, a) = r^2 + T_b(f, (a - r)/b)$, where $r = a \bmod b$ is the
remainder of $a$ on division by $b$, with $0 \le r < |b|$ (for $b = 0$ one takes $r = a$ and
$(a - r)/b = 0$). For $b \le -2$, $T_b(f, a)$ is thus the sum of the squares of the first $f$
base-$b$ digits of $a$, counted from the least significant one.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.negBaseSqDigitSumAux`, a definition declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#neg-base-sq-digit-sum-aux).

## Sum of squared digits in a negative base

Let $b \le -2$ be an integer. Every integer $a$
has an expansion $a = \sum_{i=0}^{n} a_i b^i$ with digits $0 \le a_i \le |b| - 1$, unique up to
leading zero digits, and $S_{2,b}(a) = \sum_{i=0}^{n} a_i^2$ is the sum of the squares of these
digits. The digits are produced from the least significant one by taking $a_0 = a \bmod b$ and
passing to $(a - a_0)/b$, until $0$ is reached.

The definition is made for every integer $b$, by running this digit extraction for at most
$2|a| + 2$ steps; for $b \le -2$ this suffices, since the quantity $2a$ (for $a \ge 0$) or
$2|a| + 1$ (for $a < 0$) strictly decreases at each step.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.negBaseSqDigitSum`, a definition declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#neg-base-sq-digit-sum).

## The digit-square sum of zero

For every integer $b$, the base-$b$ digit-square sum $S_{2,b}$
satisfies $S_{2,b}(0) = 0$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.negBaseSqDigitSum_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#neg-base-sq-digit-sum-zero).

## The digit-square sum of a single digit

Let $b$ and $d$ be integers with $0 < d < -b$, so
that $b \le -2$ and $d$ is a nonzero base-$b$ digit. Then the base-$b$ digit-square sum $S_{2,b}$
satisfies $S_{2,b}(d) = d^2$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.negBaseSqDigitSum_of_digit`, a theorem declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#neg-base-sq-digit-sum-of-digit).

## Sample values of the negative-base digit-square sum

Write $S_{2,b}$ for the base-$b$
digit-square sum, which sends an integer to the sum of the squares of its base-$b$ digits. Then
$S_{2,-10}(-1) = 82$, $S_{2,-10}(10) = 82$ and $S_{2,-4}(5) = 11$. Indeed $-1 = 1 \cdot (-10) + 9$
and $10 = 1 \cdot (-10)^2 + 9 \cdot (-10) + 0$ have base-$(-10)$ digits $1, 9$ and $1, 9, 0$, and
$5 = 1 \cdot (-4)^2 + 3 \cdot (-4) + 1$ has base-$(-4)$ digits $1, 3, 1$ (most significant first).

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.negBaseSqDigitSum_samples`, a theorem declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#neg-base-sq-digit-sum-samples).

## Happy integers in a negative base

Let $b$ be an integer and let $S_{2,b}$ be the
base-$b$ digit-square sum, which for $b \le -2$ sends an integer to the sum of the squares of its
base-$b$ digits. An integer $a$ is $b$-happy if $S_{2,b}^k(a) = 1$ for some $k \ge 1$, where
$S_{2,b}^k$ denotes the $k$-th iterate of $S_{2,b}$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.IsNegBaseHappy`, a definition declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy).

## $1$ is happy in every negative base

For every integer $b \le -2$, the integer $1$ is
$b$-happy.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.isNegBaseHappy_one`, a theorem declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy-one).

## Cycles of the negative-base digit-square map

For an integer $b$, let $S_{2,b}$ be the
base-$b$ digit-square sum, which for $b \le -2$ sends an integer to the sum of the squares of its
base-$b$ digits. Then $U_{2,b}$ is the set of positive integers $u$ such that $S_{2,b}^m(u) = u$
for some $m \ge 1$, that is, the positive integers lying on a cycle of $S_{2,b}$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.negBaseSqDigitCycles`, a definition declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#neg-base-sq-digit-cycles).

## One lies on a cycle of the negative-base digit-square map

For every integer $b \le -2$,
$1 \in U_{2,b}$, where $U_{2,b}$ is the set of positive integers lying on a cycle of the base-$b$
digit-square sum $S_{2,b}$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.one_mem_negBaseSqDigitCycles`, a theorem declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#one-mem-neg-base-sq-digit-cycles).

## Good sets for the digit-square map

For an integer $b$, let $S_{2,b}$ be the base-$b$
digit-square map, which for $b \le -2$ sends an integer to the sum of the squares of its base-$b$
digits; write $S_{2,b}^k$ for its $k$-fold iterate, and let $U_{2,b}$ be the set of positive
integers $u$ with $S_{2,b}^m(u) = u$ for some $m \ge 1$. A finite set $T$ of integers is
$(2, b)$-good if for each $u \in U_{2,b}$ there are integers $n \ge 1$ and $k \ge 1$ such that
$S_{2,b}^k(t + n) = u$ for every $t \in T$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Section 2.

Formalized by `MetaMathlibExt.IsNegBaseGood`, a definition declared in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-good).

## Happy numbers in base $-2$

There is an integer $n$ such that $n + 3i$ is $(-2)$-happy for
every natural number $i$, and an integer $a$ is $(-2)$-happy if and only if $a \equiv 1 \pmod 3$.

This is part (1) of the Grundman–Harris theorem.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.isNegBaseHappy_neg_two_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy-neg-two-iff).

## Happy numbers in base $-3$

There is an integer $n$ such that $n + 2i$ is $(-3)$-happy for
every natural number $i$, and an integer $a$ is $(-3)$-happy if and only if $a \equiv 1 \pmod 2$.

This is part (2) of the Grundman–Harris theorem.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.isNegBaseHappy_neg_three_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy-neg-three-iff).

## Arbitrarily long runs of consecutive happy numbers in bases $-4$, $-6$, $-8$, $-10$

Let
$b \in \{-4, -6, -8, -10\}$. For every natural number $N$ there is an integer $n$ such that
$n + i$ is $b$-happy for every $0 \le i < N$.

This is part (3) of the Grundman–Harris theorem.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.isNegBaseHappy_consecutive_runs_small` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy-consecutive-runs-small).

## Arithmetic progressions of happy numbers in odd negative bases

Let $b \le -3$ be an odd
integer. For every natural number $N$ there is an integer $n$ such that $n + 2i$ is $b$-happy for
every natural number $i < N$. Thus there are arbitrarily long finite arithmetic progressions with
common difference $2$ of $b$-happy integers.

This is part (4) of the theorem of Grundman and Harris.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.isNegBaseHappy_two_consecutive_runs_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy-two-consecutive-runs-o).

## Arbitrarily long runs of consecutive happy numbers in even bases at most $-4$

Let
$b \le -4$ be an even integer. For every natural number $N$ there is an integer $n$ such that
$n + i$ is $b$-happy for every $0 \le i < N$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.isNegBaseHappy_consecutive_runs_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-happy-consecutive-runs-even).

## Goodness pulls back along compositions of the digit-square map and the successor map

Let $b \le -2$ be an integer, let $S_{2,b}$ be the map sending an integer to the sum of the
squares of its base-$b$ digits, and let $I(t) = t + 1$. Let $T$ be a finite set of positive
integers and let $F$ be a composition $F = f_1 \circ \dots \circ f_m$ with $m \ge 0$ (the empty
composition being the identity), where each $f_i$ is $S_{2,b}$ or $I$. If the image $F(T)$ is
$(2, b)$-good, then $T$ is $(2, b)$-good.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.isNegBaseGood_of_image_comp` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-good-of-image-comp).

## A common iterate of the negative-base digit-square map falls below twice the squared base

Let $b \le -7$ be an integer, let $S_{2,b}$ be the map sending an integer to the sum of the
squares of its base-$b$ digits, and write $S_{2,b}^k$ for its $k$-fold iterate. For every finite
set $A$ of positive integers there is an integer $k \ge 1$ such that $S_{2,b}^k(a) < 2b^2$ for
every $a \in A$.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.exists_iterate_negBaseSqDigitSum_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#exists-iterate-neg-base-sq-digit-sum-lt).

## A congruence for the negative-base digit-square map

Let $b \le -12$ be an even integer,
let $S_{2,b}$ be the map sending an integer to the sum of the squares of its base-$b$ digits, and
let $v$ be an integer with $0 < v < 2b^2$. Then there are integers $w$ and $c$ with
$0 \le w < v$ and $0 \le c \le |b| - 2$ such that

$$S_{2,b}\bigl((|b| - 1)b + v - w - 1\bigr) -
S_{2,b}\bigl((|b| - 1)b^2 + |b| - 1 - w\bigr) + 5 + 2c \equiv 0 \pmod{|b| + 1}.$$

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Lemma 3.1.

Stated but not proved: `MetaMathlibExt.exists_negBaseSqDigitSum_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#exists-neg-base-sq-digit-sum-congr).

## Even bases at most $-4$ make every finite set of positive integers good

Let $b \le -4$
be an even integer. Then every finite set of positive integers is $(2, b)$-good.

## Sources

- Helen G. Grundman, *Closing an Open Problem on Negative Base Happy Numbers*, The Fibonacci Quarterly 62 (2024), Article 62-2/grundman11162023, Theorem 3.2.

Stated but not proved: `MetaMathlibExt.isNegBaseGood_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/NegativeBaseHappyNumbersWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html#is-neg-base-good-of-even).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Happy numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/happy-numbers)
