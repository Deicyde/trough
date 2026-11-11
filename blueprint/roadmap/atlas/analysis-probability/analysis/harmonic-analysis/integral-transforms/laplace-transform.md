---
declaration: section
origin: cited
lean: LaplaceConvergent, laplace, HasLaplace, laplaceConvergent_of_norm_le_exp, laplaceConvergent_of_isBigO_exp, differentiableOn_laplace_of_norm_le_exp, differentiableOn_laplace_of_isBigO_exp
statement: formalized
proof: formalized
---

# Laplace transform

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html).

## Convergence of the Laplace transform

Let $E$ be a complex normed space,
$f : \mathbb{R} \to E$ and $s \in \mathbb{C}$. The Laplace transform of $f$ converges at $s$
when the function $t \mapsto e^{-st} f(t)$ is integrable on $(0, \infty)$ with respect to
Lebesgue measure.

Integrability here is absolute (Bochner) integrability, so conditionally convergent Laplace
integrals are not covered.

## Sources

- ATLAS NumberTheoryI Definition 16.9 introduces the Laplace transform for real-valued functions; here functions are complex-valued (or valued in a complex normed space), and the source's real-valued case is covered by coercion.

Formalized by `LaplaceConvergent`, a definition declared in [MathlibExt/Analysis/LaplaceTransform/Basic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/Basic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#laplace-convergent).

## The one-sided Laplace transform

Let $E$ be a complex normed space,
$f : \mathbb{R} \to E$ and $s \in \mathbb{C}$. The Laplace transform of $f$ at $s$ is the Bochner
integral $\int_{(0, \infty)} e^{-st} f(t)\,dt \in E$.

It is defined for every $s$, with no convergence hypothesis: where $t \mapsto e^{-st} f(t)$ is not
integrable on $(0, \infty)$, or when $E$ is not complete, the integral is $0$ by convention.
Convergence of the Laplace transform is a separate notion.

Formalized by `laplace`, a definition declared in [MathlibExt/Analysis/LaplaceTransform/Basic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/Basic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#laplace).

## Laplace transform with a given value

Let $E$ be a complex normed space,
$f : \mathbb{R} \to E$, $s \in \mathbb{C}$ and $v \in E$. Then $f$ has Laplace transform $v$ at
$s$ when the Laplace transform of $f$ converges at $s$, that is, $t \mapsto e^{-st} f(t)$ is
integrable on $(0, \infty)$, and the Bochner integral $\int_{(0, \infty)} e^{-st} f(t)\,dt$
equals $v$; as usual this integral is taken to be $0$ when $E$ is not complete.

Formalized by `HasLaplace`, a definition declared in [MathlibExt/Analysis/LaplaceTransform/Basic.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/Basic.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#has-laplace).

## Convergence of the Laplace transform under an exponential bound

Let $E$ be a complex
normed space, $f : \mathbb{R} \to E$ almost everywhere strongly measurable on $(0, \infty)$, and
$a, C \in \mathbb{R}$ with $C \ge 0$ such that $\|f(t)\| \le C e^{a t}$ for all $t \ge 0$. Then for
every $s \in \mathbb{C}$ with $\operatorname{Re} s > a$ the Laplace transform of $f$ converges at
$s$, that is, $t \mapsto e^{-st} f(t)$ is integrable on $(0, \infty)$.

Formalized by `laplaceConvergent_of_norm_le_exp`, a theorem declared in [MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#laplace-convergent-of-norm-le-exp).

## Convergence of the Laplace transform under exponential growth

Let $E$ be a complex
normed space, $a \in \mathbb{R}$, and $f : \mathbb{R} \to E$ locally integrable on $[0, \infty)$
with $\|f(t)\| = O(e^{a t})$ as $t \to \infty$. Then for every $s \in \mathbb{C}$ with
$\operatorname{Re} s > a$ the Laplace transform of $f$ converges at $s$, that is,
$t \mapsto e^{-st} f(t)$ is integrable on $(0, \infty)$.

Local integrability on $[0, \infty)$, not only on $(0, \infty)$, is needed: $f(t) = 1/t$ is
continuous on $(0, \infty)$ and bounded at infinity, but not integrable near $0$.

## Sources

- ATLAS NumberTheoryI N320 (Sutherland, 18.785 Number Theory I, Lecture 16); a corrected, strengthened-premise formalization of the intended convergence claim, since the source's piecewise continuity on the open ray does not give integrability near 0. This is not a literal proof of the under-specified source wording.

Formalized by `laplaceConvergent_of_isBigO_exp`, a theorem declared in [MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#laplace-convergent-of-is-big-o-exp).

## Holomorphy of the Laplace transform under an exponential bound

Let $E$ be a complex
Banach space, $f : \mathbb{R} \to E$ almost everywhere strongly measurable on $(0, \infty)$, and
$a, C \in \mathbb{R}$ with $C \ge 0$ such that $\|f(t)\| \le C e^{a t}$ for all $t \ge 0$. Then the
Laplace transform $s \mapsto \int_{(0, \infty)} e^{-st} f(t)\,dt$ is complex differentiable at
every point of the half-plane $\{s \in \mathbb{C} : \operatorname{Re} s > a\}$.

Formalized by `differentiableOn_laplace_of_norm_le_exp`, a theorem declared in [MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#differentiable-on-laplace-of-norm-le-exp).

## Holomorphy of the Laplace transform under exponential growth

Let $E$ be a complex
Banach space, $a \in \mathbb{R}$, and $f : \mathbb{R} \to E$ locally integrable on $[0, \infty)$
with $\|f(t)\| = O(e^{a t})$ as $t \to \infty$. Then the Laplace transform
$s \mapsto \int_{(0, \infty)} e^{-st} f(t)\,dt$ is complex differentiable at every point of the
half-plane $\{s \in \mathbb{C} : \operatorname{Re} s > a\}$.

Local integrability on $[0, \infty)$, not only on $(0, \infty)$, is what makes the Laplace
integral converge on this half-plane: $f(t) = 1/t$ is continuous on $(0, \infty)$ and bounded at
infinity, but not integrable near $0$, so its Laplace integral diverges for every $s$.

## Sources

- ATLAS NumberTheoryI N320 (Sutherland, 18.785 Number Theory I, Lecture 16); a corrected, strengthened-premise formalization of the intended holomorphy claim, since the source's piecewise continuity on the open ray does not give integrability near 0. This is not a literal proof of the under-specified source wording.

Formalized by `differentiableOn_laplace_of_isBigO_exp`, a theorem declared in [MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/LaplaceTransform/ExponentialBound.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html#differentiable-on-laplace-of-is-big-o-ex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Laplace transform](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/harmonic-analysis/integral-transforms/laplace-transform)
