---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.IsReversibleSemigroup, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.prune_node_comm, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_node_comm, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_node_eq, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_slide, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_reroot, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.isReversibleSemigroup_ctmcTransition, Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.paralinear
statement: formalized
proof: formalized
---

# Pulley principle, LogDet distances and Felsenstein zone

41 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html).

## The pulley principle

## Reversible semigroup of transition matrices

A family of transition matrices `P t`, indexed by branch length, is a **reversible
semigroup** for the distribution `π`: it satisfies the Chapman–Kolmogorov equation and detailed
balance `π a P t a b = π b P t b a`. With rows summing to `1`, detailed balance makes `π`
stationary; the pulley principle uses only the two equations below.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.IsReversibleSemigroup`, a structure declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#is-reversible-semigroup).

## Partial likelihoods are invariant under swapping subtrees

Swapping the two subtrees of a node does not change its partial likelihoods; with
`likelihood_node_comm` this lets the rerooting move `likelihood_reroot` reach either child.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.prune_node_comm`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#prune-node-comm).

## Likelihood is invariant under swapping root subtrees

Swapping the two subtrees of the root does not change the likelihood.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_node_comm`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#likelihood-node-comm).

## The root can be pushed to the end of its edge

With the root on the edge between the
subtrees `l` and `r`, at distances `s` and `t`, the likelihood is that of the root placed at the
root of `l`, with `r` at distance `s + t`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_node_eq`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#likelihood-node-eq).

## Pulley principle, sliding

Moving the root along its edge does not change the
likelihood (Felsenstein 1981).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_slide`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#likelihood-slide).

## Pulley principle, rerooting

Let the root sit on the edge between an internal vertex `x`
(at distance `s₁`) and the subtree `C` (at distance `s₂`), where `x` has the subtrees `A` and
`B` at distances `a` and `b`. Moving the root to the edge between `x` and `A`, at distance `u₁`
from `A` and `u₂` from `x` with `u₁ + u₂ = a`, gives the same likelihood: the unrooted tree and
its edge lengths are unchanged (Felsenstein 1981).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.likelihood_reroot`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#likelihood-reroot).

## Reversible continuous-time models give reversible semigroups

A reversible continuous-time model gives a reversible semigroup: if `π` is in detailed
balance with the generator `Q`, the transition functions `exp (t • Q)` form a reversible
semigroup for `π`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.isReversibleSemigroup_ctmcTransition`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#is-reversible-semigroup-ctmc-transition).

## LogDet (paralinear) distance

The **LogDet (paralinear) distance** of a joint distribution matrix `F`
(`F i j = ℙ(X = i, Y = j)`): `-log |det F| + (log det Π_X + log det Π_Y) / 2`, where the
diagonal marginal matrices have determinants `∏ i, ∑ j, F i j` and `∏ j, ∑ i, F i j`. It is a
distance only when `det F ≠ 0` and the marginals are positive; otherwise the value is Lean's
totalized logarithm (`log 0 = 0`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.paralinear`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#paralinear).

## LogDet distance of a vertex to itself is zero

The distance of a vertex to itself is `0`: the joint distribution of `X` with itself is the
diagonal matrix of its (positive) marginal.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.paralinear_diagonal`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#paralinear-diagonal).

## Nonsingular transition matrices preserve positive distributions

Under a nonnegative, nonsingular transition matrix, a positive distribution stays positive:
every column of `M` has a positive entry. This puts the LogDet logarithms in their domain.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.vecMul_pos`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#vec-mul-pos).

## Additivity of the LogDet distance at a separating vertex

**Additivity of the LogDet distance at a separating vertex** (Steel 1994; Lockhart et al.
1994; Lake 1994). Let `Y` have distribution `p` (positive) and let `X` and `Z` be conditionally
independent given `Y`, with transition matrices `M` (from `Y` to `X`) and `N` (from `Y` to `Z`)
whose rows sum to `1` and whose determinants are nonzero. The joint distribution matrices are
`F_XY = Mᵀ Π_Y`, `F_YZ = Π_Y N` and `F_XZ = Mᵀ Π_Y N`, and `d(X, Z) = d(X, Y) + d(Y, Z)`. The
identity uses no sign condition on `M` and `N`; with nonnegative entries all logarithms are of
positive numbers (`vecMul_pos`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.paralinear_threePoint`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#paralinear-three-point).

## Additivity of the LogDet distance along a chain, one step

For a Markov chain
`X → Y → Z` with `X` distributed as `p` (positive), transition matrices `A` (nonnegative) and
`B` with unit row sums and nonzero determinants, `d(X, Z) = d(X, Y) + d(Y, Z)`, where
`F_XZ = Π_X A B`, `F_XY = Π_X A` and `F_YZ = Π_Y B` with `Y` distributed as `p A`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.paralinear_chain_step`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#paralinear-chain-step).

## Product of transition matrices along a path

The product `M 0 * M 1 * ⋯ * M (n - 1)` of the transition matrices along the first `n`
edges of a path.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.pathProd`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#path-prod).

## Additivity of the LogDet distance along a path

**Additivity of the LogDet distance along a path** (Steel 1994; Lockhart et al. 1994):
for a Markov chain `v₀ → v₁ → ⋯ → v_n` along a path, with positive initial distribution `p`
and nonnegative nonsingular transition matrices `M i` with unit row sums, the LogDet distance
between the ends is the sum of the distances of consecutive vertices. The joint distribution of
`v₀, v_n` is `Π_{v₀} M 0 ⋯ M (n - 1)`, and that of `v_i, v_{i+1}` is `Π_{v_i} M i`, where `v_i`
has distribution `p M 0 ⋯ M (i - 1)`. Under the general Markov model on a tree with positive
marginals and nonsingular matrices, the states along any path form such a chain once the model
is rooted at one end of the path.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.paralinear_pathProd`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#paralinear-path-prod).

## Symmetric two-state model on a branch

The **symmetric two-state model** on one branch: the state changes with probability `p`.
As a model, `0 ≤ p ≤ 1/2`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.twoState`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#two-state).

## Four-taxon quartet tree model

The quartet `((A, B), (C, D))` on the taxa `0 = A`, `1 = B`, `2 = C`, `3 = D`, with change
probabilities `pA, pB, pC, pD` on the pendant edges and `pI` on the internal edge. The root
sits at the `AB` end of the internal edge (the edge to the `AB` cherry vertex has change
probability `0`); by the pulley principle its position does not matter.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.quartet`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#quartet).

## Leaf weights of a site pattern

The leaf weights of a site pattern `σ`: the indicator of the observed state.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.siteObs`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#site-obs).

## Probability of a site pattern on a quartet

The probability of the site pattern `σ` on the quartet, with the uniform root distribution
(the stationary distribution of the symmetric model).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.patternProb`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#pattern-prob).

## Site pattern probabilities sum to one

The pattern probabilities sum to `1`, for all parameters.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.sum_patternProb`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#sum-pattern-prob).

## Nonnegativity of site pattern probabilities

The pattern probabilities are nonnegative for change probabilities in `[0, 1]`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.patternProb_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#pattern-prob-nonneg).

## Site pattern supporting a split

The site pattern `σ` **supports the split** `{a, b} | {c, d}`: `a, b` agree, `c, d` agree,
and the two pairs differ (a parsimony-informative pattern for that split).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.Supports`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#supports).

## Expected frequency of patterns supporting a split

The expected frequency of the patterns supporting the split `{a, b} | {c, d}`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.splitFreq`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#split-freq).

## Felsenstein (1978), the exact comparison

With change probability `P` on the long
non-sister branches to `A` and `C` and `Q` on the other three branches, the expected frequency
of patterns supporting the wrong split `AC | BD` exceeds that of the true split `AB | CD` by
`(1 - 2 Q) (P ^ 2 - Q (1 - Q))`, for all real `P, Q`. This is Felsenstein's equations (16)–(17)
(his four-species model has equal probabilities of change `0 → 1` and reversion `1 → 0`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.splitFreq_wrong_sub_true`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#split-freq-wrong-sub-true).

## Wrong split against third split frequency difference

The wrong split `AC | BD` against the third split `AD | BC`: the difference of expected
frequencies is `(1 - 2 Q) (P - Q) ^ 2`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.splitFreq_wrong_sub_third`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#split-freq-wrong-sub-third).

## True split against third split frequency difference

The true split `AB | CD` against the third split `AD | BC`: the difference of expected
frequencies is `Q (1 - 2 Q) (1 - 2 P)`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.splitFreq_true_sub_third`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#split-freq-true-sub-third).

## Rooted quartet with unit costs

The rooted quartet `((a, b), (c, d))` with unit costs, for Fitch's algorithm.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.quartetShape`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#quartet-shape).

## Fitch parsimony score on a quartet

The Fitch parsimony score of the site pattern `σ` on the quartet `((a, b), (c, d))`; it is
the small-parsimony score by `Parsimony.fitch_score_eq`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.parsimonyScore`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#parsimony-score).

## Difference of parsimony scores of two quartets

On four taxa, the parsimony scores of two quartets differ only on informative patterns: the
score on `AB | CD` minus the score on `AC | BD` is `1` on patterns supporting `AC | BD`, `-1` on
patterns supporting `AB | CD`, and `0` otherwise; likewise for `AD | BC`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.parsimonyScore_sub`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#parsimony-score-sub).

## Expected Fitch parsimony score on a quartet

The expected Fitch parsimony score of one site on the quartet `((a, b), (c, d))`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.expectedScore`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#expected-score).

## The Felsenstein zone

**The Felsenstein zone** (Felsenstein 1978): if `0 ≤ Q < 1/2` and `P ^ 2 > Q (1 - Q)`, the
wrong quartet `AC | BD` has strictly smaller expected parsimony score per site than both the
true quartet `AB | CD` and the third quartet `AD | BC`. The statement is algebraic in `P`; the
model has `0 ≤ P ≤ 1/2`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.expectedScore_wrong_lt`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#expected-score-wrong-lt).

## Parsimony is inconsistent in the Felsenstein zone

**Parsimony is inconsistent in the Felsenstein zone** (Felsenstein 1978): if the sites
`σ i` are pairwise independent and identically distributed with the pattern distribution of the
quartet, and `0 ≤ Q < 1/2`, `P ^ 2 > Q (1 - Q)`, then almost surely, for all long enough
alignments, the wrong quartet `AC | BD` has a strictly smaller total Fitch score than the true
quartet `AB | CD` and the third quartet `AD | BC`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.ae_eventually_parsimony_wrong`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#ae-eventually-parsimony-wrong).

## Jukes–Cantor transition matrix along a path

The JC transition matrix along a path whose branch lengths are listed in `ts`: the product
of the branch transition matrices `jcProb μ t`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.jcPath`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 614](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L614). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#jc-path).

## Chapman–Kolmogorov along a path

The JC transition matrix along a path is the
transition matrix of the total length.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.jcPath_eq`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 620](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L620). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#jc-path-eq).

## JC-corrected distances are path lengths

**JC-corrected distances are path lengths** (Jukes & Cantor 1969): the JC distance of the
probability that the two ends of a path differ is `μ` times the total branch length.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.jcDistance_jcPath`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#jc-distance-jc-path).

## Empirical p-distance

The empirical p-distance of the taxa `x, y` over the first `n` sites of the alignment
`seq` (`seq i x` is the base of taxon `x` at site `i`): the proportion of sites where they
differ.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.pHat`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 640](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L640). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#p-hat).

## Jukes–Cantor corrected empirical distance

The JC-corrected empirical distance `jcDistance (pHat seq n x y)`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.jcHat`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#jc-hat).

## Neighbor joining recovers a tree within a radius

Neighbor joining **recovers the tree within radius `r`** of the dissimilarity `d`: every
complete run of neighbor joining on a symmetric dissimilarity `D` with zero diagonal and
`|D x y - d x y| < r` for distinct taxa forms exactly the splits of the internal edges of
`(G, ι)`. Atteson's theorem gives this for the path-length metric of a binary phylogenetic tree
with `r` half the shortest internal edge length (`njRecoversWithin_of_le`).

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.NJRecoversWithin`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 652](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L652). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#njrecovers-within).

## Strong law for the p-distances

For pairwise independent, identically distributed
sites, the empirical p-distance of every pair of taxa converges almost surely to the
probability that the two taxa differ at a site.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.ae_tendsto_pHat`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#ae-tendsto-p-hat).

## Statistical consistency of neighbor joining under Jukes–Cantor

**Statistical consistency of neighbor joining under Jukes–Cantor** (Saitou & Nei 1987;
Atteson 1999). Let `(G, ι)` be a binary phylogenetic `X`-tree with path-length metric `d` for
edge lengths `w`, and let the sites be pairwise independent and identically distributed, with
the two-leaf marginals of the JC model with rate `μ` and uniform root: for every path `p` from
`x` to `y`, `ℙ(site x = i, site y = j) = jcPath μ (lengths of p) i j / 4`. If neighbor joining
recovers the tree within some radius `r > 0` of the scaled metric `μ d` (for `μ > 0`, Atteson's
theorem gives `r = μ m / 2`, `m` the shortest internal edge length), then almost surely, for all
long enough alignments, every complete run of neighbor joining on the JC-corrected empirical
distances returns exactly the splits of the internal edges of the tree.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.ae_eventually_njRun_splits_jcHat`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#ae-eventually-nj-run-splits-jc-hat).

## Atteson's radius for the scaled tree metric

Let `d` be the path-length metric of a
binary phylogenetic `X`-tree `(G, ι)` with positive edge lengths `w` whose internal edges (no
taxon at either end) have length at least `m`. For `μ > 0`, neighbor joining recovers the tree
within radius `μ m / 2` of the scaled metric `μ d`. This is `njRun_splits_of_abs_sub_lt`
(Atteson 1999) for the edge lengths `μ w`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.njRecoversWithin_of_le`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#nj-recovers-within-of-le).

## Statistical consistency of neighbor joining under Jukes–Cantor

**Statistical consistency of neighbor joining under Jukes–Cantor** (Saitou & Nei 1987;
Atteson 1999), without a robustness hypothesis. Let `(G, ι)` be a binary phylogenetic `X`-tree
with path-length metric `d` for positive edge lengths `w`, whose internal edges have length at
least `m > 0`, and let the sites be pairwise independent and identically distributed, with the
two-leaf marginals of the JC model with rate `μ > 0` and uniform root. Then almost surely, for
all long enough alignments, every complete run of neighbor joining on the JC-corrected
empirical distances returns exactly the splits of the internal edges of the tree.

Formalized by `Cslib.Bioinformatics.Phylogenetics.FelsensteinZone.ae_eventually_njRun_splits_jcHat_of_le`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean, line 794](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/FelsensteinZone.lean#L794). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html#ae-eventually-nj-run-splits-jc-hat-of-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pulley principle, LogDet distances and Felsenstein zone](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/pulley-principle-logdet-distances-and-felsenstei)
