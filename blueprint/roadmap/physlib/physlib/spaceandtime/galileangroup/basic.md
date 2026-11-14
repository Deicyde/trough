---
declaration: module
origin: cited
lean: GalileanGroup, GalileanGroup.orthogonal_smul_smul, GalileanGroup.one_rotation, GalileanGroup.one_velocity, GalileanGroup.one_spaceTranslation, GalileanGroup.one_timeTranslation, GalileanGroup.mul_rotation, GalileanGroup.mul_velocity
statement: formalized
proof: formalized
---

# The Galilean group

The module `Physlib.SpaceAndTime.GalileanGroup.Basic`, [Physlib/SpaceAndTime/GalileanGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean): 52 declarations (6 instances with no name), 18 with a docstring.

> This file defines Galilean transformations in `d` spatial dimensions, together with their group
> law and their action on `Time × Space d`.
>
> An element consists of a spatial orthogonal transformation `R`, a boost velocity `v`, a spatial
> translation `a`, and a time translation `b`. We use the active convention
> `(t, x) ↦ (t + b, R x + v t + a)`.

**`GalileanGroup`**, a structure, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L30).

> A Galilean transformation in `d` spatial dimensions. The fields are, in order, the spatial
> orthogonal part, boost velocity, spatial translation, and time translation.

```lean
structure GalileanGroup (d : ℕ := 3) where
  /-- The spatial orthogonal part. -/
  rotation : Matrix.orthogonalGroup (Fin d) ℝ
  /-- The boost velocity. -/
  velocity : EuclideanSpace ℝ (Fin d)
  /-- The spatial translation. -/
  spaceTranslation : EuclideanSpace ℝ (Fin d)
  /-- The time translation. -/
  timeTranslation : Time
```

## A. Basic support lemmas

**`GalileanGroup.orthogonal_smul_smul`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L44).

```lean
lemma orthogonal_smul_smul (R : Matrix.orthogonalGroup (Fin d) ℝ) (c : ℝ)
    (v : EuclideanSpace ℝ (Fin d)) :
    R • (c • v) = c • (R • v)
```

## B. Group operations

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L54).

> The identity Galilean transformation.

```lean
instance : One (GalileanGroup d)
```

**`GalileanGroup.one_rotation`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L58).

```lean
lemma one_rotation : (1 : GalileanGroup d).rotation = 1
```

**`GalileanGroup.one_velocity`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L61).

```lean
lemma one_velocity : (1 : GalileanGroup d).velocity = 0
```

**`GalileanGroup.one_spaceTranslation`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L64).

```lean
lemma one_spaceTranslation : (1 : GalileanGroup d).spaceTranslation = 0
```

**`GalileanGroup.one_timeTranslation`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L67).

```lean
lemma one_timeTranslation : (1 : GalileanGroup d).timeTranslation = 0
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L70).

> The product whose action is composition: `(g * h) • tx = g • h • tx`.

```lean
instance : Mul (GalileanGroup d)
```

**`GalileanGroup.mul_rotation`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L78).

```lean
lemma mul_rotation (g h : GalileanGroup d) :
    (g * h).rotation = g.rotation * h.rotation
```

**`GalileanGroup.mul_velocity`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L82).

```lean
lemma mul_velocity (g h : GalileanGroup d) :
    (g * h).velocity = g.rotation • h.velocity + g.velocity
```

**`GalileanGroup.mul_spaceTranslation`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L86).

```lean
lemma mul_spaceTranslation (g h : GalileanGroup d) :
    (g * h).spaceTranslation =
      g.spaceTranslation + g.rotation • h.spaceTranslation + h.timeTranslation.val • g.velocity
```

**`GalileanGroup.mul_timeTranslation`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L92).

```lean
lemma mul_timeTranslation (g h : GalileanGroup d) :
    (g * h).timeTranslation = g.timeTranslation + h.timeTranslation
```

**An instance with no name**, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L96).

> The inverse Galilean transformation.

```lean
instance : Inv (GalileanGroup d)
```

**`GalileanGroup.inv_rotation`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L104).

```lean
lemma inv_rotation (g : GalileanGroup d) :
    g⁻¹.rotation = g.rotation⁻¹
```

**`GalileanGroup.inv_velocity`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L109).

> The inverse boost velocity formula.

```lean
lemma inv_velocity (g : GalileanGroup d) :
    g⁻¹.velocity = -(g.rotation⁻¹ • g.velocity)
```

**`GalileanGroup.inv_spaceTranslation`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L113).

```lean
lemma inv_spaceTranslation (g : GalileanGroup d) :
    g⁻¹.spaceTranslation =
      -(g.rotation⁻¹ • g.spaceTranslation) +
        g.timeTranslation.val • (g.rotation⁻¹ • g.velocity)
```

**`GalileanGroup.inv_timeTranslation`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L119).

```lean
lemma inv_timeTranslation (g : GalileanGroup d) :
    g⁻¹.timeTranslation = -g.timeTranslation
```

**An instance with no name**, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L123).

> The Galilean transformations form a group under composition.

```lean
instance : Group (GalileanGroup d)
```

**An instance with no name**, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L156).

```lean
instance : Inhabited (GalileanGroup d)
```

## C. Action on time and space

**`GalileanGroup.actSpace`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L162).

> The Galilean action on space at the time `t`, `x ↦ R x + v t + a`.

```lean
noncomputable def actSpace (g : GalileanGroup d) (t : Time) (x : Space d) : Space d
```

**`GalileanGroup.act`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L167).

> The Galilean action on `Time × Space d`.

```lean
noncomputable def act (g : GalileanGroup d) (tx : Time × Space d) : Time × Space d
```

**An instance with no name**, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L170).

```lean
noncomputable instance : MulAction (GalileanGroup d) (Time × Space d)
```

**`GalileanGroup.smul_fst`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L188).

```lean
lemma smul_fst (g : GalileanGroup d) (tx : Time × Space d) :
    (g • tx).1 = tx.1 + g.timeTranslation
```

**`GalileanGroup.smul_snd`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L192).

```lean
lemma smul_snd (g : GalileanGroup d) (tx : Time × Space d) :
    (g • tx).2 = g.actSpace tx.1 tx.2
```

**`GalileanGroup.smul_mk`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L196).

```lean
lemma smul_mk (g : GalileanGroup d) (t : Time) (x : Space d) :
    g • ((t, x) : Time × Space d) = (t + g.timeTranslation, g.actSpace t x)
```

**`GalileanGroup.actSpace_apply`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L200).

```lean
lemma actSpace_apply (g : GalileanGroup d) (t : Time) (x : Space d) (i : Fin d) :
    g.actSpace t x i =
      (g.rotation • (x -ᵥ (0 : Space d))) i + t.val * g.velocity i + g.spaceTranslation i
```

## D. Subgroup inclusions

**`GalileanGroup.ofEuclidean`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L209).

> A Euclidean spatial transformation as a Galilean transformation with zero boost and no time
> translation.

```lean
def ofEuclidean (g : EuclideanGroup d) : GalileanGroup d
```

**`GalileanGroup.ofEuclidean_rotation`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L213).

```lean
lemma ofEuclidean_rotation (g : EuclideanGroup d) :
    (ofEuclidean g).rotation = g.linear
```

**`GalileanGroup.ofEuclidean_velocity`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L217).

```lean
lemma ofEuclidean_velocity (g : EuclideanGroup d) :
    (ofEuclidean g).velocity = 0
```

**`GalileanGroup.ofEuclidean_spaceTranslation`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L221).

```lean
lemma ofEuclidean_spaceTranslation (g : EuclideanGroup d) :
    (ofEuclidean g).spaceTranslation = g.translation
```

**`GalileanGroup.ofEuclidean_timeTranslation`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L225).

```lean
lemma ofEuclidean_timeTranslation (g : EuclideanGroup d) :
    (ofEuclidean g).timeTranslation = 0
```

**`GalileanGroup.euclidean.incl`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L229).

> Inclusion of the Euclidean group into the Galilean group.

```lean
def euclidean.incl : EuclideanGroup d →* GalileanGroup d
```

**`GalileanGroup.ofOrthogonal`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L236).

> A pure orthogonal spatial transformation as a Galilean transformation.

```lean
def ofOrthogonal (R : Matrix.orthogonalGroup (Fin d) ℝ) : GalileanGroup d
```

**`GalileanGroup.ofOrthogonal_rotation`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L240).

```lean
lemma ofOrthogonal_rotation (R : Matrix.orthogonalGroup (Fin d) ℝ) :
    (ofOrthogonal R).rotation = R
```

**`GalileanGroup.ofOrthogonal_velocity`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L244).

```lean
lemma ofOrthogonal_velocity (R : Matrix.orthogonalGroup (Fin d) ℝ) :
    (ofOrthogonal R).velocity = 0
```

**`GalileanGroup.ofOrthogonal_spaceTranslation`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L248).

```lean
lemma ofOrthogonal_spaceTranslation (R : Matrix.orthogonalGroup (Fin d) ℝ) :
    (ofOrthogonal R).spaceTranslation = 0
```

**`GalileanGroup.ofOrthogonal_timeTranslation`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L252).

```lean
lemma ofOrthogonal_timeTranslation (R : Matrix.orthogonalGroup (Fin d) ℝ) :
    (ofOrthogonal R).timeTranslation = 0
```

**`GalileanGroup.orthogonal.incl`**, a def, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L256).

> Inclusion of the orthogonal group into the Galilean group.

```lean
def orthogonal.incl : Matrix.orthogonalGroup (Fin d) ℝ →* GalileanGroup d
```

**`GalileanGroup.rotation.incl`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L263).

> Inclusion of the existing spatial rotation subgroup into the Galilean group.

```lean
noncomputable def rotation.incl : EuclideanGroup.RotationGroup d →* GalileanGroup d
```

**`GalileanGroup.ofSpaceTranslation`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L270).

> A pure spatial translation as a Galilean transformation.

```lean
def ofSpaceTranslation (a : EuclideanSpace ℝ (Fin d)) : GalileanGroup d
```

**`GalileanGroup.ofSpaceTranslation_rotation`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L274).

```lean
lemma ofSpaceTranslation_rotation (a : EuclideanSpace ℝ (Fin d)) :
    (ofSpaceTranslation a).rotation = 1
```

**`GalileanGroup.ofSpaceTranslation_velocity`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L278).

```lean
lemma ofSpaceTranslation_velocity (a : EuclideanSpace ℝ (Fin d)) :
    (ofSpaceTranslation a).velocity = 0
```

**`GalileanGroup.ofSpaceTranslation_spaceTranslation`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L282).

```lean
lemma ofSpaceTranslation_spaceTranslation (a : EuclideanSpace ℝ (Fin d)) :
    (ofSpaceTranslation a).spaceTranslation = a
```

**`GalileanGroup.ofSpaceTranslation_timeTranslation`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L286).

```lean
lemma ofSpaceTranslation_timeTranslation (a : EuclideanSpace ℝ (Fin d)) :
    (ofSpaceTranslation a).timeTranslation = 0
```

**`GalileanGroup.spaceTranslation.incl`**, a def, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L290).

> Inclusion of spatial translations into the Galilean group.

```lean
def spaceTranslation.incl :
    Multiplicative (EuclideanSpace ℝ (Fin d)) →* GalileanGroup d
```

**`GalileanGroup.spaceTranslationGroup.incl`**, a def, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L298).

> Inclusion of the existing spatial translation subgroup into the Galilean group.

```lean
noncomputable def spaceTranslationGroup.incl :
    EuclideanGroup.TranslationGroup d →* GalileanGroup d
```

**`GalileanGroup.ofTimeTranslation`**, a def, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L303).

> A pure time translation as a Galilean transformation.

```lean
def ofTimeTranslation (b : Time) : GalileanGroup d
```

**`GalileanGroup.ofTimeTranslation_rotation`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L307).

```lean
lemma ofTimeTranslation_rotation (b : Time) :
    (ofTimeTranslation (d := d) b).rotation = 1
```

**`GalileanGroup.ofTimeTranslation_velocity`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L311).

```lean
lemma ofTimeTranslation_velocity (b : Time) :
    (ofTimeTranslation (d := d) b).velocity = 0
```

**`GalileanGroup.ofTimeTranslation_spaceTranslation`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L315).

```lean
lemma ofTimeTranslation_spaceTranslation (b : Time) :
    (ofTimeTranslation (d := d) b).spaceTranslation = 0
```

**`GalileanGroup.ofTimeTranslation_timeTranslation`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L319).

```lean
lemma ofTimeTranslation_timeTranslation (b : Time) :
    (ofTimeTranslation (d := d) b).timeTranslation = b
```

**`GalileanGroup.timeTranslation.incl`**, a def, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean#L323).

> Inclusion of time translations into the Galilean group.

```lean
def timeTranslation.incl : Multiplicative Time →* GalileanGroup d
```

## Depends on

- [Euclidean group](../space/part-02/euclideangroup-basic.md)
- [The origin of `Space` and the Euclidean chart](../space/part-01/origin.md)
- [Time as an inner product space](../time/innerproductspace.md)

## Sources

- [Physlib/SpaceAndTime/GalileanGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/Basic.lean)
