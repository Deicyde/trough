---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_admissibleBlowup_forall_restrict_factors, AlgebraicGeometry.exists_admissibleBlowup_finite_cover_restrict_factors, AlgebraicGeometry.cartierBoundaryDivisorReduction, AlgebraicGeometry.cartierBoundaryReduction, AlgebraicGeometry.StrictTransformProblem.isSolvable_of_local, AlgebraicGeometry.StrictTransformProblem.isSolvable_of_isSolvableIn, AlgebraicGeometry.exists_idealSheafData_forall_blowUp_exists_free_of_rank, Stacks.StrictTransform.exists_fg_ideal_forall_chartFreeOfRank
statement: formalized
proof: formalized
---

# 38.30 Blowing up and flatness

Section 38.30 of the Stacks Project, [Tag 080X](https://stacks.math.columbia.edu/tag/080X). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 080Y, a remark

[Tag 080Y](https://stacks.math.columbia.edu/tag/080Y) in the Stacks Project.

**`AlgebraicGeometry.exists_admissibleBlowup_forall_restrict_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleLocalOnBase.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleLocalOnBase.lean#L91). The attribute's comment: “locality on S: finitely many admissible blowups of quasi-compact opens of S are all refined by the restrictions of a single U-admissible blowup of S, each refinement itself an admissible blowup of the local solution”.

> **Stacks Project, Tag 080Y**, the locality on `S` of Remark 38.30.1, for a finite family of
> quasi-compact opens. Let `S` be quasi-compact and quasi-separated, `U ⊆ S` a quasi-compact open,
> and let `W j ⊆ S` be finitely many quasi-compact opens carrying `W j ∩ U`-admissible blowups
> `c j : V j ⟶ W j`. There is one `U`-admissible blowup `p : S' ⟶ S` whose restriction to each
> `W j` factors through `c j`.
>
> Each `c j` extends to a `U`-admissible blowup `q j : T j ⟶ S` with `IsPullback (c j) _ (W j).ι
> (q j)` by [Stacks, Tag 080M], and [Stacks, Tag 080N] produces a `U`-admissible `p : S' ⟶ S`
> factoring through every `q j` by a `q j ⁻¹ᵁ U`-admissible blowup `k j`. The restriction
> `p ∣_ W j` and the composite `(p ⁻¹ᵁ W j).ι ≫ k j` agree over `S`, so the cartesian square of
> [Stacks, Tag 080M] lifts them to the required map `r` to `V j`; and `r` is the base change of
> `k j` along the flat `g j`, hence admissible.

```lean
public theorem exists_admissibleBlowup_forall_restrict_factors
    [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens) (hU : IsCompact (U : Set S))
    {ι : Type*} [Finite ι] (W : ι → S.Opens) (hW : ∀ j, IsCompact ((W j : S.Opens) : Set S))
    (V : ι → Scheme.{u}) (c : ∀ j, V j ⟶ (W j).toScheme)
    (hc : ∀ j, Stacks.Blowup.IsAdmissibleBlowup ((W j).ι ⁻¹ᵁ U) (c j)) :
    ∃ (S' : Scheme.{u}) (p : S' ⟶ S), Stacks.Blowup.IsAdmissibleBlowup U p ∧
      ∀ j, ∃ r : (p ⁻¹ᵁ W j).toScheme ⟶ V j, r ≫ c j = p ∣_ (W j) ∧
        Stacks.Blowup.IsAdmissibleBlowup (c j ⁻¹ᵁ ((W j).ι ⁻¹ᵁ U)) r
```

**`AlgebraicGeometry.exists_admissibleBlowup_finite_cover_restrict_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleLocalOnBase.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AdmissibleLocalOnBase.lean#L134). The attribute's comment: “locality on S: a solution on a quasi-compact open neighbourhood of every point of S is refined, over a finite subcover, by the restrictions of a single U-admissible blowup of S, each refinement itself an admissible blowup of the local solution”.

> **Stacks Project, Tag 080Y**, the locality on `S` of Remark 38.30.1 in the paragraph's own
> formulation. Let `S` be quasi-compact and quasi-separated and `U ⊆ S` a quasi-compact open.
> Suppose that every point `s` of `S` has a quasi-compact open neighbourhood `W s` carrying a
> `W s ∩ U`-admissible blowup `c s : V s ⟶ W s`. Then there is a finite set of points whose
> neighbourhoods already cover `S`, and one `U`-admissible blowup `p : S' ⟶ S` whose restriction
> to each of those neighbourhoods factors through the blowup given there.
>
> The finite set comes from quasi-compactness of `S`, the blowup from
> `AlgebraicGeometry.exists_admissibleBlowup_forall_restrict_factors` applied to the finite
> subfamily.

```lean
public theorem exists_admissibleBlowup_finite_cover_restrict_factors
    [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens) (hU : IsCompact (U : Set S))
    (W : S → S.Opens) (hWmem : ∀ s : S, s ∈ W s)
    (hW : ∀ s : S, IsCompact ((W s : S.Opens) : Set S))
    (V : S → Scheme.{u}) (c : ∀ s : S, V s ⟶ (W s).toScheme)
    (hc : ∀ s : S, Stacks.Blowup.IsAdmissibleBlowup ((W s).ι ⁻¹ᵁ U) (c s)) :
    ∃ (F : Finset S) (S' : Scheme.{u}) (p : S' ⟶ S),
      (∀ x : S, ∃ s ∈ F, x ∈ W s) ∧ Stacks.Blowup.IsAdmissibleBlowup U p ∧
        ∀ s ∈ F, ∃ r : (p ⁻¹ᵁ W s).toScheme ⟶ V s, r ≫ c s = p ∣_ (W s) ∧
          Stacks.Blowup.IsAdmissibleBlowup (c s ⁻¹ᵁ ((W s).ι ⁻¹ᵁ U)) r
```

**`AlgebraicGeometry.cartierBoundaryDivisorReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/CartierBoundaryDivisorReduction.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/CartierBoundaryDivisorReduction.lean#L80). The attribute's comment: “the reduction to a divisor: after one U-admissible blowup the boundary is an effective Cartier divisor whose complement is the inverse image of U, and that inverse image is scheme theoretically dense”.

> **Stacks Project, Tag 080Y**, the reduction to a divisor of Remark 38.30.1 in full. On a
> quasi-compact and quasi-separated scheme `S` a quasi-compact open `U` becomes, after a single
> `U`-admissible blowup, the complement of an effective Cartier divisor `D` supported on the
> boundary; and then `U` is scheme theoretically dense.
>
> The centre is the one of `AlgebraicGeometry.cartierBoundaryReduction`, and `D` is the
> exceptional divisor of its blowup: an effective Cartier divisor by [Stacks, Tag 02OS] part (2)
> (`Stacks.Blowup.isEffectiveCartierDivisor_exceptionalIdeal`), whose support is the boundary by
> that theorem. The density is then [Stacks, Tag 07ZU]
> (`Stacks.Divisors.isSchemeTheoreticallyDense_compl_of_isEffectiveCartierDivisor`): the
> complement of an effective Cartier divisor is scheme theoretically dense.

```lean
public theorem cartierBoundaryDivisorReduction [CompactSpace S] [QuasiSeparatedSpace S]
    (U : S.Opens) (hU : IsCompact (U : Set S)) : CartierBoundaryDivisorReduction S U
```

**`AlgebraicGeometry.cartierBoundaryReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/DominatedByBlowup.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/DominatedByBlowup.lean#L178).

> **Stacks Project, Tag 080Y.** On a quasi-compact and quasi-separated scheme `S`, a
> quasi-compact open `U` becomes the complement of an effective Cartier divisor after a single
> `U`-admissible blowup: a finite type quasi-coherent ideal sheaf `I` cutting out `S ∖ U` is
> finitely presented as a closed subscheme, is disjoint from `U`, and the exceptional divisor of
> the blowup of `S` in `I` is exactly the complement of the inverse image of `U`.

```lean
public theorem cartierBoundaryReduction [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens)
    (hU : IsCompact (U : Set S)) : CartierBoundaryReduction S U
```

**`AlgebraicGeometry.StrictTransformProblem.isSolvable_of_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformProblem/LocalGlobal.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformProblem/LocalGlobal.lean#L268). The attribute's comment: “the local-global reduction, the remark's third paragraph; the locality of P on the base is the hypothesis the remark states it under”.

> **[Stacks, Tag 080Y], the local-global reduction.** Suppose the property `P` is local on the
> base: for every strict-transform problem with that property, if the base is covered by finitely
> many quasi-compact opens over each of which the restricted triple has `P`, then the triple itself
> has `P`. Then the strict-transform problem is local on the base too: if every point of `S` has a
> quasi-compact open neighbourhood over which the problem is solvable, the problem is solvable.

```lean
public theorem isSolvable_of_local (D : StrictTransformProblem.{u})
    (hP : ∀ E : StrictTransformProblem.{u}, @E.P = @D.P →
      ∀ {ι : Type} [Finite ι] (W : ι → E.S.Opens) (hW : ∀ i, IsCompact (W i : Set E.S)),
        (⋃ i, (W i : Set E.S)) = Set.univ →
        (∀ i, (E.restrict (W i) (hW i)).P (E.restrict (W i) (hW i)).f
          (E.restrict (W i) (hW i)).F) →
        E.P E.f E.F)
    (hlocal : ∀ s : D.S, ∃ (W : D.S.Opens) (hW : IsCompact (W : Set D.S)),
      s ∈ (W : Set D.S) ∧ (D.restrict W hW).IsSolvable) :
    D.IsSolvable
```

**`AlgebraicGeometry.StrictTransformProblem.isSolvable_of_isSolvableIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformProblem/Successive.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformProblem/Successive.lean#L135). The attribute's comment: “the successive reduction, the paragraph beginning `The general strategy will be to use that a composition of U-admissible blowups is a U-admissible blowup': it suffices to find a sequence of U-admissible blowups S = S_0 <- S_1 <- ... <- S_n such that, setting F_0 = F and X_0 = X and F_i/X_i the strict transform of F_{i-1}/X_{i-1}, the triple F_n/X_n/S_n has P. The sequence is IsSolvableIn n and the single blowup it is replaced by is IsSolvable”.

> **[Stacks, Tag 080Y], the successive reduction.** To solve the strict-transform problem it
> suffices to find a *sequence* of `U`-admissible blowups `S = S₀ ← S₁ ← … ← Sₙ` whose iterated
> strict transform has the property `P`: such a sequence is replaced by a single `U`-admissible
> blowup with the same effect.
>
> The sequence is contracted one stage at a time: the amalgamation of [Stacks, Tag 080B], fed by
> the second-centre factorization of [Stacks, Tag 0803], replaces the last two centres by a single
> admissible centre on the previous base, and [Stacks, Tag 080I] identifies the iterated strict
> transform with the strict transform in it.

```lean
public theorem isSolvable_of_isSolvableIn (n : ℕ) (D : StrictTransformProblem.{u})
    (h : D.IsSolvableIn n) : D.IsSolvable
```

## Tag 0810, a lemma

[Tag 0810](https://stacks.math.columbia.edu/tag/0810) in the Stacks Project.

**`AlgebraicGeometry.exists_idealSheafData_forall_blowUp_exists_free_of_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/BlowupIntegralFibresGeometric.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/BlowupIntegralFibresGeometric.lean#L316). The attribute's comment: “the scheme-level form”.

> **Stacks Project, Tag 0810.** Let `S` be an affine scheme, `s : Γ(S, ⊤)`, `r ≥ 0` an integer,
> `f : X ⟶ S` an affine morphism and `F` a quasi-coherent `𝒪_X`-module. Assume
>
> 1. `f` is of finite presentation and flat with geometrically integral fibres;
> 2. `F` is of finite type;
> 3. `F` restricted to `f⁻¹(D(s))` is of finite presentation;
> 4. for every point `x` of `X` which is generic in its fibre and whose image lies in `D(s)`, the
>    stalk `F_x` is free of rank `r` over `𝒪_{X,x}`.
>
> Then there is a quasi-coherent sheaf of ideals `ℐ` on `S` whose ideal of global sections is
> finitely generated and whose support is `V(s)`, such that over every point `z` of the blowup
> `Bl_ℐ(S)` there is a point of `X ×_S Bl_ℐ(S)` above `z` with an open neighbourhood on which the
> strict transform of `F` is free of rank `r`.
>
> This is the geometric reading of the ring-level
> `AlgebraicGeometry.exists_fg_ideal_forall_blowup_chart_exists_away_basis`: hypotheses (1)–(4) are
> converted into its hypotheses on `Γ(S, ⊤) → Γ(X, ⊤)` and `Γ(F, ⊤)`, and its conclusion — the
> `a`-power-torsion quotient of the base change becomes free of rank `r` after inverting one
> element per prime of each affine blowup chart — is carried onto the sheaf-level strict transform
> by `AlgebraicGeometry.exists_free_open_of_chart_at`.

```lean
public theorem exists_idealSheafData_forall_blowUp_exists_free_of_rank
    {S X : Scheme.{u}} [IsAffine S] (f : X ⟶ S) [IsAffineHom f] [Flat f]
    [GeometricallyIntegral f] (hf : AlgebraicGeometry.FinitePresentation f)
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (s : Γ(S, ⊤)) (r : ℕ)
    (hFU : (F.restrict (f ⁻¹ᵁ S.basicOpen s).ι).IsFinitePresentation)
    (hrank : ∀ x : X, f.base x ∈ S.basicOpen s → f.base ⁻¹' {f.base x} ⊆ closure {x} →
      letI := Stacks.ModuleStalkSpecialization.stalkModule F x
      Nonempty (Module.Basis (Fin r) (X.presheaf.stalk x) (F.presheaf.stalk x))) :
    ∃ ℐ : S.IdealSheafData,
      (ℐ.ideal ⟨⊤, isAffineOpen_top S⟩).FG ∧
      (ℐ.support : Set S) = (↑(S.basicOpen s))ᶜ ∧
      ∀ z : Stacks.Blowup.blowUp ℐ,
        ∃ (W : (Limits.pullback f (Stacks.Blowup.blowUpToBase ℐ)).Opens)
          (x : ↥(Limits.pullback f (Stacks.Blowup.blowUpToBase ℐ))),
          x ∈ W ∧ (pullback.snd f (Stacks.Blowup.blowUpToBase ℐ)).base x = z ∧
          Nonempty ((Stacks.StrictTransform.sheaf f (Stacks.Blowup.blowUpToBase ℐ)
            (Stacks.Blowup.exceptionalIdeal ℐ) F).restrict W.ι ≅
              SheafOfModules.free.{u} (ULift.{u} (Fin r)))
```

**`Stacks.StrictTransform.exists_fg_ideal_forall_chartFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/AffineChartSections.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/AffineChartSections.lean#L302). The attribute's comment: “the conclusion read on the strict transform of [Stacks, Tag 080D]: on every affine chart of a base change on which the inverse image of the centre is the zero locus of the image of the chart's denominator, the strict transform of the module is free of rank r on a basic open through every extended prime of the chart base. The hypotheses are the source's own, read on the global sections of the two affine schemes; the existence of such charts is not claimed”.

> **Stacks Project, Tag 0810, read on the strict transform.** Let `S` be an affine scheme, `X`
> an affine scheme over it with `Γ(S, ⊤) ⟶ Γ(X, ⊤)` flat and of finite presentation with
> geometrically integral fibres, let `F` be a quasi-coherent module on `X` presented as `M^~` with
> `M` finite over `Γ(X, ⊤)`, let `t : Γ(S, ⊤)` and `r : ℕ`, and assume `M` is finitely presented
> after inverting `t` and free of rank `r` at every extended prime `qΓ(X, ⊤)` with `t ∉ q`. Then
> there is a finitely generated ideal `I ⊆ Γ(S, ⊤)` with `V(t) = V(I)` such that for every `a ∈ I`
> and every prime `q'` of the affine blowup algebra `Γ(S, ⊤)[I/a]`, the chart
> `Spec (Γ(X, ⊤) ⊗_{Γ(S,⊤)} Γ(S, ⊤)[I/a])` of a base change satisfies
> `Stacks.StrictTransform.ChartFreeOfRank` for the image of `a` and the extension of `q'`: on every
> such chart on which the inverse image of the centre is the zero locus of the image of `a`, the
> strict transform of `F` of [Stacks, Tag 080D] is free of rank `r` on a basic open `D(g)` with `g`
> outside `q'·(Γ(X, ⊤) ⊗ Γ(S, ⊤)[I/a])`.
>
> This is the scheme-level form of the ring-level
> `exists_fg_ideal_forall_blowup_chart_exists_away_basis`: the ideal, the chart algebras and the
> element `g` are the ring-level ones, and the module the ring-level statement produces a basis for
> is identified with the strict transform by `Stacks.StrictTransform.affineChartSheafIso`, through
> `Stacks.StrictTransform.nonempty_restrict_basicOpen_free_of_basis`. It is the form the proof of
> [Stacks, Tag 0811] consumes, which is about the strict transform and not about the chart-level
> torsion quotient: freeness of the strict transform near the generic point of a fibre of
> `X ×_S Bl_I(S) ⟶ Bl_I(S)` is the flatness conjunct of
> `AlgebraicGeometry.GenericFibreFlatteningBlowup`.
>
> The charts are universally quantified inside `Stacks.StrictTransform.ChartFreeOfRank`: nothing is
> claimed here about their existence, which is the content of [Stacks, Tag 0804] for the blowup of
> `S` in `I` together with the base change of that covering along `f`.

```lean
public theorem exists_fg_ideal_forall_chartFreeOfRank [IsAffine X] [IsAffine S] (f : X ⟶ S)
    (F : X.Modules) [F.IsQuasicoherent] (M : ModuleCat.{u} Γ(X, ⊤))
    (e : F ≅ (Scheme.Modules.pullback X.isoSpec.hom).obj (tilde M))
    [Algebra Γ(S, ⊤) Γ(X, ⊤)]
    (halg : (algebraMap Γ(S, ⊤) Γ(X, ⊤) : Γ(S, ⊤) →+* Γ(X, ⊤)) = f.appTop.hom)
    [Algebra.FinitePresentation Γ(S, ⊤) Γ(X, ⊤)] [Module.Flat Γ(S, ⊤) Γ(X, ⊤)]
    [Module.Finite Γ(X, ⊤) M] (t : Γ(S, ⊤)) (r : ℕ)
    (hfibre : ∀ (q : Ideal Γ(S, ⊤)) (hq : q.IsPrime),
      letI := hq
      Algebra.IsGeometricallyIntegral q.ResidueField (q.Fiber Γ(X, ⊤)))
    (hfp : Module.FinitePresentation (Localization.Away (algebraMap Γ(S, ⊤) Γ(X, ⊤) t))
      (LocalizedModule (Submonoid.powers (algebraMap Γ(S, ⊤) Γ(X, ⊤) t)) M))
    (hrank : ∀ (q : Ideal Γ(S, ⊤)) (hq : q.IsPrime), t ∉ q →
      letI := hq
      let 𝔮 := Ideal.map (algebraMap Γ(S, ⊤) Γ(X, ⊤)) q
      ∀ h𝔮 : 𝔮.IsPrime,
        letI := h𝔮
        Nonempty (LocalizedModule 𝔮.primeCompl M ≃ₗ[Localization 𝔮.primeCompl]
          (Fin r → Localization 𝔮.primeCompl))) :
    ∃ I : Ideal Γ(S, ⊤), I.FG ∧
      (∀ q : Ideal Γ(S, ⊤), q.IsPrime → (t ∈ q ↔ I ≤ q)) ∧
      ∀ (a : Γ(S, ⊤)) (ha : a ∈ I),
        letI : Fact (a ∈ I) := ⟨ha⟩
        ∀ q' : Ideal (Blowup I a), q'.IsPrime →
          ChartFreeOfRank f F M (CommRingCat.of (Γ(X, ⊤) ⊗[Γ(S, ⊤)] Blowup I a))
            (CommRingCat.ofHom (algebraMap Γ(X, ⊤) (Γ(X, ⊤) ⊗[Γ(S, ⊤)] Blowup I a)))
            (algebraMap Γ(X, ⊤) (Γ(X, ⊤) ⊗[Γ(S, ⊤)] Blowup I a) (f.appTop.hom a)) r
            (Ideal.map Algebra.TensorProduct.includeRight q')
```

**`exists_fg_ideal_forall_blowup_chart_exists_away_basis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BlowupFlattening.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/BlowupFlattening.lean#L57).

> **Stacks Project, Tag 0810.** Let `R → S` be flat and of finite presentation with
> geometrically integral fibres, let `f : R`, and let `M` be a finite `S`-module which is finitely
> presented after inverting `f` and free of rank `r` at every extended prime `pS` with `f ∉ p`.
> Then there is a finitely generated ideal `I ⊆ R` with `V(f) = V(I)` such that for every `a ∈ I`,
> writing `R' = R[I/a]` and `S' = S ⊗[R] R'`, the quotient `M'` of `S' ⊗[S] M` by its `a`-power
> torsion is free of rank `r` after inverting some `g : S'` outside `p'S'`, for every prime `p'` of
> `R'`.
>
> This is `exists_fg_ideal_forall_blowup_chart_exists_away_basis_of_projective` with its hypothesis
> `Module.Projective R S` supplied by Stacks 05FT,
> `Algebra.projective_of_geometricallyIntegral_fibres`.

```lean
public theorem exists_fg_ideal_forall_blowup_chart_exists_away_basis
    (R S : Type u) [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.FinitePresentation R S] [Module.Flat R S]
    (M : Type v) [AddCommGroup M] [Module S M] [Module R M] [IsScalarTower R S M]
    [Module.Finite S M] (f : R) (r : ℕ)
    (hfibre : ∀ (p : Ideal R) (hp : p.IsPrime),
      letI := hp
      Algebra.IsGeometricallyIntegral p.ResidueField (p.Fiber S))
    (hfp : Module.FinitePresentation (Localization.Away (algebraMap R S f))
      (LocalizedModule (Submonoid.powers (algebraMap R S f)) M))
    (hrank : ∀ (p : Ideal R) (hp : p.IsPrime), f ∉ p →
      letI := hp
      let q := Ideal.map (algebraMap R S) p
      ∀ hq : q.IsPrime,
        letI := hq
        Nonempty
          (LocalizedModule q.primeCompl M ≃ₗ[Localization q.primeCompl]
            (Fin r → Localization q.primeCompl))) :
    ∃ I : Ideal R, I.FG ∧
      (∀ (p : Ideal R), p.IsPrime → (f ∈ p ↔ I ≤ p)) ∧
      ∀ (a : R) (ha : a ∈ I),
        letI : Fact (a ∈ I) := ⟨ha⟩
        let R' := Blowup I a
        let S' := S ⊗[R] R'
        let N := S' ⊗[S] M
        let M' := N ⧸ Submodule.torsion' S' N
          (Submonoid.powers (algebraMap S S' (algebraMap R S a)))
        ∀ (p' : Ideal R') (_hp' : p'.IsPrime), ∃ g : S',
          g ∉ Ideal.map Algebra.TensorProduct.includeRight p' ∧
          Nonempty
            (LocalizedModule (Submonoid.powers g) M' ≃ₗ[Localization.Away g]
              (Fin r → Localization.Away g))
```

## Tag 0811, a lemma

[Tag 0811](https://stacks.math.columbia.edu/tag/0811) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_opens_finitelyLocallyFree_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/BlowupIntegralFibres0811.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/BlowupIntegralFibres0811.lean#L147). The attribute's comment: “the full statement under hypotheses (1)-(4) of the source: a U-admissible blowup and an open of the base change on which the strict transform is finitely locally free and which surjects onto the blowup”.

> **Stacks Project, Tag 0811.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be a morphism, let `F` be a quasi-coherent `𝒪_X`-module and let `U ⊆ S` be a
> quasi-compact open. Assume
>
> 1. `f` is affine, of finite presentation, flat, with geometrically integral fibres;
> 2. `F` is of finite type;
> 3. `F` restricted to `X_U` is of finite presentation;
> 4. `F` is flat over `S` at every generic point of a fibre over a point of `U`.
>
> Then there is a `U`-admissible blowup of `S` — given by a centre `I` of finite presentation whose
> support avoids `U` — and an open subscheme `V` of `X ×_S Bl_I(S)` such that
>
> * **(a)** the strict transform of `F` along the blowup is free of finite rank on an open
>   neighbourhood, inside `V`, of every point of `V`, that is, finitely locally free on `V`, and
> * **(b)** `V` surjects onto `Bl_I(S)`.
>
> The rank at the generic point of a fibre over `U` is made constant by iterating
> [Stacks, Tag 080P]; the complement of `U` is made an effective Cartier divisor and then, locally
> on the base, principal on an affine open, by the observations of [Stacks, Tag 080Y]; and that case
> is [Stacks, Tag 0810].

```lean
theorem exists_isAdmissibleBlowup_opens_finitelyLocallyFree_surjective
    {S X : Scheme.{u}} [CompactSpace S] [QuasiSeparatedSpace S] (f : X ⟶ S)
    [IsAffineHom f] [Flat f] [GeometricallyIntegral f]
    (hf : AlgebraicGeometry.FinitePresentation f)
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (U : S.Opens)
    (hU : IsCompact (U : Set S))
    (hFU : (F.restrict (f ⁻¹ᵁ U).ι).IsFinitePresentation)
    (hflat : ∀ x : X, f.base x ∈ U → f.base ⁻¹' {f.base x} ⊆ closure {x} →
      IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ I : S.IdealSheafData,
      FinitePresentation I.subschemeι ∧
      Disjoint (U : Set S) (I.support : Set S) ∧
      Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase I) ∧
      ∃ V : (Stacks.StrictTransform.baseChange f (blowUpToBase I)).Opens,
        (∀ z : Stacks.StrictTransform.baseChange f (blowUpToBase I), z ∈ V →
          ∃ (W : (Stacks.StrictTransform.baseChange f (blowUpToBase I)).Opens) (n : ℕ),
            z ∈ W ∧ W ≤ V ∧
            Nonempty ((Stacks.StrictTransform.sheaf f (blowUpToBase I)
              (exceptionalIdeal I) F).restrict W.ι ≅
                SheafOfModules.free.{u} (ULift.{u} (Fin n)))) ∧
        Function.Surjective (V.ι ≫ pullback.snd f (blowUpToBase I)).base
```

## Tag 0812, a lemma

[Tag 0812](https://stacks.math.columbia.edu/tag/0812) in the Stacks Project.

**`fittingIdealZero_quotient_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FittingIdealEtale.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FittingIdealEtale.lean#L83). The attribute's comment: “finite generation of the Fitting ideal”.

> **Stacks Project, Tag 0812.** The zeroth Fitting ideal of a quotient of a finite
> projective algebra by a finitely generated ideal is finitely generated.

```lean
theorem fittingIdealZero_quotient_fg
    (A : Type u) (C : Type v) [CommRing A] [CommRing C] [Algebra A C]
    [Module.Finite A C] [Module.Projective A C] (J : Ideal C) (hJ : J.FG) :
    (fittingIdeal (R := A) (M := C ⧸ J) 0).FG
```

**`map_fittingIdealZero_quotient_eq_mul_of_etale_away`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FittingIdealEtale.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FittingIdealEtale.lean#L263). The attribute's comment: “factorization after localization”.

> **Stacks Project, Tag 0812.** Let `C` be a finite locally free `A`-algebra and let `J` be
> an ideal of `C`. If `C` becomes étale over `A` after inverting `h`, then the extension of
> the zeroth Fitting ideal of `C ⧸ J` is the product of the extension of `J` with another
> ideal. This other ideal can be chosen finitely generated whenever `J` is finitely
> generated.

```lean
theorem map_fittingIdealZero_quotient_eq_mul_of_etale_away
    (A : Type u) (C : Type v) [CommRing A] [CommRing C] [Algebra A C]
    [Module.Finite A C] [Module.Projective A C] (h : C)
    (het : Algebra.Etale A (Localization.Away h)) (J : Ideal C) :
    ∃ J' : Ideal (Localization.Away h),
      (fittingIdeal (R := A) (M := C ⧸ J) 0).map (algebraMap A (Localization.Away h)) =
          J.map (algebraMap C (Localization.Away h)) * J' ∧
        (J.FG → J'.FG)
```

## Tag 0813, a lemma

[Tag 0813](https://stacks.math.columbia.edu/tag/0813) in the Stacks Project.

**`exists_ideal_map_eq_mul_after_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FittingIdealEtale.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/FittingIdealEtale.lean#L403).

> **Stacks Project, Tag 0813.** Let `A → B` be étale, let `a ∈ A`, and let `J` be a
> finitely generated ideal of `B` with `V(J) ⊆ V(aB)`. At every prime `q` of `B`,
> after localizing at some `g ∉ q`, the extension of a finitely generated ideal
> `I` of `A`, with `V(I) ⊆ V(a)`, is the product of the extension of `J` and a
> finitely generated ideal.

```lean
theorem exists_ideal_map_eq_mul_after_localization
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [Algebra.Etale A B] (a : A) (J : Ideal B) (hJ : J.FG)
    (hV : algebraMap A B a ∈ J.radical) (q : Ideal B) [q.IsPrime] :
    ∃ I : Ideal A, I.FG ∧ a ∈ I.radical ∧
      ∃ g : B, g ∉ q ∧
        ∃ J' : Ideal (Localization.Away g), J'.FG ∧
          Ideal.map ((algebraMap B (Localization.Away g)).comp (algebraMap A B)) I =
            Ideal.map (algebraMap B (Localization.Away g)) J * J'
```

## Tag 0814, a lemma

[Tag 0814](https://stacks.math.columbia.edu/tag/0814) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_isFlatOver_strictTransformSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/EtaleLocalFlatteningDescent.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/EtaleLocalFlatteningDescent.lean#L106). The attribute's comment: “the surjectivity half of condition (1) is not assumed; it is unused”.

> **Stacks Project, Tag 0814.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be a morphism of schemes, let `F` be a quasi-coherent `𝒪_X`-module and let `U ⊆ S` be
> a quasi-compact open. Assume given finitely many commutative squares `jᵢ ≫ f = fᵢ ≫ eᵢ` with
>
> 1. `eᵢ : Sᵢ ⟶ S` quasi-compact and étale,
> 2. `jᵢ : Xᵢ ⟶ X` étale and jointly surjective,
> 3. a centre `Iᵢ` on `Sᵢ` which is finitely presented as a closed subscheme and supported away
>    from `eᵢ⁻¹(U)` — so the blowup of `Sᵢ` in `Iᵢ` is an `eᵢ⁻¹(U)`-admissible blowup — such that
>    the strict transform of `jᵢ^* F` along it is flat over it.
>
> Then there is a centre `I` on `S`, finitely presented and supported away from `U`, exhibiting the
> blowup of `S` in `I` as a `U`-admissible blowup, such that the strict transform of `F` along that
> blowup is flat over it.

```lean
theorem exists_isAdmissibleBlowup_isFlatOver_strictTransformSheaf {S X : Scheme.{u}}
    [CompactSpace S] [QuasiSeparatedSpace S] (f : X ⟶ S) (F : X.Modules) [F.IsQuasicoherent]
    (U : S.Opens) (hU : IsCompact (U : Set S)) {ι : Type*} [Finite ι]
    (Sᵢ Xᵢ : ι → Scheme.{u}) (e : ∀ i, Sᵢ i ⟶ S) (j : ∀ i, Xᵢ i ⟶ X)
    (fᵢ : ∀ i, Xᵢ i ⟶ Sᵢ i) (Iᵢ : ∀ i, (Sᵢ i).IdealSheafData)
    (he : ∀ i, Etale (e i) ∧ QuasiCompact (e i)) (hj : ∀ i, Etale (j i))
    (hcoverX : ∀ x : X, ∃ i : ι, ∃ y : Xᵢ i, (j i).base y = x)
    (hcomm : ∀ i, j i ≫ f = fᵢ i ≫ e i)
    (hadm : ∀ i, FinitePresentation (Iᵢ i).subschemeι ∧
      Disjoint (e i ⁻¹ᵁ U : Set (Sᵢ i)) ((Iᵢ i).support : Set (Sᵢ i)))
    (hflat : ∀ i, IsFlatOver
      (pullback.snd (fᵢ i) (blowUpToBase (Iᵢ i))).toLRSHom.toShHom
      (Stacks.StrictTransform.sheaf (fᵢ i) (blowUpToBase (Iᵢ i)) (exceptionalIdeal (Iᵢ i))
        ((Scheme.Modules.pullback (j i)).obj F))) :
    ∃ I : S.IdealSheafData,
      FinitePresentation I.subschemeι ∧
      Disjoint (U : Set S) (I.support : Set S) ∧
      Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase I) ∧
      IsFlatOver (pullback.snd f (blowUpToBase I)).toLRSHom.toShHom
        (Stacks.StrictTransform.sheaf f (blowUpToBase I) (exceptionalIdeal I) F)
```

## Tag 0815, a theorem

[Tag 0815](https://stacks.math.columbia.edu/tag/0815) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_isFlatOver_strictTransformSheaf_of_affineCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ModuleFlatteningBlowup.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/ModuleFlatteningBlowup.lean#L129).

> **Stacks Project, Tag 0815.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be locally of finite presentation with `X` quasi-compact, let `F` be a quasi-coherent
> `𝒪_X`-module of finite type and let `U ⊆ S` be a quasi-compact open such that the restriction of
> `F` to `f⁻¹(U)` is of finite presentation and flat over `U`. Then there is a centre `I` on `S`,
> finitely presented and supported away from `U`, exhibiting the blowup of `S` in `I` as a
> `U`-admissible blowup, such that the strict transform of `F` along that blowup is an
> `𝒪_{X ×_S S'}`-module of finite presentation and flat over the blowup.
>
> The centre is the one of `AlgebraicGeometry.exists_flatteningCentre_supportSet_eq_compl`, whose
> support is `S ∖ U`; so the inverse image of `U` in the blowup is the complement of the exceptional
> divisor, hence retrocompact and scheme-theoretically dense, and [Stacks, Tag 081N] gives finite
> presentation of the flat strict transform from its finite presentation over that open.

```lean
theorem exists_isAdmissibleBlowup_isFlatOver_strictTransformSheaf_of_affineCharts
    [CompactSpace S] [QuasiSeparatedSpace S] [CompactSpace X] (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (U : S.Opens) (hU : IsCompact (U : Set S))
    (hFfp : ((Scheme.Modules.pullback (f ⁻¹ᵁ U).ι).obj F).IsFinitePresentation)
    (hFflat : IsFlatOver (f ∣_ U).toLRSHom.toShHom
      ((Scheme.Modules.pullback (f ⁻¹ᵁ U).ι).obj F)) :
    ∃ I : S.IdealSheafData,
      FinitePresentation I.subschemeι ∧
      Disjoint (U : Set S) (I.support : Set S) ∧
      Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase I) ∧
      (Stacks.StrictTransform.sheaf f (blowUpToBase I)
        (exceptionalIdeal I) F).IsFinitePresentation ∧
      IsFlatOver (pullback.snd f (blowUpToBase I)).toLRSHom.toShHom
        (Stacks.StrictTransform.sheaf f (blowUpToBase I) (exceptionalIdeal I) F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.30, Tag 080X](https://stacks.math.columbia.edu/tag/080X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
