---
declaration: section
origin: cited
lean: Stacks.Blowup.pushforwardReesGradedModule, Stacks.Blowup.pushforwardReesGradedModulePlus, Stacks.Cohomology.FormalFunctions.isCohomologyReesFinite, Stacks.Algebraization.isQuasicoherent_and_isFiniteType_pushforwardReesGradedModulePlus, Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology, Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_of_isProper, Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient_of_02O8, Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient
statement: formalized
proof: formalized
---

# 30.20 The theorem on formal functions

Section 30.20 of the Stacks Project, [Tag 02O7](https://stacks.math.columbia.edu/tag/02O7). 10 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02O7, the section

[Tag 02O7](https://stacks.math.columbia.edu/tag/02O7) in the Stacks Project.

**`Stacks.Blowup.pushforwardReesGradedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModule.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModule.lean#L116). The attribute's comment: “⨁ₙ f\_*(ℐⁿℱ) is a graded ⨁ₙ ℐⁿ-module on the base”.

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

**`Stacks.Blowup.pushforwardReesGradedModulePlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModulePlus.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/PushforwardIdealPowerGradedModulePlus.lean#L450). The attribute's comment: “⨁ₙ R ᵖ f\_*(ℐⁿℱ) is a graded ⨁ₙ ℐⁿ-module on the base, in every degree p”. References: EGA III (3.3.1), “special case”.

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

**`Stacks.Cohomology.FormalFunctions.isCohomologyReesFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/ReesCohomologyFiniteReduction.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/ReesCohomologyFiniteReduction.lean#L46). References: EGA III (3.3.2); EGA III (4.1.7.12), “more general”.

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

**`Stacks.Algebraization.isQuasicoherent_and_isFiniteType_pushforwardReesGradedModulePlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/HigherDirectImageFiniteTypeSpan.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/Completion/Quasicoherent/HigherDirectImageFiniteTypeSpan.lean#L426). References: EGA III (2.4.2), “special case”; SGA 2 XII (5.8), “(ii), special case”.

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

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/CohomologyIdealPowerSystem.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/CohomologyIdealPowerSystem.lean#L447). The attribute's comment: “parts (2) at n = 0 and (3); parts (1), (4), (5) and part (2) for n > 0 are not proved here”.

> **[Stacks, Tag 02OA], part (2) in the case `n = 0` and part (3).**
>
> For `A` Noetherian, `f : X → Spec A` proper and `ℱ` coherent there is one integer `c ≥ 0` such
> that
>
> * the image of `Hᵖ(X, Iʳℱ) → Hᵖ(X, ℱ)` is contained in `Iʳ⁻ᶜHᵖ(X, ℱ)` for `r ≥ c` -- this is
>   part (2) of the source at `n = 0`, where its `e = max(0, c - n)` is `c`; and
> * `Ker(Hᵖ(X, Iᵏℱ) → Hᵖ(X, ℱ)) = Ker(Hᵖ(X, Iᵏℱ) → Hᵖ(X, Iᵐℱ))` whenever `m + c ≤ k` -- this is
>   part (3) of the source, which is the case `m = k - c`.
>
> Parts (1), (4) and (5) of the source, and part (2) for general `n`, are **not** proved here;
> neither is the case `n > 0` of part (2), which needs a compatibility between the transition maps
> and the multiplication maps that `Stacks.RingTheory.IdealPowerSystem` deliberately does not
> assume.
>
> The hypothesis `h02O8` is [Stacks, Tag 02O8] -- a *different* Stacks tag, absent from this
> branch -- carried in general form: it is quantified over every Noetherian base ring, every
> ideal of it, every proper scheme over it, every coherent module and every degree, and is
> instantiated inside the proof at the data of this statement. See `IsCohomologyReesFinite` for
> why it is absent and what is new about its being statable.

```lean
theorem exists_uniform_bound_cohomology [IsNoetherianRing A]
    (hX : AlgebraicGeometry.IsProper X.hom) (hF : SheafOfModules.IsCoherent F) (p : ℕ)
    (h02O8 : ∀ (A' : Type u) [CommRing A'] [IsNoetherianRing A'] (I' : Ideal A')
      (X' : Over (Spec (.of A'))) (_ : AlgebraicGeometry.IsProper X'.hom)
      (F' : X'.left.Modules) (_ : SheafOfModules.IsCoherent F') (p' : ℕ),
      (cohomologyIdealPowerSystem I' X' F' p').IsReesFinite) :
    ∃ c : ℕ,
      (∀ r : ℕ, c ≤ r → LinearMap.range (cohomologyProj I X F p r) ≤
        I ^ (r - c) • (⊤ : Submodule A (cohomology X F p))) ∧
      (∀ (m k : ℕ) (hmk : m + c ≤ k),
        LinearMap.ker (cohomologyProj I X F p k) =
          LinearMap.ker (cohomologyTr I X F p
            (show m ≤ k from le_trans (Nat.le_add_right m c) hmk)))
```

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L104).

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

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient_of_02O8`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsFrom02O8.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsFrom02O8.lean#L192). The attribute's comment: “granted Tag 02O8, carried as the hypothesis h02O8”.

> **Stacks Project, Tag 02OB**, granted [Stacks, Tag 02O8].
>
> This is `Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient`
> with its two hypotheses discharged by
> `Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology`, applied in each degree `q`
> and transported along the identifications described in the implementation notes of this file.
> Nothing of the mathematics is new: the content is that the affine side of the theorem on formal
> functions rests on [Stacks, Tag 02O8] alone, which is carried here as the hypothesis `h02O8` in
> the same general form `exists_uniform_bound_cohomology` consumes it.

```lean
public theorem exists_uniform_bound_cohomology_idealPowerQuotient_of_02O8
    (A : Type u) [CommRing A] [IsNoetherianRing A] {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    (hX : AlgebraicGeometry.IsProper f) (I : Ideal A) (F : X.Modules)
    (hF : SheafOfModules.IsCoherent F) (p : ℕ)
    (h02O8 : ∀ (A' : Type u) [CommRing A'] [IsNoetherianRing A'] (I' : Ideal A')
      (X' : Over (Spec (.of A'))) (_ : AlgebraicGeometry.IsProper X'.hom)
      (F' : X'.left.Modules) (_ : SheafOfModules.IsCoherent F') (p' : ℕ),
      (cohomologyIdealPowerSystem I' X' F' p').IsReesFinite) :
    ∃ c : ℕ,
      (∀ n : ℕ, c ≤ n →
          LinearMap.ker (cohomologyOverBaseMap A f p
              (cokernel.π (C := X.Modules)
                (idealPowerMultiple (baseIdealSheaf A I f) n F).ι)).hom ≤
            I ^ (n - c) • (⊤ : Submodule A (cohomologyOverBase A f p F))) ∧
        IsMittagLefflerCategorical
          (adicQuotientSystem (baseIdealSheaf A I f) F ⋙
            (moduleGlobalSections X).rightDerived p) ∧
        ∀ n k : ℕ, (hk : n + c ≤ k) →
          LinearMap.range (((moduleGlobalSections X).rightDerived p).map
              (idealPowerQuotientDrop (baseIdealSheaf A I f)
                ((Nat.le_add_right n c).trans hk) F)).hom =
            LinearMap.range (((moduleGlobalSections X).rightDerived p).map
              (cokernel.π (C := X.Modules)
                (idealPowerMultiple (baseIdealSheaf A I f) n F).ι)).hom
```

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/IdealPowerQuotientCohomologyBound.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/IdealPowerQuotientCohomologyBound.lean#L152). The attribute's comment: “granted Tag 02OA, carried as the hypotheses h02OA\_image and h02OA\_kernel”.

> **Stacks Project, Tag 02OB**, granted [Stacks, Tag 02OA].
>
> There is a single `c ≥ 0` such that, with `𝓘 = I · 𝒪_X`:
>
> 1. `Ker(H^p(X, ℱ) → H^p(X, ℱ / 𝓘 ^ n ℱ)) ⊆ I ^ (n - c) · H^p(X, ℱ)` for every `n ≥ c`;
> 2. the inverse system `n ↦ H^p(X, ℱ / 𝓘 ^ n ℱ)` satisfies the Mittag-Leffler condition;
> 3. for every `k ≥ n + c`, the image of `H^p(X, ℱ / 𝓘 ^ k ℱ)` in `H^p(X, ℱ / 𝓘 ^ n ℱ)` equals
>    the image of `H^p(X, ℱ)`.
>
> The two hypotheses are the clauses of [Stacks, Tag 02OA] that the source's proof uses, each
> quantified over the degree because the proof applies them in degrees `p` and `p + 1` and takes
> the larger of the two constants: `h02OA_image` is clause (2) of that lemma in the case `n = 0`,
> and `h02OA_kernel` is its clause (3). The source's standing hypotheses — `A` Noetherian, `f`
> proper and `ℱ` coherent — are what make [Stacks, Tag 02OA] true and are used nowhere else, so
> they do not appear.
>
> Clause (1) is the kernel-image identity of the long exact sequence of
> `0 → 𝓘 ^ n ℱ → ℱ → ℱ / 𝓘 ^ n ℱ → 0` followed by `h02OA_image`. Clause (3) is the diagram chase
> along the ladder of those sequences: naturality of the connecting map carries a class of
> `H^p(X, ℱ / 𝓘 ^ k ℱ)` to one annihilated by the connecting map of the exponent-`n` sequence,
> because `h02OA_kernel` in degree `p + 1` identifies the kernel of `H^(p+1)(𝓘 ^ k ℱ) → H^(p+1)(ℱ)`
> with a kernel that `H^(p+1)(𝓘 ^ k ℱ) → H^(p+1)(𝓘 ^ n ℱ)` factors through. Clause (2) follows
> from clause (3).

```lean
public theorem exists_uniform_bound_cohomology_idealPowerQuotient
    (h02OA_image : ∀ q : ℕ, ∃ c : ℕ, ∀ k : ℕ, c ≤ k →
      LinearMap.range (cohomologyOverBaseMap A f q
          (idealPowerMultiple (baseIdealSheaf A I f) k F).ι).hom ≤
        I ^ (k - c) • (⊤ : Submodule A (cohomologyOverBase A f q F)))
    (h02OA_kernel : ∀ q : ℕ, ∃ c : ℕ, ∀ k : ℕ, c ≤ k →
      LinearMap.ker (((moduleGlobalSections X).rightDerived q).map
          (idealPowerMultiple (baseIdealSheaf A I f) k F).ι).hom =
        LinearMap.ker (((moduleGlobalSections X).rightDerived q).map
          (submoduleInclusion (idealPowerMultiple_antitone (baseIdealSheaf A I f) F
            (Nat.sub_le k c)))).hom) :
    ∃ c : ℕ,
      (∀ n : ℕ, c ≤ n →
          LinearMap.ker (cohomologyOverBaseMap A f p
              (cokernel.π (C := X.Modules)
                (idealPowerMultiple (baseIdealSheaf A I f) n F).ι)).hom ≤
            I ^ (n - c) • (⊤ : Submodule A (cohomologyOverBase A f p F))) ∧
        IsMittagLefflerCategorical
          (adicQuotientSystem (baseIdealSheaf A I f) F ⋙
            (moduleGlobalSections X).rightDerived p) ∧
        ∀ n k : ℕ, (hk : n + c ≤ k) →
          LinearMap.range (((moduleGlobalSections X).rightDerived p).map
              (idealPowerQuotientDrop (baseIdealSheaf A I f)
                ((Nat.le_add_right n c).trans hk) F)).hom =
            LinearMap.range (((moduleGlobalSections X).rightDerived p).map
              (cokernel.π (C := X.Modules)
                (idealPowerMultiple (baseIdealSheaf A I f) n F).ι)).hom
```

**`Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L180). References: SGA 2 IX (1.1), “Clause (3), special case”; SGA 2 IX (2.1), “(iii)”.

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
> `Stacks.FormalFunctions.isReesFinite_cohomologyIdealPowerSystem`.

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

**`Stacks.Cohomology.FormalFunctions.formalFunctionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/AdicCompletionLimitComparison.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/AdicCompletionLimitComparison.lean#L264). The attribute's comment: “the isomorphism of A-modules only, not the homeomorphism for the limit topologies; granted Tag 02OB, whose clauses (1) and (3) are carried as the hypotheses h02OB\_ker and h02OB\_range”.

> **Stacks Project, Tag 02OC**, granted [Stacks, Tag 02OB], and for the `A`-module
> isomorphism only.
>
> With `𝓘 = I · 𝒪_X`, the `I`-adic completion of `H^p(X, ℱ)` is the limit of the tower
> `n ↦ H^p(X, ℱ / 𝓘 ^ n ℱ)`. The map is the one assembled from the projections
> `H^p(X, ℱ) ⟶ H^p(X, ℱ / 𝓘 ^ n ℱ)`, which is the content of
> `formalFunctionsEquiv_proj_of`. [Stacks, Tag 02OC] further asserts that the comparison is a
> homeomorphism for the limit topologies; that is **not** proved here, and no statement in this
> file claims it.
>
> The two hypotheses are clauses (1) and (3) of [Stacks, Tag 02OB], for a fixed `c`, in the shape
> `Stacks.Cohomology.FormalFunctions.exists_uniform_bound_cohomology_idealPowerQuotient` produces
> them: `h02OB_ker` bounds the kernel of the `n`-th projection by `I ^ (n - c) H^p(X, ℱ)`, and
> `h02OB_range` says that for `k ≥ n + c` the image of `H^p(X, ℱ / 𝓘 ^ k ℱ)` in
> `H^p(X, ℱ / 𝓘 ^ n ℱ)` is the image of `H^p(X, ℱ)`. Clause (2) of that lemma, the
> Mittag-Leffler condition, is not needed: in this formulation it is subsumed by clause (3). The
> source's standing hypotheses — `A` Noetherian, `f` proper and `ℱ` coherent — are what make
> [Stacks, Tag 02OB] true and are used nowhere else, so only quasi-coherence of `ℱ`, which the
> annihilation argument needs, appears.
>
> Everything else is `Stacks.IntertwinedFiltration.adicCompletionEquivTowerLimit`, the source's
> own argument carried out abstractly.

```lean
public def formalFunctionsEquiv [F.IsQuasicoherent]
    (h02OB_ker : ∀ n : ℕ, c ≤ n →
      LinearMap.ker (adicCohomologyProj A f I F p n) ≤
        I ^ (n - c) • (⊤ : Submodule A (cohomologyOverBase A f p F)))
    (h02OB_range : ∀ n k : ℕ, (hk : n + c ≤ k) →
      LinearMap.range (((moduleGlobalSections X).rightDerived p).map
          (idealPowerQuotientDrop (baseIdealSheaf A I f)
            ((Nat.le_add_right n c).trans hk) F)).hom =
        LinearMap.range (((moduleGlobalSections X).rightDerived p).map
          (cokernel.π (C := X.Modules)
            (idealPowerMultiple (baseIdealSheaf A I f) n F).ι)).hom) :
    AdicCompletion I (cohomologyOverBase A f p F) ≃ₗ[A]
      towerLimit (adicCohomologyTower A f I F p) (adicCohomologyTowerMap A f I F p)
```

**`Stacks.Cohomology.FormalFunctions.formalFunctionsEquiv_proj_of`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/AdicCompletionLimitComparison.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/AdicCompletionLimitComparison.lean#L292). The attribute's comment: “the identification of the isomorphism of formalFunctionsEquiv as the one assembled from the projections; same hypotheses, and again nothing about the limit topologies”.

> **The comparison isomorphism of [Stacks, Tag 02OC] is the canonical one**: its `n`-th
> component carries the image in `H^p(X, ℱ) ^∧_I` of a class `x ∈ H^p(X, ℱ)` to the image of `x`
> in `H^p(X, ℱ / 𝓘 ^ n ℱ)`. Together with `formalFunctionsEquiv` this says that the maps
> `H^p(X, ℱ) / I ^ n H^p(X, ℱ) ⟶ H^p(X, ℱ / 𝓘 ^ n ℱ)` assemble into an isomorphism, rather than
> merely that the two modules are isomorphic.

```lean
public lemma formalFunctionsEquiv_proj_of [F.IsQuasicoherent]
    (h02OB_ker : ∀ n : ℕ, c ≤ n →
      LinearMap.ker (adicCohomologyProj A f I F p n) ≤
        I ^ (n - c) • (⊤ : Submodule A (cohomologyOverBase A f p F)))
    (h02OB_range : ∀ n k : ℕ, (hk : n + c ≤ k) →
      LinearMap.range (((moduleGlobalSections X).rightDerived p).map
          (idealPowerQuotientDrop (baseIdealSheaf A I f)
            ((Nat.le_add_right n c).trans hk) F)).hom =
        LinearMap.range (((moduleGlobalSections X).rightDerived p).map
          (cokernel.π (C := X.Modules)
            (idealPowerMultiple (baseIdealSheaf A I f) n F).ι)).hom)
    (n : ℕ) (x : cohomologyOverBase A f p F) :
    towerLimit.proj n (formalFunctionsEquiv A f I F p c h02OB_ker h02OB_range
        (AdicCompletion.of I (cohomologyOverBase A f p F) x)) =
      adicCohomologyProj A f I F p n x
```

**`Stacks.Cohomology.FormalFunctions.exists_formalFunctionsEquiv_of_02O8`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsFrom02O8.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsFrom02O8.lean#L238). The attribute's comment: “granted Tag 02O8, carried as the hypothesis h02O8”.

> **Stacks Project, Tag 02OC**, granted [Stacks, Tag 02O8], and for the `A`-module
> isomorphism only.
>
> With `𝓘 = I · 𝒪_X`, the `I`-adic completion of `Hᵖ(X, ℱ)` is the limit of the tower
> `n ↦ Hᵖ(X, ℱ / 𝓘ⁿℱ)`, by *the* comparison map: the projection normalisation says that the
> `n`-th component of the equivalence carries the image of a class `x ∈ Hᵖ(X, ℱ)` to the image of
> `x` in `Hᵖ(X, ℱ / 𝓘ⁿℱ)`. The constant `c` is existentially bound because
> `Stacks.Cohomology.FormalFunctions.formalFunctionsEquiv` is indexed by it.
>
> [Stacks, Tag 02OC] further asserts that the comparison is a homeomorphism for the limit
> topologies; that is **not** proved here, exactly as in
> `Stacks.Cohomology.FormalFunctions.formalFunctionsEquiv`, and this statement does not claim it.
>
> Quasi-coherence of `ℱ` is not assumed: it follows from `hF`.

```lean
public theorem exists_formalFunctionsEquiv_of_02O8
    (A : Type u) [CommRing A] [IsNoetherianRing A] {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    (hX : AlgebraicGeometry.IsProper f) (I : Ideal A) (F : X.Modules)
    (hF : SheafOfModules.IsCoherent F) (p : ℕ)
    (h02O8 : ∀ (A' : Type u) [CommRing A'] [IsNoetherianRing A'] (I' : Ideal A')
      (X' : Over (Spec (.of A'))) (_ : AlgebraicGeometry.IsProper X'.hom)
      (F' : X'.left.Modules) (_ : SheafOfModules.IsCoherent F') (p' : ℕ),
      (cohomologyIdealPowerSystem I' X' F' p').IsReesFinite) :
    ∃ (c : ℕ) (e : AdicCompletion I (cohomologyOverBase A f p F) ≃ₗ[A]
        towerLimit (adicCohomologyTower A f I F p) (adicCohomologyTowerMap A f I F p)),
      ∀ (n : ℕ) (x : cohomologyOverBase A f p F),
        towerLimit.proj n (e (AdicCompletion.of I (cohomologyOverBase A f p F) x)) =
          adicCohomologyProj A f I F p n x
```

**`Stacks.Cohomology.FormalFunctions.exists_formalFunctionsEquiv_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L236). References: EGA III (4.1.7).

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
> finite generation of `I` that `IsNoetherianRing A` supplies.

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

**`Stacks.Algebraization.isIso_cohomologyToLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/FormalFunctions.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/FormalFunctions.lean#L360). The attribute's comment: “for all p ≥ 0 and any f : X ⟶ Spec A with X locally Noetherian, hence in particular for a proper f; the finiteness of the cohomology (02O6) and the two uniform Artin-Rees bounds (02OB) enter as the hypotheses hfin, hker and hstab, none of which this library carries for a proper morphism”.

> **Stacks 087U**, granted the two uniform bounds of [Stacks, Tag 02OB] and the finiteness of
> [Stacks, Tag 02O6].
>
> Let `A` be a Noetherian ring complete with respect to an ideal `J`, let `X` be a locally
> Noetherian scheme over `A` and let `F` be a coherent sheaf on `X`. Then for every `p ≥ 0` the
> canonical map
>
>   `Hᵖ(X, F) ⟶ limₙ Hᵖ(X, F / Jⁿ F)`
>
> is an isomorphism, provided
>
> * `hfin`: `Hᵖ(X, F)` is a finite `A`-module — this is [Stacks, Tag 02O6], the finiteness of
>   the cohomology of a coherent sheaf along a proper morphism, which is **not** available in this
>   library for a proper morphism;
> * `hker`: there is a `c` with `ker (Hᵖ(X, F) ⟶ Hᵖ(X, F / Jⁿ⁺ᶜ F)) ⊆ Jⁿ Hᵖ(X, F)` for all `n`;
> * `hstab`: there is a `c` such that the image of `Hᵖ(X, F) ⟶ Hᵖ(X, F / Jⁿ F)` contains the image
>   of `Hᵖ(X, F / Jⁿ⁺ᶜ F) ⟶ Hᵖ(X, F / Jⁿ F)` for all `n`.
>
> The last two are the uniform Artin-Rees bounds of [Stacks, Tag 02OB], read through the long
> exact cohomology sequences of `0 → Jⁿ F → F → F / Jⁿ F → 0`; they are the two places where
> properness of the structure morphism enters the source's argument, and neither is available in
> this library — see the implementation notes of
> `StacksFrontier/RingTheory/LocalCohomology/UniformCohomologyBound.lean`.
>
> What is proved here is everything else: the completion step of the source's proof — that no
> completion is needed on the left because a finite module over a complete Noetherian ring is
> itself complete — together with the derivation of the comparison from the two bounds.

```lean
public theorem isIso_cohomologyToLimit (A : Type u) [CommRing A] [IsNoetherianRing A]
    (J : Ideal A) [IsAdicComplete J A] {X : Scheme.{u}} [IsLocallyNoetherian X]
    (f : X ⟶ Spec (.of A))
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (p : ℕ)
    (hfin : letI := baseAlgebra A f
      Module.Finite A
        ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).obj F.obj))
    (hker : letI := baseAlgebra A f
      ∃ c : ℕ, ∀ (n : ℕ) (x : ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections
          X).rightDerived p).obj F.obj)),
        (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).map
            (completionProjection X
              (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F (n + c))).hom x = 0 →
          x ∈ J ^ n • (⊤ : Submodule A ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections
            X).rightDerived p).obj F.obj)))
    (hstab : ∃ c : ℕ, ∀ (n : ℕ)
        (y : ↥((completionCohomologySystem
          (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F p).obj (op (n + c)))),
        ∃ x : ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).obj F.obj),
          (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).map
              (completionProjection X
                (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F n)).hom x =
            ((completionCohomologySystem
                (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F p).map
              (homOfLE (Nat.le_add_right n c)).op).hom y) :
    IsIso (cohomologyToLimit
      (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F p)
```

**`Stacks.Algebraization.isIso_cohomologyToLimit_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/FormalFunctions.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/FormalFunctions.lean#L464). The attribute's comment: “for a proper f and all p ≥ 0; the finiteness of the cohomology (02O6) and the two uniform Artin-Rees bounds (02OB) enter as the hypotheses hfin, hker and hstab, none of which this library carries for a proper morphism”.

> **Stacks 087U for a proper morphism**, granted the two uniform bounds of
> [Stacks, Tag 02OB] and the finiteness of [Stacks, Tag 02O6].
>
> This is `Stacks.Algebraization.isIso_cohomologyToLimit` with the hypothesis
> `IsLocallyNoetherian X` replaced by properness of `f`, which implies it over a Noetherian base.
> The statement is then the source's verbatim: `A` Noetherian and `J`-adically complete,
> `f : X ⟶ Spec A` proper, `F` coherent, and the conclusion for every `p ≥ 0`.
>
> The three hypotheses are the ones the source cites and the only places properness is used there;
> none of them is carried by this library for a proper morphism. See
> `Stacks.Algebraization.isIso_cohomologyToLimit` for what each of them says.

```lean
public theorem isIso_cohomologyToLimit_of_isProper (A : Type u) [CommRing A] [IsNoetherianRing A]
    (J : Ideal A) [IsAdicComplete J A] {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsProper f]
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (p : ℕ)
    (hfin : letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
      letI := baseAlgebra A f
      Module.Finite A
        ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).obj F.obj))
    (hker : letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
      letI := baseAlgebra A f
      ∃ c : ℕ, ∀ (n : ℕ) (x : ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections
          X).rightDerived p).obj F.obj)),
        (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).map
            (completionProjection X
              (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F (n + c))).hom x = 0 →
          x ∈ J ^ n • (⊤ : Submodule A ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections
            X).rightDerived p).obj F.obj)))
    (hstab : letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
      ∃ c : ℕ, ∀ (n : ℕ)
        (y : ↥((completionCohomologySystem
          (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F p).obj (op (n + c)))),
        ∃ x : ↥(((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).obj F.obj),
          (((Stacks.Cohomology.AffineBase.moduleGlobalSections X).rightDerived p).map
              (completionProjection X
                (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F n)).hom x =
            ((completionCohomologySystem
                (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F p).map
              (homOfLE (Nat.le_add_right n c)).op).hom y) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    IsIso (cohomologyToLimit
      (Stacks.Cohomology.FormalFunctions.baseIdealSheaf A J f) F p)
```

Declarations registered for the tag:

- [`Stacks.Algebraization.isIso_cohomologyToLimit_of_isProper_of_isAdicComplete`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/FullyFaithfulComplete.lean#L205), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ArtinReesChain.lean#L270) (StacksFrontier).

## Tag 02OD, a lemma

[Tag 02OD](https://stacks.math.columbia.edu/tag/02OD) in the Stacks Project.

**`Stacks.FormalFunctions.nonempty_adicCompletionHigherDirectImageStalkEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/CompletionStalkLimit.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/CompletionStalkLimit.lean#L119). References: EGA III (4.2.4), “Degree p = 0 case”.

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

**`Stacks.Cohomology.FormalFunctions.pushforwardPullbackBaseIdealIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsTheorem/IdealPowerQuotientSubscheme.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/FormalFunctionsTheorem/IdealPowerQuotientSubscheme.lean#L175). The attribute's comment: “the second step of the tag's proof: the identification i\_\{n*} ℱ\_n ≅ ℱ / 𝔪ⁿ ℱ, over an affine base and for the quotient by the n-th power of the ideal sheaf generated by an ideal of that base. The tag's conclusion is NOT asserted: that needs Tag 02OC, which rests on Tag 02O8, together with Tag 02KH”.

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

**`Stacks.FormalFunctions.infinitesimalNeighbourhood`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/InfinitesimalNeighbourhood.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/InfinitesimalNeighbourhood.lean#L260). The attribute's comment: “the infinitesimal neighbourhoods X\_n = X ×\_Y Spec(𝒪\_\{Y,y}/𝔪ⁿ) of the fibre, the setup paragraph of the tag. The conclusion -- that the completed stalk of R^p f\_* ℱ at y is the limit of the H^p(X\_n, ℱ\_n) -- is NOT asserted here: see the implementation notes for its three inputs and which of them are now available”.

> The `n`-th infinitesimal neighbourhood `X_n = Spec (𝒪_{Y,y}/𝔪_y ^ n) ×_Y X` of the fibre of
> `f : X ⟶ Y` over `y`.

```lean
public abbrev infinitesimalNeighbourhood (f : X ⟶ Y) (y : Y) (n : ℕ) : Scheme.{u}
```

## Tag 02OE, a lemma

[Tag 02OE](https://stacks.math.columbia.edu/tag/02OE) in the Stacks Project.

**`Stacks.FormalFunctions.isZero_stalk_higherDirectImage_of_finite_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteFibreVanishing.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalFunctions/FiniteFibreVanishing.lean#L142).

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

**`Stacks.AlgebraicGeometry.FibreDimension.isZero_stalk_rightDerivedPlus_of_fiber_dimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/HigherDirectImageFibreDimension/GeneralDimension.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/HigherDirectImageFibreDimension/GeneralDimension.lean#L133). References: EGA III (4.2.2), “partial”; SGA 6 X (4.4), “Stalk form of (4.4.5)”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
