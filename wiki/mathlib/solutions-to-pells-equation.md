---
article_id: af_76c2a85474a62ae4524d1644
concept: Pell.pell
---

The **solutions to Pell's equation** $x^2 - dy^2 = 1$ in the special case $d = a^2 - 1$,
for an integer $a > 1$, can be written down completely: the solutions in
[natural numbers](trough:Nat) form a single sequence of pairs, the **Pell sequence**, generated
from the obvious solution $(a, 1)$ by a linear recursion, and the integer solutions are these up
to sign. In this case the fundamental solution is evident, and the case serves as a model for the
general theory of [Pell's equation](trough:Pell.eq_pell); its explicit recursion makes the
solutions easy to compute and to reason about. Their growth, divisibility and congruence
properties are the main ingredients of [Matiyasevič's theorem](trough:Pell.matiyasevic) that
exponentiation is Diophantine.

## Definition

Fix a natural number $a > 1$ and put $d = a^2 - 1$. Then $a^2 - d \cdot 1^2 = 1$, so $(a, 1)$
solves the equation. The Pell sequence $(x_n, y_n)$ is
[defined by the recursion](lean:Pell.pell)

$$(x_0, y_0) = (1, 0), \qquad (x_{n+1}, y_{n+1}) = (a x_n + d y_n,\; x_n + a y_n).$$

In the ring $\mathbb{Z}[\sqrt d]$ of numbers $u + v\sqrt d$ with $u, v$ [integers](trough:Int),
the recursion says that
[$x_{n+1} + y_{n+1}\sqrt d$ equals $(x_n + y_n\sqrt d)(a + \sqrt d)$](lean:Pell.pellZd_succ),
so by induction

$$x_n + y_n \sqrt d = \left(a + \sqrt d\right)^n .$$

The number $d$ is never a perfect square, because $(a-1)^2 < a^2 - 1 < a^2$; Mathlib records
that [$d$ is not the square of a natural number](lean:Pell.dnsq).

## Every term is a solution, and every solution is a term

For any integer $d$, if $(x, y)$ and $(u, v)$ solve $x^2 - dy^2 = 1$ then so does
$(xu + dyv,\; xv + yu)$, since in $\mathbb{Z}[\sqrt d]$ the
[product of two solutions is a solution](lean:Pell.isPell_mul). Starting from $(1, 0)$ and
multiplying repeatedly by $(a, 1)$ therefore gives solutions only:
[$x_n^2 - d y_n^2 = 1$ for every $n$](lean:Pell.pell_eqz).

Conversely, [every solution in natural numbers is $(x_n, y_n)$ for some $n$](lean:Pell.eq_pell).
A sketch: write $\varepsilon = a + \sqrt d > 1$, and let $\beta = x + y\sqrt d$ come from a
solution with $x, y \ge 0$, so $x \ge 1$ and $\beta \ge 1$. Choose $n$ with
$\varepsilon^n \le \beta < \varepsilon^{n+1}$. Since $(a + \sqrt d)(a - \sqrt d) = 1$, the number
$\gamma = \beta (a - \sqrt d)^n = u + v\sqrt d$ lies in $\mathbb{Z}[\sqrt d]$, solves the
equation, and satisfies $1 \le \gamma < \varepsilon$. Its conjugate $u - v\sqrt d = \gamma^{-1}$
lies in $(0, 1]$, so $u > 0$ and $v \ge 0$. If $v \ge 1$, then $u^2 = 1 + dv^2 \ge a^2$ gives
$\gamma \ge a + \sqrt d = \varepsilon$, a contradiction; hence $v = 0$, $u = 1$, and
$\beta = \varepsilon^n$. Since $\sqrt d$ is irrational, comparing coordinates gives
$(x, y) = (x_n, y_n)$. Allowing signs, the integer solutions are exactly the pairs
$(\pm x_n, \pm y_n)$.

## Examples

- For $a = 2$, $d = 3$, the sequence begins $(1, 0), (2, 1), (7, 4), (26, 15), (97, 56)$;
  for instance $97^2 - 3 \cdot 56^2 = 9409 - 9408 = 1$.
- For $a = 3$, $d = 8$, it begins $(1, 0), (3, 1), (17, 6), (99, 35)$, and
  $99^2 - 8 \cdot 35^2 = 9801 - 9800 = 1$.

## Properties

- **Addition formulas.** Since the terms are powers of $\varepsilon$,
  [$x_{m+n} + y_{m+n}\sqrt d = (x_m + y_m\sqrt d)(x_n + y_n\sqrt d)$](lean:Pell.pellZd_add);
  in coordinates, [$x_{m+n} = x_m x_n + d\, y_m y_n$](lean:Pell.xn_add) and
  [$y_{m+n} = x_m y_n + y_m x_n$](lean:Pell.yn_add).
- **Second-order recursion.** Both sequences satisfy the same linear recurrence:
  [$x_{n+2} + x_n = 2a\, x_{n+1}$](lean:Pell.xn_succ_succ) and
  [$y_{n+2} + y_n = 2a\, y_{n+1}$](lean:Pell.yn_succ_succ). For $a = 2$ this reads
  $x_{n+2} = 4x_{n+1} - x_n$, as in $26 = 4 \cdot 7 - 2$.
- **Growth.** [The sequence $(x_n)$ is strictly increasing](lean:Pell.strictMono_x), and so is
  [$(y_n)$](lean:Pell.strictMono_y); moreover [$x_n \ge a^n$](lean:Pell.xn_ge_a_pow) and
  [$y_n \ge n$](lean:Pell.yn_ge_n).
- **Coprimality.** [$x_n$ and $y_n$ are coprime](lean:Pell.xy_coprime), since any common
  divisor divides $x_n^2 - d y_n^2 = 1$.
- **Divisibility.** [$y_m$ divides $y_n$ if and only if $m$ divides $n$](lean:Pell.y_dvd_iff).
  A deeper statement relates values to indices: [if $y_n^2$ divides $y_t$, then $y_n$ divides $t$](lean:Pell.dvd_of_ysq_dvd).
- **Congruences.** [$y_n \equiv n \pmod{a - 1}$](lean:Pell.yn_modEq_a_sub_one) and
  [$y_n \equiv n \pmod 2$](lean:Pell.yn_modEq_two). If $a$ and $b$ are both greater than $1$ and
  $a \equiv b \pmod c$, then
  [the $n$-th terms built from $a$ and from $b$ agree modulo $c$, in both coordinates](lean:Pell.xy_modEq_of_modEq).

The growth, divisibility and congruence properties are what make the sequence useful in logic: they let a system of
polynomial equations in natural numbers express that a pair of variables is the $k$-th term of
the sequence, which is the key step in [Matiyasevič's theorem](trough:Pell.matiyasevic).

## Generalizations

For a general positive integer $d$ that is not a square,
[Pell's equation still has a solution with $y \neq 0$](lean:Pell.exists_of_not_isSquare), and for
every integer $d$ the integer solutions form an
[abelian group](lean:Pell.Solution₁.instCommGroup) under the multiplication of
$\mathbb{Z}[\sqrt d]$. When a fundamental solution exists (the solution with $y > 0$ whose $x$ is least
among all solutions with $x > 1$), [every solution is, up to sign, an integer power of it](lean:Pell.IsFundamental.eq_zpow_or_neg_zpow).
For $d = a^2 - 1$ the fundamental solution is $(a, 1)$: a solution with $y \ge 1$ has
$x^2 = 1 + dy^2 \ge a^2$. In general the fundamental solution can be far larger than $d$, and it
is found from the [continued fraction](trough:ContFract) expansion of $\sqrt d$. For positive
non-square $d$, the solution group is an infinite cyclic group times $\{\pm 1\}$, which
parallels the
[Dirichlet unit theorem](trough:NumberField.Units.exist_unique_eq_mul_prod) for real quadratic
fields.

## In Mathlib

Mathlib treats the case $d = a^2 - 1$ separately from general $d$. The sequence takes as input
a natural number $a$ together with a proof that $a > 1$, and returns pairs of natural numbers;
its coordinates are named separately as [the $x$-sequence](lean:Pell.xn) and
[the $y$-sequence](lean:Pell.yn), with integer copies and a copy in $\mathbb{Z}[\sqrt d]$ for
algebraic manipulation. Statements in natural numbers use truncated subtraction, where $m - k$
is $0$ when $k > m$. The equation is therefore written as $x^2 - dy^2 = 1$ in natural numbers,
which is still equivalent to $x^2 = dy^2 + 1$ because the right side is not $0$; this is the
form of the hypothesis in the completeness theorem. The general theory, for every integer $d$,
works with a bundled type of integer solutions carrying its group structure, and shows that for
positive $d$ [a solution with $y \neq 0$ exists exactly when $d$ is not a
square](lean:Pell.exists_iff_not_isSquare).

## Depends on

- [Natural number](trough:Nat)
- [Integer](trough:Int)

## Proof depends on

- [Real number](trough:Real)
