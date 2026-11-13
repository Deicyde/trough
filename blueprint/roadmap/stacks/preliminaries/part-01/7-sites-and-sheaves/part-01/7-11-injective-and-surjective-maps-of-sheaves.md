---
declaration: section
origin: cited
lean: CategoryTheory.Sheaf.isLocallyInjective_iff_injective, CategoryTheory.Sheaf.IsLocallySurjective, mono_iff_isInjective, epi_iff_isSurjective, isIso_iff_isInjective_and_isSurjective, Stacks.Sites.SurjectionCoequalizer.coequalizer_of_surjection
statement: formalized
proof: formalized
---

# 7.11 Injective and surjective maps of sheaves

Section 7.11 of the Stacks Project, [Tag 00WL](https://stacks.math.columbia.edu/tag/00WL). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00WM, a definition

[Tag 00WM](https://stacks.math.columbia.edu/tag/00WM) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.isLocallyInjective_iff_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.isLocallyInjective_iff_injective#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/LocallyBijective.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/LocallyBijective.lean#L93) (StacksFrontier): “(1) A map of sheaves is injective, in the sense of 00WM (1) that it is injective on the sections over every object, exactly when it is locally injective in Mathlib's sense. Mathlib's class is stated for an arbitrary concrete category of values; this lemma is what identifies it with the pointwise-injectivity definition of 00WM (1).”.
- [`CategoryTheory.Sheaf.IsLocallySurjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.IsLocallySurjective#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/LocallyBijective.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/LocallyBijective.lean#L99) (StacksFrontier): “(2) The predicate of 00WM (2): every section of the target is locally, on a covering, in the image. Mathlib's single field `imageSieve_mem` is that condition.”.

## Tag 00WN, a lemma

[Tag 00WN](https://stacks.math.columbia.edu/tag/00WN) in the Stacks Project.

**`mono_iff_isInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/InjectiveSurjective.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/InjectiveSurjective.lean#L58). The attribute's comment: “(1)”. References: SGA 3 I (1.2), “more general”.

> A morphism of sheaves of sets is a monomorphism in the category of sheaves if and only if it
> is injective.

```lean
theorem mono_iff_isInjective {F G : Sheaf J (Type max v u)} (φ : F ⟶ G) :
    Mono φ ↔ IsInjective J φ
```

**`epi_iff_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/InjectiveSurjective.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/InjectiveSurjective.lean#L72). The attribute's comment: “(2)”. References: SGA 3 I (1.2), “more general”; SGA 3 IV (4.4.3), “special case”; SGA 3 IV (4.4.8), “special case”; SGA 3 VIB (10.15), “more general”; SGA 3 VIIA (8.1.4), “partial”; SGA 4 II (5.1), “special case”.

> A morphism of sheaves of sets is an epimorphism in the category of sheaves if and only if it
> is surjective.

```lean
theorem epi_iff_isSurjective {F G : Sheaf J (Type max v u)} (φ : F ⟶ G) :
    Epi φ ↔ IsSurjectiveSheafType J φ
```

**`isIso_iff_isInjective_and_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/InjectiveSurjective.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/InjectiveSurjective.lean#L82). The attribute's comment: “(3)”. References: SGA 3 IV (4.4.4), “iso ⇔ inj + surj”; SGA 3 IV (4.3.2.1), “more general”; SGA 4 II (4.2), “special case”.

> A morphism of sheaves of sets is an isomorphism if and only if it is both injective and
> surjective.

```lean
theorem isIso_iff_isInjective_and_isSurjective {F G : Sheaf J (Type max v u)}
    (φ : F ⟶ G) :
    IsIso φ ↔ IsInjective J φ ∧ IsSurjectiveSheafType J φ
```

## Tag 086K, a lemma

[Tag 086K](https://stacks.math.columbia.edu/tag/086K) in the Stacks Project.

**`Stacks.Sites.SurjectionCoequalizer.coequalizer_of_surjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/SurjectionCoequalizer.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/SurjectionCoequalizer.lean#L276).

> A surjection `φ : F ⟶ G` of sheaves of sets on a site exhibits `G` as the coequalizer of
> the two projections from the fiber product `F ×_G F`.

```lean
theorem coequalizer_of_surjection
    {F G : Sheaf J (Type max v u)} (φ : F ⟶ G) (hφ : IsSurjectiveSheafType J φ) :
    Nonempty (IsColimit (coequalizerCofork J φ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.11, Tag 00WL](https://stacks.math.columbia.edu/tag/00WL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
