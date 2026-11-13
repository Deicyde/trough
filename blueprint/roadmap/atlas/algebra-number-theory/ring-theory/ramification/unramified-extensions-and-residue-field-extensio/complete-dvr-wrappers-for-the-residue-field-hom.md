---
declaration: section
origin: cited
lean: DVRResidue.residueFieldMapAlgHom_bijective_of_isAdicComplete, DVRResidue.exists_algEquiv_lift_residueField_of_isAdicComplete
statement: formalized
proof: formalized
---

# Complete-DVR wrappers for the residue-field Hom bijection

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/complete-dvr-wrappers-for-the-residue-field-hom/index.html).

## Algebra maps from an étale DVR extension into a complete one match residue-field maps

Let $A$, $B$, $C$ be discrete valuation rings, with $B$ and $C$ finite $A$-algebras whose structure
maps are local homomorphisms, $B$ étale over $A$, and $C$ complete and separated for its
maximal-ideal-adic topology. Write $\kappa(R)$ for the residue field of a local ring $R$. Then
sending an $A$-algebra homomorphism $B \to C$ to the $\kappa(A)$-algebra homomorphism
$\kappa(B) \to \kappa(C)$ it induces is a bijection.

Formalized by `DVRResidue.residueFieldMapAlgHom_bijective_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVRComplete.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVRComplete.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/complete-dvr-wrappers-for-the-residue-field-hom/index.html#residue-field-map-alg-hom-bijective-of-i).

## Lifting residue-field isomorphisms between complete étale DVR extensions

Let $A$, $B$, $C$
be discrete valuation rings, with $B$ and $C$ finite $A$-algebras whose structure maps are local
homomorphisms, both étale over $A$, and both complete and separated for their maximal-ideal-adic
topologies. Write $\kappa(R)$ for the residue field of a local ring $R$. Then every
$\kappa(A)$-algebra isomorphism $e \colon \kappa(B) \to \kappa(C)$ lifts to an $A$-algebra
isomorphism $e' \colon B \to C$: the map that $e'$ induces on residue fields is $e$, and the map
that $e'^{-1}$ induces is $e^{-1}$.

Formalized by `DVRResidue.exists_algEquiv_lift_residueField_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVRComplete.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVRComplete.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/complete-dvr-wrappers-for-the-residue-field-hom/index.html#exists-alg-equiv-lift-residue-field-of-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complete-DVR wrappers for the residue-field Hom bijection](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/complete-dvr-wrappers-for-the-residue-field-hom/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/complete-dvr-wrappers-for-the-residue-field-hom)
