---
declaration: section
origin: cited
lean: AlgebraicGeometry.topologicalKrullDim_projectiveSpaceOverRing, AlgebraicGeometry.projectiveSpaceOver.smooth, AlgebraicGeometry.isProjectiveMorphism_projectiveSpaceOver, AlgebraicGeometry.projectiveSpaceOverRing.isVariety, AlgebraicGeometry.add_le_add_topologicalKrullDim_irreducibleComponent_inter, AlgebraicGeometry.inter_nonempty_projectiveSpaceOverRing, AlgebraicGeometry.le_topologicalKrullDim_inter_projectiveSpaceOverRing, AlgebraicGeometry.ProjectiveSpectrum.Proj.projectiveSpace_idealOfClosedSubscheme_isPrincipal_of_dimension
statement: formalized
proof: formalized
---

# 33.34 Projective space

Section 33.34 of the Stacks Project, [Tag 0B2N](https://stacks.math.columbia.edu/tag/0B2N). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B2P, a lemma

[Tag 0B2P](https://stacks.math.columbia.edu/tag/0B2P) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_projectiveSpaceOverRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Dimension/OverField.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/Dimension/OverField.lean#L36). The attribute's comment: “projective\_space\_dimension”.

> **Stacks Project, Tag 0B2P (dimension).** Projective `n`-space over a field has Krull
> dimension `n` as a topological space.

```lean
theorem topologicalKrullDim_projectiveSpaceOverRing (k : Type u) [Field k] (n : ℕ) :
    topologicalKrullDim (projectiveSpaceOverRing n (CommRingCat.of k)) = (n : WithBot ℕ∞)
```

**`AlgebraicGeometry.projectiveSpaceOver.smooth`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean#L93). The attribute's comment: “projective\_space\_smooth”. References: EGA IV (17.3.9), “free E, P^n\_S”.

> **Stacks Project, Tag 0B2P (smoothness).** Projective `n`-space over a scheme `S` is smooth
> over `S`, being the base change of the integral model, which is smooth over the terminal
> scheme.

```lean
public instance smooth (n : ℕ) (S : Scheme.{u}) : Smooth (projectiveSpaceOver n S ↘ S)
```

**`AlgebraicGeometry.isProjectiveMorphism_projectiveSpaceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean#L106). The attribute's comment: “projective\_space\_projective”.

> **Stacks Project, Tag 0B2P (projectivity).** Projective `n`-space over a scheme `S` is
> projective over `S`: the identity is a closed immersion of `ℙⁿ_S` into `ℙⁿ_S` over `S`.

```lean
public theorem isProjectiveMorphism_projectiveSpaceOver (n : ℕ) (S : Scheme.{u}) :
    IsProjectiveMorphism (projectiveSpaceOver n S ↘ S)
```

**`AlgebraicGeometry.projectiveSpaceOverRing.isVariety`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/SmoothProjectiveVariety.lean#L153). The attribute's comment: “projective\_space\_variety”.

> **Stacks Project, Tag 0B2P (variety).** Projective `n`-space over a field is a variety over
> that field: it is integral, and its structure morphism is separated and of finite type because it
> is proper, and quasi-compact because projective space is quasi-compact.

```lean
public instance isVariety (k : Type u) [Field k] (n : ℕ) :
    IsVariety k (projectiveSpaceOverRing n (CommRingCat.of k) ↘ Spec (CommRingCat.of k))
```

## Tag 0B2Q, a lemma

[Tag 0B2Q](https://stacks.math.columbia.edu/tag/0B2Q) in the Stacks Project.

**`AlgebraicGeometry.add_le_add_topologicalKrullDim_irreducibleComponent_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/AffineIntersection.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/AffineIntersection.lean#L464).

> **Stacks Project, Tag 0B2Q.** Let `k` be a field and let `Xs` and `Ys` be closed subsets of
> affine `n`-space over `k`, that is, of the prime spectrum of `MvPolynomial (Fin n) k`. If `Xs`
> and `Ys` are equidimensional of dimensions `r` and `s`, then every irreducible component `Z` of
> `Xs ∩ Ys` satisfies `r + s ≤ n + dim Z`, that is, has dimension at least `r + s - n`.

```lean
theorem add_le_add_topologicalKrullDim_irreducibleComponent_inter (k : Type u) [Field k]
    (n r s : ℕ) (Xs Ys : Set (PrimeSpectrum (MvPolynomial (Fin n) k)))
    (hXc : IsClosed Xs) (hYc : IsClosed Ys)
    (hXe : Equidimensional Xs) (hYe : Equidimensional Ys)
    (hXd : topologicalKrullDim Xs = r) (hYd : topologicalKrullDim Ys = s)
    (Z : Set ↥(Xs ∩ Ys)) (hZ : Z ∈ irreducibleComponents ↥(Xs ∩ Ys)) :
    (r : WithBot ℕ∞) + s ≤ n + topologicalKrullDim Z
```

## Tag 0B2R, a lemma

[Tag 0B2R](https://stacks.math.columbia.edu/tag/0B2R) in the Stacks Project.

**`AlgebraicGeometry.inter_nonempty_projectiveSpaceOverRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ProjectiveIntersection.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ProjectiveIntersection.lean#L394). The attribute's comment: “nonemptiness”.

> Let `k` be a field and let `X` and `Y` be nonempty closed subsets of `ℙⁿ_k` of dimensions `r`
> and `s`. If `n ≤ r + s` then `X` and `Y` meet.

```lean
theorem inter_nonempty_projectiveSpaceOverRing
    (X Y : Set (AlgebraicGeometry.projectiveSpaceOverRing n (CommRingCat.of k)))
    (hXc : IsClosed X) (hYc : IsClosed Y) (hXne : X.Nonempty) (hYne : Y.Nonempty)
    (hXd : topologicalKrullDim ↥X = (r : WithBot ℕ∞))
    (hYd : topologicalKrullDim ↥Y = (s : WithBot ℕ∞))
    (hrs : n ≤ r + s) : (X ∩ Y).Nonempty
```

**`AlgebraicGeometry.le_topologicalKrullDim_inter_projectiveSpaceOverRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ProjectiveIntersection.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Defs/Dimension/ProjectiveIntersection.lean#L410). The attribute's comment: “dimension bound”.

> Let `k` be a field and let `X` and `Y` be nonempty closed subsets of `ℙⁿ_k` of dimensions `r`
> and `s`. If `n ≤ r + s` then `X ∩ Y` has dimension at least `r + s - n`.

```lean
theorem le_topologicalKrullDim_inter_projectiveSpaceOverRing
    (X Y : Set (AlgebraicGeometry.projectiveSpaceOverRing n (CommRingCat.of k)))
    (hXc : IsClosed X) (hYc : IsClosed Y) (hXne : X.Nonempty) (hYne : Y.Nonempty)
    (hXd : topologicalKrullDim ↥X = (r : WithBot ℕ∞))
    (hYd : topologicalKrullDim ↥Y = (s : WithBot ℕ∞))
    (hrs : n ≤ r + s) : ((r + s - n : ℕ) : WithBot ℕ∞) ≤ topologicalKrullDim ↥(X ∩ Y)
```

## Tag 0BXU, a lemma

[Tag 0BXU](https://stacks.math.columbia.edu/tag/0BXU) in the Stacks Project.

**`AlgebraicGeometry.ProjectiveSpectrum.Proj.projectiveSpace_idealOfClosedSubscheme_isPrincipal_of_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CodimOneSubscheme/ProjHeightOne.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/CodimOneSubscheme/ProjHeightOne.lean#L365).

> **Stacks Project, Tag 0BXU.** Let `k` be a field and let `Z` be a closed subscheme of
> `P^n_k = Proj k[T₀, …, Tₙ]` which has no embedded points and every irreducible component of which
> has dimension `n - 1`. Then the homogeneous ideal `I(Z) ⊆ k[T₀, …, Tₙ]` corresponding to `Z` is
> principal.
>
> The dimension hypothesis is written without subtraction as `dim W + 1 = n`. A field is a
> Noetherian unique factorization domain, and in projective space over a field a component of
> dimension `n - 1` has codimension one, so this is a special case of Tag 0BXL in the form
> `projectiveSpace_idealOfClosedSubscheme_isPrincipal_of_codimension_one`.

```lean
theorem projectiveSpace_idealOfClosedSubscheme_isPrincipal_of_dimension (k : Type u) [Field k]
    (n : ℕ) {Z : Scheme.{u}} (i : Z ⟶ Proj (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) k))
    [IsClosedImmersion i] (hno : HasNoEmbeddedPoints Z)
    (hdim : ∀ W ∈ irreducibleComponents Z, topologicalKrullDim W + 1 = (n : WithBot ℕ∞)) :
    (idealOfClosedSubscheme
      (MvPolynomial.homogeneousSubmodule (Fin (n + 1)) k) i).IsPrincipal
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.34, Tag 0B2N](https://stacks.math.columbia.edu/tag/0B2N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
