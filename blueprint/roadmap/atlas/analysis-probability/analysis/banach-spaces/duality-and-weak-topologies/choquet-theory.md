---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Convex.ChoquetWanted.choquet_representation_of_isCompact, MathlibExt.Analysis.Convex.ChoquetWanted.choquet_representation, MathlibExt.Analysis.ChoquetWanted.Analysis.choquet, MathlibExt.Analysis.ChoquetWanted.Analysis.bauer_unique
statement: formalized
---

# Choquet theory

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory/index.html).

## Choquet representation for compact sets

Let $E$ be a second-countable real Banach space
with its Borel σ-algebra and let $K \subseteq E$ be compact. For every $x \in K$ there is a
probability measure $\mu$ on $E$ such that the set $\operatorname{ext} K$ of extreme points of
$K$ has $\mu(\operatorname{ext} K) = 1$, the identity map $y \mapsto y$ is Bochner integrable
for $\mu$, and $\int_E y \, d\mu(y) = x$.

Neither convexity nor nonemptiness of $K$ is assumed; Choquet's theorem for nonempty compact
convex sets is the special case.

Formalized by `MathlibExt.Analysis.Convex.ChoquetWanted.choquet_representation_of_isCompact`, a theorem declared in [MathlibExt/Analysis/Convex/Choquet.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/Choquet.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory/index.html#choquet-representation-of-is-compact).

## Choquet's theorem

Let $E$ be a second-countable real Banach space with its Borel σ-algebra
and let $K \subseteq E$ be a nonempty compact convex set. For every $x \in K$ there is a
probability measure $\mu$ on $E$ such that the set $\operatorname{ext} K$ of extreme points of
$K$ has $\mu(\operatorname{ext} K) = 1$, the identity map $y \mapsto y$ is Bochner integrable
for $\mu$, and $\int_E y \, d\mu(y) = x$.

## Sources

- G. Choquet, Seminaire Bourbaki 1956 and Lectures 1962; Bishop-de Leeuw and Choquet-Bishop-de Leeuw integral representation; Phelps, Lectures on Choquet's Theorem, 1966; Lean states compact-source specialization in second-countable real Banach space with `ProbabilityMeasure` carried by `extremePoints` and Bochner integral barycenter.

Formalized by `MathlibExt.Analysis.Convex.ChoquetWanted.choquet_representation`, a theorem declared in [MathlibExt/Analysis/Convex/Choquet.lean, line 784](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/Choquet.lean#L784). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory/index.html#choquet-representation).

## Choquet's representation theorem in Banach spaces

Let $X$ be a real Banach space with its
Borel σ-algebra and let $K \subseteq X$ be compact and convex. For every $x \in K$ there is a
probability measure $\mu$ on $X$ such that the complement of the set of extreme points of $K$ has
$\mu$-measure $0$ and the barycenter $\int y \, d\mu(y)$ (a Bochner integral) equals $x$.

## Sources

- G. Choquet, *Existence et unicité des représentations intégrales au moyen des points extrémaux dans les cônes convexes*, Séminaire Bourbaki (1956). Knill, *Some fundamental theorems in mathematics*, §88. Problem `choquet_representation_theorem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.ChoquetWanted.Analysis.choquet` is written with `theorem_wanted` in [WantedExt/Analysis/ChoquetWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ChoquetWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory/index.html#choquet).

## Bauer's uniqueness theorem at extreme points

Let $X$ be a real Banach space with its Borel
σ-algebra, let $K \subseteq X$ be compact and convex, and let $x$ be an extreme point of $K$. If
$\mu$ is a probability measure on $X$ with $\mu(X \setminus K) = 0$ whose barycenter
$\int y \, d\mu(y)$ (a Bochner integral) equals $x$, then $\mu$ is the Dirac measure at $x$.

## Sources

- H. Bauer, *Minimalstellen von Funktionen und Extremalpunkte*, Arch. Math. 9 (1958), 389–393; see also Phelps, *Lectures on Choquet's Theorem*. Knill, *Some fundamental theorems in mathematics*, §88. Problem `bauer_extreme_point_uniqueness` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.ChoquetWanted.Analysis.bauer_unique` is written with `theorem_wanted` in [WantedExt/Analysis/ChoquetWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ChoquetWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory/index.html#bauer-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Choquet theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/choquet-theory)
