---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GraphicalModels.TreeModel, Cslib.MachineLearning.GraphicalModels.TreeModel.parent, Cslib.MachineLearning.GraphicalModels.TreeModel.weight, Cslib.MachineLearning.GraphicalModels.TreeModel.lastParent, Cslib.MachineLearning.GraphicalModels.TreeModel.message, Cslib.MachineLearning.GraphicalModels.TreeModel.eliminate, Cslib.MachineLearning.GraphicalModels.TreeModel.sum_weight_mul_eliminate, Cslib.MachineLearning.GraphicalModels.TreeModel.rootMessage
statement: formalized
proof: formalized
---

# Variable elimination and belief propagation

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html).

## Pairwise model on a tree

For a type $\alpha$ of values and $n \in \mathbb{N}$, a pairwise
tree model on the vertices $0, \dots, n$ consists of a parent $p(k + 1) \in \{0, \dots, k\}$ for
each vertex $k + 1$ with $k < n$ (so vertex $0$ is the root and every vertex comes after its
parent), a unary factor $\varphi_i : \alpha \to \mathbb{R}$ for each vertex $i \le n$, and for each
$k < n$ a pairwise factor $\psi_k(a, b) \in \mathbb{R}$ on the edge between vertex $k + 1$ and its
parent, defined for all $a, b \in \alpha$, where $a$ is the value at vertex $k + 1$ and $b$ the
value at its parent.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel`, a structure declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#tree-model).

## Parent of a vertex

In a pairwise tree model on the vertices $0, \dots, n$, for $k < n$ the
parent of vertex $k + 1$ is the parent recorded by the model, an element of $\{0, \dots, k\}$,
regarded as one of the vertices $0, \dots, n$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.parent`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#parent).

## Weight of an assignment in a tree model

Let $\alpha$ be a type and let $m$ be a pairwise
model on a tree with vertices $0, \dots, n$, with unary factors $\varphi_i : \alpha \to \mathbb{R}$
for each vertex $i$, and with factor $\psi_k : \alpha \times \alpha \to \mathbb{R}$ on the edge
between vertex $k + 1$ and its parent $p(k + 1)$ for each $k < n$. The unnormalized weight of an
assignment $x : \{0, \dots, n\} \to \alpha$ is the real number

$$w(x) = \prod_{i=0}^{n} \varphi_i(x_i) \cdot \prod_{k=0}^{n-1} \psi_k(x_{k+1}, x_{p(k+1)}),$$

the product of all factors evaluated at $x$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.weight`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#weight).

## Parent of the last vertex

In a pairwise tree model on the vertices $0, \dots, n + 1$, this
is the parent of the last vertex $n + 1$, regarded as one of the vertices $0, \dots, n$ of the tree
with the last vertex removed.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.lastParent`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#last-parent).

## Message from the last vertex

Let $\alpha$ be finite and consider a pairwise tree model on
the vertices $0, \dots, n + 1$ with unary factors $\varphi_i$ and pairwise factors $\psi_k$. The
message from the last vertex $n + 1$ to its parent is the function $\mu : \alpha \to \mathbb{R}$
given by $\mu(a) = \sum_{b \in \alpha} \psi_n(b, a) \, \varphi_{n+1}(b)$, where $\psi_n$ is the
factor of the edge between vertex $n + 1$ and its parent.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.message`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#message).

## Eliminating the last vertex of a tree model

Let $\alpha$ be finite, let $m$ be a pairwise
tree model on the vertices $0, \dots, n + 1$ with parents $p$, unary factors $\varphi_i$ and
pairwise factors $\psi_k$, and let $\mu$ be the message from the last vertex $n + 1$ to its
parent $q = p(n + 1)$. Eliminating the last vertex gives the pairwise tree model on the vertices
$0, \dots, n$ in which vertex $k + 1$ has parent $p(k + 1)$ and edge factor $\psi_k$ for each
$k < n$, and whose unary factors are $\varphi'_q(a) = \varphi_q(a) \, \mu(a)$ and
$\varphi'_i = \varphi_i$ for every vertex $i \le n$ with $i \ne q$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.eliminate`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#eliminate).

## One step of variable elimination

Let $\alpha$ be finite, let $m$ be a pairwise tree model
on the vertices $0, \dots, n + 1$ with weight $w$, and let $m'$ be the model on the vertices
$0, \dots, n$ obtained from $m$ by eliminating the last vertex, with weight $w'$. Then for every
function $g : \alpha \to \mathbb{R}$ we have $\sum_x w(x) \, g(x_0) = \sum_y w'(y) \, g(y_0)$,
where $x$ ranges over all assignments $\{0, \dots, n + 1\} \to \alpha$ and $y$ over all
assignments $\{0, \dots, n\} \to \alpha$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.sum_weight_mul_eliminate`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#sum-weight-mul-eliminate).

## Root message of a tree model

Let $\alpha$ be finite. The root message of a pairwise tree
model $m$ on the vertices $0, \dots, n$ is the function $r_m : \alpha \to \mathbb{R}$ defined by
recursion on $n$: if $n = 0$, it is the unary factor of the root $0$; if $m$ is a model on the
vertices $0, \dots, n + 1$, it is $r_{m'}$, where $m'$ is the model on the vertices $0, \dots, n$
obtained from $m$ by eliminating the last vertex.

By variable elimination, $r_m(a)$ is the unnormalized marginal of the root at $a$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.rootMessage`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#root-message).

## Variable elimination is exact

Let $\alpha$ be finite and let $m$ be a pairwise tree model
on the vertices $0, \dots, n$ with weight $w$ and root message $r : \alpha \to \mathbb{R}$. Then
for every function $g : \alpha \to \mathbb{R}$ of the root value,
$\sum_x w(x) \, g(x_0) = \sum_{a \in \alpha} r(a) \, g(a)$, where $x$ ranges over all assignments
$\{0, \dots, n\} \to \alpha$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.sum_weight_mul_eq`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#sum-weight-mul-eq).

## Variable elimination computes the partition function

Let $\alpha$ be finite and let $m$
be a pairwise tree model on the vertices $0, \dots, n$ with weight $w$ and root message
$r : \alpha \to \mathbb{R}$. Then the partition function of $m$ is the total root message:
$\sum_x w(x) = \sum_{a \in \alpha} r(a)$, where $x$ ranges over all assignments
$\{0, \dots, n\} \to \alpha$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.partition_eq`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#partition-eq).

## Variable elimination computes the unnormalized root marginal

Let $\alpha$ be finite and
let $m$ be a pairwise tree model on the vertices $0, \dots, n$ with weight $w$ and root message
$r : \alpha \to \mathbb{R}$. Then for every $a \in \alpha$ the unnormalized marginal of the root
at $a$ equals $r(a)$, that is, $\sum_x w(x) = r(a)$, where $x$ ranges over the assignments
$\{0, \dots, n\} \to \alpha$ with $x_0 = a$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.rootMarginal_eq`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/VariableElimination.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#root-marginal-eq).

## Removing the last vertex

For a tree model with vertices $0, \dots, n + 1$, the tree model
on $0, \dots, n$ with the same parents, unary factors and edge factors: the last vertex, which is
a leaf, is removed together with its unary factor and the factor of its edge.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.dropLast`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#drop-last).

## Summing out the last vertex preserves weighted sums at the other vertices

Let $m$ be a
pairwise tree model on the vertices $0, \dots, n + 1$ with values in a finite type $\alpha$, and
let $m'$ be the model on the vertices $0, \dots, n$ obtained from $m$ by summing out its last
vertex. Write $w_m$ and $w_{m'}$ for their unnormalized weights. Then for every vertex $v \le n$
and every function $g : \alpha \to \mathbb{R}$,

$$\sum_x w_m(x)\, g(x_v) = \sum_y w_{m'}(y)\, g(y_v),$$

where $x$ and $y$ range over all assignments of values in $\alpha$ to the vertices of $m$ and of
$m'$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.sum_weight_mul_eliminate_castSucc`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#sum-weight-mul-eliminate-cast-succ).

## Sum-product belief

The belief of each vertex of a tree model over a finite set of values,
computed by sum-product message passing: the product of its unary factor, the messages from its
subtree and the message from its parent. Recursively, in a model with a single vertex the belief
of that vertex is its unary factor; in a model with vertices $0, \dots, n + 1$ the belief of the
last vertex at a value $b$ is its unary factor at $b$ times the downward message to the last
vertex at $b$, and the belief of every other vertex is its belief in the model with the last
vertex summed out.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.belief`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#belief).

## Downward message to the last vertex

For a tree model with vertices $0, \dots, n + 1$ over
a finite set of values, the message from the parent $p$ of the last vertex to the last vertex at
a value $b$ is the sum over all values $a$ of $\psi(b, a)\, \beta(a)$, where $\psi$ is the factor
of the edge between the last vertex and $p$ (last vertex first) and $\beta(a)$ is the belief of
$p$ at $a$ in the model without the last vertex.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.downMessage`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#down-message).

## Belief propagation is exact on trees

Let $m$ be a pairwise tree model on the vertices
$0, \dots, n$ with values in a finite type $\alpha$, let $w$ be its unnormalized weight, and let
$b_v$ be the belief of vertex $v$ computed by sum-product message passing. Then for every vertex
$v$ and every function $g : \alpha \to \mathbb{R}$,

$$\sum_x w(x)\, g(x_v) = \sum_{a \in \alpha} b_v(a)\, g(a),$$

where $x$ ranges over all assignments of values in $\alpha$ to the vertices.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.sum_weight_mul_eq_belief`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#sum-weight-mul-eq-belief).

## Beliefs are the unnormalized marginals

For every tree model over a finite set of values,
every vertex $v$ and every value $a$, the belief of $v$ at $a$ is the unnormalized marginal of $v$
at $a$: the sum of the weights of all assignments $x$ with $x_v = a$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.marginal_eq_belief`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#marginal-eq-belief).

## Belief at the root is the root message

For every tree model over a finite set of values,
the belief of the root, vertex $0$, is the root message computed by variable elimination: the two
agree at every value.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.belief_zero`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#belief-zero).

## Nonnegative factors

A tree model has nonnegative factors when all its unary factors and
all its edge factors take only nonnegative values.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.NonnegFactors`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#nonneg-factors).

## Max-product message

For a tree model with vertices $0, \dots, n + 1$ over a finite
nonempty set of values, the max-product message from the last vertex to its parent at a value $a$
is the maximum over all values $b$ of $\psi(b, a)\, \phi(b)$, where $\psi$ is the factor of the
edge between the last vertex and its parent and $\phi$ is the unary factor of the last vertex.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.maxMessage`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#max-message).

## Maximizing out the last vertex

For a tree model with vertices $0, \dots, n + 1$ over a
finite nonempty set of values, the tree model on $0, \dots, n$ with the same parents and edge
factors whose unary factor at the parent of the last vertex is multiplied by the max-product
message of the last vertex; the other unary factors are unchanged.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.maxEliminate`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#max-eliminate).

## Max-product value

For a tree model over a finite nonempty set of values, the value
computed by maximizing out the vertices from the last one down: for a single vertex it is the
maximum of its unary factor over all values, and for more vertices it is the max-product value of
the model with the last vertex maximized out.

When all factors are nonnegative, this is the largest weight of an assignment.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.maxWeight`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#max-weight).

## Max-product decoding

An assignment of a tree model over a finite nonempty set of values,
defined by recursion on the number of vertices. For a single vertex, its value is one that
maximizes its unary factor. For vertices $0, \dots, n + 1$, the vertices $0, \dots, n$ get the
decoding of the model with the last vertex maximized out, and the last vertex gets a value $b$
maximizing $\psi(b, a)\, \phi(b)$, where $a$ is the decoded value of its parent, $\psi$ is the
factor of the edge between the last vertex and its parent and $\phi$ is the unary factor of the
last vertex; that is, $b$ attains the max-product message of the last vertex at $a$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.decode`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#decode).

## The max-product value bounds every weight

Let $m$ be a pairwise tree model with values in
a finite nonempty type $\alpha$ whose unary and pairwise factors are all nonnegative, and let $M$
be its max-product value, obtained by maximizing out the vertices from the last one down. Then
every assignment of values in $\alpha$ to the vertices has weight at most $M$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.weight_le_maxWeight`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#weight-le-max-weight).

## Max-product decoding attains the max-product value

Let $m$ be a pairwise tree model with
values in a finite nonempty type, and let $M$ be its max-product value, obtained by maximizing out
the vertices from the last one down. Then the weight of the assignment produced by max-product
decoding equals $M$.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.weight_decode`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#weight-decode).

## Max-product decoding finds a MAP assignment

Let $m$ be a pairwise tree model with values
in a finite nonempty type $\alpha$ whose unary and pairwise factors are all nonnegative. Then every
assignment of values in $\alpha$ to the vertices has weight at most the weight of the assignment
produced by max-product decoding.

Formalized by `Cslib.MachineLearning.GraphicalModels.TreeModel.weight_le_weight_decode`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BeliefPropagation.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html#weight-le-weight-decode).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Variable elimination and belief propagation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/variable-elimination-and-belief-propagation)
