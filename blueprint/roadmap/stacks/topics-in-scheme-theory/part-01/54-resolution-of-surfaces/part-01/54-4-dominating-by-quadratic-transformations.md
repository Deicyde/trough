---
declaration: section
origin: cited
lean: Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_principalizing, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_factorization_of_isProper, Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_resolving_partialMap_of_dim_two
statement: formalized
proof: formalized
---

# 54.4 Dominating by quadratic transformations

Section 54.4 of the Stacks Project, [Tag 0BFS](https://stacks.math.columbia.edu/tag/0BFS). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AHH, a lemma

[Tag 0AHH](https://stacks.math.columbia.edu/tag/0AHH) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_principalizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupPrincipalization.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupPrincipalization.lean#L73). The attribute's comment: “a quasi-coherent ideal sheaf whose quotient is supported on a finite set of closed points with regular two-dimensional local rings becomes invertible after a finite sequence of blowups at closed points lying over that set; stated for an arbitrary scheme”.

> **Stacks Project, Tag 0AHH.** Let `X` be a scheme and `T` a finite set of closed points `x`
> of `X` such that `𝒪_{X,x}` is regular of dimension two for `x ∈ T`. Let `𝓘` be a quasi-coherent
> sheaf of ideals such that `𝒪_X / 𝓘` is supported on `T`. Then there is a sequence
> `Xₙ → Xₙ₋₁ → ⋯ → X₁ → X₀ = X` in which each `Xᵢ₊₁ → Xᵢ` is the blowing up of `Xᵢ` at a closed
> point lying over a point of `T`, such that `𝓘𝒪_{Xₙ}` is an invertible ideal sheaf.
>
> The source assumes `X` Noetherian; the statement holds without it, since the finiteness the
> argument uses is that of the local rings at the points of `T`, which regularity provides.
>
> The proof is the source's induction on the total colength `Σ length(𝒪_{X,x} / 𝓘_x)`
> (`Stacks.ResolutionOfSurfaces.totalColength`), run by
> `Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_isEffectiveCartierDivisor`. Its inductive
> step is `Stacks.ResolutionOfSurfaces.pointBlowupDescent`: blowing up a point of the support writes
> the pulled-back ideal as `𝒪(-dE) · 𝓘'` with `𝓘'` of strictly smaller total colength, by
> [Stacks, Tag 0AGT] and flat base change ([Stacks, Tag 0805]). The resulting ideal is invertible
> as a product of the pulled-back exceptional divisor
> (`PointBlowupChain.isEffectiveCartierDivisor_comap`, [Stacks, Tag 0809]) and an invertible ideal
> ([Stacks, Tag 01WU]).

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

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_factorization_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChainDominating.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/PointBlowupChainDominating.lean#L112). The attribute's comment: “a proper morphism to a Noetherian scheme which is an isomorphism away from a finite set of closed points with regular two-dimensional local rings is dominated by a finite sequence of blowups at closed points lying over that set”.

> **Stacks Project, Tag 0AHI.** A proper morphism to a Noetherian scheme which is an
> isomorphism away from a finite set `T` of closed points whose local rings are regular of dimension
> two is dominated by a sequence of blowups at closed points lying over `T`: the composite of the
> sequence factors through it.
>
> The proof follows the source. By [Stacks, Tag 081T]
> (`exists_isAdmissibleBlowup_dominating_of_isNoetherian`) a `U`-admissible blowup of `X` in an
> ideal `𝓘` with `𝒪_X / 𝓘` supported on `T` dominates `f`. By [Stacks, Tag 0AHH]
> (`exists_pointBlowupChain_isEffectiveCartierDivisor` with `pointBlowupDescent`) a sequence of
> blowups at closed points over `T` makes `𝓘` invertible, and the universal property of blowing up
> ([Stacks, Tag 0806]) factors the composite through the blowup in `𝓘`, hence through `Y`.

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

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_resolving_partialMap_of_dim_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/DominateRationalMapDimTwo.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/QuadraticTransformations/DominateRationalMapDimTwo.lean#L156). The attribute's comment: “corrected: X is also assumed quasi-compact ([IsNoetherian X], regularity giving local Noetherianity); the source's statement is false without it, see errata.md entry 0C5H”.

> **Stacks Project, Tag 0C5H.** Let `S` be a scheme, let `X` be a regular Noetherian scheme
> over `S` of dimension two, and let `Y` be proper over `S`. Given an `S`-rational map from `X` to
> `Y`, displayed on the dense open `f.domain`, there is a chain of blowups at closed points not
> lying over `f.domain`, with composite `p : Z ⟶ X`, and an `S`-morphism `h : Z ⟶ Y` which agrees
> with the rational map over `f.domain`.
>
> The source does not assume `X` quasi-compact, and without that the statement is false (see
> `errata.md`, entry 0C5H); `[IsNoetherian X]` adds exactly quasi-compactness to regularity.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
