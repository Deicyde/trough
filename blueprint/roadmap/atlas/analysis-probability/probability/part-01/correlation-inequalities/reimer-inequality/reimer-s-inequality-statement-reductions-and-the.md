---
declaration: section
origin: cited
lean: StatMech.ReimerWprobCore, StatMech.reimer_wprob_general_of_core, StatMech.reimer_inequality_of_core, StatMech.reimer_wprob_zero, StatMech.flipCfg, StatMech.flipEquiv, StatMech.bk_wprob_decreasing, StatMech.bk_inequality_decreasing
statement: formalized
proof: formalized
---

# Reimer's inequality: statement, reductions, and the monotone cases

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html).

## Reimer's inequality

**Reimer's inequality** (the van den Berg–Kesten conjecture, proved by Reimer 2000) for
product probability weights on `Fin n`: for every `n`, every weight `φ` with `φ ≥ 0` and
`φ i false + φ i true = 1`, and all events `A, B`, `wprob φ (A □ B) ≤ wprob φ A * wprob φ B`.

Formalized by `StatMech.ReimerWprobCore`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#reimer-wprob-core).

## Reimer's inequality for product weights, assuming the core case

Reimer's inequality for product probability weights on any finite set, assuming
`ReimerWprobCore`.

Formalized by `StatMech.reimer_wprob_general_of_core`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#reimer-wprob-general-of-core).

## Reimer's inequality for Bernoulli measures, assuming the core case

Reimer's inequality `P_p(A □ B) ≤ P_p(A) * P_p(B)` for all events under the product
Bernoulli measure on a finite set, **assuming** `ReimerWprobCore`.

Formalized by `StatMech.reimer_inequality_of_core`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#reimer-inequality-of-core).

## Reimer's inequality on the one-point configuration space

Reimer's inequality on the one-point configuration space `ConfigSpace (Fin 0)`.

Formalized by `StatMech.reimer_wprob_zero`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#reimer-wprob-zero).

## Flipping every coordinate of a configuration

The configuration with every coordinate flipped, `x ↦ !(ω x)`.

Formalized by `StatMech.flipCfg`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#flip-cfg).

## Coordinate flip as an involutive equivalence

Flipping all coordinates, as an involutive equivalence of `ConfigSpace E`.

Formalized by `StatMech.flipEquiv`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#flip-equiv).

## BK inequality for decreasing events under product weights

The BK inequality for two decreasing events under a product probability weight, obtained
from `StatMech.bk_wprob_general` by flipping all coordinates.

Formalized by `StatMech.bk_wprob_decreasing`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#bk-wprob-decreasing).

## BK inequality for decreasing events

The **BK inequality for decreasing events**: under the product Bernoulli(`p`) measure on a
finite set, `P_p(A □ B) ≤ P_p(A) * P_p(B)` for decreasing `A, B`.

Formalized by `StatMech.bk_inequality_decreasing`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/Reimer.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CorrelationInequalities/Reimer.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html#bk-inequality-decreasing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reimer's inequality: statement, reductions, and the monotone cases](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality/reimer-s-inequality-statement-reductions-and-the)
