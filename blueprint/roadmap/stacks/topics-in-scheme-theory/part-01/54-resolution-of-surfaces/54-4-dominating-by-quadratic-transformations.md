---
declaration: section
origin: cited
lean: Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_isEffectiveCartierDivisor, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_principalizing, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_factorization, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_factorization_of_isProper, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_resolving_partialMap, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_resolving_partialMap_of_dim_two
statement: formalized
proof: formalized
---

# 54.4 Dominating by quadratic transformations

Section 54.4 of the Stacks Project, [Tag 0BFS](https://stacks.math.columbia.edu/tag/0BFS). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AHH, a lemma

[Tag 0AHH](https://stacks.math.columbia.edu/tag/0AHH) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChain.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChain.lean#L157). The attribute's comment: “the induction on the total colength, granted the local splitting of Tag 0AGT”.

> **Stacks Project, Tag 0AHH**, the induction on the total colength. Let `T` be a finite set of
> closed points of a scheme `X` whose local rings are regular of dimension two, and let `I` be a
> quasi-coherent sheaf of ideals whose quotient is supported on `T`. Assume that at every point `y`
> of the support of such an ideal the pulled-back ideal splits as `dE + I'` for the exceptional
> divisor `E` of the blowup at `y` and an ideal `I'` again supported on a finite set of closed
> points with regular two-dimensional local rings lying over `T` and of strictly smaller total
> colength — the local statement of Tag 0AGT. Then there is a sequence of blowups at closed points
> lying over `T` along which `I` becomes an invertible sheaf of ideals.

```lean
public theorem exists_pointBlowupChain_isEffectiveCartierDivisor
    (descent : ∀ (Y : Scheme.{u}) (S : Finset Y) (J : Y.IdealSheafData),
      (∀ y ∈ S, IsClosed ({y} : Set Y)) →
      (∀ y ∈ S, IsRegularLocalRing (Y.presheaf.stalk y)) →
      (∀ y ∈ S, ringKrullDim (Y.presheaf.stalk y) = 2) →
      (J.support : Set Y) ⊆ (S : Set Y) →
      ∀ y ∈ (J.support : Set Y), ∀ hy : IsClosed ({y} : Set Y),
      ∀ M : Y.IdealSheafData, M = Scheme.IdealSheafData.vanishingIdeal ⟨{y}, hy⟩ →
        ∃ (d : ℕ) (S' : Finset (blowUp M)) (J' : (blowUp M).IdealSheafData),
          exceptionalIdeal M ^ d * J' = J.comap (blowUpToBase M) ∧
          (∀ z ∈ S', IsClosed ({z} : Set (blowUp M))) ∧
          (∀ z ∈ S', IsRegularLocalRing ((blowUp M).presheaf.stalk z)) ∧
          (∀ z ∈ S', ringKrullDim ((blowUp M).presheaf.stalk z) = 2) ∧
          (J'.support : Set (blowUp M)) ⊆ (S' : Set (blowUp M)) ∧
          (∀ z ∈ S', (blowUpToBase M).base z ∈ S) ∧
          totalColength J' S' < totalColength J S)
    {X : Scheme.{u}} (T : Finset X)
    (hclosed : ∀ x ∈ T, IsClosed ({x} : Set X))
    (hregular : ∀ x ∈ T, IsRegularLocalRing (X.presheaf.stalk x))
    (hdim : ∀ x ∈ T, ringKrullDim (X.presheaf.stalk x) = 2)
    (I : X.IdealSheafData) (hI : (I.support : Set X) ⊆ (T : Set X)) :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ X), PointBlowupChain X (T : Set X) Y f ∧
      Stacks.Divisors.IsEffectiveCartierDivisor (I.comap f)
```

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_principalizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupPrincipalization.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupPrincipalization.lean#L62). The attribute's comment: “a quasi-coherent ideal sheaf whose quotient is supported on a finite set of closed points with regular two-dimensional local rings becomes invertible after a finite sequence of blowups at closed points lying over that set; stated for an arbitrary scheme”.

> **Stacks Project, Tag 0AHH.** Let `X` be a scheme and `T` a finite set of closed points `x`
> of `X` such that `𝒪_{X,x}` is regular of dimension two for `x ∈ T`. Let `𝓘` be a quasi-coherent
> sheaf of ideals such that `𝒪_X / 𝓘` is supported on `T`. Then there is a sequence
> `Xₙ → Xₙ₋₁ → ⋯ → X₁ → X₀ = X` in which each `Xᵢ₊₁ → Xᵢ` is the blowing up of `Xᵢ` at a closed
> point lying over a point of `T`, such that `𝓘𝒪_{Xₙ}` is an invertible ideal sheaf.
>
> The source assumes `X` Noetherian; the statement holds without it.

```lean
public theorem exists_pointBlowupChain_principalizing {X : Scheme.{u}} (T : Finset X)
    (hclosed : ∀ x ∈ T, IsClosed ({x} : Set X))
    (hregular : ∀ x ∈ T, IsRegularLocalRing (X.presheaf.stalk x))
    (hdim : ∀ x ∈ T, ringKrullDim (X.presheaf.stalk x) = 2)
    (I : X.IdealSheafData) (hI : (I.support : Set X) ⊆ (T : Set X)) :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ X), PointBlowupChain X (T : Set X) Y f ∧
      Stacks.Divisors.IsEffectiveCartierDivisor (I.comap f)
```

## Tag 0AHI, a lemma

[Tag 0AHI](https://stacks.math.columbia.edu/tag/0AHI) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChain.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChain.lean#L230). The attribute's comment: “granted Tag 081T and the local splitting of Tag 0AGT”.

> **Stacks Project, Tag 0AHI.** Let `X` be a Noetherian scheme, let `T` be a finite set of
> closed points of `X` whose local rings are regular of dimension two, and let `U` be the
> complement of `T`. A proper morphism `f : Y ⟶ X` which is an isomorphism over `U` is dominated by
> a sequence `Xₙ → … → X₁ → X` of blowups at closed points lying over `T`, in the sense that the
> composite `Xₙ ⟶ X` factors through `f`.
>
> Two statements are threaded through as hypotheses rather than discharged: the local splitting of
> [Stacks, Tag 0AGT] that the formalized form of [Stacks, Tag 0AHH] consumes, and the dominating
> `U`-admissible blowup of [Stacks, Tag 081T].

```lean
public theorem exists_pointBlowupChain_factorization
    (descent : ∀ (Y : Scheme.{u}) (S : Finset Y) (J : Y.IdealSheafData),
      (∀ y ∈ S, IsClosed ({y} : Set Y)) →
      (∀ y ∈ S, IsRegularLocalRing (Y.presheaf.stalk y)) →
      (∀ y ∈ S, ringKrullDim (Y.presheaf.stalk y) = 2) →
      (J.support : Set Y) ⊆ (S : Set Y) →
      ∀ y ∈ (J.support : Set Y), ∀ hy : IsClosed ({y} : Set Y),
      ∀ M : Y.IdealSheafData, M = Scheme.IdealSheafData.vanishingIdeal ⟨{y}, hy⟩ →
        ∃ (d : ℕ) (S' : Finset (blowUp M)) (J' : (blowUp M).IdealSheafData),
          exceptionalIdeal M ^ d * J' = J.comap (blowUpToBase M) ∧
          (∀ z ∈ S', IsClosed ({z} : Set (blowUp M))) ∧
          (∀ z ∈ S', IsRegularLocalRing ((blowUp M).presheaf.stalk z)) ∧
          (∀ z ∈ S', ringKrullDim ((blowUp M).presheaf.stalk z) = 2) ∧
          (J'.support : Set (blowUp M)) ⊆ (S' : Set (blowUp M)) ∧
          (∀ z ∈ S', (blowUpToBase M).base z ∈ S) ∧
          totalColength J' S' < totalColength J S)
    {X Y : Scheme.{u}} [AlgebraicGeometry.IsNoetherian X] (T : Finset X) (U : X.Opens)
    (hU : (U : Set X) = (T : Set X)ᶜ)
    (hclosed : ∀ x ∈ T, IsClosed ({x} : Set X))
    (hregular : ∀ x ∈ T, IsRegularLocalRing (X.presheaf.stalk x))
    (hdim : ∀ x ∈ T, ringKrullDim (X.presheaf.stalk x) = 2)
    (f : Y ⟶ X) [IsProper f] [IsIso (f ∣_ U)]
    (dominated : ∃ (X' : Scheme.{u}) (b : X' ⟶ X),
      Stacks.Blowup.IsAdmissibleBlowup U b ∧ ∃ h : X' ⟶ Y, h ≫ f = b) :
    ∃ (Z : Scheme.{u}) (p : Z ⟶ X), PointBlowupChain X (T : Set X) Z p ∧
      ∃ g : Z ⟶ Y, g ≫ f = p
```

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_factorization_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChainDominating.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChainDominating.lean#L102).

> A proper morphism to a Noetherian scheme which is an isomorphism away from a finite set `T`
> of closed points whose local rings are regular of dimension two is dominated by a sequence of
> blowups at closed points lying over `T`: the composite of the sequence factors through it.

```lean
theorem exists_pointBlowupChain_factorization_of_isProper {X Y : Scheme.{u}}
    [AlgebraicGeometry.IsNoetherian X] (T : Finset X) (U : X.Opens)
    (hU : (U : Set X) = (T : Set X)ᶜ)
    (hclosed : ∀ x ∈ T, IsClosed ({x} : Set X))
    (hregular : ∀ x ∈ T, IsRegularLocalRing (X.presheaf.stalk x))
    (hdim : ∀ x ∈ T, ringKrullDim (X.presheaf.stalk x) = 2)
    (f : Y ⟶ X) [IsProper f] [IsIso (f ∣_ U)] :
    ∃ (Z : Scheme.{u}) (p : Z ⟶ X), PointBlowupChain X (T : Set X) Z p ∧
      ∃ g : Z ⟶ Y, g ≫ f = p
```

## Tag 0C5H, a lemma

[Tag 0C5H](https://stacks.math.columbia.edu/tag/0C5H) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_resolving_partialMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/DominateRationalMap.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/DominateRationalMap.lean#L98). The attribute's comment: “granted hypotheses descent (the local splitting of Tag 0AGT), domination (Tag 0AHI, exists_pointBlowupChain_factorization) and reduction (the Tag 0BX7 enlargement of the domain to a cofinite open, bundled with Tag 081T for that open)”.

> **Stacks Project, Tag 0C5H.** Let `S` be a scheme, let `X` be a scheme over `S` all of whose
> local rings are regular, and let `Y` be proper over `S`. Given an `S`-rational map from `X` to
> `Y`, displayed on the dense open `f.domain`, there is a chain of blowups at closed points not
> lying over `f.domain`, with composite `p : Z ⟶ X`, and an `S`-morphism `h : Z ⟶ Y` which agrees
> with the rational map over `f.domain`.
>
> Three inputs are hypotheses rather than theorems here: `descent`, the local splitting of
> [Stacks, Tag 0AGT] in the shape the library's [Stacks, Tag 0AHH] consumes; `domination`,
> [Stacks, Tag 0AHI]; and `reduction`, the source's reduction to a domain containing every
> codimension-one point, resting on [Stacks, Tag 0BX7], bundled with the dominating
> `U`-admissible blowup of [Stacks, Tag 081T] for the enlarged domain.

```lean
public theorem exists_pointBlowupChain_resolving_partialMap
    (descent : ∀ (A : Scheme.{u}) (W : Finset A) (J : A.IdealSheafData),
      (∀ y ∈ W, IsClosed ({y} : Set A)) →
      (∀ y ∈ W, IsRegularLocalRing (A.presheaf.stalk y)) →
      (∀ y ∈ W, ringKrullDim (A.presheaf.stalk y) = 2) →
      (J.support : Set A) ⊆ (W : Set A) →
      ∀ y ∈ (J.support : Set A), ∀ hy : IsClosed ({y} : Set A),
      ∀ M : A.IdealSheafData, M = Scheme.IdealSheafData.vanishingIdeal ⟨{y}, hy⟩ →
        ∃ (d : ℕ) (W' : Finset (blowUp M)) (J' : (blowUp M).IdealSheafData),
          exceptionalIdeal M ^ d * J' = J.comap (blowUpToBase M) ∧
          (∀ z ∈ W', IsClosed ({z} : Set (blowUp M))) ∧
          (∀ z ∈ W', IsRegularLocalRing ((blowUp M).presheaf.stalk z)) ∧
          (∀ z ∈ W', ringKrullDim ((blowUp M).presheaf.stalk z) = 2) ∧
          (J'.support : Set (blowUp M)) ⊆ (W' : Set (blowUp M)) ∧
          (∀ z ∈ W', (blowUpToBase M).base z ∈ W) ∧
          totalColength J' W' < totalColength J W)
    (domination : ∀ (_descent : ∀ (A : Scheme.{u}) (W : Finset A) (J : A.IdealSheafData),
        (∀ y ∈ W, IsClosed ({y} : Set A)) →
        (∀ y ∈ W, IsRegularLocalRing (A.presheaf.stalk y)) →
        (∀ y ∈ W, ringKrullDim (A.presheaf.stalk y) = 2) →
        (J.support : Set A) ⊆ (W : Set A) →
        ∀ y ∈ (J.support : Set A), ∀ hy : IsClosed ({y} : Set A),
        ∀ M : A.IdealSheafData, M = Scheme.IdealSheafData.vanishingIdeal ⟨{y}, hy⟩ →
          ∃ (d : ℕ) (W' : Finset (blowUp M)) (J' : (blowUp M).IdealSheafData),
            exceptionalIdeal M ^ d * J' = J.comap (blowUpToBase M) ∧
            (∀ z ∈ W', IsClosed ({z} : Set (blowUp M))) ∧
            (∀ z ∈ W', IsRegularLocalRing ((blowUp M).presheaf.stalk z)) ∧
            (∀ z ∈ W', ringKrullDim ((blowUp M).presheaf.stalk z) = 2) ∧
            (J'.support : Set (blowUp M)) ⊆ (W' : Set (blowUp M)) ∧
            (∀ z ∈ W', (blowUpToBase M).base z ∈ W) ∧
            totalColength J' W' < totalColength J W),
      ∀ {A B : Scheme.{u}} [AlgebraicGeometry.IsNoetherian A] (T : Finset A)
      (V : A.Opens), (V : Set A) = (T : Set A)ᶜ →
      (∀ x ∈ T, IsClosed ({x} : Set A)) →
      (∀ x ∈ T, IsRegularLocalRing (A.presheaf.stalk x)) →
      (∀ x ∈ T, ringKrullDim (A.presheaf.stalk x) = 2) →
      ∀ (q : B ⟶ A) [IsProper q] [IsIso (q ∣_ V)],
      (∃ (A' : Scheme.{u}) (b : A' ⟶ A), Stacks.Blowup.IsAdmissibleBlowup V b ∧
          ∃ h : A' ⟶ B, h ≫ q = b) →
        ∃ (Z : Scheme.{u}) (r : Z ⟶ A), PointBlowupChain A (T : Set A) Z r ∧
          ∃ s : Z ⟶ B, s ≫ q = r)
    {S X Y : Scheme.{u}} [X.Over S] [Y.Over S] [AlgebraicGeometry.IsNoetherian X]
    [IsProper (Y ↘ S)] (hreg : ∀ x : X, IsRegularLocalRing (X.presheaf.stalk x))
    (f : X.PartialMap Y) [f.IsOver S]
    (reduction : ∃ (T : Finset X) (V : X.Opens) (hle : f.domain ≤ V)
      (g : (V : Scheme.{u}) ⟶ Y),
      (V : Set X) = (T : Set X)ᶜ ∧
      (∀ x ∈ T, IsClosed ({x} : Set X)) ∧
      (∀ x ∈ T, ringKrullDim (X.presheaf.stalk x) = 2) ∧
      g ≫ (Y ↘ S) = V.ι ≫ (X ↘ S) ∧
      X.homOfLE hle ≫ g = f.hom ∧
      ∀ {B : Scheme.{u}} (q : B ⟶ X) [IsProper q] [IsIso (q ∣_ V)],
        ∃ (A' : Scheme.{u}) (b : A' ⟶ X), Stacks.Blowup.IsAdmissibleBlowup V b ∧
          ∃ h : A' ⟶ B, h ≫ q = b) :
    ∃ (Z : Scheme.{u}) (p : Z ⟶ X) (h : Z ⟶ Y),
      PointBlowupChain X ((f.domain : Set X)ᶜ) Z p ∧
        h ≫ (Y ↘ S) = p ≫ (X ↘ S) ∧
          pullback.fst p f.domain.ι ≫ h = pullback.snd p f.domain.ι ≫ f.hom
```

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_resolving_partialMap_of_dim_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/DominateRationalMapDimTwo.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/DominateRationalMapDimTwo.lean#L145).

> **Stacks Project, Tag 0C5H.** Let `S` be a scheme, let `X` be a regular Noetherian scheme
> over `S` of dimension two, and let `Y` be proper over `S`. Given an `S`-rational map from `X` to
> `Y`, displayed on the dense open `f.domain`, there is a chain of blowups at closed points not
> lying over `f.domain`, with composite `p : Z ⟶ X`, and an `S`-morphism `h : Z ⟶ Y` which agrees
> with the rational map over `f.domain`.

```lean
public theorem exists_pointBlowupChain_resolving_partialMap_of_dim_two
    {S X Y : Scheme.{u}} [X.Over S] [Y.Over S] [AlgebraicGeometry.IsNoetherian X]
    [IsProper (Y ↘ S)] (hreg : ∀ x : X, IsRegularLocalRing (X.presheaf.stalk x))
    (hdim : topologicalKrullDim X = 2) (f : X.PartialMap Y) [f.IsOver S] :
    ∃ (Z : Scheme.{u}) (p : Z ⟶ X) (h : Z ⟶ Y),
      PointBlowupChain X ((f.domain : Set X)ᶜ) Z p ∧
        h ≫ (Y ↘ S) = p ≫ (X ↘ S) ∧
          pullback.fst p f.domain.ι ≫ h = pullback.snd p f.domain.ι ≫ f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.4, Tag 0BFS](https://stacks.math.columbia.edu/tag/0BFS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
