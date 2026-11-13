---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GraphicalModels.BayesNet.paVal, Cslib.MachineLearning.GraphicalModels.BayesNet.intervene, Cslib.MachineLearning.GraphicalModels.BayesNet.intervene_pa_self, Cslib.MachineLearning.GraphicalModels.BayesNet.intervene_pa_of_ne, Cslib.MachineLearning.GraphicalModels.BayesNet.joint_intervene, Cslib.MachineLearning.GraphicalModels.BayesNet.sum_paVal_intervene, Cslib.MachineLearning.GraphicalModels.BayesNet.sum_intervene_joint_mul, Cslib.MachineLearning.GraphicalModels.BayesNet.sum_filter_joint_eq_cpt_mul
statement: formalized
proof: formalized
---

# Causal Bayesian networks

33 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html).

## Parent values of a node

The values of the parents of node `k` in a full assignment `x`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.paVal`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#pa-val).

## The intervention `do(X_k = a)`

The mechanism of node `k` is replaced by the point mass
at `a`, and all incoming arrows to `k` are deleted (its parent set becomes `∅`); every other
node keeps its parents and its table. (The new table of `k` is the point mass on the empty
parent set; the tables of the other nodes are transported along the equality of their
parent sets.)

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.intervene`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#intervene).

## Intervention deletes the parents of the intervened node

The parents of the intervened node are deleted.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.intervene_pa_self`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#intervene-pa-self).

## Intervention leaves the parents of other nodes unchanged

The parents of every other node are unchanged by the intervention.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.intervene_pa_of_ne`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#intervene-pa-of-ne).

## The truncated factorization

**The truncated factorization** (Pearl 2009, eq. (3.10)): after `do(X_k = a)` the joint is
the product of the tables of all nodes other than `k` on assignments with `x_k = a`, and `0`
elsewhere.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.joint_intervene`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#joint-intervene).

## Intervention preserves the law of the parents

The intervention `do(X_k = a)` does not change the law of the parents of node `k`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_paVal_intervene`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-pa-val-intervene).

## Adjustment for the direct causes

**Adjustment for the direct causes** (Pearl 2009, Theorem 3.2.2; the case `Z = pa(X)` of
the back-door adjustment): for every function `f` of the variables,
`E[f | do(X_k = a)] = ∑_z P(pa_k = z) E[f | X_k = a, pa_k = z]`, assuming
`P(X_k = a, pa_k = z) > 0` whenever `P(pa_k = z) > 0`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_intervene_joint_mul`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-intervene-joint-mul).

## A node's table is its conditional law given its parents

The table of node `k` is the conditional law of `X_k` given its parents:
`P(X_k = a, pa_k = z) = p_k (a | z) P(pa_k = z)`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_filter_joint_eq_cpt_mul`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-filter-joint-eq-cpt-mul).

## Adjustment for the direct causes under table positivity

Adjustment for the direct causes when the table of node `k` gives the value `a` positive
probability at every value of the parents.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_intervene_joint_mul_of_cpt_ne_zero`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-intervene-joint-mul-of-cpt-ne-zero).

## Back-door adjustment for a set of predecessors containing the parents

Let `Z` be a set
of nodes preceding `k` in the topological order (so `Z` contains no descendant of `k`) that
contains the parents of `k`. Then `Z` meets the back-door criterion for every outcome node
`y ∉ Z` (a path from `k` to `y` that starts with an arrow into `k` starts `k ← p` with
`p ∈ pa(k) ⊆ Z`, an interior non-collider, so it is blocked), and for every function `f` of the
variables
`E[f | do(X_k = a)] = ∑_z P(Z = z) E[f | X_k = a, Z = z]`, assuming `P(X_k = a, Z = z) > 0`
whenever `P(Z = z) > 0` (Pearl 2009, Theorem 3.3.2, in this case).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_intervene_joint_mul_of_pred`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-intervene-joint-mul-of-pred).

## A node's table is its conditional law given a predecessor set

For a set `Z` of predecessors of `k` containing its parents, the table of `k` is its
conditional law given `Z`: `P(X_k = a, Z = z) = p_k (a | z_{pa k}) P(Z = z)`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_filter_restrict_joint_eq_cpt_mul`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-filter-restrict-joint-eq-cpt-mul).

## Back-door adjustment for a set of predecessors

Back-door adjustment for a set of predecessors containing the parents, when the table of
node `k` gives the value `a` positive probability at every value of the parents.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_intervene_joint_mul_of_pred_of_cpt_ne_zero`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#sum-intervene-joint-mul-of-pred-of-cpt-n).

## Edge of a Bayesian network

The edge `i → j` of the network's graph: `i` is a parent of `j`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.Edge`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#edge).

## Descendant relation in a Bayesian network

`j` is a descendant of `i` (every node is its own descendant).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.IsDescendant`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#is-descendant).

## Adjacency in the skeleton of a Bayesian network

`i` and `j` are adjacent in the skeleton of the graph.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.Adj`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#adj).

## Path in the skeleton of a Bayesian network

A path of the skeleton from `x` to `y`: a list of distinct nodes, consecutive ones
adjacent, starting at `x` and ending at `y`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.IsPath`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#is-path).

## Blocking at a node of a path

The consecutive nodes `u, m, w` of a path are blocked by `Z` (Pearl 2009, Definition
1.2.3): either `m` is a collider `u → m ← w` none of whose descendants is in `Z`, or `m` is not
a collider (a chain or a fork) and `m ∈ Z`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.BlockedAt`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#blocked-at).

## Blocked path

A path is blocked by `Z` if some three consecutive nodes of it are.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.PathBlocked`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#path-blocked).

## d-separation

**d-separation** (Pearl 1988; Pearl 2009, Definition 1.2.3): `Z` d-separates `X` from `Y`
if every path between a node of `X` and a node of `Y` is blocked by `Z`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.DSeparated`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#dseparated).

## Blocking at a node is independent of path direction

Blocking at a node does not depend on the direction in which the path is read.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.blockedAt_comm`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#blocked-at-comm).

## The reverse of a path is a path

The reverse of a path from `x` to `y` is a path from `y` to `x`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.isPath_reverse`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#is-path-reverse).

## Reversal preserves blocked paths

If a path is blocked by `Z`, so is its reverse.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.pathBlocked_reverse`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#path-blocked-reverse).

## Symmetry of d-separation

**Symmetry of d-separation.** d-separation is symmetric.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.DSeparated.symm`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalBayesNet.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#symm).

## Mutilated network of a set intervention

The network of the intervention `do(X_W = w)` with the arrows into `W` removed: every node
`j ∈ W` has no parents and the point mass at `w j` as its table.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.mutilateSet`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#mutilate-set).

## The truncated factorization for a set of nodes

After `do(X_W = w)`, the joint is the
product of the tables of the nodes outside `W` on assignments agreeing with `w` on `W`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.joint_mutilateSet`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#joint-mutilate-set).

## Arrows of the mutilated network

The arrows of `b.mutilateSet W w` are those of `b` not pointing into `W`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.edge_mutilateSet_iff`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#edge-mutilate-set-iff).

## Descendants in the mutilated network are descendants in the original

A descendant after removing the arrows into `W` is a descendant in `b`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.IsDescendant.of_mutilateSet`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#of-mutilate-set).

## Intervened nodes descend only from themselves

After removing the arrows into `W`, a node of `W` is a descendant only of itself.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.eq_of_isDescendant_mutilateSet`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#eq-of-is-descendant-mutilate-set).

## Assignments contradicting an intervention have probability zero

After `do(X_k = a)`, assignments with `x k ≠ a` have probability `0`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.joint_intervene_eq_zero`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#joint-intervene-eq-zero).

## Joint law as interventional law times the node's table

For `x k = a`, `P(x) = P(x | do(X_k = a)) · p_k(a | x_{pa k})`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.joint_eq_intervene_mul_cpt`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#joint-eq-intervene-mul-cpt).

## The intervention `do(X_k = a)` does not change the law of the non-descendants of `k`

**The intervention `do(X_k = a)` does not change the law of the non-descendants of `k`.**

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.marginal_intervene_of_not_isDescendant`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#marginal-intervene-of-not-is-descendant).

## The back-door adjustment

**The back-door adjustment** (Pearl 1995; Pearl 2009, Theorem 3.3.2): if the
set `Z` contains no descendant of the treatment node `k` and blocks every path between `k` and
the outcome node `y` that begins with an arrow into `k`, then
`P(X_y = v | do(X_k = a)) = ∑_z P(Z = z) P(X_y = v | X_k = a, Z = z)`, assuming
`P(X_k = a, Z = z) > 0` whenever `P(Z = z) > 0`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.backdoor_adjustment`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#backdoor-adjustment).

## The front-door adjustment

**The front-door adjustment** (Pearl 1995; Pearl 2009, Theorem 3.3.4): if the
set `M` intercepts every directed path from the treatment node `k` to the outcome node `y`, no
path from `k` to a node of `M` that begins with an arrow into `k` is open (blocked by `∅`), and
every path from a node of `M` to `y` that begins with an arrow into that node is blocked by
`{k}`, then
`P(X_y = v | do(X_k = a)) = ∑_m P(M = m | X_k = a) ∑_{a'} P(X_y = v | X_k = a', M = m) P(X_k = a')`,
assuming `P(X_k = a', M = m) > 0` for all `a'` and `m`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.frontdoor_adjustment`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/CausalAdjustment.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html#frontdoor-adjustment).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Causal Bayesian networks](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/causal-bayesian-networks)
