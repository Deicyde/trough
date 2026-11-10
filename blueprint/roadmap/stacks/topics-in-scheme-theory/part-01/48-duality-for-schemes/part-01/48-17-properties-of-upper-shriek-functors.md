---
declaration: section
origin: cited
lean: Stacks.Duality.upperShriekIsoRestrictOfOpenImmersion, Stacks.Duality.upperShriekRestrictIso, Stacks.Duality.nonempty_upperShriekPlus_affineLineProj_iso, Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts, Stacks.Duality.restrictedUpperShriekIsoOfOpenSquare, Stacks.Duality.upperShriekCharts, Stacks.Duality.derivedCategoryBPlus_upperShriek, Stacks.Divisors.isDualizingModule_homologyOne_derivedSheafHomExactSupport
statement: formalized
proof: formalized
---

# 48.17 Properties of upper shriek functors

Section 48.17 of the Stacks Project, [Tag 0ATZ](https://stacks.math.columbia.edu/tag/0ATZ). 11 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AU0, a lemma

[Tag 0AU0](https://stacks.math.columbia.edu/tag/0AU0) in the Stacks Project.

**`Stacks.Duality.upperShriekIsoRestrictOfOpenImmersion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekAffineComparison/OpenImmersionRestriction.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekAffineComparison/OpenImmersionRestriction.lean#L87). The attribute's comment: “j^! = j^* with j^* the restriction to the open X, j^! computed at the compactification X-bar = Y that the source's proof chooses; over a quasi-compact quasi-separated base and on the unbounded D_QCoh”.

> **Stacks Project, Tag 0AU0 (Lemma 48.17.1).** Let `j : X ⟶ Y` be a morphism of
> `AlgebraicGeometry.FTS S` whose underlying morphism of schemes is an open immersion. Then the
> exceptional inverse image of `j` is restriction to `X`:
>
>   `j^! ≅ j^* : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)`.
>
> Here `j^!` is computed at the compactification `X̄ = Y` of `Stacks.Duality.openCompactification`,
> the one the source's proof chooses. The isomorphism is the source's: the right adjoint of
> `R(𝟙_Y)_*` is the identity (`Stacks.Duality.upperShriekIsoDerivedPullbackOfOpenImmersion`), and
> `Lj^*` is restriction along an open immersion
> (`Stacks.Duality.restrictedDerivedRestrictIsoQuasiCoherentDerivedPullback`).

```lean
def upperShriekIsoRestrictOfOpenImmersion :
    upperShriek j (openCompactification j) ≅ OpenImmersion.restrictedDerivedRestrict j.left
```

## Tag 0G4J, a lemma

[Tag 0G4J](https://stacks.math.columbia.edu/tag/0G4J) in the Stacks Project.

**`Stacks.Duality.upperShriekRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/OpenImmersionSquare.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/OpenImmersionSquare.lean#L54).

> **Stacks Project, Tag 0G4J (Lemma 48.17.2).** In Situation 48.16.1 let
> `j : U ⟶ X`, `j' : V ⟶ Y` be open immersions and `f : X ⟶ Y`, `g : U ⟶ V` morphisms of
> `FTS S` with `j ≫ f = g ≫ j'`. Then `j^* ∘ f^! ≅ g^! ∘ (j')^*` as functors on
> `D⁺_QCoh(𝒪_Y)`, for arbitrary compactifications `cf` of `f` and `cg` of `g` computing `f^!` and
> `g^!`; here `j^*`, `(j')^*` are the restrictions to the opens.
>
> This is also the first assertion of [Stacks, Tag 0BV2] (Remark 48.17.5): for open
> `U ⊆ X`, `V ⊆ Y` with `f(U) ⊆ V` and `g` the restriction of `f`, `(f^!E)|_U = g^!(E|_V)` for
> `E ∈ D⁺_QCoh(𝒪_Y)`, stated here for arbitrary open immersions and compactifications.

```lean
def upperShriekRestrictIso :
    (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙ upperShriek f cf ⋙
        OpenImmersion.restrictedDerivedRestrict j.left ≅
      (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        OpenImmersion.restrictedDerivedRestrict j'.left ⋙ upperShriek g cg
```

## Tag 0AA1, a lemma

[Tag 0AA1](https://stacks.math.columbia.edu/tag/0AA1) in the Stacks Project.

**`Stacks.Duality.nonempty_upperShriekPlus_affineLineProj_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekAffineLine.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekAffineLine.lean#L295).

> **Stacks Project, Tag 0AA1 (Lemma 48.17.3).** In Situation 48.16.1 let `Y` be an object of
> `FTS S` and let `f : X = 𝔸¹_Y ⟶ Y` be the projection. Then there is a (noncanonical) isomorphism
> `f^!(-) ≅ Lf^*(-)[1]` of functors on `D⁺_QCoh(𝒪_Y)`, with `f^!` computed at any compactification
> `j` of `f`.
>
> The proof is through the isomorphisms `μ_{f,K} : Lf^*K ⊗ᴸ f^!𝒪_Y ≅ f^!K` of
> [Stacks, Tag 0B6U] (e), `f` being smooth, together with `f^!𝒪_Y ≅ 𝒪_X[1]`: the source's
> `𝒪_{ℙ¹_Y}(-2)|_X ≅ 𝒪_X` is replaced by the fundamental class of [Stacks, Tag 0E9Z] for
> `X ⊆ ℙ¹_Y ⟶ Y` and the triviality of `Ω_{X/Y}`.

```lean
theorem nonempty_upperShriekPlus_affineLineProj_iso :
    Nonempty (upperShriekPlus (affineLineProj Y) j ⋙ ObjectProperty.ι _ ≅
      ObjectProperty.ι _ ⋙ quasiCoherentDerivedPullback' (affineLineProj Y).left ⋙
        shiftFunctor (quasiCoherentDerivedCategory (affineLineFTS Y).left) (1 : ℤ))
```

## Tag 0AA2, a lemma

[Tag 0AA2](https://stacks.math.columbia.edu/tag/0AA2) in the Stacks Project.

**`Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean#L160). The attribute's comment: “at the locally small derived categories, the model at which the coherator and the right adjoint of Ri_* are built; i^! is constructed here”.

> **Stacks Project, Tag 0AA2 (Lemma 48.17.4).** In Situation 48.16.1 — `S` a Noetherian scheme
> and `FTS S` the schemes separated and of finite type over `S` — let `i : X ⟶ Y` be a morphism of
> `FTS S` whose underlying morphism of schemes is a closed immersion. Then
> `i^!(-) = R𝓗om(𝒪_X, -)`:
>
> 1. `Ri_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint;
> 2. the upper shriek `i^! = j^* ∘ a` of [Stacks, Tag 0A9Y] at the compactification `X̄ = X` that a
>    proper morphism is (`Stacks.Duality.properCompactification`), with its right adjoint `a`
>    *produced* by (1) and its quasi-coherence inputs discharged, agrees with `R𝓗om(𝒪_X, -)` on
>    `D⁺_QCoh(𝒪_Y)`;
> 3. for every right adjoint `a` of `Ri_*` the canonical comparison `a(K) ⟶ R𝓗om(𝒪_X, K)` — the
>    mate of the counit of `a` under [Stacks, Tag 0A76] — is an isomorphism for every `K` in
>    `D⁺_QCoh(𝒪_Y)`.
>
> The existence (1) is
> `Stacks.Duality.LocallySmall.isLeftAdjoint_affineHomQuasiCoherentDerivedPushforward`, which builds
> the right adjoint as `DQ_X ∘ R𝓗om(𝒪_X, -)` from the coherator of [Stacks, Tag 0CR0]; `X` is
> quasi-compact and quasi-separated, being of finite type over a Noetherian scheme. The
> identification (2), (3) is [Stacks, Tag 0A9X] at this model
> (`Stacks.Duality.LocallySmall.isIso_rightAdjointToDerivedSheafHom_app`), whose hypotheses —
> pseudo-coherence of `i` — hold in Situation 48.16.1.

```lean
theorem upperShriek_closedImmersion_of_fts {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S}
    (i : X ⟶ Y) [IsClosedImmersion i.left] :
    (affineHomQuasiCoherentDerivedPushforward i.left).IsLeftAdjoint ∧
      IsDerivedSheafHomRightAdjoint i.left
        (upperShriek i (properCompactification i)) ∧
      ∀ (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory X.left)
        (adj : affineHomQuasiCoherentDerivedPushforward i.left ⊣ a)
        (K : (isBoundedBelowQuasiCoherent Y.left).FullSubcategory),
        IsIso ((rightAdjointToDerivedSheafHom i.left
          (isQuasicoherent_homology_derivedPushforward_of_isAffineHom i.left) a adj).app
            K.obj)
```

## Tag 0BV2, a remark

[Tag 0BV2](https://stacks.math.columbia.edu/tag/0BV2) in the Stacks Project.

**`Stacks.Duality.upperShriekRestrictIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/OpenImmersionSquare.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImageFTS/OpenImmersionSquare.lean#L54). The attribute's comment: “part (a): (f^!E)|_U ≅ g^!(E|_V) for E in D^+_QCoh, every open square and every pair of compactifications”.

> **Stacks Project, Tag 0G4J (Lemma 48.17.2).** In Situation 48.16.1 let
> `j : U ⟶ X`, `j' : V ⟶ Y` be open immersions and `f : X ⟶ Y`, `g : U ⟶ V` morphisms of
> `FTS S` with `j ≫ f = g ≫ j'`. Then `j^* ∘ f^! ≅ g^! ∘ (j')^*` as functors on
> `D⁺_QCoh(𝒪_Y)`, for arbitrary compactifications `cf` of `f` and `cg` of `g` computing `f^!` and
> `g^!`; here `j^*`, `(j')^*` are the restrictions to the opens.
>
> This is also the first assertion of [Stacks, Tag 0BV2] (Remark 48.17.5): for open
> `U ⊆ X`, `V ⊆ Y` with `f(U) ⊆ V` and `g` the restriction of `f`, `(f^!E)|_U = g^!(E|_V)` for
> `E ∈ D⁺_QCoh(𝒪_Y)`, stated here for arbitrary open immersions and compactifications.

```lean
def upperShriekRestrictIso :
    (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙ upperShriek f cf ⋙
        OpenImmersion.restrictedDerivedRestrict j.left ≅
      (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        OpenImmersion.restrictedDerivedRestrict j'.left ⋙ upperShriek g cg
```

**`Stacks.Duality.restrictedUpperShriekIsoOfOpenSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekAffineComparison/OpenSquare.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekAffineComparison/OpenSquare.lean#L171). The attribute's comment: “clause (a) only, the restriction formula (f^!E)|_U = g^!(E|_V) for an open square; clause (b), the affine formula phi^!(K) = RHom(A, K ⊗^L_R P)[n], is NOT claimed, because Stacks 0AA1 (f^! = Lf^*[1] for A^1_V -> V) is absent from this repository. Carried: h0ATXf and h0ATXi, the two instances of Stacks 0ATX for the two factorisations of the diagonal of the square. Stacks 0AU0 is NOT carried: it is proved by Stacks.Duality.upperShriekIsoDerivedPullbackOfOpenImmersion, and supplying it is the only content this statement adds to its hypotheses. Stated for open immersions rather than affine opens, and on the unbounded D_QCoh rather than D^+_QCoh”.

> **Stacks Project, Tag 0BV2 (Remark 48.17.5), clause (a).** Let `f : X ⟶ Y` and `g : U ⟶ V` be
> morphisms of `AlgebraicGeometry.FTS S` and let `j : U ⟶ X`, `i : V ⟶ Y` be morphisms of
> `FTS S` whose underlying morphisms of schemes are open immersions, with `j ≫ f = g ≫ i`. Then
> restricting an exceptional inverse image to `U` computes the exceptional inverse image of the
> restriction to `V`:
>
>   `f^! ⋙ Lj^* ≅ Li^* ⋙ g^!`,
>
> that is `(f^!E)|_U ≅ g^!(E|_V)` naturally in `E ∈ D_QCoh(𝒪_Y)`.
>
> The source's proof is reproduced. The two hypotheses `h0ATXf` and `h0ATXi` are the two instances
> of [Stacks, Tag 0ATX] that it cites, for the two factorisations `j ≫ f` and `g ≫ i` of the
> diagonal `d : U ⟶ Y` of the square. The passage from `j^!` and `i^!` to the restrictions `Lj^*`
> and `Li^*` is [Stacks, Tag 0AU0], which is not assumed here but proved in
> `Stacks.Duality.upperShriekIsoDerivedPullbackOfOpenImmersion`; it is the whole of the content
> this statement adds to its hypotheses.
>
> Clause (b) of Tag 0BV2, the affine formula `φ^!(K) = RHom(A, K ⊗^L_R P)[n]`, is not claimed: it
> needs [Stacks, Tag 0AA1], which this repository does not have.

```lean
def restrictedUpperShriekIsoOfOpenSquare (_hdj : j ≫ f = d) (_hdi : g ≫ i = d) :
    upperShriek f cf ⋙ quasiCoherentDerivedPullback' j.left ≅
      quasiCoherentDerivedPullback' i.left ⋙ upperShriek g cg
```

**`Stacks.Duality.upperShriekCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekStructureSheafCharts.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekStructureSheafCharts.lean#L679). The attribute's comment: “part (b): (f^!E)|_U corresponds to phi^!(K) = RHom(A, K (x)^L_R P)[n] for every pair of affine opens U, V with f(U) in V, every presentation A = P/I and every K in D(R) with E|_V = K~, E in D^+_QCoh, every compactification”.

> **Stacks Project, Tag 0BV2 (Remark 48.17.5), second assertion.** In Situation 48.16.1 let
> `f : X ⟶ Y` be a morphism of `FTS S`, `j` any compactification computing `f^!`, and
> `E ∈ D⁺_QCoh(𝒪_Y)`. For affine opens `U = Spec A ⊆ f⁻¹(V)`, `V = Spec R`, every presentation
> `A = P/I` with `P = R[x_1, …, x_n]` and every `K ∈ D(R)` with `E|_V ≅ K~`, the restriction
> `(f^!E)|_U` is the sheaf associated to `φ^!(K) = RHom_P(A, K ⊗ᴸ_R P)[n]`.

```lean
theorem upperShriekCharts
    {S : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S]
    {X Y : FTS S} (f : X ⟶ Y) (j : CompactificationOf (Over.mk f.left))
    (E : quasiCoherentDerivedCategory Y.left) (hE : DerivedCategoryB.IsBoundedBelow E.obj) :
    UpperShriekCharts f j E
```

## Tag 0AU1, a lemma

[Tag 0AU1](https://stacks.math.columbia.edu/tag/0AU1) in the Stacks Project.

**`Stacks.Duality.derivedCategoryBPlus_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCoherent.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCoherent.lean#L210).

> **Stacks Project, Tag 0AU1 (Lemma 48.17.6).** In Situation 48.16.1 let `f : X ⟶ Y` be a
> morphism of `FTS S`. Then `f^!` maps `D⁺_Coh(𝒪_Y)` into `D⁺_Coh(𝒪_X)`. Here `f^!` is computed at
> an arbitrary compactification `j`.

```lean
theorem derivedCategoryBPlus_upperShriek
    {S : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S] {X Y : FTS S} (f : X ⟶ Y)
    (j : CompactificationOf (Over.mk f.left)) (E : quasiCoherentDerivedCategory Y.left)
    (hE : DerivedCategoryB.derivedCategoryBPlus
      (fun M : Y.left.Modules ↦ _root_.SheafOfModules.IsCoherent M) E.obj) :
    DerivedCategoryB.derivedCategoryBPlus
      (fun M : X.left.Modules ↦ _root_.SheafOfModules.IsCoherent M)
      ((upperShriek f j).obj E).obj
```

## Tag 0AA3, a lemma

[Tag 0AA3](https://stacks.math.columbia.edu/tag/0AA3) in the Stacks Project.

**`Stacks.Divisors.isDualizingModule_homologyOne_derivedSheafHomExactSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDualizingModule.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDualizingModule.lean#L118). The attribute's comment: “for the inclusion i : D to X of an effective Cartier divisor into a locally Noetherian scheme, read on a module: if omega placed in some degree is a dualizing complex on X then H^1(a(omega)) — which clause (7) of Tag 0AU3 identifies with the degree-one cohomology of i^!omega, namely the normal sheaf twist N tensor i^*omega of the restriction — is a dualizing module on D. Nothing is carried; see the Tag 0AU3 clause string above for the three inputs, all of them proved in the library. The general finite-type case is Stacks.Duality.isDualizingComplex_upperShriek_of_fts”.

> **[Stacks, Tag 0AA3] for the inclusion of an effective Cartier divisor, read on a module.**
> Let `D ⊆ X` be an effective Cartier divisor on a locally Noetherian scheme, with closed immersion
> `i : D ⟶ X`, and let `a(-)` be the right adjoint of derived pushforward along `i` of
> [Stacks, Tag 0A76]. If a quasi-coherent `𝒪_X`-module `ω` placed in some degree is a dualizing
> complex on `X`, then the `𝒪_D`-module `H¹(a(ω))` is a dualizing module on `D`.
>
> Degree one is the degree [Stacks, Remark 0B4R] selects, and
> `Stacks.Divisors.nonempty_homologyOne_derivedSheafHomExactSupport_iso` identifies `H¹(a(ω))` with
> the normal sheaf twist `𝒩 ⊗ i^*ω` of the restriction.

```lean
theorem isDualizingModule_homologyOne_derivedSheafHomExactSupport (ω : X.Modules)
    [ω.IsQuasicoherent] (n : ℤ) (hω : Stacks.Duality.IsDualizingComplex
      ((DerivedCategory.singleFunctor X.Modules n).obj ω)) :
    letI : IsLocallyNoetherian D.subscheme := D.isLocallyNoetherian_subscheme
    Stacks.Duality.IsDualizingModule
      ((DerivedCategory.homologyFunctor D.subscheme.Modules 1).obj
        ((closedQuotient D).derivedSheafHomExactSupport.obj
          ((DerivedCategory.singleFunctor X.Modules 0).obj ω)))
```

**`Stacks.Duality.isDualizingComplex_upperShriek_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplex.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplex.lean#L148). The attribute's comment: “granted the conclusion of Tag 0A86 (dualizing may be checked on one affine cover) and the affine-chart description of f^! of Tag 0AA1 together with Tag 0BV2, carried as the explicit hypotheses h0A86 and h0AA1; f^! itself is an explicit parameter fShriek characterised by h0AA1, not a constructed or chosen functor. What is proved is the rest of the source argument: the affine charts of X lying over affine opens of Y cover X, the dualizing model of K over each such V comes from hK, Tag 0BZL upgrades its algebraic upper shriek to a dualizing complex over the chart ring of X, and h0A86 glues the local models. Neither carried hypothesis asserts that anything is dualizing”.

> **Stacks Project, Tag 0AA3 (Lemma 48.17.7).** In Situation 48.16.1, let `f : X ⟶ Y` be a
> morphism of `FTS S` and let `f^!` be an exceptional inverse image functor
> `D⁺_QCoh(𝒪_Y) ⥤ D⁺_QCoh(𝒪_X)` for it, in the sense that on affine charts it is the algebraic
> upper shriek of a polynomial presentation of the chart ring map. If `K` is a dualizing complex
> for `Y`, then `f^!K` is a dualizing complex for `X`.

```lean
theorem isDualizingComplex_upperShriek_of_fts {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S}
    (f : X ⟶ Y)
    (fShriek : quasiCoherentDerivedCategoryPlus Y.left ⥤ quasiCoherentDerivedCategoryPlus X.left)
    (K : quasiCoherentDerivedCategoryPlus Y.left)
    (h0A86 : ∀ L : DerivedCategory X.left.Modules,
      (∀ x : X.left, ∃ (U : X.left.Opens) (hU : IsAffineOpen U),
        x ∈ U ∧ HasDualizingModelOn L U hU) → IsDualizingComplex L)
    (h0AA1 : ∀ (U : X.left.Opens) (hU : IsAffineOpen U) (V : Y.left.Opens)
      (hV : IsAffineOpen V) (hUV : U ≤ f.left ⁻¹ᵁ V)
      (ω : DerivedCategory (ModuleCat.{u} Γ(Y.left, V))),
      IsTildeModelOn K.obj.obj V hV ω →
      ∃ p : Dualizing.PolynomialPresentation (f.left.appLE V U hUV).hom,
        IsTildeModelOn (fShriek.obj K).obj.obj U hU (p.upperShriekFunctor.{u, u}.obj ω))
    (hK : IsDualizingComplex K.obj.obj) :
    IsDualizingComplex (fShriek.obj K).obj.obj
```

Declarations registered for the tag:

- [`Stacks.Duality.isDualizingComplex_upperShriek_obj`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplexOfCharts.lean#L70), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplexOfChartsRegistration.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplexOfChartsRegistration.lean#L15) (StacksFrontier).

## Tag 0AU2, a lemma

[Tag 0AU2](https://stacks.math.columbia.edu/tag/0AU2) in the Stacks Project.

**`Stacks.Duality.UpperShriekDuality.upperShriekDualityIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDuality.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDuality.lean#L272).

> **Stacks Project, Tag 0AU2.** In Situation [Stacks, Tag 0F42] — `S` Noetherian — let
> `f : X ⟶ Y` be a morphism of schemes separated and of finite type over `S`, let `j` be a
> compactification of `X` over `Y`, and let `K` be a dualizing complex on `Y`. Set
> `D_Y(M) = R𝓗om(M, K)` and `D_X(E) = R𝓗om(E, f^!K)`. Then there is a canonical isomorphism
>
> `f^!M ≅ D_X(Lf^* D_Y(M))`,
>
> natural in `M ∈ D^+_Coh(𝒪_Y)`.

```lean
def upperShriekDualityIso :
    upperShriekStd f j ≅
      (plusCoh Y.left).ι ⋙ ((sheafHom Y.left).flip.obj K).rightOp ⋙ (pull f.left).op ⋙
        (sheafHom X.left).flip.obj (upperShriekDualizing f j hK)
```

## Tag 0B6U, a lemma

[Tag 0B6U](https://stacks.math.columbia.edu/tag/0B6U) in the Stacks Project.

**`Stacks.Duality.derivedCategoryBBounded_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCoherent.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekCoherent.lean#L237). The attribute's comment: “part (d)”.

> **Stacks Project, Tag 0B6U (Lemma 48.17.9), part (d).** In Situation 48.16.1 let
> `f : X ⟶ Y` be a perfect morphism of `FTS S`. Then `f^!` maps `D^b_Coh(𝒪_Y)` into
> `D^b_Coh(𝒪_X)`. Here `f^!` is computed at an arbitrary compactification `j`.

```lean
theorem derivedCategoryBBounded_upperShriek {S : Scheme.{u}} [AlgebraicGeometry.IsNoetherian S]
    {X Y : FTS S} (f : X ⟶ Y) (j : CompactificationOf (Over.mk f.left)) [Perfect f.left]
    (E : quasiCoherentDerivedCategory Y.left)
    (hE : DerivedCategoryB.derivedCategoryBBounded
      (fun M : Y.left.Modules ↦ _root_.SheafOfModules.IsCoherent M) E.obj) :
    DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules ↦ _root_.SheafOfModules.IsCoherent M)
      ((upperShriek f j).obj E).obj
```

**`Stacks.Duality.derivedCategoryBBounded_upperShriek_derivedStructureSheaf_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfect.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfect.lean#L63). The attribute's comment: “part (a)”.

> **Stacks Project, Tag 0B6U (Lemma 48.17.9), part (a).** In Situation 48.16.1 let
> `f : X ⟶ Y` be a perfect morphism of `FTS S`. Then `f^!𝒪_Y` lies in `D^b_Coh(𝒪_X)`: it is
> cohomologically bounded and its cohomology sheaves are coherent. Here `f^!` is computed at an
> arbitrary compactification `j`.

```lean
theorem derivedCategoryBBounded_upperShriek_derivedStructureSheaf_of_perfect [Perfect f.left] :
    DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules ↦ _root_.SheafOfModules.IsCoherent M)
      (((upperShriek f j).obj (derivedStructureSheaf Y.left)).obj)
```

**`Stacks.Duality.hasFiniteTorDimension_derivedScalarRestriction_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfect.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfect.lean#L81). The attribute's comment: “part (b)”.

> **Stacks Project, Tag 0B6U (Lemma 48.17.9), part (b).** In Situation 48.16.1 let
> `f : X ⟶ Y` be a perfect morphism of `FTS S`. Then `f^!𝒪_Y` has finite tor dimension in
> `D(f⁻¹𝒪_Y)`: read on the ringed space `(X, f⁻¹𝒪_Y)`, it has Tor amplitude in some interval.
> Here `f^!` is computed at an arbitrary compactification `j`.

```lean
theorem hasFiniteTorDimension_derivedScalarRestriction_upperShriek [Perfect f.left] :
    Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension
      (RingedSpace.inverseImage Y.left.toRingedSpace f.left.base)
      ((Scheme.Hom.derivedScalarRestriction f.left).obj (relativeDualizingComplexObj f j))
```

**`Stacks.Duality.isIso_derivedSheafHomothety_upperShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfect.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfect.lean#L109). The attribute's comment: “part (c)”.

> **Stacks Project, Tag 0B6U (Lemma 48.17.9), part (c).** In Situation 48.16.1 let
> `f : X ⟶ Y` be a perfect morphism of `FTS S`. Then the homothety
> `𝒪_X ⟶ R𝓗om_{𝒪_X}(f^!𝒪_Y, f^!𝒪_Y)` is an isomorphism. Here `f^!` is computed at an arbitrary
> compactification `j`.

```lean
theorem isIso_derivedSheafHomothety_upperShriek [Perfect f.left] :
    IsIso (Stacks.SheafOfModules.derivedSheafHomothety X.left.sheaf
      (relativeDualizingComplexObj f j))
```

**`Stacks.Duality.isIso_upperShriekCompareWithPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfectComparison.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekPerfectComparison.lean#L46). The attribute's comment: “part (e)”.

> Let `S` be a Noetherian scheme and `f : X ⟶ Y` a perfect morphism of `FTS S`. Then the map
> `μ_{f,K} : Lf^*K ⊗ᴸ_{𝒪_X} f^!𝒪_Y ⟶ f^!K`, `Stacks.Duality.upperShriekCompareWithPullbackCanonical`,
> is an isomorphism for all `K ∈ D⁺_QCoh(𝒪_Y)`. Here `f^!` and `μ_{f,K}` are computed at an
> arbitrary compactification `j`.

```lean
theorem isIso_upperShriekCompareWithPullback [Perfect f.left]
    (j : CompactificationOf (Over.mk f.left)) (K : quasiCoherentDerivedCategory Y.left)
    (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    IsIso (upperShriekCompareWithPullbackCanonical f j K)
```

## Tag 0E9T, a lemma

[Tag 0E9T](https://stacks.math.columbia.edu/tag/0E9T) in the Stacks Project.

**`Stacks.Duality.upperShriek_structureSheaf_isPerfectRelativeTo_and_isIso_homothety`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFlatDualizing.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFlatDualizing.lean#L122).

> **Stacks Project, Tag 0E9T (Lemma 48.17.10).** In Situation 48.16.1 (`S` Noetherian), let
> `f : X ⟶ Y` be a flat morphism of `FTS S`, with `f^!` computed at any compactification `j`. Then
> `f^!𝒪_Y` is a `Y`-perfect object of `D(𝒪_X)` and `𝒪_X ⟶ R𝓗om_{𝒪_X}(f^!𝒪_Y, f^!𝒪_Y)` is an
> isomorphism.

```lean
theorem upperShriek_structureSheaf_isPerfectRelativeTo_and_isIso_homothety :
    (letI := locallyOfFinitePresentation_left f;
      Scheme.Hom.IsPerfectRelativeTo.{u + 1, u + 1} f.left
        (RingedSpace.canonicalCertifiedDerivedSheafTensoringFamily _)
        (relativeDualizingComplexObj f j)) ∧
      IsIso (Stacks.SheafOfModules.derivedSheafHomothety X.left.sheaf
        (relativeDualizingComplexObj f j))
```

**`Stacks.Duality.isPseudoCoherent_of_isShriekOfStructureSheafOnCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativePerfection.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekRelativePerfection.lean#L193). The attribute's comment: “the pseudo-coherence half of the first assertion: f^! O_Y is a pseudo-coherent object of D(O_X), which is the first of the two conjuncts of Y-perfectness (Tag 0DI0). NOT claimed: the Tor-dimension conjunct of the first assertion, and the whole of the second assertion that O_X -> R SheafHom(f^! O_Y, f^! O_Y) is an isomorphism. Both rest on Stacks 0BZW, whose parts (1)(a), (1)(b) and (1)(c) are all proved in this repository at the level of rings -- (1)(b) as Dualizing.PolynomialPresentation.relativeDualizingComplex_hasFiniteTorDimension_of_isPerfectRingMap and (1)(c) as Dualizing.upperShriekFunctor_unit_isIso_derivedHomothety_of_isPerfectModule -- but what is absent is the affine-locality assembly for Tor dimension that Stacks 0DI2 would need, and there is no map O_X -> R SheafHom(K, K) on a scheme in this repository at all, so the sheaf-level second assertion cannot even be stated. Neither is carried as a hypothesis, since either would be the assertion itself. One hypothesis IS carried, hw: the affine-chart description of f^! O_Y, which is Stacks 0AA1 together with clause (b) of Stacks 0BV2; it asserts only an isomorphism, and it is the same hypothesis carried by Tag 0B6U part (a) and Tag 0AA3. Everything asserted about pseudo-coherence is proved, from Tag 0BZK (2) chart by chart -- whose perfect-ring-map hypothesis is discharged, not carried, from Flat and LocallyOfFinitePresentation through Tag 068A -- and Tag 08E8. f^! O_Y enters as an object of D+_QCoh(O_X) at CategoryTheory.HasDerivedCategory.standard characterised by hw, the idiom of Tag 0AA3, rather than as a value of Stacks.Duality.upperShriek, which is defined at the locally small model that Tag 08E8 is not available at”.

> **Stacks Project, Tag 0E9T, the pseudo-coherence half of the first assertion.** In
> Situation 48.16.1, let `f : X ⟶ Y` be a flat morphism of finite presentation of `FTS S`. Then the
> relative dualizing complex `ω^•_{X/Y} = f^!𝒪_Y` is a pseudo-coherent object of `D(𝒪_X)`.
>
> Over each chart the model of `f^!𝒪_Y` lies in `D^b_Coh` of the chart ring by
> Tag 0BZK (2); the chart bounds glue, and on a Noetherian scheme a bounded object with coherent
> cohomology is pseudo-coherent by Tag 08E8.

```lean
theorem isPseudoCoherent_of_isShriekOfStructureSheafOnCharts
    [Flat f.left] [LocallyOfFinitePresentation f.left]
    (ω : quasiCoherentDerivedCategory.{u + 1, u} X.left)
    (hw : IsShriekOfStructureSheafOnCharts f ω.obj) :
    RingedSpace.IsPseudoCoherent (X := X.left.toRingedSpace) ω.obj
```

## Tag 0B6V, a lemma

[Tag 0B6V](https://stacks.math.columbia.edu/tag/0B6V) in the Stacks Project.

**`Stacks.Duality.isInvertible_and_isPerfect_upperShriek_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekLocalCompleteIntersection.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekLocalCompleteIntersection.lean#L214).

> **Stacks Project, Tag 0B6V (Lemma 48.17.11).** In Situation 48.16.1 let `f : X ⟶ Y` be a
> local complete intersection morphism of `FTS S`. Then
> 1. `f^!𝒪_Y` is an invertible object of `D(𝒪_X)`, and
> 2. `f^!` maps perfect complexes to perfect complexes.
>
> Here `f^!` is computed at an arbitrary compactification `j`.

```lean
theorem isInvertible_and_isPerfect_upperShriek_of_isLocalCompleteIntersection
    (hf : IsLocalCompleteIntersectionMorphism f.left) :
    (letI := Scheme.Modules.derivedMonoidal X.left;
      MonoidalCategory.IsInvertible (relativeDualizingComplexObj f j)) ∧
    ∀ K : quasiCoherentDerivedCategory Y.left,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.left.toRingedSpace) K.obj →
        Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace)
          ((upperShriek f j).obj K).obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.17, Tag 0ATZ](https://stacks.math.columbia.edu/tag/0ATZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
