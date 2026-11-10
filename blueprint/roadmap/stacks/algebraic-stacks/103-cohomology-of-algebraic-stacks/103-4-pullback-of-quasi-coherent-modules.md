---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.exactFunctor_quasicoherentPullback, AlgebraicGeometry.Stack.preservesFiniteColimits_quasicoherentPullback, AlgebraicGeometry.Stack.isIso_iff_restrictMapToSmallEtale, AlgebraicGeometry.Stack.epi_iff_restrictMapToSmallEtale, AlgebraicGeometry.Stack.mono_iff_restrictMapToSmallEtale
statement: formalized
proof: formalized
---

# 103.4 Pullback of quasi-coherent modules

Section 103.4 of the Stacks Project, [Tag 076W](https://stacks.math.columbia.edu/tag/076W). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 076X, a lemma

[Tag 076X](https://stacks.math.columbia.edu/tag/076X) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exactFunctor_quasicoherentPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelsFlatObjects.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelsFlatObjects.lean#L86).

> **Stacks 076X.** If `f : 𝒳 ⟶ 𝒴` is a flat morphism of algebraic stacks, then
> `f^* : QCoh(𝒪_𝒴) ⥤ QCoh(𝒪_𝒳)` is an exact functor: it preserves finite colimits, as it does for
> every `f`, and finite limits, because kernels of quasi-coherent modules are computed on flat
> objects (`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentKernelsOnFlatObjects`) and `f`
> carries flat objects to flat objects.

```lean
theorem exactFunctor_quasicoherentPullback (hf : AlgebraicStacks.IsFlat B S hS f) :
    exactFunctor (quasicoherentModules B S hS 𝒴) (quasicoherentModules B S hS 𝒳)
      (quasicoherentPullback B S hS f)
```

**`AlgebraicGeometry.Stack.preservesFiniteColimits_quasicoherentPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasicoherentPullbackExactness.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/QuasicoherentPullbackExactness.lean#L140). The attribute's comment: “right exactness”.

> The inverse image of quasi-coherent modules along a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S`, `f^* : QCoh(𝒪_𝒴) ⥤ QCoh(𝒪_𝒳)`, is right exact.

```lean
theorem preservesFiniteColimits_quasicoherentPullback :
    PreservesFiniteColimits (quasicoherentPullback B S hS p q hp hq f hF)
```

## Tag 0GQF, a lemma

[Tag 0GQF](https://stacks.math.columbia.edu/tag/0GQF) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIso_iff_restrictMapToSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentFlatFamilyDetection.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentFlatFamilyDetection.lean#L344). The attribute's comment: “isomorphism”.

> **Stacks 0GQF, isomorphisms.**  Let `𝒳` be an algebraic stack and `x_i : U_i → 𝒳`, `i ∈ I`,
> flat objects with `∐ x_i : ∐ U_i → 𝒳` surjective.  An arrow `φ` of `QCoh(𝒪_𝒳)` is an
> isomorphism if and only if each restriction `φ_i = φ|_{(U_i)_{étale}}` is.

```lean
theorem isIso_iff_restrictMapToSmallEtale :
    IsIso φ ↔ ∀ i, IsIso (restrictMapToSmallEtale B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        (x i)
        ((PresheafOfModules.toPresheaf _).map φ.hom.val))
```

**`AlgebraicGeometry.Stack.epi_iff_restrictMapToSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentFlatFamilyDetection.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentFlatFamilyDetection.lean#L370). The attribute's comment: “surjectivity”.

> **Stacks 0GQF, surjectivity.**  Let `𝒳` be an algebraic stack and `x_i : U_i → 𝒳`,
> `i ∈ I`, flat objects with `∐ x_i : ∐ U_i → 𝒳` surjective.  An arrow `φ` of `QCoh(𝒪_𝒳)` is
> surjective (an epimorphism of `QCoh(𝒪_𝒳)`) if and only if each restriction
> `φ_i = φ|_{(U_i)_{étale}}` is surjective as a map of sheaves on `(U_i)_{étale}`, i.e. locally
> surjective for the étale topology.

```lean
theorem epi_iff_restrictMapToSmallEtale :
    Epi φ ↔ ∀ i, Presheaf.IsLocallySurjective (SmallEtale.topology E (𝒳.val.val.p.obj (x i)).left.1
        (contains_base B E h S hS 𝒳.val.val.p (x i)))
      (restrictMapToSmallEtale B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids (x i)
        ((PresheafOfModules.toPresheaf _).map φ.hom.val))
```

**`AlgebraicGeometry.Stack.mono_iff_restrictMapToSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentFlatFamilyMono.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentFlatFamilyMono.lean#L73). The attribute's comment: “injectivity”.

> **Stacks 0GQF, injectivity.**  Let `𝒳` be an algebraic stack and `x_i : U_i → 𝒳`, `i ∈ I`,
> flat objects with `∐ x_i : ∐ U_i → 𝒳` surjective.  An arrow `φ` of `QCoh(𝒪_𝒳)` is injective (a
> monomorphism of the abelian category `QCoh(𝒪_𝒳)`) if and only if each restriction
> `φ_i = φ|_{(U_i)_{étale}}` is injective on all sections.

```lean
theorem mono_iff_restrictMapToSmallEtale :
    Mono φ ↔ ∀ i V, Function.Injective ((restrictMapToSmallEtale B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (x i) ((PresheafOfModules.toPresheaf _).map φ.hom.val)).app V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.4, Tag 076W](https://stacks.math.columbia.edu/tag/076W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
