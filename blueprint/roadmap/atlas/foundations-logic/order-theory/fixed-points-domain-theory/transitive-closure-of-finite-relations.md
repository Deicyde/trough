---
declaration: section
origin: cited
lean: Relation.postFin, Relation.transGenStep, Relation.transGenFinFrom, Relation.transGenFin, Relation.mem_transGenFinFrom, Relation.mem_transGenFin, Relation.decidableTransGen, Relation.decidableReflTransGen
statement: formalized
proof: formalized
---

# Transitive closure of finite relations

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html).

## Successors of a finite set

Let $\alpha$ be a finite type and let $r$ be a decidable
relation on $\alpha$. For a finite set $Z \subseteq \alpha$, the set of $r$-successors of $Z$ is
the finite set $\mathrm{post}_r(Z) = \{t \in \alpha \mid r(z, t) \text{ for some } z \in Z\}$.

Formalized by `Relation.postFin`, a definition declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#post-fin).

## One step of the reachability iteration

Let $\alpha$ be a finite type with decidable
equality, let $r$ be a decidable relation on $\alpha$, and write $\mathrm{post}_r(Z)$ for the set
of $r$-successors of elements of a finite set $Z \subseteq \alpha$. For a finite set
$A \subseteq \alpha$, the step map sends a finite set $Z \subseteq \alpha$ to
$\mathrm{post}_r(A) \cup \mathrm{post}_r(Z)$.

Its least fixed point is the set of elements reachable from $A$ in one or more $r$-steps.

Formalized by `Relation.transGenStep`, a definition declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#trans-gen-step).

## Elements reachable from a finite set of sources

Let $\alpha$ be a finite type with
decidable equality, let $r$ be a decidable relation on $\alpha$, and let $A \subseteq \alpha$ be a
finite set. Write $\mathrm{post}_r(Z)$ for the set of $r$-successors of elements of a finite set
$Z \subseteq \alpha$, and let $f$ be the step map
$f(Z) = \mathrm{post}_r(A) \cup \mathrm{post}_r(Z)$. The finite set of elements reachable from
$A$ is $f^{|\alpha|}(\emptyset)$, obtained by applying $f$ to the empty set $|\alpha|$ times,
where $|\alpha|$ is the number of elements of $\alpha$.

Since $f$ is monotone, this is the least fixed point of $f$; it consists of the elements
reachable from some element of $A$ in one or more $r$-steps.

Formalized by `Relation.transGenFinFrom`, a definition declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#trans-gen-fin-from).

## Elements reachable from a point

Let $\alpha$ be a finite type with decidable equality,
let $r$ be a decidable relation on $\alpha$, and let $a \in \alpha$. The finite set of elements
reachable from $a$ is the finite set of elements reachable from the source set $\{a\}$, that is,
the elements reachable from $a$ in one or more $r$-steps.

Formalized by `Relation.transGenFin`, a definition declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#trans-gen-fin).

## Membership in the set reachable from finitely many sources

Let $\alpha$ be a finite type
with decidable equality, let $r$ be a decidable relation on $\alpha$, and let $A \subseteq \alpha$
be a finite set. An element $t \in \alpha$ lies in the finite set of elements reachable from $A$
in one or more $r$-steps (computed as a finite least fixed point) if and only if there is some
$a \in A$ such that $(a, t)$ lies in the transitive closure of $r$.

Formalized by `Relation.mem_transGenFinFrom`, a theorem declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#mem-trans-gen-fin-from).

## Membership in the set reachable from a point

Let $\alpha$ be a finite type with
decidable equality, let $r$ be a decidable relation on $\alpha$, and let $a \in \alpha$. An
element $t \in \alpha$ lies in the finite set of elements reachable from $a$ in one or more
$r$-steps (computed as a finite least fixed point) if and only if $(a, t)$ lies in the transitive
closure of $r$.

Formalized by `Relation.mem_transGenFin`, a theorem declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#mem-trans-gen-fin).

## Decidability of the transitive closure on a finite type

Let $\alpha$ be a finite type
with decidable equality and let $r$ be a decidable relation on $\alpha$. Then the transitive
closure of $r$ is decidable: for all $a, t \in \alpha$ it is decidable whether $t$ is reachable
from $a$ in one or more $r$-steps.

The decision is membership of $t$ in the finite set of elements reachable from $a$.

Formalized by `Relation.decidableTransGen`, a definition declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#decidable-trans-gen).

## Decidability of the reflexive-transitive closure on a finite type

Let $\alpha$ be a
finite type with decidable equality and let $r$ be a decidable relation on $\alpha$. Then the
reflexive-transitive closure of $r$ is decidable: for all $a, t \in \alpha$ it is decidable
whether $t$ is reachable from $a$ in zero or more $r$-steps.

Formalized by `Relation.decidableReflTransGen`, a definition declared in [MathlibExt/Logic/Relation/FiniteReachability.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Logic/Relation/FiniteReachability.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html#decidable-refl-trans-gen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Transitive closure of finite relations](https://deicyde.github.io/atlas-lean/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Order/fixed-points-domain-theory/transitive-closure-of-finite-relations)
