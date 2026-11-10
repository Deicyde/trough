---
declaration: section
origin: cited
lean: Stacks.Thickenings.isAffineHom_left_iff_right, Stacks.Thickenings.isIntegralHom_left_iff_right, Stacks.Thickenings.isQuasiAffineHom_left_iff_right, Stacks.Thickenings.isSeparated_left_iff_right, Stacks.Thickenings.quasiSeparated_left_iff_right, Stacks.Thickenings.quasiCompact_left_iff_right, Stacks.Thickenings.surjective_left_iff_right, Stacks.Thickenings.universallyClosed_left_iff_right
statement: formalized
proof: formalized
---

# 37.3 Morphisms of thickenings

Section 37.3 of the Stacks Project, [Tag 0CF2](https://stacks.math.columbia.edu/tag/0CF2). 4 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09ZV, a lemma

[Tag 09ZV](https://stacks.math.columbia.edu/tag/09ZV) in the Stacks Project.

**`Stacks.Thickenings.isAffineHom_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Affine.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Affine.lean#L218). The attribute's comment: “affine”.

> **Part (1) of [Stacks Project, Tag 09ZV].** For a morphism of thickenings, the morphism of
> closed subschemes is affine if and only if the morphism of ambient schemes is affine.
>
> Affineness of a morphism quantifies over the affine opens of its target, and
> `Stacks.Thickenings.isAffineOpen_iff_isAffineOpen_preimage` matches the affine opens of `S` with
> those of `S'`; the inverse images of matching opens along `φ.left` and `φ.right` are then matched
> by the same criterion for the thickening `i`.

```lean
theorem isAffineHom_left_iff_right {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (hi : IsThickening i) (hj : IsThickening j) (φ : Arrow.mk i ⟶ Arrow.mk j) :
    IsAffineHom φ.left ↔ IsAffineHom φ.right
```

**`Stacks.Thickenings.isIntegralHom_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Affine.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Affine.lean#L239). The attribute's comment: “integral”.

> **Part (5) of [Stacks Project, Tag 09ZV].** For a morphism of thickenings, the morphism of
> closed subschemes is integral if and only if the morphism of ambient schemes is integral.
>
> A morphism is integral exactly when it is universally closed and affine — [Stacks Project, Tag
> 01WM], which is `AlgebraicGeometry.IsIntegralHom.iff_universallyClosed_and_isAffineHom` — so this
> is part (4) of the tag together with part (1).

```lean
theorem isIntegralHom_left_iff_right {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (hi : IsThickening i) (hj : IsThickening j) (φ : Arrow.mk i ⟶ Arrow.mk j) :
    IsIntegralHom φ.left ↔ IsIntegralHom φ.right
```

**`Stacks.Thickenings.isQuasiAffineHom_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineLimit.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/QuasiAffineLimit.lean#L330). The attribute's comment: “quasi_affine”.

> **Part (9) of [Stacks Project, Tag 09ZV].** For a morphism of thickenings — a commutative
> square whose horizontal arrows are thickenings — the morphism of closed subschemes is
> quasi-affine if and only if the morphism of ambient schemes is. No hypothesis on the schemes.
>
> The `mpr` half is `Stacks.Thickenings.isQuasiAffineHom_left_of_right`, which needs nothing; the
> `mp` half is `Stacks.Thickenings.isQuasiAffineHom_right_of_left` fed the absolute statement
> `Stacks.Thickenings.quasiAffineAscendsAlongThickening`.

```lean
theorem isQuasiAffineHom_left_iff_right {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (hi : IsThickening i) (hj : IsThickening j) (φ : Arrow.mk i ⟶ Arrow.mk j) :
    IsQuasiAffineHom φ.left ↔ IsQuasiAffineHom φ.right
```

**`Stacks.Thickenings.isSeparated_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Separated.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Separated.lean#L63). The attribute's comment: “separated”.

> Separatedness is invariant under a morphism of thickenings.

```lean
theorem isSeparated_left_iff_right
    {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (hi : IsThickening i) (hj : IsThickening j)
    (φ : Arrow.mk i ⟶ Arrow.mk j) :
    IsSeparated φ.left ↔ IsSeparated φ.right
```

**`Stacks.Thickenings.quasiSeparated_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Separated.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Separated.lean#L76). The attribute's comment: “quasi_separated”.

> Quasi-separatedness of a morphism of schemes is unchanged by passing between the closed
> subschemes and the ambient schemes of a morphism of thickenings.

```lean
theorem quasiSeparated_left_iff_right {X S : Arrow (Scheme.{u})}
    (φ : X ⟶ S) (hX : IsThickening X.hom)
    (hS : IsThickening S.hom) :
    QuasiSeparated φ.left ↔ QuasiSeparated φ.right
```

**`Stacks.Thickenings.quasiCompact_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L73). The attribute's comment: “quasi_compact”.

> Quasi-compactness is preserved and reflected by a morphism of thickenings.

```lean
theorem quasiCompact_left_iff_right
    {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (φ : Arrow.mk i ⟶ Arrow.mk j)
    (hi : IsThickening i) (hj : IsThickening j) :
    QuasiCompact φ.left ↔ QuasiCompact φ.right
```

**`Stacks.Thickenings.surjective_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L107). The attribute's comment: “surjective”.

> The two vertical maps in a morphism of thickenings are simultaneously surjective.

```lean
theorem surjective_left_iff_right
    {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (hi : IsThickening i) (hj : IsThickening j)
    (f : Arrow.mk i ⟶ Arrow.mk j) :
    Surjective f.left ↔ Surjective f.right
```

**`Stacks.Thickenings.universallyClosed_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L126). The attribute's comment: “universally_closed”.

> Universal closedness is invariant under a morphism of thickenings.

```lean
theorem universallyClosed_left_iff_right {i j : Arrow Scheme.{u}} (φ : i ⟶ j)
    (hi : IsThickening i.hom) (hj : IsThickening j.hom) :
    UniversallyClosed φ.left ↔ UniversallyClosed φ.right
```

**`Stacks.Thickenings.universallyInjective_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L157). The attribute's comment: “universally_injective”.

> Universal injectivity is unchanged when a morphism of thickenings is passed from the
> closed subschemes to the ambient schemes.

```lean
theorem universallyInjective_left_iff_right {X X' S S' : Scheme.{u}}
    {i : X ⟶ X'} {j : S ⟶ S'} (hi : IsThickening i)
    (hj : IsThickening j) (f : Arrow.mk i ⟶ Arrow.mk j) :
    UniversallyInjective f.left ↔ UniversallyInjective f.right
```

**`Stacks.Thickenings.universallyOpen_left_iff_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Topological.lean#L245). The attribute's comment: “universally_open”.

> Universal openness is unchanged when a morphism of schemes is replaced by the
> corresponding morphism of thickenings.

```lean
theorem universallyOpen_left_iff_right
    {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'}
    (hi : IsThickening i) (hj : IsThickening j)
    (f : Arrow.mk i ⟶ Arrow.mk j) :
    UniversallyOpen f.left ↔ UniversallyOpen f.right
```

## Tag 0D2R, a lemma

[Tag 0D2R](https://stacks.math.columbia.edu/tag/0D2R) in the Stacks Project.

**`Stacks.AmpleThickeningAscent.isRelativelyAmple_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleThickeningAscent/Basic.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AmpleThickeningAscent/Basic.lean#L81).

> **[Stacks, Tag 0D2R].** Let `(f, f') : (X ⊆ X') → (S ⊆ S')` be a morphism of thickenings —
> a commutative square `i ≫ f' = f ≫ j` in which `i : X ⟶ X'` and `j : S ⟶ S'` are thickenings —
> and let `𝓛'` be an invertible `𝒪_{X'}`-module, with restriction `𝓛 = i^* 𝓛'` to `X`. Then `𝓛'`
> is `f'`-ample if and only if `𝓛` is `f`-ample.
>
> This is `Stacks.ThickeningInvertible.isRelativelyAmple_iff` with its hypothesis
> `Stacks.ThickeningInvertible.AmpleReflectedByThickening` discharged by
> `Stacks.AmpleThickeningAscent.ampleReflectedByThickening`.

```lean
theorem isRelativelyAmple_iff {X X' S S' : Scheme.{u}} {i : X ⟶ X'} {j : S ⟶ S'} {f : X ⟶ S}
    {f' : X' ⟶ S'} (hi : IsThickening i) (hj : IsThickening j) (hsq : i ≫ f' = f ≫ j)
    (L' : X'.Modules) [IsInvertibleModule X' L'] :
    IsRelativelyAmple f' L' ↔ IsRelativelyAmple f (pullbackModule i L')
```

**`Stacks.ThickeningInvertible.isRelativelyAmple_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ThickeningInvertible/Basic.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ThickeningInvertible/Basic.lean#L342). The attribute's comment: “the implication `ℒ'` is `f'`-ample ⟹ `ℒ` is `f`-ample, nothing carried”.

> **[Stacks, Tag 0D2R], the implication `ℒ'` is `f'`-ample `⟹` `ℒ` is `f`-ample.** For a
> morphism of thickenings `(f, f') : (X ⊆ X') → (S ⊆ S')` and an invertible `𝒪_{X'}`-module `ℒ'`
> with restriction `ℒ = i^* ℒ'` to `X`, relative ampleness of `ℒ'` over `f'` gives relative
> ampleness of `ℒ` over `f`.
>
> **Nothing is carried.** The source checks relative ampleness at every affine open of `S` and
> gets the correspondence with the affine opens of `S'` from [Stacks, Tag 06AD]; here the opens
> `j^{-1}V'`, for `V'` an affine open of `S'`, are an affine open covering of `S` — affine because
> `j` is a closed immersion, covering because `j` is surjective — and that is enough by
> [Stacks, Tag 01VJ]. Over each member the implication is the closed-immersion case of
> [Stacks, Tag 0B3E] applied to `i ∣_ (f'^{-1}V')`.

```lean
theorem isRelativelyAmple_pullback (hi : IsThickening i) (hj : IsThickening j)
    (hsq : i ≫ f' = f ≫ j) (hL' : IsRelativelyAmple f' L') :
    IsRelativelyAmple f (pullbackModule i L')
```

**`Stacks.ThickeningInvertible.isRelativelyAmple_of_isRelativelyAmple_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ThickeningInvertible/Basic.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ThickeningInvertible/Basic.lean#L383). The attribute's comment: “the implication `ℒ` is `f`-ample ⟹ `ℒ'` is `f'`-ample, carrying `href` = [Tag 09MW] mp”.

> **[Stacks, Tag 0D2R], the implication `ℒ` is `f`-ample `⟹` `ℒ'` is `f'`-ample**, granted
> [Stacks, Tag 09MW]. For a morphism of thickenings `(f, f') : (X ⊆ X') → (S ⊆ S')` and an
> invertible `𝒪_{X'}`-module `ℒ'` with restriction `ℒ = i^* ℒ'` to `X`, relative ampleness of `ℒ`
> over `f` gives relative ampleness of `ℒ'` over `f'`.
>
> **One hypothesis is carried**, `href : Stacks.ThickeningInvertible.AmpleReflectedByThickening`,
> which is the implication `k^* M` ample `⟹` `M` ample of [Stacks, Tag 09MW] with the source's own
> hypotheses. The source's proof of [Stacks, Tag 0D2R] cites [Stacks, Tag 09MW] at exactly this
> point. Everything else is proved: an affine open `V'` of `S'` has `j^{-1}V'` affine because `j`
> is a closed immersion, the commutative square identifies `f^{-1}(j^{-1}V')` with
> `i^{-1}(f'^{-1}V')`, and the restricted morphism `i ∣_ (f'^{-1}V')` is again a thickening.

```lean
theorem isRelativelyAmple_of_isRelativelyAmple_pullback (href : AmpleReflectedByThickening.{u})
    (hi : IsThickening i) (hj : IsThickening j) (hsq : i ≫ f' = f ≫ j)
    (hL : IsRelativelyAmple f (pullbackModule i L')) :
    IsRelativelyAmple f' L'
```

**`Stacks.ThickeningInvertible.isRelativelyAmple_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ThickeningInvertible/Basic.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ThickeningInvertible/Basic.lean#L401). The attribute's comment: “the biconditional, carrying `href` = the `mp` half of [Tag 09MW]”.

> **[Stacks, Tag 0D2R]**, granted [Stacks, Tag 09MW]. For a morphism of thickenings
> `(f, f') : (X ⊆ X') → (S ⊆ S')` and an invertible `𝒪_{X'}`-module `ℒ'` with restriction
> `ℒ = i^* ℒ'` to `X`, the module `ℒ'` is `f'`-ample if and only if `ℒ` is `f`-ample.
>
> The `mp` half is `Stacks.ThickeningInvertible.isRelativelyAmple_pullback` and uses no hypothesis
> beyond the source's; the `mpr` half is
> `Stacks.ThickeningInvertible.isRelativelyAmple_of_isRelativelyAmple_pullback` and carries
> `href`.

```lean
theorem isRelativelyAmple_iff (href : AmpleReflectedByThickening.{u}) (hi : IsThickening i)
    (hj : IsThickening j) (hsq : i ≫ f' = f ≫ j) :
    IsRelativelyAmple f' L' ↔ IsRelativelyAmple f (pullbackModule i L')
```

## Tag 09ZW, a lemma

[Tag 09ZW](https://stacks.math.columbia.edu/tag/09ZW) in the Stacks Project.

**`Stacks.Thickenings.locallyOfFiniteType_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Cartesian.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Cartesian.lean#L170). The attribute's comment: “locally_finite_type”.

> Local finite type ascends and descends across a cartesian morphism of thickenings when
> the thickening of the base has finite order.

```lean
theorem locallyOfFiniteType_iff_of_isFiniteOrderThickening
    {X X' S S' : Scheme.{u}} (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S')
    (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) :
    LocallyOfFiniteType f ↔ LocallyOfFiniteType f'
```

**`Stacks.Thickenings.locallyQuasiFinite_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Cartesian.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Cartesian.lean#L235). The attribute's comment: “locally_quasi_finite”.

> Local quasi-finiteness is invariant under a cartesian morphism of thickenings when the
> thickening of the base has finite order.

```lean
theorem locallyQuasiFinite_iff_of_isFiniteOrderThickening
    {X X' S S' : Scheme.{u}} (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S')
    (hi : IsThickening i)
    (hj : IsFiniteOrderThickening j)
    (sq : IsPullback i f f' j) :
    (LocallyOfFiniteType f ∧ LocallyQuasiFinite f) ↔
      (LocallyOfFiniteType f' ∧ LocallyQuasiFinite f')
```

**`Stacks.Thickenings.isProper_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Cartesian.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Cartesian.lean#L254). The attribute's comment: “proper”.

> Properness ascends and descends along a cartesian morphism of thickenings when the
> thickening of the base has finite order.

```lean
theorem isProper_iff_of_isFiniteOrderThickening
    {X X' S S' : Scheme.{u}} (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S')
    (hi : IsThickening i)
    (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) :
    IsProper f ↔ IsProper f'
```

**`Stacks.Thickenings.formallyUnramified_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianDifferentials.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianDifferentials.lean#L180). The attribute's comment: “vanishing_differentials”.

> **Stacks 09ZW, part (5).** The relative differentials of `f` vanish exactly when the
> relative differentials of `f'` vanish, for a cartesian morphism of thickenings whose base
> thickening has finite order.

```lean
theorem formallyUnramified_iff_of_isFiniteOrderThickening
    {X X' S S' : Scheme.{u}} (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S')
    (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) :
    FormallyUnramified f ↔ FormallyUnramified f'
```

**`Stacks.Thickenings.isClosedImmersion_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean#L135). The attribute's comment: “closed_immersion”.

> **Stacks 09ZW, part (1).** Being a closed immersion ascends and descends across a cartesian
> morphism of thickenings when the thickening of the base has finite order.

```lean
theorem isClosedImmersion_iff_of_isFiniteOrderThickening (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S') (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) : IsClosedImmersion f ↔ IsClosedImmersion f'
```

**`Stacks.Thickenings.isFinite_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean#L144). The attribute's comment: “finite”.

> **Stacks 09ZW, part (8).** Being finite ascends and descends across a cartesian morphism of
> thickenings when the thickening of the base has finite order.

```lean
theorem isFinite_iff_of_isFiniteOrderThickening (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S') (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) : IsFinite f ↔ IsFinite f'
```

**`Stacks.Thickenings.isImmersion_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean#L153). The attribute's comment: “immersion”.

> **Stacks 09ZW, part (10).** Being an immersion ascends and descends across a cartesian
> morphism of thickenings when the thickening of the base has finite order.

```lean
theorem isImmersion_iff_of_isFiniteOrderThickening (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S') (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) : IsImmersion f ↔ IsImmersion f'
```

**`Stacks.Thickenings.mono_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianImmersions.lean#L248). The attribute's comment: “monomorphism”.

> **Stacks 09ZW, part (9).** Being a monomorphism ascends and descends across a cartesian
> morphism of thickenings when the thickening of the base has finite order.

```lean
theorem mono_iff_of_isFiniteOrderThickening (i : X ⟶ X') (j : S ⟶ S')
    (f : X ⟶ S) (f' : X' ⟶ S') (hj : IsFiniteOrderThickening j)
    (hcart : IsPullback i f f' j) : Mono f ↔ Mono f'
```

**`Stacks.Thickenings.locallyOfFiniteType_and_relativeDimension_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianRelativeDimension.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/CartesianRelativeDimension.lean#L143). The attribute's comment: “relative_dimension”.

> **Stacks 09ZW, part (4).** Being locally of finite type of relative dimension `d` ascends
> and descends across a cartesian morphism of thickenings when the thickening of the base has
> finite order.
>
> The property is the conjunction of local finite type and relative dimension `d`, and the
> statement is that conjunction; its first half is part (2) of the same tag.

```lean
theorem locallyOfFiniteType_and_relativeDimension_iff_of_isFiniteOrderThickening
    (i : X ⟶ X') (j : S ⟶ S') (f : X ⟶ S) (f' : X' ⟶ S')
    (hj : IsFiniteOrderThickening j) (hcart : IsPullback i f f' j) (d : ℕ) :
    (∃ _ : LocallyOfFiniteType f, RelativeDimension f d) ↔
      (∃ _ : LocallyOfFiniteType f', RelativeDimension f' d)
```

**`Stacks.Thickenings.unramified_iff_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismEtaleLocal.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/FiniteOrderMorphismEtaleLocal.lean#L111). The attribute's comment: “unramified”.

> **Stacks 09ZW, part (6).** Unramifiedness ascends and descends across a cartesian morphism
> of thickenings of schemes when the thickening of the base has finite order.
>
> The invariance of unramifiedness under a cartesian morphism of thickenings,
> `Stacks.Thickenings.IsThickening.unramified_iff_of_isPullback`, needs the deformation `f'` to be
> locally of finite type; the finite order of `j` provides it from local finite type of `f`, by
> part (2) of this tag. No finiteness hypothesis on the source thickening `i` is used.

```lean
theorem unramified_iff_of_isFiniteOrderThickening
    {X X' S S' : Scheme.{u}} (i : X ⟶ X') (j : S ⟶ S') (f : X ⟶ S) (f' : X' ⟶ S')
    (hj : Stacks.Thickenings.IsFiniteOrderThickening j) (hcart : IsPullback i f f' j) :
    Unramified f ↔ Unramified f'
```

## Tag 0BPG, a lemma

[Tag 0BPG](https://stacks.math.columbia.edu/tag/0BPG) in the Stacks Project.

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.locallyQuasiFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalProperties.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/EtaleLocalProperties.lean#L89). The attribute's comment: “locally_quasi_finite”.

> **Stacks 0BPG, part (1).** Being locally quasi-finite is invariant under a cartesian,
> locally finite type morphism of thickenings of schemes.

```lean
theorem CartesianFiniteTypeMorphism.locallyQuasiFinite_iff
    (S : CartesianFiniteTypeMorphism.{u}) :
    (LocallyOfFiniteType S.f ∧ LocallyQuasiFinite S.f) ↔
      (LocallyOfFiniteType S.f' ∧ LocallyQuasiFinite S.f')
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.isClosedImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean#L122). The attribute's comment: “closed_immersion”.

> Being a closed immersion is invariant under a cartesian, locally finite type morphism of
> thickenings.

```lean
theorem isClosedImmersion_iff (S : CartesianFiniteTypeMorphism.{u}) :
    IsClosedImmersion S.f ↔ IsClosedImmersion S.f'
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.isImmersion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean#L150). The attribute's comment: “immersion”.

> Being an immersion is invariant under a cartesian, locally finite type morphism of
> thickenings.

```lean
theorem isImmersion_iff (S : CartesianFiniteTypeMorphism.{u}) :
    IsImmersion S.f ↔ IsImmersion S.f'
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.isProper_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean#L274). The attribute's comment: “proper”.

> Properness is invariant under a cartesian, locally finite type morphism of
> thickenings.

```lean
theorem isProper_iff (S : CartesianFiniteTypeMorphism.{u}) :
    IsProper S.f ↔ IsProper S.f'
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.isFinite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Extension.lean#L286). The attribute's comment: “finite”.

> Finiteness is invariant under a cartesian, locally finite type morphism of thickenings: a
> morphism of schemes is finite exactly when it is proper and locally quasi-finite, and both of
> those are invariant.

```lean
theorem isFinite_iff (S : CartesianFiniteTypeMorphism.{u}) :
    IsFinite S.f ↔ IsFinite S.f'
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.isZero_relativeDifferentials_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Monomorphism.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Monomorphism.lean#L68). The attribute's comment: “vanishing_differentials”.

> **Stacks 0BPG, part (4).** In a cartesian morphism of thickenings whose two component
> morphisms are locally of finite type, the sheaf of relative differentials `Ω_{X/Y}` is zero if
> and only if `Ω_{X'/Y'}` is zero.

```lean
theorem isZero_relativeDifferentials_iff (S : CartesianFiniteTypeMorphism.{u}) :
    IsZero S.f.relativeDifferentials ↔ IsZero S.f'.relativeDifferentials
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.mono_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Monomorphism.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Monomorphism.lean#L109). The attribute's comment: “monomorphism”.

> **Stacks 0BPG, part (6).** Being a monomorphism is invariant under a cartesian, locally
> finite type morphism of thickenings.

```lean
theorem mono_iff (S : CartesianFiniteTypeMorphism.{u}) : Mono S.f ↔ Mono S.f'
```

**`Stacks.Thickenings.CartesianFiniteTypeMorphism.unramified_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Unramified.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningMorphism/Unramified.lean#L103). The attribute's comment: “unramified”.

> Being unramified is invariant under a cartesian, locally finite type morphism of
> thickenings.

```lean
theorem CartesianFiniteTypeMorphism.unramified_iff (S : CartesianFiniteTypeMorphism.{u}) :
    Unramified S.f ↔ Unramified S.f'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.3, Tag 0CF2](https://stacks.math.columbia.edu/tag/0CF2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
