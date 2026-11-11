---
declaration: section
origin: cited
lean: DVRResidue.residueField_partial_equivalence_package_of_isAdicComplete
statement: formalized
proof: formalized
---

# Unramified extensions and residue field extensions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/index.html).

## Partial residue-field equivalence for complete finite DVR extensions

Let $A$ be a discrete
valuation ring, and write $\kappa(R)$ for the residue field of a local ring $R$. Let $B_1$ and $B_2$
be discrete valuation rings that are finite $A$-algebras with local structure maps, complete and
separated for their maximal-ideal-adic topologies, such that for $i = 1, 2$ the field
$\kappa(B_i)$ is separable over $\kappa(A)$ and $\operatorname{rank}_A B_i$ equals
$\dim_{\kappa(A)} \kappa(B_i)$. Then the following three statements hold.
(i) Sending an $A$-algebra homomorphism $B_1 \to B_2$ to the $\kappa(A)$-algebra homomorphism
$\kappa(B_1) \to \kappa(B_2)$ it induces is a bijection.
(ii) For every finite separable field extension $L$ of $\kappa(A)$ there is a discrete valuation
ring $B$ that is a finite $A$-algebra with local structure map and whose residue field
$\kappa(B)$ is isomorphic to $L$ as a $\kappa(A)$-algebra; no unramifiedness of $B$ is claimed.
(iii) Every $\kappa(A)$-algebra isomorphism $e \colon \kappa(B_1) \to \kappa(B_2)$ lifts to an
$A$-algebra isomorphism $e' \colon B_1 \to B_2$: the map that $e'$ induces on residue fields is
$e$, and the map that $e'^{-1}$ induces is $e^{-1}$.

Formalized by `DVRResidue.residueField_partial_equivalence_package_of_isAdicComplete`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVREquivalencePackage.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/LocalRing/ResidueField/DVREquivalencePackage.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/index.html#residue-field-partial-equivalence-packag).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unramified extensions and residue field extensions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio)
