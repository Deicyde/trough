---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ColorCompAllowed, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ColorCompProhibited, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ColorCompProhibit2, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowed, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibited, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibit2, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowedZ, MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibitedZ
statement: formalized
---

# Restricted n-color compositions

32 results, 14 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html).

## n-color compositions with two allowed consecutive colors

For natural numbers $b$ and $n$,
$\mathrm{CCo}_{b,b+1}(n)$ is the set of $n$-color compositions of $n$ that use only the colors $b$
and $b+1$: finite sequences of pairs $(k_1, c_1), \dots, (k_m, c_m)$ of natural numbers (part
$k_i$ with color $c_i$) such that $1 \le c_i \le k_i$ and $c_i \in \{b, b+1\}$ for every $i$, and
$k_1 + \dots + k_m = n$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ColorCompAllowed`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#color-comp-allowed).

## n-color compositions with two prohibited consecutive colors

For natural numbers $b$ and
$n$, $\mathrm{CCo}_{\widehat{b,b+1}}(n)$ is the set of $n$-color compositions of $n$ in which no
part has color $b$ or $b+1$: finite sequences of pairs $(k_1, c_1), \dots, (k_m, c_m)$ of natural
numbers (part $k_i$ with color $c_i$) such that $1 \le c_i \le k_i$, $c_i \ne b$ and
$c_i \ne b+1$ for every $i$, and $k_1 + \dots + k_m = n$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ColorCompProhibited`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#color-comp-prohibited).

## n-color compositions without color 2

For a natural number $n$, $\mathrm{CCo}_{\hat 2}(n)$
is the set of $n$-color compositions of $n$ in which no part has color $2$: finite sequences of
pairs $(k_1, c_1), \dots, (k_m, c_m)$ of natural numbers (part $k_i$ with color $c_i$) such that
$1 \le c_i \le k_i$ and $c_i \ne 2$ for every $i$, and $k_1 + \dots + k_m = n$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ColorCompProhibit2`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#color-comp-prohibit2).

## Count of n-color compositions with two consecutive colors

An $n$-color composition of a
natural number $n$ is a finite sequence of parts, each a positive integer $k$ carrying a color
$c$ with $1 \le c \le k$, whose sizes sum to $n$. For natural numbers $b$ and $n$,
$\operatorname{cco}_{b,b+1}(n)$ is the number of $n$-color compositions of $n$ in which every
part has color $b$ or $b+1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowed`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-allowed).

## Number of n-color compositions with two prohibited consecutive colors

For natural numbers
$b$ and $n$, $\mathrm{cco}_{\widehat{b,b+1}}(n)$ is the number of elements of
$\mathrm{CCo}_{\widehat{b,b+1}}(n)$, that is, the number of $n$-color compositions of $n$ in which
no part has color $b$ or $b+1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibited`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-prohibited).

## Count of n-color compositions avoiding color 2

An $n$-color composition of a natural
number $n$ is a finite sequence of parts, each a positive integer $k$ carrying a color $c$ with
$1 \le c \le k$, whose sizes sum to $n$. For a natural number $n$, $\operatorname{cco}_{\hat 2}(n)$
is the number of $n$-color compositions of $n$ in which no part has color $2$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibit2`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-prohibit2).

## Integer extension of the count of n-color compositions with two consecutive colors

For
a natural number $b$, this is the function from the integers to the integers that sends
$n \ge 0$ to $\operatorname{cco}_{b,b+1}(n)$, the number of $n$-color compositions of $n$ in
which every part has color $b$ or $b+1$, and sends every $n < 0$ to $0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowedZ`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-allowed-z).

## Integer extension of the count of n-color compositions avoiding two consecutive colors

For a natural number $b$, this is the function from the integers to the integers that sends
$n \ge 0$ to $\operatorname{cco}_{\widehat{b,b+1}}(n)$, the number of $n$-color compositions of
$n$ in which no part has color $b$ or $b+1$, and sends every $n < 0$ to $0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibitedZ`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-prohibited-z).

## Splitting a ternary string at its zeros, with a prefix

For strings $w$ and $a$ over
$\{0, 1, 2\}$, write $w = s_0 \, 0 \, s_1 \, 0 \cdots 0 \, s_m$ where $m$ is the number of $0$s
in $w$ and each $s_i$ is a (possibly empty) string without $0$. The result is the list of strings
$a s_0, s_1, \dots, s_m$, in this order, where $a s_0$ is the concatenation of $a$ and $s_0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.splitZerosAux`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#split-zeros-aux).

## Splitting a ternary string at its zeros

For a string $w$ over $\{0, 1, 2\}$, the list of
the segments of $w$ obtained by cutting at every $0$: the part before the first $0$, the parts
between consecutive $0$s and the part after the last $0$, in order and including empty parts.
A string with $m$ zeros gives $m + 1$ segments; the empty string gives one empty segment.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.splitZeros`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#split-zeros).

## Admissible ternary strings

For natural numbers $b$ and $n$, the strings $w$ over
$\{0, 1, 2\}$ of length $n - 1$ (truncated subtraction, so length $0$ when $n = 0$) such that
every segment of $w$ obtained by cutting at its zeros (before the first zero, between
consecutive zeros and after the last zero, empty segments included) either consists only of
$1$s and has length at least $b - 1$, or consists only of $2$s and has length at least $b$.
In particular an empty segment is allowed exactly when $b \le 1$.

This is the segment form of the conditions in Theorem 2 of Hopkins and Wang (no $12$ or $21$
subwords, run-length bounds, and separation of successive zeros).

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.TernaryAdmissible`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#ternary-admissible).

## Compositions with two types of part 1 and no equal adjacent 1s

For a natural
number $n$, $C^*_{1,2}(n)$ is the set of compositions of $n$ whose parts are $1_1$, $1_2$
(two types of part of size $1$) and $2$, such that no two adjacent parts are parts $1$ of
the same type.

A composition is encoded as a list over the symbols $0$, $1$, $2$, where $0$ and $1$ stand
for $1_1$ and $1_2$ and the symbol $2$ stands for the part $2$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.TwoTypeComp`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#two-type-comp).

## Tribonacci numbers with initial values $1, 0, 1$

The sequence
$t : \mathbb{N} \to \mathbb{Z}$ with $t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and
$t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.tribNat`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-nat).

## Hopkins–Wang tribonacci numbers on the integers

Let $t(0) = 1$, $t(1) = 0$,
$t(2) = 1$ and $t(n) = t(n-1) + t(n-2) + t(n-3)$ for natural numbers $n \ge 3$. This
extends $t$ to an integer-valued function on all integers by setting $t(n) = 0$ for
$n < 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib`, a definition declared in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib).

## Recurrence for n-color compositions with two consecutive colors

Fix a natural number
$b \ge 1$. For an integer $m$, let $c(m)$ be the number of $n$-color compositions of $m$ in
which every part has color $b$ or $b+1$ when $m \ge 0$, and $c(m) = 0$ when $m < 0$. Then for
every integer $n \ge 2$,

$$c(n) = c(n-1) + c(n-b) + c(n-b-1).$$

The source states the recurrence for positive $n$, but it fails at $n = 1$: for $b = 1$ the
left side is $1$ and the right side is $2$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Proposition 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowedZ_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-allowed-z-recurrence).

## Double-sum formula for n-color compositions with two consecutive colors

Let $b \ge 1$
and $n \ge 1$ be natural numbers, and let $\operatorname{cco}_{b,b+1}(n)$ be the number of
$n$-color compositions of $n$ in which every part has color $b$ or $b+1$. Then

$$\operatorname{cco}_{b,b+1}(n) = \sum_{m=1}^{n} \sum_{i=0}^{n-bm}
\binom{i+m-1}{m-1} \binom{m}{n-bm-i},$$

where the upper limit $n - bm$ is read as $0$ when $bm > n$, and every term with $bm + i > n$
is $0$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Proposition 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowed_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-allowed-eq-sum).

## Bijection between n-color compositions with colors b, b+1 and ternary strings

For all
natural numbers $b \ge 1$ and $n \ge 1$, there is a bijection between $\mathrm{CCo}_{b,b+1}(n)$,
the $n$-color compositions of $n$ using only the colors $b$ and $b+1$, and the set of strings of
length $n-1$ over the alphabet $\{0, 1, 2\}$ such that, when the string is cut at each of its
$0$s, every resulting segment (including the possibly empty segments before the first $0$, after
the last $0$, and between adjacent $0$s) either consists only of $1$s and has length at least
$b-1$, or consists only of $2$s and has length at least $b$.

The paper states the condition as: no subword $12$ or $21$, runs of $1$s of length at least
$b-1$, runs of $2$s of length at least $b$, and successive $0$s separated by at least $b-1$
digits. The segment form above also constrains the segments before the first and after the last
$0$; without that, the string $0$ would be a counterexample at $n = 2$, $b = 3$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.nonempty_equiv_colorCompAllowed_ternary` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#nonempty-equiv-color-comp-allowed-ternar).

## Binomial sum for n-color compositions with colors 1 and 2

For every natural number
$n \ge 1$, the number $\operatorname{cco}_{1,2}(n)$ of $n$-color compositions of $n$ in which
every part has color $1$ or $2$ satisfies

$$\operatorname{cco}_{1,2}(n) = \sum_{m=0}^{\lfloor n/2 \rfloor} 2^m \binom{n}{2m}.$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowed_one_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-allowed-one-eq-sum).

## n-color compositions with colors 2, 3 and compositions with parts not divisible by 3

For
every natural number $n \ge 1$, there is a bijection between $\mathrm{CCo}_{2,3}(n+1)$, the
$n$-color compositions of $n+1$ using only the colors $2$ and $3$, and the compositions of $n$ all
of whose parts are congruent to $1$ or $2$ modulo $3$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 4.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.nonempty_equiv_colorCompAllowed_two_composition_mod_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#nonempty-equiv-color-comp-allowed-two-co).

## n-color compositions with colors 2, 3 and compositions with two kinds of 1

For every
natural number $n$, there is a bijection between $\mathrm{CCo}_{2,3}(n+2)$, the $n$-color
compositions of $n+2$ using only the colors $2$ and $3$, and the compositions of $n$ whose parts
are $2$ or one of two types of part $1$, with no two adjacent parts $1$ of the same type.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 5.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.nonempty_equiv_colorCompAllowed_two_twoTypeComp` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#nonempty-equiv-color-comp-allowed-two-tw).

## Tribonacci numbers from $t(n-2)$ and a partial sum

Let $t$ be the tribonacci numbers
with $t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and $t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$,
extended by $t(n) = 0$ for $n < 0$. For every integer $n \ge 3$,

$$t(n) = t(n-2) + 2 \sum_{i=3}^{n} t(n-i).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Proposition 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_eq_add_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-eq-add-sum).

## Tribonacci numbers from $t(n-1)$ and alternate earlier terms

Let $t$ be the tribonacci
numbers with $t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and $t(n) = t(n-1) + t(n-2) + t(n-3)$ for
$n \ge 3$, extended by $t(n) = 0$ for $n < 0$. For every integer $n \ge 3$,

$$t(n) = t(n-1) + 1 + 2 \sum_{i=1}^{\lfloor n/2 \rfloor - 1} t(n-2i-1).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Proposition 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_eq_add_one_add_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-eq-add-one-add-sum).

## Tribonacci partial-sum identity for $t(3k)$

Let $t$ be the tribonacci numbers with
$t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and $t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$,
extended by $t(n) = 0$ for $n < 0$. For every natural number $k$,

$$t(3k) = 1 + \sum_{i=0}^{k} \bigl(t(3k-3i-1) + t(3k-3i-2)\bigr).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_three_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-three-mul).

## Tribonacci partial-sum identity for $t(3k+1)$

Let $t$ be the tribonacci numbers with
$t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and $t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$,
extended by $t(n) = 0$ for $n < 0$. For every natural number $k$,

$$t(3k+1) = -1 + \sum_{i=0}^{k} \bigl(t(3k-3i) + t(3k-3i-1)\bigr).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_three_mul_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-three-mul-add-one).

## Tribonacci partial-sum identity for $t(3k+2)$

Let $t$ be the tribonacci numbers with
$t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and $t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$,
extended by $t(n) = 0$ for $n < 0$. For every natural number $k$,

$$t(3k+2) = \sum_{i=0}^{k} \bigl(t(3k-3i+1) + t(3k-3i)\bigr).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_three_mul_add_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-three-mul-add-two).

## Identity for $t(n) + t(n-2)$ when $n \ge 3$ and $n \equiv 0, 1 \pmod 3$

Let $t$ be the
tribonacci numbers with $t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and
$t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$, extended by $t(n) = 0$ for $n < 0$. For every
natural number $k \ge 1$, both $n = 3k$ and $n = 3k + 1$ satisfy

$$t(n) + t(n-2) = 2 \sum_{i=0}^{k-1} t(n-3i-1).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_add_two_sub_three_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-add-two-sub-three-mul).

## Identity for $t(n) + t(n-2)$ when $n \ge 3$ and $n \equiv 2 \pmod 3$

Let $t$ be the
tribonacci numbers with $t(0) = 1$, $t(1) = 0$, $t(2) = 1$ and
$t(n) = t(n-1) + t(n-2) + t(n-3)$ for $n \ge 3$, extended by $t(n) = 0$ for $n < 0$. For every
natural number $k \ge 1$, with $n = 3k + 2$,

$$t(n) + t(n-2) = 2 + 2 \sum_{i=0}^{k-1} t(n-3i-1).$$

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.trib_add_two_sub_three_mul_add_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#trib-add-two-sub-three-mul-add-two).

## Fibonacci identity for n-color compositions with colors 3 and 4

For a natural number
$m$, let $\operatorname{cco}_{3,4}(m)$ be the number of $n$-color compositions of $m$ in which
every part has color $3$ or $4$, and let $F_k$ be the Fibonacci numbers with $F_0 = 0$ and
$F_1 = 1$. Then for every natural number $n \ge 3$,
$\operatorname{cco}_{3,4}(n) + \operatorname{cco}_{3,4}(n-2) = F_{n-1}$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Proposition 10.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoAllowed_three_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-allowed-three-add).

## Recurrence for n-color compositions avoiding two consecutive colors

Fix a natural number
$b \ge 1$. For an integer $m$, let $c(m)$ be the number of $n$-color compositions of $m$ in
which no part has color $b$ or $b+1$ when $m \ge 0$, and $c(m) = 0$ when $m < 0$. Then for
every integer $n \ge 3$,

$$c(n) = 3\,c(n-1) - c(n-2) - c(n-b) + c(n-b-2).$$

The source states the recurrence without a range, but it fails at $n = 0$, $1$ and $2$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Proposition 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibitedZ_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-prohibited-z-recurrence).

## n-color compositions without colors 1, 2 and compositions with parts 1, 2 mod 4

For
every natural number $n \ge 1$, there is a bijection between $\mathrm{CCo}_{\widehat{1,2}}(n+2)$,
the $n$-color compositions of $n+2$ in which no part has color $1$ or $2$, and the compositions of
$n$ all of whose parts are congruent to $1$ or $2$ modulo $4$.

The hypothesis $n \ge 1$ is needed: at $n = 0$ the two sets have $0$ and $1$ elements.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.nonempty_equiv_colorCompProhibited_one_composition_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#nonempty-equiv-color-comp-prohibited-one).

## n-color compositions without colors 1, 2 and palindromic compositions

For every natural
number $n \ge 1$, there is a bijection between $\mathrm{CCo}_{\widehat{1,2}}(n)$, the $n$-color
compositions of $n$ in which no part has color $1$ or $2$, and the palindromic compositions of
$\max(2n-5, 0)$ that have no part equal to $2$ and an odd number of parts.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 13.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.nonempty_equiv_colorCompProhibited_one_palindromic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#nonempty-equiv-color-comp-prohibited-one-2).

## n-color compositions avoiding colors 1 and 2 versus avoiding color 2

For a natural number
$m$, let $\operatorname{cco}_{\widehat{1,2}}(m)$ be the number of $n$-color compositions of $m$ in
which no part has color $1$ or $2$, and let $\operatorname{cco}_{\hat 2}(m)$ be the number in which
no part has color $2$. Then for every natural number $k \ge 1$,
$\operatorname{cco}_{\widehat{1,2}}(3k) = \operatorname{cco}_{\hat 2}(2k-1)$.

## Sources

- Brian Hopkins and Hua Wang, "Allowing or Prohibiting Two Consecutive Colors in `n`-Color Compositions", Theorem 14.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.NColorCompositionsWanted.ccoProhibited_one_three_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NColorCompositionsWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html#cco-prohibited-one-three-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Restricted n-color compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/restricted-n-color-compositions)
