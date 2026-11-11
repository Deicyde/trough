---
declaration: section
origin: cited
lean: MetaMathlibExt.ekeland_variational_principle_general, MetaMathlibExt.ekeland_variational_principle, MetaMathlibExt.caristi_fixedPoint
statement: formalized
proof: formalized
---

# Ekeland variational principle

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/ekeland-variational-principle/index.html).

## Ekeland variational principle without a nonemptiness assumption

Let $(X, d)$ be a complete
metric space, let $f : X \to \mathbb{R}$ be lower semicontinuous and bounded below, and let
$\varepsilon > 0$. If $x_0 \in X$ satisfies $f(x_0) \le f(x) + \varepsilon$ for every $x \in X$,
then there is $x_\varepsilon \in X$ with $f(x_\varepsilon) \le f(x_0)$,
$d(x_\varepsilon, x_0) \le 1$, and $f(x_\varepsilon) < f(y) + \varepsilon\, d(x_\varepsilon, y)$
for every $y \ne x_\varepsilon$.

The space $X$ is not separately assumed nonempty, since the point $x_0$ already lies in it.

Formalized by `MetaMathlibExt.ekeland_variational_principle_general`, a theorem declared in [MathlibExt/Analysis/Variational/EkelandCaristi.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Variational/EkelandCaristi.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/ekeland-variational-principle/index.html#ekeland-variational-principle-general).

## Ekeland variational principle

Let $(X, d)$ be a nonempty complete metric space, let
$f : X \to \mathbb{R}$ be lower semicontinuous and bounded below, and let $\varepsilon > 0$. If
$x_0 \in X$ satisfies $f(x_0) \le f(x) + \varepsilon$ for every $x \in X$, then there is
$x_\varepsilon \in X$ with $f(x_\varepsilon) \le f(x_0)$, $d(x_\varepsilon, x_0) \le 1$, and
$f(x_\varepsilon) < f(y) + \varepsilon\, d(x_\varepsilon, y)$ for every $y \ne x_\varepsilon$.

## Sources

- I. Ekeland, J. Math. Anal. Appl. 47 (1974), 324-353, DOI 10.1016/0022-247X(74)90025-0. It follows from `ekeland_variational_principle_general`; the instance `[Nonempty X]` is unused and keeps the source's shape.

Formalized by `MetaMathlibExt.ekeland_variational_principle`, a theorem declared in [MathlibExt/Analysis/Variational/EkelandCaristi.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Variational/EkelandCaristi.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/ekeland-variational-principle/index.html#ekeland-variational-principle).

## Caristi fixed-point theorem

Let $(X, d)$ be a nonempty complete metric space and let
$\varphi : X \to \mathbb{R}$ be lower semicontinuous and bounded below. If a map $T : X \to X$
satisfies $d(x, T x) \le \varphi(x) - \varphi(T x)$ for every $x \in X$, then $T$ has a fixed
point: there is $x \in X$ with $T x = x$.

## Sources

- J. Caristi, Trans. Amer. Math. Soc. 215 (1976), 241-251, DOI 10.1090/S0002-9947-1976-0394329-4.

Formalized by `MetaMathlibExt.caristi_fixedPoint`, a theorem declared in [MathlibExt/Analysis/Variational/EkelandCaristi.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Variational/EkelandCaristi.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/ekeland-variational-principle/index.html#caristi-fixed-point).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ekeland variational principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/ekeland-variational-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/ekeland-variational-principle)
