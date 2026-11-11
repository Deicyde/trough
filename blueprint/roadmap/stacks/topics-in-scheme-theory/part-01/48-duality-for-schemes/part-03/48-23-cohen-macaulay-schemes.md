---
declaration: section
origin: cited
lean: Stacks.Duality.sheafIsCohenMacaulay_homology_of_concentrated, Stacks.Duality.exists_coherent_cohenMacaulay_iso_single_of_connected, Stacks.Duality.isOpen_setOf_isCohenMacaulayLocalRing, Stacks.Duality.isCohenMacaulay_cohenMacaulayLocus, Stacks.Duality.isCohenMacaulayLocalRing_stalk_iff_concentrated, Stacks.Duality.isCohenMacaulay_iff_locally_unique_homology, Stacks.Duality.isCohenMacaulay_of_exists_coherent_dualizingModule, Stacks.Duality.isCohenMacaulayAt_iff_exists_unique_nonzero_homology_upperShriek
statement: formalized
proof: formalized
---

# 48.23 Cohen-Macaulay schemes

Section 48.23 of the Stacks Project, [Tag 0AWQ](https://stacks.math.columbia.edu/tag/0AWQ). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AWT, a lemma

[Tag 0AWT](https://stacks.math.columbia.edu/tag/0AWT) in the Stacks Project.

**`Stacks.Duality.sheafIsCohenMacaulay_homology_of_concentrated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayDualizingModule.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayDualizingModule.lean#L161). The attribute's comment: “the dualizing module is Cohen--Macaulay, at an arbitrary degree of concentration”.

> **Stacks Project, Tag 0AWT, the Cohen--Macaulayness of the dualizing module.** If the
> cohomology of a dualizing complex on a locally Noetherian scheme is concentrated in the single
> degree `n`, then `H^n` of it is a Cohen--Macaulay `𝒪_X`-module in the sense of
> [Stacks, Tag 0343].

```lean
public theorem sheafIsCohenMacaulay_homology_of_concentrated {X : Scheme.{u}}
    [IsLocallyNoetherian X] [HasDerivedCategory.{w} X.Modules]
    (K : DerivedCategory X.Modules) (hK : IsDualizingComplex K) (n : ℤ)
    (hn : ∀ i : ℤ, i ≠ n → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K)) :
    AlgebraicGeometry.SheafIsCohenMacaulay X
      ((DerivedCategory.homologyFunctor X.Modules n).obj K)
```

**`Stacks.Duality.exists_coherent_cohenMacaulay_iso_single_of_connected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayDualizingModule.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayDualizingModule.lean#L193). The attribute's comment: “the final assertion, in full”.

> **Stacks Project, Tag 0AWT, the final assertion, in full.** If `X` is connected and
> Cohen--Macaulay then there is an integer `n` and a coherent Cohen--Macaulay `𝒪_X`-module
> `ω_X = H^n(ω_X^•)` with `ω_X^• = ω_X[-n]`.
>
> This is `Stacks.Duality.exists_coherent_iso_single_of_connected` together with the
> Cohen--Macaulayness clause of the source, which that statement omits.

```lean
public theorem exists_coherent_cohenMacaulay_iso_single_of_connected {X : Scheme.{u}}
    [IsLocallyNoetherian X] [ConnectedSpace X] [HasDerivedCategory.{w} X.Modules]
    (K : DerivedCategory X.Modules) (hK : IsDualizingComplex K)
    (hX : AlgebraicGeometry.IsCohenMacaulay X) :
    ∃ n : ℤ, _root_.SheafOfModules.IsCoherent
        ((DerivedCategory.homologyFunctor X.Modules n).obj K) ∧
      AlgebraicGeometry.SheafIsCohenMacaulay X
        ((DerivedCategory.homologyFunctor X.Modules n).obj K) ∧
      Nonempty (K ≅ (DerivedCategory.singleFunctor X.Modules n).obj
        ((DerivedCategory.homologyFunctor X.Modules n).obj K))
```

**`Stacks.Duality.isOpen_setOf_isCohenMacaulayLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean#L380). The attribute's comment: “clause (3), the Cohen--Macaulay locus is open”.

> **Stacks Project, Tag 0AWT, clause (3), openness.** On a locally Noetherian scheme carrying a
> dualizing complex, the set of points whose local ring is Cohen–Macaulay is open.

```lean
public theorem isOpen_setOf_isCohenMacaulayLocalRing {X : Scheme.{u}} [IsLocallyNoetherian X]
    [HasDerivedCategory.{w} X.Modules] (K : DerivedCategory X.Modules)
    (hK : IsDualizingComplex K) :
    IsOpen {x : X | IsCohenMacaulayLocalRing (X.presheaf.stalk x)}
```

**`Stacks.Duality.isCohenMacaulay_cohenMacaulayLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean#L426). The attribute's comment: “clause (3), the Cohen--Macaulay locus is Cohen--Macaulay”.

> **Stacks Project, Tag 0AWT, clause (3), the locus is Cohen–Macaulay.** The open subscheme of
> points with Cohen–Macaulay local ring is a Cohen–Macaulay scheme.

```lean
public theorem isCohenMacaulay_cohenMacaulayLocus {X : Scheme.{u}} [IsLocallyNoetherian X]
    [HasDerivedCategory.{w} X.Modules] (K : DerivedCategory X.Modules)
    (hK : IsDualizingComplex K) :
    AlgebraicGeometry.IsCohenMacaulay (cohenMacaulayLocus K hK).toScheme
```

**`Stacks.Duality.isCohenMacaulayLocalRing_stalk_iff_concentrated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean#L571). The attribute's comment: “clause (2), the stalkwise criterion”.

> **Stacks Project, Tag 0AWT, clause (2).** On a locally Noetherian scheme carrying a dualizing
> complex `K`, the local ring at `x` is Cohen–Macaulay exactly when the derived stalk `K_x` has a
> single nonzero cohomology module.

```lean
public theorem isCohenMacaulayLocalRing_stalk_iff_concentrated {X : Scheme.{u}}
    [IsLocallyNoetherian X] [HasDerivedCategory.{w} X.Modules]
    (K : DerivedCategory X.Modules) (hK : IsDualizingComplex K) (x : X)
    [HasDerivedCategory.{w} (ModuleCat.{u} (X.presheaf.stalk x))] :
    IsCohenMacaulayLocalRing (X.presheaf.stalk x) ↔
      ∃ n : ℤ, ∀ i : ℤ, i ≠ n → Limits.IsZero ((DerivedCategory.homologyFunctor
        (ModuleCat.{u} (X.presheaf.stalk x)) i).obj
        ((AlgebraicGeometry.derivedStalkFunctor x).obj K))
```

**`Stacks.Duality.isCohenMacaulay_iff_locally_unique_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulayLocus.lean#L701). The attribute's comment: “clause (1), locally a single nonzero cohomology sheaf, read stalkwise”.

> **Stacks Project, Tag 0AWT, clause (1).** A locally Noetherian scheme carrying a dualizing
> complex `K` is Cohen–Macaulay exactly when `K` locally has a single nonzero cohomology sheaf:
> every point has an open neighbourhood on which, for all but one degree, the cohomology sheaves
> of `K` have vanishing stalks.
>
> Vanishing of all the stalks over an open is vanishing of the restricted sheaf there, by
> [Stacks, Tag 01AG] (`AlgebraicGeometry.SheafOfModules.isZero_iff_forall_isZero_stalkFunctor_obj`),
> so this is the source's "`ω_X^•` locally has a unique nonzero cohomology sheaf".

```lean
public theorem isCohenMacaulay_iff_locally_unique_homology {X : Scheme.{u}}
    [IsLocallyNoetherian X] [HasDerivedCategory.{w} X.Modules]
    (K : DerivedCategory X.Modules) (hK : IsDualizingComplex K) :
    AlgebraicGeometry.IsCohenMacaulay X ↔
      ∀ x : X, ∃ V : X.Opens, x ∈ V ∧ ∃ n : ℤ, ∀ i : ℤ, i ≠ n → ∀ y ∈ V,
        Subsingleton
          (((DerivedCategory.homologyFunctor X.Modules i).obj K).presheaf.stalk y)
```

## Tag 0AWU, a lemma

[Tag 0AWU](https://stacks.math.columbia.edu/tag/0AWU) in the Stacks Project.

**`Stacks.Duality.isCohenMacaulay_of_exists_coherent_dualizingModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulaySchemeOfDualizingModule.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/CohenMacaulaySchemeOfDualizingModule.lean#L158).

> Let `X` be a locally Noetherian scheme. If there exists a coherent sheaf `ω_X` such that
> `ω_X[0]` is a dualizing complex on `X`, then `X` is a Cohen–Macaulay scheme.

```lean
theorem isCohenMacaulay_of_exists_coherent_dualizingModule
    (h : ∃ omegaX : X.Modules, _root_.SheafOfModules.IsCoherent omegaX ∧
      IsDualizingComplex ((DerivedCategory.singleFunctor X.Modules 0).obj omegaX)) :
    AlgebraicGeometry.IsCohenMacaulay X
```

## Tag 0C0Z, a lemma

[Tag 0C0Z](https://stacks.math.columbia.edu/tag/0C0Z) in the Stacks Project.

**`Stacks.Duality.isCohenMacaulayAt_iff_exists_unique_nonzero_homology_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekChartConsequences.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekChartConsequences.lean#L87).

> Let `S` be Noetherian, `f : X ⟶ Y` a flat morphism of `FTS S` and `x ∈ X`. Then `f` is
> Cohen–Macaulay at `x` if and only if `f^!𝒪_Y` has a unique nonzero cohomology sheaf in a
> neighbourhood of `x`.

```lean
theorem isCohenMacaulayAt_iff_exists_unique_nonzero_homology_upperShriek [Flat f.left]
    (x : X.left) :
    f.left.IsCohenMacaulayAt (isLocallyNoetherian_fiber_left f) x ↔
      ∃ W : X.left.Opens, x ∈ W ∧ ∃ n : ℤ,
        ¬ IsZero ((Scheme.Modules.restrictFunctor W.ι).obj
          ((DerivedCategory.homologyFunctor X.left.Modules n).obj
            (relativeDualizingComplexObj f j))) ∧
        ∀ i : ℤ, i ≠ n → IsZero ((Scheme.Modules.restrictFunctor W.ι).obj
          ((DerivedCategory.homologyFunctor X.left.Modules i).obj
            (relativeDualizingComplexObj f j)))
```

## Tag 0C10, a remark

[Tag 0C10](https://stacks.math.columbia.edu/tag/0C10) in the Stacks Project.

**`Stacks.Duality.NormalizedOnOpens.nonempty_iso_pullback_tensor_shift_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedCohenMacaulayTwistNagata.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedCohenMacaulayTwistNagata.lean#L56). The attribute's comment: “Similar results hold for X and Y of finite type over S, not necessarily separated, with complexes normalized relative to omega\_S: omega\_X = Lf^* omega\_Y (x) omega\_\{X/Y}[d]”.

> **[Stacks, Tag 0C10], last sentence, the complexes.** Let `S` be Noetherian with a dualizing
> complex `ω_S^•` and `f : X ⟶ Y` a separated Cohen–Macaulay morphism of relative dimension `d`
> between schemes of finite type over `S`, not necessarily separated over `S`. For dualizing
> complexes `ω_X^•`, `ω_Y^•` normalized relative to `ω_S^•` and `ω_{X/Y} = H^{-d}(f^! 𝒪_Y)`,
> `ω_X^• ≅ Lf^* ω_Y^• ⊗ᴸ ω_{X/Y}[d]`.

```lean
theorem nonempty_iso_pullback_tensor_shift_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) (hf : IsShriekable f)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (hCM : haveI := hf.target_noetherian
      (ftsHomOf f hf.separatedFiniteType (isSeparatedFiniteType_id Y)
        (Category.comp_id f)).left.IsCohenMacaulay (isLocallyNoetherian_fiber_left _))
    (d : ℕ) (hd : ∀ x : X, topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) =
      (d : WithBot ℕ∞)) :
    haveI := hf.target_noetherian
    Nonempty (𝒦X.complex.obj ≅ ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj 𝒦Y.complex.obj)).obj
          (relativeDualizingSheafShift (ftsHomOf f hf.separatedFiniteType
            (isSeparatedFiniteType_id Y) (Category.comp_id f)) (nagataCompactification f hf)
            hCM d hd))
```

**`Stacks.Duality.NormalizedOnOpens.exists_homology_iso_pullback_tensor_nagata`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedCohenMacaulayTwistNagata.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/NormalizedCohenMacaulayTwistNagata.lean#L82). The attribute's comment: “Similar results hold for X and Y of finite type over S, not necessarily separated, with complexes normalized relative to omega\_S: omega\_X = f^* omega\_Y (x) omega\_\{X/Y} for connected Cohen-Macaulay schemes”.

> **[Stacks, Tag 0C10], last sentence, the dualizing modules.** In the situation of
> `nonempty_iso_pullback_tensor_shift_nagata`, if moreover `Y` is connected and Cohen–Macaulay, the
> normalized complexes `ω_Y^•` and `ω_X^•` are concentrated in single degrees `m` and `m - d`, and
> their cohomology sheaves `ω_Y`, `ω_X` there satisfy `ω_X ≅ f^* ω_Y ⊗ ω_{X/Y}`.

```lean
theorem exists_homology_iso_pullback_tensor_nagata
    (hωS : haveI := hp.base_noetherian; IsDualizingComplex ωS.obj.obj) (hf : IsShriekable f)
    (𝒦X : NormalizedOnOpens UpperShriek.nagata hp ωS)
    (𝒦Y : NormalizedOnOpens UpperShriek.nagata hq ωS)
    (hCM : haveI := hf.target_noetherian
      (ftsHomOf f hf.separatedFiniteType (isSeparatedFiniteType_id Y)
        (Category.comp_id f)).left.IsCohenMacaulay (isLocallyNoetherian_fiber_left _))
    (d : ℕ) (hd : ∀ x : X, topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) =
      (d : WithBot ℕ∞))
    [ConnectedSpace Y] (hY : AlgebraicGeometry.IsCohenMacaulay Y) :
    haveI := hf.target_noetherian
    ∃ m : ℤ,
      (∀ i : ℤ, i ≠ m → IsZero ((DerivedCategory.homologyFunctor Y.Modules i).obj
        𝒦Y.complex.obj.obj)) ∧
      (∀ i : ℤ, i ≠ m - d → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj
        𝒦X.complex.obj.obj)) ∧
      Nonempty ((DerivedCategory.homologyFunctor X.Modules (m - d)).obj 𝒦X.complex.obj.obj ≅
        ((Stacks.SheafOfModules.Tensor.sheafTensor X.sheaf).obj
          ((Scheme.Modules.pullback f).obj
            ((DerivedCategory.homologyFunctor Y.Modules m).obj 𝒦Y.complex.obj.obj))).obj
          (relativeDualizingSheaf (ftsHomOf f hf.separatedFiniteType
            (isSeparatedFiniteType_id Y) (Category.comp_id f)) (nagataCompactification f hf)
            d))
```

**`Stacks.Duality.nonempty_upperShriek_iso_pullback_tensor_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCohenMacaulayTwistIso.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCohenMacaulayTwistIso.lean#L58). The attribute's comment: “f^!K = Lf^*K (x) omega\_\{X/Y}[d] for K in D^+\_QCoh”.

> **Stacks Project, Tag 0C10, the canonical isomorphism.** For a Cohen–Macaulay morphism
> `f : X ⟶ Y` of `FTS S` of relative dimension `d` and `K ∈ D⁺_QCoh(𝒪_Y)`,
> `f^!K ≅ Lf^*K ⊗ᴸ ω_{X/Y}[d]`, through `μ_{f,K}` of Tag 0B6U.

```lean
theorem nonempty_upperShriek_iso_pullback_tensor_shift
    (hCM : f.left.IsCohenMacaulay (isLocallyNoetherian_fiber_left f)) (d : ℕ)
    (hd : ∀ x : X.left,
      topologicalKrullDimAt (f.left.fiber (f.left x)) (f.left.asFiber x) = (d : WithBot ℕ∞))
    (K : quasiCoherentDerivedCategory Y.left) (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    Nonempty ((upperShriek f j).obj K ≅
      ((quasiCoherentDerivedTensor X.left).obj
        ((quasiCoherentDerivedPullback' f.left).obj K)).obj
          (relativeDualizingSheafShift f j hCM d hd))
```

**`Stacks.Duality.nonempty_upperShriek_comp_iso_pullback_tensor_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCohenMacaulayTwistIso.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCohenMacaulayTwistIso.lean#L74). The attribute's comment: “omega\_X = Lf^* omega\_Y (x) omega\_\{X/Y}[d]”.

> **Stacks Project, Tag 0C10, "in particular".** For `πY : Y ⟶ T`, `πX = f ≫ πY` and
> `ω_T ∈ D⁺_QCoh(𝒪_T)` (for instance a dualizing complex), with `ω_Y = πY^!ω_T` and
> `ω_X = πX^!ω_T`: `ω_X ≅ Lf^*ω_Y ⊗ᴸ ω_{X/Y}[d]`.

```lean
theorem nonempty_upperShriek_comp_iso_pullback_tensor_shift
    (hCM : f.left.IsCohenMacaulay (isLocallyNoetherian_fiber_left f)) (d : ℕ)
    (hd : ∀ x : X.left,
      topologicalKrullDimAt (f.left.fiber (f.left x)) (f.left.asFiber x) = (d : WithBot ℕ∞))
    {T : FTS S} (πY : Y ⟶ T) (πX : X ⟶ T) (hπ : f ≫ πY = πX)
    (jY : CompactificationOf (Over.mk πY.left)) (jX : CompactificationOf (Over.mk πX.left))
    (ωT : quasiCoherentDerivedCategory T.left) (hωT : DerivedCategoryB.IsBoundedBelow ωT.obj) :
    Nonempty ((upperShriek πX jX).obj ωT ≅
      ((quasiCoherentDerivedTensor X.left).obj
        ((quasiCoherentDerivedPullback' f.left).obj ((upperShriek πY jY).obj ωT))).obj
          (relativeDualizingSheafShift f j hCM d hd))
```

**`Stacks.Duality.exists_homology_upperShriek_comp_iso_pullback_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCohenMacaulayTwistIso.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCohenMacaulayTwistIso.lean#L94). The attribute's comment: “omega\_X = f^* omega\_Y (x) omega\_\{X/Y} for connected Cohen-Macaulay schemes”.

> **Stacks Project, Tag 0C10, the dualizing modules.** If moreover `ω_T` is a dualizing
> complex and `Y` is connected and Cohen–Macaulay, then `ω_Y^•` and `ω_X^•` are concentrated in
> single degrees `m` and `m - d`, and their cohomology sheaves `ω_Y`, `ω_X` there satisfy
> `ω_X ≅ f^*ω_Y ⊗ ω_{X/Y}`. (Connectedness and Cohen–Macaulayness of `X` are not needed.)

```lean
theorem exists_homology_upperShriek_comp_iso_pullback_tensor
    (hCM : f.left.IsCohenMacaulay (isLocallyNoetherian_fiber_left f)) (d : ℕ)
    (hd : ∀ x : X.left,
      topologicalKrullDimAt (f.left.fiber (f.left x)) (f.left.asFiber x) = (d : WithBot ℕ∞))
    {T : FTS S} (πY : Y ⟶ T) (πX : X ⟶ T) (hπ : f ≫ πY = πX)
    (jY : CompactificationOf (Over.mk πY.left)) (jX : CompactificationOf (Over.mk πX.left))
    (ωT : quasiCoherentDerivedCategory T.left) (hωT : IsDualizingComplex ωT.obj)
    [ConnectedSpace Y.left] (hY : AlgebraicGeometry.IsCohenMacaulay Y.left) :
    ∃ m : ℤ,
      (∀ i : ℤ, i ≠ m → IsZero ((DerivedCategory.homologyFunctor Y.left.Modules i).obj
        ((upperShriek πY jY).obj ωT).obj)) ∧
      (∀ i : ℤ, i ≠ m - d → IsZero ((DerivedCategory.homologyFunctor X.left.Modules i).obj
        ((upperShriek πX jX).obj ωT).obj)) ∧
      Nonempty ((DerivedCategory.homologyFunctor X.left.Modules (m - d)).obj
          ((upperShriek πX jX).obj ωT).obj ≅
        ((Stacks.SheafOfModules.Tensor.sheafTensor X.left.sheaf).obj
          ((Scheme.Modules.pullback f.left).obj
            ((DerivedCategory.homologyFunctor Y.left.Modules m).obj
              ((upperShriek πY jY).obj ωT).obj))).obj (relativeDualizingSheaf f j d))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.23, Tag 0AWQ](https://stacks.math.columbia.edu/tag/0AWQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
