---
declaration: section
origin: cited
lean: MetaMathlibExt.cubicRecurrenceRootCondition, MetaMathlibExt.IsCubicRecurrencePair, MetaMathlibExt.cubicRecurrenceDiscriminant, MetaMathlibExt.cubicRecurrenceDiscriminant_dvd_mul
statement: formalized
proof: formalized
---

# Cubic analogues of Lucas sequences

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences/index.html).

## Root condition for the Roettger–Williams cubic

For integers $S_1, S_2, R$ and a complex
number $\gamma$, put $\rho = R(\gamma + \gamma^{-1})$ (with the convention $0^{-1} = 0$) and
$S_3 = RS_1^2 - 2RS_2 - 4R^3$. The root condition holds when $\rho$ is a root of the cubic
$x^3 - S_1x^2 + S_2x - S_3$, that is, when $\rho^3 - S_1\rho^2 + S_2\rho - S_3 = 0$.

Formalized by `MetaMathlibExt.cubicRecurrenceRootCondition`, a definition declared in [MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences/index.html#cubic-recurrence-root-condition).

## Cubic recurrence pair

Integer sequences $U$ and $W$ form a cubic recurrence pair for
integers $S_1, S_2, R$ when there are pairwise distinct complex numbers $\gamma_1, \gamma_2,
\gamma_3$, each different from $1$, with $\gamma_1\gamma_2\gamma_3 = 1$, such that each
$\gamma_i$ satisfies the cubic recurrence root condition for $(S_1, S_2, R)$, $U_0 = 0$,
$U_n(1 - \gamma_1)(1 - \gamma_2)(1 - \gamma_3) = R^{n-1}(1 - \gamma_1^n)(1 - \gamma_2^n)
(1 - \gamma_3^n)$ for every $n \ge 1$, and
$W_n = R^n\bigl((1 + \gamma_1^n)(1 + \gamma_2^n)(1 + \gamma_3^n) - 2\bigr)$ for every $n \ge 0$.

These equations determine every value of $U$ and $W$; the equation for $U_n$ is the source's
formula with its denominator $(1 - \gamma_1)(1 - \gamma_2)(1 - \gamma_3)$ cleared.

Formalized by `MetaMathlibExt.IsCubicRecurrencePair`, a definition declared in [MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences/index.html#is-cubic-recurrence-pair).

## Cubic-recurrence discriminant sequence

For an integer $R$ and integer sequences $U$ and
$W$, the discriminant sequence is $D_n = \gcd(W_n - 6R^n, U_n)$ for $n \ge 0$: the greatest
common divisor of the natural numbers $|W_n - 6R^n|$ and $|U_n|$.

Formalized by `MetaMathlibExt.cubicRecurrenceDiscriminant`, a definition declared in [MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences/index.html#cubic-recurrence-discriminant).

## Divisibility of the cubic-recurrence discriminants

Let $S_1, S_2, R$ be integers, let $U$
and $W$ be integer sequences forming a cubic recurrence pair for $(S_1, S_2, R)$, and let
$D_n = \gcd(W_n - 6R^n, U_n)$ be their discriminant sequence. Then for all integers $n \ge 1$
and $m \ge 1$, $D_n$ divides $D_{nm}$.

## Sources

- E. L. Roettger and H. C. Williams, "Some Arithmetic Properties of Certain Sequences", Journal of Integer Sequences 18 (2015), Article 15.6.2, Theorem `Dndivis`, line 269, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Roettger/roettger4.tex>.

Formalized by `MetaMathlibExt.cubicRecurrenceDiscriminant_dvd_mul`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean, line 608](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/CubicRecurrenceDiscriminant.lean#L608). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences/index.html#cubic-recurrence-discriminant-dvd-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cubic analogues of Lucas sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/cubic-analogues-of-lucas-sequences)
