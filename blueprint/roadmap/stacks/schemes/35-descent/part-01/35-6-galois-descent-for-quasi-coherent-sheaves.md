---
declaration: section
origin: cited
lean: Stacks.Descent.nonempty_equivalence_galoisDescentData_baseChange, Stacks.Descent.nonempty_equivalence_galoisDescentData
statement: formalized
proof: formalized
---

# 35.6 Galois descent for quasi-coherent sheaves

Section 35.6 of the Stacks Project, [Tag 0CDQ](https://stacks.math.columbia.edu/tag/0CDQ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CDR, a lemma

[Tag 0CDR](https://stacks.math.columbia.edu/tag/0CDR) in the Stacks Project.

**`Stacks.Descent.nonempty_equivalence_galoisDescentData_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/GaloisFieldExtension.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/GaloisFieldExtension.lean#L532).

> **Galois descent for quasi-coherent modules.**  For a finite Galois extension `K/k` with
> group `G` and a scheme `X` over `k`, the category of quasi-coherent `𝒪_X`-modules is equivalent
> to the category of systems `(ℱ, (φ_σ)_{σ ∈ G})` where `ℱ` is quasi-coherent on `X_K`, each
> `φ_σ : ℱ ≅ f_σ^* ℱ` is an isomorphism, and `φ_(στ) = f_σ^*(φ_τ) ∘ φ_σ`.  Here
> `f_σ = id_X × Spec σ`.

```lean
theorem nonempty_equivalence_galoisDescentData_baseChange :
    Nonempty ((SheafOfModules.isQuasicoherent Z.left.ringCatSheaf).FullSubcategory ≌
      GaloisDescentData (K ≃ₐ[k] K) (baseChangeProjection k K Z)
        (baseChangeOverAction k K Z))
```

## Tag 0D1V, a lemma

[Tag 0D1V](https://stacks.math.columbia.edu/tag/0D1V) in the Stacks Project.

**`Stacks.Descent.nonempty_equivalence_galoisDescentData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/GaloisEquivalence.lean, line 968](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/GaloisEquivalence.lean#L968). References: SGA 4½ Arcata (1.5.1), “a), b), c) equivalence”.

> **Galois descent for quasi-coherent modules.**  For a surjective finite étale morphism
> `f : X ⟶ Y` carrying an action of a finite group `G` over `Y` which identifies `∐_{σ : G} X`
> with `X ×_Y X`, quasi-coherent modules on `Y` are the same thing as Galois descent systems
> on `X`.

```lean
theorem nonempty_equivalence_galoisDescentData [IsFinite f] [Etale f] [Surjective f] :
    Nonempty ((SheafOfModules.isQuasicoherent Y.ringCatSheaf).FullSubcategory ≌
      GaloisDescentData G f a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.6, Tag 0CDQ](https://stacks.math.columbia.edu/tag/0CDQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
