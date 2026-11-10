---
declaration: section
origin: cited
lean: AlgebraicGeometry.hasChowModification_of_compactSpace_quasiSeparatedSpace, AlgebraicGeometry.hasDenseChowModification_of_finite_irreducibleComponents
statement: formalized
proof: formalized
---

# 32.12 Variants of Chow's Lemma

Section 32.12 of the Stacks Project, [Tag 01ZZ](https://stacks.math.columbia.edu/tag/01ZZ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0202, a lemma

[Tag 0202](https://stacks.math.columbia.edu/tag/0202) in the Stacks Project.

**`AlgebraicGeometry.hasChowModification_of_compactSpace_quasiSeparatedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowQcqs/Basic.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ChowQcqs/Basic.lean#L266). References: SGA 4 XVII (7.0.6), “(i), (iii)”; SGA 4 XII (7.1), “Chow diagram”.

> **Chow's lemma over a quasi-compact quasi-separated base.** A separated morphism of finite
> type onto a quasi-compact quasi-separated scheme admits a proper surjective modification immersed
> in a projective space over the base.

```lean
theorem hasChowModification_of_compactSpace_quasiSeparatedSpace {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] : HasChowModification f
```

## Tag 0203, a lemma

[Tag 0203](https://stacks.math.columbia.edu/tag/0203) in the Stacks Project.

**`AlgebraicGeometry.hasDenseChowModification_of_finite_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowQcqs/Basic.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ChowQcqs/Basic.lean#L302). References: EGA II (5.6.1), “(b); (i),(ii)”; SGA 4 XVII (7.0.6), “finite irred. components”; SGA 4 XII (7.1), “finite irred. components”.

> **[Stacks, Tag 0203]: the variant of Chow's lemma with a dense open.** Let `S` be
> quasi-compact and quasi-separated, let `f : X ⟶ S` be separated and of finite type, and suppose
> `X` has only finitely many irreducible components. Then there are `n`, a scheme `X'`, a proper
> surjective `π : X' ⟶ X` and an immersion `X' ⟶ ℙⁿ_S` making the triangle over `S` commute, such
> that `π` is an isomorphism over a dense open subscheme of `X`.
>
> The dense open does not survive base change, so unlike [Stacks, Tag 0202] this cannot be had by
> descending `X` to a stage and pulling the modification back. Instead the whole inverse system
> `Yⱼ = Sⱼ ×_{S_{i₁}} Y₁` is kept, Chow's lemma over a Noetherian base is applied to the
> **scheme-theoretic image** of `X` in a stage chosen so that the finitely many generic points of
> `X` have pairwise non-specializing images, and the dense open of that image then pulls back to a
> dense open of `X` because it contains every generic point.

```lean
theorem hasDenseChowModification_of_finite_irreducibleComponents {X S : Scheme.{u}} (f : X ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S] [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] (hX : (irreducibleComponents X).Finite) :
    HasDenseChowModification f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.12, Tag 01ZZ](https://stacks.math.columbia.edu/tag/01ZZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
