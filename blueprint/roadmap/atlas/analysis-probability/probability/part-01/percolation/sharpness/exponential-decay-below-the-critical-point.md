---
declaration: section
origin: cited
lean: StatMech.Percolation.w1, StatMech.Percolation.W, StatMech.Percolation.wsum, StatMech.Percolation.clusterWithin, StatMech.Percolation.incidentWithin, StatMech.Percolation.clusterEvent, StatMech.Percolation.incidentWithinFinset, StatMech.Percolation.exploration_decomposition
statement: formalized
proof: formalized
---

# Exponential decay below the critical point

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html).

## Bernoulli weight of a single edge

The Bernoulli(`p`) weight of a single edge state: `p` for open, `1 - p` for closed.

Formalized by `StatMech.Percolation.w1`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#w1).

## Product weight of an edge configuration

The product weight `∏_e w1(ω_e)` of a configuration on a finite edge set.

Formalized by `StatMech.Percolation.W`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#w).

## Expectation under Bernoulli product weights

The expectation `∑_ω f(ω) W(ω)` of `f` under the Bernoulli(`p`) product weights on a finite
edge set.

Formalized by `StatMech.Percolation.wsum`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#wsum).

## Open cluster of a site inside a set

The open cluster `C_S(o)` of `o` inside `S`: sites of `S` joined to `o` by an open path in
`S`.

Formalized by `StatMech.Percolation.clusterWithin`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#cluster-within).

## Edges from a subset into a set

The set of edges `{x, y}` with `x ∈ K` and `y ∈ S`.

Formalized by `StatMech.Percolation.incidentWithin`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#incident-within).

## Event that the cluster of the origin inside a set equals a given set

The event `{C_S(o) = K}` that the open cluster of `o` inside `S` is exactly `K`.

Formalized by `StatMech.Percolation.clusterEvent`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#cluster-event).

## Edges joining a finite set to a region

The finite set of edges `{x, y}` with `x ∈ K` and `y ∈ S`.

Formalized by `StatMech.Percolation.incidentWithinFinset`, a definition declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#incident-within-finset).

## Exploration independence of a cluster inside a set

Exploration independence: for `K ⊆ S` finite and an event `B` depending only on edges in `U`,
disjoint from the edges between `K` and `S`, `ℙ_p(C_S(o) = K, B) = ℙ_p(C_S(o) = K) ℙ_p(B)`.

Formalized by `StatMech.Percolation.exploration_decomposition`, a theorem declared in [MathlibExt/Probability/Percolation/Exploration.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Exploration.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#exploration-decomposition).

## Crossing to the box exterior that avoids a cluster

`y ∉ C` is joined by an open path avoiding `C` to a site outside `Λ_{n-1}`.

Formalized by `StatMech.Percolation.offClusterCrossing`, a definition declared in [MathlibExt/Probability/Percolation/LastExit.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/LastExit.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#off-cluster-crossing).

## Open boundary edge of a cluster

The edge `{x, y}` is open, with `x ∈ C` and `y ∉ C`.

Formalized by `StatMech.Percolation.boundaryOpen`, a definition declared in [MathlibExt/Probability/Percolation/LastExit.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/LastExit.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#boundary-open).

## Crossing inside the box that avoids a cluster

`y ∈ Λ_n \ C` is joined by an open path inside `Λ_n \ C` to a site outside `Λ_{n-1}`.

Formalized by `StatMech.Percolation.offClusterBoxCrossing`, a definition declared in [MathlibExt/Probability/Percolation/OffClusterIndep.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/OffClusterIndep.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#off-cluster-box-crossing).

## Box edges with no endpoint in a cluster

The edges of `Λ_n` with no endpoint in `C`.

Formalized by `StatMech.Percolation.boxOffCEdges`, a definition declared in [MathlibExt/Probability/Percolation/OffClusterIndep.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/OffClusterIndep.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#box-off-cedges).

## One-arm event from the origin

The event `{0 ↔ ℤ^d \ Λ_{n-1}}` that the origin is joined by an open path to a site outside
`Λ_{n-1}`.

Formalized by `StatMech.Percolation.crossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/SubcriticalDecay.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/SubcriticalDecay.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#crossing-event).

## One-arm probability

The one-arm probability `ℙ_p(0 ↔ ℤ^d \ Λ_{n-1})`.

Formalized by `StatMech.Percolation.crossProb`, a definition declared in [MathlibExt/Probability/Percolation/SubcriticalDecay.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/SubcriticalDecay.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#cross-prob).

## Exponential decay from a one-step recursion

If `φ_p(S) < 1` and `crossProb((k + 1)L) ≤ φ_p(S) · crossProb(kL)` for all `k`, then
`crossProb d p n ≤ C e^{-cn}` for some `c, C > 0`.

Formalized by `StatMech.Percolation.subcritical_decay`, a theorem declared in [MathlibExt/Probability/Percolation/SubcriticalDecay.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/SubcriticalDecay.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#subcritical-decay).

## Translation invariance of the Bernoulli product measure

The Bernoulli product measure on `{0, 1}^E` is invariant under the shift action of `G`.

Formalized by `StatMech.Percolation.bernoulli_translationInvariant`, a theorem declared in [MathlibExt/Probability/Percolation/TranslationInvariance.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TranslationInvariance.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#bernoulli-translation-invariant).

## One-arm event from a shifted origin

The event that `y` is joined by an open path to a site outside `Λ_{n-1}`.

Formalized by `StatMech.Percolation.crossingEventFrom`, a definition declared in [MathlibExt/Probability/Percolation/TranslationInvariance.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/TranslationInvariance.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#crossing-event-from).

## Exponential decay below `p̃_c`

**Exponential decay below `p̃_c`** (Duminil-Copin–Tassion 2016): if
`φ_p(S) < 1` for some finite `S ∋ 0`, then `ℙ_p(0 ↔ ℤ^d \ Λ_{n-1}) ≤ C e^{-cn}` for some
`c, C > 0`.

Formalized by `StatMech.Percolation.crossProb_exp_decay_of_phi_lt_one`, a theorem declared in [MathlibExt/Probability/Percolation/SurfaceReassembly.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/SurfaceReassembly.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html#cross-prob-exp-decay-of-phi-lt-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential decay below the critical point](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/sharpness/exponential-decay-below-the-critical-point)
