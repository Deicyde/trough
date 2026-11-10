---
declaration: section
origin: cited
lean: CategoryTheory.Limits.colimit.post, HasCardinalLT.isCardinalPresentable, Stacks.Injectives.IsSmallWithRespectTo, Stacks.Injectives.isSmallWithRespectTo_monomorphisms_of_mk_submodule_lt_cof, Module.Baer.iff_injective, baerE_lof, baerD_lof, baer_pushout_universal
statement: formalized
proof: formalized
---

# 19.2 Baer's argument for modules

Section 19.2 of the Stacks Project, [Tag 05NM](https://stacks.math.columbia.edu/tag/05NM). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05NN, an equation

[Tag 05NN](https://stacks.math.columbia.edu/tag/05NN) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.colimit.post`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.colimit.post#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch19.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch19.lean#L20) (StacksFrontier).

## Tag 05NR, a lemma

[Tag 05NR](https://stacks.math.columbia.edu/tag/05NR) in the Stacks Project.

Declarations registered for the tag:

- [`HasCardinalLT.isCardinalPresentable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasCardinalLT.isCardinalPresentable#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch19.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch19.lean#L22) (StacksFrontier).

## Tag 05NS, a definition

[Tag 05NS](https://stacks.math.columbia.edu/tag/05NS) in the Stacks Project.

**`Stacks.Injectives.IsSmallWithRespectTo`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/SmallObject.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/SmallObject.lean#L55).

> An object `A` is `α`-small with respect to `I` if `Hom(A, -)` preserves the colimit of
> every `α`-indexed system all of whose transition morphisms belong to `I`.

```lean
abbrev IsSmallWithRespectTo {C : Type u} [Category.{v} C] (A : C)
    (I : MorphismProperty C) (α : Ordinal.{w}) : Prop
```

## Tag 05NT, a proposition

[Tag 05NT](https://stacks.math.columbia.edu/tag/05NT) in the Stacks Project.

**`Stacks.Injectives.isSmallWithRespectTo_monomorphisms_of_mk_submodule_lt_cof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/SmallWithRespectToInjections.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/SmallWithRespectToInjections.lean#L109).

> **Stacks 05NT.** Let `R` be a ring, let `M` be an `R`-module and let `κ` be the
> cardinality of the set of submodules of `M`. If `α` is an ordinal whose cofinality is
> bigger than `κ`, then `M` is `α`-small with respect to injections, i.e. for every system
> `(B_β)_{β ∈ α}` of `R`-modules with injective transition maps the canonical map
> `colim_β Hom(M, B_β) ⟶ Hom(M, colim_β B_β)` is bijective.

```lean
theorem isSmallWithRespectTo_monomorphisms_of_mk_submodule_lt_cof
    {R : Type u} [Ring R] (M : ModuleCat.{u} R) (α : Ordinal.{u})
    (hα : Cardinal.mk (Submodule R M) < α.cof) :
    IsSmallWithRespectTo M (MorphismProperty.monomorphisms (ModuleCat.{u} R)) α
```

## Tag 05NU, a lemma

[Tag 05NU](https://stacks.math.columbia.edu/tag/05NU) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Baer.iff_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Baer.iff_injective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch19.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch19.lean#L27) (StacksFrontier).

## Tag 05NV, an equation

[Tag 05NV](https://stacks.math.columbia.edu/tag/05NV) in the Stacks Project.

**`baerE_lof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerPushout.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerPushout.lean#L387). The attribute's comment: “the top horizontal arrow”.

> The top horizontal arrow `⨁_{(a, φ)} a → M` of the defining square of `𝐌(M)`, read on
> the summands: the element `x` of the ideal `a`, placed in the summand indexed by the pair
> `(a, φ)`, is sent to `φ x ∈ M`.  The direct sum over the sigma type `I(M) = Σ a, Hom(a, M)`
> realizes the iterated coproduct `⨁_a ⨁_{φ ∈ Hom(a, M)}`.

```lean
theorem baerE_lof (a : Ideal R) (φ : a →ₗ[R] M) (x : a) :
    baerE R M (DirectSum.lof R (BaerIndex R M) (fun i => (i.1 : Type u)) ⟨a, φ⟩ x) = φ x
```

**`baerD_lof`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerPushout.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerPushout.lean#L397). The attribute's comment: “the left vertical arrow”.

> The left vertical arrow `⨁_{(a, φ)} a → ⨁_{(a, φ)} R` of the defining square of `𝐌(M)`,
> read on the summands: the element `x` of the ideal `a`, placed in the summand indexed by the
> pair `(a, φ)`, is sent to the same element `x`, now viewed in the copy of `R` indexed by that
> same pair `(a, φ)`.

```lean
theorem baerD_lof (a : Ideal R) (φ : a →ₗ[R] M) (x : a) :
    baerD R M (DirectSum.lof R (BaerIndex R M) (fun i => (i.1 : Type u)) ⟨a, φ⟩ x)
      = DirectSum.lof R (BaerIndex R M) (fun _ => R) ⟨a, φ⟩ (x : R)
```

**`baer_pushout_universal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerPushout.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerPushout.lean#L462). The attribute's comment: “the pushout defining 𝐌(M)”.

> The module `𝐌(M)`, together with the canonical maps `u_M : M → 𝐌(M)` and
> `v_M : T(M) → 𝐌(M)`, is the pushout of `M ← S(M) → T(M)`: for every `R`-module `N` and every
> pair of maps `f : M → N`, `g : T(M) → N` making the outer square commute, there is a unique
> `k : 𝐌(M) → N` with `k ∘ u_M = f` and `k ∘ v_M = g`.  Together with `baer_pushout_square`,
> `baerE_lof` and `baerD_lof` this says that the square
>
>     ⨁_{(a, φ)} a  --e_M-->  M
>          |                   |
>         d_M                 u_M
>          v                   v
>     ⨁_{(a, φ)} R  --v_M-->  𝐌(M)
>
> is the pushout square defining `𝐌(M)`.

```lean
theorem baer_pushout_universal (f : M →ₗ[R] N) (g : BaerT R M →ₗ[R] N)
    (h : f.comp (baerE R M) = g.comp (baerD R M)) :
    ∃! k : BaerM R M →ₗ[R] N, k.comp (baerUMap R M) = f ∧ k.comp (baerV R M) = g
```

## Tag 05NW, a lemma

[Tag 05NW](https://stacks.math.columbia.edu/tag/05NW) in the Stacks Project.

**`baer_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerPushout.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerPushout.lean#L287). The attribute's comment: “(1)”.

> Statement 1 (Functoriality).  The construction `M ↦ (u_M : M → 𝐌(M))` is functorial:
> there is an assignment `MMap` on `R`-module morphisms `χ : M → N`, giving a map
> `MMap χ : 𝐌(M) → 𝐌(N)`, such that
>
> 1. `MMap id = id` (identities are preserved);
> 2. `MMap (χ' ∘ χ) = MMap χ' ∘ MMap χ` (composition is preserved);
> 3. the maps `u_M` are a natural transformation `𝟭 ⟹ 𝐌`, i.e.
>    `MMap χ ∘ u_M = u_N ∘ χ` for every `χ : M → N`.
>
> Here the morphism action `MMap` is quantified existentially, modelling "there is a
> functor `𝐌` with `u` a natural transformation from the identity to `𝐌`".

```lean
theorem baer_functorial :
    ∃ MMap : ∀ {M N : Type u} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N],
        (M →ₗ[R] N) → (BaerM R M →ₗ[R] BaerM R N),
      (∀ (M : Type u) [AddCommGroup M] [Module R M],
          MMap (LinearMap.id : M →ₗ[R] M) = LinearMap.id) ∧
      (∀ {M N P : Type u} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
          [AddCommGroup P] [Module R P] (χ : M →ₗ[R] N) (χ' : N →ₗ[R] P),
          MMap (χ'.comp χ) = (MMap χ').comp (MMap χ)) ∧
      (∀ {M N : Type u} [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N]
          (χ : M →ₗ[R] N),
          (MMap χ).comp (baerUMap R M) = (baerUMap R N).comp χ)
```

**`baer_uMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerPushout.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerPushout.lean#L344). The attribute's comment: “(2)”.

> Statement 2 (Injectivity).  The canonical map `u_M : M → 𝐌(M)` is injective.

```lean
theorem baer_uMap_injective : Function.Injective (baerUMap R M)
```

**`baer_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerPushout.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerPushout.lean#L366). The attribute's comment: “(3)”.

> Statement 3 (Extension property).  For every ideal `a` and `R`-module map
> `φ : a → M`, there is an `R`-module map `φ' : R → 𝐌(M)` with `φ' |_a = u_M ∘ φ`, i.e.
> `φ' (a) = u_M (φ a)` for all `a ∈ a`.

```lean
theorem baer_extension (a : Ideal R) (φ : a →ₗ[R] M) :
    ∃ φ' : R →ₗ[R] BaerM R M,
      φ'.comp a.subtype = (baerUMap R M).comp φ
```

## Tag 05NX, a theorem

[Tag 05NX](https://stacks.math.columbia.edu/tag/05NX) in the Stacks Project.

**`Stacks.Injectives.baerIterateFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean#L131). The attribute's comment: “the functorial transfinite construction”.

> `M_α`, functorially in `M`: the top stage of the transfinite iteration of
> the Baer construction through the ordinal `α`.

```lean
noncomputable def baerIterateFunctor (R : Type u) [CommRing R]
    (α : Ordinal.{u}) : ModuleCat.{u} R ⥤ ModuleCat.{u} R
```

**`Stacks.Injectives.baerIterateEmbedding`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean#L137). The attribute's comment: “the natural map to the iterate”.

> The canonical natural map `M ⟶ M_α`.

```lean
noncomputable def baerIterateEmbedding (R : Type u) [CommRing R]
    (α : Ordinal.{u}) : 𝟭 (ModuleCat.{u} R) ⟶ baerIterateFunctor R α
```

**`Stacks.Injectives.baerIterate_injective_of_cofinality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean#L331). The attribute's comment: “injectivity of the target”.

> If the cofinality of `α` exceeds the cardinality of the set of ideals of `R`, then the
> top stage `M_α` of the transfinite Baer iteration is an injective `R`-module.

```lean
theorem baerIterate_injective_of_cofinality
    (R : Type u) [CommRing R] (α : Ordinal.{u})
    (hα : Cardinal.mk (Ideal R) < α.cof) (M : ModuleCat.{u} R) :
    Injective ((baerIterateFunctor R α).obj M)
```

**`Stacks.Injectives.mono_baerIterateEmbedding`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Module/BaerEmbedding.lean#L360). The attribute's comment: “the natural embedding”.

> The canonical natural map from a module to any transfinite Baer iterate is a monomorphism.
> Together with `baerIterate_injective_of_cofinality`, its components give functorial injective
> embeddings.

```lean
theorem mono_baerIterateEmbedding
    (R : Type u) [CommRing R] (α : Ordinal.{u}) (M : ModuleCat.{u} R) :
    Mono ((baerIterateEmbedding R α).app M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.2, Tag 05NM](https://stacks.math.columbia.edu/tag/05NM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
