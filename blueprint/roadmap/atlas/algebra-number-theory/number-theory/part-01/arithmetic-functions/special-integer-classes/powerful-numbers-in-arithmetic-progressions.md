---
declaration: section
origin: cited
lean: MetaMathlibExt.arbitrarily_long_arithmetic_progressions_of_powerful_numbers_general, MetaMathlibExt.arbitrarily_long_arithmetic_progressions_of_powerful_numbers, MathlibExt.NumberTheory.ErdosProblem937Wanted.IsCoprimePowerfulAP4, MathlibExt.NumberTheory.ErdosProblem937Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem937Wanted.conjecture_holds
statement: formalized
---

# Powerful numbers in arithmetic progressions

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html).

## Arithmetic progressions of 2-full numbers of every length

For every natural number
$k$ there are positive integers $a$ and $d$ such that $a + id$ is $2$-full (powerful) for every
natural number $i < k$.

Formalized by `MetaMathlibExt.arbitrarily_long_arithmetic_progressions_of_powerful_numbers_general`, a theorem declared in [MathlibExt/NumberTheory/PowerfulNumbersArithmeticProgressions.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerfulNumbersArithmeticProgressions.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html#arbitrarily-long-arithmetic-progressions).

## Arbitrarily long arithmetic progressions of powerful numbers

For every integer $k \ge 3$
there are positive integers $a$ and $d$ such that each of the $k$ numbers $a + id$ with
$0 \le i < k$ is powerful: every prime that divides $a + id$ has its square dividing $a + id$.

## Sources

- Tsz Ho Chan, "Arithmetic Progressions Among Powerful Numbers", Journal of Integer Sequences 26 (2023), Article 23.1.1, Theorem `thm-longAP`, source lines 97–99, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Chan/chan33.tex>. The paper notes the result is not new (see remark 2 in [H] there) and includes a proof for completeness. Powerful (squarefull) means every prime divisor appears with exponent at least two; nonconstant is `0 < d`. It follows from `arbitrarily_long_arithmetic_progressions_of_powerful_numbers_general`, which states powerfulness as `Nat.IsKFull 2`; the hypothesis `hk` is unused and keeps the source's shape.

Formalized by `MetaMathlibExt.arbitrarily_long_arithmetic_progressions_of_powerful_numbers`, a theorem declared in [MathlibExt/NumberTheory/PowerfulNumbersArithmeticProgressions.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PowerfulNumbersArithmeticProgressions.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html#arbitrarily-long-arithmetic-progressions-2).

## Four-term progressions of pairwise coprime powerful numbers

For natural numbers $a$ and
$d$, the numbers $a$, $a + d$, $a + 2d$, $a + 3d$ form a four-term arithmetic progression of
pairwise coprime powerful numbers when $d > 0$, each of the four numbers is powerful (that is,
$2$-full: nonzero and divisible by $p^2$ for every prime $p$ dividing it), and any two of the
four numbers are coprime.

Formalized by `MathlibExt.NumberTheory.ErdosProblem937Wanted.IsCoprimePowerfulAP4`, a definition declared in [WantedExt/NumberTheory/ErdosProblem937Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem937Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html#is-coprime-powerful-ap4).

## Statement of Erdős Problem 937

There are infinitely many pairs of natural numbers
$(a, d)$ with $d > 0$ such that the four numbers $a$, $a + d$, $a + 2d$, $a + 3d$ are powerful
(each is nonzero and divisible by $p^2$ for every prime $p$ dividing it) and pairwise coprime;
that is, infinitely many four-term arithmetic progressions of pairwise coprime powerful numbers.

Formalized by `MathlibExt.NumberTheory.ErdosProblem937Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem937Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem937Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html#conjecture).

## Erdős Problem 937 holds (Bajpai–Bennett–Chan)

There are infinitely many pairs of natural
numbers $(a, d)$ with $d > 0$ such that the four numbers $a$, $a + d$, $a + 2d$, $a + 3d$ are
powerful (each is nonzero and divisible by $p^2$ for every prime $p$ dividing it) and pairwise
coprime. That is, there are infinitely many four-term arithmetic progressions of pairwise coprime
powerful numbers.

## Sources

- Prajeet Bajpai, Michael A. Bennett, and Tsz Ho Chan, Arithmetic progressions in squarefull numbers, International Journal of Number Theory 20 (2024), 19–45, https://mathscinet.ams.org/mathscinet-getitem?mr=4688726. Resolved true: Resolved true by Bajpai–Bennett–Chan; a proof is available in an external Lean development.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem937Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem937Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem937Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Powerful numbers in arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/powerful-numbers-in-arithmetic-progressions)
