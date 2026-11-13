---
declaration: module
origin: cited
lean: EuclideanGroup, EuclideanGroup.one_translation, EuclideanGroup.one_linear, EuclideanGroup.mul_translation, EuclideanGroup.mul_linear, EuclideanGroup.SpecialEuclideanGroup, EuclideanGroup.SpecialEuclideanGroup.incl, EuclideanGroup.TranslationGroup
statement: formalized
proof: formalized
---

# Euclidean group

The module `Physlib.SpaceAndTime.Space.EuclideanGroup.Basic`, [Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean): 35 declarations (1 instance with no name), 31 with a docstring; 2 private, not shown.

> This file defines the Euclidean group as translations composed with orthogonal maps, together
> with the special Euclidean group, translation subgroup, and rotation subgroups.
>
> The affine group, together with the inclusion of the Euclidean group into it, is defined in
> `Physlib.SpaceAndTime.Space.EuclideanGroup.AffineGroup`.

**`EuclideanGroup`**, a structure, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L26).

> An n-dimensional `Euclidean group` is a group of
> rotations, reflections, and translations.

```lean
structure EuclideanGroup (n : ℕ) where
  /-- The translation part of a Euclidean transformation. -/
  translation : EuclideanSpace ℝ (Fin n)
  /-- The orthogonal linear part of a Euclidean transformation. -/
  linear : Matrix.orthogonalGroup (Fin n) ℝ
```

**An instance with no name**, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L37).

> Group structure on `E(n) = ℝ^n ⋊ O(n)`. The orthogonal component acts on translations by
> the inherited matrix-vector action on `EuclideanSpace ℝ (Fin n)`, transported through `WithLp`
> from the coordinate action `Q.val *ᵥ v.ofLp`.

```lean
noncomputable instance : Group (EuclideanGroup n)
```

### `One`/`Mul` projection lemmas

> These expose the semidirect-product formulas behind the `Group` instance so that `simp` can
> reduce the translation/linear components of `1` and `A * B`.

**`EuclideanGroup.one_translation`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L68).

```lean
lemma one_translation : (1 : EuclideanGroup n).translation = 0
```

**`EuclideanGroup.one_linear`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L70).

```lean
lemma one_linear : (1 : EuclideanGroup n).linear = 1
```

**`EuclideanGroup.mul_translation`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L72).

```lean
lemma mul_translation (A B : EuclideanGroup n) :
    (A * B).translation = A.translation + A.linear • B.translation
```

**`EuclideanGroup.mul_linear`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L75).

```lean
lemma mul_linear (A B : EuclideanGroup n) :
    (A * B).linear = A.linear * B.linear
```

**`EuclideanGroup.SpecialEuclideanGroup`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L91).

> Special Euclidean Group is the subgroup with det(Q) = 1 where Q ∈ O(n)

```lean
def SpecialEuclideanGroup (n : ℕ) : Subgroup (EuclideanGroup n)
```

**`EuclideanGroup.SpecialEuclideanGroup.incl`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L104).

> The inclusion of the special Euclidean group into the Euclidean group.

```lean
noncomputable def SpecialEuclideanGroup.incl (n : ℕ) :
    SpecialEuclideanGroup n →* EuclideanGroup n
```

**`EuclideanGroup.TranslationGroup`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L108).

> Translation is the subgroup with Q = 1.

```lean
def TranslationGroup (n : ℕ) : Subgroup (EuclideanGroup n)
```

**`EuclideanGroup.TranslationGroup.incl`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L121).

> The inclusion of the translation subgroup into the Euclidean group.

```lean
noncomputable def TranslationGroup.incl (n : ℕ) :
    TranslationGroup n →* EuclideanGroup n
```

**`EuclideanGroup.translationVector.incl`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L125).

> MonoidHom including a translation vector into the Euclidean Group.

```lean
def translationVector.incl (n : ℕ) :
    Multiplicative (EuclideanSpace ℝ (Fin n)) →* EuclideanGroup n
```

**`EuclideanGroup.translationVector.incl_range`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L139).

> An API feature: the translation vector inclusion image is the `TranslationGroup` carrier.

```lean
lemma translationVector.incl_range :
    Set.range (@translationVector.incl n) = (TranslationGroup n : Set (EuclideanGroup n))
```

**`EuclideanGroup.translation_zero`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L156).

> The translation by the zero vector is the identity of the Euclidean group.

```lean
lemma translation_zero : translationVector.incl n
    (Multiplicative.ofAdd (0 : EuclideanSpace ℝ (Fin n))) = 1
```

**`EuclideanGroup.OriginStabilizer`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L162).

> The subgroup of `EuclideanGroup n` whose elements fix the origin
> (translation = 0). This is the copy of `O(n)` sitting inside `E(n)`.

```lean
def OriginStabilizer (n : ℕ) : Subgroup (EuclideanGroup n)
```

**`EuclideanGroup.RotationGroup`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L174).

> Rotation Group is the subgroup of E(n) consisting of rotations about the origin:
> elements with `det = 1` (orientation-preserving) and `translation = 0` (origin-fixing).

```lean
noncomputable def RotationGroup (n : ℕ) : Subgroup (EuclideanGroup n)
```

**`EuclideanGroup.RotationGroup.incl`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L178).

> The inclusion of the rotation subgroup into the Euclidean group.

```lean
noncomputable def RotationGroup.incl (n : ℕ) :
    RotationGroup n →* EuclideanGroup n
```

**`EuclideanGroup.RotationsAbout`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L186).

> The subgroup of rotation about a spatial point `p : EuclideanSpace ℝ (Fin n)` consists of
> elements of the form T(p) * r * T(-p) with T(·) : translationVector.incl n (Multiplicative.ofAdd ·)
> and r : RotationGroup where r is viewed as a rotation about the origin. Note T(-p) = T(p)⁻¹.

```lean
noncomputable def RotationsAbout : Subgroup (EuclideanGroup n)
```

**`EuclideanGroup.RotationsAbout.incl`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L205).

> The inclusion of rotations about `p` into the Euclidean group.

```lean
noncomputable def RotationsAbout.incl : RotationsAbout p →* EuclideanGroup n
```

**`EuclideanGroup.RotationsAbout.toOrigin`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L209).

> Conjugate a rotation about `p` back to a rotation about the origin.

```lean
noncomputable def RotationsAbout.toOrigin :
    RotationsAbout p →* RotationGroup n
```

**`EuclideanGroup.RotationsAbout.fromOrigin`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L229).

> Conjugate a rotation about the origin to a rotation about `p`.

```lean
noncomputable def RotationsAbout.fromOrigin :
    RotationGroup n →* RotationsAbout p
```

**`EuclideanGroup.RotationsAbout.fromOrigin_comp_toOrigin`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L244).

> `RotationsAbout.toOrigin p` followed by `RotationsAbout.fromOrigin p` is the identity; the
> forward leg of the isomorphism `RotationsAboutEquiv`.

```lean
lemma RotationsAbout.fromOrigin_comp_toOrigin :
    (RotationsAbout.fromOrigin p).comp (RotationsAbout.toOrigin p) =
      MonoidHom.id (RotationsAbout p)
```

**`EuclideanGroup.RotationsAbout.toOrigin_comp_fromOrigin`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L257).

> `RotationsAbout.fromOrigin p` followed by `RotationsAbout.toOrigin p` is the identity; the
> backward leg of the isomorphism `RotationsAboutEquiv`.

```lean
lemma RotationsAbout.toOrigin_comp_fromOrigin :
    (RotationsAbout.toOrigin p).comp (RotationsAbout.fromOrigin p) =
      MonoidHom.id (RotationGroup n)
```

**`EuclideanGroup.RotationsAboutEquiv`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L270).

> API feature: conjugation by the translation `T(p)` exhibits the rotations about `p` as
> isomorphic to the rotations about the origin `RotationGroup n`.

```lean
noncomputable def RotationsAboutEquiv : RotationsAbout p ≃* RotationGroup n
```

**`EuclideanGroup.RotationsAbout_zero`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L275).

> API feature: the degenerate identity that `RotationsAbout 0 = RotationGroup n`

```lean
lemma RotationsAbout_zero : RotationsAbout (0 : EuclideanSpace ℝ (Fin n)) = RotationGroup n
```

**`EuclideanGroup.specialOrthogonal.incl`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L289).

> Rotations are members of special orthogonal groups and can be viewed as members of
> orthogonal groups.

```lean
def specialOrthogonal.incl (n : ℕ) :
    Matrix.specialOrthogonalGroup (Fin n) ℝ →* Matrix.orthogonalGroup (Fin n) ℝ
```

**`EuclideanGroup.ofRotation`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L294).

> The Euclidean group element given by a rotation about the origin (zero translation).

```lean
def ofRotation (Q : Matrix.specialOrthogonalGroup (Fin n) ℝ) :
    EuclideanGroup n
```

**`EuclideanGroup.ofRotationTranslation`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L298).

> Specialization to a group element from a rotation and a translation.

```lean
def ofRotationTranslation (Q : Matrix.specialOrthogonalGroup (Fin n) ℝ)
    (t : EuclideanSpace ℝ (Fin n)) : EuclideanGroup n
```

**`EuclideanGroup.ofRotationTranslation_translation`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L304).

> The specialization projects back to the translation component.

```lean
lemma ofRotationTranslation_translation (Q : Matrix.specialOrthogonalGroup (Fin n) ℝ)
    (t : EuclideanSpace ℝ (Fin n)) :
    (ofRotationTranslation Q t).translation = t
```

**`EuclideanGroup.ofRotationTranslation_linear`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L310).

> The specialization projects back to the linear (rotation) component.

```lean
lemma ofRotationTranslation_linear (Q : Matrix.specialOrthogonalGroup (Fin n) ℝ)
    (t : EuclideanSpace ℝ (Fin n)) :
    (ofRotationTranslation Q t).linear = specialOrthogonal.incl n Q
```

**`EuclideanGroup.ofRotationTranslation_decompose`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L316).

> API feature: the inclusion image decomposes as group product.

```lean
lemma ofRotationTranslation_decompose (Q : Matrix.specialOrthogonalGroup (Fin n) ℝ)
    (t : EuclideanSpace ℝ (Fin n)) :
    (ofRotationTranslation Q t) =
    (translationVector.incl n (Multiplicative.ofAdd t)) * (ofRotation (Q))
```

**`EuclideanGroup.specialOrthogonal.toRotation`**, a def, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L327).

> The isomorphism's forward map: a special orthogonal matrix as a rotation about the origin.

```lean
noncomputable def specialOrthogonal.toRotation (n : ℕ) :
    Matrix.specialOrthogonalGroup (Fin n) ℝ →* RotationGroup n
```

**`EuclideanGroup.specialOrthogonal.fromRotation`**, a def, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L348).

> The isomorphism's inverse map: the linear part of a rotation about the origin, as a special
> orthogonal matrix.

```lean
noncomputable def specialOrthogonal.fromRotation (n : ℕ) :
    RotationGroup n →* Matrix.specialOrthogonalGroup (Fin n) ℝ
```

**`EuclideanGroup.specialOrthogonal.fromRotation_comp_toRotation`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L356).

> `specialOrthogonal.toRotation n` followed by `specialOrthogonal.fromRotation n` is the identity;
> the forward leg of the isomorphism `specialOrthogonalEquiv`.

```lean
lemma specialOrthogonal.fromRotation_comp_toRotation :
    (specialOrthogonal.fromRotation n).comp (specialOrthogonal.toRotation n) =
      MonoidHom.id (Matrix.specialOrthogonalGroup (Fin n) ℝ)
```

**`EuclideanGroup.specialOrthogonal.toRotation_comp_fromRotation`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L365).

> `specialOrthogonal.fromRotation n` followed by `specialOrthogonal.toRotation n` is the identity;
> the backward leg of the isomorphism `specialOrthogonalEquiv`.

```lean
lemma specialOrthogonal.toRotation_comp_fromRotation :
    (specialOrthogonal.toRotation n).comp (specialOrthogonal.fromRotation n) =
      MonoidHom.id (RotationGroup n)
```

**`EuclideanGroup.specialOrthogonalEquiv`**, a def, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean#L378).

> API feature: SO(n) ≃* RotationGroup n

```lean
noncomputable def specialOrthogonalEquiv :
    Matrix.specialOrthogonalGroup (Fin n) ℝ ≃* RotationGroup n
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/EuclideanGroup/Basic.lean)
