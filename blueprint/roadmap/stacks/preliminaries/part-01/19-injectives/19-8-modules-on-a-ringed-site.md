---
declaration: section
origin: cited
lean: Stacks.Duality.shortExact_internalHomMapLeft_of_injective, internalHom_exact_of_injective, Stacks.Injectives.AbelianDual.dualFunctor_shortExact_of_injective, Stacks.Injectives.DualEvaluation.evaluation_mono, Stacks.Injectives.DualEvaluation.injective_standardModule, Stacks.Injectives.sheafOfModules_hasFunctorialInjectiveEmbeddings, CategoryTheory.IsGrothendieckAbelian.enoughInjectives, Stacks.Injectives.presheafOfModules_hasFunctorialInjectiveEmbeddings
statement: formalized
proof: formalized
---

# 19.8 Modules on a ringed site

Section 19.8 of the Stacks Project, [Tag 01DQ](https://stacks.math.columbia.edu/tag/01DQ). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01DR, a lemma

[Tag 01DR](https://stacks.math.columbia.edu/tag/01DR) in the Stacks Project.

**`Stacks.Duality.shortExact_internalHomMapLeft_of_injective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Sweep/NormalSheafAsSheafExt.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/Sweep/NormalSheafAsSheafExt.lean#L382). The attribute's comment: “for sheaves of modules on a ringed space, against the sequence of a sheaf of ideals; the library's `Stacks.Injectives.AbelianDual.dualFunctor_shortExact_of_injective` is the statement for the abelian-sheaf internal Hom against an injective abelian sheaf instead”.

> **[Stacks, Tag 01DR] for sheaves of modules, on the ideal sequence.** For an injective sheaf
> of `𝒪_Y`-modules `K` the internal Hom `𝓗om_{𝒪_Y}(-, K)` carries `0 ⟶ ℐ ⟶ 𝒪_Y ⟶ 𝒪_X ⟶ 0` to a
> short exact sequence
>
> `0 ⟶ 𝓗om(𝒪_X, K) ⟶ 𝓗om(𝒪_Y, K) ⟶ 𝓗om(ℐ, K) ⟶ 0`.
>
> Exactness at the middle term and the left-hand monomorphism are the left exactness of internal
> Hom in the first variable, [Stacks, Tag 0GMY] part (1); the right-hand epimorphism is where the
> injectivity of `K` is spent, through `epi_internalHomMapLeft_ι`.

```lean
public lemma shortExact_internalHomMapLeft_of_injective
    (K : SheafOfModules.{u}
      (SheafOfModules.Tensor.ringSheaf Y.sheaf)) [Injective K] :
    (ShortComplex.mk
      ((internalHomMapLeftNatTrans Y.sheaf (cokernel.π I.ι)).app K)
      ((internalHomMapLeftNatTrans Y.sheaf I.ι).app K)
      (by
        rw [← NatTrans.comp_app, internalHomMapLeftNatTrans_comp, cokernel.condition,
          internalHomMapLeftNatTrans_zero]
        rfl)).ShortExact
```

**`internalHom_exact_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/InternalHomExact.lean, line 897](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/InternalHomExact.lean#L897). References: SGA 4 V (4.10), “1), A = Z”.

> **Statement 1 (Stacks Tag 01DR, abelian-sheaf level).**
> Let `J` be an injective abelian sheaf on a site `(C, K)`. Then the contravariant
> internal-Hom functor `ℋom(-, J)` is exact: for every short exact sequence
> `0 → F' → F → F'' → 0` of abelian sheaves, encoded as a short complex `S` with
> `S.ShortExact`, the contravariantly induced short complex
> `(ℋom(-, J)) ∘ Sᵒᵖ`, i.e. `0 → ℋom(F'', J) → ℋom(F, J) → ℋom(F', J) → 0`,
> is again short exact.

```lean
theorem internalHom_exact_of_injective (K : GrothendieckTopology C) [HasSheafify K Ab.{max u v}]
    (J : Sheaf K Ab.{max u v}) [Injective J]
    (S : ShortComplex (Sheaf K Ab.{max u v})) (hS : S.ShortExact) :
    (S.op.map (internalHomFunctor K J)).ShortExact
```

**`Stacks.Injectives.AbelianDual.dualFunctor_shortExact_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/InternalHomExact.lean, line 1248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/InternalHomExact.lean#L1248). The attribute's comment: “module-valued exactness”.

> **Stacks 01DR (Lemma 19.8.1), the statement itself.** The functor `F ↦ F^∨`, with its
> natural `O`-module structure, is exact when `J` is an injective abelian sheaf: it carries a
> short exact sequence of sheaves of `O`-modules to a short exact sequence of sheaves of
> `O`-modules.
>
> The source's proof is "this because `J` is an injective abelian sheaf", and that is exactly how
> this runs: exactness of the forgetful functor to abelian sheaves (Stacks 03DA) reduces the
> claim to `internalHom_exact_of_injective` above, which is where the injectivity of `J` is
> spent.

```lean
theorem dualFunctor_shortExact_of_injective
    [HasSheafify K Ab.{max u v}] [K.WEqualsLocallyBijective Ab.{max u v}]
    (O : Sheaf K CommRingCat.{max u v}) (J : Sheaf K Ab.{max u v}) [Injective J]
    (S : ShortComplex (SheafOfModules.{max u v} (underlyingRingSheaf O)))
    (hS : S.ShortExact) :
    letI := (dualFunctorData O J).preservesZero
    (S.op.map (dualFunctor O J)).ShortExact
```

## Tag 01DS, a lemma

[Tag 01DS](https://stacks.math.columbia.edu/tag/01DS) in the Stacks Project.

**`Stacks.Injectives.DualEvaluation.evaluation_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/DualEvaluationMono.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/DualEvaluationMono.lean#L330).

> For every sheaf of `O`-modules `F` on a ringed site the evaluation map `ev : F ⟶ (F^∨)^∨`
> into the double dual is a monomorphism, the dual being taken against the dualizing sheaf of the
> site.

```lean
theorem evaluation_mono (F : SheafOfModules.{u} (underlyingRingSheaf O)) :
    Mono (ev O (dualizingSheafOfRingedSite O) F)
```

## Tag 01DT, a lemma

[Tag 01DT](https://stacks.math.columbia.edu/tag/01DT) in the Stacks Project.

**`Stacks.Injectives.DualEvaluation.injective_standardModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/StandardInjectiveModule.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/StandardInjectiveModule.lean#L221).

> For every sheaf `F` of `O`-modules the standard module `J(F) = Fr(F^∨)^∨` is an injective
> `O`-module.

```lean
theorem injective_standardModule (F : SheafOfModules.{u} (underlyingRingSheaf O)) :
    Injective (standardModule O Jab F)
```

## Tag 01DU, a theorem

[Tag 01DU](https://stacks.math.columbia.edu/tag/01DU) in the Stacks Project.

**`Stacks.Injectives.sheafOfModules_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSite.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSite.lean#L111).

> **Stacks Project, Tag 01DU.** The category of sheaves of modules over a sheaf of rings on
> a site has functorial injective embeddings (and consequently enough injectives).

```lean
theorem sheafOfModules_hasFunctorialInjectiveEmbeddings
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (O : Sheaf J RingCat.{u}) :
    HasFunctorialInjectiveEmbeddings (SheafOfModules.{u} O)
```

Declarations registered for the tag:

- [`CategoryTheory.IsGrothendieckAbelian.enoughInjectives`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsGrothendieckAbelian.enoughInjectives#doc) registered with `add_to_stacks` in [StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSite.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSite.lean#L56) (StacksFrontier): “enough injectives”. References: SGA 3 I (5.3.1.1), “more general”; SGA 4 I (7.13); SGA 4 V (0.1.1); SGA 4 V (0.2.1); SGA 4 V (2.5.2), “more general”.

## Tag 01DV, a proposition

[Tag 01DV](https://stacks.math.columbia.edu/tag/01DV) in the Stacks Project.

**`Stacks.Injectives.presheafOfModules_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/PresheavesOfModules.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/PresheavesOfModules.lean#L198). References: SGA 3 I (3.1.2), “more general”.

> **Stacks Project, Tag 01DV.** The category of presheaves of modules over a presheaf of
> rings has functorial injective embeddings (and consequently enough injectives).

```lean
theorem presheafOfModules_hasFunctorialInjectiveEmbeddings
    (C : Type u) [Category.{v} C] (R : Cᵒᵖ ⥤ RingCat.{w}) :
    HasFunctorialInjectiveEmbeddings (PresheafOfModules.{max u v w} R)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.8, Tag 01DQ](https://stacks.math.columbia.edu/tag/01DQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
