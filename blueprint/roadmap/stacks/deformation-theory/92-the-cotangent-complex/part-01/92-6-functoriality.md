---
declaration: section
origin: cited
lean: Stacks.ChaoticSite.isTransport_coefficientSquareComparison, Stacks.ChaoticSite.coefficientSquare_commutes, Stacks.ChaoticSite.isTransport_functorialitySquareComparison, Stacks.ChaoticSite.functorialitySquare_commutes, CommAlgCat.baseChangeAugmentation_tmul, CommAlgCat.baseChangeMap_tmul, CommAlgCat.isPolynomialAlgebra_baseChange, CommAlgCat.polynomialBaseChange
statement: formalized
proof: formalized
---

# 92.6 Functoriality

Section 92.6 of the Stacks Project, [Tag 08QL](https://stacks.math.columbia.edu/tag/08QL). 5 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08QN, an equation

[Tag 08QN](https://stacks.math.columbia.edu/tag/08QN) in the Stacks Project.

**`Stacks.ChaoticSite.isTransport_coefficientSquareComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean#L396). The attribute's comment: “change-of-coefficients square: the comparison is the canonical one”.

> **The comparison is the canonical one.** It is the identity of the restriction functor along
> `C ⥤ *`, not some other automorphism of it; this is what makes
> `Stacks.ChaoticSite.coefficientSquare_commutes` a statement about the square rather than about a
> choice.

```lean
theorem isTransport_coefficientSquareComparison :
    Stacks.IsTransport (coefficientSquareComparison.{w} C φ).hom
```

**`Stacks.ChaoticSite.coefficientSquare_commutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean#L475). The attribute's comment: “the change-of-coefficients square of constant-coefficient ringed topoi”.

> **The change-of-coefficients square commutes.** The structure map of the one composite,
> transported along the adjoint mate of the canonical comparison, is the structure map of the
> other; see `AlgebraicGeometry.RingedToposHom.SquareCommutes`, which is that equation.

```lean
theorem coefficientSquare_commutes :
    SquareCommutes (X := constantRingedTopos C R')
      (Y := constantRingedTopos (Discrete PUnit.{u₁ + 1}) R)
      (coefficientSquareDownAcross.{w} C φ) (coefficientSquareAcrossDown.{w} C φ)
      (coefficientSquareComparison.{w} C φ)
```

**`Stacks.ChaoticSite.isTransport_functorialitySquareComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean#L552). The attribute's comment: “functoriality triangle: the comparison is the canonical one”.

> **The comparison is the canonical one**, hence a transport: it is built from the
> identification `u ⋙ star = star` of the two functors to the point and nothing else.

```lean
theorem isTransport_functorialitySquareComparison :
    Stacks.IsTransport (functorialitySquareComparison.{w} C D u R).hom
```

**`Stacks.ChaoticSite.functorialitySquare_commutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedSquares.lean#L574). The attribute's comment: “the functoriality triangle of constant-coefficient ringed topoi”.

> **The functoriality triangle commutes.** Every edge is a transport, so the structure map of
> `π_C ∘ g` transported along the adjoint mate of the canonical comparison is the structure map of
> `π_D`.

```lean
theorem functorialitySquare_commutes :
    (constantRingedTopos (Discrete PUnit.{u₁ + 1}) R).forgetRing.map
        (functorialitySquareAcrossDown.{w} C D u R).fSharp ≫
      (((functorialitySquareAcrossDown.{w} C D u R).toToposHom.adj.ofNatIsoLeft
            (functorialitySquareComparison.{w} C D u R)).rightAdjointUniq
          (constantProjection.{w} D R).toToposHom.adj).hom.app
        ((constantRingedTopos D R).forgetRing.obj (constantRingedTopos D R).O) =
      (constantRingedTopos (Discrete PUnit.{u₁ + 1}) R).forgetRing.map
        (constantProjection.{w} D R).fSharp
```

**`CommAlgCat.baseChangeAugmentation_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean#L84). The attribute's comment: “base-change augmentation on a pure tensor”.

> The augmentation of `A' ⊗_A P` sends `a' ⊗ p` to `a' · b(α(p))`.

```lean
theorem baseChangeAugmentation_tmul (X : Over B) (a' : A') (p : (X.left : Type u)) :
    baseChangeAugmentation b X (a' ⊗ₜ[A] p) =
      algebraMap A' (B' : Type u) a' * b (X.hom.hom p)
```

**`CommAlgCat.baseChangeMap_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean#L96). The attribute's comment: “base change of a morphism on a pure tensor”.

> Extension of scalars of a morphism `f` of augmented algebras sends `a' ⊗ p` to `a' ⊗ f(p)`.

```lean
theorem baseChangeMap_tmul {X Y : Over B} (f : X ⟶ Y) (a' : A') (p : (X.left : Type u)) :
    baseChangeMap f (a' ⊗ₜ[A] p) = a' ⊗ₜ[A] f.left.hom p
```

**`CommAlgCat.isPolynomialAlgebra_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean#L156). The attribute's comment: “base change preserves polynomial algebras”.

> Extension of scalars takes a polynomial `A`-algebra to a polynomial `A'`-algebra:
> `A' ⊗_A A[S] = A'[S]`.

```lean
theorem isPolynomialAlgebra_baseChange (P : CommAlgCat.{u} A)
    (hP : IsPolynomialAlgebra A P) :
    IsPolynomialAlgebra A' (baseChangeObj (A' := A') P)
```

**`CommAlgCat.polynomialBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean#L180). The attribute's comment: “polynomial-site base change”.

> The functor of sites `C_{B/A} ⟶ C_{B'/A'}` induced by a commutative square of rings,
> given by extension of scalars on polynomial algebras augmented to `B`.

```lean
def polynomialBaseChange : polynomialSite A B ⥤ polynomialSite A' B'
```

**`CommAlgCat.polynomialBaseChange_obj_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean#L186). The attribute's comment: “polynomial-site base change on objects”.

> The augmentation of the image of `X` under `polynomialBaseChange b` is
> `baseChangeAugmentation b X`.

```lean
theorem polynomialBaseChange_obj_hom (X : polynomialSite A B) :
    ((polynomialBaseChange b).obj X).unop.obj.hom =
      CommAlgCat.ofHom (baseChangeAugmentation b X.unop.obj)
```

**`CommAlgCat.polynomialBaseChange_map_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialAlgebraSiteBaseChange.lean#L193). The attribute's comment: “polynomial-site base change on morphisms”.

> The underlying algebra map of the image of `f` under `polynomialBaseChange b` is
> `baseChangeMap f`.

```lean
theorem polynomialBaseChange_map_left {X Y : polynomialSite A B} (f : X ⟶ Y) :
    ((polynomialBaseChange b).map f).unop.hom.left =
      CommAlgCat.ofHom (baseChangeMap f.unop.hom)
```

**`CommAlgCat.boundedPolynomialBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialSiteBaseChangeShriek.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialSiteBaseChangeShriek.lean#L92). The attribute's comment: “polynomial-site base change, with the section's footnote in force: the functor between the sites restricted to at most κ variables. The unrestricted version is `CommAlgCat.polynomialBaseChange`”.

> The base-change functor of sites `C_{B/A} ⟶ C_{B'/A'}`, between the sites restricted to
> polynomial algebras on at most `κ` variables.

```lean
def boundedPolynomialBaseChange :
    boundedPolynomialSite A B κ ⥤ boundedPolynomialSite A' B' κ
```

## Tag 08QP, a lemma

[Tag 08QP](https://stacks.math.columbia.edu/tag/08QP) in the Stacks Project.

**`CommAlgCat.leftDerivedPointLowerShriekPolynomialBaseChangeNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialSiteBaseChangeShriek.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialSiteBaseChangeShriek.lean#L210). The attribute's comment: “a GENERALIZATION of the lemma: the identification `Lπ_!(g^{-1}ℱ') = Lπ'_!(ℱ')` under the weaker hypothesis that the base change `A' ⊗_A P_• ⟶ B'` of the chosen resolution is again a resolution, which is what the source's proof derives from `B ⊗_A^L A' = B'`. The source's own statement is `CommAlgCat.leftDerivedPointLowerShriekPolynomialBaseChangeNatIsoOfTorIndependent`, proved from this one. Both are read at the small model of the footnote-restricted site `C_{B/A}` and through the sections at the point”.

> Let
> ```
> A  --→  A'
> |       |
> B  --→  B'
> ```
> be a commutative square of rings, let `C_{B/A}` and `C_{B'/A'}` be the sites of polynomial
> algebras augmented to `B`, resp. to `B'`, of Tag 08PR, and let `g` be the morphism of topoi
> induced by the base-change functor of Tag 08QN, so that `g^{-1}` is restriction along it. Let
> `ε : P_• ⟶ B` be a resolution of `B` over `A` whose terms are polynomial algebras on at most
> `κ` variables, and assume that the base-changed augmentation `A' ⊗_A P_• ⟶ B'` is again a
> resolution of `B'` over `A'`. Then
>
> `Lπ_!(g^{-1}ℱ') = Lπ'_!(ℱ')`
>
> in every degree `n` and naturally in the abelian sheaf `ℱ'` on `C_{B'/A'}`, read through the
> sections at the point. Both sites are read at the small model of their restriction to at most `κ`
> variables.

```lean
def leftDerivedPointLowerShriekPolynomialBaseChangeNatIso
    (hε : SSet.trivialKanFibrations (Functor.whiskerRight ε (forget (CommAlgCat.{u} A))))
    (hres : IsResolution A' (B' : Type u)
      (simplicialBaseChange b ε) (augmentationBaseChange b ε))
    (n : ℕ) :
    (smallPolynomialBaseChange b κ).sheafPushforwardContinuous AddCommGrpCat.{u}
          (GrothendieckTopology.trivial (smallBoundedPolynomialSite A B κ))
          (GrothendieckTopology.trivial (smallBoundedPolynomialSite A' B' κ)) ⋙
        (Stacks.ChaoticSite.abelianPointLowerShriek
            (smallBoundedPolynomialSite A B κ)).leftDerived n ⋙
          Stacks.ChaoticSite.pointSections AddCommGrpCat.{u} ≅
      (Stacks.ChaoticSite.abelianPointLowerShriek
          (smallBoundedPolynomialSite A' B' κ)).leftDerived n ⋙
        Stacks.ChaoticSite.pointSections AddCommGrpCat.{u}
```

**`CommAlgCat.leftDerivedPointLowerShriekPolynomialBaseChangeNatIsoOfTorIndependent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/PolynomialSiteBaseChangeShriek.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/PolynomialSiteBaseChangeShriek.lean#L254). The attribute's comment: “the lemma as stated: the identification `Lπ_!(g^{-1}ℱ') = Lπ'_!(ℱ')` from the source's own hypothesis that the square induce a quasi-isomorphism `B ⊗_A^L A' = B'`, written out as vanishing of the positive `Tor_i^A(A', B)` together with bijectivity of `A' ⊗_A B → B'`. Read at the small model of the footnote-restricted site `C_{B/A}` and through the sections at the point; the generalization assuming only that the base-changed augmentation is a resolution is `CommAlgCat.leftDerivedPointLowerShriekPolynomialBaseChangeNatIso`”.

> Let
> ```
> A  --→  A'
> |       |
> B  --→  B'
> ```
> be a commutative square of rings which induces a quasi-isomorphism `B ⊗_A^L A' = B'` — that is,
> `Tor_i^A(A', B) = 0` for `i > 0` and the canonical map `A' ⊗_A B → B'` is bijective. Let
> `C_{B/A}` and `C_{B'/A'}` be the sites of polynomial algebras augmented to `B`, resp. to `B'`, of
> Tag 08PR, and let `g` be the morphism of topoi induced by the base-change functor of Tag 08QN, so
> that `g^{-1}` is restriction along it. Then
>
> `Lπ_!(g^{-1}ℱ') = Lπ'_!(ℱ')`
>
> in every degree `n` and naturally in the abelian sheaf `ℱ'` on `C_{B'/A'}`, read through the
> sections at the point. Both sites are read at the small model of their restriction to at most `κ`
> variables, for any `κ` bounding the variables of a chosen resolution `ε : P_• ⟶ B` of `B` over
> `A`.

```lean
def leftDerivedPointLowerShriekPolynomialBaseChangeNatIsoOfTorIndependent
    (hres : IsResolution A (B : Type u) P ε)
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective (baseChangeUnit b))
    (n : ℕ) :
    (smallPolynomialBaseChange b κ).sheafPushforwardContinuous AddCommGrpCat.{u}
          (GrothendieckTopology.trivial (smallBoundedPolynomialSite A B κ))
          (GrothendieckTopology.trivial (smallBoundedPolynomialSite A' B' κ)) ⋙
        (Stacks.ChaoticSite.abelianPointLowerShriek
            (smallBoundedPolynomialSite A B κ)).leftDerived n ⋙
          Stacks.ChaoticSite.pointSections AddCommGrpCat.{u} ≅
      (Stacks.ChaoticSite.abelianPointLowerShriek
          (smallBoundedPolynomialSite A' B' κ)).leftDerived n ⋙
        Stacks.ChaoticSite.pointSections AddCommGrpCat.{u}
```

## Tag 08QQ, a lemma

[Tag 08QQ](https://stacks.math.columbia.edu/tag/08QQ) in the Stacks Project.

**`CommAlgCat.cotangentExtendScalarsComplexMap_eq_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeComplexCounit.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeComplexCounit.lean#L267). The attribute's comment: “the arrow of the lemma is the functoriality map of Tag 08PN: the adjoint map out of extension of scalars is extension of scalars of the B-linear map of Tag 08PN followed by the counit, as an equality of maps of cotangent complexes”.

> **The two shapes of the functoriality map agree, on the cotangent complexes.** The adjoint
> map `L_{B/A} ⊗_B B' ⟶ L_{B'/A'}` of [Stacks, Tag 08QQ] is extension of scalars along `B → B'` of
> the `B`-linear map `L_{B/A} ⟶ L_{B'/A'}` of [Stacks, Tag 08PN], followed by the counit
> `B' ⊗_B L_{B'/A'} ⟶ L_{B'/A'}`.
>
> This is `CommAlgCat.cotangentExtendScalarsMooreMap_eq_counit` transported through the reindexing
> which places simplicial degree `n` in cohomological degree `-n`, by
> `ModuleCat.extendMap_comp_extendRestrictScalarsAdjCounitComplex`.

```lean
theorem cotangentExtendScalarsComplexMap_eq_counit :
    cotangentExtendScalarsComplexMap b =
      ((ModuleCat.extendScalars b.toRingHom).mapHomologicalComplex (ComplexShape.up ℤ)).map
          (squareCotangentComplexMap.{u, u, u} (algebraSquareOfAlgHom b)) ≫
        ModuleCat.extendRestrictScalarsAdjCounitComplex b.toRingHom (ComplexShape.up ℤ)
          (cotangentComplex.{u, u} A' B')
```

**`CommAlgCat.overDifferentialsBaseChangeNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIso.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIso.lean#L250). The attribute's comment: “the step of the proof the source performs by inspection: extension of scalars along B → B' of i^*Ω_{𝒪/A} is the restriction of i^*Ω_{𝒪'/A'} along the base-change functor of sites of Tag 08QN”.

> **`i^*Ω_{𝒪/A} ⊗_B B' = g^{-1}(i^*Ω_{𝒪'/A'})`, the step the source performs by inspection.**
> Extension of scalars along `B → B'` of the `B`-module of differentials `B ⊗_P Ω[P⁄A]` is the
> `B'`-module of differentials of the base-changed algebra `A' ⊗_A P`, naturally in the `A`-algebra
> `P` augmented to `B`.

```lean
def overDifferentialsBaseChangeNatIso :
    overDifferentialsFunctor (A := A) (B := B) ⋙ ModuleCat.extendScalars b.toRingHom ≅
      baseChangeOver b ⋙ overDifferentialsFunctor (A := A') (B := B')
```

**`CommAlgCat.quasiIso_cotangentExtendScalarsMooreMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIso.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIso.lean#L564). The attribute's comment: “on the alternating-face-map complexes, under ONE carried hypothesis: Remark 08QI as CommAlgCat.CotangentComputedByEveryResolution, which Tag 08QI discharges; the source's own hypothesis and its conclusion on THE functoriality map of Tag 08PN are kept”.

> **Stacks 08QQ, on the alternating-face-map complexes.** If the commutative square `A → B`,
> `A → A'`, `B → B'`, `A' → B'` induces a quasi-isomorphism `B ⊗_A^L A' = B'` — that is, `A'` and
> `B` are Tor-independent over `A` and `A' ⊗_A B → B'` is bijective — then the functoriality map
> `L_{B/A} ⊗_B B' ⟶ L_{B'/A'}` of Tag 08PN is a quasi-isomorphism.
>
> The hypothesis `B ⊗_A^L A' = B'` makes the base change `A' ⊗_A P_• ⟶ B'` of the standard
> resolution a resolution of `B'` over `A'`, and the functoriality map is the map induced by
> `A' ⊗_A P_• ⟶ P'_•` read through the identification of `L_{B/A} ⊗_B B'` with the complex of
> `A' ⊗_A P_•`; Remark 08QI, carried as `CommAlgCat.CotangentComputedByEveryResolution`, inverts
> that map.

```lean
theorem quasiIso_cotangentExtendScalarsMooreMap
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b))
    (hQI : CotangentComputedByEveryResolution A' B') :
    QuasiIso (cotangentExtendScalarsMooreMap b)
```

**`CommAlgCat.quasiIso_cotangentExtendScalarsComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIso.lean, line 607](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIso.lean#L607). The attribute's comment: “on the cotangent complexes, under ONE carried hypothesis: Remark 08QI as CommAlgCat.CotangentComputedByEveryResolution, which Tag 08QI discharges; the source's own hypothesis B ⊗_A^L A' = B' and its conclusion on THE functoriality map of 08PN are kept”.

> **Stacks 08QQ.** If the commutative square `A → B`, `A → A'`, `B → B'`, `A' → B'` induces a
> quasi-isomorphism `B ⊗_A^L A' = B'`, then the functoriality map
> `L_{B/A} ⊗_B B' ⟶ L_{B'/A'}` of Tag 08PN is a quasi-isomorphism of cotangent complexes. The terms
> of `L_{B/A}` are free `B`-modules, so the left-hand side computes `L_{B/A} ⊗_B^L B'`.

```lean
theorem quasiIso_cotangentExtendScalarsComplexMap
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b))
    (hQI : CotangentComputedByEveryResolution A' B') :
    QuasiIso (cotangentExtendScalarsComplexMap b)
```

**`CommAlgCat.isIso_Q_map_cotangentExtendScalarsComplexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIso.lean, line 628](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIso.lean#L628). The attribute's comment: “the lemma as an isomorphism in D(B'): the image of the functoriality map of Tag 08PN under the localization D(B') is invertible. Carries the same single hypothesis, Remark 08QI as CommAlgCat.CotangentComputedByEveryResolution, discharged by Tag 08QI”.

> **Stacks 08QQ in the derived category.** Under the hypothesis `B ⊗_A^L A' = B'` the
> functoriality map becomes an isomorphism `L_{B/A} ⊗_B^L B' ⟶ L_{B'/A'}` in `D(B')`.

```lean
theorem isIso_Q_map_cotangentExtendScalarsComplexMap
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b))
    (hQI : CotangentComputedByEveryResolution A' B') :
    IsIso (DerivedCategory.Q.map (cotangentExtendScalarsComplexMap b))
```

**`CommAlgCat.cotangentBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIso.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIso.lean#L643). The attribute's comment: “the base-change isomorphism itself, as data: an isomorphism in D(B') whose underlying morphism is the functoriality map of Tag 08PN. Carries the same single hypothesis, Remark 08QI as CommAlgCat.CotangentComputedByEveryResolution, discharged by Tag 08QI”.

> **Stacks 08QQ, the base-change isomorphism.** The isomorphism
> `L_{B/A} ⊗_B^L B' ≅ L_{B'/A'}` in `D(B')` whose underlying morphism is the functoriality map of
> the square.

```lean
def cotangentBaseChangeIso
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b))
    (hQI : CotangentComputedByEveryResolution A' B') :
    DerivedCategory.Q.obj
        (((ModuleCat.extendScalars b.toRingHom).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj (cotangentComplex.{u, u} A B)) ≅
      DerivedCategory.Q.obj (cotangentComplex.{u, u} A' B')
```

**`CommAlgCat.quasiIso_cotangentExtendScalarsMooreMap_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean#L57). The attribute's comment: “on the alternating-face-map complexes: under the source's own hypothesis and with no other, the functoriality map of Tag 08PN is a quasi-isomorphism”.

> **Stacks 08QQ on the Moore complexes.** If the square induces `B ⊗_A^L A' = B'`, the
> functoriality map of Tag 08PN is a quasi-isomorphism of the alternating face map complexes.
> This is `CommAlgCat.quasiIso_cotangentExtendScalarsMooreMap` with Remark 08QI supplied by
> `CommAlgCat.cotangentComputedByEveryResolution`.

```lean
theorem quasiIso_cotangentExtendScalarsMooreMap_unconditional
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b)) :
    QuasiIso (cotangentExtendScalarsMooreMap b)
```

**`CommAlgCat.quasiIso_cotangentExtendScalarsComplexMap_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean#L70). The attribute's comment: “on the cotangent complexes, under the source's own hypothesis B ⊗_A^L A' = B' and no other: THE functoriality map of Tag 08PN is a quasi-isomorphism”.

> **Stacks 08QQ.** If the commutative square `A → B`, `A → A'`, `B → B'`, `A' → B'` induces a
> quasi-isomorphism `B ⊗_A^L A' = B'`, then the functoriality map `L_{B/A} ⊗_B B' ⟶ L_{B'/A'}` of
> Tag 08PN is a quasi-isomorphism of cotangent complexes. This is
> `CommAlgCat.quasiIso_cotangentExtendScalarsComplexMap` with Remark 08QI supplied by
> `CommAlgCat.cotangentComputedByEveryResolution`.

```lean
theorem quasiIso_cotangentExtendScalarsComplexMap_unconditional
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b)) :
    QuasiIso (cotangentExtendScalarsComplexMap b)
```

**`CommAlgCat.isIso_Q_map_cotangentExtendScalarsComplexMap_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean#L82). The attribute's comment: “the lemma as an isomorphism in D(B'): the image of the functoriality map of Tag 08PN under the localization D(B') is invertible, under the source's own hypothesis and no other”.

> **Stacks 08QQ in the derived category.** Under the hypothesis `B ⊗_A^L A' = B'` the
> functoriality map becomes an isomorphism `L_{B/A} ⊗_B^L B' ⟶ L_{B'/A'}` in `D(B')`.

```lean
theorem isIso_Q_map_cotangentExtendScalarsComplexMap_unconditional
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b)) :
    IsIso (DerivedCategory.Q.map (cotangentExtendScalarsComplexMap b))
```

**`CommAlgCat.cotangentBaseChangeIsoUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/BaseChangeQuasiIsoUnconditional.lean#L95). The attribute's comment: “the base-change isomorphism itself, as data: an isomorphism in D(B') whose underlying morphism is the functoriality map of Tag 08PN, under the source's own hypothesis and no other”.

> **Stacks 08QQ, the base-change isomorphism.** The isomorphism
> `L_{B/A} ⊗_B^L B' ≅ L_{B'/A'}` in `D(B')` whose underlying morphism is the functoriality map of
> the square.

```lean
def cotangentBaseChangeIsoUnconditional
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hpush : Function.Bijective (baseChangeUnit b)) :
    DerivedCategory.Q.obj
        (((ModuleCat.extendScalars b.toRingHom).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj (cotangentComplex.{u, u} A B)) ≅
      DerivedCategory.Q.obj (cotangentComplex.{u, u} A' B')
```

**`CommAlgCat.derivedCotangentComplexBaseChangeFunctorialityIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/DerivedPushoutBaseChange.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/DerivedPushoutBaseChange.lean#L395). The attribute's comment: “the lemma, with the arrow the source names: under the source's own hypothesis that the square induce a quasi-isomorphism B ⊗_A^L A' = B' — written out as vanishing of the positive Tor_i^A(A', B) together with bijectivity of A' ⊗_A B → B' — THE functoriality map of Tag 08PN induces an isomorphism L_{B/A} ⊗^L_B B' ≅ L_{B'/A'} in D(B'), the derived tensor product being the chapter's total derived extension-of-scalars functor. That the underlying morphism is that functoriality map is CommAlgCat.derivedCotangentComplexBaseChangeFunctorialityIso_hom below. No hypothesis beyond the source's is carried: Remark 08QI is proved, not assumed (CommAlgCat.cotangentComputedByEveryResolution)”.

> **[Stacks, Tag 08QQ].** Let
> ```
> A  --→  A'
> |       |
> B  --→  B'
> ```
> be a commutative square of rings which induces a quasi-isomorphism `B ⊗_A^𝐋 A' = B'` — that is,
> `Tor_i^A(A', B) = 0` for `i > 0` and the canonical map `A' ⊗_A B → B'` is bijective. Then the
> functoriality map induces an isomorphism
>
> `L_{B/A} ⊗^𝐋_B B' ⟶ L_{B'/A'}`
>
> in `D(B')`, where `- ⊗^𝐋_B B'` is the total derived extension-of-scalars functor of
> `StacksFrontier.Homology.Tor.DerivedExtensionScalars`.
>
> The arrow is the source's. The cotangent complex is a bounded above complex of free modules, so
> `L_{B/A} ⊗^𝐋_B B'` is the degreewise base change `B' ⊗_B L_{B/A}`
> (`CommAlgCat.derivedExtensionScalarsCotangentComplexIso`), and on that the functoriality map of
> [Stacks, Tag 08PN] after extension of scalars is
> `CommAlgCat.cotangentExtendScalarsComplexMap`, a quasi-isomorphism by
> `CommAlgCat.quasiIso_cotangentExtendScalarsComplexMap`. That the isomorphism built here is
> induced by the functoriality map and not merely some isomorphism between the two objects is
> `CommAlgCat.derivedCotangentComplexBaseChangeFunctorialityIso_hom`.

```lean
def derivedCotangentComplexBaseChangeFunctorialityIso
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective (baseChangeUnit b)) :
    (CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsGeneral
          b.toRingHom).functor.obj (DerivedCategory.Q.obj (cotangentComplex.{u, u} A B)) ≅
      DerivedCategory.Q.obj (cotangentComplex.{u, u} A' B')
```

**`CommAlgCat.derivedCotangentComplexBaseChangeFunctorialityIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/DerivedPushoutBaseChange.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/DerivedPushoutBaseChange.lean#L412). The attribute's comment: “that the isomorphism is induced by THE functoriality map of Tag 08PN: its underlying morphism in D(B') is the image of the chain-level map CommAlgCat.cotangentExtendScalarsComplexMap, read after the canonical identification of L_{B/A} ⊗^L_B B' with the degreewise base change”.

> **The isomorphism of Tag 08QQ is the one the functoriality map induces.** Its underlying
> morphism is the image in `D(B')` of `CommAlgCat.cotangentExtendScalarsComplexMap` — the
> `B'`-linear adjoint of the `B`-linear map `L_{B/A} ⟶ L_{B'/A'}` of [Stacks, Tag 08PN] — read
> after the identification of `L_{B/A} ⊗^𝐋_B B'` with the degreewise base change `B' ⊗_B L_{B/A}`.

```lean
theorem derivedCotangentComplexBaseChangeFunctorialityIso_hom
    (hTor : RingTheory.TorIndependence.TorIndependent A A' (B : Type u))
    (hφ : Function.Bijective (baseChangeUnit b)) :
    (derivedCotangentComplexBaseChangeFunctorialityIso b hTor hφ).hom =
      (derivedExtensionScalarsCotangentComplexIso b).hom ≫
        DerivedCategory.Q.map (cotangentExtendScalarsComplexMap b)
```

## Tag 08SB, a remark

[Tag 08SB](https://stacks.math.columbia.edu/tag/08SB) in the Stacks Project.

**`CommAlgCat.nonempty_homotopy_squareCotangentComplexMap_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SquareFactoringThroughBase.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SquareFactoringThroughBase.lean#L180). The attribute's comment: “the conclusion of the remark: the induced map on cotangent complexes is homotopic to zero. The claim of the remark itself, that the functoriality map of standard resolutions is homotopic to the composition through `κ`, is `CommAlgCat.eqvGen_homotopy_squareResolutionRingMap_baseMap` of `StacksFrontier.Cotangent.SquareResolutionBaseHomotopy`; the proof here does not pass through it, factoring the square through the identity of `A'` instead.”.

> **Stacks Project, Tag 08SB.** Let `A → A'`, `B → B'` be a commutative square of ring maps
> compatible with the algebra structures `A → B` and `A' → B'`. If there is a ring map
> `κ : B → A'` which agrees with `A → A'` on the image of `A` and which recovers `B → B'` after
> `A' → B'`, then the induced map of cotangent complexes `L_{B/A} → L_{B'/A'}` is homotopic to
> zero.

```lean
public theorem nonempty_homotopy_squareCotangentComplexMap_zero
    (sq : AlgebraSquare.{u, v, u} A A' B B') (κ : B →+* A')
    (hκ : ∀ a : A, κ (algebraMap A B a) = sq.base a)
    (hκ' : ∀ b : B, algebraMap A' B' (κ b) = sq.map b) :
    Nonempty (Homotopy (squareCotangentComplexMap.{u, v, u} sq) 0)
```

**`CommAlgCat.cotangentTermDifferential_squareResolutionRingBaseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SquareResolutionBaseHomotopy.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SquareResolutionBaseHomotopy.lean#L295). The attribute's comment: “the remark's observation that the composition through `κ` induces the zero map on differentials, read degreewise on the pure differentials `1 ⊗ d p` which generate the terms of the cotangent complex.”.

> The composition `P_• → B → A' → P'_•` lands in the image of `A'`, so it kills differentials:
> the pure differential `1 ⊗ d` of each of its values vanishes. This is the step by which the
> source passes from the homotopy below to the vanishing, up to homotopy, of the induced map on
> cotangent complexes.

```lean
public theorem cotangentTermDifferential_squareResolutionRingBaseMap
    (sq : AlgebraSquare.{u, v, u} A A' B B') (κ : B →+* A') (n : SimplexCategoryᵒᵖ)
    (p : (standardResolution.{u, max u v} A B).left.obj n) :
    cotangentTermDifferential.{u, max u v} A' B' n
      ((squareResolutionRingBaseMap.{u, v} sq κ).app n p) = 0
```

**`CommAlgCat.eqvGen_homotopy_squareResolutionRingMap_baseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SquareResolutionBaseHomotopy.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SquareResolutionBaseHomotopy.lean#L376). The attribute's comment: “the claim of the remark: the functoriality map of standard resolutions is homotopic to the composition through `κ`. The consequence drawn from it, that the induced map of cotangent complexes is homotopic to zero, is `CommAlgCat.nonempty_homotopy_squareCotangentComplexMap_zero`.”.

> **Stacks Project, Tag 08SB.** Let `A → A'`, `B → B'` be a commutative square of ring maps
> compatible with the algebra structures `A → B` and `A' → B'`, and let `κ : B → A'` be a ring map
> which agrees with `A → A'` on the image of `A` and which recovers `B → B'` after `A' → B'`. Then
> the functoriality map `P_• → P'_•` of the two standard resolutions is homotopic, as a map of
> simplicial commutative rings, to the composition `P_• → B → A' → P'_•`.

```lean
public theorem eqvGen_homotopy_squareResolutionRingMap_baseMap
    (sq : AlgebraSquare.{u, v, u} A A' B B') (κ : B →+* A')
    (hκ : ∀ a : A, κ (algebraMap A B a) = sq.base a)
    (hκ' : ∀ b : B, algebraMap A' B' (κ b) = sq.map b) :
    Relation.EqvGen
      (fun f g : resolutionRing.{u, v} A B ⟶ resolutionRing.{u, v} A' B' =>
        Nonempty (SimplicialObject.Homotopy f g))
      (squareResolutionRingMap.{u, v} sq) (squareResolutionRingBaseMap.{u, v} sq κ)
```

## Tag 08SC, a lemma

[Tag 08SC](https://stacks.math.columbia.edu/tag/08SC) in the Stacks Project.

**`CommAlgCat.cotangentComplexProductMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ProductDecomposition.lean, line 460](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ProductDecomposition.lean#L460). The attribute's comment: “the canonical map `L_{B×C/A} → L_{B/A} ⊕ L_{C/A}` of the lemma, at chain level: the pair of the functoriality maps of the two projections, whose `DerivedCategory.Q` is the map in `D(B × C)` of the statement. That this map is an isomorphism in `D(B × C)` is `CommAlgCat.isIso_Q_map_cotangentComplexProductMap` of `StacksFrontier/Cotangent/ProductDecompositionBase.lean`, over an arbitrary base”.

> **The canonical map of [Stacks, Tag 08SC].** For ring maps `A → B` and `A → C`, the pair of
> the functoriality maps of the two projections `B × C → B` and `B × C → C` is a map of complexes of
> `B × C`-modules
>
> `L_{B×C/A} → L_{B/A} ⊕ L_{C/A}`,
>
> the two summands being read over `B × C` along the projections. Tag 08SC asserts that
> `DerivedCategory.Q` of this map is an isomorphism in `D(B × C)`; that is
> `CommAlgCat.isIso_Q_map_cotangentComplexProductMap` of
> `StacksFrontier/Cotangent/ProductDecompositionBase.lean`.

```lean
public noncomputable def cotangentComplexProductMap :
    cotangentComplex.{u, v} A (CommAlgCat.of A (B × C)) ⟶
      (((ModuleCat.restrictScalars (productFstSquare.{u, v} A B C).map).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj (cotangentComplex.{u, v} A B)) ⊞
        (((ModuleCat.restrictScalars (productSndSquare.{u, v} A B C).map).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj (cotangentComplex.{u, v} A C))
```

**`CommAlgCat.isIso_Q_map_cotangentComplexProductMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/ProductDecompositionBase.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/ProductDecompositionBase.lean#L179). The attribute's comment: “the lemma: for ring maps `A → B` and `A → C` the canonical map `L_{B×C/A} → L_{B/A} ⊕ L_{C/A}` -- the pair of the functoriality maps of the two projections, `CommAlgCat.cotangentComplexProductMap` -- is an isomorphism in `D(B × C)`, over an arbitrary base `A`. The chain-level form, that the map is a quasi-isomorphism, is `CommAlgCat.quasiIso_cotangentComplexProductMap`”.

> **Stacks Project, Tag 08SC.** Let `A → B` and `A → C` be ring maps. Then the canonical map
>
> `L_{B×C/A} ⟶ L_{B/A} ⊕ L_{C/A}`
>
> is an isomorphism in `D(B × C)`.
>
> The map is `CommAlgCat.cotangentComplexProductMap`, the pair of the functoriality maps of
> [Stacks, Tag 08PN] for the two projections; it is a quasi-isomorphism by
> `CommAlgCat.quasiIso_cotangentComplexProductMap`, and the localization `DerivedCategory.Q`
> inverts exactly the quasi-isomorphisms.

```lean
theorem isIso_Q_map_cotangentComplexProductMap (A : Type u) [CommRing A]
    (B C : CommAlgCat.{u} A) :
    IsIso (DerivedCategory.Q.map (cotangentComplexProductMap.{u, u} A B C))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.6, Tag 08QL](https://stacks.math.columbia.edu/tag/08QL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
