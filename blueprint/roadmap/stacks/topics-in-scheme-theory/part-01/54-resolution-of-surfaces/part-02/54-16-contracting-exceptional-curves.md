---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.IdealSheafData.ExistsContraction, AlgebraicGeometry.Scheme.IdealSheafData.IsExceptionalCurveOfFirstKind, Stacks.Blowup.exists_isExceptionalCurveOfFirstKind_exceptionalIdeal_vanishingIdeal, AlgebraicGeometry.existsUnique_comp_eq_of_isContractionOfExceptionalCurve, AlgebraicGeometry.existsUnique_iso_of_isContractionOfExceptionalCurve, AlgebraicGeometry.Scheme.IdealSheafData.isNoetherianCompleteLocalRing_formalNeighborhoodRing, AlgebraicGeometry.Scheme.IdealSheafData.isRegularLocalRing_formalNeighborhoodRing, AlgebraicGeometry.Scheme.IdealSheafData.ringKrullDim_formalNeighborhoodRing_eq_two
statement: formalized
proof: formalized
---

# 54.16 Contracting exceptional curves

Section 54.16 of the Stacks Project, [Tag 0C2I](https://stacks.math.columbia.edu/tag/0C2I). 12 tags here are carried by 48 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0C2I, the section

[Tag 0C2I](https://stacks.math.columbia.edu/tag/0C2I) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.ExistsContraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ExceptionalCurvesFirstKind.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ExceptionalCurvesFirstKind.lean#L75). The attribute's comment: “there exists a contraction of E: a morphism X ⟶ X' to a Noetherian scheme carrying E to a closed point x with O\_\{X',x} regular of dimension 2 and exhibiting X as the blowing up of X' at x”. References: SGA 7 X (1.14), “partial”.

> **There exists a contraction of `E`** (Section 0C2I): for the closed subscheme `E` of `X` cut
> out by the ideal sheaf `D`, there is a morphism `X ⟶ X'` carrying `E` to a closed point `x` of a
> Noetherian scheme `X'` with `𝒪_{X',x}` regular of dimension two, which exhibits `X` as the
> blowing up of `X'` at `x`.

```lean
def Scheme.IdealSheafData.ExistsContraction {X : Scheme.{u}} (D : X.IdealSheafData) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.IdealSheafData.IsExceptionalCurveOfFirstKind`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurve.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ExceptionalCurvesFirstKind.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ExceptionalCurvesFirstKind.lean#L60) (StacksFrontier): “an exceptional curve of the first kind: an effective Cartier divisor E with an isomorphism 𝐏¹\_k ≅ E under which the normal sheaf of E pulls back to 𝒪(-1)”.
- [`Stacks.Blowup.exists_isExceptionalCurveOfFirstKind_exceptionalIdeal_vanishingIdeal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/RegularSurfaceExceptionalCurveGlobal.lean#L219), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ExceptionalCurvesFirstKind.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ExceptionalCurvesFirstKind.lean#L64) (StacksFrontier): “the exceptional fibre E of the blowing up of X' at a closed point x with O\_\{X',x} regular of dimension 2 is an exceptional curve of the first kind (from Tag 0AGQ)”.

## Tag 0C5J, a lemma

[Tag 0C5J](https://stacks.math.columbia.edu/tag/0C5J) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_comp_eq_of_isContractionOfExceptionalCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ContractExceptionalCurve.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ContractExceptionalCurve.lean#L320). The attribute's comment: “unique factorization through the contraction”.

> **Stacks Project, Tag 0C5J.** Let `E ⊆ X` be an exceptional curve of the first kind on a
> Noetherian scheme, given by its ideal sheaf `D`, and let `b : X ⟶ X'` be a contraction of `E`.
> Then every morphism `φ : X ⟶ Y` carrying `E` to a single point factors as `φ = b ≫ ψ` for a
> unique `ψ : X' ⟶ Y`.

```lean
public theorem existsUnique_comp_eq_of_isContractionOfExceptionalCurve
    {X X' Y : Scheme.{u}} (D : X.IdealSheafData) (b : X ⟶ X')
    (hb : IsContractionOfExceptionalCurve D b) (φ : X ⟶ Y)
    (hφ : ∃ y : Y, ∀ z : D.subscheme, φ (D.subschemeι z) = y) :
    ∃! ψ : X' ⟶ Y, b ≫ ψ = φ
```

## Tag 0C5K, a lemma

[Tag 0C5K](https://stacks.math.columbia.edu/tag/0C5K) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_iso_of_isContractionOfExceptionalCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ContractExceptionalCurve.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ContractExceptionalCurve.lean#L353). The attribute's comment: “a contraction is unique up to unique isomorphism”.

> **Stacks Project, Tag 0C5K.** A contraction of an exceptional curve of the first kind is
> unique up to unique isomorphism: if `b₁ : X ⟶ X₁` and `b₂ : X ⟶ X₂` both contract the ideal
> sheaf `D`, there is exactly one isomorphism `X₁ ≅ X₂` compatible with them.

```lean
public theorem existsUnique_iso_of_isContractionOfExceptionalCurve {X X₁ X₂ : Scheme.{u}}
    {D : X.IdealSheafData} {b₁ : X ⟶ X₁} {b₂ : X ⟶ X₂}
    (h₁ : IsContractionOfExceptionalCurve D b₁) (h₂ : IsContractionOfExceptionalCurve D b₂) :
    ∃! e : X₁ ≅ X₂, b₁ ≫ e.hom = b₂
```

## Tag 0C2K, a lemma

[Tag 0C2K](https://stacks.math.columbia.edu/tag/0C2K) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.isNoetherianCompleteLocalRing_formalNeighborhoodRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean#L145). The attribute's comment: “the complete Noetherian local clause, granting the five geometric inputs as `ExceptionalMonomialData`”.

> For an exceptional curve of the first kind on a Noetherian scheme, given the five inputs
> `M : ExceptionalMonomialData D`, the ring of compatible global functions on the infinitesimal
> thickenings is a Noetherian complete local ring.

```lean
public theorem isNoetherianCompleteLocalRing_formalNeighborhoodRing [IsNoetherian X]
    (_hE : IsExceptionalCurveOfFirstKind D k e) (M : ExceptionalMonomialData D) :
    IsNoetherianCompleteLocalRing (formalNeighborhoodRing D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isRegularLocalRing_formalNeighborhoodRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean#L155). The attribute's comment: “the regularity clause, granting the five geometric inputs as `ExceptionalMonomialData`”.

> For an exceptional curve of the first kind on a Noetherian scheme, given the five inputs
> `M : ExceptionalMonomialData D`, the ring of compatible global functions on the infinitesimal
> thickenings is a regular local ring.

```lean
public theorem isRegularLocalRing_formalNeighborhoodRing [IsNoetherian X]
    (_hE : IsExceptionalCurveOfFirstKind D k e) (M : ExceptionalMonomialData D) :
    IsRegularLocalRing (formalNeighborhoodRing D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.ringKrullDim_formalNeighborhoodRing_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean#L165). The attribute's comment: “the dimension clause, granting the five geometric inputs as `ExceptionalMonomialData`”.

> For an exceptional curve of the first kind on a Noetherian scheme, given the five inputs
> `M : ExceptionalMonomialData D`, the ring of compatible global functions on the infinitesimal
> thickenings has Krull dimension `2`.

```lean
public theorem ringKrullDim_formalNeighborhoodRing_eq_two [IsNoetherian X]
    (_hE : IsExceptionalCurveOfFirstKind D k e) (M : ExceptionalMonomialData D) :
    ringKrullDim (formalNeighborhoodRing D) = 2
```

**`AlgebraicGeometry.Scheme.IdealSheafData.ker_formalNeighborhoodProjection_eq_maximalIdeal_pow_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhood.lean#L176). The attribute's comment: “the projection-kernel clause, granting the five geometric inputs as `ExceptionalMonomialData`”.

> For an exceptional curve of the first kind on a Noetherian scheme, given the five inputs
> `M : ExceptionalMonomialData D`, the kernel of the projection from the ring of compatible global
> functions to the `(n + 1)`-st thickening is the `(n + 1)`-st power of its maximal ideal.

```lean
public theorem ker_formalNeighborhoodProjection_eq_maximalIdeal_pow_of_isExceptionalCurveOfFirstKind
    [IsNoetherian X] (_hE : IsExceptionalCurveOfFirstKind D k e)
    (M : ExceptionalMonomialData D) (n : ℕ) :
    letI : IsLocalRing (formalNeighborhoodRing D) := M.monomialFiltration.isLocalRing
    RingHom.ker (formalNeighborhoodProjection D n) =
      IsLocalRing.maximalIdeal (formalNeighborhoodRing D) ^ (n + 1)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isNoetherianCompleteLocalRing_formalNeighborhoodRing_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean#L261). The attribute's comment: “the complete Noetherian local clause”.

> **Stacks 0C2K, the complete Noetherian local clause.** For an exceptional curve of the first
> kind on a Noetherian scheme, the ring `lim H⁰(Eₙ, 𝒪ₙ)` of compatible functions on the
> infinitesimal thickenings is a Noetherian complete local ring.

```lean
public theorem isNoetherianCompleteLocalRing_formalNeighborhoodRing_of_isExceptionalCurveOfFirstKind
    [IsNoetherian X] (hE : D.IsExceptionalCurveOfFirstKind k e) :
    IsNoetherianCompleteLocalRing (formalNeighborhoodRing D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isRegularLocalRing_formalNeighborhoodRing_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean#L269). The attribute's comment: “the regularity clause”.

> **Stacks 0C2K, the regularity clause.** For an exceptional curve of the first kind on a
> Noetherian scheme, the ring of compatible functions on the thickenings is a regular local ring.

```lean
public theorem isRegularLocalRing_formalNeighborhoodRing_of_isExceptionalCurveOfFirstKind
    [IsNoetherian X] (hE : D.IsExceptionalCurveOfFirstKind k e) :
    IsRegularLocalRing (formalNeighborhoodRing D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.ringKrullDim_formalNeighborhoodRing_eq_two_of_isExceptionalCurveOfFirstKind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean#L277). The attribute's comment: “the dimension clause”.

> **Stacks 0C2K, the dimension clause.** For an exceptional curve of the first kind on a
> Noetherian scheme, the ring of compatible functions on the thickenings has dimension `2`.

```lean
public theorem ringKrullDim_formalNeighborhoodRing_eq_two_of_isExceptionalCurveOfFirstKind
    [IsNoetherian X] (hE : D.IsExceptionalCurveOfFirstKind k e) :
    ringKrullDim (formalNeighborhoodRing D) = 2
```

**`AlgebraicGeometry.Scheme.IdealSheafData.IsExceptionalCurveOfFirstKind.ker_formalNeighborhoodProjection_eq_maximalIdeal_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveFormalNeighborhoodUnconditional.lean#L288). The attribute's comment: “the kernel clause: the kernel of the projection to E\_\{n+1} is the (n+1)-st power of the maximal ideal”.

> **Stacks 0C2K, the kernel clause.** For an exceptional curve of the first kind on a Noetherian
> scheme, the kernel of the projection of the ring of compatible functions to `H⁰(Eₙ₊₁, 𝒪)` is the
> `(n + 1)`-st power of the maximal ideal, for the local ring structure that comes with the
> regularity clause.

```lean
public theorem IsExceptionalCurveOfFirstKind.ker_formalNeighborhoodProjection_eq_maximalIdeal_pow
    [IsNoetherian X] (hE : D.IsExceptionalCurveOfFirstKind k e) (n : ℕ) :
    letI : IsLocalRing (formalNeighborhoodRing D) :=
      (isRegularLocalRing_formalNeighborhoodRing_of_isExceptionalCurveOfFirstKind hE).toIsLocalRing
    RingHom.ker (formalNeighborhoodProjection D n) =
      IsLocalRing.maximalIdeal (formalNeighborhoodRing D) ^ (n + 1)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isNoetherianCompleteLocalRing_formalNeighborhoodRing_of_monomialData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean#L219). The attribute's comment: “the complete Noetherian local clause, unconditionally”.

> **Stacks 0C2K, the complete Noetherian local clause.** For an exceptional curve of the first
> kind on a Noetherian scheme, the ring of compatible global functions on the infinitesimal
> thickenings is a Noetherian complete local ring.

```lean
public theorem isNoetherianCompleteLocalRing_formalNeighborhoodRing_of_monomialData [IsNoetherian X]
    (hE : IsExceptionalCurveOfFirstKind D k e) :
    IsNoetherianCompleteLocalRing (formalNeighborhoodRing D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.isRegularLocalRing_formalNeighborhoodRing_of_monomialData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean#L227). The attribute's comment: “the regularity clause, unconditionally”.

> **Stacks 0C2K, the regularity clause.**

```lean
public theorem isRegularLocalRing_formalNeighborhoodRing_of_monomialData [IsNoetherian X]
    (hE : IsExceptionalCurveOfFirstKind D k e) :
    IsRegularLocalRing (formalNeighborhoodRing D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.ringKrullDim_formalNeighborhoodRing_eq_two_of_monomialData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean#L235). The attribute's comment: “the dimension clause, unconditionally”.

> **Stacks 0C2K, the dimension clause.**

```lean
public theorem ringKrullDim_formalNeighborhoodRing_eq_two_of_monomialData [IsNoetherian X]
    (hE : IsExceptionalCurveOfFirstKind D k e) :
    ringKrullDim (formalNeighborhoodRing D) = 2
```

**`AlgebraicGeometry.Scheme.IdealSheafData.ker_formalNeighborhoodProjection_eq_maximalIdeal_pow_of_monomialData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveMonomialData.lean#L244). The attribute's comment: “the projection-kernel clause, unconditionally”.

> **Stacks 0C2K, the projection-kernel clause.** The kernel of the projection to the
> `(n + 1)`-st thickening is the `(n + 1)`-st power of the maximal ideal.

```lean
public theorem ker_formalNeighborhoodProjection_eq_maximalIdeal_pow_of_monomialData
    [IsNoetherian X] (hE : IsExceptionalCurveOfFirstKind D k e) (n : ℕ) :
    letI : IsLocalRing (formalNeighborhoodRing D) :=
      (ExceptionalMonomialData.ofIsExceptionalCurveOfFirstKind k hE).monomialFiltration.isLocalRing
    RingHom.ker (formalNeighborhoodProjection D n) =
      IsLocalRing.maximalIdeal (formalNeighborhoodRing D) ^ (n + 1)
```

## Tag 0C2L, a lemma

[Tag 0C2L](https://stacks.math.columbia.edu/tag/0C2L) in the Stacks Project.

**`AlgebraicGeometry.exists_isContractionOfExceptionalCurve_isSteinFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Contraction/ExistsContraction.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Contraction/ExistsContraction.lean#L91).

> **Stacks Project, Tag 0C2L.** Let `X` be a Noetherian scheme and `E ⊆ X` an exceptional curve
> of the first kind, cut out by `D` and presented as `𝐏¹_k` by `e`. Let `f : X ⟶ Y` be a morphism
> such that `Y` is Noetherian, `f` is proper, `f` maps `E` to a point `y` of `Y`, and `f` is
> quasi-finite at every point not in `E`. Then there exists a contraction `b : X ⟶ Z` of `E`, and it
> is the Stein factorization of `f`: `f = b ≫ π` with `𝒪_Z ⟶ b_* 𝒪_X` an isomorphism and `π`
> integral, which characterises the Stein factorization ([Stacks, Tag 03H0]).

```lean
public theorem exists_isContractionOfExceptionalCurve_isSteinFactorization
    {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y] {D : X.IdealSheafData} {k : Type u}
    [Field k] {e : projectiveLineProj k ≅ D.subscheme} (hE : D.IsExceptionalCurveOfFirstKind k e)
    (f : X ⟶ Y) [IsProper f] (y : Y)
    (hmaps : ∀ z : D.subscheme, f.base (D.subschemeι.base z) = y)
    (hqf : ∀ x ∉ (D.support : Set X), quasiFiniteAt f x) :
    ∃ (Z : Scheme.{u}) (b : X ⟶ Z) (π : Z ⟶ Y), b ≫ π = f ∧ IsIso b.c ∧ IsIntegralHom π ∧
      IsContractionOfExceptionalCurve D b
```

## Tag 0C5L, a lemma

[Tag 0C5L](https://stacks.math.columbia.edu/tag/0C5L) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.contractionPicardExactness_of_isContraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean#L306). The attribute's comment: “exactness at Pic(X), the inclusion of the kernel of the degree in the image of b^*, for a general contraction of an exceptional curve of the first kind: with nothing assumed beyond the contraction”.

> Let `b : X ⟶ X'` contract the exceptional curve of the first kind cut out by `D`, presented as
> `𝐏¹_k` by `e`. Then every Picard class of `X` of degree zero on the exceptional curve is pulled
> back along `b`.

```lean
public theorem contractionPicardExactness_of_isContraction
    (hb : IsContractionOfExceptionalCurve D b) :
    D.ContractionPicardExactness k e b
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalRestrictionHom_negativeExceptionalMultiple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean#L158). The attribute's comment: “the splitting map n ↦ O\_X(-nE), stated through Pic(P¹\_k) rather than Z: the restriction of O\_X(-nE) to the exceptional curve is O(n)”.

> The restriction of `𝒪_X(-nE)` to the exceptional curve is `𝒪(n)`, written as the `(-n)`-th
> multiple of the class of `𝒪(-1)` in `Pic(𝐏¹_k)`.

```lean
public theorem exceptionalRestrictionHom_negativeExceptionalMultiple
    (hE : D.IsExceptionalCurveOfFirstKind k e) (n : ℤ) :
    exceptionalRestrictionHom D k e (negativeExceptionalMultipleHom D n) =
      (-n) • Stacks.SheafOfModules.picardClass (projectiveLineProj k).presheaf
        (structureIsSheaf (projectiveLineProj k).toRingedSpace)
        (ProjectiveSpectrum.Proj.twistingSheaf
          (MvPolynomial.homogeneousSubmodule (Fin 2) k) (-1))
        (isInvertible_twistingSheaf_projectiveLine k (-1))
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegreeHom_negativeExceptionalMultiple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean#L185). The attribute's comment: “the splitting: the degree of O\_X(-nE) on the exceptional curve is n. The identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ is an explicit hypothesis, the library having only the injectivity half of that tag”.

> If `φ : ℤ ≃+ Pic(𝐏¹_k)` carries `-1` to the class of `𝒪(-1)`, then the degree of `𝒪_X(-nE)`
> on the exceptional curve is `n`.

```lean
public theorem exceptionalDegreeHom_negativeExceptionalMultiple
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = Stacks.SheafOfModules.picardClass (projectiveLineProj k).presheaf
      (structureIsSheaf (projectiveLineProj k).toRingedSpace)
      (ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) (-1))
      (isInvertible_twistingSheaf_projectiveLine k (-1)))
    (n : ℤ) :
    exceptionalDegreeHom D k e φ (negativeExceptionalMultipleHom D n) = n
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegreeHom_picardClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean#L207). The attribute's comment: “the normalization of the degree map: O\_X(E) has degree -1 on the exceptional curve. The identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ is an explicit hypothesis, the library having only the injectivity half of that tag”.

> If `φ : ℤ ≃+ Pic(𝐏¹_k)` carries `-1` to the class of `𝒪(-1)`, then the degree of `𝒪_X(E)` on
> the exceptional curve is `-1`.

```lean
public theorem exceptionalDegreeHom_picardClass
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = Stacks.SheafOfModules.picardClass (projectiveLineProj k).presheaf
      (structureIsSheaf (projectiveLineProj k).toRingedSpace)
      (ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) (-1))
      (isInvertible_twistingSheaf_projectiveLine k (-1))) :
    exceptionalDegreeHom D k e φ (Stacks.Divisors.picardClass D) = -1
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegreeHom_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean#L225). The attribute's comment: “right exactness: the degree map Pic(X) ⟶ Z on the exceptional curve is surjective, witnessed by the splitting n ↦ O\_X(-nE). The identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ is an explicit hypothesis, the library having only the injectivity half of that tag”.

> If `φ : ℤ ≃+ Pic(𝐏¹_k)` carries `-1` to the class of `𝒪(-1)`, then the degree map on the
> exceptional curve is surjective onto `ℤ`.

```lean
public theorem exceptionalDegreeHom_surjective
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = Stacks.SheafOfModules.picardClass (projectiveLineProj k).presheaf
      (structureIsSheaf (projectiveLineProj k).toRingedSpace)
      (ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) (-1))
      (isInvertible_twistingSheaf_projectiveLine k (-1))) :
    Function.Surjective (exceptionalDegreeHom D k e φ)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.negativeExceptionalMultipleHom_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicard.lean#L241). The attribute's comment: “the splitting n ↦ O\_X(-nE) is injective, so Z is a direct summand of Pic(X). The identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ is an explicit hypothesis, the library having only the injectivity half of that tag”.

> If `φ : ℤ ≃+ Pic(𝐏¹_k)` carries `-1` to the class of `𝒪(-1)`, then `n ↦ [𝒪_X(-nE)]` is
> injective, so `ℤ` is a direct summand of `Pic(X)`.

```lean
public theorem negativeExceptionalMultipleHom_injective
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = Stacks.SheafOfModules.picardClass (projectiveLineProj k).presheaf
      (structureIsSheaf (projectiveLineProj k).toRingedSpace)
      (ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) (-1))
      (isInvertible_twistingSheaf_projectiveLine k (-1))) :
    Function.Injective (negativeExceptionalMultipleHom D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegree_negativeExceptionalMultiple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean#L112). The attribute's comment: “the splitting: the degree of O\_X(-nE) on the exceptional curve is n”.

> **Stacks Project, Tag 0C5L, the splitting.** The degree of `𝒪_X(-nE)` on the exceptional
> curve is `n`, so the sequence of the tag is split by `n ↦ 𝒪_X(-nE)`.

```lean
public theorem exceptionalDegree_negativeExceptionalMultiple
    (hE : D.IsExceptionalCurveOfFirstKind k e) (n : ℤ) :
    D.exceptionalDegree k e (negativeExceptionalMultipleHom D n) = n
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegree_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean#L122). The attribute's comment: “right exactness: the degree map Pic(X) ⟶ Z on the exceptional curve is surjective, witnessed by the splitting n ↦ O\_X(-nE)”.

> **Stacks Project, Tag 0C5L, right exactness.** The degree map on the exceptional curve is
> surjective onto `ℤ`, because `𝒪_X(-nE)` has degree `n`.

```lean
public theorem exceptionalDegree_surjective (hE : D.IsExceptionalCurveOfFirstKind k e) :
    Function.Surjective (D.exceptionalDegree k e)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegree_picardClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean#L130). The attribute's comment: “the normalization of the degree map: O\_X(E) has degree -1 on the exceptional curve”.

> **The degree of `𝒪_X(E)` on the exceptional curve is `-1`**, the source's reading of the
> definition of an exceptional curve of the first kind.

```lean
public theorem exceptionalDegree_picardClass (hE : D.IsExceptionalCurveOfFirstKind k e) :
    D.exceptionalDegree k e (Stacks.Divisors.picardClass D) = -1
```

**`AlgebraicGeometry.Scheme.IdealSheafData.negativeExceptionalMultipleHom_injective'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean#L138). The attribute's comment: “the splitting n ↦ O\_X(-nE) is injective, so Z is a direct summand of Pic(X)”.

> **The splitting of the sequence is injective**, so `ℤ` is a direct summand of `Pic(X)`:
> distinct multiples `𝒪_X(-nE)` have distinct degrees on the exceptional curve.

```lean
public theorem negativeExceptionalMultipleHom_injective'
    (hE : D.IsExceptionalCurveOfFirstKind k e) :
    Function.Injective (negativeExceptionalMultipleHom D)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.injective_schemePullbackClassHom_of_isContraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean#L153). The attribute's comment: “left exactness: pullback Pic(X') ⟶ Pic(X) along the contraction of the exceptional curve is injective”.

> **Stacks Project, Tag 0C5L, left exactness.** Pullback of Picard classes along the
> contraction of an exceptional curve of the first kind is injective: the structure-sheaf
> comparison `𝒪_{X'} ⟶ b_*𝒪_X` of a contraction is an isomorphism, and pullback along a morphism
> with that property is injective.

```lean
public theorem injective_schemePullbackClassHom_of_isContraction
    (hb : IsContractionOfExceptionalCurve D b) :
    Function.Injective (Stacks.Picard.schemePullbackClassHom b)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalDegree_schemePullbackClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardContraction.lean#L208). The attribute's comment: “exactness at Pic(X), the inclusion of the image of b^* in the kernel of the degree: a class pulled back along the contraction has degree zero on the exceptional curve”.

> **Stacks Project, Tag 0C5L, the inclusion `im(b^*) ⊆ ker(deg)`.** A Picard class pulled back
> along the contraction has degree zero on the exceptional curve: the curve maps into the
> one-point subscheme it is contracted to, whose Picard group vanishes.

```lean
public theorem exceptionalDegree_schemePullbackClassHom
    (hb : IsContractionOfExceptionalCurve D b) (L' : Stacks.Picard.ofScheme X') :
    D.exceptionalDegree k e (Stacks.Picard.schemePullbackClassHom b L') = 0
```

**`AlgebraicGeometry.contractionPicardExactness_exceptionalIdealData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardExactness.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardExactness.lean#L123). The attribute's comment: “exactness at Pic(X), the inclusion of the kernel of the degree in the image of b^*, for the blowup of a regular local ring of dimension two in its maximal ideal: with nothing assumed”.

> Let `(A, 𝔪, κ)` be a regular local ring of dimension two, let `X ⟶ Spec A` be the blowing up of
> `Spec A` in `𝔪` and let `E` be its exceptional divisor, presented as an exceptional curve of the
> first kind by `e : 𝐏¹_k ≅ E`. Then every Picard class of `X` of degree zero on `E` is pulled back
> along any morphism out of `X`.

```lean
public theorem contractionPicardExactness_exceptionalIdealData (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) (k : Type u) [Field k]
    {e : projectiveLineProj k ≅
      (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).subscheme}
    (hE : (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).IsExceptionalCurveOfFirstKind k e)
    {X' : Scheme.{u}} (b : Stacks.Blowup.blowUpSpec (maximalIdeal A) ⟶ X') :
    (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).ContractionPicardExactness k e b
```

**`AlgebraicGeometry.Scheme.IdealSheafData.picardShortExactSequence_of_isContraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardShortExactSequence.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardShortExactSequence.lean#L79). The attribute's comment: “the short exact sequence 0 → Pic(X') → Pic(X) → Z → 0 of the contraction of an exceptional curve of the first kind, in one statement with every clause written out: pullback along b is injective, a class has degree zero on the exceptional curve iff it is pulled back along b, the degree is surjective onto Z, the splitting n ↦ O\_X(-nE) is a section of the degree, and O\_X(E) has degree -1”.

> **Stacks Project, Tag 0C5L: the Picard short exact sequence of the contraction of an
> exceptional curve of the first kind, together with its splitting.** Let `b : X ⟶ X'` contract the
> exceptional curve of the first kind `E ⊆ X` cut out by the ideal sheaf `D` and presented as
> `𝐏¹_k` by the isomorphism `e`. Then
>
> `0 ⟶ Pic(X') ⟶ Pic(X) ⟶ ℤ ⟶ 0`
>
> is exact, and split by `n ↦ 𝒪_X(-nE)`; the first map is pullback along `b` and the second is the
> degree on `E`. The five clauses below are, in order:
>
> * exactness at `Pic(X')`: pullback along `b` is injective;
> * exactness at `Pic(X)`, both inclusions at once: a class of `X` has degree zero on `E` if and
>   only if it is pulled back along `b`;
> * exactness at `ℤ`: the degree on `E` is onto `ℤ`;
> * the splitting: `𝒪_X(-nE)` has degree `n` on `E`, so `n ↦ 𝒪_X(-nE)` is a section of the degree
>   map;
> * the normalization of the degree: `𝒪_X(E)` has degree `-1` on `E`.
>
> Being an effective Cartier divisor is the first clause of the hypothesis that `D` cuts out an
> exceptional curve of the first kind, so nothing is assumed here beyond the contraction and the
> curve it contracts.

```lean
public theorem picardShortExactSequence_of_isContraction
    (hb : IsContractionOfExceptionalCurve D b)
    (hE : D.IsExceptionalCurveOfFirstKind k e) :
    Function.Injective (Stacks.Picard.schemePullbackClassHom b) ∧
      (∀ L : Stacks.Picard.ofScheme X, D.exceptionalDegree k e L = 0 ↔
        ∃ L' : Stacks.Picard.ofScheme X', Stacks.Picard.schemePullbackClassHom b L' = L) ∧
      Function.Surjective (D.exceptionalDegree k e) ∧
      (∀ n : ℤ, D.exceptionalDegree k e (negativeExceptionalMultipleHom D n) = n) ∧
      D.exceptionalDegree k e (Stacks.Divisors.picardClass D) = -1
```

## Tag 0C5M, a remark

[Tag 0C5M](https://stacks.math.columbia.edu/tag/0C5M) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.picardDecomposition_of_isContraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean#L331). The attribute's comment: “the identification Pic(X) = Pic(X') ⊕ Z for a general contraction of an exceptional curve of the first kind: with nothing assumed beyond the contraction, exactness at Pic(X) discharged”.

> The identification `Pic(X) = Pic(X') ⊕ ℤ` for `b : X ⟶ X'` the contraction of an exceptional
> curve of the first kind `E ⊆ X`: a class `ℒ` on `X` corresponds to the pair `(ℒ', n)` with `n` the
> degree of `ℒ` on `E`, and a pair `(ℒ', n)` to the class of `(b^*ℒ')(-nE)`.

```lean
public def picardDecomposition_of_isContraction
    (hb : IsContractionOfExceptionalCurve D b)
    (hE : D.IsExceptionalCurveOfFirstKind k e) :
    Stacks.Picard.ofScheme X ≃+ Stacks.Picard.ofScheme X' × ℤ
```

**`AlgebraicGeometry.Scheme.IdealSheafData.contractedPicardHom_of_isContraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean#L344). The attribute's comment: “the assignment L ↦ L' is a group homomorphism, for a general contraction of an exceptional curve of the first kind: with nothing assumed beyond the contraction, exactness at Pic(X) discharged”.

> The homomorphism `ℒ ↦ ℒ'` of the contraction `b : X ⟶ X'` of an exceptional curve of the first
> kind. It sends a Picard class `ℒ` of `X` to the unique class `ℒ'` on `X'` with `ℒ(nE) = b^*ℒ'`,
> where `n` is the degree of `ℒ` on the exceptional curve.

```lean
public def contractedPicardHom_of_isContraction
    (hb : IsContractionOfExceptionalCurve D b)
    (hE : D.IsExceptionalCurveOfFirstKind k e) :
    Stacks.Picard.ofScheme X →+ Stacks.Picard.ofScheme X'
```

**`AlgebraicGeometry.Scheme.IdealSheafData.picardDecomposition_of_isContraction_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean#L373). The attribute's comment: “the characterisation: L corresponds to the pair (L', n) if and only if L = (b^*L')(-nE), for a general contraction of an exceptional curve of the first kind: with nothing assumed beyond the contraction”.

> For the contraction of an exceptional curve of the first kind, a class `ℒ` corresponds under
> the decomposition to the pair `(ℒ', n)` if and only if `ℒ = (b^*ℒ')(-nE)`.

```lean
public theorem picardDecomposition_of_isContraction_eq_iff
    (hb : IsContractionOfExceptionalCurve D b)
    (hE : D.IsExceptionalCurveOfFirstKind k e) (L : Stacks.Picard.ofScheme X)
    (L' : Stacks.Picard.ofScheme X') (n : ℤ) :
    D.picardDecomposition_of_isContraction k e b hb hE L = (L', n) ↔
      L = Stacks.Picard.schemePullbackClassHom b L' + negativeExceptionalMultipleHom D n
```

**`AlgebraicGeometry.Scheme.IdealSheafData.picardDecomposition_of_isContraction_eq_iff_exceptionalTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean#L388). The attribute's comment: “the characterisation in the source's second form: L corresponds to (L', n) if and only if L(nE) = b^*L', for a general contraction of an exceptional curve of the first kind: with nothing assumed beyond the contraction”.

> For the contraction of an exceptional curve of the first kind, a class `ℒ` corresponds under
> the decomposition to the pair `(ℒ', n)` if and only if `ℒ(nE)` is the pullback of `ℒ'` along
> `b`.

```lean
public theorem picardDecomposition_of_isContraction_eq_iff_exceptionalTwist
    (hb : IsContractionOfExceptionalCurve D b)
    (hE : D.IsExceptionalCurveOfFirstKind k e) (L : Stacks.Picard.ofScheme X)
    (L' : Stacks.Picard.ofScheme X') (n : ℤ) :
    D.picardDecomposition_of_isContraction k e b hb hE L = (L', n) ↔
      D.exceptionalTwist n L = Stacks.Picard.schemePullbackClassHom b L'
```

**`AlgebraicGeometry.Scheme.IdealSheafData.picardDecomposition_of_isContraction_apply_fst_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ContractionPicardDescent.lean#L413). The attribute's comment: “the formula L' = b\_*L(nE) read off the proof of Tag 0C5L, stated for every pushforward on Picard classes left inverse to b^*, for a general contraction of an exceptional curve of the first kind: with nothing assumed beyond the contraction, exactness at Pic(X) discharged and such a pushforward exhibited”.

> For the contraction of an exceptional curve of the first kind, the `Pic(X')`-component of the
> decomposition is `p(ℒ(nE))`, with `n` the degree of `ℒ` on the exceptional curve, for every
> pushforward `p` on Picard classes left inverse to `b^*`.

```lean
public theorem picardDecomposition_of_isContraction_apply_fst_pushforward
    (hb : IsContractionOfExceptionalCurve D b)
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (p : Stacks.Picard.ofScheme X →+ Stacks.Picard.ofScheme X')
    (hp : ∀ L' : Stacks.Picard.ofScheme X',
      p (Stacks.Picard.schemePullbackClassHom b L') = L')
    (L : Stacks.Picard.ofScheme X) :
    (D.picardDecomposition_of_isContraction k e b hb hE L).1 =
      p (D.exceptionalTwist (D.exceptionalDegree k e L) L)
```

**`AlgebraicGeometry.Scheme.IdealSheafData.picardDecomposition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardDecomposition.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardDecomposition.lean#L254). The attribute's comment: “the identification Pic(X) = Pic(X') ⊕ Z, granted the two halves of Tag 0C5L the library does not prove — a pushforward b\_* left inverse to b^*, and exactness at Pic(X) — bundled as the hypothesis ContractionPicardSplitting, and granted the identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ, of which the library has only the injectivity half”.

> **Stacks Project, Tag 0C5M: the identification `Pic(X) = Pic(X') ⊕ ℤ`.** For the contraction
> `b : X ⟶ X'` of an exceptional curve of the first kind, a class `ℒ` on `X` is sent to the pair
> `(b_*ℒ(nE), n)` with `n` the degree of `ℒ` on the exceptional curve, and a pair `(ℒ', n)` back
> to the class of `(b^*ℒ')(-nE)`.

```lean
public def picardDecomposition (hb : D.ContractionPicardSplitting k e φ b)
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = projectiveLineTwistPicardClass k (-1)) :
    Stacks.Picard.ofScheme X ≃+ Stacks.Picard.ofScheme X' × ℤ
```

**`AlgebraicGeometry.Scheme.IdealSheafData.picardDecomposition_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardDecomposition.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardDecomposition.lean#L290). The attribute's comment: “the characterisation: L corresponds to the pair (L', n) if and only if L = (b^*L')(-nE), granted the two halves of Tag 0C5L the library does not prove, bundled as the hypothesis ContractionPicardSplitting, and the identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ”.

> **Stacks Project, Tag 0C5M: the characterisation of the decomposition.** A class `ℒ`
> corresponds to the pair `(ℒ', n)` if and only if `ℒ = (b^*ℒ')(-nE)`.

```lean
public theorem picardDecomposition_eq_iff (hb : D.ContractionPicardSplitting k e φ b)
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = projectiveLineTwistPicardClass k (-1)) (L : Stacks.Picard.ofScheme X)
    (L' : Stacks.Picard.ofScheme X') (n : ℤ) :
    picardDecomposition hb hE hφ L = (L', n) ↔
      L = Stacks.Picard.schemePullbackClassHom b L' + D.negativeExceptionalMultipleHom n
```

**`AlgebraicGeometry.Scheme.IdealSheafData.contractedPicardHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardDecomposition.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardDecomposition.lean#L308). The attribute's comment: “the assignment L ↦ L' is a group homomorphism, granted the two halves of Tag 0C5L the library does not prove, bundled as the hypothesis ContractionPicardSplitting, and granted the identification Z ≃+ Pic(P¹\_k) of Tag 0BXJ”.

> **Stacks Project, Tag 0C5M: the assignment `ℒ ↦ ℒ'` is a group homomorphism.** It is the
> `Pic(X')`-component of the decomposition `Pic(X) ≃+ Pic(X') × ℤ`.

```lean
public def contractedPicardHom (hb : D.ContractionPicardSplitting k e φ b)
    (hE : D.IsExceptionalCurveOfFirstKind k e)
    (hφ : φ (-1) = projectiveLineTwistPicardClass k (-1)) :
    Stacks.Picard.ofScheme X →+ Stacks.Picard.ofScheme X'
```

**`AlgebraicGeometry.picardDecomposition_exceptionalIdealData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardExactness.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardExactness.lean#L168). The attribute's comment: “the identification Pic(X) = Pic(X') ⊕ Z for the blowup of a regular local ring of dimension two in its maximal ideal: with nothing assumed, both hypotheses of the general decomposition discharged”.

> Let `(A, 𝔪, κ)` be a regular local ring of dimension two and let `b : X ⟶ Spec A` be the
> blowing up of `Spec A` in `𝔪`, with exceptional divisor `E` presented as an exceptional curve of
> the first kind by `e : 𝐏¹_k ≅ E`. Then `Pic(X) ≃+ Pic(Spec A) × ℤ`, a class `ℒ` corresponding to
> the pair `(ℒ', n)` with `n` the degree of `ℒ` on `E` exactly when `ℒ = (b^*ℒ')(-nE)`.

```lean
public def picardDecomposition_exceptionalIdealData (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) (k : Type u) [Field k]
    {e : projectiveLineProj k ≅
      (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).subscheme}
    (hE : (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).IsExceptionalCurveOfFirstKind
      k e) :
    Stacks.Picard.ofScheme (Stacks.Blowup.blowUpSpec (maximalIdeal A)) ≃+
      Stacks.Picard.ofScheme (Spec (CommRingCat.of A)) × ℤ
```

**`AlgebraicGeometry.contractedPicardHom_exceptionalIdealData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardExactness.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurvePicardExactness.lean#L188). The attribute's comment: “the assignment L ↦ L' is a group homomorphism, for the blowup of a regular local ring of dimension two in its maximal ideal: with nothing assumed”.

> The homomorphism `ℒ ↦ ℒ'` of the blowup of a regular local ring of dimension two in its maximal
> ideal. It sends a Picard class `ℒ` of the blowup to the unique class `ℒ'` on `Spec A` with
> `ℒ(nE) = b^*ℒ'`, where `n` is the degree of `ℒ` on the exceptional curve. It is the
> `Pic(Spec A)`-component of `AlgebraicGeometry.picardDecomposition_exceptionalIdealData`.

```lean
public def contractedPicardHom_exceptionalIdealData (A : Type u) [CommRing A]
    [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) (k : Type u) [Field k]
    {e : projectiveLineProj k ≅
      (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).subscheme}
    (hE : (Stacks.Blowup.exceptionalIdealData (maximalIdeal A)).IsExceptionalCurveOfFirstKind
      k e) :
    Stacks.Picard.ofScheme (Stacks.Blowup.blowUpSpec (maximalIdeal A)) →+
      Stacks.Picard.ofScheme (Spec (CommRingCat.of A))
```

## Tag 0C2J, a lemma

[Tag 0C2J](https://stacks.math.columbia.edu/tag/0C2J) in the Stacks Project.

**`Stacks.Surfaces.isZero_rightDerived_one_divisorTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveDivisorTwist.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveDivisorTwist.lean#L135). The attribute's comment: “assertion (1): H^1 vanishes on the twists ℒ(iE) for 0 ≤ i ≤ n+1”.

> **[Stacks, Tag 0C2J], assertion (1).** Let `E ⊆ X` be an exceptional curve of the first kind
> on a scheme `X`, let `ℒ` be an invertible `𝒪_X`-module, and let `n` be the degree of `ℒ|_E` as an
> invertible module on `𝐏¹`, recorded as an isomorphism `e^*i^*ℒ ≅ 𝒪(n)`. If `H¹(X, ℒ) = 0` and
> `0 ≤ n` then
>
> `H¹(X, ℒ(iE)) = 0` for every `0 ≤ i ≤ n + 1`.
>
> The induction is on `i`, along the ideal sequence of `E` twisted by `ℒ((i+1)E)`:
>
> `0 ⟶ ℒ(iE) ⟶ ℒ((i+1)E) ⟶ ℒ((i+1)E)|_E ⟶ 0`,
>
> whose first term is identified by `Stacks.Surfaces.twistedIdealIso` and whose third restricts to
> `𝒪(n - i - 1)` on `𝐏¹`. For `i ≤ n` that degree is at least `-1`, so the third term has no `H¹`
> by `Stacks.Surfaces.isZero_rightDerived_one_tensorPushforwardUnit`, and the degree-one row of
> the long exact sequence forces `H¹` of the middle term to vanish. The hypothesis `0 ≤ n` is the
> source's and is carried unchanged; the induction consumes only `i ≤ n + 1`, since the step that
> produces `ℒ((j+1)E)` gets the `j ≤ n` it needs from `j + 1 ≤ n + 1`.

```lean
theorem isZero_rightDerived_one_divisorTwist (E : X.IdealSheafData) (k : Type u) [Field k]
    {e : projectiveLineProj k ≅ E.subscheme}
    (hE : E.IsExceptionalCurveOfFirstKind k e)
    (L : _root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf))
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    {n : ℤ} (_hn : 0 ≤ n)
    (hdeg : (modulePullback e.hom.toLRSHom.toShHom).obj
        ((modulePullback E.subschemeι.toLRSHom.toShHom).obj L) ≅
      ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) n)
    (hL : IsZero (((moduleGlobalSections X).rightDerived 1).obj L))
    (i : ℕ) (hi : (i : ℤ) ≤ n + 1) :
    IsZero (((moduleGlobalSections X).rightDerived 1).obj (divisorTwist E L i))
```

**`Stacks.Surfaces.mono_rightDerived_one_map_tensorCanonicalSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveTwistInjectivity.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveTwistInjectivity.lean#L421). The attribute's comment: “assertion (2): injectivity on H^1 when the degree is non-positive”.

> **[Stacks, Tag 0C2J], assertion (2).** Let `E ⊆ X` be an exceptional curve of the first kind
> on a scheme `X`, let `ℒ` be an invertible `𝒪_X`-module, and let `n` be the degree of `ℒ|_E` as an
> invertible module on `𝐏¹`, recorded as an isomorphism `e^*i^*ℒ ≅ 𝒪(n)`. If `n ≤ 0` then
> multiplication by the canonical section `1_E` makes `H¹(X, ℒ)` a submodule of `H¹(X, ℒ(E))`.
>
> The map is `Stacks.Divisors.tensorCanonicalSection`, the canonical map `ℒ ⟶ ℒ ⊗ 𝒪_X(E)` of
> multiplication by `1_E`, and not merely some isomorphic copy of it.

```lean
theorem mono_rightDerived_one_map_tensorCanonicalSection (E : X.IdealSheafData) (k : Type u)
    [Field k] {e : projectiveLineProj k ≅ E.subscheme}
    (hE : E.IsExceptionalCurveOfFirstKind k e)
    (L : _root_.SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (X).sheaf)))
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    {n : ℤ} (hn : n ≤ 0)
    (hdeg : (modulePullback e.hom.toLRSHom.toShHom).obj
        ((modulePullback E.subschemeι.toLRSHom.toShHom).obj L) ≅
      ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) n) :
    Mono (((moduleGlobalSections X).rightDerived 1).map (tensorCanonicalSection E L))
```

**`Stacks.Surfaces.isZero_rightDerived_one_tensorInvertibleSheafPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveTwistVanishing.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Surfaces/ExceptionalCurveTwistVanishing.lean#L329). The attribute's comment: “assertion (1): vanishing through the twists of nonnegative degree”.

> **[Stacks, Tag 0C2J], assertion (1).** Let `E ⊆ X` be an exceptional curve of the first kind
> on a scheme `X`, let `ℒ` be an invertible `𝒪_X`-module, and let `n` be the degree of `ℒ|_E` as an
> invertible module on `𝐏¹`, recorded as an isomorphism `e^*i^*ℒ ≅ 𝒪(n)`. If `H¹(X, ℒ) = 0` and
> `n ≥ 0` then `H¹(X, ℒ(iE)) = 0` for every `0 ≤ i ≤ n + 1`.
>
> Here `ℒ(iE)` is `ℒ ⊗ 𝒪_X(iE)` with `iE = E ^ i` the `i`-fold sum of `E` with itself in the monoid
> of effective Cartier divisors.

```lean
theorem isZero_rightDerived_one_tensorInvertibleSheafPow (E : X.IdealSheafData) (k : Type u)
    [Field k] {e : projectiveLineProj k ≅ E.subscheme}
    (hE : E.IsExceptionalCurveOfFirstKind k e)
    (L : _root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf))
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    {n : ℤ} (_hn : 0 ≤ n)
    (hdeg : (modulePullback e.hom.toLRSHom.toShHom).obj
        ((modulePullback E.subschemeι.toLRSHom.toShHom).obj L) ≅
      ProjectiveSpectrum.Proj.twistingSheaf
        (MvPolynomial.homogeneousSubmodule (Fin 2) k) n)
    (h0 : IsZero (((moduleGlobalSections X).rightDerived 1).obj L))
    (i : ℕ) (hi : (i : ℤ) ≤ n + 1) :
    IsZero (((moduleGlobalSections X).rightDerived 1).obj
      (MonoidalCategory.tensorObj (C := _root_.SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf))
        L (invertibleSheaf' (E ^ i))))
```

## Tag 0C2M, a lemma

[Tag 0C2M](https://stacks.math.columbia.edu/tag/0C2M) in the Stacks Project.

**`AlgebraicGeometry.exists_contraction_isProper_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ContractExceptionalCurveAmple.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/ContractExceptionalCurveAmple.lean#L326).

> **[Stacks, Tag 0C2M].** Let `S = Spec R` be an affine Noetherian scheme, `f : X ⟶ S` a proper
> morphism, `ℒ` an ample invertible `𝒪_X`-module, and `E ⊆ X` an exceptional curve of the first
> kind, cut out by `D` and presented as `𝐏¹_k` by `e`. Then
>
> 1. there exists a contraction `b : X ⟶ X'` of `E`;
> 2. `X'` is proper over `S`: the structure morphism factors as `b ≫ f'` with `f'` proper;
> 3. the invertible `𝒪_{X'}`-module `ℒ'` of [Stacks, Remark 0C5M] is ample. Here `ℒ` has a degree
>    `n` on `E` (its restriction to `𝐏¹_k` is `𝒪(n)`), and `ℒ'` is an invertible `𝒪_{X'}`-module
>    with `b^*ℒ' = ℒ(nE)` in `Pic(X)`, i.e. `b^*[ℒ'] = [ℒ] + n • [𝒪_X(E)]`
>    (`AlgebraicGeometry.Scheme.IdealSheafData.exceptionalTwist`). Such an `ℒ'` exists, and every
>    such `ℒ'` is ample; it is unique up to isomorphism by
>    `AlgebraicGeometry.IsContractionOfExceptionalCurve.nonempty_iso_of_schemePullbackClass_eq`.

```lean
public theorem exists_contraction_isProper_isAmple {R : Type u} [CommRing R] [IsNoetherianRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IsProper f]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L] (hL : Scheme.Modules.IsAmple X L)
    {D : X.IdealSheafData} {k : Type u} [Field k] {e : projectiveLineProj k ≅ D.subscheme}
    (hE : D.IsExceptionalCurveOfFirstKind k e) :
    ∃ (X' : Scheme.{u}) (b : X ⟶ X'),
      IsContractionOfExceptionalCurve D b ∧
      (∃ f' : X' ⟶ Spec (.of R), b ≫ f' = f ∧ IsProper f') ∧
      (∃ n : ℤ, Nonempty ((modulePullback e.hom.toLRSHom.toShHom).obj
          ((modulePullback D.subschemeι.toLRSHom.toShHom).obj L) ≅
        ProjectiveSpectrum.Proj.twistingSheaf (MvPolynomial.homogeneousSubmodule (Fin 2) k) n)) ∧
      ∀ n : ℤ, Nonempty ((modulePullback e.hom.toLRSHom.toShHom).obj
          ((modulePullback D.subschemeι.toLRSHom.toShHom).obj L) ≅
        ProjectiveSpectrum.Proj.twistingSheaf (MvPolynomial.homogeneousSubmodule (Fin 2) k) n) →
        (∃ (L' : X'.Modules) (_ : Stacks.Ample.IsInvertibleModule X' L'),
          Stacks.Picard.schemePullbackClass b (cls L') =
            (haveI := hE.isEffectiveCartierDivisor; D.exceptionalTwist n (cls L))) ∧
        ∀ (L' : X'.Modules) [Stacks.Ample.IsInvertibleModule X' L'],
          Stacks.Picard.schemePullbackClass b (cls L') =
            (haveI := hE.isEffectiveCartierDivisor; D.exceptionalTwist n (cls L)) →
          Scheme.Modules.IsAmple X' L'
```

## Tag 0C2N, a lemma

[Tag 0C2N](https://stacks.math.columbia.edu/tag/0C2N) in the Stacks Project.

**`AlgebraicGeometry.exists_isContractionOfExceptionalCurve_isProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Contraction/ProjectiveContraction.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Contraction/ProjectiveContraction.lean#L409). The attribute's comment: “(1)”.

> **[Stacks, Tag 0C2N] (1).** Let `S` be a Noetherian scheme and `f : X ⟶ S` a morphism of
> finite type. Let `E ⊆ X` be an exceptional curve of the first kind, cut out by `D` and presented
> as `𝐏¹_k` by `e`, which lies in the fibre of `f` over a point `s`. If `X` is projective over `S`,
> then there exists a contraction `b : X ⟶ X'` of `E`, and `X'` is projective over `S`: the
> structure morphism factors as `b ≫ g` with `g` projective.

```lean
theorem exists_isContractionOfExceptionalCurve_isProjective {X S : Scheme.{u}} [IsNoetherian S]
    (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f] {D : X.IdealSheafData} {k : Type u}
    [Field k] {e : projectiveLineProj k ≅ D.subscheme} (hE : D.IsExceptionalCurveOfFirstKind k e)
    (s : S) (hs : ∀ x ∈ (D.support : Set X), f.base x = s) (hf : IsProjective f) :
    ∃ (X' : Scheme.{u}) (b : X ⟶ X') (g : X' ⟶ S),
      IsContractionOfExceptionalCurve D b ∧ b ≫ g = f ∧ IsProjective g
```

**`AlgebraicGeometry.exists_isContractionOfExceptionalCurve_isQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Contraction/QuasiProjectiveContraction.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/Contraction/QuasiProjectiveContraction.lean#L219). The attribute's comment: “(2)”.

> **[Stacks, Tag 0C2N] (2).** Let `S` be a Noetherian scheme and `f : X ⟶ S` a morphism of
> finite type. Let `E ⊆ X` be an exceptional curve of the first kind, cut out by `D` and presented
> as `𝐏¹_k` by `e`, which lies in the fibre of `f` over a point `s`. If `X` is quasi-projective over
> `S`, then there exists a contraction `b : X ⟶ X'` of `E`, and `X'` is quasi-projective over `S`:
> the structure morphism factors as `b ≫ g` with `g` quasi-projective.

```lean
theorem exists_isContractionOfExceptionalCurve_isQuasiProjective {X S : Scheme.{u}}
    [IsNoetherian S] (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    {D : X.IdealSheafData} {k : Type u} [Field k] {e : projectiveLineProj k ≅ D.subscheme}
    (hE : D.IsExceptionalCurveOfFirstKind k e) (s : S)
    (hs : ∀ x ∈ (D.support : Set X), f.base x = s) (hf : IsQuasiProjective f) :
    ∃ (X' : Scheme.{u}) (b : X ⟶ X') (g : X' ⟶ S),
      IsContractionOfExceptionalCurve D b ∧ b ≫ g = f ∧ IsQuasiProjective g
```

## Tag 0C5N, a lemma

[Tag 0C5N](https://stacks.math.columbia.edu/tag/0C5N) in the Stacks Project.

**`AlgebraicGeometry.isQuasiProjective_of_isRegular_of_topologicalKrullDim_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuasiProjectiveRegularSurface.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuasiProjectiveRegularSurface.lean#L193).

> **Stacks Project, Tag 0C5N.** Let `S` be a Noetherian scheme and `f : X ⟶ S` a separated
> morphism of finite type with `X` regular of dimension (at most) two. Then `f` is quasi-projective.
>
> The source assumes `dim X = 2`; the argument only uses `dim X ≤ 2`, which is what is assumed.

```lean
theorem isQuasiProjective_of_isRegular_of_topologicalKrullDim_le_two
    {X S : Scheme.{u}} [IsNoetherian S] (f : X ⟶ S) [IsSeparated f]
    [LocallyOfFiniteType f] [QuasiCompact f] (hreg : IsRegular X)
    (hdim : topologicalKrullDim X ≤ 2) : IsQuasiProjective f
```

## Tag 0C5P, a lemma

[Tag 0C5P](https://stacks.math.columbia.edu/tag/0C5P) in the Stacks Project.

**`AlgebraicGeometry.isProjective_of_isRegular_of_topologicalKrullDim_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuasiProjectiveRegularSurface.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuasiProjectiveRegularSurface.lean#L238). References: SGA 7 X (1.10), “more general”.

> **Stacks Project, Tag 0C5P.** Let `S` be a Noetherian scheme and `f : X ⟶ S` a proper morphism
> with `X` regular of dimension (at most) two. Then `f` is projective.
>
> This is [Stacks, Tag 0C5N] together with [Stacks, Tag 0BCL]: a proper quasi-projective morphism
> to a quasi-compact quasi-separated scheme is projective. The source assumes `dim X = 2`; the
> argument only uses `dim X ≤ 2`.

```lean
theorem isProjective_of_isRegular_of_topologicalKrullDim_le_two {X S : Scheme.{u}}
    [IsNoetherian S] (f : X ⟶ S) [IsProper f] (hreg : IsRegular X)
    (hdim : topologicalKrullDim X ≤ 2) : IsProjective f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.16, Tag 0C2I](https://stacks.math.columbia.edu/tag/0C2I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
