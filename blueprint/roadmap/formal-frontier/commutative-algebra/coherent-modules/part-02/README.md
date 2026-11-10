---
navigation: transparent
---

# Relative generation by… to Finite generation from the…

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

- [Relative generation by nilpotent ideals](relative-generation-by-nilpotent-ideals.md)
- [Extension of products and powers of left ideals](extension-of-products-and-powers-of-left-ideals.md)
- [Annihilators after localization](annihilators-after-localization.md)
- [Coatomicity of two-sided ideals](coatomicity-of-two-sided-ideals.md)
- [Radical colons and pointwise annihilators](radical-colons-and-pointwise-annihilators.md)
- [Finitely generated ideal colons and localization](finitely-generated-ideal-colons-and-localization.md)
- [Unit-ideal scalar families](unit-ideal-scalar-families.md)
- [Coprime scalar rows](coprime-scalar-rows.md)
- [Finite coprime-kernel decompositions](finite-coprime-kernel-decompositions.md)
- [Finite generation under pointwise unimodular clearing](finite-generation-under-pointwise-unimodular-cle.md)
- [Semilinear Noetherian ascent](semilinear-noetherian-ascent.md)
- [Artin–Rees for Noetherian modules](artin-rees-for-noetherian-modules.md)
- [Submodule adic cofinality](submodule-adic-cofinality.md)
- [Power-killed submodule criteria](power-killed-submodule-criteria.md)
- [Descent of adic cofinality](descent-of-adic-cofinality.md)
- [Adic cofinality on finite products](adic-cofinality-on-finite-products.md)
- [Cofinal ideal powers](cofinal-ideal-powers.md)
- [Semilinear transport of adic cofinality](semilinear-transport-of-adic-cofinality.md)

**Stability of adic cofinality under scalar extension.** Over commutative
rings, both (AP) and (APf) pass from an ideal `I` to its extension
`I.map (algebraMap R A)` along a **module-finite** `R`-algebra `A`, or
along an arbitrary localization algebra. The localization algebra need not
be finite over `R`. The respective `.map` and `.map_of_isLocalization`
interfaces are in
[`AdicCompatibility`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicCompatibility.lean).
Neither ideal finite generation nor finite presentation or Noetherianity
is required; the original target action and independent carrier universes
are retained.

**Adic cofinality near a closed locus.** For an ideal `I` of a commutative
ring `R` and any set `s : Set R` with `I ⊔ Ideal.span s = ⊤`, (AP) holds
for `I` if and only if it holds for every extension to `Localization.Away f`,
`f ∈ s`; the same equivalence holds for (APf). The
[`hasSubmoduleAdicCofinality_iff_forall_map_away` and finite-submodule counterpart](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/AdicLocality.lean)
need only a distinguished-open cover of `V(I)`, not of the whole spectrum.
The set need not be finite. The ambient modules remain finite, with arbitrary
submodules for (AP) and finitely generated submodules for (APf); no ideal-FG,
ambient finite-presentation or Noetherian hypothesis is added. Cutoffs are
pointwise, not a uniform shift or denominator bound, and this is not a
stalkwise criterion.

- [Krull intersection from adic cofinality](krull-intersection-from-adic-cofinality.md)
- [Finite generation from the first adic quotient](finite-generation-from-the-first-adic-quotient.md)
