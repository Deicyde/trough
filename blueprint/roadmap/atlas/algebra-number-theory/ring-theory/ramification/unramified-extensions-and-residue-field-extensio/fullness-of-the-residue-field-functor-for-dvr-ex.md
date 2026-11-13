---
declaration: section
origin: cited
lean: DVRResidue.exists_root_lift_of_adjoin_eq_top, DVRResidue.residueFieldMapAlgHom_surjective
statement: formalized
proof: formalized
---

# Fullness of the residue-field functor for DVR extensions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/fullness-of-the-residue-field-functor-for-dvr-ex/index.html).

## Lifting residue-field images to roots of a minimal polynomial

Let $A$ and $B$ be
discrete valuation rings with $B$ a finite étale $A$-algebra whose structure map is local, and
let $C$ be a Henselian local ring that is an $A$-algebra whose structure map is local. Write
$k_A$, $k_B$, $k_C$ for the residue fields. Let $\beta \in B$ generate $B$ as an $A$-algebra,
and let $\bar\beta \in k_B$ be its residue class. Then for every $k_A$-algebra homomorphism
$f : k_B \to k_C$ there is $\gamma \in C$ that is a root of the minimal polynomial of $\beta$
over $A$ and whose residue class in $k_C$ is $f(\bar\beta)$.

Formalized by `DVRResidue.exists_root_lift_of_adjoin_eq_top`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVRFull.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVRFull.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/fullness-of-the-residue-field-functor-for-dvr-ex/index.html#exists-root-lift-of-adjoin-eq-top).

## Lifting residue-field homomorphisms of finite étale DVR extensions

Let $A$, $B$, $C$ be
discrete valuation rings, with $B$ and $C$ finite $A$-algebras whose structure maps are local,
$B$ étale over $A$ and $C$ Henselian. Write $k_A$, $k_B$, $k_C$ for the residue fields. Then
every $k_A$-algebra homomorphism $k_B \to k_C$ is induced by an $A$-algebra homomorphism: the
map sending an $A$-algebra homomorphism $\varphi : B \to C$ to the induced homomorphism of
residue fields $k_B \to k_C$, $\bar b \mapsto \overline{\varphi(b)}$, is surjective.

Formalized by `DVRResidue.residueFieldMapAlgHom_surjective`, a theorem declared in [MathlibExt/RingTheory/LocalRing/ResidueField/DVRFull.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/ResidueField/DVRFull.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/fullness-of-the-residue-field-functor-for-dvr-ex/index.html#residue-field-map-alg-hom-surjective).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fullness of the residue-field functor for DVR extensions](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/fullness-of-the-residue-field-functor-for-dvr-ex/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/ramification/unramified-extensions-and-residue-field-extensio/fullness-of-the-residue-field-functor-for-dvr-ex)
