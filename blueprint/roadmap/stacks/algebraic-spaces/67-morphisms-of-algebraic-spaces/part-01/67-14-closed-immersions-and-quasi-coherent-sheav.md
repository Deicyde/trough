---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.kerIdealSmulQuotientUnitIso, AlgebraicGeometry.Space.cokernel_π_comp_kerIdealSmulQuotientUnitIso_hom, AlgebraicGeometry.Space.isIso_modulePullbackAdjunction_counit, AlgebraicGeometry.Space.modulePullbackCounitIso, AlgebraicGeometry.Space.annihilatedByKerIdeal_modulePushforward, AlgebraicGeometry.Space.annihilatedByKerIdeal_of_essImage_modulePushforward, AlgebraicGeometry.Space.fullyFaithfulQuasicoherentModulePushforward, AlgebraicGeometry.Space.quasicoherentDirectImageEquivalence
statement: formalized
proof: formalized
---

# 67.14 Closed immersions and quasi-coherent sheaves

Section 67.14 of the Stacks Project, [Tag 04CI](https://stacks.math.columbia.edu/tag/04CI). 6 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04CJ, a lemma

[Tag 04CJ](https://stacks.math.columbia.edu/tag/04CJ) in the Stacks Project.

**`AlgebraicGeometry.Space.kerIdealSmulQuotientUnitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionIdealQuotient.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionIdealQuotient.lean#L253). The attribute's comment: “part (1): the unit identifies the quotient by the defining ideal with the direct image of the inverse image”.

> **Stacks 04CJ, part (1).**  Let `i : Z ⟶ X` be a closed immersion of algebraic spaces over
> `S` and let `𝓘 = ker(i♯) ⊆ 𝒪_X` be the ideal cutting out `Z`.  For every `𝒪_X`-module `𝓕` the
> unit `𝓕 ⟶ i_*i^*𝓕` of the adjunction of Stacks 03LU induces an isomorphism `𝓕/𝓘𝓕 ≅ i_*i^*𝓕`.
>
> The isomorphism is the one the adjunction gives: `cokernel.π ≫ e.hom` is the unit, by
> `AlgebraicGeometry.Space.cokernel_π_comp_kerIdealSmulQuotientUnitMap`.

```lean
def kerIdealSmulQuotientUnitIso (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) :
    kerIdealSmulQuotient B S hS i F ≅
      (modulePushforward B S hS i).obj ((modulePullback B S hS i).obj F)
```

**`AlgebraicGeometry.Space.cokernel_π_comp_kerIdealSmulQuotientUnitIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionIdealQuotient.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionIdealQuotient.lean#L264). The attribute's comment: “part (1): the isomorphism is the one induced by the unit of the adjunction”.

> **Stacks 04CJ, part (1)**, the normalisation of the isomorphism: it is induced by the unit of
> the adjunction of Stacks 03LU, that is, composing the projection `𝓕 ⟶ 𝓕/𝓘𝓕` with it gives the
> unit.

```lean
theorem cokernel_π_comp_kerIdealSmulQuotientUnitIso_hom (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) (F : Modules.{u, u} B S hS X.1 X.2) :
    cokernel.π (kerIdealSmul B S hS i F).ι ≫
        (kerIdealSmulQuotientUnitIso B S hS i hi F).hom =
      (modulePullbackAdjunction B S hS i).unit.app F
```

**`AlgebraicGeometry.Space.isIso_modulePullbackAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L206). The attribute's comment: “part (2): inverse image is a left inverse of direct image”.

> **Stacks 04CJ, part (2)** for the modules of `AlgebraicGeometry.Space.Modules`: for a closed
> immersion `f : X ⟶ Y` of algebraic spaces and any sheaf of `𝒪_X`-modules `G`, the adjunction map
> `f^*f_*G ⟶ G` is an isomorphism.
>
> This is full faithfulness of the direct image read through the adjunction of Stacks 03LU: the
> counit of an adjunction is an isomorphism exactly when its right adjoint is fully faithful.

```lean
theorem isIso_modulePullbackAdjunction_counit (f : X ⟶ Y) (hf : IsClosedImmersion B S hS f.hom)
    (G : Modules.{u, u} B S hS X.1 X.2) :
    IsIso ((modulePullbackAdjunction B S hS f).counit.app G)
```

**`AlgebraicGeometry.Space.modulePullbackCounitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L218). The attribute's comment: “part (2): inverse image is a left inverse of direct image”.

> **Stacks 04CJ, part (2)**, functorially: inverse image along a closed immersion of algebraic
> spaces is a left inverse of direct image, the counit of the adjunction of Stacks 03LU being a
> natural isomorphism `f_* ⋙ f^* ≅ 𝟭`. This is the functorial form of
> `AlgebraicGeometry.Space.isIso_modulePullbackAdjunction_counit`.

```lean
def modulePullbackCounitIso (f : X ⟶ Y) (hf : IsClosedImmersion B S hS f.hom) :
    modulePushforward B S hS f ⋙ modulePullback B S hS f ≅
      𝟭 (Modules.{u, u} B S hS X.1 X.2)
```

**`AlgebraicGeometry.Space.annihilatedByKerIdeal_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L269). The attribute's comment: “part (3): the essential image is annihilated by the defining ideal”.

> **Stacks 04CJ, part (3)**, half of the essential-image assertion: the ideal cutting out the
> closed subspace annihilates every direct image `f_*G`.
>
> Restriction of scalars along `f♯` makes a section `a` of `𝒪_Y` act on `f_*G` as `f♯(a)`, so a
> section killed by `f♯` acts as zero. Neither the closed-immersion hypothesis on `f` nor
> surjectivity of `f♯` is used.
>
> This is also one inclusion of the essential-image clause of Stacks 08KS for algebraic spaces; the
> containment form of it is
> `AlgebraicGeometry.Space.essImage_modulePushforward_le_annihilatedByKerIdeal` of
> `StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforwardExactness.lean`, which
> carries no tag of its own, and the reverse inclusion is
> `AlgebraicGeometry.Space.essImage_modulePushforward_of_annihilatedByKerIdeal`, proved with no
> hypothesis beyond the closed immersion.

```lean
theorem annihilatedByKerIdeal_modulePushforward (f : X ⟶ Y)
    (G : Modules.{u, u} B S hS X.1 X.2) :
    AnnihilatedByKerIdeal B S hS f ((modulePushforward B S hS f).obj G)
```

**`AlgebraicGeometry.Space.annihilatedByKerIdeal_of_essImage_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L285). The attribute's comment: “part (3): the essential image is annihilated by the defining ideal”.

> **Stacks 04CJ, part (3)**, half of the essential-image assertion, in essential-image form:
> every `𝒪_Y`-module isomorphic to a direct image along `f` is annihilated by the ideal cutting out
> the closed subspace. This is
> `AlgebraicGeometry.Space.annihilatedByKerIdeal_modulePushforward` transported along an
> isomorphism, and is the inclusion `essImage f_* ⊆ {𝓕 | 𝓘𝓕 = 0}` of the essential-image clause of
> Stacks 08KS for algebraic spaces, whose tag is carried by
> `AlgebraicGeometry.Space.essImage_modulePushforward_le_annihilatedByKerIdeal` of
> `StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforwardExactness.lean`.

```lean
theorem annihilatedByKerIdeal_of_essImage_modulePushforward (f : X ⟶ Y)
    {G : Modules.{u, u} B S hS Y.1 Y.2} (hG : (modulePushforward B S hS f).essImage G) :
    AnnihilatedByKerIdeal B S hS f G
```

**`AlgebraicGeometry.Space.fullyFaithfulQuasicoherentModulePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionModulePushforward.lean#L321). The attribute's comment: “part (3): the direct image is fully faithful on quasi-coherent modules”.

> **Stacks 04CJ, part (3)**, the full-faithfulness assertion: direct image along a closed
> immersion of algebraic spaces is fully faithful on quasi-coherent modules.
>
> It is fully faithful on *all* modules by
> `AlgebraicGeometry.Space.fullyFaithfulModulePushforward`, and a full subcategory inclusion is
> fully faithful.

```lean
def fullyFaithfulQuasicoherentModulePushforward (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) :
    (quasicoherentModulePushforward B S hS f).FullyFaithful
```

**`AlgebraicGeometry.Space.quasicoherentDirectImageEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean#L97). The attribute's comment: “part (3): quasi-coherence of the direct image, and quasi-coherence of the module whose direct image an annihilated quasi-coherent module is”.

> **Part (3) of Stacks 04CJ in the form Stacks 04CL consumes.**  For a closed immersion
> `i : Z ⟶ X` of algebraic spaces the direct image carries quasi-coherent `𝒪_Z`-modules to
> quasi-coherent `𝒪_X`-modules, and every quasi-coherent `𝒪_X`-module annihilated by `𝓘 = ker(i♯)`
> is the direct image of a quasi-coherent `𝒪_Z`-module.
>
> The first clause is the closed-immersion case of Stacks 03M9,
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_modulePushforward_of_isClosedImmersion`.  For the
> second, an annihilated `𝒪_X`-module is a direct image by the unconditional essential-image clause
> `AlgebraicGeometry.Space.essImage_modulePushforward_iff`, so the unit `𝓕 ⟶ i_*i^*𝓕` is an
> isomorphism, and the witness `i^*𝓕` is quasi-coherent by the closed-immersion case of
> Stacks 03GA.

```lean
theorem quasicoherentDirectImageEquivalence (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    QuasicoherentDirectImageEquivalence B S hS i
```

**`AlgebraicGeometry.Space.quasicoherentDirectImageOfClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean#L118). The attribute's comment: “part (3): the induced functor on quasi-coherent modules”.

> **The functor `i_* : QCoh(𝒪_Z) ⥤ QCoh(𝒪_X)` of Stacks 04CJ, part (3)**, for a closed
> immersion `i : Z ⟶ X` of algebraic spaces.
>
> This is `AlgebraicGeometry.Space.quasicoherentPushforwardOfEquivalence` with its hypothesis
> discharged by `AlgebraicGeometry.Space.quasicoherentDirectImageEquivalence`; composing it with
> the inclusion of the quasi-coherent modules gives back the direct image of all modules, so it is
> the functor the source names and not another one of the same type.

```lean
def quasicoherentDirectImageOfClosedImmersion (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom) :
    QuasicoherentSheaves.{u, u} B S hS Z.1 Z.2 ⥤ QuasicoherentSheaves.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.fullyFaithfulQuasicoherentDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean#L138). The attribute's comment: “part (3): the direct image on quasi-coherent modules is fully faithful”.

> **Stacks 04CJ, part (3), the full-faithfulness clause.**  The direct image
> `i_* : QCoh(𝒪_Z) ⥤ QCoh(𝒪_X)` along a closed immersion of algebraic spaces is fully faithful.
>
> The direct image is fully faithful on all modules by
> `AlgebraicGeometry.Space.fullyFaithfulModulePushforward` (part (2)), and a lift along a full
> subcategory inclusion inherits that.

```lean
def fullyFaithfulQuasicoherentDirectImage (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom) :
    (quasicoherentDirectImageOfClosedImmersion B S hS i hi).FullyFaithful
```

**`AlgebraicGeometry.Space.exactFunctor_quasicoherentDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean#L171). The attribute's comment: “part (3): the direct image on quasi-coherent modules is exact”.

> **Stacks 04CJ, part (3), the exactness clause.**  The direct image
> `i_* : QCoh(𝒪_Z) ⥤ QCoh(𝒪_X)` along a closed immersion of algebraic spaces is an exact
> functor.

```lean
theorem exactFunctor_quasicoherentDirectImage (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    exactFunctor (QuasicoherentSheaves.{u, u} B S hS Z.1 Z.2)
      (QuasicoherentSheaves.{u, u} B S hS X.1 X.2)
      (quasicoherentDirectImageOfClosedImmersion B S hS i hi)
```

**`AlgebraicGeometry.Space.essImage_quasicoherentDirectImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentEquivalence.lean#L189). The attribute's comment: “part (3): the essential image is the quasi-coherent modules annihilated by the defining ideal”.

> **Stacks 04CJ, part (3), the essential-image clause.**  A quasi-coherent `𝒪_X`-module is the
> direct image of a quasi-coherent `𝒪_Z`-module along the closed immersion `i` exactly when the
> ideal `𝓘 = ker(i♯)` cutting out `Z` annihilates it.
>
> The forward implication is
> `AlgebraicGeometry.Space.annihilatedByKerIdeal_of_essImage_modulePushforward`, applied to the
> underlying `𝒪_X`-module.  The converse is the second clause of
> `AlgebraicGeometry.Space.quasicoherentDirectImageEquivalence`.

```lean
theorem essImage_quasicoherentDirectImage_iff (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom)
    (F : QuasicoherentSheaves.{u, u} B S hS X.1 X.2) :
    (quasicoherentDirectImageOfClosedImmersion B S hS i hi).essImage F ↔
      AnnihilatedByKerIdeal B S hS i F.obj
```

## Tag 04CK, a lemma

[Tag 04CK](https://stacks.math.columbia.edu/tag/04CK) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_largestQuasicoherentSubobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleKernelQuasicoherent.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleKernelQuasicoherent.lean#L363).

> **Stacks 04CK.**  Let `S` be a scheme, let `X` be an algebraic space over `S`, let `𝓕` be a
> quasi-coherent `𝒪_X`-module and let `𝒢 ⊆ 𝓕` be an `𝒪_X`-submodule.  There is a unique
> quasi-coherent `𝒪_X`-submodule `𝒢' ⊆ 𝒢` for which composition with the inclusion `𝒢' ⊆ 𝒢` is a
> bijection `Hom(𝓗, 𝒢') ⟶ Hom(𝓗, 𝒢)` for every quasi-coherent `𝒪_X`-module `𝓗`.
>
> This is `AlgebraicGeometry.Space.existsUnique_quasicoherentSubobject_of_isClosedUnderKernels`
> with its kernel hypothesis discharged by
> `AlgebraicGeometry.Space.isClosedUnderKernels`.

```lean
theorem existsUnique_largestQuasicoherentSubobject (M : Modules.{u, m} B S hS F hF)
    [M.IsQuasicoherentOnSite] (G : Subobject M) :
    ∃! G' : { G' : Subobject (G : Modules.{u, m} B S hS F hF) //
        (G' : Modules.{u, m} B S hS F hF).IsQuasicoherentOnSite },
      ∀ (H : Modules.{u, m} B S hS F hF) [H.IsQuasicoherentOnSite],
        Function.Bijective
          (fun f : H ⟶ (G'.1 : Modules.{u, m} B S hS F hF) ↦ f ≫ G'.1.arrow)
```

**`AlgebraicGeometry.Space.exists_greatest_quasicoherentSubobject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleKernelQuasicoherent.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleKernelQuasicoherent.lean#L381).

> **Stacks 04CK, the maximality clause.**  The quasi-coherent submodule of
> `AlgebraicGeometry.Space.existsUnique_largestQuasicoherentSubobject` is the largest
> quasi-coherent submodule of `𝓕` contained in `𝒢`.
>
> This is `AlgebraicGeometry.Space.exists_greatest_quasicoherentSubobject_of_isClosedUnderKernels`
> with its kernel hypothesis discharged by
> `AlgebraicGeometry.Space.isClosedUnderKernels`.

```lean
theorem exists_greatest_quasicoherentSubobject (M : Modules.{u, m} B S hS F hF)
    [M.IsQuasicoherentOnSite] (G : Subobject M) :
    ∃ G' : Subobject (G : Modules.{u, m} B S hS F hF),
      (G' : Modules.{u, m} B S hS F hF).IsQuasicoherentOnSite ∧
        ∀ K : Subobject (G : Modules.{u, m} B S hS F hF),
          (K : Modules.{u, m} B S hS F hF).IsQuasicoherentOnSite → K ≤ G'
```

## Tag 04CL, a lemma

[Tag 04CL](https://stacks.math.columbia.edu/tag/04CL) in the Stacks Project.

**`AlgebraicGeometry.Space.isLeftAdjoint_quasicoherentDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentUpperShriek.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentUpperShriek.lean#L56).

> **Stacks 04CL.**  Let `S` be a scheme and let `i : Z ⟶ X` be a closed immersion of algebraic
> spaces over `S`.  Then the direct image `i_* : QCoh(𝒪_Z) ⥤ QCoh(𝒪_X)` has a right adjoint, the
> functor `i^!` of the source.

```lean
theorem isLeftAdjoint_quasicoherentDirectImage (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    (quasicoherentDirectImageOfClosedImmersion B S hS i hi).IsLeftAdjoint
```

**`AlgebraicGeometry.Space.quasicoherentRightAdjointOfClosedImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentUpperShriek.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentUpperShriek.lean#L67). The attribute's comment: “the functor `i^!`”.

> **Stacks 04CL**, the functor `i^!`: the right adjoint of the direct image
> `i_* : QCoh(𝒪_Z) ⥤ QCoh(𝒪_X)` along a closed immersion `i : Z ⟶ X` of algebraic spaces. For a
> quasi-coherent `𝒪_X`-module `𝓖`, the direct image of `i^! 𝓖` is the largest quasi-coherent
> submodule of `𝓖` annihilated by the ideal cutting out `Z`.

```lean
def quasicoherentRightAdjointOfClosedImmersion (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    QuasicoherentSheaves.{u, u} B S hS X.1 X.2 ⥤ QuasicoherentSheaves.{u, u} B S hS Z.1 Z.2
```

**`AlgebraicGeometry.Space.quasicoherentDirectImageAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentUpperShriek.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionQuasicoherentUpperShriek.lean#L76). The attribute's comment: “the adjunction `i_* ⊣ i^!`”.

> **Stacks 04CL**, the adjunction `i_* ⊣ i^!` exhibiting
> `AlgebraicGeometry.Space.quasicoherentRightAdjointOfClosedImmersion` as a right adjoint of the
> direct image of quasi-coherent modules along a closed immersion of algebraic spaces.

```lean
def quasicoherentDirectImageAdjunction (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom) :
    quasicoherentDirectImageOfClosedImmersion B S hS i hi ⊣
      quasicoherentRightAdjointOfClosedImmersion B S hS i hi
```

## Tag 0CYZ, a definition

[Tag 0CYZ](https://stacks.math.columbia.edu/tag/0CYZ) in the Stacks Project.

**`AlgebraicGeometry.Space.definingIdealSheaf_schemeTheoreticUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedSubspaceIdealLattice.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedSubspaceIdealLattice.lean#L279). The attribute's comment: “the defining ideal of the scheme-theoretic union is the meet of the two defining ideals”.

> **Stacks 0CYZ.** The defining ideal sheaf of the scheme-theoretic union of two closed
> subspaces is the meet of their defining ideal sheaves.
>
> One containment is inclusion-reversal.  For the other, the meet of the two ideal sheaves is
> quasi-coherent, hence by Stacks 03MB cuts out a closed subspace `W`; that `W` contains both `Y`
> and `Z` because its ideal is contained in each of theirs, so the scheme-theoretic union, being
> the smallest closed subspace containing both, is contained in `W`, and inclusion-reversal gives
> the containment of ideals back.

```lean
theorem definingIdealSheaf_schemeTheoreticUnion :
    definingIdealSheaf B S hS X (schemeTheoreticUnion B S hS X.1 X.2 Y Z) =
      definingIdealSheaf B S hS X Y ⊓ definingIdealSheaf B S hS X Z
```

**`AlgebraicGeometry.Space.definingIdealSheaf_schemeTheoreticIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedSubspaceIdealLattice.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedSubspaceIdealLattice.lean#L307). The attribute's comment: “the defining ideal of the scheme-theoretic intersection is the sum of the two defining ideals”.

> **Stacks 0CYZ.** The defining ideal sheaf of the scheme-theoretic intersection of two closed
> subspaces is the sum of their defining ideal sheaves.
>
> One containment is inclusion-reversal.  For the other, the sum of the two ideal sheaves is
> quasi-coherent, hence by Stacks 03MB cuts out a closed subspace `W`; that `W` is contained in
> both `Y` and `Z` because its ideal contains each of theirs, hence in their intersection, and
> inclusion-reversal gives the containment of ideals back.

```lean
theorem definingIdealSheaf_schemeTheoreticIntersection :
    definingIdealSheaf B S hS X (schemeTheoreticIntersection B S hS X.1 X.2 Y Z) =
      definingIdealSheaf B S hS X Y ⊔ definingIdealSheaf B S hS X Z
```

**`AlgebraicGeometry.Space.schemeTheoreticIntersection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean#L261). The attribute's comment: “scheme-theoretic intersection”.

> **Stacks 0CYZ.** The closed subspace cut out by the sum of the defining quasi-coherent
> ideal sheaves.

```lean
def schemeTheoreticIntersection (hF : IsAlgebraicSpace B S hS F)
    (Z Y : ClosedSubspaces B S hS F) :
    ClosedSubspaces B S hS F
```

**`AlgebraicGeometry.Space.schemeTheoreticUnion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean#L280). The attribute's comment: “scheme-theoretic union”.

> **Stacks 0CYZ.** The closed subspace cut out by the intersection of the defining
> quasi-coherent ideal sheaves.

```lean
def schemeTheoreticUnion (hF : IsAlgebraicSpace B S hS F)
    (Z Y : ClosedSubspaces B S hS F) :
    ClosedSubspaces B S hS F
```

## Tag 0CZ0, a lemma

[Tag 0CZ0](https://stacks.math.columbia.edu/tag/0CZ0) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_schemeTheoreticIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L182). The attribute's comment: “the intersection square is cartesian”.

> The scheme-theoretic intersection of two closed subspaces of an algebraic
> space over `S` is the fibre product of the two over the ambient space: the square formed by the
> four inclusions is Cartesian in the category of presheaves on the big fppf site of `S`.

```lean
theorem isPullback_schemeTheoreticIntersection (hF : IsAlgebraicSpace B S hS F)
    (Z Y : ClosedSubspaces B S hS F) :
    IsPullback
      (Subfunctor.homOfLe (show (schemeTheoreticIntersection B S hS F hF Z Y).1 ≤ Z.1 from
        inf_le_left))
      (Subfunctor.homOfLe (show (schemeTheoreticIntersection B S hS F hF Z Y).1 ≤ Y.1 from
        inf_le_right))
      Z.1.ι Y.1.ι
```

**`AlgebraicGeometry.Space.isClosedImmersion_schemeTheoreticIntersection_le_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L195). The attribute's comment: “closed immersion into the first factor”.

> The scheme-theoretic intersection of two closed subspaces of an algebraic
> space over `S` is a closed subspace of the first of them.

```lean
theorem isClosedImmersion_schemeTheoreticIntersection_le_left
    (hF : IsAlgebraicSpace B S hS F) (Z Y : ClosedSubspaces B S hS F) :
    IsClosedImmersion B S hS
      (Subfunctor.homOfLe (show (schemeTheoreticIntersection B S hS F hF Z Y).1 ≤ Z.1 from
        inf_le_left))
```

**`AlgebraicGeometry.Space.isClosedImmersion_schemeTheoreticIntersection_le_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L205). The attribute's comment: “closed immersion into the second factor”.

> The scheme-theoretic intersection of two closed subspaces of an algebraic
> space over `S` is a closed subspace of the second of them.

```lean
theorem isClosedImmersion_schemeTheoreticIntersection_le_right
    (hF : IsAlgebraicSpace B S hS F) (Z Y : ClosedSubspaces B S hS F) :
    IsClosedImmersion B S hS
      (Subfunctor.homOfLe (show (schemeTheoreticIntersection B S hS F hF Z Y).1 ≤ Y.1 from
        inf_le_right))
```

## Tag 0CZ1, a lemma

[Tag 0CZ1](https://stacks.math.columbia.edu/tag/0CZ1) in the Stacks Project.

**`AlgebraicGeometry.Space.unionIntersectionShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedUnionIntersectionSequence.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedUnionIntersectionSequence.lean#L423). The attribute's comment: “the short exact sequence of the structure sheaves of the union, the two subspaces and the intersection”.

> **Stacks 0CZ1, second assertion.**  For two closed subspaces `Y, Z` of an algebraic space
> `X` over `S`, with `Y ∪ Z` and `Y ∩ Z` their scheme-theoretic union and intersection,
>
> `0 ⟶ 𝒪_{Y ∪ Z} ⟶ 𝒪_Y × 𝒪_Z ⟶ 𝒪_{Y ∩ Z} ⟶ 0`
>
> is a short exact sequence of `𝒪_X`-modules, the four structure sheaves being taken as modules
> on `X` under Stacks 04CJ, the first map built from the two canonical maps `𝒪_{Y ∪ Z} ⟶ 𝒪_Y` and
> `𝒪_{Y ∪ Z} ⟶ 𝒪_Z` and the second from the canonical map `𝒪_Y ⟶ 𝒪_{Y ∩ Z}` and the negative of
> the canonical map `𝒪_Z ⟶ 𝒪_{Y ∩ Z}`.
>
> This is `AlgebraicGeometry.Space.shortExact_biprod_of_ker_eq_inf_sup` applied to the four
> structure projections of `𝒪_X`, which are epimorphisms by
> `AlgebraicGeometry.Space.epi_structureProjection` and whose kernels are the four defining
> ideals; the two identifications of Stacks 0CYZ say that the kernels for the union and the
> intersection are the meet and the join of the kernels for `Y` and `Z`.

```lean
theorem unionIntersectionShortComplex_shortExact :
    (unionIntersectionShortComplex B S hS X Y Z).ShortExact
```

**`AlgebraicGeometry.Space.isPushout_schemeTheoreticUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedUnionPushout.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedUnionPushout.lean#L610). The attribute's comment: “the square of the two subspaces, their scheme-theoretic intersection and their scheme-theoretic union is cocartesian in the category of algebraic spaces over the base”.

> **[Stacks, Tag 0CZ1], third assertion.** Let `X` be an algebraic space over a scheme `S` and
> let `Y, Z ⊆ X` be closed subspaces, with `Y ∪ Z` and `Y ∩ Z` the scheme-theoretic union and
> intersection of [Stacks Project, Tag 0CYZ].  Then the square
>
> ```
> Y ∩ Z ⟶ Y
>   ↓        ↓
>   Z   ⟶ Y ∪ Z
> ```
>
> of the four closed subspaces and the four inclusions is cocartesian in the category of algebraic
> spaces over `S`, that is, `Y ∪ Z = Y ⨿_{Y ∩ Z} Z`.
>
> This is `AlgebraicGeometry.Space.existsUnique_desc_schemeTheoreticUnion` packaged as a colimit;
> the square commutes because both composites are the inclusion of `Y ∩ Z` into `Y ∪ Z`.

```lean
theorem isPushout_schemeTheoreticUnion (X : AlgebraicSpaces B S hS)
    (Y Z : ClosedSubspaces B S hS X.1) :
    IsPushout
      (ObjectProperty.homMk (Subfunctor.homOfLe (inf_le_left : Y.1 ⊓ Z.1 ≤ Y.1)) :
        closedSubspaceToSpace B S hS X (schemeTheoreticIntersection B S hS X.1 X.2 Y Z) ⟶
          closedSubspaceToSpace B S hS X Y)
      (ObjectProperty.homMk (Subfunctor.homOfLe (inf_le_right : Y.1 ⊓ Z.1 ≤ Z.1)) :
        closedSubspaceToSpace B S hS X (schemeTheoreticIntersection B S hS X.1 X.2 Y Z) ⟶
          closedSubspaceToSpace B S hS X Z)
      (ObjectProperty.homMk
          (Subfunctor.homOfLe (le_schemeTheoreticUnion_left B S hS X.2 Y Z)) :
        closedSubspaceToSpace B S hS X Y ⟶
          closedSubspaceToSpace B S hS X (schemeTheoreticUnion B S hS X.1 X.2 Y Z))
      (ObjectProperty.homMk
          (Subfunctor.homOfLe (le_schemeTheoreticUnion_right B S hS X.2 Y Z)) :
        closedSubspaceToSpace B S hS X Z ⟶
          closedSubspaceToSpace B S hS X (schemeTheoreticUnion B S hS X.1 X.2 Y Z))
```

**`AlgebraicGeometry.Space.isClosedImmersion_le_schemeTheoreticUnion_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L229). The attribute's comment: “closed immersion of the first subspace into the union”.

> The first of two closed subspaces of an algebraic space over `S` is a
> closed subspace of their scheme-theoretic union.

```lean
theorem isClosedImmersion_le_schemeTheoreticUnion_left (hF : IsAlgebraicSpace B S hS F)
    (Y Z : ClosedSubspaces B S hS F) :
    IsClosedImmersion B S hS
      (Subfunctor.homOfLe (le_schemeTheoreticUnion_left B S hS hF Y Z))
```

**`AlgebraicGeometry.Space.isClosedImmersion_le_schemeTheoreticUnion_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersions.lean#L238). The attribute's comment: “closed immersion of the second subspace into the union”.

> The second of two closed subspaces of an algebraic space over `S` is a
> closed subspace of their scheme-theoretic union.

```lean
theorem isClosedImmersion_le_schemeTheoreticUnion_right (hF : IsAlgebraicSpace B S hS F)
    (Y Z : ClosedSubspaces B S hS F) :
    IsClosedImmersion B S hS
      (Subfunctor.homOfLe (le_schemeTheoreticUnion_right B S hS hF Y Z))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.14, Tag 04CI](https://stacks.math.columbia.edu/tag/04CI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
