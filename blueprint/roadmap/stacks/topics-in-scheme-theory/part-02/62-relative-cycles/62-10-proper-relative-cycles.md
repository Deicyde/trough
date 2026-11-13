---
declaration: section
origin: cited
lean: Stacks.Chow.IsProperRelativeCycle, Stacks.Chow.properRelativeCycles, Stacks.Chow.isProperRelativeCycle_baseChangeFamily, Stacks.Chow.isProperRelativeCycle_iff_forall_baseChangeFamily
statement: formalized
proof: formalized
---

# 62.10 Proper relative cycles

Section 62.10 of the Stacks Project, [Tag 0H60](https://stacks.math.columbia.edu/tag/0H60). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H61, a definition

[Tag 0H61](https://stacks.math.columbia.edu/tag/0H61) in the Stacks Project.

**`Stacks.Chow.IsProperRelativeCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperRelativeCycles.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperRelativeCycles.lean#L135). The attribute's comment: “the predicate”.

> **Stacks Project, Definition 0H61.** A family `α` of `r`-cycles on the fibres of `X/S` has
> proper support when its support is contained in a closed subset `W ⊆ X` proper over `S`; a
> relative `r`-cycle with this property is a *proper relative cycle*.

```lean
def IsProperRelativeCycle {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (r : ℕ)
    (α : FamilyOfCycles f r) : Prop
```

**`Stacks.Chow.properRelativeCycles`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperRelativeCycles.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperRelativeCycles.lean#L169). The attribute's comment: “the group c(X/S, r) of proper relative cycles”.

> **Stacks Project, Definition 0H61.** The group `c(X/S, r)` of proper relative `r`-cycles on
> `X/S`: the subgroup of the group of families of `r`-cycles on the fibres of `X/S` whose members
> are the relative `r`-cycles with support contained in a closed subset proper over `S`.

```lean
def properRelativeCycles {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsLocallyNoetherian S] (r : ℕ) : AddSubgroup (FamilyOfCycles f r)
```

## Tag 0H62, a lemma

[Tag 0H62](https://stacks.math.columbia.edu/tag/0H62) in the Stacks Project.

**`Stacks.Chow.isProperRelativeCycle_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperRelativeCycles.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperRelativeCycles.lean#L211).

> **Stacks Project, Lemma 0H62.** Let `S` be locally Noetherian, let `f : X ⟶ S` be locally of
> finite type and let `α` be a relative `r`-cycle on `X/S`. If `α` is proper, then every base
> change of `α` along a morphism `S' ⟶ S` is proper.

```lean
theorem isProperRelativeCycle_baseChangeFamily {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) {α : FamilyOfCycles f r}
    (hα : α ∈ properRelativeCycles f r) :
    ∀ (S' : Scheme.{u}) (g : S' ⟶ S),
      IsProperRelativeCycle (pullback.snd f g) r (baseChangeFamily f g r α)
```

## Tag 0H63, a lemma

[Tag 0H63](https://stacks.math.columbia.edu/tag/0H63) in the Stacks Project.

**`Stacks.Chow.isProperRelativeCycle_iff_forall_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperHDescent.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ProperHDescent.lean#L264).

> **Stacks Project, Lemma 0H63.** Let `S` be locally Noetherian, let `f : X ⟶ S` be locally of
> finite type and let `α` be a family of `r`-cycles on the fibres of `X/S`. Let `{g i : S i ⟶ S}`
> be an h covering. Then `α` is a proper relative cycle if and only if each base change
> `(g i)^*α` is a proper relative cycle.
>
> Properness of a relative cycle is a condition on its support alone, so neither the valuative
> condition defining a relative `r`-cycle nor any hypothesis on the members of the covering beyond
> the h-covering condition enters.

```lean
theorem isProperRelativeCycle_iff_forall_baseChangeFamily {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsLocallyNoetherian S] (r : ℕ) (α : FamilyOfCycles f r)
    {I : Type v} (S' : I → Scheme.{u}) (g : ∀ i, S' i ⟶ S) (hg : IsHCovering S' g) :
    IsProperRelativeCycle f r α ↔
      ∀ i, IsProperRelativeCycle (pullback.snd f (g i)) r (baseChangeFamily f (g i) r α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.10, Tag 0H60](https://stacks.math.columbia.edu/tag/0H60)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
