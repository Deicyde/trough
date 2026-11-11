---
declaration: section
origin: cited
lean: modulusOfContinuity, modulusOfContinuity_bddAbove, le_modulusOfContinuity, modulusOfContinuity_nonneg, modulusOfContinuity_mono, modulusOfContinuity_tendsto_zero
statement: formalized
proof: formalized
---

# Modulus of continuity

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html).

## Modulus of continuity

For a function $f : \mathbb{R} \to \mathbb{R}$, real numbers $a$
and $b$, and a scale $\eta \in \mathbb{R}$, the modulus of continuity of $f$ on $[a, b]$ at scale
$\eta$ is

$$\omega_f(\eta) = \sup \{|f(x) - f(y)| : x, y \in [a, b],\ |x - y| \le \eta\},$$

where the supremum is taken in $\mathbb{R}$ with the convention that it is $0$ when the set is
empty or not bounded above.

Formalized by `modulusOfContinuity`, a definition declared in [MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html#modulus-of-continuity).

## The set defining the modulus of continuity is bounded above

Let
$f : \mathbb{R} \to \mathbb{R}$ be continuous on $[a, b]$. Then for every $\eta \in \mathbb{R}$ the
set $\{|f(x) - f(y)| : x, y \in [a, b],\ |x - y| \le \eta\}$ is bounded above.

Formalized by `modulusOfContinuity_bddAbove`, a theorem declared in [MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html#modulus-of-continuity-bdd-above).

## The modulus of continuity bounds increments

Let $f : \mathbb{R} \to \mathbb{R}$ be
continuous on $[a, b]$, let $\eta \in \mathbb{R}$, and let $\omega_f(\eta)$ be the modulus of
continuity of $f$ on $[a, b]$ at scale $\eta$. For all $x, y \in [a, b]$ with $|x - y| \le \eta$,
we have $|f(x) - f(y)| \le \omega_f(\eta)$.

Formalized by `le_modulusOfContinuity`, a theorem declared in [MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html#le-modulus-of-continuity).

## Nonnegativity of the modulus of continuity

Let $a \le b$ and let
$f : \mathbb{R} \to \mathbb{R}$ be continuous on $[a, b]$. For every $\eta \ge 0$, the modulus of
continuity $\omega_f(\eta)$ of $f$ on $[a, b]$ at scale $\eta$ satisfies $0 \le \omega_f(\eta)$.

The defining set contains $|f(a) - f(a)| = 0$.

Formalized by `modulusOfContinuity_nonneg`, a theorem declared in [MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html#modulus-of-continuity-nonneg).

## Monotonicity of the modulus of continuity

Let $a \le b$, let
$f : \mathbb{R} \to \mathbb{R}$ be continuous on $[a, b]$, and write $\omega_f(\eta)$ for the
modulus of continuity of $f$ on $[a, b]$ at scale $\eta$. If $0 \le \eta_1 \le \eta_2$, then
$\omega_f(\eta_1) \le \omega_f(\eta_2)$.

A smaller scale takes the supremum over a smaller set of pairs.

Formalized by `modulusOfContinuity_mono`, a theorem declared in [MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html#modulus-of-continuity-mono).

## Theorem I (Modulus of continuity vanishes)

Let $a \le b$ and let
$f : \mathbb{R} \to \mathbb{R}$ be continuous on $[a, b]$. Then the modulus of continuity
$\omega_f(\eta)$ of $f$ on $[a, b]$ tends to $0$ as $\eta \to 0^+$.

Formalized by `modulusOfContinuity_tendsto_zero`, a theorem declared in [MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/MetricSpace/ModulusOfContinuity.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html#modulus-of-continuity-tendsto-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Modulus of continuity](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/modulus-of-continuity)
