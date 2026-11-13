---
declaration: section
origin: cited
lean: AlgebraicGeometry.curvePushoutSituation, AlgebraicGeometry.exists_pushout_of_curve, AlgebraicGeometry.exists_curvePushoutCompletedLocalRing_isPullback
statement: formalized
proof: formalized
---

# 53.14 Pushouts

Section 53.14 of the Stacks Project, [Tag 0E35](https://stacks.math.columbia.edu/tag/0E35). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E35, the section

[Tag 0E35](https://stacks.math.columbia.edu/tag/0E35) in the Stacks Project.

**`AlgebraicGeometry.curvePushoutSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/Pushout.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/Pushout.lean#L101). The attribute's comment: “the verification that the assumptions of More on Morphisms, Proposition 0E25 are satisfied; the conclusions (1)-(7) are `AlgebraicGeometry.exists_pushout_of_curve`”.

> **Stacks Project, Tag 0E35.** The four conditions of the section — `X` separated of finite
> type over the field `k` of dimension `≤ 1`, `i` a closed immersion, `Z` and `Y` finite over
> `Spec k`, and `j` surjective — put the diagram in the standing situation of
> [Stacks Project, Tag 0ECI], so that the pushout `Y ⨿_Z X` of [Stacks Project, Tag 0E25] and
> everything derived from it apply.
>
> The content is the verification of the two assumptions of [Stacks Project, Tag 0ECI] that are not
> hypotheses here: that `j` is integral, and that every fibre of `j` maps under `i` into a single
> affine open of `X`.  The latter is [Stacks Project, Tag 09NN].

```lean
def curvePushoutSituation
    (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k)) (pZ : Z ⟶ Spec (.of k))
    (i : Z ⟶ X) (j : Z ⟶ Y) (hi : i ≫ pX = pZ) (hj : j ≫ pY = pZ)
    [IsSeparated pX] [LocallyOfFiniteType pX] (hdim : topologicalKrullDim X ≤ 1)
    [IsClosedImmersion i] [IsFinite pY] [IsFinite pZ] [Surjective j] :
    PushoutAlongClosedImmersionAndIntegralSituation.{u}
```

**`AlgebraicGeometry.exists_pushout_of_curve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PushoutProperties.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PushoutProperties.lean#L126).

> **Stacks Project, Tag 0E35.** Let `k` be a field, `X` separated of finite type over `k` of
> dimension `≤ 1`, `i : Z ⟶ X` a closed immersion, `Z` and `Y` finite over `Spec k` and
> `j : Z ⟶ Y` surjective, all over `k`.  Then every finite set of points of `X` lies in an affine
> open, and there is a scheme `P` over `k` with maps `a : X ⟶ P`, `b : Y ⟶ P` over `k` such that
>
> 1. the square `i, j, a, b` is a pushout in the category of schemes;
> 2. `b` is a closed immersion;
> 3. `a` is integral and surjective;
> 4. `P` is separated over `k`;
> 5. `P` is of finite type (locally of finite type and quasi-compact) over `k`;
> 6. `a` is finite;
> 7. if `X` is proper over `k`, then so is `P`.
>
> The pushout is the one of [Stacks Project, Tag 0E25] for the situation
> `AlgebraicGeometry.curvePushoutSituation`; (2) and the integrality in (3) are part of 0E25,
> (4) is [Stacks Project, Tag 0E26] and the local finite type in (5) is
> [Stacks Project, Tag 0E27].

```lean
theorem exists_pushout_of_curve
    (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k)) (pZ : Z ⟶ Spec (.of k))
    (i : Z ⟶ X) (j : Z ⟶ Y) (hi : i ≫ pX = pZ) (hj : j ≫ pY = pZ)
    [IsSeparated pX] [LocallyOfFiniteType pX] [QuasiCompact pX]
    (hdim : topologicalKrullDim X ≤ 1)
    [IsClosedImmersion i] [IsFinite pY] [IsFinite pZ] [Surjective j] :
    (∀ F : Finset X, ∃ U : X.Opens, IsAffineOpen U ∧ ∀ x ∈ F, x ∈ U) ∧
    ∃ (P : Scheme.{u}) (a : X ⟶ P) (b : Y ⟶ P) (pP : P ⟶ Spec (.of k)),
      IsPushout i j a b ∧ a ≫ pP = pX ∧ b ≫ pP = pY ∧
      IsClosedImmersion b ∧ (IsIntegralHom a ∧ Surjective a) ∧
      IsSeparated pP ∧ (LocallyOfFiniteType pP ∧ QuasiCompact pP) ∧ IsFinite a ∧
      (IsProper pX → IsProper pP)
```

## Tag 0E36, a lemma

[Tag 0E36](https://stacks.math.columbia.edu/tag/0E36) in the Stacks Project.

**`AlgebraicGeometry.exists_curvePushoutCompletedLocalRing_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/PushoutCompletedLocalRing.lean, line 1280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/PushoutCompletedLocalRing.lean#L1280).

> **Stacks Project, Tag 0E36.**  Stated in the situation of [Stacks Project, Tag 0E35] itself:
> `k` is a field, `X` is separated of finite type over `k` of dimension `≤ 1`, `i : Z ⟶ X` is a
> closed immersion, `Z` and `Y` are finite over `Spec k` and `j : Z ⟶ Y` is surjective.  Let `Y` be
> the spectrum of a field `k'` and `Z` the spectrum of a product of finite extensions `k'_i/k'`,
> let `x` be the image of `Y` in the pushout `Y ⨿_Z X` and `x'_i` the image of `Spec (k'_i)` in `X`.
> Then the completed local ring at `x` is the fibre product of the product of the completed local
> rings at the `x'_i` and the field `k'` over the product of the `k'_i`, the horizontal maps being
> the maps to the residue fields.
>
> The equations following the pullback assertion pin down the four maps in the diagram.
>
> Against the notation of [Stacks Project, Tag 0E35] the translation is `Z = Z'`, `X = X'` and
> `Y = Z`, following the library's `PushoutAlongClosedImmersionAndIntegralSituation`.  The standing
> situation of [Stacks Project, Tag 0ECI] is *derived* from the four conditions here, by
> `curvePushoutSituation` ([Stacks Project, Tag 0E35]), rather than assumed; the locally Noetherian
> hypothesis of `exists_pushoutCompletedLocalRing_isPullback` is discharged along the way through
> [Stacks Project, Tag 0E27].

```lean
public theorem exists_curvePushoutCompletedLocalRing_isPullback
    (k : Type u) [Field k] {X Y Z : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k)) (pZ : Z ⟶ Spec (.of k))
    (i : Z ⟶ X) (j : Z ⟶ Y) (hi : i ≫ pX = pZ) (hj : j ≫ pY = pZ)
    [IsSeparated pX] [LocallyOfFiniteType pX] (hdim : topologicalKrullDim X ≤ 1)
    [IsClosedImmersion i] [IsFinite pY] [IsFinite pZ] [Surjective j]
    (n : ℕ) (k' : Type u) (k'_i : Fin n → Type u)
    [Field k'] [∀ a, Field (k'_i a)]
    [∀ a, Algebra k' (k'_i a)] [∀ a, Module.Finite k' (k'_i a)]
    (eZ : Z ≅ Spec (.of (∀ a, k'_i a)))
    (eY : Y ≅ Spec (.of k'))
    (hjeq : j = eZ.hom ≫
      Spec.map (CommRingCat.ofHom (RingHom.pi fun a ↦ algebraMap k' (k'_i a))) ≫ eY.inv) :
    let s : PushoutAlongClosedImmersionAndIntegralSituation.{u} :=
      curvePushoutSituation k pX pY pZ i j hi hj hdim
    let y : Y := eY.inv (closedPoint k')
    let specPoint : ∀ a, Spec (.of (k'_i a)) ⟶ Z := fun a ↦
      Spec.map (CommRingCat.ofHom (Pi.evalRingHom k'_i a)) ≫ eZ.inv
    let z : Fin n → Z := fun a ↦ specPoint a (closedPoint (k'_i a))
    let x : pushoutScheme s := pushoutInr s y
    let x' : Fin n → X := fun a ↦ i (z a)
    ∃ (hx : ∀ a, pushoutInl s (x' a) = x)
      (completionMap : Scheme.completedLocalRing (pushoutScheme s) x →+*
        (∀ a, Scheme.completedLocalRing X (x' a)))
      (bottomResidueMap : Scheme.completedLocalRing (pushoutScheme s) x →+* k')
      (componentResidueMap : ∀ a, Scheme.completedLocalRing X (x' a) →+* k'_i a),
      let topResidueMap : (∀ a, Scheme.completedLocalRing X (x' a)) →+* (∀ a, k'_i a) :=
        RingHom.pi fun a ↦ (componentResidueMap a).comp (Pi.evalRingHom _ a)
      (∀ a, ((Pi.evalRingHom _ a).comp completionMap).comp
          (algebraMap ((pushoutScheme s).presheaf.stalk x)
            (Scheme.completedLocalRing (pushoutScheme s) x)) =
        (algebraMap (X.presheaf.stalk (x' a)) (Scheme.completedLocalRing X (x' a))).comp
          ((eqToHom (congrArg (fun p ↦ (pushoutScheme s).presheaf.stalk p)
            (hx a).symm) ≫ (pushoutInl s).stalkMap (x' a)).hom)) ∧
      (bottomResidueMap.comp
          (algebraMap ((pushoutScheme s).presheaf.stalk x)
            (Scheme.completedLocalRing (pushoutScheme s) x)) =
        (Scheme.stalkClosedPointTo (eY.inv ≫ pushoutInr s)).hom) ∧
      (∀ a, (componentResidueMap a).comp
          (algebraMap (X.presheaf.stalk (x' a))
            (Scheme.completedLocalRing X (x' a))) =
        (Scheme.stalkClosedPointTo (specPoint a ≫ i)).hom) ∧
      IsPullback
        (CommRingCat.ofHom bottomResidueMap)
        (CommRingCat.ofHom completionMap)
        (CommRingCat.ofHom (RingHom.pi fun a ↦ algebraMap k' (k'_i a)))
        (CommRingCat.ofHom topResidueMap)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.14, Tag 0E35](https://stacks.math.columbia.edu/tag/0E35)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
