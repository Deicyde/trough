---
declaration: section
origin: cited
lean: SheafToposMorphism, SheafToposMorphism.comp, CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi
statement: formalized
proof: formalized
---

# 7.15 Topoi

Section 7.15 of the Stacks Project, [Tag 00X9](https://stacks.math.columbia.edu/tag/00X9). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00XA, a definition

[Tag 00XA](https://stacks.math.columbia.edu/tag/00XA) in the Stacks Project.

**`SheafToposMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposDefs.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/ToposDefs.lean#L38). The attribute's comment: “(1); the composition (2) is `SheafToposMorphism.comp`”.

> **Stacks 00XA (1).** Let `(C, J)` and `(D, K)` be sites. A *morphism of topoi* `f` from
> `Sh(D)` to `Sh(C)` is a pair of functors `f_* : Sh(D) ⥤ Sh(C)` and `f⁻¹ : Sh(C) ⥤ Sh(D)`
> together with an adjunction `f⁻¹ ⊣ f_*` (that is, `Mor(f⁻¹ G, F) = Mor(G, f_* F)` bifunctorially)
> such that `f⁻¹` commutes with finite limits. Here `Sh(C)` is the category of sheaves of sets
> `Sheaf J (Type w)`; the fields are `pushforward` (`f_*`), `inverseImage` (`f⁻¹`), `adj` and
> `preservesFiniteLimits` of `MorphismOfTopoi`.

```lean
abbrev SheafToposMorphism {C : Type u₁} [Category.{v₁} C] (J : GrothendieckTopology C)
    {D : Type u₂} [Category.{v₂} D] (K : GrothendieckTopology D)
```

**`SheafToposMorphism.comp`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposDefs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/ToposDefs.lean#L53). The attribute's comment: “(2)”.

> **Stacks 00XA (2).** Given morphisms of topoi `f : Sh(D) → Sh(C)` and `g : Sh(E) → Sh(D)`,
> the composition `f ∘ g : Sh(E) → Sh(C)` is the morphism of topoi given by the functors
> `(f ∘ g)_* = f_* ∘ g_*` and `(f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹` (see `pushforward_comp` and
> `inverseImage_comp`).

```lean
abbrev comp (f : SheafToposMorphism.{w} J K) (g : SheafToposMorphism.{w} K L) :
    SheafToposMorphism.{w} J L
```

## Tag 00XC, a lemma

[Tag 00XC](https://stacks.math.columbia.edu/tag/00XC) in the Stacks Project.

**`CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/MorphismOfTopoi.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/MorphismOfTopoi.lean#L99).

> Given a morphism of sites `f : D → C`, i.e. a continuous functor `u : C ⥤ D` whose associated
> functor `u_s` on sheaves of sets is exact, the pair `(f⁻¹ = u_s, f_* = u^s)` is a morphism of topoi
> `Sh(D) → Sh(C)`. Here `u_s` is `Functor.sheafPullback`, `u^s` is
> `Functor.sheafPushforwardContinuous` and the adjunction is `Functor.sheafAdjunctionContinuous`.

```lean
noncomputable def CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi
    {C : Type w} [SmallCategory C] {D : Type w} [SmallCategory D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D} {u : C ⥤ D}
    (h : u.IsMorphismOfSites J K) :
    MorphismOfTopoi (Sheaf K (Type w)) (Sheaf J (Type w))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.15, Tag 00X9](https://stacks.math.columbia.edu/tag/00X9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
