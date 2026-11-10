---
declaration: section
origin: cited
lean: AlgebraicGeometry.isZero_cokernel_and_isConstructible_kernel_frobeniusSemilinear_sub_id, Stacks.EtaleCohomology.isConstructibleEtaleModule_rightDerivedConstantUnit_of_isProper_of_smooth, Stacks.EtaleCohomology.isConstructibleEtaleModule_rightDerived_constantSheaf_of_isProper_of_smooth
statement: formalized
proof: formalized
---

# 63.13 A constructibility result

Section 63.13 of the Stacks Project, [Tag 0GKT](https://stacks.math.columbia.edu/tag/0GKT). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GKU, a lemma

[Tag 0GKU](https://stacks.math.columbia.edu/tag/0GKU) in the Stacks Project.

**`AlgebraicGeometry.isZero_cokernel_and_isConstructible_kernel_frobeniusSemilinear_sub_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusKernelConstructible.lean, line 824](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ArtinSchreierSequence/FrobeniusKernelConstructible.lean#L824).

> Let `p` be a prime, let `S` be a scheme over `𝔽_p`, let `E` be a finite locally free module on
> the small étale site of `S` and let `F : E ⟶ E` be a morphism of abelian sheaves with
> `F (a • e) = a ^ p • F e` for local sections `a` of the structure sheaf and `e` of `E`. Then the
> cokernel of `F - 1` is zero and the kernel of `F - 1` is a constructible abelian sheaf.
>
> The kernel is read in the coefficient universe of the constructibility predicate, one above that
> of `E`, through the universe lift of abelian groups.

```lean
theorem isZero_cokernel_and_isConstructible_kernel_frobeniusSemilinear_sub_id
    (p : ℕ) [Fact p.Prime] (S : Scheme.{u}) (hS : B.Contains S)
    (E : SheafOfModules.{u} (SmallEtale.structureSheaf B S hS))
    [SheafOfModules.IsFiniteLocallyFree E]
    (hchar : IsInCharacteristic S p)
    (F : ((SheafOfModules.toSheaf (SmallEtale.structureSheaf B S hS)).obj E) ⟶
      ((SheafOfModules.toSheaf (SmallEtale.structureSheaf B S hS)).obj E))
    (hF : ∀ (U : SmallEtale B S hS)
      (a : (SmallEtale.structureSheaf B S hS).obj.obj (op U))
      (e : E.val.obj (op U)),
      SheafOfModules.sectionsAddHom F (op U) (a • e) =
        a ^ p • SheafOfModules.sectionsAddHom F (op U) e) :
    IsZero (cokernel (F - 𝟙 _)) ∧
      IsConstructibleAbelianSheaf B (B.obj S hS)
        ((sheafCompose (SmallEtale.topology B S hS) AddCommGrpCat.uliftFunctor.{u + 1, u}).obj
          (kernel (F - 𝟙 _)))
```

## Tag 0GKV, a lemma

[Tag 0GKV](https://stacks.math.columbia.edu/tag/0GKV) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_rightDerivedConstantUnit_of_isProper_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/ProperSmoothCurveHigherDirectImage.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/ProperSmoothCurveHigherDirectImage.lean#L63). References: SGA 4 XIV (1.11), “partial”.

> **Stacks Project, Tag 0GKV.** Let `f : X ⟶ S` be a proper smooth morphism of schemes with
> geometrically connected fibres of dimension at most `1` (the source: of dimension `1`), and let
> `ℓ` be a prime number. Then `Rᵠ f_* 𝐙/ℓ𝐙` is a constructible sheaf of `𝔽_ℓ`-modules on `S_étale`
> for every `q`.
>
> The base `S` is arbitrary: the source's absolute Noetherian approximation
> (`isConstructibleEtaleModule_rightDerivedConstantUnit_of_forall_isNoetherian`) reduces to a
> Noetherian base, where the statement is
> `isConstructibleEtaleModule_rightDerivedConstantUnit_of_isNoetherian` (both cases `ℓ` invertible
> and `ℓ = 0` on `S`).

```lean
theorem isConstructibleEtaleModule_rightDerivedConstantUnit_of_isProper_of_smooth
    (B : BigEtaleSite.{u}) {X S : B.Scheme} (f : X.obj ⟶ S.obj) [IsProper f] [Smooth f]
    [GeometricallyConnected f] (hdim : ∀ s : S.obj, topologicalKrullDim (f.fiber s) ≤ 1)
    (ℓ : ℕ) [Fact ℓ.Prime] (q : ℕ) :
    IsBigSiteConstructibleEtaleModule B S (ZMod ℓ) (rightDerivedConstantUnit f q (ZMod ℓ))
```

## Tag 0GKW, a lemma

[Tag 0GKW](https://stacks.math.columbia.edu/tag/0GKW) in the Stacks Project.

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_rightDerived_constantSheaf_of_isProper_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/ProperSmoothCurveConstantModule.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/ProperSmoothCurveConstantModule.lean#L56).

> **Stacks Project, Tag 0GKW.** Let `f : X ⟶ S` be a proper smooth morphism of schemes with
> geometrically connected fibres of dimension at most `1` (the source: of dimension `1`), let `Λ`
> be a Noetherian ring and let `M` be a finite `Λ`-module annihilated by an integer `n > 0`. Then
> `Rᵠ f_* M` is a constructible sheaf of `Λ`-modules on `S_étale` for every `q`.

```lean
theorem isConstructibleEtaleModule_rightDerived_constantSheaf_of_isProper_of_smooth
    (B : BigEtaleSite.{u}) {X S : B.Scheme} (f : X.obj ⟶ S.obj) [IsProper f] [Smooth f]
    [GeometricallyConnected f] (hdim : ∀ s : S.obj, topologicalKrullDim (f.fiber s) ≤ 1)
    (Λ : Type) [CommRing Λ] [IsNoetherianRing Λ] (M : ModuleCat.{u + 1} Λ)
    (hM : Module.Finite Λ M) (n : ℕ) (hn : 0 < n) (hnM : ∀ m : M, n • m = 0) (q : ℕ) :
    IsBigSiteConstructibleEtaleModule B S Λ
      (((etaleModuleDirectImage.{u, 0} Λ f).rightDerived q).obj
        ((constantSheaf X.obj.smallEtaleTopology (ModuleCat.{u + 1} Λ)).obj M))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.13, Tag 0GKT](https://stacks.math.columbia.edu/tag/0GKT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
