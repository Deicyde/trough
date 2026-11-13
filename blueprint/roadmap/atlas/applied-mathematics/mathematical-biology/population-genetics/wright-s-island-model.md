---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.IslandModel.islandStep, MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium, MathlibExt.Biology.PopulationGenetics.IslandModel.islandFactor_mem_Ico, MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium_denom_pos, MathlibExt.Biology.PopulationGenetics.IslandModel.islandStep_islandEquilibrium, MathlibExt.Biology.PopulationGenetics.IslandModel.eq_islandEquilibrium_of_islandStep_eq, MathlibExt.Biology.PopulationGenetics.IslandModel.islandStep_iterate_sub, MathlibExt.Biology.PopulationGenetics.IslandModel.tendsto_islandStep_iterate
statement: formalized
proof: formalized
---

# Wright's island model

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html).

## Identity-by-descent recursion in Wright's island model

One generation of Wright's island-model identity-by-descent recursion for a deme of `M`
gene copies (`M = 2N` for `N` diploids) receiving a fraction `m` of migrants from an infinite
pool: `F' = (1 - m) ^ 2 * (1 / M + (1 - 1 / M) * F)`. Biologically meaningful for `M ≥ 2`
and `0 ≤ m ≤ 1`; `M = 1` is an algebraic extension (no pair of distinct copies exists), and at
`M = 0` Lean's `1 / 0 = 0` gives a junk value.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-step).

## Equilibrium $F_{ST}$ of Wright's island model

The equilibrium identity-by-descent probability (Wright's `F_ST`) of the island model:
`F* = (1 - m) ^ 2 / (M - (M - 1) (1 - m) ^ 2)`. Biologically meaningful for `M ≥ 2` and
`0 ≤ m ≤ 1`; the denominator is positive already for `M ≥ 1` (`islandEquilibrium_denom_pos`),
where `M = 1` is an algebraic extension.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium`, a definition declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-equilibrium).

## Island-model contraction factor lies in (0, 1)

For `M ≥ 1` and `0 ≤ m ≤ 1`, the per-generation contraction factor
`(1 - m) ^ 2 (1 - 1 / M)` lies in `[0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandFactor_mem_Ico`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-factor-mem-ico).

## Positivity of the island-model equilibrium denominator

The denominator `M - (M - 1) (1 - m) ^ 2` of the equilibrium is positive (at least `1`) for
`M ≥ 1` and `0 ≤ m ≤ 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium_denom_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-equilibrium-denom-pos).

## Island-model equilibrium is a fixed point of the recursion

`F*` is a fixed point of the island-model recursion.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandStep_islandEquilibrium`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-step-island-equilibrium).

## Uniqueness of the island-model fixed point

`F*` is the only fixed point of the island-model recursion.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.eq_islandEquilibrium_of_islandStep_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#eq-island-equilibrium-of-island-step-eq).

## Geometric approach to equilibrium

After `t` generations,
`F_t - F* = ((1 - m) ^ 2 (1 - 1 / M)) ^ t (F_0 - F*)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandStep_iterate_sub`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-step-iterate-sub).

## Convergence to equilibrium

For `M ≥ 1` and `0 ≤ m ≤ 1`, the island-model recursion
converges to `F*` from every initial value `F₀`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.tendsto_islandStep_iterate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#tendsto-island-step-iterate).

## Island-model equilibrium lies in (0, 1)

The equilibrium identity-by-descent probability lies in `[0, 1]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium_mem_Icc`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-equilibrium-mem-icc).

## Island-model equilibrium is below one under migration

With migration (`0 < m ≤ 1`) the equilibrium identity-by-descent probability lies in
`[0, 1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium_mem_Ico`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-equilibrium-mem-ico).

## Complete identity by descent in isolated demes

Isolated demes (`m = 0`): the equilibrium is complete identity by descent, `F* = 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.islandEquilibrium_zero_right`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#island-equilibrium-zero-right).

## Wright's `F_ST = 1 / (1 + 4 N m)` (Wright 1931)

For demes of `N` diploids (`M = 2N`
gene copies) and migration fraction `m = κ / (4N)`, so that `4 N m = κ` is held fixed, the
equilibrium `F*` tends to `1 / (1 + κ)` as `N → ∞`.

Formalized by `MathlibExt.Biology.PopulationGenetics.IslandModel.tendsto_islandEquilibrium`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/IslandModel.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/IslandModel.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html#tendsto-island-equilibrium).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wright's island model](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-s-island-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/wright-s-island-model)
