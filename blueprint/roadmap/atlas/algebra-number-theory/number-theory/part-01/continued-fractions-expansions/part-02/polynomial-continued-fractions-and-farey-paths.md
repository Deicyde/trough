---
declaration: section
origin: cited
lean: MetaMathlibExt.polyContFract, MetaMathlibExt.polyContFract_h, MetaMathlibExt.polyContFract_s_get?, MetaMathlibExt.polyContFract_nums_zero, MetaMathlibExt.polyContFract_dens_zero, MetaMathlibExt.polyContFract_nums_one, MetaMathlibExt.polyContFract_dens_one, MetaMathlibExt.polyContFract_convergents_farey_path
statement: formalized
---

# Polynomial continued fractions and Farey paths

23 results, 14 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html).

## Finite continued fraction with polynomial partial quotients

Let $F$ be a field, let
$a_0, a_1, a_2, \ldots$ be polynomials in $F[X]$ and let $n \in \mathbb{N}$. The continued
fraction $[a_0; a_1, \ldots, a_n]$ is the generalized continued fraction over the field $F(X)$ of
rational functions with integral part $a_0$ and, for $1 \le i \le n$, an $i$th term with partial
numerator $1$ and partial denominator $a_i$; it has no further terms. For $i \ge 0$ write $A_i$
and $B_i$ for the numerator and denominator of its $i$th convergent $A_i / B_i$. Thus, with
$A_{-1} = 1$ and $B_{-1} = 0$, we have $A_0 = a_0$, $B_0 = 1$, and $A_{i+1} = a_{i+1} A_i + A_{i-1}$
and $B_{i+1} = a_{i+1} B_i + B_{i-1}$ for $0 \le i < n$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract`, a definition declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract).

## Integral part of a polynomial continued fraction

Let $F$ be a field, let $n \in \mathbb N$,
and let $a_0, a_1, \dots, a_n \in F[X]$. The integral part (head term) of the continued fraction
$[a_0, a_1, \dots, a_n]$ over $F(X)$ is $a_0$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract_h`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-h).

## Terms of a polynomial continued fraction

Let $F$ be a field, let $a_0, a_1, \ldots$ be
polynomials in $F[X]$ and let $n \in \mathbb{N}$. For every $i \in \mathbb{N}$, the term of index
$i$ (counting from $0$) of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ is the
pair with partial numerator $1$ and partial denominator $a_{i+1}$ if $i < n$, and does not exist
if $i \ge n$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract_s_get?`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-s-get).

## Zeroth convergent numerator of a polynomial continued fraction

Let $F$ be a field,
let $a_0, a_1, \ldots$ be polynomials in $F[X]$ and let $n \in \mathbb{N}$. The numerator $A_0$
of the zeroth convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ is
$a_0$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract_nums_zero`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-nums-zero).

## Zeroth convergent denominator of a polynomial continued fraction

Let $F$ be a field,
let $a_0, a_1, \ldots$ be polynomials in $F[X]$ and let $n \in \mathbb{N}$. The denominator $B_0$
of the zeroth convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ is $1$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract_dens_zero`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-dens-zero).

## First convergent numerator of a polynomial continued fraction

Let $F$ be a field,
let $a_0, a_1, \ldots$ be polynomials in $F[X]$ and let $n \ge 1$. The numerator $A_1$ of the
first convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ is
$a_1 a_0 + 1$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract_nums_one`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-nums-one).

## First convergent denominator of a polynomial continued fraction

Let $F$ be a field,
let $a_0, a_1, \ldots$ be polynomials in $F[X]$ and let $n \ge 1$. The denominator $B_1$ of the
first convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ is $a_1$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Section 1.

Formalized by `MetaMathlibExt.polyContFract_dens_one`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-dens-one).

## Convergents of a polynomial continued fraction form a Farey path

Let $F$ be a field, let
$n \in \mathbb N$, and let $a_0, a_1, \dots, a_n \in F[X]$ with $a_i$ nonconstant for
$1 \le i \le n$. Write $A_i$ and $B_i$ for the numerator and the denominator of the $i$th
convergent $A_i / B_i$ of the continued fraction $[a_0, a_1, \dots, a_n]$ over $F(X)$. Then for
every $i \le n$, $A_i$ and $B_i$ are polynomials in $F[X]$, $B_i \ne 0$, and $A_i$ and $B_i$ are
coprime in $F[X]$; and for $1 \le i \le n$, the polynomial $A_i B_{i-1} - A_{i-1} B_i$ is a unit
of $F[X]$, that is, a nonzero constant.

In the language of the paper, each convergent $A_i / B_i$ is a vertex of the Farey graph over $F$
and consecutive convergents are adjacent in it.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Theorem 4.

Stated but not proved: `MetaMathlibExt.polyContFract_convergents_farey_path` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-convergents-farey-path).

## Extending a Farey path extends the continued fraction

Let $F$ be a field, let $n \ge 1$,
and let $a_0, a_1, \dots, a_n \in F[X]$ with $a_i$ nonconstant for $1 \le i \le n$. Let
$A_0, \dots, A_n, B_0, \dots, B_n \in F[X]$ be such that, for every $i \le n$, $A_i$ and $B_i$ are
the numerator and the denominator of the $i$th convergent of the continued fraction
$[a_0, a_1, \dots, a_n]$ over $F(X)$. Let $u, v \in F[X]$ be such that $u B_n - v A_n$ is a unit
of $F[X]$ (a nonzero constant) and $\deg B_n < \deg v$. Then there is a nonconstant polynomial
$b \in F[X]$ such that, in $F(X)$,

$$b = \frac{v A_{n-1} - u B_{n-1}}{u B_n - v A_n},$$

and the $(n+1)$st convergent of the continued fraction $[a_0, a_1, \dots, a_n, b]$ equals $u/v$.

Compared with the paper: the case $n = 0$, which needs $A_{-1} = 1$ and $B_{-1} = 0$, is excluded;
the paper's degree condition on the reduced denominator of $A_n / B_n$ is stated with $B_n$ itself
(the two agree, since $A_n / B_n$ is already in lowest terms); and the hypothesis that $u$ and $v$
are coprime is omitted, since adjacency implies it.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Theorem 5.

Stated but not proved: `MetaMathlibExt.polyContFract_extend_farey_path` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-extend-farey-path).

## Continued fraction along a Farey path of polynomials

Let $F$ be a field, let
$n \in \mathbb N$, let $u_i, v_i \in F[X]$ for $i \ge 0$, and let $c_i \in F$ for $i \ge 1$.
Suppose that $v_0 = 1$ and that for $1 \le i \le n$ we have $c_i \ne 0$,
$\deg v_{i-1} < \deg v_i$ and $u_i v_{i-1} - u_{i-1} v_i = c_i$. Let $a_0, a_1, \ldots \in F[X]$
satisfy $a_0 = u_0$, $a_1 = c_1^{-1} v_1$, $a_2 = -c_2^{-1} c_1 (u_2 v_0 - u_0 v_2)$ and, for
$3 \le i \le n$,

$$a_i = (-1)^{i+1}c_i^{-1}c_{i-1}(u_i v_{i-2} - u_{i-2} v_i)\prod_{j=1}^{i-2} c_j^{2(-1)^{i-j+1}}.$$

Then $a_i$ is nonconstant for $1 \le i \le n$. Moreover, for every $i \le n$ let
$t_i = \varepsilon_i \prod_{j=1}^{i} c_j^{(-1)^{i-j+1}}$, where $\varepsilon_i = 1$ if
$i \equiv 0, 1 \pmod 4$ and $\varepsilon_i = -1$ if $i \equiv 2, 3 \pmod 4$. Then the numerator
$A_i$ and the denominator $B_i$ of the $i$th convergent of the continued fraction
$[a_0; a_1, \ldots, a_n]$ over $F(X)$ are $A_i = t_i u_i$ and $B_i = t_i v_i$, and this
convergent equals $u_i / v_i$.

The paper's coprimality hypothesis $(u_i, v_i) = 1$ is omitted: it follows from the determinant
condition.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Theorem 6.

Stated but not proved: `MetaMathlibExt.polyContFract_of_farey_path` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-of-farey-path).

## Farey paths of polynomials with alternating determinants starting at 1

Let $F$ be a
field, let $n \in \mathbb{N}$, and let $u_i, v_i \in F[X]$ for $i \ge 0$. Suppose that $v_0 = 1$
and that for $1 \le i \le n$ we have $\deg v_{i-1} < \deg v_i$ and
$u_i v_{i-1} - u_{i-1} v_i = (-1)^{i-1}$. Let $a_0, a_1, \ldots \in F[X]$ satisfy $a_0 = u_0$,
$a_1 = v_1$ and $a_i = (-1)^i (u_i v_{i-2} - u_{i-2} v_i)$ for $2 \le i \le n$. Then $a_i$ is
nonconstant for $1 \le i \le n$, and for every $i \le n$ the numerator $A_i$ and denominator
$B_i$ of the $i$th convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$
are $A_i = u_i$ and $B_i = v_i$.

The paper presents the corollaries for $\mathbb{F}_2$ and $\mathbb{F}_3$; the statement holds
verbatim over any field.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Corollary 1.

Stated but not proved: `MetaMathlibExt.polyContFract_of_farey_path_det_neg_one_pow_pred` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-of-farey-path-det-neg-on).

## Farey paths of polynomials with alternating determinants starting at −1

Let $F$ be a
field, let $n \in \mathbb{N}$, and let $u_i, v_i \in F[X]$ for $i \ge 0$. Suppose that $v_0 = 1$
and that for $1 \le i \le n$ we have $\deg v_{i-1} < \deg v_i$ and
$u_i v_{i-1} - u_{i-1} v_i = (-1)^i$. Let $a_0, a_1, \ldots \in F[X]$ satisfy $a_0 = u_0$,
$a_1 = -v_1$ and $a_i = (-1)^i (u_i v_{i-2} - u_{i-2} v_i)$ for $2 \le i \le n$. Then $a_i$ is
nonconstant for $1 \le i \le n$, and for every $i \le n$ the numerator $A_i$ and denominator
$B_i$ of the $i$th convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$
are $A_i = (-1)^i u_i$ and $B_i = (-1)^i v_i$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Corollary 2.

Stated but not proved: `MetaMathlibExt.polyContFract_of_farey_path_det_neg_one_pow` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-of-farey-path-det-neg-on-2).

## Farey paths of polynomials with all determinants 1

Let $F$ be a field, let
$n \in \mathbb{N}$, and let $u_i, v_i \in F[X]$ for $i \ge 0$. Suppose that $v_0 = 1$ and that
for $1 \le i \le n$ we have $\deg v_{i-1} < \deg v_i$ and $u_i v_{i-1} - u_{i-1} v_i = 1$. Let
$a_0, a_1, \ldots \in F[X]$ satisfy $a_0 = u_0$, $a_1 = v_1$ and
$a_i = (-1)^{i+1} (u_i v_{i-2} - u_{i-2} v_i)$ for $2 \le i \le n$. Then $a_i$ is nonconstant
for $1 \le i \le n$, and for every $i \le n$ the numerator $A_i$ and denominator $B_i$ of the
$i$th convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ are
$A_i = \varepsilon_i u_i$ and $B_i = \varepsilon_i v_i$, where $\varepsilon_i = 1$ if
$i \equiv 0, 1 \pmod 4$ and $\varepsilon_i = -1$ if $i \equiv 2, 3 \pmod 4$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Corollary 3.

Stated but not proved: `MetaMathlibExt.polyContFract_of_farey_path_det_one` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-of-farey-path-det-one).

## Farey paths of polynomials with all determinants −1

Let $F$ be a field, let
$n \in \mathbb{N}$, and let $u_i, v_i \in F[X]$ for $i \ge 0$. Suppose that $v_0 = 1$ and that
for $1 \le i \le n$ we have $\deg v_{i-1} < \deg v_i$ and $u_i v_{i-1} - u_{i-1} v_i = -1$. Let
$a_0, a_1, \ldots \in F[X]$ satisfy $a_0 = u_0$, $a_1 = -v_1$ and
$a_i = (-1)^{i+1} (u_i v_{i-2} - u_{i-2} v_i)$ for $2 \le i \le n$. Then $a_i$ is nonconstant
for $1 \le i \le n$, and for every $i \le n$ the numerator $A_i$ and denominator $B_i$ of the
$i$th convergent of the continued fraction $[a_0; a_1, \ldots, a_n]$ over $F(X)$ are
$A_i = \varepsilon_i u_i$ and $B_i = \varepsilon_i v_i$, where $\varepsilon_i = 1$ if
$i \equiv 0, 3 \pmod 4$ and $\varepsilon_i = -1$ if $i \equiv 1, 2 \pmod 4$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Corollary 4.

Stated but not proved: `MetaMathlibExt.polyContFract_of_farey_path_det_neg_one` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-cont-fract-of-farey-path-det-neg-on-3).

## Farey series over a field

Let $F$ be a field and $n$ a natural number. The Farey series
$\mathcal{F}_n$ of order $n$ over $F$ is the set of pairs $(u, v)$ of polynomials in $F[x]$, read
as the fraction $u / v$, such that $\deg u < \deg v \le n$, $u$ and $v$ are coprime, and $v$ is
monic. Here $\deg 0 = -\infty$, so $u = 0$ is allowed.

Each fraction is thus represented by exactly one such pair.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 1 (quoted from [6], there over `𝔽_{p^r}`).

Formalized by `MetaMathlibExt.polyFareySeries`, a definition declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-farey-series).

## The fraction of a pair of polynomials

Let $F$ be a field. The value of a pair $(u, v)$ of
polynomials in $F[x]$ is the rational function $u / v$ in the field $F(x)$ of rational functions
over $F$ (it is $0$ when $v = 0$).

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 1.

Formalized by `MetaMathlibExt.polyFrac`, a definition declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-frac).

## The fraction $0/1$ lies in every Farey series

For every field $F$ and every natural number
$n$, the pair $(0, 1)$, that is the fraction $0 / 1$, belongs to the Farey series $\mathcal{F}_n$
of order $n$ over $F$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 1.

Formalized by `MetaMathlibExt.zero_one_mem_polyFareySeries`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#zero-one-mem-poly-farey-series).

## The fraction 1/X in the polynomial Farey series

Let $F$ be a field. For every natural
number $n \ge 1$, the pair $(1, X)$, that is, the fraction $1/X$, belongs to the Farey series
$\mathcal F_n$ of order $n$ over $F$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 1.

Formalized by `MetaMathlibExt.one_X_mem_polyFareySeries`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#one-x-mem-poly-farey-series).

## Degree neighbours in the polynomial Farey series

Let $F$ be a field, let $n \in \mathbb N$,
and let $\mathcal F_n$ be the Farey series of order $n$ over $F$. For pairs $(u, v)$ and $(h, k)$
of polynomials over $F$, read as the fractions $u/v$ and $h/k$, the fraction $h/k$ is a
$(\deg k)$-neighbour of $u/v$ in $\mathcal F_n$ when both fractions lie in $\mathcal F_n$,
$h/k \ne u/v$ as rational functions, and $|u/v - h/k| \le |u/v - h'/k'|$ for every
$h'/k' \in \mathcal F_n$ with $\deg k' = \deg k$ and $h'/k' \ne u/v$. Here $|\cdot|$ is the
valuation of $F(X)$ at infinity, which orders nonzero rational functions $f/g$ by
$\deg f - \deg g$ and puts $0$ below every nonzero value.

The fraction $u/v$ itself is excluded from the comparison, as the paper's counts (Theorem 3 with
$t = 0$, Figure 1) require.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 2 (quoted from [6]).

Formalized by `MetaMathlibExt.IsPolyFareyDegNeighbor`, a definition declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#is-poly-farey-deg-neighbor).

## No fraction is its own degree neighbour

Let $F$ be a field and let $n \in \mathbb N$. For
every pair $(u, v)$ of polynomials over $F$, the fraction $u/v$ is not a $(\deg v)$-neighbour of
itself in the Farey series $\mathcal F_n$ of order $n$ over $F$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 2.

Formalized by `MetaMathlibExt.not_isPolyFareyDegNeighbor_self`, a theorem declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#not-is-poly-farey-deg-neighbor-self).

## Neighbouring fractions in the polynomial Farey series

Let $F$ be a field and let
$n \in \mathbb N$. Two pairs $(u, v)$ and $(h, k)$ of polynomials over $F$, read as the fractions
$u/v$ and $h/k$, are neighbours in the Farey series $\mathcal F_n$ of order $n$ over $F$ when
$u/v$ is a $(\deg v)$-neighbour of $h/k$ in $\mathcal F_n$ and $h/k$ is a $(\deg k)$-neighbour of
$u/v$ in $\mathcal F_n$. In particular, both fractions then lie in $\mathcal F_n$.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Definition 3 (quoted from [6]).

Formalized by `MetaMathlibExt.ArePolyFareyNeighbors`, a definition declared in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#are-poly-farey-neighbors).

## Neighbour criterion for the polynomial Farey series

Let $F$ be a field, let
$n \in \mathbb N$, and let $(u, v)$ and $(h, k)$ be elements of the Farey series $\mathcal F_n$ of
order $n$ over $F$, read as the fractions $u/v$ and $h/k$. Then $u/v$ and $h/k$ are neighbours in
$\mathcal F_n$ if and only if the polynomial $uk - hv$ has degree $0$, that is, $uk - hv$ is a
nonzero constant.

The paper, quoting [6], works over $\mathbb F_{p^r}$; here the field $F$ is arbitrary.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Theorem 2.

Stated but not proved: `MetaMathlibExt.arePolyFareyNeighbors_iff` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#are-poly-farey-neighbors-iff).

## Number of neighbours of a polynomial Farey fraction

Let $p$ be a prime, let
$n \in \mathbb{N}$, and let $u / v$ be a fraction of the Farey series $\mathcal{F}_n$ over
$\mathbb{F}_p$ with $q = \deg v \ge 1$. Then for every $t \in \mathbb{N}$ with $q + t \le n$,
exactly $(p - 1) p^t$ fractions $h / k \in \mathcal{F}_n$ with $\deg k = q + t$ are neighbours
of $u / v$ in $\mathcal{F}_n$, and exactly one fraction $h / k \in \mathcal{F}_n$ with
$\deg k < q$ is a neighbour of $u / v$ in $\mathcal{F}_n$.

Compared with the paper, $t$ is restricted to $q + t \le n$ (there are no fractions of larger
degree in $\mathcal{F}_n$), the hypothesis $q \ge 1$ is added (for $0 / 1$ there is no neighbour
of degree less than $0$), and the field is the prime field $\mathbb{F}_p$, the case of the
paper's count $(p - 1) p^t$ and of its Example 2.

## Sources

- Tuangrat Chaichana, Arlisa Janjing and Teeraphong Phongpattanacharoen, *An Interpretation of Continued Fractions and Farey Graphs in the Field of Rational Functions*, INTEGERS 26 (2026), Article A3, Theorem 3.

Stated but not proved: `MetaMathlibExt.polyFarey_neighbor_count` is written with `theorem_wanted` in [WantedExt/Algebra/RationalFunctionFareyPathWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/RationalFunctionFareyPathWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html#poly-farey-neighbor-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial continued fractions and Farey paths](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/polynomial-continued-fractions-and-farey-paths)
