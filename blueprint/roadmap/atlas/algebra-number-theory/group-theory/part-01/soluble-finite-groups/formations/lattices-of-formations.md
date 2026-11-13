---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.GroupClass, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsFormation, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.Incl, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsCompleteLatticeOfFormations, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsJoinIn, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsCompactIn, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsAlgebraicIn, MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsModularIn
statement: formalized
---

# Lattices of formations

28 results, 24 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html).

## Isomorphism-closed classes of groups (Kourovka 18.92)

A class of groups $\mathfrak{X}$ is
given by a membership predicate on groups whose underlying type lies in the lowest universe, such
that whenever a group $H$ belongs to $\mathfrak{X}$ and $K$ is a group isomorphic to $H$, the group
$K$ also belongs to $\mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.GroupClass`, a structure declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#group-class).

## Formations of finite groups (Kourovka 18.92)

A class $\mathfrak{X}$ of groups is a
formation if every group in $\mathfrak{X}$ is finite, $\mathfrak{X}$ contains the trivial group,
for every finite group $G$ in $\mathfrak{X}$ and every normal subgroup $N$ of $G$ the quotient
$G/N$ lies in $\mathfrak{X}$, and for every finite group $G$ with normal subgroups $N_1$ and $N_2$
such that $G/N_1$ and $G/N_2$ lie in $\mathfrak{X}$, the quotient $G/(N_1 \cap N_2)$ lies in
$\mathfrak{X}$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-formation).

## Inclusion of group classes

For classes of groups $\mathfrak{X}$ and $\mathfrak{Y}$, the
class $\mathfrak{X}$ is included in $\mathfrak{Y}$, written $\mathfrak{X} \subseteq \mathfrak{Y}$,
if every group that belongs to $\mathfrak{X}$ also belongs to $\mathfrak{Y}$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.Incl`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#incl).

## Complete lattices of formations

A set $\Theta$ of classes of groups is a complete lattice
of formations if it is nonempty, every member of $\Theta$ is a formation, for every nonempty subset
$S \subseteq \Theta$ the intersection of the classes in $S$ (the class of groups belonging to every
member of $S$) belongs to $\Theta$, and $\Theta$ has a member that contains every member of
$\Theta$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsCompleteLatticeOfFormations`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-complete-lattice-of-formations).

## Joins in a set of group classes

Let $\Theta$ and $S$ be sets of classes of groups. A class
$\mathfrak{J}$ is the join of $S$ in $\Theta$ if $\mathfrak{J} \in \Theta$, every member of $S$ is
contained in $\mathfrak{J}$, and $\mathfrak{J}$ is contained in every member of $\Theta$ that
contains every member of $S$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsJoinIn`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-join-in).

## Compact elements of a set of group classes

Let $\Theta$ be a set of classes of groups and
$\mathfrak{A}$ a class of groups. Then $\mathfrak{A}$ is compact in $\Theta$ if, for every subset
$S \subseteq \Theta$ and every join $\mathfrak{J}$ of $S$ in $\Theta$ with
$\mathfrak{A} \subseteq \mathfrak{J}$, there are a finite subset $S_1 \subseteq S$ and a join
$\mathfrak{J}_1$ of $S_1$ in $\Theta$ with $\mathfrak{A} \subseteq \mathfrak{J}_1$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsCompactIn`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-compact-in).

## Algebraic sets of group classes

A set $\Theta$ of classes of groups is algebraic if every
member $\mathfrak{A}$ of $\Theta$ is the join in $\Theta$ of some subset $S \subseteq \Theta$ all of
whose members are compact in $\Theta$.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsAlgebraicIn`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-algebraic-in).

## Modular sets of group classes

A set $\Theta$ of classes of groups is modular if for all
$\mathfrak{A}, \mathfrak{B}, \mathfrak{C} \in \Theta$ with $\mathfrak{A} \subseteq \mathfrak{C}$
the following holds: whenever $\mathfrak{J}_1$ is the join in $\Theta$ of the set
$\{\mathfrak{A}, \mathfrak{B} \cap \mathfrak{C}\}$ and $\mathfrak{D}$ is the join in $\Theta$ of
the set $\{\mathfrak{A}, \mathfrak{B}\}$, the classes $\mathfrak{J}_1$ and
$\mathfrak{D} \cap \mathfrak{C}$ contain the same groups. This is the modular law
$\mathfrak{A} \vee (\mathfrak{B} \wedge \mathfrak{C}) = (\mathfrak{A} \vee \mathfrak{B}) \wedge
\mathfrak{C}$, with joins taken in $\Theta$ and meets the intersections.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.IsModularIn`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-modular-in).

## Kourovka Problem 18.92(a) (A. N. Skiba)

The proposition that some set $\Theta$ of classes
of groups is a complete lattice of formations of finite groups and is not algebraic.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.nonAlgebraicCompleteLatticeOfFormations`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#non-algebraic-complete-lattice-of-format).

## The non-modular formation lattice problem (Kourovka 18.92(b), A. N. Skiba)

The proposition
that there is a complete lattice of formations of finite groups that is not modular, joins being
least upper bounds in the lattice and meets being intersections.

Formalized by `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.nonModularCompleteLatticeOfFormations`, a definition declared in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#non-modular-complete-lattice-of-formatio).

## Non-algebraic complete lattices of formations exist

There is a set $\Theta$ of classes of
groups that is a complete lattice of formations of finite groups and is not algebraic; that is,
Kourovka Problem 18.92(a) has a positive answer.

The Kourovka Notebook (21st issue) answers 18.92(a) "Yes", by an AI-generated solution confirmed by
A. N. Skiba (Kinyon–Urban, 2026): for a set $S$ of primes let $\mathfrak{F}_S$ be the class of
finite groups whose order has all its prime divisors in $S$; the classes $\mathfrak{F}_S$ with $S$
finite, together with the class of all finite groups, form a complete lattice of formations whose
only compact element is the bottom.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.92 (A. N. Skiba); resolution: M. Kinyon and J. Urban, Results on problems from the Kourovka Notebook, preprint, version 4, 19 September 2026, Section 3.29 (Problem 18.92): with F_S the finite groups whose order has all prime divisors in S, {F_S : S finite} ∪ {F_P} is not algebraic and the formations with prime sets ∅, {2}, {2, 3}, {5}, P form a pentagon N_5; an AI solution confirmed by A. N. Skiba, accepted in the Kourovka Notebook (21st issue), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.nonAlgebraicCompleteLatticeOfFormations_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#non-algebraic-complete-lattice-of-format-2).

## A non-modular complete lattice of formations exists (Kourovka 18.92(b))

There is a complete
lattice of formations of finite groups that is not modular: a nonempty set $\Theta$ of formations
of finite groups, ordered by inclusion, that contains the intersection of each of its nonempty
subsets and has a largest element, in which the modular law $A \vee (B \wedge C) = (A \vee B)
\wedge C$ for $A \le C$ fails, joins being least upper bounds in $\Theta$ and meets intersections.

The Kourovka Notebook (21st issue) answers 18.92(b) "Yes" (Kinyon-Urban, 2026, confirmed by A. N.
Skiba): writing $\mathfrak{F}_S$ for the finite groups whose order has all prime divisors in $S$,
the formations $\mathfrak{F}_S$ with $S = \emptyset, \{2\}, \{2, 3\}, \{5\}$ and $S$ the set of all
primes are closed under intersections and form the pentagon $N_5$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 18.92 (A. N. Skiba); resolution: M. Kinyon and J. Urban, Results on problems from the Kourovka Notebook, preprint, version 4, 19 September 2026, Section 3.29 (Problem 18.92): with F_S the finite groups whose order has all prime divisors in S, {F_S : S finite} ∪ {F_P} is not algebraic and the formations with prime sets ∅, {2}, {2, 3}, {5}, P form a pentagon N_5; an AI solution confirmed by A. N. Skiba, accepted in the Kourovka Notebook (21st issue), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.CompleteLatticeOfFormationsKourovka18Problem92Wanted.nonModularCompleteLatticeOfFormations_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CompleteLatticeOfFormationsKourovka18Problem92Wanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#non-modular-complete-lattice-of-formatio-2).

## Class of finite groups (Kourovka 13.51)

A class of finite groups is a property of finite
groups: for each finite group $G$ it states whether $G$ belongs to the class.

Closure under isomorphism is not part of the definition.

Formalized by `MathlibExt.GroupTheory.FiniteModularLatticeFormationsKourovka13Problem51Wanted.FiniteGroupClass`, an abbreviation declared in [WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#finite-group-class).

## Formation of finite groups (Kourovka 13.51)

A class $\mathfrak F$ of finite groups is a
formation when it is closed under homomorphic images (if $G \in \mathfrak F$ and $\varphi : G
\to H$ is a surjective homomorphism of finite groups, then $H \in \mathfrak F$) and, for every
finite group $G$ and normal subgroups $N_1$ and $N_2$ of $G$, $G/N_1 \in \mathfrak F$ and $G/N_2
\in \mathfrak F$ imply $G/(N_1 \cap N_2) \in \mathfrak F$ (closure under finite subdirect
products).

The empty class is a formation.

Formalized by `MathlibExt.GroupTheory.FiniteModularLatticeFormationsKourovka13Problem51Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-formation-2).

## Intersection of classes of finite groups

For classes $\mathfrak F_1$ and $\mathfrak F_2$ of
finite groups, their intersection $\mathfrak F_1 \cap \mathfrak F_2$ is the class of finite
groups $G$ with $G \in \mathfrak F_1$ and $G \in \mathfrak F_2$. For formations $\mathfrak F_1$
and $\mathfrak F_2$ it is their meet in the lattice of formations.

Formalized by `MathlibExt.GroupTheory.FiniteModularLatticeFormationsKourovka13Problem51Wanted.classMeet`, a definition declared in [WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#class-meet).

## Join of formations (Kourovka 13.51)

For classes $\mathfrak F_1$ and $\mathfrak F_2$ of
finite groups, their formation join is the class of finite groups $G$ that belong to every
formation containing all groups of $\mathfrak F_1$ and of $\mathfrak F_2$: the intersection of
all formations containing $\mathfrak F_1 \cup \mathfrak F_2$, which is the smallest such
formation. For formations $\mathfrak F_1$ and $\mathfrak F_2$ it is their join in the lattice of
formations.

Formalized by `MathlibExt.GroupTheory.FiniteModularLatticeFormationsKourovka13Problem51Wanted.formationJoin`, a definition declared in [WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#formation-join).

## Kourovka Problem 13.51 (Skiba): finite modular lattices embed in the lattice of formations

For every finite modular lattice $L$ there is an injective map $f$ from $L$ to the formations of
finite groups such that, for all $a, b \in L$, $f(a \wedge b) = f(a) \cap f(b)$ and $f(a \vee
b)$ is the smallest formation containing $f(a) \cup f(b)$.

The map is not required to preserve the least or the greatest element.

Formalized by `MathlibExt.GroupTheory.FiniteModularLatticeFormationsKourovka13Problem51Wanted.finiteModularLatticeEmbedsInFormations`, a definition declared in [WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#finite-modular-lattice-embeds-in-formati).

## Not every finite modular lattice embeds in the lattice of formations

There is a finite modular
lattice $L$ that admits no injective map $f$ from $L$ to the formations of finite groups such that,
for all $a, b \in L$, $f(a \wedge b) = f(a) \cap f(b)$ and $f(a \vee b)$ is the smallest formation
containing $f(a) \cup f(b)$. This answers Kourovka Problem 13.51 (Skiba) in the negative.

Jayadevan constructs a modular lattice with 184 elements that admits no such map (a six-variable
Desargues implication holds for formations and fails in the lattice); the Kourovka Notebook (21st
issue) answers 13.51 "No, not every" (AI solution confirmed by A. N. Skiba).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 13.51 (A. N. Skiba); resolution: A. Jayadevan, A finite modular lattice not embeddable in the lattice of formations of finite groups, preprint, Zenodo record 22863019 (2026), main theorem: a modular lattice with 184 elements (the dual of an incidence lattice with 91 points and 91 lines) admits no injective map preserving binary meets and joins into the lattice of formations; the Kourovka Notebook (21st issue) marks 13.51 solved (AI solution confirmed by A. N. Skiba), https://zenodo.org/records/22863019.

Stated but not proved: `MathlibExt.GroupTheory.FiniteModularLatticeFormationsKourovka13Problem51Wanted.finiteModularLatticeEmbedsInFormations_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteModularLatticeFormationsKourovka13Problem51Wanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#finite-modular-lattice-embeds-in-formati-2).

## Inclusion of classes of finite groups

For classes $\mathfrak{F}$ and $\mathfrak{G}$ of
finite groups, $\mathfrak{F} \subseteq \mathfrak{G}$ means that every finite group in
$\mathfrak{F}$ belongs to $\mathfrak{G}$.

Formalized by `MathlibExt.GroupTheory.FiniteGroupFormationShared.ClassLE`, a definition declared in [WantedExt/GroupTheory/FiniteGroupFormationShared.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteGroupFormationShared.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#class-le).

## Local formation of finite groups

A class $\mathfrak{F}$ of finite groups is a local
formation when it is a formation, contains the trivial group, and is saturated: a finite group $G$
belongs to $\mathfrak{F}$ whenever $G/\Phi(G)$ does, where $\Phi(G)$ is the Frattini subgroup of
$G$.

By the Gaschütz-Lubeseder-Schmid theorem a nonempty formation of finite groups is local (defined
by a formation function) iff it is saturated.

Formalized by `MathlibExt.GroupTheory.FiniteGroupFormationShared.IsLocalFormation`, a definition declared in [WantedExt/GroupTheory/FiniteGroupFormationShared.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteGroupFormationShared.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-local-formation).

## Residual of a finite group with respect to a class

For a class $\mathfrak{F}$ of finite
groups and a finite group $G$, the $\mathfrak{F}$-residual $G^{\mathfrak{F}}$ is the intersection
of all normal subgroups $N$ of $G$ with $G/N \in \mathfrak{F}$.

For a formation containing the trivial group it is the smallest such $N$.

Formalized by `MathlibExt.GroupTheory.FiniteGroupFormationShared.residual`, a definition declared in [WantedExt/GroupTheory/FiniteGroupFormationShared.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/FiniteGroupFormationShared.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#residual).

## Classes of finite groups (Kourovka 10.56)

A class of finite groups is given by its
membership predicate: a proposition about each finite group, true exactly for the members of the
class.

Formalized by `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.GroupClass`, an abbreviation declared in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#group-class-2).

## Formations of finite groups (Kourovka 10.56)

A class $X$ of finite groups is a formation
if it is closed under isomorphism, contains the trivial group, contains $G/N$ whenever it contains
$G$ and $N$ is a normal subgroup of $G$, and is closed under subdirect products: if $N_1$ and
$N_2$ are normal subgroups of a finite group $G$ with $G/N_1 \in X$ and $G/N_2 \in X$, then
$G/(N_1 \cap N_2) \in X$.

Formalized by `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.IsFormation`, a definition declared in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-formation-3).

## Formations of nilpotent groups of class at most 4

A class $X$ of finite groups is a
formation of nilpotent groups of class at most $4$ if $X$ is a formation and every group $G$ in
$X$ is nilpotent of class at most $4$, that is, the fourth term $\zeta_4(G)$ of the upper central
series of $G$ is all of $G$.

Formalized by `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.IsNilpotentClassFourFormation`, a definition declared in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#is-nilpotent-class-four-formation).

## Intersection of classes of finite groups (Kourovka 10.56)

The meet of two classes $X$ and
$Y$ of finite groups is their intersection $X \cap Y$: the class of finite groups that belong to
both $X$ and $Y$.

Formalized by `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.meet`, a definition declared in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#meet).

## Formation generated by two classes (Kourovka 10.56)

For classes $X$ and $Y$ of finite
groups, the formation generated by $X \cup Y$ is the class of finite groups that belong to every
formation containing both $X$ and $Y$. For formations $X$ and $Y$ it is their join in the lattice
of formations.

Formalized by `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.formationJoin`, a definition declared in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#formation-join-2).

## The distributivity question for nilpotent class-4 formations (Kourovka 10.56)

For all
formations $A$, $B$, $C$ of finite nilpotent groups of class at most $4$, a finite group lies in
$A \cap (B \vee C)$ if and only if it lies in $(A \cap B) \vee (A \cap C)$, where $X \vee Y$ denotes
the formation generated by $X \cup Y$. That is, the lattice of formations of finite nilpotent
groups of class at most $4$ is distributive (A. N. Skiba).

Formalized by `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.nilpotentClassFourFormationsDistributive`, a definition declared in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#nilpotent-class-four-formations-distribu).

## The lattice of nilpotent class-4 formations is not distributive (Kourovka 10.56)

There
exist formations $A$, $B$, $C$ of finite nilpotent groups of class at most $4$ such that the
classes $A \cap (B \vee C)$ and $(A \cap B) \vee (A \cap C)$ differ, that is, some finite group
lies in exactly one of them; here $X \vee Y$ denotes the formation generated by $X \cup Y$, the
intersection of all formations containing $X$ and $Y$.

The Kourovka Archive answers Problem 10.56 "No": the lattice of varieties of nilpotent $2$-groups
of class at most $4$ is not distributive (Belov; Bryce), and $\mathfrak{V} \mapsto \mathfrak{V}
\cap \mathfrak{F}$, where $\mathfrak{F}$ is the class of finite groups, embeds it in the lattice
of formations (Kovács), with image among the formations of finite nilpotent groups of class at
most $4$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.56 (A. N. Skiba); resolution: Yu. A. Belov, Algebra and Logic 9, no. 6 (1970), 371-374; R. A. Bryce, Philos. Trans. Roy. Soc. London (A) 266 (1970), 281-355, footnote on p. 335; L. Kovács, letter of 12 May 1988, Kourovka Archive, Problem 10.56 ("No"): the lattice of varieties of nilpotent 2-groups of class ≤ 4 is non-distributive, and V ↦ V ∩ F embeds it in the lattice of formations.

Stated but not proved: `MathlibExt.GroupTheory.NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.nilpotentClassFourFormationsDistributive_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NilpotentFormationLatticeDistributiveKourovka10Problem56Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html#nilpotent-class-four-formations-distribu-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattices of formations](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/soluble-finite-groups/formations/lattices-of-formations)
