---
declaration: section
origin: cited
lean: Stacks.Curves.StableModel.exists_isStableContraction_comp_tails_bridges, Stacks.Curves.DualizingPullback.nonempty_pullback_dualizingSheafOverField_iso, Stacks.Curves.StableModel.existsUnique_isStableContraction, AlgebraicGeometry.isRelativelyVeryAmple_tensorPower_three_dualizingSheafOverField_and_isZero_cohomology_one
statement: formalized
proof: formalized
---

# 53.25 Contracting to a stable curve

Section 53.25 of the Stacks Project, [Tag 0E7N](https://stacks.math.columbia.edu/tag/0E7N). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E7N, the section

[Tag 0E7N](https://stacks.math.columbia.edu/tag/0E7N) in the Stacks Project.

**`Stacks.Curves.StableModel.exists_isStableContraction_comp_tails_bridges`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/StableContraction/StableModelCharacterization.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/StableContraction/StableModelCharacterization.lean#L106).

> **Stacks Project, Tag 0E7N: contracting to a stable curve.** Let `X` be a proper scheme over a
> field `k` of dimension one with `H⁰(X, 𝒪_X) = k`, genus `g ≥ 2` and at-worst-nodal singularities.
> Contract rational tails until none are left, `t : X ⟶ X₁` ([Stacks, Tag 0E3L]), and then rational
> bridges until none are left, `d : X₁ ⟶ Y` ([Stacks, Tag 0E3Q]). The composite `c = t ≫ d` is a
> morphism over `k` such that `Y` is proper over `k` of dimension one with at-worst-nodal
> singularities, `H⁰(Y, 𝒪_Y) = k`, `Y` has genus `g`, `𝒪_Y = c_*𝒪_X`, `R¹c_*𝒪_X = 0`, and `ω_Y` is
> ample. These conditions characterize `c` ([Stacks, Tag 0E7Q]): any `c' : X ⟶ Y'` satisfying the
> conditions of `IsStableContraction` is related to `c` by exactly one isomorphism `e : Y ≅ Y'` with
> `c ≫ e.hom = c'`.

```lean
theorem exists_isStableContraction_comp_tails_bridges (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X = 1) [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (hgenus : 2 ≤ genus f)
    (hnodal : letI : X.Over (Spec (.of k)) := ⟨f⟩
      Stacks.Curves.HasAtWorstNodalSingularities k X) :
    ∃ (X₁ : Scheme.{u}) (f₁ : X₁ ⟶ Spec (.of k)) (t : X ⟶ X₁) (Y : Scheme.{u})
      (gY : Y ⟶ Spec (.of k)) (d : X₁ ⟶ Y),
      IsIteratedContractionOfRationalTails k f f₁ t ∧
      (∀ C : X₁.IdealSheafData, ¬ @IsRationalTail k _ X₁ ⟨f₁⟩ C) ∧
      IsIteratedContractionOfRationalBridges k f₁ gY d ∧
      (∀ C : Y.IdealSheafData,
        letI : Y.Over (Spec (.of k)) := ⟨gY⟩
        ∀ _ : IsProper (Y ↘ Spec (.of k)), ¬ IsRationalBridge k Y C) ∧
      IsStableContraction f gY (t ≫ d) ∧
      IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ gY.appTop) ∧
      genus gY = genus f ∧
      ∀ (Y' : Scheme.{u}) (gY' : Y' ⟶ Spec (.of k)) (c' : X ⟶ Y'),
        IsStableContraction f gY' c' → ∃! e : Y ≅ Y', (t ≫ d) ≫ e.hom = c'
```

## Tag 0E7P, a lemma

[Tag 0E7P](https://stacks.math.columbia.edu/tag/0E7P) in the Stacks Project.

**`Stacks.Curves.DualizingPullback.nonempty_pullback_dualizingSheafOverField_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/StableContraction/DualizingPullbackGorenstein.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/StableContraction/DualizingPullbackGorenstein.lean#L53). The attribute's comment: “The corrected statement, with `m ≥ 1` (errata.md, 2026-11-06). Stacks allows any `m ∈ ℤ`, and is false for every `m ≤ 0`: for `X = V(xy) ⊆ ℙ²_k` and `c` contracting one line `C` to a point, (1)–(3) hold with any `m ≤ 0`, but `ω_X|_C ≅ 𝒪_C(-1)` while `(c^*ω_Y)|_C ≅ 𝒪_C`.”.

> **Stacks Project, Tag 0E7P.** Let `c : X ⟶ Y` be a morphism of proper schemes over a field
> `k` with `𝒪_Y = c_*𝒪_X` and `R^1 c_*𝒪_X = 0`, where `X` and `Y` are reduced, Gorenstein and of
> dimension one. If `H^1(X, ω_X^{⊗ m}) = 0` and `ω_X^{⊗ m}` is globally generated for some
> `m ≥ 1`, then `c^*ω_Y ≅ ω_X`. The source allows any `m ∈ ℤ`, which is false for `m ≤ 0`.

```lean
theorem nonempty_pullback_dualizingSheafOverField_iso
    (c : X ⟶ Y) (g : Y ⟶ Spec (.of k)) [IsProper (c ≫ g)] [IsProper g]
    (hO : IsIso (SheafOfModules.unitToPushforwardObjUnit c.toRingCatSheafHom))
    (hR1 : IsZero (((Scheme.Modules.pushforward c).rightDerived 1).obj
      (SheafOfModules.unit X.ringCatSheaf)))
    [IsReduced X] [IsReduced Y] [IsGorenstein X] [IsGorenstein Y]
    (hdimX : topologicalKrullDim X = 1) (hdimY : topologicalKrullDim Y = 1)
    (m : ℕ) (hm : 1 ≤ m)
    (hH1 : IsZero (cohomologyOverField k (c ≫ g)
      (tensorSheafNPow X.toRingedSpace (dualizingSheafOverField (c ≫ g)) m) 1))
    (hgen : SheafOfModules.IsGeneratedByGlobalSections
      (tensorSheafNPow X.toRingedSpace (dualizingSheafOverField (c ≫ g)) m : X.Modules)) :
    Nonempty ((Scheme.Modules.pullback c).obj (dualizingSheafOverField g) ≅
      dualizingSheafOverField (c ≫ g))
```

## Tag 0E7Q, a lemma

[Tag 0E7Q](https://stacks.math.columbia.edu/tag/0E7Q) in the Stacks Project.

**`Stacks.Curves.StableModel.existsUnique_isStableContraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/StableContraction/StableModelCharacterization.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/StableContraction/StableModelCharacterization.lean#L84). The attribute's comment: “Condition (3) includes that `ω_Y` is invertible, as ampleness is defined for invertible modules. Uniqueness up to unique isomorphism: any two such morphisms are related by exactly one isomorphism of targets under `X`.”.

> **Stacks Project, Tag 0E7Q.** Let `X` be a proper scheme over a field `k` of dimension one
> with `H⁰(X, 𝒪_X) = k`, genus `g ≥ 2` and at-worst-nodal singularities. There is a morphism
> `c : X ⟶ Y` of schemes over `k` such that
> 1. `Y` is proper over `k`, `dim Y = 1`, and `Y` has at-worst-nodal singularities,
> 2. `𝒪_Y = c_*𝒪_X` and `R¹c_*𝒪_X = 0`, and
> 3. `ω_Y` is ample on `Y`
>
> (`IsStableContraction f gY c`), and it is unique up to unique isomorphism: any two such
> `c : X ⟶ Y`, `c' : X ⟶ Y'` are related by exactly one isomorphism `e : Y ≅ Y'` with
> `c ≫ e = c'`.

```lean
theorem existsUnique_isStableContraction (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X = 1) [IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop)]
    (hgenus : 2 ≤ genus f)
    (hnodal : letI : X.Over (Spec (.of k)) := ⟨f⟩
      Stacks.Curves.HasAtWorstNodalSingularities k X) :
    (∃ (Y : Scheme.{u}) (gY : Y ⟶ Spec (.of k)) (c : X ⟶ Y), IsStableContraction f gY c) ∧
      ∀ (Y Y' : Scheme.{u}) (gY : Y ⟶ Spec (.of k)) (gY' : Y' ⟶ Spec (.of k)) (c : X ⟶ Y)
        (c' : X ⟶ Y'), IsStableContraction f gY c → IsStableContraction f gY' c' →
        ∃! e : Y ≅ Y', c ≫ e.hom = c'
```

## Tag 0E8X, a lemma

[Tag 0E8X](https://stacks.math.columbia.edu/tag/0E8X) in the Stacks Project.

**`AlgebraicGeometry.isRelativelyVeryAmple_tensorPower_three_dualizingSheafOverField_and_isZero_cohomology_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/StableContraction/TricanonicalVeryAmple.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/StableContraction/TricanonicalVeryAmple.lean#L291).

> **Stacks Project, Tag 0E8X.** Let `X` be a proper scheme of dimension one over a field `k`
> with `H⁰(X, 𝒪_X) = k`, of genus `g ≥ 2`, with at-worst-nodal singularities, and assume the
> dualizing sheaf `ω_X` is ample. Then `ω_X^{⊗ 3}` is very ample and `H¹(X, ω_X^{⊗ 3}) = 0`.
>
> `ω_X` is invertible since `X` is Gorenstein ([Stacks, Tag 0E37]). `X` has no rational tail, so
> `ω_X^{⊗ 3}` is globally generated ([Stacks, Tag 0E3K]); its sections define a morphism to
> projective space, which is a closed immersion once it is one after base change to `k̄`
> ([Stacks, Tag 02L6]). Over `k̄` the base change is again nodal of genus `g` with ample dualizing
> sheaf the pullback of `ω_X` ([Stacks, Tag 0E32]), and `H¹(ℐ_Z ω^{⊗ 3}) = 0` for every degree-two
> `Z` gives the criterion of [Stacks, Tag 0E8T].

```lean
theorem isRelativelyVeryAmple_tensorPower_three_dualizingSheafOverField_and_isZero_cohomology_one
    (hdim : topologicalKrullDim X = 1) (hg : 2 ≤ genus (X ↘ Spec (.of k)))
    (hnodal : Stacks.Curves.HasAtWorstNodalSingularities k X)
    (hω : haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
      letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim hnodal
      Scheme.Modules.IsAmple X (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k)))) :
    haveI := connectedSpace_of_isIso_globalSections k (X ↘ Spec (.of k))
    letI := isInvertible_dualizingSheafOverField_of_hasAtWorstNodalSingularities k X hdim hnodal
    Stacks.Tag01VMVeryAmple.IsRelativelyVeryAmple (X ↘ Spec (.of k))
        (Stacks.SheafOfModules.Invertible.tensorPower X.presheaf X.ringCatSheaf.2
          (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) 3) ∧
      IsZero (cohomologyOverField k (X ↘ Spec (.of k))
        (Stacks.SheafOfModules.Invertible.tensorPower X.presheaf X.ringCatSheaf.2
          (Stacks.Duality.dualizingSheafOverField (X ↘ Spec (.of k))) 3) 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.25, Tag 0E7N](https://stacks.math.columbia.edu/tag/0E7N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
