---
declaration: section
origin: cited
lean: AlgebraicGeometry.isAdmissible_localizedCompletion, AlgebraicGeometry.spfBasicOpenRestrictIso, AlgebraicGeometry.spfBasicOpenGammaIso, AlgebraicGeometry.spf_isThickening_isIso_isSheaf_isLocalRing_basicOpen, AlgebraicGeometry.isIso_spfGammaHom, AlgebraicGeometry.spfGammaIso, AlgebraicGeometry.pseudoDiscreteSheafAdjunction, AlgebraicGeometry.pseudoDiscreteSheafEquivalence
statement: formalized
proof: formalized
---

# 87.2 Formal schemes à la EGA

Section 87.2 of the Stacks Project, [Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY). 7 tags here are carried by 65 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AHY, the section

[Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY) in the Stacks Project.

**`AlgebraicGeometry.isAdmissible_localizedCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean#L65). The attribute's comment: “the ring A\_\{f} is admissible too”.

> **The completed localization `A_{\{f\}}` of an admissible ring is admissible** (EGA I 10.1.4):
> its topology is induced from `A`, so the canonical map `A → A_{\{f\}}` is taut and carries an ideal
> of definition of `A` to one of `A_{\{f\}}`, and it is complete and separated, being a completion.

```lean
theorem isAdmissible_localizedCompletion (hA : IsAdmissible A) (f : A) :
    IsAdmissible (localizedCompletion A f)
```

**`AlgebraicGeometry.spfBasicOpenRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean#L97). The attribute's comment: “(Spf A\_\{f}, 𝒪) is isomorphic to (D(f) ∩ Spf A, 𝒪\_\{Spf A}|\_\{D(f) ∩ Spf A})”.

> **Stacks 0AHY**: for an admissible ring `A` and `f ∈ A`, the open
> `(D(f) ∩ Spf A, 𝒪_{Spf A}|_{D(f) ∩ Spf A})` of the formal spectrum is isomorphic to
> `(Spf A_{\{f\}}, 𝒪_{Spf A_{\{f\}}})`.

```lean
noncomputable def spfBasicOpenRestrictIso (hA : IsAdmissible A) (f : A) :
    (Spf A).restrict (f := (spfBasicOpen A f).inclusion')
      (spfBasicOpen A f).isOpenEmbedding' ≅ Spf (localizedCompletion A f)
```

**`AlgebraicGeometry.spfBasicOpenGammaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean#L129). The attribute's comment: “Γ(D(f) ∩ Spf A, 𝒪\_\{Spf A}) = A\_\{f} as topological rings”.

> **Stacks 0AHY**: for an admissible ring `A` and `f ∈ A`,
> `Γ(D(f) ∩ Spf A, 𝒪_{Spf A}) = A_{\{f\}}` as topological rings. The other description
> `Γ(D(f) ∩ Spf A, 𝒪_{Spf A}) = lim (A/I_λ)_f` of the source is
> `AlgebraicGeometry.spfBasicOpenIsoOn`.

```lean
noncomputable def spfBasicOpenGammaIso (hA : IsAdmissible A) (f : A) :
    (spfPresheaf A).obj (op (spfBasicOpen A f)) ≅ TopCommRingCat.of (localizedCompletion A f)
```

**`AlgebraicGeometry.spf_isThickening_isIso_isSheaf_isLocalRing_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBasicOpenAffine.lean#L190). The attribute's comment: “the formal spectrum (Spf A, 𝒪\_\{Spf A}) of an admissible topological ring”.

> **Stacks 0AHY: the formal spectrum of an admissible topological ring.** For an admissible
> topological ring `A` (with its ideals of definition `I_λ`, which form a fundamental system of
> neighbourhoods of `0`):
>
> * for `I_λ ⊆ I_μ` the morphism `Spec (A/I_μ) → Spec (A/I_λ)` is a thickening;
> * each `Spec (A/I_λ) → Spf A` is a homeomorphism onto the space of open primes;
> * `𝒪_{Spf A} = lim 𝒪_λ` is a sheaf of topological rings whose stalks are local rings, so
>   `(Spf A, 𝒪_{Spf A})` is a locally topologically ringed space;
> * `Γ(Spf A, 𝒪_{Spf A}) = A` as topological rings;
> * for `f ∈ A`, `Γ(D(f) ∩ Spf A, 𝒪_{Spf A}) = A_{\{f\}} = lim (A/I_λ)_f` as topological rings,
>   `A_{\{f\}}` is admissible, and `(Spf A_{\{f\}}, 𝒪)` is isomorphic to
>   `(D(f) ∩ Spf A, 𝒪_{Spf A}|_{D(f) ∩ Spf A})`.
>
> The remaining assertions of the section are recorded separately: the bijection
> `Mor_{LTRS}(Spf B, Spf A) = Hom_cont(A, B)` is Stacks 0AHZ
> (`AlgebraicGeometry.bijective_spfLTRSMap`), the full faithfulness of
> `Schemes → Formal Schemes` is Stacks 0AI0, the identification `Spf A = Spec A` for discrete `A`
> is `AlgebraicGeometry.isAdmissible_discrete` and `AlgebraicGeometry.discreteSpecSpfIsoOn`, and the
> adjunction and equivalence of pseudo-discrete sheaves are
> `AlgebraicGeometry.pseudoDiscreteSetSheafAdjunction` and
> `AlgebraicGeometry.pseudoDiscreteSetSheafEquivalence` (sets),
> `AlgebraicGeometry.pseudoDiscreteGroupSheafAdjunction` and
> `AlgebraicGeometry.pseudoDiscreteGroupSheafEquivalence` (groups),
> `AlgebraicGeometry.pseudoDiscreteSheafAdjunction` and
> `AlgebraicGeometry.pseudoDiscreteSheafEquivalence` (rings), and
> `AlgebraicGeometry.pseudoDiscreteModuleSheafAdjunction` and
> `AlgebraicGeometry.pseudoDiscreteModuleSheafEquivalence` (modules over a ring).

```lean
theorem spf_isThickening_isIso_isSheaf_isLocalRing_basicOpen (hA : IsAdmissible A) :
    (IsFundamentalIdealSystem A IsIdealOfDefinition) ∧
    (∀ (I J : IdealsOfDefinition A) (hJI : J.1 ≤ I.1),
      Stacks.Thickenings.IsThickening
        (Spec.map (CommRingCat.ofHom (Ideal.Quotient.factor hJI)))) ∧
    (∀ I : IdealsOfDefinition A, IsIso (spfOfQuotient A I)) ∧
    (spfPresheaf A).IsSheaf ∧
    (∀ x : spfSpace A, IsLocalRing ((spfPresheaf A).stalk x).α) ∧
    IsIso (spfGammaHom A) ∧
    (∀ f : A,
      Nonempty ((spfPresheaf A).obj (op (spfBasicOpen A f)) ≅
        TopCommRingCat.of (localizedCompletion A f)) ∧
      Nonempty ((spfPresheaf A).obj (op (spfBasicOpen A f)) ≅
        limit (spfAwayDiagramOn A IsIdealOfDefinition f)) ∧
      IsAdmissible (localizedCompletion A f) ∧
      Nonempty ((Spf A).restrict (f := (spfBasicOpen A f).inclusion')
        (spfBasicOpen A f).isOpenEmbedding' ≅ Spf (localizedCompletion A f)))
```

**`AlgebraicGeometry.isIso_spfGammaHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean, line 587](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean#L587). The attribute's comment: “Γ(Spf A, 𝒪\_\{Spf A}) = A for an admissible topological ring”.

> **Stacks 0AHY**, the source's deferred verification `Γ(D(f) ∩ Spf A, 𝒪_{Spf A}) = A_{\{f\}}`
> in the case `f = 1`: for an admissible topological ring the canonical map
> `A → Γ(Spf A, 𝒪_{Spf A})` is an isomorphism of topological rings.
>
> The global sections of `𝒪_{Spf A} = lim 𝒪_λ` are the limit of the discrete rings
> `Γ(Spec (A/I_λ), 𝒪) = A/I_λ`, and an admissible ring is precisely the limit of its quotients by
> its ideals of definition. The identification for a general `f` is
> `AlgebraicGeometry.spfBasicOpenGammaIso`, and the facts of the section about `Spf A` are collected
> in `AlgebraicGeometry.spf_isThickening_isIso_isSheaf_isLocalRing_basicOpen`.

```lean
theorem isIso_spfGammaHom [IsLinearTopology A A] (hA : IsAdmissible A) :
    IsIso (spfGammaHom A)
```

**`AlgebraicGeometry.spfGammaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean#L596). The attribute's comment: “Γ(Spf A, 𝒪\_\{Spf A}) = A for an admissible topological ring”.

> **Stacks 0AHY.** The identification `A = Γ(Spf A, 𝒪_{Spf A})` of topological rings, for an
> admissible topological ring `A`.

```lean
noncomputable def spfGammaIso [IsLinearTopology A A] (hA : IsAdmissible A) :
    TopCommRingCat.of A ≅ (spfPresheaf A).obj (op ⊤)
```

**`AlgebraicGeometry.pseudoDiscreteSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteEquivalence.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteEquivalence.lean#L172). The attribute's comment: “the pseudo-discrete construction is adjoint to the forgetful functor”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation of
> sheaves of rings is left adjoint to the forgetful functor from sheaves of topological rings to
> sheaves of rings.

```lean
noncomputable def pseudoDiscreteSheafAdjunction :
    pseudoDiscreteSheafFunctor X ⊣ sheafForgetTopology X
```

**`AlgebraicGeometry.pseudoDiscreteSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteEquivalence.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteEquivalence.lean#L228). The attribute's comment: “equivalence between sheaves of rings and pseudo-discrete sheaves of topological rings”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation is an
> equivalence between the category of sheaves of rings and the category of pseudo-discrete sheaves
> of topological rings; its inverse forgets the topology.

```lean
noncomputable def pseudoDiscreteSheafEquivalence :
    Sheaf (Opens.grothendieckTopology X) CommRingCat.{u} ≌ PseudoDiscreteSheaf X
```

**`AlgebraicGeometry.pseudoDiscreteSetSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopCat.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopCat.lean#L338). The attribute's comment: “the pseudo-discrete construction on sheaves of sets is adjoint to the forgetful functor”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation of
> sheaves of sets is left adjoint to the forgetful functor from sheaves of topological spaces to
> sheaves of sets.

```lean
noncomputable def pseudoDiscreteSetSheafAdjunction :
    pseudoDiscreteSetSheafFunctor X ⊣ sheafForgetTopCat X
```

**`AlgebraicGeometry.pseudoDiscreteSetSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopCat.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopCat.lean#L396). The attribute's comment: “equivalence between sheaves of sets and pseudo-discrete sheaves of topological spaces”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation is an
> equivalence between the category of sheaves of sets and the category of pseudo-discrete sheaves of
> topological spaces; its inverse forgets the topology.

```lean
noncomputable def pseudoDiscreteSetSheafEquivalence :
    Sheaf (Opens.grothendieckTopology X) (Type u) ≌ PseudoDiscreteTopSheaf X
```

**`AlgebraicGeometry.pseudoDiscreteGroupSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopGrp.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopGrp.lean#L293). The attribute's comment: “the pseudo-discrete construction on sheaves of groups is adjoint to the forgetful functor”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation of
> sheaves of groups is left adjoint to the forgetful functor from sheaves of topological groups to
> sheaves of groups.

```lean
noncomputable def pseudoDiscreteGroupSheafAdjunction :
    pseudoDiscreteGroupSheafFunctor X ⊣ sheafForgetTopGrp X
```

**`AlgebraicGeometry.pseudoDiscreteGroupSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopGrp.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopGrp.lean#L355). The attribute's comment: “equivalence between sheaves of groups and pseudo-discrete sheaves of topological groups”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation is an
> equivalence between the category of sheaves of groups and the category of pseudo-discrete sheaves
> of topological groups; its inverse forgets the topology.

```lean
noncomputable def pseudoDiscreteGroupSheafEquivalence :
    Sheaf (Opens.grothendieckTopology X) GrpCat.{u} ≌ PseudoDiscreteGroupSheaf X
```

**`AlgebraicGeometry.pseudoDiscreteModuleSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopModuleCat.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopModuleCat.lean#L227). The attribute's comment: “the pseudo-discrete construction on sheaves of modules is adjoint to the forgetful functor”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation of
> sheaves of modules over a ring is left adjoint to the forgetful functor from sheaves of
> topological modules to sheaves of modules.

```lean
noncomputable def pseudoDiscreteModuleSheafAdjunction :
    pseudoDiscreteModuleSheafFunctor X R ⊣ sheafForgetTopModuleCat X R
```

**`AlgebraicGeometry.pseudoDiscreteModuleSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopModuleCat.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/PseudoDiscreteTopModuleCat.lean#L289). The attribute's comment: “equivalence between sheaves of modules and pseudo-discrete sheaves of topological modules”.

> **Stacks 0AHY**: on a space with a basis of quasi-compact opens, pseudo-discretisation is an
> equivalence between the category of sheaves of modules over a ring and the category of
> pseudo-discrete sheaves of topological modules; its inverse forgets the topology.

```lean
noncomputable def pseudoDiscreteModuleSheafEquivalence :
    Sheaf (Opens.grothendieckTopology X) (ModuleCat.{u} R) ≌ PseudoDiscreteModuleSheaf X R
```

## Tag 0AHZ, an equation

[Tag 0AHZ](https://stacks.math.columbia.edu/tag/0AHZ) in the Stacks Project.

**`AlgebraicGeometry.injective_spfLTRSMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBijection.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumBijection.lean#L396). The attribute's comment: “injectivity of the comparison map Hom\_cont(A, B) → Mor\_LTRS(Spf B, Spf A)”. References: EGA I (10.4.6), “Affine case X = Spf B”; SGA 3 VIIB (1.1), “partial”.

> **Stacks 0AHZ**, injectivity of the comparison map. In the identification
> `Mor_{LTRS}((Spf B, 𝒪_{Spf B}), (Spf A, 𝒪_{Spf A})) = Hom_cont(A, B)` the map from continuous
> ring homomorphisms to morphisms of formal spectra is injective as soon as `B` is separated and
> linearly topologized: a morphism determines the map it induces on global sections, that map is
> the homomorphism read through the canonical maps into global sections, and the canonical map of
> `B` is injective.

```lean
theorem injective_spfLTRSMap [IsLinearTopology B B] [T2Space B] :
    Function.Injective (spfLTRSMap A B hA I₀ hB)
```

**`AlgebraicGeometry.surjective_spfLTRSMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumSurjectivity.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumSurjectivity.lean#L382). The attribute's comment: “surjectivity of the comparison map Hom\_cont(A, B) → Mor\_LTRS(Spf B, Spf A)”. References: EGA I (10.2.2); EGA I (10.4.6), “Affine case X = Spf B”; SGA 3 VIIB (1.1), “partial”.

> **Morphisms of formal spectra come from continuous ring maps.** Every morphism
> `g : Spf B → Spf A` of locally topologically ringed spaces between the formal spectra of admissible
> topological rings comes from a continuous ring homomorphism `A → B`, namely from
> `AlgebraicGeometry.ltrsGlobalSectionsRingHom g`, the map `g` induces on global sections read
> through the identifications `Γ(Spf A, 𝒪_{Spf A}) = A` and `Γ(Spf B, 𝒪_{Spf B}) = B` of Stacks 0AHY.

```lean
theorem surjective_spfLTRSMap : Function.Surjective (spfLTRSMap A B hA.1 I₀ hB.1)
```

**`AlgebraicGeometry.bijective_spfLTRSMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumSurjectivity.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumSurjectivity.lean#L400). The attribute's comment: “the full bijection Hom\_cont(A, B) = Mor\_LTRS(Spf B, Spf A) for admissible A, B”. References: SGA 3 VIIB (1.1), “partial”.

> **Stacks 0AHZ.** For admissible topological rings `A` and `B` the comparison map taking a
> continuous ring homomorphism `A → B` to the induced morphism `Spf B → Spf A` of locally
> topologically ringed spaces is a bijection: it is injective by
> `AlgebraicGeometry.injective_spfLTRSMap`, separatedness of `B` making the canonical map
> `B → Γ(Spf B, 𝒪_{Spf B})` injective, and surjective by
> `AlgebraicGeometry.surjective_spfLTRSMap`.

```lean
theorem bijective_spfLTRSMap : Function.Bijective (spfLTRSMap A B hA.1 I₀ hB.1)
```

## Tag 0AI0, an equation

[Tag 0AI0](https://stacks.math.columbia.edu/tag/0AI0) in the Stacks Project.

**`AlgebraicGeometry.schemeToFormalScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/SchemeToFormalScheme.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/SchemeToFormalScheme.lean#L273).

> **Stacks 0AI0.** The functor `Schemes ⟶ Formal Schemes`: pseudo-discretisation, a scheme
> being a formal scheme by `AlgebraicGeometry.isFormalScheme_schemeToLTRSObj`.

```lean
noncomputable def schemeToFormalScheme : Scheme.{u} ⥤ FormalScheme.{u}
```

**`AlgebraicGeometry.full_schemeToFormalScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/SchemeToFormalScheme.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/SchemeToFormalScheme.lean#L295). The attribute's comment: “full faithfulness: fullness”.

> **Stacks 0AI0.** The functor from schemes to formal schemes is full: a morphism of the
> pseudo-discretised spaces has an automatically continuous comparison map, so it is the image of
> the morphism of schemes with the same data.

```lean
instance full_schemeToFormalScheme : schemeToFormalScheme.{u}.Full
```

**`AlgebraicGeometry.faithful_schemeToFormalScheme`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/SchemeToFormalScheme.lean, line 304](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/SchemeToFormalScheme.lean#L304). The attribute's comment: “full faithfulness: faithfulness”.

> **Stacks 0AI0.** The functor from schemes to formal schemes is faithful: a morphism of
> schemes is recovered from its pseudo-discretisation by forgetting the topologies.

```lean
instance faithful_schemeToFormalScheme : schemeToFormalScheme.{u}.Faithful
```

## Tag 0AI1, a lemma

[Tag 0AI1](https://stacks.math.columbia.edu/tag/0AI1) in the Stacks Project.

**`AlgebraicGeometry.injective_formalSchemeFunctorOfPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPoints.lean, line 587](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPoints.lean#L587). The attribute's comment: “injectivity: a morphism of formal schemes is determined by the induced transformation of functors of points”.

> **Stacks 0AI1**, injectivity. A morphism of formal schemes whose source satisfies the size
> condition is determined by the natural transformation it induces on functors of points on the
> schemes of size below `κ`.
>
> The morphisms `Spec (A/I_λ) → Spf A ≅ 𝔛|_𝔘 → 𝔛` attached to the affine formal charts of `𝔛` are
> jointly epimorphic, and the size condition is exactly what makes them morphisms out of objects
> of `Sch_κ`, hence points of `𝔛` seen by the functor of points. Their underlying maps cover `𝔛`
> because each `Spec (A/I_λ) → Spf A` is a homeomorphism; and they separate the sections of
> `𝒪_𝔛`, because `𝒪_𝔛` is a sheaf and the sections of `𝒪_{Spf A} = lim 𝒪_λ` are a limit.

```lean
theorem injective_formalSchemeFunctorOfPoints_map {κ : Cardinal.{u}} {X Y : FormalScheme.{u}}
    (hX : IsSizeBoundedFormalScheme κ X.obj) :
    Function.Injective fun f : X ⟶ Y => (formalSchemeFunctorOfPoints κ).map f
```

**`AlgebraicGeometry.bijective_formalSchemeFunctorOfPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFull.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFull.lean#L652). The attribute's comment: “the bijection Mor(𝔛, 𝔜) = Mor(h\_𝔛, h\_𝔜) for a formal scheme 𝔛 whose size is bounded by the cutoff”.

> **Morphisms of formal schemes are transformations of functors of points.** For a formal scheme
> `𝔛` whose size is not too large — the schemes `Spec (A/I_λ)` cut out of its affine formal charts
> being objects of `Sch_κ` — and any formal scheme `𝔜`,
>
> `Mor_{Formal Schemes}(𝔛, 𝔜) = Mor_{PSh(Sch_κ)}(h_𝔛, h_𝔜)`.

```lean
theorem bijective_formalSchemeFunctorOfPoints_map {κ : Cardinal.{u}} {X Y : FormalScheme.{u}}
    (hX : IsSizeBoundedFormalScheme κ X.obj) :
    Function.Bijective fun f : X ⟶ Y => (formalSchemeFunctorOfPoints κ).map f
```

**`AlgebraicGeometry.exists_formalSchemePointsFunctor_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean#L62). The attribute's comment: “surjectivity on all schemes: every transformation of functors of points is induced by a morphism of formal schemes, with no size hypothesis”.

> Every transformation `h_𝔛 → h_𝔜` of functors of points on the category of all schemes is
> induced by a morphism of formal schemes `𝔛 → 𝔜`, with no size hypothesis.

```lean
theorem exists_formalSchemePointsFunctor_map_eq {X Y : FormalScheme.{u}}
    (φ : formalSchemePointsFunctor.obj X ⟶ formalSchemePointsFunctor.obj Y) :
    ∃ f : X ⟶ Y, formalSchemePointsFunctor.map f = φ
```

**`AlgebraicGeometry.bijective_formalSchemePointsFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean#L96). The attribute's comment: “the bijection Mor(𝔛, 𝔜) = Mor(h\_𝔛, h\_𝔜) on all schemes, with no size hypothesis”.

> For formal schemes `𝔛` and `𝔜`, the functor of points on the category of all schemes induces
> a bijection
>
> `Mor_{Formal Schemes}(𝔛, 𝔜) = Mor_{PSh(Sch)}(h_𝔛, h_𝔜)`,
>
> with no size hypothesis.

```lean
theorem bijective_formalSchemePointsFunctor_map {X Y : FormalScheme.{u}} :
    Function.Bijective fun f : X ⟶ Y => formalSchemePointsFunctor.map f
```

**`AlgebraicGeometry.full_formalSchemePointsFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFullSupplement.lean#L104). The attribute's comment: “fullness of the functor of points on morphisms, with no size hypothesis”.

> The functor of points of formal schemes on the category of all schemes is full, with no size
> hypothesis.

```lean
instance full_formalSchemePointsFunctor : formalSchemePointsFunctor.{u}.Full
```

**`AlgebraicGeometry.injective_formalSchemePointsFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean#L73). The attribute's comment: “injectivity of the functor of points on morphisms, with no size hypothesis”.

> A morphism of formal schemes is determined by the natural transformation it induces on
> functors of points on the category of all schemes.

```lean
theorem injective_formalSchemePointsFunctor_map {X Y : FormalScheme.{u}} :
    Function.Injective fun f : X ⟶ Y => formalSchemePointsFunctor.map f
```

## Tag 0AI2, a lemma

[Tag 0AI2](https://stacks.math.columbia.edu/tag/0AI2) in the Stacks Project.

**`AlgebraicGeometry.isSheafFor_formalSchemeFunctorOfPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFpqcDescent.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFpqcDescent.lean#L290).

> **Stacks 0AI2** for the functor of points of Stacks 0AI1, on the schemes of size below `κ`:
> it satisfies the sheaf condition for every family of morphisms of `Sch_κ` which is an fpqc
> covering.
>
> Members of `Sch_κ` have their fibre products in `Sch_κ`
> (`AlgebraicGeometry.Scheme.size_pullback_lt`), so a family of points compatible on `Sch_κ` is
> compatible on all schemes, and `AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints`
> applies.

```lean
theorem isSheafFor_formalSchemeFunctorOfPoints {κ : Cardinal.{u}} (X : FormalScheme.{u})
    {T : (schemeCutoff κ).FullSubcategory} {R : Presieve T}
    (covering : R ∈ Scheme.fpqcPrecoverage.{u}.comap (schemeCutoff κ).ι T) :
    Presieve.IsSheafFor ((formalSchemeFunctorOfPoints κ).obj X) R
```

**`AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints_of_isoSpf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFpqcDescentSupplement.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsFpqcDescentSupplement.lean#L49). The attribute's comment: “sheaf condition with gluing, for a formal scheme isomorphic to a formal spectrum”.

> **Stacks 0AI2**, the gluing clause included, for an affine formal scheme: the functor of
> points of a formal scheme isomorphic to a formal spectrum is an fpqc sheaf.
>
> Transporting along the isomorphism reduces this to
> `AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints_spfFormalScheme`.

```lean
theorem isSheaf_fpqcTopology_formalSchemePoints_of_isoSpf {X : FormalScheme.{u}}
    (hA : IsAdmissible A) (e : X ≅ spfFormalScheme A hA) :
    Presieve.IsSheaf Scheme.fpqcTopology.{u} (formalSchemePoints X)
```

**`AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints_schemeToFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean#L109). The attribute's comment: “sheaf condition with gluing, for a scheme seen as a formal scheme”.

> The functor of points of a scheme seen as a formal scheme satisfies the sheaf condition,
> gluing included, for fpqc coverings of schemes.

```lean
theorem isSheaf_fpqcTopology_formalSchemePoints_schemeToFormalScheme (Z : Scheme.{u}) :
    Presieve.IsSheaf Scheme.fpqcTopology.{u}
      (formalSchemePoints (schemeToFormalScheme.obj Z))
```

**`AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsSheaf.lean#L119). The attribute's comment: “sheaf condition with gluing, for a formal scheme isomorphic to a scheme”.

> The functor of points of a formal scheme isomorphic to a scheme satisfies the sheaf
> condition, gluing included, for fpqc coverings of schemes.

```lean
theorem isSheaf_fpqcTopology_formalSchemePoints_of_iso {X : FormalScheme.{u}} {Z : Scheme.{u}}
    (e : X ≅ schemeToFormalScheme.obj Z) :
    Presieve.IsSheaf Scheme.fpqcTopology.{u} (formalSchemePoints X)
```

**`AlgebraicGeometry.isSheaf_zariskiTopology_formalSchemePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsZariskiSheaf.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FunctorOfPointsZariskiSheaf.lean#L96). The attribute's comment: “Zariski case in full, separatedness and gluing: the functor of points is a sheaf for the big Zariski topology on all schemes”.

> **Stacks 0AI2**, the Zariski case in full. The functor of points of a formal scheme, on the
> category of all schemes, is a sheaf for the big Zariski topology: a matching family of points on
> the members of any Zariski covering of a scheme has a unique amalgamation.
>
> Zariski coverings are the jointly surjective families of open immersions, so this follows from
> `AlgebraicGeometry.isSheafFor_ofArrows_formalSchemePoints` once the sheaf condition for a
> Grothendieck topology generated by a precoverage is reduced to its covering families, which is
> `CategoryTheory.Precoverage.isSheaf_toGrothendieck_iff_of_isStableUnderBaseChange`.

```lean
theorem isSheaf_zariskiTopology_formalSchemePoints (X : FormalScheme.{u}) :
    Presieve.IsSheaf Scheme.zariskiTopology.{u} (formalSchemePoints X)
```

**`AlgebraicGeometry.FormalSpace.isFppfSheafFormalSchemePoints_formalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonSheaf.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalSchemeComparisonSheaf.lean#L164). The attribute's comment: “the fpqc sheaf condition read on the big fppf site of a base scheme”.

> **Stacks 0AIR**, the sheaf clause, for an *arbitrary* formal scheme: the functor of points
> of a formal scheme à la EGA satisfies the fppf sheaf condition on the big fppf site of `S`, with
> no hypothesis assumed.
>
> This is the first sentence of the source's remark, "by Lemma 87.2.2 the functor of points
> `h_𝔛` associated to a formal scheme `𝔛` is a sheaf in the fppf topology". It is
> `AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints`, the full statement of Stacks 0AI2,
> read on the big fppf site of `S` by
> `AlgebraicGeometry.FormalSpace.isFppfSheafFormalSchemePoints_of_isSheaf_fpqcTopology`.

```lean
theorem isFppfSheafFormalSchemePoints_formalScheme (X : FormalScheme.{u}) :
    IsFppfSheafFormalSchemePoints B S hS X
```

## Tag 0AI3, a remark

[Tag 0AI3](https://stacks.math.columbia.edu/tag/0AI3) in the Stacks Project.

**`AlgebraicGeometry.isIso_spfwGammaHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean#L623). The attribute's comment: “the identification the counterparts of Lemmas 87.2.1 and 87.2.2 consume: Γ(Spfw A, 𝒪) = A for a weakly admissible ring, over the whole system of weak ideals of definition”.

> **The counterpart for McQuillan's weakening of the identification
> `Γ(Spf A, 𝒪_{Spf A}) = A`.** For a weakly admissible topological ring `A` the canonical map
> `A → Γ(Spfw A, 𝒪)` into the global sections of the formal spectrum taken along the *weak* ideals
> of definition of `A` is an isomorphism of topological rings.
>
> The proof is the one for an admissible ring, run over the whole family of weak ideals of
> definition instead of over the powers of a single ideal of definition. What it needs of the
> family is exactly that its members are open, that it is closed under intersection, and that it is
> a fundamental system of open neighbourhoods of zero — the last two being the intersection clause
> and the fundamental-system clause of Stacks 0AI3 — together with completeness and separatedness
> of `A`. The cofinality of the powers `Iⁿ` of a single `I`, which an ideal of definition has and a
> weak ideal of definition need not, is used nowhere.

```lean
theorem isIso_spfwGammaHom [IsLinearTopology A A] (hA : IsWeaklyAdmissible A) :
    IsIso (spfGammaHomOn A IsWeakIdealOfDefinition)
```

**`AlgebraicGeometry.spfwGammaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/FormalSpectrumGlobalSectionsIso.lean#L633). The attribute's comment: “the identification the counterparts of Lemmas 87.2.1 and 87.2.2 consume: A = Γ(Spfw A, 𝒪) as topological rings, for a weakly admissible ring”.

> **The identification `A = Γ(Spfw A, 𝒪)` of topological rings** for a weakly admissible
> topological ring: McQuillan's counterpart of the identification `Γ(Spf A, 𝒪_{Spf A}) = A`.

```lean
noncomputable def spfwGammaIso [IsLinearTopology A A] (hA : IsWeaklyAdmissible A) :
    TopCommRingCat.of A ≅ (spfPresheafOn A IsWeakIdealOfDefinition).obj (op ⊤)
```

**`AlgebraicGeometry.IsMcQuillanFormalScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L115). The attribute's comment: “the larger category of formal schemes based on weak admissibility: its objects”.

> An object of `LTRS` is a *formal scheme in the sense of McQuillan* when every point has an
> open neighbourhood isomorphic to the formal spectrum, taken along the weak ideals of definition,
> of a weakly admissible topological ring. As for `AlgebraicGeometry.IsFormalScheme`, the
> isomorphism is asked for as one of presheafed spaces of topological rings, which for objects of
> `LTRS` is the same as an isomorphism in `LTRS`.

```lean
def IsMcQuillanFormalScheme : ObjectProperty LTRS.{u}
```

**`AlgebraicGeometry.McQuillanFormalScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L126). The attribute's comment: “the larger category of formal schemes based on weak admissibility: the category”.

> The category of *McQuillan formal schemes*: the full subcategory of `LTRS` on the objects
> locally isomorphic to a formal spectrum taken along the weak ideals of definition of a weakly
> admissible topological ring. A morphism is a morphism of `LTRS`.

```lean
abbrev McQuillanFormalScheme
```

**`AlgebraicGeometry.injective_mcQuillanFormalSchemeFunctorOfPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L255). The attribute's comment: “the counterpart of Lemma 87.2.1: a morphism of McQuillan formal schemes is determined by the induced transformation of functors of points”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.1 in McQuillan's setting. A morphism of
> McQuillan formal schemes whose source satisfies the size condition is determined by the natural
> transformation it induces on functors of points on the schemes of size below `κ`.
>
> The proof is the source's: the morphisms `Spec (A/I_λ) → 𝔛|_𝔘 → 𝔛` attached to the charts of
> `𝔛` are jointly epimorphic, and the size condition makes them points of `𝔛` seen by the functor
> of points. Their underlying maps cover `𝔛` because each `Spec (A/I_λ)` is carried
> homeomorphically onto the space of open primes of `A`, a prime being open exactly when it
> contains the weak ideal of definition `I_λ`; and they separate the sections of `𝒪_𝔛` because
> `𝒪_𝔛` is a sheaf and the sections of the structure presheaf of the chart are the limit over the
> weak ideals of definition.

```lean
theorem injective_mcQuillanFormalSchemeFunctorOfPoints_map {κ : Cardinal.{u}}
    {X Y : McQuillanFormalScheme.{u}} (hX : IsSizeBoundedMcQuillanFormalScheme κ X.obj) :
    Function.Injective fun f : X ⟶ Y => (mcQuillanFormalSchemeFunctorOfPoints κ).map f
```

**`AlgebraicGeometry.injective_mcQuillanFormalSchemePointsFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L272). The attribute's comment: “the counterpart of Lemma 87.2.1: injectivity of the functor of points on morphisms of McQuillan formal schemes, with no size hypothesis”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.1 in McQuillan's setting, with no size
> hypothesis: a morphism of McQuillan formal schemes is determined by the transformation it
> induces on functors of points on all schemes. Every McQuillan formal scheme satisfies the size
> condition for some cutoff, and the functor of points on `Sch_κ` is the restriction of the
> functor of points on all schemes.

```lean
theorem injective_mcQuillanFormalSchemePointsFunctor_map {X Y : McQuillanFormalScheme.{u}} :
    Function.Injective fun f : X ⟶ Y => mcQuillanFormalSchemePointsFunctor.map f
```

**`AlgebraicGeometry.isSeparated_fpqcTopology_mcQuillanFormalSchemePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L293). The attribute's comment: “the counterpart of Lemma 87.2.2: the functor of points of a McQuillan formal scheme on all schemes is separated for the fpqc topology”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.2 in McQuillan's setting. The functor of
> points of a McQuillan formal scheme, on the category of all schemes, is separated for the fpqc
> topology: a point of `𝔛` over a scheme `T` is determined by its restrictions along any fpqc
> covering sieve of `T`.
>
> The proof is the source's: an fpqc covering sieve contains an fpqc covering family, whose
> members are flat and jointly surjective, and a morphism from a scheme to a locally topologically
> ringed space is determined by its restrictions along such a family.

```lean
theorem isSeparated_fpqcTopology_mcQuillanFormalSchemePoints (X : McQuillanFormalScheme.{u}) :
    Presieve.IsSeparated Scheme.fpqcTopology.{u} (mcQuillanFormalSchemePoints X)
```

**`AlgebraicGeometry.isSeparatedFor_mcQuillanFormalSchemeFunctorOfPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L306). The attribute's comment: “the counterpart of Lemma 87.2.2: the functor of points of a McQuillan formal scheme on the schemes of size below the cutoff is separated for the fpqc topology”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.2 in McQuillan's setting, for the functor of
> points on the schemes of size below `κ`: a point of `𝔛` over a scheme `T` of `Sch_κ` is
> determined by its restrictions along a family of morphisms of `Sch_κ` which is an fpqc covering
> of `T`.

```lean
theorem isSeparatedFor_mcQuillanFormalSchemeFunctorOfPoints {κ : Cardinal.{u}}
    (X : McQuillanFormalScheme.{u}) {T : (schemeCutoff κ).FullSubcategory} {R : Presieve T}
    (hR : R ∈ Scheme.fpqcPrecoverage.{u}.comap (schemeCutoff κ).ι T) :
    Presieve.IsSeparatedFor ((mcQuillanFormalSchemeFunctorOfPoints κ).obj X) R
```

**`AlgebraicGeometry.isSheaf_zariskiTopology_mcQuillanFormalSchemePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/McQuillanFormalScheme.lean#L381). The attribute's comment: “the counterpart of Lemma 87.2.2: the functor of points of a McQuillan formal scheme on all schemes is a sheaf for the big Zariski topology”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.2 in McQuillan's setting, for the big Zariski
> topology. The functor of points of a McQuillan formal scheme, on the category of all schemes, is
> a sheaf for the big Zariski topology: a matching family of points on the members of any Zariski
> covering of a scheme has a unique amalgamation.
>
> The proof is the source's: Zariski coverings are the jointly surjective families of open
> immersions, and a matching family of morphisms into a locally topologically ringed space on the
> members of an open covering glues uniquely.

```lean
theorem isSheaf_zariskiTopology_mcQuillanFormalSchemePoints (X : McQuillanFormalScheme.{u}) :
    Presieve.IsSheaf Scheme.zariskiTopology.{u} (mcQuillanFormalSchemePoints X)
```

**`AlgebraicGeometry.exists_comp_eq_of_flat_surjective_spfwLTRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFormalSpectrumFpqcDescent.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFormalSpectrumFpqcDescent.lean#L125). The attribute's comment: “the counterpart of Lemma 87.2.2: existence of an amalgamation at an affine test scheme, for a point of McQuillan's formal spectrum of a weakly admissible ring along a faithfully flat morphism of affine schemes”.

> **Stacks 0AI3**, the existence half of the counterpart of Lemma 87.2.2 at an affine test
> scheme. For a weakly admissible topological ring `A`, a point `Spec S ⟶ Spfw A` of McQuillan's
> formal spectrum whose two pullbacks along any pair of morphisms agreeing over `Spec R` agree
> descends along a faithfully flat morphism `Spec S → Spec R` of affine schemes.
>
> This is the affine descent step the source's proof of Lemma 87.2.2 reduces to, and it is that
> proof unchanged: the weak ideals of definition of `A` form a weak ideal system, and the
> identification `Γ(Spfw A, 𝒪) = A` it consumes is
> `AlgebraicGeometry.isIso_spfwGammaHom`. The separatedness half, which together with this one is
> the sheaf condition for the covering `{Spec S → Spec R}`, is
> `AlgebraicGeometry.isSeparated_fpqcTopology_mcQuillanFormalSchemePoints`.

```lean
theorem exists_comp_eq_of_flat_surjective_spfwLTRS (hA : IsWeaklyAdmissible A)
    {R S : CommRingCat.{u}} (φ : R ⟶ S) (hflat : Flat (Spec.map φ))
    (hsurj : Surjective (Spec.map φ)) (u : schemeToLTRSObj (Spec S) ⟶ spfwLTRS A hA.1)
    (hu : ∀ {Z : Scheme.{u}} (p₁ p₂ : Z ⟶ Spec S), p₁ ≫ Spec.map φ = p₂ ≫ Spec.map φ →
      schemeToLTRS.map p₁ ≫ u = schemeToLTRS.map p₂ ≫ u) :
    ∃ t : schemeToLTRSObj (Spec R) ⟶ spfwLTRS A hA.1,
      schemeToLTRS.map (Spec.map φ) ≫ t = u
```

**`AlgebraicGeometry.isSheaf_fpqcTopology_mcQuillanFormalSchemePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFunctorOfPointsFpqcSheaf.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFunctorOfPointsFpqcSheaf.lean#L242). The attribute's comment: “the counterpart of Lemma 87.2.2: the functor of points of a McQuillan formal scheme on all schemes is a sheaf for the fpqc topology”.

> **Stacks 0AI3**, the existence half of the counterpart of Lemma 87.2.2 in McQuillan's setting,
> and so the full sheaf condition. The functor of points of a McQuillan formal scheme `𝔛`, on the
> category of all schemes, satisfies the sheaf condition for fpqc coverings.
>
> The proof is the source's, and is the one already carried out for admissible rings in
> `AlgebraicGeometry.isSheaf_fpqcTopology_formalSchemePoints`. Uniqueness of amalgamations is
> `AlgebraicGeometry.isSeparated_fpqcTopology_mcQuillanFormalSchemePoints`. For existence, a
> compatible family of points first descends on underlying spaces to a continuous map `g : T → 𝔛`,
> continuous maps into a fixed space forming an fpqc sheaf. Around each point `p` of `T` choose a
> weak affine formal chart `𝔘 ≅ Spfw A` of `𝔛` containing `g p`; over the open `g⁻¹ 𝔘` every member
> of the pulled-back family lands in `𝔘`, so it has an amalgamation by
> `AlgebraicGeometry.exists_isAmalgamation_of_range_subset_weakChart`. These local amalgamations
> glue because the functor of points is a Zariski sheaf
> (`AlgebraicGeometry.isSheaf_zariskiTopology_mcQuillanFormalSchemePoints`).

```lean
theorem isSheaf_fpqcTopology_mcQuillanFormalSchemePoints (X : McQuillanFormalScheme.{u}) :
    Presieve.IsSheaf Scheme.fpqcTopology.{u} (mcQuillanFormalSchemePoints X)
```

**`AlgebraicGeometry.isSheafFor_mcQuillanFormalSchemeFunctorOfPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFunctorOfPointsFpqcSheaf.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFunctorOfPointsFpqcSheaf.lean#L288). The attribute's comment: “the counterpart of Lemma 87.2.2: the functor of points of a McQuillan formal scheme on the schemes of size below the cutoff is a sheaf for the fpqc topology”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.2 in McQuillan's setting for the functor of
> points on the schemes of size below `κ`: it satisfies the sheaf condition for every family of
> morphisms of `Sch_κ` which is an fpqc covering.
>
> Members of `Sch_κ` have their fibre products in `Sch_κ`
> (`AlgebraicGeometry.Scheme.size_pullback_lt`), so a family of points compatible on `Sch_κ` is
> compatible on all schemes, and
> `AlgebraicGeometry.isSheaf_fpqcTopology_mcQuillanFormalSchemePoints` applies.

```lean
theorem isSheafFor_mcQuillanFormalSchemeFunctorOfPoints {κ : Cardinal.{u}}
    (X : McQuillanFormalScheme.{u}) {T : (schemeCutoff κ).FullSubcategory} {R : Presieve T}
    (covering : R ∈ Scheme.fpqcPrecoverage.{u}.comap (schemeCutoff κ).ι T) :
    Presieve.IsSheafFor ((mcQuillanFormalSchemeFunctorOfPoints κ).obj X) R
```

**`AlgebraicGeometry.bijective_mcQuillanFormalSchemeFunctorOfPoints_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFunctorOfPointsFull.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakFunctorOfPointsFull.lean#L596). The attribute's comment: “the counterpart of Lemma 87.2.1: the bijection Mor(𝔛, 𝔜) = Mor(h\_𝔛, h\_𝔜) for a McQuillan formal scheme 𝔛 whose size is bounded by the cutoff”.

> **Stacks 0AI3**, the counterpart of Lemma 87.2.1 in McQuillan's setting, in full. For a
> McQuillan formal scheme `𝔛` whose size is not too large — the schemes `Spec (A/I_λ)` cut out of
> its weak affine formal charts being objects of `Sch_κ` — and any McQuillan formal scheme `𝔜`,
>
> `Mor_{McQuillan Formal Schemes}(𝔛, 𝔜) = Mor_{PSh(Sch_κ)}(h_𝔛, h_𝔜)`.
>
> Injectivity is `AlgebraicGeometry.injective_mcQuillanFormalSchemeFunctorOfPoints_map` and
> surjectivity is `AlgebraicGeometry.exists_mcQuillanFormalSchemeFunctorOfPoints_map_eq`.

```lean
theorem bijective_mcQuillanFormalSchemeFunctorOfPoints_map {κ : Cardinal.{u}}
    {X Y : McQuillanFormalScheme.{u}} (hX : IsSizeBoundedMcQuillanFormalScheme κ X.obj) :
    Function.Bijective fun f : X ⟶ Y => (mcQuillanFormalSchemeFunctorOfPoints κ).map f
```

**`TopologicalRing.isWeakIdealOfDefinition_inf_of_isOpen_right`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L218). The attribute's comment: “intersection”.

> The intersection of a weak ideal of definition with an open ideal is a weak ideal of
> definition.

```lean
public lemma isWeakIdealOfDefinition_inf_of_isOpen_right {A : Type*} [CommRing A]
    [TopologicalSpace A] {I J : Ideal A} (hI : TopologicalRing.IsWeakIdealOfDefinition I)
    (hJ : IsOpen (J : Set A)) : TopologicalRing.IsWeakIdealOfDefinition (I ⊓ J)
```

**`TopologicalRing.hasBasis_nhds_zero_isWeakIdealOfDefinition`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L233). The attribute's comment: “weak\_basis”.

> In a weakly admissible linearly topologized ring, its weak ideals of definition form a
> fundamental system of neighborhoods of zero.

```lean
public lemma hasBasis_nhds_zero_isWeakIdealOfDefinition
    {A : Type*} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A]
    [IsLinearTopology A A] (hA : TopologicalRing.IsWeaklyAdmissible A) :
    (nhds (0 : A)).HasBasis
      (fun I : Ideal A ↦ TopologicalRing.IsWeakIdealOfDefinition I)
      (fun I : Ideal A ↦ (I : Set A))
```

Declarations registered for the tag:

- [`TopologicalRing.IsAdmissible`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/AdmissibleRings.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L202) (StacksFrontier): “admissible\_recall”.
- [`TopologicalRing.IsWeakIdealOfDefinition`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L208) (StacksFrontier): “weak\_admissibility”.
- [`TopologicalRing.IsWeaklyAdmissible`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L86), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/WeaklyAdmissible.lean#L209) (StacksFrontier): “weak\_admissibility”.

## Tag 0AI4, a remark

[Tag 0AI4](https://stacks.math.columbia.edu/tag/0AI4) in the Stacks Project.

**`CategoryTheory.TopologicalSheaf.hasLimits_sheaf_topModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L334). The attribute's comment: “limits (topological modules)”.

> **Stacks 0AI4** (limits), for sheaves of topological modules over a topological ring `R`:
> `Sh(C, TopMod_R)` has limits, the inclusion into presheaves preserves them, and limits of
> presheaves are computed sectionwise.

```lean
theorem hasLimits_sheaf_topModuleCat (R : Type (max u v w)) [Ring R] [TopologicalSpace R] :
    HasLimitsOfSize.{max u v w, max u v w} (Sheaf J (TopModuleCat.{max u v w} R)) ∧
      PreservesLimitsOfSize.{max u v w, max u v w}
        (sheafToPresheaf J (TopModuleCat.{max u v w} R)) ∧
      ∀ U : Cᵒᵖ, PreservesLimitsOfSize.{max u v w, max u v w}
        ((evaluation Cᵒᵖ (TopModuleCat.{max u v w} R)).obj U)
```

**`CategoryTheory.TopologicalSheaf.hasLimits_sheaf_topAddCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L344). The attribute's comment: “limits (topological abelian groups)”.

> **Stacks 0AI4** (limits), for sheaves of topological abelian groups.

```lean
theorem hasLimits_sheaf_topAddCommGrpCat :
    HasLimitsOfSize.{max u v w, max u v w} (Sheaf J TopAddCommGrpCat.{max u v w}) ∧
      PreservesLimitsOfSize.{max u v w, max u v w}
        (sheafToPresheaf J TopAddCommGrpCat.{max u v w}) ∧
      ∀ U : Cᵒᵖ, PreservesLimitsOfSize.{max u v w, max u v w}
        ((evaluation Cᵒᵖ TopAddCommGrpCat.{max u v w}).obj U)
```

**`CategoryTheory.TopologicalSheaf.hasLimits_sheaf_topCommRingCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L354). The attribute's comment: “limits (topological rings)”.

> **Stacks 0AI4** (limits), for sheaves of topological rings.

```lean
theorem hasLimits_sheaf_topCommRingCat :
    HasLimitsOfSize.{max u v w, max u v w} (Sheaf J TopCommRingCat.{max u v w}) ∧
      PreservesLimitsOfSize.{max u v w, max u v w}
        (sheafToPresheaf J TopCommRingCat.{max u v w}) ∧
      ∀ U : Cᵒᵖ, PreservesLimitsOfSize.{max u v w, max u v w}
        ((evaluation Cᵒᵖ TopCommRingCat.{max u v w}).obj U)
```

**`CategoryTheory.TopologicalSheaf.exists_bounded_subsheaf_factorization_topModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L366). The attribute's comment: “bounded\_subsheaf (topological modules)”.

> **Stacks 0AI4** (bounded subsheaf), for sheaves of topological modules over a topological
> ring `R`: any map from a fixed presheaf to a sheaf factors through a subsheaf whose values have
> cardinality bounded by a cardinal depending only on the site and the presheaf.

```lean
theorem exists_bounded_subsheaf_factorization_topModuleCat
    (R : Type (max u v w)) [Ring R] [TopologicalSpace R]
    (F : Cᵒᵖ ⥤ TopModuleCat.{max u v w} R) :
    ∃ κ : Cardinal.{max u v w}, ∀ (G : Sheaf J (TopModuleCat.{max u v w} R)) (f : F ⟶ G.obj),
      ∃ (G' : Sheaf J (TopModuleCat.{max u v w} R)) (i : G' ⟶ G), Mono i ∧
        (∀ U : Cᵒᵖ, Cardinal.mk (G'.obj.obj U) ≤ κ) ∧ ∃ f' : F ⟶ G'.obj, f' ≫ i.hom = f
```

**`CategoryTheory.TopologicalSheaf.exists_bounded_subsheaf_factorization_topAddCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L376). The attribute's comment: “bounded\_subsheaf (topological abelian groups)”.

> **Stacks 0AI4** (bounded subsheaf), for sheaves of topological abelian groups.

```lean
theorem exists_bounded_subsheaf_factorization_topAddCommGrpCat
    (F : Cᵒᵖ ⥤ TopAddCommGrpCat.{max u v w}) :
    ∃ κ : Cardinal.{max u v w}, ∀ (G : Sheaf J TopAddCommGrpCat.{max u v w}) (f : F ⟶ G.obj),
      ∃ (G' : Sheaf J TopAddCommGrpCat.{max u v w}) (i : G' ⟶ G), Mono i ∧
        (∀ U : Cᵒᵖ, Cardinal.mk (G'.obj.obj U) ≤ κ) ∧ ∃ f' : F ⟶ G'.obj, f' ≫ i.hom = f
```

**`CategoryTheory.TopologicalSheaf.exists_bounded_subsheaf_factorization_topCommRingCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L385). The attribute's comment: “bounded\_subsheaf (topological rings)”.

> **Stacks 0AI4** (bounded subsheaf), for sheaves of topological rings.

```lean
theorem exists_bounded_subsheaf_factorization_topCommRingCat
    (F : Cᵒᵖ ⥤ TopCommRingCat.{max u v w}) :
    ∃ κ : Cardinal.{max u v w}, ∀ (G : Sheaf J TopCommRingCat.{max u v w}) (f : F ⟶ G.obj),
      ∃ (G' : Sheaf J TopCommRingCat.{max u v w}) (i : G' ⟶ G), Mono i ∧
        (∀ U : Cᵒᵖ, Cardinal.mk (G'.obj.obj U) ≤ κ) ∧ ∃ f' : F ⟶ G'.obj, f' ≫ i.hom = f
```

**`CategoryTheory.TopologicalSheaf.hasWeakSheafify_topModuleCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L395). The attribute's comment: “sheafification (topological modules)”.

> **Stacks 0AI4** (sheafification), for presheaves of topological modules over a topological
> ring `R`: the inclusion of sheaves into presheaves has a left adjoint.

```lean
noncomputable instance hasWeakSheafify_topModuleCat (R : Type (max u v w)) [Ring R]
    [TopologicalSpace R] : HasWeakSheafify J (TopModuleCat.{max u v w} R)
```

**`CategoryTheory.TopologicalSheaf.hasWeakSheafify_topAddCommGrpCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L401). The attribute's comment: “sheafification (topological abelian groups)”.

> **Stacks 0AI4** (sheafification), for presheaves of topological abelian groups.

```lean
noncomputable instance hasWeakSheafify_topAddCommGrpCat :
    HasWeakSheafify J TopAddCommGrpCat.{max u v w}
```

**`CategoryTheory.TopologicalSheaf.hasWeakSheafify_topCommRingCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 407](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L407). The attribute's comment: “sheafification (topological rings)”.

> **Stacks 0AI4** (sheafification), for presheaves of topological rings.

```lean
noncomputable instance hasWeakSheafify_topCommRingCat :
    HasWeakSheafify J TopCommRingCat.{max u v w}
```

**`CategoryTheory.TopologicalSheaf.isSheaf_skyscraperPresheaf_topModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L425). The attribute's comment: “point\_mapping\_sheaf (topological modules and abelian groups)”.

> **Stacks 0AI4** (the sheaf `U ↦ Map(u(U), M)`), for topological modules over a topological
> ring `R`, topological abelian groups (`R = ℤ`) and, by
> `isSheaf_skyscraperPresheaf_topCommRingCat`, topological rings: for a point of the site given by
> `u : C ⥤ Sets` satisfying conditions (1) and (2) of Stacks 00Y5 and a topological module `M`, the
> presheaf `U ↦ ∏_{x ∈ u(U)} M` (the product in `TopModuleCat R`, i.e. with the product topology) is
> a sheaf.

```lean
theorem isSheaf_skyscraperPresheaf_topModuleCat (R : Type w) [Ring R] [TopologicalSpace R]
    (h₁ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ x : u.obj X,
      ∃ (Y : C) (f : Y ⟶ X) (_ : P f) (y : u.obj Y), u.map f y = x)
    (h₂ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ ⦃Y Z : C⦄ (f : Y ⟶ X), P f →
      ∀ (g : Z ⟶ X) [HasPullback f g], Function.Bijective (pullbackComparison u f g))
    (M : TopModuleCat.{w} R) :
    Presheaf.IsSheaf K.toGrothendieck (ElementColimit.skyscraperPresheaf u M)
```

**`CategoryTheory.TopologicalSheaf.isSheaf_skyscraperPresheaf_topCommRingCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L437). The attribute's comment: “point\_mapping\_sheaf (topological rings)”.

> **Stacks 0AI4** (the sheaf `U ↦ Map(u(U), M)`), for topological rings: the presheaf
> `U ↦ ∏_{x ∈ u(U)} M` (the product in `TopCommRingCat`, with the product topology) is a sheaf.

```lean
theorem isSheaf_skyscraperPresheaf_topCommRingCat
    (h₁ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ x : u.obj X,
      ∃ (Y : C) (f : Y ⟶ X) (_ : P f) (y : u.obj Y), u.map f y = x)
    (h₂ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ ⦃Y Z : C⦄ (f : Y ⟶ X), P f →
      ∀ (g : Z ⟶ X) [HasPullback f g], Function.Bijective (pullbackComparison u f g))
    (M : TopCommRingCat.{w}) :
    Presheaf.IsSheaf K.toGrothendieck (ElementColimit.skyscraperPresheaf u M)
```

**`CategoryTheory.TopologicalSheaf.isIso_elementColimit_map_toSheafify_topModuleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L452). The attribute's comment: “stalk\_preservation (topological modules and abelian groups)”.

> **Stacks 0AI4** (sheafification commutes with stalks), for presheaves of topological modules
> over a topological ring `R` (and so of topological abelian groups, `R = ℤ`): for a point of the
> site given by `u : C ⥤ Sets` satisfying conditions (1) and (2) of Stacks 00Y5, the canonical map
> `F_p ⟶ (F^#)_p` is an isomorphism, the stalk being the colimit in `TopModuleCat R` over the
> category of neighbourhoods.

```lean
theorem isIso_elementColimit_map_toSheafify_topModuleCat (R : Type w) [Ring R]
    [TopologicalSpace R]
    (h₁ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ x : u.obj X,
      ∃ (Y : C) (f : Y ⟶ X) (_ : P f) (y : u.obj Y), u.map f y = x)
    (h₂ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ ⦃Y Z : C⦄ (f : Y ⟶ X), P f →
      ∀ (g : Z ⟶ X) [HasPullback f g], Function.Bijective (pullbackComparison u f g))
    (F : Cᵒᵖ ⥤ TopModuleCat.{w} R) :
    IsIso ((elementColimit u (TopModuleCat.{w} R)).map (toSheafify K.toGrothendieck F))
```

**`CategoryTheory.TopologicalSheaf.isIso_elementColimit_map_toSheafify_topCommRingCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalAlgebraicSheaf.lean#L466). The attribute's comment: “stalk\_preservation (topological rings)”.

> **Stacks 0AI4** (sheafification commutes with stalks), for presheaves of topological rings:
> the canonical map `F_p ⟶ (F^#)_p` is an isomorphism, the stalk being the colimit in
> `TopCommRingCat` over the category of neighbourhoods.

```lean
theorem isIso_elementColimit_map_toSheafify_topCommRingCat
    (h₁ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ x : u.obj X,
      ∃ (Y : C) (f : Y ⟶ X) (_ : P f) (y : u.obj Y), u.map f y = x)
    (h₂ : ∀ ⦃X : C⦄ (P : Presieve X), P ∈ K X → ∀ ⦃Y Z : C⦄ (f : Y ⟶ X), P f →
      ∀ (g : Z ⟶ X) [HasPullback f g], Function.Bijective (pullbackComparison u f g))
    (F : Cᵒᵖ ⥤ TopCommRingCat.{w}) :
    IsIso ((elementColimit u TopCommRingCat.{w}).map (toSheafify K.toGrothendieck F))
```

**`CategoryTheory.TopologicalSheaf.sheafSize`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean#L70). The attribute's comment: “size”.

> The size of a sheaf of topological spaces is the supremum of the cardinalities of its
> values on objects of the site.

```lean
public noncomputable abbrev sheafSize (H : Sheaf J TopCat.{w}) : Cardinal.{max u w}
```

**`CategoryTheory.TopologicalSheaf.exists_bounded_subsheaf_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean#L282). The attribute's comment: “bounded\_subsheaf”.

> Any map from a fixed presheaf of topological spaces to a sheaf factors through a
> subsheaf of uniformly bounded size.

```lean
public theorem exists_bounded_subsheaf_factorization (F : Cᵒᵖ ⥤ TopCat.{w}) :
    ∃ κ : Cardinal.{max u v w}, ∀ (G : Sheaf J TopCat.{w}) (f : F ⟶ G.obj),
      ∃ (G' : Sheaf J TopCat.{w}) (i : G' ⟶ G),
        Mono i ∧ Cardinal.lift.{v} (sheafSize G') ≤ κ ∧
          ∃ f' : F ⟶ G'.obj, f' ≫ i.hom = f
```

**`CategoryTheory.TopologicalSheaf.hasWeakSheafify_topCat`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean#L418). The attribute's comment: “sheafification”.

> The inclusion of topological-space-valued sheaves into presheaves has a left adjoint.

```lean
public noncomputable instance hasWeakSheafify_topCat :
    HasWeakSheafify J TopCat.{max u v w}
```

**`CategoryTheory.TopologicalSheaf.isSheaf_mappingPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheafPoint.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheafPoint.lean#L75). The attribute's comment: “point\_mapping\_sheaf”.

> **Stacks 0AI4** (the sheaf `U ↦ Map(u(U), M)`). Let `p` be a point of the site `C` given by
> a functor `u : C ⥤ Sets` (Stacks 00Y5). For a topological space `M`, the presheaf
> `U ↦ Map(u(U), M) = ∏_{x ∈ u(U)} M`, with the product topology, is a sheaf of topological
> spaces.
>
> The site is the small category `C` with the topology generated by a precoverage `K` that has
> the fibre products of its coverings and is stable under base change, and `h₁`, `h₂` are
> conditions (1) and (2) of Stacks 00Y5 for `u`; condition (3) is not needed. The general form,
> for any category with products, is `CategoryTheory.ElementColimit.isSheaf_skyscraperPresheaf`.

```lean
theorem isSheaf_mappingPresheaf
    (h₁ : ∀ ⦃X : C⦄ (R : Presieve X), R ∈ K X → ∀ x : u.obj X,
      ∃ (Y : C) (f : Y ⟶ X) (_ : R f) (y : u.obj Y), u.map f y = x)
    (h₂ : ∀ ⦃X : C⦄ (R : Presieve X), R ∈ K X → ∀ ⦃Y Z : C⦄ (f : Y ⟶ X), R f →
      ∀ (g : Z ⟶ X) [HasPullback f g], Function.Bijective (pullbackComparison u f g))
    (M : TopCat.{w}) :
    Presheaf.IsSheaf K.toGrothendieck (mappingPresheaf u M)
```

**`CategoryTheory.TopologicalSheaf.isIso_elementColimit_map_toSheafify_topCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheafPoint.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheafPoint.lean#L98). The attribute's comment: “stalk\_preservation”.

> **Stacks 0AI4** (sheafification commutes with taking stalks at a point). Let `p` be a point
> of the site `C` given by a functor `u : C ⥤ Sets` (Stacks 00Y5), and let `F` be a presheaf of
> topological spaces on `C`. Then the canonical map `F_p ⟶ (F^#)_p` is an isomorphism of
> topological spaces, where `F_p = colim_{(U, x) ∈ Nbh(p)ᵒᵖ} F(U)` is the colimit in `TopCat`
> (`CategoryTheory.elementColimit`) and `F^#` is the sheafification of `hasWeakSheafify_topCat`.
>
> The site is the small category `C` with the topology generated by a precoverage `K` that has
> the fibre products of its coverings and is stable under base change, and `h₁`, `h₂` are
> conditions (1) and (2) of Stacks 00Y5 for `u`; condition (3) is not needed. No cofilteredness
> of the category of neighbourhoods is assumed, so this does not go through Mathlib's
> `GrothendieckTopology.Point`. The general form, for any category with products, colimits and
> sheafification, is `CategoryTheory.ElementColimit.isIso_elementColimit_map_toSheafify`.

```lean
theorem isIso_elementColimit_map_toSheafify_topCat
    (h₁ : ∀ ⦃X : C⦄ (R : Presieve X), R ∈ K X → ∀ x : u.obj X,
      ∃ (Y : C) (f : Y ⟶ X) (_ : R f) (y : u.obj Y), u.map f y = x)
    (h₂ : ∀ ⦃X : C⦄ (R : Presieve X), R ∈ K X → ∀ ⦃Y Z : C⦄ (f : Y ⟶ X), R f →
      ∀ (g : Z ⟶ X) [HasPullback f g], Function.Bijective (pullbackComparison u f g))
    (F : Cᵒᵖ ⥤ TopCat.{w}) :
    IsIso ((elementColimit u TopCat.{w}).map (toSheafify K.toGrothendieck F))
```

Declarations registered for the tag:

- [`CategoryTheory.Sheaf.hasLimitsOfSize`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.hasLimitsOfSize#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean#L77) (StacksFrontier): “limits”. References: EGA 0 (3.2.6), “partial”; SGA 3 IV (4.4.1), “(i)”; SGA 4 I (8.12.9), “partial”; SGA 4 II (4.1), “more general”; SGA 4 II (4.8), “more general”.
- [`CategoryTheory.Sheaf.createsLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.createsLimits#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/TopologicalSheaf.lean#L83) (StacksFrontier): “limits”. References: EGA 0 (3.2.6), “more general”; SGA 3 IV (4.4.1), “more general”; SGA 4 II (4.1), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.2, Tag 0AHY](https://stacks.math.columbia.edu/tag/0AHY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
