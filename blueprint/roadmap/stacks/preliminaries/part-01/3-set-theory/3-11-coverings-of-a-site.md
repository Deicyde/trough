---
declaration: section
origin: cited
lean: exists_covTrunc_isSite
statement: formalized
proof: formalized
---

# 3.11 Coverings of a site

Section 3.11 of the Stacks Project, [Tag 000W](https://stacks.math.columbia.edu/tag/000W). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 000X, a lemma

[Tag 000X](https://stacks.math.columbia.edu/tag/000X) in the Stacks Project.

**`exists_covTrunc_isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SmallSubsiteTruncated.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SmallSubsiteTruncated.lean#L160). The attribute's comment: “The stage `V_α` of the von Neumann hierarchy is modelled by a small collection `𝒯` of index types closed under the one-point type and `Σ`-types, as a Lean type has no rank; the truncated class is proved `Small`.”.

> **Stacks 000X**. Let `IsCov` be a site on `C` and let `Cov₀` be a set of coverings in it.
> Then there are an (infinite) cardinal `κ` and a small collection `𝒯` of index types, standing for
> the stage `V_α` of the von Neumann hierarchy, such that the class `Cov(C)_{κ, 𝒯}` of coverings in
> `IsCov` with index set in `𝒯` of cardinality at most `κ` is a *set*, contains `Cov₀`, satisfies
> the site axioms, and contains a combinatorially equivalent copy of every covering in `IsCov`.
>
> The collection `𝒯` does the work of the limit ordinal `α`: it is closed under the one-point type
> and under `Σ`-types of families of its members, which is what the composition and isomorphism
> axioms need. The index sets live in a universe `Type (max u v w)` at least as large as that of the
> objects and morphisms of `C`; `w = 0` is the case `Type (max u v)` of `exists_covBounded_isSite`.

```lean
theorem exists_covTrunc_isSite
    {C : Type u} [Category.{v} C]
    (IsCov : Covering.{u, v, max u v w} C → Prop)
    (hSite : IsSite IsCov)
    (Cov₀ : Set (Covering.{u, v, max u v w} C))
    [Small.{max u v w} Cov₀]
    (hCov₀ : ∀ 𝒰 ∈ Cov₀, IsCov 𝒰) :
    ∃ (κ : Cardinal.{max u v w}) (𝒯 : Set (Type (max u v w))),
      ℵ₀ ≤ κ ∧ Small.{max u v w} 𝒯 ∧
      Small.{max u v w} {𝒰 // CovTrunc IsCov κ 𝒯 𝒰} ∧
      (∀ 𝒰 ∈ Cov₀, CovTrunc IsCov κ 𝒯 𝒰) ∧
      IsSite (CovTrunc IsCov κ 𝒯) ∧
      (∀ 𝒰 : Covering C, IsCov 𝒰 →
        ∃ 𝒰' : Covering C, CovTrunc IsCov κ 𝒯 𝒰' ∧ Covering.CombEquiv 𝒰 𝒰')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.11, Tag 000W](https://stacks.math.columbia.edu/tag/000W)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
