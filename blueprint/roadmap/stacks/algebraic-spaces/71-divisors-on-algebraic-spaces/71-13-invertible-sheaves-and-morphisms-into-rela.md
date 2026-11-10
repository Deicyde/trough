---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.GradedPowerMapPoints.locus, AlgebraicGeometry.Space.GradedPowerMapPoints.mem_locus_iff, AlgebraicGeometry.Space.GradedPowerMapPoints.locus_comap, AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z, AlgebraicGeometry.Space.RelativeProjPoints.invertibleMorphism, AlgebraicGeometry.Space.RelativeProjPoints.invertibleMorphism_comp_π, AlgebraicGeometry.Space.RelativeProjPoints.mem_subspaceOfOpens_of_epi, AlgebraicGeometry.Space.RelativeProjPoints.locusFactor_invertibleMorphism_of_epi
statement: formalized
proof: formalized
---

# 71.13 Invertible sheaves and morphisms into relative Proj

Section 71.13 of the Stacks Project, [Tag 0D2Y](https://stacks.math.columbia.edu/tag/0D2Y). 2 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D2Y, the section

[Tag 0D2Y](https://stacks.math.columbia.edu/tag/0D2Y) in the Stacks Project.

**`AlgebraicGeometry.Space.GradedPowerMapPoints.locus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleLocus.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleLocus.lean#L216). The attribute's comment: “the open U(psi) of the situation, presented by the opens it cuts on the scheme points of X; on a scheme point it is the union, over the homogeneous sections of positive degree of f^*A over the affine opens, of the opens where the value of psi does not vanish, which is the description of Tag 01O8”.

> **The open subspace `U(ψ) ⊆ X` of [Stacks, Tag 0D2Y]**, presented by the open it cuts on each
> scheme point of `X`: on a `T`-point `x`, the open `U(ψ)` of [Stacks, Tag 01O8] of the restricted
> data, that is the union of the opens on which the values of `ψ` at the homogeneous sections of
> positive degree of `f^*𝒜` over the affine opens of the scheme of `T` do not vanish.
>
> This is the source of the morphism `r_{ℒ,ψ} : U(ψ) ⟶ Proj_Y(𝒜)` of [Stacks, Tag 0D2Z].  On each
> scheme point it is an abbreviation of
> `Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.GradedPowerMap.coveringOpen` of the
> restricted data (it is reducible), and it is reasoned about through that open's characterising
> lemmas.
>
> Two things the present tag asks for are absent, and both are recorded here rather than in the
> attribute.  Tag 0D2Y describes the same open as the union of the loci where `f^*𝒜_d ⟶ ℒ^{⊗ d}`
> is surjective; identifying the two descriptions still needs the stalk of the pullback `f^*𝒜_d`
> computed as a tensor product, for which see the "Not done here" section of
> `StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Locus.lean`.  And the family of
> opens below is not assembled into an open-subspace subfunctor object.

```lean
public def locus (P : GradedPowerMapPoints B S hS X) (T : BigFppfOver B S hS)
    (x : yoneda.obj T ⟶ X) : ((BigFppfOver.toScheme B S hS).obj T).Opens
```

**`AlgebraicGeometry.Space.GradedPowerMapPoints.mem_locus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleLocus.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleLocus.lean#L252). The attribute's comment: “membership in U(psi): a point of a scheme point of X lies in U(psi) exactly when the value of psi at some homogeneous section of f^*A of positive degree over some affine open does not vanish there”.

> **Membership in `U(ψ)`.**  A point of the scheme of `T` lies in the open that `U(ψ)` cuts on
> a `T`-point `x` of `X` exactly when the value of `ψ` at some homogeneous section of positive
> degree of `f^*𝒜` over some affine open does not vanish there.

```lean
public theorem mem_locus_iff (P : GradedPowerMapPoints B S hS X) (T : BigFppfOver B S hS)
    (x : yoneda.obj T ⟶ X) {z : (BigFppfOver.toScheme B S hS).obj T} :
    z ∈ P.locus T x ↔
      ∃ p : PositiveSection (P.algebra T x), z ∈ (P.pow T x).openOfPositiveSection p
```

**`AlgebraicGeometry.Space.GradedPowerMapPoints.locus_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleLocus.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleLocus.lean#L267). The attribute's comment: “formation of U(psi) commutes with pullback by a morphism of algebraic spaces X' -> X: the open cut by U(g^*psi) on a scheme point x' of X' is the open cut by U(psi) on x' composed with g”.

> **Formation of `U(ψ) ⊆ X` commutes with pullback by a morphism `g : X' ⟶ X` of algebraic
> spaces**, the final assertion of [Stacks, Tag 0D2Y].  The open that `U(g^*ψ)` cuts on a scheme
> point `x'` of `X'` is the open that `U(ψ)` cuts on the scheme point `x' ∘ g` of `X`, which is the
> open that the pullback of `U(ψ)` along `g` cuts on `x'`.

```lean
public theorem locus_comap (P : GradedPowerMapPoints B S hS X) (g : X' ⟶ X)
    (T : BigFppfOver B S hS) (x : yoneda.obj T ⟶ X') :
    (P.comap g).locus T x = P.locus T (x ≫ g)
```

## Tag 0D2Z, a lemma

[Tag 0D2Z](https://stacks.math.columbia.edu/tag/0D2Z) in the Stacks Project.

**`AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleBaseChange.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleBaseChange.lean#L692). The attribute's comment: “variant: X a scheme; the whole lemma, in Situation 0849 with Proj_Y(A) the relative Proj of Stacks 084B and X a scheme over the algebraic space Y: the morphism r_{L,psi} : U(psi) -> Proj_Y(A) over Y; theta : r^*((+)_d O(d)) -> (+)_d L^d|_{U(psi)} a unital multiplicative map; clause (1) for every scheme V -> Y (in particular every etale one) and every scheme over V x_Y X; clauses (2)(a) and (2)(b) for every scheme W -> X and every degree d >= 1; the characterization of r_{L,psi} by (2)(b); and clause (3) for every square with X', Y' schemes and Y' -> Y arbitrary: U(psi') = (g')^{-1}(U(psi)), r_{L',psi'} is the base change of r_{L,psi} through Proj_{Y'}(A') = Y' x_Y Proj_Y(A), and theta' is the pullback of theta”.

> **[Stacks, Tag 0D2Z].**  In Situation 0849 let `Y` be the algebraic space `s.space`, `𝒜` the
> quasi-coherent graded `𝒪_Y`-algebra `s.algebra` and `π : Proj_Y(𝒜) ⟶ Y` its relative homogeneous
> spectrum of Stacks 084B (`s.relativeProjFunctor`, `s.relativeProjπ`).  Let `f : X ⟶ Y` with `X` a
> scheme, `ℒ` invertible on `X` and `ψ : f^*𝒜 ⟶ ⨁_d ℒ^{⊗ d}` a homomorphism of graded algebras, and
> let `U(ψ) ⊆ X` be the open subspace of [Stacks, Tag 0D2Y].  Then `ψ` induces the morphism
> `r_{ℒ,ψ} = s.relativeProjPoints.invertibleMorphism ψ : U(ψ) ⟶ Proj_Y(𝒜)` and the map of graded
> algebras `θ = (toGradedPowerMap ψ).theta : r^*(⨁_d 𝒪(d)) ⟶ ⨁_d ℒ^{⊗ d}|_{U(ψ)}` (the twists of
> `Proj_Y(𝒜)` read at the scheme point `f`, where they are those of `Proj_X(f^*𝒜)`, Stacks 084D (3)),
> such that:
>
> 1. `r_{ℒ,ψ}` is a morphism over `Y`, and `θ` preserves the unit and the products;
> 2. **clause (1)**: for every scheme `v : V ⟶ Y` (in particular every `V ⟶ Y` étale), every scheme
>    `W` over `V ×_Y X`, every open `O` of `V`, `d ≥ 0` and section `a` of `v^*𝒜_d` over `O`, the
>    pullback of `θ` to `V ×_Y U(ψ)` carries the inverse image of `ψ_{Proj}(a)` to the restriction of
>    `ψ(a)` (`clauseOne`);
> 3. **clause (2)(a)**: a scheme `W ⟶ X` over which `ψ` is surjective in some degree `k ≥ 1`
>    factors through `U(ψ)`;
> 4. **clause (2)(b)**: the composite `W ⟶ U(ψ) ⟶ Proj_Y(𝒜)` is the point of `Proj_Y(𝒜)` which the
>    construction of the relative Proj attaches to the quadruple `(k, W ⟶ Y, ℒ^{⊗ k}|_W, ψ|_W)`;
> 5. **the characterization**: `r_{ℒ,ψ}` is the only morphism over `Y` with clause (2)(b);
> 6. **clause (3)**: for every commutative square `g ∘ f' = f ∘ g'` with `X'` and `Y'` schemes,
>    with `ψ' = clauseThreeTwisting ψ g f' g' hsq` the pullback of `ψ`:
>    `U(ψ') = g'^{-1}(U(ψ))`; `r_{ℒ',ψ'}` is the base change of `r_{ℒ,ψ}` through
>    `Proj_{Y'}(g^*𝒜) = Y' ×_Y Proj_Y(𝒜)`; and `θ'` is the pullback of `θ` along
>    `j : U(ψ') ⟶ U(ψ)`.

```lean
theorem tag0D2Z :
    s.relativeProjPoints.invertibleMorphism ψ ≫ s.relativeProjπ =
        (subspaceOfOpens s.site s.base s.containsBase X (toGradedPowerMap ψ).coveringOpen).ι ≫ f ∧
    SheafOfModules.sectionsMap (((toGradedPowerMap ψ).theta).app 0)
        (Stacks.Conormal.gradedPullback
            ((toGradedPowerMap ψ).globalMorphism (relativeProj (s.relativeProjPoints.algebra X f)))
            (Stacks.AlgebraicGeometry.GluedTwistAlgebra.twistDataOfGradedAlgebra
              (s.relativeProjPoints.algebra X f)).algebra).one =
      (laurentOn L (toGradedPowerMap ψ).coveringOpen).one ∧
    (∀ (n e : ℕ) (U : (toGradedPowerMap ψ).coveringOpen.toScheme.Opens)
        (x :
            ((Stacks.Conormal.gradedPullback
                ((toGradedPowerMap ψ).globalMorphism
                  (relativeProj (s.relativeProjPoints.algebra X f)))
                (Stacks.AlgebraicGeometry.GluedTwistAlgebra.twistDataOfGradedAlgebra
                  (s.relativeProjPoints.algebra X f)).algebra).piece
              (n : ℤ)).val.obj
            (op U))
        (y :
            ((Stacks.Conormal.gradedPullback
                ((toGradedPowerMap ψ).globalMorphism
                  (relativeProj (s.relativeProjPoints.algebra X f)))
                (Stacks.AlgebraicGeometry.GluedTwistAlgebra.twistDataOfGradedAlgebra
                  (s.relativeProjPoints.algebra X f)).algebra).piece
              (e : ℤ)).val.obj
            (op U)),
        (((toGradedPowerMap ψ).theta.app ((n : ℤ) + (e : ℤ))).val.app (op U)
            (((Stacks.Conormal.gradedPullback
                    ((toGradedPowerMap ψ).globalMorphism
                      (relativeProj (s.relativeProjPoints.algebra X f)))
                    (Stacks.AlgebraicGeometry.GluedTwistAlgebra.twistDataOfGradedAlgebra
                      (s.relativeProjPoints.algebra X f)).algebra).mul
                  n e).app
                (op U) x y)) =
          ((laurentOn L (toGradedPowerMap ψ).coveringOpen).mul n e).app (op U)
            (((toGradedPowerMap ψ).theta.app n).val.app (op U) x)
            (((toGradedPowerMap ψ).theta.app e).val.app (op U) y)) ∧
    (∀ {V W : BigFppfOver s.site s.base s.containsBase} (v : yoneda.obj V ⟶ s.space.1) (p : W ⟶ V)
        (q : W ⟶ X)
        (hpq : yoneda.map p ≫ v = yoneda.map q ≫ f)
        (O : ((BigFppfOver.toScheme s.site s.base s.containsBase).obj V).Opens) (n : ℕ)
        (a : Γ((s.relativeProjPoints.algebra V v).piece (n : ℤ), O)),
      ((toGradedPowerMap (clauseThreeTwisting ψ v p q hpq)).powK n).presheaf.map
          (eqToHom ((toGradedPowerMap (clauseThreeTwisting ψ v p q hpq)).toBase_preimage_eq O)).op
        ((((clauseThreeSourceIso ψ v p q hpq).inv ≫
            pullbackGradedAlgebraMap (clauseThreeRestrict ψ v p q hpq).toLRSHom.toShHom
              (toGradedPowerMap ψ).theta ≫
            (clauseThreeTargetIso ψ v p q hpq).hom).app n).val.app
          (op
              ((toGradedPowerMap (clauseThreeTwisting ψ v p q hpq)).globalMorphism
                (relativeProj (s.relativeProjPoints.algebra V v)) ⁻¹ᵁ
            ((relativeProj (s.relativeProjPoints.algebra V v)).toBase ⁻¹ᵁ O)))
          (pullbackUnit ((toGradedPowerMap (clauseThreeTwisting ψ v p q hpq)).globalMorphism
              (relativeProj (s.relativeProjPoints.algebra V v))).toLRSHom.toShHom
            (Otw (s.relativeProjPoints.algebra V v) n)
                (op ((relativeProj (s.relativeProjPoints.algebra V v)).toBase ⁻¹ᵁ O))
                (psiU (s.relativeProjPoints.algebra V v) n O a))) =
        (tensorPowerModule ((BigFppfOver.toScheme s.site s.base s.containsBase).obj W)
            (toGradedPowerMap (clauseThreeTwisting ψ v p q hpq)).L n).presheaf.map
            (homOfLE
                ((toGradedPowerMap
                  (clauseThreeTwisting ψ v p q hpq)).coveringOpen.ι.image_preimage_le
              ((BigFppfOver.toScheme s.site s.base s.containsBase).map p ⁻¹ᵁ O))).op
          ((powCompare (toGradedPowerMap (clauseThreeTwisting ψ v p q hpq)).L n).hom.app
            ((BigFppfOver.toScheme s.site s.base s.containsBase).map p ⁻¹ᵁ O)
            (valueSec (clauseThreeTwisting ψ v p q hpq) n O a))) ∧
    (∀ {W : BigFppfOver s.site s.base s.containsBase} (w : W ⟶ X) {k : ℕ} (_ : 0 < k)
        [Epi
              ((ψ.pullback ((BigFppfOver.toScheme s.site s.base s.containsBase).map w)).app
                (k : ℤ))],
            w ∈
            (subspaceOfOpens s.site s.base s.containsBase X (toGradedPowerMap ψ).coveringOpen).obj
              (op W)) ∧
    (∀ {W : BigFppfOver s.site s.base s.containsBase} (w : W ⟶ X) {k : ℕ} (hk : 0 < k)
        [Epi
            ((ψ.pullback ((BigFppfOver.toScheme s.site s.base s.containsBase).map w)).app (k : ℤ))],
        s.relativeProjPoints.locusFactor ψ w
            (s.relativeProjPoints.mem_subspaceOfOpens_of_epi ψ w hk) ≫
            s.relativeProjPoints.invertibleMorphism ψ =
                s.relativeProjPoints.quadruplePoint ψ w hk) ∧
    (∀ Φ :
        (subspaceOfOpens s.site s.base s.containsBase X
            (toGradedPowerMap ψ).coveringOpen).toFunctor ⟶
          s.relativeProjFunctor,
      Φ ≫ s.relativeProjπ =
      (subspaceOfOpens s.site s.base s.containsBase X (toGradedPowerMap ψ).coveringOpen).ι ≫ f →
      (∀ {W : BigFppfOver s.site s.base s.containsBase} (w : W ⟶ X) {k : ℕ} (hk : 0 < k)
        [Epi
            ((ψ.pullback ((BigFppfOver.toScheme s.site s.base s.containsBase).map w)).app (k : ℤ))],
        s.relativeProjPoints.locusFactor ψ w
          (s.relativeProjPoints.mem_subspaceOfOpens_of_epi ψ w hk) ≫
          Φ = s.relativeProjPoints.quadruplePoint ψ w hk) →
      Φ = s.relativeProjPoints.invertibleMorphism ψ) ∧
    (∀ {Y' X' : BigFppfOver s.site s.base s.containsBase} (g : yoneda.obj Y' ⟶ s.space.1)
        (f' : X' ⟶ Y') (g' : X' ⟶ X)
        (hsq : yoneda.map f' ≫ g = yoneda.map g' ≫ f),
      (toGradedPowerMap (clauseThreeTwisting ψ g f' g' hsq)).coveringOpen =
          (BigFppfOver.toScheme s.site s.base s.containsBase).map g' ⁻¹ᵁ
          (toGradedPowerMap ψ).coveringOpen ∧
      (∀ {T : BigFppfOver s.site s.base s.containsBase} (t : T ⟶ X')
        (ht : t ≫ g' ∈
          (subspaceOfOpens s.site s.base s.containsBase X (toGradedPowerMap ψ).coveringOpen).obj
            (op T)),
        (s.relativeProjPoints.pointEquivProjOver Y' g (t ≫ f')
            ⟨s.relativeProjPoints.locusFactor ψ (t ≫ g') ht ≫
              s.relativeProjPoints.invertibleMorphism ψ,
              locusFactor_invertibleMorphism_comp_π ψ g f' g' hsq t ht⟩).1 =
          liftOfPreimageEqTop _ _ (preimage_clauseThree_coveringOpen_eq_top ψ g f' g' hsq t ht) ≫
            (toGradedPowerMap (clauseThreeTwisting ψ g f' g' hsq)).globalMorphism
              (relativeProj (s.relativeProjPoints.algebra Y' g))) ∧
      (toGradedPowerMap (clauseThreeTwisting ψ g f' g' hsq)).theta =
        (clauseThreeSourceIso ψ g f' g' hsq).inv ≫
          pullbackGradedAlgebraMap (clauseThreeRestrict ψ g f' g' hsq).toLRSHom.toShHom
            (toGradedPowerMap ψ).theta ≫
          (clauseThreeTargetIso ψ g f' g' hsq).hom)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.invertibleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L187). The attribute's comment: “variant: the morphism r_{L,psi} : U(psi) -> Proj_Y(A) for a presentation of Proj_Y(A) by its base changes to the scheme points of Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`r_{ℒ,ψ} : U(ψ) ⟶ Proj_Y(𝒜)`, the morphism of [Stacks, Tag 0D2Z]**, as the transformation of
> functors the source's proof builds: on a test scheme `ρ : T ⟶ X` of `U(ψ)` it is
> `invertiblePoint`, and its naturality is the naturality of the identification
> `X ×_Y Proj_Y(𝒜) = Proj_X(f^*𝒜)`.

```lean
def invertibleMorphism :
    (subspaceOfOpens B S hS X (toGradedPowerMap ψ).coveringOpen).toFunctor ⟶ Proj
```

**`AlgebraicGeometry.Space.RelativeProjPoints.invertibleMorphism_comp_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L199). The attribute's comment: “variant: r_{L,psi} lies over Y, for a presentation of Proj_Y(A) by its base changes to the scheme points of Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`r_{ℒ,ψ}` is a morphism over `Y`**, as [Stacks, Tag 0D2Z] asserts: `π ∘ r_{ℒ,ψ}` is the
> restriction of `f` to `U(ψ)`.

```lean
theorem invertibleMorphism_comp_π :
    d.invertibleMorphism ψ ≫ π
      = (subspaceOfOpens B S hS X (toGradedPowerMap ψ).coveringOpen).ι ≫ f
```

**`AlgebraicGeometry.Space.RelativeProjPoints.mem_subspaceOfOpens_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L240). The attribute's comment: “variant: clause (2)(a), for a presentation of Proj_Y(A) by its base changes to the scheme points of Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **Clause (2)(a) of [Stacks, Tag 0D2Z].**  For `k ≥ 1` and a scheme `w : W ⟶ X` such that
> `ψ|_W : (f ∘ w)^*𝒜_k ⟶ (w^*ℒ)^{⊗ k}` is surjective, `w` factors through `U(ψ)`.

```lean
theorem mem_subspaceOfOpens_of_epi {W : BigFppfOver B S hS} (w : W ⟶ X) {k : ℕ} (hk : 0 < k)
    [Epi ((ψ.pullback ((BigFppfOver.toScheme B S hS).map w)).app (k : ℤ))] :
    w ∈ (subspaceOfOpens B S hS X (toGradedPowerMap ψ).coveringOpen).obj (op W)
```

**`AlgebraicGeometry.Space.RelativeProjPoints.locusFactor_invertibleMorphism_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L276). The attribute's comment: “variant: clause (2)(b), for a presentation of Proj_Y(A) by its base changes to the scheme points of Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **Clause (2)(b) of [Stacks, Tag 0D2Z].**  For `k ≥ 1` and a scheme `w : W ⟶ X` such that
> `ψ|_W` is surjective in degree `k`, the composite of the factorisation `W ⟶ U(ψ)` with
> `r_{ℒ,ψ}` is the morphism `W ⟶ Proj_Y(𝒜)` which the construction of the relative Proj attaches to
> the quadruple `(k, W ⟶ Y, ℒ^{⊗ k}|_W, ψ|_W)`.

```lean
theorem locusFactor_invertibleMorphism_of_epi {W : BigFppfOver B S hS} (w : W ⟶ X) {k : ℕ}
    (hk : 0 < k) [Epi ((ψ.pullback ((BigFppfOver.toScheme B S hS).map w)).app (k : ℤ))] :
    d.locusFactor ψ w (d.mem_subspaceOfOpens_of_epi ψ w hk) ≫ d.invertibleMorphism ψ
      = d.quadruplePoint ψ w hk
```

**`AlgebraicGeometry.Space.RelativeProjPoints.eq_invertibleMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L292). The attribute's comment: “variant: the characterization of r_{L,psi} by clause (2)(b), for a presentation of Proj_Y(A) by its base changes to the scheme points of Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`r_{ℒ,ψ}` is characterized by clause (2)**: a morphism `U(ψ) ⟶ Proj_Y(𝒜)` over `Y` which, on
> every test scheme `W ⟶ X` over which `ψ` is surjective in some positive degree, is the morphism
> attached to the quadruple of clause (2)(b), is `r_{ℒ,ψ}`.

```lean
theorem eq_invertibleMorphism
    (Φ : (subspaceOfOpens B S hS X (toGradedPowerMap ψ).coveringOpen).toFunctor ⟶ Proj)
    (hΦπ : Φ ≫ π = (subspaceOfOpens B S hS X (toGradedPowerMap ψ).coveringOpen).ι ≫ f)
    (hΦ : ∀ {W : BigFppfOver B S hS} (w : W ⟶ X) {k : ℕ} (hk : 0 < k)
      [Epi ((ψ.pullback ((BigFppfOver.toScheme B S hS).map w)).app (k : ℤ))],
      d.locusFactor ψ w (d.mem_subspaceOfOpens_of_epi ψ w hk) ≫ Φ = d.quadruplePoint ψ w hk) :
    Φ = d.invertibleMorphism ψ
```

**`AlgebraicGeometry.Space.RelativeProjPoints.invertibleMorphism_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L357). The attribute's comment: “variant: clause (3) for the morphism, for the squares in which Y' -> Y is the scheme point f : X -> Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **Clause (3) of [Stacks, Tag 0D2Z], for the morphism, when `Y' ⟶ Y` is the point `f`.**
> Consider the square with `Y' = X`, `g = f : Y' ⟶ Y`, a scheme `g' : X' ⟶ X` and `f' = g'`, so that
> `𝒜' = f^*𝒜`, `ℒ' = g'^*ℒ` and `ψ' = g'^*ψ`.  Then `U(ψ') = g'^{-1}(U(ψ))`
> (`…RelativeProjInvertibleMorphism.coveringOpen_pullback`), and `r_{ℒ',ψ'}` of
> [Stacks, Tag 01O9] agrees with the base change of `r_{ℒ,ψ}` through
> `Proj_X(f^*𝒜) = X ×_Y Proj_Y(𝒜)`: on every test scheme `t : T ⟶ X'` of `U(ψ')`, the point
> `(f' ∘ t, r_{ℒ,ψ}(g' ∘ t))` of `X ×_Y Proj_Y(𝒜)` is `r_{ℒ',ψ'} ∘ t`.

```lean
theorem invertibleMorphism_baseChange {X' T : BigFppfOver B S hS} (g' : X' ⟶ X) (t : T ⟶ X')
    (ht : t ≫ g' ∈ (subspaceOfOpens B S hS X (toGradedPowerMap ψ).coveringOpen).obj (op T)) :
    (d.pointEquivProjOver X f (t ≫ g')
        ⟨d.locusFactor ψ (t ≫ g') ht ≫ d.invertibleMorphism ψ, by
          rw [Category.assoc, invertibleMorphism_comp_π, ← Category.assoc, locusFactor_ι]⟩).1
      = liftOfPreimageEqTop _ _ (d.preimage_coveringOpen_pullback_eq_top ψ g' t ht)
        ≫ (toGradedPowerMap (ψ.pullback ((BigFppfOver.toScheme B S hS).map g'))).globalMorphism
          (relativeProj (d.algebra X f))
```

**`AlgebraicGeometry.Space.RelativeProjPoints.invertibleTheta_clauseOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismPoints.lean#L382). The attribute's comment: “variant: theta and clause (1) after base change to the scheme point f : X -> Y, for the opens of X; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`θ` and clause (1) of [Stacks, Tag 0D2Z], after base change to the scheme point
> `f : X ⟶ Y`.**  The twists of `Proj_Y(𝒜)` are given at the scheme points of `Y`
> ([Stacks, Tag 084D]); at `f` they are the twists of `Proj_X(f^*𝒜)`, so
> `r^*(⨁ 𝒪(d))` is the inverse image along `U(ψ) ⟶ Proj_X(f^*𝒜)` of those twists, and `θ` is the
> map of [Stacks, Tag 01O9].  It preserves the unit and is multiplicative, and for every open `V`
> of `X`, `d ≥ 0` and `a ∈ (f^*𝒜)_d(V)` it carries the inverse image of `ψ_P(a)` to the restriction
> of `ψ(a)` to `U(ψ) ∩ V`: the square of clause (1).

```lean
theorem invertibleTheta_clauseOne :
    SheafOfModules.sectionsMap (((toGradedPowerMap ψ).theta).app 0)
        (Stacks.Conormal.gradedPullback
          ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)))
          (twistDataOfGradedAlgebra (d.algebra X f)).algebra).one
      = (Stacks.AlgebraicGeometry.ProjChartGradedTriple.laurentOn L
          (toGradedPowerMap ψ).coveringOpen).one
    ∧ (∀ (n e : ℕ) (U : (toGradedPowerMap ψ).coveringOpen.toScheme.Opens)
        (x : ((Stacks.Conormal.gradedPullback
          ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)))
          (twistDataOfGradedAlgebra (d.algebra X f)).algebra).piece (n : ℤ)).val.obj (op U))
        (y : ((Stacks.Conormal.gradedPullback
          ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)))
          (twistDataOfGradedAlgebra (d.algebra X f)).algebra).piece (e : ℤ)).val.obj (op U)),
        (((toGradedPowerMap ψ).theta.app ((n : ℤ) + (e : ℤ))).val.app (op U)
            (((Stacks.Conormal.gradedPullback
              ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)))
              (twistDataOfGradedAlgebra (d.algebra X f)).algebra).mul n e).app (op U) x y))
          = ((Stacks.AlgebraicGeometry.ProjChartGradedTriple.laurentOn L
              (toGradedPowerMap ψ).coveringOpen).mul n e).app (op U)
              (((toGradedPowerMap ψ).theta.app n).val.app (op U) x)
              (((toGradedPowerMap ψ).theta.app e).val.app (op U) y))
    ∧ (∀ (V : ((BigFppfOver.toScheme B S hS).obj X).Opens) (n : ℕ)
        (a : Γ((d.algebra X f).piece (n : ℤ), V)),
        ((Stacks.AmpleProjectiveImmersion.tensorPowerModule _ L (n : ℤ)).restrict
            (toGradedPowerMap ψ).coveringOpen.ι).presheaf.map
            (eqToHom ((toGradedPowerMap ψ).toBase_preimage_eq V)).op
            (((toGradedPowerMap ψ).theta.app n).val.app
              (op ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)) ⁻¹ᵁ
                ((relativeProj (d.algebra X f)).toBase ⁻¹ᵁ V)))
              (Stacks.RingedSpace.pullbackUnit
                ((toGradedPowerMap ψ).globalMorphism
                  (relativeProj (d.algebra X f))).toLRSHom.toShHom
                ((twistDataOfGradedAlgebra (d.algebra X f)).algebra.piece (n : ℤ))
                (op ((relativeProj (d.algebra X f)).toBase ⁻¹ᵁ V))
                (((twistDataOfGradedAlgebra (d.algebra X f)).ψ n).app V a)))
          = (Stacks.AmpleProjectiveImmersion.tensorPowerModule _ L (n : ℤ)).presheaf.map
              (homOfLE ((toGradedPowerMap ψ).coveringOpen.ι.image_preimage_le
                (𝟙 ((BigFppfOver.toScheme B S hS).obj X) ⁻¹ᵁ V))).op
              ((Stacks.AlgebraicGeometry.CoherentMulSections.powCompare L n).hom.app
                (𝟙 ((BigFppfOver.toScheme B S hS).obj X) ⁻¹ᵁ V)
                ((toGradedPowerMap ψ).value n V a)))
```

**`AlgebraicGeometry.Space.RelativeProjSituation.quadrupleSpaceEquiv_invertibleMorphism_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismQuadruple.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismQuadruple.lean#L291). The attribute's comment: “variant: clause (2)(b) read on the functor of quadruples of Tag 084A at every quasi-compact W' -> W; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **Clause (2)(b) of Stacks 0D2Z on the constructed relative Proj, for an arbitrary scheme
> `W ⟶ X`.**
>
> Let `F = Proj_Y(𝒜)` be the functor of quadruples of Stacks 084A of Situation 0849, constructed as
> `AlgebraicGeometry.Space.RelativeProjSituation.relativeProjFunctor`, and let
> `r_{ℒ,ψ} : U(ψ) ⟶ F` be the morphism of Stacks 0D2Z for a homomorphism of graded algebras
> `ψ : f^*𝒜 ⟶ ⨁_{d ≥ 0} ℒ^{⊗ d}` on a scheme `f : X ⟶ Y`. For `k ≥ 1` and a scheme `w : W ⟶ X`
> over which `ψ|_W` is surjective in degree `k`, the composite `W ⟶ U(ψ) ⟶ F` is the morphism given
> by the construction of `F`: the point of `F(W)` it defines records, at every quasi-compact test
> object `v : W' ⟶ W`, the point of `F(W')` over `f ∘ w ∘ v` given by the class of the pullback
> along `v` of the quadruple `(k, w, (w^*ℒ)^{⊗ k}, ψ^{(k)}|_W)`, transported from the algebra
> `(w ∘ v)^*(f^*𝒜)` to the algebra `(f ∘ w ∘ v)^*𝒜` along the comparison of the restriction datum
> of the situation.

```lean
theorem quadrupleSpaceEquiv_invertibleMorphism_val
    {W : BigFppfOver s.site s.base s.containsBase} (w : W ⟶ X) {k : ℕ} (hk : 0 < k)
    [Epi ((ψ.pullback ((BigFppfOver.toScheme s.site s.base s.containsBase).map w)).app (k : ℤ))]
    (W' : BigFppfOver s.site s.base s.containsBase)
    (hW' : CompactSpace ((BigFppfOver.toScheme s.site s.base s.containsBase).obj W'))
    (v : W' ⟶ W) :
    (s.quadrupleRestriction.quadrupleSpaceEquiv s.shrink.contains_relativeProj_pointAlgebra
        s.space.property.isSheaf W
        (yonedaEquiv (s.relativeProjPoints.locusFactor ψ w
          (s.relativeProjPoints.mem_subspaceOfOpens_of_epi ψ w hk) ≫
            s.relativeProjPoints.invertibleMorphism ψ))).val W' hW' v =
      ⟨yoneda.map (v ≫ w) ≫ f,
        s.quadrupleRestriction.fibreOfF f (v ≫ w) (yoneda.map (v ≫ w) ≫ f) rfl
          (F.pullback ((BigFppfOver.toScheme s.site s.base s.containsBase).map v)
            (clauseTwoClass ψ ((BigFppfOver.toScheme s.site s.base s.containsBase).map w) hk))
          ((pullback_clauseTwoClass_fst ψ _ _ hk).trans
            ((congrArg (_ ≫ ·) (Category.comp_id _)).trans (Functor.map_comp _ _ _).symm))⟩
```

**`AlgebraicGeometry.Space.InvertibleQuotientLocus.morphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean#L220). The attribute's comment: “variant: the morphism r_{L,psi} built from a family of degree-one restrictions of psi to the test schemes of U(psi); the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`r_{ℒ,ψ} : U(ψ) ⟶ Proj_Y(𝒜)`, the morphism of [Stacks, Tag 0D2Z].**
>
> Its value on a test scheme `W ⟶ X` of `U(ψ)` is the morphism `W ⟶ Proj_Y(𝒜)` that the
> construction of the relative Proj attaches to `ψ|_W`, and its naturality is the compatibility of
> the restrictions of `ψ` with base change: this is the transformation of functors the source's
> proof produces.

```lean
public def morphism : L.locus.toFunctor ⟶ Proj
```

**`AlgebraicGeometry.Space.InvertibleQuotientLocus.morphism_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean#L233). The attribute's comment: “variant: the morphism of `morphism` lies over Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`r_{ℒ,ψ}` is a morphism over `Y`**, as [Stacks, Tag 0D2Z] asserts: composing it with the
> structure morphism `π : Proj_Y(𝒜) ⟶ Y` gives the restriction of `f : X ⟶ Y` to `U(ψ)`.

```lean
public theorem morphism_comp_toBase : L.morphism hgen rep ≫ π = L.locus.ι ≫ f
```

**`AlgebraicGeometry.Space.InvertibleQuotientLocus.factor_comp_morphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean#L265). The attribute's comment: “variant: clause (2)(b) for the morphism of `morphism`, at the test schemes of U(psi); the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **Clause (2)(b) of [Stacks, Tag 0D2Z].**  For a scheme `W ⟶ X` lying in `U(ψ)`, the composite
> of the factorisation `W ⟶ U(ψ)` with `r_{ℒ,ψ}` is the morphism `W ⟶ Proj_Y(𝒜)` that the
> construction of the relative Proj attaches to `ψ|_W` — in this library, the morphism the
> representing bijection of [Stacks, Tag 085D] attaches to it.

```lean
public theorem factor_comp_morphism {W : BigFppfOver B S hS} (w : W ⟶ X)
    (hw : w ∈ L.locus.obj (op W)) :
    L.factor w hw ≫ L.morphism hgen rep = d.pointOfPair TA i hgen rep X f w (L.pair hw)
```

**`AlgebraicGeometry.Space.InvertibleQuotientLocus.eq_morphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleMorphismSpaces.lean#L287). The attribute's comment: “variant: the uniqueness of the morphism of `morphism` given clause (2)(b); the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **`r_{ℒ,ψ}` is the only morphism with clause (2)(b).**  Together with `factor_comp_morphism`
> this is the "characterized by" of [Stacks, Tag 0D2Z] for clause (2)(b): every test scheme of
> `U(ψ)` carries a restriction of `ψ`, so clause (2)(b) prescribes the morphism on every point of
> `U(ψ)`.

```lean
public theorem eq_morphism (Φ : L.locus.toFunctor ⟶ Proj)
    (hΦ : ∀ {W : BigFppfOver B S hS} (w : W ⟶ X) (hw : w ∈ L.locus.obj (op W)),
      L.factor w hw ≫ Φ = d.pointOfPair TA i hgen rep X f w (L.pair hw)) :
    Φ = L.morphism hgen rep
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.isOpenSubspace_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L311). The attribute's comment: “the source U(psi) of r_{L,psi}, for an algebraic space X, is an open subspace of X”.

> **`U(ψ)` is an open subspace of the algebraic space `X`.**  Its points are those near which
> some `f^*𝒜_d ⟶ ℒ^{⊗ d}`, `d ≥ 1`, is surjective (`…mem_locusOpen_iff_exists_epi`), and its
> preimage along a scheme point `x` is `U(x^*ψ)` (`…preimage_locus`).

```lean
theorem isOpenSubspace_locus (hX : IsAlgebraicSpace s.site s.base s.containsBase X) :
    IsOpenSubspace s.site s.base s.containsBase R.locus
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.invertibleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L503). The attribute's comment: “the canonical morphism r_{L,psi} : U(psi) -> Proj_Y(A) for a morphism of algebraic spaces f : X -> Y, an invertible O_X-module L and a homomorphism of graded algebras psi : f^*A -> (+)_d L^d, given on X by their restrictions to the scheme points of X; U(psi) is the open subspace of the algebraic space X of Tag 0D2Y and Proj_Y(A) the relative Proj of Tag 084A/084B”.

> **`r_{ℒ,ψ} : U(ψ) ⟶ Proj_Y(𝒜)`, the morphism of [Stacks, Tag 0D2Z], for a morphism of
> algebraic spaces `f : X ⟶ Y`**, as the transformation of functors on the big fppf site that the
> source's proof builds: its value on a scheme point `x : T ⟶ U(ψ)` is the morphism of
> [Stacks, Tag 01O9] for the restriction `x^*ψ` (`point`), read in `Proj_Y(𝒜)` through
> `T ×_Y Proj_Y(𝒜) = Proj_T((f ∘ x)^*𝒜)`; its naturality is clause (3) of the scheme case.

```lean
def invertibleMorphism : R.locus.toFunctor ⟶ s.relativeProjFunctor
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.invertibleMorphism_comp_π`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L515). The attribute's comment: “r_{L,psi} is a morphism of algebraic spaces over Y, for a morphism of algebraic spaces f : X -> Y”.

> **`r_{ℒ,ψ}` is a morphism over `Y`**: `π ∘ r_{ℒ,ψ}` is the restriction of `f` to `U(ψ)`.

```lean
theorem invertibleMorphism_comp_π :
    R.invertibleMorphism ≫ s.relativeProjπ = R.locus.ι ≫ f
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.mem_locus_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L547). The attribute's comment: “clause (2)(a), for a morphism of algebraic spaces f : X -> Y: a scheme W -> X over which psi is surjective in some degree d >= 1 factors through the open subspace U(psi) of the algebraic space X”.

> **Clause (2)(a) of [Stacks, Tag 0D2Z].**  For `k ≥ 1` and a scheme `w : W ⟶ X` such that
> `ψ|_W : (f ∘ w)^*𝒜_k ⟶ (w^*ℒ)^{⊗ k}` is surjective, `w` factors through `U(ψ)`.

```lean
theorem mem_locus_of_epi {W : BigFppfOver s.site s.base s.containsBase} (w : yoneda.obj W ⟶ X)
    {k : ℕ} (hk : 0 < k) [hw : Epi ((R.twisting W w).app (k : ℤ))] :
    yonedaEquiv w ∈ R.locus.obj (op W)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.factor_invertibleMorphism_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L573). The attribute's comment: “clause (2)(b), for a morphism of algebraic spaces f : X -> Y: for a scheme W -> X over which psi is surjective in degree k >= 1, W -> U(psi) -> Proj_Y(A) is the morphism the construction of the relative Proj attaches to the quadruple (k, W -> Y, L^k|_W, psi|_W)”.

> **Clause (2)(b) of [Stacks, Tag 0D2Z].**  For `k ≥ 1` and a scheme `w : W ⟶ X` such that
> `ψ|_W` is surjective in degree `k`, the composite of the factorisation `W ⟶ U(ψ)` with
> `r_{ℒ,ψ}` is the morphism `W ⟶ Proj_Y(𝒜)` which the construction of the relative Proj attaches to
> the quadruple `(k, W ⟶ Y, ℒ^{⊗ k}|_W, ψ|_W)`.

```lean
theorem factor_invertibleMorphism_of_epi {W : BigFppfOver s.site s.base s.containsBase}
    (w : yoneda.obj W ⟶ X) {k : ℕ} (hk : 0 < k) [hw : Epi ((R.twisting W w).app (k : ℤ))] :
    R.factor w (R.mem_locus_of_epi w hk) ≫ R.invertibleMorphism = R.quadruplePoint w hk
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.eq_invertibleMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 610](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L610). The attribute's comment: “r_{L,psi} is characterized by property (2), for a morphism of algebraic spaces f : X -> Y: it is the only morphism U(psi) -> Proj_Y(A) over Y with clause (2)(b)”.

> **`r_{ℒ,ψ}` is characterized by clause (2)**: a morphism `U(ψ) ⟶ Proj_Y(𝒜)` over `Y` which,
> on every scheme `W ⟶ X` over which `ψ` is surjective in some positive degree, is the morphism
> attached to the quadruple of clause (2)(b), is `r_{ℒ,ψ}`.

```lean
theorem eq_invertibleMorphism (Φ : R.locus.toFunctor ⟶ s.relativeProjFunctor)
    (hΦπ : Φ ≫ s.relativeProjπ = R.locus.ι ≫ f)
    (hΦ : ∀ {W : BigFppfOver s.site s.base s.containsBase} (w : yoneda.obj W ⟶ X) {k : ℕ}
      (hk : 0 < k) [Epi ((R.twisting W w).app (k : ℤ))],
      R.factor w (R.mem_locus_of_epi w hk) ≫ Φ = R.quadruplePoint w hk) :
    Φ = R.invertibleMorphism
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.invertibleMorphism_baseChange_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean, line 752](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpace.lean#L752). The attribute's comment: “clause (3), the open and the morphism, for a morphism of algebraic spaces f : X -> Y and an ARBITRARY commutative square g o f' = f o g' with X', Y' schemes: with psi' the pullback of psi, U(psi') = (g')^{-1}(U(psi)) as open subspaces, and r_{psi',L'} : U(psi') -> Proj_{Y'}(g^*A) of Tag 01O9 is the base change of r_{L,psi} through the identification Proj_{Y'}(g^*A) = Y' x_Y Proj_Y(A) of Tag 084B, tested on every scheme T -> U(psi')”.

> **Clause (3) of [Stacks, Tag 0D2Z], for a morphism of algebraic spaces `f : X ⟶ Y`.**
> Consider a commutative square `g ∘ f' = f ∘ g'` with `g' : X' ⟶ X`, `f' : X' ⟶ Y'`,
> `g : Y' ⟶ Y` and `X'`, `Y'` schemes, `𝒜' = g^*𝒜`, `ℒ' = (g')^*ℒ`, and let `ψ'` be the pullback
> of `ψ` (`squarePsi`).  Then
>
> * `U(ψ') = (g')^{-1}(U(ψ))`: the preimage of the open subspace `U(ψ) ⊆ X` along `g'` is the open
>   subscheme `U(ψ')` of `X'` of [Stacks, Tag 01O9]; and
> * `r_{ψ',ℒ'} : U(ψ') ⟶ Proj_{Y'}(𝒜')` of [Stacks, Tag 01O9] agrees with the base change of
>   `r_{ψ,ℒ}` through the identification `Proj_{Y'}(𝒜') = Y' ×_Y Proj_Y(𝒜)` of Stacks 084B: for
>   every test scheme `t : T ⟶ X'` of `U(ψ')`, the `T`-point of `Y' ×_Y Proj_Y(𝒜)` with components
>   `f' ∘ t` and `r_{ψ,ℒ} ∘ g' ∘ t` is, in `Proj_{Y'}(𝒜')`, the composite
>   `T ⟶ U(ψ') ⟶ Proj_{Y'}(𝒜')`.

```lean
theorem invertibleMorphism_baseChange_square {X' Y' : BigFppfOver s.site s.base s.containsBase}
    (g' : yoneda.obj X' ⟶ X) (f' : X' ⟶ Y') (g : yoneda.obj Y' ⟶ s.space.1)
    (hsq : yoneda.map f' ≫ g = g' ≫ f) :
    R.locus.preimage g' = subspaceOfOpens s.site s.base s.containsBase X'
        (toGradedPowerMap (R.squarePsi g' f' g hsq)).coveringOpen ∧
    ∀ {T : BigFppfOver s.site s.base s.containsBase} (t : T ⟶ X')
      (ht : yonedaEquiv (yoneda.map t ≫ g') ∈ R.locus.obj (op T)),
      (s.relativeProjPoints.pointEquivProjOver Y' g (t ≫ f')
          ⟨R.factor (yoneda.map t ≫ g') ht ≫ R.invertibleMorphism,
            R.factor_invertibleMorphism_comp_π g' f' g hsq t ht⟩).1 =
        liftOfPreimageEqTop _ ((BigFppfOver.toScheme s.site s.base s.containsBase).map t)
            (R.preimage_coveringOpen_squarePsi_eq_top g' f' g hsq t ht) ≫
          (toGradedPowerMap (R.squarePsi g' f' g hsq)).globalMorphism
            (relativeProj (s.relativeProjPoints.algebra Y' g))
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.isOpenSubspace_locus_ofUnitalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean#L543). The attribute's comment: “the source U(psi) of r_{L,psi}, for an algebraic space X with an invertible O_X-module L on its small etale site and a homomorphism of graded algebras psi : f^*A -> (+)_n L^n on X: an open subspace of X”.

> **`U(ψ)` is an open subspace of the algebraic space `X`**, for a pair `(ℒ, ψ)` on `X`.

```lean
theorem isOpenSubspace_locus_ofUnitalHom :
    IsOpenSubspace s.site s.base s.containsBase (ofUnitalHom s f L ψ).locus
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.invertibleMorphism_comp_π_ofUnitalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean#L552). The attribute's comment: “the canonical morphism r_{L,psi} : U(psi) -> Proj_Y(A) over Y, for an algebraic space X with an invertible O_X-module L on its small etale site and a homomorphism of graded algebras psi : f^*A -> (+)_n L^n on X”.

> **`r_{ℒ,ψ} : U(ψ) ⟶ Proj_Y(𝒜)` is a morphism over `Y`**, for a pair `(ℒ, ψ)` on the algebraic
> space `X`.

```lean
theorem invertibleMorphism_comp_π_ofUnitalHom :
    (ofUnitalHom s f L ψ).invertibleMorphism ≫ s.relativeProjπ =
      (ofUnitalHom s f L ψ).locus.ι ≫ f.hom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.mem_locus_ofUnitalHom_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean#L563). The attribute's comment: “clause (2)(a), for a pair (L, psi) on an algebraic space X: a scheme W -> X over which psi|_W is surjective in some degree k >= 1 factors through U(psi)”.

> **Clause (2)(a) of [Stacks, Tag 0D2Z]** for a pair `(ℒ, ψ)` on the algebraic space `X`: a
> scheme `w : W ⟶ X` over which `ψ|_W : (f ∘ w)^*𝒜_k ⟶ (w^*ℒ)^{⊗ k}` is surjective for some
> `k ≥ 1` factors through `U(ψ)`. Here `ψ|_W` is the restriction `(ofUnitalHom s f L ψ).twisting W w`
> of `ψ` to `W` (`pointTwisting`, the map of `AlgebraicGeometry.Space.pointPsi`).

```lean
theorem mem_locus_ofUnitalHom_of_epi {W : BigFppfOver s.site s.base s.containsBase}
    (w : yoneda.obj W ⟶ X.1) {k : ℕ} (hk : 0 < k)
    [Epi (((ofUnitalHom s f L ψ).twisting W w).app (k : ℤ))] :
    yonedaEquiv w ∈ (ofUnitalHom s f L ψ).locus.obj (op W)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.factor_invertibleMorphism_ofUnitalHom_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean#L576). The attribute's comment: “clause (2)(b), for a pair (L, psi) on an algebraic space X: for a scheme W -> X over which psi|_W is surjective in degree k >= 1, W -> U(psi) -> Proj_Y(A) is the morphism attached to the quadruple (k, W -> Y, L^k|_W, psi|_W)”.

> **Clause (2)(b) of [Stacks, Tag 0D2Z]** for a pair `(ℒ, ψ)` on the algebraic space `X`: for a
> scheme `w : W ⟶ X` over which `ψ|_W` is surjective in degree `k ≥ 1`, the composite
> `W ⟶ U(ψ) ⟶ Proj_Y(𝒜)` is the morphism which the construction of the relative Proj attaches to
> the quadruple `(k, W ⟶ Y, ℒ^{⊗ k}|_W, ψ|_W)`.

```lean
theorem factor_invertibleMorphism_ofUnitalHom_of_epi {W : BigFppfOver s.site s.base s.containsBase}
    (w : yoneda.obj W ⟶ X.1) {k : ℕ} (hk : 0 < k)
    [Epi (((ofUnitalHom s f L ψ).twisting W w).app (k : ℤ))] :
    (ofUnitalHom s f L ψ).factor w (mem_locus_ofUnitalHom_of_epi s f L ψ w hk) ≫
        (ofUnitalHom s f L ψ).invertibleMorphism =
      (ofUnitalHom s f L ψ).quadruplePoint w hk
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.eq_invertibleMorphism_ofUnitalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean#L590). The attribute's comment: “r_{L,psi} is characterized by property (2), for a pair (L, psi) on an algebraic space X: it is the only morphism U(psi) -> Proj_Y(A) over Y with clause (2)(b)”.

> **`r_{ℒ,ψ}` is characterized by clause (2)**, for a pair `(ℒ, ψ)` on the algebraic space `X`:
> a morphism `U(ψ) ⟶ Proj_Y(𝒜)` over `Y` which, on every scheme `W ⟶ X` over which `ψ|_W` is
> surjective in some degree `k ≥ 1`, is the morphism attached to the quadruple of clause (2)(b), is
> `r_{ℒ,ψ}`.

```lean
theorem eq_invertibleMorphism_ofUnitalHom
    (Φ : (ofUnitalHom s f L ψ).locus.toFunctor ⟶ s.relativeProjFunctor)
    (hΦπ : Φ ≫ s.relativeProjπ = (ofUnitalHom s f L ψ).locus.ι ≫ f.hom)
    (hΦ : ∀ {W : BigFppfOver s.site s.base s.containsBase} (w : yoneda.obj W ⟶ X.1) {k : ℕ}
      (hk : 0 < k) [Epi (((ofUnitalHom s f L ψ).twisting W w).app (k : ℤ))],
      (ofUnitalHom s f L ψ).factor w (mem_locus_ofUnitalHom_of_epi s f L ψ w hk) ≫ Φ =
        (ofUnitalHom s f L ψ).quadruplePoint w hk) :
    Φ = (ofUnitalHom s f L ψ).invertibleMorphism
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.invertibleMorphism_baseChange_square_ofUnitalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceModule.lean#L614). The attribute's comment: “clause (3), the open and the morphism, for a pair (L, psi) on an algebraic space X and an arbitrary commutative square g o f' = f o g' with X', Y' schemes: U(psi') = (g')^{-1}(U(psi)) and r_{psi',L'} is the base change of r_{L,psi}”.

> **Clause (3) of [Stacks, Tag 0D2Z]** for a pair `(ℒ, ψ)` on the algebraic space `X`: for a
> commutative square `g ∘ f' = f ∘ g'` with `X'`, `Y'` schemes and `ψ'` the pullback of `ψ`,
> `U(ψ') = (g')^{-1}(U(ψ))` and `r_{ψ',ℒ'}` of Tag 01O9 is the base change of `r_{ℒ,ψ}` through
> `Proj_{Y'}(g^*𝒜) = Y' ×_Y Proj_Y(𝒜)`, tested on every scheme `T ⟶ U(ψ')`.

```lean
theorem invertibleMorphism_baseChange_square_ofUnitalHom
    {X' Y' : BigFppfOver s.site s.base s.containsBase} (g' : yoneda.obj X' ⟶ X.1)
    (f' : X' ⟶ Y') (g : yoneda.obj Y' ⟶ s.space.1) (hsq : yoneda.map f' ≫ g = g' ≫ f.hom) :
    (ofUnitalHom s f L ψ).locus.preimage g' = subspaceOfOpens s.site s.base s.containsBase X'
        (toGradedPowerMap ((ofUnitalHom s f L ψ).squarePsi g' f' g hsq)).coveringOpen ∧
    ∀ {T : BigFppfOver s.site s.base s.containsBase} (t : T ⟶ X')
      (ht : yonedaEquiv (yoneda.map t ≫ g') ∈ (ofUnitalHom s f L ψ).locus.obj (op T)),
      (s.relativeProjPoints.pointEquivProjOver Y' g (t ≫ f')
          ⟨(ofUnitalHom s f L ψ).factor (yoneda.map t ≫ g') ht ≫
              (ofUnitalHom s f L ψ).invertibleMorphism,
            (ofUnitalHom s f L ψ).factor_invertibleMorphism_comp_π g' f' g hsq t ht⟩).1 =
        liftOfPreimageEqTop _ ((BigFppfOver.toScheme s.site s.base s.containsBase).map t)
            ((ofUnitalHom s f L ψ).preimage_coveringOpen_squarePsi_eq_top g' f' g hsq t ht) ≫
          (toGradedPowerMap ((ofUnitalHom s f L ψ).squarePsi g' f' g hsq)).globalMorphism
            (relativeProj (s.relativeProjPoints.algebra Y' g))
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.tag0D2Z_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceTheta0D2Z.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceTheta0D2Z.lean#L238). The attribute's comment: “the whole lemma, in Situation 0849 with Proj_Y(A) the relative Proj of Stacks 084B and X an algebraic space over the algebraic space Y: U(psi) an open subspace of X; the morphism r_{L,psi} : U(psi) -> Proj_Y(A) over Y with clauses (2)(a), (2)(b) and characterized by (2)(b); clause (3) for the open and the morphism; theta : r^*((+)_d O(d)) -> (+)_d L^d|_{U(psi)} a unital multiplicative map with clause (1), restricting at every scheme point of U(psi) to theta of Tag 01O9 and along every square with X', Y' schemes to the theta of the pulled-back psi (clause (3)), and the only map with these restrictions”.

> **[Stacks, Tag 0D2Z] for `X` an algebraic space.**  In Situation 0849 let `f : X ⟶ Y` be a
> morphism of algebraic spaces, `ℒ` an invertible `𝒪_X`-module and `ψ : f^*𝒜 ⟶ ⨁_d ℒ^{⊗ d}` a
> homomorphism of graded algebras.  Then `U(ψ)` is an open subspace of `X`, `r_{ℒ,ψ} : U(ψ) ⟶
> Proj_Y(𝒜)` is a morphism over `Y` with clauses (2)(a), (2)(b), characterized by (2)(b), and
> satisfying clause (3); and there is a map `θ : r^*(⨁_d 𝒪(d)) ⟶ ⨁_d ℒ^{⊗ d}|_{U(ψ)}` of graded
> algebras with clause (1), whose restriction to every scheme point `w : W ⟶ U(ψ)` is `θ` of
> [Stacks, Tag 01O9] for `w^*ψ`, which for every square `g ∘ f' = f ∘ g'` with `X'`, `Y'` schemes
> restricts to the map `θ'` of the pullback `ψ'` on every scheme over `U(ψ') = (g')^{-1}(U(ψ))`
> (clause (3)), and which is the only map with these restrictions.

```lean
theorem tag0D2Z_space :
    IsOpenSubspace s.site s.base s.containsBase (ofUnitalHom s f L ψ).locus ∧
    (ofUnitalHom s f L ψ).invertibleMorphism ≫ s.relativeProjπ =
      (ofUnitalHom s f L ψ).locus.ι ≫ f.hom ∧
    (∀ {W : BigFppfOver s.site s.base s.containsBase} (w : yoneda.obj W ⟶ X.1) {k : ℕ}
      (_ : 0 < k) [Epi (((ofUnitalHom s f L ψ).twisting W w).app (k : ℤ))],
      yonedaEquiv w ∈ (ofUnitalHom s f L ψ).locus.obj (Opposite.op W)) ∧
    (∀ {W : BigFppfOver s.site s.base s.containsBase} (w : yoneda.obj W ⟶ X.1) {k : ℕ}
      (hk : 0 < k) [Epi (((ofUnitalHom s f L ψ).twisting W w).app (k : ℤ))],
      (ofUnitalHom s f L ψ).factor w (mem_locus_ofUnitalHom_of_epi s f L ψ w hk) ≫
          (ofUnitalHom s f L ψ).invertibleMorphism =
        (ofUnitalHom s f L ψ).quadruplePoint w hk) ∧
    (∀ Φ : (ofUnitalHom s f L ψ).locus.toFunctor ⟶ s.relativeProjFunctor,
      Φ ≫ s.relativeProjπ = (ofUnitalHom s f L ψ).locus.ι ≫ f.hom →
      (∀ {W : BigFppfOver s.site s.base s.containsBase} (w : yoneda.obj W ⟶ X.1) {k : ℕ}
        (hk : 0 < k) [Epi (((ofUnitalHom s f L ψ).twisting W w).app (k : ℤ))],
        (ofUnitalHom s f L ψ).factor w (mem_locus_ofUnitalHom_of_epi s f L ψ w hk) ≫ Φ =
          (ofUnitalHom s f L ψ).quadruplePoint w hk) →
      Φ = (ofUnitalHom s f L ψ).invertibleMorphism) ∧
    (∀ {X' Y' : BigFppfOver s.site s.base s.containsBase} (g' : yoneda.obj X' ⟶ X.1)
      (f' : X' ⟶ Y') (g : yoneda.obj Y' ⟶ s.space.1) (hsq : yoneda.map f' ≫ g = g' ≫ f.hom),
      (ofUnitalHom s f L ψ).locus.preimage g' = subspaceOfOpens s.site s.base s.containsBase X'
          (toGradedPowerMap ((ofUnitalHom s f L ψ).squarePsi g' f' g hsq)).coveringOpen ∧
      ∀ {T : BigFppfOver s.site s.base s.containsBase} (t : T ⟶ X')
        (ht : yonedaEquiv (yoneda.map t ≫ g') ∈ (ofUnitalHom s f L ψ).locus.obj (Opposite.op T)),
        (s.relativeProjPoints.pointEquivProjOver Y' g (t ≫ f')
            ⟨(ofUnitalHom s f L ψ).factor (yoneda.map t ≫ g') ht ≫
                (ofUnitalHom s f L ψ).invertibleMorphism,
              (ofUnitalHom s f L ψ).factor_invertibleMorphism_comp_π g' f' g hsq t ht⟩).1 =
          Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.liftOfPreimageEqTop _
              ((BigFppfOver.toScheme s.site s.base s.containsBase).map t)
              ((ofUnitalHom s f L ψ).preimage_coveringOpen_squarePsi_eq_top g' f' g hsq t ht) ≫
            (toGradedPowerMap ((ofUnitalHom s f L ψ).squarePsi g' f' g hsq)).globalMorphism
              (relativeProj
                (s.relativeProjPoints.algebra Y' g))) ∧
    ∃ θ : ∀ d : ℤ,
        (thetaSourceOfUnitalHom s f L ψ (basePresentation s) d).obj ⟶ (thetaTarget s f L ψ d).obj,
      (∀ i j : ℤ,
        thetaSourceMul (ofUnitalHom s f L ψ) X.property (basePresentation s) i j ≫ θ (i + j) =
          (θ i ⊗ₘ θ j) ≫ thetaTargetMul s f L ψ i j) ∧
      thetaSourceUnit (ofUnitalHom s f L ψ) X.property (basePresentation s) ≫ θ 0 =
        thetaTargetUnit s f L ψ ∧
      ClauseOneSections s f L ψ (basePresentation s) θ ∧
      (∀ (d : ℤ) {T : BigFppfOver s.shrink.site s.shrink.base s.shrink.containsBase}
        (w : yoneda.obj T ⟶ (locusSpaceOfUnitalHom s f L ψ).obj),
        (modulePullback s.shrink.site s.shrink.base s.shrink.containsBase (pointHom w)).map
            (θ d) =
          (chartSourceIso (basePresentation s) w (locusOpen_locusPoint w) d).hom ≫
            ((representedQuasicoherentSchemeEquivalence s.shrink.site s.shrink.base
                s.shrink.containsBase T).functor.map
              (chartSchemeTheta s f L ψ (locusPoint w) (locusOpen_locusPoint w) d)).hom ≫
            (chartTargetIso w d).hom) ∧
      (∀ {X' Y' : BigFppfOver s.site s.base s.containsBase} (g' : yoneda.obj X' ⟶ X.1)
        (f' : X' ⟶ Y') (g : yoneda.obj Y' ⟶ s.space.1) (hsq : yoneda.map f' ≫ g = g' ≫ f.hom)
        (d : ℤ) {T : BigFppfOver s.shrink.site s.shrink.base s.shrink.containsBase} (t : T ⟶ X')
        (w : yoneda.obj T ⟶ (locusSpaceOfUnitalHom s f L ψ).obj)
        (hw : yoneda.map t ≫ g' = locusPoint w)
        (k : (BigFppfOver.toScheme s.site s.base s.containsBase).obj T ⟶
          (toGradedPowerMap ((ofUnitalHom s f L ψ).squarePsi g' f' g hsq)).coveringOpen.toScheme)
        (hk : k ≫ (toGradedPowerMap ((ofUnitalHom s f L ψ).squarePsi g' f' g hsq)).coveringOpen.ι =
          (BigFppfOver.toScheme s.site s.base s.containsBase).map t),
        (modulePullback s.shrink.site s.shrink.base s.shrink.containsBase (pointHom w)).map
            (θ d) =
          (chartSourceIso (basePresentation s) w (locusOpen_locusPoint w) d).hom ≫
            ((representedQuasicoherentSchemeEquivalence s.shrink.site s.shrink.base
                s.shrink.containsBase T).functor.map
              (eqToHom (chartSchemeThetaSource_congr s f L ψ hw
                  (locusOpen_comp_eq_top_of_eq g' t w hw) (locusOpen_locusPoint w) d).symm ≫
                squarePointChartTheta s f L ψ g' f' g hsq t
                  (locusOpen_comp_eq_top_of_eq g' t w hw) k hk d ≫
                eqToHom (congrArg (fun z => pointLaurentPieceQcoh L T z d) hw))).hom ≫
            (chartTargetIso w d).hom) ∧
      (∀ θ' : ∀ d : ℤ,
          (thetaSourceOfUnitalHom s f L ψ (basePresentation s) d).obj ⟶ (thetaTarget s f L ψ d).obj,
        (∀ (d : ℤ) {T : BigFppfOver s.shrink.site s.shrink.base s.shrink.containsBase}
          (w : yoneda.obj T ⟶ (locusSpaceOfUnitalHom s f L ψ).obj),
          (modulePullback s.shrink.site s.shrink.base s.shrink.containsBase (pointHom w)).map
              (θ' d) =
            (chartSourceIso (basePresentation s) w (locusOpen_locusPoint w) d).hom ≫
              ((representedQuasicoherentSchemeEquivalence s.shrink.site s.shrink.base
                  s.shrink.containsBase T).functor.map
                (chartSchemeTheta s f L ψ (locusPoint w) (locusOpen_locusPoint w) d)).hom ≫
              (chartTargetIso w d).hom) →
        θ' = θ)
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.theta_map_eq_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceTheta.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceTheta.lean#L168). The attribute's comment: “theta for X an algebraic space, on the scheme points of U(psi): for scheme points x : T -> X and x o tau, tau : T' -> T, the map theta_{x o tau} of Tag 01O9 for (x o tau)^*psi is the pullback along tau of theta_x, through the canonical isomorphisms of the sources r'^*((+)_d O(d)) and of the targets (+)_d ((x o tau)^*L)^d. This is the last assertion of clause (3) for the square with Y' = X' = T' and f' = id, that is, the compatibility of the restrictions of theta between scheme points”.

> **The restriction of `θ` to the scheme point `x ∘ τ` is the pullback along `τ` of its
> restriction to `x`** (Stacks 0D2Z for an algebraic space `X`, on the scheme points of `U(ψ)`):
> `θ_{x ∘ τ}` is `j^*θ_x` for the restriction `j : U((x ∘ τ)^*ψ) ⟶ U(x^*ψ)` of `τ`, read through the
> identification of the sources (`…GradedAlgebraRestriction.squareThetaSourceIso`, then
> `…GradedPowerMap.thetaTransportSourceIso`) and of the targets
> (`…GradedAlgebraRestriction.squareThetaTargetIso`, then
> `…GradedPowerMap.thetaTransportTargetIso` for `τ^*(x^*ℒ) ≅ (x ∘ τ)^*ℒ`).

```lean
theorem theta_map_eq_pullback :
    (toGradedPowerMap (R.twisting T' (yoneda.map τ ≫ x))).theta =
      ((toGradedPowerMap (s.quadrupleRestriction.squareTwisting
          s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf (R.twisting T
            x)
          ((yoneda.map τ ≫ x) ≫ f) (𝟙 T') τ
          (yoneda_map_id_comp_assoc s f τ x))).thetaTransportSourceIso
        (R.coveringOpen_twisting_map_le τ x)
        (homOfLE_globalMorphism_of_eq_congrBase_congrModule (CategoryTheory.Functor.map_id _ T') _
          (R.lineIso τ x) _ (R.twisting_map τ x))).inv ≫
        pullbackGradedAlgebraMap
          (Scheme.homOfLE
            ((BigFppfOver.toScheme s.shrink.site s.shrink.base s.shrink.containsBase).obj T')
            (R.coveringOpen_twisting_map_le τ x)).toLRSHom.toShHom
          ((s.quadrupleRestriction.squareThetaSourceIso s.shrink.contains_relativeProj_pointAlgebra
              s.shrink.space.property.isSheaf (R.twisting T x) ((yoneda.map τ ≫ x) ≫ f) (𝟙 T') τ
              (yoneda_map_id_comp_assoc s f τ x)).inv ≫
            pullbackGradedAlgebraMap
              (Scheme.Hom.resLE
                ((BigFppfOver.toScheme s.shrink.site s.shrink.base s.shrink.containsBase).map τ)
                (toGradedPowerMap (R.twisting T x)).coveringOpen
                (toGradedPowerMap (s.quadrupleRestriction.squareTwisting
                  s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
                  (R.twisting T x) ((yoneda.map τ ≫ x) ≫ f) (𝟙 T') τ
                  (yoneda_map_id_comp_assoc s f τ x))).coveringOpen
                (s.quadrupleRestriction.coveringOpen_squareTwisting
                  s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
                  (R.twisting T x) ((yoneda.map τ ≫ x) ≫ f) (𝟙 T') τ
                  (yoneda_map_id_comp_assoc s f τ x)).le).toLRSHom.toShHom
              (toGradedPowerMap (R.twisting T x)).theta ≫
            (s.quadrupleRestriction.squareThetaTargetIso s.shrink.contains_relativeProj_pointAlgebra
              s.shrink.space.property.isSheaf (R.twisting T x) ((yoneda.map τ ≫ x) ≫ f) (𝟙 T') τ
              (yoneda_map_id_comp_assoc s f τ x)).hom) ≫
        ((toGradedPowerMap (s.quadrupleRestriction.squareTwisting
          s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf (R.twisting T
            x)
          ((yoneda.map τ ≫ x) ≫ f) (𝟙 T') τ
          (yoneda_map_id_comp_assoc s f τ x))).thetaTransportTargetIso
          (R.lineIso τ x) (R.coveringOpen_twisting_map_le τ x)).hom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.InvertibleTwistingRestriction.theta_map_eq_pullback_ofUnitalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceTheta.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSpaceTheta.lean#L248). The attribute's comment: “theta for an algebraic space X with an invertible O_X-module L on its small etale site and a homomorphism of graded algebras psi : f^*A -> (+)_n L^n, on the scheme points of U(psi): theta_{x o tau} is the pullback along tau of theta_x, through the canonical isomorphisms of the sources and of the targets”.

> **The restriction of `θ` to the scheme point `x ∘ τ` is the pullback along `τ` of its
> restriction to `x`**, for a pair `(ℒ, ψ)` on the small étale site of the algebraic space `X`:
> `theta_map_eq_pullback` for the restriction datum `ofUnitalHom s f L ψ` of `(ℒ, ψ)`.

```lean
theorem theta_map_eq_pullback_ofUnitalHom :
    (toGradedPowerMap ((ofUnitalHom s f L ψ).twisting T' (yoneda.map τ ≫ x))).theta =
      ((toGradedPowerMap (s.quadrupleRestriction.squareTwisting
          s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
          ((ofUnitalHom s f L ψ).twisting T x)
          ((yoneda.map τ ≫ x) ≫ f.hom) (𝟙 T') τ
          (yoneda_map_id_comp_assoc s f.hom τ x))).thetaTransportSourceIso
        ((ofUnitalHom s f L ψ).coveringOpen_twisting_map_le τ x)
        (homOfLE_globalMorphism_of_eq_congrBase_congrModule (CategoryTheory.Functor.map_id _ T') _
          ((ofUnitalHom s f L ψ).lineIso τ x) _ ((ofUnitalHom s f L ψ).twisting_map τ x))).inv ≫
        pullbackGradedAlgebraMap
          (Scheme.homOfLE
            ((BigFppfOver.toScheme s.shrink.site s.shrink.base s.shrink.containsBase).obj T')
            ((ofUnitalHom s f L ψ).coveringOpen_twisting_map_le τ x)).toLRSHom.toShHom
          ((s.quadrupleRestriction.squareThetaSourceIso s.shrink.contains_relativeProj_pointAlgebra
              s.shrink.space.property.isSheaf ((ofUnitalHom s f L ψ).twisting T x)
              ((yoneda.map τ ≫ x) ≫ f.hom) (𝟙 T') τ
              (yoneda_map_id_comp_assoc s f.hom τ x)).inv ≫
            pullbackGradedAlgebraMap
              (Scheme.Hom.resLE
                ((BigFppfOver.toScheme s.shrink.site s.shrink.base s.shrink.containsBase).map τ)
                (toGradedPowerMap ((ofUnitalHom s f L ψ).twisting T x)).coveringOpen
                (toGradedPowerMap (s.quadrupleRestriction.squareTwisting
                  s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
                  ((ofUnitalHom s f L ψ).twisting T x) ((yoneda.map τ ≫ x) ≫ f.hom) (𝟙 T') τ
                  (yoneda_map_id_comp_assoc s f.hom τ x))).coveringOpen
                (s.quadrupleRestriction.coveringOpen_squareTwisting
                  s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
                  ((ofUnitalHom s f L ψ).twisting T x) ((yoneda.map τ ≫ x) ≫ f.hom) (𝟙 T') τ
                  (yoneda_map_id_comp_assoc s f.hom τ x)).le).toLRSHom.toShHom
              (toGradedPowerMap ((ofUnitalHom s f L ψ).twisting T x)).theta ≫
            (s.quadrupleRestriction.squareThetaTargetIso s.shrink.contains_relativeProj_pointAlgebra
              s.shrink.space.property.isSheaf ((ofUnitalHom s f L ψ).twisting T x)
              ((yoneda.map τ ≫ x) ≫ f.hom) (𝟙 T') τ
              (yoneda_map_id_comp_assoc s f.hom τ x)).hom) ≫
        ((toGradedPowerMap (s.quadrupleRestriction.squareTwisting
          s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
          ((ofUnitalHom s f L ψ).twisting T x)
          ((yoneda.map τ ≫ x) ≫ f.hom) (𝟙 T') τ
          (yoneda_map_id_comp_assoc s f.hom τ x))).thetaTransportTargetIso
          ((ofUnitalHom s f L ψ).lineIso τ x)
          ((ofUnitalHom s f L ψ).coveringOpen_twisting_map_le τ x)).hom
```

**`AlgebraicGeometry.Space.RelativeProjSituation.invertibleMorphism_baseChange_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSquare.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSquare.lean#L730). The attribute's comment: “clause (3), the open and the morphism, at a scheme point f : X -> Y of the base (X a scheme), for an ARBITRARY commutative square g o f' = f o g' with X', Y' schemes, on the relative Proj constructed as the functor of quadruples of Tag 084A: with psi' the pullback of psi to (f')^*(g^*A) (through the comparisons (f')^*(g^*A) = (g o f')^*A = (f o g')^*A = (g')^*(f^*A)), U(psi') = (g')^{-1}(U(psi)), and r_{psi',L'} : U(psi') -> Proj_{Y'}(g^*A) of Tag 01O9 is the base change of r_{psi,L} through the identification Proj_{Y'}(g^*A) = Y' x_Y Proj_Y(A) of Tag 084B, tested on every scheme T -> U(psi')”.

> **Clause (3) of Stacks 0D2Z, for the open and the morphism, for an arbitrary commutative
> square, on the constructed relative Proj.**
>
> Let `F = Proj_Y(𝒜)` be the relative Proj of Situation 0849, constructed as the functor of
> quadruples of Stacks 084A (`AlgebraicGeometry.Space.RelativeProjSituation.relativeProjFunctor`),
> `f : X ⟶ Y` a scheme point of the algebraic space `Y`, `ℒ` an invertible `𝒪_X`-module,
> `ψ : f^*𝒜 ⟶ ⨁_{d ≥ 0} ℒ^{⊗ d}` a homomorphism of graded algebras and
> `r_{ℒ,ψ} : U(ψ) ⟶ F` the morphism of Stacks 0D2Z.  Consider a commutative square
> `g ∘ f' = f ∘ g'` with `f' : X' ⟶ Y'`, `g' : X' ⟶ X` and `g : Y' ⟶ Y`, `X'` and `Y'` schemes; put
> `𝒜' = g^*𝒜`, `ℒ' = (g')^*ℒ` and let `ψ' : (f')^*𝒜' ⟶ ⨁_d (ℒ')^{⊗ d}` be the pullback of `ψ`
> (`AlgebraicGeometry.Space.GradedAlgebraRestriction.squareTwisting`).  Then
>
> * `U(ψ') = (g')^{-1}(U(ψ))`, `U(ψ')` being the open of Tag 01O9 for `ψ'` over `Y'`; and
> * `r_{ψ',ℒ'} : U(ψ') ⟶ Proj_{Y'}(𝒜')` of Tag 01O9 agrees with the base change of `r_{ψ,ℒ}`
>   through the identification `Proj_{Y'}(𝒜') = Y' ×_Y F` of Stacks 084B: for every test scheme
>   `t : T ⟶ X'` of `U(ψ')`, the `T`-point of `Y' ×_Y F` with components `f' ∘ t` and
>   `r_{ψ,ℒ} ∘ g' ∘ t` is, in `Proj_{Y'}(𝒜')`, the composite `T ⟶ U(ψ') ⟶ Proj_{Y'}(𝒜')`.

```lean
theorem invertibleMorphism_baseChange_square :
    (toGradedPowerMap (s.quadrupleRestriction.squareTwisting
        s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
          ψ g f' g' hsq)).coveringOpen =
      (BigFppfOver.toScheme s.site s.base s.containsBase).map g' ⁻¹ᵁ
        (toGradedPowerMap ψ).coveringOpen ∧
    ∀ {T : BigFppfOver s.site s.base s.containsBase} (t : T ⟶ X')
      (ht : t ≫ g' ∈ (subspaceOfOpens s.site s.base s.containsBase X
        (toGradedPowerMap ψ).coveringOpen).obj (op T)),
      (s.relativeProjPoints.pointEquivProjOver Y' g (t ≫ f')
          ⟨s.relativeProjPoints.locusFactor ψ (t ≫ g') ht ≫
            s.relativeProjPoints.invertibleMorphism ψ,
            s.quadrupleRestriction.locusFactor_invertibleMorphism_comp_π
              s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf ψ g f' g'
                hsq t
              ht⟩).1 =
        liftOfPreimageEqTop _ ((BigFppfOver.toScheme s.site s.base s.containsBase).map t)
            (s.quadrupleRestriction.preimage_coveringOpen_squareTwisting_eq_top
              s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf ψ g f' g'
                hsq t
              ht) ≫
          (toGradedPowerMap (s.quadrupleRestriction.squareTwisting
            s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf ψ g f' g'
              hsq)).globalMorphism (relativeProj (s.relativeProjPoints.algebra Y' g))
```

**`AlgebraicGeometry.Space.RelativeProjSituation.invertibleTheta_baseChange_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSquare.lean, line 783](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSquare.lean#L783). The attribute's comment: “clause (3), theta: at a scheme point f : X -> Y of the base (X a scheme), for an ARBITRARY commutative square g o f' = f o g' with X', Y' schemes, on the relative Proj constructed as the functor of quadruples of Tag 084A, the map theta' : r'^*((+)_d O(d)) -> (+)_d (L')^d|_{U(psi')} of Tag 01O9 for the pullback psi' of psi is the pullback j^*theta of theta along the restriction j : U(psi') -> U(psi) of g', through the canonical isomorphisms of graded algebras j^*r^*((+)_d O(d)) = r'^*((+)_d O(d)) and j^*((+)_d L^d|_{U(psi)}) = (+)_d (L')^d|_{U(psi')}”.

> **The last assertion of clause (3) of Stacks 0D2Z, `θ'` is the pullback of `θ`, for an
> arbitrary commutative square, on the constructed relative Proj.**
>
> In the situation of `invertibleMorphism_baseChange_square` (a commutative square
> `g ∘ f' = f ∘ g'` with `X'`, `Y'` schemes, `𝒜' = g^*𝒜`, `ℒ' = (g')^*ℒ` and `ψ'` the pullback of
> `ψ`), let `θ : r_{ℒ,ψ}^*(⨁_d 𝒪(d)) ⟶ ⨁_d ℒ^{⊗ d}|_{U(ψ)}` and
> `θ' : r_{ℒ',ψ'}^*(⨁_d 𝒪(d)) ⟶ ⨁_d (ℒ')^{⊗ d}|_{U(ψ')}` be the homomorphisms of graded algebras of
> Tag 01O9, for `ψ` at the point `f` and for `ψ'` over `Y'`.  Then `θ'` is the inverse image `j^*θ`
> of `θ` along the restriction `j : U(ψ') = (g')^{-1}(U(ψ)) ⟶ U(ψ)` of `g'`, read through the
> canonical identifications of sheaves of graded algebras
> `j^*r_{ℒ,ψ}^*(⨁_d 𝒪(d)) ≅ r_{ℒ',ψ'}^*(⨁_d 𝒪(d))`
> (`AlgebraicGeometry.Space.GradedAlgebraRestriction.squareThetaSourceIso`: pseudofunctoriality of
> the inverse image and the comparison of the twists of Tag 01NR along the morphisms of relative
> Proj's over the point `g ∘ f' = f ∘ g'` of `X'`, Stacks 084B (3)) and
> `j^*(⨁_d ℒ^{⊗ d}|_{U(ψ)}) ≅ ⨁_d (ℒ')^{⊗ d}|_{U(ψ')}`
> (`AlgebraicGeometry.Space.GradedAlgebraRestriction.squareThetaTargetIso`).

```lean
theorem invertibleTheta_baseChange_square :
    (toGradedPowerMap (s.quadrupleRestriction.squareTwisting
        s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
          ψ g f' g' hsq)).theta =
      (s.quadrupleRestriction.squareThetaSourceIso s.shrink.contains_relativeProj_pointAlgebra
          s.shrink.space.property.isSheaf ψ g f' g' hsq).inv ≫
        pullbackGradedAlgebraMap
          (Scheme.Hom.resLE ((BigFppfOver.toScheme s.site s.base s.containsBase).map g')
            (toGradedPowerMap ψ).coveringOpen
            (toGradedPowerMap (s.quadrupleRestriction.squareTwisting
              s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
              ψ g f' g' hsq)).coveringOpen
            (s.quadrupleRestriction.coveringOpen_squareTwisting
              s.shrink.contains_relativeProj_pointAlgebra s.shrink.space.property.isSheaf
              ψ g f' g' hsq).le).toLRSHom.toShHom
          (toGradedPowerMap ψ).theta ≫
        (s.quadrupleRestriction.squareThetaTargetIso s.shrink.contains_relativeProj_pointAlgebra
          s.shrink.space.property.isSheaf ψ g f' g' hsq).hom
```

**`AlgebraicGeometry.Space.RelativeProjPoints.invertibleTheta_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSquare.lean, line 827](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleSquare.lean#L827). The attribute's comment: “theta is characterized by clause (1), at the scheme point f : X -> Y: a homomorphism of graded algebras theta' : r^*((+)_d O(d)) -> (+)_d L^d|_{U(psi)} which for every open V of X, d >= 0 and a in (f^*A)_d(V) carries the pullback of psi_P(a) to the restriction of psi(a) is theta”.

> **`θ` is characterized by clause (1) of [Stacks, Tag 0D2Z], after base change to the scheme
> point `f : X ⟶ Y`.**  With the twists of `Proj_Y(𝒜)` at `f` those of `Proj_X(f^*𝒜)`, as in
> `invertibleTheta_clauseOne`: a homomorphism of graded algebras
> `θ' : r^*(⨁_d 𝒪(d)) ⟶ ⨁_d ℒ^{⊗ d}|_{U(ψ)}` which, for every open `V` of `X`, `d ≥ 0` and
> `a ∈ (f^*𝒜)_d(V)`, carries the inverse image of `ψ_P(a)` to the restriction of `ψ(a)` to
> `U(ψ) ∩ V` is `θ`.

```lean
theorem invertibleTheta_unique
    (θ' : SheafOfModules.GradedAlgebra.Hom
      (Stacks.Conormal.gradedPullback
        ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)))
        (twistDataOfGradedAlgebra (d.algebra X f)).algebra)
      (Stacks.AlgebraicGeometry.ProjChartGradedTriple.laurentOn L
        (toGradedPowerMap ψ).coveringOpen))
    (h : ∀ (V : ((BigFppfOver.toScheme B S hS).obj X).Opens) (n : ℕ)
        (a : Γ((d.algebra X f).piece (n : ℤ), V)),
        ((Stacks.AmpleProjectiveImmersion.tensorPowerModule _ L (n : ℤ)).restrict
            (toGradedPowerMap ψ).coveringOpen.ι).presheaf.map
            (eqToHom ((toGradedPowerMap ψ).toBase_preimage_eq V)).op
            ((θ'.app n).val.app
              (op ((toGradedPowerMap ψ).globalMorphism (relativeProj (d.algebra X f)) ⁻¹ᵁ
                ((relativeProj (d.algebra X f)).toBase ⁻¹ᵁ V)))
              (Stacks.RingedSpace.pullbackUnit
                ((toGradedPowerMap ψ).globalMorphism
                  (relativeProj (d.algebra X f))).toLRSHom.toShHom
                ((twistDataOfGradedAlgebra (d.algebra X f)).algebra.piece (n : ℤ))
                (op ((relativeProj (d.algebra X f)).toBase ⁻¹ᵁ V))
                (((twistDataOfGradedAlgebra (d.algebra X f)).ψ n).app V a)))
          = (Stacks.AmpleProjectiveImmersion.tensorPowerModule _ L (n : ℤ)).presheaf.map
              (homOfLE ((toGradedPowerMap ψ).coveringOpen.ι.image_preimage_le
                (𝟙 ((BigFppfOver.toScheme B S hS).obj X) ⁻¹ᵁ V))).op
              ((Stacks.AlgebraicGeometry.CoherentMulSections.powCompare L n).hom.app
                (𝟙 ((BigFppfOver.toScheme B S hS).obj X) ⁻¹ᵁ V)
                ((toGradedPowerMap ψ).value n V a))) :
    θ' = (toGradedPowerMap ψ).theta
```

**`AlgebraicGeometry.Space.RelativeProjPoints.invertibleTheta_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleThetaBaseChange.lean, line 561](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeProjInvertibleThetaBaseChange.lean#L561). The attribute's comment: “variant: clause (3), last sentence, for the squares in which Y' -> Y is the scheme point f : X -> Y; the tag is AlgebraicGeometry.Space.RelativeProjSituation.tag0D2Z”.

> **The last sentence of clause (3) of [Stacks, Tag 0D2Z]: `θ'` is the pullback of `θ`**, for
> the squares in which `Y' ⟶ Y` is the scheme point `f : X ⟶ Y`.  Consider the square with
> `Y' = X`, `g = f`, a scheme `g' : X' ⟶ X` and `f' = g'`, so that `𝒜' = f^*𝒜` (the algebra
> `d.algebra X f` of the presentation of `Proj_Y(𝒜)` at `f`), `ℒ' = g'^*ℒ` and `ψ' = g'^*ψ`; at the
> point `f` the twists `𝒪(d)` of `Proj_Y(𝒜)` are those of `Proj_X(f^*𝒜)`, as in
> `invertibleTheta_clauseOne`.  Then the map
> `θ' : r_{ℒ',ψ'}^*(⨁_d 𝒪(d)) ⟶ ⨁_d (ℒ')^{⊗ d}|_{U(ψ')}` is the inverse image of
> `θ : r_{ℒ,ψ}^*(⨁_d 𝒪(d)) ⟶ ⨁_d ℒ^{⊗ d}|_{U(ψ)}` along the restriction
> `j : U(ψ') = g'^{-1}(U(ψ)) ⟶ U(ψ)` of `g'`, read through the canonical identifications
> `j^*r_{ℒ,ψ}^*(⨁ 𝒪(d)) ≅ r_{ℒ',ψ'}^*(⨁ 𝒪(d))` (pseudofunctoriality of the inverse image, along
> `j ≫ r_{ℒ,ψ} = r_{ℒ',ψ'}`, which is `invertibleMorphism_baseChange`) and
> `j^*(⨁ ℒ^{⊗ d}|_{U(ψ)}) ≅ ⨁ (g'^*ℒ)^{⊗ d}|_{U(ψ')}` of sheaves of graded algebras.

```lean
theorem invertibleTheta_baseChange {X' : BigFppfOver B S hS} (g' : X' ⟶ X) :
    (toGradedPowerMap (ψ.pullback ((BigFppfOver.toScheme B S hS).map g'))).theta =
      (thetaSourceIso ψ ((BigFppfOver.toScheme B S hS).map g')).inv ≫
        pullbackGradedAlgebraMap
          (coveringOpenPullback ψ ((BigFppfOver.toScheme B S hS).map g')).toLRSHom.toShHom
          (toGradedPowerMap ψ).theta ≫
        (thetaTargetIso ψ ((BigFppfOver.toScheme B S hS).map g')).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.13, Tag 0D2Y](https://stacks.math.columbia.edu/tag/0D2Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
