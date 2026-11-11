---
declaration: section
origin: cited
lean: OmegaCompletePartialOrder.ContinuousHom.ωScottContinuous_of_apply, OmegaCompletePartialOrder.ContinuousHom.curry, OmegaCompletePartialOrder.ContinuousHom.lfp, OmegaCompletePartialOrder.ContinuousHom.lfp_eq, OmegaCompletePartialOrder.ContinuousHom.lfp_le, OmegaCompletePartialOrder.ContinuousHom.lfp_ωScottContinuous, OmegaCompletePartialOrder.ContinuousHom.lfpHom
statement: formalized
proof: formalized
---

# Scott-continuous maps and least fixed points

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html).

## Scott continuity into a function space is checked pointwise

Let $\alpha$, $\beta$,
$\gamma$ be ω-complete partial orders, and let $g$ be a map from $\alpha$ to the ω-complete
partial order of Scott-continuous maps $\beta \to \gamma$, ordered pointwise. If for every
$b \in \beta$ the map $a \mapsto g(a)(b)$ is Scott-continuous, then $g$ is Scott-continuous.
Here a map is Scott-continuous when it is monotone and preserves suprema of ω-chains.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.ωScottContinuous_of_apply`, a theorem declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#scott-continuous-of-apply).

## Currying of Scott-continuous maps

Let $\alpha$, $\beta$, $\gamma$ be ω-complete partial
orders and let $f : \alpha \times \beta \to \gamma$ be a Scott-continuous map, that is, a map that
is monotone and preserves suprema of ω-chains. Its currying is the Scott-continuous map from
$\alpha$ to the ω-complete partial order of Scott-continuous maps $\beta \to \gamma$, ordered
pointwise, that sends $a$ to the map $b \mapsto f(a, b)$.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.curry`, a definition declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#curry).

## Least fixed point of a Scott-continuous map

Let $D$ be an ω-complete partial order with
a least element $\bot$, and let $f : D \to D$ be Scott-continuous, that is, monotone and
preserving suprema of ω-chains. The least fixed point $\operatorname{lfp} f$ of $f$ is the
supremum of the Kleene chain $\bot \le f(\bot) \le f(f(\bot)) \le \cdots$, whose $n$-th term is
the $n$-fold iterate $f^n(\bot)$.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.lfp`, a definition declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#lfp).

## The least fixed point is a fixed point

Let $D$ be an ω-complete partial order with a
least element $\bot$, and let $f : D \to D$ be Scott-continuous, that is, monotone and preserving
suprema of ω-chains. Then the least fixed point $\operatorname{lfp} f$ of $f$ satisfies
$f(\operatorname{lfp} f) = \operatorname{lfp} f$.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.lfp_eq`, a theorem declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#lfp-eq).

## The least fixed point lies below every prefixed point

Let $D$ be an ω-complete partial
order with a least element $\bot$, let $f : D \to D$ be Scott-continuous, that is, monotone and
preserving suprema of ω-chains, and let $\operatorname{lfp} f$ be the supremum of the Kleene
chain $\bot \le f(\bot) \le f(f(\bot)) \le \cdots$. If $a \in D$ satisfies $f(a) \le a$, then
$\operatorname{lfp} f \le a$.

Together with $f(\operatorname{lfp} f) = \operatorname{lfp} f$, this makes $\operatorname{lfp} f$
the least fixed point of $f$.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.lfp_le`, a theorem declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#lfp-le).

## Scott continuity of the least-fixed-point operator

Let $D$ be an ω-complete partial
order with a least element $\bot$. For a Scott-continuous map $f : D \to D$, that is, one that is
monotone and preserves suprema of ω-chains, let $\operatorname{lfp} f$ be its least fixed point.
The map $f \mapsto \operatorname{lfp} f$, from the ω-complete partial order of Scott-continuous
maps $D \to D$, ordered pointwise, to $D$, is Scott-continuous.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.lfp_ωScottContinuous`, a theorem declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#lfp-scott-continuous).

## The least-fixed-point operator as a Scott-continuous map

Let $D$ be an ω-complete
partial order with a least element $\bot$. The least-fixed-point operator, sending a
Scott-continuous map $f : D \to D$ to its least fixed point $\operatorname{lfp} f$, bundled as a
Scott-continuous map from the ω-complete partial order of Scott-continuous maps $D \to D$,
ordered pointwise, to $D$.

Formalized by `OmegaCompletePartialOrder.ContinuousHom.lfpHom`, a definition declared in [MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Order/OmegaCompletePartialOrder/ContinuousHom.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html#lfp-hom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Scott-continuous maps and least fixed points](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Order/fixed-points-domain-theory/scott-continuous-maps-and-least-fixed-points)
