---
declaration: section
origin: cited
lean: MetaMathlibExt.reducedFormsOfDiscriminant, MetaMathlibExt.gaussClassNumber, MetaMathlibExt.unweightedHurwitzClassNumber, MetaMathlibExt.reducedFormWeight, MetaMathlibExt.kroneckerFOdd, MetaMathlibExt.kroneckerFEven, MetaMathlibExt.kroneckerDiscriminant, MetaMathlibExt.kroneckerClassMultiplier
statement: formalized
---

# Kronecker's class number sums

14 results, 11 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html).

## Reduced forms of a given discriminant

For an integer $d$, $R(d)$ is the finite set of
integer triples $(a, b, c)$ such that the binary quadratic form $a x^2 + b x y + c y^2$ is Gauss
reduced (that is, $a > 0$, $b^2 - 4ac < 0$, $|b| \le a \le c$, and $b \ge 0$ whenever $|b| = a$ or
$a = c$) and has discriminant $b^2 - 4ac = d$. In particular $R(d)$ is empty when $d \ge 0$.

The set is computed by a finite search: a reduced form satisfies $-d = 4ac - b^2 \ge 3a^2$, so
$1 \le a \le \lfloor \sqrt{-d} \rfloor$ and $|b| \le a$, and $c = (b^2 - d) / (4a)$ is determined
by $a$ and $b$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Section 1.

Formalized by `MetaMathlibExt.reducedFormsOfDiscriminant`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#reduced-forms-of-discriminant).

## Gauss class number of a discriminant

For an integer $d$, the Gauss class number $h(d)$
is the number of integer triples $(a, b, c)$ with $b^2 - 4ac = d$ for which the binary quadratic
form $ax^2 + bxy + cy^2$ is positive definite ($a > 0$ and $d < 0$), reduced ($|b| \le a \le c$,
with $b \ge 0$ whenever $|b| = a$ or $a = c$) and primitive ($\gcd(a, b, c) = 1$).

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Section 1.

Formalized by `MetaMathlibExt.gaussClassNumber`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#gauss-class-number).

## Unweighted Hurwitz class number

For an integer $d$, the unweighted Hurwitz class number
$H(d)$ is the number of elements of the set $R(d)$ of reduced forms of discriminant $d$, that is,
the number of integer triples $(a, b, c)$, primitive or not, for which $a x^2 + b x y + c y^2$ is
a Gauss-reduced binary quadratic form of discriminant $b^2 - 4ac = d$. Every reduced form is
counted with weight $1$; in particular $H(d) = 0$ when $d \ge 0$.

This differs from the weighted Hurwitz class number, which counts forms equivalent to a multiple
of $x^2 + y^2$ or of $x^2 + x y + y^2$ with weight $1/2$ or $1/3$ (the paper remarks that the
literature uses several conventions).

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, equation (1).

Formalized by `MetaMathlibExt.unweightedHurwitzClassNumber`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#unweighted-hurwitz-class-number).

## Weight of a reduced binary quadratic form

The weight of an integer triple $(a, b, c)$,
standing for the form $ax^2 + bxy + cy^2$, is $1/2$ if $a = c$ and $b = 0$, $1/3$ if
$a = b = c \ne 0$, and $1$ otherwise.

On reduced forms the weight is $1/2$ for $a(x^2 + y^2)$, $1/3$ for $a(x^2 + xy + y^2)$, and $1$
for every other form.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, equation (3).

Formalized by `MetaMathlibExt.reducedFormWeight`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#reduced-form-weight).

## Kronecker's sum $F_o(n)$

For a natural number $n$, $F_o(n)$ is the sum of the weights of
the reduced positive-definite integral binary quadratic forms $ax^2 + bxy + cy^2$ of
discriminant $b^2 - 4ac = -4n$ in which $a$ or $c$ is odd. Here a form is reduced when
$|b| \le a \le c$, with $b \ge 0$ whenever $|b| = a$ or $a = c$, and its weight is $1/2$ if
$a = c$ and $b = 0$, $1/3$ if $a = b = c$, and $1$ otherwise.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, equation (4).

Formalized by `MetaMathlibExt.kroneckerFOdd`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-fodd).

## Kronecker's sum $F_e(n)$

For a natural number $n$, $F_e(n)$ is the sum of the weights of
the reduced positive-definite integral binary quadratic forms $ax^2 + bxy + cy^2$ of
discriminant $b^2 - 4ac = -4n$ in which $a$ and $c$ are both even. Here a form is reduced when
$|b| \le a \le c$, with $b \ge 0$ whenever $|b| = a$ or $a = c$, and its weight is $1/2$ if
$a = c$ and $b = 0$, $1/3$ if $a = b = c$, and $1$ otherwise.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, equation (5).

Formalized by `MetaMathlibExt.kroneckerFEven`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-feven).

## The discriminant $d(\alpha, g)$ attached to $n = 2^\alpha g h^2$

For natural numbers
$\alpha$ and $g$, let $d(\alpha, g) = -8g$ if $\alpha$ is odd; if $\alpha$ is even, let
$d(\alpha, g) = -4g$ when $g \equiv 1 \pmod 4$ and $d(\alpha, g) = -g$ otherwise.

In the paper $n = 2^\alpha g h^2$ with $g$ and $h$ odd and $g$ squarefree, so the last case is
$g \equiv 3 \pmod 4$; the paper writes $d(n)$ for $d(\alpha, g)$, the fundamental discriminant of
$\mathbb{Q}(\sqrt{-n})$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Section 1, after equation (17).

Formalized by `MetaMathlibExt.kroneckerDiscriminant`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-discriminant).

## Kronecker's class-number multiplier

For an integer $d$ and a natural number $h \ge 1$,
$\ell(d, h)$ is the product, over the primes $p$ dividing $h$, of

$$\sum_{i=0}^{v} p^i - \left(\frac{d}{p}\right) \sum_{i=0}^{v-1} p^i,$$

where $v$ is the exponent of $p$ in $h$ and $\left(\frac{d}{p}\right)$ is the Jacobi symbol; in
particular $\ell(d, 1) = 1$. Also $\ell(d, 0) = 1$.

In the paper $h$ is odd, so each $p$ is an odd prime, the symbol is the Legendre symbol, and the
factor equals $\frac{p^{v+1} - 1}{p - 1} - \left(\frac{d}{p}\right) \frac{p^v - 1}{p - 1}$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Section 1, definition of `ℓ(n)`.

Formalized by `MetaMathlibExt.kroneckerClassMultiplier`, a definition declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-class-multiplier).

## Class numbers of the discriminants $-3$, $-4$ and $-12$

The Gauss class numbers satisfy
$h(-3) = h(-4) = h(-12) = 1$, and the unweighted Hurwitz class number satisfies $H(-12) = 2$.

The two reduced forms of discriminant $-12$ are $x^2 + 3y^2$ and the imprimitive form
$2x^2 + 2xy + 2y^2$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Section 1.

Formalized by `MetaMathlibExt.gaussClassNumber_small`, a theorem declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#gauss-class-number-small).

## Kronecker's sums at $n = 1$ and $n = 3$

Kronecker's sums $F_o$ and $F_e$ satisfy
$F_o(1) = 1/2$, $F_e(1) = 0$, $F_o(3) = 1$ and $F_e(3) = 1/3$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, equations (4) and (5).

Formalized by `MetaMathlibExt.kroneckerF_small`, a theorem declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-f-small).

## Small values of the discriminant $d(\alpha, g)$ and the multiplier $\ell(d, h)$

The
discriminant attached to $n = 2^\alpha g h^2$ satisfies $d(0, 1) = -4$, $d(0, 3) = -3$ and
$d(1, 1) = -8$, and Kronecker's class-number multiplier satisfies $\ell(-4, 1) = 1$ and
$\ell(-4, 3) = 5$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Section 1.

Formalized by `MetaMathlibExt.kroneckerDiscriminant_kroneckerClassMultiplier_small`, a theorem declared in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-discriminant-kronecker-class-m).

## Gauss's three-square formula after Aygin and Williams

Let $n$, $\alpha$, $g$, $h$ be
natural numbers with $n = 2^\alpha g h^2$, where $g$ and $h$ are odd and $g$ is squarefree. Let
$d$ be the Kronecker discriminant of $(\alpha, g)$, namely $d = -4g$ if $\alpha$ is even and
$g \equiv 1 \pmod 4$, $d = -g$ if $\alpha$ is even and $g \equiv 3 \pmod 4$, and $d = -8g$ if
$\alpha$ is odd. Put $L = \ell(d, h) \, h(d)$, where $\ell(d, h)$ is the Kronecker class
multiplier and $h(d)$ is the Gauss class number of $d$, and let $r_3(n)$ be the number of ordered
triples $(x, y, z)$ of integers with $x^2 + y^2 + z^2 = n$. Then: if $\alpha$ is even and $g = 1$,
then $r_3(n) = 6L$; if $\alpha$ is even and $g = 3$, then $r_3(n) = 8L$; if $\alpha$ is even,
$g \equiv 1 \pmod 4$ and $g \ne 1$, then $r_3(n) = 12L$; if $\alpha$ is even, $g \equiv 3 \pmod 8$
and $g \ne 3$, then $r_3(n) = 24L$; if $\alpha$ is even and $g \equiv 7 \pmod 8$, then
$r_3(n) = 0$; and if $\alpha$ is odd, then $r_3(n) = 12L$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Theorem 1.

Stated but not proved: `MetaMathlibExt.threeSquareRepresentationCount_eq_kronecker_classNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#three-square-representation-count-eq-kro).

## Aygin–Williams evaluation of Kronecker's sums

Let $n = 2^\alpha g h^2$ with $g$ and $h$
odd natural numbers and $g$ squarefree. Let $d = -4g$ if $\alpha$ is even and
$g \equiv 1 \pmod 4$, $d = -g$ if $\alpha$ is even and $g \equiv 3 \pmod 4$, and $d = -8g$ if
$\alpha$ is odd. Let $L = \ell(d, h) \cdot h(d)$, where $\ell(d, h)$ is Kronecker's class-number
multiplier and $h(d)$ is the Gauss class number of $d$, and for even $\alpha$ let
$t = 2^{\alpha/2}$. Then Kronecker's sums $F_o$ and $F_e$ satisfy:

- if $\alpha$ is even and $g = 1$, then $F_o(n) = \frac{t}{2} L$ and
  $F_e(n) = \left(\frac{t}{2} - \frac{1}{2}\right) L$;
- if $\alpha$ is even and $g = 3$, then $F_o(n) = tL$ and $F_e(n) = \left(t - \frac{2}{3}\right) L$;
- if $\alpha$ is even, $g \equiv 1 \pmod 4$ and $g \ne 1$, then $F_o(n) = tL$ and
  $F_e(n) = (t - 1) L$;
- if $\alpha$ is even, $g \equiv 3 \pmod 8$ and $g \ne 3$, then $F_o(n) = 3tL$ and
  $F_e(n) = (3t - 2) L$;
- if $\alpha$ is even and $g \equiv 7 \pmod 8$, then $F_o(n) = F_e(n) = tL$;
- if $\alpha$ is odd, then $F_o(n) = 2^{(\alpha - 1)/2} L$ and
  $F_e(n) = \left(2^{(\alpha - 1)/2} - 1\right) L$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Theorem 2.

Stated but not proved: `MetaMathlibExt.kroneckerFOdd_kroneckerFEven_eq_classNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#kronecker-fodd-kronecker-feven-eq-class).

## Unweighted Hurwitz class numbers via Gauss class numbers

Let $n$, $\alpha$, $g$, $h$ be
natural numbers with $n = 2^\alpha g h^2$, where $g$ and $h$ are odd and $g$ is squarefree. Let
$d$ be the Kronecker discriminant of $(\alpha, g)$, namely $d = -4g$ if $\alpha$ is even and
$g \equiv 1 \pmod 4$, $d = -g$ if $\alpha$ is even and $g \equiv 3 \pmod 4$, and $d = -8g$ if
$\alpha$ is odd. Put $L = \ell(d, h) \, h(d)$, where $\ell(d, h)$ is the Kronecker class
multiplier and $h(d)$ is the Gauss class number of $d$, and let $H(-4n)$ be the unweighted
Hurwitz class number of $-4n$. Then, with $\alpha / 2$ and $(\alpha + 1) / 2$ exact quotients in
the cases where they occur: if $\alpha$ is even and $g = 1$, then
$H(-4n) = (2^{\alpha/2} - 1/2) L + 1/2$; if $\alpha$ is even and $g = 3$, then
$H(-4n) = (2^{\alpha/2 + 1} - 2/3) L + 2/3$; if $\alpha$ is even, $g \ne 1$ and
$g \equiv 1 \pmod 4$, then $H(-4n) = (2^{\alpha/2 + 1} - 1) L$; if $\alpha$ is even, $g \ne 3$ and
$g \equiv 3 \pmod 8$, then $H(-4n) = (3 \cdot 2^{\alpha/2 + 1} - 2) L$; if $\alpha$ is even and
$g \equiv 7 \pmod 8$, then $H(-4n) = 2^{\alpha/2 + 1} L$; and if $\alpha$ is odd, then
$H(-4n) = (2^{(\alpha + 1)/2} - 1) L$.

## Sources

- Zafer Selcuk Aygin and Kenneth S. Williams, *A Note on the Evaluation of Two Arithmetic Functions of Kronecker*, INTEGERS 26 (2026), Article A29, Theorem 3.

Stated but not proved: `MetaMathlibExt.unweightedHurwitzClassNumber_neg_four_mul_eq_classNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/KroneckerFormSumsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html#unweighted-hurwitz-class-number-neg-four).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kronecker's class number sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/kronecker-s-class-number-sums)
