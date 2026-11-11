---
declaration: section
origin: cited
lean: CategoryTheory.IsGrothendieckAbelian.tensorObjPreadditiveCoyonedaObjAdjunction, Stacks.Injectives.mono_homEquiv_symm_of_mono, Stacks.Injectives.preadditiveCoyonedaObjFullyFaithful, Stacks.Injectives.preservesFiniteLimits_and_preservesFiniteColimits_tensorObj, Stacks.Injectives.gabriel_popescu, Stacks.Injectives.exists_derivedGabrielPopescuData
statement: formalized
proof: formalized
---

# 19.14 The Gabriel-Popescu theorem

Section 19.14 of the Stacks Project, [Tag 0F5R](https://stacks.math.columbia.edu/tag/0F5R). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F5S, a lemma

[Tag 0F5S](https://stacks.math.columbia.edu/tag/0F5S) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsGrothendieckAbelian.tensorObjPreadditiveCoyonedaObjAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsGrothendieckAbelian.tensorObjPreadditiveCoyonedaObjAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch19.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch19.lean#L24) (StacksFrontier): “the left adjoint `- ⊗ G` of `Hom(G, -)` into right `End(G)`-modules”.

## Tag 0F5T, a lemma

[Tag 0F5T](https://stacks.math.columbia.edu/tag/0F5T) in the Stacks Project.

**`Stacks.Injectives.mono_homEquiv_symm_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/GabrielPopescuMono.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/GabrielPopescuMono.lean#L29).

> Let `G` be a separator of a Grothendieck abelian category. If a map of
> `(End G)ᵐᵒᵖ`-modules `f : M ⟶ Hom(G, A)` is a monomorphism, equivalently injective, then the
> map `M ⊗ G ⟶ A` adjoint to it is a monomorphism as well.

```lean
theorem mono_homEquiv_symm_of_mono (G : C) (hG : IsSeparator G)
    {M : ModuleCat (End G)ᵐᵒᵖ} {A : C} (f : M ⟶ (preadditiveCoyonedaObj G).obj A) (hf : Mono f) :
    Mono (((tensorObjPreadditiveCoyonedaObjAdjunction G).homEquiv M A).symm f)
```

## Tag 0F5U, a theorem

[Tag 0F5U](https://stacks.math.columbia.edu/tag/0F5U) in the Stacks Project.

**`Stacks.Injectives.preadditiveCoyonedaObjFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean#L32). The attribute's comment: “(2) for the constructed functor `Hom(G, -)`”.

> Let `G` be a separator of a Grothendieck abelian category `C`. The embedding
> `Hom(G, -) : C ⥤ Mod (End G)ᵐᵒᵖ` is fully faithful.

```lean
noncomputable def preadditiveCoyonedaObjFullyFaithful (G : C) (hG : IsSeparator G) :
    (preadditiveCoyonedaObj G).FullyFaithful
```

**`Stacks.Injectives.preservesFiniteLimits_and_preservesFiniteColimits_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean#L43). The attribute's comment: “(3) for the constructed functor `- ⊗ G`”.

> Let `G` be a separator of a Grothendieck abelian category `C`. The left adjoint
> `- ⊗ G : Mod (End G)ᵐᵒᵖ ⥤ C` of the embedding `Hom(G, -)` is exact: it preserves finite
> limits, and it preserves finite colimits because it is a left adjoint.

```lean
theorem preservesFiniteLimits_and_preservesFiniteColimits_tensorObj (G : C)
    (hG : IsSeparator G) :
    PreservesFiniteLimits (tensorObj G) ∧ PreservesFiniteColimits (tensorObj G)
```

**`Stacks.Injectives.gabriel_popescu`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean#L52).

> **The Gabriel--Popescu theorem.** For a Grothendieck abelian category `C` there is a
> possibly noncommutative ring `R` together with functors `G : C ⥤ Mod R` and `F : Mod R ⥤ C`
> such that `F` is left adjoint to `G`, `G` is fully faithful, and `F` is exact.

```lean
theorem gabriel_popescu (C : Type u) [Category.{v} C] [Abelian C]
    [IsGrothendieckAbelian.{v} C] :
    ∃ (R : Type v) (_ : Ring R) (G : C ⥤ ModuleCat.{v} R) (F : ModuleCat.{v} R ⥤ C),
      Nonempty (F ⊣ G) ∧ G.Full ∧ G.Faithful ∧
        PreservesFiniteLimits F ∧ PreservesFiniteColimits F
```

Declarations registered for the tag:

- [`CategoryTheory.IsGrothendieckAbelian.tensorObjPreadditiveCoyonedaObjAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsGrothendieckAbelian.tensorObjPreadditiveCoyonedaObjAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/GabrielPopescuEmbedding.lean#L26) (StacksFrontier): “(1) for the constructed functors: `- ⊗ G` is left adjoint to `Hom(G, -)`”.

## Tag 0F5V, a lemma

[Tag 0F5V](https://stacks.math.columbia.edu/tag/0F5V) in the Stacks Project.

**`Stacks.Injectives.exists_derivedGabrielPopescuData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/GabrielPopescu.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/GabrielPopescu.lean#L270).

> **Stacks 0F5V (Gabriel--Popescu on derived categories).** The
> Gabriel--Popescu embedding of a Grothendieck abelian category admits a fully
> faithful right derived functor.  Its left adjoint is induced by the exact
> Gabriel--Popescu left adjoint, and the counit is an isomorphism.

```lean
theorem exists_derivedGabrielPopescuData (G : C) (hG : IsSeparator G) :
    Nonempty (DerivedGabrielPopescuData G hG)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.14, Tag 0F5R](https://stacks.math.columbia.edu/tag/0F5R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
