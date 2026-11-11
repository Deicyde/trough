---
declaration: section
origin: cited
lean: Deformation.exists_minimal_preimage, Deformation.isMinimal_descentPushforward, Deformation.exists_smallestDescent, Deformation.isVersal_smallestDescent, Deformation.exists_mvPowerSeries_algEquiv_of_smallestDescent, Deformation.IsMinimalVersal, Deformation.exists_minimalVersalFormalObject, Deformation.exists_minimalVersal_powerSeries
statement: formalized
proof: formalized
---

# 90.14 Minimal versal formal objects

Section 90.14 of the Stacks Project, [Tag 06T0](https://stacks.math.columbia.edu/tag/06T0). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06T1, a lemma

[Tag 06T1](https://stacks.math.columbia.edu/tag/06T1) in the Stacks Project.

**`Deformation.exists_minimal_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/MinimalDescent.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/MinimalDescent.lean#L195). The attribute's comment: “minimality\_lifted”.

> Every minimal descent object of `x` is, up to isomorphism, the image of a
> minimal descent object of `y` when `y ⟶ x` lies over a surjection and (S1)
> holds.

```lean
theorem exists_minimal_preimage
    {Λ : Type u} {k : Type w} [CommRing Λ] [IsNoetherianRing Λ]
    [Field k] [Algebra Λ k] [Module.Finite Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (hS1 : SchlessingerConditionS1 p)
    {y x : F} (g : y ⟶ x)
    (hg : Function.Surjective (p.map g).hom)
    (X : DescentObject p x) (hX : IsMinimalObject X) :
    ∃ Y : DescentObject p y,
      IsMinimalObject Y ∧ Nonempty ((descentPushforward p hp g).functor.obj Y ≅ X)
```

**`Deformation.isMinimal_descentPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/VersalObject/MinimalDescent.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/VersalObject/MinimalDescent.lean#L280). The attribute's comment: “minimality\_preserved”.

> Pushforward along a morphism preserves minimal descent objects under (S1).

```lean
theorem isMinimal_descentPushforward
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (hS1 : SchlessingerConditionS1 p)
    {y x : F} (g : y ⟶ x)
    (X : DescentObject p y)
    (hX : IsMinimalObject X) :
    IsMinimalObject
      ((descentPushforward p hp g).functor.obj X)
```

## Tag 06T2, a lemma

[Tag 06T2](https://stacks.math.columbia.edu/tag/06T2) in the Stacks Project.

**`Deformation.exists_smallestDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/MinimalVersal/Existence.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/MinimalVersal/Existence.lean#L44).

> **Stacks Project, Tag 06T2.** A versal formal object of a category cofibered in groupoids
> satisfying (S1) admits a smallest formal descent: a descent over a complete local subalgebra of
> its base that stays minimal after every Artinian base change and admits no proper further
> descent.

```lean
public theorem exists_smallestDescent
    [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hp : IsCofiberedInGroupoids p)
    (hS1 : SchlessingerConditionS1 p)
    (ξ : FormalObject p) (hξ : IsVersal hp ξ) :
    Nonempty (SmallestDescent ξ)
```

## Tag 06T3, a lemma

[Tag 06T3](https://stacks.math.columbia.edu/tag/06T3) in the Stacks Project.

**`Deformation.isVersal_smallestDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/MinimalVersal/DescentVersality.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/MinimalVersal/DescentVersality.lean#L65). The attribute's comment: “descended object versal”.

> A smallest descent of a versal formal object of a category cofibered in groupoids is again a
> versal formal object.

```lean
public theorem isVersal_smallestDescent
    (hp : IsCofiberedInGroupoids p) {ξ : FormalObject p} (hξ : IsVersal hp ξ)
    (d : SmallestDescent ξ) : IsVersal hp d.object
```

**`Deformation.exists_mvPowerSeries_algEquiv_of_smallestDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/MinimalVersal/PowerSeriesDecomposition.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/MinimalVersal/PowerSeriesDecomposition.lean#L519). The attribute's comment: “power series decomposition”. References: SGA 7 VI (2.10), “smallest descent case”.

> **Stacks Project, Tag 06T3.** The base of a versal formal object is a power series algebra
> over the base of a smallest descent of it, compatibly with the descended-base inclusion: the
> isomorphism carries a constant to the image of its coefficient.

```lean
public theorem exists_mvPowerSeries_algEquiv_of_smallestDescent
    (hp : IsCofiberedInGroupoids p) (ξ : FormalObject p) (hξ : IsVersal hp ξ)
    (d : SmallestDescent ξ) :
    ∃ r : ℕ, ∃ e : MvPowerSeries (Fin r) d.object.base ≃ₐ[Λ] ξ.base,
      ∀ a : d.object.base, e (MvPowerSeries.C a) = d.inclusion.base.hom a
```

## Tag 06T4, a definition

[Tag 06T4](https://stacks.math.columbia.edu/tag/06T4) in the Stacks Project.

**`Deformation.IsMinimalVersal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/MinimalVersal.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/MinimalVersal.lean#L45). References: SGA 7 VI (1.19), “(2)”.

> A formal object is minimal versal if it is versal and every morphism from a
> formal object into it is surjective on its underlying complete local algebra.

```lean
public abbrev IsMinimalVersal (hp : IsCofiberedInGroupoids p)
    (ξ : FormalObject p) : Prop
```

## Tag 06T5, a lemma

[Tag 06T5](https://stacks.math.columbia.edu/tag/06T5) in the Stacks Project.

**`Deformation.exists_minimalVersalFormalObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/MinimalExistence.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/VersalObject/MinimalExistence.lean#L52). The attribute's comment: “existence”.

> **Stacks 06T5.** A predeformation category with a versal formal object has a minimal
> versal formal object: a smallest descent of the given versal object is one.

```lean
public theorem exists_minimalVersalFormalObject (hp : IsPredeformationCategory p)
    (hξ : ∃ ξ : FormalObject p, IsVersal hp.cofibered ξ) :
    ∃ ξ : FormalObject p, IsMinimalVersal hp.cofibered ξ
```

**`Deformation.exists_minimalVersal_powerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/MinimalPowerSeries.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/VersalObject/MinimalPowerSeries.lean#L62). The attribute's comment: “power\_series\_extension”.

> **Stacks 06T5.** Any versal formal object `ξ` of a predeformation category is the
> pushforward of a minimal versal formal object `η` along a power series ring extension: there is
> a morphism `η ⟶ ξ` which is strongly cocartesian over its base map, and an isomorphism of
> `Λ`-algebras `η.base[[x_1, …, x_r]] ≃ ξ.base` carrying a constant to the image of its
> coefficient under that base map.

```lean
public theorem exists_minimalVersal_powerSeries [IsNoetherianRing Λ] [Module.Finite Λ k]
    (hp : IsPredeformationCategory p) (ξ : FormalObject p) (hξ : IsVersal hp.cofibered ξ) :
    ∃ η : FormalObject p, ∃ f : η ⟶ ξ, IsMinimalVersal hp.cofibered η ∧
      (FormalObject.projection (p := p)).IsStronglyCocartesian f.base f ∧
      ∃ r : ℕ, ∃ e : MvPowerSeries (Fin r) η.base ≃ₐ[Λ] ξ.base,
        ∀ a : η.base, e (MvPowerSeries.C a) = f.base.hom a
```

**`Deformation.isomorphic_of_isMinimalVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/MinimalUniqueness.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/VersalObject/MinimalUniqueness.lean#L46). The attribute's comment: “uniqueness”. References: SGA 7 VI (1.20), “uniqueness”; SGA 7 VI (1.10), “(ii) uniqueness”.

> Any two minimal versal formal objects are isomorphic.

```lean
public theorem isomorphic_of_isMinimalVersal (hp : IsPredeformationCategory p)
    (ξ η : FormalObject p) (hξ : IsMinimalVersal hp.cofibered ξ)
    (hη : IsMinimalVersal hp.cofibered η) :
    Nonempty (ξ ≅ η)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.14, Tag 06T0](https://stacks.math.columbia.edu/tag/06T0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
