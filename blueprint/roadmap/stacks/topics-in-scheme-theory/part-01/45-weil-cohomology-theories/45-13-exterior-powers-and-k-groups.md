---
declaration: section
origin: cited
lean: AlgebraicGeometry.VectorBundleKZero.exists_lambdaOperations, AlgebraicGeometry.VectorBundleKZero.exists_lambdaOperations_pullbackRingHom
statement: formalized
proof: formalized
---

# 45.13 Exterior powers and K-groups

Section 45.13 of the Stacks Project, [Tag 0FIB](https://stacks.math.columbia.edu/tag/0FIB). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FIC, a lemma

[Tag 0FIC](https://stacks.math.columbia.edu/tag/0FIC) in the Stacks Project.

**`AlgebraicGeometry.VectorBundleKZero.exists_lambdaOperations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/LambdaOperations.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/LambdaOperations.lean#L547). The attribute's comment: “all three clauses, granted one hypothesis: the filtration of `⋀ⁿ` along a short exact sequence of finite locally free modules, which the library does not construct. The pullback homomorphism of `K₀(Vect(-))`, whose construction the source omits, is also a hypothesis”. References: SGA 6 0 (2.9), “partial”; SGA 6 V (2.2.1), “Second conjunct only”.

> **Stacks Project, Tag 0FIC.** Let `X` be a scheme. There are maps
> `λ^r : K₀(Vect(X)) → K₀(Vect(X))` which send `[ℰ]` to `[⋀^r ℰ]` when `ℰ` is a finite locally
> free `𝒪_X`-module and which are compatible with pullbacks.
>
> All three clauses of the source are present: the operations are produced as a family of maps,
> the second conjunct is their value on the class of a finite locally free module, and the third
> is their commutation with any ring map of Grothendieck rings realising pullback of finite
> locally free modules.
>
> The sole hypothesis `ExteriorPowersData X` is the geometric input of the source's proof: the
> filtration of `⋀ⁿ` along a short exact sequence, which the library does not construct. Finite
> local freeness of `⋀ⁿ ℰ` and the comparison `f^*(⋀^r ℰ) ≅ ⋀^r(f^*ℰ)` of Tag 01CI are not
> assumed; both are proved.

```lean
theorem exists_lambdaOperations (X : Scheme.{u}) (h : ExteriorPowersData X) :
    ∃ lam : ℕ → VectorBundleKZero X → VectorBundleKZero X,
      (∀ (r : ℕ) (E : X.Modules), IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
          lam r (classOf X E) = classOf X (Scheme.Modules.exteriorPower E (r : ℤ))) ∧
        (∀ (Y : Scheme.{u}) (f : Y ⟶ X) (hY : ExteriorPowersData Y)
            (p : VectorBundleKZero X →+* VectorBundleKZero Y),
          (∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
              p (classOf X E) = classOf Y ((Scheme.Modules.pullback f).obj E)) →
            (∀ E : X.Modules, IsFiniteLocallyFree.{u, u, u} (R := X.ringCatSheaf) E →
              IsFiniteLocallyFree.{u, u, u} (R := Y.ringCatSheaf)
                ((Scheme.Modules.pullback f).obj E)) →
              ∀ (r : ℕ) (a : VectorBundleKZero X),
                lambdaOperation hY r (p a) = p (lambdaOperation h r a))
```

**`AlgebraicGeometry.VectorBundleKZero.exists_lambdaOperations_pullbackRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/LambdaOperationsScheme.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/LambdaOperationsScheme.lean#L290). The attribute's comment: “the maps `λ^r` on `K₀(Vect(X))` for every scheme `X`, their value `λ^r[ℰ] = [⋀^r ℰ]` on finite locally free modules, and their compatibility with pullback `λ^r ∘ f^* = f^* ∘ λ^r` for the pullback ring map `f^*` of `K₀(Vect(-))`; no hypothesis”. References: SGA 6 X (1.2), “clause (1.2.1)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
