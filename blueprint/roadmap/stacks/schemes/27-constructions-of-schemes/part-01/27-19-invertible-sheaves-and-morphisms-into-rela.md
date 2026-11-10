---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.GradedPowerMap.value_mul, Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.GradedPowerMap.coveringOpen, Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.tag01O9
statement: formalized
proof: formalized
---

# 27.19 Invertible sheaves and morphisms into relative Proj

Section 27.19 of the Stacks Project, [Tag 01O8](https://stacks.math.columbia.edu/tag/01O8). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01O8, the section

[Tag 01O8](https://stacks.math.columbia.edu/tag/01O8) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.GradedPowerMap.value_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Locus.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Locus.lean#L120). The attribute's comment: “item (6): the components of psi are multiplicative across degrees, the value at a product of homogeneous sections over an open of the base being the product of the values in the tensor powers of L over the preimage of that open”.

> `ψ` is multiplicative across degrees on values: `ψ(a · b) = ψ(a) · ψ(b)` in
> `Γ(f^{-1}(V), ℒ^{⊗ (n + m)})`.

```lean
public theorem value_mul (n m : ℕ) (V : S.Opens) (a : Γ(A.piece (n : ℤ), V))
    (b : Γ(A.piece (m : ℤ), V)) :
    P.value (n + m) V ((A.mul (n : ℤ) (m : ℤ)).app V a b)
      = Stacks.AlgebraicGeometry.NatTensorPowLocalMul.localMulSections P.L
          (P.value n V a) (P.value m V b)
```

**`Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.GradedPowerMap.coveringOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Locus.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Locus.lean#L175). The attribute's comment: “the open U(psi) = union over triples (U, V, a) -- V affine open of the base, U = f^\{-1}(V), a a homogeneous section of positive degree of A over V -- of the open U\_\{psi(a)} on which the section psi(a) of L^\{tensor deg(a)} over U does not vanish”.

> The open `U(ψ) = ⋃_{(U, V, a)} U_{ψ(a)}`: the union of the opens on which the values of `ψ`
> at the homogeneous sections of positive degree over the affine opens of the base do not
> vanish.

```lean
public def coveringOpen : T.Opens
```

## Tag 01O9, a lemma

[Tag 01O9](https://stacks.math.columbia.edu/tag/01O9) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjInvertibleMorphism.tag01O9`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Statement.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjInvertibleMorphism/Statement.lean#L87). The attribute's comment: “the open U(psi), the morphism r\_\{L,psi} : U(psi) -> Proj\_S(A) over S and the unital map of graded algebras theta : r^*(sum\_d O(d)) -> sum\_d L^d|\_\{U(psi)}; properties (1), (2) and (3) for them; and every triple (U', r', theta') with properties (1), (2) and (3) is (U(psi), r\_\{L,psi}, theta)”.

> **[Stacks, Tag 01O9].** For `ψ : f^*𝒜 ⟶ ⨁_{d} ℒ^{⊗ d}` with `ℒ` invertible, put
> `P = toGradedPowerMap ψ`, `U(ψ) = P.coveringOpen`, `r = P.globalMorphism (relativeProj A)` and
> `θ = P.theta`. Then:
>
> 1. `r` is a morphism over `S`: `r ≫ π = (U(ψ) ⊆ X) ≫ f`;
> 2. `θ` preserves the unit, and its components in degrees `d, e ≥ 0` are multiplicative, so that
>    they form a map of graded algebras `r^*(⨁_{d ≥ 0} 𝒪(d)) ⟶ ⨁_{d ≥ 0} ℒ^{⊗ d}|_{U(ψ)}`;
> 3. **property (1)**: for every open `V ⊆ S`, `d ≥ 0` and `a ∈ 𝒜_d(V)`, `θ` carries the pullback
>    along `r` of the section `ψ(a)` of `𝒪(d)` over `π^{-1}(V)` to `ψ(a)` restricted to
>    `f^{-1}(V) ∩ U(ψ) = r^{-1}(π^{-1}(V))`;
> 4. **property (2)**: for every `d ≥ 1` and every open `W ⊆ X` on which
>    `ψ_d : f^*𝒜_d|_W ⟶ ℒ^{⊗ d}|_W` is surjective, `W ⊆ U(ψ)` and `r|_W` is the morphism
>    `W ⟶ Proj_S(𝒜)` which the representation of the functor of quadruples by `Proj_S(𝒜)` attaches
>    to `(d, f|_W, ℒ^{⊗ d}|_W, ψ|_W)`;
> 5. **property (3)**, for the open and the morphism: for every affine open `V ⊆ S`, with
>    `ψ' : 𝒜(V) ⟶ Γ_*(f^{-1}(V), ℒ)` the induced map, `U(ψ') = U(ψ) ∩ f^{-1}(V)` and `r`
>    restricted along `U(ψ') ⟶ U(ψ)` is `i_V ∘ r_{ℒ, ψ'}`; and any morphism `U(ψ) ⟶ Proj_S(𝒜)` with
>    that restriction property over every affine `V` is `r`;
> 6. the triple `(U(ψ), r, θ)` (with `θ` in degrees `d ≥ 0`) is `Triple.canonical P`, and it has
>    properties (1), (2) and (3), property (3) including that `θ` restricted along
>    `U(ψ') ⟶ U(ψ)` is the `θ'` of the induced map, read through `i_V`;
> 7. **the characterization**: every triple `(U', r', θ')` with properties (1), (2) and (3) is
>    `(U(ψ), r, θ)`.

```lean
theorem tag01O9 :
    (toGradedPowerMap ψ).globalMorphism (relativeProj A) ≫ (relativeProj A).toBase
        = (toGradedPowerMap ψ).coveringOpen.ι ≫ f
      ∧ SheafOfModules.sectionsMap (((toGradedPowerMap ψ).theta).app 0)
          (Stacks.Conormal.gradedPullback ((toGradedPowerMap ψ).globalMorphism (relativeProj A))
            (GluedTwistAlgebra.twistDataOfGradedAlgebra A).algebra).one
        = (Stacks.AlgebraicGeometry.ProjChartGradedTriple.laurentOn L
            (toGradedPowerMap ψ).coveringOpen).one
      ∧ (∀ (d e : ℕ) (U : (toGradedPowerMap ψ).coveringOpen.toScheme.Opens)
          (x : ((Stacks.Conormal.gradedPullback
            ((toGradedPowerMap ψ).globalMorphism (relativeProj A))
            (GluedTwistAlgebra.twistDataOfGradedAlgebra A).algebra).piece (d : ℤ)).val.obj (op U))
          (y : ((Stacks.Conormal.gradedPullback
            ((toGradedPowerMap ψ).globalMorphism (relativeProj A))
            (GluedTwistAlgebra.twistDataOfGradedAlgebra A).algebra).piece (e : ℤ)).val.obj (op U)),
          (((toGradedPowerMap ψ).theta.app ((d : ℤ) + (e : ℤ))).val.app (op U)
              (((Stacks.Conormal.gradedPullback
                ((toGradedPowerMap ψ).globalMorphism (relativeProj A))
                (GluedTwistAlgebra.twistDataOfGradedAlgebra A).algebra).mul d e).app (op U) x y))
            = ((Stacks.AlgebraicGeometry.ProjChartGradedTriple.laurentOn L
                (toGradedPowerMap ψ).coveringOpen).mul d e).app (op U)
                (((toGradedPowerMap ψ).theta.app d).val.app (op U) x)
                (((toGradedPowerMap ψ).theta.app e).val.app (op U) y))
      ∧ (∀ (V : S.Opens) (d : ℕ) (a : Γ(A.piece (d : ℤ), V)),
          ((tensorPowerModule X L (d : ℤ)).restrict
            (toGradedPowerMap ψ).coveringOpen.ι).presheaf.map
              (eqToHom ((toGradedPowerMap ψ).toBase_preimage_eq V)).op
              (((toGradedPowerMap ψ).theta.app d).val.app
                (op ((toGradedPowerMap ψ).globalMorphism (relativeProj A) ⁻¹ᵁ
                  ((relativeProj A).toBase ⁻¹ᵁ V)))
                (Stacks.RingedSpace.pullbackUnit
                  ((toGradedPowerMap ψ).globalMorphism (relativeProj A)).toLRSHom.toShHom
                  ((GluedTwistAlgebra.twistDataOfGradedAlgebra A).algebra.piece (d : ℤ))
                  (op ((relativeProj A).toBase ⁻¹ᵁ V))
                  (((GluedTwistAlgebra.twistDataOfGradedAlgebra A).ψ d).app V a)))
            = (tensorPowerModule X L (d : ℤ)).presheaf.map
                (homOfLE ((toGradedPowerMap ψ).coveringOpen.ι.image_preimage_le (f ⁻¹ᵁ V))).op
                ((Stacks.AlgebraicGeometry.CoherentMulSections.powCompare L d).hom.app (f ⁻¹ᵁ V)
                  (valueSec ψ d V a)))
      ∧ (∀ {k : ℕ} (hk : 0 < k) (W : X.Opens) [Epi ((ψ.pullback W.ι).app (k : ℤ))],
          ∃ h : W ≤ (toGradedPowerMap ψ).coveringOpen,
            X.homOfLE h ≫ (toGradedPowerMap ψ).globalMorphism (relativeProj A)
              = F.classifyingMorphism A (F.mk (W.ι ≫ f) (by exact_mod_cast hk)
                  (restrictQuadruple ψ W k)))
      ∧ (∀ V : S.affineOpens,
          (f ⁻¹ᵁ V.1).ι ''ᵁ ((toGradedPowerMap ψ).affineDatum V.1).coveringOpen
              = (toGradedPowerMap ψ).coveringOpen ⊓ f ⁻¹ᵁ V.1
            ∧ ∀ j : (((toGradedPowerMap ψ).affineDatum V.1).coveringOpen).toScheme ⟶
                (toGradedPowerMap ψ).coveringOpen.toScheme,
              j ≫ (toGradedPowerMap ψ).coveringOpen.ι
                  = (((toGradedPowerMap ψ).affineDatum V.1).coveringOpen).ι ≫ (f ⁻¹ᵁ V.1).ι →
                j ≫ (toGradedPowerMap ψ).globalMorphism (relativeProj A)
                  = ((toGradedPowerMap ψ).affineDatum V.1).glued ≫ (relativeProj A).chart V.1 V.2)
      ∧ (∀ R : (toGradedPowerMap ψ).coveringOpen.toScheme ⟶ (relativeProj A).scheme,
          (∀ V : S.affineOpens,
            ∀ j : (((toGradedPowerMap ψ).affineDatum V.1).coveringOpen).toScheme ⟶
                (toGradedPowerMap ψ).coveringOpen.toScheme,
              j ≫ (toGradedPowerMap ψ).coveringOpen.ι
                  = (((toGradedPowerMap ψ).affineDatum V.1).coveringOpen).ι ≫ (f ⁻¹ᵁ V.1).ι →
                j ≫ R = ((toGradedPowerMap ψ).affineDatum V.1).glued
                  ≫ (relativeProj A).chart V.1 V.2) →
          R = (toGradedPowerMap ψ).globalMorphism (relativeProj A))
      ∧ Triple.canonical (toGradedPowerMap ψ)
          = ⟨(toGradedPowerMap ψ).coveringOpen,
              (toGradedPowerMap ψ).globalMorphism (relativeProj A),
              GradedNonnegHom.ofHom (toGradedPowerMap ψ).theta⟩
      ∧ Triple.IsTriple ψ (Triple.canonical (toGradedPowerMap ψ))
      ∧ (∀ t : Triple A L, Triple.IsTriple ψ t → t = Triple.canonical (toGradedPowerMap ψ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.19, Tag 01O8](https://stacks.math.columbia.edu/tag/01O8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
