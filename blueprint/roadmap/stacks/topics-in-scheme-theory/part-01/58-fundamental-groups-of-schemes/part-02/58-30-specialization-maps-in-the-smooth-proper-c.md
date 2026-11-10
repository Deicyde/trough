---
declaration: section
origin: cited
lean: AlgebraicGeometry.surjective_specializationMap_of_isProper_of_flat, AlgebraicGeometry.bijective_isSpecializationMap_of_ringChar_zero, AlgebraicGeometry.surjective_and_exists_continuousMulEquiv_primeToP
statement: formalized
proof: formalized
---

# 58.30 Specialization maps in the smooth proper case

Section 58.30 of the Stacks Project, [Tag 0BUQ](https://stacks.math.columbia.edu/tag/0BUQ). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C0P, a lemma

[Tag 0C0P](https://stacks.math.columbia.edu/tag/0C0P) in the Stacks Project.

**`AlgebraicGeometry.surjective_specializationMap_of_isProper_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationSurjective.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationSurjective.lean#L542). The attribute's comment: “the whole statement, under the source's hypotheses only.”. References: SGA 1 X (2.4), “more general”; SGA 1 X (3.8), “more general”.

> **Stacks Project, Tag 0C0P.** Let `f : X ⟶ S` be a flat proper morphism with geometrically
> connected fibres and let `s' ⇝ s` be a specialization of points of `S`, realized as in the
> construction of the specialization map: `A` is a strict henselization of `𝒪_{S,s}` relative to a
> separable closure of `κ(s)`, and the two geometric points are factored through `Spec A`, the
> special one over the closed point. Let
>
> ```
> sp : π₁(X_{s̄'}) ⟶ π₁(X_{s̄})
> ```
>
> be the resulting specialization map, that is, a continuous homomorphism satisfying the equation
> defining it against the canonical maps to `π₁(X_A)`. If the fibre `X_s` is geometrically reduced,
> then `sp` is surjective.
>
> No finiteness hypothesis beyond properness is needed. Every specialization map is isomorphic to a
> specialization map over a strictly henselian valuation ring `R`, for the base change
> `X_R ⟶ Spec R` along a morphism `Spec R ⟶ S` carrying the generic point of `Spec R` to the image
> of `s̄'` and the closed point to the image of `s̄`. That base change is flat and proper with
> geometrically connected fibres, its closed fibre is geometrically reduced because `X_s` is, and
> over a valuation ring a flat morphism of finite type is automatically of finite presentation. So
> the geometrically reduced fibre locus of `X_R ⟶ Spec R` is open and contains the closed point of
> the local scheme `Spec R`, hence is all of it; the homotopy sequence of `X_R ⟶ Spec R` together
> with the triviality of `π₁(Spec R)` makes the specialization map over `R` surjective, and
> surjectivity transports back to `sp`.
>
> `AlgebraicGeometry.surjective_specializationMap_of_properFlat` is the same conclusion for a
> morphism which is moreover assumed to be of finite presentation.

```lean
theorem surjective_specializationMap_of_isProper_of_flat {X S : Scheme.{u}} (f : X ⟶ S)
    [IsProper f] [Flat f] [GeometricallyConnected f] (s' s : GeometricPoint S)
    (hred : GeometricallyReduced
      (f.fiberToSpecResidueField (s.hom (closedPoint s.residueField))))
    (A : Type u) [CommRing A] [IsLocalRing A]
    [Algebra (S.presheaf.stalk (s.hom (closedPoint s.residueField))) A]
    (hA : Stacks.StrictHenselization.IsStrictHenselization
      (S.presheaf.stalk (s.hom (closedPoint s.residueField)))
      (SeparableClosure
        (maximalIdeal (S.presheaf.stalk (s.hom (closedPoint s.residueField)))).ResidueField) A)
    (p' : s'.source ⟶ Spec (.of A))
    (hp' : p' ≫ specStalkAlgebraHom S (s.hom (closedPoint s.residueField)) A = s'.hom)
    (p : s.source ⟶ Spec (.of A))
    (hp : p ≫ specStalkAlgebraHom S (s.hom (closedPoint s.residueField)) A = s.hom)
    (hclosed : p (closedPoint s.residueField) = closedPoint A)
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x) :
    letI : ConnectedSpace
        ↥(pullback f (specStalkAlgebraHom S (s.hom (closedPoint s.residueField)) A)) :=
      connectedSpace_pullback_spec_of_isProper f A _
    ∀ t : finiteEtaleFiberFunctor (x'.map (fiberOverGeometricPointMap f s' _ p' hp')) ≅
        finiteEtaleFiberFunctor (x.map (fiberOverGeometricPointMap f s _ p hp)),
      (∀ γ, etaleFundamentalGroupMap (fiberOverGeometricPointMap f s _ p hp) x (sp γ)
          = etaleFundamentalGroupMulEquiv t
            (etaleFundamentalGroupMap (fiberOverGeometricPointMap f s' _ p' hp') x' γ)) →
        Function.Surjective sp
```

## Tag 0C0Q, a proposition

[Tag 0C0Q](https://stacks.math.columbia.edu/tag/0C0Q) in the Stacks Project.

**`AlgebraicGeometry.bijective_isSpecializationMap_of_ringChar_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationInjective/GaloisGenericFibreDescent.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationInjective/GaloisGenericFibreDescent.lean#L723). The attribute's comment: “the whole statement, under the source's hypotheses only: `f` smooth and proper with geometrically connected fibres (`IsProper f`, `Smooth f`, `GeometricallyConnected f`), a specialization of points of `S` realized by a specialization map `sp` (`hsp`), and `κ(s)` of characteristic zero (`hchar`). The conclusion `Function.Bijective sp` is the source's conclusion that `sp` is an isomorphism: `sp` is a continuous homomorphism of profinite groups, so bijectivity is invertibility. Both halves are proved -- surjectivity through Tag 0C0P and injectivity through the descent of the Galois covers of a geometric generic fibre over a strictly henselian discrete valuation ring of residue characteristic zero.”. References: SGA 1 X (2.5), “more general”; SGA 1 X (3.8), “special case”; SGA 1 X (3.9).

> **[Stacks, Tag 0C0Q].** Let `f : X ⟶ S` be a smooth proper morphism with geometrically
> connected fibres, let `s' ⇝ s` be a specialization of points of `S` realized by a specialization
> map `sp : π₁(X_{s̄'}) ⟶ π₁(X_{s̄})`, and suppose the residue characteristic of `s` is zero. Then
> `sp` is bijective, i.e. an isomorphism of topological groups.
>
> Surjectivity is [Stacks, Tag 0C0P]. Injectivity is reduced, by
> `AlgebraicGeometry.bijective_isSpecializationMap_of_ringChar_zero_of_forall_essImage_isGalois`, to
> the descent of the Galois covers of a geometric generic fibre over a strictly henselian discrete
> valuation ring of residue characteristic zero, which is
> `AlgebraicGeometry.exists_finiteEtale_model_of_isGalois_geometricGenericFibre`.

```lean
theorem bijective_isSpecializationMap_of_ringChar_zero {X S : Scheme.{u}} (f : X ⟶ S)
    [IsProper f] [Smooth f] [GeometricallyConnected f] (s' s : GeometricPoint S)
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x)
    (hsp : IsSpecializationMap f s' s x' x sp)
    (hchar : ringChar (S.residueField (s.hom default)) = 0) :
    Function.Bijective sp
```

## Tag 0C0R, a theorem

[Tag 0C0R](https://stacks.math.columbia.edu/tag/0C0R) in the Stacks Project.

**`AlgebraicGeometry.surjective_and_exists_continuousMulEquiv_primeToP`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationPrimeToP/GaloisGenericFibrePrimeToP.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationPrimeToP/GaloisGenericFibrePrimeToP.lean#L461). The attribute's comment: “the whole statement, under the source's hypotheses only: `f` smooth and proper with geometrically connected fibres (`IsProper f`, `Smooth f`, `GeometricallyConnected f`), a specialization of points of `S` realized by a specialization map `sp` (`hsp`), and `p` the characteristic of `κ(s)` (`hchar`). Both of the source's conclusions are stated and proved: `sp` is surjective, and the induced map of the maximal prime-to-`p` quotients is an isomorphism of topological groups commuting with the projections, which is the source's isomorphism `π'₁(X_{s̄'}) ≅ π'₁(X_{s̄})`.”. References: SGA 1 X (3.8), “more general”; SGA 1 X (3.9).

> **[Stacks, Tag 0C0R].** Let `f : X ⟶ S` be a smooth proper morphism with geometrically
> connected fibres, let `s' ⇝ s` be a specialization of points of `S` realized by a specialization
> map `sp : π₁(X_{s̄'}) ⟶ π₁(X_{s̄})`, and let `p` be the characteristic of `κ(s)`. Then `sp` is
> surjective and induces an isomorphism `π'₁(X_{s̄'}) ≅ π'₁(X_{s̄})` of the maximal prime-to-`p`
> quotients, commuting with the projections.
>
> Surjectivity is [Stacks, Tag 0C0P]. The isomorphism of the maximal prime-to-`p` quotients is
> reduced by
> `surjective_and_exists_continuousMulEquiv_primeToP_of_forall_isDiscreteValuationRing`
> to the descent of the Galois covers of order prime to `p` of a geometric generic fibre over a
> strictly henselian discrete valuation ring with algebraically closed residue field of
> characteristic `p`, which is
> `AlgebraicGeometry.exists_finiteEtale_model_of_isGalois_geometricGenericFibre_of_not_dvd`.

```lean
theorem surjective_and_exists_continuousMulEquiv_primeToP {X S : Scheme.{u}} (f : X ⟶ S)
    [Smooth f] [IsProper f] [GeometricallyConnected f] (s' s : GeometricPoint S) (p : ℕ)
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x)
    (hsp : IsSpecializationMap f s' s x' x sp)
    (hchar : ringChar (S.residueField (s.hom default)) = p) :
    Function.Surjective sp ∧
      ∃ e : PrimeToP p (EtaleFundamentalGroup (fiberOverGeometricPoint f s') x') ≃ₜ*
          PrimeToP p (EtaleFundamentalGroup (fiberOverGeometricPoint f s) x),
        ∀ g, e (primeToPMk p _ g) = primeToPMk p _ (sp g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.30, Tag 0BUQ](https://stacks.math.columbia.edu/tag/0BUQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
