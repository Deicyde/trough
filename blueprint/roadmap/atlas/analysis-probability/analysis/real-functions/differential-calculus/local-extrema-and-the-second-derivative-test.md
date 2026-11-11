---
declaration: section
origin: cited
lean: IsStrictLocalMin, IsStrictLocalMax, IsStrictLocalMin.isLocalMin, IsStrictLocalMax.isLocalMax, IsStrictLocalMin.neg, IsStrictLocalMax.neg, isStrictLocalMin_of_deriv_deriv_pos, isStrictLocalMax_of_deriv_deriv_neg
statement: formalized
proof: formalized
---

# Local extrema and the second-derivative test

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html).

## Strict local minimum

Let $f \colon X \to Y$ be a function from a topological space
$X$ to a set $Y$ equipped with a relation $<$. Then $f$ has a strict local minimum at a point
$a \in X$ if $f(a) < f(x)$ for all $x \ne a$ in some neighborhood of $a$.

This strengthens the usual (non-strict) notion of local minimum: the inequality is strict and
the point $a$ itself is excluded.

Formalized by `IsStrictLocalMin`, a definition declared in [MathlibExt/Topology/Order/LocalExtr.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Order/LocalExtr.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#is-strict-local-min).

## Strict local maximum

Let $f \colon X \to Y$ be a function from a topological space
$X$ to a set $Y$ equipped with a relation $<$. Then $f$ has a strict local maximum at a point
$a \in X$ if $f(x) < f(a)$ for all $x \ne a$ in some neighborhood of $a$.

Formalized by `IsStrictLocalMax`, a definition declared in [MathlibExt/Topology/Order/LocalExtr.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Order/LocalExtr.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#is-strict-local-max).

## A strict local minimum is a local minimum

Let $f \colon X \to Y$ be a function from a
topological space $X$ to a preordered set $Y$. If $f$ has a strict local minimum at $a \in X$,
then $f$ has a local minimum at $a$, that is, $f(a) \le f(x)$ for all $x$ in some neighborhood
of $a$.

Formalized by `IsStrictLocalMin.isLocalMin`, a theorem declared in [MathlibExt/Topology/Order/LocalExtr.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Order/LocalExtr.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#is-local-min).

## A strict local maximum is a local maximum

Let $f \colon X \to Y$ be a function from a
topological space $X$ to a preordered set $Y$. If $f$ has a strict local maximum at $a \in X$,
then $f$ has a local maximum at $a$, that is, $f(x) \le f(a)$ for all $x$ in some neighborhood
of $a$.

Formalized by `IsStrictLocalMax.isLocalMax`, a theorem declared in [MathlibExt/Topology/Order/LocalExtr.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Order/LocalExtr.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#is-local-max).

## Negation turns a strict local minimum into a strict local maximum

Let $X$ be a
topological space and let $Y$ be an additive group with a relation $<$ such that addition on
the left and addition on the right are strictly monotone. If $f \colon X \to Y$ has a strict
local minimum at $a \in X$, then $x \mapsto -f(x)$ has a strict local maximum at $a$.

Formalized by `IsStrictLocalMin.neg`, a theorem declared in [MathlibExt/Topology/Order/LocalExtr.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Order/LocalExtr.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#neg).

## Negation turns a strict local maximum into a strict local minimum

Let $X$ be a
topological space and let $Y$ be an additive group with a relation $<$ such that addition on
the left and addition on the right are strictly monotone. If $f \colon X \to Y$ has a strict
local maximum at $a \in X$, then $x \mapsto -f(x)$ has a strict local minimum at $a$.

Formalized by `IsStrictLocalMax.neg`, a theorem declared in [MathlibExt/Topology/Order/LocalExtr.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Order/LocalExtr.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#neg-2).

## Strict second-derivative test, minimum version

Let $f : \mathbb{R} \to \mathbb{R}$ and
$x_0 \in \mathbb{R}$. If $f''(x_0) > 0$, $f'(x_0) = 0$, and $f$ is continuous at $x_0$, then $f$
has a strict local minimum at $x_0$.

Formalized by `isStrictLocalMin_of_deriv_deriv_pos`, a theorem declared in [MathlibExt/Analysis/Calculus/StrictSecondDerivativeTest.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/StrictSecondDerivativeTest.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#is-strict-local-min-of-deriv-deriv-pos).

## Strict second-derivative test, maximum version

Let $f : \mathbb{R} \to \mathbb{R}$ and
$x_0 \in \mathbb{R}$. If $f''(x_0) < 0$, $f'(x_0) = 0$, and $f$ is continuous at $x_0$, then $f$
has a strict local maximum at $x_0$.

This is the minimum version applied to $-f$.

Formalized by `isStrictLocalMax_of_deriv_deriv_neg`, a theorem declared in [MathlibExt/Analysis/Calculus/StrictSecondDerivativeTest.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/StrictSecondDerivativeTest.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html#is-strict-local-max-of-deriv-deriv-neg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local extrema and the second-derivative test](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/differential-calculus/local-extrema-and-the-second-derivative-test)
