---
declaration: section
origin: cited
lean: Stacks.Examples.RadicalTower.exists_not_isEquivalence_fppfTorsors_toPrincipal
statement: formalized
proof: formalized
---

# 110.52 A torsor which is not an fppf torsor

Section 110.52 of the Stacks Project, [Tag 04AF](https://stacks.math.columbia.edu/tag/04AF). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 077B, a lemma

[Tag 077B](https://stacks.math.columbia.edu/tag/077B) in the Stacks Project.

**`Stacks.Examples.RadicalTower.exists_not_isEquivalence_fppfTorsors_toPrincipal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/GroupSchemes/PrincipalNotFppf/StackComparison.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/GroupSchemes/PrincipalNotFppf/StackComparison.lean#L301). The attribute's comment: “G-Principal and G-Torsors are not equivalent in general: for S = Spec ℚ and the group scheme G = ∏ᵢ μ\_\{i+2} the canonical functor G-Torsors ⥤ G-Principal is not essentially surjective, hence not an equivalence, over every big fppf site”.

> **Stacks Project, Tag 077B.**  The stack `G-Principal` of principal homogeneous `G`-spaces
> (Stacks 04UN) and the stack `G-Torsors` of fppf `G`-torsors (Stacks 04UR) are not equivalent in
> general: there are a big fppf site, a scheme `S` in it and a group scheme `G` over `S` in it,
> regarded as a group algebraic space over `S`, for which the canonical functor
> `G-Torsors ⥤ G-Principal` is not essentially surjective, hence not an equivalence.  One may take
> `S = Spec ℚ` and `G = ∏ᵢ μ_{i+2}`, over any big fppf site: this is
> `Stacks.Examples.RadicalTower.not_essSurj_toPrincipal`.

```lean
theorem exists_not_isEquivalence_fppfTorsors_toPrincipal :
    ∃ (𝒞 : BigFppfSite.{0}) (S : Scheme.{0}) (hS : 𝒞.Contains S)
      (G : BigFppfOver 𝒞 S hS) (hG : GrpObj ((toSchemeOver 𝒞 S hS).obj G)),
      ¬ (FppfTorsors.toPrincipal (isAlgebraicSpace_yoneda 𝒞 S hS (BigFppfOver.mk 𝒞 S hS hS (𝟙 S)))
          (GroupAlgebraicSpace.ofGroupSchemeInSite 𝒞 S hS _ _ G hG)).EssSurj ∧
      ¬ (FppfTorsors.toPrincipal (isAlgebraicSpace_yoneda 𝒞 S hS (BigFppfOver.mk 𝒞 S hS hS (𝟙 S)))
          (GroupAlgebraicSpace.ofGroupSchemeInSite 𝒞 S hS _ _ G hG)).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.52, Tag 04AF](https://stacks.math.columbia.edu/tag/04AF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
