---
declaration: section
origin: cited
lean: IsArithFrobAt.eq_of_inertia_eq_bot, IsArithFrobAt.existsUnique_of_inertia_eq_bot
statement: formalized
proof: formalized
---

# Frobenius elements under trivial inertia

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-under-trivial-inertia/index.html).

## Frobenius elements coincide when inertia is trivial

Let $R$ and $S$ be commutative rings
with $S$ an $R$-algebra, let a group $G$ act on $S$ by $R$-algebra automorphisms, and let $Q$ be
an ideal of $S$. Write $P$ for the preimage of $Q$ in $R$ and $q$ for the number of elements of
$R/P$ (with $q = 0$ when $R/P$ is infinite). Call $\sigma \in G$ an arithmetic Frobenius element at
$Q$ if $\sigma x - x^q \in Q$ for all $x \in S$, and call the inertia subgroup of $Q$ the set of
$\tau \in G$ with $\tau x - x \in Q$ for all $x \in S$. If $\sigma, \sigma' \in G$ are arithmetic
Frobenius elements at $Q$ and the inertia subgroup of $Q$ is trivial, then $\sigma = \sigma'$.

Formalized by `IsArithFrobAt.eq_of_inertia_eq_bot`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Unique.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Frobenius/Unique.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-under-trivial-inertia/index.html#eq-of-inertia-eq-bot).

## Existence and uniqueness of the Frobenius element under trivial inertia

Let $R$ and $S$
be commutative rings with $S$ an $R$-algebra, and let a finite group $G$ act on $S$ by
$R$-algebra automorphisms such that every element of $S$ fixed by $G$ is the image of an element
of $R$. Let $Q$ be a prime ideal of $S$ with $S/Q$ finite, write $P$ for the preimage of $Q$ in
$R$ and $q$ for the number of elements of $R/P$. Call $\sigma \in G$ an arithmetic Frobenius
element at $Q$ if $\sigma x - x^q \in Q$ for all $x \in S$. If the inertia subgroup of $Q$, the set
of $\tau \in G$ with $\tau x - x \in Q$ for all $x \in S$, is trivial, then there is exactly one
arithmetic Frobenius element at $Q$ in $G$.

Formalized by `IsArithFrobAt.existsUnique_of_inertia_eq_bot`, a theorem declared in [MathlibExt/RingTheory/Frobenius/Unique.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Frobenius/Unique.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-under-trivial-inertia/index.html#exists-unique-of-inertia-eq-bot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frobenius elements under trivial inertia](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-under-trivial-inertia/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/frobenius-elements/frobenius-elements-under-trivial-inertia)
