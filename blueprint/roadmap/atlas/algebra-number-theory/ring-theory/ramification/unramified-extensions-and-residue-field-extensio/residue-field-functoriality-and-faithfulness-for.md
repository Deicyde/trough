---
declaration: section
origin: cited
lean: DVRResidue.AlgHom.isLocalHom_of_isDiscreteValuationRing, DVRResidue.residueFieldMapAlgHom, DVRResidue.residueFieldMapAlgHom_injective
statement: formalized
proof: formalized
---

# Residue-field functoriality and faithfulness for DVR extensions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/residue-field-functoriality-and-faithfulness-for/index.html).

## Algebra maps

## Algebra maps from a DVR into a finite local DVR extension are local

Let $A$, $B$, $C$
be discrete valuation rings, with $B$ and $C$ algebras over $A$, where $C$ is finite as an
$A$-module and the structure map $A \to C$ is a local homomorphism. Then every $A$-algebra
homomorphism $B \to C$ is a local homomorphism.

Formalized by `DVRResidue.AlgHom.isLocalHom_of_isDiscreteValuationRing`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVR.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVR.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/residue-field-functoriality-and-faithfulness-for/index.html#is-local-hom-of-is-discrete-valuation-ri).

## Induced map on residue fields of DVR extensions

Let $A$, $B$, $C$ be discrete valuation
rings, with $B$ and $C$ algebras over $A$ whose structure maps are local homomorphisms, where $C$
is finite as an $A$-module. Write $\kappa(R)$ for the residue field of a local ring $R$. An
$A$-algebra homomorphism $f \colon B \to C$ induces the $\kappa(A)$-algebra homomorphism
$\kappa(B) \to \kappa(C)$ that sends the residue class of $b \in B$ to the residue class of
$f(b)$.

Formalized by `DVRResidue.residueFieldMapAlgHom`, a definition declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVR.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVR.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/residue-field-functoriality-and-faithfulness-for/index.html#residue-field-map-alg-hom).

## Residue-field maps determine algebra maps out of a formally unramified DVR extension

Let $A$, $B$, $C$ be discrete valuation rings, with $B$ and $C$ algebras over $A$ whose structure
maps are local homomorphisms, where $C$ is finite as an $A$-module and $B$ is formally unramified
over $A$. Write $\kappa(R)$ for the residue field of a local ring $R$. Then two $A$-algebra
homomorphisms $B \to C$ that induce the same $\kappa(A)$-algebra homomorphism
$\kappa(B) \to \kappa(C)$ are equal.

Formalized by `DVRResidue.residueFieldMapAlgHom_injective`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVR.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVR.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/residue-field-functoriality-and-faithfulness-for/index.html#residue-field-map-alg-hom-injective).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residue-field functoriality and faithfulness for DVR extensions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/residue-field-functoriality-and-faithfulness-for/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/residue-field-functoriality-and-faithfulness-for)
