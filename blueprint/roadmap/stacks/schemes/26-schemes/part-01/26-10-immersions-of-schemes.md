---
declaration: section
origin: cited
lean: Stacks.ClosedImmersion.exists_ideal_iso_quotient_of_isAffineOpen, Stacks.ClosedImmersion.exists_scheme_of_isClosedImmersion, Stacks.ClosedImmersion.exists_scheme_of_closedSubspace, Stacks.ClosedImmersion.exists_ideal_idealSheaf_restrict_iso_tilde_of_locallyRingedSpace, Stacks.ClosedImmersion.isQuasicoherent_idealSheaf, Stacks.ClosedImmersion.isQuasicoherent_iff_localGenerators, AlgebraicGeometry.IsOpenImmersion, AlgebraicGeometry.Scheme.Opens
statement: formalized
proof: formalized
---

# 26.10 Immersions of schemes

Section 26.10 of the Stacks Project, [Tag 01IM](https://stacks.math.columbia.edu/tag/01IM). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01IN, a lemma

[Tag 01IN](https://stacks.math.columbia.edu/tag/01IN) in the Stacks Project.

**`Stacks.ClosedImmersion.exists_ideal_iso_quotient_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/ClosedSubspaceScheme.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/ClosedSubspaceScheme.lean#L114). The attribute's comment: “affine\_local\_quotient”.

> Over an affine open `U` of a scheme `X`, a closed immersion of locally ringed spaces
> `i : Z ⟶ X` is, compatibly with the canonical presentation of `U` as `Spec Γ(X, U)`, the spectrum
> of a quotient of `Γ(X, U)`.

```lean
theorem exists_ideal_iso_quotient_of_isAffineOpen (X : Scheme.{u}) (Z : LocallyRingedSpace.{u})
    (i : Z ⟶ X.toLocallyRingedSpace) [hi : IsClosedImmersion i.toShHom]
    (U : X.Opens) (hU : IsAffineOpen U) :
    ∃ (I : Ideal Γ(X, U)) (e : pullback i U.ι.toLRSHom ≅
        (Spec (CommRingCat.of (Γ(X, U) ⧸ I))).toLocallyRingedSpace),
      pullback.snd i U.ι.toLRSHom ≫ hU.isoSpec.hom.toLRSHom =
        e.hom ≫ (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))).toLRSHom
```

**`Stacks.ClosedImmersion.exists_scheme_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/ClosedSubspaceScheme.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/ClosedSubspaceScheme.lean#L134). The attribute's comment: “source\_is\_scheme”.

> The source of a closed immersion of locally ringed spaces into a scheme carries a scheme
> structure.

```lean
theorem exists_scheme_of_isClosedImmersion (X : Scheme.{u}) (Z : LocallyRingedSpace.{u})
    (i : Z ⟶ X.toLocallyRingedSpace) [IsClosedImmersion i.toShHom] :
    ∃ Z' : Scheme.{u}, Z'.toLocallyRingedSpace = Z
```

**`Stacks.ClosedImmersion.exists_scheme_of_closedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/ClosedSubspaceScheme.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/ClosedSubspaceScheme.lean#L195). The attribute's comment: “closed\_subspace\_is\_scheme”.

> The closed subspace of a scheme cut out by a locally generated ideal sheaf carries a scheme
> structure on its underlying locally ringed space.

```lean
theorem exists_scheme_of_closedSubspace (X : Scheme.{u})
    (J : SheafOfModules.{u} (structureSheafRing X.toLocallyRingedSpace.toRingedSpace))
    (j : J ⟶ SheafOfModules.unit (structureSheafRing X.toLocallyRingedSpace.toRingedSpace))
    [Mono j] (hJ : Nonempty (SheafOfModules.LocalGeneratorsData.{u} J)) :
    ∃ Z : Scheme.{u}, Z.toLocallyRingedSpace =
      (closedSubspace X.toLocallyRingedSpace J j hJ).space
```

**`Stacks.ClosedImmersion.exists_ideal_idealSheaf_restrict_iso_tilde_of_locallyRingedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/IdealSheafAffineOpen.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/IdealSheafAffineOpen.lean#L264). The attribute's comment: “kernel\_on\_affine\_open”.

> The affine-local description of the ideal sheaf for a closed immersion of locally ringed
> spaces `i : Z ⟶ X` into a scheme: over an affine open `U = Spec R` of `X` there is an ideal
> `I ⊆ R = Γ(X, U)` presenting the fibre over `U` as `Spec (R ⧸ I)`, and the kernel `ℐ` of
> `𝒪_X ⟶ i_* 𝒪_Z` restricts on `U` to `I^~`.
>
> The source `Z` is a scheme by `Stacks.ClosedImmersion.sourceScheme`, so `i` is a morphism of
> schemes `Stacks.ClosedImmersion.sourceSchemeHom` with the same ideal sheaf, and this is
> `Stacks.ClosedImmersion.exists_ideal_idealSheaf_restrict_iso_tilde` for that morphism.

```lean
theorem exists_ideal_idealSheaf_restrict_iso_tilde_of_locallyRingedSpace (X : Scheme.{u})
    (Z : LocallyRingedSpace.{u}) (i : Z ⟶ X.toLocallyRingedSpace)
    [hi : IsClosedImmersion i.toShHom] (U : X.Opens) (hU : IsAffineOpen U) :
    ∃ (I : Ideal Γ(X, U)) (e : pullback (sourceSchemeHom X Z i) U.ι ≅
        Spec (CommRingCat.of (Γ(X, U) ⧸ I))),
      pullback.snd (sourceSchemeHom X Z i) U.ι ≫ hU.isoSpec.hom =
          e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)) ∧
        ∃ φ : (Scheme.Modules.restrictFunctor U.ι).obj (idealSheaf i.toShHom) ≅
            (modulePullback hU.isoSpec.hom.toLRSHom.toShHom).obj
              (tilde (ModuleCat.of Γ(X, U) I)),
          φ.hom ≫ (modulePullback hU.isoSpec.hom.toLRSHom.toShHom).map
                (tildeIdealι Γ(X, U) I) ≫
              (Stacks.IdealSheafRestrict.pullbackUnitIso hU.isoSpec.hom).hom =
            (Scheme.Modules.restrictFunctor U.ι).map
                (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
                  (structureSheafHom i.toShHom))) ≫
              (Scheme.Modules.restrictUnitIso U.ι).hom
```

**`Stacks.ClosedImmersion.isQuasicoherent_idealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/IdealSheafQuasicoherent.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/IdealSheafQuasicoherent.lean#L53). The attribute's comment: “kernel\_quasi\_coherent”.

> **Stacks Project, Tag 01IN.** The kernel of `𝒪_X ⟶ i_* 𝒪_Z` for a closed immersion of
> locally ringed spaces `i : Z ⟶ X` into a scheme is a quasi-coherent sheaf of ideals.

```lean
theorem isQuasicoherent_idealSheaf (X : Scheme.{u}) (Z : LocallyRingedSpace.{u})
    (i : Z ⟶ X.toLocallyRingedSpace) [hi : IsClosedImmersion i.toShHom] :
    (idealSheaf i.toShHom).IsQuasicoherent
```

**`Stacks.ClosedImmersion.isQuasicoherent_iff_localGenerators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/IdealSheafQuasicoherent.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/IdealSheafQuasicoherent.lean#L66). The attribute's comment: “ideal\_quasi\_coherent\_iff\_locally\_generated”.

> **Stacks Project, Tag 01IN.** A sheaf of ideals on a scheme is locally generated by sections
> if and only if it is quasi-coherent.

```lean
theorem isQuasicoherent_iff_localGenerators (X : Scheme.{u})
    (J : (SheafOfModules.unit X.ringCatSheaf).Submodule) :
    J.toSheafOfModules.IsQuasicoherent ↔
      Nonempty (SheafOfModules.LocalGeneratorsData.{u} J.toSheafOfModules)
```

## Tag 01IO, a definition

[Tag 01IO](https://stacks.math.columbia.edu/tag/01IO) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L44) (StacksFrontier): “part (1): open immersions”. References: EGA I (4.2.1).
- [`AlgebraicGeometry.Scheme.Opens`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Opens#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L46) (StacksFrontier): “part (2): open subsets”. References: SGA 1 IX (2.3); SGA 1 VIII (4.4); SGA 4 VII (4.2.2), “partial”.
- [`AlgebraicGeometry.Scheme.Opens.toScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Opens.toScheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L50) (StacksFrontier): “part (2): restricted scheme”. References: EGA I (10.4.4), “special case”; EGA I (2.1.7); EGA I (2.2.10); EGA I (2.2.3); EGA I (4.1.3), “special case”; EGA IV (4.5.3), “partial”; EGA IV (4.9.6), “partial”; EGA IV (9.6.7); EGA IV (9.7.11), “more general”; SGA 2 XII (4.1).
- [`AlgebraicGeometry.Scheme.Opens.ι`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Opens.ι#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L61) (StacksFrontier): “part (2): inclusion”. References: EGA I (2.2.3); EGA I (4.1.7), “special case”; EGA I (4.2.1); SGA 1 XIII (2.1.0); SGA 2 XII (4.1); SGA 4 XVI (3.1), “more general”.
- [`AlgebraicGeometry.IsClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L68) (StacksFrontier): “part (3): closed immersions”. References: EGA I (4.2.1); SGA 3 IV (4.7).
- [`AlgebraicGeometry.Scheme.IdealSheafData`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L71) (StacksFrontier): “part (4): ideal sheaves”.
- [`AlgebraicGeometry.Scheme.IdealSheafData.subscheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.subscheme#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L72) (StacksFrontier): “part (4): closed subscheme”. References: EGA I (10.14.2), “partial”; EGA I (4.1.2); EGA I (4.1.3); EGA I (5.1.9), “more general”; EGA II (4.6.15), “more general”; EGA II (8.13.4); EGA III (5.3.5); EGA IV (21.15.3.3), “more general”; EGA IV (21.2.12), “more general”; EGA IV (21.6.5); EGA IV (4.5.3), “partial”; SGA 3 III (4.5.0).
- [`AlgebraicGeometry.Scheme.IdealSheafData.subschemeι`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.subschemeι#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L85) (StacksFrontier): “part (4): inclusion”. References: EGA I (4.1.7), “special case”; EGA I (5.1.9), “more general”; EGA II (4.6.15), “more general”; EGA II (8.13.4); EGA III (4.1.3), “canonical immersion i\_k”; EGA IV (21.15.3.3), “more general”; EGA IV (21.2.12), “more general”; EGA IV (21.6.5); SGA 1 III (7.1), “partial”; SGA 3 III (4.5.0).
- [`AlgebraicGeometry.IsImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L96) (StacksFrontier): “part (5): locally closed immersions”. References: EGA I (4.2.1); SGA 3 IV (4.7), “partial”.
- [`AlgebraicGeometry.IsImmersion.isImmersion_iff_exists`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsImmersion.isImmersion_iff_exists#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Immersion/Basic.lean#L99) (StacksFrontier): “part (5): factorization”. References: EGA I (4.2.1); SGA 6 0 (2.1), “special case”.

## Tag 01IQ, a lemma

[Tag 01IQ](https://stacks.math.columbia.edu/tag/01IQ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.isClosedImmersion_iff_isClosed_range`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/ImmersionClosedness.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/ImmersionClosedness.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/ImmersionClosedness.lean#L135) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.10, Tag 01IM](https://stacks.math.columbia.edu/tag/01IM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
