---
declaration: section
origin: cited
lean: StatMech.harris_inequality, StatMech.ih_event_dependsOn_of_indicator, StatMech.ih_indicator_dependsOn_of_event, StatMech.ih_dependsOn_inter, StatMech.ih_dependsOn_iUnion, StatMech.ih_fill, StatMech.ih_fill_mono, StatMech.ih_section
statement: formalized
proof: formalized
---

# Harris inequality

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html).

## Harris inequality

The **Harris inequality** (Harris 1960): under the product Bernoulli(`p`) measure on a finite
configuration space, increasing events are positively correlated,
`P_p(A) * P_p(B) ≤ P_p(A ∩ B)`. No measurability hypothesis is needed since `E` is finite.
See also `IsUpperSet.le_card_inter_finset` (Harris–Kleitman, counting form).

Formalized by `StatMech.harris_inequality`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Harris.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Harris.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#harris-inequality).

## An event depends on the coordinates its indicator depends on

If the indicator of `A` depends only on the coordinates in `S` (Mathlib's `DependsOn`), so
does the event `A` (`StatMech.DependsOn`).

Formalized by `StatMech.ih_event_dependsOn_of_indicator`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-event-depends-on-of-indicator).

## Indicator of an event depends on the coordinates the event depends on

If the event `A` depends only on `S`, so does its indicator function.

Formalized by `StatMech.ih_indicator_dependsOn_of_event`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-indicator-depends-on-of-event).

## Events depending on a coordinate set are closed under intersection

Events depending only on `S` are closed under intersection.

Formalized by `StatMech.ih_dependsOn_inter`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-depends-on-inter).

## Events depending on a coordinate set are closed under unions

Events depending only on `S` are closed under arbitrary unions.

Formalized by `StatMech.ih_dependsOn_iUnion`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-depends-on-i-union).

## Filling a finite configuration with closed coordinates

The configuration on `E` equal to `η` on the finite set `F` and closed (`false`) off `F`.

Formalized by `StatMech.ih_fill`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-fill).

## Monotonicity of the closed filling map

`ih_fill F` is monotone.

Formalized by `StatMech.ih_fill_mono`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-fill-mono).

## Section of an event on a finite coordinate set

The section of an event `A` on `F`: the configurations `η` on `F` with `ih_fill F η ∈ A`.

Formalized by `StatMech.ih_section`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-section).

## Section of an increasing event is increasing

The section of an increasing event is increasing.

Formalized by `StatMech.ih_section_isIncreasing`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-section-is-increasing).

## Finitely dependent event is a cylinder over its section

An event depending only on the coordinates in `F` is the cylinder over its section on `F`.

Formalized by `StatMech.ih_eq_cylinder_of_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-eq-cylinder-of-depends-on).

## Harris inequality for finitely dependent increasing events

The **Harris inequality** on a countable configuration space for increasing events that
depend on finitely many coordinates: `P_p(A) * P_p(B) ≤ P_p(A ∩ B)`.

Formalized by `StatMech.ih_harris_of_finite_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-harris-of-finite-depends-on).

## Positive correlation passes to decreasing intersections

Positive correlation passes to limits of decreasing sequences of measurable events: if
`μ(A n) μ(B n) ≤ μ(A n ∩ B n)` for all `n`, the same holds for `⋂ n, A n` and `⋂ n, B n`.

Formalized by `StatMech.ih_harris_iInter_of_antitone`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-harris-i-inter-of-antitone).

## Continuity from above of a finite measure, real-valued form

Continuity from above of a finite measure, real-valued form: `μ.real (A n)` tends to
`μ.real (⋂ n, A n)` for a decreasing sequence of measurable sets.

Formalized by `StatMech.ih_tendsto_measureReal_iInter`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/InfiniteHarris.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html#ih-tendsto-measure-real-i-inter).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Harris inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/harris-fkg-bk/harris-inequality)
