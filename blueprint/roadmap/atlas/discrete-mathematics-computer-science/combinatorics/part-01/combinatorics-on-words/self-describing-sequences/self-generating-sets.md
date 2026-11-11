---
declaration: section
origin: cited
lean: MetaMathlibExt.SelfGeneratingSet.StrictGrowth, MetaMathlibExt.SelfGeneratingSet.SG, MetaMathlibExt.SelfGeneratingSet.FixedPoint, MetaMathlibExt.SelfGeneratingSet.Gen, MetaMathlibExt.SelfGeneratingSet.GeneratedSet, MetaMathlibExt.SelfGeneratingSet.fixedPoint_isSG, MetaMathlibExt.SelfGeneratingSet.generated_isSG, MetaMathlibExt.SelfGeneratingSet.generated_le_of_sg
statement: formalized
proof: formalized
---

# Self-generating sets

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html).

## Strict growth of a set of generators

A finite set $F$ of functions
$\mathbb{N} \to \mathbb{N}$ has strict growth when $x < f(x)$ for every $f \in F$ and every
$x \in \mathbb{N}$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.StrictGrowth`, a definition declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#strict-growth).

## Self-generating sets

Let $F$ be a finite set of functions $\mathbb{N} \to \mathbb{N}$
and let $s \in \mathbb{N}$. A set $\Gamma \subseteq \mathbb{N}$ is self-generating for $s$ and $F$
when $s \in \Gamma$ and $f(x) \in \Gamma$ for every $f \in F$ and every $x \in \Gamma$.

The source writes this condition as $\mathrm{SG}(s, F)$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.SG`, a definition declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#sg).

## Fixed-point sets for a seed and generators

Let $F$ be a finite set of functions
$\mathbb{N} \to \mathbb{N}$ and let $s \in \mathbb{N}$. A set $C \subseteq \mathbb{N}$ is a
fixed-point set for $F$ and $s$ when, for every $y \in \mathbb{N}$, $y \in C$ if and only if
$y = s$ or $y = f(x)$ for some $f \in F$ and some $x \in C$; equivalently,
$C = \{s\} \cup \bigcup_{f \in F} f(C)$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.FixedPoint`, a definition declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#fixed-point).

## Reachability from a seed by generators

Let $F$ be a finite set of functions
$\mathbb{N} \to \mathbb{N}$ and let $s \in \mathbb{N}$. Reachability from $s$ is the least
predicate on $\mathbb{N}$ that holds at $s$ and holds at $f(w)$ whenever it holds at $w$ and
$f \in F$. Thus $y$ is reachable exactly when $y = f_k(\cdots f_1(s) \cdots)$ for some $k \ge 0$
and $f_1, \ldots, f_k \in F$; the case $k = 0$ is $s$ itself.

Formalized by `MetaMathlibExt.SelfGeneratingSet.Gen`, an inductive type declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#gen).

## Set generated from a seed

For a finite set $F$ of functions $\mathbb{N} \to \mathbb{N}$
and a seed $s \in \mathbb{N}$, the set generated from $s$ by $F$ consists of all numbers
$f_k(\cdots f_1(s) \cdots)$ with $k \ge 0$ and $f_1, \dots, f_k \in F$; the case $k = 0$ gives
$s$ itself.

Formalized by `MetaMathlibExt.SelfGeneratingSet.GeneratedSet`, a definition declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#generated-set).

## Fixed-point sets are self-generating

Let $F$ be a finite set of functions
$\mathbb{N} \to \mathbb{N}$ and $s \in \mathbb{N}$. Every fixed-point set $C$ for $F$ and $s$ is
self-generating: $s \in C$, and $f(x) \in C$ for every $f \in F$ and every $x \in C$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.fixedPoint_isSG`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#fixed-point-is-sg).

## The generated set is self-generating

Let $F$ be a finite set of functions
$\mathbb{N} \to \mathbb{N}$ and $s \in \mathbb{N}$. The set generated from $s$ by $F$ contains $s$
and is closed under every $f \in F$: if $x$ is in it and $f \in F$, then $f(x)$ is in it.

Formalized by `MetaMathlibExt.SelfGeneratingSet.generated_isSG`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#generated-is-sg).

## The generated set lies in every self-generating set

Let $F$ be a finite set of
functions $\mathbb{N} \to \mathbb{N}$ and let $s \in \mathbb{N}$. If a set $G \subseteq \mathbb{N}$
contains $s$ and satisfies $f(x) \in G$ for every $f \in F$ and every $x \in G$, then $G$ contains
the set generated from $s$ by $F$, that is, every number obtained from $s$ by applying finitely
many (possibly no) functions of $F$ in succession.

Formalized by `MetaMathlibExt.SelfGeneratingSet.generated_le_of_sg`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#generated-le-of-sg).

## The generated set is a fixed-point set

Let $F$ be a finite set of functions
$\mathbb{N} \to \mathbb{N}$ and $s \in \mathbb{N}$, and let $\Gamma$ be the set generated from $s$
by $F$. Then for every $y \in \mathbb{N}$, $y \in \Gamma$ if and only if $y = s$ or $y = f(x)$
for some $f \in F$ and $x \in \Gamma$.

This direction does not require the generators to be strictly increasing.

Formalized by `MetaMathlibExt.SelfGeneratingSet.generated_fixedPoint`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#generated-fixed-point).

## Under strict growth, a fixed-point set is the generated set

Let $F$ be a finite set of
functions $\mathbb{N} \to \mathbb{N}$ with $x < f(x)$ for every $f \in F$ and every
$x \in \mathbb{N}$, let $s \in \mathbb{N}$, and let $C \subseteq \mathbb{N}$ be a fixed-point set
for $F$ and $s$: $y \in C$ exactly when $y = s$ or $y = f(x)$ for some $f \in F$ and $x \in C$.
Then $C$ equals the set generated from $s$ by $F$, the numbers obtained from $s$ by applying
finitely many functions of $F$.

The proof is by strong induction: if an element of $C$ is $f(x)$ with $f \in F$ and $x \in C$,
then strict growth gives $x < f(x)$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.fixedPoint_eq_generated`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#fixed-point-eq-generated).

## The generated set is the intersection of all self-generating sets

Let $F$ be a finite
set of functions $\mathbb{N} \to \mathbb{N}$ and $s \in \mathbb{N}$. The set generated from $s$ by
$F$ equals the intersection of all sets $G \subseteq \mathbb{N}$ that contain $s$ and are closed
under every $f \in F$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.generated_eq_sInter`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#generated-eq-s-inter).

## Under strict growth, a fixed-point set is the intersection of all self-generating sets

Let $F$ be a finite set of functions $\mathbb{N} \to \mathbb{N}$ with $x < f(x)$ for every
$f \in F$ and every $x \in \mathbb{N}$, and let $s \in \mathbb{N}$. If $C$ is a fixed-point set for
$F$ and $s$, then $C$ is the intersection of all sets $G \subseteq \mathbb{N}$ that contain $s$
and are closed under every $f \in F$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.fixedPoint_eq_sInter`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#fixed-point-eq-s-inter).

## Under strict growth, a fixed-point set is the least self-generating set

Let $F$ be a
finite set of functions $\mathbb{N} \to \mathbb{N}$ with $x < f(x)$ for every $f \in F$ and every
$x \in \mathbb{N}$, and let $s \in \mathbb{N}$. If $C$ is a fixed-point set for $F$ and $s$, then
$C$ contains $s$ and is closed under every $f \in F$, and $C \subseteq G$ for every set
$G \subseteq \mathbb{N}$ that contains $s$ and is closed under every $f \in F$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.fixedPoint_isLeast`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#fixed-point-is-least).

## The least self-generating set is the generated set

Let $F$ be a finite set of
functions $\mathbb{N} \to \mathbb{N}$ and let $s \in \mathbb{N}$. Call a set
$G \subseteq \mathbb{N}$ self-generating if $s \in G$ and $f(x) \in G$ for every $f \in F$ and
every $x \in G$. If $C$ is self-generating and is contained in every self-generating set, then
$C$ equals the set generated from $s$ by $F$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.isLeast_eq_generated`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#is-least-eq-generated).

## Under strict growth, fixed-point sets are unique

Let $F$ be a finite set of functions
$\mathbb{N} \to \mathbb{N}$ with $x < f(x)$ for every $f \in F$ and every $x \in \mathbb{N}$, and
let $s \in \mathbb{N}$. If $C_1$ and $C_2$ are both fixed-point sets for $F$ and $s$, then
$C_1 = C_2$.

Formalized by `MetaMathlibExt.SelfGeneratingSet.fixedPoint_unique`, a theorem declared in [MathlibExt/Combinatorics/SelfGeneratingSet.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SelfGeneratingSet.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html#fixed-point-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Self-generating sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/self-generating-sets)
