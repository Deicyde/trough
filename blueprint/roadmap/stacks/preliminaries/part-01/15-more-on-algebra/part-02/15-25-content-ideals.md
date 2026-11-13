---
declaration: section
origin: cited
lean: IsContentIdeal, contentIdeal_fg, isContentIdeal_map_of_injective_mapQ_maximalIdeal, exists_isContentIdeal_of_flat_isMittagLeffler
statement: formalized
proof: formalized
---

# 15.25 Content ideals

Section 15.25 of the Stacks Project, [Tag 0AS9](https://stacks.math.columbia.edu/tag/0AS9). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ASA, a definition

[Tag 0ASA](https://stacks.math.columbia.edu/tag/0ASA) in the Stacks Project.

**`IsContentIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ContentIdeal.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ContentIdeal.lean#L58). References: SGA 3 XXII (5.1.1), “more general”.

> `I₀` is a *content ideal* of `x`: it is the least element of `S_x` under inclusion,
> i.e. `x ∈ I₀ M` and any ideal `I` with `x ∈ I M` contains `I₀`. Here the submodule `I M`
> of `M` is spelled `I • (⊤ : Submodule A M)`.
>
> Flatness of `M` is not needed to state this, so the predicate is given for an arbitrary
> module; for a flat module it is exactly the source's definition.

```lean
def IsContentIdeal (x : M) (I₀ : Ideal A) : Prop
```

## Tag 0ASB, a lemma

[Tag 0ASB](https://stacks.math.columbia.edu/tag/0ASB) in the Stacks Project.

**`contentIdeal_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ContentIdeal.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ContentIdeal.lean#L95).

> **Stacks Tag 0ASB.** If a content ideal `I₀` of `x` exists, then `I₀` is finitely
> generated.
>
> The source states this for a flat module `M`, but flatness is never used: the content ideal is
> by definition the least ideal `I` with `x ∈ I M`, and `x ∈ I₀ M` already exhibits `x` inside
> `J M` for some finitely generated `J ≤ I₀`, whence `J = I₀` by minimality. The hypothesis is
> therefore dropped, which only strengthens the statement.

```lean
theorem contentIdeal_fg {A : Type*} [CommRing A] {M : Type*} [AddCommGroup M] [Module A M]
    (x : M) (I₀ : Ideal A) (h : IsContentIdeal x I₀) :
    I₀.FG
```

## Tag 0ASC, a lemma

[Tag 0ASC](https://stacks.math.columbia.edu/tag/0ASC) in the Stacks Project.

**`isContentIdeal_map_of_injective_mapQ_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ContentIdeal.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ContentIdeal.lean#L276).

> **Stacks Tag 0ASC.** A map between flat modules over a local ring which is injective modulo
> the maximal ideal preserves content ideals of elements.

```lean
theorem isContentIdeal_map_of_injective_mapQ_maximalIdeal
    {A : Type*} [CommRing A] [IsLocalRing A]
    {M N : Type*} [AddCommGroup M] [Module A M] [Module.Flat A M]
    [AddCommGroup N] [Module A N] [Module.Flat A N]
    (u : M →ₗ[A] N)
    (hu : Function.Injective
      (Submodule.mapQ (maximalIdeal A • (⊤ : Submodule A M))
        (maximalIdeal A • (⊤ : Submodule A N)) u
        (Submodule.smul_top_le_comap_smul_top (maximalIdeal A) u)))
    {x : M} {I : Ideal A} (hx : IsContentIdeal x I) :
    IsContentIdeal (u x) I
```

## Tag 0ASD, a lemma

[Tag 0ASD](https://stacks.math.columbia.edu/tag/0ASD) in the Stacks Project.

**`exists_isContentIdeal_of_flat_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ContentIdeal.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ContentIdeal.lean#L439).

> **Stacks Tag 0ASD.** Every element of a flat Mittag-Leffler module has a content ideal.

```lean
theorem exists_isContentIdeal_of_flat_isMittagLeffler
    {A : Type u} [CommRing A]
    {M : Type v} [AddCommGroup M] [Module A M]
    [Module.Flat A M]
    (hM : IsMittagLeffler.{u, max u v, v, max u v, max u v} A M) (x : M) :
    ∃ I : Ideal A, IsContentIdeal x I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.25, Tag 0AS9](https://stacks.math.columbia.edu/tag/0AS9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
