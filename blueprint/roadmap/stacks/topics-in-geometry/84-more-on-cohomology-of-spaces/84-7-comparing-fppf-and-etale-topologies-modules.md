---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.associatedSectionsEquiv, AlgebraicGeometry.BigEtaleSpaceSite.associatedPresheaf, AlgebraicGeometry.Space.isSheafFor_associatedPresheaf_of_isFpqcCovering, AlgebraicGeometry.BigEtaleSpaceSite.isSheaf_associatedPresheaf, AlgebraicGeometry.BigFppfSpaceSite.isSheaf_associatedPresheaf, BigEtaleSpaceSite.associatedPresheafIsoPullback, BigFppfSpaceSite.nonempty_associatedPresheaf_iso_pullback, BigEtaleSpaceSite.quasicoherentPullbackEquivalence
statement: formalized
proof: formalized
---

# 84.7 Comparing fppf and étale topologies: modules

Section 84.7 of the Stacks Project, [Tag 0DGM](https://stacks.math.columbia.edu/tag/0DGM). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DGN, a lemma

[Tag 0DGN](https://stacks.math.columbia.edu/tag/0DGN) in the Stacks Project.

**`AlgebraicGeometry.Space.associatedSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModule.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModule.lean#L303). The attribute's comment: “the value of the rule 𝓕 ↦ 𝓕ᵃ at an object (f : Y ⟶ X) of the big étale site of an algebraic space X is Γ(Y, f^*𝓕), the global sections of the inverse image of 𝓕 along f”.

> **The value of `𝓕ᵃ` at `(f : Y ⟶ X)` is `Γ(Y, f^*𝓕)`**: the morphisms `f^*𝒪_X ⟶ f^*𝓕` of
> `𝒪_Y`-modules correspond to the global sections of `f^*𝓕`.
>
> The inverse image of the structure sheaf is the structure sheaf
> (`AlgebraicGeometry.Space.modulePullbackUnitIso`), and a morphism out of the structure sheaf is
> a global section (`CategoryTheory.SheafOfModules.unitHomEquiv`).

```lean
noncomputable def associatedSectionsEquiv {X : AlgebraicSpaces B S hS}
    (F : Modules.{u, u} B S hS X.1 X.2) (Y : Over X) :
    ((modulePullback B S hS Y.hom).obj (SheafOfModules.unit _ :
          Modules.{u, u} B S hS X.1 X.2) ⟶
        (modulePullback B S hS Y.hom).obj F) ≃
      ((modulePullback B S hS Y.hom).obj F).sections
```

**`AlgebraicGeometry.BigEtaleSpaceSite.associatedPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModule.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModule.lean#L351). The attribute's comment: “the construction of the rule 𝓕 ↦ 𝓕ᵃ as a presheaf of abelian groups on the big étale site of an algebraic space; none of the seven assertions the source makes about it”.

> **Stacks 0DGN, the rule `𝓕ᵃ` on the big étale site of an algebraic space.**  For an
> `𝒪_X`-module `𝓕` on the small étale site of an algebraic space `X` of a big étale space site of
> Stacks 0DBX, the presheaf of abelian groups on the category underlying the big étale site of
> `X` whose value at `(f : Y ⟶ X)` is `Γ(Y, f^*𝓕)`.
>
> This is `AlgebraicGeometry.Space.associatedPresheaf` read on that category; the identification
> of its value with `Γ(Y, f^*𝓕)` is `AlgebraicGeometry.Space.associatedSectionsEquiv`.

```lean
noncomputable def BigEtaleSpaceSite.associatedPresheaf {S : Scheme.{u}}
    (T : BigEtaleSpaceSite S) (X : T.Spaces)
    (F : Space.Modules.{u, u} T.fppfSite S T.fppf_mem X.1 X.2) :
    (Over X)ᵒᵖ ⥤ AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.isSheafFor_associatedPresheaf_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleFpqcSheaf.lean, line 508](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleFpqcSheaf.lean#L508). The attribute's comment: “(1): for 𝓕 a quasi-coherent 𝒪\_X-module, 𝓕ᵃ satisfies the sheaf condition for every fpqc covering \{U\_i → U} of an object of (Spaces/X)\_étale; the fppf and étale cases are isSheafFor\_associatedPresheaf\_of\_isFppfCovering and isSheafFor\_associatedPresheaf\_of\_isEtaleCovering”.

> **Stacks 0DGN, clause (1): `𝓕ᵃ` is an fpqc sheaf.**  For a quasi-coherent `𝒪_X`-module `𝓕`
> on an algebraic space `X` over `S`, the rule `𝓕ᵃ : (f : Y ⟶ X) ↦ Γ(Y, f^*𝓕)`
> (`AlgebraicGeometry.Space.associatedPresheaf`) satisfies the sheaf condition for every family
> `{Y i ⟶ Y}` of morphisms of algebraic spaces over `X` which is an fpqc covering of `Y`.
>
> This is `AlgebraicGeometry.Space.isSheafFor_associatedPresheaf_ofArrows_overMk` for the members
> `(g i).left` of the family, each `Y i` being the object `Over.mk (Y i).hom` of `Over X`.

```lean
theorem isSheafFor_associatedPresheaf_of_isFpqcCovering {Y : Over X} {Yi : I → Over X}
    (g : ∀ i, Yi i ⟶ Y) (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite]
    (hg : IsFpqcCovering B S hS fun i ↦ (g i).left.hom) :
    (Presieve.ofArrows Yi g).IsSheafFor (associatedPresheaf F ⋙ forget AddCommGrpCat)
```

**`AlgebraicGeometry.BigEtaleSpaceSite.isSheaf_associatedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L70). The attribute's comment: “(1), a fortiori for étale coverings: 𝓕ᵃ is a sheaf on (Spaces/X)\_étale, for 𝓕 a quasi-coherent 𝒪\_X-module; the fpqc sheaf condition is Space.isSheafFor\_associatedPresheaf\_of\_isFpqcCovering”.

> **The rule `𝓕ᵃ` is a sheaf on `(Spaces/X)_étale`** (the étale case of Stacks 0DGN,
> clause (1)).  For a quasi-coherent `𝒪_X`-module `𝓕` on an algebraic space `X` of a big étale
> site, the rule `𝓕ᵃ : (f : Y ⟶ X) ↦ Γ(Y, f^*𝓕)` is a sheaf of
> abelian groups on the big étale site of `X`: it is isomorphic to the underlying presheaf of the
> sheaf of modules `π_X^*𝓕` (clause (2)).

```lean
theorem BigEtaleSpaceSite.isSheaf_associatedPresheaf {S : Scheme.{u}} (T : BigEtaleSpaceSite S)
    (X : T.Spaces) (F : Space.Modules.{u, u} T.fppfSite S T.fppf_mem X.1 X.2)
    [F.IsQuasicoherentOnSite] :
    Presheaf.IsSheaf (T.bigEtaleTopology X) (T.associatedPresheaf X F)
```

**`AlgebraicGeometry.BigFppfSpaceSite.isSheaf_associatedPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L86). The attribute's comment: “(1), a fortiori for fppf coverings: 𝓕ᵃ is a sheaf on (Spaces/X)\_fppf, for 𝓕 a quasi-coherent 𝒪\_X-module; the fpqc sheaf condition is Space.isSheafFor\_associatedPresheaf\_of\_isFpqcCovering”.

> **The rule `𝓕ᵃ` is a sheaf on `(Spaces/X)_fppf`** (the fppf case of Stacks 0DGN,
> clause (1)).  For a quasi-coherent `𝒪_X`-module `𝓕` on an algebraic space `X` of a big fppf
> site, the rule `𝓕ᵃ : (f : Y ⟶ X) ↦ Γ(Y, f^*𝓕)` is a sheaf of
> abelian groups on the big fppf site of `X`: it is isomorphic to the underlying presheaf of the
> sheaf of modules `a_X^*𝓕` (clause (3)).

```lean
theorem BigFppfSpaceSite.isSheaf_associatedPresheaf {S : Scheme.{u}} (T : BigFppfSpaceSite S)
    (X : T.Spaces) (F : Space.Modules.{u, u} T.schemeSite S T.scheme_mem X.1 X.2)
    [F.IsQuasicoherentOnSite] :
    Presheaf.IsSheaf (BigFppfSpaceOver.topology T X) (Space.associatedPresheaf F)
```

Declarations registered for the tag:

- [`BigEtaleSpaceSite.associatedPresheafIsoPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BigEtaleSpaceSite.associatedPresheafIsoPullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L94) (StacksFrontier): “(2): 𝓕ᵃ ≅ π\_X^*𝓕 on (Spaces/X)\_étale, for 𝓕 a quasi-coherent 𝒪\_X-module read on the spaces-étale site through ι”.
- [`BigFppfSpaceSite.nonempty_associatedPresheaf_iso_pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BigFppfSpaceSite.nonempty_associatedPresheaf_iso_pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L98) (StacksFrontier): “(3): 𝓕ᵃ ≅ a\_X^*𝓕 on (Spaces/X)\_fppf, for 𝓕 a quasi-coherent 𝒪\_X-module read on the spaces-étale site through ι”.
- [`BigEtaleSpaceSite.quasicoherentPullbackEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BigEtaleSpaceSite.quasicoherentPullbackEquivalence#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L102) (StacksFrontier): “(4): 𝓕 ↦ 𝓕ᵃ = π\_X^*𝓕 is an equivalence between quasi-coherent 𝒪\_X-modules and quasi-coherent modules on ((Spaces/X)\_étale, 𝒪), with quasi-inverse π\_\{X,*}”.
- [`BigFppfSpaceSite.quasicoherentPullbackEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BigFppfSpaceSite.quasicoherentPullbackEquivalence#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L106) (StacksFrontier): “(5): 𝓕 ↦ 𝓕ᵃ = a\_X^*𝓕 is an equivalence between quasi-coherent 𝒪\_X-modules and quasi-coherent modules on ((Spaces/X)\_fppf, 𝒪), with quasi-inverse a\_\{X,*}”.
- [`BigFppfSpaceSite.pushforward_pullback_of_quasicoherent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BigFppfSpaceSite.pushforward_pullback_of_quasicoherent#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L110) (StacksFrontier): “(6): ε\_\{X,*}a\_X^*𝓕 ≅ π\_X^*𝓕 and 𝓕 ≅ a\_\{X,*}a\_X^*𝓕 (the unit is an isomorphism) for 𝓕 a quasi-coherent 𝒪\_X-module”.
- [`BigFppfSpaceSite.isZero_rightDerived_pushforward_pullback_of_quasicoherent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BigFppfSpaceSite.isZero_rightDerived_pushforward_pullback_of_quasicoherent#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleAssociatedModuleStatement.lean#L114) (StacksFrontier): “(7): R^i ε\_\{X,*}(a\_X^*𝓕) = 0 and R^i a\_\{X,*}(a\_X^*𝓕) = 0 for i > 0 and 𝓕 a quasi-coherent 𝒪\_X-module”.

## Tag 0DGP, a lemma

[Tag 0DGP](https://stacks.math.columbia.edu/tag/0DGP) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_bigEtalePullbackToPushforwardPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfModuleRightAcyclicCanonical.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfModuleRightAcyclicCanonical.lean#L127). The attribute's comment: “(1) the canonical map π\_X^*𝓕 ⟶ ε\_\{X,*}a\_X^*𝓕 (unit of ε\_X^* ⊣ ε\_\{X,*} and a\_X = π\_X ∘ ε\_X) is an isomorphism, and ε\_\{X,*}a\_X^*𝓕 ⟶ Rε\_\{X,*}a\_X^*𝓕 is an isomorphism”.

> **Stacks 0DGP: the map `π_X^*𝓕 ⟶ Rε_{X,*}(a_X^*𝓕)` is an isomorphism** for a quasi-coherent
> `𝒪_X`-module `𝓕`: the canonical map `π_X^*𝓕 ⟶ ε_{X,*}(a_X^*𝓕)` is an isomorphism (Stacks 0DGN
> (6)) and `a_X^*𝓕` is right acyclic for `ε_{X,*}` (Stacks 0DGN (7)), so that the canonical map
> `ε_{X,*}(a_X^*𝓕) ⟶ Rε_{X,*}(a_X^*𝓕)` is an isomorphism too.

```lean
theorem isIso_bigEtalePullbackToPushforwardPullback
    (F : SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (Space.spacesEtaleRingedSite T.schemeSite S T.scheme_mem X).O))
    [hF : F.IsQuasicoherentOnSite] :
    IsIso (bigEtalePullbackToPushforwardPullback T E h X F) ∧
      Functor.rightAcyclic.{u + 2, u + 2}
        (fppfToBigEtaleRingedHom T E h X).toRingedToposSiteHom.pushforwardTopos
        ((fppfToSpacesEtaleRingedSiteHom T X).toRingedToposSiteHom.pullbackTopos.obj F)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.BigFppfSpaceSite.isIso_derivedPushforward_pullback_of_quasicoherent`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfModuleRightAcyclic.lean#L117), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfQuasicoherentTags.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfQuasicoherentTags.lean#L28) (StacksFrontier): “both maps: π\_X^*𝓕 ≅ ε\_\{X,*}a\_X^*𝓕 ⟶ Rε\_\{X,*}a\_X^*𝓕 and 𝓕 ≅ a\_\{X,*}a\_X^*𝓕 ⟶ Ra\_\{X,*}a\_X^*𝓕, the second map in each being the canonical (right acyclicity) isomorphism”.

## Tag 0DGQ, a lemma

[Tag 0DGQ](https://stacks.math.columbia.edu/tag/0DGQ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.BigFppfSpaceSite.homology_pullback_of_quasicoherent`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigEtaleQuasicoherentHomology.lean#L330), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfQuasicoherentTags.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfQuasicoherentTags.lean#L32) (StacksFrontier).

## Tag 0DGR, a lemma

[Tag 0DGR](https://stacks.math.columbia.edu/tag/0DGR) in the Stacks Project.

**`AlgebraicGeometry.BigFppfSpaceSite.isIso_derivedUnits_of_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleDerivedUnitQuasicoherent.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigFppfToSmallEtaleDerivedUnitQuasicoherent.lean#L173).

> **Stacks 0DGR.** Let `S` be a scheme and `X` an algebraic space over `S`. For `K` in
> `D_QCoh(𝒪_X)`, an object of `D(X_{spaces,étale}, 𝒪_X)` all of whose cohomology sheaves are
> quasi-coherent, the maps
>
> `Lπ_X^*K ⟶ Rε_{X,*}(La_X^*K)` and `K ⟶ Ra_{X,*}(La_X^*K)`
>
> are isomorphisms, where `a_X = π_X ∘ ε_X : ((Spaces/X)_fppf, 𝒪) ⟶ (X_{spaces,étale}, 𝒪_X)`.
> The first map is the unit of `Lε_X^* ⊣ Rε_{X,*}` at `Lπ_X^*K` followed by `Rε_{X,*}` of the
> comparison `Lε_X^*Lπ_X^*K ⟶ La_X^*K` of Stacks 0D6D; the second is the unit of `La_X^* ⊣ Ra_{X,*}`
> at `K`.

```lean
theorem isIso_derivedUnits_of_quasicoherent
    (X : T.Spaces)
    (K : DerivedCategory (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
      (Space.spacesEtaleRingedSite E.fppfSite S E.fppf_mem (etaleSpace T E h X)).O)))
    (hK : ∀ i : ℤ, ((DerivedCategory.homologyFunctor _ i).obj K).IsQuasicoherentOnSite) :
    IsIso ((derivedAdjunction (epsilonHom T E h X)
        (fppfToBigEtaleRingedHom T E h X).isMorphismOfSites).unit.app
          ((derivedPullback (BigEtaleSpaceSite.spacesEtaleRestrictionRingedSiteHom E
            (etaleSpace T E h X)).toRingedToposSiteHom).obj K) ≫
      (derivedPushforward (epsilonHom T E h X)).map
        ((derivedPullbackCompComparison (epsilonHom T E h X)
          (BigEtaleSpaceSite.spacesEtaleRestrictionRingedSiteHom E
            (etaleSpace T E h X)).toRingedToposSiteHom).app K)) ∧
    IsIso ((derivedAdjunction ((BigEtaleSpaceSite.spacesEtaleRestrictionRingedSiteHom E
        (etaleSpace T E h X)).toRingedToposSiteHom.comp (epsilonHom T E h X))
        (RingedToposSiteHom.isMorphismOfSites_comp_u _ _
          (fppfToBigEtaleRingedHom T E h X).isMorphismOfSites
          (BigEtaleSpaceSite.spacesEtaleRestrictionRingedSiteHom E
            (etaleSpace T E h X)).isMorphismOfSites)).unit.app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 84.7, Tag 0DGM](https://stacks.math.columbia.edu/tag/0DGM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
