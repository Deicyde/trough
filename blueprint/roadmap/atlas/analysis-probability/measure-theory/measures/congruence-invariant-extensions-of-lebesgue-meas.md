---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.ScottishBook169Wanted.AreCongruent, MathlibExt.MeasureTheory.ScottishBook169Wanted.IsCongruenceInvariant, MathlibExt.MeasureTheory.ScottishBook169Wanted.IsCountablyAdditive, MathlibExt.MeasureTheory.ScottishBook169Wanted.CountablyAdditiveCongruenceClaim, MathlibExt.MeasureTheory.ScottishBook169Wanted.no_countably_additive_congruence_measure
statement: formalized
---

# Congruence-invariant extensions of Lebesgue measure

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html).

## Congruent plane sets

Two sets $E$ and $F$ in the Euclidean plane $\mathbb{R}^2$ are
congruent when some isometry of the plane onto itself maps $E$ onto $F$.

Formalized by `MathlibExt.MeasureTheory.ScottishBook169Wanted.AreCongruent`, a definition declared in [WantedExt/MeasureTheory/ScottishBook169Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScottishBook169Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html#are-congruent).

## Congruence-invariant set functions on the plane

A function $\mu$ that assigns to every
subset of the Euclidean plane $\mathbb{R}^2$ a value in $[0, \infty]$ is congruence invariant when
$\mu(E) = \mu(F)$ for all congruent plane sets $E$ and $F$.

Formalized by `MathlibExt.MeasureTheory.ScottishBook169Wanted.IsCongruenceInvariant`, a definition declared in [WantedExt/MeasureTheory/ScottishBook169Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScottishBook169Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html#is-congruence-invariant).

## Countably additive set function

`μ` is countably additive on pairwise-disjoint families. This is the
countably-additive reading of "additive" in Problem 169; the typescript
does not say whether finite or countable additivity is meant.

Formalized by `MathlibExt.MeasureTheory.ScottishBook169Wanted.IsCountablyAdditive`, a definition declared in [WantedExt/MeasureTheory/ScottishBook169Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScottishBook169Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html#is-countably-additive).

## Problem of a congruence-invariant countably additive plane measure

The countably additive reading of Problem 169: there is a function
`μ`, defined for all plane sets, equal on congruent sets, countably
additive, extending the Caratheodory linear measure (read as Lebesgue
volume on measurable sets), with values in `[0, +∞]` (automatic for
`ENNReal`).

Formalized by `MathlibExt.MeasureTheory.ScottishBook169Wanted.CountablyAdditiveCongruenceClaim`, a definition declared in [WantedExt/MeasureTheory/ScottishBook169Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScottishBook169Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html#countably-additive-congruence-claim).

## No countably additive congruence-invariant measure on all plane sets

The countably additive reading is false in ZFC. Sketch: let
`V₀ ⊆ [0,1]` meet each `ℚ`-coset of `ℝ` exactly once (Vitali selector)
and put `V = V₀ × [0,1]`. Enumerating `ℚ ∩ [-1,1]` as `(qₙ)`, the
translates `Tₙ = V + (qₙ, 0)` are pairwise disjoint, each congruent to
`V`, so all have the same mass `c = μ V`. Their union contains the unit
square `Q = [0,1] × [0,1]` and lies in the strip `[-1,2] × [0,1]` of
volume 3, so countable additivity and monotonicity give
`1 = μ Q ≤ μ U ≤ 3`, while countable additivity also gives
`μ U = ∑'ₙ c`, which is `0` if `c = 0` and `+∞` if `c > 0`, a
contradiction. Hence no such `μ` exists. This refutes the countably
additive formalization only. The typescript says bare "additive"; the
finite-additivity reading is Banach's 1923 theorem (a Banach measure: a
finitely additive, isometry-invariant function on all plane sets
extending Lebesgue measure), not this claim, and is not asserted here.

## Sources

- E. Szpilrajn, Problem 169 of the Scottish Book; typescript PDF p.78, printed p.75. Banach, Fund. Math. 4 (1923), 7-33.

Stated but not proved: `MathlibExt.MeasureTheory.ScottishBook169Wanted.no_countably_additive_congruence_measure` is written with `theorem_wanted` in [WantedExt/MeasureTheory/ScottishBook169Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/MeasureTheory/ScottishBook169Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html#no-countably-additive-congruence-measure).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Congruence-invariant extensions of Lebesgue measure](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/measures/congruence-invariant-extensions-of-lebesgue-meas)
