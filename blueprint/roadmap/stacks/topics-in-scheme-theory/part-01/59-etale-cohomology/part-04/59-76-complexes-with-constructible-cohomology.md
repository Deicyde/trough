---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.ConstructibleDerivedCategory, Stacks.EtaleCohomology.ConstructibleEtaleDerivedCategory, Stacks.EtaleCohomology.isConstructible_derivedRestriction, Stacks.EtaleCohomology.isConstructible_derivedModuleExtensionByZero, Stacks.EtaleCohomology.isConstructible_derivedPullback, Stacks.EtaleCohomology.isConstructible_mapDerivedCategory_smallEtaleSheafPullback, Stacks.EtaleCohomology.exists_shriekConstant_cover_of_isConstructible_homology, Stacks.EtaleCohomology.exists_shriekConstant_cover_of_isConstructibleModuleEtaleSheaf
statement: formalized
proof: formalized
---

# 59.76 Complexes with constructible cohomology

Section 59.76 of the Stacks Project, [Tag 095V](https://stacks.math.columbia.edu/tag/095V). 6 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 095W, a definition

[Tag 095W](https://stacks.math.columbia.edu/tag/095W) in the Stacks Project.

**`Stacks.EtaleCohomology.ConstructibleDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/Basic.lean#L67). References: SGA 5 I (App.1.1), “constant Λ coefficients”; SGA 5 IIIB (6.1), “D_c(-)”.

> The full subcategory of the unbounded derived category of small-étale
> `Λ`-module sheaves with constructible cohomology sheaves.

```lean
public abbrev ConstructibleDerivedCategory (B : BigEtaleSite.{u}) (X : B.Scheme)
    (Λ : Type r) [Ring Λ]
    [HasSheafify (SmallEtale.topology B X.1 X.property) (ModuleCat.{w} Λ)]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{w} Λ)
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V) (ModuleCat.{w} Λ)]
```

**`Stacks.EtaleCohomology.ConstructibleEtaleDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleEtaleDerivedCategory.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleEtaleDerivedCategory.lean#L48). The attribute's comment: “the full subcategory of D(X_ét, Λ) of complexes whose cohomology sheaves are constructible, for module sections in any universe containing that of the schemes”. References: SGA 5 IIIB (6.1).

> **Stacks 095W.** `D_c(X_ét, Λ)`: the full subcategory of the unbounded derived category of
> sheaves of `Λ`-modules on the small étale site of `X` on the complexes all of whose cohomology
> sheaves are constructible sheaves of `Λ`-modules.

```lean
public abbrev ConstructibleEtaleDerivedCategory (B : BigEtaleSite.{u}) (X : B.Scheme)
    (Λ : Type r) [Ring Λ]
```

## Tag 095X, a lemma

[Tag 095X](https://stacks.math.columbia.edu/tag/095X) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructible_derivedRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZero.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZero.lean#L148). The attribute's comment: “part (1)”.

> Let `Λ` be a Noetherian ring, let `X` be a scheme and let `U` be an object of the small étale
> site of `X`. If a complex `K` of étale sheaves of `Λ`-modules on `X` lies in `D_c(X_étale, Λ)`,
> then its restriction `K|_U` lies in `D_c(U_étale, Λ)`.

```lean
public theorem isConstructible_derivedRestriction
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsConstructible B X Λ K) :
    IsConstructible B U.obj.left Λ
      ((moduleRestriction.{u, r, max (u + 1) r} B X.obj X.property U
        Λ).mapDerivedCategory.obj K)
```

**`Stacks.EtaleCohomology.isConstructible_derivedModuleExtensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZero.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZero.lean#L168). The attribute's comment: “part (2)”.

> Let `Λ` be a Noetherian ring, let `X` be a scheme and let `U` be an object of the small étale
> site of `X` whose structure morphism `j : U ⟶ X` is quasi-compact and quasi-separated. If a complex
> `M` of étale sheaves of `Λ`-modules on `U` lies in `D_c(U_étale, Λ)`, then `j_! M` lies in
> `D_c(X_étale, Λ)`.

```lean
public theorem isConstructible_derivedModuleExtensionByZero
    (hqc : QuasiCompact (B.inclusion.map U.obj.hom))
    (hqs : QuasiSeparated (B.inclusion.map U.obj.hom))
    (M : DerivedCategory (Sheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hM : IsConstructible B U.obj.left Λ M) :
    IsConstructible B X Λ
      ((moduleExtensionByZero.{u, r} B X.obj X.property U Λ).mapDerivedCategory.obj M)
```

## Tag 095Y, a lemma

[Tag 095Y](https://stacks.math.columbia.edu/tag/095Y) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructible_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/InverseImage.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/InverseImage.lean#L109).

> **Stacks 095Y.** Let `Λ` be a Noetherian ring and `f : X ⟶ Y` a morphism of schemes. If a
> complex of étale sheaves of `Λ`-modules on `Y` lies in `D_c(Y_étale, Λ)`, that is has
> constructible cohomology sheaves in every degree, then its derived inverse image `Lf^*K` lies in
> `D_c(X_étale, Λ)`.

```lean
public theorem isConstructible_derivedPullback {X Y : B.Scheme} (f : X ⟶ Y)
    [HasSheafify (SmallEtale.topology B Y.obj Y.property) (ModuleCat.{max (u + 1) w} Λ)]
    [HasSheafify (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) w} Λ)]
    [∀ (S T : B.Scheme) (g : T ⟶ S),
      ((smallEtaleBaseChange B g).sheafPushforwardContinuous (ModuleCat.{max (u + 1) w} Λ)
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V)
        (ModuleCat.{max (u + 1) w} Λ)]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B Y.obj Y.property)
      (ModuleCat.{max (u + 1) w} Λ)))
    (hK : IsConstructible B Y Λ K) :
    IsConstructible B X Λ
      (((smallEtaleBaseChange B f).sheafPullback (ModuleCat.{max (u + 1) w} Λ)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).mapDerivedCategory.obj K)
```

**`Stacks.EtaleCohomology.isConstructible_mapDerivedCategory_smallEtaleSheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/InverseImageUnconditional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/InverseImageUnconditional.lean#L68).

> **Stacks 095Y.** Let `Λ` be a Noetherian ring and `f : X ⟶ Y` a morphism of schemes. If
> `K ∈ D_c(Y_étale, Λ)`, that is the cohomology sheaves of `K` are constructible in every degree,
> then `Lf^*K ∈ D_c(X_étale, Λ)`.
>
> Inverse image of module sheaves is exact, so `Lf^*` is the termwise functor
> `CategoryTheory.Functor.mapDerivedCategory` and `Hⁱ(Lf^*K) ≅ f⁻¹(HⁱK)`, which is constructible by
> Tag 095G; this is `Stacks.EtaleCohomology.isConstructible_derivedPullback`, whose sheafification
> and inverse-image instances are supplied by the small étale site.

```lean
public theorem isConstructible_mapDerivedCategory_smallEtaleSheafPullback {X Y : B.Scheme}
    (f : X ⟶ Y)
    (K : DerivedCategory (Sheaf (SmallEtale.topology B Y.obj Y.property)
      (ModuleCat.{max (u + 1) w} Λ)))
    (hK : IsConstructible B Y Λ K) :
    IsConstructible B X Λ
      (((smallEtaleBaseChange B f).sheafPullback (ModuleCat.{max (u + 1) w} Λ)
        (SmallEtale.topology B Y.obj Y.property)
        (SmallEtale.topology B X.obj X.property)).mapDerivedCategory.obj K)
```

## Tag 095Z, a lemma

[Tag 095Z](https://stacks.math.columbia.edu/tag/095Z) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_shriekConstant_cover_of_isConstructible_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekCoverOfCohomology.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekCoverOfCohomology.lean#L168).

> **Stacks 095Z.** Let `X` be a quasi-compact and quasi-separated scheme, let `Λ` be a
> Noetherian ring, let `K ∈ D(X_étale, Λ)` and let `b` be an integer for which `H^b(K)` is
> constructible. Then there are finitely many affine objects `U i` of the small étale site of `X`
> and a map `F[-b] ⟶ K`, where `F = ⊕ᵢ j_{U i!} Λ-underline`, inducing a surjection on degree-`b`
> cohomology.
>
> A complex `A` representing `K` is chosen;
> `AlgebraicGeometry.exists_finite_epi_comp_sigma_moduleShriekConstant_affine` — Tags 093B and
> 095P in the shape the source's proof quotes them — covers the degree-`b` cocycles of `A` well
> enough for the canonical surjection onto `H^b(K)` to survive, and
> `Stacks.Homology.exists_single_map_epi_derivedHomology` turns that cover into the
> required map in the derived category.
>
> Nothing is granted; see "What the proof rests on" in the module documentation.

```lean
public theorem exists_shriekConstant_cover_of_isConstructible_homology (X : B.Scheme)
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    [HasSheafify (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)]
    [∀ (S T : B.Scheme) (g : T ⟶ S),
      ((smallEtaleBaseChange B g).sheafPushforwardContinuous (ModuleCat.{max (u + 1) r} Λ)
        (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V)
        (ModuleCat.{max (u + 1) r} Λ)]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ))) (b : ℤ)
    (hK : IsConstructibleModuleSheaf B X Λ
      ((homologyFunctor (Sheaf (SmallEtale.topology B X.obj X.property)
        (ModuleCat.{max (u + 1) r} Λ)) b).obj K)) :
    ∃ (n : ℕ) (U : Fin n → SmallEtale B X.obj X.property),
      (∀ i, IsAffine ((SmallEtale.toScheme B X.obj X.property).obj (U i))) ∧
      ∃ f : (singleFunctor (Sheaf (SmallEtale.topology B X.obj X.property)
          (ModuleCat.{max (u + 1) r} Λ)) b).obj
          (∐ fun i : Fin n ↦ moduleShriekConstant.{u, r, r} B X Λ (U i)) ⟶ K,
        Epi ((homologyFunctor (Sheaf (SmallEtale.topology B X.obj X.property)
          (ModuleCat.{max (u + 1) r} Λ)) b).map f)
```

**`Stacks.EtaleCohomology.exists_shriekConstant_cover_of_isConstructibleModuleEtaleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekCoverOfCohomologyEtale.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekCoverOfCohomologyEtale.lean#L68).

> **Stacks 095Z.** Let `X` be a quasi-compact and quasi-separated scheme, let `Λ` be a
> Noetherian ring, let `K ∈ D(X_étale, Λ)` and let `b` be an integer such that `H^b(K)` is
> constructible. Then there exist a sheaf `F = ⊕ᵢ j_{U i!} Λ-underline`, a finite direct sum with
> every `U i` an affine object of `X_étale`, and a map `F[-b] ⟶ K` in `D(X_étale, Λ)` inducing a
> surjection `F ⟶ H^b(K)`.

```lean
public theorem exists_shriekConstant_cover_of_isConstructibleModuleEtaleSheaf (X : B.Scheme)
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ))) (b : ℤ)
    (hK : IsConstructibleModuleEtaleSheaf B X Λ
      ((homologyFunctor (Sheaf (SmallEtale.topology B X.obj X.property)
        (ModuleCat.{max (u + 1) r} Λ)) b).obj K)) :
    ∃ (n : ℕ) (U : Fin n → SmallEtale B X.obj X.property),
      (∀ i, IsAffine ((SmallEtale.toScheme B X.obj X.property).obj (U i))) ∧
      ∃ f : (singleFunctor (Sheaf (SmallEtale.topology B X.obj X.property)
          (ModuleCat.{max (u + 1) r} Λ)) b).obj
          (∐ fun i : Fin n ↦ moduleShriekConstant.{u, r, r} B X Λ (U i)) ⟶ K,
        Epi ((singleFunctorCompHomologyFunctorIso (Sheaf (SmallEtale.topology B X.obj X.property)
            (ModuleCat.{max (u + 1) r} Λ)) b).inv.app
              (∐ fun i : Fin n ↦ moduleShriekConstant.{u, r, r} B X Λ (U i)) ≫
          (homologyFunctor (Sheaf (SmallEtale.topology B X.obj X.property)
            (ModuleCat.{max (u + 1) r} Λ)) b).map f)
```

## Tag 0960, a lemma

[Tag 0960](https://stacks.math.columbia.edu/tag/0960) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructible_of_isRepresentedByBoundedAboveConstructibleFlatComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/BoundedAboveShriekComplex.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/BoundedAboveShriekComplex.lean#L373). The attribute's comment: “the implication (3) => (1), from the weak Serre property `hSerre` of the constructible sheaves of modules”.

> **Tag 0960, the implication (3) ⟹ (1).** An object of `D(X_étale, Λ)` represented by a
> bounded above complex of flat constructible sheaves of `Λ`-modules has constructible cohomology
> sheaves.
>
> A flat constructible sheaf is constructible, by
> `AlgebraicGeometry.isConstructibleModuleSheaf_of_isConstructibleFlatModuleSheaf`, and a complex
> of constructible sheaves has constructible cohomology, by
> `Stacks.EtaleCohomology.isConstructible_of_forall_isConstructibleModuleSheaf`, which is where
> the weak Serre hypothesis `hSerre` is used; see "Where the weak Serre property comes from" in the
> module documentation for why it is still a hypothesis at a free coefficient universe, and
> `AlgebraicGeometry.isWeakSerreClass_isConstructibleModuleSheafProperty` for what discharges it
> at `max (u + 1) r`. The bound is not needed for this implication and is not used.

```lean
public theorem isConstructible_of_isRepresentedByBoundedAboveConstructibleFlatComplex
    (hSerre : (isConstructibleModuleSheafProperty.{u, w, r} B X Λ).IsWeakSerreClass)
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)))
    (hK : IsRepresentedByBoundedAboveConstructibleFlatComplex.{u, w, r} B X Λ K) :
    IsConstructible B X Λ K
```

**`Stacks.EtaleCohomology.isRepresentedByBoundedAboveConstructibleFlatComplex_of_shriekSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/BoundedAboveShriekComplex.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/BoundedAboveShriekComplex.lean#L430). The attribute's comment: “the implication (2) => (3)”.

> **Tag 0960, the implication (2) ⟹ (3).** A bounded above complex whose terms are finite
> direct sums of sheaves `j_{U!} Λ-underline` with `U` affine is a bounded above complex of flat
> constructible sheaves of `Λ`-modules, so an object of `D(X_étale, Λ)` satisfying condition (2)
> satisfies condition (3).
>
> The same complex is used; each term is isomorphic to a finite direct sum of affine shriek
> constants, which is flat constructible by
> `AlgebraicGeometry.isConstructibleFlatModuleSheaf_sigma_moduleShriekConstant_of_quasiSeparated`,
> and flat constructibility is invariant under isomorphism by
> `AlgebraicGeometry.isConstructibleFlatModuleSheaf_congr`. That input conjoins Tag 03S8 with the
> flatness of `j_{U!} Λ-underline`, which the source leaves unstated, and the closure of flat
> constructible sheaves under finite direct sums; see "Why quasi-separatedness is assumed" in the
> module documentation for why it is the only hypothesis on `X` that enters. Quasi-compactness of
> `X` is not needed for this implication and is not assumed.

```lean
public theorem isRepresentedByBoundedAboveConstructibleFlatComplex_of_shriekSum
    [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsRepresentedByAffineShriekSumComplex.{u, r} B X Λ K) :
    IsRepresentedByBoundedAboveConstructibleFlatComplex.{u, max (u + 1) r, r} B X Λ K
```

**`Stacks.EtaleCohomology.isConstructible_of_isRepresentedByAffineShriekSumComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/BoundedAboveShriekComplex.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/BoundedAboveShriekComplex.lean#L455). The attribute's comment: “the implication (2) => (1)”.

> **Tag 0960, the implication (2) ⟹ (1).** An object of `D(X_étale, Λ)` represented by a
> bounded above complex whose terms are finite direct sums of sheaves `j_{U!} Λ-underline` with
> `U` affine has constructible cohomology sheaves, so it lies in the constructible derived
> category of Tag 095W.
>
> This is the composite of the implications (2) ⟹ (3) and (3) ⟹ (1), and nothing is carried. The
> weak Serre property the second step needs is at this coefficient universe Stacks 03RZ (3),
> `AlgebraicGeometry.isWeakSerreClass_isConstructibleModuleSheafProperty`; the flat
> constructibility of a finite affine shriek sum which the first step needs is
> `AlgebraicGeometry.isConstructibleFlatModuleSheaf_sigma_moduleShriekConstant_of_quasiSeparated`,
> and that is the only reason `X` is asked to be quasi-separated. Quasi-compactness of `X` is not
> needed and is not assumed.

```lean
public theorem isConstructible_of_isRepresentedByAffineShriekSumComplex
    [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsRepresentedByAffineShriekSumComplex.{u, r} B X Λ K) :
    IsConstructible B X Λ K
```

**`Stacks.EtaleCohomology.isRepresentedByAffineShriekSumComplex_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean#L307). The attribute's comment: “the implication (1) => (2)”.

> **Tag 0960, the implication (1) ⟹ (2).** Let `X` be a quasi-compact and quasi-separated
> scheme, let `Λ` be a Noetherian ring and let `K ∈ D^-(X_étale, Λ)` have constructible cohomology
> sheaves. Then `K` is represented by a bounded above complex each of whose terms is a finite
> direct sum of sheaves `j_{U!} Λ-underline` with `U` an affine object of the small étale site
> of `X`.
>
> Boundedness above of `K` is the vanishing `hvan` of `H^i(K)` for `i > b`, which by
> `DerivedCategory.isLE_iff` says exactly that `K` lies in `D^-(X_étale, Λ)`; it is the standing
> assumption of the source's equivalence.
>
> The proof chooses a cochain complex `A` with `A^i = 0` for `i > b` representing `K`
> (`DerivedCategory.exists_iso_Q_obj_of_isLE`) and resolves it by the finite affine shriek sums
> using `Stacks.Homology.BoundedAboveResolution.exists_quasiIso_isStrictlyLE_of_coversEpis`. The
> three closure properties that engine needs of the class of finite affine shriek sums are
> `Stacks.EtaleCohomology.isAffineShriekSum_zero`,
> `Stacks.EtaleCohomology.isAffineShriekSum_biprod` and
> `Stacks.EtaleCohomology.isAffineShriekSum_of_iso`, and the covering property is
> `Stacks.EtaleCohomology.coversEpis_isAffineShriekSum`, which rests on Stacks 093B (2) with
> Stacks 095P and on Stacks 03S8 for sheaves of modules. The weak Serre class the engine tests its
> kernels against is the constructible sheaves of `Λ`-modules, Stacks 03RZ (3), supplied by
> `AlgebraicGeometry.isWeakSerreClass_isConstructibleModuleSheafProperty`. Nothing is carried.

```lean
public theorem isRepresentedByAffineShriekSumComplex_of_isConstructible
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ))) (hK : IsConstructible B X Λ K) (b : ℤ)
    (hvan : ∀ i : ℤ, b < i → IsZero ((DerivedCategory.homologyFunctor
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)) i).obj K)) :
    IsRepresentedByAffineShriekSumComplex.{u, r} B X Λ K
```

**`Stacks.EtaleCohomology.isRepresentedByBoundedAboveConstructibleFlatComplex_of_isConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean#L346). The attribute's comment: “the implication (1) => (3)”. References: SGA 4½ Rapport (4.7), “partial”.

> **Tag 0960, the implication (1) ⟹ (3).** Let `X` be a quasi-compact and quasi-separated
> scheme, let `Λ` be a Noetherian ring and let `K ∈ D^-(X_étale, Λ)` have constructible cohomology
> sheaves. Then `K` is represented by a bounded above complex of flat constructible sheaves of
> `Λ`-modules.
>
> This is the composite of (1) ⟹ (2),
> `Stacks.EtaleCohomology.isRepresentedByAffineShriekSumComplex_of_isConstructible`, with
> (2) ⟹ (3),
> `Stacks.EtaleCohomology.isRepresentedByBoundedAboveConstructibleFlatComplex_of_shriekSum`. Both
> steps are unconditional.

```lean
public theorem isRepresentedByBoundedAboveConstructibleFlatComplex_of_isConstructible
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ))) (hK : IsConstructible B X Λ K) (b : ℤ)
    (hvan : ∀ i : ℤ, b < i → IsZero ((DerivedCategory.homologyFunctor
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)) i).obj K)) :
    IsRepresentedByBoundedAboveConstructibleFlatComplex.{u, max (u + 1) r, r} B X Λ K
```

**`Stacks.EtaleCohomology.isRepresentedByAffineShriekSumComplex_of_constructibleFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean#L368). The attribute's comment: “the implication (3) => (2)”.

> **Tag 0960, the implication (3) ⟹ (2).** An object of `D(X_étale, Λ)` represented by a
> bounded above complex of flat constructible sheaves of `Λ`-modules is represented by a bounded
> above complex each of whose terms is a finite direct sum of sheaves `j_{U!} Λ-underline` with
> `U` an affine object of the small étale site of `X`.
>
> This is the composite of (3) ⟹ (1),
> `Stacks.EtaleCohomology.isConstructible_of_isRepresentedByBoundedAboveConstructibleFlatComplex`,
> with (1) ⟹ (2),
> `Stacks.EtaleCohomology.isRepresentedByAffineShriekSumComplex_of_isConstructible`. No
> boundedness hypothesis on `K` is needed here: condition (3) exhibits a complex which vanishes
> above some degree `a`, and `DerivedCategory.isLE_Q_obj_iff` transports that bound to `K`.

```lean
public theorem isRepresentedByAffineShriekSumComplex_of_constructibleFlat
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsRepresentedByBoundedAboveConstructibleFlatComplex.{u, max (u + 1) r, r} B X Λ K) :
    IsRepresentedByAffineShriekSumComplex.{u, r} B X Λ K
```

**`Stacks.EtaleCohomology.isConstructible_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekSumResolution.lean#L400). References: SGA 4½ Rapport (4.7), “(1) ⇒ (3)”.

> **Tag 0960.** Let `X` be a quasi-compact and quasi-separated scheme, let `Λ` be a Noetherian
> ring and let `K ∈ D^-(X_étale, Λ)`, the bound being the hypothesis `hvan`. Then the following
> are equivalent:
>
> 1. `K` lies in `D_c(X_étale, Λ)`, i.e. every cohomology sheaf of `K` is constructible;
> 2. `K` is represented by a bounded above complex whose terms are finite direct sums of sheaves
>    `j_{U!} Λ-underline` with `U` an affine object of the small étale site of `X`;
> 3. `K` is represented by a bounded above complex of flat constructible sheaves of `Λ`-modules.
>
> The equivalence is closed along the cycle (1) ⟹ (2) ⟹ (3) ⟹ (1), by
> `Stacks.EtaleCohomology.isRepresentedByAffineShriekSumComplex_of_isConstructible`,
> `Stacks.EtaleCohomology.isRepresentedByBoundedAboveConstructibleFlatComplex_of_shriekSum` and
> `Stacks.EtaleCohomology.isConstructible_of_isRepresentedByBoundedAboveConstructibleFlatComplex`,
> whose weak Serre hypothesis is discharged at this coefficient universe by Stacks 03RZ (3),
> `AlgebraicGeometry.isWeakSerreClass_isConstructibleModuleSheafProperty`. The three remaining
> implications are also stated separately, as the composites they are; `hvan` is used only in
> (1) ⟹ (2), the other two steps producing their own bound.

```lean
public theorem isConstructible_tfae
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ))) (b : ℤ)
    (hvan : ∀ i : ℤ, b < i → IsZero ((DerivedCategory.homologyFunctor
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)) i).obj K)) :
    List.TFAE
      [IsConstructible B X Λ K,
        IsRepresentedByAffineShriekSumComplex.{u, r} B X Λ K,
        IsRepresentedByBoundedAboveConstructibleFlatComplex.{u, max (u + 1) r, r} B X Λ K]
```

## Tag 0961, a lemma

[Tag 0961](https://stacks.math.columbia.edu/tag/0961) in the Stacks Project.

**`Stacks.EtaleCohomology.minus_and_isConstructible_derivedTensor_of_arbitraryScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/DerivedTensorArbitraryScheme.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/DerivedTensorArbitraryScheme.lean#L334). The attribute's comment: “for an arbitrary scheme: both halves of the conclusion, the boundedness estimate for the derived tensor product and the constructible case alike, from the bounded above representative with flat etale stalks of Stacks 05T7 and 093B (2), the quasi-compact quasi-separated case of Stacks 0960 and 095I, and Zariski descent for constructibility, Stacks 095F”.

> **Stacks 0961.** Let `X` be a scheme, `Λ` a Noetherian ring and `K, L ∈ D_c^-(X_étale, Λ)`.
> Then `K ⊗_Λ^L L` is in `D_c^-(X_étale, Λ)`: it is bounded above, and all of its cohomology
> sheaves are constructible.
>
> Nothing is asked of the scheme, and no part of the conclusion is assumed. The only thing asked of
> the derived tensor product `T` is `hcomp`, which says that `T` *is* the derived tensor product:
> its value on a pair of complexes whose right member is a bounded above complex of flat sheaves is
> the total tensor complex. Both halves of the conclusion come from one complex `Tot(P ⊗_Λ G)`,
> where `P` and `G` are the bounded above representatives with flat étale stalks of
> `AlgebraicGeometry.exists_isStrictlyLE_flat_etaleModuleStalk_of_isLE` — boundedness above with
> the bound `a + b`, and constructibility of the cohomology sheaves by
> `Stacks.EtaleCohomology.isConstructibleModuleSheaf_homology_mapBifunctor`.

```lean
public theorem minus_and_isConstructible_derivedTensor_of_arbitraryScheme
    (hcomp : IsDerivedTensorOnFlatComplexes.{u, w} B X Λ T)
    (K L : DerivedCategory.Minus (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) w} Λ)))
    (hK : IsConstructible B X Λ K.obj) (hL : IsConstructible B X Λ L.obj) :
    (DerivedCategory.TStructure.t (C := Sheaf (SmallEtale.topology B X.obj X.property)
        (ModuleCat.{max (u + 1) w} Λ))).minus ((T.obj K.obj).obj L.obj) ∧
      IsConstructible B X Λ ((T.obj K.obj).obj L.obj)
```

**`Stacks.EtaleCohomology.minus_and_isConstructible_etaleModuleSheafDerivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/EtaleModuleSheafDerivedTensor.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/EtaleModuleSheafDerivedTensor.lean#L299). The attribute's comment: “for the derived tensor product of sheaves of Lambda-modules on the small etale site of an arbitrary scheme, built on K-flat resolutions (Stacks 06YS, 06YU) and shown to be computed by total tensor complexes on bounded above complexes of flat sheaves (Stacks 06YQ)”.

> **Stacks 0961.** Let `X` be a scheme, `Λ` a Noetherian ring and `K, L ∈ D_c^-(X_étale, Λ)`.
> Then `K ⊗_Λ^L L` is in `D_c^-(X_étale, Λ)`: it is bounded above, and all of its cohomology
> sheaves are constructible.
>
> The derived tensor product is `Stacks.EtaleCohomology.etaleModuleSheafDerivedTensor`, the
> derived functor of the tensor product of sheaves of `Λ`-modules on K-flat resolutions, and
> nothing is assumed of it or of `X`. That it is computed by the total tensor complex on a bounded
> above complex of flat sheaves is proved,
> `Stacks.EtaleCohomology.isDerivedTensorOnFlatComplexes_etaleModuleSheafDerivedTensor`, and the
> rest is the arbitrary-scheme argument of
> `Stacks.EtaleCohomology.minus_and_isConstructible_derivedTensor_of_arbitraryScheme`.

```lean
theorem minus_and_isConstructible_etaleModuleSheafDerivedTensor (X : B.Scheme)
    (K L : DerivedCategory.Minus (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) w} Λ)))
    (hK : IsConstructible B X Λ K.obj) (hL : IsConstructible B X Λ L.obj) :
    (DerivedCategory.TStructure.t (C := Sheaf (SmallEtale.topology B X.obj X.property)
        (ModuleCat.{max (u + 1) w} Λ))).minus
        (((etaleModuleSheafDerivedTensor B X Λ).obj K.obj).obj L.obj) ∧
      IsConstructible B X Λ (((etaleModuleSheafDerivedTensor B X Λ).obj K.obj).obj L.obj)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.76, Tag 095V](https://stacks.math.columbia.edu/tag/095V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
