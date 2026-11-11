---
declaration: section
origin: cited
lean: Subgroup.le_of_card_subgroupOf_eq, Ideal.card_inertia_tower_formula, Ideal.ramificationIdx_mul_card_inertia_subgroupOf, Ideal.ramificationIdx_eq_one_iff_inertia_le_fixingSubgroup, Ideal.ramificationIdx_eq_one_iff_le_inertiaField, Ideal.ramificationIdx_mul_inertiaDeg_mul_card_stabilizer_subgroupOf, Ideal.ramificationIdx_inertiaDeg_eq_one_iff_stabilizer_le_fixingSubgroup, Ideal.ramificationIdx_inertiaDeg_eq_one_iff_le_decompositionField
statement: formalized
proof: formalized
---

# Decomposition and inertia groups

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html).

## Subgroup

## Equal cardinality of an intersection forces containment

Let $H$ and $K$ be subgroups of
a group $G$ with $H$ finite. If $H \cap K$ has as many elements as $H$, then $H \le K$.

Formalized by `Subgroup.le_of_card_subgroupOf_eq`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#le-of-card-subgroup-of-eq).

## Tower formula for inertia groups

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. For a subgroup $S \le G$ write
$I_S(\mathfrak P)$ for the inertia group of $\mathfrak P$ in $S$, the set of $\sigma \in S$ with
$\sigma(x) - x \in \mathfrak P$ for all $x \in B$. Then
$e(\mathfrak P_E \mid \mathfrak p) \cdot |I_H(\mathfrak P)| = |I_G(\mathfrak P)|$, where
$e(\mathfrak P_E \mid \mathfrak p)$ is the ramification index of $\mathfrak P_E$ over
$\mathfrak p$.

Formalized by `Ideal.card_inertia_tower_formula`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#card-inertia-tower-formula).

## Tower formula for inertia groups, intersected with the fixing group

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $I(\mathfrak P)$ be the
inertia group of $\mathfrak P$, the set of $\sigma \in G$ with $\sigma(x) - x \in \mathfrak P$
for all $x \in B$. Then
$e(\mathfrak P_E \mid \mathfrak p) \cdot |I(\mathfrak P) \cap H| = |I(\mathfrak P)|$, where
$e(\mathfrak P_E \mid \mathfrak p)$ is the ramification index of $\mathfrak P_E$ over
$\mathfrak p$.

Formalized by `Ideal.ramificationIdx_mul_card_inertia_subgroupOf`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-mul-card-inertia-subgro).

## Ramification index one and the inertia group

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $I(\mathfrak P)$ be the
inertia group of $\mathfrak P$, the set of $\sigma \in G$ with $\sigma(x) - x \in \mathfrak P$
for all $x \in B$. Then the ramification index $e(\mathfrak P_E \mid \mathfrak p)$ of
$\mathfrak P_E$ over $\mathfrak p$ equals $1$ if and only if $I(\mathfrak P) \le H$.

Formalized by `Ideal.ramificationIdx_eq_one_iff_inertia_le_fixingSubgroup`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-eq-one-iff-inertia-le-f).

## Ramification index one and the inertia field

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $I(\mathfrak P)$ be the
inertia group of $\mathfrak P$, the set of $\sigma \in G$ with $\sigma(x) - x \in \mathfrak P$
for all $x \in B$, and let $L^{I(\mathfrak P)}$ be its fixed field in $L$. Then the ramification
index $e(\mathfrak P_E \mid \mathfrak p)$ of $\mathfrak P_E$ over $\mathfrak p$ equals $1$ if and
only if $E \subseteq L^{I(\mathfrak P)}$.

Formalized by `Ideal.ramificationIdx_eq_one_iff_le_inertiaField`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-eq-one-iff-le-inertia-f).

## Tower formula for decomposition groups

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $D(\mathfrak P)$ be the
decomposition group of $\mathfrak P$, the set of $\sigma \in G$ with
$\sigma(\mathfrak P) = \mathfrak P$, and let $e$ and $f$ be the ramification index and the
inertia degree of $\mathfrak P_E$ over $\mathfrak p$. Then
$e f \cdot |D(\mathfrak P) \cap H| = |D(\mathfrak P)|$.

Formalized by `Ideal.ramificationIdx_mul_inertiaDeg_mul_card_stabilizer_subgroupOf`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-mul-inertia-deg-mul-car).

## Ramification index and inertia degree one and the decomposition group

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $D(\mathfrak P)$ be the
decomposition group of $\mathfrak P$, the set of $\sigma \in G$ with
$\sigma(\mathfrak P) = \mathfrak P$, and let $e$ and $f$ be the ramification index and the
inertia degree of $\mathfrak P_E$ over $\mathfrak p$. Then $e = 1$ and $f = 1$ if and only if
$D(\mathfrak P) \le H$.

Formalized by `Ideal.ramificationIdx_inertiaDeg_eq_one_iff_stabilizer_le_fixingSubgroup`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-inertia-deg-eq-one-iff).

## Ramification index and inertia degree one and the decomposition field

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $D(\mathfrak P)$ be the
decomposition group of $\mathfrak P$, the set of $\sigma \in G$ with
$\sigma(\mathfrak P) = \mathfrak P$, and let $L^{D(\mathfrak P)}$ be its fixed field in $L$. Let
$e$ and $f$ be the ramification index and the inertia degree of $\mathfrak P_E$ over
$\mathfrak p$. Then $e = 1$ and $f = 1$ if and only if $E \subseteq L^{D(\mathfrak P)}$.

Formalized by `Ideal.ramificationIdx_inertiaDeg_eq_one_iff_le_decompositionField`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-inertia-deg-eq-one-iff-2).

## Fields below the inertia and decomposition fields

Let $L/K$ be a finite Galois extension with Galois group $G$. Let $A$ and $B$ be Dedekind domains
with $B$ a finite torsion-free $A$-algebra, and let $G$ act on $B$ by ring automorphisms as a
Galois group of $B$ over $A$: faithfully, fixing the image of $A$, and with every element of $B$
fixed by $G$ in the image of $A$. Let $E$ be an intermediate field of $L/K$ and $H \le G$ the
subgroup fixing $E$ pointwise. Let $C$ be a Dedekind domain and a torsion-free $A$-algebra, and
give $E$ an $A$-algebra structure and an injective ring map $C \to E$ whose image is the set of
elements of $E$ integral over $A$ (the composite $A \to C \to E$ need not be the given map
$A \to E$). Suppose $B$ is also a finite torsion-free $C$-algebra, with $A \to C \to B$ equal to
$A \to B$, and that $H$, acting on $B$ by restriction, is a Galois group of $B$ over $C$. Let
$\mathfrak p$, $\mathfrak P_E$ and $\mathfrak P$ be maximal ideals of $A$, $C$ and $B$ such that
$\mathfrak P$ lies over $\mathfrak p$ and over $\mathfrak P_E$ and $\mathfrak P_E$ lies over
$\mathfrak p$, and suppose that every prime of $B$ over $\mathfrak p$, and every prime of $B$
over $\mathfrak P_E$, has a separable residue field extension. Let $I(\mathfrak P)$ be the
inertia group of $\mathfrak P$, the set of $\sigma \in G$ with $\sigma(x) - x \in \mathfrak P$
for all $x \in B$, and $D(\mathfrak P)$ its decomposition group, the set of $\sigma \in G$ with
$\sigma(\mathfrak P) = \mathfrak P$; let $L^{I(\mathfrak P)}$ and $L^{D(\mathfrak P)}$ be their
fixed fields in $L$, and let $e$ and $f$ be the ramification index and the inertia degree of
$\mathfrak P_E$ over $\mathfrak p$. Then $e = 1$ if and only if $E \subseteq L^{I(\mathfrak P)}$,
and $e = f = 1$ if and only if $E \subseteq L^{D(\mathfrak P)}$.

## Sources

- ATLAS NumberTheoryI, Corollary 7.14.

Formalized by `Ideal.ramificationIdx_inertiaDeg_eq_one_iff_le_inertiaField_decompositionField`, a theorem declared in [MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/RamificationInertia/InertiaDecompositionFields.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html#ramification-idx-inertia-deg-eq-one-iff-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decomposition and inertia groups](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/decomposition-and-inertia-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/decomposition-and-inertia-groups)
