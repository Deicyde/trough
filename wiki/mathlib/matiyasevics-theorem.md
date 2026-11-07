**Matiyasevič's theorem**, also called the MRDP theorem (after Matiyasevič, Robinson, Davis and
Putnam), says that every recursively enumerable set of [natural numbers](trough:Nat) (one whose
members some algorithm can list) is Diophantine: it is the set of parameter values for which some polynomial equation with integer
coefficients has a solution in natural numbers. Since some recursively enumerable sets cannot be
decided by any algorithm, no algorithm can decide whether an arbitrary polynomial equation with
integer coefficients has a solution in natural numbers (and hence, by a reduction given below, in
integers), which is the negative answer to Hilbert's tenth problem. The
decisive number-theoretic step is that exponentiation is Diophantine, and the standard route to it
runs through the solutions of [Pell's equation](trough:Pell.pell) $x^2 - (a^2 - 1)y^2 = 1$. Mathlib
formalizes this step, and its theorem under this name is a Diophantine description of those
solutions.

## Statement

A set $S$ of $n$-tuples of natural numbers is
Diophantine if there is a polynomial $P(x_1, \dots, x_n, y_1, \dots, y_m)$ with
integer coefficients such that a tuple $x$ lies in $S$ exactly when $P(x, y) = 0$ for some natural
numbers $y_1, \dots, y_m$. A function is Diophantine when its graph is a
Diophantine set. The full theorem says that the Diophantine sets are exactly the recursively
enumerable sets, those whose members some algorithm lists. One direction is easy: an algorithm can
search through all candidate witnesses $y$.

The key step concerns Pell's equation. Fix a natural number $a > 1$ and put
$x_0 = 1$, $y_0 = 0$ and

$$x_{n+1} = a x_n + (a^2 - 1) y_n, \qquad y_{n+1} = x_n + a y_n,$$

so that $x_n + y_n \sqrt{a^2 - 1} = (a + \sqrt{a^2 - 1})^n$; this is
the recursive definition. Each pair $(x_n, y_n)$ satisfies
$x_n^2 - (a^2 - 1) y_n^2 = 1$, and
every solution of $x^2 - (a^2 - 1)y^2 = 1$ in natural numbers is one of these pairs.

The theorem states that, for natural numbers $a, k, x, y$,
$a > 1$ with $x = x_k$ and $y = y_k$ holds if and only if $a > 1$, $k \le y$, and either $x = 1$
and $y = 0$, or there are natural numbers $u, v, s, t, b$
with

$$x^2 - (a^2 - 1) y^2 = 1, \qquad u^2 - (a^2 - 1) v^2 = 1, \qquad s^2 - (b^2 - 1) t^2 = 1,$$

$$b > 1, \qquad v > 0, \qquad y^2 \mid v,$$

$$b \equiv 1 \pmod{4y}, \qquad b \equiv a \pmod{u}, \qquad s \equiv x \pmod{u}, \qquad t \equiv k \pmod{4y}.$$

Each condition is a polynomial equation, an inequality, a divisibility or a
[congruence](trough:Int.ModEq), and each of these can be written as a polynomial equation after
adding a variable. Since Diophantine sets are closed under
intersection, union and
existential quantification over some of the variables, it follows that
the set of quadruples $(a, k, x, y)$ with $a > 1$, $x = x_k$ and $y = y_k$ is
Diophantine.

## Examples

For $a = 2$ the pairs $(x_n, y_n)$ begin $(1, 0), (2, 1), (7, 4), (26, 15), (97, 56)$, and
$97^2 - 3 \cdot 56^2 = 9409 - 9408 = 1$. Continuing, $y_8 = 10864 = 16 \cdot 679$ is divisible by
$y_2^2 = 16$, an instance of a divisibility used in the proof. For $a = 3$ the $y_n$ begin
$0, 1, 6, 35, 204$: here $y_2 = 6$ divides $y_4 = 204$, while $y_3 = 35$ does not.

## Proof

The proof rests on properties of the sequences, each proved by induction or from the addition
formulas:

- $y_m$ divides $y_n$ if and only if $m$ divides $n$, and
  $y_n^2$ divides $y_{n y_n}$; conversely,
  if $y_n^2$ divides $y_t$, then $y_n$ divides $t$.
- $n \le y_n$, and $y_n \equiv n \pmod{a - 1}$.
- If $a \equiv b \pmod c$ with $a, b > 1$, the sequences built from $a$ and from $b$ agree
  term by term modulo $c$.
- If $0 < i \le n$ and $x_j \equiv x_i \pmod{x_n}$, then $j \equiv i \pmod{4n}$ or
  $j + i \equiv 0 \pmod{4n}$.

Suppose $x = x_k$ and $y = y_k$ with $k > 0$ (the case $k = 0$ is the alternative $x = 1$,
$y = 0$). Put $m = 2ky$, $u = x_m$ and $v = y_m$. Then $y^2$ divides $y_{ky}$, which divides $v$.
Here $k \le y_k = y$, and $v > 0$ because $m > 0$. Because $m$ is even, $v$ is even, and $x_m$ is coprime to $y_m$, so $u$
is coprime to $4y$. The [Chinese remainder theorem](trough:Ideal.quotientInfRingEquivPiQuotient)
gives $b$ with $b \equiv a \pmod u$ and $b \equiv 1 \pmod{4y}$, and $b > 1$ because $a < u$. Take
$s$ and $t$ to be the $k$-th terms of the sequences built from $b$; all three Pell equations hold
because each pair is a term of a Pell sequence. Then $s \equiv x \pmod u$, and
$t \equiv k \pmod{b - 1}$, hence modulo $4y$.

Conversely, the three Pell equations make $(x, y) = (x_i, y_i)$ and $(u, v) = (x_n, y_n)$ for $a$,
and $(s, t)$ the $j$-th pair for $b$. The first alternative, $x = 1$ and $y = 0$, gives $k = 0$
directly, since $k \le y$, and $(1, 0) = (x_0, y_0)$. If $i = 0$ then $y = 0$ and $k = 0$. Otherwise $v > 0$ and
$y^2 \mid v$ give $i \le n$ and $y \mid n$. From $b \equiv 1 \pmod{4y}$ one gets
$j \equiv t \equiv k \pmod{4y}$, and from $b \equiv a \pmod u$ one gets
$x_j \equiv s \equiv x_i \pmod{x_n}$, so $j \equiv \pm i \pmod{4n}$, hence modulo $4y$. Since
$0 < i \le y$ and $k \le y$, the sum $k + i$ lies strictly between $0$ and $4y$, which excludes the
minus sign, and $k \equiv i \pmod{4y}$ then forces $k = i$.

## Consequences

- **Exponentiation is Diophantine.** The sequences grow exponentially:
  $x_k \ge a^k$. Moreover,
  for every natural number $n$, $x_k \equiv (a - n) y_k + n^k \pmod{2an - n^2 - 1}$ as a
  congruence of integers. For $a = 10$, $n = 2$ and $k = 3$ the
  modulus is $35$, and $x_3 - 8 y_3 = 3970 - 3192 = 778$ leaves remainder $8 = 2^3$. Once $a$ is
  large enough that the modulus exceeds $n^k$, the power is this remainder, which leads to
  a description of $m = n^k$ in terms of the Pell sequences for an auxiliary $a$, a Pell
  equation, a congruence, a linear equation and inequalities.
  In Diophantine terms, if $f$ and $g$ are Diophantine functions, then so is
  $v \mapsto f(v)^{g(v)}$.
- **Hilbert's tenth problem.** Combined with the separate fact that every recursively enumerable
  set is defined by equations that may also use exponentiation, this yields the full theorem. The
  set of programs that halt on a given input
  is recursively enumerable but
  not computable (the
  [halting problem](trough:ComputablePred.halting_problem)), so some Diophantine set is undecidable.
  Solvability in integers is no easier, since
  [every natural number is a sum of four squares](trough:Nat.sum_four_squares).
- **Primes.** Applied to the primes, the full theorem (every recursively enumerable set
  is Diophantine) gives a polynomial with integer coefficients whose
  positive values, as its variables range over the natural numbers, are exactly the prime numbers.

## In Mathlib

The Pell sequences and the theorem are stated in the natural numbers, while the polynomials that
define Diophantine sets take integer values on natural-number arguments. The Pell sequences take a natural number $a$
together with a proof that $a > 1$, so the left side of the theorem asserts that such a proof
exists along with the two equalities. Subtraction of natural numbers is truncated at zero, but
each Pell equation in the statement asks for a difference equal to $1$, which rules out truncation,
so the equations mean what they say; a congruence modulo $0$ is equality. Diophantine sets are
sets of functions from an arbitrary index type to the natural numbers, with witnesses indexed by
an arbitrary type as well, defined with Mathlib's own
type of integer polynomial functions rather than its general
[multivariate polynomials](trough:MvPolynomial). Diophantine functions and partial functions are
those with Diophantine graphs, and
the partial map sending $(a, k)$ with $a > 1$ to $x_k$ is Diophantine.
Mathlib stops at exponentiation: it contains neither the theorem that every recursively enumerable
set is Diophantine nor the negative solution of Hilbert's tenth problem.

## Depends on

- [Natural number](trough:Nat)
- [Polynomial in several indeterminates](trough:MvPolynomial)
- [Congruence in $\Z$](trough:Int.ModEq)
- [Solutions to Pell's equation](trough:Pell.pell)

## Proof depends on

- [Solutions to Pell’s Equation](trough:Pell.eq_pell)
- [Chinese remainder theorem](trough:Ideal.quotientInfRingEquivPiQuotient)
