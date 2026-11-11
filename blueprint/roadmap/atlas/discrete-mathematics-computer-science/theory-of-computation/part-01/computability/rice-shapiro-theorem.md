---
declaration: section
origin: cited
lean: Cslib.Decidability.rice_shapiro_mono, Cslib.Decidability.rice_shapiro_finite, Cslib.Decidability.finFun, Cslib.Decidability.IsGraph, Cslib.Decidability.rePred_isGraph, Cslib.Decidability.exists_finFun_eq, Cslib.Decidability.rePred_subgraph, Cslib.Decidability.tm2Recognizable_of_basis
statement: formalized
proof: formalized
---

# Rice–Shapiro theorem

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html).

## Rice–Shapiro, upward closure

In a class with a recognizable index set, every partial
recursive extension of a partial recursive member is a member.

Formalized by `Cslib.Decidability.rice_shapiro_mono`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#rice-shapiro-mono).

## Rice–Shapiro, finite approximation

Every partial recursive member of a class with a
recognizable index set has a partial recursive finite subfunction in the class.

Formalized by `Cslib.Decidability.rice_shapiro_finite`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#rice-shapiro-finite).

## Finite function of a list of pairs

For a finite list $\theta$ of pairs of natural
numbers, the finite function of $\theta$ is the partial function
$\mathbb{N} \rightharpoonup \mathbb{N}$ whose value at $x$ is the second component of the first
pair in $\theta$ with first component $x$, and which is undefined at $x$ when $\theta$ has no pair
with first component $x$.

Formalized by `Cslib.Decidability.finFun`, a definition declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#fin-fun).

## Graphs of finite functions

A finite list $\theta$ of pairs of natural numbers is a graph
when, for every pair $(x, y)$ in $\theta$, the finite function of $\theta$ takes the value $y$ at
$x$; that is, the first pair in $\theta$ with first component $x$ is $(x, y)$.

Formalized by `Cslib.Decidability.IsGraph`, a definition declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#is-graph).

## Being a graph is recursively enumerable

The set of finite lists of pairs of natural
numbers that are graphs is recursively enumerable.

This set is in fact decidable.

Formalized by `Cslib.Decidability.rePred_isGraph`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#re-pred-is-graph).

## Finite-domain partial functions are finite functions

For every partial function
$g : \mathbb{N} \rightharpoonup \mathbb{N}$ with finite domain there is a finite list $\theta$ of
pairs of natural numbers such that the finite function of $\theta$ is $g$ and, for every pair
$(x, y)$ in $\theta$, $g(x)$ is defined and equals $y$.

Formalized by `Cslib.Decidability.exists_finFun_eq`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#exists-fin-fun-eq).

## Extending a finite list of pairs is recursively enumerable

The set of pairs
$(c, \theta)$, where $c$ is a code of a partial recursive function and $\theta$ is a finite list of
pairs of natural numbers, such that for every pair $(x, y)$ in $\theta$ the function computed by
$c$ is defined at $x$ with value $y$, is recursively enumerable.

Formalized by `Cslib.Decidability.rePred_subgraph`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#re-pred-subgraph).

## Effective Rice–Shapiro, sufficiency

Let $C$ be a class of partial functions
$\mathbb{N} \rightharpoonup \mathbb{N}$ and let $B$ be a recognizable set of finite lists of pairs
of natural numbers. Suppose that a partial recursive function $f$ is in $C$ if and only if some
$\theta \in B$ satisfies: for every pair $(x, y)$ in $\theta$, $f(x)$ is defined and equals $y$.
Then the index set of $C$, the set of codes $c$ of partial recursive functions such that the
function computed by $c$ is in $C$, is recognizable.

Formalized by `Cslib.Decidability.tm2Recognizable_of_basis`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#tm2-recognizable-of-basis).

## Effective Rice–Shapiro, necessity

Let $C$ be a class of partial functions
$\mathbb{N} \rightharpoonup \mathbb{N}$ whose index set, the set of codes $c$ of partial
recursive functions such that the function computed by $c$ is in $C$, is recognizable. Then there
is a recognizable set $B$ of finite lists of pairs of natural numbers, each of which is a graph,
such that a partial recursive function $f$ is in $C$ if and only if some $\theta \in B$
satisfies: for every pair $(x, y)$ in $\theta$, $f(x)$ is defined and equals $y$.

Formalized by `Cslib.Decidability.exists_basis_of_tm2Recognizable`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#exists-basis-of-tm2-recognizable).

## The effective Rice–Shapiro theorem

A class of partial functions has a recognizable index
set iff, among partial recursive functions, its members are exactly the extensions of the finite
functions in some recognizable set of graphs.

Formalized by `Cslib.Decidability.tm2Recognizable_iff_exists_basis`, a theorem declared in [CSLibExt/Computability/Decidability/RiceShapiro.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Decidability/RiceShapiro.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html#tm2-recognizable-iff-exists-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rice–Shapiro theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/computability/rice-shapiro-theorem)
