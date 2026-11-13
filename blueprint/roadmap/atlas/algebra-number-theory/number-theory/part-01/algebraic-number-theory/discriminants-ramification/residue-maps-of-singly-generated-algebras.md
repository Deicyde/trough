---
declaration: section
origin: cited
lean: Ideal.quotient_algebraMap_surjective_of_adjoin_singleton_eq_top, Ideal.inertiaDeg_eq_one_of_adjoin_singleton_eq_top
statement: formalized
proof: formalized
---

# Residue maps of singly generated algebras

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/residue-maps-of-singly-generated-algebras/index.html).

## Surjectivity of the residue map for a singly generated algebra

Let $A$ and $B$ be
commutative rings, $B$ an $A$-algebra, $\mathfrak q$ an ideal of $B$ and $\mathfrak p$ its
preimage under $A \to B$. If $B$ is generated as an $A$-algebra by a single element
$\pi \in \mathfrak q$, then the canonical map $A/\mathfrak p \to B/\mathfrak q$ is surjective.

Indeed, every element of $B$ is $f(\pi)$ for a polynomial $f$ with coefficients in $A$, and
modulo $\mathfrak q$ it agrees with the image of the constant coefficient of $f$, because $\pi$
maps to zero.

Formalized by `Ideal.quotient_algebraMap_surjective_of_adjoin_singleton_eq_top`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/ResidueGenerator.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/ResidueGenerator.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/residue-maps-of-singly-generated-algebras/index.html#quotient-algebra-map-surjective-of-adjoi).

## Inertia degree one for a singly generated algebra

Let $A$ and $B$ be commutative rings,
$B$ an $A$-algebra, and $\mathfrak q$ a maximal ideal of $B$ whose preimage $\mathfrak p$ under
$A \to B$ is maximal. If $B$ is generated as an $A$-algebra by a single element
$\pi \in \mathfrak q$, then the inertia degree of $\mathfrak q$ over $\mathfrak p$ is $1$.

The canonical map $A/\mathfrak p \to B/\mathfrak q$ is surjective, so the residue field
extension has degree one.

Formalized by `Ideal.inertiaDeg_eq_one_of_adjoin_singleton_eq_top`, a theorem declared in [MathlibExt/NumberTheory/RamificationInertia/ResidueGenerator.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RamificationInertia/ResidueGenerator.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/residue-maps-of-singly-generated-algebras/index.html#inertia-deg-eq-one-of-adjoin-singleton-e).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residue maps of singly generated algebras](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/residue-maps-of-singly-generated-algebras/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/residue-maps-of-singly-generated-algebras)
