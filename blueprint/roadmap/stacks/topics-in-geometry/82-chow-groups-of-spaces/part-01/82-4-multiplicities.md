---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.geometricLength_eq_iff_forall_etaleChart, AlgebraicGeometry.Space.geometricLength_eq_iff_exists_etaleChart, AlgebraicGeometry.Space.geometricLength_eq_of_image_eq, AlgebraicGeometry.Space.length_etaleLocalRing_eq_length_chartLocalRing, AlgebraicGeometry.Space.tfae_hasLengthAt, AlgebraicGeometry.Space.geometricLength, AlgebraicGeometry.Space.HasLengthAt, AlgebraicGeometry.Space.geometricLength_chartDirectImage
statement: formalized
proof: formalized
---

# 82.4 Multiplicities

Section 82.4 of the Stacks Project, [Tag 0EE0](https://stacks.math.columbia.edu/tag/0EE0). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EE1, a lemma

[Tag 0EE1](https://stacks.math.columbia.edu/tag/0EE1) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricLength_eq_iff_forall_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricLengthPointIndependence.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricLengthPointIndependence.lean#L168). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 0EE1, conditions (1) and (3).** The length of a quasi-coherent `F` at a geometric
> point `x̄` is `d` exactly when the length of the Zariski stalk of `φ^* F` is `d` at the point of
> the chart under the chosen lift, for *every* small étale neighbourhood of `x̄` whose chart is a
> scheme.
>
> Every neighbourhood computes the same length
> (`AlgebraicGeometry.Space.geometricLength_eq_chartZariskiLength`), and there is one
> (`AlgebraicGeometry.Space.nonempty_smallEtaleNeighborhood`).

```lean
theorem geometricLength_eq_iff_forall_etaleChart {x : GeometricPoint B S hS X}
    (F : Modules.{u, u} B S hS X hX) [F.IsQuasicoherentOnSite] (d : ℕ∞) :
    geometricLength B S hS ⟨X, hX⟩ x F = d ↔
      ∀ V : SmallEtaleNeighborhood x,
        chartZariskiLength.{u, u} B S hS hX V.chart (chartPoint B S hS X V) F = d
```

**`AlgebraicGeometry.Space.geometricLength_eq_iff_exists_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricLengthPointIndependence.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricLengthPointIndependence.lean#L185). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0EE1, conditions (1) and (2).** The length of a quasi-coherent `F` at a geometric
> point `x̄` is `d` exactly when the length of the Zariski stalk of `φ^* F` is `d` at the point of
> the chart under the chosen lift, for *some* small étale neighbourhood of `x̄` whose chart is a
> scheme.
>
> Together with `AlgebraicGeometry.Space.geometricLength_eq_iff_forall_etaleChart` this is the
> exchange of quantifiers which Stacks 0EE1 asserts: the length agrees on some étale scheme
> chart exactly when it agrees on every one.

```lean
theorem geometricLength_eq_iff_exists_etaleChart {x : GeometricPoint B S hS X}
    (F : Modules.{u, u} B S hS X hX) [F.IsQuasicoherentOnSite] (d : ℕ∞) :
    geometricLength B S hS ⟨X, hX⟩ x F = d ↔
      ∃ V : SmallEtaleNeighborhood x,
        chartZariskiLength.{u, u} B S hS hX V.chart (chartPoint B S hS X V) F = d
```

**`AlgebraicGeometry.Space.geometricLength_eq_of_image_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricLengthPointIndependence.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricLengthPointIndependence.lean#L238). The attribute's comment: “independence of the chosen geometric point above a point of the space”.

> **Stacks 0EE1: the length at a geometric point does not depend on the geometric point.**
> Let `F` be a quasi-coherent `𝒪_X`-module and let `x̄` and `ȳ` be geometric points of `X` lying
> over the same point `x` of `|X|`.  Then `F` has the same length at `x̄` as at `ȳ`.  So the
> length of Stacks 0EE2 is a function of `x`, which is what makes that definition well posed.
>
> The two points are dominated by a common third
> (`AlgebraicGeometry.Space.GeometricPoint.exists_common_extension`), and the length is
> unchanged along a domination
> (`AlgebraicGeometry.Space.geometricLength_eq_of_dominates`).

```lean
theorem geometricLength_eq_of_image_eq (x y : GeometricPoint B S hS X)
    (h : x.image = y.image) (F : Modules.{u, u} B S hS X hX)
    [F.IsQuasicoherentOnSite] :
    geometricLength B S hS ⟨X, hX⟩ x F = geometricLength B S hS ⟨X, hX⟩ y F
```

**`AlgebraicGeometry.Space.length_etaleLocalRing_eq_length_chartLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkLength.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricStalkLength.lean#L93). The attribute's comment: “the structure sheaf: lengths agree on an étale scheme chart”.

> **Stacks 0EE1 for the structure sheaf.** The étale local ring of an algebraic space at a
> geometric point has the same length as the local ring of any étale scheme chart at a point over
> it. Since the chart is arbitrary, the two readings of Stacks 0EE1 — some chart and every chart —
> agree, and the common value is the length of `𝒪_{X, x̄}`.
>
> This is the case `N = 𝒪_{U, u}` of
> `AlgebraicGeometry.Space.length_chartStalkBaseChange_obj`, the base change
> `𝒪_{X, x̄} ⊗_{𝒪_{U, u}} 𝒪_{U, u}` being `𝒪_{X, x̄}`.

```lean
theorem length_etaleLocalRing_eq_length_chartLocalRing {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) :
    Module.length ↥(etaleLocalRing B S hS X x) ↥(etaleLocalRing B S hS X x) =
      Module.length ↥(chartLocalRing B S hS X V) ↥(chartLocalRing B S hS X V)
```

**`AlgebraicGeometry.Space.tfae_hasLengthAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LengthAtPoint.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LengthAtPoint.lean#L200).

> **Stacks 0EE1 at a point `x` of `|X|`: conditions (1), (2) and (3) are equivalent.** For a
> quasi-coherent `𝒪_X`-module `F`, a point `x ∈ |X|` and `d ∈ ℕ∞`, the following are
> equivalent:
>
> 1. `length_{𝒪_{X, x̄}} F_{x̄} = d` for a geometric point `x̄` above `x`;
> 2. for some étale morphism `U → X` with `U` a scheme and `u ∈ U` mapping to `x`,
>    `length_{𝒪_{U, u}} (F|_U)_u = d`;
> 3. for every étale morphism `U → X` with `U` a scheme and `u ∈ U` mapping to `x`,
>    `length_{𝒪_{U, u}} (F|_U)_u = d`.
>
> Condition (1) is `AlgebraicGeometry.Space.HasLengthAt` by definition, so this is the
> statement that `AlgebraicGeometry.Space.HasLengthAt` is "the equivalent conditions of
> Lemma 0EE1", as Stacks 0EE2 has it. Together with
> `AlgebraicGeometry.Space.geometricLength_eq_of_image_eq` (condition (1) does not depend on the
> geometric point chosen above `x`) this is the whole of Stacks 0EE1.

```lean
theorem tfae_hasLengthAt (F : Modules.{u, u} B S hS X hX) [F.IsQuasicoherentOnSite]
    (x : points B S hS X) (d : ℕ∞) :
    List.TFAE
      [∃ xbar : GeometricPoint B S hS X,
          xbar.LiesOver x ∧ geometricLength B S hS ⟨X, hX⟩ xbar F = d,
        ∃ (W : SmallEtale B S hS X) (u : chartScheme W), chartSchemeToPoints B S hS X W u = x ∧
          Module.length ((chartScheme W).presheaf.stalk u)
            (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
              (restrictToChart B S hS hX F W).val.presheaf u) = d,
        ∀ (W : SmallEtale B S hS X) (u : chartScheme W), chartSchemeToPoints B S hS X W u = x →
          Module.length ((chartScheme W).presheaf.stalk u)
            (TopCat.Presheaf.stalk (C := AddCommGrpCat.{u})
              (restrictToChart B S hS hX F W).val.presheaf u) = d]
```

## Tag 0EE2, a definition

[Tag 0EE2](https://stacks.math.columbia.edu/tag/0EE2) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricLength`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricLength.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricLength.lean#L98). The attribute's comment: “at a geometric point; no declaration packages a chosen geometric point above a point of `|X|` together with the independence of Lemma 0EE1 (`AlgebraicGeometry.Space.geometricLength_eq_of_image_eq`) into the definition at a point of `|X|`”.

> **The length of an `𝒪_X`-module at a geometric point.** For an algebraic space `X` over a
> scheme `S`, a geometric point `x̄` of `X` and an `𝒪_X`-module `F`, this is the length of the
> stalk `F_{x̄}` of Stacks 05VQ as a module over the étale local ring `𝒪_{X, x̄}` of
> Stacks 04KG, a value in `ℕ∞ = {0, 1, 2, …, ∞}`.
>
> This is the quantity of condition (1) of Stacks 0EE1; Stacks 0EE2 defines "`F` has length `d`
> at a point `x` of `|X|`" to mean that this value is `d` for a geometric point above `x`, which
> by Stacks 0EE1 does not depend on the choice — proved, for a quasi-coherent `F`, as
> `AlgebraicGeometry.Space.geometricLength_eq_of_image_eq` in
> `GeometricLengthPointIndependence.lean`.

```lean
def geometricLength (X : AlgebraicSpaces B S hS) (x : GeometricPoint B S hS X.1)
    (F : Modules.{u, m} B S hS X.1 X.2) : ℕ∞
```

**`AlgebraicGeometry.Space.HasLengthAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LengthAtPoint.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LengthAtPoint.lean#L102).

> **Stacks 0EE2: `F` has length `d` at `x`.** For a quasi-coherent `𝒪_X`-module `F`, a point
> `x` of `|X|` and `d ∈ ℕ∞`, this says that the stalk `F_{x̄}` has length `d` over the étale local
> ring `𝒪_{X, x̄}` for a geometric point `x̄` of `X` lying over `x`.
>
> Stacks 0EE2 defines this as the equivalent conditions of Stacks 0EE1; the definition uses
> condition (1), which by that lemma does not depend on the choice of `x̄`
> (`AlgebraicGeometry.Space.geometricLength_eq_of_image_eq`, so the condition holds for some
> `x̄` above `x` iff for every one: `AlgebraicGeometry.Space.hasLengthAt_iff_forall_geometricPoint`)
> and is equivalent to conditions (2) and (3), the length of `(F|_U)_u` over `𝒪_{U, u}` for some,
> respectively every, étale `U → X` from a scheme and `u ∈ U` over `x`
> (`AlgebraicGeometry.Space.tfae_hasLengthAt`).

```lean
def HasLengthAt (F : Modules.{u, u} B S hS X hX) [F.IsQuasicoherentOnSite]
    (x : points B S hS X) (d : ℕ∞) : Prop
```

## Tag 0EE3, a lemma

[Tag 0EE3](https://stacks.math.columbia.edu/tag/0EE3) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricLength_chartDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionGeometricLength.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionGeometricLength.lean#L450). The attribute's comment: “at a geometric point of the source, and for the direct image of modules along base change of étale scheme charts; the form at a point of the space is `AlgebraicGeometry.Space.lengthAtPoint_chartDirectImage_iff` of `StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionLengthAtPoint.lean`”.

> **Stacks 0EE3 for algebraic spaces, at a geometric point.** Let `f : X ⟶ Y` be a closed
> immersion of algebraic spaces over a scheme `S`, let `G` be an `𝒪_X`-module and let `x̄` be a
> geometric point of `X`. Then `f_*G` has the same length at `f(x̄)` as `G` has at `x̄`.
>
> The germ map `𝒪_{Y, f(x̄)} → 𝒪_{X, x̄}` of a closed immersion is surjective
> (`AlgebraicGeometry.Space.surjective_etaleLocalRingMap_of_isClosedImmersion`) and the stalk of
> `f_*G` at `f(x̄)` is the stalk of `G` at `x̄` semilinearly over it
> (`AlgebraicGeometry.Space.geometricStalkPushforwardAddEquiv`), so
> `AlgebraicGeometry.Space.geometricLength_eq_of_surjective_of_addEquiv` applies: restriction of
> scalars along a surjection does not change the lattice of submodules, hence not its length.
>
> No quasi-coherence of `G` is assumed. The direct image is the one along base change of étale
> scheme charts; see the implementation notes of this file.

```lean
theorem geometricLength_chartDirectImage (f : X ⟶ Y) (hf : IsClosedImmersion B S hS f.hom)
    (x : GeometricPoint B S hS X.1) (G : Modules.{u, m} B S hS X.1 X.2) :
    geometricLength B S hS Y (geometricPointMap f.hom x)
        ((smallBaseChangeModulePushforward B S hS f hf.rep).obj G) =
      geometricLength B S hS X x G
```

**`AlgebraicGeometry.Space.geometricLength_chartDirectImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionGeometricLength.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionGeometricLength.lean#L470). The attribute's comment: “at a geometric point of the source, and for the direct image of modules along base change of étale scheme charts; the form at a point of the space is `AlgebraicGeometry.Space.lengthAtPoint_chartDirectImage_iff` of `StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionLengthAtPoint.lean`”.

> **Stacks 0EE3 for algebraic spaces, at a geometric point**, in the iff form of the source:
> for every `d` in `ℕ∞ = {0, 1, 2, …, ∞}`, the module `G` has length `d` at the geometric
> point `x̄` of `X` exactly when `f_*G` has length `d` at `f(x̄)`.
>
> This is `AlgebraicGeometry.Space.geometricLength_chartDirectImage` read as an equivalence.

```lean
theorem geometricLength_chartDirectImage_iff (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) (x : GeometricPoint B S hS X.1)
    (G : Modules.{u, m} B S hS X.1 X.2) (d : ℕ∞) :
    geometricLength B S hS X x G = d ↔
      geometricLength B S hS Y (geometricPointMap f.hom x)
        ((smallBaseChangeModulePushforward B S hS f hf.rep).obj G) = d
```

**`AlgebraicGeometry.Space.lengthAtPoint_chartDirectImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionLengthAtPoint.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionLengthAtPoint.lean#L226). The attribute's comment: “at a point of the space, for the direct image of modules along base change of étale scheme charts”.

> **Stacks 0EE3 at a point of the space.** Let `f : X ⟶ Y` be a closed immersion of algebraic
> spaces over a scheme `S`, let `G` be a quasi-coherent `𝒪_X`-module, let `p` be a point of `|X|`
> with image `f(p)` in `|Y|` and let `d` be an element of `ℕ∞ = {0, 1, 2, …, ∞}`. Then `G` has
> length `d` at `p` if and only if `f_*G` has length `d` at `f(p)`.
>
> "Has length `d` at a point" is the condition of Stacks 0EE2: the length of the module at that
> point of the space, `AlgebraicGeometry.Space.lengthAtPoint`, is `d`. Both sides are therefore
> `= d` for one and the same number, by
> `AlgebraicGeometry.Space.lengthAtPoint_chartDirectImage`.

```lean
theorem lengthAtPoint_chartDirectImage_iff (f : X ⟶ Y)
    (hf : IsClosedImmersion B S hS f.hom) (G : Modules.{u, u} B S hS X.1 X.2)
    [G.IsQuasicoherentOnSite] (p : points B S hS X.1) (d : ℕ∞) :
    lengthAtPoint B S hS X p G = d ↔
      lengthAtPoint B S hS Y (pointsMap B S hS X.1 f.hom p)
        (chartDirectImage B S hS f hf G) = d
```

**`Stacks.ClosedImmersion.length_stalkObj_pushforward_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/StalkLength.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/ClosedImmersion/StalkLength.lean#L186). The attribute's comment: “for a closed immersion of schemes”.

> **Stacks 0EE3 for a closed immersion of schemes**, in the form the source states: for
> `d ∈ {0, 1, 2, …, ∞}`, the module `G` has length `d` at `z` if and only if `i_* G` has length
> `d` at the image `i(z)`.
>
> Both sides are read off `Stacks.ClosedImmersion.length_stalkObj_pushforward`, which says the
> two lengths are equal.

```lean
theorem length_stalkObj_pushforward_eq_iff {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] (G : Z.Modules) (z : Z) (d : ℕ∞) :
    Module.length (TopCat.Presheaf.stalk (C := RingCat.{u}) Z.ringCatSheaf.obj z)
          (SheafOfModules.stalkObj Z.ringCatSheaf z G) = d ↔
      Module.length (TopCat.Presheaf.stalk (C := RingCat.{u}) X.ringCatSheaf.obj (i.base z))
          (SheafOfModules.stalkObj X.ringCatSheaf (i.base z)
            ((Scheme.Modules.pushforward i).obj G)) = d
```

## Tag 0EE4, a lemma

[Tag 0EE4](https://stacks.math.columbia.edu/tag/0EE4) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_iff_isAbsolutelyQuasiSeparated_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicityAtPoint.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicityAtPoint.lean#L126). The attribute's comment: “decent iff quasi-separated”.

> **The parenthetical of Stacks 0EE4.**  A locally Noetherian algebraic space over `S` is
> decent if and only if it is quasi-separated.
>
> Decency of a quasi-separated algebraic space is the chain of conditions of Stacks 03JX and needs
> no finiteness hypothesis; quasi-separatedness of a locally Noetherian decent algebraic space is
> Stacks 0BB6.

```lean
theorem isDecentSpace_iff_isAbsolutelyQuasiSeparated_of_isLocallyNoetherian
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hNoeth : HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsLocallyNoetherian Y)) :
    IsDecentSpace B S hS X ↔ IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X
```

**`AlgebraicGeometry.Space.tfae_isGenericPoint_supp_restrictToChart_geometricLength`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicityAtPoint.lean, line 325](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicityAtPoint.lean#L325). The attribute's comment: “conditions (1), (2) and (3)”.

> **Stacks 0EE4, conditions (1), (2) and (3).**  Let `X` be a locally Noetherian algebraic
> space over `S`, let `F` be a coherent `𝒪_X`-module and let `x ∈ |X|`.  The following are
> equivalent:
>
> 1. for some étale morphism `U → X` with `U` a scheme and some `u ∈ U` mapping to `x`, the point
>    `u` is a generic point of an irreducible component of `Supp(F|_U)`;
> 2. for every étale morphism `U → X` with `U` a scheme and every `u ∈ U` mapping to `x`, the
>    point `u` is a generic point of an irreducible component of `Supp(F|_U)`;
> 3. the length of `F` at `x` is finite and nonzero.
>
> The étale morphisms from schemes are the étale scheme charts `W` of `X`, and `u` maps to `x`
> when `AlgebraicGeometry.Space.chartSchemeToPoints` sends it to `x`.  The length of `F` at `x`
> is the length of Stacks 0EE2: the length at a geometric point above `x`, which by Stacks 0EE1
> (`AlgebraicGeometry.Space.geometricLength_eq_of_image_eq`) does not depend on the geometric
> point; condition (3) is stated at every geometric point above `x`.
>
> Each chart point above `x` satisfies the chart condition exactly when the length is finite and
> nonzero (`AlgebraicGeometry.Space.exists_isGenericPoint_supp_restrictToChart_iff_geometricLength`),
> and a chart point above `x` exists.

```lean
theorem tfae_isGenericPoint_supp_restrictToChart_geometricLength
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) [IsCoherent B S hS X.1 X.2 F]
    (x : points B S hS X.1) :
    List.TFAE
      [∃ (W : SmallEtale B S hS X.1) (u : chartScheme W),
          chartSchemeToPoints B S hS X.1 W u = x ∧
            ∃ Z : irreducibleComponents
                (SheafOfModules.supp (restrictToChart B S hS X.2 F W) : Set (chartScheme W)),
              IsGenericPoint u (Subtype.val '' Z.1),
        ∀ (W : SmallEtale B S hS X.1) (u : chartScheme W),
          chartSchemeToPoints B S hS X.1 W u = x →
            ∃ Z : irreducibleComponents
                (SheafOfModules.supp (restrictToChart B S hS X.2 F W) : Set (chartScheme W)),
              IsGenericPoint u (Subtype.val '' Z.1),
        ∀ xbar : GeometricPoint B S hS X.1, xbar.LiesOver x →
          geometricLength B S hS X xbar F ≠ ⊤ ∧ 0 < geometricLength B S hS X xbar F]
```

**`AlgebraicGeometry.Space.tfae_isGenericPoint_supportOfSheaf_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicityAtPoint.lean, line 451](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MultiplicityAtPoint.lean#L451). The attribute's comment: “conditions (1) to (4), for a decent space”.

> **Stacks 0EE4, conditions (1) to (4), for a decent space.**  Let `X` be a locally Noetherian
> algebraic space over `S` which is decent (equivalently, by
> `AlgebraicGeometry.Space.isDecentSpace_iff_isAbsolutelyQuasiSeparated_of_isLocallyNoetherian`,
> quasi-separated), let `F` be a coherent `𝒪_X`-module and let `x ∈ |X|`.  The three conditions of
> `AlgebraicGeometry.Space.tfae_isGenericPoint_supp_restrictToChart_geometricLength` are also
> equivalent to
>
> 4. `x` is a generic point of an irreducible component of `Supp(F)`.
>
> The support of `F` is the support of Stacks 04KA of its underlying sheaf of abelian groups
> (`AlgebraicGeometry.Space.supportOfSheaf`).  Condition (4) is equivalent to the chart condition
> at every chart point above `x`
> (`AlgebraicGeometry.Space.exists_isGenericPoint_supp_restrictToChart_iff_supportOfSheaf`).

```lean
theorem tfae_isGenericPoint_supportOfSheaf_of_isDecentSpace
    (hLN : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hdec : IsDecentSpace B S hS X.1) (F : Modules.{u, u} B S hS X.1 X.2)
    [IsCoherent B S hS X.1 X.2 F] (x : points B S hS X.1) :
    List.TFAE
      [∃ (W : SmallEtale B S hS X.1) (u : chartScheme W),
          chartSchemeToPoints B S hS X.1 W u = x ∧
            ∃ Z : irreducibleComponents
                (SheafOfModules.supp (restrictToChart B S hS X.2 F W) : Set (chartScheme W)),
              IsGenericPoint u (Subtype.val '' Z.1),
        ∀ (W : SmallEtale B S hS X.1) (u : chartScheme W),
          chartSchemeToPoints B S hS X.1 W u = x →
            ∃ Z : irreducibleComponents
                (SheafOfModules.supp (restrictToChart B S hS X.2 F W) : Set (chartScheme W)),
              IsGenericPoint u (Subtype.val '' Z.1),
        ∀ xbar : GeometricPoint B S hS X.1, xbar.LiesOver x →
          geometricLength B S hS X xbar F ≠ ⊤ ∧ 0 < geometricLength B S hS X xbar F,
        ∃ Z : irreducibleComponents
            (supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F)),
          IsGenericPoint x (Subtype.val '' Z.1)]
```

## Tag 0EE6, a lemma

[Tag 0EE6](https://stacks.math.columbia.edu/tag/0EE6) in the Stacks Project.

**`AlgebraicGeometry.Space.isGenericPoint_of_deltaDimensionClosed_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/MaximalDeltaDimension.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/MaximalDeltaDimension.lean#L60).

> **Stacks 0EE6.** A point of a closed set of points at which the induced dimension function
> attains the delta-dimension bound is a generic point of an irreducible component of that set.

```lean
theorem isGenericPoint_of_deltaDimensionClosed_le (f : X ⟶ D.space) (hf : D.IsGood f)
    (T : Set (points D.site D.base D.base_mem X)) (hT : IsClosed T)
    (t : points D.site D.base D.base_mem X) (ht : t ∈ T) (k : ℤ)
    (hbound : deltaDimensionClosed D f hf T hT ≤ (k : EInt))
    (hdim : inducedDimensionValue D.site D.base D.base_mem D.delta f t = k) :
    ∃ Z : irreducibleComponents T, IsGenericPoint (⟨t, ht⟩ : T) Z.1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.4, Tag 0EE0](https://stacks.math.columbia.edu/tag/0EE0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
