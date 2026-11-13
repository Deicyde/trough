---
declaration: section
origin: cited
lean: Stacks.Frobenius.absoluteFrobenius, Stacks.Frobenius.absoluteFrobenius_naturality, AlgebraicGeometry.absoluteFrobenius_universalHomeomorphism, AlgebraicGeometry.absoluteFrobenius_isIntegralHom, AlgebraicGeometry.absoluteFrobenius_residueFieldMap_isPurelyInseparable, AlgebraicGeometry.frobeniusTwist, AlgebraicGeometry.relativeFrobenius_existsUnique, AlgebraicGeometry.relativeFrobenius
statement: formalized
proof: formalized
---

# 33.36 Frobenii

Section 33.36 of the Stacks Project, [Tag 0CC6](https://stacks.math.columbia.edu/tag/0CC6). 11 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03SM, a definition

[Tag 03SM](https://stacks.math.columbia.edu/tag/03SM) in the Stacks Project.

**`Stacks.Frobenius.absoluteFrobenius`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Frobenius.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Frobenius.lean#L157). References: SGA 3 VIIA (4.1), “absolute Frobenius fr(X)”; SGA 5 XV (1.Definition2); SGA 4½ Fonctions L (3.4), “F\_abs definition”; SGA 4½ Rapport (1.1), “q = p”; SGA 3 VIIB (4.1.1); SGA 7 IX (4.3.2), “special case”; SGA 7 XXI (1.0); SGA 7 XXII (6.2), “(6.2.1) F\_q for q = p”.

> **Stacks Project, Tag 03SM.** The absolute Frobenius of a scheme in characteristic `p`: it
> is the identity on points and the `p`-th power map on the structure sheaf.

```lean
noncomputable def absoluteFrobenius (X : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hX : IsInCharacteristic X p) : X ⟶ X
```

## Tag 0CC7, a lemma

[Tag 0CC7](https://stacks.math.columbia.edu/tag/0CC7) in the Stacks Project.

**`Stacks.Frobenius.absoluteFrobenius_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Absolute.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Absolute.lean#L39). References: EGA 0 (21.2.6), “more general”; SGA 3 VIIA (4.1); SGA 4½ Rapport (1.3), “special case”; SGA 7 IX (4.3.2), “partial”.

> The absolute Frobenius is natural with respect to morphisms of schemes in characteristic
> `p`.

```lean
public lemma absoluteFrobenius_naturality {X Y : Scheme.{u}} (f : X ⟶ Y) (p : ℕ)
    [Fact p.Prime] (hX : IsInCharacteristic X p) (hY : IsInCharacteristic Y p) :
    absoluteFrobenius X p hX ≫ f = f ≫ absoluteFrobenius Y p hY
```

## Tag 0CC8, a lemma

[Tag 0CC8](https://stacks.math.columbia.edu/tag/0CC8) in the Stacks Project.

**`AlgebraicGeometry.absoluteFrobenius_universalHomeomorphism`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/AbsoluteUniversalHomeomorphism.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/AbsoluteUniversalHomeomorphism.lean#L109).

> The absolute Frobenius of a scheme in positive prime characteristic is a universal
> homeomorphism.

```lean
instance absoluteFrobenius_universalHomeomorphism
    (X : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hX : IsInCharacteristic X p) :
    UniversalHomeomorphism (absoluteFrobenius X p hX)
```

**`AlgebraicGeometry.absoluteFrobenius_isIntegralHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/AbsoluteUniversalHomeomorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/AbsoluteUniversalHomeomorphism.lean#L131).

> The absolute Frobenius of a scheme in positive prime characteristic is integral.

```lean
instance absoluteFrobenius_isIntegralHom
    (X : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hX : IsInCharacteristic X p) :
    IsIntegralHom (absoluteFrobenius X p hX)
```

**`AlgebraicGeometry.absoluteFrobenius_residueFieldMap_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/AbsoluteUniversalHomeomorphism.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/AbsoluteUniversalHomeomorphism.lean#L139).

> The map on residue fields induced by the absolute Frobenius is purely inseparable at every
> point.

```lean
theorem absoluteFrobenius_residueFieldMap_isPurelyInseparable
    (X : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hX : IsInCharacteristic X p)
    (x : X) :
    ((absoluteFrobenius X p hX).residueFieldMap x).hom.IsPurelyInseparable
```

## Tag 0CC9, a definition

[Tag 0CC9](https://stacks.math.columbia.edu/tag/0CC9) in the Stacks Project.

**`AlgebraicGeometry.frobeniusTwist`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean#L69). The attribute's comment: “frobenius\_twist”. References: SGA 3 VIIA (4.1), “special case”; SGA 3 VIIA (4.3.2); SGA 3 VIIB (4.1.1); SGA 3 XVII (4.3.2), “partial”.

> **Stacks Project, Tag 0CC9.** Frobenius twisting is base change along the absolute
> Frobenius of the base scheme. Its value at `X : Over S` is `X ×_S S`, regarded as an
> `S`-scheme through the second projection.

```lean
public noncomputable def frobeniusTwist (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) : Over S ⥤ Over S
```

**`AlgebraicGeometry.relativeFrobenius_existsUnique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean#L95). The attribute's comment: “relative\_frobenius\_characterization”.

> **Stacks Project, Tag 0CC9.** The relative Frobenius is the unique morphism over `S`
> whose first projection is the absolute Frobenius of `X` and whose second projection is the
> structure morphism of `X`.

```lean
public theorem relativeFrobenius_existsUnique (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (X : Over S) :
    ∃! g : X ⟶ (frobeniusTwist S p hS).obj X,
      (g.left ≫ pullback.fst X.hom (absoluteFrobenius S p hS) =
          absoluteFrobenius X.left p (isInCharacteristic_of_hom X.hom p hS)) ∧
      (g.left ≫ pullback.snd X.hom (absoluteFrobenius S p hS) = X.hom)
```

**`AlgebraicGeometry.relativeFrobenius`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean#L114). The attribute's comment: “relative\_frobenius”. References: SGA 5 XV (1.Definition3); SGA 3 VIIA (4.1), “Fr(X/S) for S-schemes”; SGA 3 VIIA (4.1.3), “Case n=1”; SGA 5 XII (7.3).

> **Stacks Project, Tag 0CC9.** The relative Frobenius morphism of an `S`-scheme.

```lean
public noncomputable def relativeFrobenius (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (X : Over S) : X ⟶ (frobeniusTwist S p hS).obj X
```

## Tag 0CCA, a lemma

[Tag 0CCA](https://stacks.math.columbia.edu/tag/0CCA) in the Stacks Project.

**`AlgebraicGeometry.relativeFrobenius_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Twist.lean#L147). References: SGA 3 VIIA (4.1), “special case”; SGA 3 VIIA (4.1.3), “special case”; SGA 4½ Rapport (1.3), “special case”; SGA 5 XV (1.Proposition1), “partial”.

> **Stacks Project, Tag 0CCA.** The relative Frobenius is natural in an `S`-scheme.

```lean
public lemma relativeFrobenius_naturality (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) {X Y : Over S} (f : X ⟶ Y) :
    relativeFrobenius S p hS X ≫ (frobeniusTwist S p hS).map f =
      f ≫ relativeFrobenius S p hS Y
```

## Tag 0CCB, a lemma

[Tag 0CCB](https://stacks.math.columbia.edu/tag/0CCB) in the Stacks Project.

**`AlgebraicGeometry.relativeFrobenius_universalHomeomorphism`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L67). References: SGA 5 XV (1.Proposition2), “a) univ. homeo”.

> The relative Frobenius is a universal homeomorphism.

```lean
instance relativeFrobenius_universalHomeomorphism
    (S : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hS : IsInCharacteristic S p)
    (X : Over S) :
    UniversalHomeomorphism (relativeFrobenius S p hS X).left
```

**`AlgebraicGeometry.relativeFrobenius_isIntegralHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L84). References: SGA 5 XV (1.Proposition2), “a) integral”; SGA 3 VIIA (7.4.2), “more general”.

> The relative Frobenius is integral.

```lean
instance relativeFrobenius_isIntegralHom
    (S : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hS : IsInCharacteristic S p)
    (X : Over S) :
    IsIntegralHom (relativeFrobenius S p hS X).left
```

**`AlgebraicGeometry.relativeFrobenius_residueFieldMap_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L93). References: SGA 5 XV (1.Proposition2), “a) radicial”.

> Every residue-field extension induced by the relative Frobenius is purely inseparable.

```lean
theorem relativeFrobenius_residueFieldMap_isPurelyInseparable
    (S : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hS : IsInCharacteristic S p)
    (X : Over S) (x : X.left) :
    (((relativeFrobenius S p hS X).left).residueFieldMap x).hom.IsPurelyInseparable
```

## Tag 0CCC, a lemma

[Tag 0CCC](https://stacks.math.columbia.edu/tag/0CCC) in the Stacks Project.

**`AlgebraicGeometry.relativeFrobenius_toRelativeDifferentials_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/RelativeFrobenius.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/RelativeFrobenius.lean#L352). References: EGA 0 (21.3.2), “more general”.

> **Stacks Project, Tag 0CCC.** The canonical map from the differentials of
> `X` over `S` to the differentials of `X` over its Frobenius twist is an
> isomorphism.

```lean
theorem relativeFrobenius_toRelativeDifferentials_isIso
    (S : Scheme.{u}) (p : ℕ) [Fact p.Prime] (hS : IsInCharacteristic S p) (X : Over S) :
    IsIso (Scheme.Hom.toRelativeDifferentials
      (relativeFrobenius S p hS X).left ((frobeniusTwist S p hS).obj X).hom)
```

## Tag 0CCD, a lemma

[Tag 0CCD](https://stacks.math.columbia.edu/tag/0CCD) in the Stacks Project.

**`AlgebraicGeometry.relativeFrobenius_isFinite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L106). References: SGA 5 XV (1.Proposition2), “Clause a), special case”.

> **Stacks Project, Tag 0CCD.** The relative Frobenius of an `S`-scheme locally of finite type
> over `S` is finite.

```lean
instance relativeFrobenius_isFinite (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (X : Over S) [LocallyOfFiniteType X.hom] :
    IsFinite (relativeFrobenius S p hS X).left
```

## Tag 0CCE, a lemma

[Tag 0CCE](https://stacks.math.columbia.edu/tag/0CCE) in the Stacks Project.

**`AlgebraicGeometry.geometricallyReduced_iff_isReduced_frobeniusTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Geometric/ReducedFrobeniusTwist.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Geometric/ReducedFrobeniusTwist.lean#L68).

> **Stacks Project, Tag 0CCE.** A scheme over a field of characteristic `p > 0` is
> geometrically reduced if and only if its Frobenius twist is reduced.

```lean
public theorem geometricallyReduced_iff_isReduced_frobeniusTwist
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    let hS : IsInCharacteristic (Spec (.of k)) p :=
      Stacks.Frobenius.isInCharacteristic_of_over (Over.mk (𝟙 (Spec (.of k))))
    GeometricallyReduced f ↔
      IsReduced (((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk f)).left)
```

## Tag 0CCF, a lemma

[Tag 0CCF](https://stacks.math.columbia.edu/tag/0CCF) in the Stacks Project.

**`AlgebraicGeometry.isReduced_frobeniusTwist_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/ReducedTwistTFAE.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/ReducedTwistTFAE.lean#L56). The attribute's comment: “reduced\_twist\_tfae”.

> **Stacks Project, Tag 0CCF.** For a reduced scheme `X` locally of finite type over a field
> `k` of characteristic `p > 0`, the following are equivalent: the Frobenius twist of `X` is
> reduced, `X` is geometrically reduced over `k`, and `X` has a dense open subscheme smooth over
> `k`.

```lean
theorem isReduced_frobeniusTwist_tfae
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsReduced X] [LocallyOfFiniteType f] :
    let hS : IsInCharacteristic (Spec (.of k)) p :=
      Stacks.Frobenius.isInCharacteristic_of_over (Over.mk (𝟙 (Spec (.of k))))
    List.TFAE
      [IsReduced (((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk f)).left),
        GeometricallyReduced f,
        ∃ U : X.Opens, Dense (U : Set X) ∧ Smooth (U.ι ≫ f)]
```

**`AlgebraicGeometry.isReduced_frobeniusTwist_tfae_of_isVariety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/ReducedTwistTFAE.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/ReducedTwistTFAE.lean#L85). The attribute's comment: “reduced\_twist\_tfae, the variety form with a nonempty smooth open”.

> **Stacks Project, Tag 0CCF.** For a variety `X` over a field `k` of characteristic `p > 0`,
> the following are equivalent: the Frobenius twist of `X` is reduced, `X` is geometrically reduced
> over `k`, and there is a nonempty open subscheme of `X` smooth over `k`.

```lean
theorem isReduced_frobeniusTwist_tfae_of_isVariety
    {k : Type u} [Field k] (p : ℕ) [Fact p.Prime] [CharP k p]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsVariety k f] :
    let hS : IsInCharacteristic (Spec (.of k)) p :=
      Stacks.Frobenius.isInCharacteristic_of_over (Over.mk (𝟙 (Spec (.of k))))
    List.TFAE
      [IsReduced (((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk f)).left),
        GeometricallyReduced f,
        ∃ U : X.Opens, (U : Set X).Nonempty ∧ Smooth (U.ι ≫ f)]
```

**`AlgebraicGeometry.residueDegree_relativeFrobenius_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeFrobeniusDegree.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeFrobeniusDegree.lean#L86). The attribute's comment: “frobenius\_degree, as the residue degree at the generic point”.

> **Stacks Project, Tag 0CCF.** For a geometrically reduced integral scheme of dimension `d`,
> locally of finite type over a field `k` of characteristic `p`, the residue degree of the
> relative Frobenius at the generic point is `p ^ d`.

```lean
theorem residueDegree_relativeFrobenius_genericPoint
    {k : Type u} [Field k] {X : Scheme.{u}} (pX : X ⟶ Spec (.of k))
    (p : ℕ) [Fact p.Prime] [CharP k p] [IsIntegral X] [LocallyOfFiniteType pX]
    (hS : IsInCharacteristic (Spec (.of k)) p) (hgeom : GeometricallyReduced pX)
    (d : ℕ) (hd : topologicalKrullDim X = d) :
    (relativeFrobenius (Spec (.of k)) p hS (Over.mk pX)).left.residueDegree (genericPoint X) =
      p ^ d
```

**`AlgebraicGeometry.degreeOver_relativeFrobenius`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeFrobeniusDegree.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeFrobeniusDegree.lean#L132). The attribute's comment: “frobenius\_degree”.

> **Stacks Project, Tag 0CCF.** For a variety `X` of dimension `d` over a field `k` of
> characteristic `p` whose Frobenius twist is reduced, the relative Frobenius of `X` has degree
> `p ^ d` over the twist.

```lean
theorem degreeOver_relativeFrobenius
    {k : Type u} [Field k] {X : Scheme.{u}} (pX : X ⟶ Spec (.of k)) [IsVariety k pX]
    (p : ℕ) [Fact p.Prime] [CharP k p] (hS : IsInCharacteristic (Spec (.of k)) p)
    (hred : IsReduced (((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk pX)).left))
    (d : ℕ) (hd : topologicalKrullDim X = d) :
    letI : LocallyOfFiniteType (Over.mk pX).hom := inferInstanceAs (LocallyOfFiniteType pX)
    letI : IsVariety k ((frobeniusTwist (Spec (.of k)) p hS).obj (Over.mk pX)).hom :=
      isVariety_frobeniusTwist_of_isReduced pX p hred
    degreeOver (relativeFrobenius (Spec (.of k)) p hS (Over.mk pX)).left = p ^ d
```

**`AlgebraicGeometry.relativeFrobenius_isDominant`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L117). The attribute's comment: “finite\_dominant”.

> The relative Frobenius is dominant over a base of prime characteristic.

```lean
instance relativeFrobenius_isDominant (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (X : Over S) :
    IsDominant (relativeFrobenius S p hS X).left
```

**`AlgebraicGeometry.isVariety_frobeniusTwist_of_isReduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L125). The attribute's comment: “twist\_variety”.

> A reduced Frobenius twist of a variety over a field is a variety.

```lean
theorem isVariety_frobeniusTwist_of_isReduced
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [IsVariety k f] (p : ℕ) [Fact p.Prime] [CharP k p] :
    let hchar : IsInCharacteristic (Spec (.of k)) p := by
      let φ : k →+* Γ(Spec (.of k), ⊤) := (Scheme.ΓSpecIso (.of k)).inv.hom
      change (p : Γ(Spec (.of k), ⊤)) = 0
      rw [← map_natCast φ, CharP.cast_eq_zero k p]
      exact map_zero φ
    IsReduced (((frobeniusTwist (Spec (.of k)) p hchar).obj (Over.mk f)).left) →
      IsVariety k (((frobeniusTwist (Spec (.of k)) p hchar).obj (Over.mk f)).hom)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.relativeFrobenius_isFinite`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L106), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/RelativeUniversalHomeomorphism.lean#L113) (StacksFrontier): “finite\_dominant”.

## Tag 0CCG, a remark

[Tag 0CCG](https://stacks.math.columbia.edu/tag/0CCG) in the Stacks Project.

**`AlgebraicGeometry.nFoldFrobeniusTwist`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean#L75). The attribute's comment: “n\_fold\_frobenius\_twist”. References: SGA 3 VIIA (4.1), “X^\{(p/S)} for S-schemes”; SGA 3 VIIA (4.1.3), “special case”; SGA 3 VIIA (4.3.1); SGA 3 VIIB (4.1.1), “more general”; SGA 3 XVII (4.3.2), “Notation X^(p^n)”.

> The `n`-fold Frobenius twist of an `S`-scheme is its base change along the `n`-fold absolute
> Frobenius of `S`, regarded as an `S`-scheme via the second projection.

```lean
public noncomputable abbrev nFoldFrobeniusTwist (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (n : ℕ) (X : Over S) : Over S
```

**`AlgebraicGeometry.nFoldRelativeFrobenius`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean#L89). The attribute's comment: “n\_fold\_relative\_frobenius”. References: SGA 3 VIIA (4.1), “Fr(X/S) for S-schemes”; SGA 3 VIIA (4.1.3), “special case”; SGA 5 XII (7.3), “more general”; SGA 5 XV (1.Definition3), “more general”.

> The morphism from an `S`-scheme to its `n`-fold Frobenius twist, with components the `n`-fold
> absolute Frobenius and the structure morphism.

```lean
public noncomputable def nFoldRelativeFrobenius (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (n : ℕ) (X : Over S) :
    X ⟶ nFoldFrobeniusTwist S p hS n X
```

**`AlgebraicGeometry.nFoldRelativeFrobenius_eq_successiveRelativeFrobenius`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean#L311). The attribute's comment: “successive\_composition”.

> The `(n+1)`-fold relative Frobenius is the composite of the relative Frobenius morphisms of
> `X` and its first `n` successive twists, under the canonical identifications.

```lean
public theorem nFoldRelativeFrobenius_eq_successiveRelativeFrobenius
    (S : Scheme.{u}) (p : ℕ)
    [Fact p.Prime] (hS : IsInCharacteristic S p) (n : ℕ) (X : Over S) :
    nFoldRelativeFrobenius S p hS (n + 1) X =
      successiveRelativeFrobenius S p hS X n
```

**`AlgebraicGeometry.relativeFrobenius_nFoldFrobeniusTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean#L356). The attribute's comment: “frobenius\_on\_twists”. References: SGA 3 VIIA (4.3.2), “more general”.

> Under the canonical identification of the two orders of Frobenius twisting, relative
> Frobenius on the `m`-fold twist is the `m`-fold base change of relative Frobenius on `X`.

```lean
public theorem relativeFrobenius_nFoldFrobeniusTwist (S : Scheme.{u}) (p : ℕ)
    [Fact p.Prime] (hS : IsInCharacteristic S p) (m : ℕ) (X : Over S) :
    (Over.pullback (absoluteFrobeniusPow S p hS m)).map
        (relativeFrobenius S p hS X) ≫
      (frobeniusTwistCommIso S p hS m X).hom =
        relativeFrobenius S p hS (nFoldFrobeniusTwist S p hS m X)
```

**`AlgebraicGeometry.nFoldRelativeFrobenius_eq_twistedRelativeFrobeniusComposite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean#L439). The attribute's comment: “twisted\_composition”.

> The `(n+1)`-fold relative Frobenius is the composite of the first `n+1` Frobenius base
> changes of the relative Frobenius of `X`.

```lean
public theorem nFoldRelativeFrobenius_eq_twistedRelativeFrobeniusComposite
    (S : Scheme.{u}) (p : ℕ) [Fact p.Prime]
    (hS : IsInCharacteristic S p) (n : ℕ) (X : Over S) :
    nFoldRelativeFrobenius S p hS (n + 1) X =
      twistedRelativeFrobeniusComposite S p hS X n
```

Declarations registered for the tag:

- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Frobenius/Iterated.lean#L79) (StacksFrontier): “twist\_functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.36, Tag 0CC6](https://stacks.math.columbia.edu/tag/0CC6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
