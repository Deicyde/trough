---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpace.IsPseudoCoherentComplexFrom, AlgebraicGeometry.RingedSpace.IsPseudoCoherentComplex, AlgebraicGeometry.RingedSpace.IsPseudoCoherentFrom, AlgebraicGeometry.RingedSpace.IsPseudoCoherent, AlgebraicGeometry.RingedSpace.isPseudoCoherentComplexFrom_of_iso, AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_local_derived_approximation, Stacks.PseudoCoherence.DerivedCharacterization.isPseudoCoherentFrom_of_local_derived_approximation, Stacks.PseudoCoherence.DerivedCharacterization.isPseudoCoherentComplexFrom_of_iso
statement: formalized
proof: formalized
---

# 20.47 Pseudo-coherent modules

Section 20.47 of the Stacks Project, [Tag 08CA](https://stacks.math.columbia.edu/tag/08CA). 10 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08CB, a definition

[Tag 08CB](https://stacks.math.columbia.edu/tag/08CB) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.IsPseudoCoherentComplexFrom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean#L109). The attribute's comment: “part (1)”.

> A complex of `𝒪_X`-modules is `m`-pseudo-coherent if every point of `X` has an open
> neighbourhood on which the complex admits a strictly perfect approximation in degrees at
> least `m`: a map from a strictly perfect complex which is an isomorphism on cohomology in every
> degree above `m` and an epimorphism on cohomology in degree `m`.

```lean
public abbrev IsPseudoCoherentComplexFrom
    (E : CochainComplex (StrictlyPerfect.OXMod.{u, u, u} X) ℤ) (m : ℤ) : Prop
```

**`AlgebraicGeometry.RingedSpace.IsPseudoCoherentComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean#L122). The attribute's comment: “part (2)”.

> A complex of `𝒪_X`-modules is pseudo-coherent if it is `m`-pseudo-coherent for every
> integer `m`.

```lean
public abbrev IsPseudoCoherentComplex
    (E : CochainComplex (StrictlyPerfect.OXMod.{u, u, u} X) ℤ) : Prop
```

**`AlgebraicGeometry.RingedSpace.IsPseudoCoherentFrom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean#L129). The attribute's comment: “part (3), m-pseudo-coherent”.

> An object of the derived category of `𝒪_X`-modules is `m`-pseudo-coherent if it is
> represented by an `m`-pseudo-coherent complex.

```lean
public abbrev IsPseudoCoherentFrom
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u, u} X)]
    (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u, u} X)) (m : ℤ) : Prop
```

**`AlgebraicGeometry.RingedSpace.IsPseudoCoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/SheafLevel.lean#L138). The attribute's comment: “part (3), pseudo-coherent”.

> An object of the derived category of `𝒪_X`-modules is pseudo-coherent if it is represented by
> a pseudo-coherent complex.

```lean
public abbrev IsPseudoCoherent
    [HasDerivedCategory.{d} (StrictlyPerfect.OXMod.{u, u, u} X)]
    (E : DerivedCategory (StrictlyPerfect.OXMod.{u, u, u} X)) : Prop
```

## Tag 08CC, a lemma

[Tag 08CC](https://stacks.math.columbia.edu/tag/08CC) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentComplexFrom_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentIso.lean, line 674](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentIso.lean#L674). The attribute's comment: “part (2)”. References: SGA 6 I (2.2), “a)”.

> Let `E` be an `m`-pseudo-coherent object of the derived category of `𝒪_X`-modules. Then every
> complex of `𝒪_X`-modules representing `E` is `m`-pseudo-coherent.

```lean
public theorem isPseudoCoherentComplexFrom_of_iso (E : DerivedCategory (OXMod.{u, u} X)) (m : ℤ)
    (hE : IsPseudoCoherentFrom E m) (K : CochainComplex (OXMod.{u, u} X) ℤ)
    (e : DerivedCategory.Q.obj K ≅ E) : IsPseudoCoherentComplexFrom K m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_local_derived_approximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentIso.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentIso.lean#L704). The attribute's comment: “part (1)”. References: SGA 6 I (2.2), “b) (ii')=>(ii)”.

> Let `E` be an object of the derived category of `𝒪_X`-modules and suppose that every point of
> `X` has an open neighbourhood `U` on which some strictly perfect complex `𝒫` maps to `E|_U` in
> `D(𝒪_U)` by a morphism which is an isomorphism on cohomology above `m` and an epimorphism in degree
> `m`. Then `E` is `m`-pseudo-coherent. Here `E|_U` is presented as `Q(𝒦|_U)` for a complex `𝒦`
> representing `E`.

```lean
public theorem isPseudoCoherentFrom_of_local_derived_approximation
    [∀ U : Opens X.carrier,
      HasDerivedCategory.{d'} (OXMod.{u, u} (X.restrict U.isOpenEmbedding))]
    (E : DerivedCategory (OXMod.{u, u} X)) (m : ℤ) (K : CochainComplex (OXMod.{u, u} X) ℤ)
    (e : DerivedCategory.Q.obj K ≅ E)
    (h : ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ P : CochainComplex (OXMod.{u, u} (X.restrict U.isOpenEmbedding)) ℤ,
        IsStrictlyPerfect P ∧
        ∃ α : DerivedCategory.Q.obj P ⟶ DerivedCategory.Q.obj (restrictComplex K U),
          (∀ j : ℤ, m < j → IsIso ((DerivedCategory.homologyFunctor _ j).map α)) ∧
          Epi ((DerivedCategory.homologyFunctor _ m).map α)) :
    IsPseudoCoherentFrom E m
```

**`Stacks.PseudoCoherence.DerivedCharacterization.isPseudoCoherentFrom_of_local_derived_approximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedCharacterization.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedCharacterization.lean#L244). The attribute's comment: “part (1)”.

> **Tag 08CC part (1).** Local strictly perfect approximations in the derived category make a
> derived object `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_local_derived_approximation
    [∀ U : Opens X.carrier,
      HasDerivedCategory.{d'} (OXMod.{u} (X.restrict U.isOpenEmbedding))]
    (E : DerivedCategory (OXMod.{u} X)) (m : ℤ) (K : CochainComplex (OXMod.{u} X) ℤ)
    (e : DerivedCategory.Q.obj K ≅ E)
    (h : ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧
      ∃ P : CochainComplex (OXMod.{u} (X.restrict U.isOpenEmbedding)) ℤ,
        IsStrictlyPerfect P ∧
        ∃ α : DerivedCategory.Q.obj P ⟶
          DerivedCategory.Q.obj (AlgebraicGeometry.RingedSpace.PseudoCoherence.restrictComplex K U),
          (∀ j : ℤ, m < j → IsIso ((DerivedCategory.homologyFunctor _ j).map α)) ∧
          Epi ((DerivedCategory.homologyFunctor _ m).map α)) :
    AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherentFrom (X := X) E m
```

**`Stacks.PseudoCoherence.DerivedCharacterization.isPseudoCoherentComplexFrom_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedCharacterization.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedCharacterization.lean#L264). The attribute's comment: “part (2)”. References: SGA 6 I (2.2), “a)”.

> **Tag 08CC part (2).** Every complex representing an `m`-pseudo-coherent derived object is
> `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentComplexFrom_of_iso (E : DerivedCategory (OXMod.{u} X)) (m : ℤ)
    (hE : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherentFrom (X := X) E m)
    (K : CochainComplex (OXMod.{u} X) ℤ) (e : DerivedCategory.Q.obj K ≅ E) :
    AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherentComplexFrom (X := X) K m
```

## Tag 09U7, a lemma

[Tag 09U7](https://stacks.math.columbia.edu/tag/09U7) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.isPseudoCoherentFrom_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedPullback.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedPullback.lean#L189).

> **Stacks 09U7.**  The derived pullback of an `m`-pseudo-coherent object of `D(𝒪_Y)` along a
> morphism of ringed spaces is `m`-pseudo-coherent.
>
> `isPseudoCoherentFrom_derivedPullback_of_complexLevel` reduces this to the complex level, which is
> `AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.isPseudoCoherentComplexFrom_modulePullback`.

```lean
theorem isPseudoCoherentFrom_derivedPullback {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (E : DerivedCategory (OXMod.{u} Y)) (m : ℤ)
    (hE : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherentFrom (X := Y) E m) :
    AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherentFrom (X := X)
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback f).obj E) m
```

## Tag 08CD, a lemma

[Tag 08CD](https://stacks.math.columbia.edu/tag/08CD) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_obj₃_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentTriangle.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentTriangle.lean#L483). The attribute's comment: “part (1)”.

> **Stacks 08CD, part (1).** If the first term of a distinguished triangle in the derived
> category of `𝒪_X`-modules is `(m + 1)`-pseudo-coherent and the second is `m`-pseudo-coherent,
> then the third is `m`-pseudo-coherent.

```lean
public theorem isPseudoCoherentFrom_obj₃_of_distinguished (m : ℤ)
    (T : Triangle (DerivedCategory (OXMod.{u, u} X))) (hT : T ∈ distinguishedTriangles)
    (hK : IsPseudoCoherentFrom T.obj₁ (m + 1)) (hL : IsPseudoCoherentFrom T.obj₂ m) :
    IsPseudoCoherentFrom T.obj₃ m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_obj₂_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentTriangle.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentTriangle.lean#L497). The attribute's comment: “part (2)”. References: SGA 6 I (2.5), “b), ringed space”.

> **Stacks 08CD, part (2).** If the first and third terms of a distinguished triangle in the
> derived category of `𝒪_X`-modules are `m`-pseudo-coherent, then so is the second.
>
> Apply part (1) to the inverse rotation of the triangle, whose first two terms are `M[-1]` and
> `K`.

```lean
public theorem isPseudoCoherentFrom_obj₂_of_distinguished (m : ℤ)
    (T : Triangle (DerivedCategory (OXMod.{u, u} X))) (hT : T ∈ distinguishedTriangles)
    (hK : IsPseudoCoherentFrom T.obj₁ m) (hM : IsPseudoCoherentFrom T.obj₃ m) :
    IsPseudoCoherentFrom T.obj₂ m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_obj₁_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentTriangle.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentTriangle.lean#L511). The attribute's comment: “part (3)”.

> **Stacks 08CD, part (3).** If the second term of a distinguished triangle in the derived
> category of `𝒪_X`-modules is `(m + 1)`-pseudo-coherent and the third is `m`-pseudo-coherent, then
> the first is `(m + 1)`-pseudo-coherent.
>
> Apply part (1) to the rotation of the triangle, whose third term is `K[1]`.

```lean
public theorem isPseudoCoherentFrom_obj₁_of_distinguished (m : ℤ)
    (T : Triangle (DerivedCategory (OXMod.{u, u} X))) (hT : T ∈ distinguishedTriangles)
    (hL : IsPseudoCoherentFrom T.obj₂ (m + 1)) (hM : IsPseudoCoherentFrom T.obj₃ m) :
    IsPseudoCoherentFrom T.obj₁ (m + 1)
```

## Tag 09J3, a lemma

[Tag 09J3](https://stacks.math.columbia.edu/tag/09J3) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedTensorProduct.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedTensorProduct.lean#L480). The attribute's comment: “part (1)”. References: SGA 6 I (2.16), “special case”.

> **Tag 09J3, part (1).**  Let `(X, 𝒪_X)` be a ringed space and let `K`, `L` be objects of
> `D(𝒪_X)`.  If `K` is `n`-pseudo-coherent with `H^i(K) = 0` for `i > a`, and `L` is
> `m`-pseudo-coherent with `H^j(L) = 0` for `j > b`, then `K ⊗_{𝒪_X}^{𝐋} L` is
> `t`-pseudo-coherent for `t = max (m + a, n + b)`.
>
> If `a < n` then `t > a + b`, so the conclusion follows from right t-exactness of the derived
> tensor product alone; that is
> `Stacks.Cohomology.PseudoCoherentTensor.isPseudoCoherentFrom_derivedTensorProduct_of_lt`.
> Otherwise `n ≤ a`.  Both factors are replaced by K-flat representatives `𝒜`, `ℬ` with no terms
> above their own bounds (Tag 06YQ through Tag 05T7); on those the derived tensor product is
> `Tot(𝒜 ⊗_{𝒪_X} ℬ)` by the comparison of Tag 06YU, so that complex represents
> `K ⊗^{𝐋} L` and is the one fed to Tag 08CC part (1).  Pseudo-coherence passes to `𝒜` and `ℬ` by
> Tag 08CC part (2), and `AlgebraicGeometry.RingedSpace.localApproximationData` produces the
> required local approximations in degree `t`.

```lean
theorem isPseudoCoherentFrom_derivedTensorProduct
    (T : Stacks.DerivedTensor.RingedSite.DerivedTensorProduct X.sheaf)
    (K L : DerivedCategory (KFlatDerivedPullback.Modules X)) (n m a b : ℤ)
    (hK : IsPseudoCoherentFrom (X := X) K n)
    (hKa : ∀ i : ℤ, a < i →
      IsZero ((DerivedCategory.homologyFunctor (KFlatDerivedPullback.Modules X) i).obj K))
    (hL : IsPseudoCoherentFrom (X := X) L m)
    (hLb : ∀ j : ℤ, b < j →
      IsZero ((DerivedCategory.homologyFunctor (KFlatDerivedPullback.Modules X) j).obj L)) :
    IsPseudoCoherentFrom (X := X) ((T.tensor.obj K).obj L) (max (m + a) (n + b))
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherent_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedTensorProduct.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DerivedTensorProduct.lean#L521). The attribute's comment: “part (2)”.

> **Tag 09J3, part (2).**  The derived tensor product of two pseudo-coherent objects of
> `D(𝒪_X)` is pseudo-coherent.
>
> Neither factor is assumed bounded above, so the representatives come from the unrestricted
> K-flat resolutions of Tag 06YS rather than from a bounded one; `Tot(𝒜 ⊗_{𝒪_X} ℬ)` is then a
> representative of `K ⊗^{𝐋} L`, and it suffices to see that it is `q`-pseudo-coherent as a
> complex for every `q`.  By Tag 08CC that is `q`-pseudo-coherence of `K ⊗^{𝐋} L`, which
> `AlgebraicGeometry.RingedSpace.localApproximationData_of_isPseudoCoherentComplex` supplies: the
> cohomological bounds that part (1) needs are produced on an open covering, which is the source's
> reduction to a covering on which both factors are bounded above.

```lean
theorem isPseudoCoherent_derivedTensorProduct
    (T : Stacks.DerivedTensor.RingedSite.DerivedTensorProduct X.sheaf)
    (K L : DerivedCategory (KFlatDerivedPullback.Modules X))
    (hK : IsPseudoCoherent (X := X) K) (hL : IsPseudoCoherent (X := X) L) :
    IsPseudoCoherent (X := X) ((T.tensor.obj K).obj L)
```

## Tag 08CE, a lemma

[Tag 08CE](https://stacks.math.columbia.edu/tag/08CE) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentSummand.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/PseudoCoherentSummand.lean#L159). The attribute's comment: “m-pseudo-coherent, both summands”. References: SGA 6 I (2.12), “n-pc: sum ⇒ F',F''”.

> **Stacks 064X on a ringed space: both summands of an `m`-pseudo-coherent binary biproduct in
> `D(𝒪_X)` are `m`-pseudo-coherent.**
>
> `m`-pseudo-coherence is local
> (`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_local_restrict`), so it is enough to find,
> around every point, an open `U` on which the restriction of the summand is `m`-pseudo-coherent.
> Choose `U` so that `A ⊞ B` has no cohomology above some degree there
> (`AlgebraicGeometry.RingedSpace.exists_isZero_homology_gt_derivedRestrict`); restriction is
> additive, so `(A ⊞ B)|_U ≅ A|_U ⊞ B|_U`, and
> `AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_biprod_of_isZero_homology_gt` applies on
> `X|U`.
>
> This is also **Stacks 08CE** for a fixed degree: the ringed-space statement of 08CE at a fixed
> degree is literally this one, and both of its conclusions are proved here at once.

```lean
public theorem isPseudoCoherentFrom_of_biprod (m : ℤ)
    {A B : DerivedCategory (OXMod.{u, u} X)} (h : IsPseudoCoherentFrom (A ⊞ B) m) :
    IsPseudoCoherentFrom A m ∧ IsPseudoCoherentFrom B m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_left_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean#L177). The attribute's comment: “m-pseudo-coherent, first summand”. References: SGA 6 I (2.12), “n-pc: sum ⇒ F'”.

> **Stacks Project, Tag 08CE.** The first summand of an `m`-pseudo-coherent biproduct is
> `m`-pseudo-coherent.

```lean
public theorem isPseudoCoherentFrom_left_of_biprod
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    (K L : DerivedCategory (OXMod.{u, u} X)) (m : ℤ)
    (h : IsPseudoCoherentFrom (K ⊞ L) m) : IsPseudoCoherentFrom K m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_right_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean#L234). The attribute's comment: “m-pseudo-coherent, second summand”. References: SGA 6 I (2.12), “n-pc: sum ⇒ F''”.

> **Stacks Project, Tag 08CE.** The second summand of an `m`-pseudo-coherent biproduct is
> `m`-pseudo-coherent.

```lean
public theorem isPseudoCoherentFrom_right_of_biprod
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    (K L : DerivedCategory (OXMod.{u, u} X)) (m : ℤ)
    (h : IsPseudoCoherentFrom (K ⊞ L) m) : IsPseudoCoherentFrom L m
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherent_left_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean#L243). The attribute's comment: “pseudo-coherent, first summand”.

> **Stacks Project, Tag 08CE.** The first summand of a pseudo-coherent biproduct is
> pseudo-coherent.

```lean
public theorem isPseudoCoherent_left_of_biprod
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    (K L : DerivedCategory (OXMod.{u, u} X)) (h : IsPseudoCoherent (K ⊞ L)) :
    IsPseudoCoherent K
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherent_right_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/DirectSummand.lean#L257). The attribute's comment: “pseudo-coherent, second summand”.

> **Stacks Project, Tag 08CE.** The second summand of a pseudo-coherent biproduct is
> pseudo-coherent.

```lean
public theorem isPseudoCoherent_right_of_biprod
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    (K L : DerivedCategory (OXMod.{u, u} X)) (h : IsPseudoCoherent (K ⊞ L)) :
    IsPseudoCoherent L
```

**`Stacks.PseudoCoherence.Summands.isPseudoCoherent_of_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/Summands.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/PseudoCoherence/Summands.lean#L62). The attribute's comment: “pseudo-coherent, both summands”.

> **Stacks 08CE.** Both summands of a pseudo-coherent binary biproduct in `D(O_X)` are
> pseudo-coherent.
>
> Pseudo-coherence is `m`-pseudo-coherence in every degree, by
> `AlgebraicGeometry.RingedSpace.isPseudoCoherent_iff_forall`, and in each degree the two summands
> are `m`-pseudo-coherent by
> `AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_biprod`.

```lean
theorem isPseudoCoherent_of_biprod {X : RingedSpace.{u, u}}
    [HasDerivedCategory.{d} (OXMod.{u, u} X)]
    [∀ V : Opens X.carrier,
      HasDerivedCategory.{d'} (OXMod.{u, u} (X.restrict V.isOpenEmbedding))]
    (A B : DerivedCategory (OXMod.{u, u} X))
    (h : AlgebraicGeometry.RingedSpace.IsPseudoCoherent (A ⊞ B)) :
    AlgebraicGeometry.RingedSpace.IsPseudoCoherent A ∧
      AlgebraicGeometry.RingedSpace.IsPseudoCoherent B
```

## Tag 09V7, a lemma

[Tag 09V7](https://stacks.math.columbia.edu/tag/09V7) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentComplexFrom_of_locally_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/BoundedComplex.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/BoundedComplex.lean#L387). References: SGA 5 VIII (5.1), “'if' direction”.

> **Stacks 09V7.** Let `X` be a ringed space, let `m` be an integer and let `𝒦` be a complex of
> `𝒪_X`-modules which is bounded above on a neighbourhood of every point and whose term `𝒦^i` is
> `(m - i)`-pseudo-coherent for every `i`. Then `𝒦` is an `m`-pseudo-coherent complex.
>
> The hypothesis on the terms is turned into the form the induction uses by
> `AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_singleFunctor_of_singleFunctor_zero`, and
> `AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_Q_of_locally_boundedAbove` is read back on
> the complex through Stacks 08CC part (2).

```lean
public theorem isPseudoCoherentComplexFrom_of_locally_boundedAbove (m : ℤ)
    (K : CochainComplex (OXMod.{u, u} X) ℤ)
    (hbdd : ∀ x : X.carrier, ∃ U : Opens X.carrier, x ∈ U ∧ ∃ b : ℤ, ∀ p : ℤ, b < p →
      IsZero ((restrictComplex K U).X p))
    (hK : ∀ i : ℤ, IsPseudoCoherentFrom
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X) 0).obj (K.X i)) (m - i)) :
    IsPseudoCoherentComplexFrom K m
```

## Tag 09V8, a lemma

[Tag 09V8](https://stacks.math.columbia.edu/tag/09V8) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_of_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/PseudoCoherent/CohomologyBoundedAbove.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/PseudoCoherent/CohomologyBoundedAbove.lean#L208).

> **Stacks Project, Tag 09V8.** Let `X` be a ringed space, `m : ℤ` and `E` an object of the
> derived category of `𝒪_X`-modules which is locally bounded above. If the cohomology sheaf `Hⁱ(E)`
> is `(m - i)`-pseudo-coherent for every `i`, then `E` is `m`-pseudo-coherent.

```lean
theorem isPseudoCoherentFrom_of_homology (E : DerivedCategory (OXMod.{u, u} X)) (m : ℤ)
    (hbdd : IsLocallyBoundedAbove E)
    (hcoh : ∀ i : ℤ, IsPseudoCoherentFrom
      ((DerivedCategory.singleFunctor (OXMod.{u, u} X) 0).obj
        ((DerivedCategory.homologyFunctor (OXMod.{u, u} X) i).obj E)) (m - i)) :
    IsPseudoCoherentFrom E m
```

## Tag 08DN, a lemma

[Tag 08DN](https://stacks.math.columbia.edu/tag/08DN) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isFinitePresentation_homology_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/FinitePresentationNextCohomology.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/FinitePresentationNextCohomology.lean#L251). The attribute's comment: “part (2)”.

> Let `X` be a ringed space and let `K` be an `m`-pseudo-coherent object of the derived category
> of `𝒪_X`-modules with `H^i(K) = 0` for `i > m + 1`. Then `H^{m+1}(K)` is an `𝒪_X`-module of finite
> presentation.

```lean
public theorem isFinitePresentation_homology_of_isPseudoCoherentFrom
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] (K : DerivedCategory (OXMod.{u, u} X)) (m : ℤ)
    (hK : IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m + 1 < i →
      IsZero ((DerivedCategory.homologyFunctor (OXMod.{u, u} X) i).obj K)) :
    SheafOfModules.IsFinitePresentation (R := structureSheafOfRings X)
      ((DerivedCategory.homologyFunctor (OXMod.{u, u} X) (m + 1)).obj K)
```

**`AlgebraicGeometry.RingedSpace.isFiniteType_homology_of_isPseudoCoherentFrom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/ImmersionIndependence.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/ImmersionIndependence.lean#L234). The attribute's comment: “part (1)”.

> **Stacks 08DN, part (1).** Let `X` be a ringed space and let `K` be an `m`-pseudo-coherent
> object of the derived category of `𝒪_X`-modules with `H^i(K) = 0` for `i > m`. Then `H^m(K)` is an
> `𝒪_X`-module of finite type.
>
> Finite type is a local condition, so it is enough to produce, around each point of `X`, an
> epimorphism onto `H^m(K)` from a finite free module. Let `E` be a complex representing `K` which
> is `m`-pseudo-coherent as a complex, and let `𝒫 ⟶ E|_U` be a strictly perfect approximation on an
> open neighbourhood `U` of the given point: it is an isomorphism on cohomology above `m` and an
> epimorphism in degree `m`. Since restriction is exact and `H^i(K)` vanishes above `m`, the
> cohomology of `𝒫` vanishes above `m` too, so
> `AlgebraicGeometry.RingedSpace.exists_isDirectSummandOfFiniteFree_restrict_cycles` makes `Z^m(𝒫)`
> a direct summand of a finite free module after restriction to a smaller `W`. Composing the
> retraction with `Z^m(𝒫) ⟶ H^m(𝒫) ⟶ H^m(E|_U) ≅ H^m(E)|_U` gives the required epimorphism, which
> `AlgebraicGeometry.RingedSpace.exists_epi_free_over_of_epi_finiteFree` reads in the slice idiom in
> which finite type is phrased.

```lean
public theorem isFiniteType_homology_of_isPseudoCoherentFrom
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] (K : DerivedCategory (OXMod.{u, u} X)) (m : ℤ)
    (hK : IsPseudoCoherentFrom K m)
    (hvanish : ∀ i : ℤ, m < i →
      IsZero ((DerivedCategory.homologyFunctor (OXMod.{u, u} X) i).obj K)) :
    SheafOfModules.IsFiniteType (R := structureSheafOfRings X)
      ((DerivedCategory.homologyFunctor (OXMod.{u, u} X) m).obj K)
```

## Tag 09V9, a lemma

[Tag 09V9](https://stacks.math.columbia.edu/tag/09V9) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_singleFunctor_zero_neg_one_iff_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/FinitePresentationDegreeMinusOne.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/FinitePresentationDegreeMinusOne.lean#L338). The attribute's comment: “finite_presentation_iff_minus_one_pseudo_coherent”.

> Let `X` be a ringed space and let `ℱ` be a sheaf of `𝒪_X`-modules.
> Then `ℱ`, viewed in degree zero as an object of the derived category of `𝒪_X`-modules, is
> `(-1)`-pseudo-coherent if and only if `ℱ` is an `𝒪_X`-module of finite presentation.

```lean
public theorem isPseudoCoherentFrom_singleFunctor_zero_neg_one_iff_isFinitePresentation
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] (F : OXMod.{u, u} X) :
    IsPseudoCoherentFrom ((DerivedCategory.singleFunctor (OXMod.{u, u} X) 0).obj F) (-1) ↔
      SheafOfModules.IsFinitePresentation (R := structureSheafOfRings X) F
```

**`AlgebraicGeometry.RingedSpace.isPseudoCoherentFrom_singleFunctor_zero_iff_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/FiniteTypeDegreeZero.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/FiniteTypeDegreeZero.lean#L146). The attribute's comment: “finite_type_iff_zero_pseudo_coherent”.

> Let `X` be a ringed space and let `ℱ` be a sheaf of `𝒪_X`-modules. Then `ℱ`, viewed in degree
> zero as an object of the derived category of `𝒪_X`-modules, is `0`-pseudo-coherent if and only if
> `ℱ` is an `𝒪_X`-module of finite type.

```lean
public theorem isPseudoCoherentFrom_singleFunctor_zero_iff_isFiniteType
    [HasDerivedCategory.{d} (OXMod.{u, u} X)] (F : OXMod.{u, u} X) :
    IsPseudoCoherentFrom ((DerivedCategory.singleFunctor (OXMod.{u, u} X) 0).obj F) 0 ↔
      SheafOfModules.IsFiniteType (R := structureSheafOfRings X) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.47, Tag 08CA](https://stacks.math.columbia.edu/tag/08CA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
