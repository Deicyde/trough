---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.finite_residueFieldHom_genericPoint_of_hasTranscendenceDegreeAt_zero, AlgebraicGeometry.Space.isQuasiFiniteAt_iff_forall_eq_of_pointsMap_eq, AlgebraicGeometry.Space.hasTranscendenceDegreeAt_zero_of_isQuasiFiniteAt, AlgebraicGeometry.Space.tfae_hasTranscendenceDegreeAt_eq_zero_and_isFiniteOverAffineOpen, AlgebraicGeometry.Space.degree, AlgebraicGeometry.Space.degree_pos, AlgebraicGeometry.Space.degree_comp
statement: formalized
proof: formalized
---

# 72.5 Morphisms between integral algebraic spaces

Section 72.5 of the Stacks Project, [Tag 0ENG](https://stacks.math.columbia.edu/tag/0ENG). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AD5, a lemma

[Tag 0AD5](https://stacks.math.columbia.edu/tag/0AD5) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_residueFieldHom_genericPoint_of_hasTranscendenceDegreeAt_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/EqualDeltaDimension.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/EqualDeltaDimension.lean#L486). The attribute's comment: “condition (1) implies condition (2): finiteness of the residue field extension at the generic point, from vanishing of the relative transcendence degree there”.

> **Spaces over Fields, Lemma 0AD5, (1) implies (2).** Let `f : X ⟶ Y` be a dominant
> morphism of integral algebraic spaces over `S` which is locally of finite type. If the
> transcendence degree of the generic point of `X` over the generic point of `Y` is zero, then
> the induced extension of residue fields at the generic point is finite.
>
> Both residue fields are read on a pair of representable open charts through the generic point,
> which exist by Stacks 086U and Stacks 03IE.

```lean
theorem finite_residueFieldHom_genericPoint_of_hasTranscendenceDegreeAt_zero
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXInt : IsIntegralSpace B S hS X) (hYInt : IsIntegralSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) (hdom : IsDominant B S hS f)
    (htr : HasTranscendenceDegreeAt B S hS f (genericPoint B S hS hX hXInt) 0) :
    letI := (residueFieldHom B S hS X Y hY hXInt.2.1 hYInt.2.1 f
      (genericPoint B S hS hX hXInt)).toAlgebra
    Module.Finite
      (residueField B S hS Y hYInt.2.1
        (pointsMap B S hS X f (genericPoint B S hS hX hXInt)))
      (residueField B S hS X hXInt.2.1 (genericPoint B S hS hX hXInt))
```

**`AlgebraicGeometry.Space.isQuasiFiniteAt_iff_forall_eq_of_pointsMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralGenericallyFinite.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralGenericallyFinite.lean#L109). The attribute's comment: “conditions (4) and (5)”.

> **Stacks 0AD5, conditions (4) and (5).** Let `f : X ⟶ Y` be a dominant morphism locally of
> finite type of algebraic spaces over `S` with `Y` integral, and let `x` and `y` be generic
> points of `|X|` and `|Y|`. Then `f` is quasi-finite at `x` exactly when `x` is the only point
> of `|X|` mapping to `y`.

```lean
theorem isQuasiFiniteAt_iff_forall_eq_of_pointsMap_eq
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hYint : IsIntegralSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hdom : IsDominant B S hS f)
    {x : points B S hS X} (hx : IsGenericPoint x (Set.univ : Set (points B S hS X)))
    {y : points B S hS Y} (hy : IsGenericPoint y (Set.univ : Set (points B S hS Y))) :
    IsQuasiFiniteAt B S hS f x ↔
      ∀ x' : points B S hS X, pointsMap B S hS X f x' = y → x' = x
```

**`AlgebraicGeometry.Space.hasTranscendenceDegreeAt_zero_of_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralGenericallyFinite.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralGenericallyFinite.lean#L167). The attribute's comment: “condition (4) implies condition (1)”.

> **Stacks 0AD5, condition (4) implies condition (1).** A morphism of algebraic spaces over
> `S` which is quasi-finite at a point of its source has transcendence degree zero there: on an
> open subspace containing the point the morphism is locally quasi-finite, so contributes a
> finite residue field extension in every étale chart, and an open immersion does not change the
> transcendence degree (Stacks 06RX).

```lean
theorem hasTranscendenceDegreeAt_zero_of_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    {x : points B S hS X} (h : IsQuasiFiniteAt B S hS f x) :
    HasTranscendenceDegreeAt B S hS f x 0
```

**`AlgebraicGeometry.Space.tfae_hasTranscendenceDegreeAt_eq_zero_and_isFiniteOverAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralGenericallyFiniteTfae.lean, line 958](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralGenericallyFiniteTfae.lean#L958).

> **Stacks 0AD5.** Let `S` be a scheme, let `X` and `Y` be integral algebraic spaces over
> `S`, let `x ∈ |X|` and `y ∈ |Y|` be the generic points, and let `f : X ⟶ Y` be locally of
> finite type and dominant. The following are equivalent:
>
> 1. the transcendence degree of `x/y` is `0`;
> 2. the extension `κ(x)/κ(y)` is finite;
> 3. there exist nonempty affine opens `U ⊂ X` and `V ⊂ Y` such that `f(U) ⊂ V` and
>    `f|_U : U ⟶ V` is finite;
> 4. `f` is quasi-finite at `x`;
> 5. `x` is the only point of `|X|` mapping to `y`.
>
> If `f` is separated or if `f` is quasi-compact, then these are also equivalent to
>
> 6. there exists a nonempty affine open `V ⊂ Y` such that `f^{-1}(V) ⟶ V` is finite.

```lean
theorem tfae_hasTranscendenceDegreeAt_eq_zero_and_isFiniteOverAffineOpen
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXInt : IsIntegralSpace B S hS X) (hYInt : IsIntegralSpace B S hS Y)
    (f : X ⟶ Y) (hlft : IsLocallyOfFiniteType B S hS f) (hdom : IsDominant B S hS f)
    {x : points B S hS X} (hx : IsGenericPoint x (Set.univ : Set (points B S hS X)))
    {y : points B S hS Y} (hy : IsGenericPoint y (Set.univ : Set (points B S hS Y))) :
    List.TFAE
        [HasTranscendenceDegreeAt B S hS f x 0,
          HasFiniteResidueFieldExtensionAt B S hS hY hXInt.2.1 hYInt.2.1 f x,
          ExistsAffineOpenFiniteRestriction B S hS f,
          IsQuasiFiniteAt B S hS f x,
          ∀ x' : points B S hS X, pointsMap B S hS X f x' = y → x' = x] ∧
      ((IsSeparated B S hS f ∨ IsQuasiCompact B S hS f) →
        List.TFAE
          [HasTranscendenceDegreeAt B S hS f x 0,
            HasFiniteResidueFieldExtensionAt B S hS hY hXInt.2.1 hYInt.2.1 f x,
            ExistsAffineOpenFiniteRestriction B S hS f,
            IsQuasiFiniteAt B S hS f x,
            (∀ x' : points B S hS X, pointsMap B S hS X f x' = y → x' = x),
            IsFiniteOverAffineOpen B S hS f])
```

## Tag 0AD6, a definition

[Tag 0AD6](https://stacks.math.columbia.edu/tag/0AD6) in the Stacks Project.

**`AlgebraicGeometry.Space.degree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralDegree.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralDegree.lean#L214). The attribute's comment: “the degree of X over Y”.

> **Stacks 0AD6.** The degree of `X` over `Y` for a morphism `f : X ⟶ Y` of integral
> algebraic spaces over `S`: the degree `[κ(x) : κ(y)]` of the extension of residue fields at
> the generic point `x` of `|X|` and its image `y`.

```lean
noncomputable def degree (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXint : IsIntegralSpace B S hS X) (hYint : IsIntegralSpace B S hS Y) (f : X ⟶ Y) : ℕ
```

**`AlgebraicGeometry.Space.degree_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralDegree.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralDegree.lean#L244). The attribute's comment: “positivity of the degree, under condition (2) of Stacks 0AD5, which this development cannot yet deduce from the other four”.

> **Stacks 0AD6.** The degree of `X` over `Y` is a positive integer once the extension of
> residue fields at the generic point is finite, which is condition (2) of Stacks 0AD5.

```lean
theorem degree_pos (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXint : IsIntegralSpace B S hS X) (hYint : IsIntegralSpace B S hS Y) (f : X ⟶ Y)
    {x : points B S hS X}
    (hx : IsGenericPoint x (Set.univ : Set (points B S hS X)))
    (hfin : HasFiniteResidueFieldExtensionAt B S hS hY hXint.isDecentSpace
      hYint.isDecentSpace f x) :
    0 < degree B S hS hX hY hXint hYint f
```

## Tag 0ENH, a lemma

[Tag 0ENH](https://stacks.math.columbia.edu/tag/0ENH) in the Stacks Project.

**`AlgebraicGeometry.Space.degree_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralDegree.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralDegree.lean#L272). The attribute's comment: “multiplicativity of the degree; local finiteness of type of the two morphisms, finiteness of the two residue field extensions and dominance of g are not needed”.

> **Stacks 0ENH.** For a dominant morphism `f : X ⟶ Y` and a morphism `g : Y ⟶ Z` of
> integral algebraic spaces over `S`, the degree of `X` over `Z` is the degree of `X` over `Y`
> times the degree of `Y` over `Z`.
>
> The generic point of `|X|` maps to the generic point of `|Y|` because `f` is dominant, so all
> three degrees are read off the same tower of residue fields, and degrees multiply in a tower
> of field extensions (Stacks 09G9).

```lean
theorem degree_comp (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (hXint : IsIntegralSpace B S hS X)
    (hYint : IsIntegralSpace B S hS Y) (hZint : IsIntegralSpace B S hS Z) (f : X ⟶ Y)
    (g : Y ⟶ Z) (hf : IsDominant B S hS f) :
    degree B S hS hX hZ hXint hZint (f ≫ g) =
      degree B S hS hX hY hXint hYint f * degree B S hS hY hZ hYint hZint g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.5, Tag 0ENG](https://stacks.math.columbia.edu/tag/0ENG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
