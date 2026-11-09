# $p$-adic number

For a [prime number](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) $p$, the **$p$-adic numbers** form a [field](../field-theory/field.md) $\mathbb{Q}_p$ that
contains the [rational numbers](rational-number.md) and is complete for a notion of size in which a number is
small when it is divisible by a high power of $p$. Just as the [real numbers](real-number.md) arise by
filling in the gaps of $\mathbb{Q}$ for the ordinary absolute value, $\mathbb{Q}_p$ arises by filling
them in for the $p$-adic absolute value. The $p$-adic numbers let analytic methods (limits, series,
approximation) be applied to questions about divisibility and congruences, and they are a basic tool
of modern number theory.

## Definition

Every nonzero rational number $x$ can be written as $x = p^{v} a/b$ with $v$ an integer and $a, b$
integers not divisible by $p$. The exponent $v$ is determined by $x$; it is the
[$p$-adic valuation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicVal/Basic.html#padicValRat) $v_p(x)$, the multiplicity of $p$ in the numerator minus its
multiplicity in the denominator. The [$p$-adic absolute value](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNorm.html#padicNorm) of $x$ is

$$|x|_p = p^{-v_p(x)}, \qquad |0|_p = 0.$$

It satisfies $|xy|_p = |x|_p\,|y|_p$ and the strong triangle inequality
[$|x + y|_p \le \max(|x|_p, |y|_p)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNorm.html#padicNorm.nonarchimedean), so $d(x, y) = |x - y|_p$ is a [metric](../../topology/metric-spaces/metric-space.md)
on $\mathbb{Q}$. This metric space is not [complete](../../topology/uniform-notions/completeness.md). The field $\mathbb{Q}_p$ is
[its completion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic): its elements are equivalence classes of
[Cauchy sequences](../../topology/uniform-notions/cauchy-sequence.md) of rationals for $|\cdot|_p$, two sequences being equivalent when
their difference tends to $0$. Sums and products are taken term by term.

## Examples

- Since $18 = 2 \cdot 3^2$, one has $|18|_3 = 1/9$, while $|1/6|_3 = 3$. In $\mathbb{Q}_3$ the integer
  $18$ is close to $0$ and the fraction $1/6$ is large.
- The prime itself has [$|p|_p = 1/p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.norm_p), and
  [$|p^n|_p = p^{-n}$ for every natural number $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.norm_p_pow), so the powers $p^n$ tend to
  $0$ in $\mathbb{Q}_p$.
- Every integer $k$ satisfies [$|k|_p \le 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.norm_int_le_one), with
  [$|k|_p < 1$ if and only if $p$ divides $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.norm_intCast_lt_one_iff).
- Because $|p^n|_p \to 0$, the geometric series $1 + p + p^2 + \cdots$ converges in $\mathbb{Q}_p$ to
  $1/(1 - p)$. Multiplying by $p - 1$ gives
  $$-1 = (p - 1) + (p - 1)p + (p - 1)p^2 + \cdots,$$
  a series with digits between $0$ and $p - 1$ that converges to the rational number $-1$.
- More generally, every nonzero $x \in \mathbb{Q}_p$ has a unique expansion
  $x = \sum_{n \ge m} a_n p^n$ with an integer $m$, digits $a_n \in \{0, 1, \dots, p - 1\}$ and
  $a_m \neq 0$; the sum may have infinitely many nonzero terms, but only finitely many negative powers
  of $p$ occur.

## Properties

- **Field and norm.** The absolute value extends from $\mathbb{Q}$ to $\mathbb{Q}_p$; the
  [extended norm restricts to $|\cdot|_p$ on the rationals](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.eq_padicNorm), and with it
  $\mathbb{Q}_p$ is a [normed field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.normedField).
- **Completeness and density.** [Every Cauchy sequence in $\mathbb{Q}_p$ converges](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.complete),
  and [the rationals are dense in $\mathbb{Q}_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.denseRange_ratCast).
- **Ultrametric inequality.** For all $x, y \in \mathbb{Q}_p$,
  [$|x + y|_p \le \max(|x|_p, |y|_p)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.nonarchimedean), and
  [equality holds when $|x|_p \neq |y|_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.add_eq_max_of_ne). Consequently every triangle is
  isosceles, and, since $\mathbb{Q}_p$ is complete, a series in $\mathbb{Q}_p$ converges exactly when
  its terms tend to $0$.
- **Valuation.** The valuation extends to $\mathbb{Q}_p$:
  [it agrees with $v_p$ on rationals](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.valuation_ratCast),
  [$|x|_p = p^{-v_p(x)}$ for $x \neq 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.norm_eq_zpow_neg_valuation), and
  [$v_p(xy) = v_p(x) + v_p(y)$ for nonzero $x$ and $y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.valuation_mul). The norm therefore
  takes only the values $0$ and $p^n$ for $n \in \mathbb{Z}$, and every nonzero $x$ is $p^{v_p(x)}u$ with
  $|u|_p = 1$.
- **Integers.** The closed unit ball $\{x : |x|_p \le 1\}$ is a subring, the
  [$p$-adic integers](p-adic-integer.md) $\mathbb{Z}_p$. It is [compact](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/ProperSpace.html#PadicInt.compactSpace), its
  [units are exactly the elements of norm $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.isUnit_iff), it is a
  [local ring](../rings/local-ring.md) whose
  [maximal ideal is generated by $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.maximalIdeal_eq_span_p), and
  [$\mathbb{Q}_p$ is its field of fractions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicIntegers.html#PadicInt.isFractionRing). Since $\mathbb{Z}_p$ is a
  compact neighbourhood of $0$, the field $\mathbb{Q}_p$ is locally compact.

## Related concepts

- [Ostrowski's theorem](../../../thousand-plus/number-theory/part-02/ostrowskis-theorem.md) explains why the $p$-adic
  fields and $\mathbb{R}$ are the natural completions of $\mathbb{Q}$:
  [every nontrivial real-valued absolute value on $\mathbb{Q}$ is equivalent either to the ordinary absolute value or to the $p$-adic absolute value for exactly one prime $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Ostrowski.html#Rat.AbsoluteValue.equiv_real_or_padic).
- [Hensel's lemma](../number-theory/hensels-lemma-for-z-p.md) turns approximate roots into exact ones: for a polynomial $F$
  with coefficients in $\mathbb{Z}_p$ and $a \in \mathbb{Z}_p$ with $|F(a)|_p < |F'(a)|_p^2$,
  [there is a unique root $z \in \mathbb{Z}_p$ of $F$ with $|z - a|_p < |F'(a)|_p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/Hensel.html#hensels_lemma).
  For example, $a = 2$ and $F = X^2 + 1$ give $|F(2)|_5 = 1/5 < 1 = |F'(2)|_5^2$, so $-1$ has a square
  root in $\mathbb{Q}_5$.
- The construction is a special case of the [completion](../../topology/uniform-notions/completion.md) of a metric
  space, and the same recipe applied to the ordinary absolute value produces $\mathbb{R}$.

## In Mathlib

Mathlib takes $p$ to be a natural number together with a standing hypothesis that it is prime. It
builds $\mathbb{Q}_p$ with the same concrete construction by Cauchy sequences of rationals that it
uses for the real numbers, rather than through its general completion of uniform spaces, and the
field structure is inherited from that construction. The main norm is real-valued, so that
$\mathbb{Q}_p$ fits the general theory of normed fields; [a rational-valued version](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#padicNormE) is kept
alongside it. The valuation on $\mathbb{Q}_p$ is an integer-valued function that, by convention,
[assigns $0$ to the number $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.valuation_zero), so statements about it carry nonzero
hypotheses; Mathlib also provides
[an additive valuation with values in the integers extended by $+\infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic.addValuation),
which sends $0$ to $+\infty$ as in the textbook convention. The $p$-adic integers are defined as the
subring of elements of norm at most $1$, not as an inverse limit of the rings $\mathbb{Z}/p^n\mathbb{Z}$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Rational number](rational-number.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Field](../field-theory/field.md)
- [Metric space](../../topology/metric-spaces/metric-space.md)
- [Cauchy sequence](../../topology/uniform-notions/cauchy-sequence.md)
- [Completion](../../topology/uniform-notions/completion.md)

## Sources

- [Mathlib documentation: `Padic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Padics/PadicNumbers.html#Padic)
- [Source of `Padic` in Mathlib/NumberTheory/Padics/PadicNumbers.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/Padics/PadicNumbers.lean#L542)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L28)
