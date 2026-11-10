---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isTwistedEulerNumericalPolynomial_of_isCoherent, AlgebraicGeometry.Space.hasTwistedEulerPolynomialOfDegreeLE_coherentSchemeTheoreticSupport, AlgebraicGeometry.Space.hasTwistedEulerPolynomialOfDegreeLE_fin_zero, AlgebraicGeometry.Space.exists_twistedEuler_sub_finsum_mul_twistedEuler_topDimensionalComponent, AlgebraicGeometry.Space.intersectionNumber, AlgebraicGeometry.Space.intersectionNumber_eq_coeff, AlgebraicGeometry.Space.selfIntersectionNumber, AlgebraicGeometry.Space.exists_eval_eq_eulerCharacteristic_and_exists_intCast_eq_coeff_one
statement: formalized
proof: formalized
---

# 72.18 Numerical intersections

Section 72.18 of the Stacks Project, [Tag 0DN3](https://stacks.math.columbia.edu/tag/0DN3). 8 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DN4, a lemma

[Tag 0DN4](https://stacks.math.columbia.edu/tag/0DN4) in the Stacks Project.

**`AlgebraicGeometry.Space.isTwistedEulerNumericalPolynomial_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerNumericalPolynomialProper.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerNumericalPolynomialProper.lean#L76). The attribute's comment: “for every closed subspace Z with F = i_*G, G coherent; the scheme-theoretic support is the smallest such Z (Stacks 07U0), and the bound at it is hasTwistedEulerPolynomialOfDegreeLE_coherentSchemeTheoreticSupport”. References: SGA 6 X (2.3.1), “more general”.

> **Stacks 0DN4.**  Let `k` be a field, `X` a proper algebraic space over `k`, `F` a coherent
> `𝒪_X`-module and `L₁, …, L_r` invertible `𝒪_X`-modules.  For every closed subspace `i : Z ⟶ X`
> with `F ≅ i_*𝒢` for a coherent `𝒪_Z`-module `𝒢`, the twisted Euler characteristics
> `χ(X, F ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_r^{⊗ n_r})` are the values at the integral tuples of a rational
> polynomial which is zero or of total degree at most `dim Z`.  Taking `Z` to be the
> scheme-theoretic support of `F` is
> `AlgebraicGeometry.Space.hasTwistedEulerPolynomialOfDegreeLE_coherentSchemeTheoreticSupport`.

```lean
theorem isTwistedEulerNumericalPolynomial_of_isCoherent
    (F : Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    (hF : IsCoherent B (Spec (.of k)) hk X.1 X.2 F)
    (L : Fin r → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O)).property (L j)] :
    @IsTwistedEulerNumericalPolynomial.{u, w} k _ B hk X r f hf F L _
      (isCoherent_twistedModuleUlift_of_isProper.{u, w} k B hk X f hf L F hF)
```

**`AlgebraicGeometry.Space.hasTwistedEulerPolynomialOfDegreeLE_coherentSchemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerNumericalPolynomialProper.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerNumericalPolynomialProper.lean#L101).

> **Stacks 0DN4.**  Let `k` be a field, `X` a proper algebraic space over `k`, `F` a coherent
> `𝒪_X`-module and `L₁, …, L_r` invertible `𝒪_X`-modules.  The map
> `(n₁, …, n_r) ↦ χ(X, F ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_r^{⊗ n_r})` is the restriction to the integral tuples
> of a rational polynomial which is zero or of total degree at most the dimension of the
> scheme-theoretic support of `F`.  It is numerical, its values being integers
> (`AlgebraicGeometry.Space.exists_intCast_eq_eval_of_representsTwistedEuler`), and unique
> (`AlgebraicGeometry.Space.eq_of_representsTwistedEuler`); when the support is empty it is `0`.
>
> `F` is the direct image of a coherent module on its scheme-theoretic support (Stacks 07U0 and
> 07UG), and `AlgebraicGeometry.Space.isTwistedEulerNumericalPolynomial_of_isCoherent` applies.

```lean
theorem hasTwistedEulerPolynomialOfDegreeLE_coherentSchemeTheoreticSupport
    (F : Modules.{u, u} B (Spec (.of k)) hk X.1 X.2) [hF : IsCoherent B (Spec (.of k)) hk X.1 X.2 F]
    (L : Fin r → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O)).property (L j)] :
    @HasTwistedEulerPolynomialOfDegreeLE.{u, w} k _ B hk X r f hf F L _
      (isCoherent_twistedModuleUlift_of_isProper.{u, w} k B hk X f hf L F hF)
      (dimension B (Spec (.of k)) hk
        (closedSubspaceToSpace B (Spec (.of k)) hk X
          (coherentSchemeTheoreticSupport B (Spec (.of k)) hk X F)).1
        (closedSubspaceToSpace B (Spec (.of k)) hk X
          (coherentSchemeTheoreticSupport B (Spec (.of k)) hk X F)).2)
```

**`AlgebraicGeometry.Space.hasTwistedEulerPolynomialOfDegreeLE_fin_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerPolynomial.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerPolynomial.lean#L374). The attribute's comment: “the case r = 0 of no invertible modules: the constant function χ(X, F) is represented by a constant polynomial, of total degree 0, which is at most the dimension of the closed subspace carrying F whenever that subspace has a point. The empty-support case, and every case with invertible modules present, is not proved”.

> **Stacks 0DN4 in the case `r = 0`.**  With no invertible modules to twist by, the function
> on `ℤ ^ 0` is the constant `χ(X, F)`, so it is represented by a constant polynomial, whose total
> degree is `0`; and `0` is at most the dimension of the closed subspace `Z` carrying `F` as soon
> as `Z` has a point, by `AlgebraicGeometry.Space.zero_le_dimension`.  Taking `Z` to be the scheme
> theoretic support of `F` gives the source's statement for `r = 0`.
>
> The point of `Z` is the one hypothesis beyond the source's, and it is the empty-support case
> that it excludes: a space with no points has dimension `⊥`, the bound then forces the
> representing polynomial to be `0`, hence `χ(X, F) = 0`, and that needs an empty scheme theoretic
> support to force `F ≅ 0`, which this library does not provide.  The closed immersion `i`, the
> module `G` and the isomorphism `F ≅ i_*G` are the source's hypotheses, carried so that the
> statement is the one of the tag; the constant polynomial does not use them.

```lean
theorem hasTwistedEulerPolynomialOfDegreeLE_fin_zero
    (Z : AlgebraicSpaces B (Spec (.of k)) hk) (i : Z ⟶ X)
    (_hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (G : Modules.{u, u} B (Spec (.of k)) hk Z.1 Z.2)
    (_hG : IsCoherent B (Spec (.of k)) hk Z.1 Z.2 G)
    (_hF : F ≅ (modulePushforward B (Spec (.of k)) hk i).obj G)
    (z : points B (Spec (.of k)) hk Z.1) :
    HasTwistedEulerPolynomialOfDegreeLE.{u, w} k B hk X f hf F L
      (dimension B (Spec (.of k)) hk Z.1 Z.2)
```

## Tag 0EDE, a lemma

[Tag 0EDE](https://stacks.math.columbia.edu/tag/0EDE) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_twistedEuler_sub_finsum_mul_twistedEuler_topDimensionalComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerTopDimensionalComponents.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedEulerTopDimensionalComponents.lean#L210).

> **Stacks 0EDE.**  Let `X` be proper over a field `k`, `F` a coherent `𝒪_X`-module and
> `L₁, …, L_r` invertible `𝒪_X`-modules.  Let `Z_C` be the reduced closed subspace on an
> irreducible component `C` of `Supp(F)` of dimension `d = dim Supp(F)`, `x̄_C` a geometric generic
> point of `C` and `m_C = length_{𝒪_{X, x̄_C}}(F_{x̄_C})`.  Then
> `χ(X, F ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_r^{⊗ n_r}) - ∑_C m_C χ(Z_C, (L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_r^{⊗ n_r})|_{Z_C})`
> is given by a rational polynomial in `n₁, …, n_r` which is zero or of total degree `< d`.

```lean
theorem exists_twistedEuler_sub_finsum_mul_twistedEuler_topDimensionalComponent
    (F : Modules.{u, u} B (Spec (.of k)) hk X.1 X.2) (hF : IsCoherent B (Spec (.of k)) hk X.1 X.2 F)
    (x : irreducibleComponents (moduleSupportSet B (Spec (.of k)) hk X F) → GeometricPoint B (Spec
        (.of k)) hk X.1)
    (hx : ∀ C, IsGenericPoint (x C).image (Subtype.val '' (C : Set (moduleSupportSet B (Spec
        (.of k)) hk X F)))) :
    have hT : IsClosed (moduleSupportSet B (Spec (.of k)) hk X F) := isClosed_moduleSupportSet B
        (Spec (.of k)) hk X F hF
    have hW : ∀ C : irreducibleComponents (moduleSupportSet B (Spec (.of k)) hk X F),
        IsClosedSubspace B (Spec (.of k)) hk (reducedClosedSubspace B (Spec (.of k)) hk X.1 X.2 _
          (closedSetComponentPoints B (Spec (.of k)) hk (moduleSupportSet B (Spec
              (.of k)) hk X F) hT C).isClosed) := fun C =>
      isClosedSubspace_reducedClosedSubspace B (Spec (.of k)) hk X.1 X.2 _
        (closedSetComponentPoints B (Spec (.of k)) hk (moduleSupportSet B (Spec
            (.of k)) hk X F) hT C).isClosed
    have hfZ : ∀ C : irreducibleComponents (moduleSupportSet B (Spec (.of k)) hk X F),
        IsProper B (Spec (.of k)) hk ((closedSubfunctorι B (Spec (.of k)) hk (hW C)).hom ≫ f) :=
      fun C => isProper_comp B (Spec (.of k)) hk (hW C).1 X.2
        (isAlgebraicSpace_yoneda B (Spec (.of k)) hk (baseObject k B hk)) _ f
        (isProper_of_isClosedImmersion B (Spec (.of k)) hk (hW C).1 X.2 _ (hW C).2) hf
    ∃ P : MvPolynomial (Fin r) ℚ,
      (P = 0 ∨ (P.totalDegree : WithBot ℕ∞) < topologicalKrullDim (moduleSupportSet B (Spec
          (.of k)) hk X F)) ∧
      ∀ n : Fin r → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
        (@eulerCharacteristic.{u, w} k _ B hk X.1 X.2 f hf
          (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2 F L n)
          (isCoherent_twistedModuleUlift_of_isProper.{u, w} k B hk X f hf L F hF n) : ℚ) -
        ∑ᶠ C ∈ {C : irreducibleComponents (moduleSupportSet B (Spec (.of k)) hk X F) |
            topologicalKrullDim (Subtype.val '' (C : Set (moduleSupportSet B (Spec
                (.of k)) hk X F))) = topologicalKrullDim (moduleSupportSet B (Spec
                    (.of k)) hk X F)},
          haveI := fun j => stacksIsInvertible_modulePullback_obj B (Spec (.of k)) hk
            (closedSubfunctorι B (Spec (.of k)) hk (hW C)) (L j)
          ((geometricLength B (Spec (.of k)) hk X (x C) F).toNat : ℚ) *
            (@eulerCharacteristic.{u, w} k _ B hk (closedSubfunctorSpace B (Spec (.of k)) hk
                (hW C)).1
              (closedSubfunctorSpace B (Spec (.of k)) hk (hW C)).2
              ((closedSubfunctorι B (Spec (.of k)) hk (hW C)).hom ≫ f) (hfZ C)
              (twistedModuleUlift.{u, w} B (Spec (.of k)) hk
                (closedSubfunctorSpace B (Spec (.of k)) hk (hW C)).1
                (closedSubfunctorSpace B (Spec (.of k)) hk (hW C)).2
                (SheafOfModules.unit (Stacks.SheafOfModules.Tensor.ringSheaf
                  (smallEtaleRingedSite B (Spec (.of k)) hk
                    (closedSubfunctorSpace B (Spec (.of k)) hk (hW C)).1
                    (closedSubfunctorSpace B (Spec (.of k)) hk (hW C)).2).O))
                (fun j => (modulePullback B (Spec (.of k)) hk
                  (closedSubfunctorι B (Spec (.of k)) hk (hW C))).obj (L j)) n)
              (isCoherent_twistedModuleUlift_of_isProper.{u, w} k B hk
                (closedSubfunctorSpace B (Spec (.of k)) hk (hW C))
                ((closedSubfunctorι B (Spec (.of k)) hk (hW C)).hom ≫ f) (hfZ C) _ _
                (isCoherent_unit_of_isClosedImmersion k B hk X
                  (closedSubfunctorSpace B (Spec (.of k)) hk (hW C)) f hf
                  (closedSubfunctorι B (Spec (.of k)) hk (hW C)) (hW C).2) n) : ℚ)
```

## Tag 0EDF, a definition

[Tag 0EDF](https://stacks.math.columbia.edu/tag/0EDF) in the Stacks Project.

**`AlgebraicGeometry.Space.intersectionNumber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean, line 776](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean#L776). References: SGA 6 X (4.4), “defn, algebraic spaces”.

> **Stacks 0EDF.** The intersection number `(L₁ ⋯ L_d · Z)` of `d` invertible
> `𝒪_X`-modules against a closed subspace `i : Z ⟶ X` of dimension `d` of a proper algebraic
> space `X` over a field `k`: the coefficient of `n₁ ⋯ n_d` in the numerical polynomial
> `χ(X, i_*𝒪_Z ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_d^{⊗ n_d})`, computed as the `d`-fold mixed finite difference
>
> `∑_{T ⊆ {1, …, d}} (-1)^{d - |T|} χ(X, i_*𝒪_Z ⊗ ⨂_{j ∈ T} L_j)`
>
> of that function.  This is an honest integer: only finitely many values of the function are
> used, so neither polynomiality nor a choice of representing polynomial enters.

```lean
def intersectionNumber (d : ℕ) (f : X.1 ⟶ yoneda.obj (baseObject k B hk))
    (hf : IsProper B (Spec (.of k)) hk f) (i : Z ⟶ X)
    (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (_hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)] :
    ℤ
```

**`AlgebraicGeometry.Space.intersectionNumber_eq_coeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean, line 820](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean#L820). The attribute's comment: “the coefficient of n_1 ⋯ n_d”. References: SGA 6 X (4.4), “defn, algebraic spaces”.

> **Stacks 0EDF, the coefficient of `n₁ ⋯ n_d`.**  If a rational polynomial `P` in `d`
> variables of total degree at most `d` takes the Euler characteristics
> `χ(X, i_*𝒪_Z ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_d^{⊗ n_d})` as its values at the integral tuples, then the
> intersection number `(L₁ ⋯ L_d · Z)` is the coefficient of `n₁ ⋯ n_d` in `P`.
>
> This is the source's own description of the intersection number.  The existence of such a `P`,
> which is Stacks 0DN4, is not assumed: the statement is unconditional in `P`, and the proof is
> the monomial computation
> `MvPolynomial.sum_neg_one_pow_mul_eval_indicator_eq_coeff_one`.

```lean
theorem intersectionNumber_eq_coeff (d : ℕ) (f : X.1 ⟶ yoneda.obj (baseObject k B hk))
    (hf : IsProper B (Spec (.of k)) hk f) (i : Z ⟶ X)
    (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)]
    (P : MvPolynomial (Fin d) ℚ)
    (hP : ∀ n : Fin d → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
      ((@eulerCharacteristic.{u, w} k _ B hk X.1 X.2 f hf
        (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
          (structureSheafPushforward B (Spec (.of k)) hk i) L n)
          (isCoherent_twistedModuleUlift_structureSheafPushforward.{u, w}
            k B hk X Z f hf i hi L n) : ℤ) : ℚ))
    (hdeg : P.totalDegree ≤ d) :
    ((intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L : ℤ) : ℚ) =
      P.coeff (Finsupp.equivFunOnFinite.symm fun _ => 1)
```

**`AlgebraicGeometry.Space.selfIntersectionNumber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean, line 891](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean#L891). The attribute's comment: “the self-intersection notation (L^d · Z)”.

> **Stacks 0EDF, the self-intersection notation `(L^d · Z)`.**  The intersection number of a
> single invertible `𝒪_X`-module `L` repeated `d` times against a closed subspace `i : Z ⟶ X` of
> dimension `d`.

```lean
def selfIntersectionNumber (d : ℕ) (f : X.1 ⟶ yoneda.obj (baseObject k B hk))
    (hf : IsProper B (Spec (.of k)) hk f) (i : Z ⟶ X)
    (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d)
    (L : Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property L] :
    ℤ
```

## Tag 0EDG, a lemma

[Tag 0EDG](https://stacks.math.columbia.edu/tag/0EDG) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_eval_eq_eulerCharacteristic_and_exists_intCast_eq_coeff_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberAdditivity.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberAdditivity.lean#L128). References: SGA 6 X (2.3.1), “special case”.

> **Stacks 0EDG.**  In the situation of Definition 0EDF — `X` a proper algebraic space over a
> field `k`, `i : Z ⟶ X` a closed subspace of dimension `d` and `L₁, …, L_d` invertible
> `𝒪_X`-modules — the intersection number `(L₁ ⋯ L_d · Z)` is an integer: the function
> `n ↦ χ(X, i_*𝒪_Z ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_d^{⊗ n_d})` is the restriction to the integral tuples of a
> rational polynomial of total degree at most `d`, and the coefficient of `n₁ ⋯ n_d` in any
> rational polynomial with these values is the cast of an integer.
>
> The first conjunct is Stacks 0DN4,
> `AlgebraicGeometry.Space.exists_representsTwistedEuler_structureSheafPushforward`, and it is
> what makes the second one say something about *the* numerical polynomial of the source: a
> rational polynomial is determined by its values at the integral tuples
> (`MvPolynomial.eq_of_eval_intCast_eq`), so every polynomial with these values is that one, and
> `AlgebraicGeometry.Space.exists_intCast_eq_coeff_one` applies to it, the integer being
> `AlgebraicGeometry.Space.intersectionNumber`.

```lean
theorem exists_eval_eq_eulerCharacteristic_and_exists_intCast_eq_coeff_one (d : ℕ)
    (f : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f)
    (i : Z ⟶ X) (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)] :
    (∃ P : MvPolynomial (Fin d) ℚ, (∀ n : Fin d → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
      ((@eulerCharacteristic.{u, w} k _ B hk X.1 X.2 f hf
        (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
          (structureSheafPushforward B (Spec (.of k)) hk i) L n)
          (isCoherent_twistedModuleUlift_structureSheafPushforward.{u, w}
            k B hk X Z f hf i hi L n) : ℤ) : ℚ)) ∧ P.totalDegree ≤ d) ∧
    ∀ P : MvPolynomial (Fin d) ℚ, (∀ n : Fin d → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
      ((@eulerCharacteristic.{u, w} k _ B hk X.1 X.2 f hf
        (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
          (structureSheafPushforward B (Spec (.of k)) hk i) L n)
          (isCoherent_twistedModuleUlift_structureSheafPushforward.{u, w}
            k B hk X Z f hf i hi L n) : ℤ) : ℚ)) →
      ∃ m : ℤ, P.coeff (Finsupp.equivFunOnFinite.symm fun _ => 1) = (m : ℚ)
```

**`AlgebraicGeometry.Space.exists_intCast_eq_coeff_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean, line 868](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean#L868). The attribute's comment: “granted a representing numerical polynomial, whose existence is Tag 0DN4”.

> **Stacks 0EDG.**  The intersection number `(L₁ ⋯ L_d · Z)` is an integer: the coefficient of
> `n₁ ⋯ n_d` in a rational polynomial of total degree at most `d` taking the Euler characteristics
> `χ(X, i_*𝒪_Z ⊗ L₁^{⊗ n₁} ⊗ ⋯ ⊗ L_d^{⊗ n_d})` as its values at the integral tuples is the cast of
> an integer, namely of `AlgebraicGeometry.Space.intersectionNumber`.
>
> That coefficient is a priori only rational, and integrality is special to it: a numerical
> polynomial such as `n (n - 1) / 2` has coefficients which are not integers, and it is the degree
> bound that makes the coefficient of the squarefree monomial a mixed finite difference of
> finitely many integer values.

```lean
theorem exists_intCast_eq_coeff_one (d : ℕ) (f : X.1 ⟶ yoneda.obj (baseObject k B hk))
    (hf : IsProper B (Spec (.of k)) hk f) (i : Z ⟶ X)
    (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)]
    (P : MvPolynomial (Fin d) ℚ)
    (hP : ∀ n : Fin d → ℤ, MvPolynomial.eval (fun j => (n j : ℚ)) P =
      ((@eulerCharacteristic.{u, w} k _ B hk X.1 X.2 f hf
        (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
          (structureSheafPushforward B (Spec (.of k)) hk i) L n)
          (isCoherent_twistedModuleUlift_structureSheafPushforward.{u, w}
            k B hk X Z f hf i hi L n) : ℤ) : ℚ))
    (hdeg : P.totalDegree ≤ d) :
    ∃ m : ℤ, P.coeff (Finsupp.equivFunOnFinite.symm fun _ => 1) = (m : ℚ)
```

## Tag 0EDH, a lemma

[Tag 0EDH](https://stacks.math.columbia.edu/tag/0EDH) in the Stacks Project.

**`AlgebraicGeometry.Space.intersectionNumber_eq_add_intersectionNumber_of_iso_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberAdditivity.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberAdditivity.lean#L169).

> **Stacks 0EDH.**  In the situation of Definition 0EDF, the intersection number is additive
> in each of its invertible modules: if `L_{i₀} ≅ L_{i₀}' ⊗ L_{i₀}''`, and `L'` and `L''` agree with
> `L` away from `i₀`, then
>
> `(L₁ ⋯ L_{i₀} ⋯ L_d · Z) = (L₁ ⋯ L_{i₀}' ⋯ L_d · Z) + (L₁ ⋯ L_{i₀}'' ⋯ L_d · Z)`.
>
> The proof is the source's: by Stacks 0DN4
> (`AlgebraicGeometry.Space.exists_representsTwistedEuler_structureSheafPushforward`) the twisted
> Euler characteristics of `i_*𝒪_Z` by the `d + 1` invertible modules
> `L_{i₀}'', L_1', …, L_d'` are the values of a numerical polynomial of total degree at most `d`
> in `d + 1` variables, and
> `AlgebraicGeometry.Space.intersectionNumber_eq_add_of_iso_tensorSheaf_of_totalDegree_le` reads
> the three intersection numbers off it.

```lean
theorem intersectionNumber_eq_add_intersectionNumber_of_iso_tensorSheaf (d : ℕ)
    (f : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f)
    (i : Z ⟶ X) (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d) (i₀ : Fin d)
    (L L' L'' : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)]
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L' j)]
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L'' j)]
    (hL' : ∀ j, j ≠ i₀ → L' j = L j) (hL'' : ∀ j, j ≠ i₀ → L'' j = L j)
    (hL : L i₀ ≅ (((Stacks.SheafOfModules.Tensor.sheafTensor
      (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).obj (L' i₀)).obj (L'' i₀) :
        Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)) :
    intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L =
      intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L' +
        intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L''
```

**`AlgebraicGeometry.Space.intersectionNumber_eq_add_of_iso_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NumericalIntersection.lean#L925). The attribute's comment: “with the numerical polynomial of Stacks 0DN4 for the split family of d + 1 invertible modules carried as a hypothesis”.

> **Stacks 0EDH.**  Additivity of the intersection number in each of its invertible modules.
> Let `k` be a field, let `X` be a proper algebraic space over `k`, let `i : Z ⟶ X` be a closed
> subspace of dimension `d` and let `L₁, …, L_d` be invertible `𝒪_X`-modules.  Let `L'` and `L''`
> be two families agreeing with `L` away from one index `i₀` and satisfying
> `L_{i₀} ≅ L_{i₀}' ⊗ L_{i₀}''`.  Then
>
> `(L₁ ⋯ L_{i₀} ⋯ L_d · Z) = (L₁ ⋯ L_{i₀}' ⋯ L_d · Z) + (L₁ ⋯ L_{i₀}'' ⋯ L_d · Z)`.
>
> The mechanism is the source's.  The Euler characteristics of the twists of `i_*𝒪_Z` by the
> `d + 1` invertible modules `L_{i₀}'', L_1', …, L_d'` are the values of a rational polynomial `Q`
> of total degree at most `d` in `d + 1` variables, which is Stacks 0DN4 and is the one thing
> carried, as the hypotheses `Q`, `hQ` and `hQdeg`; the three intersection numbers are then the
> three mixed finite differences of `Q` obtained by tying the two new variables together, by
> setting the second to zero, and by setting the first to zero.  Their alternating combination is
> the `(d + 1)`-fold mixed finite difference of `Q`, which vanishes because the squarefree monomial
> in `d + 1` variables has degree `d + 1`;
> this is `MvPolynomial.sum_neg_one_pow_mul_sub_eval_cons_eq_zero`.
>
> The three comparisons of the twists by the split family with the twists by `L`, `L'` and `L''`
> are proved: at the indicator tuples only the exponents `0` and `1` occur, where the constraints
> of the sheaf tensor product suffice and no multiplication of tensor powers is needed.  See the
> implementation notes.

```lean
theorem intersectionNumber_eq_add_of_iso_tensorSheaf (d : ℕ)
    (f : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f)
    (i : Z ⟶ X) (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d) (i₀ : Fin d)
    (L L' L'' : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)]
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L' j)]
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L'' j)]
    [∀ n : Fin d → ℤ, IsCoherent B (Spec (.of k)) hk X.1 X.2
      (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
        (structureSheafPushforward B (Spec (.of k)) hk i) L n)]
    [∀ n : Fin d → ℤ, IsCoherent B (Spec (.of k)) hk X.1 X.2
      (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
        (structureSheafPushforward B (Spec (.of k)) hk i) L' n)]
    [∀ n : Fin d → ℤ, IsCoherent B (Spec (.of k)) hk X.1 X.2
      (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
        (structureSheafPushforward B (Spec (.of k)) hk i) L'' n)]
    [∀ m : Fin (d + 1) → ℤ, IsCoherent B (Spec (.of k)) hk X.1 X.2
      (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
        (structureSheafPushforward B (Spec (.of k)) hk i) (Fin.cons (L'' i₀) L') m)]
    (hL' : ∀ j, j ≠ i₀ → L' j = L j) (hL'' : ∀ j, j ≠ i₀ → L'' j = L j)
    (hL : L i₀ ≅ (((Stacks.SheafOfModules.Tensor.sheafTensor
      (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).obj (L' i₀)).obj (L'' i₀) :
        Modules.{u, u} B (Spec (.of k)) hk X.1 X.2))
    (Q : MvPolynomial (Fin (d + 1)) ℚ) (hQdeg : Q.totalDegree ≤ d)
    (hQ : ∀ m : Fin (d + 1) → ℤ, MvPolynomial.eval (fun p => (m p : ℚ)) Q =
      ((eulerCharacteristic.{u, w} k B hk X.1 X.2 f hf
        (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
          (structureSheafPushforward B (Spec (.of k)) hk i) (Fin.cons (L'' i₀) L') m) : ℤ) : ℚ)) :
    intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L =
      intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L' +
        intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L''
```

## Tag 0EDI, a lemma

[Tag 0EDI](https://stacks.math.columbia.edu/tag/0EDI) in the Stacks Project.

**`AlgebraicGeometry.Space.intersectionNumber_eq_finsum_mul_intersectionNumber_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberComponents.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberComponents.lean#L308). References: SGA 6 X (4.4), “partial”.

> **Stacks 0EDI.**  Let `k` be a field, `X` a proper algebraic space over `k`, `i : Z ⟶ X` a
> closed subspace of dimension `d` and `L₁, …, L_d` invertible `𝒪_X`-modules.  Let `Z_C ⊆ Z` be the
> irreducible components of `Z` of dimension `d` — the components `C` of the closed set
> `|Z| ⊆ |X|` of Krull dimension `d`, each with its reduced induced structure (Stacks 03IQ) — let
> `x̄_C` be a geometric generic point of `Z_C` and let
> `m_C = length_{𝒪_{X, x̄_C}}(𝒪_{Z, x̄_C})`, the length of the stalk of `i_*𝒪_Z` at `x̄_C`.  Then
>
> `(L₁ ⋯ L_d · Z) = ∑_C m_C (L₁ ⋯ L_d · Z_C)`.
>
> As in the source this is immediate from Stacks 0EDE, in the form
> `AlgebraicGeometry.Space.exists_twistedEuler_sub_finsum_mul_componentStructureSheaf` applied to
> `F = i_*𝒪_Z`, whose support is `|Z|`
> (`AlgebraicGeometry.Space.moduleSupportSet_structureSheafPushforward_of_isClosedImmersion`):
> the difference of the Euler characteristics is a polynomial of total degree `< d`, so its
> coefficient of `n₁ ⋯ n_d` vanishes, and comparing that coefficient is
> `Space.intersectionNumber_eq_finsum_mul_of_eval_eq_sub_finsum_irreducibleComponents`.
> The length `m_C` is a natural number by Stacks 0EE4.

```lean
theorem intersectionNumber_eq_finsum_mul_intersectionNumber_irreducibleComponents (d : ℕ)
    (f : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f)
    (i : Z ⟶ X) (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)]
    (x : irreducibleComponents (Set.range (pointsMap B (Spec (.of k)) hk Z.1 i.hom)) →
      GeometricPoint B (Spec (.of k)) hk X.1)
    (hx : ∀ C, IsGenericPoint (x C).image
      (Subtype.val '' (C : Set (Set.range (pointsMap B (Spec (.of k)) hk Z.1 i.hom))))) :
    intersectionNumber.{u, w} k B hk X Z d f hf i hi hd L =
      ∑ᶠ (C : {C : irreducibleComponents (Set.range (pointsMap B (Spec (.of k)) hk Z.1 i.hom)) //
          topologicalKrullDim (Subtype.val ''
            (C : Set (Set.range (pointsMap B (Spec (.of k)) hk Z.1 i.hom)))) = d}),
        ((geometricLength B (Spec (.of k)) hk X (x C.1)
            (structureSheafPushforward B (Spec (.of k)) hk i)).toNat : ℤ) *
          intersectionNumber.{u, w} k B hk X
            (closedSubfunctorSpace B (Spec (.of k)) hk
              (isClosedSubspace_reducedClosedSubspace B (Spec (.of k)) hk X.1 X.2 _
                (closedSetComponentPoints B (Spec (.of k)) hk _
                  (isClosed_range_pointsMap_of_isClosedImmersion B (Spec (.of k)) hk X.2 i.hom hi)
                  C.1).isClosed)) d f hf
            (closedSubfunctorι B (Spec (.of k)) hk
              (isClosedSubspace_reducedClosedSubspace B (Spec (.of k)) hk X.1 X.2 _
                (closedSetComponentPoints B (Spec (.of k)) hk _
                  (isClosed_range_pointsMap_of_isClosedImmersion B (Spec (.of k)) hk X.2 i.hom hi)
                  C.1).isClosed))
            (isClosedSubspace_reducedClosedSubspace B (Spec (.of k)) hk X.1 X.2 _
              (closedSetComponentPoints B (Spec (.of k)) hk _
                (isClosed_range_pointsMap_of_isClosedImmersion B (Spec (.of k)) hk X.2 i.hom hi)
                C.1).isClosed).2
            ((dimension_reducedClosedSubspace B (Spec (.of k)) hk X.1 X.2
              (isDecentSpace_of_isProper_baseObject k B hk X.1 X.2 f hf) _ _).trans C.2) L
```

## Tag 0EDJ, a lemma

[Tag 0EDJ](https://stacks.math.columbia.edu/tag/0EDJ) in the Stacks Project.

**`AlgebraicGeometry.Space.intersectionNumber_modulePullback_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberProperImage.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberProperImage.lean#L668).

> **Stacks 0EDJ.** Let `k` be a field, let `f : Y ⟶ X` be a morphism of algebraic spaces proper
> over `k`, let `Z ⊂ Y` be an integral closed subspace of dimension `d` and let `L₁, …, L_d` be
> invertible `𝒪_X`-modules. Let `f(Z) ⊂ X` be the image of `Z`: the integral closed subspace on the
> closure of `f(|Z|)`, which is the scheme-theoretic image of `Z ⟶ X`, and has dimension at most
> `d`. Then
>
> `(f^*L₁ ⋯ f^*L_d · Z) = deg(Z/f(Z)) · (L₁ ⋯ L_d · f(Z))`
>
> where `deg(Z/f(Z))` is the degree of Stacks 0AD6 if `dim f(Z) = d`, and the right hand side is
> `0` if `dim f(Z) < d`.
>
> The three conjuncts are: `f(Z)` is the scheme-theoretic image of `Z ⟶ X`
> (`AlgebraicGeometry.Space.IntegralClosedSubspace.closureImage_subspace_eq_schemeTheoreticImage`,
> Stacks 0830); `dim f(Z) ≤ d`
> (`AlgebraicGeometry.Space.IntegralClosedSubspace.dimension_closureImage_le`, Stacks 0EDC); and
> the formula, which is
> `AlgebraicGeometry.Space.intersectionNumber_modulePullback_eq_degree_mul` when `dim f(Z) = d` and
> `AlgebraicGeometry.Space.intersectionNumber_modulePullback_eq_zero_of_dimension_lt` otherwise.

```lean
theorem intersectionNumber_modulePullback_eq (f : Y ⟶ X)
    (Z : IntegralClosedSubspace B (Spec (.of k)) hk Y.1) {d : ℕ}
    (hZd : dimension B (Spec (.of k)) hk Z.subspace.toFunctor Z.isClosedSubspace.1 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [hL : ∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)] :
    let W := IntegralClosedSubspace.closureImage B (Spec (.of k)) hk X.2
      (isDecentSpace_of_isProper_baseObject k B hk X.1 X.2 pX hpX) f.hom Z
    W.subspace = schemeTheoreticImageSubfunctor B (Spec (.of k)) hk (Z.subspace.ι ≫ f.hom) ∧
      dimension B (Spec (.of k)) hk W.subspace.toFunctor W.isClosedSubspace.1 ≤ d ∧
      @intersectionNumber.{u, w} k _ B hk Y
          (closedSubspaceToSpace B (Spec (.of k)) hk Y ⟨Z.subspace, Z.isClosedSubspace⟩) d pY hpY
          (closedSubspaceInclusion B (Spec (.of k)) hk Y ⟨Z.subspace, Z.isClosedSubspace⟩)
          Z.isClosedSubspace.2 hZd
          (fun j => (modulePullback B (Spec (.of k)) hk f).obj (L j))
          (fun j => stacksIsInvertible_modulePullback_obj B (Spec (.of k)) hk f (L j)
            (hM := hL j)) =
        if hW : dimension B (Spec (.of k)) hk W.subspace.toFunctor W.isClosedSubspace.1 = d then
          (degree B (Spec (.of k)) hk Z.isClosedSubspace.1 W.isClosedSubspace.1 Z.isIntegralSpace
              W.isIntegralSpace
              (IntegralClosedSubspace.toClosureImage B (Spec (.of k)) hk X.2
                (isDecentSpace_of_isProper_baseObject k B hk X.1 X.2 pX hpX) f.hom Z) : ℤ) *
            intersectionNumber.{u, w} k B hk X
              (closedSubspaceToSpace B (Spec (.of k)) hk X ⟨W.subspace, W.isClosedSubspace⟩) d pX
              hpX (closedSubspaceInclusion B (Spec (.of k)) hk X ⟨W.subspace, W.isClosedSubspace⟩)
              W.isClosedSubspace.2 hW L
        else 0
```

## Tag 0EDK, a lemma

[Tag 0EDK](https://stacks.math.columbia.edu/tag/0EDK) in the Stacks Project.

**`AlgebraicGeometry.Space.intersectionNumber_eq_sum_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberCartierDivisor.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/IntersectionNumberCartierDivisor.lean#L168). The attribute's comment: “the right-hand side as the defining sum of Definition 0EDF for D, of dimension at most d; it is intersectionNumber D when dim D = d and 0 when dim D < d”.

> **Stacks 0EDK.**  Let `k` be a field, let `X` be a proper algebraic space over `k`, let
> `i : Z ⟶ X` be a closed subspace of dimension `d + 1` and let `L₁, …, L_{d+1}` be invertible
> `𝒪_X`-modules.  Let `D ⊆ Z` be an effective Cartier divisor with `L₁|_Z ≅ 𝒪_Z(D)`, and let
> `j : D ⟶ X` be its inclusion into `X`.  Then
>
> `(L₁ ⋯ L_{d+1} · Z) = (L₂ ⋯ L_{d+1} · D)`.
>
> The right-hand side is written as the defining expression of Definition 0EDF,
> `∑_{T ⊆ {2, …, d + 1}} (-1)^{d - |T|} χ(X, j_*𝒪_D ⊗ ⨂_{l ∈ T} L_l)`:
>
> * (i) this is the intersection number of Definition 0EDF read for the closed subspace `D`, which
>   has dimension at most `d` (`AlgebraicGeometry.Space.dimension_le_of_isEffectiveCartierDivisor`)
>   but not necessarily exactly `d`;
> * (ii) it is `AlgebraicGeometry.Space.intersectionNumber` of `D` by
>   `AlgebraicGeometry.Space.intersectionNumber_eq_sum` whenever `dim D = d`, which is
>   `intersectionNumber_eq_intersectionNumber_of_isEffectiveCartierDivisor_of_dimension_eq`;
> * (iii) it is `0` when `dim D < d`, by Stacks 0DN4, which is
>   `AlgebraicGeometry.Space.sum_eulerCharacteristic_eq_zero_of_dimension_lt`.
>
> No hypothesis beyond the source's is taken.

```lean
theorem intersectionNumber_eq_sum_of_isEffectiveCartierDivisor (d : ℕ)
    (f : X.1 ⟶ yoneda.obj (baseObject k B hk)) (hf : IsProper B (Spec (.of k)) hk f) (i : Z ⟶ X)
    (hi : IsClosedImmersion B (Spec (.of k)) hk i.hom)
    (hd : dimension B (Spec (.of k)) hk Z.1 Z.2 = d + 1)
    (Dv : ClosedSubspaces B (Spec (.of k)) hk Z.1)
    (hDv : IsEffectiveCartierDivisor B (Spec (.of k)) hk Z Dv)
    (L : Fin (d + 1) → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O)).property (L j)]
    (hL : (modulePullback B (Spec (.of k)) hk i).obj (L 0) ≅
      associatedInvertibleSheaf B (Spec (.of k)) hk Z Dv hDv) :
    intersectionNumber.{u, w} k B hk X Z (d + 1) f hf i hi hd L =
      ∑ T : Finset (Fin d), (-1 : ℤ) ^ (d - T.card) *
        @eulerCharacteristic.{u, w} k _ B hk X.1 X.2 f hf
          (twistedModuleUlift.{u, w} B (Spec (.of k)) hk X.1 X.2
            (structureSheafPushforward B (Spec (.of k)) hk
              ((ObjectProperty.homMk Dv.1.ι :
                (⟨Dv.1.toFunctor, Dv.2.1⟩ : AlgebraicSpaces B (Spec (.of k)) hk) ⟶ Z) ≫ i))
            (fun j => L j.succ) fun j => if j ∈ T then 1 else 0)
          (isCoherent_twistedModuleUlift_structureSheafPushforward.{u, w} k B hk X
            ⟨Dv.1.toFunctor, Dv.2.1⟩ f hf _
            (isClosedImmersion_comp B (Spec (.of k)) hk Dv.1.ι i.hom Dv.2.2 hi) _ _)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.18, Tag 0DN3](https://stacks.math.columbia.edu/tag/0DN3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
