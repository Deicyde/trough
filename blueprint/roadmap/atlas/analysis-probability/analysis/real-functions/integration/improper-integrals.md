---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Integral.ImproperIntegralAbsoluteConditionalWanted.dirichlet_integral_conditionally_convergent, MathlibExt.MeasureTheory.Integral.ImproperIntegralComparisonWanted.improper_integral_comparison_test, MathlibExt.MeasureTheory.Integral.ImproperIntegralComparisonWanted.improper_integral_limit_comparison_test
statement: formalized
---

# Improper integrals

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/improper-integrals/index.html).

## Conditional convergence of the Dirichlet integral on $(1, \infty)$

The function
$x \mapsto \sin x / x$ is interval integrable on $[1, b]$ for every real $b \ge 1$, the integrals
$\int_1^b \frac{\sin x}{x}\,dx$ converge to a real limit as $b \to \infty$, and $\sin x / x$ is
not Lebesgue integrable on $(1, \infty)$.

## Sources

- W. Rudin, *Principles of Mathematical Analysis*, 3rd ed., Ch. 11, Exercise 15 (conditional convergence of the sine integral).

Stated but not proved: `MathlibExt.MeasureTheory.Integral.ImproperIntegralAbsoluteConditionalWanted.dirichlet_integral_conditionally_convergent` is written with `theorem_wanted` in [WantedExt/MeasureTheory/Integral/ImproperIntegralAbsoluteConditionalWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/Integral/ImproperIntegralAbsoluteConditionalWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/improper-integrals/index.html#dirichlet-integral-conditionally-converg).

## Comparison test for improper integrals

Let $a \in \mathbb{R}$ and let
$f, g : \mathbb{R} \to \mathbb{R}$ be interval integrable on $[a, b]$ for every $b \ge a$, with
$0 \le f(x) \le g(x)$ for all $x \ge a$. If $\int_a^b g(x)\,dx$ converges to a real limit as
$b \to \infty$, then $\int_a^b f(x)\,dx$ also converges to a real limit as $b \to \infty$.

## Sources

- https://mathbooks.unl.edu/Calculus/sec-5-11-comparison.html

Stated but not proved: `MathlibExt.MeasureTheory.Integral.ImproperIntegralComparisonWanted.improper_integral_comparison_test` is written with `theorem_wanted` in [WantedExt/MeasureTheory/Integral/ImproperIntegralComparisonWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/Integral/ImproperIntegralComparisonWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/improper-integrals/index.html#improper-integral-comparison-test).

## Limit comparison test for improper integrals

Let $a, L \in \mathbb{R}$
with $L \ne 0$, and let $f, g : \mathbb{R} \to \mathbb{R}$ be interval integrable on $[a, b]$ for
every $b \ge a$, with $f(x) > 0$ and $g(x) > 0$ for all $x \ge a$. If $f(x) / g(x) \to L$ as
$x \to \infty$, then $\int_a^b f(x)\,dx$ converges to a real limit as $b \to \infty$ if and
only if $\int_a^b g(x)\,dx$ converges to a real limit as $b \to \infty$.

## Sources

- T. Apostol, *Mathematical Analysis*, 2nd ed., §10.23 (limit comparison test).

Stated but not proved: `MathlibExt.MeasureTheory.Integral.ImproperIntegralComparisonWanted.improper_integral_limit_comparison_test` is written with `theorem_wanted` in [WantedExt/MeasureTheory/Integral/ImproperIntegralComparisonWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/Integral/ImproperIntegralComparisonWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/improper-integrals/index.html#improper-integral-limit-comparison-test).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Improper integrals](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/improper-integrals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/integration/improper-integrals)
