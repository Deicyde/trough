---
declaration: section
origin: cited
lean: MetaMathlibExt.IsAntimultiplicative, MetaMathlibExt.isAntimultiplicative_one, MetaMathlibExt.IsAntimultiplicative.apply_prime, MetaMathlibExt.dirichletUnits_multiplicative_antimultiplicative_subgroups, MetaMathlibExt.existsUnique_multiplicative_mul_antimultiplicative, MetaMathlibExt.dirichletRealPower_vectorSpace, MetaMathlibExt.dirichletRealPower_multiplicative_antimultiplicative_subspaces
statement: formalized
---

# Antimultiplicative arithmetic functions

7 results, 3 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html).

## Antimultiplicative arithmetical functions

Let $R$ be a type with a zero and a one. An
arithmetical function $f$ with values in $R$ is antimultiplicative if $f(1) = 1$ and $f(p^k) = 0$
for every prime $p$ and every integer $k \ge 1$.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Section 2.

Formalized by `MetaMathlibExt.IsAntimultiplicative`, a definition declared in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#is-antimultiplicative).

## The Dirichlet identity is antimultiplicative

For every semiring $R$, the identity
$\delta$ of Dirichlet convolution on arithmetical functions with values in $R$, given by
$\delta(1) = 1$ and $\delta(n) = 0$ for $n \ne 1$, is antimultiplicative.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Section 2.

Formalized by `MetaMathlibExt.isAntimultiplicative_one`, a theorem declared in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#is-antimultiplicative-one).

## Antimultiplicative functions vanish at primes

Let $R$ be a type with a zero and a one, and
let $f$ be an antimultiplicative arithmetical function with values in $R$. Then $f(p) = 0$ for
every prime $p$.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Section 2.

Formalized by `MetaMathlibExt.IsAntimultiplicative.apply_prime`, a theorem declared in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#apply-prime).

## Multiplicative and antimultiplicative units form subgroups

Let $U$ be the group of units
of the ring of real arithmetical functions under Dirichlet convolution. The units $f$ with
$f(1) = 1$, the multiplicative units and the antimultiplicative units form subgroups $U_1$, $U_M$
and $U_A$ of $U$, respectively. Moreover $U_M \le U_1$, $U_A \le U_1$ and
$U_M \cap U_A = \{\delta\}$, where $\delta$ is the Dirichlet identity.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Proposition 1.

Stated but not proved: `MetaMathlibExt.dirichletUnits_multiplicative_antimultiplicative_subgroups` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#dirichlet-units-multiplicative-antimulti).

## Unique splitting into multiplicative and antimultiplicative parts

Every real
arithmetical function $f$ with $f(1) = 1$ can be written in exactly one way as a Dirichlet
convolution $f = g * h$ of a multiplicative real arithmetical function $g$ and an
antimultiplicative real arithmetical function $h$.

In the source, writing $U_1$, $U_M$ and $U_A$ for the real arithmetical functions $f$ with
$f(1) = 1$, the multiplicative ones and the antimultiplicative ones, this is written
$U_1 = U_M \oplus U_A$.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Proposition 2.

Stated but not proved: `MetaMathlibExt.existsUnique_multiplicative_mul_antimultiplicative` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#exists-unique-multiplicative-mul-antimul).

## Rearick's real power and its vector space laws

Let $L$ denote the Rearick logarithm and
$*$ the Dirichlet convolution. There is a map $(\alpha, f) \mapsto f^{(\alpha)}$, sending a real
number $\alpha$ and a real arithmetical function $f$ to a real arithmetical function, such that:
for every real $\alpha$ and every real arithmetical function $f$ with $f(1) = 1$, we have
$f^{(\alpha)}(1) = 1$ and $L(f^{(\alpha)}) = \alpha L(f)$; and for all real arithmetical functions
$f$, $g$ with $f(1) = g(1) = 1$ and all real $\alpha$, $\beta$, we have
$(f^{(\alpha)})^{(\beta)} = f^{(\alpha\beta)}$, $f^{(\alpha+\beta)} = f^{(\alpha)} * f^{(\beta)}$,
$(f * g)^{(\alpha)} = f^{(\alpha)} * g^{(\alpha)}$ and $f^{(1)} = f$.

In the source this is the statement that the real arithmetical functions $f$ with $f(1) = 1$ form
a real vector space, with Dirichlet convolution as addition and the real power as scalar
multiplication.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Theorem 1.

Stated but not proved: `MetaMathlibExt.dirichletRealPower_vectorSpace` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#dirichlet-real-power-vector-space).

## Real powers preserve multiplicativity and antimultiplicativity

Let $L$ denote the
Rearick logarithm. Let $f$ and $F$ be real arithmetical functions with $f(1) = F(1) = 1$, and let
$\alpha$ be a real number with $L(F) = \alpha L(f)$. If $f$ is multiplicative, then $F$ is
multiplicative, and if $f$ is antimultiplicative, then $F$ is antimultiplicative. Moreover, every
real arithmetical function $f$ with $f(1) = 1$ can be written in exactly one way as a Dirichlet
convolution $f = g * h$ with $g$ multiplicative and $h$ antimultiplicative.

In the source $F$ is Rearick's real power $f^{(\alpha)}$, and the theorem says that the
multiplicative and the antimultiplicative functions with $f(1) = 1$ form subspaces of the real
vector space of all real arithmetical functions $f$ with $f(1) = 1$, whose direct sum is that space.

## Sources

- Pentti Haukkanen and Timo Tossavainen, *Some Perpendicularities of Arithmetical Functions*, INTEGERS 25 (2025), Article A33, Theorem 2.

Stated but not proved: `MetaMathlibExt.dirichletRealPower_multiplicative_antimultiplicative_subspaces` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ArithmeticFunction/ArithmeticFunctionPerpendicularityWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html#dirichlet-real-power-multiplicative-anti).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Antimultiplicative arithmetic functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/antimultiplicative-arithmetic-functions)
