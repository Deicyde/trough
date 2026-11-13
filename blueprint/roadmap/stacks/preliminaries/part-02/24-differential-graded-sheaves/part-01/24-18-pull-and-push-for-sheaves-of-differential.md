---
declaration: section
origin: cited
lean: Stacks.DifferentialGradedPullbackConstruction.exists_pullbackPushforwardHomEquiv, SheafOfModules.DifferentialGradedModule.exists_toposPullbackPushforwardHomEquiv
statement: formalized
proof: formalized
---

# 24.18 Pull and push for sheaves of differential graded modules

Section 24.18 of the Stacks Project, [Tag 0FRT](https://stacks.math.columbia.edu/tag/0FRT). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FRU, a lemma

[Tag 0FRU](https://stacks.math.columbia.edu/tag/0FRU) in the Stacks Project.

**`Stacks.DifferentialGradedPullbackConstruction.exists_pullbackPushforwardHomEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedPushPullAdjunction.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedPushPullAdjunction.lean#L127). The attribute's comment: “the case of a morphism of small ringed sites whose functor is continuous, representably flat and final; for an arbitrary morphism of ringed topoi this is SheafOfModules.DifferentialGradedModule.exists\_toposPullbackPushforwardHomEquiv”.

> **Pull and push for sheaves of differential graded modules**: for the direct image `f_*` and
> the pullback `f^*M = f⁻¹M ⊗_{f⁻¹A'} A` along a morphism of small ringed sites, together with a
> unital homomorphism `φ₀ : f⁻¹A' ⟶ A`,
> `Hom_{Mod^dg(A', d)}(M, f_*N) = Hom_{Mod^dg(A, d)}(f^*M, N)`.
>
> The identification `e` of the two differential graded Hom objects is given in every degree `n`,
> it is precomposition with the unit `M ⟶ f^*M` of the pullback — so in particular it is additive
> and natural — and it carries the differential of the one Hom complex to the differential of the
> other. Its degree-zero closed part is the bijection `e₀` of hom-sets of the adjunction
> `f^* ⊣ f_*`, which sends a morphism `g : f^*M ⟶ N` to the unit followed by `g`, read as a
> morphism `M ⟶ f_*N`.

```lean
theorem exists_pullbackPushforwardHomEquiv (φ₀ : inverseImageAlgebra α hO hP A' ⟶ A)
    (hφ₀ : φ₀.IsUnital) :
    ∃ (e : ∀ (M : SheafOfModules.DifferentialGradedModule.{u, u, u} A')
          (N : SheafOfModules.DifferentialGradedModule.{u, u, u} A) (n : ℤ),
          HomogeneousMap (X := ⟨D, K, Psharp⟩) A (pullbackObj α hO hP φ₀ hφ₀ M) N n ≃
            HomogeneousMap (X := ⟨C, J, Osharp⟩) A' M
              (pushforwardObj (semilinearHom α hO hP φ₀ hφ₀) N) n)
        (e₀ : ∀ (M : SheafOfModules.DifferentialGradedModule.{u, u, u} A')
          (N : SheafOfModules.DifferentialGradedModule.{u, u, u} A),
          (pullbackObj α hO hP φ₀ hφ₀ M ⟶ N) ≃
            (M ⟶ pushforwardObj (semilinearHom α hO hP φ₀ hφ₀) N)),
      (∀ M N n w, (e M N n w).val =
          precompCochain (pullbackUnit α hO hP φ₀ hφ₀ M) w.val) ∧
      (∀ M N n w w' w'', w''.val = w.val + w'.val →
          (e M N n w'').val = (e M N n w).val + (e M N n w').val) ∧
      (∀ M N n w w', w'.val = δ n (n + 1) w.val →
          (e M N (n + 1) w').val = δ n (n + 1) (e M N n w).val) ∧
      (∀ M N g, e₀ M N g = semilinearHomEquiv (semilinearHom α hO hP φ₀ hφ₀) M N
          ((pullbackUnit α hO hP φ₀ hφ₀ M).postcomp g))
```

**`SheafOfModules.DifferentialGradedModule.exists_toposPullbackPushforwardHomEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPushPullHomComplex.lean, line 581](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPushPullHomComplex.lean#L581).

> **Stacks Project, Tag 0FRU.** Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of
> ringed topoi, let `A` be a differential graded `O_C`-algebra, let `B` be a differential graded
> `O_D`-algebra and let `φ : B ⟶ f_*A` be a unital homomorphism of differential graded
> `O_D`-algebras (the datum of Tag 0FRT in the form of Remark 0FRG). Then for a right differential
> graded `B`-module `N` and a right differential graded `A`-module `M`,
> `Hom_{Mod^dg(B, d)}(N, f_*M) = Hom_{Mod^dg(A, d)}(f^*N, M)`.
>
> Here `f^*N = f^*N ⊗_{f^*B} A` is `toposPullbackDg f φ hφ` (that is, `toposBaseChangeFunctor f φ
> hφ`) and `f\_*` is `toposPushforwardDg f φ hφ` (that is,
> `toposPushforward (toposDirectImageModules f) φ hφ`). The identification `e` of the two
> differential graded Hom objects is given in every degree `n`; it is `w ↦ η_N ∘ f_*(w)` for `η`
> the unit of the adjunction `f^* ⊣ f_*` and `f_*(w)` the direct image of the homogeneous map `w`;
> it is additive and carries the differential of the one Hom complex to the differential of the
> other, so it is an isomorphism of complexes; it is natural in `N` and in `M`; and on morphisms of
> differential graded modules it is the hom-set bijection of the adjunction `f^* ⊣ f_*`
> (`toposPullbackPushforwardAdjunction`, that is, `toposBaseChangeAdjunction`).

```lean
theorem exists_toposPullbackPushforwardHomEquiv :
    ∃ e : ∀ (N : DifferentialGradedModule.{u, u, u} B)
        (M : DifferentialGradedModule.{u, u, u} A) (n : ℤ),
        HomogeneousMap (X := X.toRingedSite) A ((toposPullbackDg f φ hφ).obj N) M n ≃
          HomogeneousMap (X := Y.toRingedSite) B N ((toposPushforwardDg f φ hφ).obj M) n,
      (∀ N M n w, toposCochain (e N M n w) =
        (Cochain.ofHom (toposBaseChangeUnit f φ hφ N).toHomologicalComplex).comp
          (toposCochain (toposPushforwardHomogeneous f φ hφ w)) (zero_add n)) ∧
      (∀ N M n w w' w'', toposCochain w'' = toposCochain w + toposCochain w' →
        toposCochain (e N M n w'') = toposCochain (e N M n w) + toposCochain (e N M n w')) ∧
      (∀ N M n w w', toposCochain w' = δ n (n + 1) (toposCochain w) →
        toposCochain (e N M (n + 1) w') = δ n (n + 1) (toposCochain (e N M n w))) ∧
      (∀ (N N' : DifferentialGradedModule.{u, u, u} B) M n (v : N' ⟶ N) w w',
        toposCochain w' =
          (Cochain.ofHom ((toposPullbackDg f φ hφ).map v).toHomologicalComplex).comp
            (toposCochain w) (zero_add n) →
        toposCochain (e N' M n w') =
          (Cochain.ofHom v.toHomologicalComplex).comp (toposCochain (e N M n w)) (zero_add n)) ∧
      (∀ N (M M' : DifferentialGradedModule.{u, u, u} A) n (v : M ⟶ M') w w',
        toposCochain w' = (toposCochain w).comp (Cochain.ofHom v.toHomologicalComplex)
          (add_zero n) →
        toposCochain (e N M' n w') = (toposCochain (e N M n w)).comp
          (Cochain.ofHom ((toposPushforwardDg f φ hφ).map v).toHomologicalComplex) (add_zero n)) ∧
      (∀ (N : DifferentialGradedModule.{u, u, u} B) (M : DifferentialGradedModule.{u, u, u} A)
          (g : (toposPullbackDg f φ hφ).obj N ⟶ M) w,
        toposCochain w = Cochain.ofHom g.toHomologicalComplex →
        toposCochain (e N M 0 w) = Cochain.ofHom
          ((toposPullbackPushforwardAdjunction f φ hφ).homEquiv N M g).toHomologicalComplex)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.18, Tag 0FRT](https://stacks.math.columbia.edu/tag/0FRT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
