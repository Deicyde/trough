---
declaration: section
origin: cited
lean: Stacks.AffineFromFiniteSurjective.isAffine_of_finite_surjective, Stacks.AffineFromUniversallyClosed.isAffine_of_surjective_universallyClosed, Stacks.AffineClosedUnion.isAffine_of_isClosedImmersion_iUnion_of_surjective_appTop, Stacks.AffineClosedUnion.isAffine_of_surjective_sigmaDesc_of_surjective_appTop, Stacks.AffineClosedUnion.isAffine_of_isClosedImmersion_iUnion_unconditional, Stacks.AffineClosedUnion.isAffine_of_surjective_sigmaDesc_unconditional, Stacks.AmpleThickeningAscent.isAmple_modulePullback_iff, Stacks.AmpleThickeningLimit.isAmple_modulePullback
statement: formalized
proof: formalized
---

# 32.11 Characterizing affine schemes

Section 32.11 of the Stacks Project, [Tag 01ZS](https://stacks.math.columbia.edu/tag/01ZS). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01ZT, a lemma

[Tag 01ZT](https://stacks.math.columbia.edu/tag/01ZT) in the Stacks Project.

**`Stacks.AffineFromFiniteSurjective.isAffine_of_finite_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/AffineFromFiniteSurjective.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineFromFiniteSurjective.lean#L133).

> The target of a finite surjective morphism of schemes is affine when
> its source is affine.

```lean
theorem isAffine_of_finite_surjective {X S : Scheme.{u}} (f : X ⟶ S)
    [IsFinite f] [Surjective f] [IsAffine X] : IsAffine S
```

## Tag 05YU, a proposition

[Tag 05YU](https://stacks.math.columbia.edu/tag/05YU) in the Stacks Project.

**`Stacks.AffineFromUniversallyClosed.isAffine_of_surjective_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/AffineFromSurjectiveUniversallyClosed.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineFromSurjectiveUniversallyClosed.lean#L220).

> **[Stacks, Tag 05YU].** A scheme admitting a surjective universally closed morphism from an
> affine scheme is affine.
>
> By the reduction above the morphism is integral over a separated, quasi-compact and
> quasi-separated base, so `f_* 𝒪_X` is an integral quasi-coherent sheaf of `𝒪_S`-algebras.  Part
> (1) of [Stacks, Tag 0817] presents it as a directed colimit of finite quasi-coherent
> subalgebras, indexed in the universe of the scheme, and the relative spectrum turns that colimit
> into an inverse system of schemes finite over `S` whose limit is `X`.  One stage of that system
> is affine by [Stacks, Tag 01Z6], and is surjective over `S` because `f` factors through it, so
> [Stacks, Tag 01ZT] applies to it.

```lean
theorem isAffine_of_surjective_universallyClosed [IsAffine X] [Surjective f]
    [UniversallyClosed f] : IsAffine S
```

## Tag 09NL, a lemma

[Tag 09NL](https://stacks.math.columbia.edu/tag/09NL) in the Stacks Project.

**`Stacks.AffineClosedUnion.isAffine_of_isClosedImmersion_iUnion_of_surjective_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Reduction.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Reduction.lean#L131).

> **[Stacks, Tag 09NL], granted that global functions lift to the ambient scheme.** A scheme
> which is set theoretically the union of finitely many affine closed subschemes is affine,
> provided every global function on its reduced induced closed subscheme is the restriction of a
> global function on it.
>
> The hypothesis `hlift` is the only thing assumed, it concerns the single morphism
> `X.nilradical.subschemeι`, and it is the cohomological content of [Stacks, Tag 06AD] for that
> thickening: see the module docstring. Everything else — that the reduced induced closed
> subscheme is affine — is
> `Stacks.AffineClosedUnion.isAffine_nilradical_subscheme_of_isClosedImmersion_iUnion`.

```lean
theorem isAffine_of_isClosedImmersion_iUnion_of_surjective_appTop {ι : Type*} [Finite ι]
    {Z : ι → Scheme.{u}} (f : ∀ i, Z i ⟶ X) [∀ i, IsClosedImmersion (f i)]
    [∀ i, IsAffine (Z i)] (hcov : ⋃ i, Set.range (f i).base = Set.univ)
    (hlift : Function.Surjective X.nilradical.subschemeι.appTop.hom) : IsAffine X
```

**`Stacks.AffineClosedUnion.isAffine_of_surjective_sigmaDesc_of_surjective_appTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Reduction.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Reduction.lean#L147).

> **[Stacks, Tag 09NL] in the tag's own vocabulary, granted that global functions lift to the
> ambient scheme.** The covering hypothesis is surjectivity of the morphism from the coproduct, as
> in the tag; it is the same hypothesis by
> `Stacks.AffineClosedUnion.surjective_sigmaDesc_iff`.
>
> The hypothesis `hlift` is as in
> `Stacks.AffineClosedUnion.isAffine_of_isClosedImmersion_iUnion_of_surjective_appTop`.

```lean
theorem isAffine_of_surjective_sigmaDesc_of_surjective_appTop {ι : Type v} [Finite ι]
    {Z : ι → Scheme.{u}} (f : ∀ i, Z i ⟶ X) [∀ i, IsAffine (Z i)]
    [∀ i, IsClosedImmersion (f i)] [hsurj : Surjective (Sigma.desc f)]
    (hlift : Function.Surjective X.nilradical.subschemeι.appTop.hom) : IsAffine X
```

**`Stacks.AffineClosedUnion.isAffine_of_isClosedImmersion_iUnion_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Unconditional.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Unconditional.lean#L61).

> **[Stacks, Tag 09NL].** A scheme which is set theoretically the union of finitely many
> affine closed subschemes is affine. Nothing is assumed about the ambient scheme.
>
> Its reduced induced closed subscheme is affine by
> `Stacks.AffineClosedUnion.isAffine_nilradical_subscheme_of_isClosedImmersion_iUnion`, and `X` is
> a thickening of that subscheme by
> `Stacks.AffineClosedUnion.isThickening_subschemeι_nilradical`, so [Stacks, Tag 06AD] in the form
> `Stacks.Thickenings.isAffine_of_isThickening` gives affineness of `X` itself.

```lean
theorem isAffine_of_isClosedImmersion_iUnion_unconditional {ι : Type*} [Finite ι]
    {Z : ι → Scheme.{u}} (f : ∀ i, Z i ⟶ X) [∀ i, IsClosedImmersion (f i)]
    [∀ i, IsAffine (Z i)] (hcov : ⋃ i, Set.range (f i).base = Set.univ) : IsAffine X
```

**`Stacks.AffineClosedUnion.isAffine_of_surjective_sigmaDesc_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Unconditional.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineClosedUnion/Unconditional.lean#L72).

> **[Stacks, Tag 09NL] in the tag's own vocabulary.** The covering is surjectivity of the
> morphism from the coproduct of the affine closed subschemes, as the tag states it; it is the
> same hypothesis as a union of ranges by
> `Stacks.AffineClosedUnion.surjective_sigmaDesc_iff`.

```lean
theorem isAffine_of_surjective_sigmaDesc_unconditional {ι : Type v} [Finite ι]
    {Z : ι → Scheme.{u}} (f : ∀ i, Z i ⟶ X) [∀ i, IsAffine (Z i)]
    [∀ i, IsClosedImmersion (f i)] [hsurj : Surjective (Sigma.desc f)] : IsAffine X
```

## Tag 09MW, a lemma

[Tag 09MW](https://stacks.math.columbia.edu/tag/09MW) in the Stacks Project.

**`Stacks.AmpleThickeningAscent.isAmple_modulePullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleThickeningAscent/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleThickeningAscent/Basic.lean#L66).

> **[Stacks, Tag 09MW].** Let `i : Z ⟶ X` be a closed immersion of schemes inducing a
> homeomorphism of underlying topological spaces, and `𝓛` an invertible `𝒪_X`-module. Then `i^* 𝓛`
> is ample on `Z` if and only if `𝓛` is ample on `X`. No Noetherian hypothesis.
>
> The implication `𝓛` ample `⟹` `i^* 𝓛` ample is
> `Stacks.AmpleThickeningLimit.isAmple_modulePullback`; the converse is
> `Stacks.AmpleThickeningAscent.isAmple_of_isAmple_pullback_of_isThickening`.

```lean
theorem isAmple_modulePullback_iff {Z X : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i]
    (hi : IsHomeomorph i.base) (L : X.Modules) [IsInvertibleModule X L] :
    IsAmple Z ((modulePullback i.toLRSHom.toShHom).obj L) ↔ IsAmple X L
```

**`Stacks.AmpleThickeningLimit.isAmple_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleThickeningLimit/Basic.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleThickeningLimit/Basic.lean#L121). The attribute's comment: “the implication `L` ample ⟹ `i^* L` ample”.

> **The implication `L` ample `⟹` `i^* L` ample of [Stacks, Tag 09MW].** For a closed immersion
> `i : Z ⟶ X` inducing a homeomorphism of underlying spaces and an invertible `𝒪_X`-module `L`,
> ampleness of `L` gives ampleness of `i^* L`. No Noetherian hypothesis.
>
> The homeomorphism hypothesis is **not used** — hence its binder is named `_hi`: the proof needs
> only that `i` is an affine morphism. It is carried so that this is literally one half of the
> source statement rather than a
> more general lemma wearing the tag of [Stacks, Tag 09MW]. Neither is this half of the source any
> harder than part (2) of [Stacks, Tag 0892] for a quasi-affine morphism, which
> `Stacks.SectionRatioNoAmple.isAmple_modulePullback_of_isQuasiAffineHom` proves with no premise; a
> closed immersion is affine, and an affine morphism is quasi-affine because the inverse image of an
> affine open is affine.
>
> This is `Stacks.AmpleSurjectiveThickening.isAmple_modulePullback` — the same half of
> [Stacks, Tag 09MS] — with its `[Surjective i]` and `[IsNoetherian X]` hypotheses dropped, which is
> exactly the difference between the two tags on this side of the biconditional.

```lean
theorem isAmple_modulePullback [IsClosedImmersion i] (_hi : IsHomeomorph i.base)
    (hL : IsAmple X L) :
    IsAmple Z ((modulePullback i.toLRSHom.toShHom).obj L)
```

**`Stacks.AmpleThickeningLimit.isAmple_modulePullback_iff_of_isHomeomorph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleThickeningLimit/Unconditional.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleThickeningLimit/Unconditional.lean#L213).

> **[Stacks, Tag 09MW].** Let `i : Z ⟶ X` be a closed immersion of schemes inducing a
> homeomorphism of underlying topological spaces, and let `L` be an invertible `𝒪_X`-module. Then
> `i^* L` is ample on `Z` if and only if `L` is ample on `X`.
>
> No hypothesis beyond the source's: neither Noetherianness nor separatedness nor
> quasi-compactness of either scheme is assumed. The `mpr` half is
> `Stacks.AmpleThickeningLimit.isAmple_modulePullback`; the `mp` half is
> `Stacks.AmpleThickeningLimit.isAmple_of_isAmple_modulePullback_of_isHomeomorph`.

```lean
theorem isAmple_modulePullback_iff_of_isHomeomorph [IsClosedImmersion i]
    (hi : IsHomeomorph i.base) :
    IsAmple Z ((modulePullback i.toLRSHom.toShHom).obj L) ↔ IsAmple X L
```

## Tag 0B7L, a lemma

[Tag 0B7L](https://stacks.math.columbia.edu/tag/0B7L) in the Stacks Project.

**`Stacks.Thickenings.isQuasiAffine_of_isQuasiAffine_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Affine.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Affine.lean#L292). The attribute's comment: “the implication: ambient quasi-affine ⟹ closed subscheme quasi-affine”.

> **The implication *ambient quasi-affine `⟹` closed subscheme quasi-affine* of
> [Stacks Project, Tag 0B7L].** If the ambient scheme of a thickening `i : X ⟶ X'` is quasi-affine,
> then so is the closed subscheme.
>
> This is the implication the source calls elementary, and it is: a closed immersion is an affine
> morphism, and `AlgebraicGeometry.Scheme.IsQuasiAffine.of_isAffineHom` says the source of an affine
> morphism into a quasi-affine scheme is quasi-affine. Surjectivity of `i` is not used; it is
> carried because it is half of the source's hypothesis, so that this is literally one implication
> of the source statement.
>
> The source's hypothesis that `i` is a closed immersion inducing a homeomorphism of underlying
> spaces is `Stacks.Thickenings.IsThickening`: for a closed immersion, being a homeomorphism on
> points is being surjective, which is
> `Stacks.Thickenings.IsThickening.isHomeomorph`.
>
> The reverse implication is the one part (9) of [Stacks Project, Tag 09ZV] needs. It is isolated as
> `Stacks.Thickenings.QuasiAffineAscendsAlongThickening`, and it is proved for every **finite-order**
> thickening in
> `StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineAscent.lean`
> (`Stacks.Thickenings.isQuasiAffine_of_isFiniteOrderThickening`), hence for every thickening of a
> locally Noetherian scheme, and for an arbitrary thickening in
> `Stacks.Thickenings.isQuasiAffine_of_isThickening` of
> `StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineLimit.lean`.

```lean
theorem isQuasiAffine_of_isQuasiAffine_ambient {X X' : Scheme.{u}} {i : X ⟶ X'}
    (hi : IsThickening i) (hX' : Scheme.IsQuasiAffine X') : Scheme.IsQuasiAffine X
```

**`Stacks.Thickenings.isQuasiAffine_iff_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineLimit.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineLimit.lean#L315).

> **[Stacks Project, Tag 0B7L].** For a closed immersion inducing a homeomorphism of underlying
> spaces — equivalently, a surjective closed immersion — the ambient scheme is quasi-affine if and
> only if the closed subscheme is. No Noetherian hypothesis.
>
> *Ambient `⟹` closed subscheme* is the elementary implication, a closed immersion being affine
> (`Stacks.Thickenings.isQuasiAffine_of_isQuasiAffine_ambient`); *closed subscheme `⟹` ambient* is
> `Stacks.Thickenings.isQuasiAffine_of_isThickening`. This supersedes the Noetherian
> `Stacks.Thickenings.isQuasiAffine_iff_of_isNoetherian`, which is
> [Stacks Project, Tag 0B7K].

```lean
theorem isQuasiAffine_iff_of_isThickening {Y Y' : Scheme.{u}} {k : Y ⟶ Y'}
    (hk : IsThickening k) : Scheme.IsQuasiAffine Y' ↔ Scheme.IsQuasiAffine Y
```

## Tag 0E21, a lemma

[Tag 0E21](https://stacks.math.columbia.edu/tag/0E21) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.exists_affine_nonvanishingOpen_factorsThrough`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/CommonStage.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/CommonStage.lean#L285).

> **[Stacks, Tag 0E21].**
>
> Let `L` be an ample invertible sheaf on a scheme `X`, let `W ⊆ X` be open and let
> `Spec A ⟶ W` be a family of points of `W` parametrised by an integral algebra `A` over a field
> `k`. Then there is an `n > 0` and a global section `s` of `L ^ ⊗ n` whose nonvanishing open `X_s`
> is affine, is contained in `W`, and is such that `Spec A ⟶ W` factors through `X_s`.
>
> This is `exists_affine_nonvanishingOpen_factorsThrough_of_isOneAffineOpenStep` with its one
> remaining hypothesis discharged by
> `AlgebraicGeometry.Scheme.FiniteTypeApproximation.isOneAffineOpenStep`, the single-affine step of
> Noetherian approximation relative to a quasi-compact open ([Stacks, Tag 07RN]).

```lean
theorem exists_affine_nonvanishingOpen_factorsThrough
    (k : Type v) (A : Type u) [Field k] [CommRing A] [Algebra k A] [Algebra.IsIntegral k A]
    (X : Scheme.{u}) (L : X.Modules)
    [hLinv : AlgebraicGeometry.SheafOfModules.IsInvertible X.toRingedSpace.presheaf
      (structureSheafRing X.toRingedSpace).property L]
    (hL : IsAmple X L)
    (W : X.Opens) (f : Spec (CommRingCat.of A) ⟶ (W : Scheme.{u})) :
    ∃ n : ℕ, 0 < n ∧
      ∃ s : (tensorPower X.toRingedSpace.presheaf
        (structureSheafRing X.toRingedSpace).property L (n : ℤ)).sections,
      ∃ U : X.Opens,
        U = nonvanishingOpen
          (tensorPower X.toRingedSpace.presheaf
            (structureSheafRing X.toRingedSpace).property L (n : ℤ)) s ∧
        IsAffineOpen U ∧ U ≤ W ∧
        ∃ g : Spec (CommRingCat.of A) ⟶ (U : Scheme.{u}), g ≫ U.ι = f ≫ W.ι
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.11, Tag 01ZS](https://stacks.math.columbia.edu/tag/01ZS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
