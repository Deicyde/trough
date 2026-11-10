---
declaration: section
origin: cited
lean: Algebra.Presentation.lichtenbaumSchlessingerComplex, Biderivation, Biderivation.IsCompatibleOnVars, Biderivation.existsUnique_mvPolynomial, Biderivation.existsUnique_mvPolynomial_of_op_smul_eq, Algebra.Presentation.cotangentToLichtenbaumSchlessinger, Algebra.Presentation.truncGECotangentIsoLichtenbaumSchlessinger, Algebra.Presentation.truncGECotangentIsoLichtenbaumSchlessinger_fac
statement: formalized
proof: formalized
---

# 92.13 Comparison with Lichtenbaum-Schlessinger

Section 92.13 of the Stacks Project, [Tag 09AM](https://stacks.math.columbia.edu/tag/09AM). 5 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09CD, an equation

[Tag 09CD](https://stacks.math.columbia.edu/tag/09CD) in the Stacks Project.

**`Algebra.Presentation.lichtenbaumSchlessingerComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessinger.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessinger.lean#L392).

> The Lichtenbaum–Schlessinger complex associated to a polynomial presentation and chosen
> generators of its defining ideal.

```lean
noncomputable def lichtenbaumSchlessingerComplex
    (P : Algebra.Presentation A B X T) : LichtenbaumSchlessingerComplex P
```

## Tag 09CE, a definition

[Tag 09CE](https://stacks.math.columbia.edu/tag/09CE) in the Stacks Project.

**`Biderivation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Biderivation.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Biderivation.lean#L77). References: EGA 0 (20.1.2); EGA 0 (20.1.1).

> An `A`-biderivation from an `A`-algebra `B` to a `(B, B)`-bimodule `M` is
> an `A`-linear map satisfying the Leibniz rule for the left and right actions.

```lean
structure Biderivation (A : Type u) (B : Type v) (M : Type w)
    [CommSemiring A] [Semiring B] [AddCommMonoid M] [Algebra A B]
    [Module A M] [Module B M] [Module Bᵐᵒᵖ M]
    [IsScalarTower A B M] [IsScalarTower A Bᵐᵒᵖ M]
    [SMulCommClass B Bᵐᵒᵖ M]
    extends B →ₗ[A] M
```

## Tag 09CF, a lemma

[Tag 09CF](https://stacks.math.columbia.edu/tag/09CF) in the Stacks Project.

**`Biderivation.IsCompatibleOnVars`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Biderivation.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Biderivation.lean#L130). The attribute's comment: “the compatibility equations the values on the variables must satisfy”.

> **Stacks 09CF.** The equations that commutativity of the polynomial variables forces on the
> values of a biderivation of `A[S]`: the Leibniz rule applied to the two readings of
> `X s * X t = X t * X s`. For a bimodule whose two actions agree they hold automatically.
>
> The source imposes no such condition; that omission is a Stacks erratum, and these equations
> really can fail, as
> `Biderivation.not_isCompatibleOnVars_erratumValues` shows for the counterexample of
> `StacksFrontier.Cotangent.BiderivationErratum`.

```lean
def IsCompatibleOnVars (A : Type u) {S : Type v} {M : Type w} [CommSemiring A]
    [AddCommGroup M] [Module (MvPolynomial S A) M] [Module (MvPolynomial S A)ᵐᵒᵖ M]
    (m : S → M) : Prop
```

**`Biderivation.existsUnique_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Biderivation.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Biderivation.lean#L358). The attribute's comment: “existence and uniqueness of the biderivation with prescribed values”.

> **Stacks 09CF.** Let `P = A[S]` be a polynomial ring over `A` and let `M` be a `(P, P)`
> bimodule over `A`. Given `m s ∈ M` for `s ∈ S` satisfying the compatibility equations that
> commutativity of the variables forces, there is a unique `A`-biderivation `P → M` sending
> `X s` to `m s`.
>
> This is the corrected form of the tag. The source prescribes the values `m s` with no condition
> at all, and the existence half of that unrestricted claim is false: it is a Stacks erratum,
> refuted by `Biderivation.not_exists_biderivation_erratum` in
> `StacksFrontier.Cotangent.BiderivationErratum`, which exhibits `k[x, y]` acting on `k` by
> evaluation at `(1, 0)` on the left and at `(0, 0)` on the right and prescribed values `0` and
> `1` admitting no biderivation. Uniqueness is unaffected, and by
> `Biderivation.existsUnique_mvPolynomial_iff` the compatibility hypothesis below is not merely
> sufficient but exactly the obstruction.

```lean
theorem existsUnique_mvPolynomial (m : S → M) (hcomm : IsCompatibleOnVars A m) :
    ∃! D : Biderivation A (MvPolynomial S A) M, ∀ s, D (X s) = m s
```

**`Biderivation.existsUnique_mvPolynomial_of_op_smul_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/Biderivation.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/Biderivation.lean#L391). The attribute's comment: “the unrestricted assertion of the source, for a bimodule whose two actions agree”.

> **Stacks 09CF**, in the case the source applies it: when the two actions of the polynomial
> ring on `M` agree, the compatibility equations hold for every family of prescribed values, and
> the source's unrestricted assertion is recovered.
>
> This hypothesis cannot be dropped: stated for an arbitrary bimodule the source's assertion is a
> Stacks erratum, refuted by
> `Biderivation.not_forall_existsUnique_mvPolynomial_erratumModule` in
> `StacksFrontier.Cotangent.BiderivationErratum`, whose bimodule is a copy of `k` carrying the two
> different actions evaluation at `(1, 0)` and evaluation at `(0, 0)`.

```lean
theorem existsUnique_mvPolynomial_of_op_smul_eq
    (h : ∀ (q : MvPolynomial S A) (x : M), MulOpposite.op q • x = q • x) (m : S → M) :
    ∃! D : Biderivation A (MvPolynomial S A) M, ∀ s, D (X s) = m s
```

## Tag 09CG, a lemma

[Tag 09CG](https://stacks.math.columbia.edu/tag/09CG) in the Stacks Project.

**`Algebra.Presentation.cotangentToLichtenbaumSchlessinger`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparison.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparison.lean#L154). The attribute's comment: “the canonical map L_{B/A} → L in D(B), attached to a chain-level comparison carried as the explicit datum Algebra.Presentation.LichtenbaumSchlessingerComparison”.

> **Stacks 09CG.** The canonical map `L_{B/A} → L` in `D(B)` attached to a chain-level
> comparison: its image under the localization functor.

```lean
public def cotangentToLichtenbaumSchlessinger (c : LichtenbaumSchlessingerComparison P) :
    DerivedCategory.Q.obj (cotangentComplexULift.{u, v, w} A B) ⟶
      DerivedCategory.Q.obj (lichtenbaumSchlessingerComplex P).complex
```

**`Algebra.Presentation.truncGECotangentIsoLichtenbaumSchlessinger`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparison.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparison.lean#L190). The attribute's comment: “the induced map τ_{≥ -2} L_{B/A} → L is an isomorphism in D(B)”.

> **Stacks 09CG.** The isomorphism `τ_{≥ -2} L_{B/A} ≅ L` induced by the canonical map.

```lean
public def truncGECotangentIsoLichtenbaumSchlessinger
    (c : LichtenbaumSchlessingerComparison P) :
    (DerivedCategory.TStructure.t.truncGE (-2)).obj
        (DerivedCategory.Q.obj (cotangentComplexULift.{u, v, w} A B)) ≅
      DerivedCategory.Q.obj (lichtenbaumSchlessingerComplex P).complex
```

**`Algebra.Presentation.truncGECotangentIsoLichtenbaumSchlessinger_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparison.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparison.lean#L202). The attribute's comment: “the isomorphism τ_{≥ -2} L_{B/A} → L is induced by the canonical map L_{B/A} → L”.

> **Stacks 09CG.** The isomorphism `τ_{≥ -2} L_{B/A} ≅ L` is the one induced by the canonical
> map `L_{B/A} → L`: composing it with the projection to the truncation returns that map.

```lean
public theorem truncGECotangentIsoLichtenbaumSchlessinger_fac
    (c : LichtenbaumSchlessingerComparison P) :
    (DerivedCategory.TStructure.t.truncGEπ (-2)).app
        (DerivedCategory.Q.obj (cotangentComplexULift.{u, v, w} A B)) ≫
      (truncGECotangentIsoLichtenbaumSchlessinger c).hom =
        cotangentToLichtenbaumSchlessinger c
```

**`Algebra.Presentation.LichtenbaumSchlessingerComparison.canonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean#L37). The attribute's comment: “the map of complexes L_{B/A} → L built from the choices ψ and λ of the source, with its isomorphisms on H^0 (Remark 08UP, Lemma 08RB), H^{-1} (idem) and H^{-2} (Remark 09D6)”.

> The chain-level comparison of a presentation constructed in the source: the map of complexes
> `Algebra.Presentation.lsChainMap`, which is `dψ ⊗ 1`, `λ̄` and `q` in degrees `0`, `-1` and `-2`,
> together with its isomorphisms on `H⁰`, `H^{-1}` and `H^{-2}`.

```lean
public def LichtenbaumSchlessingerComparison.canonical : LichtenbaumSchlessingerComparison P
```

**`Algebra.Presentation.canonicalCotangentToLichtenbaumSchlessinger`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean#L53). The attribute's comment: “the canonical map L_{B/A} → L in D(B), the class of the map of complexes dψ ⊗ 1, λ̄, q built from the choices ψ : P₀ → P and the biderivation λ of the source”.

> The canonical map `L_{B/A} → L` in `D(B)`: the image under the localization functor of the
> map of complexes `Algebra.Presentation.lsChainMap`. It does not depend on the choices `ψ` and
> `λ`: `Algebra.Presentation.Q_map_eq_canonicalCotangentToLichtenbaumSchlessinger`.

```lean
public def canonicalCotangentToLichtenbaumSchlessinger :
    DerivedCategory.Q.obj (cotangentComplexULift.{u, v, w} A B) ⟶
      DerivedCategory.Q.obj (lichtenbaumSchlessingerComplex P).complex
```

**`Algebra.Presentation.isIso_descTruncGE_canonicalCotangentToLichtenbaumSchlessinger`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean#L71). The attribute's comment: “the canonical map L_{B/A} → L induces an isomorphism τ_{≥ -2} L_{B/A} → L in D(B)”.

> The canonical map `L_{B/A} → L` factors through the truncation `τ_{≥ -2} L_{B/A}`, and the
> factorization is an isomorphism.

```lean
public theorem isIso_descTruncGE_canonicalCotangentToLichtenbaumSchlessinger :
    IsIso (DerivedCategory.TStructure.t.descTruncGE
      (canonicalCotangentToLichtenbaumSchlessinger P) (-2))
```

**`Algebra.Presentation.canonicalTruncGECotangentIsoLichtenbaumSchlessinger`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean#L79). The attribute's comment: “the induced map τ_{≥ -2} L_{B/A} → L is an isomorphism in D(B)”.

> The isomorphism `τ_{≥ -2} L_{B/A} ≅ L` induced by the canonical map.

```lean
public def canonicalTruncGECotangentIsoLichtenbaumSchlessinger :
    (DerivedCategory.TStructure.t.truncGE (-2)).obj
        (DerivedCategory.Q.obj (cotangentComplexULift.{u, v, w} A B)) ≅
      DerivedCategory.Q.obj (lichtenbaumSchlessingerComplex P).complex
```

**`Algebra.Presentation.canonicalTruncGECotangentIsoLichtenbaumSchlessinger_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonCanonical/Canonical.lean#L90). The attribute's comment: “the isomorphism τ_{≥ -2} L_{B/A} → L is induced by the canonical map L_{B/A} → L”.

> The isomorphism `τ_{≥ -2} L_{B/A} ≅ L` is the one induced by the canonical map
> `L_{B/A} → L`: composing it with the projection to the truncation returns that map.

```lean
public theorem canonicalTruncGECotangentIsoLichtenbaumSchlessinger_fac :
    (DerivedCategory.TStructure.t.truncGEπ (-2)).app
        (DerivedCategory.Q.obj (cotangentComplexULift.{u, v, w} A B)) ≫
      (canonicalTruncGECotangentIsoLichtenbaumSchlessinger P).hom =
        canonicalCotangentToLichtenbaumSchlessinger P
```

**`Algebra.Presentation.Q_map_eq_canonicalCotangentToLichtenbaumSchlessinger`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonIndependence.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonIndependence.lean#L630). The attribute's comment: “the formulas dψ ⊗ 1, λ̄, q specify the comparison for every permissible choice of ψ and λ, and changing these choices gives the same morphism in D(B)”.

> **Independence of the choices.** Every map of complexes `L_{B/A} → L` given by the formulas
> `dψ ⊗ 1`, `λ̄`, `q` of the source, for any permissible choice of `ψ : P₀ → P` and of the
> biderivation `λ : P₁ → F/TrivRel`, represents the canonical map
> `Algebra.Presentation.canonicalCotangentToLichtenbaumSchlessinger` in `D(B)`.

```lean
theorem Q_map_eq_canonicalCotangentToLichtenbaumSchlessinger (c : LichtenbaumSchlessingerChoice P)
    (f : cotangentComplexULift.{u, v, w} A B ⟶ (lichtenbaumSchlessingerComplex P).complex)
    (hf : IsLichtenbaumSchlessingerComparison P c f) :
    DerivedCategory.Q.map f = canonicalCotangentToLichtenbaumSchlessinger P
```

## Tag 09D7, a remark

[Tag 09D7](https://stacks.math.columbia.edu/tag/09D7) in the Stacks Project.

**`Algebra.Presentation.LichtenbaumSchlessingerHom.canonicalCotangentToLichtenbaumSchlessinger_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonNatural.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerComparisonNatural.lean#L411). The attribute's comment: “the second commutative diagram: L_{B/A} → L, L → L' equals L_{B/A} → L_{B'/A'}, L_{B'/A'} → L' in D(B)”.

> For a commutative square of rings `A → A'`, `B → B'` and compatible presentations `P → P'`
> with `f'_t` the image of `f_t`, the canonical maps `L_{B/A} → L` and `L_{B'/A'} → L'` commute in
> `D(B)` with the map `L_{B/A} → L_{B'/A'}` of cotangent complexes and the map `L → L'` of
> Lichtenbaum–Schlessinger complexes, the objects over `B'` being read over `B` along `B → B'`.

```lean
theorem canonicalCotangentToLichtenbaumSchlessinger_naturality :
    DerivedCategory.Q.map (cotangentComplexULiftSquareMap.{u, u', v, w} A A' B B') ≫
        (ModuleCat.restrictScalars (algebraMap B B')).mapDerivedCategoryFactors.inv.app
          (cotangentComplexULift.{u', max u v, w} A' B') ≫
        (ModuleCat.restrictScalars (algebraMap B B')).mapDerivedCategory.map
          (canonicalCotangentToLichtenbaumSchlessinger.{u', max u v, w} P') ≫
        (ModuleCat.restrictScalars (algebraMap B B')).mapDerivedCategoryFactors.hom.app
          (lichtenbaumSchlessingerComplex P').complex =
      canonicalCotangentToLichtenbaumSchlessinger.{u, max u' v, w} P ≫
        DerivedCategory.Q.map f.complexMap
```

**`Algebra.Presentation.LichtenbaumSchlessingerHom.relationQuotientMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean#L206). The attribute's comment: “the vertical arrow Rel/TrivRel → Rel'/TrivRel' of the displayed diagram”.

> The map `Rel/TrivRel → Rel'/TrivRel'` induced by `Rel → Rel'`, in degree `-2`.

```lean
def relationQuotientMap : relationQuotient P →ₛₗ[f.ringHom] relationQuotient P'
```

**`Algebra.Presentation.LichtenbaumSchlessingerHom.freeTensorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean#L246). The attribute's comment: “the vertical arrow F ⊗_P B → F' ⊗_{P'} B' of the displayed diagram”.

> **Stacks 09D7.** The arrow `F ⊗_P B → F' ⊗_{P'} B'` of the diagram, in degree `-1`.

```lean
def freeTensorMap :
    (B ⊗[P.Ring] (T →₀ P.Ring)) →ₗ[B] B' ⊗[P'.Ring] ((T ⊕ S) →₀ P'.Ring)
```

**`Algebra.Presentation.LichtenbaumSchlessingerHom.differentialTensorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean#L270). The attribute's comment: “the vertical arrow Ω_{P/A} ⊗_P B → Ω_{P'/A'} ⊗_{P'} B' of the displayed diagram”.

> **Stacks 09D7.** The arrow `Ω_{P/A} ⊗_P B → Ω_{P'/A'} ⊗_{P'} B'` of the diagram, in degree
> `0`.

```lean
def differentialTensorMap :
    (B ⊗[P.Ring] Ω[P.Ring⁄A]) →ₗ[B] B' ⊗[P'.Ring] Ω[P'.Ring⁄A']
```

**`Algebra.Presentation.LichtenbaumSchlessingerHom.freeTensorMap_relationBoundaryR`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean#L308). The attribute's comment: “commutativity of the left-hand square of the displayed diagram”.

> **Stacks 09D7.** The left-hand square of the displayed diagram commutes: the arrow
> `Rel/TrivRel → F ⊗_P B` followed by the vertical arrow in degree `-1` agrees with the vertical
> arrow in degree `-2` followed by `Rel'/TrivRel' → F' ⊗_{P'} B'`.

```lean
lemma freeTensorMap_relationBoundaryR (q : relationQuotient P) :
    f.freeTensorMap (relationBoundaryR P q) =
      relationBoundaryR P' (f.relationQuotientMap q)
```

**`Algebra.Presentation.LichtenbaumSchlessingerHom.differentialTensorMap_relationDifferentialB`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctoriality.lean#L331). The attribute's comment: “commutativity of the right-hand square of the displayed diagram”.

> **Stacks 09D7.** The right-hand square of the displayed diagram commutes: the arrow
> `F ⊗_P B → Ω_{P/A} ⊗_P B` followed by the vertical arrow in degree `0` agrees with the vertical
> arrow in degree `-1` followed by `F' ⊗_{P'} B' → Ω_{P'/A'} ⊗_{P'} B'`.

```lean
lemma differentialTensorMap_relationDifferentialB (z : B ⊗[P.Ring] (T →₀ P.Ring)) :
    f.differentialTensorMap (relationDifferentialB P z) =
      relationDifferentialB P' (f.freeTensorMap z)
```

**`Algebra.Presentation.LichtenbaumSchlessingerHom.complexMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctorialityComplex.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/LichtenbaumSchlessingerFunctorialityComplex.lean#L272). The attribute's comment: “the first commutative diagram: the canonical map of Lichtenbaum–Schlessinger complexes L → L' with vertical arrows Rel/TrivRel → Rel'/TrivRel', F ⊗_P B → F' ⊗_{P'} B', Ω_{P/A} ⊗_P B → Ω_{P'/A'} ⊗_{P'} B'”.

> The canonical map of Lichtenbaum–Schlessinger complexes `L → L'` attached to compatible
> presentations of a commutative square of rings: the arrows `Rel/TrivRel → Rel'/TrivRel'`,
> `F ⊗_P B → F' ⊗_{P'} B'`, `Ω_{P/A} ⊗_P B → Ω_{P'/A'} ⊗_{P'} B'` (tensored up to `B'`), which
> commute with the differentials. It is `B`-linear, `L'` being read over `B` along `B → B'`.

```lean
def complexMap : (lichtenbaumSchlessingerComplex P).complex ⟶
    ((𝓡).mapHomologicalComplex (ComplexShape.up ℤ)).obj
      (lichtenbaumSchlessingerComplex P').complex
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.13, Tag 09AM](https://stacks.math.columbia.edu/tag/09AM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
