---
declaration: section
origin: cited
lean: AlgebraicGeometry.VectorBundleKZero.exists_lambdaOperations_pullbackRingHom
statement: formalized
proof: formalized
---

# 45.13 Exterior powers and K-groups

Section 45.13 of the Stacks Project, [Tag 0FIB](https://stacks.math.columbia.edu/tag/0FIB). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FIC, a lemma

[Tag 0FIC](https://stacks.math.columbia.edu/tag/0FIC) in the Stacks Project.

**`AlgebraicGeometry.VectorBundleKZero.exists_lambdaOperations_pullbackRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/LambdaOperationsScheme.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/LambdaOperationsScheme.lean#L290). The attribute's comment: “there exist maps `λ^r : K₀(Vect(X)) → K₀(Vect(X))`, `r : ℕ`, for every scheme `X`, with `λ^r [ℰ] = [⋀^r ℰ]` for each finite locally free `𝒪_X`-module `ℰ` and `λ^r (f^* a) = f^* (λ^r a)` for every morphism `f : Y ⟶ X`, `f^*` being `pullbackRingHom f`”. References: SGA 6 X (1.2), “clause (1.2.1)”.

> **Stacks Project, Tag 0FIC.** Let `X` be a scheme. There are maps
> `λ^r : K₀(Vect(X)) → K₀(Vect(X))` which send `[ℰ]` to `[⋀^r ℰ]` when `ℰ` is a finite locally free
> `𝒪_X`-module and which are compatible with pullbacks: for every morphism of schemes `f : Y ⟶ X`,
> `λ^r ∘ f^* = f^* ∘ λ^r`, where `f^*` is the pullback ring map `pullbackRingHom f`.
>
> The family is `X ↦ lambdaOperation (exteriorPowersData X)`, so nothing is assumed: the filtration
> relation the construction consumes is `exteriorPowersData`, and the pullback map is the one
> constructed in `StacksFrontier.AlgebraicGeometry.Chow.VectorBundleKZeroPullback`.

```lean
theorem exists_lambdaOperations_pullbackRingHom :
    ∃ lam : ∀ X : Scheme.{u}, ℕ → VectorBundleKZero X → VectorBundleKZero X,
      (∀ (X : Scheme.{u}) (r : ℕ) (E : X.Modules),
          IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
            lam X r (classOf X E) = classOf X (Scheme.Modules.exteriorPower E (r : ℤ))) ∧
        (∀ {X Y : Scheme.{u}} (f : Y ⟶ X) (r : ℕ) (a : VectorBundleKZero X),
          lam Y r (pullbackRingHom f a) = pullbackRingHom f (lam X r a))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.13, Tag 0FIB](https://stacks.math.columbia.edu/tag/0FIB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
