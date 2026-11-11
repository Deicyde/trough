---
declaration: section
origin: cited
lean: MetaMathlibExt.ContinuedFractionEventuallyPeriodic, MetaMathlibExt.IsRealQuadraticIrrational, MetaMathlibExt.continuedFractionEventuallyPeriodic_of_isRealQuadraticIrrational, MetaMathlibExt.isRealQuadraticIrrational_of_continuedFractionEventuallyPeriodic, MetaMathlibExt.continuedFractionEventuallyPeriodic_iff_isRealQuadraticIrrational
statement: formalized
proof: formalized
---

# Periodic continued fractions

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html).

## Eventually periodic continued fractions

Let $x$ be a real number with regular continued
fraction $[a_0; a_1, a_2, \dots]$. The continued fraction of $x$ is eventually periodic if it does
not terminate and its sequence of partial denominators $(a_n)_{n \ge 1}$, which omits the head
coefficient $a_0$, is eventually periodic: there are natural numbers $p > 0$ and $n_0 \ge 1$ such
that $a_{n+p} = a_n$ for every $n \ge n_0$.

## Sources

- Nimbran–Levrie lines 130–134.

Formalized by `MetaMathlibExt.ContinuedFractionEventuallyPeriodic`, a definition declared in [MathlibExt/NumberTheory/ContinuedFractions/LagrangePeriodic.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ContinuedFractions/LagrangePeriodic.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html#continued-fraction-eventually-periodic).

## Real quadratic irrationals

A real number $x$ is a real quadratic irrational if it is
integral (equivalently, algebraic) over $\mathbb{Q}$ and its minimal polynomial over $\mathbb{Q}$
has degree $2$.

Degree two over $\mathbb{Q}$ captures real quadratic irrationality: such $x$ is exactly an
irrational root of a quadratic polynomial with rational coefficients.

## Sources

- Nimbran–Levrie line 136 (Euler–Lagrange statement).

Formalized by `MetaMathlibExt.IsRealQuadraticIrrational`, a definition declared in [MathlibExt/NumberTheory/ContinuedFractions/LagrangePeriodic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ContinuedFractions/LagrangePeriodic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html#is-real-quadratic-irrational).

## Lagrange's theorem on periodic continued fractions

If a real number $x$ is a real
quadratic irrational, then the continued fraction of $x$ is eventually periodic.

Formalized by `MetaMathlibExt.continuedFractionEventuallyPeriodic_of_isRealQuadraticIrrational`, a theorem declared in [MathlibExt/NumberTheory/ContinuedFractions/LagrangePeriodic.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ContinuedFractions/LagrangePeriodic.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html#continued-fraction-eventually-periodic-o).

## Euler's theorem on periodic continued fractions

If the continued fraction of a real
number $x$ is eventually periodic, then $x$ is a real quadratic irrational.

Formalized by `MetaMathlibExt.isRealQuadraticIrrational_of_continuedFractionEventuallyPeriodic`, a theorem declared in [MathlibExt/NumberTheory/ContinuedFractions/EulerPeriodic.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ContinuedFractions/EulerPeriodic.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html#is-real-quadratic-irrational-of-continue).

## Euler–Lagrange theorem

A real number $x$ has an eventually periodic continued fraction if
and only if $x$ is a real quadratic irrational.

The theorem asserts neither pure periodicity nor the stronger criterion for reduced quadratic
irrationals.

## Sources

- Nimbran–Levrie line 136.

Formalized by `MetaMathlibExt.continuedFractionEventuallyPeriodic_iff_isRealQuadraticIrrational`, a theorem declared in [MathlibExt/NumberTheory/ContinuedFractions/EulerPeriodic.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ContinuedFractions/EulerPeriodic.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html#continued-fraction-eventually-periodic-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Periodic continued fractions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/periodic-continued-fractions)
