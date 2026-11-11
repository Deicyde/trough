---
declaration: section
origin: cited
lean: StatMech.bernoulliMeasure, StatMech.bernoulliMeasure_eq, StatMech.bernoulliProductMeasure, StatMech.bernoulliProductMeasure_eq_gbernoulliLaw, StatMech.bernoulliProductMeasure.apply_singleton, StatMech.bernoulliProductMeasure.real_singleton, StatMech.bernoulliProductMeasure.real_eq_sum, StatMech.bernoulliProductMeasure.real_singleton_nonneg
statement: formalized
proof: formalized
---

# Bernoulli product measures and cylinder events

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html).

## Bernoulli distribution on the Booleans

The Bernoulli distribution on `Bool` with success probability `p`: mass `p` on `true` and
`1 - p` on `false`. This is Mathlib's `ProbabilityTheory.bernoulliMeasure true false p`, with the
parameter given as an `ℝ≥0` bounded by `1`.

Formalized by `StatMech.bernoulliMeasure`, a definition declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#bernoulli-measure).

## Bernoulli distribution agrees with the library Bernoulli measure

`bernoulliMeasure p hp` is Mathlib's `ProbabilityTheory.bernoulliMeasure true false p`.

Formalized by `StatMech.bernoulliMeasure_eq`, a lemma declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#bernoulli-measure-eq).

## Bernoulli product measure on configuration space

The Bernoulli product measure on `ConfigSpace E`: the coordinates are independent and each is
`true` with probability `p` (`Measure.infinitePi` of `bernoulliMeasure p hp`). See also Mathlib's
`ProbabilityTheory.setBernoulli`, the same product measure on `Set E`.

Formalized by `StatMech.bernoulliProductMeasure`, a definition declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#bernoulli-product-measure).

## Bernoulli product measure on bonds is the bond percolation law

On bond configurations `Sym2 V → Bool`, `bernoulliProductMeasure` is the bond percolation law
`MathlibExt.Probability.ProductBondPercolation.gbernoulliLaw`.

Formalized by `StatMech.bernoulliProductMeasure_eq_gbernoulliLaw`, a lemma declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#bernoulli-product-measure-eq-gbernoulli).

## Mass of a configuration under a finite Bernoulli product measure

For finite `E`, the mass of a configuration is the product of its coordinate masses.

Formalized by `StatMech.bernoulliProductMeasure.apply_singleton`, a theorem declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#apply-singleton).

## Mass of a configuration under a finite Bernoulli product measure, real form

For finite `E`, the mass of a configuration is the product of its coordinate masses.

Formalized by `StatMech.bernoulliProductMeasure.real_singleton`, a theorem declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-singleton).

## Probability of an event as a sum of configuration masses

For finite `E`, the probability of an event is the sum of the masses of its configurations.

Formalized by `StatMech.bernoulliProductMeasure.real_eq_sum`, a theorem declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-eq-sum).

## Nonnegativity of configuration masses

Configuration masses are nonnegative.

Formalized by `StatMech.bernoulliProductMeasure.real_singleton_nonneg`, a theorem declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-singleton-nonneg).

## Configuration masses sum to one

For finite `E`, the configuration masses sum to `1`.

Formalized by `StatMech.bernoulliProductMeasure.sum_real_singleton`, a theorem declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#sum-real-singleton).

## Log-modularity of Bernoulli product weights

The configuration weights of a Bernoulli product measure are log-modular:
`w(a) w(b) = w(a ⊔ b) w(a ⊓ b)`. In particular they satisfy the FKG lattice condition.

Formalized by `StatMech.bernoulliProductMeasure.real_singleton_logModular`, a theorem declared in [MathlibExt/Probability/Configuration/ProductMeasure.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/ProductMeasure.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-singleton-log-modular).

## Point masses of the Bernoulli distribution

The mass of a point under the Bernoulli distribution: `p` at `true`, `1 - p` at `false`.

Formalized by `StatMech.bernoulliMeasure_real_singleton`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#bernoulli-measure-real-singleton).

## Mass of a configuration on a finite index set is its product weight

On a finite index set, the mass of a configuration is its product weight `configWeight`.

Formalized by `StatMech.realSingleton_eq_configWeight`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-singleton-eq-config-weight).

## Bernoulli product measure of an event on a finite index set

On a finite index set, the Bernoulli product measure of an event is its weight `prob p`.

Formalized by `StatMech.finiteRealProb_eq_prob`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#finite-real-prob-eq-prob).

## Configuration patched from one configuration on a finite set and another off it

The configuration that agrees with `η` on the finite set `F` and with `ω` off `F`.

Formalized by `StatMech.extendOff`, a definition declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#extend-off).

## Events depending on finitely many coordinates are cylinders

An event whose indicator depends only on the coordinates in `F` is the cylinder over its
projection onto `F`.

Formalized by `StatMech.eq_cylinder_restrict_image`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#eq-cylinder-restrict-image).

## Bernoulli product measure of a cylinder event

The infinite Bernoulli product measure of a cylinder over `F` is the finite Bernoulli product
measure of its base.

Formalized by `StatMech.bernoulliProductMeasure_cylinder`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#bernoulli-product-measure-cylinder).

## Bernoulli product measure of a cylinder event, real-valued form

Real-valued form of `bernoulliProductMeasure_cylinder`.

Formalized by `StatMech.realProb_cylinder`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-prob-cylinder).

## Probability of a finitely dependent event as a finite weight

The probability of an event depending only on the coordinates in `F` is the finite weight
`prob p` of its projection onto `F`.

Formalized by `StatMech.realProb_cylinder_eq_prob`, a theorem declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-prob-cylinder-eq-prob).

## Probability of a finitely dependent event as a polynomial in $p$

The probability of an event depending only on the coordinates in `F`, as an explicit
polynomial in `p`.

Formalized by `StatMech.realProb_cylinder_eq_finsum`, a theorem declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#real-prob-cylinder-eq-finsum).

## Differentiability in $p$ of the probability of a cylinder event

The weight of the projection of an event onto finitely many coordinates is differentiable
in `p`.

Formalized by `StatMech.differentiable_realProb_cylinder`, a theorem declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#differentiable-real-prob-cylinder).

## Finite projections of increasing events are increasing

The projection of an increasing event onto finitely many coordinates is increasing.

Formalized by `StatMech.isIncreasing_restrict_image`, a lemma declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#is-increasing-restrict-image).

## Russo's formula

**Russo's formula** for an increasing event `A` projected onto finitely many coordinates `F`:
the derivative in `p` of its weight is the sum over `e ∈ F` of the weight of the event that `e`
is pivotal (L. Russo, 1981).

Formalized by `StatMech.hasDerivAt_realProb_cylinder_pivotal`, a theorem declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#has-deriv-at-real-prob-cylinder-pivotal).

## Russo's formula

**Russo's formula**, `deriv` form of `hasDerivAt_realProb_cylinder_pivotal`.

Formalized by `StatMech.deriv_realProb_cylinder_pivotal`, a theorem declared in [MathlibExt/Probability/Configuration/CylinderDeriv.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Configuration/CylinderDeriv.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html#deriv-real-prob-cylinder-pivotal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli product measures and cylinder events](https://deicyde.github.io/atlas-lean/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/random-fields/bernoulli-product-measures-and-cylinder-events)
