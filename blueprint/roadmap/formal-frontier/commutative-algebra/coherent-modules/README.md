# Coherent modules

> Coherent rings and modules, finite-presentation criteria, exact-sequence closure, localization and descent, coherent-module categories, universal coherence, Hom and tensor-product closure, finite square-zero kernels and projection base change, coherence criteria for idealizations over division rings, finite-support idealizations and faithfully flat noncoherent algebras over fields, finite-type ideal/module transfer, left Noetherianity under scalar clearing, pointwise unimodular finite-generation ascent for semilinear maps, generator bounds for semilinear images, Artin–Rees for Noetherian modules, finite-submodule adic cofinality, radical colons of arbitrary subsets, and localization saturation commuting with colons by finitely generated ideals, annihilator localization for finitely generated semimodules, relative generation by nilpotent ideals, and finite-generation, finite-presentation, finite-projectivity and flatness descent under injective tensor units, internal Krull–Schmidt decompositions and finite-length cancellation in Lean.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

76 articles: 4 for highlights of its formalization.yaml and 72 for headline results in its README whose declaration link names a declaration the linked file declares. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules), read at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3) (2026-11-05).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other: revision-specific independent AI-agent review”
- Review notes: “Review and acceptance are recorded for exact revisions in the project's maintained release records. Changes require independent review and applicable build, proof-integrity, rights and provenance evidence before acceptance; this field does not certify any arbitrary checkout or replace that evidence. AI-agent review is not human peer review, legal certification, source-author endorsement or complete source formalization.”
- Automation: agent; tool setup “Formal Frontier AI agents using Lean, Lake and Git for development, assembly, review and maintenance.”
- Automation notes: “Original project contributions and upstream/tooling provenance are summarized in docs/CREDITS.md. Review and verification apply to exact revisions; AI-agent participation does not imply human peer review or source-author endorsement.”

## Scope

Reusable coherence and finite-presentation results with each declaration's actual algebraic hypotheses and independent module universes. Universal coherence explicitly records its target-algebra universe. Coordinatewise extension identifies coefficient-linear maps additively with matrix-linear maps of columns for finite nonempty indices over arbitrary possibly noncommutative semirings, retaining the given coefficient actions. The induced endomorphism semiring equivalence preserves composition; on the regular coefficient module its source identifies with the opposite coefficient semiring, not the full matrix semiring. For empty indices only surjectivity is asserted. Zero semirings are allowed, and no coefficient-module structure on a general Hom is used. For left ideals I over a possibly noncommutative semiring and arbitrary submodules N and P of an additive commutative semimodule, the relative bound P ≤ N ⊔ I • P persists along every ideal power. Global nilpotence of I then gives P ≤ N, without finite generation, additive inverses, cancellation or nontriviality; the scalar and module universes are independent. Hom/tensor closure remains theorem-based, with a finitely presented first argument and coherent second argument. Square-zero kernel and projection base-change results hold over commutative semirings and additive commutative modules; kernel finiteness requires a finite module, while base change does not. For a field and its given vector space, the canonical idealization is coherent exactly when the vector space is finitely generated, including the zero space and with independent scalar and vector universes. For a ring and its given compatible bimodule, coherence of the extension implies left finite generation when scalar multiplication on one vector is injective; no centrality of the right action is assumed. The sufficient condition is left coherence of the base and left finite presentation of the coefficients. Ideal/module predicate transfer is over finite-type algebras of a commutative ring, assuming isomorphism invariance and descent along every compatible surjective square-zero algebra map. The base universe is independent of the common algebra/module universe. Semilinear image bounds hold over arbitrary semirings without assuming surjectivity of the scalar homomorphism. The natural-valued generator bound assumes finite generation of the source. A target submodule is finitely generated when its comap is finitely generated and, for each of its elements n, the scalars a with f m = a • n for some m generate the unit left ideal. Without finite generation, the same condition identifies the target submodule with the target-scalar span of its comap image. The single-left-inverse and unit-clearing criteria are specializations; at the top submodule the existing criteria transfer module-finiteness from the source. No Noetherianity or scalar-homomorphism surjectivity is required. Scalar-clearing ascent uses arbitrary source and target semirings and additive commutative semimodules in four independent universes, with witnesses b * a = 1 and f m = a • n for each target element n. Comap reflects submodule order. Unit clearing and function-surjectivity specialize this result; regular semimodules recover ring Noetherianity, alongside ideal extension/contraction. Finite-submodule adic cofinality concerns finitely generated submodules of finite original modules over a commutative ring, without finite presentation of the ambient module or finite generation of the ideal. Its eliminator allows independent ring and module universes. Nilpotent ideals and ideals of Noetherian rings satisfy the property. The full module Artin–Rees theorem only assumes Noetherianity of the original module, not of the ring. Colons of radical ideals by arbitrary subsets are radical over commutative semirings. Taking the zero ideal over a reduced commutative semiring gives radical pointwise annihilators, including empty subsets and zero rings. For commutative semirings R and S, a submonoid T of R and an R-algebra S realizing localization at T, extension followed by contraction commutes with colon by a finitely generated ideal J. The numerator ideal I is arbitrary; finite generation of J does not mean its underlying set is finite. The two universes are independent, and zero semirings, zero in T, the zero ideal J and top ideals are allowed. For commutative semirings R and A and a standard localized-module map from M to N, extension of the annihilator of M is the annihilator of N when M is finitely generated over R. The additive commutative monoids carry their given R-module structures and N has its compatible A-action; all four carrier universes are independent. Zero modules, zero semirings and zero in the localizing submonoid are retained, without finite presentation, faithful action or an added flatness hypothesis. Equality after localization for two maps from a finitely generated semimodule is equivalent to equality after multiplying both maps by one element of the localizing submonoid. For a commutative ring R, injectivity of the canonical tensor units on all additive commutative R-semimodules in Type (max uR uM) reflects finite generation along extension to a possibly noncommutative semiring S and finite presentation along extension to a possibly noncommutative ring S. Finite projectivity descends along extension to a possibly noncommutative semiring S, without a finite-presentation premise on the original module. It also reflects membership, inclusions and finite generation of extended submodule images. For commutative S it reflects flatness. The tensor has its canonical left-factor S-action, and ascent gives the corresponding equivalences. The scalar algebra has an independent universe and is not assumed flat over R. The original module carries only its given additive commutative monoid and R-action; group structures are derived internally where needed, without an additional scalar action on M. No coherence, nontriviality or nonzero-module assumption or complete source coverage is asserted.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Coherent rings, coherent modules and finite presentation* (folklore; independently-proves).
- *Semilinear Noetherian ascent under scalar clearing* (folklore; independently-proves).
- [Foundations of Rigid Geometry I](https://arxiv.org/abs/1308.4734v5), Kazuhiro Fujiwara, Fumiharu Kato (book; background).

## Builds on

- [Homological algebra](../../homological-algebra-and-category-theory/homological-algebra/README.md) (a Lake dependency, pinned at 6c7f755c)

## Used by

- [Adic modules](../adic-modules/README.md)
- [Algebraic groups](../../algebraic-geometry/algebraic-groups/README.md)
- [Formal power series](../formal-power-series/README.md)
- [Graded rings](../graded-rings/README.md)
- [Group rings](../../ring-theory/group-rings/README.md)
- [Minimal primes](../minimal-primes/README.md)
- [Multivariate polynomials](../multivariate-polynomials/README.md)
- [Projective modules](../../ring-theory/projective-modules/README.md)
- [Scheme properties](../../algebraic-geometry/scheme-properties/README.md)
- [Toric ideals](../toric-ideals/README.md)
- [Valuation integers](../../number-theory/valuation-integers/README.md)
- [Vector bundles](../../topology/vector-bundles/README.md)

## [Coherence via kernels of maps… to Inverse images with nilpotent…](part-01/README.md)

- [Coherence via kernels of maps from finite free modules](part-01/coherence-via-kernels-of-maps-from-finite-free-m.md)
- [Finiteness, projectivity and flatness under injective tensor units](part-01/finiteness-projectivity-and-flatness-under-injec.md)
- [Internal Krull–Schmidt decompositions and cancellation](part-01/internal-krull-schmidt-decompositions-and-cancel.md)
- [Coherence of square-zero extensions and finite-support idealizations](part-01/coherence-of-square-zero-extensions-and-finite-s.md)
- [Additive intertwining by ranges](part-01/additive-intertwining-by-ranges.md)
- [Fibrewise additive intertwining](part-01/fibrewise-additive-intertwining.md)
- [Finite coarsening of complete orthogonal idempotents](part-01/finite-coarsening-of-complete-orthogonal-idempot.md)
- [Dual endomorphisms](part-01/dual-endomorphisms.md)
- [Tensor–dual Frobenius criterion](part-01/tensor-dual-frobenius-criterion.md)
- [Annihilator quotients with two scalar actions](part-01/annihilator-quotients-with-two-scalar-actions.md)
- [Noetherian semilinear Hom](part-01/noetherian-semilinear-hom.md)
- [Hom and End of matrix columns](part-01/hom-and-end-of-matrix-columns.md)
- [Projective matrix-column semimodules](part-01/projective-matrix-column-semimodules.md)
- [Left ideals of finite matrix semirings](part-01/left-ideals-of-finite-matrix-semirings.md)
- [Coherence of finite matrix rings](part-01/coherence-of-finite-matrix-rings.md)
- [Left-regular elements in left Artinian rings](part-01/left-regular-elements-in-left-artinian-rings.md)
- [Closed semimodule categories](part-01/closed-semimodule-categories.md)
- [Kernels over semirings](part-01/kernels-over-semirings.md)
- [Sums of nilpotent left ideals](part-01/sums-of-nilpotent-left-ideals.md)
- [Inverse images with nilpotent kernel](part-01/inverse-images-with-nilpotent-kernel.md)

## [Relative generation by… to Finite generation from the…](part-02/README.md)

- [Relative generation by nilpotent ideals](part-02/relative-generation-by-nilpotent-ideals.md)
- [Extension of products and powers of left ideals](part-02/extension-of-products-and-powers-of-left-ideals.md)
- [Annihilators after localization](part-02/annihilators-after-localization.md)
- [Coatomicity of two-sided ideals](part-02/coatomicity-of-two-sided-ideals.md)
- [Radical colons and pointwise annihilators](part-02/radical-colons-and-pointwise-annihilators.md)
- [Finitely generated ideal colons and localization](part-02/finitely-generated-ideal-colons-and-localization.md)
- [Unit-ideal scalar families](part-02/unit-ideal-scalar-families.md)
- [Coprime scalar rows](part-02/coprime-scalar-rows.md)
- [Finite coprime-kernel decompositions](part-02/finite-coprime-kernel-decompositions.md)
- [Finite generation under pointwise unimodular clearing](part-02/finite-generation-under-pointwise-unimodular-cle.md)
- [Semilinear Noetherian ascent](part-02/semilinear-noetherian-ascent.md)
- [Artin–Rees for Noetherian modules](part-02/artin-rees-for-noetherian-modules.md)
- [Submodule adic cofinality](part-02/submodule-adic-cofinality.md)
- [Power-killed submodule criteria](part-02/power-killed-submodule-criteria.md)
- [Descent of adic cofinality](part-02/descent-of-adic-cofinality.md)
- [Adic cofinality on finite products](part-02/adic-cofinality-on-finite-products.md)
- [Cofinal ideal powers](part-02/cofinal-ideal-powers.md)
- [Semilinear transport of adic cofinality](part-02/semilinear-transport-of-adic-cofinality.md)
- [Krull intersection from adic cofinality](part-02/krull-intersection-from-adic-cofinality.md)
- [Finite generation from the first adic quotient](part-02/finite-generation-from-the-first-adic-quotient.md)

## [Finite presentation from… to Faithfully flat tensor products](part-03/README.md)

- [Finite presentation from cofinal ideal quotients](part-03/finite-presentation-from-cofinal-ideal-quotients.md)
- [Essentially finite-type scalar extension](part-03/essentially-finite-type-scalar-extension.md)
- [Coherent modules and kernels](part-03/coherent-modules-and-kernels.md)
- [Coherent homology](part-03/coherent-homology.md)
- [Coherence along semilinear retractions](part-03/coherence-along-semilinear-retractions.md)
- [Coherent dependent direct sums](part-03/coherent-dependent-direct-sums.md)
- [Coherence over product coefficient rings](part-03/coherence-over-product-coefficient-rings.md)
- [Finite presentation over product coefficient rings](part-03/finite-presentation-over-product-coefficient-rin.md)
- [Finite presentation along scalar towers](part-03/finite-presentation-along-scalar-towers.md)
- [Coherence along quotient coefficients](part-03/coherence-along-quotient-coefficients.md)
- [Coherence under scalar restriction](part-03/coherence-under-scalar-restriction.md)
- [Hom, tensor, and categories](part-03/hom-tensor-and-categories.md)
- [Coherent right duals](part-03/coherent-right-duals.md)
- [Finite-module tensor zero detection](part-03/finite-module-tensor-zero-detection.md)
- [Ideal action on finite coefficients](part-03/ideal-action-on-finite-coefficients.md)
- [Semilinear invariance of flatness](part-03/semilinear-invariance-of-flatness.md)
- [Finiteness, projectivity and flatness under pure scalar extension](part-01/finiteness-projectivity-and-flatness-under-injec.md)
- [Annihilators under finite-limit-preserving scalar extension](part-03/annihilators-under-finite-limit-preserving-scala.md)
- [Annihilator contraction under faithfully flat extension](part-03/annihilator-contraction-under-faithfully-flat-ex.md)
- [Faithfully flat tensor products](part-03/faithfully-flat-tensor-products.md)

## [Faithfully flat dependent… to Finite-type ideal/module…](part-04/README.md)

- [Faithfully flat dependent direct sums](part-04/faithfully-flat-dependent-direct-sums.md)
- [Finitely generated ideals and dependent products](part-04/finitely-generated-ideals-and-dependent-products.md)
- [Faithful flatness after base change covering maximal ideals](part-04/faithful-flatness-after-base-change-covering-max.md)
- [Faithful flatness of unital algebras](part-04/faithful-flatness-of-unital-algebras.md)
- [Faithfully flat products of algebras](part-04/faithfully-flat-products-of-algebras.md)
- [Products of localizations at submonoids](part-04/products-of-localizations-at-submonoids.md)
- [Families of principal localizations](part-04/families-of-principal-localizations.md)
- [Faithfully flat coherence descent](part-04/faithfully-flat-coherence-descent.md)
- [Universal coherence](part-04/universal-coherence.md)
- [Associative square-zero multiplication](part-04/associative-square-zero-multiplication.md)
- [Commutativity of square-zero extensions](part-04/commutativity-of-square-zero-extensions.md)
- [Square-zero kernels and projection base change](part-04/square-zero-kernels-and-projection-base-change.md)
- [Full left-ideal lattice of square-zero extensions](part-04/full-left-ideal-lattice-of-square-zero-extension.md)
- [Module length and square-zero extensions](part-04/module-length-and-square-zero-extensions.md)
- [Coherent square-zero extensions](part-01/coherence-of-square-zero-extensions-and-finite-s.md)
- [Opposites of square-zero extensions](part-04/opposites-of-square-zero-extensions.md)
- [Left Noetherian square-zero extensions](part-04/left-noetherian-square-zero-extensions.md)
- [Finite-type ideal/module transfer](part-04/finite-type-ideal-module-transfer.md)
