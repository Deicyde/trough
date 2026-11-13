---
declaration: section
origin: cited
lean: IntermediateField.IsFiniteUnramified, IntermediateField.maximalUnramifiedSubextension, IntermediateField.le_maximalUnramifiedSubextension, IntermediateField.maximalUnramifiedSubextension_le_iff, IntermediateField.IsFiniteUnramified.map, IntermediateField.map_maximalUnramifiedSubextension
statement: formalized
proof: formalized
---

# Maximal unramified subextension

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html).

## Finite unramified intermediate fields

Let $A$ be a commutative ring and $L/K$ a field
extension such that the map $A \to L$ factors as $A \to K \to L$. An intermediate field $E$ of
$L/K$ is finite unramified relative to $A$ if $E$ is finite-dimensional over $K$ and the
integral closure of $A$ in $E$ is formally unramified over $A$.

Formalized by `IntermediateField.IsFiniteUnramified`, a definition declared in [MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html#is-finite-unramified).

## Maximal unramified subextension

Let $A$ be a commutative ring and $L/K$ a field
extension such that the map $A \to L$ factors as $A \to K \to L$. The maximal unramified
subextension of $L/K$ relative to $A$ is the supremum, in the lattice of intermediate fields of
$L/K$, of all intermediate fields of $L/K$ that are finite unramified relative to $A$.

The supremum need not itself be finite or formally unramified.

Formalized by `IntermediateField.maximalUnramifiedSubextension`, a definition declared in [MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html#maximal-unramified-subextension).

## Finite unramified subfields lie in the maximal unramified subextension

Let $A$ be a
commutative ring and $L/K$ a field extension such that the map $A \to L$ factors as
$A \to K \to L$. Every intermediate field $E$ of $L/K$ that is finite unramified relative to $A$
is contained in the maximal unramified subextension of $L/K$ relative to $A$.

Formalized by `IntermediateField.le_maximalUnramifiedSubextension`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html#le-maximal-unramified-subextension).

## Universal property of the maximal unramified subextension

Let $A$ be a commutative ring
and $L/K$ a field extension such that the map $A \to L$ factors as $A \to K \to L$. An
intermediate field $F$ of $L/K$ contains the maximal unramified subextension of $L/K$ relative
to $A$ if and only if $F$ contains every intermediate field of $L/K$ that is finite unramified
relative to $A$.

Formalized by `IntermediateField.maximalUnramifiedSubextension_le_iff`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html#maximal-unramified-subextension-le-iff).

## Automorphisms preserve finite unramified subfields

Let $A$ be a commutative ring and
$L/K$ a field extension such that the map $A \to L$ factors as $A \to K \to L$. If an
intermediate field $E$ of $L/K$ is finite unramified relative to $A$, then for every
$K$-algebra automorphism $\sigma$ of $L$ the image $\sigma(E)$ is finite unramified relative
to $A$.

Formalized by `IntermediateField.IsFiniteUnramified.map`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html#map).

## The maximal unramified subextension is stable under automorphisms

Let $A$ be a
commutative ring and $L/K$ a field extension such that the map $A \to L$ factors as
$A \to K \to L$, and let $M$ be the maximal unramified subextension of $L/K$ relative to $A$.
For every $K$-algebra automorphism $\sigma$ of $L$, $\sigma(M) = M$.

Formalized by `IntermediateField.map_maximalUnramifiedSubextension`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/MaximalUnramified.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html#map-maximal-unramified-subextension).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximal unramified subextension](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/maximal-unramified-subextension)
