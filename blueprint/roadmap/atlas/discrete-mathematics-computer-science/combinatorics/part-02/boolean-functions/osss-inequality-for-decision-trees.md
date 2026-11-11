---
declaration: section
origin: cited
lean: StatMech.OSSS.weight, StatMech.OSSS.expect, StatMech.OSSS.IsProbWeight, StatMech.OSSS.pt, StatMech.OSSS.cov, StatMech.OSSS.var, StatMech.OSSS.infl, StatMech.OSSS.condMean
statement: formalized
proof: formalized
---

# OSSS inequality for decision trees

29 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html).

## Probability of a configuration under a product weight

The probability `∏ₑ ν e (ω e)` of the configuration `ω` under the product weight `ν`.

Formalized by `StatMech.OSSS.weight`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#weight).

## Expectation under a product weight

The expectation `∑_ω weight ν ω * g ω` of `g` under the product weight `ν`.

Formalized by `StatMech.OSSS.expect`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#expect).

## Product probability weight

`ν` is a product probability weight: each `ν e` is a probability vector on `Bool`.

Formalized by `StatMech.OSSS.IsProbWeight`, a structure declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#is-prob-weight).

## Point-mass weight on the Booleans

The point mass at `b`, as a weight on `Bool`. Replacing `ν e` by `pt b` conditions on `ω e = b`.

Formalized by `StatMech.OSSS.pt`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#pt).

## Covariance under a product weight

The covariance `𝔼[f g] - 𝔼[f] 𝔼[g]` under the product weight `ν`.

Formalized by `StatMech.OSSS.cov`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#cov).

## Variance under a product weight

The variance of `g` under the product weight `ν`.

Formalized by `StatMech.OSSS.var`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#var).

## Influence of a coordinate

The influence of coordinate `e` on `g`: `𝔼 |g(ω^{e ↦ 1}) - g(ω^{e ↦ 0})|`. For the indicator of
 an event this is the probability that `e` is pivotal (`infl_indicator_eq_pivotal`).

See also `BooleanCube.boolInfluence`, the uniform-measure influence `𝔼 ((f x - f x^{⊕i}) / 2)²`;
 for `0/1`-valued functions on the uniform cube the two differ by the factor `4`.

Formalized by `StatMech.OSSS.infl`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#infl).

## Conditional expectation given the other coordinates

The conditional expectation of `g` given all coordinates except `e`.

Formalized by `StatMech.OSSS.condMean`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#cond-mean).

## Binary decision tree

A binary decision tree on the variables `E`: a leaf outputs a Boolean value, and a node queries
 a variable and continues in the first subtree if it is `true` and in the second otherwise.

Formalized by `StatMech.OSSS.DecisionTree`, an inductive type declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#decision-tree).

## Boolean function computed by a decision tree

The Boolean function computed by the decision tree.

Formalized by `StatMech.OSSS.DecisionTree.eval`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#eval).

## Variables queried by a decision tree on an input

The set of variables the decision tree queries on input `ω`.

Formalized by `StatMech.OSSS.DecisionTree.queried`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#queried).

## Real-valued function computed by a decision tree

The function computed by the decision tree, as a `0/1`-valued real function.

Formalized by `StatMech.OSSS.DecisionTree.evalR`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#eval-r).

## Revealment of a variable by a decision tree

The revealment `δₑ(T)`: the probability that the decision tree `T` queries the variable `e`.

Formalized by `StatMech.OSSS.reveal`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#reveal).

## Configuration with one coordinate flipped

The configuration `ω` with coordinate `e` flipped.

See also `BooleanCube.flipCoord`, the same operation on `Fin n → Bool`.

Formalized by `StatMech.OSSS.flipAt`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#flip-at).

## Root step of the OSSS induction

Root step of the OSSS induction: the covariance of a function whose discrete derivative in `e`
 is bounded by `1` with the martingale increment `g - 𝔼[g | ω_{≠e}]` is at most `Infₑ(g)`.

Formalized by `StatMech.OSSS.claimA`, a lemma declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#claim-a).

## Subtree step of the OSSS induction

Subtree step of the OSSS induction: for `G` independent of the root variable `e`, the covariance
 with a tree rooted at `e` splits into the covariances with the two subtrees under the
 conditioned weights.

Formalized by `StatMech.OSSS.claimB`, a lemma declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#claim-b).

## OSSS covariance inequality over all product weights

The OSSS covariance inequality, stated for all product weights at once so that it can be proved
 by induction on the decision tree. Use `osss` for the usual argument order.

Formalized by `StatMech.OSSS.osss_cov`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 834](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#osss-cov).

## OSSS inequality

**OSSS inequality** (O'Donnell, Saks, Schramm, Servedio, *Every decision tree has an influential
 variable*, FOCS 2005): if the decision tree `T` computes `f`, then `Var(f) ≤ ∑ᵢ δᵢ(T) Infᵢ(f)`
 under every product probability measure.

Formalized by `StatMech.OSSS.osss_var`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 899](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L899). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#osss-var).

## OSSS inequality

**OSSS inequality**, covariance form (O'Donnell, Saks, Schramm, Servedio, *Every decision tree
 has an influential variable*, FOCS 2005; in this form Duminil-Copin, Raoufi, Tassion, Ann. of
 Math. 2019): if the decision tree `T` computes the Boolean function `f`, then for every real
 function `g` and every product probability measure, `Cov(f, g) ≤ ∑ᵢ δᵢ(T) Infᵢ(g)`, where
 `Infᵢ(g) = 𝔼 |g(ω^{i ↦ 1}) - g(ω^{i ↦ 0})|`.

This is `osss_cov` with the weight and its hypothesis as leading arguments.

Formalized by `StatMech.OSSS.osss`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#osss).

## Bernoulli product weight

The Bernoulli(`p`) product weight: every coordinate is `true` with probability `p`.

Formalized by `StatMech.OSSS.bernoulliWeight`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 915](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L915). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#bernoulli-weight).

## OSSS inequality for the Bernoulli product measure

The OSSS inequality for the Bernoulli(`p`) product measure.

Formalized by `StatMech.OSSS.osss_bernoulli`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 926](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L926). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#osss-bernoulli).

## Influence on an indicator is the pivotal probability

The influence of `e` on the indicator of `A` is the probability that `e` is pivotal for `A`.

Formalized by `StatMech.OSSS.infl_indicator_eq_pivotal`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 947](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L947). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#infl-indicator-eq-pivotal).

## Bernoulli product weight computes product-measure integrals

The Bernoulli(`p`) product weight computes integrals against
`StatMech.bernoulliProductMeasure`, the corresponding product probability measure.

Formalized by `StatMech.OSSS.expect_bernoulliWeight_eq_integral`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/OSSS.lean, line 959](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/OSSS.lean#L959). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#expect-bernoulli-weight-eq-integral).

## Decision tree querying a list of variables

The decision tree that queries the variables of `l` in order and then outputs the value of `φ`
 at the configuration that agrees with the answers on `l` and is `false` elsewhere. It computes
 `φ` when `φ` depends only on the variables in `l` (`eval_fullTree`).

Formalized by `StatMech.OSSS.Poincare.fullTree`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Poincare.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Poincare.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#full-tree).

## Function depending only on listed coordinates

`φ` depends only on the coordinates in the list `l`.

Formalized by `StatMech.OSSS.Poincare.InsensOutside`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Poincare.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Poincare.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#insens-outside).

## Decision tree querying every variable

The decision tree that queries every variable and then outputs the value of `φ`; it computes `φ`
 and has revealment `1` at every variable.

Formalized by `StatMech.OSSS.Poincare.fullTreeUniv`, a definition declared in [CSLibExt/Complexity/BooleanFunctions/Poincare.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Poincare.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#full-tree-univ).

## Poincaré inequality for Boolean functions under a product measure

Poincaré inequality for Boolean functions under a product measure: `Var(1_A) ≤ ∑ₑ Infₑ(1_A)`,
 where `Infₑ(1_A)` is the probability that `e` is pivotal. This is the OSSS inequality for the
 full decision tree; it is weaker than the Efron–Stein inequality `Var(f) ≤ ∑ₑ pₑ(1 - pₑ) 𝔼[(∂ₑ
 f)²]` by the factor `pₑ(1 - pₑ) ≤ 1/4`.

Formalized by `StatMech.OSSS.Poincare.poincare`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Poincare.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Poincare.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#poincare).

## Covariance form of the Poincaré inequality

Covariance form of `poincare`: `Cov(1_A, g) ≤ ∑ₑ Infₑ(g)` for every real function `g`.

Formalized by `StatMech.OSSS.Poincare.poincare_cov`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Poincare.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Poincare.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#poincare-cov).

## Poincaré inequality for the Bernoulli product measure

`poincare` for the Bernoulli(`p`) product measure.

Formalized by `StatMech.OSSS.Poincare.poincare_bernoulli`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/Poincare.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/BooleanFunctions/Poincare.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html#poincare-bernoulli).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: OSSS inequality for decision trees](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/boolean-functions/osss-inequality-for-decision-trees)
