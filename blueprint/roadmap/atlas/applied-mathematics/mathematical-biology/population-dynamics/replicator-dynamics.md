---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.Replicator.meanFitness, MathlibExt.Biology.Dynamics.Replicator.IsSolution, MathlibExt.Biology.Dynamics.Replicator.IsRestPoint, MathlibExt.Biology.Dynamics.Replicator.isRestPoint_iff, MathlibExt.Biology.Dynamics.Replicator.IsSolution.hasDerivAt_sum, MathlibExt.Biology.Dynamics.Replicator.IsSolution.sum_eq_one, MathlibExt.Biology.Dynamics.Replicator.IsSolution.eq_zero_of_eq_zero, MathlibExt.Biology.Dynamics.Replicator.IsSolution.pos_of_pos
statement: formalized
proof: formalized
---

# Replicator dynamics

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html).

## Replicator

## Mean fitness of a population state

The mean fitness `f̄(x) = ∑ i, x i * f x i` of the population state `x` for the fitness
function `f`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.meanFitness`, a definition declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#mean-fitness).

## Solution of the replicator equation

`x` solves the replicator equation `x_i' = x_i (f_i(x) - f̄(x))` for all times `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution`, a structure declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#is-solution).

## Rest point of the replicator equation

`x` is a rest point of the replicator equation: `x_i (f_i(x) - f̄(x)) = 0` for all `i`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsRestPoint`, a definition declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#is-rest-point).

## Rest points in the interior are equalizers

If every strategy is present (`x i > 0`),
then `x` is a rest point iff every strategy has fitness equal to the mean fitness.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.isRestPoint_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#is-rest-point-iff).

## Evolution of the total frequency under replicator dynamics

The total frequency `∑ x_i` evolves by `(∑ x_i)' = f̄(x) (1 - ∑ x_i)`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.hasDerivAt_sum`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#has-deriv-at-sum).

## Invariance of the simplex hyperplane

For continuous fitness `f`, a solution with
`∑ x_i(0) = 1` satisfies `∑ x_i(t) = 1` for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.sum_eq_one`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#sum-eq-one).

## Invariance of the faces of the simplex

For continuous fitness `f`, a strategy absent
at time `0` (`x_i(0) = 0`) stays absent for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.eq_zero_of_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#eq-zero-of-eq-zero).

## Present strategies stay present

For continuous fitness `f`, a strategy with positive
frequency at time `0` has positive frequency for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.pos_of_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#pos-of-pos).

## Invariance of the simplex (Hofbauer–Sigmund 1998, §7.1)

For continuous fitness `f`, a
solution starting in the standard simplex (`x i ≥ 0` for all `i` and `∑ i, x i = 1`) stays in
it for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.mem_simplex`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/Replicator.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#mem-simplex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Replicator dynamics](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-dynamics/replicator-dynamics)
