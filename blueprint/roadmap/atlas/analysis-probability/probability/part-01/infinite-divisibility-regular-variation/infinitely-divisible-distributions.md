---
declaration: section
origin: cited
lean: MeasureTheory.Measure.convPow, MeasureTheory.Measure.convPow_zero, MeasureTheory.Measure.convPow_succ, MeasureTheory.Measure.convPow_one, MeasureTheory.Measure.sfinite_convPow, MeasureTheory.Measure.isProbabilityMeasure_convPow, MeasureTheory.Measure.convPow_succ_eq_iterate, MeasureTheory.Measure.convPow_add
statement: formalized
proof: formalized
---

# Infinitely divisible distributions

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html).

## Convolution power of a measure

Let $M$ be an additive commutative monoid with a
σ-algebra and let $\nu$ be a measure on $M$. The $n$-th convolution power $\nu^{*n}$ of $\nu$ is
defined by recursion on $n$: $\nu^{*0} = \delta_0$, the Dirac measure at the identity $0$ of
$M$, and $\nu^{*(n+1)} = \nu^{*n} * \nu$, where $*$ denotes convolution of measures.

When addition on $M$ is jointly measurable and $\nu$ is the law of a random variable $Y$,
$\nu^{*n}$ is the law of the sum of $n$ independent copies of $Y$.

Formalized by `MeasureTheory.Measure.convPow`, a definition declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow).

## The zeroth convolution power

For every measure $\nu$ on an additive commutative monoid
$M$ with a σ-algebra, the zeroth convolution power of $\nu$ is the Dirac measure $\delta_0$ at
the identity element $0$ of $M$.

Formalized by `MeasureTheory.Measure.convPow_zero`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-zero).

## Recursion for convolution powers

Let $M$ be an additive commutative monoid with a
σ-algebra and let $\nu$ be a measure on $M$. For every natural number $n$, the $(n+1)$-st
convolution power of $\nu$ is the convolution of the $n$-th convolution power of $\nu$
with $\nu$.

Formalized by `MeasureTheory.Measure.convPow_succ`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-succ).

## The first convolution power

Let $M$ be an additive commutative monoid with a
σ-algebra for which addition $M \times M \to M$ is measurable, and let $\nu$ be an s-finite
measure on $M$. Then the first convolution power of $\nu$ is $\nu$ itself.

Formalized by `MeasureTheory.Measure.convPow_one`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-one).

## Convolution powers of an s-finite measure are s-finite

Let $M$ be an additive
commutative monoid with a measurable structure. If $\nu$ is an s-finite measure on $M$, then for
every natural number $n$ its $n$-fold convolution power $\nu^{*n}$ is s-finite.

Formalized by `MeasureTheory.Measure.sfinite_convPow`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#sfinite-conv-pow).

## Convolution powers of a probability measure are probability measures

Let $M$ be an
additive commutative monoid with a measurable structure. If $\nu$ is a probability measure on
$M$, then for every natural number $n$ its $n$-fold convolution power $\nu^{*n}$ is a probability
measure.

Formalized by `MeasureTheory.Measure.isProbabilityMeasure_convPow`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#is-probability-measure-conv-pow).

## Convolution powers as iterated left convolution

Let $M$ be an additive commutative
monoid with a σ-algebra for which addition $M \times M \to M$ is measurable, and let $\nu$ be an
s-finite measure on $M$. For every natural number $n$, the $(n+1)$-st convolution power of
$\nu$ equals the measure obtained from $\nu$ by applying the map $\mu \mapsto \nu * \mu$
exactly $n$ times, where $*$ denotes convolution of measures.

Formalized by `MeasureTheory.Measure.convPow_succ_eq_iterate`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-succ-eq-iterate).

## Convolution powers add exponents

Let $M$ be an additive commutative monoid with a
σ-algebra for which addition $M \times M \to M$ is measurable, and let $\nu$ be an s-finite
measure on $M$. Writing $*$ for convolution of measures and $\nu^{*n}$ for the $n$-th
convolution power of $\nu$, for all natural numbers $m$ and $n$ we have
$\nu^{*(m+n)} = \nu^{*m} * \nu^{*n}$.

Formalized by `MeasureTheory.Measure.convPow_add`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-add).

## Interchange law for convolution

Let $M$ be an additive commutative monoid with a
σ-algebra for which addition $M \times M \to M$ is measurable. For all s-finite measures
$a, b, c, d$ on $M$ we have $(a * b) * (c * d) = (a * c) * (b * d)$, where $*$ denotes
convolution of measures.

Formalized by `MeasureTheory.Measure.conv_mul_conv`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-mul-conv).

## Convolution power of a convolution

Let $M$ be an additive commutative monoid with a
σ-algebra for which addition $M \times M \to M$ is measurable, and let $\nu$ and $\rho$ be
s-finite measures on $M$. Writing $*$ for convolution of measures and $\mu^{*n}$ for the $n$-th
convolution power of a measure $\mu$, for every natural number $n$ we have
$(\nu * \rho)^{*n} = \nu^{*n} * \rho^{*n}$.

Formalized by `MeasureTheory.Measure.convPow_conv`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-conv).

## Infinitely divisible measures

Let $M$ be an additive commutative monoid with a measurable
structure in which addition is jointly measurable. A measure $\mu$ on $M$ is
**infinitely divisible** if for every natural number $n \ge 1$ there is a probability measure
$\nu$ on $M$ whose $n$-fold convolution power $\nu^{*n}$ equals $\mu$.

Equivalently, a random variable $X$ with law $\mu$ can, for every $n \ge 1$, be written in law as
the sum of $n$ i.i.d. copies of some random variable $Y$.

Formalized by `MeasureTheory.Measure.IsInfinitelyDivisible`, a definition declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#is-infinitely-divisible).

## Infinitely divisible measures are probability measures

Let $M$ be an additive
commutative monoid with a measurable structure in which addition is jointly measurable. Every
infinitely divisible measure on $M$ is a probability measure.

The convolution root of order one is the measure itself, and it is a probability measure by
definition.

Formalized by `MeasureTheory.Measure.IsInfinitelyDivisible.isProbabilityMeasure`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#is-probability-measure).

## Infinite divisibility through iterated convolution

Let $M$ be an additive commutative
monoid with a measurable structure in which addition is jointly measurable. A measure $\mu$ on
$M$ is infinitely divisible if and only if for every natural number $n \ne 0$ there is a
probability measure $\nu$ on $M$ such that $\mu = \nu * (\nu * (\cdots * (\nu * \nu)))$ with $n$
factors $\nu$, that is, $\mu$ is obtained from $\nu$ by convolving on the left with $\nu$ exactly
$n - 1$ times.

Formalized by `MeasureTheory.Measure.isInfinitelyDivisible_iff_exists_iterate`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#is-infinitely-divisible-iff-exists-itera).

## Infinite divisibility is closed under convolution

Let $M$ be an additive commutative
monoid with a measurable structure in which addition is jointly measurable. If $\mu$ and $\eta$
are infinitely divisible measures on $M$, then their convolution $\mu * \eta$ is infinitely
divisible.

For each $n \ge 1$, convolving an $n$-th convolution root of $\mu$ with one of $\eta$ gives an
$n$-th convolution root of $\mu * \eta$.

Formalized by `MeasureTheory.Measure.IsInfinitelyDivisible.conv`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv).

## Convolution powers of a Dirac measure

Let $M$ be an additive commutative monoid with a
σ-algebra for which addition $M \times M \to M$ is measurable. For every point $x \in M$ and
every natural number $n$, the $n$-th convolution power of the Dirac measure $\delta_x$ is
$\delta_{nx}$, where $nx$ is the sum of $n$ copies of $x$ (so $0x = 0$).

Formalized by `MeasureTheory.Measure.convPow_dirac`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-dirac).

## Dirac measures on the real line are infinitely divisible

For every real number $a$, the
Dirac measure $\delta_a$ on $\mathbb{R}$ is infinitely divisible: for every $n \ge 1$, $\delta_a$
is the $n$-fold convolution power of $\delta_{a/n}$.

Formalized by `MeasureTheory.Measure.isInfinitelyDivisible_dirac`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#is-infinitely-divisible-dirac).

## Convolution powers of a Poisson measure

For every real rate $r \ge 0$ and every natural
number $n$, the $(n+1)$-st convolution power of the Poisson measure on $\mathbb{N}$ with rate
$r$ is the Poisson measure on $\mathbb{N}$ with rate $(n+1)r$.

Formalized by `MeasureTheory.Measure.convPow_succ_poissonMeasure`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#conv-pow-succ-poisson-measure).

## Poisson distributions are infinitely divisible

For every real $r \ge 0$, the Poisson
distribution with parameter $r$, as a measure on $\mathbb{N}$, is infinitely divisible: for
every $n \ge 1$ it is the $n$-fold convolution power of the Poisson distribution with parameter
$r/n$.

Formalized by `MeasureTheory.Measure.isInfinitelyDivisible_poissonMeasure`, a theorem declared in [MathlibExt/Probability/InfinitelyDivisible.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/InfinitelyDivisible.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html#is-infinitely-divisible-poisson-measure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinitely divisible distributions](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/infinite-divisibility-regular-variation/infinitely-divisible-distributions)
