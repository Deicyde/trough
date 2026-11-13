---
declaration: section
origin: cited
lean: Stacks.Blowup.pushforwardReesGradedModule, Stacks.Blowup.pushforwardReesGradedModulePlus, Stacks.Cohomology.FormalFunctions.isCohomologyReesFinite, Stacks.Algebraization.isQuasicoherent_and_isFiniteType_pushforwardReesGradedModulePlus, Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_of_isProper, Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient_of_isProper, Stacks.Cohomology.FormalFunctions.exists_formalFunctionsEquiv_of_isProper, Stacks.Algebraization.isIso_cohomologyToLimit_of_isProper_of_isAdicComplete
statement: formalized
proof: formalized
---

# 30.20 The theorem on formal functions

Section 30.20 of the Stacks Project, [Tag 02O7](https://stacks.math.columbia.edu/tag/02O7). 10 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02O7, the section

[Tag 02O7](https://stacks.math.columbia.edu/tag/02O7) in the Stacks Project.

**`Stacks.Blowup.pushforwardReesGradedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModule.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModule.lean#L116). The attribute's comment: “⨁ₙ f\_*(ℐⁿℱ) is a graded ⨁ₙ ℐⁿ-module on the base”.

> **[Stacks, Tag 02O7]: the graded `⨁ₙ ℐⁿ`-module `⨁ₙ f_*(ℐⁿℱ)` on the base, in degree
> zero.**  The maps `pushforwardReesSmul` make the pushforwards of the ideal-power multiples of
> `ℱ` a graded module over the Rees algebra of `ℐ` on `Y`.
>
> Since `f_*` is left exact it is `R ⁰ f_*`, so this is the structure the source puts on
> `⨁ₙ R ᵖ f_*(ℐⁿℱ)` for `p = 0`.  Each axiom is the corresponding axiom of
> `Stacks.Blowup.reesGradedModule` on `X`, transported along the multiplicativity and unitality of
> `Stacks.Blowup.reesPieceComap`; the compatibility with restriction on `Y` is inherited from
> `reesPieceComap` being a morphism of sheaves.

```lean
public def pushforwardReesGradedModule : SheafOfModules.GradedModule (reesGradedAlgebra I)
```

**`Stacks.Blowup.pushforwardReesGradedModulePlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModulePlus.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModulePlus.lean#L450). The attribute's comment: “⨁ₙ R ᵖ f\_*(ℐⁿℱ) is a graded ⨁ₙ ℐⁿ-module on the base, in every degree p”. References: EGA III (3.3.1), “special case”.

> **[Stacks, Tag 02O7]: the graded `⨁ₙ ℐⁿ`-module `⨁ₙ R ᵖ f_*(ℐⁿℱ)` on the base, in every
> degree `p`.**  This is the structure the setup paragraph of the source obtains "by localizing and
> then sheafifying": the maps `ℐⁱ ⊗_{𝒪_Y} R ᵖ f_*(ℐⁿℱ) ⟶ R ᵖ f_*(ℐⁿ⁺ⁱℱ)`, presented as the
> biadditive maps on sections that `SheafOfModules.GradedModule` consumes, together with the four
> laws.
>
> `Stacks.Blowup.pushforwardReesGradedModule` is the same statement for `p = 0`, and is **not**
> superseded by this one: there the action is the multiplication of the Rees algebra on sections,
> by `rfl`, whereas here it divides by the higher direct image of the unit of
> `AlgebraicGeometry.Scheme.Modules.restrictAdjunction`, and the two agree at `p = 0` only through
> `R ⁰ f_* ≅ f_*`.

```lean
public def pushforwardReesGradedModulePlus (f : X ⟶ Y) (I : Y.IdealSheafData) (F : X.Modules)
    (p : ℕ) : SheafOfModules.GradedModule (reesGradedAlgebra I)
```

## Tag 02O8, a lemma

[Tag 02O8](https://stacks.math.columbia.edu/tag/02O8) in the Stacks Project.

**`Stacks.Cohomology.FormalFunctions.isCohomologyReesFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/ReesCohomologyFiniteReduction.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/ReesCohomologyFiniteReduction.lean#L46). References: EGA III (3.3.2); EGA III (4.1.7.12), “more general”.

> **[Stacks, Tag 02O8].** For `A` Noetherian, `f : X ⟶ Spec A` proper and `ℱ` coherent, the
> graded module `⨁_{n ≥ 0} Hᵖ(X, Iⁿℱ)` is a finite module over the Rees algebra
> `B = ⨁_{n ≥ 0} Iⁿ`.
>
> This is `Stacks.Cohomology.FormalFunctions.isCohomologyReesFinite_of_isCoherent`, the reduction
> of the tag to [Stacks, Tag 0897] part (1) at a graded `⨁ₙ ℐⁿ`-module, with that hypothesis
> supplied by `Stacks.Cohomology.FormalFunctions.isCohomologyReesFiniteOfGradedModule`.

```lean
public theorem isCohomologyReesFinite [IsNoetherianRing A]
    (F : X.left.Modules) [F.IsCoherent] (p : ℕ)
    (hX : AlgebraicGeometry.IsProper X.hom) :
    IsCohomologyReesFinite I X F p
```

## Tag 02O9, a lemma

[Tag 02O9](https://stacks.math.columbia.edu/tag/02O9) in the Stacks Project.

**`Stacks.Algebraization.isQuasicoherent_and_isFiniteType_pushforwardReesGradedModulePlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/HigherDirectImageFiniteTypeSpan.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/HigherDirectImageFiniteTypeSpan.lean#L426). References: EGA III (2.4.2), “special case”; SGA 2 XII (5.8), “(ii), special case”.

> **Stacks Project, Tag 02O9.** Let `f : X ⟶ Y` be a morphism of schemes, `ℱ` an `𝒪_X`-module
> and `ℐ ⊆ 𝒪_Y` a quasi-coherent sheaf of ideals, and assume `Y` locally Noetherian, `f` proper
> and `ℱ` coherent. Then the graded `𝒜 = ⨁ₙ ℐⁿ`-module
> `ℳ = ⨁ₙ R ᵖ f_*(ℐⁿℱ) = Stacks.Blowup.pushforwardReesGradedModulePlus f ℐ ℱ p`
> is **quasi-coherent** — every homogeneous piece is — and **of finite type** over `𝒜`.
>
> This is the source's own argument. Quasi-coherence of a piece is [Stacks, Tag 01XJ] applied to
> `ℐⁿℱ`. Finite type is local on `Y`, and over an affine open `V` it is [Stacks, Tag 02O8] on the
> chart `f⁻¹(V) ⟶ Spec Γ(Y, V)`, turned into the spanning family the affine criterion
> `SheafOfModules.GradedModule.isFiniteType_of_affine_span` consumes by
> `Stacks.Algebraization.exists_affine_span_pushforwardReesGradedModulePlus`.
>
> Quasi-compactness and quasi-separatedness of `f` and quasi-coherence of `ℱ` are consequences of
> the source's hypotheses and are derived, not assumed.

```lean
public theorem isQuasicoherent_and_isFiniteType_pushforwardReesGradedModulePlus
    [IsLocallyNoetherian Y] [IsProper f] [F.IsCoherent] :
    (∀ n : ℤ, ((Stacks.Blowup.pushforwardReesGradedModulePlus f I F p).piece n).IsQuasicoherent) ∧
      (Stacks.Blowup.pushforwardReesGradedModulePlus f I F p).IsFiniteType
        (J := Opens.grothendieckTopology Y)
```

## Tag 02OA, a lemma

[Tag 02OA](https://stacks.math.columbia.edu/tag/02OA) in the Stacks Project.

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L104). The attribute's comment: “all five parts, for a proper scheme over a Noetherian ring and a coherent module”.

> **[Stacks, Tag 02OA].** For `A` Noetherian, `I ⊆ A` an ideal, `f : X ⟶ Spec A` proper and
> `ℱ` coherent there is one integer `c ≥ 0` such that
>
> 1. the multiplication map `Iʳ⁻ᶜ ⊗ Hᵖ(X, Iᶜℱ) → Hᵖ(X, Iʳℱ)` is surjective for `r ≥ c`;
> 2. the image of `Hᵖ(X, Iⁿ⁺ᵐℱ) → Hᵖ(X, Iⁿℱ)` is contained in `Iᵐ⁻ᵉHᵖ(X, Iⁿℱ)` with
>    `e = max(0, c - n)`, whenever `n + m ≥ c` — and, in the shape where the target is `Hᵖ(X, ℱ)`
>    itself rather than `Hᵖ(X, I⁰ℱ)`, the image of `Hᵖ(X, Iʳℱ) → Hᵖ(X, ℱ)` is contained in
>    `Iʳ⁻ᶜHᵖ(X, ℱ)` for `r ≥ c`, which is the source's `n = 0`;
> 3. `Ker(Hᵖ(X, Iᵏℱ) → Hᵖ(X, ℱ)) = Ker(Hᵖ(X, Iᵏℱ) → Hᵖ(X, Iᵐℱ))` whenever `m + c ≤ k`, which is
>    the source's part (3) in the case `m = k - c`;
> 4. there are `A`-linear maps `cmp : IⁿHᵖ(X, ℱ) → Hᵖ(X, Iⁿ⁻ᶜℱ)` for `n ≥ c` whose two
>    composites with the canonical maps are canonical: `cmp` followed by
>    `Hᵖ(X, Iⁿ⁻ᶜℱ) → Hᵖ(X, ℱ)` is the inclusion of `IⁿHᵖ(X, ℱ)` — which, read inside
>    `Iⁿ⁻²ᶜHᵖ(X, ℱ)`, where the image of `Hᵖ(X, Iⁿ⁻ᶜℱ) → Hᵖ(X, ℱ)` lies by part (2), is the
>    source's composite `IⁿHᵖ(X, ℱ) → Hᵖ(X, Iⁿ⁻ᶜℱ) → Iⁿ⁻²ᶜHᵖ(X, ℱ)` — and, for `n ≥ 2c`, the
>    image under `cmp` of the class of `x ∈ Hᵖ(X, Iⁿℱ)` in `Iⁿ⁻ᶜHᵖ(X, ℱ)` (the hypothesis
>    `(y : Hᵖ(X, ℱ)) = ...` below says that `y` is that class, which lies in `Iⁿ⁻ᶜHᵖ(X, ℱ)` by
>    part (2)) is the canonical image of `x` in `Hᵖ(X, Iⁿ⁻²ᶜℱ)`;
> 5. the two inverse systems `(Hᵖ(X, Iⁿℱ))` and `(IⁿHᵖ(X, ℱ))` are pro-isomorphic, in the
>    explicit up-to-refinement sense `InverseSequence.ProIso`.
>
> Parts (1), (2) and (3) are the Artin-Rees argument for Rees systems,
> `Stacks.RingTheory.ReesSystem.exists_uniform_bound_rees`, run on
> `Stacks.Cohomology.FormalFunctions.cohomologyIdealPowerSystem`: its finiteness input is
> [Stacks, Tag 02O8], `Stacks.Cohomology.FormalFunctions.isCohomologyReesFinite`, and its two
> compatibility laws are `cohomologyIdealPowerSystem_isTrMulCompatible`. Parts (4) and (5) are
> `Stacks.Cohomology.FormalFunctions.exists_comparison_cohomology`, whose hypotheses are those
> three parts.

```lean
theorem exists_uniform_bound_cohomology_of_isProper [IsNoetherianRing A]
    (hX : AlgebraicGeometry.IsProper X.hom) [F.IsCoherent] (p : ℕ) :
    ∃ c : ℕ,
      (∀ r : ℕ, c ≤ r → Function.Surjective
        ((cohomologyTr I X F p (show r ≤ r - c + c by omega)).comp
          (cohomologyMulTensor I X F p (r - c) c))) ∧
      (∀ n m : ℕ, c ≤ n + m →
        LinearMap.range (cohomologyTr I X F p (Nat.le_add_right n m)) ≤
          I ^ (m - (c - n)) • (⊤ : Submodule A (cohomologyIdealPower I X F p n))) ∧
      (∀ r : ℕ, c ≤ r → LinearMap.range (cohomologyProj I X F p r) ≤
        I ^ (r - c) • (⊤ : Submodule A (cohomology X F p))) ∧
      (∀ (m k : ℕ) (hmk : m + c ≤ k),
        LinearMap.ker (cohomologyProj I X F p k) =
          LinearMap.ker (cohomologyTr I X F p
            (show m ≤ k from le_trans (Nat.le_add_right m c) hmk))) ∧
      (∃ cmp : ∀ n : ℕ, c ≤ n →
          ↥(I ^ n • (⊤ : Submodule A (cohomology X F p))) →ₗ[A]
            cohomologyIdealPower I X F p (n - c),
        (∀ (n : ℕ) (hn : c ≤ n) (y : ↥(I ^ n • (⊤ : Submodule A (cohomology X F p)))),
            cohomologyProj I X F p (n - c) (cmp n hn y) = (y : cohomology X F p)) ∧
          ∀ (n : ℕ) (hn : c + c ≤ n) (x : cohomologyIdealPower I X F p n)
            (y : ↥(I ^ (n - c) • (⊤ : Submodule A (cohomology X F p)))),
            (y : cohomology X F p) = cohomologyProj I X F p n x →
            cmp (n - c) (Nat.le_sub_of_add_le hn) y =
              cohomologyTr I X F p ((Nat.sub_le (n - c) c).trans (Nat.sub_le n c)) x) ∧
      Nonempty (InverseSequence.ProIso (cohomologyIdealPowerFunctor I X F p)
        (Stacks.RingTheory.idealPowerSmulSystem I (cohomology X F p)))
```

## Tag 02OB, a lemma

[Tag 02OB](https://stacks.math.columbia.edu/tag/02OB) in the Stacks Project.

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L184). References: SGA 2 IX (1.1), “Clause (3), special case”; SGA 2 IX (2.1), “(iii)”.

> **[Stacks, Tag 02OB].** For `A` Noetherian, `J ⊆ A` an ideal, `f : X ⟶ Spec A` proper and
> `ℱ` coherent there is a single `c ≥ 0` such that, with `𝓙 = J · 𝒪_X`:
>
> 1. `Ker(Hᵖ(X, ℱ) → Hᵖ(X, ℱ / 𝓙ⁿℱ)) ⊆ Jⁿ⁻ᶜHᵖ(X, ℱ)` for every `n ≥ c`;
> 2. the inverse system `n ↦ Hᵖ(X, ℱ / 𝓙ⁿℱ)` satisfies the Mittag-Leffler condition;
> 3. for every `k ≥ n + c` the image of `Hᵖ(X, ℱ / 𝓙ᵏℱ)` in `Hᵖ(X, ℱ / 𝓙ⁿℱ)` equals the image of
>    `Hᵖ(X, ℱ)`.
>
> This is
> `Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient_of_02O8`
> with its hypothesis, [Stacks, Tag 02O8] in general form, discharged by
> `Stacks.FormalFunctions.isReesFinite_cohomologyIdealPowerSystem`. It is the only registration of
> [Stacks, Tag 02OB]: the two statements it is assembled from,
> `exists_uniform_bound_cohomology_idealPowerQuotient_of_02O8` and
> `exists_uniform_bound_cohomology_idealPowerQuotient`, take [Stacks, Tag 02O8] and two clauses of
> [Stacks, Tag 02OA] as inputs and carry no registration.

```lean
theorem exists_uniform_bound_cohomology_idealPowerQuotient_of_isProper [IsNoetherianRing A]
    (hf : AlgebraicGeometry.IsProper f) [G.IsCoherent] (p : ℕ) :
    ∃ c : ℕ,
      (∀ n : ℕ, c ≤ n →
          LinearMap.ker (cohomologyOverBaseMap A f p
              (cokernel.π (C := X.Modules)
                (idealPowerMultiple (baseIdealSheaf A J f) n G).ι)).hom ≤
            J ^ (n - c) • (⊤ : Submodule A (cohomologyOverBase A f p G))) ∧
        IsMittagLefflerCategorical
          (adicQuotientSystem (baseIdealSheaf A J f) G ⋙
            (Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p) ∧
        ∀ n k : ℕ, (hk : n + c ≤ k) →
          LinearMap.range
              (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).map
                (idealPowerQuotientDrop (baseIdealSheaf A J f)
                  ((Nat.le_add_right n c).trans hk) G)).hom =
            LinearMap.range
              (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).map
                (cokernel.π (C := X.Modules)
                  (idealPowerMultiple (baseIdealSheaf A J f) n G).ι)).hom
```

## Tag 02OC, a theorem

[Tag 02OC](https://stacks.math.columbia.edu/tag/02OC) in the Stacks Project.

**`Stacks.Cohomology.FormalFunctions.exists_formalFunctionsEquiv_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L243). References: EGA III (4.1.7).

> **[Stacks, Tag 02OC].** For `A` Noetherian, `I ⊆ A` an ideal, `f : X ⟶ Spec A` proper and
> `ℱ` coherent, the maps `Hᵖ(X, ℱ)/IⁿHᵖ(X, ℱ) → Hᵖ(X, ℱ/𝓘ⁿℱ)` assemble into an isomorphism
>
>   `Hᵖ(X, ℱ)^∧_I ≅ limₙ Hᵖ(X, ℱ/𝓘ⁿℱ)`
>
> of `A`-modules, and that isomorphism is a homeomorphism for the limit topologies.
>
> The second component says that the `n`-th projection of the isomorphism carries the image of a
> class `x ∈ Hᵖ(X, ℱ)` to the image of `x` in `Hᵖ(X, ℱ/𝓘ⁿℱ)`, so the isomorphism is the one the
> source's system of maps defines and not merely some isomorphism between the two modules. The
> third is the source's further assertion: the limit topology on `Hᵖ(X, ℱ)^∧_I = limₙ Hᵖ(X, ℱ)/Iⁿ`
> and the limit topology on `limₙ Hᵖ(X, ℱ/𝓘ⁿℱ)` correspond under it. By
> `Stacks.IntertwinedFiltration.adicCompletionModuleLimitTopology_eq_adicModuleTopology` the
> topology on the left is equally the `I`-adic topology of the completion, which is the source's
> own footnote to the statement.
>
> The module isomorphism is `Stacks.Cohomology.FormalFunctions.formalFunctionsEquiv` together
> with `formalFunctionsEquiv_proj_of`, and the homeomorphism is
> `Stacks.IntertwinedFiltration.isHomeomorph_adicCompletionEquivTowerLimit_limitTopology` for the
> same map; the hypotheses of all three are clauses (1) and (3) of [Stacks, Tag 02OB], which come
> from `exists_uniform_bound_cohomology_idealPowerQuotient_of_isProper`, together with the
> finite generation of `I` that `IsNoetherianRing A` supplies. Those three declarations carry no
> registration under [Stacks, Tag 02OC]: each takes clauses (1) and (3) of [Stacks, Tag 02OB] as
> inputs and states one component of the theorem, and this theorem, which states all three
> components with the source's hypotheses, is the registered form of [Stacks, Tag 02OC].

```lean
theorem exists_formalFunctionsEquiv_of_isProper [IsNoetherianRing A]
    (hf : AlgebraicGeometry.IsProper f) [F.IsCoherent] (p : ℕ) :
    ∃ e : AdicCompletion I (cohomologyOverBase A f p F) ≃ₗ[A]
        towerLimit (adicCohomologyTower A f I F p) (adicCohomologyTowerMap A f I F p),
      (∀ (n : ℕ) (x : cohomologyOverBase A f p F),
          towerLimit.proj n (e (AdicCompletion.of I (cohomologyOverBase A f p F) x)) =
            adicCohomologyProj A f I F p n x) ∧
        @IsHomeomorph _ _
          (adicCompletionModuleLimitTopology (M := cohomologyOverBase A f p F) I)
          (towerLimit.limitTopology (adicCohomologyTower A f I F p)
            (adicCohomologyTowerMap A f I F p)) e
```

## Tag 087U, a lemma

[Tag 087U](https://stacks.math.columbia.edu/tag/087U) in the Stacks Project.

**`Stacks.Algebraization.isIso_cohomologyToLimit_of_isProper_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/FullyFaithfulComplete.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/FullyFaithfulComplete.lean#L207). The attribute's comment: “for all p ≥ 0: A Noetherian and J-adically complete, f : X ⟶ Spec A proper, F coherent; 02O6 and 02OB are proved theorems used in the proof”. References: SGA 2 IX (1.3), “The edge φ'\_i”.

> **The theorem on formal functions over a complete base, [Stacks, Tag 087U].** For `A`
> Noetherian and complete with respect to `J`, `f : X ⟶ Spec A` proper and `F` coherent, the
> comparison `Hᵖ(X, F) ⟶ limₙ Hᵖ(X, F / 𝓙ⁿ F)` is an isomorphism in every degree `p`.
>
> This is `Stacks.Algebraization.isIso_cohomologyToLimit` with its three hypotheses discharged:
> the finiteness of the cohomology by [Stacks, Tag 02O6], and the two uniform Artin-Rees bounds
> by [Stacks, Tag 02OB] over the unconditional [Stacks, Tag 02O8].
>
> This is the declaration [Stacks, Tag 087U] is registered on; the conditional statements of
> `StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/FormalFunctions.lean`, where the
> comparison map and the reduction are built, are untagged.

```lean
public theorem isIso_cohomologyToLimit_of_isProper_of_isAdicComplete
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (p : ℕ) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    IsIso (cohomologyToLimit (baseIdealSheaf A J f) F p)
```

## Tag 02OD, a lemma

[Tag 02OD](https://stacks.math.columbia.edu/tag/02OD) in the Stacks Project.

**`Stacks.FormalFunctions.nonempty_adicCompletionHigherDirectImageStalkEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/CompletionStalkLimit.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/CompletionStalkLimit.lean#L119). References: EGA III (4.2.4), “Degree p = 0 case”.

> **Stacks Project, Tag 02OD.** Let `f : X ⟶ Y` be a proper morphism of schemes with `Y`
> locally Noetherian, let `ℱ` be a coherent `𝒪_X`-module and let `y` be a point of `Y`. Let
> `X_n = Spec (𝒪_{Y, y}/𝔪_y ⁿ) ×_Y X` be the infinitesimal neighbourhoods of the fibre `X_y` and
> `ℱ_n = i_n ^* ℱ`. Then in every degree `p`
>
> `(R ᵖ f_* ℱ) _y ^∧ ≅ lim_n H ᵖ (X_n, ℱ_n)`
>
> as `𝒪 ^∧_{Y, y}`-modules.

```lean
public theorem nonempty_adicCompletionHigherDirectImageStalkEquiv (f : X ⟶ Y)
    [IsLocallyNoetherian Y] [IsProper f] (F : X.Modules) [F.IsCoherent] (y : Y) (p : ℕ) :
    Nonempty
      (AdicCompletion (stalkMaximalIdeal y) (higherDirectImageStalk f F y p) ≃ₗ[
          AdicCompletion (stalkMaximalIdeal y) (Y.presheaf.stalk y)]
        towerLimit (infinitesimalCohomology f F y p) (infinitesimalCohomologyMap f F y p))
```

**`Stacks.Cohomology.FormalFunctions.pushforwardPullbackBaseIdealIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsTheorem/IdealPowerQuotientSubscheme.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsTheorem/IdealPowerQuotientSubscheme.lean#L175). The attribute's comment: “the second step of the tag's proof: the identification i\_\{n*} ℱ\_n ≅ ℱ / 𝔪ⁿ ℱ, over an affine base and for the quotient by the n-th power of the ideal sheaf generated by an ideal of that base. The tag's conclusion is NOT asserted: that needs Tag 02OC, which rests on Tag 02O8, together with Tag 02KH”.

> **`i_{n*} ℱ_n ≅ ℱ / I ⁿ ℱ`.** The direct image of the restriction of `ℱ` to the infinitesimal
> neighbourhood `X_n = X ×_{Spec A} Spec (A / I ⁿ)` is the quotient of `ℱ` by the `n`-th power of
> the ideal sheaf `I · 𝒪_X`.
>
> This is the **second step of the proof of [Stacks, Tag 02OD]**, not its conclusion: the source
> derives `H ᵖ (X_n, ℱ_n) = H ᵖ (X, ℱ / 𝔪 ⁿ ℱ)` from it by the Leray spectral sequence for `i_n`
> together with [Stacks, Tag 01Y6]. At `p = 0` no spectral sequence is needed, because a direct
> image does not change global sections, so the global sections of this isomorphism are that
> identification. The tag's conclusion — that the completed stalk of `R ᵖ f_* ℱ` at `y` is the limit
> of the `H ᵖ (X_n, ℱ_n)` — is **not** asserted here: it needs in addition [Stacks, Tag 02OC], which
> rests on [Stacks, Tag 02O8], and flat base change [Stacks, Tag 02KH] to reduce `Y` to
> `Spec 𝒪_{Y,y}`, which is the reduction that makes `i_n` a closed immersion in the first place.
>
> The underlying mathematics is [Stacks, Tag 0EL1], already proved in the library as
> `Stacks.Algebraization.idealQuotientPushforwardIso`; what is asserted here is that the fibre
> product of the source's diagram is a presentation it applies to.

```lean
public def pushforwardPullbackBaseIdealIso :
    (Scheme.Modules.pushforward (baseNeighbourhoodι A I f n)).obj
        ((Scheme.Modules.pullback (baseNeighbourhoodι A I f n)).obj F) ≅
      idealPowerQuotient (baseIdealSheaf A I f) n F
```

**`Stacks.FormalFunctions.infinitesimalNeighbourhood`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/InfinitesimalNeighbourhood.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/InfinitesimalNeighbourhood.lean#L260). The attribute's comment: “the infinitesimal neighbourhoods X\_n = X ×\_Y Spec(𝒪\_\{Y,y}/𝔪ⁿ) of the fibre, the setup paragraph of the tag. The conclusion -- that the completed stalk of R^p f\_* ℱ at y is the limit of the H^p(X\_n, ℱ\_n) -- is NOT asserted here: see the implementation notes for its three inputs and which of them are now available”.

> The `n`-th infinitesimal neighbourhood `X_n = Spec (𝒪_{Y,y}/𝔪_y ^ n) ×_Y X` of the fibre of
> `f : X ⟶ Y` over `y`.

```lean
public abbrev infinitesimalNeighbourhood (f : X ⟶ Y) (y : Y) (n : ℕ) : Scheme.{u}
```

## Tag 02OE, a lemma

[Tag 02OE](https://stacks.math.columbia.edu/tag/02OE) in the Stacks Project.

**`Stacks.FormalFunctions.isZero_stalk_higherDirectImage_of_finite_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteFibreVanishing.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteFibreVanishing.lean#L142).

> **Stacks Project, Tag 02OE.** Let `f : X ⟶ Y` be a morphism of schemes and let `y : Y`.
> Assume `Y` is locally Noetherian, `f` is proper, and the fibre `f ⁻¹' {y}` is finite. Then for
> every coherent `𝒪_X`-module `F` and every `p > 0` the stalk `(R ᵖ f_* F)_y` vanishes.
>
> This is `isZero_stalk_higherDirectImage_of_finite_preimage`, which needs neither hypothesis;
> coherence of `F` gives quasi-coherence through [Stacks, Tag 01BW]
> (`Stacks.AlgebraicGeometry.CoherentTFAE.isQuasicoherent_isFiniteType_of_isCoherent`), for which
> no hypothesis on `Y` is needed either. Both hypotheses are kept here because the tag states
> them.

```lean
theorem isZero_stalk_higherDirectImage_of_finite_fibre {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsLocallyNoetherian Y] [IsProper f] (y : Y) (hfin : (f ⁻¹' {y}).Finite) (F : X.Modules)
    [F.IsCoherent] (p : ℤ) (hp : 0 < p) :
    IsZero
      ((((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F).presheaf.stalk y)
```

## Tag 02V7, a lemma

[Tag 02V7](https://stacks.math.columbia.edu/tag/02V7) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FibreDimension.isZero_stalk_rightDerivedPlus_of_fiber_dimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageFibreDimension/GeneralDimension.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/HigherDirectImageFibreDimension/GeneralDimension.lean#L133). References: EGA III (4.2.2), “partial”; SGA 6 X (4.4), “Stalk form of (4.4.5)”.

> **[Stacks, Tag 02V7].** Let `f : X ⟶ Y` be a morphism of schemes and let `y ∈ Y`. Assume
> `Y` locally Noetherian, `f` proper and `dim(X_y) = d`. Then for every coherent sheaf `ℱ` on `X`
> we have `(Rᵖ f_* ℱ)_y = 0` for all `p > d`.
>
> The fibre dimension is taken as the upper bound `dim(X_y) ≤ d`, which is what the proof uses.
> A neighbourhood `V` of `y` over which every fibre is bounded by `d` is produced by
> `AlgebraicGeometry.exists_isAffineOpen_forall_topologicalKrullDim_fiber_le`; the stalk at `y` of
> the higher direct image along `f` is the one along `f ∣_ V`; over the affine base `V` the higher
> direct image vanishes as soon as the cohomology of `f ⁻¹ V` does; and that vanishing is
> `isZero_rightDerived_moduleGlobalSections_of_affine_base`.

```lean
theorem isZero_stalk_rightDerivedPlus_of_fiber_dimension_le
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsProper f] [IsLocallyNoetherian Y] (y : Y) (d : ℕ)
    (hdim : topologicalKrullDim (f.fiber y) ≤ (d : WithBot ℕ∞))
    (F : X.Modules) [F.IsCoherent] (p : ℤ) (hp : (d : ℤ) < p) :
    IsZero ((((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F).presheaf.stalk y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.20, Tag 02O7](https://stacks.math.columbia.edu/tag/02O7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
