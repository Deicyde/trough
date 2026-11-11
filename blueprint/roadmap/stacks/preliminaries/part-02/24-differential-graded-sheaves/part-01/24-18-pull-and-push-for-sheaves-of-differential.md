---
declaration: section
origin: cited
lean: Stacks.DifferentialGradedPullbackConstruction.exists_pullbackPushforwardHomEquiv
statement: formalized
proof: formalized
---

# 24.18 Pull and push for sheaves of differential graded modules

Section 24.18 of the Stacks Project, [Tag 0FRT](https://stacks.math.columbia.edu/tag/0FRT). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRU, a lemma

[Tag 0FRU](https://stacks.math.columbia.edu/tag/0FRU) in the Stacks Project.

**`Stacks.DifferentialGradedPullbackConstruction.exists_pullbackPushforwardHomEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedPushPullAdjunction.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedPushPullAdjunction.lean#L121).

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.18, Tag 0FRT](https://stacks.math.columbia.edu/tag/0FRT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
