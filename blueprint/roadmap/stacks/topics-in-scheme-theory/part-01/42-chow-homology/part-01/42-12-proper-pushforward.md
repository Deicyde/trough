---
declaration: section
origin: cited
lean: Stacks.Chow.properPushforward, Stacks.Chow.properPushforward_apply, Stacks.Chow.properPushforward_single, Stacks.Chow.properPushforward_comp, Stacks.Chow.exact_intersectionToSummands_summandsToUnion, Stacks.Chow.surjective_summandsToUnion, Stacks.Chow.properPushforward_cycleAssociatedToCoherentSheaf, Stacks.Chow.properPushforward_cycleAssociatedToClosedSubscheme
statement: formalized
proof: formalized
---

# 42.12 Proper pushforward

Section 42.12 of the Stacks Project, [Tag 02R3](https://stacks.math.columbia.edu/tag/02R3). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02R4, a definition

[Tag 02R4](https://stacks.math.columbia.edu/tag/02R4) in the Stacks Project.

**`Stacks.Chow.properPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L286). The attribute's comment: “pushforward of cycles”.

> Proper pushforward of cycles of delta-dimension `k`.

```lean
def properPushforward (C : ChowSituation.{u}) {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f]
    (hf : f ≫ sY = sX) (k : ℤ) : CycleGroup C sX k → CycleGroup C sY k
```

**`Stacks.Chow.properPushforward_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L297). The attribute's comment: “coefficient formula”.

> The coefficient of the proper pushforward at a point is the locally finite sum of the
> coefficients above it, weighted by their residue-field degrees when the delta-dimension is
> preserved.

```lean
theorem properPushforward_apply (C : ChowSituation.{u}) {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f]
    (hf : f ≫ sY = sX) (k : ℤ) (c : CycleGroup C sX k) (y : Y) :
    (properPushforward C sX sY f hf k c).1 y =
      ∑ᶠ x ∈ f.base ⁻¹' {y}, c.1 x *
        (if relativeDimension C.dimensionFunction sX x =
            relativeDimension C.dimensionFunction sY (f.base x)
          then (f.residueDegree x : ℤ) else 0)
```

**`Stacks.Chow.properPushforward_single`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Vocabulary.lean#L340). The attribute's comment: “pushforward of an integral component”.

> An integral closed subscheme maps to its image with multiplicity the degree of the
> function-field extension if its delta-dimension is preserved, and to zero otherwise.

```lean
theorem properPushforward_single (C : ChowSituation.{u}) {X Y : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f]
    (hf : f ≫ sY = sX) (k : ℤ) (x : X) (c : CycleGroup C sX k)
    (hc : c.1 = @Function.locallyFinsuppWithin.single X _ ℤ (Classical.decEq X) _ x (1 : ℤ)) :
    (properPushforward C sX sY f hf k c).1 =
      if relativeDimension C.dimensionFunction sY (f.base x) = k then
        @Function.locallyFinsuppWithin.single Y _ ℤ (Classical.decEq Y) _
          (f.base x) (f.residueDegree x : ℤ)
      else 0
```

## Tag 02R5, a lemma

[Tag 02R5](https://stacks.math.columbia.edu/tag/02R5) in the Stacks Project.

**`Stacks.Chow.properPushforward_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardChow/Functoriality.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardChow/Functoriality.lean#L268).

> **Stacks 02R5.** Proper pushforward of `k`-cycles is functorial: pushing forward along
> `f : X ⟶ Y` and then along `g : Y ⟶ Z` is pushing forward along the composite.

```lean
theorem properPushforward_comp (C : ChowSituation.{u}) {X Y Z : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (sZ : Z ⟶ C.S)
    [LocallyOfFiniteType sZ] (f : X ⟶ Y) [IsProper f] (g : Y ⟶ Z) [IsProper g]
    (hf : f ≫ sY = sX) (hg : g ≫ sZ = sY) (k : ℤ) :
    properPushforward C sY sZ g hg k ∘ properPushforward C sX sY f hf k =
      properPushforward C sX sZ (f ≫ g) (by rw [Category.assoc, hg, hf]) k
```

## Tag 0F92, a lemma

[Tag 0F92](https://stacks.math.columbia.edu/tag/0F92) in the Stacks Project.

**`Stacks.Chow.exact_intersectionToSummands_summandsToUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/UnionOfClosedSubschemes.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/UnionOfClosedSubschemes.lean#L222). The attribute's comment: “exactness in the middle”.

> The sequence of a union of two closed subschemes is exact in the middle: a pair of
> `k`-cycles on the two closed subschemes has vanishing sum of pushforwards exactly when it comes
> from a `k`-cycle on the scheme-theoretic intersection.

```lean
theorem exact_intersectionToSummands_summandsToUnion :
    Function.Exact (intersectionToSummands C sX I J k) (summandsToUnion C sX I J k)
```

**`Stacks.Chow.surjective_summandsToUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/UnionOfClosedSubschemes.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/Degrees/UnionOfClosedSubschemes.lean#L234). The attribute's comment: “surjectivity”.

> If two closed subschemes cover the ambient scheme set-theoretically, every `k`-cycle on it is
> the sum of the pushforwards of a `k`-cycle on each of them.

```lean
theorem surjective_summandsToUnion (hcover : I.support ⊔ J.support = ⊤) :
    Function.Surjective (summandsToUnion C sX I J k)
```

## Tag 02R6, a lemma

[Tag 02R6](https://stacks.math.columbia.edu/tag/02R6) in the Stacks Project.

**`Stacks.Chow.properPushforward_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Basic.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Basic.lean#L196). The attribute's comment: “part (2)”.

> Let `f : X ⟶ Y` be a proper morphism of schemes locally of finite type over the base `S` of
> chapter 42, and let `F` be a coherent `𝒪_X`-module whose support has delta-dimension at most
> `k`, with `f_* F` coherent. Then proper pushforward of `k`-cycles carries the cycle of `F` to the
> cycle of the direct image: `f_* [F]_k = [f_* F]_k`.

```lean
theorem properPushforward_cycleAssociatedToCoherentSheaf (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f]
    (hf : f ≫ sY = sX) (F : X.Modules) [F.IsCoherent]
    [((Scheme.Modules.pushforward f).obj F).IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sX) ≤ (k : EInt)) :
    properPushforward C sX sY f hf k (cycleAssociatedToCoherentSheaf C sX F k hFk) =
      cycleAssociatedToCoherentSheaf C sY ((Scheme.Modules.pushforward f).obj F) k
        (schemeDeltaDimension_reducedSupport_pushforward_le C sX sY f hf F hFk)
```

**`Stacks.Chow.properPushforward_cycleAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Basic.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Basic.lean#L251). The attribute's comment: “part (1)”.

> Let `f : X ⟶ Y` be a proper morphism of schemes locally of finite type over the base `S` of
> chapter 42, and let `i : Z ⟶ X` be a closed subscheme with `dim_δ(Z) ≤ k`, with `f_* (i_* 𝒪_Z)`
> coherent. Then proper pushforward of `k`-cycles carries the cycle of `Z` to the cycle of the
> direct image of its structure sheaf: `f_* [Z]_k = [f_* 𝒪_Z]_k`, where `𝒪_Z` is read as the
> coherent `𝒪_X`-module `i_* 𝒪_Z`.

```lean
theorem properPushforward_cycleAssociatedToClosedSubscheme (C : ChowSituation.{u})
    {Z : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f] (hf : f ≫ sY = sX) (i : Z ⟶ X)
    [IsClosedImmersion i] (k : ℤ) (hZ : schemeDeltaDimension C (i ≫ sX) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    ∀ [((Scheme.Modules.pushforward f).obj
      ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))).IsCoherent],
    properPushforward C sX sY f hf k (cycleAssociatedToClosedSubscheme C sX i k) =
      cycleAssociatedToCoherentSheaf C sY
        ((Scheme.Modules.pushforward f).obj
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))) k
        (schemeDeltaDimension_reducedSupport_pushforward_le C sX sY f hf
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))
          (schemeDeltaDimension_reducedSupport_pushforwardStructureSheaf_le C sX i hZ))
```

**`Stacks.Chow.properPushforward_cycleAssociatedToCoherentSheaf_eq_directImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/DirectImageCycle.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/DirectImageCycle.lean#L51). The attribute's comment: “part (2)”.

> **Stacks 02R6, part (2).** Let `f : X ⟶ Y` be a proper morphism of schemes locally of finite
> type over the base `S` of chapter 42, and let `F` be a coherent `𝒪_X`-module whose support has
> delta-dimension at most `k`. Then `f_* [F]_k = [f_* F]_k`, where `f_* F` is coherent by
> [Stacks, Tag 02O5] since `Y` is locally Noetherian.

```lean
theorem properPushforward_cycleAssociatedToCoherentSheaf_eq_directImage (C : ChowSituation.{u})
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [IsProper f] (hf : f ≫ sY = sX) (F : X.Modules) [F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sX) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    letI : ((Scheme.Modules.pushforward f).obj F).IsCoherent := properDirectImageIsCoherent f F
    properPushforward C sX sY f hf k (cycleAssociatedToCoherentSheaf C sX F k hFk) =
      cycleAssociatedToCoherentSheaf C sY ((Scheme.Modules.pushforward f).obj F) k
        (schemeDeltaDimension_reducedSupport_pushforward_le C sX sY f hf F hFk)
```

**`Stacks.Chow.properPushforward_cycleAssociatedToClosedSubscheme_eq_directImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/DirectImageCycle.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/DirectImageCycle.lean#L70). The attribute's comment: “part (1)”.

> **Stacks 02R6, part (1).** Let `f : X ⟶ Y` be a proper morphism of schemes locally of finite
> type over the base `S` of chapter 42, and let `i : Z ⟶ X` be a closed subscheme with
> `dim_δ(Z) ≤ k`. Then `f_* [Z]_k = [f_* 𝒪_Z]_k`, where `𝒪_Z` is the coherent `𝒪_X`-module
> `i_* 𝒪_Z` and its direct image `f_* 𝒪_Z` is coherent by [Stacks, Tag 02O5] since `Y` is locally
> Noetherian.

```lean
theorem properPushforward_cycleAssociatedToClosedSubscheme_eq_directImage (C : ChowSituation.{u})
    {Z : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f] (hf : f ≫ sY = sX) (i : Z ⟶ X)
    [IsClosedImmersion i] (k : ℤ) (hZ : schemeDeltaDimension C (i ≫ sX) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    letI : ((Scheme.Modules.pushforward f).obj
        ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))).IsCoherent :=
      properDirectImageIsCoherent f _
    properPushforward C sX sY f hf k (cycleAssociatedToClosedSubscheme C sX i k) =
      cycleAssociatedToCoherentSheaf C sY
        ((Scheme.Modules.pushforward f).obj
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))) k
        (schemeDeltaDimension_reducedSupport_pushforward_le C sX sY f hf
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))
          (schemeDeltaDimension_reducedSupport_pushforwardStructureSheaf_le C sX i hZ))
```

**`Stacks.Chow.properPushforward_cycleAssociatedToCoherentSheaf_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Unconditional.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Unconditional.lean#L66). The attribute's comment: “part (2)”.

> **[Stacks, Tag 02R6], part (2).** Let `f : X ⟶ Y` be a proper morphism of schemes locally of
> finite type over the base `S` of chapter 42, and let `F` be a coherent `𝒪_X`-module whose support
> has delta-dimension at most `k`. Then proper pushforward of `k`-cycles carries the cycle of `F`
> to the cycle of the direct image: `f_* [F]_k = [f_* F]_k`.
>
> The coherence of `f_* F`, which is what lets the right-hand cycle be formed, is the proper
> mapping theorem [Stacks, Tag 02O5] in the form `Stacks.Chow.properDirectImageIsCoherent`: `Y` is
> locally Noetherian because it is locally of finite type over the locally Noetherian base. The
> equation itself is
> `Stacks.Chow.properPushforward_cycleAssociatedToCoherentSheaf`.

```lean
theorem properPushforward_cycleAssociatedToCoherentSheaf_unconditional (C : ChowSituation.{u})
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y)
    [IsProper f] (hf : f ≫ sY = sX) (F : X.Modules) [F.IsCoherent] (k : ℤ)
    (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sX) ≤ (k : EInt)) :
    letI : ((Scheme.Modules.pushforward f).obj F).IsCoherent :=
      haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
      properDirectImageIsCoherent f F
    properPushforward C sX sY f hf k (cycleAssociatedToCoherentSheaf C sX F k hFk) =
      cycleAssociatedToCoherentSheaf C sY ((Scheme.Modules.pushforward f).obj F) k
        (schemeDeltaDimension_reducedSupport_pushforward_le C sX sY f hf F hFk)
```

**`Stacks.Chow.properPushforward_cycleAssociatedToClosedSubscheme_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Unconditional.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardCoherent/Unconditional.lean#L89). The attribute's comment: “part (1)”.

> **[Stacks, Tag 02R6], part (1).** Let `f : X ⟶ Y` be a proper morphism of schemes locally of
> finite type over the base `S` of chapter 42, and let `i : Z ⟶ X` be a closed subscheme with
> `dim_δ(Z) ≤ k`. Then proper pushforward of `k`-cycles carries the cycle of `Z` to the cycle of
> the direct image of its structure sheaf: `f_* [Z]_k = [f_* 𝒪_Z]_k`.
>
> Here `𝒪_Z` is read as the coherent `𝒪_X`-module `i_* 𝒪_Z`, and the coherence of its direct image
> along `f` is again [Stacks, Tag 02O5]. The equation is
> `Stacks.Chow.properPushforward_cycleAssociatedToClosedSubscheme`.

```lean
theorem properPushforward_cycleAssociatedToClosedSubscheme_unconditional (C : ChowSituation.{u})
    {Z : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [IsProper f] (hf : f ≫ sY = sX) (i : Z ⟶ X)
    [IsClosedImmersion i] (k : ℤ) (hZ : schemeDeltaDimension C (i ≫ sX) ≤ (k : EInt)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : ((Scheme.Modules.pushforward f).obj
        ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))).IsCoherent :=
      haveI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
      properDirectImageIsCoherent f ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))
    properPushforward C sX sY f hf k (cycleAssociatedToClosedSubscheme C sX i k) =
      cycleAssociatedToCoherentSheaf C sY
        ((Scheme.Modules.pushforward f).obj
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))) k
        (schemeDeltaDimension_reducedSupport_pushforward_le C sX sY f hf
          ((Scheme.Modules.pushforward i).obj (Ample.unitModule Z))
          (schemeDeltaDimension_reducedSupport_pushforwardStructureSheaf_le C sX i hZ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.12, Tag 02R3](https://stacks.math.columbia.edu/tag/02R3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
