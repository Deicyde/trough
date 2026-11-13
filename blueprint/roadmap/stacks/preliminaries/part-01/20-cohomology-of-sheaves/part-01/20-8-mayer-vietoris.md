---
declaration: section
origin: cited
lean: Stacks.Cohomology.InjectiveRestriction.injective_restriction_surjective, Stacks.Cohomology.AbsoluteMayerVietoris.mayerVietoris_exact, Stacks.Cohomology.AbsoluteMayerVietoris.mono_mvFirst_zero, Stacks.Cohomology.MayerVietoris.mayerVietorisInitialSequence_exact, Stacks.Cohomology.MayerVietoris.mayerVietoris_delta_naturality, CategoryTheory.GrothendieckTopology.MayerVietorisSquare.sequence_exact, Stacks.Cohomology.RelativeMayerVietoris.relativeMayerVietoris, Stacks.Cohomology.RelativeMayerVietoris.relativeMayerVietorisPlus
statement: formalized
proof: formalized
---

# 20.8 Mayer-Vietoris

Section 20.8 of the Stacks Project, [Tag 01E9](https://stacks.math.columbia.edu/tag/01E9). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01EA, a lemma

[Tag 01EA](https://stacks.math.columbia.edu/tag/01EA) in the Stacks Project.

**`Stacks.Cohomology.InjectiveRestriction.injective_restriction_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/InjectiveSheavesRestrictOnto.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechAcyclicity/InjectiveSheavesRestrictOnto.lean#L192).

> An injective sheaf of modules has surjective restriction maps.

```lean
public theorem injective_restriction_surjective
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{v})
    (I : SheafOfModules.{w} R) [Injective I]
    {U' U : Opens X} (h : U' ≤ U) :
    Function.Surjective (I.val.presheaf.map (homOfLE h).op)
```

## Tag 01EB, a lemma

[Tag 01EB](https://stacks.math.columbia.edu/tag/01EB) in the Stacks Project.

**`Stacks.Cohomology.AbsoluteMayerVietoris.mayerVietoris_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MayerVietorisHgroup/Basic.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MayerVietorisHgroup/Basic.lean#L512). The attribute's comment: “in the right-derived model `Hgroup`”.

> **Stacks Project, Tag 01EB (Mayer--Vietoris), in the right-derived model of cohomology.**
> Every six-term window
> `H^n(X,F) ⟶ H^n(U,F) ⊞ H^n(V,F) ⟶ H^n(U ⊓ V,F) ⟶ H^\{n+1}(X,F) ⟶ H^\{n+1}(U,F) ⊞ H^\{n+1}(V,F)
> ⟶ H^\{n+1}(U ⊓ V,F)` of the Mayer--Vietoris sequence is exact.  The two outer maps are the
> restriction maps, by `mvFirst_eq` and `mvSecond_eq`.

```lean
public theorem mayerVietoris_exact (n : ℕ) (F : SheafOfModules.{u} O) :
    (ComposableArrows.mk₅ ((mvFirst O U V n).app F) ((mvSecond O U V n).app F)
      ((mvDelta O U V hUV n).app F) ((mvFirst O U V (n + 1)).app F)
      ((mvSecond O U V (n + 1)).app F)).Exact
```

**`Stacks.Cohomology.AbsoluteMayerVietoris.mono_mvFirst_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MayerVietorisHgroup/Basic.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MayerVietorisHgroup/Basic.lean#L558). The attribute's comment: “the leading zero, in the right-derived model `Hgroup`”.

> **The Mayer--Vietoris sequence starts with a zero**: the pair of restriction maps
> `H⁰(X,F) ⟶ H⁰(U,F) ⊞ H⁰(V,F)` is a monomorphism.

```lean
public theorem mono_mvFirst_zero (F : SheafOfModules.{u} O) :
    Mono ((mvFirst O U V 0).app F)
```

**`Stacks.Cohomology.MayerVietoris.mayerVietorisInitialSequence_exact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LongExactSequence.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LongExactSequence.lean#L87). The attribute's comment: “initial segment”.

> The Mayer--Vietoris sequence is exact at its initial segment, including the leading zero.

```lean
lemma mayerVietorisInitialSequence_exact :
    (mayerVietorisInitialSequence S F).Exact
```

**`Stacks.Cohomology.MayerVietoris.mayerVietoris_delta_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LongExactSequence.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LongExactSequence.lean#L129). The attribute's comment: “functoriality”.

> The connecting morphisms in the Mayer--Vietoris long exact sequence are natural in the
> coefficient sheaf.

```lean
lemma mayerVietoris_delta_naturality {G : Sheaf J AddCommGrpCat.{v}} (f : F ⟶ G)
    (n₀ n₁ : ℕ) (h : n₀ + 1 = n₁) :
    S.δ F n₀ n₁ h ≫ ((Sheaf.cohomologyPresheafFunctor J n₁).map f).app (op S.X₄) =
      ((Sheaf.cohomologyPresheafFunctor J n₀).map f).app (op S.X₁) ≫ S.δ G n₀ n₁ h
```

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.MayerVietorisSquare.sequence_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.MayerVietorisSquare.sequence_exact#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LongExactSequence.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/MayerVietoris/LongExactSequence.lean#L141) (StacksFrontier): “successive windows”.

## Tag 01EC, a lemma

[Tag 01EC](https://stacks.math.columbia.edu/tag/01EC) in the Stacks Project.

**`Stacks.Cohomology.RelativeMayerVietoris.relativeMayerVietoris`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/LongExactSequence.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/LongExactSequence.lean#L395).

> For a morphism `f : X → Y`, two open subspaces covering `X`, and their intersection, the
> higher direct images of every module fit into a long exact Mayer--Vietoris sequence, naturally
> in the module.

```lean
public theorem relativeMayerVietoris
    (iU : U ⟶ X) (iV : V ⟶ X) (iW : W ⟶ X)
    [SheafedSpace.IsOpenImmersion iU] [SheafedSpace.IsOpenImmersion iV]
    [SheafedSpace.IsOpenImmersion iW]
    (cover : Set.range iU.hom.base ∪ Set.range iV.hom.base = Set.univ)
    (intersection : Set.range iW.hom.base =
      Set.range iU.hom.base ∩ Set.range iV.hom.base) :
    Nonempty (RelativeMayerVietorisSequence f iU iV iW)
```

**`Stacks.Cohomology.RelativeMayerVietoris.relativeMayerVietorisPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/LongExactSequence.lean, line 701](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/RelativeMayerVietoris/LongExactSequence.lean#L701). The attribute's comment: “bounded-below integer-indexed sequence”.

> The bounded below higher direct images of a module and of its restrictions to a two-open
> cover and to the intersection form a functorial long exact sequence indexed by the integers.

```lean
public theorem relativeMayerVietorisPlus
    (iU : U ⟶ X) (iV : V ⟶ X) (iW : W ⟶ X)
    [SheafedSpace.IsOpenImmersion iU] [SheafedSpace.IsOpenImmersion iV]
    [SheafedSpace.IsOpenImmersion iW]
    (cover : Set.range iU.hom.base ∪ Set.range iV.hom.base = Set.univ)
    (intersection : Set.range iW.hom.base =
      Set.range iU.hom.base ∩ Set.range iV.hom.base) :
    Nonempty (RelativeMayerVietorisSequencePlus f iU iV iW)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.8, Tag 01E9](https://stacks.math.columbia.edu/tag/01E9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
