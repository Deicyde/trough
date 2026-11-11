---
declaration: section
origin: cited
lean: exists_covBounded_isSite
statement: formalized
proof: formalized
---

# 3.11 Coverings of a site

Section 3.11 of the Stacks Project, [Tag 000W](https://stacks.math.columbia.edu/tag/000W). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 000X, a lemma

[Tag 000X](https://stacks.math.columbia.edu/tag/000X) in the Stacks Project.

**`exists_covBounded_isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SmallSubsite.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pretopology/SmallSubsite.lean#L296).

> **Stacks 000X**. Let `IsCov` be a site on `C` and let `Cov₀` be a set-sized family of
> coverings in it. Then there are a cardinal `κ` and a limit ordinal `α` such that the coverings
> in `IsCov` whose index set has cardinality at most `κ` again form a site, contain `Cov₀`, and
> every covering in `IsCov` is combinatorially equivalent to one of them. One may take
> `κ = ℵ₀ ⊔ κ₀ ⊔ κ_rep`, with `κ₀` bounding the index sets of `Cov₀` and `κ_rep` bounding those
> of a system of combinatorial representatives, and `α = ω`.

```lean
theorem exists_covBounded_isSite
    {C : Type u} [Category.{v} C]
    (IsCov : Covering.{u, v, max u v} C → Prop)
    (hSite : IsSite IsCov)
    (Cov₀ : Set (Covering.{u, v, max u v} C))
    [hSmall : Small.{max u v} Cov₀]
    (hCov₀ : ∀ 𝒰 ∈ Cov₀, IsCov 𝒰) :
    ∃ (κ : Cardinal.{max u v}) (α : Ordinal.{max u v}),
      Order.IsSuccLimit α ∧
      (∀ 𝒰 ∈ Cov₀, CovBounded IsCov κ 𝒰) ∧
      IsSite (CovBounded IsCov κ) ∧
      (∀ 𝒰 : Covering C, IsCov 𝒰 →
        ∃ 𝒰' : Covering C,
          CovBounded IsCov κ 𝒰' ∧ Covering.CombEquiv 𝒰 𝒰')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 3.11, Tag 000W](https://stacks.math.columbia.edu/tag/000W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
