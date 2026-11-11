---
declaration: section
origin: cited
lean: Deformation.Examples.isCofiberedInGroupoids_chart, Deformation.Examples.FlatSchemeFamily, Deformation.Examples.FlatSchemeFamily.Hom, Deformation.Examples.FlatSchemeFamily.instCategory, Deformation.Examples.flatSchemeFamilyProjection, Deformation.Examples.flatSchemeFamilyProjection_cofiberedInGroupoids, Deformation.Examples.SchemeDeformationCategory, Deformation.Examples.SchemeDeformationCategory.Hom
statement: formalized
proof: formalized
---

# 93.9 Schemes

Section 93.9 of the Stacks Project, [Tag 0DY6](https://stacks.math.columbia.edu/tag/0DY6). 10 tags here are carried by 40 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DY7, an example

[Tag 0DY7](https://stacks.math.columbia.edu/tag/0DY7) in the Stacks Project.

**`Deformation.Examples.isCofiberedInGroupoids_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeChartEquivalence.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeChartEquivalence.lean#L242). The attribute's comment: “the deformation category of an affine open presented as a spectrum is cofibered in groupoids, transported along Tag 0DYX from the ring side; the clause for a general scheme is not covered”.

> **The deformation category of an affine open presented as a spectrum is cofibered in
> groupoids.** This has no scheme-side proof in this repository: it is transported from the
> deformation category of the coordinate ring, which is a deformation category by Tag 0DY2.

```lean
theorem isCofiberedInGroupoids_chart :
    IsCofiberedInGroupoids
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U.ι ≫ X.hom)))
```

**`Deformation.Examples.FlatSchemeFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L78). The attribute's comment: “flat\_scheme\_families”.

> A scheme flat over the spectrum of an object of `𝒞_Λ`.

```lean
structure FlatSchemeFamily (Λ : Type u) (k : Type w) [CommRing Λ] [Field k] [Algebra Λ k]
```

**`Deformation.Examples.FlatSchemeFamily.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L92). The attribute's comment: “flat\_scheme\_families”.

> A cartesian base-change arrow between flat scheme families.

```lean
structure Hom (P Q : FlatSchemeFamily.{u, v, w} Λ k)
```

**`Deformation.Examples.FlatSchemeFamily.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L103). The attribute's comment: “flat\_scheme\_families”.

> Flat scheme families over objects of `𝒞_Λ` and their base-change arrows form
> a category.

```lean
instance instCategory : Category (FlatSchemeFamily.{u, v, w} Λ k)
```

**`Deformation.Examples.flatSchemeFamilyProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L127). The attribute's comment: “flat\_scheme\_families”.

> The canonical functor sending a flat scheme family to its object of `𝒞_Λ`.

```lean
def flatSchemeFamilyProjection :
    FlatSchemeFamily.{u, v, w} Λ k ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k
```

**`Deformation.Examples.flatSchemeFamilyProjection_cofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L136). The attribute's comment: “cofibred\_projection”.

> Base change makes the projection from flat scheme families cofibered in groupoids.

```lean
theorem flatSchemeFamilyProjection_cofiberedInGroupoids
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] :
    IsCofiberedInGroupoids (flatSchemeFamilyProjection.{u, v, w} (Λ := Λ) (k := k))
```

**`Deformation.Examples.SchemeDeformationCategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L209). The attribute's comment: “scheme\_deformation\_category”. References: SGA 7 VI (1.1(c)).

> A flat family over an object of `𝒞_Λ` together with an identification of its fibre over
> the closed point with a fixed scheme over `k`. The identification is recorded as a cartesian
> square.

```lean
structure SchemeDeformationCategory (X : Over (Spec (.of k)))
```

**`Deformation.Examples.SchemeDeformationCategory.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L228). The attribute's comment: “scheme\_deformation\_category”.

> A cartesian arrow of deformations: contravariant on the schemes, covariant on the objects
> of `𝒞_Λ`, and compatible with the two identifications of the fibre over the closed point.

```lean
structure Hom {X : Over (Spec (.of k))}
    (P Q : SchemeDeformationCategory (Λ := Λ) (k := k) X)
```

**`Deformation.Examples.SchemeDeformationCategory.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L241). The attribute's comment: “scheme\_deformation\_category”. References: SGA 7 VI (1.1(c)).

> Deformations of a fixed scheme over `k` form a category.

```lean
instance instCategory (X : Over (Spec (.of k))) :
    Category (SchemeDeformationCategory (Λ := Λ) (k := k) X)
```

**`Deformation.Examples.schemeDeformationCategoryProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L269). The attribute's comment: “scheme\_deformation\_category”.

> The canonical projection from the category of deformations of a scheme to `𝒞_Λ`.

```lean
def schemeDeformationCategoryProjection (X : Over (Spec (.of k))) :
    SchemeDeformationCategory (Λ := Λ) (k := k) X ⥤ ArtinianLocalAlgCat.{u, u, u} Λ k
```

**`Deformation.Examples.schemeDeformationCategoryProjection_cofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesCofibered.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesCofibered.lean#L143). The attribute's comment: “cofibred\_projection, for the deformation category of a scheme”. References: SGA 7 VI (1.1(c)), “more general”.

> **The deformation category of a scheme is cofibered in groupoids.** A deformation can be
> base changed along any morphism of `𝒞_Λ`
> (`Deformation.Examples.baseChangeDeformation`), and an arrow out of a deformation descends
> uniquely through that base change, because its component on total spaces is determined by the
> universal property of the fibre product.
>
> This is the lower half of the cofibered condition that
> `Deformation.full_of_exists_lift_of_isHomLift_id` asks of the source-forgetful functor of
> [Stacks, Tag 0E3X].

```lean
theorem schemeDeformationCategoryProjection_cofiberedInGroupoids
    (X : Over (Spec (.of k))) :
    IsCofiberedInGroupoids (schemeDeformationCategoryProjection (Λ := Λ) (k := k) X)
```

**`Deformation.Examples.isFirstOrderThickening_specialMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpecialFibreFirstOrder.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SpecialFibreFirstOrder.lean#L117). The attribute's comment: “the special-fibre immersion of a deformation over the dual numbers is a first-order thickening”.

> **The special-fibre immersion of a first-order deformation of a scheme is a first-order
> thickening.** It is a closed immersion by
> `Deformation.Examples.deformationSpecialMap_isClosedImmersion`, being a base change of the
> closed point, and its ideal sheaf is square-zero because the maximal ideal of the base object
> is, by `Deformation.Examples.maximalIdeal_sq_eq_bot_of_dualNumberEquiv`.
>
> This is the hypothesis `i.ker ^ 2 = ⊥` of [Stacks Project, Tag 0CK2], discharged for the
> deformations over the dual numbers to which [Stacks Project, Tag 0E3V] applies it.

```lean
theorem isFirstOrderThickening_specialMap {X : Over (Spec (CommRingCat.of k))}
    (P : SchemeDeformationCategory (Λ := Λ) (k := k) X)
    (coordinate : P.base ≃ₐ[Λ] DualNumber k) :
    Stacks.Thickenings.IsFirstOrderThickening P.specialMap
```

## Tag 0DY8, a lemma

[Tag 0DY8](https://stacks.math.columbia.edu/tag/0DY8) in the Stacks Project.

**`Deformation.Examples.isDeformationCategory_schemeDeformationCategoryProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesDeformationCategory.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesDeformationCategory.lean#L241). The attribute's comment: “the clause that the deformation category of a fixed scheme over k is a deformation category, unconditionally; condition (RS) for the category of all flat scheme families of Example 0DY7 is Deformation.Examples.satisfiesRS\_flatSchemeFamilyProjection”. References: SGA 7 VI (1.1(c)), “more general”.

> The deformation category of a fixed scheme `X` over the residue field is a deformation
> category: a predeformation category satisfying (RS).

```lean
theorem isDeformationCategory_schemeDeformationCategoryProjection
    (X : Over (Spec (.of k))) :
    IsDeformationCategory.{u, u, u}
      (schemeDeformationCategoryProjection.{u} (Λ := Λ) (k := k) X)
```

**`Deformation.Examples.satisfiesRS_flatSchemeFamilyProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesRimSchlessingerSquares.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesRimSchlessingerSquares.lean#L48). The attribute's comment: “condition (RS) for the category of flat scheme families of Example 0DY7, unconditionally. The two gluing clauses it rests on are the last assertion of Tag 07RV and the equivalence assertion of the closing paragraph of Tag 07RX, both proved in this repository: Stacks.Pushout.isPullback\_of\_isPushout\_glued and Stacks.Pushout.isPushout\_restrictions\_of\_flat. The pushout of spectra, the existence of the glued family, its flatness and both halves of the universal property are proved as well. The clause that the deformation category of a fixed scheme over k is a deformation category is Deformation.Examples.isDeformationCategory\_schemeDeformationCategoryProjection”.

> The category of flat families of schemes over `𝒞_Λ` satisfies the Rim-Schlessinger condition
> (RS).

```lean
theorem satisfiesRS_flatSchemeFamilyProjection :
    SatisfiesRS (flatSchemeFamilyProjection.{u, v, w} (Λ := Λ) (k := k))
```

## Tag 0DY9, a lemma

[Tag 0DY9](https://stacks.math.columbia.edu/tag/0DY9) in the Stacks Project.

**`Deformation.Examples.infinitesimalAutomorphismGroupTrivialDeformationChain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesInfinitesimalAutomorphismsTrivial.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesInfinitesimalAutomorphismsTrivial.lean#L168). The attribute's comment: “first display: for a scheme X over the field k, Inf(Def\_X) = Ext^0(NL\_\{X/k}, O\_X) = Hom(Omega\_\{X/k}, O\_X) = Der\_k(O\_X, O\_X), as three identifications: Inf(Def\_X) is the library's infinitesimal automorphism group of the deformation category of X at the trivial deformation X x\_k Spec k[eps], and is isomorphic as a group to Der\_k(O\_X, O\_X); Ext^0 out of the naive cotangent complex is additively Hom(Omega\_\{X/k}, O\_X); and Hom(Omega\_\{X/k}, O\_X) is k-linearly Der\_k(O\_X, O\_X). The second display, T Def\_X = Ext^1(NL\_\{X/k}, O\_X), is registered separately”. References: SGA 1 III (6.1), “special case”; SGA 3 VIIA (2.5), “first component”; SGA 3 VIIA (6.4.3), “special case”; SGA 7 VI (4.16), “special case”.

> **The first display of [Stacks Project, Tag 0DY9].** For a scheme `X` over the field `k`,
>
> `Inf(𝓓_X) = Ext⁰_{𝒪_X}(NL_{X/k}, 𝒪_X) = Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X) = Der_k(𝒪_X, 𝒪_X)`,
>
> given as the three identifications of those four groups.
>
> `Inf(𝓓_X)` is the library's infinitesimal automorphism group
> `Deformation.infinitesimalAutomorphismGroup` of the deformation category of `X`, which is a
> predeformation category by [Stacks Project, Tag 0DY8], formed at its canonical data: the point
> `X` over `k`, its pushforward the trivial deformation `X ×_{Spec k} Spec k[ε]`, and the pair
> `k → k[ε] → k`. That is, the automorphisms of the trivial deformation that are the identity
> modulo `ε`.
>
> * The first identification is an isomorphism of **groups**: composition of such automorphisms
>   corresponds to addition of derivations
>   (`Deformation.Examples.infinitesimalAutomorphismGroupMulEquivDerivations`, at the coordinate
>   `Deformation.Examples.artinianDualNumbersCoordinate` of the dual-number object).
> * The second is `AlgebraicGeometry.Scheme.naiveCotangentExtZeroAddEquiv`: `Ext⁰` out of the naive
>   cotangent complex `NL_{X/k}` of the structure morphism of `X` is the `Hom` out of its degree `0`
>   cohomology sheaf, which is `Ω_{X/k}` by [Stacks Project, Tag 0D0J].
> * The third is `k`-linear: `Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X)` carries the `k`-structure of sheaves of
>   modules on a scheme over `k` (`AlgebraicGeometry.modulesLinear`), and the derivations of `𝒪_X`
>   over `k` with values in `𝒪_X` the one of
>   `Deformation.Examples.schemeMorphismDerivationsModule`; it is corepresentability of relative
>   derivations (`Deformation.Examples.schemeMorphismDerivationsLinearEquiv`) read through the
>   comparison `AlgebraicGeometry.Scheme.Hom.cotangentSheafIso` of the two constructions of the
>   sheaf of relative differentials.
>
> `Der_k(𝒪_X, 𝒪_X)` is written `schemeMorphismDerivations (𝟙 X.left) X.hom`, the derivations of
> `𝒪_X` over `k` with values in the pushforward of `𝒪_X` along the identity of `X`, which is `𝒪_X`
> itself (`Deformation.Examples.schemeMorphismPushforwardStructureSheaf_id`, by `rfl`).

```lean
def infinitesimalAutomorphismGroupTrivialDeformationChain (X : Over (Spec (CommRingCat.of k))) :
    (infinitesimalAutomorphismGroup
        (isDeformationCategory_schemeDeformationCategoryProjection (Λ := Λ) X).predeformation
        (x₀ := residueTrivialFiberObj X) (xε := dualNumbersTrivialFiberObj X)
        dualNumbersInclusion.{u, u, u}
        (residueMorphism.{u, u, u} (artinianDualNumbers.{u, u, u} Λ k))
        isCanonicalDualNumberPair_dualNumbersInclusion.{u, u, u}
        (dualNumbersTrivialDeformationHom X) (dualNumbersTrivialDeformationHom_isHomLift X)
        ≃* Multiplicative (schemeMorphismDerivations (Λ := Λ) (k := k) (𝟙 X.left) X.hom))
      × (Scheme.naiveCotangentExt X.hom (structureSheafModules X.left) 0
          ≃+ (Scheme.Hom.relativeDifferentials X.hom ⟶ structureSheafModules X.left))
      × (letI : Module k (Scheme.Hom.relativeDifferentials X.hom ⟶ structureSheafModules X.left) :=
            (modulesLinear k (Over.mk X.hom)).homModule _ _;
          letI := schemeMorphismDerivationsModule (Λ := Λ) (k := k) (𝟙 X.left) X.hom
            (structureSheafModules X.left);
          ((Scheme.Hom.relativeDifferentials X.hom ⟶ structureSheafModules X.left) ≃ₗ[k]
            schemeMorphismDerivations (Λ := Λ) (k := k) (𝟙 X.left) X.hom))
```

**`Deformation.Examples.schemeTangentSpaceLinearEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTangentSpaceLinearEquivExt.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTangentSpaceLinearEquivExt.lean#L251). The attribute's comment: “second display: for a scheme X over the field k, T Def\_X = Ext^1(NL\_\{X/k}, O\_X) as k-vector spaces, from the tangent space of the deformation category of X (isomorphism classes of flat deformations of X over k[eps], with the canonical vector space structure of 06IH) onto Ext^1\_\{O\_X}(NL\_\{X/k}, O\_X); a deformation goes to its 08UC difference class with the trivial deformation X x\_k Spec k[eps], which goes to 0. The first display, Inf(Def\_X) = Ext^0(NL\_\{X/k}, O\_X) = Der\_k(O\_X, O\_X), is registered separately”.

> **Stacks Project, Tag 0DY9, second display.** For a scheme `X` over the field `k`,
>
> `T𝓓_X = Ext¹_{𝒪_X}(NL_{X/k}, 𝒪_X)`
>
> as `k`-vector spaces.
>
> `T𝓓_X` is the tangent space of the deformation category of `X` of [Stacks Project, Tag 0DY7]:
> the value at the dual numbers `k[ε]` of its functor of isomorphism classes
> ([Stacks Project, Tag 06SR]), the set of isomorphism classes of flat deformations of `X` over
> `k[ε]`, with the canonical `k`-vector space structure of [Stacks Project, Tag 06IH].
> `Ext¹_{𝒪_X}(NL_{X/k}, 𝒪_X)` is `AlgebraicGeometry.Scheme.naiveCotangentExt` of the structure
> morphism of `X` with coefficients `𝒪_X` in degree `1`, a `k`-vector space through the `k`-linear
> structure of `𝒪_X`-modules.
>
> The identification is the source's proof: a flat deformation of `X` over `k[V] = k ⊕ V` is a
> solution of the deformation problem of [Stacks Project, Tag 08U7] for `Spec k ⊂ Spec k[V]` with
> ideal `f^*𝒥 = 𝒪_X ⊗_k V`, and its class is the difference class of
> [Stacks Project, Tag 08UC] against the trivial deformation `X ×_k Spec k[V]`
> (`Deformation.Examples.tangentExtClassAt`). These classes are bijective
> (`Deformation.Examples.bijective_tangentExtClassAt`) and natural in `V`
> (`Deformation.Examples.tangentExtClassAt_naturality`), so they are `k`-linear for the structure of
> Tag 06IH at `V = k`, where `𝒪_X ⊗_k k = 𝒪_X`. The trivial deformation goes to `0`
> (`Deformation.Examples.schemeTangentSpaceLinearEquivExt_trivial`) and the class of a deformation
> is its difference class (`Deformation.Examples.schemeTangentSpaceLinearEquivExt_classOf`).

```lean
noncomputable def schemeTangentSpaceLinearEquivExt :
    letI : Fact (IsPredeformationCategory (schemeDeformationBased (Λ := Λ) X).p) :=
      ⟨(isDeformationCategory_schemeDeformationCategoryProjection (Λ := Λ) X).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
      (isomorphismClasses (schemeDeformationBased (Λ := Λ) X) (schemeDeformation_cofibered X)))) :=
      ⟨schlessingerConditionS2_schemeDeformation X⟩
    letI := schemeTangentExtModule X (structureSheafModules X.left)
    schemeTangentSpace (Λ := Λ) (k := k) X ≃ₗ[k]
      Scheme.naiveCotangentExt X.hom (structureSheafModules X.left) 1
```

## Tag 0DYA, a lemma

[Tag 0DYA](https://stacks.math.columbia.edu/tag/0DYA) in the Stacks Project.

**`Deformation.Examples.finiteDimensional_schemeTangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesFiniteDimensional.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesFiniteDimensional.lean#L116). The attribute's comment: “the tangent space clause: for X proper over k, T Def\_X (isomorphism classes of flat deformations of X over k[eps], with the canonical vector space structure of 06IH) is finite dimensional over k”.

> **Stacks 0DYA, the tangent space.** For a scheme `X` proper over the field `k`, the tangent
> space `T𝓓_X` of its deformation category ([Stacks Project, Tag 0DY7]) — the isomorphism classes
> of flat deformations of `X` over `k[ε]`, with the canonical vector-space structure of
> [Stacks Project, Tag 06IH] — is finite dimensional over `k`.
>
> By [Stacks Project, Tag 0DY9] it is `Ext¹_{𝒪_X}(NL_{X/k}, 𝒪_X)`
> (`Deformation.Examples.schemeTangentSpaceLinearEquivExtRankOne` and
> `Deformation.Examples.schemeTangentExtRankOneLinearEquiv`, the identification of
> `Deformation.Examples.schemeTangentSpaceLinearEquivExt` before the change of model of the
> derived category); `NL_{X/k}` is in `D^-_Coh(𝒪_X)` by [Stacks Project, Tag 0D0K]
> (`derivedCategoryBMinus_naiveCotangentComplex`) and `𝒪_X` in `D^+_Coh(𝒪_X)`, so the `Ext` group
> is finite dimensional by [Stacks Project, Tag 0D0D].

```lean
theorem finiteDimensional_schemeTangentSpace [IsProper X.hom] :
    letI : Fact (IsPredeformationCategory (schemeDeformationBased (Λ := Λ) X).p) :=
      ⟨(isDeformationCategory_schemeDeformationCategoryProjection (Λ := Λ) X).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
      (isomorphismClasses (schemeDeformationBased (Λ := Λ) X) (schemeDeformation_cofibered X)))) :=
      ⟨schlessingerConditionS2_schemeDeformation X⟩
    FiniteDimensional k (schemeTangentSpace (Λ := Λ) (k := k) X)
```

**`Deformation.Examples.finiteDimensional_localizedAutomorphismFunctorTangent_schemeDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesFiniteDimensional.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesFiniteDimensional.lean#L253). The attribute's comment: “the infinitesimal automorphism clause: for X proper over k, Inf(Def\_X) is finite dimensional over k, with the vector space structure of 06JV, at every point of the deformation category and every choice of pushforwards”.

> **Stacks 0DYA, the infinitesimal automorphisms.** For a scheme `X` proper over the field `k`,
> the `k`-vector space `Inf(𝓓_X)` of infinitesimal automorphisms of its deformation category
> ([Stacks Project, Tag 0DY7]) is finite dimensional. `Inf(𝓓_X)` is the tangent space at the
> identity of the automorphism functor of a point `x₀` of the deformation category, with the
> vector-space structure of [Stacks Project, Tag 06JV] (addition is composition, the scalar action
> is transport along `ε ↦ cε`); this holds at every point `x₀` and every choice `P` of
> pushforwards, in particular at the trivial deformation `X` over `k`.
>
> The proof is the source's: `Inf(𝓓_X)` embeds `k`-linearly in `Der_k(𝒪_X, 𝒪_X)`
> (`infinitesimalAutomorphismDerivationLinearMap`, injective by
> `injective_infinitesimalAutomorphismDerivationLinearMap`), the identification of
> [Stacks Project, Tag 0DY9], and `Der_k(𝒪_X, 𝒪_X) = Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X)` is finite
> dimensional by [Stacks Project, Tag 0D0D].

```lean
theorem finiteDimensional_localizedAutomorphismFunctorTangent_schemeDeformation [IsProper X.hom]
    {x₀ : SchemeDeformationCategory (Λ := Λ) (k := k) X}
    (P : ChosenPushforwardsAt (schemeDeformationCategoryProjection (Λ := Λ) (k := k) X) x₀) :
    letI := naturalLocalizedTangentAddCommGroup P
      (isDeformationCategory_schemeDeformationCategoryProjection (Λ := Λ) X).satisfiesRS
    letI := naturalLocalizedTangentModule P
      (isDeformationCategory_schemeDeformationCategoryProjection (Λ := Λ) X).satisfiesRS
    FiniteDimensional k (localizedAutomorphismFunctorTangent P)
```

## Tag 0ET5, a lemma

[Tag 0ET5](https://stacks.math.columbia.edu/tag/0ET5) in the Stacks Project.

**`Deformation.Examples.exists_hull_isomorphismClasses_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesHull.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesHull.lean#L95). The attribute's comment: “the hull: for X proper over k and Λ a complete local ring with residue field k, the functor A ↦ Ob(Def\_X(A))/≅ of isomorphism classes of deformations of X has a hull”.

> **Stacks Project, Tag 0ET5**, the hull. Let `X` be a proper scheme over the field `k` and
> let `Λ` be a Noetherian complete local ring with residue field `k` (the classical case). Then the
> functor `F : 𝒞_Λ → Sets, A ↦ Ob(Def_X(A))/≅` of isomorphism classes of deformations of `X` has
> a hull: a versal formal object of `F` whose differential is bijective.
>
> `Def_X` is a deformation category by Stacks 0DY8 and its tangent space is finite dimensional by
> Stacks 0DYA (`Deformation.Examples.finiteDimensional_schemeTangentSpace`), so Stacks 06J7 and
> 06IZ give the hull.

```lean
theorem exists_hull_isomorphismClasses_scheme (hΛ : IsClassical Λ k)
    (X : Over (Spec (CommRingCat.of k))) [IsProper X.hom] :
    let F := isomorphismClasses (schemeDeformationBased (Λ := Λ) X) (schemeDeformation_cofibered X)
    ∃ ξ : FormalObject (CategoryOfElements.π F),
      IsHull (categoryOfElements_projection_isCofibered F) ξ
```

**`Deformation.Examples.isProrepresentableULift_isomorphismClasses_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesHull.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesHull.lean#L118). The attribute's comment: “prorepresentability: for X proper over k and Λ a complete local ring with residue field k, if Der\_k(O\_X, O\_X) = 0 then the functor A ↦ Ob(Def\_X(A))/≅ is prorepresentable”. References: SGA 7 X (2.27), “more general”.

> **Stacks Project, Tag 0ET5**, prorepresentability. Let `X` be a proper scheme over the field
> `k` and let `Λ` be a Noetherian complete local ring with residue field `k`. If
> `Der_k(𝒪_X, 𝒪_X) = 0`, then the functor `F : 𝒞_Λ → Sets, A ↦ Ob(Def_X(A))/≅` is
> prorepresentable.
>
> By the first display of Stacks 0DY9, `Inf(Def_X) = Der_k(𝒪_X, 𝒪_X)` vanishes
> (`Deformation.Examples.infinitesimalAutomorphisms_schemeDeformation_eq_bot`), so `Def_X` and `F`
> are equivalent (Stacks 06K0) and `F` is a deformation functor with finite-dimensional tangent
> space (Stacks 0DYA); Schlessinger's theorem, Stacks 06JM, applies. Prorepresentability is stated
> in the universe-raised form `Deformation.IsProrepresentableULift`, the values of `F` lying one
> universe above the morphisms of `𝒞_Λ`.

```lean
theorem isProrepresentableULift_isomorphismClasses_scheme (hΛ : IsClassical Λ k)
    (X : Over (Spec (CommRingCat.of k))) [IsProper X.hom]
    (hDer : ∀ D : schemeMorphismDerivations (Λ := Λ) (k := k) (𝟙 X.left) X.hom, D = 0) :
    IsProrepresentableULift
      (isomorphismClasses (schemeDeformationBased (Λ := Λ) X) (schemeDeformation_cofibered X))
```

## Tag 0DYW, a lemma

[Tag 0DYW](https://stacks.math.columbia.edu/tag/0DYW) in the Stacks Project.

**`Deformation.Examples.openRestrictionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/OpenSubschemes.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/OpenSubschemes.lean#L263). References: SGA 7 VI (4.1(d)).

> **Stacks 0DYW.** Let `X` be a scheme over `k` and `U ⊆ X` an open subscheme. Restricting a
> deformation of `X` to the open corresponding to `U` is a functor from the deformation category
> of `X` to that of `U`, over the category `𝒞_Λ` of Artinian local `Λ`-algebras.

```lean
def openRestrictionFunctor (X : Over (Spec (.of k))) (U : X.left.Opens) :
    BasedFunctor
      (BasedCategory.ofFunctor (schemeDeformationCategoryProjection (Λ := Λ) (k := k) X))
      (BasedCategory.ofFunctor
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U.ι ≫ X.hom))))
```

## Tag 0DYX, a lemma

[Tag 0DYX](https://stacks.math.columbia.edu/tag/0DYX) in the Stacks Project.

**`Deformation.Examples.chartEquivalenceOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeChartEquivalence.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeChartEquivalence.lean#L212). The attribute's comment: “for an affine open presented as a spectrum by an isomorphism over Spec k, which is the form Situation 0DYY provides”.

> **Stacks 0DYX for an affine open presented as a spectrum.** The deformation category of an
> open `U` of `X` which is presented as `Spec P` over `Spec k` is equivalent, over `𝒞_Λ`, to the
> deformation category of the `k`-algebra `P`: transport the deformations along the presentation
> and then take global sections.

```lean
def chartEquivalenceOver :
    StacksRepresentableCFG.EquivalenceOver
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U.ι ≫ X.hom)))
      (Over.forget (residueFieldAlgebra (Λ := Λ) (k := k) P) ⋙
        FlatAlgebraCategory.projection (Λ := Λ) (k := k))
```

**`Deformation.Examples.SchemeRingDeformation.sectionsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeRingDeformation.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeRingDeformation.lean#L257). The attribute's comment: “the functor sending (A, Y) to the global sections of Y”.

> **Stacks 0DYX.** Global sections as a functor from deformations of `Spec P` to
> deformations of `P`.

```lean
def sectionsFunctor :
    SchemeDeformationCategory (Λ := Λ) (k := k) (specOver k P) ⥤
      ringDeformationCategory (Λ := Λ) (k := k) P
```

**`Deformation.Examples.SchemeRingDeformation.equivalenceOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeRingDeformation.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemeRingDeformation.lean#L483). The attribute's comment: “the equivalence Def\_(Spec P) = Def\_P; 06AD is isAffine\_of\_isThickening”. References: SGA 7 VI (4.1(b)).

> **Stacks 0DYX.** For a `k`-algebra `P`, global sections are an equivalence from the
> deformation category of the affine scheme `Spec P` to the deformation category of `P`, over the
> category of Artinian local `Λ`-algebras with residue field `k`.

```lean
def equivalenceOver :
    StacksRepresentableCFG.EquivalenceOver
      (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (specOver k P))
      (Over.forget (residueFieldAlgebra (Λ := Λ) (k := k) P) ⋙
        FlatAlgebraCategory.projection (Λ := Λ) (k := k))
```

## Tag 0DZM, a lemma

[Tag 0DZM](https://stacks.math.columbia.edu/tag/0DZM) in the Stacks Project.

**`Deformation.Examples.localRingDeformationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean#L286). The attribute's comment: “the functor”.

> **Stacks 0DZM.** Taking the local ring at a point of a scheme defines a functor of
> deformation categories over the category of Artinian local algebras.

```lean
noncomputable def localRingDeformationFunctor
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (X : Over (Spec (.of k))) (x : X.left) :
    letI : Algebra k (X.left.presheaf.stalk x) :=
      letI : Algebra k ((Spec (.of k)).presheaf.stalk (X.hom.base x)) :=
        StructureSheaf.stalkAlgebra k (X.hom.base x)
      ((X.hom.stalkMap x).hom.comp (algebraMap k _)).toAlgebra
    BasedFunctor
      (BasedCategory.ofFunctor
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) X))
      (BasedCategory.ofFunctor
        (Over.forget
          (residueFieldAlgebra (Λ := Λ) (k := k) (X.left.presheaf.stalk x)) ⋙
          FlatAlgebraCategory.projection (Λ := Λ) (k := k)))
```

**`Deformation.Examples.localRingDeformationFunctor_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean#L316). The attribute's comment: “fibers”.

> **Stacks 0DZM.** The underlying algebra of the image deformation is the stalk of the
> deformed scheme at the image of the chosen point.

```lean
theorem localRingDeformationFunctor_fiber
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (X : Over (Spec (.of k))) (x : X.left)
    (P : SchemeDeformationCategory (Λ := Λ) (k := k) X) :
    letI : Algebra k (X.left.presheaf.stalk x) :=
      letI : Algebra k ((Spec (.of k)).presheaf.stalk (X.hom.base x)) :=
        StructureSheaf.stalkAlgebra k (X.hom.base x)
      ((X.hom.stalkMap x).hom.comp (algebraMap k _)).toAlgebra
    ((localRingDeformationFunctor X x).obj P).left.fiber =
      P.scheme.presheaf.stalk (P.specialMap.base x)
```

**`Deformation.Examples.localRingDeformationFunctor_specialMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean#L330). The attribute's comment: “special-fiber maps”.

> **Stacks 0DZM.** The special-fibre map of the image is the stalk map of the special-fibre
> embedding.

```lean
theorem localRingDeformationFunctor_specialMap
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (X : Over (Spec (.of k))) (x : X.left)
    (P : SchemeDeformationCategory (Λ := Λ) (k := k) X) :
    letI : Algebra k (X.left.presheaf.stalk x) :=
      letI : Algebra k ((Spec (.of k)).presheaf.stalk (X.hom.base x)) :=
        StructureSheaf.stalkAlgebra k (X.hom.base x)
      ((X.hom.stalkMap x).hom.comp (algebraMap k _)).toAlgebra
    HEq ((localRingDeformationFunctor X x).obj P).hom.map.hom
      (P.specialMap.stalkMap x).hom
```

**`Deformation.Examples.localRingDeformationFunctor_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Deformations/Schemes/LocalRing.lean#L344). The attribute's comment: “morphism maps”.

> **Stacks 0DZM.** On morphisms, the induced algebra map is the stalk map of the morphism
> between the deformed schemes.

```lean
theorem localRingDeformationFunctor_map
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (X : Over (Spec (.of k))) (x : X.left)
    {P Q : SchemeDeformationCategory (Λ := Λ) (k := k) X} (f : P ⟶ Q) :
    letI : Algebra k (X.left.presheaf.stalk x) :=
      letI : Algebra k ((Spec (.of k)).presheaf.stalk (X.hom.base x)) :=
        StructureSheaf.stalkAlgebra k (X.hom.base x)
      ((X.hom.stalkMap x).hom.comp (algebraMap k _)).toAlgebra
    HEq ((localRingDeformationFunctor X x).map f).left.map.hom
      (f.map.stalkMap (Q.specialMap.base x)).hom
```

## Tag 0DYY, a situation

[Tag 0DYY](https://stacks.math.columbia.edu/tag/0DYY) in the Stacks Project.

**`Deformation.Examples.GluingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/Schemes.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/Schemes.lean#L283).

> A scheme over `k`, covered by two affine opens with affine intersection, together with
> coordinate rings for the three affine schemes.

```lean
structure GluingSituation (Λ k : Type u) [CommRing Λ] [Field k] [Algebra Λ k]
```

## Tag 0DYZ, a lemma

[Tag 0DYZ](https://stacks.math.columbia.edu/tag/0DYZ) in the Stacks Project.

**`Deformation.Examples.twoOpenComparisonFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean#L492). The attribute's comment: “the comparison functor Def\_X ⥤ Def\_\{U\_1} ×\_\{Def\_\{U\_12}} Def\_\{U\_2} only; it is not shown to be an equivalence (that needs the glueing quasi-inverse of the proof) and the translation into the ring deformation categories Def\_\{P\_i} is not included”.

> Let `X` be a scheme over `k` with two opens `U₁` and `U₂`. Restricting a deformation of `X`
> to `U₁` and to `U₂`, together with the identification of the two induced deformations of
> `U₁ ⊓ U₂`, is a functor from the deformation category of `X` to the 2-fibre product
> `Def_{U₁} ×_{Def_{U₁ ⊓ U₂}} Def_{U₂}` over `𝒞_Λ`.

```lean
def twoOpenComparisonFunctor (X : Over (Spec (.of k))) (U₁ U₂ : X.left.Opens) :
    SchemeDeformationCategory (Λ := Λ) (k := k) X ⥤
      TwoFibreProductOver
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U₁.ι ≫ X.hom)))
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U₂.ι ≫ X.hom)))
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk ((U₁ ⊓ U₂).ι ≫ X.hom)))
        (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_left : U₁ ⊓ U₂ ≤ U₁))
        (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_right : U₁ ⊓ U₂ ≤ U₂))
```

**`Deformation.Examples.twoOpenComparisonFunctor_comp_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean#L542). The attribute's comment: “the comparison functor Def\_X ⥤ Def\_\{U\_1} ×\_\{Def\_\{U\_12}} Def\_\{U\_2} is a functor over 𝒞\_Λ; it is not shown to be an equivalence and the ring deformation categories Def\_\{P\_i} are not involved”.

> The comparison functor of a two-open cover is strictly over `𝒞_Λ`.

```lean
theorem twoOpenComparisonFunctor_comp_structureFunctor (X : Over (Spec (.of k)))
    (U₁ U₂ : X.left.Opens) :
    twoOpenComparisonFunctor (Λ := Λ) (k := k) X U₁ U₂ ⋙
        TwoFibreProductOver.structureFunctor
          (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U₁.ι ≫ X.hom)))
          (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (U₂.ι ≫ X.hom)))
          (schemeDeformationCategoryProjection (Λ := Λ) (k := k)
            (Over.mk ((U₁ ⊓ U₂).ι ≫ X.hom)))
          (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_left : U₁ ⊓ U₂ ≤ U₁))
          (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_right : U₁ ⊓ U₂ ≤ U₂)) =
      schemeDeformationCategoryProjection (Λ := Λ) (k := k) X
```

**`Deformation.Examples.GluingSituation.comparisonFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean#L559). The attribute's comment: “the comparison functor in Situation 0DYY; it is not shown to be an equivalence and the translation into the ring deformation categories Def\_\{P\_i} is not included”.

> The comparison functor of the two-open cover of a glueing situation.

```lean
def GluingSituation.comparisonFunctor (S : GluingSituation Λ k) :
    SchemeDeformationCategory (Λ := Λ) (k := k) S.X ⥤
      TwoFibreProductOver
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (S.U₁.ι ≫ S.X.hom)))
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k) (Over.mk (S.U₂.ι ≫ S.X.hom)))
        (schemeDeformationCategoryProjection (Λ := Λ) (k := k)
          (Over.mk ((S.U₁ ⊓ S.U₂).ι ≫ S.X.hom)))
        (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_left : S.U₁ ⊓ S.U₂ ≤ S.U₁))
        (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_right : S.U₁ ⊓ S.U₂ ≤ S.U₂))
```

**`Deformation.Examples.glueDeformation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean, line 1014](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean#L1014). The attribute's comment: “the glueing construction of the proof, on objects only: an object of the 2-fibre product Def\_\{U\_1} ×\_\{Def\_\{U\_12}} Def\_\{U\_2} is glued to a deformation of X over the same object of 𝒞\_Λ, flat over it, with special fibre X, and restricting to U\_1 and U\_2 gives the two charts back. Not shown functorial in the datum, so not yet a quasi-inverse of twoOpenComparisonFunctor; neither the equivalence nor the Def\_\{P\_i} form is proved”.

> Let `X` be a scheme over `k` covered by two opens `U₁` and `U₂`. An object of the 2-fibre
> product `Def_{U₁} ×_{Def_{U₁ ⊓ U₂}} Def_{U₂}` consists of a deformation of `U₁`, a deformation
> of `U₂` and an isomorphism of their restrictions to `U₁ ⊓ U₂`; glueing the two total spaces
> along that isomorphism gives a deformation of `X` over the same object of `𝒞_Λ`.

```lean
def glueDeformation : SchemeDeformationCategory (Λ := Λ) (k := k) X
```

**`Deformation.Examples.GluingSituation.glueDeformation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean, line 1274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCover.lean#L1274). The attribute's comment: “the glueing construction of the proof in Situation 0DYY, on objects only; see `glueDeformation` for the precise content and for what the equivalence still needs”.

> In a glueing situation the two affine opens cover the scheme, and an object of the 2-fibre
> product of their deformation categories is glued to a deformation of the scheme itself.

```lean
def GluingSituation.glueDeformation (S : GluingSituation Λ k)
    (Q : TwoOpenDeformations (Λ := Λ) S.X S.U₁ S.U₂) :
    SchemeDeformationCategory (Λ := Λ) (k := k) S.X
```

**`Deformation.Examples.comparisonGlue_w`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean#L404). The attribute's comment: “the compatibility of the two chart isomorphisms of the glueing with the comparison isomorphism of the datum, i.e. that the two of them are one morphism of the 2-fibre product; the equivalence itself is not proved here”.

> **The two chart isomorphisms of the glued deformation are compatible with the comparison
> isomorphism of the datum.** This is the `CategoryTheory.TwoFibreProductOver.Hom.w` of the pair,
> that is, what makes `Deformation.Examples.restrictGlueDeformationLeft` and
> `Deformation.Examples.restrictGlueDeformationRight` the two components of a *single* morphism of
> the `2`-fibre product. The source of Tag 0DYZ says only "we omit the verification".

```lean
theorem comparisonGlue_w :
    (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_left : U₁ ⊓ U₂ ≤ U₁)).map
        (restrictGlueDeformationLeftHom X U₁ U₂ Q hcover) ≫ Q.iso.hom =
      (restrictDeformationLEIso (glueDeformation X U₁ U₂ Q hcover)
            (inf_le_left : U₁ ⊓ U₂ ≤ U₁) ≪≫
          (restrictDeformationLEIso (glueDeformation X U₁ U₂ Q hcover)
            (inf_le_right : U₁ ⊓ U₂ ≤ U₂)).symm).hom ≫
        (openRestrictionLEFunctor (Λ := Λ) (k := k) (inf_le_right : U₁ ⊓ U₂ ≤ U₂)).map
          (restrictGlueDeformationRightHom X U₁ U₂ Q hcover)
```

**`Deformation.Examples.comparisonGlueHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean#L453). The attribute's comment: “the comparison morphism from the comparison of the glued deformation to the datum, built from the two chart isomorphisms; it is an isomorphism, but only the morphism is constructed here, and the equivalence of Tag 0DYZ is not proved”.

> **Stacks 0DYZ**, the comparison morphism out of the glueing. The two chart isomorphisms of
> the glued deformation are the two components of one morphism of the `2`-fibre product from the
> comparison of the glued deformation to the datum it was glued from.

```lean
def comparisonGlueHom :
    (twoOpenComparisonFunctor (Λ := Λ) X U₁ U₂).obj (glueDeformation X U₁ U₂ Q hcover) ⟶ Q
```

**`Deformation.Examples.glueDeformationHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean, line 779](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean#L779). The attribute's comment: “the glueing construction of the proof on morphisms: a morphism of the 2-fibre product into the comparison of a deformation is glued to a morphism of deformations of X; the equivalence of Tag 0DYZ is not proved here”.

> **Stacks 0DYZ**, the glueing quasi-inverse on morphisms. A morphism of the `2`-fibre product
> from a datum `Q` to the comparison of a deformation `P` of `X` glues to a morphism from the
> deformation glued from `Q` to `P`. The source of Tag 0DYZ says only "we omit the
> verification".

```lean
def glueDeformationHom : glueDeformation X U₁ U₂ Q hcover ⟶ P
```

**`Deformation.Examples.twoOpenComparisonFunctor_map_glueDeformationHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean, line 801](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean#L801). The attribute's comment: “the compatibility of the glued morphism with the comparison morphism out of the glueing; the equivalence of Tag 0DYZ is not proved here”.

> **The triangle of the lifting problem commutes**: the comparison of the glued morphism is
> the comparison morphism out of the glueing followed by the given morphism.

```lean
theorem twoOpenComparisonFunctor_map_glueDeformationHom :
    (twoOpenComparisonFunctor (Λ := Λ) X U₁ U₂).map (glueDeformationHom X U₁ U₂ Q hcover P g) =
      comparisonGlueHom X U₁ U₂ Q hcover ≫ g
```

**`Deformation.Examples.isSmooth_twoOpenComparisonBasedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean, line 860](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverGlue.lean#L860). The attribute's comment: “smoothness of the comparison morphism Def\_X ⟶ Def\_\{U\_1} ×\_\{Def\_\{U\_12}} Def\_\{U\_2}, which is what Tag 0DZN consumes; that the comparison morphism is an *equivalence* — the full assertion of 0DYZ — is not proved, and neither is the translation into the ring deformation categories Def\_\{P\_i}”.

> **Stacks 0DYZ in the form Tag 0DZN uses it.** If the two opens cover `X` then the comparison
> morphism `Def_X ⟶ Def_{U₁} ×_{Def_{U₁ ⊓ U₂}} Def_{U₂}` is smooth: a lifting problem is solved by
> glueing the datum over the smaller object of `𝒞_Λ` to a deformation of `X`, glueing the given
> morphism to a morphism of deformations of `X`, and comparing the glued deformation with the
> datum by the two chart isomorphisms.

```lean
theorem isSmooth_twoOpenComparisonBasedFunctor (hcover : U₁ ⊔ U₂ = ⊤) :
    IsSmooth (twoOpenComparisonBasedFunctor (Λ := Λ) X U₁ U₂)
```

**`Deformation.Examples.GluingSituation.deformationCategories_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverRings.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Geometric/SchemesTwoOpenCoverRings.lean#L357). The attribute's comment: “Def\_X = Def\_\{P\_1} ×\_\{Def\_\{P\_12}} Def\_\{P\_2} as an equivalence over 𝒞\_Λ of deformation categories, with the ring deformation categories of Example 0DY1 and the restriction functors along U\_12 ⊆ U\_i”.

> **Stacks 0DYZ.** In Situation 0DYY, `Def_X` and `Def_{P₁} ×_{Def_{P₁₂}} Def_{P₂}` are
> deformation categories, and the comparison functor between them is an equivalence of
> categories over `𝒞_Λ`. Here `Def_{P_i}` is the deformation category of the `k`-algebra `P_i`
> of Example 0DY1, `Def_X` that of the scheme `X` of Example 0DY7, and the two legs of the
> 2-fibre product are the restriction functors `Def_{P_i} ⟶ Def_{P₁₂}` along `U₁₂ ⊆ U_i`.

```lean
theorem deformationCategories_equivalence :
    IsDeformationCategory.{u, u, u} (schemeDeformationCategoryProjection (Λ := Λ) (k := k) S.X) ∧
      IsDeformationCategory.{u, u, u} (ringChartDeformationsProjection S) ∧
      ∃ e : EquivalenceOver (schemeDeformationCategoryProjection (Λ := Λ) (k := k) S.X)
        (ringChartDeformationsProjection S), e.hom.functor = ringComparisonFunctor S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.9, Tag 0DY6](https://stacks.math.columbia.edu/tag/0DY6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
