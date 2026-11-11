---
declaration: section
origin: cited
lean: MetaMathlibExt.modelConds, MetaMathlibExt.modelSets, MetaMathlibExt.IsCompatible, MetaMathlibExt.IsPredenseBelow, MetaMathlibExt.IsGenericFor, MetaMathlibExt.IsProperForcing, MetaMathlibExt.ProperForcingAxiom
statement: formalized
proof: formalized
---

# Proper forcing and the proper forcing axiom

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html).

## Conditions in a model

Let $\mathbb{P}$ be a set and $M$ a subset of the disjoint union
$\mathbb{P} \sqcup \mathcal{P}(\mathbb{P})$. The conditions in $M$ form the set $M_c$ of those
$p \in \mathbb{P}$ whose copy in the disjoint union belongs to $M$; informally,
$M_c = M \cap \mathbb{P}$.

Formalized by `MetaMathlibExt.modelConds`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#model-conds).

## Sets of conditions in a model

Let $\mathbb{P}$ be a set and $M$ a subset of the disjoint
union $\mathbb{P} \sqcup \mathcal{P}(\mathbb{P})$. The sets of conditions in $M$ form the family
$M_s$ of those $D \subseteq \mathbb{P}$ whose copy in the disjoint union belongs to $M$;
informally, $M_s = M \cap \mathcal{P}(\mathbb{P})$.

Formalized by `MetaMathlibExt.modelSets`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#model-sets).

## Compatible conditions

Two elements $p$ and $q$ of a partial order $\mathbb{P}$ are
compatible if there is $r \in \mathbb{P}$ with $r \le p$ and $r \le q$.

Formalized by `MetaMathlibExt.IsCompatible`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#is-compatible).

## Predense below a condition

A set $A \subseteq \mathbb{P}$ of elements of a partial order
$\mathbb{P}$ is predense below $q \in \mathbb{P}$ if for every $r \le q$ there is $a \in A$ such
that $r$ and $a$ are compatible.

Formalized by `MetaMathlibExt.IsPredenseBelow`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#is-predense-below).

## (M, ℙ)-generic conditions

Let $\mathbb{P}$ be a partial order and $M$ a subset of the
disjoint union $\mathbb{P} \sqcup \mathcal{P}(\mathbb{P})$. Write $M_c$ for the set of
$p \in \mathbb{P}$ whose copy in the disjoint union lies in $M$, and $M_s$ for the set of
$D \subseteq \mathbb{P}$ whose copy lies in $M$. A condition $q \in \mathbb{P}$ is
$(M, \mathbb{P})$-generic if for every $D \in M_s$ that is dense in $\mathbb{P}$ (every element
of $\mathbb{P}$ has an element of $D$ below it), the set $D \cap M_c$ is predense below $q$: for
every $r \le q$ there are $a \in D \cap M_c$ and $s \in \mathbb{P}$ with $s \le r$ and $s \le a$.

No condition is imposed on $M$ here. In the intended application $M$ is the trace of a countable
elementary submodel of $H(\theta)$, for a sufficiently large regular cardinal $\theta$, that
contains $\mathbb{P}$; genericity depends only on $M_c$ and $M_s$, and the elementarity is
supplied by the club in the definition of proper partial orders.

Formalized by `MetaMathlibExt.IsGenericFor`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#is-generic-for).

## Proper partial orders

Let $\mathbb{P}$ be a partial order and let $X$ be the disjoint
union $\mathbb{P} \sqcup \mathcal{P}(\mathbb{P})$; for $M \subseteq X$ write $M_c$ for the set of
$p \in \mathbb{P}$ whose copy in $X$ lies in $M$. Then $\mathbb{P}$ is proper if there is a club
$C$ in $[X]^\omega$ such that for every $M \in C$ and every $p \in M_c$ there is an
$(M, \mathbb{P})$-generic condition $q \le p$. Here a club in $[X]^\omega$ is a family of
countable subsets of $X$ such that every countable subset of $X$ is contained in a member of the
family, and the union of every increasing sequence $M_0 \subseteq M_1 \subseteq \cdots$ of
members of the family is again a member.

The usual requirement $\mathbb{P} \in M$ is not imposed: $\mathbb{P}$ is an element of $X$ (as a
subset of itself), and since $C$ is cofinal it has members containing it.

Formalized by `MetaMathlibExt.IsProperForcing`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/Proper.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#is-proper-forcing).

## Proper Forcing Axiom

For every proper partial order $\mathbb{P}$, every family
$\mathcal{D}$ of at most $\aleph_1$ dense subsets of $\mathbb{P}$, and every condition
$p \in \mathbb{P}$, there is a filter $G \subseteq \mathbb{P}$ with $p \in G$ that meets every
member of $\mathcal{D}$, that is, $G \cap D \neq \emptyset$ for every $D \in \mathcal{D}$.

Here a set $D \subseteq \mathbb{P}$ is dense if for every $q \in \mathbb{P}$ there is $d \in D$
with $d \le q$, and a filter is a nonempty, upward closed subset $G$ of $\mathbb{P}$ such that
any two elements of $G$ have a common lower bound in $G$.

Formalized by `MetaMathlibExt.ProperForcingAxiom`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/ProperForcingAxiom.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Forcing/ForcingAxioms/ProperForcingAxiom.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html#proper-forcing-axiom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Proper forcing and the proper forcing axiom](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/forcing/proper-forcing-and-the-proper-forcing-axiom)
