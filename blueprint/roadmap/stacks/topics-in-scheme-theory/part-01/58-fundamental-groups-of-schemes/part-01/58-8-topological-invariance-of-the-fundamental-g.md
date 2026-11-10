---
declaration: section
origin: cited
lean: AlgebraicGeometry.etaleFundamentalGroupContinuousMulEquivOfIsEquivalence, AlgebraicGeometry.isHomeomorph_connectedComponentsMap_of_finiteEtaleBaseChange, AlgebraicGeometry.connectedSpace_iff_of_finiteEtaleBaseChange, AlgebraicGeometry.fundamentalGroupContinuousMulEquivOfFiniteEtaleBaseChange, AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_henselianPair, AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_isThickening, AlgebraicGeometry.finiteEtaleBaseChange_normalizationOfIrreducible_isEquivalence, AlgebraicGeometry.faithful_finiteEtaleBaseChange_of_universalHomeomorphism
statement: formalized
proof: formalized
---

# 58.8 Topological invariance of the fundamental group

Section 58.8 of the Stacks Project, [Tag 0BTT](https://stacks.math.columbia.edu/tag/0BTT). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BQA, a lemma

[Tag 0BQA](https://stacks.math.columbia.edu/tag/0BQA) in the Stacks Project.

**`AlgebraicGeometry.etaleFundamentalGroupContinuousMulEquivOfIsEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/BaseChangeEquivalence.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/EtaleFundamental/BaseChangeEquivalence.lean#L150). The attribute's comment: “part (2)”. References: SGA 4 XII (6.5), “(ii) b')⇒b'') π₁”.

> If base change along `f : X ⟶ Y` is an equivalence on finite étale covers, then `f` identifies
> the étale fundamental group of `X` at a geometric point `x` with the étale fundamental group of `Y`
> at the image geometric point, as topological groups.

```lean
def etaleFundamentalGroupContinuousMulEquivOfIsEquivalence (f : X ⟶ Y) (x : GeometricPoint X)
    [(finiteEtaleBaseChange f).IsEquivalence] :
    EtaleFundamentalGroup X x ≃ₜ* EtaleFundamentalGroup Y (x.map f)
```

**`AlgebraicGeometry.isHomeomorph_connectedComponentsMap_of_finiteEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/CoverEquivalenceInvariance.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/CoverEquivalenceInvariance.lean#L272). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0BQA, part (1).** Let `f : X ⟶ Y` be a morphism of quasi-compact and
> quasi-separated schemes such that the base change functor `FÉt_Y ⥤ FÉt_X` is an equivalence of
> categories. Then the induced map `π₀(X) → π₀(Y)` on spaces of connected components is a
> homeomorphism.
>
> The equivalence identifies the clopen subsets of `Y` with those of `X` by taking preimages, and
> in a spectral space that lattice determines the connected components; both spaces of connected
> components are profinite, so a continuous bijection between them is a homeomorphism.

```lean
theorem isHomeomorph_connectedComponentsMap_of_finiteEtaleBaseChange {X Y : Scheme.{u}}
    (f : X ⟶ Y) [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y]
    [QuasiSeparatedSpace Y] (hf : (finiteEtaleBaseChange f).IsEquivalence) :
    IsHomeomorph f.continuous.connectedComponentsMap
```

**`AlgebraicGeometry.connectedSpace_iff_of_finiteEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/CoverEquivalenceInvariance.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/CoverEquivalenceInvariance.lean#L347). The attribute's comment: “part (2), the source is connected iff the target is”. References: SGA 4 XII (6.5), “(ii) b')⇒b'') π₀”.

> **Stacks Project, Tag 0BQA, part (2), the "or equivalently".** Under the hypotheses of
> Tag 0BQA the source is connected if and only if the target is: part (1) puts the two spaces of
> connected components in bijection, and a space is connected exactly when its space of connected
> components is a single point.

```lean
theorem connectedSpace_iff_of_finiteEtaleBaseChange {X Y : Scheme.{u}} (f : X ⟶ Y)
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    (hf : (finiteEtaleBaseChange f).IsEquivalence) : ConnectedSpace X ↔ ConnectedSpace Y
```

**`AlgebraicGeometry.fundamentalGroupContinuousMulEquivOfFiniteEtaleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/CoverEquivalenceInvariance.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/CoverEquivalenceInvariance.lean#L391). The attribute's comment: “part (2)”. References: SGA 4 XII (6.5), “(ii) b')⇒b'') π₁”; SGA 1 V (6.10), “special case”.

> **Stacks Project, Tag 0BQA, part (2).** Let `f : X ⟶ Y` be a morphism of connected schemes
> such that the base change functor `FÉt_Y ⥤ FÉt_X` is an equivalence of categories, and let `x` be
> a geometric point of `X`. Then the induced continuous homomorphism
> `AlgebraicGeometry.etaleFundamentalGroupMap` is an isomorphism of topological groups
> `π₁(X, x) ≅ π₁(Y, f ∘ x)`.
>
> The two connectedness hypotheses are equivalent to one another whenever `X` and `Y` are
> quasi-compact and quasi-separated, by
> `AlgebraicGeometry.connectedSpace_iff_of_finiteEtaleBaseChange`. Combined with
> `AlgebraicGeometry.etaleFundamentalGroupMap_finiteEtaleFiberProjection`, the recorded
> identification of the underlying map says that the isomorphism intertwines the actions of the two
> fundamental groups on the geometric fibre of every finite étale cover of `Y`.

```lean
def fundamentalGroupContinuousMulEquivOfFiniteEtaleBaseChange {X Y : Scheme.{u}} (f : X ⟶ Y)
    [ConnectedSpace X] [ConnectedSpace Y]
    (hf : (finiteEtaleBaseChange f).IsEquivalence) (x : GeometricPoint X) :
    { e : EtaleFundamentalGroup X x ≃ₜ* EtaleFundamentalGroup Y (x.map f) //
      ∀ σ : EtaleFundamentalGroup X x, e σ = etaleFundamentalGroupMap f x σ }
```

## Tag 09ZS, a lemma

[Tag 09ZS](https://stacks.math.columbia.edu/tag/09ZS) in the Stacks Project.

**`AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/Basic.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/Basic.lean#L212). References: EGA IV (18.5.15), “more general”; SGA 7 XIII (1.2.1), “FÉt equivalence”; SGA 3 X (4.0), “ÉtCov(S)≃ÉtCov(S₀)”; SGA 4 XII (5.9bis), “X = S affine”.

> For a henselian pair `(A, I)`, base change from `Spec A` to `Spec (A ⨸ I)` is an
> equivalence on finite étale schemes.

```lean
public theorem finiteEtaleBaseChange_isEquivalence_of_henselianPair
    (A : Type u) [CommRing A] (I : Ideal A) (hI : HenselianPair A I) :
    (MorphismProperty.Over.pullback
      ((@IsFinite : MorphismProperty Scheme.{u}) ⊓ @Etale) ⊤
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))).IsEquivalence
```

## Tag 0BQB, a lemma

[Tag 0BQB](https://stacks.math.columbia.edu/tag/0BQB) in the Stacks Project.

**`AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/Thickening.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/Thickening.lean#L79). References: SGA 1 IX (1.7), “special case”; SGA 1 IX (4.10), “special case”.

> **Stacks Project, Tag 0BQB.** Let `X ⊆ X'` be a thickening of schemes. The functor
> `FÉt_{X'} ⟶ FÉt_X`, `U' ↦ U' ×_{X'} X`, is an equivalence of categories.

```lean
theorem finiteEtaleBaseChange_isEquivalence_of_isThickening {X X' : Scheme.{u}} (i : X ⟶ X')
    (hi : IsThickening i) : (finiteEtaleBaseChange i).IsEquivalence
```

## Tag 0BQN, a proposition

[Tag 0BQN](https://stacks.math.columbia.edu/tag/0BQN) in the Stacks Project.

**`AlgebraicGeometry.finiteEtaleBaseChange_normalizationOfIrreducible_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/UnibranchNormalizationEquivalence.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FiniteLocallyConstant/UnibranchNormalizationEquivalence.lean#L97). The attribute's comment: “fullness and essential surjectivity of the base change functor `FÉt_X ⥤ FÉt_Xᵛ`, alongside faithfulness, i.e. the whole equivalence, specialised to the normalization of an irreducible geometrically unibranch scheme. No part of Tag 0BQN is reproved here. All three halves are already available for an arbitrary universal homeomorphism, unconditionally, as `AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_universalHomeomorphism`, which also carries this tag, and whose faithfulness half is additionally isolated as `AlgebraicGeometry.faithful_finiteEtaleBaseChange_of_universalHomeomorphism`. What this declaration adds is only that the normalization morphism of an irreducible geometrically unibranch scheme is such a universal homeomorphism, which is Tag 0GIQ, so that the equivalence becomes available at the morphism along which the source reduces Tag 0GIY”.

> **Stacks Project, Tag 0BQN at the normalization of a geometrically unibranch scheme.** Let
> `X` be an irreducible, geometrically unibranch scheme. Base change along the normalization
> `ν : X^ν → X` is an equivalence `FÉt_X ⥤ FÉt_{X^ν}`, `V ↦ V ×_X X^ν`.
>
> The normalization of an irreducible geometrically unibranch scheme is a universal homeomorphism
> by Stacks Tag 0GIQ, and base change along a universal homeomorphism is an equivalence of
> categories of finite étale covers by
> `AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_universalHomeomorphism`.

```lean
theorem finiteEtaleBaseChange_normalizationOfIrreducible_isEquivalence (X : Scheme.{u})
    [IrreducibleSpace X] (hX : IsGeometricallyUnibranch X) :
    (finiteEtaleBaseChange (Scheme.normalizationOfIrreducible X)).IsEquivalence
```

**`AlgebraicGeometry.faithful_finiteEtaleBaseChange_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/UniversalHomeomorphism.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/UniversalHomeomorphism.lean#L64). The attribute's comment: “faithfulness of the base change functor `FÉt_Y ⥤ FÉt_X`”.

> **Stacks Project, Tag 0BQN, faithfulness of the base change functor.** Let `f : X ⟶ Y` be a
> universal homeomorphism. Base change along `f` is faithful on finite étale covers: two morphisms
> `V₁ ⟶ V₂` of finite étale covers of `Y` whose base changes `V₁ ×_Y X ⟶ V₂ ×_Y X` agree are
> equal.
>
> A universal homeomorphism is surjective, which is all that faithfulness uses.

```lean
theorem faithful_finiteEtaleBaseChange_of_universalHomeomorphism (f : X ⟶ Y)
    [UniversalHomeomorphism f] : (finiteEtaleBaseChange f).Faithful
```

**`AlgebraicGeometry.finiteEtaleBaseChange_isEquivalence_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/UniversalHomeomorphismEquivalence.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/UniversalHomeomorphismEquivalence.lean#L107). The attribute's comment: “the equivalence `FÉt_Y ⥤ FÉt_X`”. References: EGA IV (18.1.2), “special case”; SGA 1 IX (1.7), “partial”; SGA 1 IX (4.10), “special case”; SGA 1 IX (6.8), “special case”; SGA 4½ Th finitude (2.7), “partial”.

> **Topological invariance of finite étale covers.** Let `f : X ⟶ Y` be a universal
> homeomorphism of schemes. Then base change `FÉt_Y ⥤ FÉt_X`, `V ↦ V ×_Y X`, is an equivalence of
> categories.
>
> Base change along `f` is an equivalence of small étale sites (Stacks 04DZ), and an étale
> `V ⟶ Y` is finite exactly when `V ×_Y X ⟶ X` is, by
> `AlgebraicGeometry.isFinite_of_isFinite_pullback_snd_of_universalHomeomorphism`; so the
> equivalence restricts to the finite étale covers.

```lean
theorem finiteEtaleBaseChange_isEquivalence_of_universalHomeomorphism (f : X ⟶ Y)
    [UniversalHomeomorphism f] : (finiteEtaleBaseChange f).IsEquivalence
```

**`AlgebraicGeometry.fundamentalGroupContinuousMulEquivOfUniversalHomeomorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/UniversalHomeomorphismEquivalence.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/TopologicalInvarianceFundamental/UniversalHomeomorphismEquivalence.lean#L157). The attribute's comment: “the isomorphism of fundamental groups”.

> **Topological invariance of the étale fundamental group.** Let `f : X ⟶ Y` be a universal
> homeomorphism of connected schemes and `x` a geometric point of `X`. Then the induced continuous
> homomorphism `AlgebraicGeometry.etaleFundamentalGroupMap f x : π₁(X, x) → π₁(Y, f ∘ x)` is an
> isomorphism of topological groups.

```lean
def fundamentalGroupContinuousMulEquivOfUniversalHomeomorphism (f : X ⟶ Y)
    [UniversalHomeomorphism f] [ConnectedSpace X] [ConnectedSpace Y] (x : GeometricPoint X) :
    { e : EtaleFundamentalGroup X x ≃ₜ* EtaleFundamentalGroup Y (x.map f) //
      ∀ σ : EtaleFundamentalGroup X x, e σ = etaleFundamentalGroupMap f x σ }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.8, Tag 0BTT](https://stacks.math.columbia.edu/tag/0BTT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
