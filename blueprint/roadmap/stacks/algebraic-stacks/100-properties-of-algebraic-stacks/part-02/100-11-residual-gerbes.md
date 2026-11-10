---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isFlat_of_fieldSpectrum_cover, AlgebraicGeometry.Stack.isSurjective_of_fieldSpectrum_cover, AlgebraicGeometry.Stack.tfae_isReducedWithUniquePoint, AlgebraicGeometry.Stack.isReducedLocallyNoetherianWithUniquePoint_iff_hasLocallyOfFinitePresentationFlatFieldSpectrumCover, AlgebraicGeometry.Stack.isEmpty_points_or_isEquivalenceOver_of_isMonomorphism, AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_fullSubcategoryInclusion, AlgebraicGeometry.Stack.eq_of_isReducedLocallyNoetherianUniquePointSubstack, AlgebraicGeometry.Stack.exists_isReducedLocallyNoetherianUniquePointSubstack
statement: formalized
proof: formalized
---

# 100.11 Residual gerbes

Section 100.11 of the Stacks Project, [Tag 06ML](https://stacks.math.columbia.edu/tag/06ML). 14 tags here are carried by 62 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06MM, a lemma

[Tag 06MM](https://stacks.math.columbia.edu/tag/06MM) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFlat_of_fieldSpectrum_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FieldSpectrumCoverFlat.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FieldSpectrumCoverFlat.lean#L104). The attribute's comment: “flatness”.

> **Stacks 06MM, flatness.** Let `𝒵` be an algebraic stack over `S` admitting a surjective flat
> 1-morphism from the algebraic stack of the spectrum of a field. Then every 1-morphism to `𝒵` from
> the algebraic stack of the spectrum of a field is flat.
>
> Form the canonical 2-fibre product of the given cover `f` with the 1-morphism `g` in question.
> Its projection to the source of `f` is flat because that source is the algebraic stack of the
> spectrum of a field, so the composite with `f` is flat; `f` being surjective and flat,
> **Stacks 06PZ** descends that flatness to `g`.
>
> The companion `AlgebraicGeometry.Stack.isSurjective_of_fieldSpectrum_cover` is the surjectivity
> half of the tag, which needs no flatness hypothesis.

```lean
theorem isFlat_of_fieldSpectrum_cover (𝒵 : AlgebraicStacks.{u, w} B S hS)
    (F F' : FieldSpectrum B S hS)
    (f : schemeStack.{u, w} B S hS F.base ⟶ 𝒵)
    (g : schemeStack.{u, w} B S hS F'.base ⟶ 𝒵)
    (hsurj : IsSurjective B S hS f) (hflat : AlgebraicStacks.IsFlat B S hS f) :
    AlgebraicStacks.IsFlat B S hS g
```

**`AlgebraicGeometry.Stack.isSurjective_of_fieldSpectrum_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FieldSpectrumCoverSurjective.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FieldSpectrumCoverSurjective.lean#L90). The attribute's comment: “surjectivity”.

> **Stacks 06MM, surjectivity.** Let `𝒵` be an algebraic stack over `S` admitting a surjective
> 1-morphism from the algebraic stack of the spectrum of a field. Then every 1-morphism to `𝒵` from
> the algebraic stack of the spectrum of a field is surjective.
>
> The spectrum of a field has one point, so a surjection out of its stack leaves `𝒵` with at most
> one point; the source of the second 1-morphism has a point, which therefore hits every point of
> `𝒵`. Flatness of the given surjection, which Stacks 06MM also assumes, is not needed.

```lean
theorem isSurjective_of_fieldSpectrum_cover (𝒵 : AlgebraicStacks.{u, w} B S hS)
    (F F' : FieldSpectrum B S hS)
    (f : schemeStack.{u, w} B S hS F.base ⟶ 𝒵)
    (g : schemeStack.{u, w} B S hS F'.base ⟶ 𝒵)
    (hf : IsSurjective B S hS f) :
    IsSurjective B S hS g
```

## Tag 06MN, a lemma

[Tag 06MN](https://stacks.math.columbia.edu/tag/06MN) in the Stacks Project.

**`AlgebraicGeometry.Stack.tfae_isReducedWithUniquePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointStack.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointStack.lean#L426).

> For an algebraic stack `𝒵` over `S` the following are equivalent:
>
> 1. `𝒵` is reduced and its space of points `|𝒵|` is a singleton;
> 2. there is a surjective flat 1-morphism `Spec k ⟶ 𝒵` with `k` a field;
> 3. there is a surjective flat 1-morphism `Spec k ⟶ 𝒵`, locally of finite type, with `k` a field.

```lean
theorem tfae_isReducedWithUniquePoint (𝒵 : AlgebraicStacks.{u, w} B S hS) :
    List.TFAE
      [IsReducedWithUniquePoint B S hS 𝒵,
        HasFlatFieldSpectrumCover B S hS 𝒵,
        HasLocallyOfFiniteTypeFlatFieldSpectrumCover B S hS 𝒵]
```

## Tag 06MP, a lemma

[Tag 06MP](https://stacks.math.columbia.edu/tag/06MP) in the Stacks Project.

**`AlgebraicGeometry.Stack.isReducedLocallyNoetherianWithUniquePoint_iff_hasLocallyOfFinitePresentationFlatFieldSpectrumCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointStackFinitePresentation.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointStackFinitePresentation.lean#L136).

> For an algebraic stack `𝒵` over `S` the following are equivalent:
>
> 1. `𝒵` is reduced, locally Noetherian, and its space of points `|𝒵|` is a singleton;
> 2. there is a 1-morphism `Spec k ⟶ 𝒵` with `k` a field which is locally of finite presentation,
>    surjective and flat.

```lean
theorem
  isReducedLocallyNoetherianWithUniquePoint_iff_hasLocallyOfFinitePresentationFlatFieldSpectrumCover
    (𝒵 : AlgebraicStacks.{u, w} B S hS) :
    IsReducedLocallyNoetherianWithUniquePoint B S hS 𝒵 ↔
      HasLocallyOfFinitePresentationFlatFieldSpectrumCover B S hS 𝒵
```

## Tag 06MQ, a lemma

[Tag 06MQ](https://stacks.math.columbia.edu/tag/06MQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEmpty_points_or_isEquivalenceOver_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeMonomorphism.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeMonomorphism.lean#L453).

> **Stacks 06MQ.** Let `f : 𝒵' ⟶ 𝒵` be a monomorphism of algebraic stacks over `S` and assume
> that `𝒵` admits a 1-morphism from the algebraic stack of the spectrum of a field which is locally
> of finite presentation, surjective and flat (condition (2) of **Stacks 06MP**). Then either `𝒵'`
> has no points, or `f` is an equivalence over the big fppf site of `S`.
>
> The nonempty case is
> `AlgebraicGeometry.Stack.isEquivalenceOver_of_isMonomorphism_of_fieldSpectrumCover`.

```lean
theorem isEmpty_points_or_isEquivalenceOver_of_isMonomorphism
    (𝒵' 𝒵 : AlgebraicStacks.{u, w} B S hS) (f : 𝒵' ⟶ 𝒵)
    (hf : AlgebraicStacks.IsMonomorphism B S hS f)
    (hcov : HasLocallyOfFinitePresentationFlatFieldSpectrumCover B S hS 𝒵) :
    IsEmpty (AlgebraicStacks.points B S hS 𝒵') ∨
      Nonempty (Functor.IsEquivalenceOver 𝒵'.val.val.p 𝒵.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom))
```

## Tag 06MR, a lemma

[Tag 06MR](https://stacks.math.columbia.edu/tag/06MR) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_fullSubcategoryInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstack.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstack.lean#L133). The attribute's comment: “the inclusion morphism of the substack is representable by algebraic spaces and a monomorphism, granting the implication (2) ⟹ (3) of Stacks 04Y5 for the inclusion of a strictly full algebraic subcategory, which is the hypothesis hrep and which the library leaves open”.

> **The last assertion of Stacks 06MR.** The inclusion of a strictly full subcategory of an
> algebraic stack `𝒵` over `S` which is itself an algebraic stack is representable by algebraic
> spaces and a monomorphism in the sense of **Stacks 04ZW**.
>
> The monomorphy clause is unconditional, by the implication (2) ⟹ (1) of **Stacks 04ZZ** for a
> fully faithful 1-morphism. Representability by algebraic spaces is what the source takes from
> **Stacks 04Y5**, the inclusion being faithful; the library has the implication (2) ⟹ (3) of
> Stacks 04Y5 as
> `AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_faithful`,
> fed with the bootstrap theorem Stacks 04S6 part (3).

```lean
theorem AlgebraicStacks.isMonomorphism_fullSubcategoryInclusion
    (𝒵 : AlgebraicStacks.{u, w} B S hS) (P : ObjectProperty 𝒵.val.val.obj)
    (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒵 P)) :
    AlgebraicStacks.IsMonomorphism B S hS (fullSubcategoryInclusion 𝒵 P hP)
```

**`AlgebraicGeometry.Stack.eq_of_isReducedLocallyNoetherianUniquePointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstack.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstack.lean#L233). The attribute's comment: “the uniqueness of the substack, with the equivalent conditions of Stacks 06MP read as its condition (2), and granting the implication (2) ⟹ (3) of Stacks 04Y5 for the inclusion of a strictly full algebraic subcategory, which is the hypothesis hrep and which the library leaves open”.

> **Stacks 06MR, the uniqueness assertion.** Let `𝒵` be an algebraic stack over `S` which is
> reduced with a singleton space of points, that is, which satisfies condition (1) of
> **Stacks 06MN**. Then at most one strictly full subcategory of `𝒵` is an algebraic stack
> satisfying condition (2) of **Stacks 06MP**.
>
> Existence is not proved; see the module docstring.

```lean
theorem eq_of_isReducedLocallyNoetherianUniquePointSubstack
    (𝒵 : AlgebraicStacks.{u, w} B S hS) (h𝒵 : IsReducedWithUniquePoint B S hS 𝒵)
    {P Q : ObjectProperty 𝒵.val.val.obj}
    (hP : IsReducedLocallyNoetherianUniquePointSubstack.{u, w} B S hS 𝒵 P)
    (hQ : IsReducedLocallyNoetherianUniquePointSubstack.{u, w} B S hS 𝒵 Q) : P = Q
```

**`AlgebraicGeometry.Stack.exists_isReducedLocallyNoetherianUniquePointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackExistence.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackExistence.lean#L310). The attribute's comment: “the existence of the substack, with the equivalent conditions of Stacks 06MP read as its condition (2), granting the implication (1) ⟹ (3) of Stacks 06MN, which is the hypothesis h06MN, and granting Stacks 04T4 (1), (4), (5) and (6) together with Stacks 06FI, which is the hypothesis hpres; both are quantified over every algebraic stack over S and so restrict no object, and the library discharges neither, its own Stacks 06FI carrying Artin's representability theorem, Stacks 06DC, as an open hypothesis; what is proved is the replacement of the quotient stack by its essential image in Z, with the invariance of condition (2) of Stacks 06MP under an equivalence over the site”.

> **Stacks 06MR, the existence assertion.** Let `𝒵` be an algebraic stack over `S` which is
> reduced with a singleton space of points, that is, which satisfies condition (1) of
> **Stacks 06MN**. Then some strictly full subcategory of `𝒵` is an algebraic stack satisfying
> condition (2) of **Stacks 06MP**.
>
> The subcategory is the essential image of the fully faithful 1-morphism supplied by the carried
> `AlgebraicGeometry.Stack.HasFullyFaithfulFinitePresentationPresentations` out of the surjective flat cover,
> locally of finite type, by the spectrum of a field that condition (3) of **Stacks 06MN** supplies
> (`AlgebraicGeometry.Stack.tfae_isReducedWithUniquePoint`). It is closed under
> isomorphism; the source factors through it by an equivalence of categories, hence by an equivalence
> over the big fppf site by **Stacks 003Z**; so it is an algebraic stack by **Stacks 03YQ** and
> inherits condition (2) of Stacks 06MP by `AlgebraicGeometry.Stack`
> `.hasLocallyOfFinitePresentationFlatFieldSpectrumCover_of_isEquivalenceFunctor`.

```lean
theorem exists_isReducedLocallyNoetherianUniquePointSubstack
    (hpres : HasFullyFaithfulFinitePresentationPresentations.{u, w} B S hS)
    (𝒵 : AlgebraicStacks.{u, w} B S hS) (h𝒵 : IsReducedWithUniquePoint B S hS 𝒵) :
    ∃ P : ObjectProperty 𝒵.val.val.obj,
      IsReducedLocallyNoetherianUniquePointSubstack.{u, w} B S hS 𝒵 P
```

**`AlgebraicGeometry.Stack.existsUnique_isReducedLocallyNoetherianUniquePointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackExistence.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackExistence.lean#L344). The attribute's comment: “existence and uniqueness of the substack assembled, with the equivalent conditions of Stacks 06MP read as its condition (2), granting the implication (1) ⟹ (3) of Stacks 06MN (h06MN), Stacks 04T4 (1), (4), (5) and (6) together with Stacks 06FI (hpres), and the implication (2) ⟹ (3) of Stacks 04Y5 for the inclusion of a strictly full algebraic subcategory (hrep); all three are quantified over every algebraic stack over S and so restrict no object, and the library discharges none of them”.

> **Stacks 06MR, the first assertion.** Let `𝒵` be an algebraic stack over `S` which is reduced
> with a singleton space of points. Then exactly one strictly full subcategory of `𝒵` is an algebraic
> stack satisfying condition (2) of **Stacks 06MP**.
>
> Existence is `AlgebraicGeometry.Stack.exists_isReducedLocallyNoetherianUniquePointSubstack` and
> uniqueness is `AlgebraicGeometry.Stack.eq_of_isReducedLocallyNoetherianUniquePointSubstack`.

```lean
theorem existsUnique_isReducedLocallyNoetherianUniquePointSubstack
    (hpres : HasFullyFaithfulFinitePresentationPresentations.{u, w} B S hS)
    (𝒵 : AlgebraicStacks.{u, w} B S hS) (h𝒵 : IsReducedWithUniquePoint B S hS 𝒵) :
    ∃! P : ObjectProperty 𝒵.val.val.obj,
      IsReducedLocallyNoetherianUniquePointSubstack.{u, w} B S hS 𝒵 P
```

**`AlgebraicGeometry.Stack.exists_isReducedLocallyNoetherianUniquePointSubstack_of_isReducedWithUniquePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackLocalImage.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackLocalImage.lean#L69). The attribute's comment: “the existence of the substack, with the equivalent conditions of Stacks 06MP read as its condition (2)”.

> Let `𝒵` be an algebraic stack over `S` which is reduced with a singleton space of points,
> that is, which satisfies condition (1) of Stacks 06MN. Then some strictly full subcategory of `𝒵`
> is an algebraic stack satisfying condition (2) of Stacks 06MP.

```lean
theorem exists_isReducedLocallyNoetherianUniquePointSubstack_of_isReducedWithUniquePoint
    (𝒵 : AlgebraicStacks.{u, w} B S hS) (h𝒵 : IsReducedWithUniquePoint B S hS 𝒵) :
    ∃ P : ObjectProperty 𝒵.val.val.obj,
      IsReducedLocallyNoetherianUniquePointSubstack.{u, w} B S hS 𝒵 P
```

**`AlgebraicGeometry.Stack.existsUnique_isReducedLocallyNoetherianUniquePointSubstack_of_isReducedWithUniquePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackLocalImage.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedUniquePointSubstackLocalImage.lean#L81). The attribute's comment: “existence and uniqueness of the substack assembled, with the equivalent conditions of Stacks 06MP read as its condition (2)”.

> Let `𝒵` be an algebraic stack over `S` which is reduced with a singleton space of points.
> Then exactly one strictly full subcategory of `𝒵` is an algebraic stack satisfying condition (2)
> of Stacks 06MP.

```lean
theorem existsUnique_isReducedLocallyNoetherianUniquePointSubstack_of_isReducedWithUniquePoint
    (𝒵 : AlgebraicStacks.{u, w} B S hS) (h𝒵 : IsReducedWithUniquePoint B S hS 𝒵) :
    ∃! P : ObjectProperty 𝒵.val.val.obj,
      IsReducedLocallyNoetherianUniquePointSubstack.{u, w} B S hS 𝒵 P
```

## Tag 06MS, an example

[Tag 06MS](https://stacks.math.columbia.edu/tag/06MS) in the Stacks Project.

**`AlgebraicGeometry.RationalGaloisQuotient.selfFiberProduct`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L167). The attribute's comment: “the self-fibre-product U of Spec(ℚ̄) over Spec(ℚ), over its second factor”.

> **Stacks 06MS.** The self-fibre-product `U = Spec(ℚ̄) ×_{Spec(ℚ)} Spec(ℚ̄)`, as a scheme
> over `Spec(ℚ̄)` through its second projection.

```lean
abbrev selfFiberProduct : Over cover.left
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isLocallyNoetherian_selfFiberProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L229). The attribute's comment: “the cover U is not locally Noetherian, the source's non-noetherianity of X read on its atlas”.

> **Stacks 06MS.** The self-fibre-product `U` is not locally Noetherian: `ℚ̄ ⊗_ℚ ℚ̄` is a
> ring of Krull dimension zero, so a Noetherian one would be Artinian and have finitely many
> primes, whereas the infinite group `Gal(ℚ̄/ℚ)` injects into its primes.

```lean
theorem not_isLocallyNoetherian_selfFiberProduct :
    ¬ IsLocallyNoetherian selfFiberProduct.left
```

**`AlgebraicGeometry.RationalGaloisQuotient.isClosed_singleton_selfFiberProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L246). The attribute's comment: “every point of U is closed”.

> **Stacks 06MS.** Every point of the self-fibre-product `U` is closed: `ℚ̄ ⊗_ℚ ℚ̄` is
> integral over the field `ℚ̄`, so each of its primes is maximal.

```lean
theorem isClosed_singleton_selfFiberProduct (x : selfFiberProduct.left) :
    IsClosed ({x} : Set selfFiberProduct.left)
```

**`AlgebraicGeometry.RationalGaloisQuotient.galoisGroupEquivSelfFiberProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L312). The attribute's comment: “U = Gal(ℚ̄/ℚ) × Spec(ℚ̄) on points: the points of U are in bijection with the absolute Galois group”.

> **Stacks 06MS.** The points of `U = Spec(ℚ̄) ×_{Spec(ℚ)} Spec(ℚ̄)` are in bijection with
> `Gal(ℚ̄/ℚ)`: `σ` goes to the point cut out by the kernel of `x ⊗ y ↦ σ(x) y`. This is the source's
> `U = Gal(ℚ̄/ℚ) × Spec(ℚ̄)` on underlying sets.

```lean
def galoisGroupEquivSelfFiberProduct : galoisGroup ≃ selfFiberProduct.left
```

**`AlgebraicGeometry.RationalGaloisQuotient.selfFiberProductAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L324). The attribute's comment: “the action of the absolute Galois group on U over Spec(ℚ̄)”.

> **Stacks 06MS.** The action of `Gal(ℚ̄/ℚ)` on the self-fibre-product `U` over `Spec(ℚ̄)`:
> the base change along the structure morphism of `Spec(ℚ̄)` of the Galois action on `Spec(ℚ̄)`,
> so it moves the first projection and fixes the second.

```lean
def selfFiberProductAction : galoisGroup →* Aut selfFiberProduct
```

**`AlgebraicGeometry.RationalGaloisQuotient.constantGaloisGroupScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L332). The attribute's comment: “G: the absolute Galois group with the discrete topology as a constant group scheme over Spec(ℚ̄)”.

> **Stacks 06MS.** The absolute Galois group of `ℚ` with the discrete topology, viewed as a
> constant group scheme over `Spec(ℚ̄)` as in **Stacks 03YW**. This is the group scheme `G` the
> source lets act on `U`.

```lean
abbrev constantGaloisGroupScheme : Grp (Over cover.left)
```

**`AlgebraicGeometry.RationalGaloisQuotient.selfFiberProductAction_actsFreely`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L344). The attribute's comment: “G acts freely on U”.

> **Stacks 06MS.** The Galois group acts freely on the self-fibre-product `U`: the first
> projection `U ⟶ Spec(ℚ̄)` is equivariant, and the Galois action on `Spec(ℚ̄)` is already free by
> this library's **Stacks 02Z6**.

```lean
theorem selfFiberProductAction_actsFreely :
    Space.ActsFreelyOnNonemptyPoints selfFiberProduct galoisGroup
      (selfFiberProductAction B₀ hQ hK)
```

**`AlgebraicGeometry.RationalGaloisQuotient.selfFiberProductAction_transitive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L408). The attribute's comment: “G acts transitively on U”.

> **Stacks 06MS.** The Galois group acts transitively on the points of `U`: every prime of
> `ℚ̄ ⊗_ℚ ℚ̄` is the kernel of `x ⊗ y ↦ τ(x) y` for some Galois element `τ`, and `σ` moves the
> prime of `τ` to the prime of `τ σ⁻¹`.

```lean
theorem selfFiberProductAction_transitive (x y : selfFiberProduct.left) :
    ∃ σ : galoisGroup, (selfFiberProductAction B₀ hQ hK σ).asIso.hom.left x = y
```

**`AlgebraicGeometry.RationalGaloisQuotient.constantGaloisGroupSchemeAction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L428). The attribute's comment: “the action of G, as the constant group scheme over Spec(ℚ̄), on U”.

> **Stacks 06MS.** The action of `G`, viewed as the constant group scheme over `Spec(ℚ̄)` of
> **Stacks 03YW**, on `U` (**Stacks 022Z**): the action map `G ×_{Spec(ℚ̄)} U ⟶ U` which on the
> summand of `G ×_{Spec(ℚ̄)} U` indexed by `σ` is the automorphism `selfFiberProductAction σ`.

```lean
abbrev constantGaloisGroupSchemeAction : ModObj constantGaloisGroupScheme.X selfFiberProduct
```

**`AlgebraicGeometry.RationalGaloisQuotient.constantGaloisGroupSchemeAction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L436). The attribute's comment: “the action of the constant group scheme G on U is the Galois action on summands and on constant points”.

> **Stacks 06MS.** The action of the constant group scheme `G` on `U` restricts, on the summand
> of `G ×_{Spec(ℚ̄)} U` indexed by `σ ∈ Gal(ℚ̄/ℚ)`, to the automorphism `selfFiberProductAction σ`;
> and the constant `T`-point `σ` of `G` acts on the `T`-points of `U` by composition with it.

```lean
theorem constantGaloisGroupSchemeAction_eq (σ : galoisGroup) :
    letI := constantGaloisGroupSchemeAction B₀ hQ hK
    constantGroupSchemeLeg selfFiberProduct σ ≫ γ[constantGaloisGroupScheme.X, selfFiberProduct] =
        (selfFiberProductAction B₀ hQ hK σ).asIso.hom ∧
      ∀ {T : Over cover.left} (x : T ⟶ selfFiberProduct),
        (toUnit T ≫ constantGroupSchemePoint galoisGroup cover.left σ :
            T ⟶ constantGaloisGroupScheme.X) • x =
          x ≫ (selfFiberProductAction B₀ hQ hK σ).asIso.hom
```

**`AlgebraicGeometry.RationalGaloisQuotient.isFreeAction_constantGaloisGroupSchemeAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L450). The attribute's comment: “the constant group scheme G acts freely on U”.

> **Stacks 06MS.** The constant group scheme `G` acts freely on `U`, in the sense of
> **Stacks 07S1**: for every scheme `T` over `Spec(ℚ̄)` the group `G(T)` of locally constant maps
> `T → Gal(ℚ̄/ℚ)` acts freely on `U(T)`.

```lean
theorem isFreeAction_constantGaloisGroupSchemeAction :
    letI := constantGaloisGroupSchemeAction B₀ hQ hK
    IsFreeAction constantGaloisGroupScheme.X selfFiberProduct
```

**`AlgebraicGeometry.RationalGaloisQuotient.exists_smul_eq_constantGaloisGroupSchemeAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L459). The attribute's comment: “the constant group scheme G acts transitively on U”.

> **Stacks 06MS.** The constant group scheme `G` acts transitively on `U`: for any two points
> `u, v` of `U` some point of `G ×_{Spec(ℚ̄)} U` lies over `u` under the projection and over `v`
> under the action map.

```lean
theorem exists_smul_eq_constantGaloisGroupSchemeAction (u v : selfFiberProduct.left) :
    letI := constantGaloisGroupSchemeAction B₀ hQ hK
    ∃ z : (constantGaloisGroupScheme.X ⊗ selfFiberProduct).left,
      (snd constantGaloisGroupScheme.X selfFiberProduct).left z = u ∧
        (γ[constantGaloisGroupScheme.X, selfFiberProduct]).left z = v
```

**`AlgebraicGeometry.RationalGaloisQuotient.galoisSelfProductQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L531). The attribute's comment: “X = U/G, the fppf sheaf quotient”.

> **Stacks 06MS.** The algebraic space `X = U/G` of the example: the fppf sheaf quotient of
> the self-fibre-product by the Galois action, as in **Stacks 02Z3**.

```lean
abbrev galoisSelfProductQuotient : (BigFppfOver B cover.left hS)ᵒᵖ ⥤ Type 0
```

**`AlgebraicGeometry.RationalGaloisQuotient.isAlgebraicSpace_galoisSelfProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L538). The attribute's comment: “X is an algebraic space”.

> **Stacks 06MS.** `X = U/G` is an algebraic space over `Spec(ℚ̄)`; this is the source's
> remark that the example is even an algebraic space.

```lean
theorem isAlgebraicSpace_galoisSelfProductQuotient :
    IsAlgebraicSpace B cover.left hS (galoisSelfProductQuotient B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isLocallyNoetherian_galoisSelfProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L581). The attribute's comment: “X is not locally Noetherian, the failure Definition 06MU excludes”.

> **Stacks 06MS.** `X` is not locally Noetherian: `U ⟶ X` is an étale atlas, and an
> étale-local property of an algebraic space holds on every étale chart as soon as it holds at
> all, while `U` is not locally Noetherian.

```lean
theorem not_isLocallyNoetherian_galoisSelfProductQuotient :
    ¬ Space.HasEtaleLocalProperty B cover.left hS
      (galoisSelfProductQuotient B₀ hQ hK B hS hU)
      (fun T : Scheme.{0} ↦ IsLocallyNoetherian T)
```

**`AlgebraicGeometry.RationalGaloisQuotient.canonicalPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L595). The attribute's comment: “the morphism x : Spec(ℚ̄) ⟶ U ⟶ X”.

> **Stacks 06MS.** The morphism `x : Spec(ℚ̄) ⟶ U ⟶ X` of the example: the diagonal followed
> by the projection onto the quotient.

```lean
def canonicalPoint :
    yoneda.obj (Space.baseTerminal B cover.left hS) ⟶ galoisSelfProductQuotient B₀ hQ hK B hS hU
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isIso_canonicalPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L603). The attribute's comment: “x is not an isomorphism”.

> **Stacks 06MS, the point of the example.** The morphism `x : Spec(ℚ̄) ⟶ X` is *not* an
> isomorphism. If it were, `X` would be represented by `Spec(ℚ̄)`, hence locally Noetherian; but
> `X` is not locally Noetherian.

```lean
theorem not_isIso_canonicalPoint : ¬ IsIso (canonicalPoint B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.isReduced_galoisSelfProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 613](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L613). The attribute's comment: “X is reduced”.

> **Stacks 06MS.** `X` is reduced, witnessed by the reduced étale atlas `U ⟶ X`.

```lean
theorem isReduced_galoisSelfProductQuotient :
    Space.HasEtaleLocalProperty B cover.left hS
      (galoisSelfProductQuotient B₀ hQ hK B hS hU)
      (fun T : Scheme.{0} ↦ IsReduced T)
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isNoetherian_galoisSelfProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L624). The attribute's comment: “X is non-noetherian”.

> **Stacks 06MS.** `X` is not a Noetherian algebraic space in the sense of **Stacks 03EA**,
> because it is not locally Noetherian.

```lean
theorem not_isNoetherian_galoisSelfProductQuotient (hZ : B.Contains (⊤_ Scheme.{0})) :
    ¬ Space.IsNoetherian B cover.left hS hZ (galoisSelfProductQuotient B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.mono_canonicalPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L632). The attribute's comment: “x is a monomorphism”.

> **Stacks 06MS.** The morphism `x : Spec(ℚ̄) ⟶ X` is a monomorphism, because `Spec(ℚ̄)` is
> the terminal object of the big fppf site over `Spec(ℚ̄)`: this is the source's remark that `x`
> is a monomorphism since `X` is an algebraic space over `ℚ̄`.

```lean
theorem mono_canonicalPoint : Mono (canonicalPoint B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.nonempty_points_galoisSelfProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 648](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L648). The attribute's comment: “X has a point”.

> **Stacks 06MS.** `X` has a point, namely the class of `x`; with
> `AlgebraicGeometry.RationalGaloisQuotient.subsingleton_points_galoisSelfProductQuotient` it is the
> only one.

```lean
theorem nonempty_points_galoisSelfProductQuotient :
    Nonempty (Space.points B cover.left hS (galoisSelfProductQuotient B₀ hQ hK B hS hU))
```

**`AlgebraicGeometry.RationalGaloisQuotient.isFiniteTypePoint_canonicalFieldPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 656](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L656). The attribute's comment: “x is a (locally) finite type point of X”.

> **Stacks 06MS.** The class of `x` is a finite type point of `X` in the sense of
> **Stacks 06EG**: it is the image of the closed point of `U` cut out by the diagonal under the
> étale chart `U ⟶ X`.

```lean
theorem isFiniteTypePoint_canonicalFieldPoint :
    Space.IsFiniteTypePoint B cover.left hS (galoisSelfProductQuotient B₀ hQ hK B hS hU)
      ((canonicalFieldPoint B₀ hQ hK B hS hU).class B cover.left hS _)
```

**`AlgebraicGeometry.RationalGaloisQuotient.eq_class_canonicalFieldPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L722). The attribute's comment: “X has exactly one point, namely the class of x”.

> **Stacks 06MS.** The algebraic space `X = U/G` has exactly one point, and it is the class of
> `x : Spec(ℚ̄) ⟶ X`.

```lean
theorem eq_class_canonicalFieldPoint
    (p : Space.points B cover.left hS (galoisSelfProductQuotient B₀ hQ hK B hS hU)) :
    p = (canonicalFieldPoint B₀ hQ hK B hS hU).class B cover.left hS _
```

**`AlgebraicGeometry.RationalGaloisQuotient.nonempty_unique_points_galoisSelfProductQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L729). The attribute's comment: “X has exactly one point”.

> **Stacks 06MS.** The space of points of `X = U/G` is a singleton.

```lean
theorem nonempty_unique_points_galoisSelfProductQuotient :
    Nonempty (Unique
      (Space.points B cover.left hS (galoisSelfProductQuotient B₀ hQ hK B hS hU)))
```

**`AlgebraicGeometry.RationalGaloisQuotient.not_isEquivalence_substackInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 777](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L777). The attribute's comment: “the morphism Stacks 06MR constructs for X is not an isomorphism: for every object property of X satisfying the conditions of Stacks 06MR, its substack inclusion is not an equivalence over the big fppf site”.

> **Stacks 06MS, the assertion about the morphism of Stacks 06MR.** Let `P` be any object
> property of `X` of the kind **Stacks 06MR** produces, that is one which is closed under
> isomorphism and cuts out an algebraic stack satisfying condition (2) of **Stacks 06MP**. Then
> the inclusion `X_P ⟶ X` is *not* an equivalence over the big fppf site, which is this library's
> notion of an isomorphism of algebraic stacks.
>
> Stacks 06MR asserts that exactly one object property of `X` has that kind, so this says that
> the morphism Stacks 06MR constructs for `X` is not an isomorphism. Quantifying over all
> candidates rather than naming the one Stacks 06MR constructs avoids the two undischarged
> hypotheses under which this library proves the existence half of Stacks 06MR, and makes the
> statement stronger rather than weaker.
>
> If the inclusion were an equivalence, condition (2) of Stacks 06MP would transport to `X`, and
> condition (1) — in particular local Noetherianity — would follow; but `X` is not locally
> Noetherian.

```lean
theorem not_isEquivalence_substackInclusion
    (P : ObjectProperty (quotientStack.{w} B₀ hQ hK B hS hU).val.val.obj)
    (hP : Stack.IsReducedLocallyNoetherianUniquePointSubstack.{0, w} B cover.left hS
      (quotientStack.{w} B₀ hQ hK B hS hU) P) :
    ¬ Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor
      (Stack.fullSubcategoryInclusion (quotientStack.{w} B₀ hQ hK B hS hU) P
        hP.2.choose).hom)
```

**`AlgebraicGeometry.RationalGaloisQuotient.isReducedWithUniquePoint_quotientStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 797](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L797). The attribute's comment: “X, as an algebraic stack, is reduced with exactly one point: the hypothesis of Lemma 06MR”.

> **Stacks 06MS.** `X`, as an algebraic stack, satisfies the hypothesis of **Stacks 06MR**,
> condition (1) of **Stacks 06MN**: it is reduced and its space of points is a singleton.

```lean
theorem isReducedWithUniquePoint_quotientStack :
    Stack.IsReducedWithUniquePoint B cover.left hS (quotientStack.{w} B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.isMonomorphism_canonicalPointStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L842). The attribute's comment: “x is a monomorphism of algebraic stacks”.

> **Stacks 06MS.** `x : Spec(ℚ̄) ⟶ X` is a monomorphism of algebraic stacks in the sense of
> **Stacks 04ZW**: it is fully faithful because `x` is a monomorphism of sheaves, and a fully
> faithful 1-morphism of algebraic stacks is a monomorphism.

```lean
theorem isMonomorphism_canonicalPointStack :
    Stack.AlgebraicStacks.IsMonomorphism B cover.left hS
      (canonicalPointStack.{w} B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.isReducedLocallyNoetherianUniquePointSubstack_canonicalPointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 874](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L874). The attribute's comment: “x is the morphism constructed in Lemma 06MR, and it is not an isomorphism: the substack of X cut out by x is closed under isomorphism, algebraic and satisfies the conditions of 06MP, x factors through its inclusion by an equivalence, and that inclusion is not an equivalence”.

> **Stacks 06MS: `x` is the morphism constructed in Lemma 06MR.** The strictly full
> subcategory of `X` cut out by `x : Spec(ℚ̄) ⟶ X` is a substack of the kind **Stacks 06MR**
> produces for the reduced one-point algebraic stack `X`: it is closed under isomorphism, its full
> subcategory is an algebraic stack, and that algebraic stack satisfies condition (2) of
> **Stacks 06MP**. Moreover `x` factors through the inclusion of that substack by a 1-morphism whose
> underlying functor is an equivalence of categories, so `x` *is* the inclusion morphism of
> Lemma 06MR up to equivalence. And that inclusion morphism is *not* an isomorphism: it is not an
> equivalence over the big fppf site, because `X` is not locally Noetherian.

```lean
theorem isReducedLocallyNoetherianUniquePointSubstack_canonicalPointSubstack :
    Stack.IsReducedLocallyNoetherianUniquePointSubstack.{0, w} B cover.left hS
        (quotientStack.{w} B₀ hQ hK B hS hU) (canonicalPointSubstack.{w} B₀ hQ hK B hS hU) ∧
      ∃ hP : Stack.IsAlgebraicStack.{0, w} B cover.left hS
          (Stack.fullSubcategoryBased (quotientStack.{w} B₀ hQ hK B hS hU)
            (canonicalPointSubstack.{w} B₀ hQ hK B hS hU)),
        ∃ t : Stack.schemeStack.{0, w} B cover.left hS (baseFieldSpectrum B hS).base ⟶
            Stack.fullSubcategoryAlgebraicStack (quotientStack.{w} B₀ hQ hK B hS hU)
              (canonicalPointSubstack.{w} B₀ hQ hK B hS hU) hP,
          Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor t.hom) ∧
            Nonempty (t ≫ Stack.fullSubcategoryInclusion (quotientStack.{w} B₀ hQ hK B hS hU)
              (canonicalPointSubstack.{w} B₀ hQ hK B hS hU) hP ≅
                canonicalPointStack.{w} B₀ hQ hK B hS hU ≫ 𝟙 _) ∧
          ¬ Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor
            (Stack.fullSubcategoryInclusion (quotientStack.{w} B₀ hQ hK B hS hU)
              (canonicalPointSubstack.{w} B₀ hQ hK B hS hU) hP).hom)
```

**`AlgebraicGeometry.RationalGaloisQuotient.isReducedLocallyNoetherianUniquePointSubstack_iff_eq_canonicalPointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 911](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L911). The attribute's comment: “x is the morphism constructed in Lemma 06MR: the substack cut out by x is the unique strictly full subcategory of X which is an algebraic stack satisfying the conditions of 06MP”.

> **Stacks 06MS: `x` is the morphism constructed in Lemma 06MR.** The substack of `X` cut out
> by `x : Spec(ℚ̄) ⟶ X` is *the* strictly full subcategory of `X` which Stacks 06MR produces: a
> strictly full subcategory of `X` is an algebraic stack satisfying the conditions of
> **Stacks 06MP** if and only if it is the substack cut out by `x`.
>
> Uniqueness is the argument of Stacks 06MR. Its input, that the inclusion of a strictly full
> algebraic substack is a monomorphism, holds because `X` is an algebraic space: such a substack is
> a stack in setoids, hence an algebraic space by **Stacks 04SZ**, so its inclusion is
> representable by algebraic spaces by **Stacks 02ZZ**.

```lean
theorem isReducedLocallyNoetherianUniquePointSubstack_iff_eq_canonicalPointSubstack
    (Q : ObjectProperty (quotientStack.{w} B₀ hQ hK B hS hU).val.val.obj) :
    Stack.IsReducedLocallyNoetherianUniquePointSubstack.{0, w} B cover.left hS
        (quotientStack.{w} B₀ hQ hK B hS hU) Q ↔
      Q = canonicalPointSubstack.{w} B₀ hQ hK B hS hU
```

**`AlgebraicGeometry.RationalGaloisQuotient.le_canonicalPointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 935](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L935). The attribute's comment: “x is the morphism constructed in Lemma 06MR: every strictly full subcategory of X with the properties of Lemma 06MR is contained in the substack cut out by x”.

> **Stacks 06MS: `x` is the morphism constructed in Lemma 06MR, the uniqueness half.** Every
> strictly full subcategory of `X` of the kind **Stacks 06MR** produces — closed under isomorphism,
> algebraic, and satisfying condition (2) of **Stacks 06MP** — is contained in the substack cut out
> by `x`.
>
> This is one half of
> `AlgebraicGeometry.RationalGaloisQuotient`
> `.isReducedLocallyNoetherianUniquePointSubstack_iff_eq_canonicalPointSubstack`.

```lean
theorem le_canonicalPointSubstack
    (Q : ObjectProperty (quotientStack.{w} B₀ hQ hK B hS hU).val.val.obj)
    (hQ' : Stack.IsReducedLocallyNoetherianUniquePointSubstack.{0, w} B cover.left hS
      (quotientStack.{w} B₀ hQ hK B hS hU) Q) :
    Q ≤ canonicalPointSubstack.{w} B₀ hQ hK B hS hU
```

**`AlgebraicGeometry.RationalGaloisQuotient.isResidualGerbeAt_canonicalPointSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 950](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L950). The attribute's comment: “Spec(ℚ̄) ⟶ X is the residual gerbe of X at x”.

> **Stacks 06MS: `Spec(ℚ̄) ⟶ X` is the residual gerbe of `X` at `x`.** The residual gerbe of
> `X` at `x` exists in the sense of **Stacks 06MU (1)** — `x : Spec(ℚ̄) ⟶ X` is a monomorphism from
> a reduced algebraic stack with a single point mapping to `x` — and the strictly full subcategory
> cut out by `x` meets the specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of
> **Stacks 06MT** that defines the residual gerbe of **Stacks 06MU (2)**: it is a reduced, locally
> Noetherian algebraic stack with exactly one point, lying over `x`.

```lean
theorem isResidualGerbeAt_canonicalPointSubstack :
    Stack.HasReducedSingletonPointMonomorphism B cover.left hS
        (quotientStack.{w} B₀ hQ hK B hS hU) (canonicalStackPoint.{w} B₀ hQ hK B hS hU) ∧
      Stack.IsResidualGerbeAt B cover.left hS (quotientStack.{w} B₀ hQ hK B hS hU)
        (canonicalStackPoint.{w} B₀ hQ hK B hS hU)
        (canonicalPointSubstack.{w} B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.isLocallyOfFiniteType_canonicalPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 971](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L971). The attribute's comment: “x : Spec(ℚ̄) ⟶ U ⟶ X is locally of finite type”.

> **Stacks 06MS.** `x : Spec(ℚ̄) ⟶ U ⟶ X` is locally of finite type: the diagonal
> `Spec(ℚ̄) ⟶ U` is a closed immersion, `U` being separated over `Spec(ℚ̄)`, and `U ⟶ X` is étale.

```lean
theorem isLocallyOfFiniteType_canonicalPoint :
    Space.IsLocallyOfFiniteType B cover.left hS (canonicalPoint B₀ hQ hK B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.ne_and_isReducedUniquePointSubstackAt_canonicalPointSubstack_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean, line 1070](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeNotIsomorphismExample.lean#L1070). The attribute's comment: “imposing that residual gerbes are locally Noetherian is necessary in Definition 06MU: without that clause the substack cut out by x and all of X are two distinct reduced one-point substacks over x with monomorphic inclusions, and only the first is locally Noetherian”.

> **Stacks 06MS: imposing that residual gerbes be locally Noetherian is necessary in
> Definition 06MU.** Drop the local Noetherianity clause from the specification
> `AlgebraicGeometry.Stack.IsResidualGerbeAt` of the residual gerbe, leaving
> `AlgebraicGeometry.Stack.IsReducedUniquePointSubstackAt`: a strictly full subcategory which is a
> reduced algebraic stack with exactly one point, lying over `x`. Then two *distinct* strictly full
> subcategories of `X` meet it at `x` — the substack cut out by `x` and all of `X` — and both
> inclusions are monomorphisms of algebraic stacks; so the residual gerbe would not be unique. The
> local Noetherianity clause is exactly what tells them apart: the substack cut out by `x` is the
> residual gerbe of `X` at `x`, and all of `X` is not locally Noetherian.

```lean
theorem ne_and_isReducedUniquePointSubstackAt_canonicalPointSubstack_top :
    canonicalPointSubstack.{w} B₀ hQ hK B hS hU ≠ ⊤ ∧
      Stack.IsReducedUniquePointSubstackAt B cover.left hS (quotientStack.{w} B₀ hQ hK B hS hU)
        (canonicalStackPoint.{w} B₀ hQ hK B hS hU) (canonicalPointSubstack.{w} B₀ hQ hK B hS hU) ∧
      Stack.IsReducedUniquePointSubstackAt B cover.left hS (quotientStack.{w} B₀ hQ hK B hS hU)
        (canonicalStackPoint.{w} B₀ hQ hK B hS hU) ⊤ ∧
      (∀ (P : ObjectProperty (quotientStack.{w} B₀ hQ hK B hS hU).val.val.obj)
        (hP : Stack.IsAlgebraicStack.{0, w} B cover.left hS
          (Stack.fullSubcategoryBased (quotientStack.{w} B₀ hQ hK B hS hU) P)),
        Stack.AlgebraicStacks.IsMonomorphism B cover.left hS
          (Stack.fullSubcategoryInclusion (quotientStack.{w} B₀ hQ hK B hS hU) P hP)) ∧
      Stack.IsResidualGerbeAt B cover.left hS (quotientStack.{w} B₀ hQ hK B hS hU)
        (canonicalStackPoint.{w} B₀ hQ hK B hS hU) (canonicalPointSubstack.{w} B₀ hQ hK B hS hU) ∧
      ¬ Stack.IsResidualGerbeAt B cover.left hS (quotientStack.{w} B₀ hQ hK B hS hU)
        (canonicalStackPoint.{w} B₀ hQ hK B hS hU) ⊤
```

## Tag 06MT, a lemma

[Tag 06MT](https://stacks.math.columbia.edu/tag/06MT) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_iff_hasReducedSingletonPointMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeEquivalentConditions.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeEquivalentConditions.lean#L191). The attribute's comment: “conditions (1) and (2) are equivalent, granting the existence half of Stacks 0509 at the whole point set — that every algebraic stack over S has a reduction, a reduced closed substack whose inclusion is surjective on points — which is the hypothesis hreduction. That hypothesis is quantified over every algebraic stack over S, mentions neither the stack nor the point the conclusion ranges over, and so restricts no object; the library does not have it, its Stacks 050C recording the reduction as a predicate for that reason”.

> **Conditions (1) and (2) of Stacks 06MT are equivalent.** A point of an algebraic stack over
> `S` is the image of the singleton space of points of a monomorphism to it exactly when it is the
> image of the singleton space of points of a monomorphism with reduced source.
>
> The implication (2) ⟹ (1) is
> `AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_reduced`, which the source calls
> immediate; the implication (1) ⟹ (2) is
> `AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_of_hasSingletonPointMonomorphism`,
> which passes to the reduction of Stacks 0509.

```lean
theorem hasSingletonPointMonomorphism_iff_hasReducedSingletonPointMonomorphism
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (x : AlgebraicStacks.points B S hS 𝒳) :
    HasSingletonPointMonomorphism B S hS 𝒳 x ↔
      HasReducedSingletonPointMonomorphism B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_iff_hasFlatFieldCoverMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeEquivalentConditions.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeEquivalentConditions.lean#L213). The attribute's comment: “conditions (2) and (3) are equivalent; unconditional”.

> **Conditions (2) and (3) of Stacks 06MT are equivalent.** A point of an algebraic stack over
> `S` is the image of the singleton space of points of a monomorphism with reduced source exactly
> when it is the image, under a monomorphism, of a point of the spectrum of a field covering the
> source surjectively and flatly.
>
> Both directions are the equivalence of conditions (1) and (2) of **Stacks 06MN**,
> `AlgebraicGeometry.Stack.isReducedWithUniquePoint_iff_hasFlatFieldSpectrumCover`, applied to the
> source of the monomorphism, which is left unchanged. Going forwards, the unique point of the
> source has a preimage on the cover because the cover is surjective; going backwards, the image
> of the chosen point of the cover is a point of the source, and the source has at most one
> point.

```lean
theorem hasReducedSingletonPointMonomorphism_iff_hasFlatFieldCoverMonomorphism
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (x : AlgebraicStacks.points B S hS 𝒳) :
    HasReducedSingletonPointMonomorphism B S hS 𝒳 x ↔
      HasFlatFieldCoverMonomorphism B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_iff_hasFlatFieldCoverMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeEquivalentConditions.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeEquivalentConditions.lean#L244). The attribute's comment: “conditions (1) and (3) are equivalent, granting the existence half of Stacks 0509 at the whole point set — that every algebraic stack over S has a reduction — which is the hypothesis hreduction, used only for the forward implication. That hypothesis is quantified over every algebraic stack over S, mentions neither the stack nor the point the conclusion ranges over, and so restricts no object; the library does not have it”.

> **Conditions (1) and (3) of Stacks 06MT are equivalent.** The implication (1) ⟹ (3) is
> (1) ⟹ (2) followed by (2) ⟹ (3); the implication (3) ⟹ (1) is
> `AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_flatFieldCover`.

```lean
theorem hasSingletonPointMonomorphism_iff_hasFlatFieldCoverMonomorphism
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (x : AlgebraicStacks.points B S hS 𝒳) :
    HasSingletonPointMonomorphism B S hS 𝒳 x ↔ HasFlatFieldCoverMonomorphism B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_iff_hasSingletonPointMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeExistsUnique.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeExistsUnique.lean#L165). The attribute's comment: “conditions (1) and (2) are equivalent, unconditionally: the reduction is the theorem `exists_reduction` (Stacks 0509), so nothing is assumed. This supersedes the base's `hasSingletonPointMonomorphism_iff_hasReducedSingletonPointMonomorphism`, which carries `hreduction`”.

> **Conditions (1) and (2) of Stacks 06MT are equivalent.** Let `𝒳` be an algebraic stack over
> `S` and let `x` be a point of `|𝒳|`. Some *reduced* algebraic stack admits a monomorphism to `𝒳`
> whose space of points is a singleton mapping to `x` if and only if some algebraic stack does.
>
> The forward implication is `AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_reduced`,
> which the source calls immediate. For the converse the source replaces the given `𝒵` by its
> reduction, and so does this proof. The reduction is `AlgebraicGeometry.Stack.exists_reduction`,
> the reduced closed substack of **Stacks 0509** on the whole of `|𝒵|`; its inclusion
> `j : 𝒵_red ⟶ 𝒵` is a monomorphism, being representable by algebraic spaces as a closed immersion
> and fully faithful as the inclusion of a full subcategory, so `j` composed with the given
> monomorphism is one by **Stacks 04ZY**. The space `|𝒵_red|` is a singleton because `j` is
> surjective on points by the choice of the reduction and injective on them by **Stacks 0500**,
> `|𝒵|` being a singleton; and the unique point of `𝒵_red` maps to the unique point of `𝒵`, hence
> to `x`.

```lean
theorem hasReducedSingletonPointMonomorphism_iff_hasSingletonPointMonomorphism
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (x : AlgebraicStacks.points B S hS 𝒳) :
    HasReducedSingletonPointMonomorphism B S hS 𝒳 x ↔
      HasSingletonPointMonomorphism B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.tfae_hasSingletonPointMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeExistsUnique.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeExistsUnique.lean#L202). The attribute's comment: “the equivalence of conditions (1), (2) and (3), unconditionally: (1) iff (2) is `hasReducedSingletonPointMonomorphism_iff_hasSingletonPointMonomorphism` of this file, proved from the theorem `exists_reduction`, not the base's `hreduction`-carrying version”.

> **Stacks 06MT, the equivalence of conditions (1), (2) and (3).** Let `𝒳` be an algebraic stack
> over `S` and let `x` be a point of `|𝒳|`. The following are equivalent:
>
> 1. some algebraic stack admits a monomorphism to `𝒳` whose space of points is a singleton mapping
>    to `x`;
> 2. some reduced algebraic stack does;
> 3. some algebraic stack `𝒵` admits a monomorphism `f : 𝒵 ⟶ 𝒳` and a surjective flat 1-morphism
>    `z : Spec(k) ⟶ 𝒵` from the spectrum of a field, with `x = f(z)`.
>
> The equivalence of (1) and (2) is
> `AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_iff_hasSingletonPointMonomorphism`
> and that of (2) and (3) is
> `AlgebraicGeometry.Stack.hasReducedSingletonPointMonomorphism_iff_hasFlatFieldCoverMonomorphism`.

```lean
theorem tfae_hasSingletonPointMonomorphism
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (x : AlgebraicStacks.points B S hS 𝒳) :
    List.TFAE
      [HasSingletonPointMonomorphism B S hS 𝒳 x,
        HasReducedSingletonPointMonomorphism B S hS 𝒳 x,
        HasFlatFieldCoverMonomorphism B S hS 𝒳 x]
```

**`AlgebraicGeometry.Stack.existsUnique_isResidualGerbeAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeExistsUnique.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeExistsUnique.lean#L264). The attribute's comment: “the final assertion: under the equivalent conditions there is a unique strictly full subcategory of X which is a reduced, locally Noetherian algebraic stack whose space of points is a singleton mapping to x; unconditional, through this file's (1) iff (2) and the unconditional 06MR”.

> Let `𝒳` be an algebraic stack over `S` and let `x` be a point of `|𝒳|` such that some
> algebraic stack whose space of points is a singleton mapping to `x` admits a monomorphism to
> `𝒳` (`HasSingletonPointMonomorphism`). Then there is exactly one strictly full subcategory
> `𝒵_x ⊂ 𝒳` which is a reduced, locally Noetherian algebraic stack whose space of points is a
> singleton mapping to `x`.

```lean
theorem existsUnique_isResidualGerbeAt
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (x : AlgebraicStacks.points B S hS 𝒳)
    (h : HasSingletonPointMonomorphism B S hS 𝒳 x) :
    ∃! P : ObjectProperty 𝒳.val.val.obj, IsResidualGerbeAt B S hS 𝒳 x P
```

## Tag 06MU, a definition

[Tag 06MU](https://stacks.math.columbia.edu/tag/06MU) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasReducedSingletonPointMonomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean#L165). The attribute's comment: “part (1), the existence of the residual gerbe of X at x, read as condition (2) of the three equivalent conditions of Stacks 06MT”.

> **Condition (2) of Stacks 06MT.** The one-point substack of condition (1) can be chosen
> reduced.

```lean
abbrev HasReducedSingletonPointMonomorphism
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property)) : Prop
```

**`AlgebraicGeometry.Stack.residualGerbe`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean#L262). The attribute's comment: “part (2), the residual gerbe as an algebraic stack: the strictly full subcategory of X cut out by an object property meeting the specification IsResidualGerbeAt of Stacks 06MT”.

> **Stacks 06MU, part (2): the residual gerbe of `𝒳` at `x`, as an algebraic stack.** The
> source takes it to be the strictly full subcategory `𝒵_x ⊂ 𝒳` produced by **Stacks 06MT**, that
> is, the one cut out by an object property of `𝒳` meeting the specification
> `AlgebraicGeometry.Stack.IsResidualGerbeAt`: closed under isomorphism, with full subcategory a
> reduced, locally Noetherian algebraic stack having exactly one point, lying over `x`.
>
> That object property `P` and the proof `hP` that it meets the specification are the data of this
> definition. They are the defining property of the object being defined — what the source supposes
> when it says that, the residual gerbe existing, it *is* `𝒵_x` — and not a substitute for an
> unproved result: the algebraic stack returned is
> `AlgebraicGeometry.Stack.fullSubcategoryAlgebraicStack` at `P`, whose algebraicity is one of the
> conjuncts of `hP`.
>
> Nothing here picks `P` out. Uniqueness of the object property, and with it the definite article
> in "*the* residual gerbe", is the final assertion of Stacks 06MT; the library proves it as
> `AlgebraicGeometry.Stack.eq_of_isResidualGerbeAt_of_bootstrap`, and the existence of such an
> object property relative to Stacks 06FI, as `AlgebraicGeometry.Stack`
> `.exists_isResidualGerbeAt_of_hasReducedSingletonPointMonomorphism`, both in
> `StacksFrontier.AlgebraicGeometry.Stacks.ResidualGerbeEquivalentConditions`.

```lean
abbrev residualGerbe
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property))
    (P : ObjectProperty 𝒳.val.val.obj) (hP : IsResidualGerbeAt B S hS 𝒳 x P) :
    AlgebraicStacks.{u, w} B S hS
```

**`AlgebraicGeometry.Stack.residualGerbeInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbe.lean#L285). The attribute's comment: “part (2), the inclusion of the residual gerbe into X as a strictly full subcategory”.

> **Stacks 06MU, part (2): the inclusion of the residual gerbe of `𝒳` at `x`.** The residual
> gerbe is a *strictly full subcategory* of `𝒳`, and this is the inclusion 1-morphism `𝒵_x ⟶ 𝒳`
> that makes it one: `AlgebraicGeometry.Stack.fullSubcategoryInclusion` at the object property
> witnessing the specification.
>
> The inclusion is fully faithful, being the inclusion of a full subcategory
> (`AlgebraicGeometry.Stack.full_fullSubcategoryInclusion` and
> `AlgebraicGeometry.Stack.faithful_fullSubcategoryInclusion`), and it satisfies the monomorphy
> clause of **Stacks 04ZW** by
> `AlgebraicGeometry.Stack.AlgebraicStacks.mono_representingMaps_fullSubcategoryInclusion`. That it
> is also representable by algebraic spaces, and so a monomorphism, is
> `AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_fullSubcategoryInclusion`, the last
> assertion of Stacks 06MR, in a module downstream of this one.

```lean
def residualGerbeInclusion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property))
    (P : ObjectProperty 𝒳.val.val.obj) (hP : IsResidualGerbeAt B S hS 𝒳 x P) :
    residualGerbe B S hS 𝒳 x P hP ⟶ 𝒳
```

## Tag 0H21, an example

[Tag 0H21](https://stacks.math.columbia.edu/tag/0H21) in the Stacks Project.

**`AlgebraicGeometry.Stack.isMonomorphism_and_isResidualGerbeAt_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeSchemePoint.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeSchemePoint.lean#L272). The attribute's comment: “the scheme case: the monomorphism x ⟶ X out of the spectrum of the residue field at a point x of a scheme X is the residual gerbe of X at x”.

> **Stacks 0H21, assertion (1).** Let `X` be an object of the big fppf site of `S`, let `x` be a
> point of its underlying scheme and assume the spectrum of the residue field `κ(x)` lies in the
> site. Identifying `x` with `Spec (κ(x))`, the 1-morphism `x ⟶ X` of algebraic stacks over `S` is
> a monomorphism (**Stacks 04ZW**) and the strictly full subcategory of `(Sch/X)_fppf` it cuts out
> is the residual gerbe of `(Sch/X)_fppf` at `x`, in the sense of
> `AlgebraicGeometry.Stack.IsResidualGerbeAt` (the specification of **Stacks 06MT**).
>
> The point of `|(Sch/X)_fppf|` is `AlgebraicGeometry.Stack.residueFieldPointClass`, the class of
> the tautological field-valued point of `Spec (κ(x))`, which is the point determined by `x` under
> the usual identification of the points of `(Sch/X)_fppf` with the points of `X`.

```lean
theorem isMonomorphism_and_isResidualGerbeAt_residueField
    (X : BigFppfOver B S hS) (x : (BigFppfOver.toScheme B S hS).obj X)
    (hx : B.Contains (Spec (((BigFppfOver.toScheme B S hS).obj X).residueField x))) :
    AlgebraicStacks.IsMonomorphism B S hS
        (schemeStackMap.{u, w} B S hS (residueFieldInclusion B S hS X x hx)) ∧
      IsResidualGerbeAt B S hS (schemeStack.{u, w} B S hS X)
        (residueFieldPointClass.{u, w} B S hS X x hx)
        (CatFiberedInGroupoids.homFunctor
          (schemeStackMap.{u, w} B S hS (residueFieldInclusion B S hS X x hx)).hom).essImage
```

**`AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_algebraicSpaceStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeSchemePoint.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeSchemePoint.lean#L299). The attribute's comment: “the algebraic space case: the residual gerbe at a point of an algebraic space, called the residual space, always exists”.

> **Stacks 0H21, assertion (2).** Let `F` be an algebraic space over `S` and let `x` be a point
> of `|F|`. Then the residual gerbe of `F` at `x` — the *residual space* at `x` — exists: the
> algebraic stack of `F` satisfies condition (1) of **Stacks 06MT** at `x`, which by **Stacks 06MU**
> is existence of the residual gerbe there.
>
> The algebraic stack of `F` is represented by `F` itself, so this is
> `AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_isRepresentableByAlgebraicSpace`, whose
> witness is the 1-morphism induced by the residual space of **Stacks 06R0**; residual spaces exist
> by **Stacks 06QZ**.

```lean
theorem hasSingletonPointMonomorphism_algebraicSpaceStack
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (x : AlgebraicStacks.points B S hS (algebraicSpaceStack.{u, w} B S hS F hF)) :
    HasSingletonPointMonomorphism B S hS (algebraicSpaceStack.{u, w} B S hS F hF) x
```

## Tag 06MV, a lemma

[Tag 06MV](https://stacks.math.columbia.edu/tag/06MV) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRegularStack_of_isReducedLocallyNoetherianWithUniquePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RegularSingletonStack.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RegularSingletonStack.lean#L129).

> A reduced, locally Noetherian algebraic stack over `S` whose space of points of
> **Stacks 04XG** is a singleton is regular.
>
> Reducedness and singletonness give a surjective flat 1-morphism `Spec k ⟶ 𝒵` out of the spectrum
> of a field by **Stacks 06MN**. Against a locally Noetherian smooth surjective scheme atlas
> `V ⟶ 𝒵`, the 2-fibre product `Spec k ×_𝒵 V` is represented by an algebraic space which is smooth
> over `Spec k`, hence regular by **Stacks 06M1**, and whose projection to `V` is flat and
> surjective, so `V` is regular by **Stacks 06MK**.

```lean
theorem isRegularStack_of_isReducedLocallyNoetherianWithUniquePoint
    (𝒵 : AlgebraicStacks.{u, w} B S hS)
    (h : IsReducedLocallyNoetherianWithUniquePoint B S hS 𝒵) :
    IsRegularStack B S hS 𝒵
```

## Tag 06MW, a lemma

[Tag 06MW](https://stacks.math.columbia.edu/tag/06MW) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_factorization_of_isResidualGerbeAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFieldPointFactorization.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFieldPointFactorization.lean#L229).

> **Stacks 06MW.** Let `𝒳` be an algebraic stack over `S`, let `x` be a point of `|𝒳|` and
> assume the residual gerbe `𝒵_x` of `𝒳` at `x` exists, i.e. an object property `P` of `𝒳`
> satisfies the specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of **Stacks 06MT**. Let
> `f` be a 1-morphism to `𝒳` from the algebraic stack of the spectrum of a field, some point of
> which maps to `x`. Then `f` factors through the inclusion `𝒵_x ⟶ 𝒳`: there is a 1-morphism `g`
> to the full subcategory selected by `P` and a 2-isomorphism `g ≫ (𝒵_x ⟶ 𝒳) ≅ f`.
>
> The factorisation is `AlgebraicGeometry.Stack.exists_factorization_of_hasUniquePointOver`, which
> uses only the one-point clause of `IsResidualGerbeAt`. It needs the inclusion `𝒵_x ⟶ 𝒳` to be a
> monomorphism, so representable by algebraic spaces; the source has this from Stacks 04Y5, the
> inclusion being fully faithful, and the library has the implication (2) ⟹ (3) of Stacks 04Y5 as
> `AlgebraicGeometry.Stack.AlgebraicStacks.isRepresentableByAlgebraicSpaces_of_faithful`,
> from the bootstrap theorem Stacks 04S6 part (3).

```lean
theorem exists_factorization_of_isResidualGerbeAt
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : AlgebraicStacks.points B S hS 𝒳)
    (P : ObjectProperty 𝒳.val.val.obj)
    (hP : IsResidualGerbeAt B S hS 𝒳 x P)
    (F : FieldSpectrum B S hS) (f : schemeStack.{u, w} B S hS F.base ⟶ 𝒳)
    (t : AlgebraicStacks.points B S hS (schemeStack.{u, w} B S hS F.base))
    (ht : AlgebraicStacks.pointsMap B S hS f t = x) :
    ∃ g : schemeStack.{u, w} B S hS F.base ⟶ fullSubcategoryAlgebraicStack 𝒳 P hP.2.choose,
      Nonempty (g ≫ fullSubcategoryInclusion 𝒳 P hP.2.choose ≅ f)
```

## Tag 06MX, a lemma

[Tag 06MX](https://stacks.math.columbia.edu/tag/06MX) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isResidualGerbeAt_of_isMonomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFromMonomorphism.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFromMonomorphism.lean#L210). The attribute's comment: “with the equivalent conditions of Stacks 06MP read as its CONDITION (2), `Dualizing`-style condition (1) being unavailable here: the library proves only (2) => (1) of 06MP, its (1) => (2) resting on fppf descent of flatness (05VY, 06Q0) which is not carried, and there is no transport of `IsReducedStack`/`IsLocallyNoetherianStack` — both `HasPropertyOnSomeSchemeAtlas` — along an equivalence over the site. Otherwise unconditional. The uniqueness of the subcategory is NOT claimed: that is Stacks 06MR, which carries the representability hypothesis of 04Y5 (2) => (3)”.

> **Stacks 06MX.** Let `𝒳` be an algebraic stack over `S`, let `x` be a point of its space of
> points of **Stacks 04XG**, let `𝒵` be an algebraic stack over `S` satisfying condition (2) of
> **Stacks 06MP**, and let `f : 𝒵 ⟶ 𝒳` be a monomorphism whose image on points is exactly `{x}`.
> Then the residual gerbe of `𝒳` at `x` exists — some object property of `𝒳` satisfies the
> specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of **Stacks 06MT** — and `f` factors
> through the inclusion of that full subcategory by a 1-morphism whose underlying functor is an
> equivalence of categories.
>
> The object property is the essential image of the functor underlying `f`. The monomorphism `f`
> is fully faithful by **Stacks 05UK**, so the factorization through the essential image is an
> equivalence of categories, hence an equivalence over the big fppf site by **Stacks 003Z**; the
> full subcategory is therefore an algebraic stack by **Stacks 03YQ** and inherits condition (2)
> of Stacks 06MP, which makes it reduced, locally Noetherian and one-point by the implication
> (2) ⟹ (1) of Stacks 06MP. Its point lies over `x` because the factorization 2-commutes and the
> image of `|f|` is `{x}`.

```lean
theorem exists_isResidualGerbeAt_of_isMonomorphism
    (𝒳 𝒵 : AlgebraicStacks.{u, w} B S hS) (f : 𝒵 ⟶ 𝒳)
    (hf : AlgebraicStacks.IsMonomorphism B S hS f)
    (h𝒵 : HasLocallyOfFinitePresentationFlatFieldSpectrumCover B S hS 𝒵)
    (x : AlgebraicStacks.points B S hS 𝒳)
    (himg : Set.range (AlgebraicStacks.pointsMap B S hS f) = {x}) :
    ∃ (P : ObjectProperty 𝒳.val.val.obj)
      (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P)),
      IsResidualGerbeAt B S hS 𝒳 x P ∧
        ∃ g : 𝒵 ⟶ fullSubcategoryAlgebraicStack 𝒳 P hP,
          Functor.IsEquivalence (CatFiberedInGroupoids.homFunctor g.hom) ∧
            Nonempty (g ≫ fullSubcategoryInclusion 𝒳 P hP ≅ f)
```

## Tag 0DTH, a lemma

[Tag 0DTH](https://stacks.math.columbia.edu/tag/0DTH) in the Stacks Project.

**`AlgebraicGeometry.Stack.residualGerbeMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFunctoriality.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFunctoriality.lean#L121). The attribute's comment: “the 1-morphism induced between substacks whose objects f carries into one another”.

> **The 1-morphism induced by `f` on residual gerbes, Stacks 0DTH.** Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks over `S`, let `P` cut out a substack `𝒵_x` of `𝒳` and let `Q` cut
> out a substack `𝒵_y` of `𝒴`. If `f` carries every object of `𝒳` with the property `P` to an
> object of `𝒴` with the property `Q`, then it induces a 1-morphism `𝒵_x ⟶ 𝒵_y`, namely the lift
> through the full subcategory `𝒵_y` of the underlying functor of `𝒵_x ⟶ 𝒳 ⟶ 𝒴`.
>
> In the application `P` and `Q` are the residual gerbes of `𝒳` at `x` and of `𝒴` at its image,
> and `hmem` is `AlgebraicGeometry.Stack.map_mem_of_isResidualGerbeAt`.

```lean
def residualGerbeMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    {P : ObjectProperty 𝒳.val.val.obj} {Q : ObjectProperty 𝒴.val.val.obj}
    (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    (hQ : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒴 Q))
    (hmem : ∀ ξ : 𝒳.val.val.obj, P ξ → Q (f.hom.hom.toFunctor.obj ξ)) :
    fullSubcategoryAlgebraicStack 𝒳 P hP ⟶ fullSubcategoryAlgebraicStack 𝒴 Q hQ
```

**`AlgebraicGeometry.Stack.residualGerbeMap_comp_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFunctoriality.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFunctoriality.lean#L138). The attribute's comment: “the commutativity of the square for that 1-morphism”.

> **The commutative square of Stacks 0DTH.** The induced 1-morphism `𝒵_x ⟶ 𝒵_y` composed with
> the inclusion of `𝒵_y` into `𝒴` is the inclusion of `𝒵_x` into `𝒳` composed with `f`.

```lean
theorem residualGerbeMap_comp_inclusion
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    {P : ObjectProperty 𝒳.val.val.obj} {Q : ObjectProperty 𝒴.val.val.obj}
    (hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    (hQ : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒴 Q))
    (hmem : ∀ ξ : 𝒳.val.val.obj, P ξ → Q (f.hom.hom.toFunctor.obj ξ)) :
    residualGerbeMap B S hS f hP hQ hmem ≫ fullSubcategoryInclusion 𝒴 Q hQ =
      fullSubcategoryInclusion 𝒳 P hP ≫ f
```

**`AlgebraicGeometry.Stack.residualGerbeMap_comp_inclusion_of_isResidualGerbeAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFunctoriality.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeFunctoriality.lean#L211).

> **Stacks 0DTH.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let `x` be a
> point of `𝒳` and let `y` be its image under `f`. Assume the residual gerbes of `𝒳` at `x` and of
> `𝒴` at `y` exist, cut out by the object properties `P` and `Q` respectively, in the sense of the
> specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of Stacks 06MT. Then `f` induces a
> commutative square: the 1-morphism `residualGerbeMap` from the residual gerbe at `x` to the
> residual gerbe at `y`, composed with the inclusion of the latter, is the inclusion of the former
> composed with `f`.
>
> That `f` carries the residual gerbe at `x` into the one at `y` is
> `AlgebraicGeometry.Stack.map_mem_of_isResidualGerbeAt`, the source's argument through Stacks 06MQ;
> it uses the bootstrap theorem Stacks 04S6 part (3) for the representability by algebraic spaces
> of the inclusion of the residual gerbe at `y` that the source takes from Stacks 04Y5.

```lean
theorem residualGerbeMap_comp_inclusion_of_isResidualGerbeAt
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property))
    (y : points B S hS 𝒴.val.val (Classical.choose 𝒴.property))
    (hxy : pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
      (Classical.choose 𝒴.property) f.hom.hom x = y)
    (P : ObjectProperty 𝒳.val.val.obj) (Q : ObjectProperty 𝒴.val.val.obj)
    (hx : IsResidualGerbeAt B S hS 𝒳 x P) (hy : IsResidualGerbeAt B S hS 𝒴 y Q) :
    residualGerbeMap B S hS f hx.2.choose hy.2.choose
        (map_mem_of_isResidualGerbeAt B S hS f x y hxy hx hy) ≫
        fullSubcategoryInclusion 𝒴 Q hy.2.choose =
      fullSubcategoryInclusion 𝒳 P hx.2.choose ≫ f
```

## Tag 0DTI, a lemma

[Tag 0DTI](https://stacks.math.columbia.edu/tag/0DTI) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalenceOver_residualGerbeMap_of_hasSelfProductEquivalenceAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeIsomorphism.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeIsomorphism.lean#L352).

> **Stacks 0DTI.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S`, let `x` be a
> point of `|𝒳|` and let the object properties `P` of `𝒳` and `Q` of `𝒴` be residual gerbes of `𝒳`
> at `x` and of `𝒴` at the image of `x`, in the sense of the specification
> `AlgebraicGeometry.Stack.IsResidualGerbeAt` of **Stacks 06MT**. If there is a 1-morphism from the
> algebraic stack of the spectrum of a field to `𝒳` in the equivalence class of `x` whose
> self-product comparison over `𝒳` and over `𝒴` is an equivalence, then the 1-morphism
> `𝒵_x ⟶ 𝒵_y` induced by `f` --- the **Stacks 0DTH** map
> `AlgebraicGeometry.Stack.residualGerbeMap` --- is an isomorphism: an equivalence over the big
> fppf site of `S`.
>
> The proof is the source's. Full faithfulness of `𝒵_x ⟶ 𝒳 ⟶ 𝒴`, the source's first two
> paragraphs, is `AlgebraicGeometry.Stack.full_and_faithful_comp_of_hasSelfProductEquivalenceAt`.
> The concluding sentence is taken through **Stacks 06MQ**: the **Stacks 0DTH** square commutes on
> the nose, so cancelling the faithful inclusion `𝒵_y ⟶ 𝒴` makes `𝒵_x ⟶ 𝒵_y` fully faithful, hence
> a monomorphism by the implication (2) ⟹ (1) of **Stacks 04ZZ** once it is known representable by
> algebraic spaces. The residual gerbe `𝒵_y` is reduced, locally Noetherian and one-point by its
> specification, so it is covered by the spectrum of a field by the implication (1) ⟹ (2) of
> **Stacks 06MP**, and `|𝒵_x|` is nonempty by its own specification, which rules out the empty
> alternative of Stacks 06MQ.
>
> The representability of `𝒵_x ⟶ 𝒵_y`, and of the inclusion `𝒵_y ⟶ 𝒴` behind the Stacks 0DTH map,
> is what the source takes from Stacks 04Y5; the library has the implication (2) ⟹ (3) of
> Stacks 04Y5 from the bootstrap theorem Stacks 04S6 part (3).

```lean
theorem isEquivalenceOver_residualGerbeMap_of_hasSelfProductEquivalenceAt
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (x : AlgebraicStacks.points B S hS 𝒳)
    (P : ObjectProperty 𝒳.val.val.obj) (Q : ObjectProperty 𝒴.val.val.obj)
    (hx : IsResidualGerbeAt B S hS 𝒳 x P)
    (hy : IsResidualGerbeAt B S hS 𝒴 (AlgebraicStacks.pointsMap B S hS f x) Q)
    (hself : HasSelfProductEquivalenceAt B S hS f x) :
    Nonempty (Functor.IsEquivalenceOver
      (fullSubcategoryAlgebraicStack 𝒳 P hx.2.choose).val.val.p
      (fullSubcategoryAlgebraicStack 𝒴 Q hy.2.choose).val.val.p
      (CatFiberedInGroupoids.homFunctor
        (residualGerbeMap B S hS f hx.2.choose hy.2.choose
          (map_mem_of_isResidualGerbeAt B S hS f x _ rfl hx hy)).hom))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.11, Tag 06ML](https://stacks.math.columbia.edu/tag/06ML)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
