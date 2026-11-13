---
declaration: section
origin: cited
lean: AlgebraicGeometry.isQuasiProjective_tfae_of_exists_isAmple, AlgebraicGeometry.QuasiProjectiveSchemesOver.baseChange, AlgebraicGeometry.isQuasiProjective_comp_of_exists_isAmple, AlgebraicGeometry.isQuasiProjective_pullback_snd_comp, AlgebraicGeometry.quasiProjectiveOver_isClosedUnderBinaryProducts, AlgebraicGeometry.isQuasiProjective_of_isQuasiAffineHom, AlgebraicGeometry.isQuasiProjective_of_locallyQuasiFinite_of_isSeparated, AlgebraicGeometry.isQuasiProjective_of_isImmersion
statement: formalized
proof: formalized
---

# 37.49 Quasi-projective schemes

Section 37.49 of the Stacks Project, [Tag 0B41](https://stacks.math.columbia.edu/tag/0B41). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B42, a lemma

[Tag 0B42](https://stacks.math.columbia.edu/tag/0B42) in the Stacks Project.

**`AlgebraicGeometry.isQuasiProjective_tfae_of_exists_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveOverAmpleBase.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveOverAmpleBase.lean#L238). The attribute's comment: “all five conditions, with no hypothesis”.

> **Stacks Project, Tag 0B42.** Let `S` be a scheme carrying an ample invertible module and let
> `f : X ⟶ S` be a morphism of schemes. The following are equivalent:
>
> 1. `f` is quasi-projective;
> 2. `f` is H-quasi-projective;
> 3. `X` is a quasi-compact open subscheme, over `S`, of a scheme projective over `S`;
> 4. `f` is of finite type and `X` carries an ample invertible module;
> 5. `f` is of finite type and carries an `f`-very ample invertible module.
>
> The cycle is (1) ⟹ (4) ⟹ (2) ⟹ (1), with (2) ⟹ (3), (3) ⟹ (5) and (5) ⟹ (1) closing the
> remaining conditions. Nothing is assumed.

```lean
theorem isQuasiProjective_tfae_of_exists_isAmple (f : X ⟶ S)
    (hS : ∃ (M : S.Modules) (hM : Stacks.Ample.IsInvertibleModule S M),
      letI : Stacks.Ample.IsInvertibleModule S M := hM
      Stacks.Ample.IsAmple S M) :
    List.TFAE
      [IsQuasiProjective f,
        IsHQuasiProjective f,
        ∃ (X' : Scheme.{u}) (p : X' ⟶ S) (j : X ⟶ X'),
          IsOpenImmersion j ∧ QuasiCompact j ∧ j ≫ p = f ∧ IsProjective p,
        (LocallyOfFiniteType f ∧ QuasiCompact f) ∧
          ∃ (L : X.Modules) (hL : Stacks.Ample.IsInvertibleModule X L),
            letI : Stacks.Ample.IsInvertibleModule X L := hL
            Stacks.Ample.IsAmple X L,
        (LocallyOfFiniteType f ∧ QuasiCompact f) ∧
          ∃ (L : X.Modules) (hL : Stacks.Ample.IsInvertibleModule X L),
            letI : Stacks.Ample.IsInvertibleModule X L := hL
            Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple f L]
```

## Tag 0B43, a lemma

[Tag 0B43](https://stacks.math.columbia.edu/tag/0B43) in the Stacks Project.

**`AlgebraicGeometry.QuasiProjectiveSchemesOver.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L234). The attribute's comment: “part (1), base change; the source's hypothesis that `S'` has an ample invertible sheaf is not needed, Tag 0B3G needing no such hypothesis”. References: EGA II (5.3.4).

> **Stacks Project, Tag 0B43, clause (1).** For a morphism of bases `g : S' ⟶ S`, base change
> along `g` is a functor `QP_S ⥤ QP_{S'}`: the fibre product `X ×_S S'` of a scheme `X`
> quasi-projective over `S` is quasi-projective over `S'`.
>
> The object part is [Stacks, Tag 0B3G], `AlgebraicGeometry.IsQuasiProjective.of_isPullback`,
> applied to the fibre-product square. That result is unconditional, so the hypothesis of the
> source that `S'` carries an ample invertible sheaf is not needed and is not assumed.

```lean
def QuasiProjectiveSchemesOver.baseChange {S S' : Scheme.{u}} (g : S' ⟶ S) :
    QuasiProjectiveSchemesOver S ⥤ QuasiProjectiveSchemesOver S'
```

**`AlgebraicGeometry.isQuasiProjective_comp_of_exists_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L250). The attribute's comment: “part (2), composition”.

> **Stacks Project, Tag 0B43, clause (2).** Let `S` carry an ample invertible sheaf. If
> `X ∈ QP_S` and `Y ∈ QP_X`, then `Y ∈ QP_S`: for `f : Y ⟶ X` and `g : X ⟶ S` quasi-projective,
> `f ≫ g` is quasi-projective.
>
> The source reads this off condition (4) of [Stacks, Tag 0B42]. It is taken here from
> [Stacks, Tag 0C4M], `AlgebraicGeometry.IsQuasiProjective.comp`, which is already proved over a
> quasi-compact base; the ample invertible sheaf on `S` supplies that quasi-compactness and nothing
> else is used.

```lean
theorem isQuasiProjective_comp_of_exists_isAmple {X Y S : Scheme.{u}} (f : Y ⟶ X) (g : X ⟶ S)
    (hS : ∃ (M : S.Modules) (hM : Stacks.Ample.IsInvertibleModule S M),
      letI : Stacks.Ample.IsInvertibleModule S M := hM
      Stacks.Ample.IsAmple S M)
    (hf : IsQuasiProjective f) (hg : IsQuasiProjective g) : IsQuasiProjective (f ≫ g)
```

**`AlgebraicGeometry.isQuasiProjective_pullback_snd_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L267). The attribute's comment: “part (3), fibre products”.

> **Stacks Project, Tag 0B43, clause (3). `QP_S` is closed under fibre products over `S`.** For
> `f : X ⟶ S` and `g : Y ⟶ S` quasi-projective and `S` carrying an ample invertible sheaf, the
> structure morphism `X ×_S Y ⟶ S` is quasi-projective.
>
> This is the source's proof: the projection `X ×_S Y ⟶ Y` is a base change of `f`, hence
> quasi-projective by clause (1), and clause (2) composes it with `g`.

```lean
theorem isQuasiProjective_pullback_snd_comp {X Y S : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S)
    (hS : ∃ (M : S.Modules) (hM : Stacks.Ample.IsInvertibleModule S M),
      letI : Stacks.Ample.IsInvertibleModule S M := hM
      Stacks.Ample.IsAmple S M)
    (hf : IsQuasiProjective f) (hg : IsQuasiProjective g) :
    IsQuasiProjective (pullback.snd f g ≫ g)
```

**`AlgebraicGeometry.quasiProjectiveOver_isClosedUnderBinaryProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L306). The attribute's comment: “part (3), fibre products, as closure of the category under binary products”. References: EGA II (5.3.4), “(iv)”.

> **Stacks Project, Tag 0B43, clause (3), as a closure property of the category `QP_S`.** For
> `S` carrying an ample invertible sheaf, the full subcategory of schemes quasi-projective over `S`
> is closed under binary products in the category of schemes over `S` — that is, under fibre
> products over `S`.
>
> A binary product in `Over S` is a fibre product of the sources over `S`, by
> `AlgebraicGeometry.isLimitOverBinaryFan`, so this is
> `AlgebraicGeometry.isQuasiProjective_pullback_snd_comp` transported along the comparison
> isomorphism.

```lean
theorem quasiProjectiveOver_isClosedUnderBinaryProducts (S : Scheme.{u})
    (hS : ∃ (M : S.Modules) (hM : Stacks.Ample.IsInvertibleModule S M),
      letI : Stacks.Ample.IsInvertibleModule S M := hM
      Stacks.Ample.IsAmple S M) :
    (quasiProjectiveOver S).IsClosedUnderBinaryProducts
```

**`AlgebraicGeometry.isQuasiProjective_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L335). The attribute's comment: “part (6), quasi-affine of finite type; no hypothesis on the base is used”.

> **Stacks Project, Tag 0B43, clause (6).** If `f : X ⟶ S` is quasi-affine of finite type then
> `X ∈ QP_S`.
>
> This is Morphisms [Stacks, Tag 0B3H],
> `Stacks.HProjective.isQuasiProjective_of_isQuasiAffineHom`: the structure sheaf `𝒪_X` is ample
> relative to a quasi-affine morphism. It needs no hypothesis on the base. Finite type is the
> conjunction of local finite type and quasi-compactness as in [Stacks, Tag 01T1], and
> quasi-compactness already follows from quasi-affineness, so only the local finite type half
> appears.

```lean
theorem isQuasiProjective_of_isQuasiAffineHom {X S : Scheme.{u}} (f : X ⟶ S)
    [IsQuasiAffineHom f] (hf : LocallyOfFiniteType f) : IsQuasiProjective f
```

**`AlgebraicGeometry.isQuasiProjective_of_locallyQuasiFinite_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L351). The attribute's comment: “part (7), quasi-finite and separated; no hypothesis on the base is used”. References: EGA III (4.4.12), “more general”.

> **Stacks Project, Tag 0B43, clause (7).** If `f : X ⟶ S` is quasi-finite and separated then
> `X ∈ QP_S`.
>
> This is the source's proof: a quasi-finite separated morphism is quasi-affine by
> [Stacks, Tag 02LR], `AlgebraicGeometry.isQuasiAffineHom_of_locallyQuasiFinite`, and clause (6)
> applies. Quasi-finiteness is local quasi-finiteness together with finite type, as in
> [Stacks, Tag 02NG]. No hypothesis on the base is used.

```lean
theorem isQuasiProjective_of_locallyQuasiFinite_of_isSeparated {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [LocallyQuasiFinite f] [LocallyOfFiniteType f] [QuasiCompact f] :
    IsQuasiProjective f
```

**`AlgebraicGeometry.isQuasiProjective_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveCategoryClosure.lean#L367). The attribute's comment: “part (8), quasi-compact immersion; no hypothesis on the base is used”.

> **Stacks Project, Tag 0B43, clause (8).** If `f : X ⟶ S` is a quasi-compact immersion then
> `X ∈ QP_S`.
>
> The source goes through clause (7) and Morphisms [Stacks, Tag 01TN], an immersion being locally
> quasi-finite; here that tag is Mathlib's `LocallyQuasiFinite` instance for an immersion, and an
> immersion is locally of finite type as well, so clause (7) applies directly. No hypothesis on the
> base is used.

```lean
theorem isQuasiProjective_of_isImmersion {X S : Scheme.{u}} (f : X ⟶ S) [IsImmersion f]
    [QuasiCompact f] : IsQuasiProjective f
```

**`AlgebraicGeometry.isQuasiProjective_sigmaDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveDisjointUnion.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveDisjointUnion.lean#L230). The attribute's comment: “part (4), finite disjoint unions; proved through clause (6) and clause (2) over the base `∐ S` rather than through the ampleness of a glued module on a disjoint union, which the source asserts with details omitted”.

> Let `S` carry an ample invertible sheaf. If `f i : Z i ⟶ S` is quasi-projective for every
> member of a finite family, then the structure morphism `∐ Z ⟶ S` of the disjoint union is
> quasi-projective.

```lean
theorem isQuasiProjective_sigmaDesc (f : ∀ i, Z i ⟶ S)
    (hS : ∃ (M : S.Modules) (hM : Stacks.Ample.IsInvertibleModule S M),
      letI : Stacks.Ample.IsInvertibleModule S M := hM
      Stacks.Ample.IsAmple S M)
    (hf : ∀ i, IsQuasiProjective (f i)) : IsQuasiProjective (Sigma.desc f)
```

**`AlgebraicGeometry.quasiProjectiveOver_prop_of_isColimit_cofan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveDisjointUnion.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Projective/QuasiProjectiveDisjointUnion.lean#L268). The attribute's comment: “part (4), finite disjoint unions, as closure of the category under finite coproducts”. References: EGA II (5.3.6), “special case”.

> For `S` carrying an ample invertible sheaf, the full subcategory of schemes quasi-projective
> over `S` is closed under finite coproducts in the category of schemes over `S`.

```lean
theorem quasiProjectiveOver_prop_of_isColimit_cofan (S : Scheme.{u})
    (hS : ∃ (M : S.Modules) (hM : Stacks.Ample.IsInvertibleModule S M),
      letI : Stacks.Ample.IsInvertibleModule S M := hM
      Stacks.Ample.IsAmple S M)
    {ι : Type u} [Finite ι] {X : ι → Over S} (hX : ∀ i, quasiProjectiveOver S (X i))
    (c : Cofan X) (hc : IsColimit c) : quasiProjectiveOver S c.pt
```

**`AlgebraicGeometry.IsProjective.isQuasiProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveBundleProperFiniteType/Basic.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveBundleProperFiniteType/Basic.lean#L219). The attribute's comment: “part (5), a projective morphism is in `QP_S`; the source's hypothesis that `S` has an ample invertible sheaf is not needed, Tag 07RL needing no such hypothesis”.

> **Stacks Project, Tag 07RL. A projective morphism is quasi-projective.** Properness supplies
> the finite-type half, and the `f`-very ample module of
> `AlgebraicGeometry.IsProjective.exists_isRelativelyVeryAmple` is `f`-ample by [Stacks, Tag 01VN],
> `f` being quasi-compact. No hypothesis on the base is used, which is how the source states the
> tag.
>
> It is also **clause (5) of [Stacks, Tag 0B43]**, which the source proves by citing Tag 07RL:
> membership of `X` in the category `QP_S` of that tag is
> `AlgebraicGeometry.IsQuasiProjective X.hom`, so "if `X ⟶ S` is projective then `X ∈ QP_S`" is
> this statement. Tag 0B43's hypothesis that `S` carries an ample invertible sheaf is not needed
> for it and is not assumed.

```lean
theorem IsProjective.isQuasiProjective {f : X ⟶ S} (hf : IsProjective f) :
    IsQuasiProjective f
```

## Tag 0EJY, a lemma

[Tag 0EJY](https://stacks.math.columbia.edu/tag/0EJY) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.IsQuasiAffine.of_isAffineHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IsQuasiAffine.of_isAffineHom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L54) (StacksFrontier): “U is quasi-affine (stated for affine f; integral morphisms are affine)”. References: EGA II (5.1.10), “(ii), special case”.
- [`AlgebraicGeometry.Scheme.isPullback_toSpecΓ_toSpecΓ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.isPullback_toSpecΓ_toSpecΓ#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch37.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch37.lean#L56) (StacksFrontier): “the square U → Spec Γ(U), X → Spec Γ(X) is cartesian (stated for affine f)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.49, Tag 0B41](https://stacks.math.columbia.edu/tag/0B41)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
