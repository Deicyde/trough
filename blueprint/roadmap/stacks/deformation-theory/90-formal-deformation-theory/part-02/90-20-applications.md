---
declaration: section
origin: cited
lean: Deformation.boundaryLinearMap, Deformation.isDeformationCategory_twoFibreProductOver, Deformation.injective_infProjPair, Deformation.exact_infProjPair_infLegDiff, Deformation.exact_boundaryLinearMap_tangentProjPair, Deformation.exact_tangentProjPair_tangentLegDiff, Deformation.tangentProjPair_boundaryFun_eq_zero, Deformation.exact_infLegDiff_infBoundaryLinearMap
statement: formalized
proof: formalized
---

# 90.20 Applications

Section 90.20 of the Stacks Project, [Tag 0DYM](https://stacks.math.columbia.edu/tag/0DYM). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06L5, a lemma

[Tag 06L5](https://stacks.math.columbia.edu/tag/06L5) in the Stacks Project.

**`Deformation.boundaryLinearMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductBoundaryLinear.lean, line 495](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductBoundaryLinear.lean#L495). The attribute's comment: “part (2), the boundary map `Inf(ℱ) → T𝒲` of the six-term exact sequence, as a `k`-linear map of the vector spaces of Tag 06IH”.

> **Stacks Project, Tag 06L5, part (2): the boundary map `δ : Inf(ℱ) → T𝒲` of the six-term
> sequence, as a `k`-linear map**, at an arbitrary coordinate module. At the rank-one module this
> is the third map of the six-term exact sequence of the `2`-fibre product.
>
> This is the form of `δ` that the sequence of `k`-vector spaces asks for;
> `Deformation.boundaryFun`, of which it is the linear reading, is a map of sets.

```lean
public noncomputable def boundaryLinearMap
    (pF : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k) (f : H ⥤ F) (g : G ⥤ F)
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {y₀ : H} {z₀ : G} (hzy : (g ⋙ pF).obj z₀ = (f ⋙ pF).obj y₀)
    {cmp : f.obj y₀ ≅ g.obj z₀}
    (hcmp : pF.IsHomLift (𝟙 ((f ⋙ pF).obj y₀)) cmp.hom)
    (PH : ChosenPushforwardsAt (f ⋙ pF) y₀) (PG : ChosenPushforwardsAt (g ⋙ pF) z₀)
    (PF : ChosenPushforwardsAt pF (f.obj y₀)) (M : FGModuleCat.{max v w} k) :
    ↥((infinitesimalAutomorphismLinearLift PF hF.satisfiesRS).functor.obj M) →ₗ[k]
      ↥((productTangentLift.{u, v, w} pF f g hH hG hF).obj M)
```

**`Deformation.isDeformationCategory_twoFibreProductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductDeformation.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductDeformation.lean#L260). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 06L5, part (1).** The `2`-fibre product `𝒲 = ℋ ×_ℱ 𝒢` of two
> `1`-morphisms of deformation categories over `𝒞_Λ` is again a deformation category.
>
> Condition (RS) is Tag 06L4, and it carries the cofibered-in-groupoids condition with it; the
> special fibre `𝒲(k)` has a unique isomorphism class because `ℋ(k)`, `𝒢(k)` and `ℱ(k)` do.

```lean
theorem isDeformationCategory_twoFibreProductOver
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {H : Type u₁} [Category.{v₁} H]
    {G : Type u₂} [Category.{v₂} G]
    {F : Type u₃} [Category.{v₃} F]
    (pH : H ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (pG : G ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (pF : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (f : H ⥤ F) (g : G ⥤ F)
    (hf : f ⋙ pF = pH) (hg : g ⋙ pF = pG)
    (hH : IsDeformationCategory pH)
    (hG : IsDeformationCategory pG)
    (hF : IsDeformationCategory pF) :
    IsDeformationCategory (TwoFibreProductOver.structureFunctor pH pG pF f g)
```

**`Deformation.injective_infProjPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductInfRow.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductInfRow.lean#L302). The attribute's comment: “part (2), the map `Inf(𝒲) → Inf(ℋ) ⊕ Inf(𝒢)` of the six-term exact sequence and the injectivity of it asserted at the first spot”.

> **Stacks Project, Tag 06L5, part (2): exactness at `Inf(𝒲)`.** The map
> `a : Inf(𝒲) → Inf(ℋ) ⊕ Inf(𝒢)` of the six-term sequence is injective, which is the `0 →` at
> its source.
>
> This is the source's "injectivity of the first map comes from the fact that
> `f × g : 𝒲 → ℋ × 𝒢` is faithful": the induced map on infinitesimal automorphisms is
> conjugation by the comparison of dual-number pushforwards
> (`Deformation.inducedInfinitesimalLinearMap_apply`), so a tangent vector in the kernel of both
> components is an automorphism of a pushforward of `w₀` whose two projections are identities,
> and a self-arrow of the `2`-fibre product is determined by its two components
> (`CategoryTheory.TwoFibreProductOver.Hom.ext'`).

```lean
public theorem injective_infProjPair
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {w₀ : TwoFibreProductOver (f ⋙ pF) (g ⋙ pF) pF f g}
    (PW : ChosenPushforwardsAt
      (TwoFibreProductOver.structureFunctor (f ⋙ pF) (g ⋙ pF) pF f g) w₀)
    (QH : ChosenPushforwardsAt (f ⋙ pF) w₀.x)
    (QG : ChosenPushforwardsAt (g ⋙ pF) w₀.y) :
    letI := naturalLocalizedTangentAddCommGroup PW
      (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).satisfiesRS
    letI := naturalLocalizedTangentModule PW
      (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup QH hH.satisfiesRS
    letI := naturalLocalizedTangentModule QH hH.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup QG hG.satisfiesRS
    letI := naturalLocalizedTangentModule QG hG.satisfiesRS
    Function.Injective (infProjPair.{u, v, w} pF f g hH hG hF PW QH QG)
```

**`Deformation.exact_infProjPair_infLegDiff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductInfRow.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductInfRow.lean#L743). The attribute's comment: “part (2), exactness at `Inf(ℋ) ⊕ Inf(𝒢)` of the six-term exact sequence”.

> **Stacks Project, Tag 06L5, part (2): exactness at `Inf(ℋ) ⊕ Inf(𝒢)`.** In the
> `Inf`-row
>
> `Inf(𝒲) → Inf(ℋ) ⊕ Inf(𝒢) → Inf(ℱ)`
>
> of the six-term sequence of the `2`-fibre product `𝒲 = ℋ ×_ℱ 𝒢`, the kernel of the difference
> of the two outer legs is the image of the pair of the two projections.
>
> This is the source's "if `(β, γ)` map to the same element of `Inf_{x₀}(ℱ)` then `(β, γ)`
> defines an automorphism of `w'₀ = (k[ε], y'₀, z'₀, c' ∘ b')`". Each of the five maps in sight is
> conjugation by a comparison of chosen pushforwards
> (`Deformation.inducedInfinitesimalLinearMapOfEq_spec_iso`,
> `Deformation.canonicalLocalizedTangentAutomorphismLinearEquiv_spec`), and
> `Deformation.pushforwardIso_eq_comparison_comp` identifies the composite of those comparisons
> with the comparison isomorphism carried by the chosen pushforward of `w₀`. The two halves are
> then the two readings of one square: the comparison square of a self-arrow of that pushforward
> gives the vanishing of the composite (`Deformation.eq_of_conjugation`), and conversely a pair
> with equal images satisfies that square (`Deformation.square_of_conjugation`), hence defines a
> self-arrow, which is automatically infinitesimal because the special fibre of `𝒲` is thin
> (`Deformation.ker_transportAutHom_eq_top_of_isThin`).

```lean
public theorem exact_infProjPair_infLegDiff
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {w₀ : TwoFibreProductOver (f ⋙ pF) (g ⋙ pF) pF f g}
    (PW : ChosenPushforwardsAt
      (TwoFibreProductOver.structureFunctor (f ⋙ pF) (g ⋙ pF) pF f g) w₀)
    (QH : ChosenPushforwardsAt (f ⋙ pF) w₀.x)
    (QG : ChosenPushforwardsAt (g ⋙ pF) w₀.y)
    (PF : ChosenPushforwardsAt pF (f.obj w₀.x))
    (PF' : ChosenPushforwardsAt pF (g.obj w₀.y))
    (hw₀ : (f ⋙ pF).obj w₀.x = residueFieldObject.{u, v, w} Λ k) :
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w} PW
      (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w} PW
      (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₁, v₁} QH hH.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₁, v₁} QH hH.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₂, v₂} QG hG.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₂, v₂} QG hG.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₃, v₃} PF hF.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₃, v₃} PF hF.satisfiesRS
    Function.Exact (infProjPair.{u, v, w} pF f g hH hG hF PW QH QG)
      (infLegDiff.{u, v, w} pF f g hH hG hF QH QG PF PF' hw₀)
```

**`Deformation.exact_boundaryLinearMap_tangentProjPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductSelfExact.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductSelfExact.lean#L280). The attribute's comment: “part (2), exactness at `T𝒲` of the six-term exact sequence, for the `k`-linear boundary map `Inf(ℱ) → T𝒲` and the map `T𝒲 → Tℋ ⊕ T𝒢`”.

> **Stacks Project, Tag 06L5, part (2), for the `k`-linear boundary map: exactness at `T𝒲`.**
> The kernel of `c : T𝒲 → Tℋ ⊕ T𝒢` is the image of the `k`-linear boundary map
> `δ : Inf(ℱ) → T𝒲`.
>
> That the composite vanishes is `Deformation.tangentProjPair_boundaryFun_eq_zero`, which holds for
> every automorphism of `x'₀`. Conversely an element of the kernel is the class of a quadruple
> `(k[M], y'₀, z'₀, c' ∘ α ∘ b')` by `Deformation.exists_aut_boundaryObject_tangentClassAt_eq`, and
> that `α` is in the image of the linear lift because
> `Deformation.ker_transportAutHom_squareZeroUnderRed_eq_top` makes the lift's value *all* of the
> automorphisms of the pushforward, transport along
> `Deformation.squareZeroCrossUnderIso` matching the two normalizations of the square-zero
> extension.
>
> This is the statement of part (2) at `T𝒲`: both of its maps are `k`-linear maps of the vector
> spaces of Tag 06IH, and it carries neither the splitting of `k ⟶ k[M]` nor the hypothesis that
> the basepoint lies over the residue field that the set-level
> `Deformation.exact_boundaryFun_tangentProjPair` needs.

```lean
public theorem exact_boundaryLinearMap_tangentProjPair
    (pF : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k) (f : H ⥤ F) (g : G ⥤ F)
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {y₀ : H} {z₀ : G} (hzy : (g ⋙ pF).obj z₀ = (f ⋙ pF).obj y₀)
    {cmp : f.obj y₀ ≅ g.obj z₀}
    (hcmp : pF.IsHomLift (𝟙 ((f ⋙ pF).obj y₀)) cmp.hom)
    (PH : ChosenPushforwardsAt (f ⋙ pF) y₀) (PG : ChosenPushforwardsAt (g ⋙ pF) z₀)
    (PF : ChosenPushforwardsAt pF (f.obj y₀)) (M : FGModuleCat.{max v w} k) :
    Function.Exact (boundaryLinearMap.{u, v, w} pF f g hH hG hF hzy hcmp PH PG PF M)
      (tangentProjPair.{u, v, w} pF f g hH hG hF M)
```

**`Deformation.exact_tangentProjPair_tangentLegDiff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductSixTermExact.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductSixTermExact.lean#L329). The attribute's comment: “part (2), the tangent row `T𝒲 → Tℋ ⊕ T𝒢 → Tℱ` of the six-term exact sequence and its exactness at `Tℋ ⊕ T𝒢`”.

> In the tangent row `T𝒲 → Tℋ ⊕ T𝒢 → Tℱ` of the six-term sequence of the `2`-fibre product
> `𝒲 = ℋ ×_ℱ 𝒢`, the kernel of the difference of the two outer legs is the image of the pair of
> the two projections.

```lean
public theorem exact_tangentProjPair_tangentLegDiff
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF) (M : FGModuleCat.{max v w} k) :
    Function.Exact (tangentProjPair.{u, v, w} pF f g hH hG hF M)
      (tangentLegDiff.{u, v, w} pF f g hH hG hF M)
```

**`Deformation.tangentProjPair_boundaryFun_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductSixTermExact.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductSixTermExact.lean#L550). The attribute's comment: “part (2), that the boundary map of the six-term exact sequence lands in the kernel of `T𝒲 → Tℋ ⊕ T𝒢`”.

> The boundary map `δ : Aut(x'₀) → T𝒲` of the six-term sequence lands in the kernel of the
> map `c : T𝒲 → Tℋ ⊕ T𝒢`.

```lean
public theorem tangentProjPair_boundaryFun_eq_zero
    (pF : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k) (f : H ⥤ F) (g : G ⥤ F)
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {y₀ : H} {z₀ : G} (hzy : (g ⋙ pF).obj z₀ = (f ⋙ pF).obj y₀)
    {cmp : f.obj y₀ ≅ g.obj z₀}
    (hcmp : pF.IsHomLift (𝟙 ((f ⋙ pF).obj y₀)) cmp.hom)
    (PH : ChosenPushforwardsAt (f ⋙ pF) y₀) (PG : ChosenPushforwardsAt (g ⋙ pF) z₀)
    (PF : ChosenPushforwardsAt pF (f.obj y₀)) (M : FGModuleCat.{max v w} k)
    (α : Aut (PF.obj (squareZeroCrossUnder.{u, v, w} ((f ⋙ pF).obj y₀) M))) :
    tangentProjPair.{u, v, w} pF f g hH hG hF M
        (boundaryFun.{u, v, w} f g hzy hcmp PH PG PF hF.predeformation.cofibered
          (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).predeformation
          (tangentConditionS2.{u, v, w}
            (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF)) M α) = 0
```

**`Deformation.exact_infLegDiff_infBoundaryLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductSixTermFull/SixTerm.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductSixTermFull/SixTerm.lean#L94). The attribute's comment: “part (2), exactness at `Inf(ℱ)` of the six-term exact sequence, for the map `Inf(ℋ) ⊕ Inf(𝒢) → Inf(ℱ)` and the boundary map `Inf(ℱ) → T𝒲`”.

> **Stacks Project, Tag 06L5, part (2): exactness at `Inf(ℱ)`.** In the six-term sequence of
> the `2`-fibre product `𝒲 = ℋ ×_ℱ 𝒢`, the kernel of the boundary map `δ : Inf(ℱ) → T𝒲` is the
> image of the difference `b : Inf(ℋ) ⊕ Inf(𝒢) → Inf(ℱ)` of the two outer legs.
>
> This is the source's "if `α` gives the trivial deformation `(k[ε], y'₀, z'₀, c' ∘ α ∘ b')` of
> `w₀`, then the isomorphism `w'₀ → δ(α)` produces a pair `(β, γ)` which is a preimage of `α`",
> together with its converse. The class of the quadruple `δ(α)` vanishes exactly when `α`
> satisfies the boundary square for some pair of automorphisms of `y'₀` and `z'₀`
> (`Deformation.tangentClassAt_boundaryObject_eq_zero_iff`), and the boundary square says exactly
> that `α` is the value of `b` on the pair those automorphisms define
> (`Deformation.eq_comp_inv_iff_boundary_square`): the two maps `b` is the difference of are
> conjugation by the comparisons of Tag 07W6 and Tag 06JV (2) at the dual numbers, and the three
> transports `Deformation.transportAut_comp_boundaryCompareFst`,
> `Deformation.map_cross_comp_boundaryCompareSnd` and
> `Deformation.transportAut_comp_boundaryCompareSnd` carry those conjugations to the re-based
> square-zero extension at which `δ` is built.
>
> Every automorphism of a chosen pushforward to the dual numbers is infinitesimal, the special
> fibre of a predeformation category being thin
> (`Deformation.ker_transportAutHom_eq_top_of_isThin`), so the pair of automorphisms the square
> produces does come from `Inf(ℋ) ⊕ Inf(𝒢)`. The sign the source defers is absorbed by reading
> the difference as `-c(g(γ)) + f(β)`; the two orders agree because the tangent space is an
> abelian group.

```lean
public theorem exact_infLegDiff_infBoundaryLinearMap
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {w₀ : TwoFibreProductOver (f ⋙ pF) (g ⋙ pF) pF f g}
    (PW : ChosenPushforwardsAt
      (TwoFibreProductOver.structureFunctor (f ⋙ pF) (g ⋙ pF) pF f g) w₀)
    (QH : ChosenPushforwardsAt (f ⋙ pF) w₀.x)
    (QG : ChosenPushforwardsAt (g ⋙ pF) w₀.y)
    (PF : ChosenPushforwardsAt pF (f.obj w₀.x))
    (PF' : ChosenPushforwardsAt pF (g.obj w₀.y))
    (hw₀ : (f ⋙ pF).obj w₀.x = residueFieldObject.{u, v, w} Λ k) :
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₁, v₁} QH hH.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₁, v₁} QH hH.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₂, v₂} QG hG.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₂, v₂} QG hG.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₃, v₃} PF hF.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₃, v₃} PF hF.satisfiesRS
    Function.Exact (infLegDiff.{u, v, w} pF f g hH hG hF QH QG PF PF' hw₀)
      (infBoundaryLinearMap.{u, v, w} pF f g hH hG hF QH QG PF)
```

**`Deformation.twoFibreProduct_sixTermExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductSixTermFull/SixTerm.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductSixTermFull/SixTerm.lean#L350). The attribute's comment: “part (2), the six-term exact sequence `0 → Inf(𝒲) → Inf(ℋ) ⊕ Inf(𝒢) → Inf(ℱ) → T𝒲 → Tℋ ⊕ T𝒢 → Tℱ` of a 2-fibre product of deformation categories, with its five `k`-linear maps and the exactness at all five of its spots: at `Inf(𝒲)`, at `Inf(ℋ) ⊕ Inf(𝒢)`, at `Inf(ℱ)`, at `T𝒲` and at `Tℋ ⊕ T𝒢`”.

> **Stacks Project, Tag 06L5, part (2): the six-term sequence**
>
> `0 → Inf(𝒲) → Inf(ℋ) ⊕ Inf(𝒢) → Inf(ℱ) → T𝒲 → Tℋ ⊕ T𝒢 → Tℱ`
>
> of the `2`-fibre product `𝒲 = ℋ ×_ℱ 𝒢` of deformation categories, with all five of its
> `k`-linear maps and the exactness at every one of its five spots in one statement.
>
> The five conjuncts are, in order: injectivity of `a` at `Inf(𝒲)` (the source's `0 →`,
> `Deformation.injective_infProjPair`), exactness at `Inf(ℋ) ⊕ Inf(𝒢)`
> (`Deformation.exact_infProjPair_infLegDiff`), exactness at `Inf(ℱ)`
> (`Deformation.exact_infLegDiff_infBoundaryLinearMap`), exactness at `T𝒲`
> (`Deformation.exact_boundaryLinearMap_tangentProjPair`, read through the model bridge of
> `Deformation.infBoundaryLinearMap`) and exactness at `Tℋ ⊕ T𝒢`
> (`Deformation.exact_tangentProjPair_tangentLegDiff`).
>
> The basepoints are the images of one object `w₀` of `𝒲`, as in the source's "let `x₀, y₀, z₀`
> be the image of `w₀`", and the tangent terms are taken at the rank-one coordinate module, at
> which they are the tangent spaces of Tag 06IH.

```lean
public theorem twoFibreProduct_sixTermExact
    (hH : IsDeformationCategory.{u, v, w} (f ⋙ pF))
    (hG : IsDeformationCategory.{u, v, w} (g ⋙ pF))
    (hF : IsDeformationCategory.{u, v, w} pF)
    {w₀ : TwoFibreProductOver (f ⋙ pF) (g ⋙ pF) pF f g}
    (PW : ChosenPushforwardsAt
      (TwoFibreProductOver.structureFunctor (f ⋙ pF) (g ⋙ pF) pF f g) w₀)
    (QH : ChosenPushforwardsAt (f ⋙ pF) w₀.x)
    (QG : ChosenPushforwardsAt (g ⋙ pF) w₀.y)
    (PF : ChosenPushforwardsAt pF (f.obj w₀.x))
    (PF' : ChosenPushforwardsAt pF (g.obj w₀.y))
    (hw₀ : (f ⋙ pF).obj w₀.x = residueFieldObject.{u, v, w} Λ k) :
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w} PW
      (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w} PW
      (isDeformationCategory_productBased.{u, v, w} pF f g hH hG hF).satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₁, v₁} QH hH.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₁, v₁} QH hH.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₂, v₂} QG hG.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₂, v₂} QG hG.satisfiesRS
    letI := naturalLocalizedTangentAddCommGroup.{u, v, w, u₃, v₃} PF hF.satisfiesRS
    letI := naturalLocalizedTangentModule.{u, v, w, u₃, v₃} PF hF.satisfiesRS
    Function.Injective (infProjPair.{u, v, w} pF f g hH hG hF PW QH QG) ∧
      Function.Exact (infProjPair.{u, v, w} pF f g hH hG hF PW QH QG)
          (infLegDiff.{u, v, w} pF f g hH hG hF QH QG PF PF' hw₀) ∧
        Function.Exact (infLegDiff.{u, v, w} pF f g hH hG hF QH QG PF PF' hw₀)
            (infBoundaryLinearMap.{u, v, w} pF f g hH hG hF QH QG PF) ∧
          Function.Exact (infBoundaryLinearMap.{u, v, w} pF f g hH hG hF QH QG PF)
              (tangentProjPair.{u, v, w} pF f g hH hG hF (FGModuleCat.of k (ULift.{v} k))) ∧
            Function.Exact
              (tangentProjPair.{u, v, w} pF f g hH hG hF (FGModuleCat.of k (ULift.{v} k)))
              (tangentLegDiff.{u, v, w} pF f g hH hG hF (FGModuleCat.of k (ULift.{v} k)))
```

## Tag 0DYN, a lemma

[Tag 0DYN](https://stacks.math.columbia.edu/tag/0DYN) in the Stacks Project.

**`Deformation.mapTwoFibreProductBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean#L191). The attribute's comment: “the canonical functor between the two 2-fibre products”.

> The canonical functor over `𝒞_Λ` from the `2`-fibre product of `ℋ₁` and `ℋ₂` over `𝒢` to
> their `2`-fibre product over `ℱ`, for a morphism `q : 𝒢 → ℱ`: it keeps both components and
> applies `q` to the comparison isomorphism.

```lean
public def mapTwoFibreProductBaseChange
    (p₁ : BasedFunctor 𝓗₁ 𝓖) (p₂ : BasedFunctor 𝓗₂ 𝓖) (q : BasedFunctor 𝓖 𝓕) :
    BasedFunctor (twoFibreProductBasedCategory p₁ p₂)
      (twoFibreProductBasedCategory (BasedFunctor.comp p₁ q) (BasedFunctor.comp p₂ q))
```

**`Deformation.isSmooth_mapTwoFibreProductBaseChange'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Applications/TwoFibreProductBaseChangeSmooth.lean#L538). The attribute's comment: “smoothness”.

> Let `p₁ : ℋ₁ → 𝒢`, `p₂ : ℋ₂ → 𝒢` and `q : 𝒢 → ℱ` be morphisms of categories cofibered in
> groupoids over `𝒞_Λ`. Assume that `ℱ` and `𝒢` are deformation categories, that `T𝒢 → Tℱ` is
> injective, and that `Inf(𝒢) → Inf(ℱ)` is surjective. Then `ℋ₁ ×_𝒢 ℋ₂ → ℋ₁ ×_ℱ ℋ₂` is smooth.

```lean
public theorem isSmooth_mapTwoFibreProductBaseChange'
    (p₁ : BasedFunctor 𝓗₁ 𝓖) (p₂ : BasedFunctor 𝓗₂ 𝓖) (q : BasedFunctor 𝓖 𝓕)
    (h𝓗₁ : IsCofiberedInGroupoids 𝓗₁.p) (h𝓗₂ : IsCofiberedInGroupoids 𝓗₂.p)
    (h𝓖 : IsDeformationCategory 𝓖.p) (h𝓕 : IsDeformationCategory 𝓕.p)
    (htangent : Function.Injective
      (differential h𝓖.predeformation.cofibered h𝓕.predeformation.cofibered q))
    {z₀ : 𝓖.p.Fiber (residueFieldObject.{u, w, w} Λ k)}
    (PG : ChosenPushforwardsAt 𝓖.p z₀.1) (PF : ChosenPushforwardsAt 𝓕.p (q.obj z₀.1))
    (hinf :
      letI := naturalLocalizedTangentAddCommGroup PG h𝓖.satisfiesRS
      letI := naturalLocalizedTangentModule PG h𝓖.satisfiesRS
      letI := naturalLocalizedTangentAddCommGroup PF h𝓕.satisfiesRS
      letI := naturalLocalizedTangentModule PF h𝓕.satisfiesRS
      Function.Surjective (inducedInfinitesimalLinearMapOfEq q.toFunctor q.w
        h𝓖.satisfiesRS h𝓕.satisfiesRS PG PF)) :
    IsSmooth (mapTwoFibreProductBaseChange p₁ p₂ q)
```

## Tag 0DYP, a lemma

[Tag 0DYP](https://stacks.math.columbia.edu/tag/0DYP) in the Stacks Project.

**`Deformation.isSmooth_iff_differential_surjective_and_lifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Smoothness/Criterion.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Smoothness/Criterion.lean#L115).

> Surjectivity of the differential and preservation of the existence of lifts across small
> extensions characterize smoothness.

```lean
public theorem isSmooth_iff_differential_surjective_and_lifts
    (h𝓕 : IsDeformationCategory 𝓕.p)
    (h𝓖 : IsDeformationCategory 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) :
    IsSmooth φ ↔
      (Function.Surjective
        (differential h𝓕.predeformation.cofibered
          h𝓖.predeformation.cofibered φ) ∧
       ∀ ⦃B A : ArtinianLocalAlgCat.{u, w, w} Λ k⦄
         (f : B ⟶ A),
         InfinitesimalLifting.IsSmallExtension
           (CommRingCat.ofHom f.hom.toRingHom) →
         ∀ (x : 𝓕.p.Fiber A),
           (∃ (y' : 𝓖.obj) (g : y' ⟶ φ.obj x.1),
             𝓖.p.IsHomLift f g) →
           (∃ (x' : 𝓕.obj) (h : x' ⟶ x.1),
             𝓕.p.IsHomLift f h))
```

## Tag 0E3R, a lemma

[Tag 0E3R](https://stacks.math.columbia.edu/tag/0E3R) in the Stacks Project.

**`Deformation.isSmooth_of_differential_surjective_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Smoothness/Composite.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Smoothness/Composite.lean#L45).

> **Stacks Project, Tag 0E3R.** A morphism of deformation categories is smooth if its
> differential is surjective and its composite with another morphism is smooth.

```lean
public theorem isSmooth_of_differential_surjective_of_comp
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    {𝓗 : BasedCategory.{v₃, u₃} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    (h𝓕 : IsDeformationCategory 𝓕.p)
    (h𝓖 : IsDeformationCategory 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) (ψ : BasedFunctor 𝓖 𝓗)
    (hd : Function.Surjective
      (differential h𝓕.predeformation.cofibered
        h𝓖.predeformation.cofibered φ))
    (hsmooth : IsSmooth (BasedFunctor.comp φ ψ)) :
    IsSmooth φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.20, Tag 0DYM](https://stacks.math.columbia.edu/tag/0DYM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
