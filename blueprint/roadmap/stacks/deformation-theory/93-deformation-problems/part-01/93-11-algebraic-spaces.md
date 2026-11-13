---
declaration: section
origin: cited
lean: Deformation.Examples.FlatAlgebraicSpaceFamily, Deformation.Examples.FlatAlgebraicSpaceFamily.Hom, Deformation.Examples.FlatAlgebraicSpaceFamily.instCategory, Deformation.Examples.flatAlgebraicSpaceFamilyFunctor, Deformation.Examples.flatAlgebraicSpaceFamilyFunctor_isCofiberedInGroupoids, Deformation.Examples.isFlat_of_over_residueField, Deformation.Examples.spaceSpecialFiber, Deformation.Examples.spaceDeformationProjection
statement: formalized
proof: formalized
---

# 93.11 Algebraic spaces

Section 93.11 of the Stacks Project, [Tag 0E3Y](https://stacks.math.columbia.edu/tag/0E3Y). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E3Z, an example

[Tag 0E3Z](https://stacks.math.columbia.edu/tag/0E3Z) in the Stacks Project.

**`Deformation.Examples.FlatAlgebraicSpaceFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L160). The attribute's comment: “the category ℱ: objects”.

> **Stacks 0E3Z.** A flat family of algebraic spaces: an object of `𝒞_Λ` together with an
> algebraic space over its spectrum, flat over it.

```lean
public structure FlatAlgebraicSpaceFamily
```

**`Deformation.Examples.FlatAlgebraicSpaceFamily.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L177). The attribute's comment: “the category ℱ: morphisms”.

> **Stacks 0E3Z.** A morphism of flat families, covariant on coefficient algebras: a
> morphism of the coefficient algebras together with a cartesian morphism of spaces over it.

```lean
public structure Hom (P Q : FlatAlgebraicSpaceFamily B hΛ hSpec)
```

**`Deformation.Examples.FlatAlgebraicSpaceFamily.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L189). The attribute's comment: “the category ℱ”.

> **Stacks 0E3Z.** Flat families of algebraic spaces and their cartesian morphisms form a
> category; composition pastes two cartesian squares.

```lean
public instance instCategory : Category (FlatAlgebraicSpaceFamily B hΛ hSpec)
```

**`Deformation.Examples.flatAlgebraicSpaceFamilyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L291). The attribute's comment: “the functor p”.

> **Stacks 0E3Z.** Forget the space and retain the coefficient algebra.

```lean
public def flatAlgebraicSpaceFamilyFunctor :
    FlatAlgebraicSpaceFamily B hΛ hSpec ⥤ ArtinianLocalAlgCat.{u, u, u} Λ k
```

**`Deformation.Examples.flatAlgebraicSpaceFamilyFunctor_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L315). The attribute's comment: “p is cofibred in groupoids”.

> **Stacks 0E3Z.** The projection from flat families of algebraic spaces to their
> coefficient algebras is cofibered in groupoids: the cocartesian lift of `A ⟶ A'` is the base
> change of the space along `Spec A' ⟶ Spec A`, which is flat because flatness of morphisms of
> algebraic spaces is stable under base change.

```lean
public theorem flatAlgebraicSpaceFamilyFunctor_isCofiberedInGroupoids :
    IsCofiberedInGroupoids (flatAlgebraicSpaceFamilyFunctor B hΛ hSpec)
```

**`Deformation.Examples.isFlat_of_over_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L340). The attribute's comment: “flatness of the special fibre”.

> An algebraic space over the spectrum of the residue field is flat over it: the target of
> every étale chart is `Spec k`, over which any morphism is flat, and the atlas of Stacks 025Y
> supplies a surjective chart, so the one-chart form of Stacks 03MJ applies.

```lean
public theorem isFlat_of_over_residueField
    (X : (BigFppfOver B (Spec (.of Λ)) hΛ)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of Λ)) hΛ X)
    (toK : X ⟶ yoneda.obj (spaceBaseOver B hΛ hSpec (residueFieldBase Λ k))) :
    Space.IsFlat B (Spec (.of Λ)) hΛ toK
```

**`Deformation.Examples.spaceSpecialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L365). The attribute's comment: “the object x₀”.

> **Stacks 0E3Z.** An algebraic space `X` over the residue field, as the object `(k, X)` of
> the category of flat families.

```lean
public def spaceSpecialFiber (X : (BigFppfOver B (Spec (.of Λ)) hΛ)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of Λ)) hΛ X)
    (toK : X ⟶ yoneda.obj (spaceBaseOver B hΛ hSpec (residueFieldBase Λ k))) :
    FlatAlgebraicSpaceFamily B hΛ hSpec
```

**`Deformation.Examples.spaceDeformationProjection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Spaces.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Spaces.lean#L379). The attribute's comment: “the deformation category of X”.

> **Stacks 0E3Z.** The deformation category of an algebraic space `X` over the residue
> field, with its structure functor to `𝒞_Λ`: its objects are flat families equipped with a
> cartesian morphism to `(k, X)`.

```lean
public abbrev spaceDeformationProjection
    (X : (BigFppfOver B (Spec (.of Λ)) hΛ)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of Λ)) hΛ X)
    (toK : X ⟶ yoneda.obj (spaceBaseOver B hΛ hSpec (residueFieldBase Λ k))) :
    Over (spaceSpecialFiber B hΛ hSpec X hX toK) ⥤ ArtinianLocalAlgCat.{u, u, u} Λ k
```

## Tag 0E40, a lemma

[Tag 0E40](https://stacks.math.columbia.edu/tag/0E40) in the Stacks Project.

**`Deformation.Examples.satisfiesRS_flatAlgebraicSpaceFamilyFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesRimSchlessinger.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesRimSchlessinger.lean#L149). The attribute's comment: “condition (RS) for the category of flat families of algebraic spaces of Example 0E3Z”.

> **Stacks Project, Tag 0E40.** The category of flat families of algebraic spaces over `𝒞_Λ` of
> Example 0E3Z satisfies the Rim-Schlessinger condition (RS).
>
> For a cospan `X₁ ⟶ X ⟵ X₂` of flat families over `A₁ ⟶ A ⟵ A₂` with `A₂ ⟶ A` surjective, the
> pushout of algebraic spaces `X₂ ⨿_X X₁` (Stacks 07VX), with its morphism to the spectrum of
> `A₁ ×_A A₂`, is a flat family (Stacks 07W3, clause (2)) restricting to `X₁` and `X₂` (Stacks
> 07W0); it is a fibre product of flat families because any flat family over `A₁ ×_A A₂` is the
> pushout of its two restrictions (the counit assertion of Stacks 07W3).

```lean
theorem satisfiesRS_flatAlgebraicSpaceFamilyFunctor :
    SatisfiesRS (flatAlgebraicSpaceFamilyFunctor B hΛ hSpec)
```

**`Deformation.Examples.isDeformationCategory_spaceDeformationProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesRimSchlessinger.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesRimSchlessinger.lean#L382). The attribute's comment: “the in-particular clause: the deformation category of an algebraic space over k is a deformation category”.

> **Stacks Project, Tag 0E40**, the in-particular clause. The deformation category of an
> algebraic space `X` over the residue field `k` is a deformation category: a predeformation
> category satisfying (RS).
>
> It is the category of flat families lying over the family `(k, X)`, which lies over the residue
> field, a terminal object of `𝒞_Λ`; condition (RS) for the category of all flat families is
> `Deformation.Examples.satisfiesRS_flatAlgebraicSpaceFamilyFunctor`.

```lean
theorem isDeformationCategory_spaceDeformationProjection
    (X : (BigFppfOver B (Spec (.of Λ)) hΛ)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B (Spec (.of Λ)) hΛ X)
    (toK : X ⟶ yoneda.obj (spaceBaseOver B hΛ hSpec (residueFieldBase Λ k))) :
    IsDeformationCategory.{u, u, u} (spaceDeformationProjection B hΛ hSpec X hX toK)
```

## Tag 0E41, a lemma

[Tag 0E41](https://stacks.math.columbia.edu/tag/0E41) in the Stacks Project.

**`Deformation.Examples.spaceInfinitesimalAutomorphismGroupChain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesInfinitesimalAutomorphisms.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesInfinitesimalAutomorphisms.lean#L97). The attribute's comment: “first display: for an algebraic space X over the field k, Inf(Def\_X) = Ext^0(NL\_\{X/k}, O\_X) = Hom(Omega\_\{X/k}, O\_X) = Der\_k(O\_X, O\_X), as three identifications at every point x0 over k and every pushforward x0 -> x\_eps along a dual-number pair (06JS): Inf(Def\_X) is isomorphic as a group to Der\_k(O\_X, O\_X), Ext^0 out of the naive cotangent complex is k-linearly Hom(Omega\_\{X/k}, O\_X), and Hom(Omega\_\{X/k}, O\_X) is k-linearly Der\_k(O\_X, O\_X), k acting through the structure morphism X -> Spec k. The second display, T Def\_X = Ext^1(NL\_\{X/k}, O\_X), is registered separately”.

> **The first display of [Stacks Project, Tag 0E41].**  In Example 0E3Z, let `X` be an
> algebraic space over the field `k`.  Then
>
> `Inf(𝓓_X) = Ext⁰_{𝒪_X}(NL_{X/k}, 𝒪_X) = Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X) = Der_k(𝒪_X, 𝒪_X)`,
>
> given as the identifications of those four groups.  `Inf(𝓓_X)` is the infinitesimal
> automorphism group `Deformation.infinitesimalAutomorphismGroup` of [Stacks Project, Tag 06JS] of
> the deformation category of `X`, a predeformation category
> (`Deformation.Examples.isPredeformationCategory_spaceDeformationProjection`), formed at an
> arbitrary point `x₀` over `k`, an arbitrary pushforward `i : x₀ ⟶ xε` of it along a dual-number
> pair `k → k[ε] → k` — the automorphisms of the deformation `X'` of `X` over `k[ε]` (the trivial
> one, `X ×_{Spec k} Spec k[ε]`) which are the identity modulo `ε`.
>
> `k` acts on `𝒪_X`-modules, and so on `Ext⁰`, on `Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X)` and on
> `Der_k(𝒪_X, 𝒪_X)`, through the pullback of functions along the structure morphism `X ⟶ Spec k`
> (`Deformation.Examples.spaceResidueFieldRingHom`).
>
> * The first component identifies `Inf(𝓓_X)` with `Der_k(𝒪_X, 𝒪_X)` as **groups**, composition of
>   automorphisms corresponding to addition of derivations; through the other two it is
>   `Ext⁰_{𝒪_X}(NL_{X/k}, 𝒪_X)`.
> * The second is `Ext⁰_{𝒪_X}(NL_{X/k}, 𝒪_X) = Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X)`, `k`-linearly, from
>   `H⁰(NL_{X/k}) = Ω_{X/k}` (Stacks 0D0Y).
> * The third is `Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X) = Der_k(𝒪_X, 𝒪_X)`, `k`-linearly, postcomposition with
>   the universal derivation of Stacks 04CT, as Modules on Sites, Definition 04BN defines `Ω`.

```lean
def spaceInfinitesimalAutomorphismGroupChain
    [HasDerivedCategory.{w} (NaiveCotangentModules B (Spec (.of Λ)) hΛ (spaceOf B hΛ X hX))]
    {Aε : ArtinianLocalAlgCat.{u, u, u} Λ k}
    {x₀ : (spaceDeformationProjection B hΛ hSpec X hX toK).Fiber
      (residueFieldObject.{u, u, u} Λ k)}
    {xε : (spaceDeformationProjection B hΛ hSpec X hX toK).Fiber Aε}
    (g : residueFieldObject.{u, u, u} Λ k ⟶ Aε) (e : Aε ⟶ residueFieldObject.{u, u, u} Λ k)
    (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1)
    (hi : (spaceDeformationProjection B hΛ hSpec X hX toK).IsHomLift g i) :
    letI := naiveCotangentModulesLinear B (Spec (.of Λ)) hΛ (X := spaceOf B hΛ X hX)
      (spaceResidueFieldRingHom B hΛ hSpec X hX toK)
    letI := modulesLinearOfRingHom B (Spec (.of Λ)) hΛ (X := spaceOf B hΛ X hX)
      (spaceResidueFieldRingHom B hΛ hSpec X hX toK)
    letI : Module k (SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK)) :=
      derivationModuleOfRingHom B (Spec (.of Λ)) hΛ (X := spaceOf B hΛ X hX)
        (spaceResidueFieldRingHom B hΛ hSpec X hX toK)
        (spaceStructureMap B hΛ hSpec X hX toK) (spaceStructureModule B hΛ (spaceOf B hΛ X hX))
    (infinitesimalAutomorphismGroup
        (isPredeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK) g e hpair i hi ≃*
      Multiplicative (SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK))) ×
    (DerivedCategory.Ext (DerivedCategory.Q.obj (naiveCotangentComplex B (Spec (.of Λ)) hΛ
        (spaceStructureMap B hΛ hSpec X hX toK)))
        ((DerivedCategory.singleFunctor _ 0).obj
          (naiveCotangentCoefficient B (Spec (.of Λ)) hΛ
            (spaceStructureModule B hΛ (spaceOf B hΛ X hX)))) 0 ≃ₗ[k]
      (sheafOfDifferentials B (Spec (.of Λ)) hΛ (spaceStructureMap B hΛ hSpec X hX toK) ⟶
        spaceStructureModule B hΛ (spaceOf B hΛ X hX))) ×
    ((sheafOfDifferentials B (Spec (.of Λ)) hΛ (spaceStructureMap B hΛ hSpec X hX toK) ⟶
        spaceStructureModule B hΛ (spaceOf B hΛ X hX)) ≃ₗ[k]
      SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK))
```

**`Deformation.Examples.spaceInfinitesimalAutomorphismGroup_linearEquivDerivations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesInfinitesimalAutomorphismsLinear.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesInfinitesimalAutomorphismsLinear.lean#L311). The attribute's comment: “first display, k-linear form: for an algebraic space X over the field k, Inf(Def\_X) with the vector space structure of 06JV (addition is composition; c acts by pushforward along eps -> c eps, along every arrow over such a rescaling fixing the pushforward x0 -> x\_eps) is k-linearly isomorphic to Der\_k(O\_X, O\_X), k acting through the structure morphism X -> Spec k, by the first identification of the first display, at every point x0 over k and every pushforward along a dual-number pair”. References: SGA 3 II (3.14), “special case”.

> **The first display of [Stacks Project, Tag 0E41], `k`-linearly: `Inf(𝓓_X) = Der_k(𝒪_X, 𝒪_X)`
> as `k`-vector spaces.**  In Example 0E3Z, let `X` be an algebraic space over the field `k`.  At
> every point `x₀` of the deformation category of `X` over `k`, every pushforward `i : x₀ ⟶ xε` of
> it along a dual-number pair `k → k[ε] → k` and every predeformation-category structure, the
> infinitesimal automorphism group `Inf(𝓓_X)` of [Stacks Project, Tag 06JS] carries the
> `k`-vector-space structure of [Stacks Project, Tag 06JV]:
>
> * addition is composition of infinitesimal automorphisms;
> * a scalar `c` acts by pushforward along `ε ↦ c ε`: for every endomorphism `s` of the base which is
>   `ε ↦ c ε` in a dual-number coordinate and every arrow `j : xε ⟶ xε` over `s` fixing `i`, `c • a`
>   is the pushforward of `a` along `j`;
>
> and the first identification of the first display,
> `Deformation.Examples.spaceInfinitesimalAutomorphismGroupMulEquivDerivations`, is a `k`-linear
> isomorphism onto `Der_k(𝒪_X, 𝒪_X)`, `k` acting on derivations through the structure morphism
> `X ⟶ Spec k`.  The remaining identifications of the display,
> `Ext⁰_{𝒪_X}(NL_{X/k}, 𝒪_X) = Hom_{𝒪_X}(Ω_{X/k}, 𝒪_X) = Der_k(𝒪_X, 𝒪_X)`, are `k`-linear by
> `Deformation.Examples.spaceInfinitesimalAutomorphismGroupChain`.

```lean
theorem spaceInfinitesimalAutomorphismGroup_linearEquivDerivations :
    letI : Module k (SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK)) :=
      derivationModuleOfRingHom B (Spec (.of Λ)) hΛ (X := spaceOf B hΛ X hX)
        (spaceResidueFieldRingHom B hΛ hSpec X hX toK)
        (spaceStructureMap B hΛ hSpec X hX toK) (spaceStructureModule B hΛ (spaceOf B hΛ X hX))
    ∃ A : AddCommGroup (Additive (infinitesimalAutomorphismGroup hp g e hpair i hi)),
      letI := A
      ∃ M : Module k (Additive (infinitesimalAutomorphismGroup hp g e hpair i hi)),
        letI := M
        (∀ a b : infinitesimalAutomorphismGroup hp g e hpair i hi,
          Additive.ofMul a + Additive.ofMul b = Additive.ofMul (a * b)) ∧
        (∀ (c : k) (s : Aε ⟶ Aε),
          (∃ φ : Aε ≃ₐ[Λ] DualNumber k,
            (∀ t : Aε, (φ t).1 = Aε.residueEquiv (IsLocalRing.residue Aε t)) ∧
            (∀ t : k, φ (s.hom (φ.symm (TrivSqZeroExt.inl t))) = TrivSqZeroExt.inl t) ∧
            φ (s.hom (φ.symm DualNumber.eps)) = c • DualNumber.eps) →
          ∀ (j : xε.1 ⟶ xε.1) (hj : (spaceDeformationProjection B hΛ hSpec X hX toK).IsHomLift s j),
            i ≫ j = i → ∀ a : infinitesimalAutomorphismGroup hp g e hpair i hi,
              ∃ b : infinitesimalAutomorphismGroup hp g e hpair i hi,
                b.val = pushforwardAutomorphismHom hp.cofibered s j hj a.val ∧
                  c • Additive.ofMul a = Additive.ofMul b) ∧
        ∃ E : Additive (infinitesimalAutomorphismGroup hp g e hpair i hi) ≃ₗ[k]
            SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK),
          ∀ a : infinitesimalAutomorphismGroup hp g e hpair i hi,
            DFunLike.coe
              (F := Additive (infinitesimalAutomorphismGroup hp g e hpair i hi) ≃ₗ[k]
                SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK)) E
              (Additive.ofMul a) =
            Multiplicative.toAdd
              (spaceInfinitesimalAutomorphismGroupMulEquivDerivations B hΛ hSpec X hX toK hpair i
                hp hi a)
```

**`Deformation.Examples.spaceTangentSpaceLinearEquivExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesTangentSpaceLinearEquivExt.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesTangentSpaceLinearEquivExt.lean#L145). The attribute's comment: “second display: for an algebraic space X over the field k, T Def\_X = Ext^1(NL\_\{X/k}, O\_X) as k-vector spaces, from the tangent space of the deformation category of X (isomorphism classes of flat deformations of X over k[eps], with the canonical vector space structure of 06IH) onto Ext^1\_\{O\_X}(NL\_\{X/k}, O\_X) of the naive cotangent complex of 0D0V, k acting through the structure morphism X -> Spec k; a deformation goes to the 0GQ5 class of the extension 0 -> O\_X -> O\_X' -> O\_X -> 0. The first display is registered separately”.

> **Stacks 0E41, second display.** In Example 0E3Z let `X` be an algebraic space over `k`. Then
> `T Def_X = Ext¹_{𝒪_X}(NL_{X/k}, 𝒪_X)`: the tangent space of the deformation category `Def_X` (the
> isomorphism classes of flat deformations of `X` over `k[ε]`, with the vector-space structure of
> Stacks 06IH) is `k`-linearly isomorphic to `Ext¹` of the naive cotangent complex `NL_{X/k}` of
> Stacks 0D0V into `𝒪_X` (sections raised to the universe of `NL_{X/k}`, any model of the derived
> category), `k` acting through the structure morphism `X ⟶ Spec k`. A deformation `X'` goes to the
> class (Stacks 0GQ5) of the extension `0 ⟶ 𝒪_X ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0`
> (`Deformation.Examples.spaceTangentSpaceLinearEquivExtModel_apply`).

```lean
def spaceTangentSpaceLinearEquivExt
    [HasDerivedCategory.{w} (Space.NaiveCotangentModules B (Spec (.of Λ)) hΛ (spaceOf B hΛ X hX))] :
    letI : Fact (IsPredeformationCategory
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK)).p) :=
      ⟨(isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π (isomorphismClasses
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
          toK).predeformation.cofibered))) :=
      ⟨Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK)⟩
    letI := Space.naiveCotangentModulesLinear B (Spec (.of Λ)) hΛ (X := spaceOf B hΛ X hX)
      (spaceResidueFieldRingHom B hΛ hSpec X hX toK)
    artinianTangentSpace Λ k (isomorphismClasses
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
          toK).predeformation.cofibered) ≃ₗ[k]
      DerivedCategory.Ext
        (DerivedCategory.Q.obj (Space.naiveCotangentComplex B (Spec (.of Λ)) hΛ
          (spaceStructureMap B hΛ hSpec X hX toK)))
        ((DerivedCategory.singleFunctor _ 0).obj
          (Space.naiveCotangentCoefficient B (Spec (.of Λ)) hΛ
            (spaceStructureModule B hΛ (spaceOf B hΛ X hX)))) 1
```

## Tag 0E42, a lemma

[Tag 0E42](https://stacks.math.columbia.edu/tag/0E42) in the Stacks Project.

**`Deformation.Examples.spaceInfinitesimalAutomorphisms_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesFiniteDimensional.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesFiniteDimensional.lean#L99). The attribute's comment: “infinitesimal automorphisms: for an algebraic space X proper over the field k, Inf(Def\_X), with the vector space structure of 06JV (addition is composition; c acts by pushforward along eps -> c eps), is finite dimensional over k, at every point x0 over k and every pushforward x0 -> x\_eps along a dual-number pair”.

> **Stacks 0E42, the infinitesimal automorphisms.**  In Example 0E3Z, let `X` be an algebraic
> space over the field `k` which is proper over `k`.  Then `Inf(𝓓_X)` is a finite-dimensional
> `k`-vector space: at every point `x₀` of `𝓓_X` over `k` and every pushforward `i : x₀ ⟶ xε` of it
> along a dual-number pair `k → Aε → k`, the infinitesimal automorphism group of Stacks 06JS carries
> a `k`-vector-space structure
>
> * whose addition is composition of infinitesimal automorphisms, and
> * in which a scalar `c` acts by pushforward along `ε ↦ c ε`: for every endomorphism `s` of `Aε`
>   which is `ε ↦ c ε` in a dual-number coordinate of `Aε` (and the identity on the residue field)
>   and every arrow `j : xε ⟶ xε` over `s` fixing `i`, `c • a` is the pushforward of `a` along `j`,
>
> and this vector space is finite dimensional.  The predeformation-category structure of `𝓓_X` is
> that of Stacks 0E40 (`Deformation.Examples.isDeformationCategory_spaceDeformationProjection`).

```lean
theorem spaceInfinitesimalAutomorphisms_finiteDimensional
    (hproper : Space.IsProper B (Spec (.of Λ)) hΛ toK)
    {Aε : ArtinianLocalAlgCat.{u, u, u} Λ k}
    {x₀ : (spaceDeformationProjection B hΛ hSpec X hX toK).Fiber
      (residueFieldObject.{u, u, u} Λ k)}
    {xε : (spaceDeformationProjection B hΛ hSpec X hX toK).Fiber Aε}
    (g : residueFieldObject.{u, u, u} Λ k ⟶ Aε) (e : Aε ⟶ residueFieldObject.{u, u, u} Λ k)
    (hpair : IsCanonicalDualNumberPair g e) (i : x₀.1 ⟶ xε.1)
    (hi : (spaceDeformationProjection B hΛ hSpec X hX toK).IsHomLift g i) :
    ∃ hA : AddCommGroup (infinitesimalAutomorphismGroup
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation g e
        hpair i hi),
      letI := hA
      ∃ hM : Module k (infinitesimalAutomorphismGroup
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation g e
        hpair i hi),
        letI := hM
        (∀ a b : (infinitesimalAutomorphismGroup
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation g e
        hpair i hi), a + b = a * b) ∧
        (∀ (c : k) (s : Aε ⟶ Aε),
            IsDualNumberScaling c s →
            s ≫ e = e →
            ∀ (j : xε.1 ⟶ xε.1)
                (hj : (spaceDeformationProjection B hΛ hSpec X hX toK).IsHomLift s j),
              i ≫ j = i → ∀ a : (infinitesimalAutomorphismGroup
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation g e
        hpair i hi),
                ∃ b : (infinitesimalAutomorphismGroup
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation g e
        hpair i hi),
                  b.val = pushforwardAutomorphismHom
                    (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
                      toK).predeformation.cofibered s j hj a.val ∧ c • a = b) ∧
        FiniteDimensional k (infinitesimalAutomorphismGroup
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation g e
        hpair i hi)
```

**`Deformation.Examples.spaceTangentSpace_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesTangentSpaceFinite.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesTangentSpaceFinite.lean#L55). The attribute's comment: “tangent space: for an algebraic space X proper over the field k, the tangent space T Def\_X of its deformation category (isomorphism classes of flat deformations over k[eps], with the canonical vector space structure of 06IH) is finite dimensional over k. The clause on Inf(Def\_X) is registered separately”.

> **Stacks 0E42, the tangent space.** In Lemma 0E41, if the algebraic space `X` is proper over
> `k`, then `T Def_X` (with the vector-space structure of Stacks 06IH) is finite dimensional over
> `k`.

```lean
theorem spaceTangentSpace_finiteDimensional (hproper : Space.IsProper B (Spec (.of Λ)) hΛ toK) :
    letI : Fact (IsPredeformationCategory
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK)).p) :=
      ⟨(isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK).predeformation⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π (isomorphismClasses
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
          toK).predeformation.cofibered))) :=
      ⟨Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX toK)⟩
    FiniteDimensional k (artinianTangentSpace Λ k (isomorphismClasses
        (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
        (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
          toK).predeformation.cofibered))
```

## Tag 0ET7, a lemma

[Tag 0ET7](https://stacks.math.columbia.edu/tag/0ET7) in the Stacks Project.

**`Deformation.Examples.exists_hull_spaceIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesHull.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesHull.lean#L102). The attribute's comment: “for a proper algebraic space X over k and Λ complete local with residue field k, the functor of isomorphism classes of Def\_X has a hull”.

> **Stacks 0ET7, the hull.** Let `Λ` be a complete local ring with residue field `k` and let
> `X` be a proper algebraic space over `k`. Then the functor `A ↦ Ob(Def_X(A))/≅` of isomorphism
> classes of deformations of `X` has a hull: a versal formal object whose differential is
> bijective.

```lean
public theorem exists_hull_spaceIsomorphismClasses (hcl : IsClassical Λ k)
    (hproper : Space.IsProper B (Spec (.of Λ)) hΛ toK) :
    let G := isomorphismClasses
      (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
      (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
        toK).predeformation.cofibered
    ∃ ξ : FormalObject (Functor.Elements.π G),
      IsHull (categoryOfElements_projection_isCofibered G) ξ
```

**`Deformation.Examples.isProrepresentableULift_spaceIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SpacesHull.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SpacesHull.lean#L120). The attribute's comment: “if Der\_k(O\_X, O\_X) = 0, the functor of isomorphism classes of Def\_X is prorepresentable”.

> **Stacks 0ET7, prorepresentability.** Let `Λ` be a complete local ring with residue field
> `k` and let `X` be a proper algebraic space over `k` with `Der_k(𝒪_X, 𝒪_X) = 0`. Then the functor
> `A ↦ Ob(Def_X(A))/≅` of isomorphism classes of deformations of `X` is prorepresentable.

```lean
public theorem isProrepresentableULift_spaceIsomorphismClasses (hcl : IsClassical Λ k)
    (hproper : Space.IsProper B (Spec (.of Λ)) hΛ toK)
    (hDer : ∀ D : SpaceDerivations B hΛ (spaceStructureMap B hΛ hSpec X hX toK), D = 0) :
    IsProrepresentableULift (isomorphismClasses
      (BasedCategory.ofFunctor (spaceDeformationProjection B hΛ hSpec X hX toK))
      (isDeformationCategory_spaceDeformationProjection B hΛ hSpec X hX
        toK).predeformation.cofibered)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.11, Tag 0E3Y](https://stacks.math.columbia.edu/tag/0E3Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
