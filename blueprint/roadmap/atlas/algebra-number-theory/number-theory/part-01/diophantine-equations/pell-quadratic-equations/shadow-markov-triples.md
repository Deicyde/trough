---
declaration: section
origin: cited
lean: MetaMathlibExt.shadowMarkoffMutate, MetaMathlibExt.shadowMarkoffRoot, MetaMathlibExt.ShadowMarkoffTreeNode, MetaMathlibExt.shadowMarkoffTree, MetaMathlibExt.shadowMarkoffMutate_vertex_001, MetaMathlibExt.exists_polygon_shadowMarkoffTree_nonneg_iff, MetaMathlibExt.shadowMarkoffTree_one_shadow_eq
statement: formalized
---

# Shadow Markov triples

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html).

## Shadow Markoff mutation

A state is a pair $(x, y)$ of a classical part
$x \in \mathbb{Q}^3$ and a shadow part $y \in \mathbb{Q}^3$, with coordinates indexed by the
positions $0, 1, 2$. The shadow Markoff mutation at position $i$ replaces $x_i$ by
$x_i' = \bigl(\sum_{j \ne i} x_j^2\bigr) / x_i$ and $y_i$ by
$\bigl(-x_i' y_i + 2 \sum_{j \ne i} x_j y_j\bigr) / x_i$, and leaves every other coordinate of
$x$ and $y$ unchanged.

Division by $0$ gives $0$: if $x_i = 0$, the new $x_i$ and the new $y_i$ are both $0$.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Section 1, equations (MutA) and (SMarmutBis).

Formalized by `MetaMathlibExt.shadowMarkoffMutate`, a definition declared in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#shadow-markoff-mutate).

## Initial triple of a shadow Markoff tree

For
$v = (\alpha, \beta, \gamma) \in \mathbb{Z}^3$, the initial triple with shadow part $v$ is
$(1 + \alpha\varepsilon, 1 + \beta\varepsilon, 1 + \gamma\varepsilon)$, where
$\varepsilon^2 = 0$. It is stored as the state $(x, y)$ with classical part
$x = (1, 1, 1) \in \mathbb{Q}^3$ and shadow part
$y = (\alpha, \beta, \gamma) \in \mathbb{Q}^3$.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Section 1, equation (InitTrip).

Formalized by `MetaMathlibExt.shadowMarkoffRoot`, a definition declared in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#shadow-markoff-root).

## Lower nodes of a shadow Markoff tree

Fix $v \in \mathbb{Z}^3$ and let $r$ be the
initial triple with shadow part $v$, viewed as a state (a pair of a classical part and a shadow
part, both in $\mathbb{Q}^3$, with coordinates indexed by the positions $0, 1, 2$). The lower
nodes of the shadow Markoff tree of $v$ are pairs $(s, l)$ of a state $s$ and a position $l$, the
position mutated last. They are defined inductively: the state obtained from $r$ by the shadow
Markoff mutation at position $0$ and then at position $1$, tagged with $l = 1$, is a lower node;
and if $(s, l)$ is a lower node and $i \ne l$, then the mutation of $s$ at position $i$, tagged
with $i$, is a lower node. Nothing else is a lower node.

The first lower node has classical part $(2, 5, 1)$, the paper's $(1, 2, 5)$; the lower nodes
are the nodes of the tree below the paper's $(1, 1, 2)$.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Section 2 (the classical Markoff tree: "The initial triple `(1,1,1)` is the root of the tree. It is followed by `(1,1,2)` and `(1,2,5)`. After that, any mutation is allowed.") and Section 4.

Formalized by `MetaMathlibExt.ShadowMarkoffTreeNode`, an inductive type declared in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#shadow-markoff-tree-node).

## Shadow Markoff tree

For $v \in \mathbb{Z}^3$, the shadow Markoff tree of $v$ is the
set of states $(x, y) \in \mathbb{Q}^3 \times \mathbb{Q}^3$ (classical part $x$, shadow part
$y$) consisting of the initial triple $r$ with shadow part $v$, the shadow Markoff mutation of
$r$ at position $0$, and the state $s$ of every lower node $(s, l)$ of the shadow Markoff tree
of $v$.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Sections 2 and 4.

Formalized by `MetaMathlibExt.shadowMarkoffTree`, a definition declared in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#shadow-markoff-tree).

## The first two mutations in the tree of the vertex $(0:0:1)$

Number the positions
$0, 1, 2$ and write a state as $(x \mid y)$, with classical part $x \in \mathbb{Q}^3$ and shadow
part $y \in \mathbb{Q}^3$. The initial triple $(1, 1, 1 + \varepsilon)$, where
$\varepsilon^2 = 0$, has shadow part $(0, 0, 1)$ (the paper's vertex $(0:0:1)$) and is the state
$(1, 1, 1 \mid 0, 0, 1)$. Its shadow Markoff mutation at position $0$ is
$(2, 1, 1 \mid 2, 0, 1)$, and the mutation of that state at position $1$ is
$(2, 5, 1 \mid 2, 10, 1)$.

These match the labels $2\ 2$ and $5\ 10$ of the paper's figure.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Section 4.1 (the tree of the vertex `(0:0:1)`).

Formalized by `MetaMathlibExt.shadowMarkoffMutate_vertex_001`, a theorem declared in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#shadow-markoff-mutate-vertex-001).

## Nonnegativity on a shadow Markoff tree is governed by finitely many points

There is a
finite set $V \subseteq \mathbb{Q}^3$ such that for every
$v = (\alpha, \beta, \gamma) \in \mathbb{Z}^3$ the following are equivalent: every state $(x, y)$
of the shadow Markoff tree of $v$, the tree of the initial triple
$(1 + \alpha\varepsilon, 1 + \beta\varepsilon, 1 + \gamma\varepsilon)$ with $\varepsilon^2 = 0$,
has all coordinates of its classical part $x$ and of its shadow part $y$ nonnegative; and $v = tw$
for some rational $t \ge 0$ and some point $w$ of the convex hull of $V$ in $\mathbb{Q}^3$.

In projective terms, the source describes the points $(\alpha : \beta : \gamma)$ with a
nonnegative tree as a convex polygon in an affine chart of the rational projective plane; the
statement above asserts only that some finite set $V$ exists.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Theorem 2 (`jis-2024-24.8.3-thm-2`).

Stated but not proved: `MetaMathlibExt.exists_polygon_shadowMarkoffTree_nonneg_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#exists-polygon-shadow-markoff-tree-nonne).

## Shadow parts equal classical parts when $v = (1, 1, 1)$

In the shadow Markoff tree of
$v = (1, 1, 1)$, the tree of the initial triple
$(1 + \varepsilon, 1 + \varepsilon, 1 + \varepsilon)$ with $\varepsilon^2 = 0$, every solution
$(x, y)$ has shadow part $y$ equal to its classical part $x$.

So the shadow parts of this tree reproduce the classical Markoff tree.

## Sources

- Nathan Bonin, *Conditions of Positivity on a Shadow Markoff Tree*, Journal of Integer Sequences 27 (2024), Article 24.8.3, Lemma 3 (`jis-2024-24.8.3-lem-3`).

Stated but not proved: `MetaMathlibExt.shadowMarkoffTree_one_shadow_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ShadowMarkoffTreeWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html#shadow-markoff-tree-one-shadow-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shadow Markov triples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/shadow-markov-triples)
