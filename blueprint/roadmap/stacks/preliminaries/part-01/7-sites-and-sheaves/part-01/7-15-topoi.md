---
declaration: section
origin: cited
lean: LeftAdjointsPreserveFiniteLimits, CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi
statement: formalized
proof: formalized
---

# 7.15 Topoi

Section 7.15 of the Stacks Project, [Tag 00X9](https://stacks.math.columbia.edu/tag/00X9). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00XA, a definition

[Tag 00XA](https://stacks.math.columbia.edu/tag/00XA) in the Stacks Project.

**`LeftAdjointsPreserveFiniteLimits`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/ToposDefs.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/ToposDefs.lean#L25).

> **Stacks 00XA.** A *topos* is a category `Sheaf J A` of sheaves on a site, and a *morphism of
> topoi* `f` from `Sheaf K A` to `Sheaf J A` is a pair of functors `f_* : Sheaf K A ⥤ Sheaf J A` and
> `f⁻¹ : Sheaf J A ⥤ Sheaf K A` such that `f⁻¹ ⊣ f_*` bifunctorially and `f⁻¹` is left exact. This
> records the second requirement: the left adjoint of such a pair preserves finite limits.

```lean
def LeftAdjointsPreserveFiniteLimits (C : Type*) [Category C] (J : GrothendieckTopology C)
    (D : Type*) [Category D] (K : GrothendieckTopology D)
    (A : Type*) [Category A] : Prop
```

## Tag 00XC, a lemma

[Tag 00XC](https://stacks.math.columbia.edu/tag/00XC) in the Stacks Project.

**`CategoryTheory.Functor.IsMorphismOfSites.morphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/MorphismOfTopoi.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Topos/MorphismOfTopoi.lean#L99).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
