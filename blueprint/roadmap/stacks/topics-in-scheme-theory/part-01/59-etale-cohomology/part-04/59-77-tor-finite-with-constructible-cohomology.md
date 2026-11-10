---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.CanonicalConstructibleFiniteTorDerivedCategory, Stacks.EtaleCohomology.ConstructibleFiniteTorDerivedCategory, Stacks.EtaleCohomology.exists_constructibleFiniteTor_iff_isRepresentedByConstructibleFlatComplex, Stacks.EtaleCohomology.exists_constructibleFlat_representative_of_hasTorAmplitude, Stacks.EtaleCohomology.isConstructible_of_isRepresentedByConstructibleFlatComplex, Stacks.EtaleCohomology.isConstructibleFiniteTor_iff_isRepresentedByFlatConstructibleComplex, Stacks.EtaleCohomology.locallyHasFiniteTorDimension_of_isRepresentedByConstructibleFlatComplex, Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryOfConstructibleFlatComplex
statement: formalized
proof: formalized
---

# 59.77 Tor finite with constructible cohomology

Section 59.77 of the Stacks Project, [Tag 0F4M](https://stacks.math.columbia.edu/tag/0F4M). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03TQ, a definition

[Tag 03TQ](https://stacks.math.columbia.edu/tag/03TQ) in the Stacks Project.

**`Stacks.EtaleCohomology.CanonicalConstructibleFiniteTorDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/CanonicalFiniteTorDimension.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/CanonicalFiniteTorDimension.lean#L135). The attribute's comment: “the derived tensor products on the slices of the constant-coefficient étale ringed site are constructed here, by Stacks 06YU at free universes, so no derived tensor product is assumed”. References: SGA 5 III (1.1), “D_ctf(X) definition”; SGA 4½ Rapport (4.6), “ii)”; SGA 5 IIIB (6.1), “D_ctf(-)”; SGA 4½ Th finitude (1.7).

> **Stacks 03TQ.** The category `D_{ctf}(X_étale, Λ)`: the full subcategory of the
> constructible derived category of Stacks 095W consisting of the objects whose image in the
> derived category of modules over the constant coefficient ring sheaf has locally finite Tor
> dimension in the sense of Stacks 08FZ.
>
> Tor dimension is measured against the derived tensor products
> `Stacks.EtaleCohomology.canonicalSliceDerivedTensorProduct` of Stacks 06YU on the slices of that
> ringed site.

```lean
abbrev CanonicalConstructibleFiniteTorDerivedCategory
```

**`Stacks.EtaleCohomology.ConstructibleFiniteTorDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/FiniteTorDimension.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/FiniteTorDimension.lean#L106). References: SGA 5 III (1.1), “D_ctf(X) definition”; SGA 4½ Rapport (4.6), “ii)”; SGA 5 IIIB (6.1), “D_ctf(-)”.

> **Stacks 03TQ.** The category `D_{ctf}(X_étale, Λ)`: the full subcategory of the
> constructible derived category of Stacks 095W consisting of the objects whose image in the
> derived category of modules over the constant coefficient ring sheaf has locally finite Tor
> dimension in the sense of Stacks 08FZ, measured against the derived tensor products `T` on the
> slices of that ringed site.

```lean
abbrev ConstructibleFiniteTorDerivedCategory
    (T : ∀ U : (constantCoefficientRingedSite.{u, w, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) w r, d}
        ((constantCoefficientRingedSite.{u, w, r} B X Λ).over U))
```

## Tag 03TT, a lemma

[Tag 03TT](https://stacks.math.columbia.edu/tag/03TT) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_constructibleFiniteTor_iff_isRepresentedByConstructibleFlatComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFiniteTorRepresentation.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFiniteTorRepresentation.lean#L556). The attribute's comment: “the equivalence of (1) and (2)”. References: SGA 4½ Rapport (4.6), “special case”.

> Let `Λ` be a Noetherian ring and `X` a quasi-compact and quasi-separated
> scheme. An object `K` of `D(X_étale, Λ)` lies in `D_ctf(X_étale, Λ)` (Tag 03TQ) if and only if it
> can be represented by a finite complex of constructible flat sheaves of `Λ`-modules.
>
> `D_ctf(X_étale, Λ)` is the category of Tag 03TQ, measured against the given derived tensor
> products `T` on the slices; membership of `K` is the existence of an object of that category
> isomorphic to `K`.

```lean
public theorem exists_constructibleFiniteTor_iff_isRepresentedByConstructibleFlatComplex
    (T : ∀ U : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).over U))
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ))) :
    (∃ L : ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) r, r, d} B X Λ T,
        Nonempty (L.obj.obj ≅ K)) ↔
      IsRepresentedByConstructibleFlatComplex.{u, max (u + 1) r, r} B X Λ K
```

**`Stacks.EtaleCohomology.exists_constructibleFlat_representative_of_hasTorAmplitude`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFiniteTorRepresentation.lean, line 682](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFiniteTorRepresentation.lean#L682). The attribute's comment: “the last sentence: Tor amplitude in [a, b] gives a representative F^a → ⋯ → F^b by constructible flat sheaves”.

> Let `Λ` be a Noetherian ring and `X` a quasi-compact and
> quasi-separated scheme. If `K ∈ D_ctf(X_étale, Λ)` has Tor amplitude in `[a, b]`, then `K` can be
> represented by a complex `F^a → ⋯ → F^b` of constructible flat sheaves of `Λ`-modules.
>
> Tor amplitude is that of the associated object of `D(𝒪)`, `𝒪` the constant coefficient ring
> sheaf, against a derived tensor product `T₀` on `𝒪` (Stacks 08FZ (1)); the hypothesis `hK` is
> the constructibility of the cohomology sheaves of `K`.

```lean
public theorem exists_constructibleFlat_representative_of_hasTorAmplitude
    (T₀ : Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
      (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ))
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsConstructible B X Λ K) (a b : ℤ)
    (hamp : HasTorAmplitude T₀
      ((moduleSheafOverConstantCoefficientsFunctor.{u, max (u + 1) r, r}
        B X Λ).mapDerivedCategory.obj K) a b) :
    ∃ F : CochainComplex
        (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)) ℤ,
      F.IsStrictlyGE a ∧ F.IsStrictlyLE b ∧
        (∀ i : ℤ, IsConstructibleFlatModuleSheaf B X Λ (F.X i)) ∧
        Nonempty (DerivedCategory.Q.obj F ≅ K)
```

**`Stacks.EtaleCohomology.isConstructible_of_isRepresentedByConstructibleFlatComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlat.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlat.lean#L275). The attribute's comment: “the direction (2) => (1), the constructible-cohomology half, from the weak Serre property `hSerre` of the constructible sheaves of modules”.

> **Tag 03TT, the direction (2) ⟹ (1) for the constructible-cohomology condition.** An
> object of `D(X_étale, Λ)` represented by a bounded complex of constructible flat sheaves of
> `Λ`-modules has constructible cohomology sheaves, so it lies in the constructible derived
> category of Tag 095W.
>
> The cohomology sheaf in degree `i` is a cokernel of a map from the term in degree `i - 1` into
> the sheaf of cycles, which is a kernel of a map between the terms in degrees `i` and `i + 1`;
> each term is constructible, and the hypothesis `hSerre` that the constructible sheaves of
> `Λ`-modules form a weak Serre subcategory of all sheaves of `Λ`-modules — Tag 0754, closure
> under kernels, cokernels, extensions and isomorphism — carries constructibility to the kernel
> and then to the cokernel.

```lean
public theorem isConstructible_of_isRepresentedByConstructibleFlatComplex
    (hSerre : (isConstructibleModuleSheafProperty.{u, w, r} B X Λ).IsWeakSerreClass)
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)))
    (hK : IsRepresentedByConstructibleFlatComplex.{u, w, r} B X Λ K) :
    IsConstructible B X Λ K
```

**`Stacks.EtaleCohomology.isConstructibleFiniteTor_iff_isRepresentedByFlatConstructibleComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlatCharacterization.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlatCharacterization.lean#L583). References: SGA 4½ Rapport (4.6), “special case”.

> **Stacks 03TT.** Let `Λ` be a Noetherian ring, let `X` be a quasi-compact and quasi-separated
> scheme and let `K ∈ D(X_étale, Λ)`. The following are equivalent:
>
> 1. `K ∈ D_ctf(X_étale, Λ)`, that is, `K` has constructible cohomology sheaves and the image of
>    `K` over the constant coefficient ringed site of Tag 03TR has locally finite Tor dimension in
>    the sense of Tag 08FZ;
> 2. `K` is represented by a finite complex of constructible flat sheaves of `Λ`-modules.
>
> In fact, if `K` has Tor amplitude in `[a, b]` then it can be represented by a complex
> `F^a → ⋯ → F^b` with each `F^p` a constructible flat sheaf of `Λ`-modules.
>
> Condition (1) is membership of
> `Stacks.EtaleCohomology.ConstructibleFiniteTorDerivedCategory`, whose defining property is
> exactly this conjunction; condition (2) is
> `Stacks.EtaleCohomology.IsRepresentedByFlatConstructibleComplex`.
>
> Condition (1) is stated **absolutely**: the derived tensor products against which finite Tor
> dimension and Tor amplitude are measured are not parameters of the statement but the canonical
> ones, `Stacks.SheafOfModules.canonicalDerivedTensorProduct` of Tag 06YU on the constant
> coefficient ringed site and on each of its slices. Those exist at the universes this chapter
> works in — the site is an `AlgebraicGeometry.RingedSite.{u + 1, u, max (u + 1) r}`, whose
> morphisms and whose sections lie in *different* universes — because the K-flat resolutions
> Tag 06YU is built from resolve by flat modules supplied by a flat cover and so relate none of
> the three universes of the site. The two directions and the refinement are proved above against
> an arbitrary datum, which is the more general statement; the tag is carried here, where the
> quantifier over the datum is gone and the equivalence is therefore not vacuous.

```lean
public theorem isConstructibleFiniteTor_iff_isRepresentedByFlatConstructibleComplex
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ))) :
    ((IsConstructible B X Λ K ∧
        Stacks.SheafOfModules.DerivedTensorProduct.LocallyHasFiniteTorDimension
          (X := constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ)
          (fun U => Stacks.SheafOfModules.canonicalDerivedTensorProductGeneral.{u + 1, u,
            max (u + 1) r, d}
            ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).over U))
          ((moduleSheafOverConstantCoefficientsFunctor.{u, max (u + 1) r,
            r} B X Λ).mapDerivedCategory.obj K)) ↔
      IsRepresentedByFlatConstructibleComplex.{u, r} B X Λ K) ∧
    ∀ a b : ℤ, a ≤ b → IsConstructible B X Λ K →
      Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitude
        (Stacks.SheafOfModules.canonicalDerivedTensorProductGeneral.{u + 1, u, max (u + 1) r, d}
          (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ))
        ((moduleSheafOverConstantCoefficientsFunctor.{u, max (u + 1) r,
          r} B X Λ).mapDerivedCategory.obj K) a b →
      ∃ F : CochainComplex (Sheaf (SmallEtale.topology B X.obj X.property)
          (ModuleCat.{max (u + 1) r} Λ)) ℤ,
        F.IsStrictlyGE a ∧ F.IsStrictlyLE b ∧
        (∀ i : ℤ, IsConstructibleModuleSheaf B X Λ (F.X i)) ∧
        (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u + 1, max (u + 1) r,
          max (u + 1) r} (O := (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).O)
          ((moduleSheafOverConstantCoefficientsFunctor.{u, max (u + 1) r,
            r} B X Λ).obj (F.X i))) ∧
        Nonempty (DerivedCategory.Q.obj F ≅ K)
```

**`Stacks.EtaleCohomology.locallyHasFiniteTorDimension_of_isRepresentedByConstructibleFlatComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlatFiniteTor.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlatFiniteTor.lean#L239). The attribute's comment: “the finite-tor-dimension half of the direction (2) => (1), at a free coefficient universe; the constructible-cohomology half of that direction is `Stacks.EtaleCohomology.isConstructible_of_isRepresentedByConstructibleFlatComplex` and the two are combined in `Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryOfConstructibleFlatComplex`”. References: SGA 4½ Rapport (4.6), “partial”.

> **Tag 03TT, the finite-Tor-dimension half of the direction (2) ⟹ (1).** An object of
> `D(X_étale, Λ)` represented by a bounded complex of constructible flat sheaves of `Λ`-modules
> has locally finite Tor dimension in the sense of Tag 08FZ, read on its image under the change of
> coefficients of Tag 03TR and measured against the derived tensor products `T` on the slices of
> the constant coefficient ringed site.
>
> Each term of the complex becomes a flat module over the constant coefficient ring sheaf, by
> `AlgebraicGeometry.isFlat_moduleSheafOverConstantCoefficients_of_isConstructibleFlatModuleSheaf`;
> the change of coefficients is exact, so applied degreewise it carries the complex to a
> representative of the image of `K`; and
> `Stacks.SheafOfModules.DerivedTensorProduct.FreeModuleUniverse.locallyHasFiniteTorDimension_of_flatRepresentative`
> reads Stacks 08G1 on every slice.

```lean
theorem locallyHasFiniteTorDimension_of_isRepresentedByConstructibleFlatComplex
    (T : ∀ U : (constantCoefficientRingedSite.{u, w, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) w r, d}
        ((constantCoefficientRingedSite.{u, w, r} B X Λ).over U))
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)))
    (hK : IsRepresentedByConstructibleFlatComplex.{u, w, r} B X Λ K) :
    Stacks.SheafOfModules.DerivedTensorProduct.LocallyHasFiniteTorDimension
      (X := constantCoefficientRingedSite.{u, w, r} B X Λ) T
      ((moduleSheafOverConstantCoefficientsFunctor.{u, w, r} B X Λ).mapDerivedCategory.obj K)
```

**`Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryOfConstructibleFlatComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlatFiniteTor.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ConstructibleFlatFiniteTor.lean#L320). The attribute's comment: “the direction (2) => (1), both halves, with the weak Serre property of the constructible sheaves of modules discharged by Tag 03RZ (3) at the coefficient universe max (u + 1) r. The direction (1) => (2) and the sharpened bound on the length of the representative are not proved”. References: SGA 4½ Rapport (4.6), “partial”.

> **Tag 03TT, the direction (2) ⟹ (1).** An object of `D(X_étale, Λ)` represented by a bounded
> complex of constructible flat sheaves of `Λ`-modules is an object of `D_{ctf}(X_étale, Λ)`: its
> cohomology sheaves are constructible and its image under the change of coefficients of Tag 03TR
> has locally finite Tor dimension.
>
> The two halves are
> `Stacks.EtaleCohomology.isConstructible_of_isRepresentedByConstructibleFlatComplex` and
> `Stacks.EtaleCohomology.locallyHasFiniteTorDimension_of_isRepresentedByConstructibleFlatComplex`.
> The weak Serre property of the constructible sheaves of modules, which the first of them asks
> for, is Tag 03RZ (3) at the coefficient universe `max (u + 1) r`; that is why the module sections
> are fixed there rather than left free, and it is why nothing is carried as a hypothesis.

```lean
def constructibleFiniteTorDerivedCategoryOfConstructibleFlatComplex
    (T : ∀ U : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).over U))
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsRepresentedByConstructibleFlatComplex.{u, max (u + 1) r, r} B X Λ K) :
    ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) r, r, d} B X Λ T
```

## Tag 03TR, a remark

[Tag 03TR](https://stacks.math.columbia.edu/tag/03TR) in the Stacks Project.

**`AlgebraicGeometry.stalk_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantCoefficients.lean, line 681](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantCoefficients.lean#L681). The attribute's comment: “finiteness in each degree”.

> Every term of the stalk at a geometric point of a complex of constructible sheaves of
> `Λ`-modules is a finite `Λ`-module.
>
> The constructibility hypothesis is spelled out as stratumwise local constancy with finitely
> generated values, which is what `AlgebraicGeometry.IsConstructibleModuleSheaf` — Tag 03RW part
> (3) — unfolds to; stating it this way is what makes the statement available for a coefficient
> ring that is not commutative, the definition of Tag 03RW being given for a Noetherian ring.

```lean
theorem stalk_finite
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous
        (ModuleCat.{w} Λ) (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) (ModuleCat.{w} Λ)]
    (K : CochainComplex
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)) ℤ)
    (hconstructible : ∀ i : ℤ,
      IsStratifiedLocallyConstantWith B X Λ (ModuleCat.isFG Λ) (K.X i))
    (s : GeometricPoint X.obj) (i : ℤ) :
    Module.Finite Λ ((etaleModuleStalkFunctor B X Λ s).obj (K.X i))
```

**`AlgebraicGeometry.stalk_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantCoefficients.lean, line 971](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantCoefficients.lean#L971). The attribute's comment: “projectivity in each degree”.

> Every term of the stalk at a geometric point of a complex of constructible sheaves of
> `Λ`-modules which are flat over the constant coefficient ring sheaf is a projective
> `Λ`-module.

```lean
theorem stalk_projective
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous
        (ModuleCat.{w} Λ) (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) (ModuleCat.{w} Λ)]
    (K : CochainComplex
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)) ℤ)
    (hconstructible : ∀ i : ℤ, IsConstructibleModuleSheaf B X Λ (K.X i))
    (hflat : ∀ i : ℤ, Stacks.SheafOfModules.IsFlat.{u, u + 1, max (u + 1) w r, max (u + 1) w r}
      (moduleSheafOverConstantCoefficients.{u, w, r} B X Λ (K.X i)))
    (s : GeometricPoint X.obj) (i : ℤ) :
    Module.Projective Λ ((etaleModuleStalkFunctor B X Λ s).obj (K.X i))
```

**`AlgebraicGeometry.stalk_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantCoefficients.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantCoefficients.lean#L992). The attribute's comment: “perfection of the stalk complex”.

> The stalk at a geometric point of a bounded complex of constructible sheaves of `Λ`-modules
> which are flat over the constant coefficient ring sheaf is a perfect object of the derived
> category of `Λ`-modules.

```lean
theorem stalk_isPerfect
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous
        (ModuleCat.{w} Λ) (SmallEtale.topology B S.obj S.property)
        (SmallEtale.topology B T.obj T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.obj T.property),
      HasWeakSheafify ((SmallEtale.topology B T.obj T.property).over V) (ModuleCat.{w} Λ)]
    (K : CochainComplex
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)) ℤ)
    (hbounded : (CochainComplex.plus _ K) ∧ (CochainComplex.minus _ K))
    (hconstructible : ∀ i : ℤ, IsConstructibleModuleSheaf B X Λ (K.X i))
    (hflat : ∀ i : ℤ, Stacks.SheafOfModules.IsFlat.{u, u + 1, max (u + 1) w r, max (u + 1) w r}
      (moduleSheafOverConstantCoefficients.{u, w, r} B X Λ (K.X i)))
    (s : GeometricPoint X.obj)
    [HasDerivedCategory (ModuleCat.{w} Λ)] :
    StacksDraft.Perfect.IsPerfect
      (DerivedCategory.Q.obj (etaleModuleStalkComplex B X Λ s K))
```

## Tag 0962, a lemma

[Tag 0962](https://stacks.math.columbia.edu/tag/0962) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleFiniteTor_derivedRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZeroMembership.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZeroMembership.lean#L231). The attribute's comment: “part (1): for K in D_ctf(X_et, Λ), the restriction K|_U — the image of K under the derived restriction functor of Tag 03S3 — satisfies membership of D_ctf(U_et, Λ)”.

> **Stacks 0962, part (1).** Let `Λ` be a Noetherian ring and let `j : U ⟶ X` be an étale
> morphism of schemes, the object `U` of the small étale site of `X`. If `K` lies in
> `D_ctf(X_étale, Λ)`, then its restriction `K|_U`, the image of `K` under the derived functor of
> the restriction functor of Tag 03S3, lies in `D_ctf(U_étale, Λ)`.
>
> This is `Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryRestriction`, whose output
> is `K|_U` by construction: constructibility by Tag 095X part (1), and locally finite Tor
> dimension by the finite-Tor-dimension half of Tag 0963 at the structure morphism of `U`,
> transported along Tag 03S3 part (3).

```lean
public theorem isConstructibleFiniteTor_derivedRestriction
    (T : ∀ V : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).over V))
    (T' : ∀ V : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B U.obj.left Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B U.obj.left Λ).over V))
    (K : DerivedCategory (Sheaf (SmallEtale.topology B X.obj X.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hK : IsConstructibleFiniteTor.{u, max (u + 1) r, r, d} B X Λ T K) :
    IsConstructibleFiniteTor.{u, max (u + 1) r, r, d} B U.obj.left Λ T'
      ((moduleRestriction.{u, r, max (u + 1) r} B X.obj X.property U Λ).mapDerivedCategory.obj
        K)
```

**`Stacks.EtaleCohomology.isConstructibleFiniteTor_derivedExtensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZeroMembership.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/RestrictionExtensionByZeroMembership.lean#L260). The attribute's comment: “part (2): for j quasi-compact and quasi-separated and M in D_ctf(U_et, Λ), the extension by zero j_! M — the image of M under the derived extension-by-zero functor of Tag 03S3 — satisfies membership of D_ctf(X_et, Λ)”.

> **Stacks 0962, part (2).** Let `Λ` be a Noetherian ring and let `j : U ⟶ X` be an étale
> morphism of schemes, the object `U` of the small étale site of `X`, which is quasi-compact and
> quasi-separated. If `M` lies in `D_ctf(U_étale, Λ)`, then its extension by zero `j_! M`, the
> image of `M` under the derived functor of the extension-by-zero functor of Tag 03S3, lies in
> `D_ctf(X_étale, Λ)`.
>
> This is `Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryExtensionByZero`, whose
> output is `j_! M` by construction: constructibility by Tag 095X part (2), and locally finite Tor
> dimension read at the stalks by Tag 03S5 and Tag 0DJJ.

```lean
public theorem isConstructibleFiniteTor_derivedExtensionByZero
    (hqc : QuasiCompact (B.inclusion.map U.obj.hom))
    (hqs : QuasiSeparated (B.inclusion.map U.obj.hom))
    (T : ∀ V : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).over V))
    (T' : ∀ V : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B U.obj.left Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B U.obj.left Λ).over V))
    (M : DerivedCategory (Sheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
      (ModuleCat.{max (u + 1) r} Λ)))
    (hM : IsConstructibleFiniteTor.{u, max (u + 1) r, r, d} B U.obj.left Λ T' M) :
    IsConstructibleFiniteTor.{u, max (u + 1) r, r, d} B X Λ T
      ((moduleExtensionByZero.{u, r} B X.obj X.property U Λ).mapDerivedCategory.obj M)
```

**`Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekFiniteTor.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/ShriekFiniteTor.lean#L479). The attribute's comment: “both parts, in the two components of the pair: part (1) with `K|_U` the restriction of Tag 03S3, part (2) with the quasi-compactness and quasi-separatedness of `j` as the premises of that component. The constructible-cohomology halves are the two parts of Tag 095X; the finite-Tor-dimension half of part (1) is that of Tag 0963 at the structure morphism of `U`, and that of part (2) is read at the stalks, by Tag 03S5 for sheaves of modules and Tag 0DJJ on the slices over affine objects, over which `U ×_X V'` is quasi-compact”.

> **Stacks 0962.** Let `Λ` be a Noetherian ring and let `j : U ⟶ X` be an étale morphism of
> schemes, that is an object `U` of the small étale site of `X`. Then
>
> 1. the restriction `K|_U` of an object `K` of `D_ctf(X_étale, Λ)` is an object of
>    `D_ctf(U_étale, Λ)`, and
> 2. the extension by zero `j_! M` of an object `M` of `D_ctf(U_étale, Λ)` is an object of
>    `D_ctf(X_étale, Λ)`, when `j` is quasi-compact and quasi-separated.
>
> The two clauses are the two components of the pair; the quasi-compactness and
> quasi-separatedness of `j`, which the source asks for in part (2) only, are hypotheses of the
> second component alone. The first component is
> `Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryRestriction` and the second
> `Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryExtensionByZero`.

```lean
public def constructibleFiniteTorDerivedCategoryEtale
    (T : ∀ V : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B X Λ).over V))
    (T' : ∀ V : (constantCoefficientRingedSite.{u, max (u + 1) r, r} B U.obj.left Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) r, r} B U.obj.left Λ).over V)) :
    (ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) r, r, d} B X Λ T →
        ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) r, r, d} B U.obj.left Λ T') ×
      (QuasiCompact (B.inclusion.map U.obj.hom) →
        QuasiSeparated (B.inclusion.map U.obj.hom) →
        ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) r, r, d} B U.obj.left Λ T' →
        ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) r, r, d} B X Λ T)
```

## Tag 0963, a lemma

[Tag 0963](https://stacks.math.columbia.edu/tag/0963) in the Stacks Project.

**`Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryPullback_unconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/PullbackFiniteTorStalkwise.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleComplexes/PullbackFiniteTorStalkwise.lean#L431). The attribute's comment: “the constructible-cohomology half by Tag 095Y, the finite-Tor-dimension half by Tag 0DJJ read at the stalks on the slices of the constant coefficient ringed sites”. References: SGA 5 III (1.2), “more general”; SGA 5 IIIB (6.2), “special case”.

> **Stacks 0963.** Let `Λ` be a Noetherian ring and `f : X ⟶ Y` a morphism of schemes. The
> derived inverse image of an object of `D_{ctf}(Y_étale, Λ)` is an object of
> `D_{ctf}(X_étale, Λ)`.
>
> Constructibility of the cohomology sheaves of `Lf^*K` is Tag 095Y, which is
> `Stacks.EtaleCohomology.constructibleDerivedCategoryPullback`. Locally finite Tor dimension of
> its image under the change of coefficients is
> `Stacks.EtaleCohomology.pullbackPreservesLocallyFiniteTorDimension`.
>
> `Stacks.EtaleCohomology.constructibleFiniteTorDerivedCategoryPullback` is the same statement
> taking the finite-Tor-dimension half as a hypothesis, which this one discharges.

```lean
public def constructibleFiniteTorDerivedCategoryPullback_unconditional
    (T : ∀ U : (constantCoefficientRingedSite.{u, max (u + 1) w, r} B Y Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) w r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) w, r} B Y Λ).over U))
    (T' : ∀ U : (constantCoefficientRingedSite.{u, max (u + 1) w, r} B X Λ).C,
      Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, max (u + 1) w r, d}
        ((constantCoefficientRingedSite.{u, max (u + 1) w, r} B X Λ).over U))
    (K : ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) w, r, d} B Y Λ T) :
    ConstructibleFiniteTorDerivedCategory.{u, max (u + 1) w, r, d} B X Λ T'
```

## Tag 09BI, a lemma

[Tag 09BI](https://stacks.math.columbia.edu/tag/09BI) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleCover_constantFiniteProjectiveComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantPerfectComplexEtale.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantPerfectComplexEtale.lean#L141).

> **Tag 09BI, with its finite-Tor-dimension input named at the points of the site.**
>
> Let `X` be a connected scheme in a big étale site and `Λ` a Noetherian ring. Let `K` be a bounded
> object of the derived category of sheaves of `Λ`-modules on the small étale site of `X` whose
> cohomology sheaves are locally constant of finite type, and suppose that at every point `q` of
> the site lifting to an object `V` the derived fibre of the restriction to the slice over `V` of a
> representative of `K` has a bounded flat representative over `Λ` — the finite-Tor-dimension half
> of membership in `D_{ctf}(X_{étale}, Λ)`. Then there is a single finite complex `E` of finite
> projective `Λ`-modules and an étale covering of `X` over every member of which `K` becomes the
> constant complex attached to `E`.

```lean
theorem exists_etaleCover_constantFiniteProjectiveComplex
    (K : DerivedCategory.Bounded
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)))
    (hK : ∀ n : ℤ, Stacks.ConstantSheaf.IsFiniteTypeLocallyConstantModuleSheaf.{u, u + 1, u, u}
      (SmallEtale.topology B X.obj X.property) Λ
      ((DerivedCategory.homologyFunctor
        (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)) n).obj K.obj))
    (hflat : ∀ (T : CochainComplex
        (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)) ℤ)
      (V : SmallEtale B X.obj X.property)
      (q : (SmallEtale.topology B X.obj X.property).Point.{u + 1}) (z : q.fiber.obj V),
      (K.obj ≅ DerivedCategory.Q.obj T) →
      ∃ c d : ℤ, StacksDraft.Perfect.HasFlatRepresentative.{u, u + 1}
        (((q.over z).sheafFiber (A := ModuleCat.{u + 1} Λ)).mapDerivedCategory.obj
          (DerivedCategory.Q.obj
            ((((SmallEtale.topology B X.obj X.property).overPullback
              (ModuleCat.{u + 1} Λ) V).mapHomologicalComplex (ComplexShape.up ℤ)).obj T))) c d) :
    ∃ (E : CochainComplex (ModuleCat.{u + 1} Λ) ℤ) (a b : ℤ)
      (T : CochainComplex
        (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)) ℤ)
      (_e : K.obj ≅ DerivedCategory.Q.obj T),
      E.IsStrictlyGE a ∧ E.IsStrictlyLE b ∧
      (∀ n : ℤ, Module.Finite Λ (E.X n)) ∧ (∀ n : ℤ, Module.Projective Λ (E.X n)) ∧
      ∃ (I : Type (u + 1)) (U : I → SmallEtale B X.obj X.property)
        (f : ∀ i, U i ⟶ SmallEtale.final B X.obj X.property),
        Sieve.ofArrows U f ∈ SmallEtale.topology B X.obj X.property
          (SmallEtale.final B X.obj X.property) ∧
        ∀ i, Nonempty (DerivedCategory.Q.obj
            ((((SmallEtale.topology B X.obj X.property).overPullback
              (ModuleCat.{u + 1} Λ) (U i)).mapHomologicalComplex (ComplexShape.up ℤ)).obj T) ≅
          DerivedCategory.Q.obj
            (((constantSheaf ((SmallEtale.topology B X.obj X.property).over (U i))
              (ModuleCat.{u + 1} Λ)).mapHomologicalComplex (ComplexShape.up ℤ)).obj E))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.77, Tag 0F4M](https://stacks.math.columbia.edu/tag/0F4M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
