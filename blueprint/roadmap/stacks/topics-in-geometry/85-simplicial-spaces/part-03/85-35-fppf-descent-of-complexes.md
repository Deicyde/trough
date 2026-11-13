---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.negativeExt_eq_zero_and_exact_derivedPullback, AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.exists_derivedPullback_degreeZero_iso_compatible
statement: formalized
proof: formalized
---

# 85.35 Fppf descent of complexes

Section 85.35 of the Stacks Project, [Tag 0DL8](https://stacks.math.columbia.edu/tag/0DL8). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DL9, a lemma

[Tag 0DL9](https://stacks.math.columbia.edu/tag/0DL9) in the Stacks Project.

**`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.negativeExt_eq_zero_and_exact_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDerivedHomDescent.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDerivedHomDescent.lean#L482).

> Let `a : U → X` be an fppf hypercovering of an algebraic space and `K, E` objects of
> `D_{QCoh}(𝒪_X)` with `Ext^i_{U_n}(La_n^*K, La_n^*E) = 0` for `i < 0` and all `n`. Then
> (1) `Ext^i_X(K, E) = 0` for `i < 0`, and (2) the sequence
> `0 ⟶ Hom_X(K, E) ⟶ Hom_{U_0}(La_0^*K, La_0^*E) ⟶ Hom_{U_1}(La_1^*K, La_1^*E)` is exact, where the
> first map is `La_0^*` and the second the difference of the pullbacks along the two faces.

```lean
theorem negativeExt_eq_zero_and_exact_derivedPullback
    {K E : @DerivedCategory (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
      (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X).O)) _ _
      (HasDerivedCategory.standard _)}
    (hK : (@DerivedCategoryB.derivedCategoryB _ _ _ (HasDerivedCategory.standard _)
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u + 1, u + 1, u + 1}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X).O))) K)
    (hE : (@DerivedCategoryB.derivedCategoryB _ _ _ (HasDerivedCategory.standard _)
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u + 1, u + 1, u + 1}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X).O))) E)
    (hvan : ∀ (n : SimplexCategory) (i : ℤ), i < 0 →
      ∀ g : (derivedPullback
          (X := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op n)))
          (Y := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X)
          (spacesEtaleRingedToposHom (a.app (op n)))).obj K ⟶
        ((derivedPullback (X := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op n)))
          (Y := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X)
          (spacesEtaleRingedToposHom (a.app (op n)))).obj E)⟦i⟧, g = 0) :
    (∀ (i : ℤ), i < 0 → ∀ g : K ⟶ E⟦i⟧, g = 0) ∧
      Function.Injective (fun g : K ⟶ E ↦
        (derivedPullback (X := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op ⦋0⦌)))
          (Y := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X)
          (spacesEtaleRingedToposHom (a.app (op ⦋0⦌)))).map g) ∧
      Function.Exact (fun g : K ⟶ E ↦
        (derivedPullback (X := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op ⦋0⦌)))
          (Y := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X)
          (spacesEtaleRingedToposHom (a.app (op ⦋0⦌)))).map g)
        (fun ψ ↦ augmentationFaceTransport a 0 ψ - augmentationFaceTransport a 1 ψ)
```

## Tag 0DLA, a lemma

[Tag 0DLA](https://stacks.math.columbia.edu/tag/0DLA) in the Stacks Project.

**`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.exists_derivedPullback_degreeZero_iso_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDerivedGluing.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDerivedGluing.lean#L478).

> **Stacks 0DLA: gluing quasi-coherent derived descent data along an fppf hypercovering.** Let
> `a : U → X` be an fppf hypercovering of an algebraic space `X`, `K₀ ∈ D_{QCoh}(𝒪_{U_0})` and
> `α : L(f_{δ¹₁})^* K₀ ≅ L(f_{δ¹₀})^* K₀` an isomorphism satisfying the cocycle condition (on `U_2`,
> through the canonical identifications of the composite face maps). Set
> `K_n = L(f_{τⁿₙ})^* K₀` with `τⁿₙ : ⦋0⦌ → ⦋n⦌, 0 ↦ n`, and assume `Ext^i(K_n, K_n) = 0` for
> `i < 0`. Then there are `K ∈ D_{QCoh}(𝒪_X)` and an isomorphism `e : La_0^* K ≅ K₀` compatible with
> `α`: `L(f_{δ¹₁})^* e ≫ α = θ₁ ≫ θ₀⁻¹ ≫ L(f_{δ¹₀})^* e`, where
> `θ_i : L(f_{δ¹ᵢ})^* La_0^* ≅ La_1^*` are the canonical isomorphisms (`a_0 ∘ f_{δ¹ᵢ} = a_1`).

```lean
theorem exists_derivedPullback_degreeZero_iso_compatible
    (h : IsHypercoveringAugmentation T.pretopologyBigFppfPretopology U a)
    (K₀ : @DerivedCategory (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
      (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op ⦋0⦌))).O)) _ _
      (HasDerivedCategory.standard _))
    (hK₀ : @DerivedCategoryB.derivedCategoryB _ _ _ (HasDerivedCategory.standard _)
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u + 1, u + 1, u + 1}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op ⦋0⦌))).O)) K₀)
    (α : (derivedPullback (spacesEtaleRingedToposHom
        (U.map (SimplexCategory.δ (1 : Fin 2)).op))).obj K₀ ≅
      (derivedPullback (spacesEtaleRingedToposHom
        (U.map (SimplexCategory.δ (0 : Fin 2)).op))).obj K₀)
    (hα : SpacesEtaleDerivedCocycle U K₀ α)
    (hExt : ∀ (n : ℕ) (i : ℤ), i < 0 →
      ∀ g : (derivedPullback (spacesEtaleRingedToposHom
          (U.map (SimplexCategory.const ⦋0⦌ ⦋n⦌ (Fin.last n)).op))).obj K₀ ⟶
        (shiftFunctor (@DerivedCategory (SheafOfModules.{u + 1}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem (U.obj (op ⦋n⦌))).O)) _ _
          (HasDerivedCategory.standard _)) i).obj
          ((derivedPullback (spacesEtaleRingedToposHom
            (U.map (SimplexCategory.const ⦋0⦌ ⦋n⦌ (Fin.last n)).op))).obj K₀), g = 0) :
    ∃ K : @DerivedCategory (SheafOfModules.{u + 1} (Stacks.SheafOfModules.Tensor.ringSheaf
        (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X).O)) _ _
        (HasDerivedCategory.standard _),
      @DerivedCategoryB.derivedCategoryB _ _ _ (HasDerivedCategory.standard _)
        (SheafOfModules.isQuasicoherentOnSite.{u + 1, u + 1, u + 1, u + 1}
          (Stacks.SheafOfModules.Tensor.ringSheaf
            (spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X).O)) K ∧
      ∃ e : (derivedPullback (X := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem
          (U.obj (op ⦋0⦌))) (Y := spacesEtaleRingedTopos T.schemeSite S T.scheme_mem X)
          (spacesEtaleRingedToposHom (a.app (op ⦋0⦌)))).obj K ≅ K₀,
        (derivedPullback (spacesEtaleRingedToposHom (U.map (SimplexCategory.δ (1 : Fin 2)).op))).map
            e.hom ≫ α.hom =
          ((augmentationTransitionDerivedIso a (SimplexCategory.δ (1 : Fin 2))).hom.app K ≫
            (augmentationTransitionDerivedIso a (SimplexCategory.δ (0 : Fin 2))).inv.app K) ≫
            (derivedPullback (spacesEtaleRingedToposHom
              (U.map (SimplexCategory.δ (0 : Fin 2)).op))).map e.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.35, Tag 0DL8](https://stacks.math.columbia.edu/tag/0DL8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
