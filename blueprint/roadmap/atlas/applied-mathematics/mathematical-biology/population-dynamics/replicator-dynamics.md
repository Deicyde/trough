---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.Replicator.meanFitness, MathlibExt.Biology.Dynamics.Replicator.IsSolution, MathlibExt.Biology.Dynamics.Replicator.IsRestPoint, MathlibExt.Biology.Dynamics.Replicator.isRestPoint_iff, MathlibExt.Biology.Dynamics.Replicator.IsSolution.hasDerivAt_sum, MathlibExt.Biology.Dynamics.Replicator.IsSolution.sum_eq_one, MathlibExt.Biology.Dynamics.Replicator.IsSolution.eq_zero_of_eq_zero, MathlibExt.Biology.Dynamics.Replicator.IsSolution.pos_of_pos
statement: formalized
proof: formalized
---

# Replicator dynamics

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html).

## Replicator

## Mean fitness of a population state

The mean fitness `f̄(x) = ∑ i, x i * f x i` of the population state `x` for the fitness
function `f`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.meanFitness`, a definition declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#mean-fitness).

## Solution of the replicator equation

`x` solves the replicator equation `x_i' = x_i (f_i(x) - f̄(x))` for all times `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution`, a structure declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#is-solution).

## Rest point of the replicator equation

`x` is a rest point of the replicator equation: `x_i (f_i(x) - f̄(x)) = 0` for all `i`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsRestPoint`, a definition declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#is-rest-point).

## Rest points in the interior are equalizers

If every strategy is present (`x i > 0`),
then `x` is a rest point iff every strategy has fitness equal to the mean fitness.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.isRestPoint_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#is-rest-point-iff).

## Evolution of the total frequency under replicator dynamics

The total frequency `∑ x_i` evolves by `(∑ x_i)' = f̄(x) (1 - ∑ x_i)`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.hasDerivAt_sum`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#has-deriv-at-sum).

## Invariance of the simplex hyperplane

For continuous fitness `f`, a solution with
`∑ x_i(0) = 1` satisfies `∑ x_i(t) = 1` for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.sum_eq_one`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#sum-eq-one).

## Invariance of the faces of the simplex

For continuous fitness `f`, a strategy absent
at time `0` (`x_i(0) = 0`) stays absent for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.eq_zero_of_eq_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#eq-zero-of-eq-zero).

## Present strategies stay present

For continuous fitness `f`, a strategy with positive
frequency at time `0` has positive frequency for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.pos_of_pos`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#pos-of-pos).

## Invariance of the simplex (Hofbauer–Sigmund 1998, §7.1)

For continuous fitness `f`, a
solution starting in the standard simplex (`x i ≥ 0` for all `i` and `∑ i, x i = 1`) stays in
it for all `t ≥ 0`.

Formalized by `MathlibExt.Biology.Dynamics.Replicator.IsSolution.mem_simplex`, a theorem declared in [MathlibExt/Biology/Dynamics/Replicator.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Dynamics/Replicator.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html#mem-simplex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Replicator dynamics](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-dynamics/replicator-dynamics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-dynamics/replicator-dynamics)
