---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GraphicalModels.sum_snoc, Cslib.MachineLearning.GraphicalModels.Chain, Cslib.MachineLearning.GraphicalModels.Chain.joint, Cslib.MachineLearning.GraphicalModels.Chain.sum_joint_snoc, Cslib.MachineLearning.GraphicalModels.Chain.sum_joint, Cslib.MachineLearning.GraphicalModels.Chain.cond_eq_div, Cslib.MachineLearning.GraphicalModels.Chain.joint_eq_prod, Cslib.MachineLearning.GraphicalModels.Chain.joint_congr
statement: formalized
proof: formalized
---

# Bayesian networks

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html).

## Splitting a sum over $\alpha^{n+1}$ at the last coordinate

Let $\alpha$ be a finite
type, $M$ an additive commutative monoid, $n$ a natural number and $f : \alpha^{n+1} \to M$.
Then $\sum_{x \in \alpha^{n+1}} f(x) =
\sum_{y \in \alpha^n} \sum_{a \in \alpha} f(y_0, \dots, y_{n-1}, a)$, where
$y = (y_0, \dots, y_{n-1})$.

Formalized by `Cslib.MachineLearning.GraphicalModels.sum_snoc`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#sum-snoc).

## Chain of conditional distributions

A chain of conditional distributions with values in
a type $\alpha$ assigns to every $k \in \mathbb{N}$ and every assignment $(x_0, \dots, x_{k-1})$
of values in $\alpha$ to the variables $0, \dots, k - 1$ a finitely supported probability
distribution $p_k(\cdot \mid x_0, \dots, x_{k-1})$ on $\alpha$, the conditional distribution of
variable $k$ given the earlier ones.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain`, a structure declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#chain).

## Joint distribution of a chain

For a chain of conditional distributions with values in
a type $\alpha$, write $p_k(\cdot \mid x_0, \dots, x_{k-1})$ for the conditional distribution of
variable $k$ given the earlier ones. The joint distribution $P_n : \alpha^n \to \mathbb{R}$ of
the first $n$ variables is defined by the chain rule: $P_0 = 1$ and
$P_{n+1}(x_0, \dots, x_n) = P_n(x_0, \dots, x_{n-1}) \, p_n(x_n \mid x_0, \dots, x_{n-1})$.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.joint`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#joint).

## Marginalizing the last variable of a chain

Let $c$ be a chain of conditional
distributions with values in a finite type $\alpha$, and write $P_k$ for its joint distribution
of the first $k$ variables. For every $n$ and every $y = (y_0, \dots, y_{n-1}) \in \alpha^n$,
$\sum_{a \in \alpha} P_{n+1}(y_0, \dots, y_{n-1}, a) = P_n(y)$.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.sum_joint_snoc`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#sum-joint-snoc).

## The joint distribution of a chain sums to one

Let $c$ be a chain of conditional
distributions with values in a finite type $\alpha$, and write $P_n$ for its joint distribution
of the first $n$ variables. For every $n$, $\sum_{x \in \alpha^n} P_n(x) = 1$.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.sum_joint`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#sum-joint).

## Conditionals of the joint of a chain

Let $c$ be a chain of conditional distributions
with values in a type $\alpha$, let $P_m$ be its joint distribution of the first $m$ variables,
and let $p_n(\cdot \mid y)$ be its conditional distribution of variable $n$ given values
$y \in \alpha^n$ of the earlier ones. For every $n$, every $y \in \alpha^n$ with $P_n(y) \ne 0$
and every $a \in \alpha$, we have $P_{n+1}(y, a) / P_n(y) = p_n(a \mid y)$, where
$(y, a) \in \alpha^{n+1}$ extends $y$ by the value $a$.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.cond_eq_div`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-eq-div).

## Factorization of the joint of a chain

For a chain of conditional distributions with
values in a type $\alpha$, write $p_k(\cdot \mid x_0, \dots, x_{k-1})$ for the conditional
distribution of variable $k$ given the earlier ones and $P_n$ for the joint distribution of
the first $n$ variables. Then for every $n$ and every $x \in \alpha^n$ we have
$P_n(x) = \prod_{k < n} p_k(x_k \mid x_0, \dots, x_{k-1})$.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.joint_eq_prod`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#joint-eq-prod).

## Joint distribution determined by the first conditionals

Let $n \in \mathbb{N}$. If two
chains of conditional distributions $c$ and $c'$ with values in a type $\alpha$ have the same
conditional distribution of variable $k$ given the earlier variables for every $k < n$, then
they have the same joint distribution of the first $n$ variables.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.joint_congr`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#joint-congr).

## Replacing one conditional of a chain

Given a chain $c$ of conditional distributions with
values in $\alpha$, an index $n$ and a family $f$ assigning to each $y \in \alpha^n$ a
probability distribution $f(y)$ on $\alpha$, the updated chain has conditional distribution $f$
for variable $n$ and the same conditional distribution as $c$ for every other variable.

Formalized by `Cslib.MachineLearning.GraphicalModels.Chain.update`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#update).

## The chain rule

Let $\alpha$ be a finite nonempty type and $n \in \mathbb{N}$. For every
function $P : \alpha^n \to \mathbb{R}$ with $P(x) \ge 0$ for all $x$ and $\sum_x P(x) = 1$,
there is a chain of conditional distributions with values in $\alpha$ whose joint distribution
of the first $n$ variables equals $P$.

Formalized by `Cslib.MachineLearning.GraphicalModels.exists_chain`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#exists-chain).

## Bayesian network

A Bayesian network with values in a type $\alpha$ on the nodes
$0, \dots, n - 1$, listed in a topological order, assigns to each node $k$ a finite set of
parents among the earlier nodes $0, \dots, k - 1$, and a conditional probability table: for each
assignment of values in $\alpha$ to the parents of $k$, a finitely supported probability
distribution on $\alpha$ for the value of node $k$.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet`, a structure declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#bayes-net).

## The chain of a Bayesian network

A Bayesian network $b$ on nodes $0, \dots, n - 1$ with
values in a nonempty type $\alpha$ defines a chain of conditional distributions. For $k < n$,
the conditional distribution of variable $k$ given values $y_0, \dots, y_{k-1}$ of the earlier
variables is the table of node $k$ applied to the values $y_j$ of its parents $j$. For
$k \ge n$ it is the point mass at a fixed arbitrary element of $\alpha$.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.toChain`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#to-chain).

## Joint distribution of a Bayesian network

Let $B$ be a Bayesian network on the nodes
$0, \dots, n - 1$ with values in a nonempty type $\alpha$. The joint distribution of $B$ is the
function $P : \alpha^n \to \mathbb{R}$ given by $P(x) = P_n(x)$ for $x \in \alpha^n$, where $P_n$
is the joint distribution of the first $n$ variables of the chain of conditional distributions
of $B$.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.joint`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#joint-2).

## Factorization of a Bayesian network

The joint is the product over nodes of the
probability of the node's value given the values of its parents.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.joint_eq_prod`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#joint-eq-prod-2).

## The joint distribution of a Bayesian network sums to one

Let $B$ be a Bayesian network
on the nodes $0, \dots, n - 1$ with values in a finite nonempty type $\alpha$, and let $P$ be its
joint distribution. Then $\sum_{x \in \alpha^n} P(x) = 1$.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.sum_joint`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#sum-joint-2).

## The ordered Markov property

Let $B$ be a Bayesian network on the nodes
$0, \dots, n - 1$ with values in a nonempty type $\alpha$, and let $P_m$ be the joint
distribution of the first $m$ nodes of $B$ viewed as a chain of conditional distributions. For
a node $k < n$, write $p_k(\cdot \mid z)$ for its conditional probability table at values $z$
of its parents. Let $y = (y_0, \dots, y_{k-1}) \in \alpha^k$ with $P_k(y) \ne 0$, and write
$y_{\mathrm{pa}(k)}$ for the values of $y$ at the parents of $k$. Then for every $a \in \alpha$,

$$P_{k+1}(y_0, \dots, y_{k-1}, a) / P_k(y) = p_k(a \mid y_{\mathrm{pa}(k)}).$$

In particular, the conditional distribution of node $k$ given all earlier nodes depends only on
the values of its parents.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.cond_eq_cpt`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianNetwork.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-eq-cpt).

## Marginal on a finite set of nodes as a filtered sum

`FiniteWeight.marginal` on a `Finset` of nodes, as a sum over a decidable filter.

Formalized by `Cslib.MachineLearning.GraphicalModels.marginal_coe`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#marginal-coe).

## Conditional independence for finite sets of nodes

`FiniteWeight.CondIndep` for `Finset`s of nodes, with the unions taken in `Finset`.

Formalized by `Cslib.MachineLearning.GraphicalModels.condIndep_coe_iff`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-indep-coe-iff).

## A marginal depends only on the fixed variables

`marginal P S x'` depends only on the values of `x'` on `S`.

Formalized by `Cslib.MachineLearning.GraphicalModels.marginal_congr_of_eqOn`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#marginal-congr-of-eq-on).

## Fixing more variables decreases the marginal

Fixing more variables decreases the probability.

Formalized by `Cslib.MachineLearning.GraphicalModels.marginal_le_of_subset`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#marginal-le-of-subset).

## Summing out one more variable from a marginal

Summing out one more variable `i ∉ S`.

Formalized by `Cslib.MachineLearning.GraphicalModels.marginal_eq_sum_insert`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#marginal-eq-sum-insert).

## Symmetry of conditional independence

Conditional independence is symmetric.

Formalized by `Cslib.MachineLearning.GraphicalModels.condIndep_symm`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-indep-symm).

## Decomposition

If `X ⫫ Y | Z` then `X' ⫫ Y | Z` for `X' ⊆ X`.

Formalized by `Cslib.MachineLearning.GraphicalModels.condIndep_mono_left`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-indep-mono-left).

## Weak union

If `X ∪ W ⫫ Y | Z` then `X ⫫ Y | Z ∪ W` (for a nonnegative law).

Formalized by `Cslib.MachineLearning.GraphicalModels.condIndep_weak_union`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-indep-weak-union).

## Ancestral set of nodes

A set of nodes is ancestral if it contains the parents of each of its nodes.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.IsAncestral`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#is-ancestral).

## Product of the tables of an ancestral set

The product of the tables of the nodes in `A`, with the uniform distribution on the other
nodes. For an ancestral `A` it has the same marginals on `A` as the joint
(`marginal_joint_eq_ancProd`).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.ancProd`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#anc-prod).

## The ancestral product on all nodes is the joint

On all nodes, `ancProd` is the joint.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.ancProd_univ`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#anc-prod-univ).

## The law of an ancestral set depends only on its tables

For an ancestral set `A` and
`S ⊆ A`, the marginals of the joint on `S` are those of `ancProd A`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.marginal_joint_eq_ancProd`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 783](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L783). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#marginal-joint-eq-anc-prod).

## Global Markov property for finite sets of nodes

The global Markov property for `Finset`s of nodes; `condIndep_of_dSeparated` is the
statement for arbitrary sets of nodes.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.condIndep_of_dSeparated_finset`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 945](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L945). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-indep-of-d-separated-finset).

## The global Markov property

**The global Markov property** (soundness of d-separation: Geiger, Verma & Pearl 1990;
Lauritzen, Dawid, Larsen & Leimer 1990): if `Z` d-separates `X` from `Y` in the graph of a
Bayesian network, then `X` and `Y` are conditionally independent given `Z` under its joint
law. No disjointness of `X`, `Y`, `Z` is needed.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesNet.condIndep_of_dSeparated`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean, line 969](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/GlobalMarkov.lean#L969). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html#cond-indep-of-d-separated).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bayesian networks](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/bayesian-networks)
