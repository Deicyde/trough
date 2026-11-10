---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.epi_divisorSequenceSecondMapOfCurve, Stacks.EtaleCohomology.exact_divisorSequenceOfCurve, Stacks.EtaleCohomology.shortExact_divisorSequenceOfCurve, Stacks.EtaleCohomology.closedPointDivisorSections, Stacks.EtaleCohomology.closedPointDivisorSections_restrict_eq_zero, Stacks.EtaleCohomology.integerSkyscraperDivisorOfPoint_map, Stacks.EtaleCohomology.closedPointDivisorPresheafSection_map, Stacks.EtaleCohomology.closedPointDivisorPresheafSection_restrict_eq_zero
statement: formalized
proof: formalized
---

# 59.68 Higher vanishing for the multiplicative group

Section 59.68 of the Stacks Project, [Tag 03RH](https://stacks.math.columbia.edu/tag/03RH). 5 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03RI, a theorem

[Tag 03RI](https://stacks.math.columbia.edu/tag/03RI) in the Stacks Project.

**`Stacks.EtaleCohomology.epi_divisorSequenceSecondMapOfCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorEpi.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorEpi.lean#L472). The attribute's comment: “the right-hand exactness of the sequence for a smooth curve over a field: the second map, as constructed here, is an epimorphism of étale sheaves; the exactness in the middle is proved separately, as Stacks.EtaleCohomology.exact_divisorSequenceOfCurve”.

> **The second map of the fundamental exact sequence of Stacks 03RI is an epimorphism**, for a
> smooth curve over a field:
> `j_* 𝐆_{m,η} ⟶ ⨁_{x ∈ X_0} (i_x)_* 𝐙 ⟶ 0`
> is exact. This is the right-hand exactness of the source, with the algebraically closed base
> field of the source weakened to an arbitrary field.
>
> It is
> `Stacks.EtaleCohomology.epi_divisorSequenceSecondMapOfCurve_of_forall_imageSieve_ι_mem` with its
> hypothesis discharged by `Stacks.EtaleCohomology.imageSieve_ι_mem_of_isCurve`.
>
> Together with the left end,
> `Stacks.EtaleCohomology.mono_multiplicativeDirectImageComparison_genericPointInclusion`, and the
> vanishing of the composite,
> `Stacks.EtaleCohomology.multiplicativeDirectImageComparison_comp_divisorSequenceSecondMapOfCurve`,
> what remains of Stacks 03RI is the exactness in the middle,
> `Stacks.EtaleCohomology.exact_divisorSequenceOfCurve`; the four together are the short exactness
> of the sequence, `Stacks.EtaleCohomology.shortExact_divisorSequenceOfCurve`, which is what
> discharges the short exactness hypothesis of
> `Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_smoothCurve`.

```lean
theorem epi_divisorSequenceSecondMapOfCurve {k : Type u} [Field k] {X : Scheme.{u}}
    (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g] :
    Epi (divisorSequenceSecondMapOfCurve.{u, v} g)
```

**`Stacks.EtaleCohomology.exact_divisorSequenceOfCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorMiddleExactness.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorMiddleExactness.lean#L280). The attribute's comment: “the exactness in the middle of the sequence for a smooth curve over a field: a section of j_* G_m killed by the divisor map is étale locally an invertible global function”.

> For a smooth curve `X` over a field, the fundamental exact sequence
> `0 → 𝐆_{m,X} → j_* 𝐆_{m,η} → ⨁_{x ∈ X_0} (i_x)_* 𝐙 → 0` is exact in the middle: the kernel of
> the divisor map `j_* 𝐆_{m,η} ⟶ ⨁_{x ∈ X_0} (i_x)_* 𝐙` is the image of `𝐆_{m,X}`.

```lean
theorem exact_divisorSequenceOfCurve {k : Type u} [Field k] {X : Scheme.{u}}
    (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g] :
    (ShortComplex.mk
      (multiplicativeDirectImageComparison.{u, u + 1} (genericPointInclusion X))
      (divisorSequenceSecondMapOfCurve.{u, u + 1} g)
      (multiplicativeDirectImageComparison_comp_divisorSequenceSecondMapOfCurve.{u, u + 1}
        g)).Exact
```

**`Stacks.EtaleCohomology.shortExact_divisorSequenceOfCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorMiddleExactness.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorMiddleExactness.lean#L299). The attribute's comment: “the fundamental exact sequence for a smooth curve over a field, as a short exact sequence of étale sheaves”.

> Let `X` be a smooth curve over a field `k`, let `η` be its generic point with inclusion
> `j : η ⟶ X`, and let `X_0` be its set of closed points with inclusions `i_x`. Then
>
> `0 → 𝐆_{m,X} → j_* 𝐆_{m,η} → ⨁_{x ∈ X_0} (i_x)_* 𝐙 → 0`
>
> is a short exact sequence of étale sheaves on `X`.

```lean
theorem shortExact_divisorSequenceOfCurve {k : Type u} [Field k] {X : Scheme.{u}}
    (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g] :
    (ShortComplex.mk
      (multiplicativeDirectImageComparison.{u, u + 1} (genericPointInclusion X))
      (divisorSequenceSecondMapOfCurve.{u, u + 1} g)
      (multiplicativeDirectImageComparison_comp_divisorSequenceSecondMapOfCurve.{u, u + 1}
        g)).ShortExact
```

**`Stacks.EtaleCohomology.closedPointDivisorSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSections.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSections.lean#L273). The attribute's comment: “the second map on sections over an arbitrary étale X-scheme, for X integral and normal”.

> **The second map of the fundamental exact sequence
> `0 → 𝐆_{m,X} → j_* 𝐆_{m,η} → ⨁_{x ∈ X_0} (i_x)_* 𝐙 → 0`, on sections over an arbitrary étale
> `X`-scheme `U`**: an invertible global function on the generic fibre `η ×_X U` is sent to the
> finitely supported family of its orders of vanishing in `⨁_{x ∈ X_0} ((i_x)_* 𝐙)(U)`, the member
> at a closed point `x` being the locally constant `𝐙`-valued map on the fibre `x ×_X U` recording
> the order of vanishing at each point of `U` over `x`.

```lean
def closedPointDivisorSections :
    Additive ((Γ(pullback U.hom (genericPointInclusion X), ⊤))ˣ) →+
      DirectSum ↥(closedPoints X)
        fun x : closedPoints X => (integerSkyscraper.{u, v} X x.1).obj.obj (op U)
```

**`Stacks.EtaleCohomology.closedPointDivisorSections_restrict_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSections.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSections.lean#L300). The attribute's comment: “the sequence on sections over an arbitrary étale X-scheme is a complex, for X integral and normal”.

> **The fundamental exact sequence is a complex on sections over an arbitrary étale
> `X`-scheme `U`**: the restriction to the generic fibre of an invertible global function on `U` has
> zero family of orders of vanishing.

```lean
theorem closedPointDivisorSections_restrict_eq_zero (a : (Γ(U.left, ⊤))ˣ) :
    closedPointDivisorSections.{u, v} U (Additive.ofMul (Units.map
      (pullback.fst U.hom (genericPointInclusion X)).appTop.hom.toMonoidHom a)) = 0
```

**`Stacks.EtaleCohomology.integerSkyscraperDivisorOfPoint_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafMap.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafMap.lean#L117). The attribute's comment: “the x-component of the second map is compatible with restriction along a morphism of étale X-schemes, read in the sections of i_{x,*} Z, for X integral and normal”.

> **The `x`-component of the second map of the fundamental exact sequence is compatible with
> restriction along a morphism of the small étale site**, read in the sections of `(i_x)_* 𝐙` over an
> étale `X`-scheme. Neither object is assumed irreducible.

```lean
theorem integerSkyscraperDivisorOfPoint_map {X : Scheme.{u}} [AlgebraicGeometry.IsIntegral X]
    [IsNormal X] {U V : X.Etale} [IsLocallyNoetherian U.left] [IsLocallyNoetherian V.left]
    (x : X) (φ : U ⟶ V) (a : (Γ(pullback V.hom (genericPointInclusion X), ⊤))ˣ) :
    ((integerSkyscraper.{u, v} X x).obj.map φ.op).hom
        (integerSkyscraperDivisorOfPoint.{u, v} V x (Additive.ofMul a)) =
      integerSkyscraperDivisorOfPoint.{u, v} U x
        (Additive.ofMul (Units.map (etaleGenericFibreMap φ).appTop.hom.toMonoidHom a))
```

**`Stacks.EtaleCohomology.closedPointDivisorPresheafSection_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafMap.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafMap.lean#L195). The attribute's comment: “the second map of the sequence is compatible with restriction along a morphism of étale X-schemes, read in the coproduct of the underlying presheaves of the skyscrapers, for X integral and normal”.

> **The second map on sections is compatible with restriction**, read in the coproduct of the
> underlying presheaves of the skyscrapers: restricting the section attached to a unit on the generic
> fibre of `V` along a morphism `φ : U ⟶ V` of the small étale site gives the section attached to the
> restricted unit. Neither object is assumed irreducible.

```lean
theorem closedPointDivisorPresheafSection_map {U V : X.Etale} [IsLocallyNoetherian U.left]
    [NoetherianSpace U.left] [IsLocallyNoetherian V.left] [NoetherianSpace V.left]
    (φ : U ⟶ V) (a : (Γ(pullback V.hom (genericPointInclusion X), ⊤))ˣ) :
    ((∐ fun x : closedPoints X ↦ (closedPointSkyscraper.{u, v} X x).obj).map φ.op).hom
        (closedPointDivisorPresheafSection.{u, v} V (Additive.ofMul a)) =
      closedPointDivisorPresheafSection.{u, v} U (Additive.ofMul (Units.map
        ((smallEtaleBaseChange (genericPointInclusion X)).map
          φ).left.appTop.hom.toMonoidHom a))
```

**`Stacks.EtaleCohomology.closedPointDivisorPresheafSection_restrict_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafMap.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafMap.lean#L213). The attribute's comment: “the sequence is a complex on sections over an arbitrary étale X-scheme, read in the coproduct of the underlying presheaves of the skyscrapers, for X integral and normal”.

> **An invertible global function on `U` has trivial image under the second map**, read in the
> presheaf coproduct: the sequence is a complex on sections over an étale `X`-scheme with Noetherian
> space, with no irreducibility hypothesis.

```lean
theorem closedPointDivisorPresheafSection_restrict_eq_zero (U : X.Etale)
    [IsLocallyNoetherian U.left] [NoetherianSpace U.left] (a : (Γ(U.left, ⊤))ˣ) :
    closedPointDivisorPresheafSection.{u, v} U (Additive.ofMul (Units.map
      (pullback.fst U.hom (genericPointInclusion X)).appTop.hom.toMonoidHom a)) = 0
```

**`Stacks.EtaleCohomology.closedPointDivisorSheafSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L250). The attribute's comment: “the second map on sections over an étale X-scheme with Noetherian space, valued in the sheaf ⨁_x i_{x,*} Z, for X integral and normal; no irreducibility is assumed”.

> **The second map of the fundamental exact sequence of Stacks 03RI over an arbitrary étale
> `X`-scheme with Noetherian space, valued in the sheaf `⨁_x (i_x)_* 𝐙` itself.** This is
> `Stacks.EtaleCohomology.closedPointDivisorSections` followed by
> `Stacks.EtaleCohomology.closedPointDivisorSheaf.sheafSectionOfDirectSum`.
>
> No irreducibility hypothesis is carried on `U`, which is the generality of the source.

```lean
def closedPointDivisorSheafSection (U : X.Etale) [IsLocallyNoetherian U.left]
    [NoetherianSpace U.left] :
    Additive ((Γ(pullback U.hom (genericPointInclusion X), ⊤))ˣ) →+
      (closedPointDivisorSheaf.{u, v} X).obj.obj (op U)
```

**`Stacks.EtaleCohomology.closedPointDivisorSheafSection_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L283). The attribute's comment: “the second map of the sequence is compatible with restriction along a morphism of étale X-schemes with Noetherian spaces, read in the sheaf ⨁_x i_{x,*} Z, for X integral and normal; no irreducibility is assumed”.

> **The commuting square that makes the second map of Stacks 03RI a map of presheaves**, read in
> the sheaf `⨁_x (i_x)_* 𝐙`: restricting the section attached to a unit on the generic fibre of `V`
> along a morphism `φ : U ⟶ V` of the small étale site gives the section attached to the restricted
> unit.
>
> It is `Stacks.EtaleCohomology.closedPointDivisorSections_map` together with the naturality of the
> passage from the direct sum of the groups of sections to the sections of the sheaf,
> `Stacks.EtaleCohomology.closedPointDivisorSheaf.map_comp_sheafSectionOfDirectSum`. Neither object
> is assumed irreducible, so this is the square at the generality of the source.

```lean
theorem closedPointDivisorSheafSection_map {U V : X.Etale} [IsLocallyNoetherian U.left]
    [NoetherianSpace U.left] [IsLocallyNoetherian V.left] [NoetherianSpace V.left]
    (φ : U ⟶ V) (a : (Γ(pullback V.hom (genericPointInclusion X), ⊤))ˣ) :
    ((closedPointDivisorSheaf.{u, v} X).obj.map φ.op).hom
        (closedPointDivisorSheafSection.{u, v} V (Additive.ofMul a)) =
      closedPointDivisorSheafSection.{u, v} U (Additive.ofMul (Units.map
        ((smallEtaleBaseChange (genericPointInclusion X)).map
          φ).left.appTop.hom.toMonoidHom a))
```

**`Stacks.EtaleCohomology.closedPointDivisorSheafSection_restrict_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L301). The attribute's comment: “the sequence is a complex on sections over an étale X-scheme with Noetherian space, read in the sheaf ⨁_x i_{x,*} Z, for X integral and normal; no irreducibility is assumed”.

> **An invertible global function on `U` has trivial image under the second map of Stacks 03RI
> read in the sheaf `⨁_x (i_x)_* 𝐙`**: the sequence of the source is a complex over an arbitrary
> étale `X`-scheme with Noetherian space, with no irreducibility hypothesis.

```lean
theorem closedPointDivisorSheafSection_restrict_eq_zero (U : X.Etale)
    [IsLocallyNoetherian U.left] [NoetherianSpace U.left] (a : (Γ(U.left, ⊤))ˣ) :
    closedPointDivisorSheafSection.{u, v} U (Additive.ofMul (Units.map
      (pullback.fst U.hom (genericPointInclusion X)).appTop.hom.toMonoidHom a)) = 0
```

**`Stacks.EtaleCohomology.affineEtaleDivisorRestricted`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L493). The attribute's comment: “the second map of the sequence on the affine étale site, as a morphism of presheaves, for X integral, normal and locally Noetherian”.

> **The second map of the fundamental exact sequence of Stacks 03RI on the affine étale site**,
> as a morphism of presheaves of abelian groups. Its component at an affine étale `X`-scheme `W` is
> `Stacks.EtaleCohomology.affineEtaleDivisorApp`, and its commuting square is
> `Stacks.EtaleCohomology.affineEtaleDivisorApp_naturality`.

```lean
def affineEtaleDivisorRestricted :
    (Scheme.AffineEtale.Spec X).op ⋙ ((genericPointDirectImage.{u, v} X).obj
        (Stacks.Kummer.multiplicativeSheaf.{u, v} (Spec X.functionField))).obj ⟶
      (Scheme.AffineEtale.Spec X).op ⋙ (closedPointDivisorSheaf.{u, v} X).obj
```

**`Stacks.EtaleCohomology.divisorSequenceSecondMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L523). The attribute's comment: “the second map of the sequence, as a morphism of étale sheaves, for X integral, normal and locally Noetherian; the exactness of the sequence is not proved at this generality”.

> **The second map of the fundamental exact sequence of Stacks 03RI, as a morphism of abelian
> sheaves on the small étale site of `X`:**
> `j_* 𝐆_{m,η} ⟶ ⨁_{x ∈ X_0} (i_x)_* 𝐙`.
>
> It is `Stacks.EtaleCohomology.affineEtaleDivisorRestricted` transferred along the inclusion of the
> affine étale site, which is cover dense and full and hence locally full, so
> `CategoryTheory.Functor.IsCoverDense.restrictHomEquivHom` is a bijection. The source states the
> sequence for a smooth curve over an algebraically closed field; the hypotheses carried here —
> integral, normal, locally Noetherian — are all weaker, and are discharged in that setting by
> `Stacks.EtaleCohomology.isLocallyNoetherian_of_isCurve` and
> `Stacks.EtaleCohomology.isNormal_of_isCurve_of_smooth`.
>
> Being data, this definition is not pinned down by its type: the zero morphism inhabits it too.
> What pins it down is `Stacks.EtaleCohomology.whiskerLeft_divisorSequenceSecondMap` together with
> `Stacks.EtaleCohomology.divisorSequenceSecondMap_hom_app` and
> `Stacks.EtaleCohomology.affineEtaleDivisorApp_apply`, which say that on sections over an affine
> étale `X`-scheme it is the family of orders of vanishing, and
> `Stacks.EtaleCohomology.divisorSequenceSecondMap_eq_of_whiskerLeft`, which says that no other
> morphism of sheaves does so.

```lean
def divisorSequenceSecondMap :
    (genericPointDirectImage.{u, v} X).obj
        (Stacks.Kummer.multiplicativeSheaf.{u, v} (Spec X.functionField)) ⟶
      closedPointDivisorSheaf.{u, v} X
```

**`Stacks.EtaleCohomology.multiplicativeDirectImageComparison_comp_divisorSequenceSecondMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L595). The attribute's comment: “the sequence is a complex: the two constructed maps compose to zero, for X integral, normal and locally Noetherian; the exactness of the sequence is not proved at this generality”.

> **The two maps of the fundamental exact sequence of Stacks 03RI compose to zero**, so that
> `0 → 𝐆_{m,X} → j_* 𝐆_{m,η} → ⨁_{x ∈ X_0} (i_x)_* 𝐙 → 0`
> is a complex of abelian sheaves on the small étale site of `X`.
>
> Both composites are morphisms into the sheaf `⨁_x (i_x)_* 𝐙`, so restriction to the affine étale
> site is injective on them and it suffices to compare them there, where
> `Stacks.EtaleCohomology.comparison_app_comp_affineEtaleDivisorApp` applies.

```lean
theorem multiplicativeDirectImageComparison_comp_divisorSequenceSecondMap :
    multiplicativeDirectImageComparison.{u, v} (genericPointInclusion X) ≫
        divisorSequenceSecondMap.{u, v} X = 0
```

**`Stacks.EtaleCohomology.divisorSequenceSecondMapOfCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L686). The attribute's comment: “the second map of the sequence for a smooth curve over a field, as a morphism of étale sheaves; the short exactness of the sequence is proved in the MiddleExactness file of this directory”.

> **The second map of the fundamental exact sequence of Stacks 03RI for a smooth curve over a
> field**, which is the setting of the source. The three hypotheses of
> `Stacks.EtaleCohomology.divisorSequenceSecondMap` are discharged there: a curve is integral by
> `AlgebraicGeometry.IsVariety` and locally Noetherian by
> `Stacks.EtaleCohomology.isLocallyNoetherian_of_isCurve`, and a smooth curve is normal by
> `Stacks.EtaleCohomology.isNormal_of_isCurve_of_smooth`.

```lean
def divisorSequenceSecondMapOfCurve {k : Type u} [Field k] {X : Scheme.{u}}
    (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g] :
    (genericPointDirectImage.{u, v} X).obj
        (Stacks.Kummer.multiplicativeSheaf.{u, v} (Spec X.functionField)) ⟶
      closedPointDivisorSheaf.{u, v} X
```

**`Stacks.EtaleCohomology.multiplicativeDirectImageComparison_comp_divisorSequenceSecondMapOfCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/ClosedPointDivisorSheafSecondMap.lean#L703). The attribute's comment: “the sequence is a complex for a smooth curve over a field: the two constructed maps compose to zero; the short exactness of the sequence is proved in the MiddleExactness file of this directory”.

> **The two maps of the fundamental exact sequence of Stacks 03RI compose to zero for a smooth
> curve over a field.** This is
> `Stacks.EtaleCohomology.multiplicativeDirectImageComparison_comp_divisorSequenceSecondMap` with
> the hypotheses of that statement discharged as in
> `Stacks.EtaleCohomology.divisorSequenceSecondMapOfCurve`.

```lean
theorem multiplicativeDirectImageComparison_comp_divisorSequenceSecondMapOfCurve {k : Type u}
    [Field k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g] :
    multiplicativeDirectImageComparison.{u, v} (genericPointInclusion X) ≫
        divisorSequenceSecondMapOfCurve.{u, v} g = 0
```

**`Stacks.EtaleCohomology.fundamentalSequence_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequence.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequence.lean#L297).

> **Stacks Project, Tag 03RI.** Let `X` be a smooth curve over a field, let `η = Spec k(X)` be
> its generic point with inclusion `j : η ⟶ X`, and let `X_0` be the set of closed points of `X`
> with inclusions `i_x : Spec κ(x) ⟶ X`. Then
>
> `0 ⟶ 𝐆_{m,X} ⟶ j_* 𝐆_{m,η} ⟶ ⨁_{x ∈ X_0} (i_x)_* 𝐙 ⟶ 0`
>
> is a short exact sequence of abelian sheaves on the small étale site of `X`. The first map is the
> comparison morphism `Stacks.EtaleCohomology.multiplicativeDirectImageComparison` along `j`, which
> restricts an invertible global function on an étale `X`-scheme `U` to the generic fibre
> `U ×_X η`; the second is `Stacks.EtaleCohomology.closedPointDivisorMap`, the family of orders of
> vanishing.
>
> Exactness at `𝐆_{m,X}` is
> `Stacks.EtaleCohomology.mono_multiplicativeDirectImageComparison_genericPointInclusion`: the
> generic fibre is scheme-theoretically dense. Exactness in the middle is
> `Stacks.EtaleCohomology.exact_fundamentalSequence`, which rests on algebraic Hartogs on the
> normal scheme `U`. Exactness on the right is
> `Stacks.EtaleCohomology.epi_closedPointDivisorMap`: a divisor on a nonsingular curve is locally
> the divisor of a rational function, and the pullback of that function along an étale morphism has
> the prescribed orders of vanishing.

```lean
theorem fundamentalSequence_shortExact :
    (ShortComplex.mk (multiplicativeDirectImageComparison.{u, v} (genericPointInclusion X))
      (closedPointDivisorMap.{u, v} fX)
      (comparison_comp_closedPointDivisorMap.{u, v} fX)).ShortExact
```

**`Stacks.EtaleCohomology.injective_restrict_genericFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequenceSections.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequenceSections.lean#L323). The attribute's comment: “exactness at Γ(U, 𝒪_U^*) of the sequence on sections over an étale X-scheme”.

> **Exactness of the fundamental exact sequence of Stacks 03RI at `Γ(U, 𝒪_U^*)`, read on
> sections over an étale `X`-scheme `U`.** On an integral scheme the generic fibre `η ×_X U` is
> scheme-theoretically dense in `U`, so an invertible global function on `U` is determined by its
> restriction to it.
>
> This is the injectivity of the first map of the sequence
> `0 → Γ(U, 𝒪_U^*) → Γ(η ×_X U, 𝒪^*) → ⨁_{x ∈ X_0} Γ(x ×_X U, 𝐙)`
> displayed in the proof of the source.

```lean
theorem injective_restrict_genericFibre :
    Function.Injective (Units.map
      (pullback.fst U.hom (genericPointInclusion X)).appTop.hom.toMonoidHom)
```

**`Stacks.EtaleCohomology.genericFibreDivisorSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequenceSections.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequenceSections.lean#L346). The attribute's comment: “the second map on sections over an irreducible étale X-scheme”.

> **The second map of the fundamental exact sequence of Stacks 03RI, on sections over an
> irreducible étale `X`-scheme `U`**: an invertible global function on the generic fibre `η ×_X U`
> is sent to the family of its orders of vanishing, the member at a closed point `x` being the
> locally constant `𝐙`-valued map on the fibre `x ×_X U` recording the order of vanishing at each
> point of `U` over `x`.
>
> The family has finite support, a rational function having finitely many zeros and poles, so it is
> an element of the direct sum `⨁_{x ∈ X_0} ((i_x)_* 𝐙)(U)`, the third term of the sequence
> displayed in the proof of the source.

```lean
def genericFibreDivisorSections :
    Additive ((Γ(pullback U.hom (genericPointInclusion X), ⊤))ˣ) →+
      DirectSum ↥(closedPoints X)
        fun x : closedPoints X => (integerSkyscraper.{u, v} X x.1).obj.obj (op U)
```

**`Stacks.EtaleCohomology.genericFibreDivisorSections_restrict_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequenceSections.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/FundamentalExactSequenceSections.lean#L376). The attribute's comment: “the sequence on sections over an irreducible étale X-scheme is a complex”.

> **The sequence of Stacks 03RI is a complex, read on sections over an irreducible étale
> `X`-scheme `U`**: an invertible global function on `U` restricts to an invertible function on the
> generic fibre with no zeros and no poles, so its family of orders of vanishing is zero.
>
> Together with `Stacks.EtaleCohomology.injective_restrict_genericFibre` this is the sequence
> `0 → Γ(U, 𝒪_U^*) → Γ(η ×_X U, 𝒪^*) → ⨁_{x ∈ X_0} Γ(x ×_X U, 𝐙)`
> displayed in the proof of the source, exact at its left end and a complex at the middle.

```lean
theorem genericFibreDivisorSections_restrict_eq_zero (a : (Γ(U.left, ⊤))ˣ) :
    genericFibreDivisorSections.{u, v} U (Additive.ofMul (Units.map
      (pullback.fst U.hom (genericPointInclusion X)).appTop.hom.toMonoidHom a)) = 0
```

**`Stacks.EtaleCohomology.etaleGenericFibreOrd_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/GenericFibreFunctionFieldNaturality.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/GenericFibreFunctionFieldNaturality.lean#L272). The attribute's comment: “the second map of the sequence is compatible with restriction along a morphism of étale X-schemes, read on the order of vanishing at a point”.

> **The order of vanishing of an invertible global function on the generic fibre is compatible
> with restriction along a morphism `φ : U ⟶ V` of the small étale site of `X`:** restricting along
> `Stacks.EtaleCohomology.etaleGenericFibreMap φ` and taking the order of vanishing at a point `y`
> of `U` gives the order of vanishing at `φ.left.base y`.

```lean
theorem etaleGenericFibreOrd_appTop {X : Scheme.{u}} [IrreducibleSpace X] {U V : X.Etale}
    [IsIntegral U.left] [IsIntegral V.left] [IsLocallyNoetherian U.left]
    [IsLocallyNoetherian V.left] (φ : U ⟶ V) (y : U.left)
    (a : (Γ(pullback V.hom (genericPointInclusion X), ⊤))ˣ) :
    etaleGenericFibreOrd U y
        (Additive.ofMul (Units.map (etaleGenericFibreMap φ).appTop.hom.toMonoidHom a)) =
      etaleGenericFibreOrd V (φ.left.base y) (Additive.ofMul a)
```

## Tag 03RJ, a lemma

[Tag 03RJ](https://stacks.math.columbia.edu/tag/03RJ) in the Stacks Project.

**`Stacks.EtaleCohomology.isZero_rightDerived_genericPointDirectImage_multiplicativeSheaf_of_trdeg_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/GenericPointHigherDirectImageMultiplicative.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/GenericPointHigherDirectImageMultiplicative.lean#L66). References: SGA 4½ Arcata (3.3.2), “more general”.

> **Stacks Project, Tag 03RJ.** Let `k` be an algebraically closed field, let `X` be an
> integral scheme whose function field `K = k(X)` has transcendence degree one over `k`, and let
> `j : Spec K ⟶ X` be the inclusion of the generic point. Then
>
> `R^q j_* 𝐆_{m,K} = 0` for every `q ≥ 1`.
>
> A smooth curve over `k` satisfies the hypotheses, by
> `AlgebraicGeometry.trdeg_functionField_eq_one`, so this is more general than the tag.

```lean
theorem isZero_rightDerived_genericPointDirectImage_multiplicativeSheaf_of_trdeg_eq_one
    (k : Type u) [Field k] [IsAlgClosed k] {X : Scheme.{u}} [IsIntegral X]
    [Algebra k X.functionField] (hK : Algebra.trdeg k X.functionField = 1)
    (q : ℕ) (hq : 1 ≤ q) :
    IsZero (((etaleAbelianDirectImage.{u, u + 1} (genericPointInclusion X)).rightDerived q).obj
      (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField)))
```

**`Stacks.EtaleCohomology.isZero_rightDerived_genericPointDirectImage_multiplicativeSheaf_smoothCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/GenericPointHigherDirectImageSmoothCurveVanishing.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/GenericPointHigherDirectImageSmoothCurveVanishing.lean#L82).

> **Stacks Project, Tag 03RJ.** Let `k` be an algebraically closed field, `X` a smooth curve
> over `k` with structure morphism `g`, `η = Spec k(X)` its generic point and `j : η ⟶ X` the
> inclusion of the generic point. Then
>
> `R^q j_* 𝐆_{m,η} = 0` for every `q ≥ 1`.
>
> No hypothesis is carried. The higher direct image is killed on the étale neighbourhoods by
> `Stacks.EtaleCohomology.isZero_rightDerived_etaleAbelianDirectImage_multiplicativeSheaf_of_field`,
> which leaves the vanishing of `H^q_étale(Spec L, 𝐆_m)` at each finite separable extension `L` of
> `k(X)`. That is Stacks 03RG, since `L` has transcendence degree one over `k`.
>
> Smoothness is in the statement because the source assumes it. The proof does not use it: the
> curve hypothesis is enough.

```lean
theorem isZero_rightDerived_genericPointDirectImage_multiplicativeSheaf_smoothCurve
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k))
    [IsCurve k g] [Smooth g] (q : ℕ) (hq : 1 ≤ q) :
    IsZero (((etaleAbelianDirectImage.{u, u + 1} (genericPointInclusion X)).rightDerived q).obj
      (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField)))
```

## Tag 03RK, a lemma

[Tag 03RK](https://stacks.math.columbia.edu/tag/03RK) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupHigherVanishing.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupHigherVanishing.lean#L245). The attribute's comment: “vanishing of the positive-degree étale cohomology of the direct image of 𝐆_m along the generic point of a curve over an algebraically closed field”.

> **Stacks Project, Tag 03RK.** Let `X` be a curve over an algebraically closed field `k`,
> with structure morphism `g`, let `η = Spec k(X)` be its generic point and `j : η ⟶ X` the
> inclusion of the generic point. Then
>
> `H^p_étale(X, j_* 𝐆_{m,η}) = 0` for every `p ≥ 1`.
>
> The source assumes `X` smooth; the proof does not use smoothness, so it is not assumed and the
> statement is more general than the tag. The smooth case, with the source's hypotheses verbatim,
> is `Stacks.EtaleCohomology.subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf_smoothCurve`.
>
> The source argues by the Leray spectral sequence `E₂^{p,q} = H^p(X, R^q j_* 𝐆_{m,η})`, whose
> `q ≥ 1` rows vanish by Stacks 03RJ and whose abutment `H^{p+q}(η, 𝐆_m)` vanishes for
> `p + q ≥ 1` by Stacks 03RG. The proof here is the edge isomorphism of that spectral sequence,
> `Stacks.EtaleCohomology.subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf_of_isZero_rightDerived`,
> with both inputs proved: Stacks 03RJ is
> `Stacks.EtaleCohomology.isZero_rightDerived_genericPointDirectImage_multiplicativeSheaf_of_trdeg_eq_one`,
> whose premise is `AlgebraicGeometry.trdeg_functionField_eq_one`, and Stacks 03RG at the function
> field of `X` is `Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_spec_functionField`.

```lean
theorem subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf {k : Type u} [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsCurve k g]
    (p : ℕ) (hp : 1 ≤ p) :
    Subsingleton (Sheaf.H.{u + 1, u + 1} ((genericPointDirectImage.{u, u + 1} X).obj
      (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField))) p)
```

**`Stacks.EtaleCohomology.subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf_smoothCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupSmoothCurveVanishing.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupSmoothCurveVanishing.lean#L77).

> **Stacks Project, Tag 03RK.** Let `X` be a smooth curve over an algebraically closed field
> `k`, let `η = Spec k(X)` be its generic point and `j : η ⟶ X` the inclusion. Then
>
> `H^p_étale(X, j_* 𝐆_{m,η}) = 0` for every `p ≥ 1`.
>
> This is `Stacks.EtaleCohomology.subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf`,
> the collapse of the Leray spectral sequence to its edge isomorphism, with Stacks 03RJ and
> Stacks 03RG proved.

```lean
theorem subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf_smoothCurve
    {k : Type u} [Field k] [IsAlgClosed k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k))
    [IsCurve k g] [Smooth g] (p : ℕ) (hp : 1 ≤ p) :
    Subsingleton (Sheaf.H.{u + 1, u + 1} ((genericPointDirectImage.{u, u + 1} X).obj
      (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField))) p)
```

## Tag 03RL, a lemma

[Tag 03RL](https://stacks.math.columbia.edu/tag/03RL) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_sheafH_sigma_closedPointPushforward_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointDirectSumCohomology.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedPointDirectSumCohomology.lean#L178). The attribute's comment: “vanishing of the positive-degree étale cohomology of the direct sum over the closed points of the pushforwards of the constant integer sheaf”.

> **Stacks Project, Tag 03RL.** Let `X` be a quasi-compact, quasi-separated scheme locally of
> finite type over an algebraically closed field — a smooth curve over an algebraically closed
> field, for instance. For every `q ≥ 1` the degree-`q` étale cohomology of
> `⨁_{x ∈ X₀} (i_x)_* ℤ` vanishes, the sum being over the closed points `X₀` of `X` and `i_x` the
> inclusion of a closed point.

```lean
public theorem subsingleton_sheafH_sigma_closedPointPushforward_smallEtale {k : Type u} [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [LocallyOfFiniteType g]
    [CompactSpace X] [QuasiSeparatedSpace X] (q : ℕ) (hq : 1 ≤ q) :
    Subsingleton (Sheaf.H.{u + 1, u + 1}
      (∐ fun x : closedPoints X ↦
        (smallEtalePushforwardAb (X.fromSpecResidueField x.1)).obj
          ((constantSheaf (smallEtaleTopology (Spec (X.residueField x.1))) Ab.{u + 1}).obj
            (AddCommGrpCat.of (ULift.{u + 1} ℤ)))) q)
```

## Tag 03RM, a theorem

[Tag 03RM](https://stacks.math.columbia.edu/tag/03RM) in the Stacks Project.

**`Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_smoothCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupHigherVanishing.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupHigherVanishing.lean#L281). The attribute's comment: “vanishing of the degree ≥ 2 étale cohomology of 𝐆_m on a smooth curve over an algebraically closed field, over Tag 03RI, Tag 03RJ and Tag 03RG as hypotheses”.

> **Stacks Project, Tag 03RM.** Let `X` be a smooth curve over an algebraically closed field
> `k`, let `η = Spec k(X)` be its generic point and `j : η ⟶ X` the inclusion of the generic
> point. Then
>
> `H^q_étale(X, 𝐆_m) = 0` for every `q ≥ 2`.
>
> The proof is the long exact sequence of étale cohomology attached to the divisor sequence
> `0 → 𝐆_{m,X} → j_* 𝐆_{m,η} → ⨁_{x ∈ X_0} i_{x,*} 𝐙 → 0` of Stacks 03RI: the segment
> `H^{q-1}(X, ⨁_x i_{x,*} 𝐙) → H^q(X, 𝐆_{m,X}) → H^q(X, j_* 𝐆_{m,η})` has both outer groups
> zero, the left one by Stacks 03RL since `q - 1 ≥ 1`, the right one by Stacks 03RK.
>
> Stacks 03RL is used from the library, as
> `Stacks.EtaleCohomology.subsingleton_sheafH_sigma_closedPointPushforward_smallEtale`, and
> the vanishing of `H^q(X, j_* 𝐆_{m,η})` is the edge argument
> `Stacks.EtaleCohomology.subsingleton_sheafH_genericPointDirectImage_multiplicativeSheaf_of_isZero_rightDerived`
> (which is how Stacks 03RK is proved above), applied to the hypotheses `h03RJ` (Stacks 03RJ) and
> `h03RG` (Stacks 03RG) carried here. The
> divisor sequence itself is carried as its second map `d` with `hzero` and `hSE` (Stacks 03RI);
> its first map is the comparison morphism
> `Stacks.EtaleCohomology.multiplicativeDirectImageComparison` along `j`, which restricts an
> invertible global function on an étale `X`-scheme `U` to the generic fibre `U ×_X η`.

```lean
theorem subsingleton_sheafH_multiplicativeSheaf_smoothCurve {k : Type u} [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g]
    (d : (genericPointDirectImage.{u, u + 1} X).obj
          (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField)) ⟶
        closedPointDivisorSheaf.{u, u + 1} X)
    (hzero : multiplicativeDirectImageComparison.{u, u + 1} (genericPointInclusion X) ≫ d = 0)
    (hSE : (ShortComplex.mk
      (multiplicativeDirectImageComparison.{u, u + 1} (genericPointInclusion X)) d
      hzero).ShortExact)
    (h03RJ : ∀ q : ℕ, 0 < q →
      IsZero (((etaleAbelianDirectImage.{u, u + 1} (genericPointInclusion X)).rightDerived q).obj
        (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField))))
    (h03RG : ∀ q : ℕ, 1 ≤ q → Subsingleton (Sheaf.H.{u + 1, u + 1}
      (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} (Spec X.functionField)) q))
    (q : ℕ) (hq : 2 ≤ q) :
    Subsingleton
      (Sheaf.H.{u + 1, u + 1} (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} X) q)
```

**`Stacks.EtaleCohomology.subsingleton_sheafH_multiplicativeSheaf_of_smoothCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupSmoothCurveVanishing.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Curves/MultiplicativeGroupSmoothCurveVanishing.lean#L94).

> **Stacks Project, Tag 03RM.** Let `X` be a smooth curve over an algebraically closed field
> `k`. Then
>
> `H^q_étale(X, 𝐆_m) = 0` for every `q ≥ 2`.
>
> The long exact sequence of the fundamental exact sequence of Stacks 03RI,
> `Stacks.EtaleCohomology.shortExact_divisorSequenceOfCurve`, places `H^q(X, 𝐆_m)` between
> `H^{q-1}(X, ⨁_{x ∈ X_0} i_{x,*} 𝐙)`, zero by Stacks 03RL, and `H^q(X, j_* 𝐆_{m,η})`, zero by
> Stacks 03RK; the latter rests on Stacks 03RJ and Stacks 03RG, supplied here.

```lean
theorem subsingleton_sheafH_multiplicativeSheaf_of_smoothCurve {k : Type u} [Field k]
    [IsAlgClosed k] {X : Scheme.{u}} (g : X ⟶ Spec (.of k)) [IsCurve k g] [Smooth g]
    (q : ℕ) (hq : 2 ≤ q) :
    Subsingleton
      (Sheaf.H.{u + 1, u + 1} (Stacks.Kummer.multiplicativeSheaf.{u, u + 1} X) q)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.68, Tag 03RH](https://stacks.math.columbia.edu/tag/03RH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
