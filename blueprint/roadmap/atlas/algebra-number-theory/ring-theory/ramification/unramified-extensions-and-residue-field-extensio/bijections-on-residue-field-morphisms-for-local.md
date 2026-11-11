---
declaration: section
origin: cited
lean: DVRResidue.residueFieldMapAlgHom_bijective, DVRResidue.exists_algEquiv_lift_residueField
statement: formalized
proof: formalized
---

# Bijections on residue-field morphisms for local DVR extensions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/bijections-on-residue-field-morphisms-for-local/index.html).

## Algebra maps from an étale DVR extension into a Henselian one match residue-field maps

Let $A$, $B$, $C$ be discrete valuation rings, with $B$ and $C$ finite $A$-algebras whose structure
maps are local homomorphisms, $B$ étale over $A$, and $C$ a Henselian local ring. Write
$\kappa(R)$ for the residue field of a local ring $R$. Then sending an $A$-algebra homomorphism
$B \to C$ to the $\kappa(A)$-algebra homomorphism $\kappa(B) \to \kappa(C)$ it induces is a
bijection.

Formalized by `DVRResidue.residueFieldMapAlgHom_bijective`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVRBijective.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/LocalRing/ResidueField/DVRBijective.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/bijections-on-residue-field-morphisms-for-local/index.html#residue-field-map-alg-hom-bijective).

## Lifting residue-field isomorphisms between Henselian étale DVR extensions

Let $A$, $B$,
$C$ be discrete valuation rings, with $B$ and $C$ finite $A$-algebras whose structure maps are local
homomorphisms, both étale over $A$ and both Henselian local rings. Write $\kappa(R)$ for the
residue field of a local ring $R$. Then every $\kappa(A)$-algebra isomorphism
$e \colon \kappa(B) \to \kappa(C)$ lifts to an $A$-algebra isomorphism $e' \colon B \to C$: the
map that $e'$ induces on residue fields is $e$, and the map that $e'^{-1}$ induces is $e^{-1}$.

Formalized by `DVRResidue.exists_algEquiv_lift_residueField`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVRBijective.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/LocalRing/ResidueField/DVRBijective.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/bijections-on-residue-field-morphisms-for-local/index.html#exists-alg-equiv-lift-residue-field).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bijections on residue-field morphisms for local DVR extensions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/bijections-on-residue-field-morphisms-for-local/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/bijections-on-residue-field-morphisms-for-local)
