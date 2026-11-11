---
declaration: section
origin: cited
lean: RiemannXi.riemannXi, RiemannXi.differentiable_riemannXi, RiemannXi.riemannXi_one_sub, RiemannXi.riemannXi_eq_mul_completedRiemannZeta, RiemannXi.riemannXi_ne_zero_of_one_le_re, RiemannXi.re_pos_of_riemannXi_eq_zero, RiemannXi.re_lt_one_of_riemannXi_eq_zero, RiemannXi.riemannXi_mem_strip
statement: formalized
proof: formalized
---

# Riemann xi function

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html).

## Riemann xi function

Let $\Lambda$ be the completed Riemann zeta function, the
meromorphic continuation of $\pi^{-s/2}\Gamma(s/2)\zeta(s)$, which has simple poles at
$s = 0$ and $s = 1$, and let $\Lambda_0$ be the entire function with
$\Lambda_0(s) = \Lambda(s) + \frac{1}{s} + \frac{1}{1 - s}$ for $s \ne 0, 1$. The Riemann
xi function is $\xi(s) = \frac{s(s - 1)}{2}\Lambda_0(s) + \frac{1}{2}$ for $s \in \mathbb{C}$.

Formalized by `RiemannXi.riemannXi`, a definition declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#riemann-xi).

## The Riemann xi function is entire

The Riemann xi function $\xi$ is complex
differentiable at every point of $\mathbb{C}$.

Formalized by `RiemannXi.differentiable_riemannXi`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#differentiable-riemann-xi).

## Functional equation of the Riemann xi function

Let $\xi$ be the Riemann xi function.
For every complex number $s$, $\xi(1 - s) = \xi(s)$.

Formalized by `RiemannXi.riemannXi_one_sub`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#riemann-xi-one-sub).

## The xi function in terms of the completed zeta function

Let $\xi$ be the Riemann xi
function and let $\Lambda$ be the completed Riemann zeta function, the meromorphic continuation
of $\pi^{-s/2}\Gamma(s/2)\zeta(s)$, which has simple poles at $s = 0$ and $s = 1$. For every
complex number $s$ with $s \ne 0$ and $s \ne 1$, $\xi(s) = \frac{s(s - 1)}{2}\Lambda(s)$.

Formalized by `RiemannXi.riemannXi_eq_mul_completedRiemannZeta`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#riemann-xi-eq-mul-completed-riemann-zeta).

## The xi function has no zeros with real part at least one

Let $\xi$ be the Riemann xi
function. For every complex number $s$ with $\operatorname{Re}(s) \ge 1$, $\xi(s) \ne 0$.

Formalized by `RiemannXi.riemannXi_ne_zero_of_one_le_re`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#riemann-xi-ne-zero-of-one-le-re).

## Zeros of the xi function have positive real part

Let $\xi$ be the Riemann xi
function. If $s$ is a complex number with $\xi(s) = 0$, then $\operatorname{Re}(s) > 0$.

Formalized by `RiemannXi.re_pos_of_riemannXi_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#re-pos-of-riemann-xi-eq-zero).

## Zeros of the xi function have real part less than one

Let $\xi$ be the Riemann xi
function. If $s$ is a complex number with $\xi(s) = 0$, then $\operatorname{Re}(s) < 1$.

Formalized by `RiemannXi.re_lt_one_of_riemannXi_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#re-lt-one-of-riemann-xi-eq-zero).

## Zeros of the xi function lie in the critical strip

Let $\xi$ be the Riemann xi
function. If $s$ is a complex number with $\xi(s) = 0$, then $0 < \operatorname{Re}(s) < 1$.

Formalized by `RiemannXi.riemannXi_mem_strip`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#riemann-xi-mem-strip).

## Basic properties of the Riemann xi function

The Riemann xi function $\xi$ is
entire, satisfies $\xi(1 - s) = \xi(s)$ for every complex number $s$, and every complex
number $s$ with $\xi(s) = 0$ satisfies $0 < \operatorname{Re}(s) < 1$.

Formalized by `RiemannXi.riemannXi_entire_functional_equation_and_critical_strip`, a theorem declared in [MathlibExt/NumberTheory/LSeries/RiemannXi.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/RiemannXi.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html#riemann-xi-entire-functional-equation-an).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riemann xi function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/riemann-xi-function)
