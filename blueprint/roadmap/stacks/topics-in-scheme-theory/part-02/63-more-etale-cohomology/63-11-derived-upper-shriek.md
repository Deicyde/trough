---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.DerivedUpperShriek.isLeftAdjoint_derivedLowerShriek, Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.isLeftAdjoint_derivedLowerShriek, Stacks.EtaleCohomology.isLeftAdjoint_derivedLowerShriekUnbounded_of_compactification, AlgebraicGeometry.SmallEtale.exists_compactification_rightAdjointIso_moduleRUpperShriekFunctor, AlgebraicGeometry.SmallEtale.exists_compactification_rightAdjointIso_pullbackMod_mapDerivedCategory, Stacks.EtaleCohomology.DerivedUpperShriek.exists_isZero_homology_derivedUpperShriek_obj, Stacks.EtaleCohomology.derivedUpperShriekUnboundedSheafyTrace, Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.sheafyTrace
statement: formalized
proof: formalized
---

# 63.11 Derived upper shriek

Section 63.11 of the Stacks Project, [Tag 0G2B](https://stacks.math.columbia.edu/tag/0G2B). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G2C, a lemma

[Tag 0G2C](https://stacks.math.columbia.edu/tag/0G2C) in the Stacks Project.

**`Stacks.EtaleCohomology.DerivedUpperShriek.isLeftAdjoint_derivedLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistence.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistence.lean#L83). The attribute's comment: “Rf_! = Rf̄_*j_!, with its commutation with direct sums (Tag 0G29) assumed”.

> Let `Λ` be a coefficient ring, let `A` be the Grothendieck abelian category of sheaves of
> `Λ`-modules on `X_étale`, and let `Rf_! = Rf̄_* ∘ j_!` be the derived lower shriek of a
> compactification `f = f̄ ∘ j`, with `j_!` and `Rf̄_*` exact. If `Rf_!` commutes with direct sums —
> which is [Stacks, Tag 0G29] when `f` is a separated finite-type morphism of quasi-compact
> quasi-separated schemes and `Λ` is torsion — then `Rf_!` has a right adjoint
> `Rf^! : D(Y_étale, Λ) ⟶ D(X_étale, Λ)`.

```lean
theorem isLeftAdjoint_derivedLowerShriek : (shriek ⋙ pushforwardFbar).IsLeftAdjoint
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.isLeftAdjoint_derivedLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistence.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistence.lean#L117). The attribute's comment: “for a CompactificationData; the commutation with direct sums (Tag 0G29) assumed”.

> The functor `Rf_! = Rf̄_* ∘ j_!` read off a `CompactificationData` has a right adjoint as soon
> as it commutes with direct sums, which is [Stacks, Tag 0G29].

```lean
theorem isLeftAdjoint_derivedLowerShriek
    (data : CompactificationData (DerivedCategory A) DX DY)
    [data.shriek.CommShift ℤ] [data.shriek.IsTriangulated]
    [data.pushforwardFbar.CommShift ℤ] [data.pushforwardFbar.IsTriangulated]
    [∀ J : Type (max w u v),
      PreservesColimitsOfShape (Discrete J) data.derivedLowerShriek] :
    data.derivedLowerShriek.IsLeftAdjoint
```

**`Stacks.EtaleCohomology.isLeftAdjoint_derivedLowerShriekUnbounded_of_compactification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistenceUnbounded.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/AdjointExistenceUnbounded.lean#L220). The attribute's comment: “Rf_! = Rf̄_* ∘ Rj_! on D(X_étale, Λ), Λ a torsion ring in any universe, for every compactification”. References: SGA 4 XVII (3.2.6), “(i), special case”.

> **[Stacks, Tag 0G2C].** Let `f : X ⟶ Y` be a finite type separated morphism of quasi-compact
> and quasi-separated schemes and let `Λ` be a torsion ring, in any universe. The functor
> `Rf_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` has a right adjoint
> `Rf^! : D(Y_étale, Λ) ⟶ D(X_étale, Λ)`.
>
> Here `Rf_!` is `Rf̄_* ∘ Rj_!` for a compactification `f = f̄ ∘ j`, as in [Stacks, Tag 0F7H]: such
> a compactification exists ([Stacks, Tag 0F41]), and for every one of them `Rf_!` is a left
> adjoint.

```lean
theorem isLeftAdjoint_derivedLowerShriekUnbounded_of_compactification (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] [CompactSpace Y]
    [QuasiSeparatedSpace Y] (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      ∀ j : CompactificationOf (Over.mk f),
        (derivedLowerShriekUnbounded.{u, r} f j Λ).IsLeftAdjoint
```

## Tag 0GL8, a lemma

[Tag 0GL8](https://stacks.math.columbia.edu/tag/0GL8) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.exists_compactification_rightAdjointIso_moduleRUpperShriekFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/RUpperShriekCompactification.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/RUpperShriekCompactification.lean#L174). The attribute's comment: “Rf^! of Tag 0G2C is the Rf^! of Tag 0F5N, for every right adjoint of Rf_!”. References: EGA IV (18.12.13), “special case”.

> **[Stacks, Tag 0GL8].** Let `f : X ⟶ Y` be a separated quasi-finite morphism of a big
> étale site with `Y` quasi-compact and quasi-separated, and let `Λ` be a ring. Then `f` factors
> as an open immersion `j : X ⟶ X̄` followed by a finite morphism `f̄ : X̄ ⟶ Y` (Zariski's main
> theorem, [Stacks, Tag 05K0]), and for every model of `D(X̄_étale, Λ)` and every total right
> derived functor `Rf̄_*` of `f̄_*`, the derived lower shriek `Rf_! = Rf̄_* ∘ j_!` of
> [Stacks, Tag 0G2C] has a right adjoint, and every right adjoint `Rf^!` of it is isomorphic to
> the derived upper shriek `Rf^! : D(Y_étale, Λ) ⥤ D(X_étale, Λ)` of [Stacks, Tag 0F5N].
>
> Quasi-finiteness is [Stacks, Tag 02NG]: locally quasi-finite, locally of finite type and
> quasi-compact together. The compactification is produced, not assumed.

```lean
theorem exists_compactification_rightAdjointIso_moduleRUpperShriekFunctor
    (B : BigEtaleSite.{u}) (Λ : Type u) [Ring Λ] {X Y : B.Scheme} (f : X ⟶ Y)
    [IsSeparated (B.inclusion.map f)] [LocallyQuasiFinite (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map f)] [QuasiCompact (B.inclusion.map f)]
    [CompactSpace Y.obj] [QuasiSeparatedSpace Y.obj]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y Λ)] :
    ∃ (Xbar : B.Scheme) (j : X ⟶ Xbar) (fbar : Xbar ⟶ Y)
      (_ : IsOpenImmersion (B.inclusion.map j)) (_ : IsFinite (B.inclusion.map fbar)),
      f = j ≫ fbar ∧
      ∀ [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Xbar Λ)]
        (RFbar : DerivedCategory (ModuleSheaf.{u, u, u} B Xbar Λ) ⥤
          DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ))
        (α : (etalePushforwardMod B Λ fbar).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RFbar),
        RFbar.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Xbar Λ) (ComplexShape.up ℤ)) →
        ((fShriekMod.{u, u, u} B Λ j).mapDerivedCategory ⋙ RFbar).IsLeftAdjoint ∧
        ∀ (G : DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ) ⥤
            DerivedCategory (ModuleSheaf.{u, u, u} B X Λ)),
          ((fShriekMod.{u, u, u} B Λ j).mapDerivedCategory ⋙ RFbar ⊣ G) →
          Nonempty (G ≅ moduleRUpperShriekFunctor.{u, u, w, u} B Λ f)
```

## Tag 0GL9, a lemma

[Tag 0GL9](https://stacks.math.columbia.edu/tag/0GL9) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.exists_compactification_rightAdjointIso_pullbackMod_mapDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/EtaleRUpperShriekPullback.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/EtaleRUpperShriekPullback.lean#L147). The attribute's comment: “Rj^! of Tag 0G2C is j^{-1}, for every right adjoint of Rj_!”. References: EGA IV (18.12.13), “special case”.

> **[Stacks, Tag 0GL9].** Let `j : U ⟶ X` be a separated étale morphism of a big étale site
> with `U` quasi-compact and `X` quasi-compact and quasi-separated, and let `Λ` be a ring. Then
> `j` factors as an open immersion `j' : U ⟶ X̄` followed by a finite morphism `j̄ : X̄ ⟶ X`
> (Zariski's main theorem), and for every model of `D(X̄_étale, Λ)` and every total right derived
> functor `Rj̄_*` of `j̄_*`, the derived lower shriek `Rj_! = Rj̄_* ∘ j'_!` of [Stacks, Tag 0G2C]
> has a right adjoint, and every right adjoint `Rj^!` of it is isomorphic to the inverse image
> `j^{-1} : D(X_étale, Λ) ⥤ D(U_étale, Λ)`.
>
> The compactification is produced, not assumed.

```lean
theorem exists_compactification_rightAdjointIso_pullbackMod_mapDerivedCategory
    (B : BigEtaleSite.{u}) (Λ : Type u) [Ring Λ] {U X : B.Scheme} (j : U ⟶ X)
    [IsSeparated (B.inclusion.map j)] [Etale (B.inclusion.map j)]
    [CompactSpace U.obj] [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B U Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)] :
    ∃ (Xbar : B.Scheme) (j' : U ⟶ Xbar) (fbar : Xbar ⟶ X)
      (_ : IsOpenImmersion (B.inclusion.map j')) (_ : IsFinite (B.inclusion.map fbar)),
      j = j' ≫ fbar ∧
      ∀ [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Xbar Λ)]
        (RFbar : DerivedCategory (ModuleSheaf.{u, u, u} B Xbar Λ) ⥤
          DerivedCategory (ModuleSheaf.{u, u, u} B X Λ))
        (α : (etalePushforwardMod B Λ fbar).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
          DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RFbar),
        RFbar.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Xbar Λ) (ComplexShape.up ℤ)) →
        ((fShriekMod.{u, u, u} B Λ j').mapDerivedCategory ⋙ RFbar).IsLeftAdjoint ∧
        ∀ (G : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
            DerivedCategory (ModuleSheaf.{u, u, u} B U Λ)),
          ((fShriekMod.{u, u, u} B Λ j').mapDerivedCategory ⋙ RFbar ⊣ G) →
          Nonempty (G ≅ (pullbackMod.{u, u, u} B Λ j).mapDerivedCategory)
```

## Tag 0GLA, a lemma

[Tag 0GLA](https://stacks.math.columbia.edu/tag/0GLA) in the Stacks Project.

**`Stacks.EtaleCohomology.DerivedUpperShriek.exists_isZero_homology_derivedUpperShriek_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/UpperShriekExistence.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/UpperShriekExistence.lean#L95).

> Let `f : X ⟶ Y` be a separated morphism of finite type between quasi-compact and
> quasi-separated schemes, let `j` be a compactification of `f`, and let `Λ` be a torsion ring
> (`n = 0` in `Λ` for some `n ≥ 1`). The functor `Rf^!`, the right adjoint of
> `Rf_! = R(fbar)_* ∘ j_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)` of [Stacks, Tag 0G2C], sends
> `D^+(Y_étale, Λ)` into `D^+(X_étale, Λ)`. More precisely, there is an integer `N ≥ 0` such that
> if `K ∈ D(Y_étale, Λ)` has `H^i(K) = 0` for `i < a`, then `H^i(Rf^!K) = 0` for `i < a - N`.

```lean
theorem exists_isZero_homology_derivedUpperShriek_obj {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    (j : CompactificationOf (Over.mk f)) :
    letI := isLeftAdjoint_derivedLowerShriekUnbounded Λ n hn hΛ f j
    (∀ K : DerivedCategory (EtaleModules.{u, 0} Λ Y),
      (∃ a : ℤ, ∀ i < a, IsZero ((DerivedCategory.homologyFunctor _ i).obj K)) →
      ∃ b : ℤ, ∀ i < b, IsZero ((DerivedCategory.homologyFunctor _ i).obj
        ((derivedLowerShriekUnbounded.{u, 0} f j Λ).rightAdjoint.obj K))) ∧
    ∃ N : ℕ, ∀ (K : DerivedCategory (EtaleModules.{u, 0} Λ Y)) (a : ℤ),
      (∀ i < a, IsZero ((DerivedCategory.homologyFunctor _ i).obj K)) →
      ∀ i < a - N, IsZero ((DerivedCategory.homologyFunctor _ i).obj
        ((derivedLowerShriekUnbounded.{u, 0} f j Λ).rightAdjoint.obj K))
```

## Tag 0GLB, an equation

[Tag 0GLB](https://stacks.math.columbia.edu/tag/0GLB) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedUpperShriekUnboundedSheafyTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/EtaleSheafyTrace.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/EtaleSheafyTrace.lean#L221).

> Let `Λ` be a torsion ring and let `f : X ⟶ Y` be a morphism of schemes with a
> compactification `f = f̄ ∘ j`, so that `Rf_! = Rf̄_* ∘ Rj_! : D(X_étale, Λ) ⟶ D(Y_étale, Λ)`
> has the right adjoint `Rf^!` of [Stacks, Tag 0G2C]. For every `K` in `D(Y_étale, Λ)` and `L` in
> `D(X_étale, Λ)` this is the canonical map
>
> `Rf_*RHom_Λ(L, Rf^!K) ⟶ RHom_Λ(Rf_!L, K)`,
>
> the composite `Rf_*RHom_Λ(L, Rf^!K) ⟶ RHom_Λ(Rf_!L, Rf_!Rf^!K) ⟶ RHom_Λ(Rf_!L, K)` of the map of
> [Stacks, Tag 0GL7] and the counit `Rf_!Rf^!K ⟶ K` of the adjunction
> (`Stacks.EtaleCohomology.derivedUpperShriekUnboundedSheafyTrace_eq`).
>
> A compactification exists when `f` is separated of finite type between quasi-compact and
> quasi-separated schemes, [Stacks, Tag 0F41].

```lean
def derivedUpperShriekUnboundedSheafyTrace
    (L : letI := HasDerivedCategory.standard (EtaleModules.{u, r} Λ X)
      DerivedCategory (EtaleModules.{u, r} Λ X))
    (K : letI := HasDerivedCategory.standard (EtaleModules.{u, r} Λ Y)
      DerivedCategory (EtaleModules.{u, r} Λ Y)) :
    letI := HasDerivedCategory.standard (EtaleModules.{u, r} Λ X)
    letI := HasDerivedCategory.standard (EtaleModules.{u, r} Λ Y)
    (etaleModuleDerivedDirectImageUnbounded.{u, r} Λ f).obj
        (((etaleDerivedHom.{u, r} Λ X).obj (op L)).obj
          ((derivedUpperShriekUnbounded.{u, r} Λ j hΛ).obj K)) ⟶
      ((etaleDerivedHom.{u, r} Λ Y).obj (op ((derivedLowerShriekUnbounded.{u, r} f j Λ).obj L))).obj
        K
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.sheafyTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean#L74). The attribute's comment: “the map, for a chosen compactification and a chosen adjunction Rf_! ⊣ Rf^!”.

> The sheafy trace map
>
> `Rf_*RHom_Λ(L, Rf^!K) ⟶ RHom_Λ(Rf_!L, K)`,
>
> the composite of the canonical map `α` of [Stacks, Tag 0GL7] at `(L, Rf^!K)` with the internal
> Hom of the counit `Rf_!Rf^!K ⟶ K` of the adjunction `Rf_! ⊣ Rf^!`.

```lean
def sheafyTrace (L : DU) (K : DY) :
    data.derivedPushforward.obj ((data.homU.obj (op L)).obj (upperShriek.obj K)) ⟶
      (data.homY.obj (op (data.derivedLowerShriek.obj L))).obj K
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.sheafyTrace_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean#L83). The attribute's comment: “the defining composite through RHom(Rf_!L, Rf_!Rf^!K)”.

> The sheafy trace map is the canonical map of [Stacks, Tag 0GL7] followed by the internal Hom
> of the counit of `Rf_! ⊣ Rf^!`.

```lean
theorem sheafyTrace_eq (L : DU) (K : DY) :
    sheafyTrace data adj L K =
      data.lowerShriekHomMap L (upperShriek.obj K) ≫
        (data.homY.obj (op (data.derivedLowerShriek.obj L))).map (adj.counit.app K)
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.sheafyTrace_naturality_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean#L91). The attribute's comment: “functoriality in K”.

> The sheafy trace map is natural in `K`.

```lean
theorem sheafyTrace_naturality_target (L : DU) {K K' : DY} (k : K ⟶ K') :
    data.derivedPushforward.map ((data.homU.obj (op L)).map (upperShriek.map k)) ≫
        sheafyTrace data adj L K' =
      sheafyTrace data adj L K ≫
        (data.homY.obj (op (data.derivedLowerShriek.obj L))).map k
```

**`Stacks.EtaleCohomology.DerivedUpperShriek.CompactificationData.sheafyTrace_naturality_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTrace.lean#L104). The attribute's comment: “functoriality in L”.

> The sheafy trace map is natural in `L`, contravariantly.

```lean
theorem sheafyTrace_naturality_source {L L' : DU} (l : L' ⟶ L) (K : DY) :
    data.derivedPushforward.map ((data.homU.map l.op).app (upperShriek.obj K)) ≫
        sheafyTrace data adj L' K =
      sheafyTrace data adj L K ≫
        (data.homY.map (data.derivedLowerShriek.map l).op).app K
```

## Tag 0GLC, a lemma

[Tag 0GLC](https://stacks.math.columbia.edu/tag/0GLC) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_derivedUpperShriekUnboundedSheafyTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTraceIsIso.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/SheafyTraceIsIso.lean#L74). References: SGA 7 XIII (2.1.6), “more general”.

> **[Stacks, Tag 0GLC].** Let `f : X ⟶ Y` be a separated finite type morphism of quasi-compact
> and quasi-separated schemes and let `Λ` be a torsion ring (`m = 0` in `Λ` for some `m ≥ 1`). Then
> `f` has a compactification `j : X ⟶ X̄` over `Y`, and for every compactification `j`, every
> `K ∈ D(Y_étale, Λ)` and every `L ∈ D(X_étale, Λ)` the map
> `Rf_*RHom_Λ(L, Rf^!K) ⟶ RHom_Λ(Rf_!L, K)` of [Stacks, Tag 0GLB], with `Rf_! = Rf̄_* ∘ j_!` and
> `Rf^!` its right adjoint of [Stacks, Tag 0G2C], is an isomorphism.

```lean
theorem isIso_derivedUpperShriekUnboundedSheafyTrace (Λ : Type) [CommRing Λ]
    (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) {X Y : Scheme.{u}} (f : X ⟶ Y)
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      ∀ (j : CompactificationOf (Over.mk f)) (K : DerivedCategory (EtaleModules.{u, 0} Λ Y))
        (L : DerivedCategory (EtaleModules.{u, 0} Λ X)),
        IsIso (derivedUpperShriekUnboundedSheafyTrace.{u, 0} f j hΛ L K)
```

## Tag 0GLD, a lemma

[Tag 0GLD](https://stacks.math.columbia.edu/tag/0GLD) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_derivedUpperShriekUnboundedGlobalTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/GlobalTrace.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/GlobalTrace.lean#L104). References: SGA 7 XIII (2.1.6), “more general”.

> **[Stacks, Tag 0GLD].** Let `f : X ⟶ Y` be a separated finite type morphism of quasi-compact
> and quasi-separated schemes and let `Λ` be a torsion ring (`m = 0` in `Λ` for some `m ≥ 1`). Then
> `f` has a compactification `j : X ⟶ X̄` over `Y`, and for every compactification `j`, every
> `K ∈ D(Y_étale, Λ)` and every `L ∈ D(X_étale, Λ)` the map of [Stacks, Tag 0GLB] induces an
> isomorphism `RHom_X(L, Rf^!K) ⟶ RHom_Y(Rf_!L, K)` of global derived homs
> `RHom_X(-, -) = RΓ(X, RHom_Λ(-, -))` ([Stacks, Tag 0B6E]), with `Rf_! = Rf̄_* ∘ j_!` and `Rf^!`
> its right adjoint of [Stacks, Tag 0G2C].

```lean
theorem isIso_derivedUpperShriekUnboundedGlobalTrace (Λ : Type) [CommRing Λ]
    (hΛ : ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) {X Y : Scheme.{u}} (f : X ⟶ Y)
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    (∃ j : CompactificationOf (Over.mk f), QuasiCompact j.immersion) ∧
      ∀ (j : CompactificationOf (Over.mk f)) (K : DerivedCategory (EtaleModules.{u, 0} Λ Y))
        (L : DerivedCategory (EtaleModules.{u, 0} Λ X)),
        IsIso (derivedUpperShriekUnboundedGlobalTrace.{u, 0} f j hΛ L K)
```

## Tag 0GLE, a lemma

[Tag 0GLE](https://stacks.math.columbia.edu/tag/0GLE) in the Stacks Project.

**`Stacks.EtaleCohomology.derivedUpperShriekBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek.lean#L114).

> **Stacks Project, Tag 0GLE.** Let
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
> be a cartesian square of schemes, let `Λ` be a ring, and let `j`, `j'` be compactifications of
> `f`, `f'`.  Let `Uf`, `Uf'` be right adjoints of `Rf_!`, `Rf'_!` and let `Pg`, `Pg'` be left
> adjoints of `Rg_*`, `Rg'_*`.  Given the base change isomorphism
> `Rf_! ⋙ Pg ≅ Pg' ⋙ Rf'_!` of Stacks Tag 0F7L for derived lower shriek, the derived upper
> shrieks satisfy `Rf^! ∘ Rg_* ≅ Rg'_* ∘ R(f')^!`.
>
> Both sides of the conclusion are right adjoint to `Rf_! ⋙ Pg`, so the isomorphism is the
> uniqueness of right adjoints applied to the given base change isomorphism of the left
> adjoints.

```lean
def derivedUpperShriekBaseChange {X' X Y' Y : Scheme.{u}}
    (g' : X' ⟶ X) {f' : X' ⟶ Y'} {f : X ⟶ Y} (g : Y' ⟶ Y)
    (_sq : IsPullback g' f' f g)
    (j : CompactificationOf (Over.mk f)) (j' : CompactificationOf (Over.mk f'))
    (Λ : Type r) [Ring Λ]
    {Uf : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ X)}
    (adjF : derivedLowerShriek.{u, r} f j Λ ⊣ Uf)
    {Uf' : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y') ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ X')}
    (adjF' : derivedLowerShriek.{u, r} f' j' Λ ⊣ Uf')
    {Pg : DerivedCategory.Plus (EtaleModules.{u, r} Λ Y) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ Y')}
    (adjG : Pg ⊣ etaleModuleDerivedDirectImage.{u, r} Λ g)
    {Pg' : DerivedCategory.Plus (EtaleModules.{u, r} Λ X) ⥤
      DerivedCategory.Plus (EtaleModules.{u, r} Λ X')}
    (adjG' : Pg' ⊣ etaleModuleDerivedDirectImage.{u, r} Λ g')
    (baseChange : derivedLowerShriek.{u, r} f j Λ ⋙ Pg ≅
      Pg' ⋙ derivedLowerShriek.{u, r} f' j' Λ) :
    etaleModuleDerivedDirectImage.{u, r} Λ g ⋙ Uf ≅
      Uf' ⋙ etaleModuleDerivedDirectImage.{u, r} Λ g'
```

**`Stacks.EtaleCohomology.derivedUpperShriekUnboundedBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/UnboundedProperBaseChange.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/DerivedUpperShriek/UnboundedProperBaseChange.lean#L91).

> **Stacks Project, Tag 0GLE.** Consider a cartesian square
> ```
> X' --g'--> X
> |f'        |f
> v          v
> Y' --g---> Y
> ```
> of quasi-compact and quasi-separated schemes with `f` separated and of finite type, and let `Λ`
> be a torsion ring (`n = 0` in `Λ` for some `n ≥ 1`). Let `Rf^!` and `R(f')^!` be the right
> adjoints ([Stacks, Tag 0G2C]) of the derived lower shrieks `Rf_! : D(X_étale, Λ) ⥤ D(Y_étale, Λ)`
> and `Rf'_! : D(X'_étale, Λ) ⥤ D(Y'_étale, Λ)` of arbitrary compactifications `j` of `f` and `j'`
> of `f'`. Then `Rf^! ∘ Rg_* ≅ Rg'_* ∘ R(f')^!` as functors `D(Y'_étale, Λ) ⥤ D(X_étale, Λ)`.

```lean
def derivedUpperShriekUnboundedBaseChange :
    letI := DerivedUpperShriek.isLeftAdjoint_derivedLowerShriekUnbounded Λ n hn hΛ f j
    letI := DerivedUpperShriek.isLeftAdjoint_derivedLowerShriekUnbounded Λ n hn hΛ f' j'
    etaleModuleDerivedDirectImageUnbounded.{u, 0} Λ g ⋙
        (derivedLowerShriekUnbounded.{u, 0} f j Λ).rightAdjoint ≅
      (derivedLowerShriekUnbounded.{u, 0} f' j' Λ).rightAdjoint ⋙
        etaleModuleDerivedDirectImageUnbounded.{u, 0} Λ g'
```

## Tag 0GLF, a remark

[Tag 0GLF](https://stacks.math.columbia.edu/tag/0GLF) in the Stacks Project.

**`Stacks.EtaleCohomology.ChangeOfRings.upperShriek_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ChangeOfRings/UpperShriekRestrictScalars.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ChangeOfRings/UpperShriekRestrictScalars.lean#L69).

> **[Stacks, Tag 0GLF].** Let `φ : Λ₁ ⟶ Λ₂` be a homomorphism of torsion rings (`n = 0` in
> `Λ₁` for some `n ≥ 1`, hence also in `Λ₂`) and let `f : X ⟶ Y` be a separated morphism of finite
> type between quasi-compact and quasi-separated schemes. Then `f` has a compactification
> ([Stacks, Tag 0F41]), and for every compactification `j`, with `Rf_! = R(fbar)_* ∘ j_!` and `Rf^!`
> its right adjoint over `Λ₁` and over `Λ₂` ([Stacks, Tag 0G2C]),
>
> `res ∘ Rf^! ≅ Rf^! ∘ res : D(Y_étale, Λ₂) ⥤ D(X_étale, Λ₁)`,
>
> `res` being restriction of scalars along `φ`.

```lean
theorem upperShriek_restrictScalars (n : ℕ) (hn : 0 < n) (hΛ₁ : (n : Λ₁) = 0)
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f]
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y] :
    Nonempty (CompactificationOf (Over.mk f)) ∧
      ∀ j : CompactificationOf (Over.mk f),
        letI := DerivedUpperShriek.isLeftAdjoint_derivedLowerShriekUnbounded Λ₁ n hn hΛ₁ f j
        letI := DerivedUpperShriek.isLeftAdjoint_derivedLowerShriekUnbounded Λ₂ n hn
          (natCast_eq_zero_of_ringHom φ hΛ₁) f j
        Nonempty ((derivedLowerShriekUnbounded.{u, 0} f j Λ₂).rightAdjoint ⋙
            derivedRestrictScalars.{u, 0} φ X ≅
          derivedRestrictScalars.{u, 0} φ Y ⋙
            (derivedLowerShriekUnbounded.{u, 0} f j Λ₁).rightAdjoint)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.11, Tag 0G2B](https://stacks.math.columbia.edu/tag/0G2B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
