---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.SierpinskiMersenneWanted.exists_arithProg_sierpinski_add_mersenne, MetaMathlibExt.IsSierpinskiNumber, MetaMathlibExt.IsRieselNumber, MetaMathlibExt.not_isSierpinskiNumber_one, MetaMathlibExt.not_isRieselNumber_one, MetaMathlibExt.repstring, MetaMathlibExt.repstring_ten_one_two_three, MetaMathlibExt.repstring_two_one_zero_three
statement: formalized
---

# Sierpiński and Riesel numbers

30 results, 11 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html).

## Composite numbers from Mersenne shifts of an arithmetic progression

For a natural
number $j$ let $M_j = 2^j - 1$ be the $j$-th Mersenne number (so $M_0 = 0$). For every natural
number $t$ there are natural numbers $a$ and $d > 0$ such that, for every natural number $r$,
every natural number $j \le t$ and every natural number $n$, the number
$(a + rd + M_j) \cdot 2^n + 1$ is composite.

## Sources

- Carrie E. Finch-Smith and R. Scottfield Groth, "Arbitrarily Long Sequences of Sierpiński Numbers that are the Sum of a Sierpiński Number and a Mersenne Number", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.SierpinskiMersenneWanted.exists_arithProg_sierpinski_add_mersenne` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiMersenneWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiMersenneWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#exists-arith-prog-sierpinski-add-mersenn).

## Sierpiński number

A natural number $k$ is a Sierpiński number if $k$ is odd and,
for every integer $n \ge 1$, the number $k \cdot 2^n + 1$ is not prime.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, abstract and Section 1.

Formalized by `MetaMathlibExt.IsSierpinskiNumber`, a definition declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-sierpinski-number).

## Riesel number

A natural number $k$ is a Riesel number if $k$ is odd and, for every
integer $n \ge 1$, the number $k \cdot 2^n - 1$ is not prime.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, abstract and Section 1.

Formalized by `MetaMathlibExt.IsRieselNumber`, a definition declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-riesel-number).

## $1$ is not a Sierpiński number

The number $1$ is not a Sierpiński number, since
$1 \cdot 2 + 1 = 3$ is prime.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 1.

Formalized by `MetaMathlibExt.not_isSierpinskiNumber_one`, a theorem declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#not-is-sierpinski-number-one).

## One is not a Riesel number

The number $1$ is not a Riesel number, since
$1 \cdot 2^2 - 1 = 3$ is prime.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 1.

Formalized by `MetaMathlibExt.not_isRieselNumber_one`, a theorem declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#not-is-riesel-number-one).

## Repstrings

For natural numbers $b$, $k$, $z$ and $t$, let $\ell$ be the number of base-$b$
digits of $k$. The $b$-repstring is

$$k_b^{(z;t)} = \left\lfloor \frac{k\,(b^{(z+\ell)t} - 1)}{b^{z+\ell} - 1} \right\rfloor,$$

where subtraction is truncated at $0$ and the integer division gives $0$ when the denominator is
$0$. For $z = 0$ it is the $b$-repinteger $k_b^{(t)}$.

For $b \ge 2$ and $k \ge 1$ the division is exact, and $k_b^{(z;t)}$ is the number whose base-$b$
expansion is $k$ written $t$ times with $z$ zeros between consecutive copies.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Sections 1 and 4.

Formalized by `MetaMathlibExt.repstring`, a definition declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#repstring).

## A $10$-repstring

The $10$-repstring with $k = 1$, $z = 2$ and $t = 3$ is
$1_{10}^{(2;3)} = 1001001$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 4.

Formalized by `MetaMathlibExt.repstring_ten_one_two_three`, a theorem declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#repstring-ten-one-two-three).

## The three-digit $2$-repunit

The $2$-repstring with $k = 1$, $z = 0$ and $t = 3$, that is,
the $2$-repunit $1_2^{(3)}$ with three digits, equals $7$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 1.

Formalized by `MetaMathlibExt.repstring_two_one_zero_three`, a theorem declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#repstring-two-one-zero-three).

## Sierpiński covering data

Let $k$ be a natural number and $S$ a finite set of triples
$(r, m, p)$ of natural numbers. Then $S$ is Sierpiński covering data for $k$ if every integer is
congruent to $r$ modulo $m$ for some $(r, m, p) \in S$, distinct triples in $S$ have distinct
third entries, and every $(r, m, p) \in S$ has $m \ge 1$, $p$ prime, $p \mid 2^m - 1$ and
$p \mid k \cdot 2^r + 1$.

This is the input of the covering system method for Sierpiński numbers; the last condition says
that $k \equiv -2^{-r} \pmod{p}$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 2, Equation (2).

Formalized by `MetaMathlibExt.IsSierpinskiCoveringData`, a definition declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-sierpinski-covering-data).

## Riesel covering data

Let $k$ be a natural number and let $S$ be a finite set of triples
$(r, m, p)$ of natural numbers. Then $S$ is Riesel covering data for $k$ (data producing $k$ as a
Riesel number by the covering system method) when every integer is congruent to $r$ modulo $m$
for some $(r, m, p) \in S$, distinct triples in $S$ have distinct third entries $p$, and every
$(r, m, p) \in S$ has $m \ge 1$, $p$ prime, $p \mid 2^m - 1$ and $p \mid k \cdot 2^r - 1$ (for
$k \ge 1$ the last condition says $k \equiv 2^{-r} \pmod p$).

Subtraction is in the natural numbers, so for $k = 0$ the condition $p \mid k \cdot 2^r - 1$ reads
$p \mid 0$ and holds trivially.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 2, Equation (3).

Formalized by `MetaMathlibExt.IsRieselCoveringData`, a definition declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-riesel-covering-data).

## Empty Sierpiński covering data

For every natural number $k$, the empty set is not
Sierpiński covering data for $k$: the empty family of residue classes does not cover $\mathbb{Z}$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 2.

Formalized by `MetaMathlibExt.not_isSierpinskiCoveringData_empty`, a theorem declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#not-is-sierpinski-covering-data-empty).

## The empty set is not Riesel covering data

For every natural number $k$, the empty set is
not Riesel covering data for $k$, because its residue classes do not cover $\mathbb{Z}$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Section 2.

Formalized by `MetaMathlibExt.not_isRieselCoveringData_empty`, a theorem declared in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#not-is-riesel-covering-data-empty).

## Theorem 3.2 (no Sierpiński $2$-repdigits from coverings)

For every natural number
$t \ge 1$, the covering system method cannot produce the $2$-repdigit $2^t - 1$ as a
Sierpiński number: no finite set of triples $(r_j, m_j, p_j)$ is Sierpiński covering data
for $2^t - 1$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.2.

Stated but not proved: `MetaMathlibExt.not_isSierpinskiCoveringData_two_pow_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#not-is-sierpinski-covering-data-two-pow).

## Covering-produced Sierpiński numbers give infinitely many Sierpiński repintegers

Let $k$
be a Sierpiński number that has Sierpiński covering data, so that $k$ is produced as a Sierpiński
number by the covering system method. Then for every natural number $b \ge 2$ there are infinitely
many $t \ge 1$ such that the $b$-repinteger $k_b^{(t)} = k\,(b^{\ell t} - 1)/(b^{\ell} - 1)$, where
$\ell$ is the number of base-$b$ digits of $k$ (so $k_b^{(t)}$ is $k$ written $t$ times in base
$b$), is a Sierpiński number.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.3.

Stated but not proved: `MetaMathlibExt.infinite_sierpinski_repintegers` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-sierpinski-repintegers).

## Covering-produced Riesel numbers give infinitely many Riesel repintegers

Let $k$ be a
Riesel number that has Riesel covering data, so that $k$ is produced as a Riesel number by the
covering system method. Then for every natural number $b \ge 2$ there are infinitely many $t \ge 1$
such that the $b$-repinteger $k_b^{(t)} = k\,(b^{\ell t} - 1)/(b^{\ell} - 1)$, where $\ell$ is the
number of base-$b$ digits of $k$ (so $k_b^{(t)}$ is $k$ written $t$ times in base $b$), is a Riesel
number.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.4.

Stated but not proved: `MetaMathlibExt.infinite_riesel_repintegers` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-riesel-repintegers).

## Binary repintegers of 18107 that are Sierpiński numbers

For every natural number
$t \equiv 25 \pmod{56}$, the binary repinteger $18107_2^{(t)} = 18107\,(2^{15t} - 1)/(2^{15} - 1)$,
whose binary expansion is that of $18107$ (fifteen binary digits) written $t$ times, is a
Sierpiński number.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.5.

Stated but not proved: `MetaMathlibExt.isSierpinskiNumber_repstring_18107` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-sierpinski-number-repstring-18107).

## Binary repintegers of 18107 that are Riesel numbers

For every natural number
$t \equiv 31 \pmod{56}$, the binary repinteger $18107_2^{(t)} = 18107\,(2^{15t} - 1)/(2^{15} - 1)$,
whose binary expansion is that of $18107$ (fifteen binary digits) written $t$ times, is a Riesel
number.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.6.

Stated but not proved: `MetaMathlibExt.isRieselNumber_repstring_18107` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-riesel-number-repstring-18107).

## Infinitely many Sierpiński repdigits in every base $b > 78557$

Let $b > 78557$ be a
natural number. Then there are infinitely many Sierpiński numbers of the form $k(b^t - 1)/(b - 1)$
with $1 \le k < b$ and $t \ge 1$, that is, $b$-repdigits: the digit $k$ written $t$ times in
base $b$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Corollary 3.7.

Stated but not proved: `MetaMathlibExt.infinite_sierpinski_repdigits` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-sierpinski-repdigits).

## Infinitely many Riesel repdigits in every base $b > 509203$

Let $b > 509203$ be a
natural number. Then there are infinitely many Riesel numbers of the form $k(b^t - 1)/(b - 1)$ with
$1 \le k < b$ and $t \ge 1$, that is, $b$-repdigits: the digit $k$ written $t$ times in base $b$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Corollary 3.8.

Stated but not proved: `MetaMathlibExt.infinite_riesel_repdigits` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-riesel-repdigits).

## Repdigits with digit 41 that are Sierpiński numbers

Let $b$ and $t$ be natural numbers
with $b \equiv 87 \pmod{11184810}$ and $t \equiv 59 \pmod{120}$. Then the base-$b$ repdigit
$41_b^{(t)} = 41\,(b^t - 1)/(b - 1)$ is a Sierpiński number. Since $b \ge 87 > 41$, its $t$
base-$b$ digits all equal $41$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.9.

Stated but not proved: `MetaMathlibExt.isSierpinskiNumber_repstring_41` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-sierpinski-number-repstring-41).

## Riesel repdigits with digit $101$ in bases $b \equiv 180 \pmod{11184810}$

Let $b$ and $t$
be natural numbers with $b \equiv 180 \pmod{11184810}$ and $t \equiv 171 \pmod{240}$. Then the
$b$-repinteger $101_b^{(t)}$, which is the repdigit $101\,(b^t - 1)/(b - 1)$ because $101 < b$, is
a Riesel number.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.10.

Stated but not proved: `MetaMathlibExt.isRieselNumber_repstring_101` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-riesel-number-repstring-101).

## Infinitely many Sierpiński repunits from primitive divisors of $2^{2^j} - 1$

Let $\tau$
be a natural number. For $1 \le j \le \tau$ let $p_j$ be a primitive prime divisor of
$2^{2^j} - 1$ in the sequence $(2^m - 1)_{m \ge 0}$, and let $q \ne p_\tau$ be a primitive prime
divisor of $2^{2^\tau} - 1$ in the same sequence. Let $b > 2$ be a natural number with $q \nmid b$.
For $1 \le j \le \tau$ put $\ell_j = 1$ if $p_j \mid b$, $\ell_j = p_j$ if $p_j \nmid b$ and
$b \equiv 1 \pmod{p_j}$, and otherwise $\ell_j = \operatorname{ord}_{p_j}(b)$, the multiplicative
order of $b$ modulo $p_j$; let $L = \operatorname{lcm}(2, \ell_1, \dots, \ell_\tau)$. Suppose that
either (i) $b \equiv 1 \pmod q$ and $q \nmid L$, or (ii) $b \not\equiv 1 \pmod q$ and there is a
natural number $s \equiv 1 \pmod L$ with $(b^s - 1)/(b - 1) \equiv -1 \pmod q$. Then there are
infinitely many Sierpiński numbers among the $b$-repunits $(b^t - 1)/(b - 1)$ with $t \ge 1$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.11.

Stated but not proved: `MetaMathlibExt.infinite_sierpinski_repunits_of_primitive_divisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-sierpinski-repunits-of-primitiv).

## Infinitely many Sierpiński repunits in bases $b \equiv 1, 147, 265, 378 \pmod{641}$ with $b \not\equiv 1 \pmod 5$

**Infinitely many Sierpiński repunits in bases $b \equiv 1, 147, 265, 378 \pmod{641}$ with
$b \not\equiv 1 \pmod 5$.** Let $b > 2$ be a natural number with $b \equiv c \pmod{641}$ for some
$c \in \{1, 147, 265, 378\}$ and $b \not\equiv 1 \pmod 5$. Then there are infinitely many
Sierpiński numbers among the $b$-repunits $(b^t - 1)/(b - 1)$ with $t \ge 1$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Corollary 3.12.

Stated but not proved: `MetaMathlibExt.infinite_sierpinski_repunits_mod_641` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-sierpinski-repunits-mod-641).

## Infinitely many Riesel repunits from primitive divisors of $2^{2^j} - 1$

Let $\tau$ be a
natural number. For $1 \le j \le \tau$ let $p_j$ be a primitive prime divisor of $2^{2^j} - 1$ in
the sequence $(2^m - 1)_{m \ge 0}$, let $q \ne p_\tau$ be a primitive prime divisor of
$2^{2^\tau} - 1$ in the same sequence, and put $P = p_1 \cdots p_\tau$. Let $b > 2$ be a natural
number with $b \equiv 1 \pmod P$, and suppose that (i) $q \mid b$, or (ii) $b \equiv 1 \pmod q$, or
(iii) $q \nmid b$, $b \not\equiv 1 \pmod q$ and $\gcd(P, \operatorname{ord}_q(b)) = 1$, where
$\operatorname{ord}_q(b)$ is the multiplicative order of $b$ modulo $q$. Then there are infinitely
many Riesel numbers among the $b$-repunits $(b^t - 1)/(b - 1)$ with $t \ge 1$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 3.13.

Stated but not proved: `MetaMathlibExt.infinite_riesel_repunits_of_primitive_divisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-riesel-repunits-of-primitive-di).

## Infinitely many Riesel repunits in bases $b \equiv 16518444216571 \pmod{2^{64} - 1}$

Let $b$ be a natural number with $b \equiv 16518444216571 \pmod{18446744073709551615}$, where
$18446744073709551615 = 2^{64} - 1$. Then there are infinitely many Riesel numbers among the
$b$-repunits $(b^t - 1)/(b - 1)$ with $t \ge 1$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Corollary 3.14.

Stated but not proved: `MetaMathlibExt.infinite_riesel_repunits_mod_two_pow_64_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-riesel-repunits-mod-two-pow-64).

## Binary repstrings of 659 that are Sierpiński numbers

For every natural number $t$ with
$t \equiv 131 \pmod{2730}$ or $t \equiv 1361 \pmod{2730}$, the binary repstring
$659_2^{(2;t)} = 659\,(2^{12t} - 1)/(2^{12} - 1)$ is a Sierpiński number. Its binary expansion is
that of $659$ (ten binary digits) written $t$ times with two zeros between consecutive copies.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 4.3.

Stated but not proved: `MetaMathlibExt.isSierpinskiNumber_repstring_659` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-sierpinski-number-repstring-659).

## Binary repstrings of 659 that are Riesel numbers

For every natural number $t$ with
$t \equiv 1369 \pmod{2730}$ or $t \equiv 2599 \pmod{2730}$, the binary repstring
$659_2^{(2;t)} = 659\,(2^{12t} - 1)/(2^{12} - 1)$ is a Riesel number. Its binary expansion is that
of $659$ (ten binary digits) written $t$ times with two zeros between consecutive copies.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 4.4.

Stated but not proved: `MetaMathlibExt.isRieselNumber_repstring_659` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-riesel-number-repstring-659).

## Theorem 4.6 (Sierpiński and Riesel repstring coverings correspond)

Let $k \ge 1$,
$\mathfrak{t} \ge 1$, $w \ge 1$ and $z \ge 0$ be natural numbers. There is a single finite set
of triples that is Sierpiński covering data for the $2$-repstring $k_2^{(z;t)}$ for every
$t \ge 1$ with $t \equiv \mathfrak{t} \pmod{w}$ if and only if there is a single finite set
of triples that is Riesel covering data for $k_2^{(z;t')}$ for every $t' \ge 1$ with
$t' \equiv -\mathfrak{t} \pmod{w}$.

## Sources

- Bispels, Cohen, Harrington, Lowrance, Pontes, Schaumann and Wong, *On Sierpiński and Riesel Repdigits and Repintegers*, INTEGERS 26 (2026), Article A12, Theorem 4.6.

Stated but not proved: `MetaMathlibExt.sierpinskiCoveringData_repstring_iff_riesel` is written with `theorem_wanted` in [WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SierpinskiRieselRepdigitsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#sierpinski-covering-data-repstring-iff-r).

## Narayana numbers that are Riesel numbers

Let $(N_t)$ be Narayana's cows sequence, with
$N_0 = 0$ and $N_1 = N_2 = 1$. If $t$ is congruent modulo $718391520$ to one of the $27$ residues
$3629412$, $13386852$, $73151172$, $96325092$, $101203812$, $119499012$, $175604292$,
$198778212$, $212194692$, $240247332$, $268299972$, $328064292$, $337821732$, $360995652$,
$384169572$, $402464772$, $425638692$, $467107812$, $476865252$, $495160452$, $564682212$,
$587856132$, $592734852$, $611030052$, $629325252$, $652499172$, $703725732$, then $N_t$ is a
Riesel number: $N_t$ is odd and $N_t \cdot 2^n - 1$ is not prime for every $n \ge 1$.

With this indexing, $N_t$ is odd exactly when $t \bmod 7 \in \{1, 2, 3, 5\}$.

## Sources

- Katherine Franzone and Joshua Harrington, *Sierpiński and Riesel Numbers in Narayana's Cow Sequence*, INTEGERS 24 (2024), Article A10, Theorem 2.

Stated but not proved: `MetaMathlibExt.isRieselNumber_narayanaCowsSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/NarayanaSierpinskiRieselWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NarayanaSierpinskiRieselWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#is-riesel-number-narayana-cows-sequence).

## Infinitely many Narayana numbers are Sierpiński numbers

There are infinitely many
natural numbers $k$ that are Sierpiński numbers and terms of Narayana's cows sequence $(N_t)$,
that is, $k = N_t$ for some $t$; here a Sierpiński number is an odd $k$ such that
$k \cdot 2^n + 1$ is not prime for every $n \ge 1$.

## Sources

- Katherine Franzone and Joshua Harrington, *Sierpiński and Riesel Numbers in Narayana's Cow Sequence*, INTEGERS 24 (2024), Article A10, Theorem 3.

Stated but not proved: `MetaMathlibExt.infinite_setOf_isSierpinskiNumber_narayanaCowsSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/NarayanaSierpinskiRieselWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NarayanaSierpinskiRieselWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html#infinite-set-of-is-sierpinski-number-nar).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sierpiński and Riesel numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/special-primes/sierpi-ski-and-riesel-numbers)
