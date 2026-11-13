---
declaration: section
origin: cited
lean: CochainComplex.Plus.exists_functorial_injective_resolution_and_exists_resolutionFunctor
statement: formalized
proof: formalized
---

# 13.24 Functorial injective embeddings and resolution functors

Section 13.24 of the Stacks Project, [Tag 0140](https://stacks.math.columbia.edu/tag/0140). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0141, a lemma

[Tag 0141](https://stacks.math.columbia.edu/tag/0141) in the Stacks Project.

**`CochainComplex.Plus.exists_functorial_injective_resolution_and_exists_resolutionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/FunctorialInjectiveResolution.lean, line 1040](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/FunctorialInjectiveResolution.lean#L1040).

> Let `C` be an abelian category.
>
> (1) If `C` has functorial injective embeddings, i.e. is equipped with a functor
> `J : C ⥤ ℐ` to the full subcategory of injective objects and a natural transformation
> `η : 𝟭 C ⟶ J` with monomorphic components ([Stacks, Tag 0139]), then there is a functor
> `F : Comp⁺(C) ⥤ Comp⁺(ℐ)` on bounded below cochain complexes and a natural transformation
> `α : 𝟭 ⟶ F ⋙ ι` whose components are quasi-isomorphisms, i.e. a functorial injective
> resolution of bounded below complexes.
>
> (2) Any such pair `(F, α)` — over an arbitrary abelian `C` — induces a resolution functor
> for `C` ([Stacks, Tag 013W]), namely the one whose value at `K` is the image of `F K` in
> `K⁺(ℐ)` and whose comparison map is the homotopy class of `α_K`.

```lean
public theorem exists_functorial_injective_resolution_and_exists_resolutionFunctor :
    (∀ (J : C ⥤ InjectiveObject C) (η : 𝟭 C ⟶ J ⋙ InjectiveObject.ι C),
        (∀ A, Mono (η.app A)) →
        ∃ (F : CochainComplex.Plus C ⥤ CochainComplex.Plus (InjectiveObject C))
          (α : 𝟭 (CochainComplex.Plus C) ⟶ F ⋙ (InjectiveObject.ι C).mapCochainComplexPlus),
          ∀ K, CochainComplex.Plus.quasiIso C (α.app K)) ∧
      ∀ (F : CochainComplex.Plus C ⥤ CochainComplex.Plus (InjectiveObject C))
        (α : 𝟭 (CochainComplex.Plus C) ⟶ F ⋙ (InjectiveObject.ι C).mapCochainComplexPlus),
        (∀ K, CochainComplex.Plus.quasiIso C (α.app K)) →
        ∃ R : HomotopyCategory.Plus.ResolutionFunctor C,
          ∀ K : CochainComplex.Plus C,
            ∃ h : (R ((HomotopyCategory.Plus.quotient C).obj K)).X₁ =
                (HomotopyCategory.Plus.quotient (InjectiveObject C)).obj (F.obj K),
              (R ((HomotopyCategory.Plus.quotient C).obj K)).w =
                (HomotopyCategory.Plus.quotient C).map (α.app K) ≫
                  eqToHom (congrArg (InjectiveObject.ι C).mapHomotopyCategoryPlus.obj h.symm)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.24, Tag 0140](https://stacks.math.columbia.edu/tag/0140)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
