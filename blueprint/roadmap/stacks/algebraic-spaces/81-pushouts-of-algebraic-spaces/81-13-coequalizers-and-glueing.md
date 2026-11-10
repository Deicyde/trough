---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.properKernelPairCoequalizers_of_core, AlgebraicGeometry.Space.properKernelPairCoequalizers_holds, AlgebraicGeometry.Space.CoequalizerGlueSituation, AlgebraicGeometry.Space.CoequalizerGlueSituation.nonempty_glueCoequalizer, AlgebraicGeometry.Space.CoequalizerGlueSituation.isFinite_glueCoequalizer_toTarget, AlgebraicGeometry.Space.CoequalizerGlueSituation.universalHomeomorphism_glueCoequalizer_toTarget, AlgebraicGeometry.Space.CoequalizerGlueSituation.glueCoequalizer_closedSubspace_lift, AlgebraicGeometry.Space.CoequalizerGlueSituation.exists_glueCoequalizer
statement: formalized
proof: formalized
---

# 81.13 Coequalizers and glueing

Section 81.13 of the Stacks Project, [Tag 0AGF](https://stacks.math.columbia.edu/tag/0AGF). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AGG, a lemma

[Tag 0AGG](https://stacks.math.columbia.edu/tag/0AGG) in the Stacks Project.

**`AlgebraicGeometry.Space.properKernelPairCoequalizers_of_core`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ProperKernelPairCoequalizer.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ProperKernelPairCoequalizer.lean#L122). The attribute's comment: “all six clauses; clause (5) is proved from the others, while existence of the coequalizer and clauses (1) to (4) are carried in the hypothesis”.

> Let `g : Y ⟶ X` be a proper morphism of algebraic spaces over `S` with `X` locally
> Noetherian and let `R = Y ×_X Y` with its two projections `s, t : R ⟶ Y`. Then `s` and `t` have a
> coequalizer `X'` in the category of algebraic spaces over `S`, and: (1) the morphism `X' ⟶ X` is
> finite; (2) the morphism `Y ⟶ X'` is proper; (3) the morphism `Y ⟶ X'` is surjective; (4) the
> morphism `X' ⟶ X` is universally injective; (5) if `g` is surjective, the morphism `X' ⟶ X` is a
> universal homeomorphism. Existence of the coequalizer and clauses (1) to (4) are the hypothesis
> `hcore`.

```lean
theorem properKernelPairCoequalizers_of_core
    (hcore : ProperKernelPairCoequalizerCore B S hS) :
    ProperKernelPairCoequalizers B S hS
```

**`AlgebraicGeometry.Space.properKernelPairCoequalizers_holds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ProperKernelPairSheafDescent.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/ProperKernelPairSheafDescent.lean#L207).

> **Stacks 0AGG.** Let `S` be a scheme and let `g : Y ⟶ X` be a morphism of algebraic spaces
> over `S` with `X` locally Noetherian and `g` proper. Let `R = Y ×_X Y` with projections
> `s, t : R ⟶ Y`. There exists a coequalizer `X'` of `s, t : R ⟶ Y` in the category of algebraic
> spaces over `S`. Moreover
> 1. the morphism `X' ⟶ X` is finite;
> 2. the morphism `Y ⟶ X'` is proper;
> 3. the morphism `Y ⟶ X'` is surjective;
> 4. the morphism `X' ⟶ X` is universally injective;
> 5. if `g` is surjective, the morphism `X' ⟶ X` is a universal homeomorphism.
>
> The statement `AlgebraicGeometry.Space.ProperKernelPairCoequalizers` consists of exactly these
> six clauses: existence of the coequalizer as an
> `AlgebraicGeometry.Space.KernelPairCoequalizer` (a colimit cofork of the kernel pair in the
> category of algebraic spaces over `S`), and clauses (1) to (5) for every such coequalizer.
> Everything is proved here, unconditionally: nothing is carried as a hypothesis. The two inputs
> of the proof, the proper case of Stacks 0GFW and the translation step of Stacks 0GG0, are the
> theorems `AlgebraicGeometry.Space.descentEffectiveAlongProperSurjective` and
> `AlgebraicGeometry.Space.etaleSpaceDescentEffectiveOfSheafDescent`.

```lean
theorem properKernelPairCoequalizers_holds : ProperKernelPairCoequalizers B S hS
```

## Tag 0AGH, a situation

[Tag 0AGH](https://stacks.math.columbia.edu/tag/0AGH) in the Stacks Project.

**`AlgebraicGeometry.Space.CoequalizerGlueSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/Coequalizers.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/Coequalizers.lean#L49).

> **Stacks 0AGH.** The standing situation for the coequalizer construction: a locally
> Noetherian algebraic space `X` over `S`, a closed immersion `i : Z ⟶ X` with complementary open
> subspace `U`, and a proper morphism `f : X' ⟶ X` which is an isomorphism over `U`.

```lean
structure CoequalizerGlueSituation
```

## Tag 0AGI, a lemma

[Tag 0AGI](https://stacks.math.columbia.edu/tag/0AGI) in the Stacks Project.

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.nonempty_glueCoequalizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean#L286). The attribute's comment: “existence of the coequalizer; this clause is Stacks 0AGG, carried as the hypothesis hAGG because 0AGG rests on 08AR, which the library does not have”.

> **Stacks 0AGI**, existence of the coequalizer `X₁` of `s, t : R ⟶ Y` in the category of
> algebraic spaces over `S`, for `Y = X' ⨿ Z` and `R = Y ×_X Y`.

```lean
theorem nonempty_glueCoequalizer
    (hAGG : ProperKernelPairCoequalizers T.B T.S T.hS)
    (hproper : IsProper T.B T.S T.hS T.glueMap.hom) :
    Nonempty (KernelPairCoequalizer T.B T.S T.hS T.glueMap)
```

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.isFinite_glueCoequalizer_toTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean#L295). The attribute's comment: “the morphism to X is finite; this clause is part (1) of Stacks 0AGG, carried as the hypothesis hAGG”.

> **Stacks 0AGI**, finiteness of `X₁ ⟶ X`.

```lean
theorem isFinite_glueCoequalizer_toTarget
    (hAGG : ProperKernelPairCoequalizers T.B T.S T.hS)
    (hproper : IsProper T.B T.S T.hS T.glueMap.hom)
    (D : KernelPairCoequalizer T.B T.S T.hS T.glueMap) :
    IsFinite T.B T.S T.hS D.toTarget.hom
```

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.universalHomeomorphism_glueCoequalizer_toTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean#L307). The attribute's comment: “the morphism to X is a universal homeomorphism; part (5) of Stacks 0AGG is carried as the hypothesis hAGG, and its surjectivity input is proved here”.

> **Stacks 0AGI**, the morphism `X₁ ⟶ X` is a universal homeomorphism. The surjectivity of
> `g` which part (5) of Stacks 0AGG asks for is supplied by
> `AlgebraicGeometry.Space.CoequalizerGlueSituation.isSurjective_glueMap`.

```lean
theorem universalHomeomorphism_glueCoequalizer_toTarget
    (hAGG : ProperKernelPairCoequalizers T.B T.S T.hS)
    (hproper : IsProper T.B T.S T.hS T.glueMap.hom)
    (D : KernelPairCoequalizer T.B T.S T.hS T.glueMap) :
    UniversalHomeomorphism T.B T.S T.hS D.toTarget.hom
```

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.glueCoequalizer_closedSubspace_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean#L319). The attribute's comment: “Z lifts to the coequalizer; proved here”.

> **Stacks 0AGI**, the closed immersion `Z ⟶ X` lifts to the coequalizer: the composition of
> the coproduct inclusion of `Z` with the quotient morphism is a lift. This clause is proved
> outright: it needs only that `Y ⟶ X₁ ⟶ X` is `g`, which is `g` on the summand `Z`.

```lean
theorem glueCoequalizer_closedSubspace_lift
    (D : KernelPairCoequalizer T.B T.S T.hS T.glueMap) :
    (coprod.inr ≫ D.π) ≫ D.toTarget = (ObjectProperty.homMk T.i : _ ⟶ T.targetSpace)
```

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.exists_glueCoequalizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueingUnconditional.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueingUnconditional.lean#L56).

> **Stacks 0AGI.** In Situation 0AGH (`X` locally Noetherian over `S`, `Z ⟶ X` a closed
> immersion with complementary open `U`, `f : X' ⟶ X` proper and an isomorphism over `U`), let
> `Y = X' ⨿ Z` and `R = Y ×_X Y` with projections `s, t : R ⟶ Y`. There exists a coequalizer `X₁`
> of `s, t` in the category of algebraic spaces over `S`; the morphism `X₁ ⟶ X` is finite and a
> universal homeomorphism, it is an isomorphism over `U` (its base change along `U ⟶ X` is an
> isomorphism), and `Z ⟶ X` lifts to `X₁`. Everything is proved: Stacks 0AGG is
> `AlgebraicGeometry.Space.properKernelPairCoequalizers_holds`.

```lean
theorem exists_glueCoequalizer :
    ∃ D : KernelPairCoequalizer T.B T.S T.hS T.glueMap,
      IsFinite T.B T.S T.hS D.toTarget.hom ∧
      UniversalHomeomorphism T.B T.S T.hS D.toTarget.hom ∧
      IsIso (pullback.snd D.toTarget.hom T.U.ι) ∧
      ∃ l : T.closedSpace ⟶ D.space, l ≫ D.toTarget = ObjectProperty.homMk T.i
```

## Tag 0AGJ, an equation

[Tag 0AGJ](https://stacks.math.columbia.edu/tag/0AGJ) in the Stacks Project.

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.ClosedSubspaceSystem.towerMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean#L396). The attribute's comment: “the morphism of the tower”.

> **Stacks 0AGJ.** The morphism `X_n ⟶ X_{n+1}` of the tower
> `X_1 ⟶ X_2 ⟶ X_3 ⟶ … ⟶ X`, induced by the morphisms `Y_n ⟶ Y_{n+1}` and `R_n ⟶ R_{n+1}`.

```lean
def towerMap (n : ℕ) : (D n).space ⟶ (D (n + 1)).space
```

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.ClosedSubspaceSystem.towerMap_comp_toTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueing.lean#L411). The attribute's comment: “the tower is a tower over X”.

> **Stacks 0AGJ.** Each morphism of the tower `X_1 ⟶ X_2 ⟶ X_3 ⟶ … ⟶ X` is a morphism over
> `X`: the triangle formed with the two morphisms to `X` commutes.

```lean
theorem towerMap_comp_toTarget (n : ℕ) :
    N.towerMap D n ≫ (D (n + 1)).toTarget = (D n).toTarget
```

## Tag 0AGK, a lemma

[Tag 0AGK](https://stacks.math.columbia.edu/tag/0AGK) in the Stacks Project.

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.exists_factorsThroughSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueingUnconditional.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueingUnconditional.lean#L73).

> **Stacks 0AGK.** In Situation 0AGH assume `X` quasi-compact. Let `Z_n` be the infinitesimal
> neighbourhoods of `Z` in `X` and `X_n` the coequalizers of the kernel pairs of
> `X' ⨿ Z_n ⟶ X`, forming the tower `X_1 ⟶ X_2 ⟶ X_3 ⟶ … ⟶ X` of Stacks 0AGJ (for any choice
> `D` of these coequalizers, which exist by Stacks 0AGI). Then for all `n` large enough there is
> an `m` such that `X_n ⟶ X_{n+m}` factors through a closed immersion `X ⟶ X_{n+m}`; the closed
> immersion is moreover a section of `X_{n+m} ⟶ X`. Everything is proved: Stacks 0AGG is
> `AlgebraicGeometry.Space.properKernelPairCoequalizers_holds`.

```lean
theorem exists_factorsThroughSection (hqc : IsQuasiCompactSpace T.B T.S T.hS T.X)
    (D : ∀ n, KernelPairCoequalizer T.B T.S T.hS (T.neighbourhoodSystem.glueMapAt n)) :
    ∃ n₀, ∀ n, n₀ ≤ n → ∃ m, T.neighbourhoodSystem.FactorsThroughSection D n m
```

## Tag 0AGL, a remark

[Tag 0AGL](https://stacks.math.columbia.edu/tag/0AGL) in the Stacks Project.

**`AlgebraicGeometry.Space.CoequalizerGlueSituation.exists_isEssentiallyConstantWith`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueingUnconditional.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/CoequalizerGlueingUnconditional.lean#L85).

> **Stacks 0AGL.** In Situation 0AGH with `X` quasi-compact, the system
> `X_1 ⟶ X_2 ⟶ X_3 ⟶ …` of Stacks 0AGJ (for any choice `D` of the coequalizers) is essentially
> constant with value `X` in the sense of Stacks 05PU, with respect to the cocone of the morphisms
> `X_n ⟶ X`. Everything is proved: Stacks 0AGG is
> `AlgebraicGeometry.Space.properKernelPairCoequalizers_holds`.

```lean
theorem exists_isEssentiallyConstantWith (hqc : IsQuasiCompactSpace T.B T.S T.hS T.X)
    (D : ∀ n, KernelPairCoequalizer T.B T.S T.hS (T.neighbourhoodSystem.glueMapAt n)) :
    ∃ (i : ℕ) (r : T.targetSpace ⟶ (D i).space),
      CategoryTheory.EssentiallyConstantInd.IsEssentiallyConstantWith
        (T.neighbourhoodSystem.towerDiagram D)
        (T.neighbourhoodSystem.towerCocone D) i r
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.13, Tag 0AGF](https://stacks.math.columbia.edu/tag/0AGF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
