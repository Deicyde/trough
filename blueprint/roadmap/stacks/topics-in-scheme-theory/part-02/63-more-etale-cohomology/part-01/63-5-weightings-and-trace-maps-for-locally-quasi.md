---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.modFShriekProjectionIso, AlgebraicGeometry.separableDegreeWeightedFiberSum_flatQuasiFiniteWeight_of_etale, AlgebraicGeometry.etaleCanonicalTrace, AlgebraicGeometry.moduleEtaleCanonicalTrace, AlgebraicGeometry.SmallEtale.existsUnique_hasWeightedTraceStalks, AlgebraicGeometry.etaleCanonicalTrace_naturality, AlgebraicGeometry.moduleEtaleCanonicalTrace_naturality, AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_baseChange
statement: formalized
proof: formalized
---

# 63.5 Weightings and trace maps for locally quasi-finite morphisms

Section 63.5 of the Stacks Project, [Tag 0GKE](https://stacks.math.columbia.edu/tag/0GKE). 7 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GKF, a lemma

[Tag 0GKF](https://stacks.math.columbia.edu/tag/0GKF) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.modFShriekProjectionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekModuleProjectionIso.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FShriekModuleProjectionIso.lean#L206). The attribute's comment: “the projection formula isomorphism”.

> **Stacks 0GKF**, the canonical isomorphism of the projection formula
> `f_!F ⊗_Λ G ≅ f_!(F ⊗_Λ f^{-1}G)` for a locally quasi-finite morphism `f : X ⟶ Y`.

```lean
public def modFShriekProjectionIso
    (F : ModuleSheaf.{u, v, max (u + 1) v} B X Λ)
    (G : ModuleSheaf.{u, v, max (u + 1) v} B Y Λ) :
    (fShriekMod.{u, v, max (u + 1) v} B Λ f).obj F ⊗ G ≅
      (fShriekMod.{u, v, max (u + 1) v} B Λ f).obj
        (F ⊗ ((modPullback.{u, v, max (u + 1) v} B Λ f).obj G))
```

## Tag 0GKG, a lemma

[Tag 0GKG](https://stacks.math.columbia.edu/tag/0GKG) in the Stacks Project.

**`AlgebraicGeometry.separableDegreeWeightedFiberSum_flatQuasiFiniteWeight_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleCanonicalWeighting.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleCanonicalWeighting.lean#L150). The attribute's comment: “The fibre integral `∫_{U → V} w` out of which the trace map `Tr_{f, w}` is built, computed for an étale morphism with its canonical weighting: it is the plain separable-degree fibre count. For an étale morphism with its canonical weighting the trace map itself is the counit of `j_! ⊣ j^{-1}`, by `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit` of `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.EtaleTraceIsCounit`; for a general locally quasi-finite morphism and a general weighting its construction is a separate matter. Its uniqueness and its characterisation on stalks are, for an arbitrary locally quasi-finite morphism and an arbitrary integer-valued weight, in `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.WeightedTraceConstruction`; and the fibre integral of a section supported on a part finite over the base, for an arbitrary locally quasi-finite morphism and an arbitrary weighting, in `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.FibreIntegral`.”.

> **The fibre integral defining the trace map of Stacks 0GKG, for an étale morphism with its
> canonical weighting.** The construction of `Tr_{f, w}` sends a section supported on a locally
> closed `Z ⊂ X_V` finite over `V` to the fibre integral `∫_{Z → V} w|_Z`, which is
> `AlgebraicGeometry.separableDegreeWeightedFiberSum`. For an étale morphism carrying its
> canonical weighting that integral is the plain separable-degree fibre count: the weights
> contribute nothing.

```lean
theorem separableDegreeWeightedFiberSum_flatQuasiFiniteWeight_of_etale
    {V : Scheme.{u}} (π : U ⟶ V) :
    separableDegreeWeightedFiberSum π (flatQuasiFiniteWeight j) =
      separableDegreeWeightedFiberSum π 1
```

**`AlgebraicGeometry.etaleCanonicalTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean#L91). The attribute's comment: “The trace map `Tr_{f, w} : f_! f^{-1}ℱ ⟶ ℱ` in the single case of an étale morphism carrying its canonical weighting, where by Remark 0GL4 it is the counit of `j_! ⊣ j^{-1}`; it is defined here to be that counit. The general construction, for a locally quasi-finite morphism and an arbitrary weighting, is a separate matter. That the counit does satisfy the stalk characterisation `AlgebraicGeometry.SmallEtale.HasWeightedTraceStalks` of Lemma 0GKG for the canonical weighting, so that by `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_unique` it is the trace map of Lemma 0GKG in the étale case, is `AlgebraicGeometry.hasWeightedTraceStalks_counit` in `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.EtaleTraceIsCounit`. The substantive fact licensing this case is the companion `AlgebraicGeometry.flatQuasiFiniteWeight_eq_one_of_etale`.”.

> **The trace map of Stacks 0GKG for an étale morphism with its canonical weighting.** The
> canonical weighting of an étale `j : U ⟶ X` is the constant function `1`
> (`AlgebraicGeometry.flatQuasiFiniteWeight_eq_one_of_etale`), for which the prescribed stalk
> behaviour of the trace is the sum map `⨁_{j(ū) = x̄} ℱ_x̄ ⟶ ℱ_x̄`; that map is the counit of
> `j_! ⊣ j^{-1}`, and the counit is what is taken here.

```lean
def etaleCanonicalTrace :
    abelianRestriction B X hX U ⋙ abelianExtensionByZero B X hX U ⟶
      𝟭 (Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.moduleEtaleCanonicalTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean#L158). The attribute's comment: “The trace map on étale sheaves of `Λ`-modules, in the single case of an étale morphism carrying its canonical weighting, where by Remark 0GL4 it is the counit of `j_! ⊣ j^{-1}`; it is defined here to be that counit. Same scope as `AlgebraicGeometry.etaleCanonicalTrace`: the general weighted construction of Lemma 0GKG, for a locally quasi-finite morphism and an arbitrary weighting, is a separate matter, and the stalk characterisation `AlgebraicGeometry.SmallEtale.HasWeightedTraceStalks` under which it is unique is verified for the counit with abelian coefficients in `AlgebraicGeometry.hasWeightedTraceStalks_counit`.”.

> **The trace map of Stacks 0GKG for an étale morphism with its canonical weighting, on
> sheaves of `Λ`-modules.** As in the abelian case, this is the counit of `j_! ⊣ j^{-1}`.

```lean
def moduleEtaleCanonicalTrace :
    moduleRestriction B X hX U Λ ⋙ moduleExtensionByZero B X hX U Λ ⟶
      𝟭 (Sheaf (SmallEtale.topology B X hX) (ModuleCat.{max (u + 1) v} Λ))
```

**`AlgebraicGeometry.SmallEtale.existsUnique_hasWeightedTraceStalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceExistence.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceExistence.lean#L88).

> **Stacks 0GKG.** Let `f : X ⟶ Y` be a locally quasi-finite morphism of schemes and let
> `w : X → ℤ` be a weighting of `f`. For every abelian sheaf `F` on the small étale site of `Y`
> there exists a unique trace map `Tr_{f, w, F} : f_! f^{-1}F ⟶ F` with the prescribed behaviour
> on stalks: at every geometric point `s̄` of `Y` the map it induces on stalks, read through the
> decomposition of `(f_! f^{-1}F)_{s̄}` into the direct sum of the stalks of `f^{-1}F` over the
> geometric fibre above `s̄`, is the weighted sum `(a_{x̄})_{x̄} ↦ ∑_{x̄} w(x̄) · a_{x̄}` over that
> fibre.

```lean
public theorem existsUnique_hasWeightedTraceStalks {w : X.obj → ℤ}
    (hw : IsWeighting (B.inclusion.map f) w)
    (F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{max (u + 1) v}) :
    ∃! τ : (fShriekFunctor.{u, v} B f).obj ((abPullback.{u, v} B f).obj F) ⟶ F,
      HasWeightedTraceStalks.{u, v} B f w F τ
```

## Tag 0GKH, a lemma

[Tag 0GKH](https://stacks.math.columbia.edu/tag/0GKH) in the Stacks Project.

**`AlgebraicGeometry.etaleCanonicalTrace_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean#L114). The attribute's comment: “Part (1) only — functoriality of the trace map in the sheaf — for an étale morphism with its canonical weighting, the case of Remark 0GL4, where the trace is the counit of `j_! ⊣ j^{-1}`. Part (1) for an ARBITRARY locally quasi-finite morphism and an arbitrary weight is `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_naturality`, stated for the morphisms with the characterising stalk behaviour of Lemma 0GKG. Part (2), compatibility with arbitrary base change, and part (3), the version for `K` in the unbounded derived category `D(Y_étale, Λ)`, are NOT carried by this declaration. The general weighted trace of Lemma 0GKG that parts (1)-(3) are about is `AlgebraicGeometry.SmallEtale.weightedTrace` of `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.WeightedTraceExistence`; see the clause on `AlgebraicGeometry.etaleCanonicalTrace`.”.

> The trace map is functorial in the abelian sheaf: for `φ : ℱ ⟶ 𝒢` the square formed by
> `Tr_ℱ`, `Tr_𝒢` and `j_! j^{-1}φ` commutes.

```lean
theorem etaleCanonicalTrace_naturality
    {F G : Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}} (φ : F ⟶ G) :
    (abelianRestriction B X hX U ⋙ abelianExtensionByZero B X hX U).map φ ≫
        (etaleCanonicalTrace B X hX U).app G =
      (etaleCanonicalTrace B X hX U).app F ≫ φ
```

**`AlgebraicGeometry.moduleEtaleCanonicalTrace_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean#L179). The attribute's comment: “Part (1) with `Λ`-module coefficients — functoriality of the trace map in the sheaf of `Λ`-modules — for an étale morphism with its canonical weighting. This is the coefficient half of part (3); the DERIVED half of part (3), for `K` in `D(Y_étale, Λ)`, is NOT carried, and neither is part (2), compatibility with arbitrary base change. For part (1) with abelian coefficients but an arbitrary locally quasi-finite morphism and arbitrary weight, see `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_naturality`. The general weighted trace of Lemma 0GKG is `AlgebraicGeometry.SmallEtale.weightedTrace`; see the clause on `AlgebraicGeometry.moduleEtaleCanonicalTrace`.”.

> The trace map is functorial in the sheaf of `Λ`-modules.

```lean
theorem moduleEtaleCanonicalTrace_naturality
    {F G : Sheaf (SmallEtale.topology B X hX) (ModuleCat.{max (u + 1) v} Λ)} (φ : F ⟶ G) :
    (moduleRestriction B X hX U Λ ⋙ moduleExtensionByZero B X hX U Λ).map φ ≫
        (moduleEtaleCanonicalTrace B X hX U Λ).app G =
      (moduleEtaleCanonicalTrace B X hX U Λ).app F ≫ φ
```

**`AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceBaseChange.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceBaseChange.lean#L504). The attribute's comment: “part (2), compatibility of the trace map with arbitrary base change, for an arbitrary cartesian square with locally quasi-finite vertical morphism and an arbitrary integer-valued weight: the base change of a trace map for `(f, w)` is a trace map for `(f', w ∘ p)`, and the square formed by the base-change isomorphism of 0F5J, the comparison of the two iterated inverse images, and the two trace maps commutes. The trace maps enter through the behaviour on geometric stalks by which 0GKG characterises them, which determines at most one morphism per sheaf by `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_unique`. The finite-type and quasi-finiteness conditions on the base change are supplied from the square.”. References: SGA 4 XVII (6.2.5), “more general”.

> **Stacks 0GKH, part (2): the trace map is compatible with arbitrary base change.** Let
> `f : X ⟶ Y` be locally quasi-finite, let `w` be an integer-valued function on `X`, let `F` be an
> abelian sheaf on the small étale site of `Y`, and let
>
> ```
> X' --p--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> be a cartesian square. Then the base change along `g` of a trace map `τ` for `(f, w)` at `F`,
> transported along the base-change isomorphism `g^{-1}f_!G ≅ f'_!p^{-1}G` of Stacks 0F5J and the
> comparison `p^{-1}f^{-1}F ≅ f'^{-1}g^{-1}F` of the two iterated inverse images, is a trace map for
> `(f', w ∘ p)` at `g^{-1}F`; equivalently, the square formed by those two comparisons and the two
> trace maps commutes.
>
> The finite-type and quasi-finiteness hypotheses on the base change `f'` are supplied from the
> square, so only the hypotheses of the source are assumed. The weighting hypothesis of the source
> is not needed: the statement holds for an arbitrary integer-valued `w`, the pulled-back function
> `w ∘ p` being a weighting of `f'` whenever `w` is a weighting of `f` by Stacks 0F3B
> (`AlgebraicGeometry.IsWeighting.comp_of_isPullback`). The trace maps enter through the behaviour
> on geometric stalks by which Stacks 0GKG characterises them, which by
> `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_unique` determines at most one morphism for
> each sheaf.

```lean
public theorem hasWeightedTraceStalks_baseChange (w : X.obj → ℤ)
    (F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1})
    {τ : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F}
    (hτ : HasWeightedTraceStalks.{u, u + 1} B f w F τ) :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    letI := locallyQuasiFinite_of_isPullback B p f' f g sq
    HasWeightedTraceStalks.{u, u + 1} B f' (w ∘ B.inclusion.map p)
        ((abPullback.{u, u + 1} B g).obj F)
        ((fShriekFunctor.{u, u + 1} B f').map
            ((inverseImageSquareIso.{u} B p f' f g sq).inv.app F) ≫
          (fShriekBaseChangeNatIso.{u} B p f' f g sq).inv.app
            ((abPullback.{u, u + 1} B f).obj F) ≫
          (abPullback.{u, u + 1} B g).map τ) ∧
      ∀ τ' : (fShriekFunctor.{u, u + 1} B f').obj
          ((abPullback.{u, u + 1} B f').obj ((abPullback.{u, u + 1} B g).obj F)) ⟶
            (abPullback.{u, u + 1} B g).obj F,
        HasWeightedTraceStalks.{u, u + 1} B f' (w ∘ B.inclusion.map p)
            ((abPullback.{u, u + 1} B g).obj F) τ' →
          (fShriekBaseChangeNatIso.{u} B p f' f g sq).hom.app
              ((abPullback.{u, u + 1} B f).obj F) ≫
            (fShriekFunctor.{u, u + 1} B f').map
              ((inverseImageSquareIso.{u} B p f' f g sq).hom.app F) ≫ τ' =
            (abPullback.{u, u + 1} B g).map τ
```

**`AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceDerivedConstruction.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceDerivedConstruction.lean#L459). The attribute's comment: “part (3), the weighted trace with coefficients in a ring Λ on unbounded derived categories, for an arbitrary cartesian square with locally quasi-finite vertical morphism and a weighting w of it: for every K in D(Y\_étale, Λ) a morphism Tr\_\{f,w,K} : f\_!f^\{-1}K ⟶ K, functorial in K, restricting to the sheaf-level trace of 0GKG, and compatible with arbitrary base change. The Λ-linear inverse images along f, f', g and p are `AlgebraicGeometry.SmallEtale.pullbackMod`, the lift of the abelian inverse image of 03Q1; the two comparisons attached to the square are the lifts `AlgebraicGeometry.SmallEtale.fShriekBaseChangeMod` and `AlgebraicGeometry.SmallEtale.inverseImageSquareMod` of the isomorphism of 0F5J and of the comparison of the two iterated inverse images; the trace maps at Λ-coefficients are `AlgebraicGeometry.SmallEtale.weightedTraceMod`, the trace of 0GKG read as a morphism of sheaves of Λ-modules, which the first two clauses show to have the characterising behaviour on geometric stalks of 0GKG and to be the unique morphism with it. The base-change square at Λ-coefficients is deduced from part (2) at abelian coefficients, and the derived square is its image under the deriving operation. The finite-type and quasi-finiteness conditions on the base change are supplied from the square, so the hypotheses are those of the source. The coefficient universes are those at which 0F5J is available: ModuleSheaf.\{u, u+1, u} with Λ : Type u.”. References: SGA 4 XVII (6.2.5), “more general”.

> **The weighted trace with coefficients in a ring, on unbounded derived categories.** Let
> `f : X ⟶ Y` be locally quasi-finite, let `w` be a weighting of `f`, let `Λ` be a ring, and let
>
> ```
> X' --p--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> be a cartesian square. Then:
>
> * for every sheaf of `Λ`-modules `M` on the small étale site of `Y` the morphism
>   `Tr_{f, w, M} : f_! f^{-1}M ⟶ M` of `AlgebraicGeometry.SmallEtale.weightedTraceMod` has the
>   behaviour on geometric stalks by which Stacks 0GKG characterises the trace of `(f, w)`, and it
>   is the only morphism of sheaves of `Λ`-modules with that behaviour;
> * `f^{-1}` and `f_!` are exact on sheaves of `Λ`-modules, so each induces a functor on unbounded
>   derived categories, and the trace maps induce a natural transformation
>   `Tr_{f, w} : f_! f^{-1} ⟶ id` of `D(Y_étale, Λ)`, whose component at `K` is
>   `Tr_{f, w, K} : f_! f^{-1}K ⟶ K`;
> * that transformation is **functorial in `K`**: every naturality square commutes;
> * it **restricts to the sheaf-level trace**: it is the derived form of the natural
>   transformation whose component at a sheaf of `Λ`-modules `M` is `Tr_{f, w, M}`, read through
>   the canonical identification of the derived functor of `f^{-1} ⋙ f_!` with the composite of
>   the derived functors and of the derived functor of the identity with the identity;
> * it is **compatible with arbitrary base change**: the two comparisons attached to the square at
>   `Λ`-coefficients — the base-change isomorphism `g^{-1}f_!N ≅ f'_!p^{-1}N` of Stacks 0F5J and
>   the comparison `p^{-1}f^{-1}M ≅ f'^{-1}g^{-1}M` of the two iterated inverse images — carry the
>   derived trace of `(f, w)` to the derived trace of `(f', w ∘ p)`, both whiskered by the derived
>   `g^{-1}`;
> * and the weight attached to the base change is the right one: `w ∘ p` is a weighting of `f'`,
>   which is Stacks 0F3B.
>
> Every object of the statement is constructed: the `Λ`-linear inverse images along the four
> morphisms of the square are `AlgebraicGeometry.SmallEtale.pullbackMod`, the two comparisons are
> `AlgebraicGeometry.SmallEtale.fShriekBaseChangeMod` and
> `AlgebraicGeometry.SmallEtale.inverseImageSquareMod`, and the trace maps at `Λ`-coefficients are
> `AlgebraicGeometry.SmallEtale.weightedTraceMod` for `(f, w)` and for `(f', w ∘ p)`.
>
> The finite-type and quasi-finiteness hypotheses on the base change `f'` are supplied from the
> square, so the hypotheses are those of the source: `f` locally quasi-finite, `w` a weighting of
> `f`, and the square cartesian.
>
> The coefficient universes are the ones at which the base-change isomorphism of Stacks 0F5J is
> available: the abelian étale sheaves have coefficients in `AddCommGrpCat.{u + 1}`, so the sheaves
> of `Λ`-modules are taken at `ModuleSheaf.{u, u + 1, u}` with `Λ : Type u`.

```lean
public theorem derivedWeightedTraceMod_spec {w : X.obj → ℤ}
    (hw : IsWeighting (B.inclusion.map f) w) :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    letI := locallyQuasiFinite_of_isPullback B p f' f g sq
    (∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
        HasWeightedTraceStalksMod.{u, u + 1, u} B Λ f (pullbackMod.{u, u + 1, u} B Λ f)
          (pullbackModForgetIso.{u, u + 1, u} B Λ f) w M
          (weightedTraceMod.{u, u + 1, u} B Λ f hw M)) ∧
      (∀ (M : ModuleSheaf.{u, u + 1, u} B Y Λ)
          (σ : (fShriekMod.{u, u + 1, u} B Λ f).obj
            ((pullbackMod.{u, u + 1, u} B Λ f).obj M) ⟶ M),
          HasWeightedTraceStalksMod.{u, u + 1, u} B Λ f (pullbackMod.{u, u + 1, u} B Λ f)
            (pullbackModForgetIso.{u, u + 1, u} B Λ f) w M σ →
            σ = weightedTraceMod.{u, u + 1, u} B Λ f hw M) ∧
      (∀ (K K' : DerivedCategory (ModuleSheaf.{u, u + 1, u} B Y Λ)) (ψ : K ⟶ K'),
          ((pullbackMod.{u, u + 1, u} B Λ f).mapDerivedCategory ⋙
              (fShriekMod.{u, u + 1, u} B Λ f).mapDerivedCategory).map ψ ≫
              (derivedWeightedTraceMod.{u, u + 1, t, u} B Λ f hw).app K' =
            (derivedWeightedTraceMod.{u, u + 1, t, u} B Λ f hw).app K ≫ ψ) ∧
      (derivedWeightedTraceMod.{u, u + 1, t, u} B Λ f hw =
          (Stacks.Cohomology.PerfectComplexTriangles.mapDerivedCategoryCompIso
              (pullbackMod.{u, u + 1, u} B Λ f) (fShriekMod.{u, u + 1, u} B Λ f)).inv ≫
            NatTrans.mapDerivedCategory
              (weightedTraceModTrans.{u, u + 1, u} B Λ f hw) ≫
            (Functor.mapDerivedCategoryIdIso _).hom) ∧
      (∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
          (weightedTraceModTrans.{u, u + 1, u} B Λ f hw).app M =
            weightedTraceMod.{u, u + 1, u} B Λ f hw M) ∧
      (NatTrans.mapDerivedCategory
            (traceBaseChangeComparison.{u, u + 1, u} B Λ f' f (pullbackMod.{u, u + 1, u} B Λ f)
              (pullbackMod.{u, u + 1, u} B Λ f') (pullbackMod.{u, u + 1, u} B Λ g)
              (pullbackMod.{u, u + 1, u} B Λ p) (fShriekBaseChangeMod.{u} B Λ p f' f g sq)
              (inverseImageSquareMod.{u} B Λ p f' f g sq)).hom ≫
          (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
            (pullbackMod.{u, u + 1, u} B Λ g)
            (pullbackMod.{u, u + 1, u} B Λ f' ⋙ fShriekMod.{u, u + 1, u} B Λ f')).hom ≫
          Functor.whiskerLeft (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory
            (NatTrans.mapDerivedCategory
              (weightedTraceModTrans.{u, u + 1, u} B Λ f'
                (AlgebraicGeometry.IsWeighting.comp_of_isPullback hw (sq.map B.inclusion)))) ≫
          (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
            (pullbackMod.{u, u + 1, u} B Λ g)
            (𝟭 (ModuleSheaf.{u, u + 1, u} B Y' Λ))).inv =
        (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
            (pullbackMod.{u, u + 1, u} B Λ f ⋙ fShriekMod.{u, u + 1, u} B Λ f)
            (pullbackMod.{u, u + 1, u} B Λ g)).hom ≫
          Functor.whiskerRight
            (NatTrans.mapDerivedCategory (weightedTraceModTrans.{u, u + 1, u} B Λ f hw))
            (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory ≫
          (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
            (𝟭 (ModuleSheaf.{u, u + 1, u} B Y Λ))
            (pullbackMod.{u, u + 1, u} B Λ g)).inv) ∧
      AlgebraicGeometry.IsWeighting (B.inclusion.map f') (w ∘ B.inclusion.map p)
```

**`AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceProperties.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceProperties.lean#L160). The attribute's comment: “part (1), functoriality of the trace map in the sheaf, for an arbitrary locally quasi-finite morphism and an arbitrary integer-valued weight. Stated for morphisms with the behaviour on geometric stalks by which Lemma 0GKG characterises the trace map, which by `AlgebraicGeometry.SmallEtale.existsUnique_hasWeightedTraceStalks` is exactly the trace map of that lemma: it exists for every weighting and every sheaf, and is unique. Part (2) is `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalks_baseChange`.”. References: SGA 4 XVII (6.2.5).

> **Stacks 0GKH, part (1): the trace map is functorial in the abelian sheaf.** If `τ_F` and
> `τ_G` are trace maps for `(f, w)` at `F` and at `G` — morphisms with the weighted behaviour on
> geometric stalks which characterises the trace of Stacks 0GKG — then for every `φ : F ⟶ G` the
> square
> `f_! f^{-1}F ⟶ f_! f^{-1}G ⟶ G` versus `f_! f^{-1}F ⟶ F ⟶ G`
> commutes.
>
> The source deduces this from the characterisation on stalks, and so does the proof here: the
> geometric stalk functors are jointly faithful, the stalk of a trace map is the weighted sum over
> the geometric fibre read through the decomposition of Stacks 0F5F, that decomposition is natural
> in the sheaf, and the weighted sum is natural by
> `AlgebraicGeometry.SmallEtale.weightedTraceStalkMap_natural`. No hypothesis on `w` is needed.

```lean
public theorem hasWeightedTraceStalks_naturality (w : X.obj → ℤ)
    {F G : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{max (u + 1) v}}
    (φ : F ⟶ G)
    {τF : (fShriekFunctor.{u, v} B f).obj ((abPullback.{u, v} B f).obj F) ⟶ F}
    {τG : (fShriekFunctor.{u, v} B f).obj ((abPullback.{u, v} B f).obj G) ⟶ G}
    (hF : HasWeightedTraceStalks.{u, v} B f w F τF)
    (hG : HasWeightedTraceStalks.{u, v} B f w G τG) :
    (fShriekFunctor.{u, v} B f).map ((abPullback.{u, v} B f).map φ) ≫ τG = τF ≫ φ
```

## Tag 0GL3, a lemma

[Tag 0GL3](https://stacks.math.columbia.edu/tag/0GL3) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceCompositionDerived.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceCompositionDerived.lean#L427). The attribute's comment: “the derived trace maps compose: g\_! Tr\_\{f,w\_f,g^\{-1}K} followed by Tr\_\{g,w\_g,K} is Tr\_\{g∘f,w\_\{g∘f},K} for every K in D(Z\_étale, Λ)”.

> **Stacks 0GL3.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be locally quasi-finite morphisms, `w_f` a
> weighting of `f` and `w_g` a weighting of `g`, and `Λ` a ring. For `K` in `D(Z_étale, Λ)` the
> composite
> `(g ∘ f)_!(g ∘ f)^{-1}K = g_! f_! f^{-1} g^{-1}K ⟶ g_! g^{-1}K ⟶ K`
> of `g_! Tr_{f, w_f, g^{-1}K}` and `Tr_{g, w_g, K}` is `Tr_{g ∘ f, w_{g ∘ f}, K}`, where
> `w_{g ∘ f}(x) = w_f(x) w_g(f(x))` (a weighting of `g ∘ f` by Stacks 0GK9).
>
> The identification `(g ∘ f)_!(g ∘ f)^{-1}K = g_! f_! f^{-1} g^{-1}K` is the derived form of the
> composition laws `(g ∘ f)^{-1} ≅ f^{-1} ∘ g^{-1}` of Stacks 021J and `(g ∘ f)_! ≅ g_! ∘ f_!` of
> Stacks 0F6T at `Λ`-coefficients, followed by the identification of the derived functor of a
> composite with the composite of the derived functors. The trace maps are those of Stacks 0GKH,
> part (3).

```lean
public theorem derivedWeightedTraceMod_comp (K : DerivedCategory (ModuleSheaf.{u, v, r} B Z Λ)) :
    (fShriekMod.{u, v, r} B Λ (f ≫ g)).mapDerivedCategory.map
        ((CategoryTheory.mapDerivedCategoryIsoComp (pullbackMod.{u, v, r} B Λ g)
          (pullbackMod.{u, v, r} B Λ f) (pullbackMod.{u, v, r} B Λ (f ≫ g))
          (pullbackModCompIso B Λ f g)).hom.app K) ≫
      (CategoryTheory.mapDerivedCategoryIsoComp (fShriekMod.{u, v, r} B Λ f)
          (fShriekMod.{u, v, r} B Λ g) (fShriekMod.{u, v, r} B Λ (f ≫ g))
          (fShriekModCompIso B Λ f g)).hom.app
        ((pullbackMod.{u, v, r} B Λ f).mapDerivedCategory.obj
          ((pullbackMod.{u, v, r} B Λ g).mapDerivedCategory.obj K)) ≫
      (fShriekMod.{u, v, r} B Λ g).mapDerivedCategory.map
        ((derivedWeightedTraceMod.{u, v, t, r} B Λ f hw_f).app
          ((pullbackMod.{u, v, r} B Λ g).mapDerivedCategory.obj K)) ≫
      (derivedWeightedTraceMod.{u, v, t, r} B Λ g hw_g).app K =
    (derivedWeightedTraceMod.{u, v, t, r} B Λ (f ≫ g) (isWeighting_comp B f g hw_f hw_g)).app K
```

## Tag 0GKI, an example

[Tag 0GKI](https://stacks.math.columbia.edu/tag/0GKI) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.flatQuasiFiniteTrace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L156). The attribute's comment: “the trace maps `Tr_{f, K} : f_! f^{-1} K ⟶ K` for `K` in `D(Y_étale, Λ)`, obtained -- as the example says -- by applying Lemmas 0GKG and 0GKH to `f` and the canonical weighting of 0F3D, which is `AlgebraicGeometry.flatQuasiFiniteWeight`. The example asserts no property of these maps beyond the two in the next two declarations, functoriality in `K` and compatibility with arbitrary base change.”. References: SGA 4½ Cycle (2.3.1), “special case”.

> **Stacks Project, Example 0GKI: the trace maps of a flat quasi-finite morphism.** For
> `f : X ⟶ Y` flat, locally quasi-finite and locally of finite presentation, and a ring `Λ`, the
> family of trace maps
>
> `Tr_{f, K} : f_! f^{-1} K ⟶ K`,  `K ∈ D(Y_étale, Λ)`,
>
> obtained by applying Stacks `0GKG` and `0GKH` to `f` and the canonical weighting of Stacks
> `0F3D`. It is a natural transformation of endofunctors of `D(Y_étale, Λ)`, so the example's
> "functorial for `K`" is built into the datum; it is stated separately as
> `AlgebraicGeometry.SmallEtale.flatQuasiFiniteTrace_naturality`.

```lean
def flatQuasiFiniteTrace :
    (pullbackMod.{u, u + 1, u} B Λ f).mapDerivedCategory ⋙
        (fShriekMod.{u, u + 1, u} B Λ f).mapDerivedCategory ⟶
      𝟭 (DerivedCategory (ModuleSheaf.{u, u + 1, u} B Y Λ))
```

**`AlgebraicGeometry.SmallEtale.flatQuasiFiniteTrace_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L166). The attribute's comment: “the example's `functorial for K in D(Y_étale, Λ)`, for the trace maps attached to the canonical weighting”.

> **Stacks Project, Example 0GKI: the trace maps are functorial in `K`.**

```lean
theorem flatQuasiFiniteTrace_naturality
    {K K' : DerivedCategory (ModuleSheaf.{u, u + 1, u} B Y Λ)} (ψ : K ⟶ K') :
    ((pullbackMod.{u, u + 1, u} B Λ f).mapDerivedCategory ⋙
          (fShriekMod.{u, u + 1, u} B Λ f).mapDerivedCategory).map ψ ≫
        (flatQuasiFiniteTrace.{u, t} B Λ f).app K' =
      (flatQuasiFiniteTrace.{u, t} B Λ f).app K ≫ ψ
```

**`AlgebraicGeometry.SmallEtale.flatQuasiFiniteTrace_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L217). The attribute's comment: “the example's `compatible with arbitrary base change`, for the trace maps attached to the canonical weighting. Both sides are traces of the example: the `f'` side is the trace attached to the canonical weighting of `f'` itself, not to the restricted weight that 0GKH part (2) delivers, the two being identified by `AlgebraicGeometry.flatQuasiFiniteWeight_of_isPullback` -- the example's closing claim that `w` restricts to the canonical weighting of `f'`”. References: SGA 4 XVII (6.2.3), “more general”; SGA 4 XVII (6.2.5), “special case”.

> **Stacks Project, Example 0GKI: the trace maps are compatible with arbitrary base change.**
> Let
>
> ```
> X' --p--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> be cartesian. Then `f'` is again flat, locally quasi-finite and locally of finite presentation,
> so it has its own canonical weighting, and the square formed by the base-change comparison
> `g^{-1} f_! ≅ f'_! p^{-1}` of Stacks `0F5J`, the comparison of the two iterated inverse images,
> and the two trace maps of the example commutes.
>
> The statement is the base-change clause of
> `AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod_spec` with the weighting on the `f'` side
> replaced by the canonical weighting of `f'`. That replacement is exactly the example's closing
> remark that `w` restricts to the canonical weighting of `f'`, which is
> `AlgebraicGeometry.flatQuasiFiniteWeight_of_isPullback`.

```lean
theorem flatQuasiFiniteTrace_baseChange :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    letI := locallyQuasiFinite_of_isPullback B p f' f g sq
    letI : Flat (B.inclusion.map f') :=
      MorphismProperty.of_isPullback (sq.map B.inclusion) inferInstance
    letI : LocallyOfFinitePresentation (B.inclusion.map f') :=
      MorphismProperty.of_isPullback (sq.map B.inclusion) inferInstance
    NatTrans.mapDerivedCategory
          (traceBaseChangeComparison.{u, u + 1, u} B Λ f' f (pullbackMod.{u, u + 1, u} B Λ f)
            (pullbackMod.{u, u + 1, u} B Λ f') (pullbackMod.{u, u + 1, u} B Λ g)
            (pullbackMod.{u, u + 1, u} B Λ p) (fShriekBaseChangeMod.{u} B Λ p f' f g sq)
            (inverseImageSquareMod.{u} B Λ p f' f g sq)).hom ≫
        (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
          (pullbackMod.{u, u + 1, u} B Λ g)
          (pullbackMod.{u, u + 1, u} B Λ f' ⋙ fShriekMod.{u, u + 1, u} B Λ f')).hom ≫
        Functor.whiskerLeft (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory
          (NatTrans.mapDerivedCategory
            (weightedTraceModTrans.{u, u + 1, u} B Λ f'
              (flatQuasiFiniteWeight_isWeighting (B.inclusion.map f')))) ≫
        (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
          (pullbackMod.{u, u + 1, u} B Λ g)
          (𝟭 (ModuleSheaf.{u, u + 1, u} B Y' Λ))).inv =
      (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
          (pullbackMod.{u, u + 1, u} B Λ f ⋙ fShriekMod.{u, u + 1, u} B Λ f)
          (pullbackMod.{u, u + 1, u} B Λ g)).hom ≫
        Functor.whiskerRight
          (NatTrans.mapDerivedCategory (weightedTraceModTrans.{u, u + 1, u} B Λ f
            (flatQuasiFiniteWeight_isWeighting (B.inclusion.map f))))
          (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory ≫
        (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
          (𝟭 (ModuleSheaf.{u, u + 1, u} B Y Λ))
          (pullbackMod.{u, u + 1, u} B Λ g)).inv
```

**`AlgebraicGeometry.SmallEtale.flatQuasiFiniteWeight_and_flatQuasiFiniteTrace_allClauses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L302). The attribute's comment: “the example in full, as one conjunction in its own order: (1) positivity and (2) the weighting property of the function `w` of the displayed formula, which is the example's `canonical positive weighting`; (3) functoriality in `K` and (4) compatibility with the arbitrary base change, for the family `Tr_{f, K} : f_! f^{-1} K ⟶ K` of `AlgebraicGeometry.SmallEtale.flatQuasiFiniteTrace`; (5) that the base change `f'` is again flat, locally quasi-finite and locally of finite presentation; and (6) that `w` restricts along `p` to the canonical weighting of `f'`. The trace maps themselves are data, so they enter by name: the conjunction asserts every property the example asserts of them.”. References: SGA 4 XVII (6.2.3), “more general”; SGA 4 XVII (6.2.5), “special case”.

> **Stacks Project, Example 0GKI, in full.** For `f : X ⟶ Y` flat, locally quasi-finite and
> locally of finite presentation, a ring `Λ`, and an arbitrary cartesian square
>
> ```
> X' --p--> X
> |f'       |f
> Y' --g--> Y
> ```
>
> the six conjuncts are, in the example's own order:
>
> 1. the function `w = flatQuasiFiniteWeight f` of the displayed formula is strictly positive, and
> 2. is a weighting of `f` — together, the example's "canonical positive weighting";
> 3. the family `flatQuasiFiniteTrace` of trace maps `Tr_{f, K} : f_! f^{-1} K ⟶ K` is functorial
>    for `K` in `D(Y_étale, Λ)`, and
> 4. compatible with the base change, which being arbitrary gives "compatible with arbitrary base
>    change";
> 5. `f'` is again flat, locally quasi-finite and locally of finite presentation; and
> 6. `w` restricts along `p` to the canonical weighting of `f'`.
>
> The trace maps themselves are data, so they enter the conjunction by name rather than as an
> existential: every property the example asserts of them is asserted here of
> `AlgebraicGeometry.SmallEtale.flatQuasiFiniteTrace`.
>
> Neither side of conjunct 4 can be written down without the four instances of `f'`, so the
> statement binds them in a `letI` block; each is the proof conjunct 5 asserts, so nothing beyond
> the example's hypotheses is assumed, and the elaborated statement carries no binder for them.

```lean
theorem flatQuasiFiniteWeight_and_flatQuasiFiniteTrace_allClauses :
    -- the canonical positive weighting `w` of the example
    (∀ x, 0 < flatQuasiFiniteWeight (B.inclusion.map f) x) ∧
    IsWeighting (B.inclusion.map f) (flatQuasiFiniteWeight (B.inclusion.map f)) ∧
    -- the trace maps are functorial for `K` in `D(Y_étale, Λ)`
    (∀ (K K' : DerivedCategory (ModuleSheaf.{u, u + 1, u} B Y Λ)) (ψ : K ⟶ K'),
        ((pullbackMod.{u, u + 1, u} B Λ f).mapDerivedCategory ⋙
              (fShriekMod.{u, u + 1, u} B Λ f).mapDerivedCategory).map ψ ≫
            (flatQuasiFiniteTrace.{u, t} B Λ f).app K' =
          (flatQuasiFiniteTrace.{u, t} B Λ f).app K ≫ ψ) ∧
    -- and compatible with the arbitrary base change
    (letI := locallyOfFiniteType_of_isPullback B p f' f g sq
     letI := locallyQuasiFinite_of_isPullback B p f' f g sq
     letI : Flat (B.inclusion.map f') :=
       MorphismProperty.of_isPullback (sq.map B.inclusion) inferInstance
     letI : LocallyOfFinitePresentation (B.inclusion.map f') :=
       MorphismProperty.of_isPullback (sq.map B.inclusion) inferInstance
     NatTrans.mapDerivedCategory
           (traceBaseChangeComparison.{u, u + 1, u} B Λ f' f (pullbackMod.{u, u + 1, u} B Λ f)
             (pullbackMod.{u, u + 1, u} B Λ f') (pullbackMod.{u, u + 1, u} B Λ g)
             (pullbackMod.{u, u + 1, u} B Λ p) (fShriekBaseChangeMod.{u} B Λ p f' f g sq)
             (inverseImageSquareMod.{u} B Λ p f' f g sq)).hom ≫
         (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
           (pullbackMod.{u, u + 1, u} B Λ g)
           (pullbackMod.{u, u + 1, u} B Λ f' ⋙ fShriekMod.{u, u + 1, u} B Λ f')).hom ≫
         Functor.whiskerLeft (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory
           (NatTrans.mapDerivedCategory
             (weightedTraceModTrans.{u, u + 1, u} B Λ f'
               (flatQuasiFiniteWeight_isWeighting (B.inclusion.map f')))) ≫
         (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
           (pullbackMod.{u, u + 1, u} B Λ g)
           (𝟭 (ModuleSheaf.{u, u + 1, u} B Y' Λ))).inv =
       (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
           (pullbackMod.{u, u + 1, u} B Λ f ⋙ fShriekMod.{u, u + 1, u} B Λ f)
           (pullbackMod.{u, u + 1, u} B Λ g)).hom ≫
         Functor.whiskerRight
           (NatTrans.mapDerivedCategory (weightedTraceModTrans.{u, u + 1, u} B Λ f
             (flatQuasiFiniteWeight_isWeighting (B.inclusion.map f))))
           (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory ≫
         (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
           (𝟭 (ModuleSheaf.{u, u + 1, u} B Y Λ))
           (pullbackMod.{u, u + 1, u} B Λ g)).inv) ∧
    -- any base change of `f` satisfies the same three properties
    (Flat (B.inclusion.map f') ∧ LocallyQuasiFinite (B.inclusion.map f') ∧
      LocallyOfFinitePresentation (B.inclusion.map f')) ∧
    -- and `w` restricts to the canonical weighting of `f'`
    flatQuasiFiniteWeight (B.inclusion.map f') =
      flatQuasiFiniteWeight (B.inclusion.map f) ∘ (B.inclusion.map p)
```

**`AlgebraicGeometry.flatQuasiFiniteWeight_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLengthBaseChange.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLengthBaseChange.lean#L203). The attribute's comment: “the final claim: any base change `f'` of `f` satisfies the same three hypotheses -- which is `AlgebraicGeometry.Flat.isStableUnderBaseChange`, `AlgebraicGeometry.locallyQuasiFinite_isStableUnderBaseChange` and `AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange`, recorded on the tag in `StacksFrontier.AlgebraicGeometry.Spaces.Groupoids.WeightingBaseChange` -- and that the canonical weighting `w` of the example restricts along the projection to the canonical weighting of `f'`”.

> **Stacks Project, Example 0GKI, final claim.** Let `f : X ⟶ Y` be flat, locally quasi-finite
> and locally of finite presentation and let `f' : X' ⟶ Y'` be a base change of `f` along
> `g : Y' ⟶ Y`, with `p : X' ⟶ X` the projection. Then the canonical weighting of `f'` is the
> restriction along `p` of the canonical weighting of `f`.
>
> The weight at a point is the length of the local ring of the scheme-theoretic fibre through it
> times the inseparable degree of the residue field extension. The comparison morphism of fibres
> `N` is flat, so Tag `02M1` splits the length upstairs as the length downstairs times the length
> of the local ring of the fibre of `N`, and
> `Stacks.Chow.length_fiberStalk_mul_finInsepDegree_of_isPullback` trades that last length against
> the two inseparable degrees.

```lean
theorem flatQuasiFiniteWeight_of_isPullback {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y)
    {p : X' ⟶ X} {f' : X' ⟶ Y'} {g : Y' ⟶ Y} (sq : IsPullback p f' f g)
    [LocallyQuasiFinite f] [LocallyOfFinitePresentation f] [Flat f] :
    flatQuasiFiniteWeight f' = flatQuasiFiniteWeight f ∘ p
```

Declarations registered for the tag:

- [`AlgebraicGeometry.flatQuasiFiniteWeight`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean#L960), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L103) (StacksFrontier): “the canonical positive weighting `w` of the example, given by the displayed formula -- the function itself”.
- [`AlgebraicGeometry.flatQuasiFiniteWeight_pos`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean#L1070), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L106) (StacksFrontier): “the canonical positive weighting `w` of the example -- positivity”.
- [`AlgebraicGeometry.flatQuasiFiniteWeight_isWeighting`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean#L1097), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/FlatQuasiFiniteTrace.lean#L109) (StacksFrontier): “the canonical positive weighting `w` of the example -- that it is a weighting of `f`, which the example cites More on Morphisms, Lemma 0F3D for”.
- [`AlgebraicGeometry.Flat.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean#L38) (StacksFrontier): “base\_change\_preserves\_hypotheses”. References: EGA III (7.7.2), “special case”; EGA III (7.9.7), “special case”; EGA IV (11.5.4), “necessity”; EGA IV (2.1.4); EGA IV (2.2.13), “(i)”; EGA IV (2.5.1), “special case”; EGA IV (20.6.9), “flatness of X' over S'”; EGA IV (21.15.9), “partial”; EGA IV (7.3.5), “partial”; SGA 3 III (0.13), “partial”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (11.1); SGA 3 VIB (2.1.2), “partial”; SGA 3 VIB (3.11), “fiber-flatness”; SGA 3 VIIB (1.3.3), “(iii), special case”; SGA 3 XIX (2.1); SGA 4 Vbis (3.3), “special case”; SGA 6 0 (2.9), “special case”; SGA 6 XII (2.3), “(a)”; SGA 6 XII (4.1), “(1)”; SGA 7 VII (1.3.8), “partial”.
- [`AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean#L40) (StacksFrontier): “base\_change\_preserves\_hypotheses”. References: EGA I (10.13.5), “(ii)”; EGA I (6.3.4), “clause (iv)”; EGA I (6.6.6); EGA II (3.5.5), “partial”; EGA IV (1.3.4); EGA IV (2.7.1), “(iii)”; SGA 3 VIB (2.1.2), “partial”.
- [`AlgebraicGeometry.instIsStableUnderBaseChangeSchemeLocallyQuasiFinite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instIsStableUnderBaseChangeSchemeLocallyQuasiFinite#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean#L43) (StacksFrontier): “base\_change\_preserves\_hypotheses”. References: EGA II (6.2.4), “(iii)”; SGA 3 V (7.4), “special case”; SGA 3 VIB (10.1), “sufficiency”; SGA 3 VIB (2.8), “(i) ⇒ (ii), partial”.
- [`AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/WeightingBaseChange.lean#L46) (StacksFrontier): “base\_change\_preserves\_hypotheses”. References: EGA IV (1.4.3); EGA IV (2.7.1), “(iv)”; EGA IV (20.6.9), “partial”; EGA IV (21.15.9), “partial”; EGA IV (8.6.2), “partial”; SGA 3 VIB (5.6.1.0), “partial”.

## Tag 0GL4, a remark

[Tag 0GL4](https://stacks.math.columbia.edu/tag/0GL4) in the Stacks Project.

**`AlgebraicGeometry.flatQuasiFiniteWeight_eq_one_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleCanonicalWeighting.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleCanonicalWeighting.lean#L101). The attribute's comment: “The canonical weighting of Example 0GKI is identically 1 for an étale morphism — the computation that makes its trace map the counit of `j_! ⊣ j^{-1}`. The remark's own equality of the two morphisms is `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit` in `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.EtaleTraceIsCounit`, which uses this computation together with the stalk characterisation of Lemma 0GKG.”.

> **Stacks 0GL4.** The canonical weighting of Stacks 0F3D, for an étale morphism of schemes,
> takes the value `1` at every point of the source.
>
> This is the reason the trace map of Example 0GKI for an étale `j : U ⟶ X` is the counit of the
> adjunction `j_! ⊣ j^{-1}`: the trace for a weighting `w` acts on the stalk
> `(j_! j^{-1}ℱ)_ȳ = ⨁_{j(x̄) = ȳ} ℱ_ȳ` by multiplication by `w(x̄)` on the summand indexed by
> `x̄`, so for `w = 1` it is the sum map, which is the counit.

```lean
theorem flatQuasiFiniteWeight_eq_one_of_etale (u : U) :
    flatQuasiFiniteWeight j u = 1
```

**`AlgebraicGeometry.flatQuasiFiniteWeight_etale_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleCanonicalWeighting.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleCanonicalWeighting.lean#L128). The attribute's comment: “The canonical weighting of Example 0GKI is identically 1 for an étale morphism, as an equality of functions. Same scope as `AlgebraicGeometry.flatQuasiFiniteWeight_eq_one_of_etale`; the remark's equality of the trace with the counit is `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit`.”.

> **Stacks 0GL4.** The canonical weighting of an étale morphism is the constant function
> `1`, as an equality of functions `U → ℤ`.

```lean
theorem flatQuasiFiniteWeight_etale_eq_one : flatQuasiFiniteWeight j = 1
```

**`AlgebraicGeometry.etaleCanonicalTrace_eq_comparison_comp_abelianTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean#L136). The attribute's comment: “The Étale Cohomology, Section 03SH half of the remark: the counit of `j_! ⊣ j^{-1}` is the morphism already called the trace there, namely the trace map of Stacks 03SE read through the comparison `j_! ⟶ j_*`. Stated for a FINITE étale `j`, because that is where the 03SE trace is defined in this library. The remark's own equality — counit versus the trace map of Example 0GKI — is `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit` in `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.EtaleTraceIsCounit`.”.

> For a finite étale `j` the trace map of Stacks 03SE is defined on `j_* j^{-1}` rather than on
> `j_! j^{-1}`, through the comparison isomorphism `j_! ≅ j_*`. Composing the comparison with it
> returns the counit: the morphism for which the terminology "trace" was already used in Étale
> Cohomology, Section 03SH is the counit of `j_! ⊣ j^{-1}`.

```lean
theorem etaleCanonicalTrace_eq_comparison_comp_abelianTrace :
    etaleCanonicalTrace B X hX U =
      Functor.whiskerLeft (abelianRestriction B X hX U)
        (abelianExtensionByZeroToPushforward B X hX U) ≫ abelianTrace B X hX U
```

**`AlgebraicGeometry.moduleEtaleCanonicalTrace_eq_comparison_comp_moduleTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceCounit.lean#L198). The attribute's comment: “The Étale Cohomology, Section 03SH half of the remark on sheaves of `Λ`-modules: the counit of `j_! ⊣ j^{-1}` is the morphism already called the trace there, namely the trace map of Stacks 03SE read through the comparison `j_! ⟶ j_*`. Stated for a FINITE étale `j`, where the 03SE trace is defined. The remark's own equality against the trace map of Example 0GKI, with abelian coefficients, is `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit`.”.

> On sheaves of `Λ`-modules: for a finite étale `j`, composing the comparison `j_! ⟶ j_*` with
> the trace map of Stacks 03SE returns the counit of `j_! ⊣ j^{-1}`.

```lean
theorem moduleEtaleCanonicalTrace_eq_comparison_comp_moduleTrace :
    moduleEtaleCanonicalTrace B X hX U Λ =
      Functor.whiskerLeft (moduleRestriction B X hX U Λ)
        (moduleExtensionByZeroToPushforward B X hX U Λ) ≫ moduleTrace B X hX U Λ
```

**`AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounit.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounit.lean#L290). The attribute's comment: “For an abelian étale sheaf `ℱ`: a morphism `j_! j^{-1}ℱ ⟶ ℱ` has the behaviour on geometric stalks by which Lemma 0GKG characterises the trace map of Example 0GKI, for the canonical weighting of Stacks 0F3D, exactly when it is the counit of the adjunction `j_! ⊣ j^{-1}`. The forward implication is the remark's equality; the backward implication produces the trace map, so nothing about it is assumed.”. References: SGA 4 XVII (6.2.11), “more general”; SGA 4 XVIII (3.1.8), “(iii), special case”; SGA 4½ Dualite (2.3), “special case”.

> For an étale morphism `j : U ⟶ X` the trace map `Tr : j_! j^{-1}ℱ ⟶ ℱ` of Example 0GKI is
> the counit of the adjunction between `j_!` and `j^{-1}`.
>
> The trace map of Example 0GKI is the morphism Stacks 0GKG attaches to the canonical weighting of
> Stacks 0F3D, characterised by its behaviour on geometric stalks; so the identification is stated
> as an equivalence: a morphism `j_! j^{-1}ℱ ⟶ ℱ` has that behaviour exactly when it is the
> counit. The forward direction is the remark's equality and the backward direction produces the
> trace map.

```lean
public theorem hasWeightedTraceStalks_iff_eq_counit
    (τ : (SmallEtale.fShriekFunctor.{u, u + 1} B U.obj.hom).obj
      ((SmallEtale.abPullback.{u, u + 1} B U.obj.hom).obj F) ⟶ F) :
    SmallEtale.HasWeightedTraceStalks.{u, u + 1} B U.obj.hom
        (flatQuasiFiniteWeight (B.inclusion.map U.obj.hom)) F τ ↔
      τ = (etaleFShriekAbPullbackAdjunction B X hX U).counit.app F
```

**`AlgebraicGeometry.derivedWeightedTraceFamily_eq_derivedCounit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean#L316). The attribute's comment: “At derived coefficients, on the unbounded derived category of abelian étale sheaves: for an étale j the derived form of the family of trace maps of Example 0GKI -- each of them characterised on geometric stalks by Lemma 0GKG for the canonical weighting of 0F3D -- is the counit of the adjunction between the derived functors of j\_! and j^\{-1}, which is the derived form of the adjunction of Stacks 03S3. Both descents are constructed here: the trace by `CategoryTheory.NatTrans.mapDerivedCategoryCompToId` as in 0GKH part (3), the adjunction by `CategoryTheory.Adjunction.mapDerivedCategory`, and they are compared by the coherence lemma `CategoryTheory.Adjunction.mapDerivedCategory_counit`. The sheaf-level input is `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit`. Coefficients in AddCommGrpCat.\{u + 1}, the universe at which 03S3 is available here; the universe of the derived category is arbitrary.”.

> **Stacks 0GL4 on the unbounded derived category of abelian étale sheaves.** Let
> `j : U ⟶ X` be étale and let `τ` be the family of trace maps of Example 0GKI, that is a morphism
> `j_! j^{-1}ℱ ⟶ ℱ` for each abelian étale sheaf `ℱ` on `X` with the behaviour on geometric stalks
> by which Lemma 0GKG characterises the trace for the canonical weighting of Stacks 0F3D. Both
> `j_!` and `j^{-1}` are exact, so the family descends to a natural transformation
> `j_! j^{-1} ⟶ id` of the unbounded derived category, and the adjunction of Stacks 03S3 descends
> to an adjunction of the descended functors. Then the descended trace is the counit of the
> descended adjunction.
>
> The weighting hypothesis of Stacks 0GKG is not needed and the trace maps are not assumed to
> exist: the counit itself is such a family, by
> `AlgebraicGeometry.hasWeightedTraceStalks_counit`.

```lean
public theorem derivedWeightedTraceFamily_eq_derivedCounit :
    NatTrans.mapDerivedCategoryCompToId (abPullback.{u, u + 1} B U.obj.hom)
        (fShriekFunctor.{u, u + 1} B U.obj.hom)
        (weightedTraceFamilyNatTrans.{u, u + 1} B U.obj.hom
          (flatQuasiFiniteWeight (B.inclusion.map U.obj.hom)) τ hτ) =
      (Adjunction.mapDerivedCategory (etaleFShriekAbPullbackAdjunction B X hX U)).counit
```

**`AlgebraicGeometry.hasWeightedTraceStalksMod_iff_eq_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean#L464). The attribute's comment: “At Lambda-coefficients on a single sheaf of Lambda-modules, for an arbitrary ring Lambda: a morphism j\_!j^\{-1}M ⟶ M of sheaves of Lambda-modules is the trace map of 0GKH part (3) for the canonical weighting of 0F3D -- its underlying morphism of abelian sheaves having the behaviour on geometric stalks prescribed by 0GKG -- if and only if it is the counit of the Lambda-linear adjunction `AlgebraicGeometry.SmallEtale.etaleFShriekModPullbackAdjunction` at M. The backward direction is the existence of the trace map at Lambda-coefficients, the forward direction is the remark. The Lambda-linear form of `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit`.”. References: SGA 4 IX (5.1), “more general”; SGA 4 XVII (6.2.11), “more general”; SGA 4 XVIII (3.1.8), “(iii), special case”; SGA 4½ Dualite (2.3), “special case”.

> **Stacks 0GL4 at `Λ`-coefficients, on a single sheaf of `Λ`-modules.** For an étale `j`, a
> ring `Λ` and a sheaf of `Λ`-modules `M` on the small étale site of `X`, a morphism
> `τ : j_! j^{-1}M ⟶ M` is the trace map of Stacks 0GKH part (3) for the canonical weighting of
> `j` — that is, the morphism of abelian sheaves underlying it has the behaviour on geometric
> stalks prescribed by Lemma 0GKG — if and only if it is the counit of the `Λ`-linear adjunction
> `j_! ⊣ j^{-1}` at `M`. The backward direction produces the trace map, so the equivalence also
> says that the trace map exists.

```lean
public theorem hasWeightedTraceStalksMod_iff_eq_counit
    (M : ModuleSheaf.{u, u + 1, u} B (B.obj X hX) Λ)
    (τ : (fShriekMod.{u, u + 1, u} B Λ U.obj.hom).obj
      ((pullbackMod.{u, u + 1, u} B Λ U.obj.hom).obj M) ⟶ M) :
    HasWeightedTraceStalksMod.{u, u + 1, u} B Λ U.obj.hom
        (pullbackMod.{u, u + 1, u} B Λ U.obj.hom)
        (pullbackModForgetIso.{u, u + 1, u} B Λ U.obj.hom)
        (flatQuasiFiniteWeight (B.inclusion.map U.obj.hom)) M τ ↔
      τ = (etaleFShriekModPullbackAdjunction B X hX U Λ).counit.app M
```

**`AlgebraicGeometry.derivedWeightedTraceMod_eq_derivedCounit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean#L661). The attribute's comment: “At the derived coefficients of the remark, D(X\_etale, Lambda) for an arbitrary ring Lambda: for an étale j the derived trace Tr\_\{j,w} of 0GKH part (3) -- `AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod` for the canonical weighting of 0F3D -- is the counit of the adjunction between the derived functors of the Lambda-linear j\_! and j^\{-1}, so for each K in D(X\_etale, Lambda) the morphism Tr\_\{j,w,K} : j\_!j^\{-1}K ⟶ K is the counit at K. Every object the statement names is constructed and nothing is quantified over: the derived trace is `AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod`, the derived form of the sheaf-level `AlgebraicGeometry.SmallEtale.weightedTraceMod`, which is the trace of 0GKG by `AlgebraicGeometry.SmallEtale.weightedTraceMod_hasWeightedTraceStalksMod` and the unique such morphism by `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalksMod_unique`; the Lambda-linear inverse image is `AlgebraicGeometry.SmallEtale.pullbackMod`, the lift of the abelian j^\{-1} of 03Q1; the Lambda-linear adjunction is `AlgebraicGeometry.SmallEtale.etaleFShriekModPullbackAdjunction`, the lift of the abelian adjunction of 03S3, whose counit is the abelian counit on underlying abelian sheaves by `AlgebraicGeometry.SmallEtale.forgetModuleSheaf_map_etaleFShriekModPullbackAdjunction_counit`; and the weighting is the canonical one of 0F3D, a weighting by `AlgebraicGeometry.flatQuasiFiniteWeight_isWeighting`. The identification of the derived trace with the derived counit comes from the abelian case `AlgebraicGeometry.hasWeightedTraceStalks_iff_eq_counit` through the coherence lemma `CategoryTheory.Adjunction.mapDerivedCategory_counit`, which says that the counit of a derived adjunction is the derived counit, and the sheaf-level trace is the counit by `AlgebraicGeometry.hasWeightedTraceStalksMod_counit_etale` with the uniqueness of 0GKG at Lambda-coefficients. Coefficient universes ModuleSheaf.\{u, u+1, u} with Lambda : Type u, those of 0GKH part (3); the universe of the derived category is arbitrary.”. References: SGA 4 XVII (6.2.11), “more general”; SGA 4 XVIII (3.1.8), “(iii), special case”; SGA 4½ Dualite (2.3), “special case”.

> **Stacks 0GL4 on `D(X_étale, Λ)`.** Let `j : U ⟶ X` be étale and let `Λ` be a ring. The
> derived trace `Tr_{j, w} : j_! j^{-1} ⟶ id` of `D(X_étale, Λ)` of Stacks 0GKH part (3), for the
> canonical weighting `w` of `j` of Stacks 0F3D, is the counit of the adjunction between the
> derived functors of the `Λ`-linear `j_!` and `j^{-1}`.
>
> Every object in the statement is constructed. The trace is
> `AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod`, the derived form of the sheaf-level
> trace `AlgebraicGeometry.SmallEtale.weightedTraceMod`, which has at each sheaf of `Λ`-modules
> the behaviour on geometric stalks by which Lemma 0GKG characterises the trace — that is
> `AlgebraicGeometry.SmallEtale.weightedTraceMod_hasWeightedTraceStalksMod` — and is by
> `AlgebraicGeometry.SmallEtale.hasWeightedTraceStalksMod_unique` the only such morphism, so it is
> *the* trace map and `Tr_{j, w}` is *the* derived trace rather than one of a family of candidates.
> The `Λ`-linear inverse image is `AlgebraicGeometry.SmallEtale.pullbackMod` and the `Λ`-linear
> adjunction `AlgebraicGeometry.SmallEtale.etaleFShriekModPullbackAdjunction`, the lift of the
> adjunction of Stacks 03S3, whose counit is the abelian counit on underlying abelian sheaves by
> `AlgebraicGeometry.SmallEtale.forgetModuleSheaf_map_etaleFShriekModPullbackAdjunction_counit`;
> the weighting is the canonical one, a weighting by
> `AlgebraicGeometry.flatQuasiFiniteWeight_isWeighting`.
>
> This is `AlgebraicGeometry.derivedWeightedTrace_pullbackMod_eq_derivedCounit`, which leaves the
> trace family general, instantiated at that constructed trace.

```lean
public theorem derivedWeightedTraceMod_eq_derivedCounit :
    SmallEtale.derivedWeightedTraceMod.{u, u + 1, t, u} B Λ U.obj.hom
        (flatQuasiFiniteWeight_isWeighting (B.inclusion.map U.obj.hom)) =
      (Adjunction.mapDerivedCategory
        (etaleFShriekModPullbackAdjunction B X hX U Λ)).counit
```

**`AlgebraicGeometry.derivedWeightedTraceMod_app_eq_derivedCounit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean, line 686](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/EtaleTraceIsCounitDerived.lean#L686). The attribute's comment: “At a fixed object K of D(X\_etale, Lambda) for an arbitrary ring Lambda, which is how the remark reads: for an étale j the trace map Tr\_\{j,w,K} : j\_!j^\{-1}K ⟶ K of 0GKH part (3) -- the component at K of `AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod` for the canonical weighting of 0F3D -- is the counit at K of the adjunction between the derived functors of the Lambda-linear j\_! and j^\{-1}. The trace, the two functors and the adjunction are all constructed and nothing is quantified over; this is the component form of `AlgebraicGeometry.derivedWeightedTraceMod_eq_derivedCounit`.”. References: SGA 4 XVIII (3.1.8), “(iii), special case”.

> **Stacks 0GL4 on `D(X_étale, Λ)`, at a fixed object.** For an étale `j`, a ring `Λ` and an
> object `K` of `D(X_étale, Λ)`, the trace map `Tr_{j, w, K} : j_! j^{-1}K ⟶ K` of Stacks 0GKH
> part (3), for the canonical weighting `w` of `j`, is the counit at `K` of the adjunction between
> the derived functors of the `Λ`-linear `j_!` and `j^{-1}`. This is the form in which the remark
> reads, and it is the component at `K` of
> `AlgebraicGeometry.derivedWeightedTraceMod_eq_derivedCounit`.

```lean
public theorem derivedWeightedTraceMod_app_eq_derivedCounit_app
    (K : DerivedCategory (ModuleSheaf.{u, u + 1, u} B (B.obj X hX) Λ)) :
    (SmallEtale.derivedWeightedTraceMod.{u, u + 1, t, u} B Λ U.obj.hom
          (flatQuasiFiniteWeight_isWeighting (B.inclusion.map U.obj.hom))).app K =
      (Adjunction.mapDerivedCategory
        (etaleFShriekModPullbackAdjunction B X hX U Λ)).counit.app K
```

## Tag 0GKJ, an example

[Tag 0GKJ](https://stacks.math.columbia.edu/tag/0GKJ) in the Stacks Project.

**`AlgebraicGeometry.exists_weighting_genericSeparableDegree_of_isGeometricallyUnibranch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceLocallyQuasiFinite.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceLocallyQuasiFinite.lean#L144). The attribute's comment: “the weighting of the example, with the sign the cited lemma gives: a locally quasi-finite morphism locally of finite type onto a geometrically unibranch locally Noetherian base carries a weighting w, nonnegative, equal at each point to the generic separable degree of the strict henselizations, and restricting along every base change of f to a weighting there. Nonnegative and not positive is what the source's own citation 0F3E gives, and 0F3C forbids more for an f that is not universally open. The trace maps Tr\_\{f, w, K} that the example then reads off 0GKG and 0GKH for this f and w are not asserted here; they come from `AlgebraicGeometry.SmallEtale.weightedTrace` and 0GKH, both of which are about an arbitrary weighting and not about this example's hypotheses. The whole example, this weighting together with its trace maps on abelian sheaves and on D(Y\_étale, Λ), is the theorem `exists_weighting_derivedWeightedTraceMod_of_isGeometricallyUnibranch` of the namespace `AlgebraicGeometry.SmallEtale`”.

> A locally quasi-finite morphism locally of finite type onto a geometrically unibranch
> locally Noetherian scheme carries an integer-valued weighting `w` which is nonnegative, whose
> restriction along an arbitrary base change of `f` is a weighting of that base change, and whose
> value at a point `x` is the generic separable degree of the strict henselization of the local
> ring at `x` over the strict henselization of the local ring at `f x` — the number of geometric
> points of the generic fibre of `Spec O_{X, x}^{sh} ⟶ Spec O_{Y, f(x)}^{sh}`, which is how
> Stacks 0GKJ describes it.
>
> The last conjunct is the description quantified over all compatible choices of strict
> henselizations, of the minimal prime of the one downstairs and of an algebraic closure of its
> residue field, exactly as in `AlgebraicGeometry.exists_weighting_genericSeparableDegree`, so no
> choice of henselization is built into the statement.
>
> `0 ≤ w x` is all the sign information there is, and the source's word *positive* cannot be
> taken literally: see the implementation notes and
> `AlgebraicGeometry.not_exists_positive_weighting_of_not_universallyOpen`.

```lean
public theorem exists_weighting_genericSeparableDegree_of_isGeometricallyUnibranch
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    [IsLocallyNoetherian Y] (hY : IsGeometricallyUnibranch Y) :
    ∃ w : X → ℤ,
      IsWeighting f w ∧
      (∀ x : X, 0 ≤ w x) ∧
      (∀ (X' Y' : Scheme.{u}) (q : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y),
        IsPullback q f' f g → IsWeighting f' (w ∘ q)) ∧
      ∀ (x : X)
        (κY : Type u) [Field κY]
        [Algebra (maximalIdeal (Y.presheaf.stalk (f x))).ResidueField κY]
        [IsSepClosure (maximalIdeal (Y.presheaf.stalk (f x))).ResidueField κY]
        (Rsh : Type u) [CommRing Rsh] [IsLocalRing Rsh]
        [Algebra (Y.presheaf.stalk (f x)) Rsh]
        (_hRsh : Stacks.StrictHenselization.IsStrictHenselization
          (Y.presheaf.stalk (f x)) κY Rsh)
        (κX : Type u) [Field κX]
        [Algebra (maximalIdeal (X.presheaf.stalk x)).ResidueField κX]
        [IsSepClosure (maximalIdeal (X.presheaf.stalk x)).ResidueField κX]
        (Ssh : Type u) [CommRing Ssh] [IsLocalRing Ssh]
        [Algebra (X.presheaf.stalk x) Ssh] [Algebra Rsh Ssh]
        [Algebra (Y.presheaf.stalk (f x)) Ssh]
        [IsScalarTower (Y.presheaf.stalk (f x)) Rsh Ssh]
        (_hSsh : Stacks.StrictHenselization.IsStrictHenselization
          (X.presheaf.stalk x) κX Ssh)
        (_hcomp : (algebraMap (Y.presheaf.stalk (f x)) Ssh) =
          (algebraMap (X.presheaf.stalk x) Ssh).comp (f.stalkMap x).hom)
        (p : Ideal Rsh) [p.IsPrime] (_hp : p ∈ minimalPrimes Rsh)
        (Kbar : Type u) [Field Kbar]
        [Algebra p.ResidueField Kbar] [IsAlgClosure p.ResidueField Kbar],
        w x = (Nat.card (AlgHom p.ResidueField
          (TensorProduct Rsh p.ResidueField Ssh) Kbar) : ℤ)
```

**`AlgebraicGeometry.SmallEtale.exists_weighting_weightedTrace_of_isGeometricallyUnibranch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceQuasiFiniteUnibranch.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceQuasiFiniteUnibranch.lean#L111). The attribute's comment: “the example in the generality of arbitrary Λ-linear lifts, of which the form with every lift, comparison and trace family constructed, the faithful registration of 0GKJ, is `exists_weighting_derivedWeightedTraceMod_of_isGeometricallyUnibranch` in the namespace `AlgebraicGeometry.SmallEtale`: for the nonnegative generic-separable-degree weighting w of 0F3E, 0GKG and all three parts of 0GKH hold, the derived clause for every choice of Λ-linear inverse images, comparisons and trace families compatible with the abelian ones. The source's word *positive* is a slip for *nonnegative*: 0F3E, the lemma 0GKJ cites, gives Z\_\{≥0}, and `AlgebraicGeometry.exists_locallyQuasiFinite_isNormal_not_exists_positive_weighting` exhibits a morphism at these hypotheses with no positive weighting; 0GKG and 0GKH impose no sign condition on w, so this costs the trace maps nothing. The trace maps enter through the behaviour on geometric stalks by which 0GKG characterises them, whose uniqueness half is one of the clauses, and the Λ-linear inverse images and the comparisons attached to the cartesian square are quantified over as lifts of the abelian ones exactly as in `AlgebraicGeometry.SmallEtale.derivedWeightedTrace_spec_of_lifts`. The coefficient universe is AddCommGrpCat.\{u+1} with ModuleSheaf.\{u, u+1, u} and Λ : Type u, which is where 0F5J and hence parts (2) and (3) live. The first assertion on its own is `AlgebraicGeometry.exists_weighting_genericSeparableDegree_of_isGeometricallyUnibranch`.”. References: SGA 4 XVII (6.2.5), “special case”.

> **The trace maps of a locally quasi-finite morphism over a geometrically unibranch locally
> Noetherian base.** Let `f : X ⟶ Y` be a locally
> quasi-finite morphism of a big étale site, locally of finite type, with `Y` geometrically
> unibranch and locally Noetherian. Then there is an integer-valued function `w` on `X` such that:
>
> * `w` is a weighting of `f`, it is nonnegative, and its value at `x` is the generic separable
>   degree of the strict henselization of the local ring at `x` over the strict henselization of
>   the local ring at `f x`;
> * **Stacks 0GKG for `(f, w)`:** for every abelian sheaf `F` on the small étale site of `Y` there
>   is exactly one trace map `Tr_{f, w, F} : f_! f^{-1}F ⟶ F` with the behaviour on geometric
>   stalks that lemma prescribes, namely the weighted sum `(a_x̄)_x̄ ↦ ∑_x̄ w(x̄) · a_x̄` over the
>   geometric fibre;
> * **Stacks 0GKH part (1):** those trace maps are functorial in `F`;
> * **Stacks 0GKH part (2):** they are compatible with arbitrary base change — for a cartesian
>   square with horizontal morphisms `p : X' ⟶ X`, `g : Y' ⟶ Y`, the restriction `w ∘ p` is a
>   weighting of `f'` (with nothing assumed about `Y'`), the base change along `g` of a trace map
>   for `(f, w)` is a trace map for `(f', w ∘ p)`, and the square formed by the base-change
>   isomorphism `g^{-1}f_!G ≅ f'_!p^{-1}G` of Stacks 0F5J, the comparison
>   `p^{-1}f^{-1}F ≅ f'^{-1}g^{-1}F` of the two iterated inverse images, and the two trace maps
>   commutes;
> * **Stacks 0GKH part (3):** given a ring `Λ`, the trace maps induce on unbounded derived
>   categories a natural transformation `f_! f^{-1} ⟶ id` of `D(Y_étale, Λ)`, whose component at
>   `K` is `Tr_{f, w, K} : f_! f^{-1}K ⟶ K`; it is functorial in `K`, it restricts to the
>   sheaf-level trace, and it is compatible with arbitrary base change.
>
> The last clause quantifies over the `Λ`-linear inverse images along the four morphisms of the
> square and the two comparisons attached to it, each presented as a lift of its abelian
> counterpart, and over the families of `Λ`-linear trace maps characterised on geometric
> stalks.

```lean
public theorem exists_weighting_weightedTrace_of_isGeometricallyUnibranch
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyQuasiFinite (B.inclusion.map f)]
    [IsLocallyNoetherian Y.obj] (hY : IsGeometricallyUnibranch Y.obj) :
    ∃ w : X.obj → ℤ,
      -- the weighting of the first assertion, which the trace maps below belong to
      IsWeighting (B.inclusion.map f) w ∧
      (∀ x : X.obj, 0 ≤ w x) ∧
      (∀ (x : X.obj)
          (κY : Type u) [Field κY]
          [Algebra (maximalIdeal (Y.obj.presheaf.stalk (B.inclusion.map f x))).ResidueField κY]
          [IsSepClosure
            (maximalIdeal (Y.obj.presheaf.stalk (B.inclusion.map f x))).ResidueField κY]
          (Rsh : Type u) [CommRing Rsh] [IsLocalRing Rsh]
          [Algebra (Y.obj.presheaf.stalk (B.inclusion.map f x)) Rsh]
          (_hRsh : Stacks.StrictHenselization.IsStrictHenselization
            (Y.obj.presheaf.stalk (B.inclusion.map f x)) κY Rsh)
          (κX : Type u) [Field κX]
          [Algebra (maximalIdeal (X.obj.presheaf.stalk x)).ResidueField κX]
          [IsSepClosure (maximalIdeal (X.obj.presheaf.stalk x)).ResidueField κX]
          (Ssh : Type u) [CommRing Ssh] [IsLocalRing Ssh]
          [Algebra (X.obj.presheaf.stalk x) Ssh] [Algebra Rsh Ssh]
          [Algebra (Y.obj.presheaf.stalk (B.inclusion.map f x)) Ssh]
          [IsScalarTower (Y.obj.presheaf.stalk (B.inclusion.map f x)) Rsh Ssh]
          (_hSsh : Stacks.StrictHenselization.IsStrictHenselization
            (X.obj.presheaf.stalk x) κX Ssh)
          (_hcomp : algebraMap (Y.obj.presheaf.stalk (B.inclusion.map f x)) Ssh =
            (algebraMap (X.obj.presheaf.stalk x) Ssh).comp
              ((B.inclusion.map f).stalkMap x).hom)
          (q : Ideal Rsh) [q.IsPrime] (_hq : q ∈ minimalPrimes Rsh)
          (Kbar : Type u) [Field Kbar]
          [Algebra q.ResidueField Kbar] [IsAlgClosure q.ResidueField Kbar],
          w x = (Nat.card (AlgHom q.ResidueField
            (TensorProduct Rsh q.ResidueField Ssh) Kbar) : ℤ)) ∧
      -- Stacks 0GKG for `(f, w)`: the trace map exists and is unique
      (∀ F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1},
        ∃! τ : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F,
          HasWeightedTraceStalks.{u, u + 1} B f w F τ) ∧
      -- Stacks 0GKH part (1): functoriality in the abelian sheaf
      (∀ (F G : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1})
          (φ : F ⟶ G)
          (τF : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F)
          (τG : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj G) ⟶ G),
          HasWeightedTraceStalks.{u, u + 1} B f w F τF →
          HasWeightedTraceStalks.{u, u + 1} B f w G τG →
            (fShriekFunctor.{u, u + 1} B f).map ((abPullback.{u, u + 1} B f).map φ) ≫ τG =
              τF ≫ φ) ∧
      -- Stacks 0GKH part (2): compatibility with arbitrary base change
      (∀ (X' Y' : B.Scheme) (p : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y)
          (sq : IsPullback p f' f g)
          (F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1})
          (τ : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F),
          HasWeightedTraceStalks.{u, u + 1} B f w F τ →
          letI := locallyOfFiniteType_of_isPullback B p f' f g sq
          letI := locallyQuasiFinite_of_isPullback B p f' f g sq
          IsWeighting (B.inclusion.map f') (w ∘ B.inclusion.map p) ∧
          HasWeightedTraceStalks.{u, u + 1} B f' (w ∘ B.inclusion.map p)
              ((abPullback.{u, u + 1} B g).obj F)
              ((fShriekFunctor.{u, u + 1} B f').map
                  ((inverseImageSquareIso.{u} B p f' f g sq).inv.app F) ≫
                (fShriekBaseChangeNatIso.{u} B p f' f g sq).inv.app
                  ((abPullback.{u, u + 1} B f).obj F) ≫
                (abPullback.{u, u + 1} B g).map τ) ∧
            ∀ τ' : (fShriekFunctor.{u, u + 1} B f').obj
                ((abPullback.{u, u + 1} B f').obj ((abPullback.{u, u + 1} B g).obj F)) ⟶
                  (abPullback.{u, u + 1} B g).obj F,
              HasWeightedTraceStalks.{u, u + 1} B f' (w ∘ B.inclusion.map p)
                  ((abPullback.{u, u + 1} B g).obj F) τ' →
                (fShriekBaseChangeNatIso.{u} B p f' f g sq).hom.app
                    ((abPullback.{u, u + 1} B f).obj F) ≫
                  (fShriekFunctor.{u, u + 1} B f').map
                    ((inverseImageSquareIso.{u} B p f' f g sq).hom.app F) ≫ τ' =
                  (abPullback.{u, u + 1} B g).map τ) ∧
      -- Stacks 0GKH part (3): the trace on `D(Y_étale, Λ)`
      (∀ (Λ : Type u) [Ring Λ] (X' Y' : B.Scheme) (p : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y)
          (sq : IsPullback p f' f g),
        letI := locallyOfFiniteType_of_isPullback B p f' f g sq
        letI := locallyQuasiFinite_of_isPullback B p f' f g sq
        ∀ (modPullF : ModuleSheaf.{u, u + 1, u} B Y Λ ⥤ ModuleSheaf.{u, u + 1, u} B X Λ)
          (hpullF : modPullF ⋙ forgetModuleSheaf.{u, u + 1, u} B X Λ ≅
            forgetModuleSheaf.{u, u + 1, u} B Y Λ ⋙ abPullback.{u, u + 1} B f)
          (modPullF' : ModuleSheaf.{u, u + 1, u} B Y' Λ ⥤ ModuleSheaf.{u, u + 1, u} B X' Λ)
          (hpullF' : modPullF' ⋙ forgetModuleSheaf.{u, u + 1, u} B X' Λ ≅
            forgetModuleSheaf.{u, u + 1, u} B Y' Λ ⋙ abPullback.{u, u + 1} B f')
          (modPullG : ModuleSheaf.{u, u + 1, u} B Y Λ ⥤ ModuleSheaf.{u, u + 1, u} B Y' Λ)
          (hpullG : modPullG ⋙ forgetModuleSheaf.{u, u + 1, u} B Y' Λ ≅
            forgetModuleSheaf.{u, u + 1, u} B Y Λ ⋙ abPullback.{u, u + 1} B g)
          (modPullP : ModuleSheaf.{u, u + 1, u} B X Λ ⥤ ModuleSheaf.{u, u + 1, u} B X' Λ)
          (hpullP : modPullP ⋙ forgetModuleSheaf.{u, u + 1, u} B X' Λ ≅
            forgetModuleSheaf.{u, u + 1, u} B X Λ ⋙ abPullback.{u, u + 1} B p)
          (bcMod : fShriekMod.{u, u + 1, u} B Λ f ⋙ modPullG ≅
            modPullP ⋙ fShriekMod.{u, u + 1, u} B Λ f')
          (epsMod : modPullF ⋙ modPullP ≅ modPullG ⋙ modPullF')
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B X Λ)]
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B Y Λ)]
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B X' Λ)]
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B Y' Λ)],
          (∀ n : ModuleSheaf.{u, u + 1, u} B X Λ,
            (forgetModuleSheaf.{u, u + 1, u} B Y' Λ).map (bcMod.hom.app n) ≫
                (fShriekModForgetIso.{u, u + 1, u} B Λ f').hom.app (modPullP.obj n) ≫
                (fShriekFunctor.{u, u + 1} B f').map (hpullP.hom.app n) =
              hpullG.hom.app ((fShriekMod.{u, u + 1, u} B Λ f).obj n) ≫
                (abPullback.{u, u + 1} B g).map
                  ((fShriekModForgetIso.{u, u + 1, u} B Λ f).hom.app n) ≫
                (fShriekBaseChangeNatIso.{u} B p f' f g sq).hom.app
                  ((forgetModuleSheaf.{u, u + 1, u} B X Λ).obj n)) →
          (∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
            (forgetModuleSheaf.{u, u + 1, u} B X' Λ).map (epsMod.hom.app M) ≫
                hpullF'.hom.app (modPullG.obj M) ≫
                (abPullback.{u, u + 1} B f').map (hpullG.hom.app M) =
              hpullP.hom.app (modPullF.obj M) ≫
                (abPullback.{u, u + 1} B p).map (hpullF.hom.app M) ≫
                (inverseImageSquareIso.{u} B p f' f g sq).hom.app
                  ((forgetModuleSheaf.{u, u + 1, u} B Y Λ).obj M)) →
          ∀ (τ : ∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
              (fShriekMod.{u, u + 1, u} B Λ f).obj (modPullF.obj M) ⟶ M)
            (hτ : ∀ M, HasWeightedTraceStalksMod.{u, u + 1, u} B Λ f modPullF hpullF w M (τ M))
            (τ' : ∀ N : ModuleSheaf.{u, u + 1, u} B Y' Λ,
              (fShriekMod.{u, u + 1, u} B Λ f').obj (modPullF'.obj N) ⟶ N)
            (hτ' : ∀ N, HasWeightedTraceStalksMod.{u, u + 1, u} B Λ f' modPullF' hpullF'
              (w ∘ B.inclusion.map p) N (τ' N)),
            letI := additive_of_forgetModPullIso.{u, u + 1, u} B Λ f modPullF hpullF
            letI := preservesFiniteLimits_of_forgetModPullIso.{u, u + 1, u} B Λ f modPullF hpullF
            letI :=
              preservesFiniteColimits_of_forgetModPullIso.{u, u + 1, u} B Λ f modPullF hpullF
            letI := additive_of_forgetModPullIso.{u, u + 1, u} B Λ f' modPullF' hpullF'
            letI :=
              preservesFiniteLimits_of_forgetModPullIso.{u, u + 1, u} B Λ f' modPullF' hpullF'
            letI :=
              preservesFiniteColimits_of_forgetModPullIso.{u, u + 1, u} B Λ f' modPullF' hpullF'
            letI := additive_of_forgetModPullIso.{u, u + 1, u} B Λ g modPullG hpullG
            letI := preservesFiniteLimits_of_forgetModPullIso.{u, u + 1, u} B Λ g modPullG hpullG
            letI :=
              preservesFiniteColimits_of_forgetModPullIso.{u, u + 1, u} B Λ g modPullG hpullG
            letI := additive_of_forgetModPullIso.{u, u + 1, u} B Λ p modPullP hpullP
            letI := preservesFiniteLimits_of_forgetModPullIso.{u, u + 1, u} B Λ p modPullP hpullP
            letI :=
              preservesFiniteColimits_of_forgetModPullIso.{u, u + 1, u} B Λ p modPullP hpullP
            -- functoriality in `K`
            (∀ (K K' : DerivedCategory (ModuleSheaf.{u, u + 1, u} B Y Λ)) (ψ : K ⟶ K'),
                (modPullF.mapDerivedCategory ⋙
                    (fShriekMod.{u, u + 1, u} B Λ f).mapDerivedCategory).map ψ ≫
                    (derivedWeightedTrace.{u, u + 1, t, u} B Λ f modPullF hpullF w τ hτ).app K' =
                  (derivedWeightedTrace.{u, u + 1, t, u} B Λ f modPullF hpullF w τ hτ).app K ≫
                    ψ) ∧
              -- the derived trace is the sheaf-level trace, derived
              (derivedWeightedTrace.{u, u + 1, t, u} B Λ f modPullF hpullF w τ hτ =
                  (Stacks.Cohomology.PerfectComplexTriangles.mapDerivedCategoryCompIso
                      modPullF (fShriekMod.{u, u + 1, u} B Λ f)).inv ≫
                    NatTrans.mapDerivedCategory
                      (weightedTraceModNatTrans.{u, u + 1, u} B Λ f modPullF hpullF w τ hτ) ≫
                    (Functor.mapDerivedCategoryIdIso _).hom) ∧
              (∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
                  (weightedTraceModNatTrans.{u, u + 1, u} B Λ f modPullF hpullF w τ hτ).app M =
                    τ M) ∧
              -- compatibility with arbitrary base change
              (NatTrans.mapDerivedCategory
                    (traceBaseChangeComparison.{u, u + 1, u} B Λ f' f modPullF modPullF' modPullG
                      modPullP bcMod epsMod).hom ≫
                  (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso modPullG
                    (modPullF' ⋙ fShriekMod.{u, u + 1, u} B Λ f')).hom ≫
                  Functor.whiskerLeft modPullG.mapDerivedCategory
                    (NatTrans.mapDerivedCategory
                      (weightedTraceModNatTrans.{u, u + 1, u} B Λ f' modPullF' hpullF'
                        (w ∘ B.inclusion.map p) τ' hτ')) ≫
                  (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso modPullG
                    (𝟭 (ModuleSheaf.{u, u + 1, u} B Y' Λ))).inv =
                (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
                    (modPullF ⋙ fShriekMod.{u, u + 1, u} B Λ f) modPullG).hom ≫
                  Functor.whiskerRight
                    (NatTrans.mapDerivedCategory
                      (weightedTraceModNatTrans.{u, u + 1, u} B Λ f modPullF hpullF w τ hτ))
                    modPullG.mapDerivedCategory ≫
                  (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
                    (𝟭 (ModuleSheaf.{u, u + 1, u} B Y Λ)) modPullG).inv))
```

**`AlgebraicGeometry.SmallEtale.exists_weighting_derivedWeightedTraceMod_of_isGeometricallyUnibranch`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceQuasiFiniteUnibranchDerived.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/WeightedTrace/WeightedTraceQuasiFiniteUnibranchDerived.lean#L116). The attribute's comment: “the full example: a locally quasi-finite f (LocallyOfFiniteType together with Mathlib's LocallyQuasiFinite) onto a geometrically unibranch locally Noetherian Y carries a weighting w, the generic separable degree of the strict henselizations (0F3E), and for this w the trace maps of 0GKG exist and are unique on abelian sheaves, are functorial and compatible with arbitrary base change (0GKH (1), (2)), and for every ring Λ the constructed trace `AlgebraicGeometry.SmallEtale.derivedWeightedTraceMod` : f\_!f^\{-1}K ⟶ K on D(Y\_étale, Λ) (any model of the derived categories) is functorial in K, restricts to the sheaf-level trace `AlgebraicGeometry.SmallEtale.weightedTraceMod`, and is compatible with arbitrary base change through the constructed comparisons `fShriekBaseChangeMod` and `inverseImageSquareMod`, w ∘ p being a weighting of every base change f'. Nothing is quantified over beyond Λ, K, the square and the derived-category model. The source's word *positive* is false as written: 0F3E gives Z\_\{≥0}, and `AlgebraicGeometry.exists_locallyQuasiFinite_isNormal_not_exists_positive_weighting` is a counterexample (the closed point (2) of Spec ℤ), so w is stated nonnegative; 0GKG and 0GKH need no sign. Coefficients: ModuleSheaf.\{u, u+1, u} with Λ : Type u, where 0F5J is available.”. References: SGA 4 XVII (6.2.5), “special case”.

> **The trace for a locally quasi-finite morphism over a geometrically unibranch base.** Let
> `f : X ⟶ Y` be a locally quasi-finite morphism (locally of finite type with quasi-finite fibres) of
> a big étale site, with `Y` geometrically unibranch and locally Noetherian. Then there is a
> weighting `w : X → ℤ` of `f` such that:
>
> * `w` is nonnegative and its value at `x` is the generic separable degree of the strict
>   henselization of the local ring at `x` over that of the local ring at `f x` (Stacks 0F3E);
> * **Stacks 0GKG for `(f, w)`:** every abelian sheaf `F` on `Y_étale` has exactly one trace map
>   `Tr_{f, w, F} : f_! f^{-1}F ⟶ F` with the prescribed behaviour on geometric stalks;
> * **Stacks 0GKH (1), (2):** these trace maps are functorial in `F` and compatible with arbitrary
>   base change, the restriction `w ∘ p` along a base change being a weighting of `f'`;
> * **the trace on `D(Y_étale, Λ)`:** for every ring `Λ` and every cartesian square
>   `X' --p--> X`, `f' : X' ⟶ Y'`, `g : Y' ⟶ Y`, the trace map
>   `Tr_{f, w, M} = weightedTraceMod` on sheaves of `Λ`-modules has the stalk behaviour of 0GKG and
>   is the only morphism with it, and the derived trace
>   `Tr_{f, w} = derivedWeightedTraceMod : f_! f^{-1} ⟶ id` of `D(Y_étale, Λ)` is functorial in `K`,
>   restricts to the sheaf-level trace, and is compatible with the base change: the comparisons
>   `g^{-1}f_! ≅ f'_!p^{-1}` (Stacks 0F5J) and `p^{-1}f^{-1} ≅ f'^{-1}g^{-1}` at `Λ`-coefficients
>   carry the derived trace of `(f, w)`, whiskered by the derived `g^{-1}`, to the derived trace of
>   `(f', w ∘ p)`.
>
> All the `Λ`-linear functors, comparison isomorphisms and trace maps are the constructed ones of
> `StacksFrontier.AlgebraicGeometry.EtaleCohomology.WeightedTrace.WeightedTraceDerivedConstruction`;
> the derived categories are arbitrary models.

```lean
public theorem exists_weighting_derivedWeightedTraceMod_of_isGeometricallyUnibranch
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyQuasiFinite (B.inclusion.map f)]
    [IsLocallyNoetherian Y.obj] (hY : IsGeometricallyUnibranch Y.obj) :
    ∃ (w : X.obj → ℤ) (hw : IsWeighting (B.inclusion.map f) w),
      (∀ x : X.obj, 0 ≤ w x) ∧
      (∀ (x : X.obj)
          (κY : Type u) [Field κY]
          [Algebra (maximalIdeal (Y.obj.presheaf.stalk (B.inclusion.map f x))).ResidueField κY]
          [IsSepClosure
            (maximalIdeal (Y.obj.presheaf.stalk (B.inclusion.map f x))).ResidueField κY]
          (Rsh : Type u) [CommRing Rsh] [IsLocalRing Rsh]
          [Algebra (Y.obj.presheaf.stalk (B.inclusion.map f x)) Rsh]
          (_hRsh : Stacks.StrictHenselization.IsStrictHenselization
            (Y.obj.presheaf.stalk (B.inclusion.map f x)) κY Rsh)
          (κX : Type u) [Field κX]
          [Algebra (maximalIdeal (X.obj.presheaf.stalk x)).ResidueField κX]
          [IsSepClosure (maximalIdeal (X.obj.presheaf.stalk x)).ResidueField κX]
          (Ssh : Type u) [CommRing Ssh] [IsLocalRing Ssh]
          [Algebra (X.obj.presheaf.stalk x) Ssh] [Algebra Rsh Ssh]
          [Algebra (Y.obj.presheaf.stalk (B.inclusion.map f x)) Ssh]
          [IsScalarTower (Y.obj.presheaf.stalk (B.inclusion.map f x)) Rsh Ssh]
          (_hSsh : Stacks.StrictHenselization.IsStrictHenselization
            (X.obj.presheaf.stalk x) κX Ssh)
          (_hcomp : algebraMap (Y.obj.presheaf.stalk (B.inclusion.map f x)) Ssh =
            (algebraMap (X.obj.presheaf.stalk x) Ssh).comp
              ((B.inclusion.map f).stalkMap x).hom)
          (q : Ideal Rsh) [q.IsPrime] (_hq : q ∈ minimalPrimes Rsh)
          (Kbar : Type u) [Field Kbar]
          [Algebra q.ResidueField Kbar] [IsAlgClosure q.ResidueField Kbar],
          w x = (Nat.card (AlgHom q.ResidueField
            (TensorProduct Rsh q.ResidueField Ssh) Kbar) : ℤ)) ∧
      -- Stacks 0GKG for `(f, w)`: the trace map on abelian sheaves exists and is unique
      (∀ F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1},
        ∃! τ : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F,
          HasWeightedTraceStalks.{u, u + 1} B f w F τ) ∧
      -- Stacks 0GKH part (1): functoriality in the abelian sheaf
      (∀ (F G : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1})
          (φ : F ⟶ G)
          (τF : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F)
          (τG : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj G) ⟶ G),
          HasWeightedTraceStalks.{u, u + 1} B f w F τF →
          HasWeightedTraceStalks.{u, u + 1} B f w G τG →
            (fShriekFunctor.{u, u + 1} B f).map ((abPullback.{u, u + 1} B f).map φ) ≫ τG =
              τF ≫ φ) ∧
      -- Stacks 0GKH part (2): compatibility with arbitrary base change on abelian sheaves
      (∀ (X' Y' : B.Scheme) (p : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y)
          (sq : IsPullback p f' f g)
          (F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1})
          (τ : (fShriekFunctor.{u, u + 1} B f).obj ((abPullback.{u, u + 1} B f).obj F) ⟶ F),
          HasWeightedTraceStalks.{u, u + 1} B f w F τ →
          letI := locallyOfFiniteType_of_isPullback B p f' f g sq
          letI := locallyQuasiFinite_of_isPullback B p f' f g sq
          IsWeighting (B.inclusion.map f') (w ∘ B.inclusion.map p) ∧
          HasWeightedTraceStalks.{u, u + 1} B f' (w ∘ B.inclusion.map p)
              ((abPullback.{u, u + 1} B g).obj F)
              ((fShriekFunctor.{u, u + 1} B f').map
                  ((inverseImageSquareIso.{u} B p f' f g sq).inv.app F) ≫
                (fShriekBaseChangeNatIso.{u} B p f' f g sq).inv.app
                  ((abPullback.{u, u + 1} B f).obj F) ≫
                (abPullback.{u, u + 1} B g).map τ) ∧
            ∀ τ' : (fShriekFunctor.{u, u + 1} B f').obj
                ((abPullback.{u, u + 1} B f').obj ((abPullback.{u, u + 1} B g).obj F)) ⟶
                  (abPullback.{u, u + 1} B g).obj F,
              HasWeightedTraceStalks.{u, u + 1} B f' (w ∘ B.inclusion.map p)
                  ((abPullback.{u, u + 1} B g).obj F) τ' →
                (fShriekBaseChangeNatIso.{u} B p f' f g sq).hom.app
                    ((abPullback.{u, u + 1} B f).obj F) ≫
                  (fShriekFunctor.{u, u + 1} B f').map
                    ((inverseImageSquareIso.{u} B p f' f g sq).hom.app F) ≫ τ' =
                  (abPullback.{u, u + 1} B g).map τ) ∧
      -- the trace `Tr_{f, w, K}` on `D(Y_étale, Λ)`, every piece constructed
      (∀ (Λ : Type u) [Ring Λ] (X' Y' : B.Scheme) (p : X' ⟶ X) (f' : X' ⟶ Y') (g : Y' ⟶ Y)
          (sq : IsPullback p f' f g)
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B X Λ)]
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B Y Λ)]
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B X' Λ)]
          [HasDerivedCategory.{t} (ModuleSheaf.{u, u + 1, u} B Y' Λ)],
        letI := locallyOfFiniteType_of_isPullback B p f' f g sq
        letI := locallyQuasiFinite_of_isPullback B p f' f g sq
        -- the trace map at `Λ`-coefficients has the stalk behaviour of 0GKG ...
        (∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
            HasWeightedTraceStalksMod.{u, u + 1, u} B Λ f (pullbackMod.{u, u + 1, u} B Λ f)
              (pullbackModForgetIso.{u, u + 1, u} B Λ f) w M
              (weightedTraceMod.{u, u + 1, u} B Λ f hw M)) ∧
          -- ... and is the only morphism with it
          (∀ (M : ModuleSheaf.{u, u + 1, u} B Y Λ)
              (σ : (fShriekMod.{u, u + 1, u} B Λ f).obj
                ((pullbackMod.{u, u + 1, u} B Λ f).obj M) ⟶ M),
              HasWeightedTraceStalksMod.{u, u + 1, u} B Λ f (pullbackMod.{u, u + 1, u} B Λ f)
                (pullbackModForgetIso.{u, u + 1, u} B Λ f) w M σ →
                σ = weightedTraceMod.{u, u + 1, u} B Λ f hw M) ∧
          -- functoriality of `Tr_{f, w, K}` in `K`
          (∀ (K K' : DerivedCategory (ModuleSheaf.{u, u + 1, u} B Y Λ)) (ψ : K ⟶ K'),
              ((pullbackMod.{u, u + 1, u} B Λ f).mapDerivedCategory ⋙
                  (fShriekMod.{u, u + 1, u} B Λ f).mapDerivedCategory).map ψ ≫
                  (derivedWeightedTraceMod.{u, u + 1, t, u} B Λ f hw).app K' =
                (derivedWeightedTraceMod.{u, u + 1, t, u} B Λ f hw).app K ≫ ψ) ∧
          -- the derived trace is the sheaf-level trace, derived
          (derivedWeightedTraceMod.{u, u + 1, t, u} B Λ f hw =
              (Stacks.Cohomology.PerfectComplexTriangles.mapDerivedCategoryCompIso
                  (pullbackMod.{u, u + 1, u} B Λ f) (fShriekMod.{u, u + 1, u} B Λ f)).inv ≫
                NatTrans.mapDerivedCategory
                  (weightedTraceModTrans.{u, u + 1, u} B Λ f hw) ≫
                (Functor.mapDerivedCategoryIdIso _).hom) ∧
          (∀ M : ModuleSheaf.{u, u + 1, u} B Y Λ,
              (weightedTraceModTrans.{u, u + 1, u} B Λ f hw).app M =
                weightedTraceMod.{u, u + 1, u} B Λ f hw M) ∧
          -- compatibility with arbitrary base change
          (NatTrans.mapDerivedCategory
                (traceBaseChangeComparison.{u, u + 1, u} B Λ f' f
                  (pullbackMod.{u, u + 1, u} B Λ f) (pullbackMod.{u, u + 1, u} B Λ f')
                  (pullbackMod.{u, u + 1, u} B Λ g) (pullbackMod.{u, u + 1, u} B Λ p)
                  (fShriekBaseChangeMod.{u} B Λ p f' f g sq)
                  (inverseImageSquareMod.{u} B Λ p f' f g sq)).hom ≫
              (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
                (pullbackMod.{u, u + 1, u} B Λ g)
                (pullbackMod.{u, u + 1, u} B Λ f' ⋙ fShriekMod.{u, u + 1, u} B Λ f')).hom ≫
              Functor.whiskerLeft (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory
                (NatTrans.mapDerivedCategory
                  (weightedTraceModTrans.{u, u + 1, u} B Λ f'
                    (AlgebraicGeometry.IsWeighting.comp_of_isPullback hw
                      (sq.map B.inclusion)))) ≫
              (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
                (pullbackMod.{u, u + 1, u} B Λ g)
                (𝟭 (ModuleSheaf.{u, u + 1, u} B Y' Λ))).inv =
            (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
                (pullbackMod.{u, u + 1, u} B Λ f ⋙ fShriekMod.{u, u + 1, u} B Λ f)
                (pullbackMod.{u, u + 1, u} B Λ g)).hom ≫
              Functor.whiskerRight
                (NatTrans.mapDerivedCategory (weightedTraceModTrans.{u, u + 1, u} B Λ f hw))
                (pullbackMod.{u, u + 1, u} B Λ g).mapDerivedCategory ≫
              (Stacks.DerivedCategoryComparisons.mapDerivedCategoryCompIso
                (𝟭 (ModuleSheaf.{u, u + 1, u} B Y Λ))
                (pullbackMod.{u, u + 1, u} B Λ g)).inv) ∧
          AlgebraicGeometry.IsWeighting (B.inclusion.map f') (w ∘ B.inclusion.map p))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.5, Tag 0GKE](https://stacks.math.columbia.edu/tag/0GKE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
