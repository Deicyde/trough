---
declaration: section
origin: cited
lean: Stacks.PicardFunctor.picardPresheaf, Stacks.PicardFunctor.picardFunctor, Stacks.PicardFunctor.injective_schemePullbackClass_baseChangeProj, Stacks.PicardFunctor.exact_schemePullbackClass_baseChangeProj_toPicardFunctorHom_of_isIso_c, Stacks.PicardFunctor.schemePullbackClass_baseChangeSection_baseChangeProj, Stacks.PicardFunctor.injective_schemePullbackClass_baseChangeProj_of_section, Stacks.PicardFunctor.exact_schemePullbackClass_baseChangeProj_toPicardFunctorHom, Stacks.PicardFunctor.surjective_toPicardFunctorHom
statement: formalized
proof: formalized
---

# 44.4 The Picard functor

Section 44.4 of the Stacks Project, [Tag 0B9K](https://stacks.math.columbia.edu/tag/0B9K). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B9L, a definition

[Tag 0B9L](https://stacks.math.columbia.edu/tag/0B9L) in the Stacks Project.

**`Stacks.PicardFunctor.picardPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardFunctor.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardFunctor.lean#L154). The attribute's comment: “the presheaf of Picard groups of the base changes”.

> **Stacks Project, Tag 0B9L.** The presheaf `T ↦ Pic(X_T)` on the `S`-schemes of the site,
> whose fppf sheafification is the Picard functor. Its action on a morphism of test schemes is
> pullback of Picard classes.

```lean
def picardPresheaf : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)
```

**`Stacks.PicardFunctor.picardFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardFunctor.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardFunctor.lean#L176). The attribute's comment: “the Picard functor”. References: SGA 6 X (2.4), “definition of Pic\_\{X/S}”; SGA 6 XIII (3.1).

> **Stacks Project, Tag 0B9L.** The *Picard functor* `Pic_{X/S} : (Sch/S)_{fppf} ⥤ Sets` of a
> morphism `f : X ⟶ S` of a big fppf site: the fppf sheafification of the presheaf
> `T ↦ Pic(X_T)` of isomorphism classes of invertible modules on the base changes of `X`.

```lean
def picardFunctor : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (u + 1)
```

## Tag 0B9M, a lemma

[Tag 0B9M](https://stacks.math.columbia.edu/tag/0B9M) in the Stacks Project.

**`Stacks.PicardFunctor.injective_schemePullbackClass_baseChangeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceLeftExactness.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceLeftExactness.lean#L155). The attribute's comment: “left exactness”.

> **Stacks Project, Tag 0B9M.** If the comparison map `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` is an
> isomorphism for every `S`-scheme `T` of the site, then pullback along `X_T ⟶ T` is injective on
> Picard groups; this is exactness at `Pic(T)` of
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/S}(T)`.

```lean
theorem injective_schemePullbackClass_baseChangeProj
    (hO : ∀ T : BigFppfOver B S hS,
      IsIso (baseChangeProj B hX hS f T).toLRSHom.toHom.c)
    (T : BigFppfOver B S hS) :
    Function.Injective (Stacks.Picard.schemePullbackClass (baseChangeProj B hX hS f T))
```

**`Stacks.PicardFunctor.exact_schemePullbackClass_baseChangeProj_toPicardFunctorHom_of_isIso_c`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceMiddleExactness.lean, line 627](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceMiddleExactness.lean#L627). The attribute's comment: “exactness at Pic(X\_T)”.

> If the comparison map `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` is an isomorphism for every `S`-scheme `T` of the
> site, then a Picard class of `X_T` dies in `Pic_{X/S}(T)` exactly when it is pulled back along the
> projection `X_T ⟶ T`; this is exactness at `Pic(X_T)` of `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/S}(T)`.

```lean
theorem exact_schemePullbackClass_baseChangeProj_toPicardFunctorHom_of_isIso_c
    (hOiso : ∀ U : BigFppfOver B S hS, IsIso (baseChangeProj B hX hS f U).toLRSHom.toHom.c)
    (T : BigFppfOver B S hS) :
    Function.Exact (Stacks.Picard.schemePullbackClass (baseChangeProj B hX hS f T))
      (toPicardFunctorHom B hX hS f T)
```

## Tag 0B9N, a lemma

[Tag 0B9N](https://stacks.math.columbia.edu/tag/0B9N) in the Stacks Project.

**`Stacks.PicardFunctor.schemePullbackClass_baseChangeSection_baseChangeProj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/SplittingExactness.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/SplittingExactness.lean#L66). The attribute's comment: “the splitting”.

> **Stacks Project, Tag 0B9N.** Pullback of Picard classes along the induced section
> `σ_T : T ⟶ X_T` is a left inverse of pullback along the projection `X_T ⟶ T`: the sequence
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/S}(T) ⟶ 0` is split by `σ_T^*`.

```lean
theorem schemePullbackClass_baseChangeSection_baseChangeProj (T : BigFppfOver B S hS) :
    Function.LeftInverse
      (Stacks.Picard.schemePullbackClass (baseChangeSection B hX hS f σ hσ T))
      (Stacks.Picard.schemePullbackClass (baseChangeProj B hX hS f T))
```

**`Stacks.PicardFunctor.injective_schemePullbackClass_baseChangeProj_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/SplittingExactness.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/SplittingExactness.lean#L79). The attribute's comment: “injectivity”.

> **Stacks Project, Tag 0B9N.** Pullback of Picard classes along the projection `X_T ⟶ T` is
> injective, the induced section providing a left inverse; this is exactness at `Pic(T)` of
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/S}(T) ⟶ 0`.

```lean
theorem injective_schemePullbackClass_baseChangeProj_of_section (T : BigFppfOver B S hS) :
    Function.Injective (Stacks.Picard.schemePullbackClass (baseChangeProj B hX hS f T))
```

**`Stacks.PicardFunctor.exact_schemePullbackClass_baseChangeProj_toPicardFunctorHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/SplittingExactness.lean, line 591](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/SplittingExactness.lean#L591). The attribute's comment: “exactness in the middle”.

> **Stacks Project, Tag 0B9N.** The image of pullback from `Pic(T)` is exactly the kernel of
> the map to the Picard functor: a Picard class of `X_T` dies in `Pic_{X/S}(T)` if and only if it
> is pulled back along the projection `X_T ⟶ T`. This is exactness in the middle of
> `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/S}(T) ⟶ 0`.

```lean
theorem exact_schemePullbackClass_baseChangeProj_toPicardFunctorHom
    (hOiso : ∀ U : BigFppfOver B S hS,
      IsIso (baseChangeProj B hX hS f U).toLRSHom.toHom.c)
    (T : BigFppfOver B S hS) :
    Function.Exact (Stacks.Picard.schemePullbackClass (baseChangeProj B hX hS f T))
      (toPicardFunctorHom B hX hS f T)
```

**`Stacks.PicardFunctor.surjective_toPicardFunctorHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/Surjectivity.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PicardScheme/PicardSequenceSplitExact/Surjectivity.lean#L386). The attribute's comment: “surjectivity”.

> **Stacks Project, Tag 0B9N.** Every section of the Picard functor over a test scheme `T` is
> the class of an invertible module on `X_T`: pullback `Pic(X_T) ⟶ Pic_{X/S}(T)` is surjective.
> This is exactness at `Pic_{X/S}(T)` of `0 ⟶ Pic(T) ⟶ Pic(X_T) ⟶ Pic_{X/S}(T) ⟶ 0`.
>
> A section is locally the class of an invertible module; normalising those local classes by the
> induced sections makes them agree on the overlaps of the covering family, so they form a
> quasi-coherent descent datum for the base-changed family, which is an fpqc covering of `X_T`.
> Effectivity of fpqc descent produces a module on `X_T`, invertible because its pullbacks are,
> and its class restricts to the given section on the covering family.

```lean
theorem surjective_toPicardFunctorHom
    (hOiso : ∀ U : BigFppfOver B S hS,
      IsIso (baseChangeProj B hX hS f U).toLRSHom.toHom.c)
    (T : BigFppfOver B S hS) :
    Function.Surjective (toPicardFunctorHom B hX hS f T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 44.4, Tag 0B9K](https://stacks.math.columbia.edu/tag/0B9K)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
