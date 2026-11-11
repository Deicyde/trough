---
declaration: section
origin: cited
lean: StatMech.Sharpness.HasOddBoundary, StatMech.Sharpness.highTempSubgraphWeight, StatMech.Sharpness.edgeIndicatorCurrent, StatMech.Sharpness.sourcePair, StatMech.Sharpness.HighTempFirstExit, StatMech.Sharpness.highTempFirstExit, StatMech.Sharpness.highTempInternalEdges, StatMech.Sharpness.HighTempSwitchInput
statement: formalized
proof: formalized
---

# Simon–Lieb inequality

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html).

## Edge set with prescribed odd-degree vertices

The set of vertices of odd degree in the edge set `F` is exactly `A`.

Formalized by `StatMech.Sharpness.HasOddBoundary`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSources.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSources.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#has-odd-boundary).

## High-temperature weight of an edge set

The high-temperature weight `∏_{e ∈ F} tanh(βJ_e)` of an edge set.

Formalized by `StatMech.Sharpness.highTempSubgraphWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSources.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSources.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-subgraph-weight).

## Indicator current of an edge set

The current equal to `1` on the edges of `F` and `0` elsewhere.

Formalized by `StatMech.Sharpness.edgeIndicatorCurrent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSources.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSources.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#edge-indicator-current).

## Source pair $\{a\} \triangle \{b\}$

The source set `{a} ∆ {b}` (empty when `a = b`).

Formalized by `StatMech.Sharpness.sourcePair`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSwitching.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSwitching.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#source-pair).

## First-exit data for a high-temperature edge set

First-exit data for an edge set `K` with boundary `{o} ∆ {z}` and a set `S ∋ o`, `z ∉ S`: an
exit edge `xy` of `K` with `x ∈ S`, `y ∉ S`, and a subset `Q ⊆ K` of edges inside `S` with boundary
`{o} ∆ {x}` not containing `xy`.

Formalized by `StatMech.Sharpness.HighTempFirstExit`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSwitching.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSwitching.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-first-exit).

## Chosen first-exit data

A choice of first-exit data, from `exists_highTempFirstExit`.

Formalized by `StatMech.Sharpness.highTempFirstExit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSwitching.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSwitching.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-first-exit-2).

## Edges of a graph inside a set

The edges of `G` inside `S`.

Formalized by `StatMech.Sharpness.highTempInternalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-internal-edges).

## Input pair of the high-temperature switching

A pair of edge sets `(F, H)`, the input of the switching.

Formalized by `StatMech.Sharpness.HighTempSwitchInput`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-input).

## Output tuple of the high-temperature switching

A tuple `(x, y, A, B)` of an exit edge and two edge sets, the output of the switching.

Formalized by `StatMech.Sharpness.HighTempSwitchOutput`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-output).

## Valid switching inputs

Valid inputs: `F ⊆ E(G)` with boundary `{o} ∆ {z}` and `H` inside `S` with empty boundary.

Formalized by `StatMech.Sharpness.HighTempSwitchInput.Valid`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#valid).

## Valid switching outputs

Valid outputs: `x ∈ S`, `y ∉ S`, `A` inside `S` with boundary `{o} ∆ {x}`, and `B ⊆ E(G)` with
boundary `{y} ∆ {z}`.

Formalized by `StatMech.Sharpness.HighTempSwitchOutput.Valid`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#valid-2).

## Finite set of valid switching inputs

The finite set of valid inputs.

Formalized by `StatMech.Sharpness.highTempSwitchInputs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-inputs).

## Finite set of valid switching outputs

The finite set of valid outputs.

Formalized by `StatMech.Sharpness.highTempSwitchOutputs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-outputs).

## High-temperature switching map

The switching map: cut `F ∆ H` at its first exit from `S` and redistribute the pieces.

Formalized by `StatMech.Sharpness.highTempSwitch`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch).

## Switching map between valid inputs and outputs

The switching as a map between the finite sets of valid inputs and outputs.

Formalized by `StatMech.Sharpness.highTempSwitchMap`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-map).

## Weight of a switching input

The weight `∏_{e ∈ F} t_e ∏_{e ∈ H} t_e` of an input.

Formalized by `StatMech.Sharpness.highTempSwitchInputWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-input-weight).

## Weight of a switching output

The weight `∏_{e ∈ A} t_e · t_{xy} · ∏_{e ∈ B} t_e` of an output.

Formalized by `StatMech.Sharpness.highTempSwitchOutputWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-switch-output-weight).

## Edge sets with a given boundary

The edge sets `F ⊆ E` with boundary `A`.

Formalized by `StatMech.Sharpness.highTempSourceSubgraphs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-source-subgraphs).

## High-temperature source sum

The high-temperature source sum `∑_{F ⊆ E, ∂F = A} ∏_{e ∈ F} t_e`.

Formalized by `StatMech.Sharpness.highTempSourceSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#high-temp-source-sum).

## Two-point function with couplings

The two-point function `⟨σ_aσ_b⟩_{β,J}` (equal to `1` when `a = b`).

Formalized by `StatMech.Sharpness.twoPointJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#two-point-j).

## Simon–Lieb inequality on a finite graph

The Simon–Lieb inequality: for `β, J ≥ 0`, `o ∈ S` and `z ∉ S`, `⟨σ_oσ_z⟩ ≤ ∑_{x ∈ S} ∑_{y ∉ S}
tanh(βJ_{xy}) ⟨σ_oσ_x⟩_{J|S} ⟨σ_yσ_z⟩`. Reference: B. Simon, "Correlation inequalities and the decay
of correlations in ferromagnets", Comm. Math. Phys. 77 (1980) 111–126; E. H. Lieb, "A refinement of
Simon's correlation inequality", Comm. Math. Phys. 77 (1980) 127–135.

Formalized by `StatMech.Sharpness.twoPointJ_simon_finite`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 810](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L810). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#two-point-j-simon-finite).

## Simon–Lieb weight

The Simon–Lieb weight `tanh(βJ_{xy}) ⟨σ_oσ_x⟩_{J|S}`.

Formalized by `StatMech.Sharpness.simonWeightPair`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean, line 901](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempSimon.lean#L901). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#simon-weight-pair).

## Ghost-graph coupling with a site field

The coupling on `G` plus a ghost vertex: `J` on the edges of `G` and `H_x` on the edge `{x,
ghost}`.

Formalized by `StatMech.Sharpness.vertexGhostCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#vertex-ghost-coupling).

## Boltzmann weight with a site field

The Boltzmann weight `exp(β(∑_e J_e σ_e + ∑_x H_x σ_x))` with a site field `H`.

Formalized by `StatMech.Sharpness.vertexFieldWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#vertex-field-weight).

## Partition function with a site field

The partition function with site field `H`.

Formalized by `StatMech.Sharpness.vertexFieldZ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#vertex-field-z).

## Gibbs expectation with a site field

The Gibbs expectation with site field `H`.

Formalized by `StatMech.Sharpness.vertexFieldExpectation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#vertex-field-expectation).

## Two-point function with a site field

The two-point function `⟨σ_aσ_b⟩_{β,J,H}` with site field `H`.

Formalized by `StatMech.Sharpness.vertexFieldTwoPoint`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempVertexField.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#vertex-field-two-point).

## Simon weight of a boundary pair

The Simon weight `w(x, y) = tanh(βJ_{xy}) ⟨σ_oσ_x⟩_{J|S}`.

Formalized by `StatMech.Sharpness.simonWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonLieb.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonLieb.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#simon-weight).

## Simon–Lieb type inequality for a nonnegative two-point function

A Simon–Lieb type inequality for a nonnegative two-point function `τ`, root `o`, set `S`,
weights `w` and boundary targets `B`: `τ(o, z) ≤ ∑_{x ∈ S} ∑_{y ∈ B} w(x, y) τ(y, z)` for every `z ∉
S`.

Formalized by `StatMech.Sharpness.SimonLieb`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonLiebSelfImprovement.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonLiebSelfImprovement.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#simon-lieb).

## Simon constant of a weight function

The Simon constant `φ = ∑_{x ∈ S} ∑_{y ∈ B} w(x, y)`.

Formalized by `StatMech.Sharpness.simonConst`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonLiebSelfImprovement.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonLiebSelfImprovement.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#simon-const).

## Spin pair product as a bounded continuous function

The bounded continuous function `σ ↦ σ_x σ_y` on configuration space.

Formalized by `StatMech.Sharpness.spinPairBCF`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#spin-pair-bcf).

## Plus-state two-point function at zero field

The plus-state two-point function `⟨σ_xσ_y⟩^+_β` at zero field.

Formalized by `StatMech.Sharpness.plusCorr`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#plus-corr).

## Simon–Lieb boundary sum against a measure

The Simon–Lieb boundary sum `∑_{(x,y) ∈ ∂S} tanh β ⟨σ_0σ_x⟩_S ∫ σ_yσ_z dμ` for a measure `μ`.

Formalized by `StatMech.Sharpness.simonBoundaryIntegral`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#simon-boundary-integral).

## Simon–Lieb boundary sum in the plus state

The Simon–Lieb boundary sum `∑_{(x,y) ∈ ∂S} tanh β ⟨σ_0σ_x⟩_S ⟨σ_yσ_z⟩^+_β` in the plus state.

Formalized by `StatMech.Sharpness.simonBoundaryPlus`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SimonPlusLimit.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#simon-boundary-plus).

## Boundary edges of a finite volume

The edges touching `Λ` that are not inside `Λ`.

Formalized by `StatMech.Sharpness.plusBoundaryEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#plus-boundary-edges).

## Field induced by the plus boundary condition

The field on `x ∈ Λ` induced by the plus boundary condition: the number of edges from `x` to
sites outside `Λ`.

Formalized by `StatMech.Sharpness.plusBoundaryField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#plus-boundary-field).

## Unit coupling on the edges of a graph

The coupling equal to `1` on the edges of `G` and `0` elsewhere.

Formalized by `StatMech.Sharpness.unitEdgeCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#unit-edge-coupling).

## Underlying lattice sites of a subset of a volume

The sites of `ℤ^d` underlying a set `T` of sites of `Λ`.

Formalized by `StatMech.Sharpness.plusCutSites`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#plus-cut-sites).

## Identification of volume sites with lattice sites

The identification of `T` (as sites of `Λ`) with `plusCutSites T` (as sites of `ℤ^d`).

Formalized by `StatMech.Sharpness.plusCutVertexEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#plus-cut-vertex-equiv).

## Sites of a volume lying in a set

The sites of `Λ` that lie in `T`.

Formalized by `StatMech.Sharpness.sitesInVolume`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#sites-in-volume).

## Simon–Lieb inequality in the infinite-volume plus state

The Simon–Lieb inequality in the infinite-volume plus state: for `β ≥ 0`, a finite `T ∋ 0` and
`z ∉ T`, `⟨σ_0σ_z⟩^+_β ≤ ∑_{(x,y) ∈ ∂T} tanh β ⟨σ_0σ_x⟩_T ⟨σ_yσ_z⟩^+_β`. Reference: B. Simon,
"Correlation inequalities and the decay of correlations in ferromagnets", Comm. Math. Phys. 77
(1980) 111–126; E. H. Lieb, "A refinement of Simon's correlation inequality", Comm. Math. Phys. 77
(1980) 127–135.

Formalized by `StatMech.Sharpness.plusCorr_simon`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/HighTempPlusBox.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html#plus-corr-simon).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Simon–Lieb inequality](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/simon-lieb-inequality)
