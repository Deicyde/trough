---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsBlowupAtClosedPoint, AlgebraicGeometry.Space.BlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.GlobalBlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.LocalBlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_localBlowupFactorization, AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_localBlowupFactorization_restrictionComponent, AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalBlowupFactorization_iff, AlgebraicGeometry.Space.exists_blowupFactorization_isPullbackDefined
statement: formalized
proof: formalized
---

# 89.4 Dominating by quadratic transformations

Section 89.4 of the Stacks Project, [Tag 0AHG](https://stacks.math.columbia.edu/tag/0AHG). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BHE, a definition

[Tag 0BHE](https://stacks.math.columbia.edu/tag/0BHE) in the Stacks Project.

**`AlgebraicGeometry.Space.IsBlowupAtClosedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean#L187).

> **Stacks 0BHE.** A morphism `f : Y ⟶ X` of algebraic spaces **is the blowing up of `X` at
> the closed point `z`** when there is a blowing up of `X` in the reduced closed subspace
> supported on `{z}` to which `f` is isomorphic over `X`.
>
> Being the blowing up in a closed subspace is the universal property of Stacks 085U, which is
> `AlgebraicGeometry.Space.IsBlowupAlong`; it already determines the morphism up to isomorphism
> over `X`, so asking for the isomorphism here changes nothing and makes
> `AlgebraicGeometry.Space.IsBlowupAtClosedPoint.comp_iso` available.  The centre is
> `AlgebraicGeometry.Space.closedPointSubspace`, which is the `i(Spec(k))` of the source by
> `AlgebraicGeometry.Space.eq_closedPointSubspace`.

```lean
def IsBlowupAtClosedPoint {X Y : AlgebraicSpaces B S hS} (z : points B S hS X.obj)
    (hz : IsClosed ({z} : Set (points B S hS X.obj))) (f : Y ⟶ X) : Prop
```

## Tag 0BHF, a lemma

[Tag 0BHF](https://stacks.math.columbia.edu/tag/0BHF) in the Stacks Project.

**`AlgebraicGeometry.Space.BlowupFactorization`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean#L397). The attribute's comment: “the condition asserted on both sides of the equivalence: a factorization of the given morphism as a finite sequence of blowings up at closed points lying over the given set of points. The equivalence itself is AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalBlowupFactorization_iff.”.

> **A factorization of `f : Y ⟶ X` as a sequence of blowings up at closed points lying over
> the set of points `T ⊆ |X|`**: a tower
>
> `Zₘ ⟶ Zₘ₋₁ ⟶ … ⟶ Z₁ ⟶ Z₀ = X`
>
> of blowings up at closed points, all of whose centres lie over `T`, together with an
> identification of `Y` with its top `Zₘ` under which `f` is the composite `Zₘ ⟶ X`.
>
> This is the condition on both sides of **Stacks 0BHF**, taken there with `T = {x₁, …, xₙ}` for
> the morphism to `X` and with `T = {uᵢ}` for the morphism to the `i`th étale neighborhood.

```lean
structure BlowupFactorization (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : AlgebraicSpaces B S hS} (T : Set (points B S hS X.obj)) (f : Y ⟶ X)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.GlobalBlowupFactorization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean#L491). The attribute's comment: “the condition on the morphism to X: it factors as a finite sequence of blowings up at closed points lying over x₁, …, xₙ”.

> **Stacks 0BHF**, the condition on the morphism to `X`: `f : Y ⟶ X` factors as
>
> `Y = Zₘ ⟶ Zₘ₋₁ ⟶ … ⟶ Z₁ ⟶ Z₀ = X`
>
> where each `Z_{j+1} ⟶ Z_j` is the blowing up of `Z_j` at a closed point `z_j` lying over
> `{x₁, …, xₙ}`.

```lean
abbrev GlobalBlowupFactorization {Y : AlgebraicSpaces B S hS} (f : Y ⟶ D.space)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.LocalBlowupFactorization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupsAtClosedPoints.lean#L503). The attribute's comment: “the condition on the morphism to the i-th étale neighborhood: it factors as a finite sequence of blowings up at closed points lying over uᵢ”.

> **Stacks 0BHF**, the condition on the morphism to the `i`th étale neighborhood:
> `gᵢ : Yᵢ ⟶ Uᵢ` factors as
>
> `Yᵢ = Z_{i, mᵢ} ⟶ … ⟶ Z_{i, 1} ⟶ Z_{i, 0} = Uᵢ`
>
> where each `Z_{i, j+1} ⟶ Z_{i, j}` is the blowing up of `Z_{i, j}` at a closed point lying over
> `uᵢ`.

```lean
abbrev LocalBlowupFactorization (i : Fin n) {Y : AlgebraicSpaces B S hS}
    (g : Y ⟶ D.neighborhoodSpace i)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_localBlowupFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupTowerEtaleRestriction.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupTowerEtaleRestriction.lean#L474). The attribute's comment: “the only-if direction: a factorization of f as a sequence of blowings up at closed points lying over x₁, …, xₙ gives, for each i, a factorization of its base change gᵢ as a sequence of blowings up at closed points lying over uᵢ. The if direction is AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalBlowupFactorization_of_isPullback and the equivalence itself is AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalBlowupFactorization_iff.”.

> **Stacks 0BHF, the "only if" direction.**  Let `X, xᵢ, Uᵢ ⟶ X, uᵢ` be as in Stacks 0BH9 and
> let `f : Y ⟶ X` be a morphism of algebraic spaces with base change `gᵢ : Yᵢ ⟶ Uᵢ` along
> `Uᵢ ⟶ X`.  If `f` factors as a finite sequence of blowings up at closed points lying over
> `{x₁, …, xₙ}`, then `gᵢ` factors as a finite sequence of blowings up at closed points lying
> over `uᵢ`.
>
> The sequence over `Uᵢ` is the base change of the given one, which is
> `AlgebraicGeometry.Space.ClosedPointNeighborhoods.exists_blowupTower_of_isPullback`.  No
> hypothesis on `f` beyond the cartesian square is used; in particular `f` need not be an
> isomorphism over `X ∖ {x₁, …, xₙ}`, so the statement is stronger than the source's, which fixes
> `f` in `C_{X, {x₁, …, xₙ}}`.

```lean
theorem nonempty_localBlowupFactorization {i : Fin n} {Y Y' : AlgebraicSpaces B S hS}
    {f : Y ⟶ D.space} {a : Y' ⟶ Y} {g : Y' ⟶ D.neighborhoodSpace i}
    (sq : IsPullback a g f (D.toSpaceHom i)) (F : D.GlobalBlowupFactorization f) :
    Nonempty (D.LocalBlowupFactorization i g)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_localBlowupFactorization_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupTowerEtaleRestriction.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupTowerEtaleRestriction.lean#L501). The attribute's comment: “the only-if direction at the functor F: a factorization of f as a sequence of blowings up at closed points lying over x₁, …, xₙ gives, for each i, a factorization of gᵢ = F(f)ᵢ as a sequence of blowings up at closed points lying over uᵢ. The if direction at F is nonempty_globalBlowupFactorization_restrictionComponent and the equivalence itself is AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalBlowupFactorization_iff.”.

> **Stacks 0BHF, the "only if" direction, for the functor `F` of Stacks 0BHA.**  Let
> `X, xᵢ, Uᵢ ⟶ X, uᵢ` be as in Stacks 0BH9 and let `f : Y ⟶ X` be an object of
> `C_{X, {x₁, …, xₙ}}` corresponding to `gᵢ : Yᵢ ⟶ Uᵢ` under `F`.  If `f` factors as a finite
> sequence of blowings up at closed points lying over `{x₁, …, xₙ}`, then for every `i` the
> morphism `gᵢ` factors as a finite sequence of blowings up at closed points lying over `uᵢ`.
>
> This is `AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_localBlowupFactorization` at
> the cartesian square of
> `AlgebraicGeometry.Space.ClosedPointNeighborhoods.isPullback_restrictionComponent_obj`, which is
> what "corresponds under `F`" means.

```lean
theorem nonempty_localBlowupFactorization_restrictionComponent
    (M : D.modificationsAwayFromPoints) (i : Fin n)
    (F : D.GlobalBlowupFactorization (ObjectProperty.homMk M.obj.hom :
      (⟨M.obj.left, M.property.1⟩ : AlgebraicSpaces B S hS) ⟶ D.space)) :
    Nonempty (D.LocalBlowupFactorization i (ObjectProperty.homMk
      ((D.restrictionComponent i).obj M).obj.hom :
      (⟨((D.restrictionComponent i).obj M).obj.left,
          ((D.restrictionComponent i).obj M).property.1⟩ : AlgebraicSpaces B S hS) ⟶
        D.neighborhoodSpace i))
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.nonempty_globalBlowupFactorization_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupTowerGlobalConverse.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BlowupTowerGlobalConverse.lean#L487).

> **Stacks 0BHF.**  Let `X, xᵢ, Uᵢ ⟶ X, uᵢ` be as in Stacks 0BH9 and let `f : Y ⟶ X` be an
> object of the category `C_{X, {x₁, …, xₙ}}` of Stacks 0BHA.  Then `f` factors as a finite
> sequence of blowings up at closed points lying over `{x₁, …, xₙ}` if and only if, for every
> `i`, the morphism `gᵢ = F(f)ᵢ` factors as a finite sequence of blowings up at closed points
> lying over `uᵢ`.
>
> The "only if" direction is `nonempty_localBlowupFactorization_restrictionComponent` and the
> "if" direction is `nonempty_globalBlowupFactorization_restrictionComponent`.

```lean
theorem nonempty_globalBlowupFactorization_iff (M : D.modificationsAwayFromPoints) :
    Nonempty (D.GlobalBlowupFactorization (ObjectProperty.homMk M.obj.hom :
        (⟨M.obj.left, M.property.1⟩ : AlgebraicSpaces B S hS) ⟶ D.space)) ↔
      ∀ i, Nonempty (D.LocalBlowupFactorization i (ObjectProperty.homMk
        ((D.restrictionComponent i).obj M).obj.hom :
        (⟨((D.restrictionComponent i).obj M).obj.left,
            ((D.restrictionComponent i).obj M).property.1⟩ : AlgebraicSpaces B S hS) ⟶
          D.neighborhoodSpace i))
```

## Tag 0BHG, a lemma

[Tag 0BHG](https://stacks.math.columbia.edu/tag/0BHG) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_blowupFactorization_isPullbackDefined`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrincipalizationAtClosedPoints.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PrincipalizationAtClosedPoints.lean#L159). The attribute's comment: “the induction producing the sequence of blowings up, granted the existence of the blowing up of an algebraic space at a closed point (0BHE, hence 084A/084B/085Q), the algebraic-space analogue of 0809, and the local splitting of 0AGT”.

> **Stacks 0BHG.** Let `S` be a scheme, let `X` be a Noetherian algebraic space over `S` and
> let `T ⊆ |X|` be a finite set of closed points `x` such that `X` is regular at `x` and the local
> ring of `X` at `x` has dimension `2`.  Let `ℐ ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals, given
> by the closed subspace `Z ⊆ X` it cuts out, such that `𝒪_X/ℐ` is supported on `T`, that is,
> `|Z| ⊆ T`.  **Then there is a sequence**
>
> `X_m ⟶ X_{m-1} ⟶ … ⟶ X_1 ⟶ X_0 = X`
>
> **where `X_{j+1} ⟶ X_j` is the blowing up of `X_j` at a closed point `x_j` lying above a point
> of `T`, such that `ℐ𝒪_{X_m}` is an invertible ideal sheaf** — that is, such that the inverse
> image of `Z` along the composite `X_m ⟶ X` is an effective Cartier divisor.
>
> Along the sequence produced, every effective Cartier divisor on `X` also has a defined
> pullback; that is the form in which the induction uses its own output and it is recorded in the
> conclusion.
>
> Three inputs are granted, since the library has them for schemes only: the existence of the
> blowing up of an algebraic space at a closed point (Stacks 0BHE, whose construction needs the
> relative `Proj` of Stacks 084A and 084B), the algebraic-space analogue of Stacks 0809, and the
> local splitting of Stacks 0AGT with respect to a colength function given as a parameter — the
> hypothesis which the scheme case, Stacks 0AHH, carries as well.  See the module
> documentation.

```lean
theorem exists_blowupFactorization_isPullbackDefined
    (colength : ∀ Y : AlgebraicSpaces B S hS,
      ClosedSubspaces B S hS Y.1 → Set (points B S hS Y.1) → ℕ∞)
    (blowupExists : ∀ (Y : AlgebraicSpaces B S hS) (y : points B S hS Y.1)
      (hy : IsClosed ({y} : Set (points B S hS Y.1))),
      ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ Y), IsBlowupAtClosedPoint B S hS y hy b)
    (pullbackOfEffectiveCartier : ∀ (Y Y' : AlgebraicSpaces B S hS) (y : points B S hS Y.1)
      (hy : IsClosed ({y} : Set (points B S hS Y.1))) (b : Y' ⟶ Y),
      IsBlowupAtClosedPoint B S hS y hy b →
      ∀ D : ClosedSubspaces B S hS Y.1, IsEffectiveCartierDivisor B S hS Y D →
        IsPullbackDefined B S hS b D)
    (splitting : ∀ (Y : AlgebraicSpaces B S hS) (T : Set (points B S hS Y.1)), T.Finite →
      (∀ y ∈ T, IsClosed ({y} : Set (points B S hS Y.1))) →
      (∀ y ∈ T, IsRegularAt B S hS Y.1 y) →
      (∀ y ∈ T, localRingDimension B S hS y = 2) →
      ∀ Z : ClosedSubspaces B S hS Y.1, subspacePointSet B S hS Y.1 Z.1 ⊆ T →
      ∀ y ∈ subspacePointSet B S hS Y.1 Z.1,
      ∀ (hy : IsClosed ({y} : Set (points B S hS Y.1))) (Y' : AlgebraicSpaces B S hS)
        (b : Y' ⟶ Y), IsBlowupAtClosedPoint B S hS y hy b →
        ∃ (E Z' : ClosedSubspaces B S hS Y'.1) (T' : Set (points B S hS Y'.1)),
          preimageClosedSubspace b Z = sumClosedSubspaces B S hS Y' E Z' ∧
          IsEffectiveCartierDivisor B S hS Y' E ∧
          T'.Finite ∧
          (∀ z ∈ T', IsClosed ({z} : Set (points B S hS Y'.1))) ∧
          (∀ z ∈ T', IsRegularAt B S hS Y'.1 z) ∧
          (∀ z ∈ T', localRingDimension B S hS z = 2) ∧
          (∀ z ∈ T', pointsMap B S hS Y'.1 b.hom z ∈ T) ∧
          subspacePointSet B S hS Y'.1 Z'.1 ⊆ T' ∧
          colength Y' Z' T' < colength Y Z T)
    (hterm : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (_hX : IsNoetherian B S hS hterm X.1)
    (T : Set (points B S hS X.1)) (hTfinite : T.Finite)
    (hTclosed : ∀ x ∈ T, IsClosed ({x} : Set (points B S hS X.1)))
    (hTregular : ∀ x ∈ T, IsRegularAt B S hS X.1 x)
    (hTdim : ∀ x ∈ T, localRingDimension B S hS x = 2)
    (Z : ClosedSubspaces B S hS X.1)
    (hZsupport : subspacePointSet B S hS X.1 Z.1 ⊆ T) :
    ∃ (Y : AlgebraicSpaces B S hS) (f : Y ⟶ X),
      Nonempty (BlowupFactorization B S hS T f) ∧
        IsPullbackDefined B S hS f Z ∧
        ∀ D : ClosedSubspaces B S hS X.1, IsEffectiveCartierDivisor B S hS X D →
          IsPullbackDefined B S hS f D
```

**`AlgebraicGeometry.Space.exists_blowupFactorization_isPullbackDefined_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PrincipalizationAtClosedPointsUnconditional.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PrincipalizationAtClosedPointsUnconditional.lean#L266).

> Let `S` be a scheme, let `X` be a Noetherian algebraic space over `S` and let `T ⊆ |X|` be a
> finite set of closed points `x` such that `X` is regular at `x` and the local ring of `X` at `x`
> has dimension `2`. Let `ℐ ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals, given by the closed
> subspace `Z ⊆ X` it cuts out, such that `𝒪_X/ℐ` is supported on `T`, that is, `|Z| ⊆ T`. **Then
> there is a sequence**
>
> `X_m ⟶ X_{m-1} ⟶ … ⟶ X_1 ⟶ X_0 = X`
>
> **where `X_{j+1} ⟶ X_j` is the blowing up of `X_j` at a closed point `x_j` lying above a point
> of `T`, such that `ℐ𝒪_{X_m}` is an invertible ideal sheaf** — that is, such that the inverse
> image of `Z` along the composite `X_m ⟶ X` is an effective Cartier divisor.

```lean
theorem exists_blowupFactorization_isPullbackDefined_of_isNoetherian
    (hterm : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hX : IsNoetherian B S hS hterm X.1)
    (T : Set (points B S hS X.1)) (hTfinite : T.Finite)
    (hTclosed : ∀ x ∈ T, IsClosed ({x} : Set (points B S hS X.1)))
    (hTregular : ∀ x ∈ T, IsRegularAt B S hS X.1 x)
    (hTdim : ∀ x ∈ T, localRingDimension B S hS x = 2)
    (Z : ClosedSubspaces B S hS X.1)
    (hZsupport : subspacePointSet B S hS X.1 Z.1 ⊆ T) :
    ∃ (Y : AlgebraicSpaces B S hS) (f : Y ⟶ X),
      Nonempty (BlowupFactorization B S hS T f) ∧ IsPullbackDefined B S hS f Z
```

## Tag 0BHH, a lemma

[Tag 0BHH](https://stacks.math.columbia.edu/tag/0BHH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_blowupFactorization_factors_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DominationByPointBlowups.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DominationByPointBlowups.lean#L91).

> **Dominating a modification by blowing up closed points.** Let `S` be a scheme, let `X` be a
> Noetherian algebraic space over `S` and let `T ⊆ |X|` be a finite set of closed points `x` such
> that `X` is regular at `x` and the local ring of `X` at `x` has dimension `2`. Let `f : Y ⟶ X` be
> a proper morphism of algebraic spaces which is an isomorphism over `U = X ∖ T`. **Then there
> exist a sequence**
>
> `X_n ⟶ X_{n-1} ⟶ … ⟶ X_1 ⟶ X_0 = X`
>
> **where `X_{i+1} ⟶ X_i` is the blowing up of `X_i` at a closed point `x_i` lying above a point
> of `T`, and a factorization `X_n ⟶ Y ⟶ X` of the composition.**

```lean
theorem exists_blowupFactorization_factors_of_isProper
    (hterm : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hX : IsNoetherian B S hS hterm X.1)
    (T : Set (points B S hS X.1)) (hTfinite : T.Finite)
    (hTclosed : ∀ x ∈ T, IsClosed ({x} : Set (points B S hS X.1)))
    (hTregular : ∀ x ∈ T, IsRegularAt B S hS X.1 x)
    (hTdim : ∀ x ∈ T, localRingDimension B S hS x = 2)
    (Y : AlgebraicSpaces B S hS) (f : Y ⟶ X) (hf : IsProper B S hS f.hom)
    (hfU : IsIso (pullback.snd f.hom (openSubspaceOfPoints B S hS X.1 Tᶜ).ι)) :
    ∃ (X' : AlgebraicSpaces B S hS) (b : X' ⟶ X),
      Nonempty (BlowupFactorization B S hS T b) ∧ ∃ h : X' ⟶ Y, h ≫ f = b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.4, Tag 0AHG](https://stacks.math.columbia.edu/tag/0AHG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
