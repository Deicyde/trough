---
declaration: section
origin: cited
lean: IsSite.exists_topology_and_isSheaf_iff, CategoryTheory.Coverage.toGrothendieck
statement: formalized
proof: formalized
---

# 7.48 The topology defined by a site

Section 7.48 of the Stacks Project, [Tag 00ZB](https://stacks.math.columbia.edu/tag/00ZB). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00ZC, a lemma

[Tag 00ZC](https://stacks.math.columbia.edu/tag/00ZC) in the Stacks Project.

**`IsSite.exists_topology_and_isSheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Pretopology/SiteTopology.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Pretopology/SiteTopology.lean#L136). The attribute's comment: “Both parts for a site as in 00VH (no fibre products assumed in `C`); the sheaf condition is the equalizer of 00VM. Mathlib's own 00ZC tag on `Pretopology.toGrothendieck` only names the topology of a pretopology in a category with all fibre products.”.

> **Stacks 00ZC.** Let `C` be a site with coverings `IsCov`. For `U : C`, let `J(U)` be the
> set of sieves `S` on `U` such that some covering `{fᵢ : Uᵢ ⟶ U}` of the site generates a sieve
> contained in `S`. Then (1) `J` is a Grothendieck topology on `C`, and (2) a presheaf of sets
> is a sheaf for `J` if and only if it is a sheaf on the site, that is, for every covering the
> fork `F(U) ⟶ ∏ F(Uᵢ) ⇉ ∏ F(Uᵢ ×_U Uⱼ)` is an equalizer (Stacks 00VM). The topology is
> `IsSite.topology`.

```lean
theorem exists_topology_and_isSheaf_iff (h : IsSite IsCov) :
    ∃ J : GrothendieckTopology C,
      (∀ (U : C) (S : Sieve U),
        S ∈ J U ↔ ∃ E : PreZeroHypercover.{w} U, IsCov ⟨U, E⟩ ∧ Sieve.generate E.presieve₀ ≤ S) ∧
      ∀ F : Cᵒᵖ ⥤ Type w,
        Presieve.IsSheaf J F ↔
          ∀ (𝒰 : Covering.{u, v, w} C) (h𝒰 : IsCov 𝒰),
            haveI := h.hasPairwisePullbacks h𝒰
            Nonempty (IsLimit (Fork.ofι (Equalizer.Presieve.Arrows.forkMap F 𝒰.2.X 𝒰.2.f)
              (Equalizer.Presieve.Arrows.w F 𝒰.2.X 𝒰.2.f)))
```

## Tag 00ZD, a definition

[Tag 00ZD](https://stacks.math.columbia.edu/tag/00ZD) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Coverage.toGrothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Coverage.toGrothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Topology/AssociatedToSite.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topology/AssociatedToSite.lean#L21) (StacksFrontier): “the Grothendieck topology associated to a site, i.e. the smallest topology for which every covering of the site generates a covering sieve”. References: SGA 3 IV (4.2.2), “special case”; SGA 4 II (1.1.6), “special case”; SGA 4 II (1.3.1), “generated topology”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.48, Tag 00ZB](https://stacks.math.columbia.edu/tag/00ZB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
