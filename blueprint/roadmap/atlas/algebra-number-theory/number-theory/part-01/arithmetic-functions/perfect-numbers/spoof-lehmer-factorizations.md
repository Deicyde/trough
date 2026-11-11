---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSpoofFactorization, MetaMathlibExt.spoofEval, MetaMathlibExt.spoofTotient, MetaMathlibExt.spoofEval_spoofTotient_three_three, MetaMathlibExt.IsSpoofLehmer, MetaMathlibExt.isSpoofLehmer_three_three, MetaMathlibExt.isSpoofLehmer_one_one, MetaMathlibExt.IsTrivialSpoof
statement: formalized
---

# Spoof Lehmer factorizations

38 results, 21 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html).

## Spoof factorizations

A finite multiset $F = \{(x_1, a_1), \dots, (x_r, a_r)\}$ of pairs of
natural numbers, read as the formal product $x_1^{a_1} \cdots x_r^{a_r}$, is a spoof factorization
if every base $x_i$ and every exponent $a_i$ is positive.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 1.

Formalized by `MetaMathlibExt.IsSpoofFactorization`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-spoof-factorization).

## Spoof evaluation

Let $F = x_1^{a_1} \cdots x_r^{a_r}$ be a finite multiset of pairs
$(x_i, a_i)$ of natural numbers, each a base $x_i$ with an exponent $a_i$. The spoof evaluation of
$F$ is the integer $\tilde e(F) = x_1^{a_1} \cdots x_r^{a_r} = \prod_{i=1}^{r} x_i^{a_i}$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 2.

Formalized by `MetaMathlibExt.spoofEval`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-eval).

## Spoof totient

Let $F$ be a finite multiset of pairs $(x_i, a_i)$ of natural numbers,
$i = 1, \dots, r$, viewed as the formal product $x_1^{a_1} \cdots x_r^{a_r}$. The spoof totient
of $F$ is the integer $\tilde\varphi(F) = \prod_{i=1}^{r} (x_i^{a_i} - x_i^{a_i - 1})$, where
the exponent $a_i - 1$ is truncated at $0$, so a pair with $a_i = 0$ contributes the factor $0$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 3.

Formalized by `MetaMathlibExt.spoofTotient`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-totient).

## Spoof evaluation and spoof totient of $3 \cdot 3$

Let $3 \cdot 3$ denote the spoof
factorization $3^1 \cdot 3^1$, with two factors of base $3$ and exponent $1$. Its spoof evaluation
is $\tilde e(3 \cdot 3) = 9$ and its spoof totient is $\tilde\varphi(3 \cdot 3) = 4$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definitions 2 and 3.

Formalized by `MetaMathlibExt.spoofEval_spoofTotient_three_three`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-eval-spoof-totient-three-three).

## Spoof Lehmer factorizations

Let $k$ be an integer and $F$ a finite multiset of pairs
$(x, a)$ of natural numbers. Write $\tilde e(F) = \prod x^a$ for the spoof evaluation and
$\tilde\varphi(F) = \prod (x^a - x^{a-1})$ for the spoof totient of $F$, the products running
over the pairs of $F$ with multiplicity. Then $F$ is a (spoof) $k$-Lehmer factorization if $F$ is
a spoof factorization (every base and exponent is positive), $k \cdot \tilde\varphi(F) =
\tilde e(F) - 1$, and $F$ has at least two factors counted with multiplicity or some factor
whose exponent is greater than $1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 4.

Formalized by `MetaMathlibExt.IsSpoofLehmer`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-spoof-lehmer).

## $3 \cdot 3$ is a $2$-Lehmer factorization

The spoof factorization $3^1 \cdot 3^1$ is a
$2$-Lehmer factorization; indeed $2 \cdot (3 - 1)(3 - 1) = 3 \cdot 3 - 1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Table 1.

Formalized by `MetaMathlibExt.isSpoofLehmer_three_three`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-spoof-lehmer-three-three).

## The factorizations $1^a \cdot 1^b$ are Lehmer for every $k$

For all positive integers
$a$ and $b$ and every integer $k$, the spoof factorization $1^a \cdot 1^b$ is a $k$-Lehmer
factorization.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Example 1.

Formalized by `MetaMathlibExt.isSpoofLehmer_one_one`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-spoof-lehmer-one-one).

## Trivial spoof factorizations

A finite multiset $F$ of pairs $(x, a)$ of natural numbers,
read as a spoof factorization with bases $x$ and exponents $a$, is trivial if every base $x$
occurring in $F$ equals $1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 6.

Formalized by `MetaMathlibExt.IsTrivialSpoof`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-trivial-spoof).

## Odd spoof factorizations

A finite multiset $F$ of pairs $(x, a)$ of natural numbers, read
as a spoof factorization with bases $x$ and exponents $a$, is odd if every base $x$ occurring in
$F$ is odd.

A spoof factorization that is not odd is called even.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 7.

Formalized by `MetaMathlibExt.IsOddSpoof`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-odd-spoof).

## Factorization with all exponents one

For a finite multiset $x$ of natural numbers
$x_1, \dots, x_r$, this is the formal product $x_1 \cdots x_r = x_1^1 \cdots x_r^1$, that is,
the multiset of pairs $(x_1, 1), \dots, (x_r, 1)$, each consisting of a base $x_i$ and the
exponent $1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Remark 3.

Formalized by `MetaMathlibExt.spoofOfBases`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-of-bases).

## The exponent-one factorization on the bases 3 and 3

The factorization with all exponents
one on the multiset of bases consisting of two copies of $3$ is the multiset consisting of two
copies of the pair $(3, 1)$, that is, $3 \cdot 3 = 3^1 \cdot 3^1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Remark 3.

Formalized by `MetaMathlibExt.spoofOfBases_three_three`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-of-bases-three-three).

## Solutions of the Lehmer equation

A finite multiset $x$ of natural numbers solves
Equation (1) if every element $x_j$ of $x$ satisfies $x_j \ge 2$ and there is a positive integer
$k$ with $k \prod_j (x_j - 1) = \prod_j x_j - 1$, where the products run over the elements of $x$
with multiplicity and are computed in $\mathbb{Z}$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Equation (1).

Formalized by `MetaMathlibExt.IsLehmerEquationSolution`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-lehmer-equation-solution).

## The multiset $\{3, 3\}$ solves the Lehmer equation

Every element of the multiset
$\{3, 3\}$ is at least $2$, and there is a positive integer $k$ with
$k \cdot (3 - 1)(3 - 1) = 3 \cdot 3 - 1$ (namely $k = 2$). So $\{3, 3\}$ solves Equation (1), the
equation $k \prod_j (x_j - 1) = \prod_j x_j - 1$ in the elements $x_j$ of a multiset, counted
with multiplicity.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Table 1.

Formalized by `MetaMathlibExt.isLehmerEquationSolution_three_three`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-lehmer-equation-solution-three-three).

## The Lehmer function $\kappa_r$

For a list $t = (t_1, \dots, t_r)$ of real numbers,

$$\kappa_r(t_1, \dots, t_r) = \frac{t_1 \cdots t_r - 1}{(t_1 - 1) \cdots (t_r - 1)},$$

with division by zero giving $0$ (so $\kappa_r(t) = 0$ when some $t_i = 1$).

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 8.

Formalized by `MetaMathlibExt.lehmerKappa`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-kappa).

## The Lehmer function at $(2, 2)$

The Lehmer function
$\kappa_2(t_1, t_2) = (t_1 t_2 - 1) / ((t_1 - 1)(t_2 - 1))$ takes the value $\kappa_2(2, 2) = 3$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 8 and proof of Theorem 5.

Formalized by `MetaMathlibExt.lehmerKappa_two_two`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-kappa-two-two).

## Admissible completions for the Lehmer bounds

Let $t = (t_1, \dots, t_s)$ be a list of
real numbers and let $r$ be a natural number. The admissible completions of $t$ to length $r$
are the lists $u = (u_1, \dots, u_m)$ of real numbers with $s + m = r$ such that
$t_1, \dots, t_s, u_1, \dots, u_m$ is nondecreasing and $u_j \ge 2$ for every $j$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 9.

Formalized by `MetaMathlibExt.lehmerCompletions`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-completions).

## The lower Lehmer bound

Let $t = (t_1, \dots, t_s)$ be a list of real numbers and let $r$
be a natural number. An admissible completion of $t$ to length $r$ is a list
$u = (u_1, \dots, u_m)$ of real numbers with $s + m = r$ such that
$t_1, \dots, t_s, u_1, \dots, u_m$ is nondecreasing and $u_j \ge 2$ for every $j$. The lower
Lehmer bound $L(t; r)$ is the infimum of $\kappa_r(t_1, \dots, t_s, u_1, \dots, u_m)$ over all
admissible completions $u$ of $t$ to length $r$, where $\kappa_r$ is the Lehmer function. The
infimum is taken to be $0$ when there is no admissible completion or the values are unbounded
below.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 9.

Formalized by `MetaMathlibExt.lehmerLower`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-lower).

## Upper Lehmer bound $U(t; r)$

For real numbers $y_1, \dots, y_r$ let
$\kappa_r(y_1, \dots, y_r) = (y_1 \cdots y_r - 1) / ((y_1 - 1) \cdots (y_r - 1))$, where division
by $0$ gives $0$. For a list $t = (t_1, \dots, t_s)$ of real numbers and a natural number $r$, an
admissible completion of $t$ is a list $u = (u_{s+1}, \dots, u_r)$ of $r - s$ real numbers (there
is none if $s > r$) such that $t_1, \dots, t_s, u_{s+1}, \dots, u_r$ is nondecreasing and
$u_j \ge 2$ for every $j$. Then $U(t; r)$ is the supremum in $\mathbb{R}$ of
$\kappa_r(t_1, \dots, t_s, u_{s+1}, \dots, u_r)$ over all admissible completions $u$ of $t$; by
convention it is $0$ when $t$ has no admissible completion or these values are not bounded above.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 9.

Formalized by `MetaMathlibExt.lehmerUpper`, a definition declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-upper).

## A full-length nondecreasing list has only the empty completion

Let
$t = (t_1, \dots, t_r)$ be a nondecreasing list of $r$ real numbers. Then the empty list is the
only admissible completion of $t$ to length $r$, that is, the only list $u$ of real numbers such
that $r + |u| = r$, the concatenation of $t$ and $u$ is nondecreasing, and every entry of $u$ is
at least $2$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 9.

Formalized by `MetaMathlibExt.lehmerCompletions_length`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-completions-length).

## The Lehmer bounds of a full-length list

Let $L(t; r)$ and $U(t; r)$ be the lower and
upper Lehmer bounds and $\kappa_r$ the Lehmer function. For every nondecreasing list
$t = (t_1, \dots, t_r)$ of real numbers, $L(t; r) = U(t; r) = \kappa_r(t_1, \dots, t_r)$.

The only admissible completion of such a list to its own length $r$ is the empty list.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Definition 9 and proof of Lemma 3.

Formalized by `MetaMathlibExt.lehmerLower_upper_length`, a theorem declared in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-lower-upper-length).

## Spoof Lehmer factorizations with a base $1$ are trivial

If a finite multiset $F$ of pairs
$(x, a)$ of natural numbers is a $k$-Lehmer factorization for some integer $k$, and some pair in
$F$ has base $x = 1$, then every base of $F$ equals $1$, that is, $F$ is trivial.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Proposition 1.

Stated but not proved: `MetaMathlibExt.isTrivialSpoof_of_isSpoofLehmer_of_one_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#is-trivial-spoof-of-is-spoof-lehmer-of-o).

## Nontrivial spoof Lehmer factorizations have all exponents $1$

If $F$ is a nontrivial spoof
$k$-Lehmer factorization for some integer $k$, then every exponent of $F$ is $1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 3.

Stated but not proved: `MetaMathlibExt.spoofLehmer_exponents_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-exponents-eq-one).

## Bases of a spoof Lehmer factorization modulo divisors of its evaluation

Let
$x_1, \dots, x_r$ be natural numbers and let $F = x_1 \cdots x_r$ be the spoof factorization with
these bases, all with exponent $1$. Suppose $F$ is a nontrivial spoof $k$-Lehmer factorization for
some integer $k$. If $n$ is an integer with $n \ne \pm 1$ that divides the spoof evaluation
$\tilde e(F)$, then $x_i \not\equiv 1 \pmod n$ for every $i$.

The source states this for every integer $n$ dividing $\tilde e(F)$, but the hypothesis
$n \ne \pm 1$ cannot be dropped: $3 \cdot 3$ is a nontrivial spoof $2$-Lehmer factorization
($2 \cdot 4 = 9 - 1$), $1$ divides $\tilde e(3 \cdot 3) = 9$, and $3 \equiv 1 \pmod 1$. The source's
proof reaches $0 \equiv -1 \pmod n$, which is a contradiction only when $n \nmid 1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 4.

Stated but not proved: `MetaMathlibExt.spoofLehmer_base_not_modEq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-base-not-mod-eq-one).

## Bases of a nontrivial spoof Lehmer factorization are not $1$ modulo one another

Let
$x_1, \dots, x_r$ be natural numbers and let $F = x_1 \cdots x_r$ be the spoof factorization with
these bases, all with exponent $1$. If $F$ is a nontrivial spoof $k$-Lehmer factorization for some
integer $k$, then $x_i \not\equiv 1 \pmod{x_j}$ for all $i$ and $j$, including $i = j$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Corollary 1.

Stated but not proved: `MetaMathlibExt.spoofLehmer_base_not_modEq_one_base` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-base-not-mod-eq-one-base).

## Primes dividing the evaluation of a spoof Lehmer factorization

Let $x_1, \dots, x_r$ be
natural numbers and let $F = x_1 \cdots x_r$ be the spoof factorization with these bases, all with
exponent $1$. Suppose $F$ is a nontrivial spoof $k$-Lehmer factorization for some integer $k$. If
$p$ is a prime dividing the spoof evaluation $\tilde e(F)$, then $x_i \not\equiv 1 \pmod p$ for
every $i$. Moreover, if $F$ is even (not every base is odd), then every base $x_i$ is even.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Corollary 2.

Stated but not proved: `MetaMathlibExt.spoofLehmer_base_not_modEq_one_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-base-not-mod-eq-one-prime).

## Bounds and monotonicity of the Lehmer function

For real numbers $t_1, \dots, t_r$ let
$\kappa_r(t_1, \dots, t_r) = (t_1 \cdots t_r - 1) / ((t_1 - 1) \cdots (t_r - 1))$. Let $r \ge 2$
and let $t_1, \dots, t_r \ge 2$ be real numbers. Then
$1 < \kappa_r(t_1, \dots, t_r) \le 2^r - 1$. Moreover, for every index $j$ and every real
$y > t_j$, replacing $t_j$ by $y$ strictly decreases $\kappa_r$, that is,
$\kappa_r(t_1, \dots, t_{j-1}, y, t_{j+1}, \dots, t_r) < \kappa_r(t_1, \dots, t_r)$.

The hypothesis $r \ge 2$ is needed: $\kappa_1(t) = 1$ for every $t \ge 2$, so for $r = 1$ the
lower bound fails and $\kappa_1$ is not strictly decreasing.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 5.

Stated but not proved: `MetaMathlibExt.lehmerKappa_antitone_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-kappa-antitone-bounds).

## Formulas for the Lehmer bounds

Let $L(t; r)$ and $U(t; r)$ be the lower and upper
Lehmer bounds of a list $t$ of real numbers, and write $\emptyset$ for the empty list. Then
$L(\emptyset; r) = 1$ for every $r \ge 1$, and $U(\emptyset; r) = 2^r - 1$ for every natural
number $r$. Let $t = (t_1, \dots, t_s)$ with $s \ge 1$ and $2 \le t_1 \le \dots \le t_s$, and
let $r \ge s$ be a natural number. Then

$$U(t; r) = \frac{t_1 \cdots t_{s-1} t_s^{r-s+1} - 1}
{(t_1 - 1) \cdots (t_{s-1} - 1)(t_s - 1)^{r-s+1}},$$

and if moreover $r > s$, then

$$L(t; r) = \frac{t_1 \cdots t_s}{(t_1 - 1) \cdots (t_s - 1)}.$$

The condition $r > s$ for $L$ is needed: for $s = r$ the only admissible completion of $t$ is the
empty list, so $L(t; r) = \kappa_r(t)$, where $\kappa_r$ is the Lehmer function; for $t = (2)$
and $r = 1$ this is $\kappa_1(2) = 1$, while the formula gives $2$. Likewise
$L(\emptyset; 0) = \kappa_0 = 0$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Lemma 1.

Stated but not proved: `MetaMathlibExt.lehmerLower_upper_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-lower-upper-formula).

## Monotonicity of the Lehmer bounds

Let $L(t; r)$ and $U(t; r)$ be the lower and upper
Lehmer bounds: the infimum and the supremum of $\kappa_r(t_1, \dots, t_s, u_1, \dots, u_{r-s})$
over the admissible completions $u$ of $t = (t_1, \dots, t_s)$, where $\kappa_r$ is the Lehmer
function. Let $r$ be a natural number and let $t = (t_1, \dots, t_s)$ and
$t' = (t'_1, \dots, t'_s)$ be nondecreasing lists of real numbers of the same length $s \le r$
with $t_i \ge 2$ and $t_i \le t'_i$ for every $i$. Then $L(t'; r) \le L(t; r)$ and
$U(t'; r) \le U(t; r)$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Lemma 2.

Stated but not proved: `MetaMathlibExt.lehmerLower_upper_antitone` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-lower-upper-antitone).

## Lehmer bounds at the initial segments of a spoof Lehmer factorization

Let
$x_1 \le \dots \le x_r$ be natural numbers and let $F = x_1 \cdots x_r$ be the spoof factorization
with these bases, all with exponent $1$. Suppose $F$ is a nontrivial spoof $k$-Lehmer factorization
for an integer $k$. For a list $t = (t_1, \dots, t_s)$ of real numbers, let $L(t; r)$ and $U(t; r)$
be the lower and upper Lehmer bounds: the infimum and the supremum in $\mathbb{R}$ of
$\kappa_r(t_1, \dots, t_s, u_{s+1}, \dots, u_r)$ over all real numbers $u_{s+1}, \dots, u_r \ge 2$
such that $t_1, \dots, t_s, u_{s+1}, \dots, u_r$ is nondecreasing, where
$\kappa_r(y_1, \dots, y_r) = (y_1 \cdots y_r - 1) / ((y_1 - 1) \cdots (y_r - 1))$. Then for every
$s$ with $0 \le s \le r$ we have $L(x_1, \dots, x_s; r) \le k \le U(x_1, \dots, x_s; r)$, and
$L(x_1, \dots, x_s; r) = k$ if and only if $s = r$. Moreover $1 < k \le 2^r - 1$.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Lemma 3.

Stated but not proved: `MetaMathlibExt.spoofLehmer_lower_le_le_upper` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-lower-le-le-upper).

## Finitely many solutions of the Lehmer equation in $r$ variables

For every natural
number $r \ge 2$, there are only finitely many pairs $(k, x)$ of an integer $k > 0$ and a tuple
$x = (x_1, \dots, x_r)$ of natural numbers with $x_i \ge 2$ for every $i$ such that
$k (x_1 - 1) \cdots (x_r - 1) = x_1 \cdots x_r - 1$.

The source also claims that the solutions can be computed explicitly; that claim is not part of
this statement.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 1.

Stated but not proved: `MetaMathlibExt.lehmerEquation_solutions_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-equation-solutions-finite).

## Solutions of the Lehmer equation with at most six variables

Call a finite multiset
$\{x_1, \dots, x_r\}$ of natural numbers a solution of the Lehmer equation if $x_i \ge 2$ for
every $i$ and $k (x_1 - 1) \cdots (x_r - 1) = x_1 \cdots x_r - 1$ for some integer $k > 0$.
There are exactly $76$ solutions with $2 \le r \le 6$ (counted over all such $r$ together).
Exactly $31$ of them have every $x_i$ odd, and exactly $45$ have every $x_i$ even.

Solutions are counted as multisets, that is, up to the order of the $x_i$, as in Tables 1 and 2.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 2.

Stated but not proved: `MetaMathlibExt.lehmerEquation_solutions_count` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#lehmer-equation-solutions-count).

## Finitely many nontrivial spoof Lehmer factorizations with $r$ factors

For every natural
number $r$, there are only finitely many finite multisets $F$ of pairs (base, exponent) of natural
numbers with exactly $r$ elements such that $F$ is a nontrivial spoof $k$-Lehmer factorization for
some integer $k$.

The source also asserts that these factorizations can be computed explicitly and verifiably; that
claim is not part of this statement.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 6.

Stated but not proved: `MetaMathlibExt.spoofLehmer_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-finite).

## Spoof Lehmer factorizations with at most six factors

Let $F$ be a finite multiset of pairs
(base, exponent) of natural numbers with at most $6$ elements. Then $F$ is a nontrivial odd spoof
$k$-Lehmer factorization for some integer $k$ if and only if every exponent of $F$ is $1$ and the
multiset of bases of $F$ is one of the following $31$, written as tuples: $(3, 3)$, $(3, 5, 15)$,
$(3, 5, 17, 255)$, $(3, 3, 3, 3)$, $(3, 5, 17, 257, 65535)$, $(3, 5, 17, 285, 2507)$,
$(5, 5, 5, 43, 5375)$, $(5, 5, 9, 9, 89)$, $(3, 5, 17, 257, 65537, 4294967295)$,
$(3, 5, 17, 257, 65555, 226112997)$, $(3, 5, 17, 257, 65717, 23794275)$,
$(3, 5, 17, 257, 68975, 1314417)$, $(3, 5, 17, 353, 929, 83623935)$, $(3, 5, 17, 377, 1217, 2295)$,
$(3, 5, 17, 395, 1059, 2303)$, $(3, 5, 33, 53, 69, 8343)$, $(3, 9, 9, 23, 131, 732159)$,
$(5, 5, 5, 43, 5377, 28901375)$, $(5, 5, 5, 43, 5387, 2632285)$, $(5, 5, 5, 43, 5407, 937505)$,
$(5, 5, 5, 43, 5477, 291475)$, $(5, 5, 5, 43, 5717, 90115)$, $(5, 5, 5, 43, 6215, 39817)$,
$(5, 5, 5, 43, 6487, 31385)$, $(5, 5, 5, 43, 8507, 14605)$, $(5, 5, 5, 45, 807, 267023)$,
$(5, 5, 5, 47, 453, 2661375)$, $(5, 5, 5, 47, 457, 50659)$, $(5, 5, 5, 65, 129, 2325)$,
$(5, 7, 7, 7, 133, 228095)$ and $(3, 3, 5, 5, 9, 89)$. Also, $F$ is a nontrivial spoof $k$-Lehmer
factorization for some integer $k$ and $F$ is even (some base is even) if and only if every exponent
of $F$ is $1$ and the multiset of bases of $F$ is one of the following $45$, written as tuples:
$(2, 2)$, $(2, 4, 8)$, $(2, 2, 4)$, $(2, 2, 2)$, $(2, 4, 10, 80)$, $(2, 2, 6, 24)$, $(2, 2, 4, 4)$,
$(2, 2, 2, 8)$, $(2, 2, 2, 2)$, $(2, 4, 10, 82, 6560)$, $(2, 4, 10, 92, 670)$,
$(2, 4, 10, 100, 422)$, $(2, 4, 10, 112, 290)$, $(2, 2, 6, 26, 624)$, $(2, 2, 8, 12, 384)$,
$(2, 2, 2, 10, 80)$, $(2, 2, 2, 4, 32)$, $(2, 2, 2, 2, 16)$, $(2, 2, 2, 2, 6)$, $(2, 2, 2, 2, 4)$,
$(2, 2, 2, 2, 2)$, $(2, 4, 10, 82, 6562, 43046720)$, $(2, 4, 10, 82, 12440, 13882)$,
$(2, 4, 10, 88, 1120, 9944)$, $(2, 4, 26, 26, 26, 8272)$, $(2, 8, 8, 8, 206, 210944)$,
$(2, 2, 6, 26, 626, 390624)$, $(2, 2, 6, 42, 62, 2156)$, $(2, 2, 8, 12, 386, 148224)$,
$(2, 2, 8, 12, 404, 8166)$, $(2, 2, 8, 12, 416, 5154)$, $(2, 2, 8, 12, 636, 974)$,
$(2, 2, 12, 14, 18, 206)$, $(2, 2, 2, 10, 82, 6560)$, $(2, 2, 2, 10, 92, 670)$,
$(2, 2, 2, 10, 100, 422)$, $(2, 2, 2, 10, 112, 290)$, $(2, 2, 2, 4, 34, 1088)$,
$(2, 2, 2, 4, 38, 244)$, $(2, 2, 2, 6, 8, 384)$, $(2, 2, 2, 4, 8, 16)$, $(2, 2, 2, 2, 18, 288)$,
$(2, 2, 2, 2, 6, 6)$, $(2, 2, 2, 2, 2, 32)$ and $(2, 2, 2, 2, 2, 2)$.

The source further attributes $11$ of the odd and $27$ of the even factorizations to the families of
its Examples 2–5, leaving $20$ and $18$ sporadic ones; that attribution is not part of this
statement.

## Sources

- Grant Molnar and Guntas Singh, *Spoof Lehmer Factorizations*, INTEGERS 26 (2026), Article A33, Theorem 7.

Stated but not proved: `MetaMathlibExt.spoofLehmer_atMostSix_tables` is written with `theorem_wanted` in [WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SpoofLehmerFactorizationWanted.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-lehmer-at-most-six-tables).

## Spoof totient of a unitary factorization

For natural numbers $x_1, \dots, x_r$, the spoof
totient of the spoof factorization $x_1 \cdots x_r$ with every exponent $1$ is
$\prod_{i=1}^{r} (x_i - 1)$, computed in the integers. This is Hasanalizade's spoof unitary
totient $\tilde{\varphi}^*(x_1 \cdots x_r)$.

## Sources

- Elchin Hasanalizade, *Some Remarks on a Paper of Molnar and Singh*, INTEGERS 26 (2026), Article A100, Section 1 (definition of `φ̃*`).

Formalized by `MetaMathlibExt.spoofTotient_spoofOfBases`, a theorem declared in [WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-totient-spoof-of-bases).

## Nielsen's bound

Let $r$, $a$ and $b$ be natural numbers and let $x_1 \le \dots \le x_r$ be
integers with every $x_j > 1$. If
$\prod_{j=1}^{r} (1 - 1/x_j) \le a/b < \prod_{j=1}^{r-1} (1 - 1/x_j)$, then
$a \prod_{j=1}^{r} x_j \le (a + 1)^{2^r} - (a + 1)^{2^{r-1}}$.

The paper assumes $r$, $a$ and $b$ positive; this follows from the hypotheses, since the left-hand
product is positive (so $a > 0$ and $b > 0$, reading $a/0$ as $0$) and both products equal $1$
when $r = 0$.

## Sources

- Elchin Hasanalizade, *Some Remarks on a Paper of Molnar and Singh*, INTEGERS 26 (2026), Article A100, Lemma 1, citing P. Nielsen, Math. Comp. 84 (2015), Lemma 1.4.

Stated but not proved: `MetaMathlibExt.nielsen_prod_one_sub_inv_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#nielsen-prod-one-sub-inv-bound).

## Bound on unitary Lehmer factorizations

Let $k$ be an integer and let $x_1, \dots, x_r$ be
natural numbers. If the spoof factorization $x_1 \cdots x_r$ with every exponent $1$ is a spoof
$k$-Lehmer factorization (a unitary $k$-Lehmer factorization), then its spoof evaluation
$\tilde{e}(x_1 \cdots x_r) = \prod_{i=1}^{r} x_i$ is at most $2^{2^r} - 2^{2^{r-1}}$.

The paper takes $k > 0$; here $k$ is any integer. For $k \le 0$ the hypothesis forces the spoof
evaluation to be $1$.

## Sources

- Elchin Hasanalizade, *Some Remarks on a Paper of Molnar and Singh*, INTEGERS 26 (2026), Article A100, Theorem 1.

Stated but not proved: `MetaMathlibExt.spoofEval_le_of_isSpoofLehmer_spoofOfBases` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#spoof-eval-le-of-is-spoof-lehmer-spoof-o).

## Repeated unitary Lehmer factorizations

Let $k$ be an integer and let $x \ge 2$ and $s$ be
natural numbers. If the spoof factorization $x \cdots x$ with $s$ factors, each with base $x$ and
exponent $1$, is a spoof $k$-Lehmer factorization (a unitary $k$-Lehmer factorization), then
either $x = 2$ and $s \ge 2$, or $x = 3$ and $s \in \{2, 4\}$.

The paper assumes $k \ge 2$ instead of $x \ge 2$; as printed the statement fails for $x = 1$:
for every $s \ge 2$ the factorization $1 \cdots 1$ with $s$ factors has spoof totient $0$ and
spoof evaluation $1$, so it is a spoof $k$-Lehmer factorization for every $k$. The paper's proof
treats only $x = 2$, $x = 3$ and $x \ge 4$. When $x \ge 2$, the hypothesis forces $k \ge 2$.

## Sources

- Elchin Hasanalizade, *Some Remarks on a Paper of Molnar and Singh*, INTEGERS 26 (2026), Article A100, Theorem 2.

Stated but not proved: `MetaMathlibExt.eq_two_or_eq_three_of_isSpoofLehmer_replicate` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#eq-two-or-eq-three-of-is-spoof-lehmer-re).

## Lehmer's lemma for unitary spoof factorizations

Let $F$ be a finite multiset of integers,
write $E = \prod_{f \in F} f$ and $P = \prod_{f \in F} (f - 1)$, and let $k$, $\alpha$, $x$ and $y$
be integers with $\alpha = \pm 1$. If $k P = E + \alpha$ and $k P (x - 1)(y - 1) = E x y - 1$,
then $(\alpha x - E - \alpha)(\alpha y - E - \alpha) - (E^2 + \alpha E - \alpha) = 0$.

The second equation says that $F \cdot x \cdot y$ satisfies the unitary $k$-Lehmer equation
(Equation (3)). The paper takes $F$ with positive entries and $k \ge 2$; the identity holds for
every finite multiset of integers and every integer $k$.

## Sources

- Elchin Hasanalizade, *Some Remarks on a Paper of Molnar and Singh*, INTEGERS 26 (2026), Article A100, Theorem 3.

Stated but not proved: `MetaMathlibExt.unitary_spoof_lehmer_lemma` is written with `theorem_wanted` in [WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/UnitarySpoofLehmerWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html#unitary-spoof-lehmer-lemma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spoof Lehmer factorizations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/spoof-lehmer-factorizations)
