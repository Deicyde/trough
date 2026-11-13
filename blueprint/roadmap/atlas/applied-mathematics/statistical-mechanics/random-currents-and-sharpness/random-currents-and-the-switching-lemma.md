---
declaration: section
origin: cited
lean: StatMech.Sharpness.Current, StatMech.Sharpness.incidentFlux, StatMech.Sharpness.sources, StatMech.Sharpness.weight, StatMech.Sharpness.weight_nonneg, StatMech.Sharpness.currentSubgraph, StatMech.Sharpness.CurrentConnected, StatMech.Sharpness.oddSubgraph
statement: formalized
proof: formalized
---

# Random currents and the switching lemma

81 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html).

## Current: a multiplicity in $\mathbb{N}$ for each unordered pair

A current on the edges of `V`: a multiplicity `n_e ∈ ℕ` for every unordered pair `e`.

Formalized by `StatMech.Sharpness.Current`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#current).

## Incident flux of a current at a vertex

The total multiplicity `∑_{e ∋ x} n_e` of the edges of `G` incident to `x`.

Formalized by `StatMech.Sharpness.incidentFlux`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#incident-flux).

## Sources of a current

The sources `∂n`: the vertices with odd incident flux.

Formalized by `StatMech.Sharpness.sources`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#sources).

## Weight of a random current

The current weight `w(n) = ∏_{e ∈ E(G)} (βJ_e)^{n_e}/n_e!`.

Formalized by `StatMech.Sharpness.weight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#weight).

## Current weights are nonnegative for nonnegative $\beta$ and couplings

Current weights are nonnegative for `β ≥ 0` and nonnegative couplings.

Formalized by `StatMech.Sharpness.weight_nonneg`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#weight-nonneg).

## Subgraph of edges carrying positive current

The subgraph of `G` of edges with `n_e ≥ 1`.

Formalized by `StatMech.Sharpness.currentSubgraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#current-subgraph).

## Connectivity through edges carrying positive current

`x` and `y` are joined by a path of edges carrying positive current.

Formalized by `StatMech.Sharpness.CurrentConnected`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#current-connected).

## Subgraph of edges with odd current

The subgraph of `G` of edges with odd multiplicity.

Formalized by `StatMech.Sharpness.oddSubgraph`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#odd-subgraph).

## Backbone paths along odd-current edges

Backbone paths from `x` to `y`: paths in the subgraph of odd edges.

Formalized by `StatMech.Sharpness.IsBackbonePath`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#is-backbone-path).

## Canonical backbone path of a current

A canonical backbone path: the least one for a given linear order on backbone paths.

Formalized by `StatMech.Sharpness.backbone`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#backbone).

## Trace of a current as a bond configuration

The trace of a current: the bond configuration with `e` open iff `n_e ≥ 1`.

Formalized by `StatMech.Sharpness.percolationField`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#percolation-field).

## Ghost vertex of the extended vertex set

The ghost vertex `none` of `Option V`.

Formalized by `StatMech.Sharpness.ghost`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#ghost).

## Graph with a ghost vertex joined to every site

The graph on `V ⊔ {ghost}` with the edges of `G` and an edge from every site to the ghost.

Formalized by `StatMech.Sharpness.withGhost`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/RandomCurrent.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#with-ghost).

## Number of walk edges at a vertex

The number of edges of the walk `p` incident to `x`.

Formalized by `StatMech.Sharpness.walkDeg`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneProps.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneProps.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#walk-deg).

## Current with a walk removed

The current `n` with one unit removed from each traversal of an edge of `p`.

Formalized by `StatMech.Sharpness.removeWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneProps.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneProps.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#remove-walk).

## Extension of an edge function to a current

Extension of a function on the edges of `G` to a current, zero off `E(G)`.

Formalized by `StatMech.Sharpness.ofEdgeFun`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#of-edge-fun).

## Current sum with prescribed sources

The current sum `Z(∂ = A) = ∑_{∂n = A} w(n)` over currents on the edges of `G`.

Formalized by `StatMech.Sharpness.currentSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#current-sum).

## Term of the exponential expansion of an edge weight

The `k`-th term `(βJ_e σ_e)^k / k!` of the expansion of `exp(βJ_e σ_e)`.

Formalized by `StatMech.Sharpness.gEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#g-edge).

## Boltzmann weight with couplings

The Boltzmann weight `exp(β ∑_e J_e σ_e)` with couplings `J`.

Formalized by `StatMech.Sharpness.boltzmannJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#boltzmann-j).

## Partition function with couplings

The partition function with couplings `J`.

Formalized by `StatMech.Sharpness.partitionJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#partition-j).

## Correlation function with couplings

The correlation `⟨σ_A⟩_{β,J}` with couplings `J`.

Formalized by `StatMech.Sharpness.expectationJ`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#expectation-j).

## Random-current representation

The random-current representation: `⟨σ_A⟩_{β,J} = Z(∂ = A)/Z(∂ = ∅)`. Reference: M. Aizenman,
"Geometric analysis of φ⁴ fields and Ising models", Comm. Math. Phys. 86 (1982) 1–48; J. Ginibre
(1970); H. Duminil-Copin, "Random currents expansion of the Ising model", lecture notes (2016),
arXiv:1607.06933.

Formalized by `StatMech.Sharpness.current_representation`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentRep.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#current-representation).

## Odd current on every edge of a path

Every edge of the path carries odd current.

Formalized by `StatMech.Sharpness.shb_IsBackboneOf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#shb-is-backbone-of).

## Odd-current paths between two vertices

The paths from `x` to `y` all of whose edges carry odd current.

Formalized by `StatMech.Sharpness.shb_backboneSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#shb-backbone-set).

## Odd-current path as a backbone path

A path with odd current on every edge as a backbone path.

Formalized by `StatMech.Sharpness.shb_backboneOf_imp_isBackbonePath`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#shb-backbone-of-imp-is-backbone-path).

## Least backbone path between two vertices

The least backbone path from `x` to `y`, if any.

Formalized by `StatMech.Sharpness.shb_backboneSelect`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#shb-backbone-select).

## Weight of currents with a given selected backbone

`Z_ω`: the total weight of currents with sources `{x, y}` whose selected backbone is `ω`.

Formalized by `StatMech.Sharpness.shb_backboneNum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#shb-backbone-num).

## Backbone weight $\rho(\omega)$

The backbone weight `ρ(ω) = Z_ω/Z(∂ = ∅)`.

Formalized by `StatMech.Sharpness.shb_rho`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BackboneDecomposition.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#shb-rho).

## Unordered pair inside a set

An unordered pair `e` is inside `S` if both of its endpoints lie in `S`.

Formalized by `StatMech.Sharpness.edgeInside`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentSplitting.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentSplitting.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#edge-inside).

## Current with no edge crossing a set's boundary

The current `n` uses no edge joining `S` to `Sᶜ`: every edge with `n e ≥ 1` is inside `S` or
inside `Sᶜ`.

Formalized by `StatMech.Sharpness.NoCrossing`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentSplitting.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentSplitting.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#no-crossing).

## Restriction of a current to a set

The restriction `n|_S` of a current to the edges inside `S`, zero elsewhere.

Formalized by `StatMech.Sharpness.restrictTo`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentSplitting.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/CurrentSplitting.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#restrict-to).

## Subsets of a sigma type as families of fibre subsets

Subsets of `Σ e, β e` correspond to families of subsets of the fibres.

Formalized by `StatMech.Sharpness.FluxEdgeCopy.sigmaFinsetEquivPi`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#sigma-finset-equiv-pi).

## Edge copies of a current

The edge copies of a current `m`: `m_e` copies of each edge `e`.

Formalized by `StatMech.Sharpness.FluxEdgeCopy.Copy`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#copy).

## Endpoints of an edge copy

The endpoints of an edge copy.

Formalized by `StatMech.Sharpness.FluxEdgeCopy.endsM`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#ends-m).

## Profile of a set of edge copies

The profile of a set of copies: the number of copies of each edge it contains.

Formalized by `StatMech.Sharpness.FluxEdgeCopy.profileFlux`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#profile-flux).

## Double-current sum restricted to disconnection

The double-current sum `∑_{∂n₁ = A, ∂n₂ = B} w(n₁) w(n₂) 1_{u ↮ v in n₁ + n₂}`.

Formalized by `StatMech.Sharpness.FluxEdgeCopy.sourcePairDisconnSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/EdgeCopyEncoding.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#source-pair-disconn-sum).

## Graph edges as ghost-graph edges

The edges of `G`, as edges of the ghost graph.

Formalized by `StatMech.Sharpness.FieldGhostDict.origEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#orig-edges).

## Ghost edges

The ghost edges `{x, ghost}`.

Formalized by `StatMech.Sharpness.FieldGhostDict.ghostEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#ghost-edges).

## Coupling on the ghost graph with uniform field

The coupling on the ghost graph: `J` on the edges of `G` and `h` on the ghost edges.

Formalized by `StatMech.Sharpness.FieldGhostDict.ghostCoupling`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#ghost-coupling).

## Global spin flip

The global spin flip `σ ↦ -σ`.

Formalized by `StatMech.Sharpness.FieldGhostDict.flipV`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#flip-v).

## Embedding of vertices into the ghost graph

The embedding `V ↪ Option V`.

Formalized by `StatMech.Sharpness.FieldGhostDict.someEmb`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#some-emb).

## Random-current representation with a field for even source sets

The random-current representation with a field: for `|A|` even, `⟨σ_A⟩_{β,h} = Z_ghost(∂ =
A)/Z_ghost(∂ = ∅)` on the ghost graph. Reference: M. Aizenman, D. J. Barsky, R. Fernández, "The
phase transition in a general class of Ising-type models is sharp", J. Stat. Phys. 47 (1987)
343–374; H. Duminil-Copin, "Random currents expansion of the Ising model", lecture notes (2016),
arXiv:1607.06933.

Formalized by `StatMech.Sharpness.FieldGhostDict.fgd_isingExpectation_eq_currentSum_ratio`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/FieldGhostDict.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#fgd-ising-expectation-eq-current-sum-rat).

## Reparametrizing triples of functions by their sum and two summands

Triples of functions to `ℕ` correspond to a sum `m` together with two functions with pointwise
sum `≤ m`.

Formalized by `StatMech.Sharpness.tripleEquivSigma`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultiReplica.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultiReplica.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#triple-equiv-sigma).

## Triple-current sum with prescribed sources

The triple-current sum `∑_{∂n₁ = A, ∂n₂ = B, ∂n₃ = C} w(n₁) w(n₂) w(n₃)`.

Formalized by `StatMech.Sharpness.sourceTripleSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultiReplica.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultiReplica.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#source-triple-sum).

## Degree of a vertex in a multigraph edge set

The degree of `x` in the multigraph edge set `T`.

Formalized by `StatMech.Sharpness.RandomCurrent.degK`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#deg-k).

## Sources of a multigraph edge set

The odd-degree vertices of the multigraph edge set `T`.

Formalized by `StatMech.Sharpness.RandomCurrent.sources`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#sources-2).

## Adjacency through an edge of a multigraph edge set

`a ≠ b` are the endpoints of an edge of `K`.

Formalized by `StatMech.Sharpness.RandomCurrent.adjStep`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#adj-step).

## Connectivity in a multigraph edge set

Connectivity in `K`: the reflexive transitive closure of `adjStep`.

Formalized by `StatMech.Sharpness.RandomCurrent.connK`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#conn-k).

## Cluster of a vertex in a multigraph edge set

The cluster of `u` in `K`.

Formalized by `StatMech.Sharpness.RandomCurrent.compOf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#comp-of).

## Switching lemma for multigraph currents

The switching lemma: for `m` with sources `A` and `u ≠ v`, `∑_{K ⊆ m, ∂K = A ∆ {u, v}} F(m) =
∑_{K ⊆ m, ∂K = A} F(m) 1_{u ↔ v in m}`. Reference: M. Aizenman, "Geometric analysis of φ⁴ fields and
Ising models", Comm. Math. Phys. 86 (1982) 1–48; H. Duminil-Copin, "Random currents expansion of the
Ising model", lecture notes (2016), arXiv:1607.06933.

Formalized by `StatMech.Sharpness.RandomCurrent.switching_lemma`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/Switching.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#switching-lemma).

## Sub-subset-weighted pair sum on a multigraph

For a multigraph `ends`, the sum over edge subsets `m` with sources `A` of `F m` times the
number of sub-subsets `K ⊆ m` with sources `A`, restricted to `m` satisfying `P`.

Formalized by `StatMech.Sharpness.drd_pairSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaRewriteDichotomy.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/DeltaRewriteDichotomy.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#drd-pair-sum).

## Vertices not connected to a root through a multigraph edge set

The vertices not connected to `o` using edges of `m` in the multigraph `ends`.

Formalized by `StatMech.Sharpness.RandomCurrent.notConnCompK`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#not-conn-comp-k).

## Multigraph edge lying inside a vertex set

Both endpoints of the multigraph edge `i` lie in `S`.

Formalized by `StatMech.Sharpness.RandomCurrent.edgeInsideK`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#edge-inside-k).

## Multigraph edge set with no edge crossing a vertex set

Every edge of `m` lies inside `S` or inside `Sᶜ`.

Formalized by `StatMech.Sharpness.RandomCurrent.NoCrossingK`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#no-crossing-k).

## Sum over edge sets split into parts with sources $A$ and $B$

The sum over edge sets `m` with sources `A ∆ B` and over splittings `m = K ⊔ (m \ K)` with
sources `A` and `B` of `F m`.

Formalized by `StatMech.Sharpness.RandomCurrent.srcPairFamily`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MultigraphClusterSwitching.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#src-pair-family).

## Odd-degree vertices in a cluster

The odd-degree vertices of `m` in the cluster of `u`.

Formalized by `StatMech.Sharpness.RandomCurrent.compOddVertices`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SwitchingDichotomy.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SwitchingDichotomy.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#comp-odd-vertices).

## Four-vertex multigraph with edges $\{0, 1\}$ and $\{2, 3\}$

A multigraph on `Fin 4` with the two edges `{0, 1}` and `{2, 3}`.

Formalized by `StatMech.Sharpness.RandomCurrent.witEnds`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SwitchingDichotomy.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SwitchingDichotomy.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#wit-ends).

## Full edge set of the four-vertex multigraph

All edges of `witEnds`.

Formalized by `StatMech.Sharpness.RandomCurrent.witM`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SwitchingDichotomy.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SwitchingDichotomy.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#wit-m).

## Single-edge current weight $(\beta J_e)^k/k!$

The single-edge weight `(βJ_e)^k / k!`.

Formalized by `StatMech.Sharpness.wEdge`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TwoReplica.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TwoReplica.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#w-edge).

## Reparametrizing pairs of functions by their sum and one summand

Pairs `(p, q)` of functions to `ℕ` correspond to a sum `m = p + q` together with `p ≤ m`.

Formalized by `StatMech.Sharpness.pairEquivSigma`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TwoReplica.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TwoReplica.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#pair-equiv-sigma).

## Double-current sum with prescribed sources

The double-current sum `∑_{∂n₁ = A, ∂n₂ = B} w(n₁) w(n₂)`.

Formalized by `StatMech.Sharpness.sourcePairSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/TwoReplica.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/TwoReplica.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#source-pair-sum).

## Current as a multiplicity on unordered pairs

A current: a multiplicity in `ℕ` on every unordered pair. See also
`StatMech.Sharpness.Current`.

Formalized by `StatMech.Ising.Current`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#current-2).

## Incident flux of a current on an edge set

The total multiplicity of the edges of `E` incident to `x`.

Formalized by `StatMech.Ising.incidentFlux`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#incident-flux-2).

## Source set of a current on an edge set

The source set of a current: the sites with odd incident flux. See also
`StatMech.Sharpness.sources` and `StatMech.Ising.sources_edgeFinset_eq`.

Formalized by `StatMech.Ising.sources`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#sources-3).

## Adjacency through an edge of an edge set

`a` and `b` are distinct endpoints of an edge in `P`.

Formalized by `StatMech.Ising.adjP`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#adj-p).

## Connectivity through the edges of an edge set

Connectivity through the edges of `P`: the reflexive-transitive closure of `adjP P`.

Formalized by `StatMech.Ising.connP`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#conn-p).

## Edges of an edge set with positive multiplicity

The edges of `E` with positive multiplicity.

Formalized by `StatMech.Ising.posEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#pos-edges).

## Edges of an edge set with odd multiplicity

The edges of `E` with odd multiplicity.

Formalized by `StatMech.Ising.oddEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#odd-edges).

## Degree of a site in an edge set

The number of edges of `P` incident to `x`.

Formalized by `StatMech.Ising.degP`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#deg-p).

## Odd-degree sites of an edge set

The sites of odd degree in the edge set `P`.

Formalized by `StatMech.Ising.srcP`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#src-p).

## Cluster of a site in an edge set

The cluster of `u` in the edge set `P`.

Formalized by `StatMech.Ising.compOf`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#comp-of-2).

## Reflection of a sub-current along an edge set

The reflection of a sub-current `n ≤ m` along `P`: `m e - n e` on `P` and `n e` elsewhere.

Formalized by `StatMech.Ising.reflect`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#reflect).

## Switching lemma

**Switching lemma** (counting form). If `u ≠ v` are connected by the odd edges of `n₁ + n₂`,
the sub-currents of `n₁ + n₂` with sources `A ∆ {u, v}` and with sources `A` are
equinumerous.

R. B. Griffiths, C. A. Hurst and S. Sherman, J. Math. Phys. 11 (1970); M. Aizenman,
*Geometric analysis of φ⁴ fields and Ising models*, Comm. Math. Phys. 86 (1982).

Formalized by `StatMech.Ising.ising_switching_lemma_pair`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplica.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#ising-switching-lemma-pair).

## Restriction of a current to an edge predicate

The restriction of the current `n` to the edges satisfying `p` (zero elsewhere).

Formalized by `StatMech.Ising.acwRestrict`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#acw-restrict).

## Internal edge of a vertex set

Both endpoints of `e` lie in `S`.

Formalized by `StatMech.Ising.acwInternal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#acw-internal).

## Vertex set that no edge of the graph crosses

Every edge of `G` lies inside `S` or inside its complement.

Formalized by `StatMech.Ising.acwClosedCut`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#acw-closed-cut).

## Sourced current sum as correlation times sourceless sum

`Z_A = ⟨σ_A⟩ Z_∅`.

Formalized by `StatMech.Ising.acw_currentSum_eq_expectation`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/CurrentWeight.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#acw-current-sum-eq-expectation).

## Sources on a graph's edge set agree with random-current sources

The source set of a current on the edges of `G` is `Sharpness.sources G`.

Formalized by `StatMech.Ising.sources_edgeFinset_eq`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#sources-edge-finset-eq).

## Reflection as an involution of the sub-currents of a current

Reflection along `P` as an involutive equivalence of the sub-currents of `m`.

Formalized by `StatMech.Ising.reflectEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#reflect-equiv).

## Weighted sum over splittings with prescribed sources

The weighted sum `F ∑_K w(K) w(m - K)` over sub-currents `K ≤ m` with sources `A`.

Formalized by `StatMech.Ising.splitWeightedSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#split-weighted-sum).

## Switching lemma

**Switching lemma** (weighted form). If `u ≠ v` are connected by odd edges of `m`, the
weighted sums over splittings with sources `A ∆ {u, v}` and `A` agree.

M. Aizenman, *Geometric analysis of φ⁴ fields and Ising models*, Comm. Math. Phys. 86 (1982).

Formalized by `StatMech.Ising.ising_switching_weighted`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/TwoReplicaWeighted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html#ising-switching-weighted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random currents and the switching lemma](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/random-currents-and-sharpness/random-currents-and-the-switching-lemma)
