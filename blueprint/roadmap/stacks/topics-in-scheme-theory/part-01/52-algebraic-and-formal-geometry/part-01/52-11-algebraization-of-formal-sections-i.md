---
declaration: section
origin: cited
lean: Stacks.Algebraization.isIso_toLimit_homology_puncturedSpectrumSections_of_two_le, Stacks.Algebraization.isIso_toLimit_homology_puncturedSpectrumSections, Stacks.Algebraization.isIso_toLimit_homology_derivedCompletion_puncturedSpectrumSections, Stacks.Algebraization.exists_homologyIso_limit_derivedCompletion_puncturedSpectrumSections, Stacks.Algebraization.coherentFormalAlgebraization, Stacks.Algebraization.PuncturedNeighbourhood.exists_ideal_finite_neighbourhoodCohomology, Stacks.Algebraization.PuncturedNeighbourhood.finite_neighbourhoodCohomology, Stacks.Algebraization.mono_comparisonMap_maximalIdeal
statement: formalized
proof: formalized
---

# 52.11 Algebraization of formal sections, I

Section 52.11 of the Stacks Project, [Tag 0DXH](https://stacks.math.columbia.edu/tag/0DXH). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DXI, a lemma

[Tag 0DXI](https://stacks.math.columbia.edu/tag/0DXI) in the Stacks Project.

**`Stacks.Algebraization.isIso_toLimit_homology_puncturedSpectrumSections_of_two_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCohomologyMittagLeffler.lean, line 672](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCohomologyMittagLeffler.lean#L672). The attribute's comment: “degrees `i ≥ 2`, for `RΓ(U, ℒ)` with `ℒ` a derived limit of `ℱ/Iⁿℱ` in `D(𝒪_U)`, which is `RΓ(U, ℱ)^∧` only by [Stacks, Tag 0BLX] + [Stacks, Tag 0A0K]; the Mittag-Leffler input of [Stacks, Tag 0DX1] part (2) is proved here, not assumed”.

> **Stacks Project, Tag 0DXI in degrees `i ≥ 2`, with no Mittag-Leffler hypothesis.** Let
> `(A, 𝔪)` be a Noetherian local ring, let `U = Spec A ∖ {𝔪}` be its punctured spectrum, let `ℱ` be
> a coherent `𝒪_U`-module and let `I ⊆ A` be an ideal. Let `S` be the adic quotient tower
> `n ↦ ℱ/Iⁿℱ`, pinned down by the quotient maps `π` through the universal property of killing
> multiplication by `Iⁿ`, and let `ℒ` be a derived limit of that tower in `D(𝒪_U)` — by
> [Stacks, Tag 0A0K] that is the derived completion `ℱ^∧`. Then for every `i ≥ 2` the comparison
> map `Hⁱ(RΓ(U, ℒ)) ⟶ lim_n Hⁱ(U, ℱ/Iⁿℱ)`, characterized by its composites with the limit
> projections, is an isomorphism.
>
> This is `Stacks.Algebraization.isIso_toLimit_homology_puncturedSpectrumSections` with its
> hypothesis `hML` discharged by
> `Stacks.Algebraization.isMittagLefflerCategorical_puncturedSpectrumCohomologySystem`, which is
> [Stacks, Tag 0DX1] part (2). The degree restriction is the one that lemma imposes: the Milnor
> sequence in degree `i` consumes the Mittag-Leffler condition in degree `i - 1`, and Tag 0DX1 part
> (2) supplies it for `i - 1 > 0`. As in that earlier statement the left-hand side is named by
> `ℒ`, which is `RΓ(U, ℱ)^∧` only by [Stacks, Tag 0BLX]; see the module documentation. The form
> recording the Milnor triangle that `a` fits into is
> `Stacks.Algebraization`
> `.exists_milnorTriangle_isIso_toLimit_homology_puncturedSpectrumSections_of_two_le`.

```lean
theorem isIso_toLimit_homology_puncturedSpectrumSections_of_two_le
    [IsNoetherianRing A] (I : Ideal A)
    (F : SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A)))
    [SheafOfModules.IsCoherent F]
    (S : ℕᵒᵖ ⥤ SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A)))
    (hScoherent : ∀ n : ℕᵒᵖ, SheafOfModules.IsCoherent (S.obj n))
    (π : ∀ n : ℕᵒᵖ, F ⟶ S.obj n)
    (hπ_epi : ∀ n : ℕᵒᵖ, Epi (π n))
    (hπ_nat : ∀ {m n : ℕᵒᵖ} (h : m ⟶ n), π m ≫ S.map h = π n)
    (hπ_smul : ∀ (n : ℕ) (a : A), a ∈ I ^ n →
      (baseSmul (puncturedSpectrumRingedSpace A) (puncturedSpectrumScalars A) a).asHom.app F ≫
        π (op n) = 0)
    (hπ_univ : ∀ (n : ℕ)
      (G : SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) (f : F ⟶ G),
      (∀ a ∈ I ^ n,
        (baseSmul (puncturedSpectrumRingedSpace A) (puncturedSpectrumScalars A) a).asHom.app F ≫
          f = 0) →
      ∃ g : S.obj (op n) ⟶ G, π (op n) ≫ g = f)
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))))
    (hL : IsDerivedLimit (S ⋙ DerivedCategory.singleFunctor
      (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0) L)
    (i : ℤ) (hi : 2 ≤ i) :
    let Hi := DerivedCategory.homologyFunctor (ModuleCat.{u} A) i
    let RΓS : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      S ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0 ⋙
        puncturedSpectrumDerivedSections A
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ RΓS.obj (op n)
    ∃ (a : (puncturedSpectrumDerivedSections A).obj L ⟶ ∏ᶜ Y)
      (q : Hi.obj ((puncturedSpectrumDerivedSections A).obj L) ⟶
        limit (puncturedSpectrumCohomologySystem A S i)),
      (∀ n : ℕ, q ≫ limit.π (puncturedSpectrumCohomologySystem A S i) (op n) =
        Hi.map a ≫ Hi.map (Pi.π Y n)) ∧ IsIso q
```

**`Stacks.Algebraization.isIso_toLimit_homology_puncturedSpectrumSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCompletedSections.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumCompletedSections.lean#L324). The attribute's comment: “for `RΓ(U, ℒ)` with `ℒ` a derived limit of the tower `ℱ/Iⁿℱ` in `D(𝒪_U)`, which is `RΓ(U, ℱ)^∧` only by [Stacks, Tag 0BLX] + [Stacks, Tag 0A0K]; the Mittag-Leffler condition of [Stacks, Tag 0DX1] part (2) is carried as the hypothesis `hML`, neither it nor [Stacks, Tag 0BLX] being available in this library”.

> **Stacks Project, Tag 0DXI, for the derived sections of a derived limit of the adic quotient
> tower.** Let `(A, 𝔪)` be a Noetherian local ring, let `U = Spec A ∖ {𝔪}` be its punctured
> spectrum, let `ℱ` be a coherent `𝒪_U`-module and let `I ⊆ A` be an ideal.  Let `S` be the adic
> quotient tower `n ↦ ℱ/Iⁿℱ`, pinned down by the quotient maps `π` through the universal property
> of killing multiplication by `Iⁿ`, and let `ℒ` be a derived limit of that tower in `D(𝒪_U)` —
> by [Stacks, Tag 0A0K] that is the derived completion `ℱ^∧`.  Then for *every* `i` the comparison
> map
> `Hⁱ(RΓ(U, ℒ)) ⟶ lim_n Hⁱ(U, ℱ/Iⁿℱ)`,
> characterized by its composites with the limit projections, is an isomorphism.
>
> The `R¹lim` term of the Milnor short exact sequence of [Stacks, Tag 0D60] vanishes because the
> inverse system `n ↦ H^{i-1}(U, ℱ/Iⁿℱ)` is Mittag-Leffler, which is the hypothesis `hML` — asked
> for in that one degree only, so that for `i ≥ 2` it is exactly what [Stacks, Tag 0DX1] part (2)
> would supply; that part of Tag 0DX1 is unavailable in this library.  By [Stacks, Tag 0BLX]
> `RΓ(U, ℱ^∧)` is the derived `I`-adic completion `RΓ(U, ℱ)^∧`, which is how the source names the
> left-hand side; that identity is also unavailable here, so the left-hand side is named by `ℒ`
> instead.  See the module documentation.

```lean
theorem isIso_toLimit_homology_puncturedSpectrumSections
    [IsNoetherianRing A] (I : Ideal A)
    (F : SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A)))
    [SheafOfModules.IsCoherent F]
    (S : ℕᵒᵖ ⥤ SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A)))
    (hScoherent : ∀ n : ℕᵒᵖ, SheafOfModules.IsCoherent (S.obj n))
    (π : ∀ n : ℕᵒᵖ, F ⟶ S.obj n)
    (hπ_epi : ∀ n : ℕᵒᵖ, Epi (π n))
    (hπ_nat : ∀ {m n : ℕᵒᵖ} (h : m ⟶ n), π m ≫ S.map h = π n)
    (hπ_smul : ∀ (n : ℕ) (a : A), a ∈ I ^ n →
      (baseSmul (puncturedSpectrumRingedSpace A) (puncturedSpectrumScalars A) a).asHom.app F ≫
        π (op n) = 0)
    (hπ_univ : ∀ (n : ℕ)
      (G : SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) (f : F ⟶ G),
      (∀ a ∈ I ^ n,
        (baseSmul (puncturedSpectrumRingedSpace A) (puncturedSpectrumScalars A) a).asHom.app F ≫
          f = 0) →
      ∃ g : S.obj (op n) ⟶ G, π (op n) ≫ g = f)
    (L : DerivedCategory (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))))
    (hL : IsDerivedLimit (S ⋙ DerivedCategory.singleFunctor
      (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0) L)
    (i : ℤ)
    (hML : IsMittagLefflerCategorical (puncturedSpectrumCohomologySystem A S (i - 1))) :
    let Hi := DerivedCategory.homologyFunctor (ModuleCat.{u} A) i
    let RΓS : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      S ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0 ⋙
        puncturedSpectrumDerivedSections A
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ RΓS.obj (op n)
    ∃ (a : (puncturedSpectrumDerivedSections A).obj L ⟶ ∏ᶜ Y)
      (q : Hi.obj ((puncturedSpectrumDerivedSections A).obj L) ⟶
        limit (puncturedSpectrumCohomologySystem A S i)),
      (∀ n : ℕ, q ≫ limit.π (puncturedSpectrumCohomologySystem A S i) (op n) =
        Hi.map a ≫ Hi.map (Pi.π Y n)) ∧ IsIso q
```

**`Stacks.Algebraization.isIso_toLimit_homology_derivedCompletion_puncturedSpectrumSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumDerivedCompletion.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumDerivedCompletion.lean#L213). The attribute's comment: “the whole lemma: for `(A, 𝔪)` Noetherian local with punctured spectrum `U`, a coherent `𝒪_U`-module `ℱ` and an ideal `I ⊆ A`, the comparison map `Hⁱ(RΓ(U,ℱ)^∧) ⟶ lim_n Hⁱ(U, ℱ/Iⁿℱ)` is an isomorphism in every degree `i`, the left-hand side being the derived `I`-adic completion in `D(A)` of the derived sections `RΓ(U,ℱ)` and the tower on the right being the adic quotient tower at `I𝒪_U`. The map shown invertible is the comparison map, characterized by the limit projections through an `α` required to exhibit `RΓ(U,ℱ)^∧` as a derived limit of `n ↦ RΓ(U, ℱ/Iⁿℱ)`”.

> **Stacks Project, Tag 0DXI.** Let `(A, 𝔪)` be a Noetherian local ring, let
> `U = Spec A ∖ {𝔪}` be its punctured spectrum, let `ℱ` be a coherent `𝒪_U`-module and let
> `I ⊆ A` be an ideal, presented by a finite generating family `a_1, …, a_r`. Then for every `i`
> the comparison map
>
> `Hⁱ(RΓ(U, ℱ)^∧) ⟶ lim_n Hⁱ(U, ℱ/Iⁿℱ)`
>
> is an isomorphism, where `RΓ(U, ℱ)^∧` is the derived `I`-adic completion of `RΓ(U, ℱ)` in `D(A)`
> and `ℱ/Iⁿℱ` is the adic quotient tower at the sheaf of ideals `I𝒪_U`.
>
> The comparison map is the one determined by the Milnor triangle: it is characterized by its
> composites with the limit projections through a morphism
> `α : RΓ(U, ℱ)^∧ ⟶ ∏ₙ RΓ(U, ℱ/Iⁿℱ)` which is required to exhibit `RΓ(U, ℱ)^∧` as a derived limit
> of `n ↦ RΓ(U, ℱ/Iⁿℱ)`, so the conclusion is about the comparison map and not about some map.
>
> Nothing is assumed: the derived limit of the tower, the identification of its derived sections
> with `RΓ(U, ℱ)^∧` and the Mittag-Leffler condition that makes the comparison invertible are all
> produced — by [Stacks, Tag 0A0K] parts (3) and (4), by [Stacks, Tag 0BLX], and by
> [Stacks, Tag 0DX1] part (2) together with its degree-zero and negative-degree companions.

```lean
theorem isIso_toLimit_homology_derivedCompletion_puncturedSpectrumSections
    (ha : Ideal.span (Set.range a) = I) (i : ℤ) :
    let S := puncturedSpectrumAdicQuotientSystem A a F
    let Hi := DerivedCategory.homologyFunctor (ModuleCat.{u} A) i
    let C := (DerivedCompletion.derivedCompletionFunctor A a).obj
      ((puncturedSpectrumDerivedSections A).obj ((DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0).obj F))
    let RΓS : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      S ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0 ⋙
        puncturedSpectrumDerivedSections A
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ RΓS.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ RΓS.map (homOfLE (Nat.le_succ n)).op
    ∃ (α : C ⟶ ∏ᶜ Y) (β : (∏ᶜ Y) ⟶ C⟦(1 : ℤ)⟧),
      Triangle.mk α d β ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
      ∃ q : Hi.obj C ⟶ limit (puncturedSpectrumCohomologySystem A S i),
        (∀ n : ℕ, q ≫ limit.π (puncturedSpectrumCohomologySystem A S i) (op n) =
          Hi.map α ≫ Hi.map (Pi.π Y n)) ∧ IsIso q
```

**`Stacks.Algebraization.exists_homologyIso_limit_derivedCompletion_puncturedSpectrumSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumDerivedCompletion.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumDerivedCompletion.lean#L290). The attribute's comment: “the whole lemma read as an isomorphism of `A`-modules: `Hⁱ(RΓ(U,ℱ)^∧) ≅ lim_n Hⁱ(U, ℱ/Iⁿℱ)` in every degree `i`, for `(A, 𝔪)` Noetherian local with punctured spectrum `U`, a coherent `𝒪_U`-module `ℱ` and an ideal `I ⊆ A`. The isomorphism is the comparison map, characterized by the limit projections through an `α` required to exhibit `RΓ(U,ℱ)^∧` as a derived limit of `n ↦ RΓ(U, ℱ/Iⁿℱ)`”.

> **Stacks Project, Tag 0DXI, read as an isomorphism of `A`-modules.** In the situation of
> `Stacks.Algebraization.isIso_toLimit_homology_derivedCompletion_puncturedSpectrumSections`, the
> degree-`i` cohomology of the derived `I`-adic completion of `RΓ(U, ℱ)` is isomorphic to the
> inverse limit of the `A`-modules `Hⁱ(U, ℱ/Iⁿℱ)`.
>
> The isomorphism keeps the characterization by the limit projections and `α` is still required to
> be a derived-limit structure map of `n ↦ RΓ(U, ℱ/Iⁿℱ)`, so what is asserted is that the
> comparison map is invertible and not merely that the two modules are abstractly isomorphic.

```lean
theorem exists_homologyIso_limit_derivedCompletion_puncturedSpectrumSections
    (ha : Ideal.span (Set.range a) = I) (i : ℤ) :
    let S := puncturedSpectrumAdicQuotientSystem A a F
    let Hi := DerivedCategory.homologyFunctor (ModuleCat.{u} A) i
    let C := (DerivedCompletion.derivedCompletionFunctor A a).obj
      ((puncturedSpectrumDerivedSections A).obj ((DerivedCategory.singleFunctor
        (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0).obj F))
    let RΓS : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{u} A) :=
      S ⋙ DerivedCategory.singleFunctor
          (SheafOfModules.{u} (structureSheafRing (puncturedSpectrumRingedSpace A))) 0 ⋙
        puncturedSpectrumDerivedSections A
    let Y : ℕ → DerivedCategory (ModuleCat.{u} A) := fun n ↦ RΓS.obj (op n)
    let d : (∏ᶜ Y) ⟶ ∏ᶜ Y := Pi.lift fun n : ℕ ↦
      Pi.π Y n - Pi.π Y (n + 1) ≫ RΓS.map (homOfLE (Nat.le_succ n)).op
    ∃ (α : C ⟶ ∏ᶜ Y) (β : (∏ᶜ Y) ⟶ C⟦(1 : ℤ)⟧),
      Triangle.mk α d β ∈ distTriang (DerivedCategory (ModuleCat.{u} A)) ∧
      ∃ eq : Hi.obj C ≅ limit (puncturedSpectrumCohomologySystem A S i),
        ∀ n : ℕ, eq.hom ≫ limit.π (puncturedSpectrumCohomologySystem A S i) (op n) =
          Hi.map α ≫ Hi.map (Pi.π Y n)
```

## Tag 0DXQ, a theorem

[Tag 0DXQ](https://stacks.math.columbia.edu/tag/0DXQ) in the Stacks Project.

**`Stacks.Algebraization.coherentFormalAlgebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentSheafPuncturedAlgebraization.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentSheafPuncturedAlgebraization.lean#L216).

> **Stacks 0DXQ.**  Let `(A, 𝔪)` be a Noetherian local ring which has a dualizing complex and
> is complete with respect to an ideal `I`.  Set `X = Spec A`, `Y = V(I)` and `U = X ∖ {𝔪}`, and
> let `ℱ` be a coherent sheaf on `U`.  Assume
>
> 1. `cd(A, I) ≤ d`, and
> 2. for any `x ∈ X ∖ Y` whose closure in `X` meets `U ∩ Y`,
>    `depth(ℱ_x) ≥ s` or `depth(ℱ_x) + dim(closure of x) > d + s`,
>
> Then there is an open `V₀ ⊆ U` containing `U ∩ Y` such that for any open `V ⊆ V₀` containing
> `U ∩ Y` the map
>
> `H^i(V, ℱ) ⟶ lim_n H^i(U, ℱ/Iⁿℱ)`
>
> is an isomorphism for `i < s`.  If in addition `depth(ℱ_x) + dim(closure of x) > s` for all
> `x ∈ U ∩ Y`, then these cohomology groups are finite `A`-modules.
>
> Concretely: there is a finite `A`-module `M` with `ℱ ≅ M̃|_U` and `ℱ/Iⁿℱ ≅ (M/IⁿM)~|_U` as
> towers, and an ideal `J₀` with `V(J₀) ∩ V(I) = {𝔪}` — that is, the open
> `V₀ = X ∖ V(J₀) ⊆ U` containing `U ∩ Y` — such that for every ideal `J ⊆ J₀` with
> `V(J) ∩ V(I) = {𝔪}` — that is, for every open `V = X ∖ V(J) ⊆ V₀` containing `U ∩ Y` — and every
> degree `i < s`, the canonical map `H^i(V, M̃) ⟶ lim_n H^i(U, (M/IⁿM)~)` is an isomorphism, and
> `H^i(V, M̃)` is a finite `A`-module whenever the extra depth bound holds.
>
> Both groups of that map are identified with the source's own, so that nothing is left to the
> reader:
>
> * `H^i(V, M̃)` is `H^i(V, ℱ|_V)`, the cohomology on `V` of the sheaf `ℱ` itself, by the conjunct
>   built from `Stacks.Algebraization.openCohomologyBaseRestrictIso`;
> * the tower `n ↦ H^i(U, (M/IⁿM)~)` whose limit the map lands in is the tower
>   `n ↦ H^i(U, ℱ/Iⁿℱ)`, transition maps included, by the conjunct built from
>   `Stacks.Algebraization.quotientSystemOpenCohomologyNatIso`.  An isomorphism of towers is
>   stronger than the isomorphism of limits it induces, so this pins the right-hand side without
>   either limit having to be formed again.
>
> The division of the two clauses is the source's.  The comparison is asserted under assumptions
> (1) and (2) alone; the extra bound `depth(ℱ_x) + dim(closure of x) > s` on `U ∩ Y` appears only
> as the hypothesis of the finiteness clause, where the source puts it ("If in addition …").  One
> ideal `J₀` serves both, by the case distinction carried out in
> `Stacks.Algebraization.PuncturedNeighbourhood.comparison_and_finiteness`.
>
> Nothing beyond the hypotheses of the theorem is assumed.  The module `M` is produced by Stacks
> 0BK0 (1), the ideal `J₀` by Stacks 0DXP and Stacks 0DXN, the stabilizing data of Stacks 0EFI and
> the bound `0 ≤ d` from assumption (1), and the localization triangle data of the degree-zero case
> from a finite generating family of `J`.  Properness of `I` — the source's standing `𝔪 ∈ V(I)`,
> without which `V(I)` is empty — is derived too, not assumed: over a local ring `I = A` would make
> `A` `⊤`-adically Hausdorff, hence zero.
>
> The two cohomology groups of the conclusion are named through the presentation `ℱ ≅ M̃|_U` and
> the tower isomorphism `ℱ/Iⁿℱ ≅ (M/IⁿM)~|_U`, both of which the statement exhibits; this is the
> reading the source itself uses, its proof opening with the choice of such an `M`.  The statement
> also carries out that reading, exhibiting each of the two groups of the comparison map as the
> corresponding group of `ℱ` — see the two conjuncts described above.

```lean
theorem coherentFormalAlgebraization (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A))
    (hcomplete : IsAdicComplete I A)
    (hdualizing : Dualizing.IsDualizingComplex omega)
    (hcd : Stacks.LocalCohomology.cohomologicalDimension A I
      (Ideal.fg_of_isNoetherianRing I) ≤ d)
    (F : (complementZeroLocus A (maximalIdeal A) : Scheme).Modules) [F.IsCoherent]
    (h2 : StalkDepthOrDimensionBound I F s d) :
    ∃ M : ModuleCat.{u} A, Module.Finite A M ∧
      Nonempty (F ≅ ((tilde.functor (CommRingCat.of A)).obj M).restrict
        (complementZeroLocus A (maximalIdeal A)).ι) ∧
      Nonempty (quotientSystemNearVanishing A I (maximalIdeal A) F ≅
        (adicQuotientModuleSystem A I M ⋙ tilde.functor (CommRingCat.of A)) ⋙
          Scheme.Modules.restrictFunctor (complementZeroLocus A (maximalIdeal A)).ι) ∧
      (∀ i : ℕ, Nonempty (quotientSystemNearVanishing A I (maximalIdeal A) F ⋙
          openCohomologyBaseFunctor A (complementZeroLocus A (maximalIdeal A)) i ≅
        adicQuotientModuleSystem A I M ⋙
          complementCohomologyBaseFunctor (A := CommRingCat.of A) (maximalIdeal A) i)) ∧
      ∃ J₀ : Ideal A,
        PrimeSpectrum.zeroLocus (J₀ : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
            {closedPoint A} ∧
          ∀ J : Ideal A, J ≤ J₀ →
            ∀ hV : PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
              {closedPoint A},
            ∀ i : ℕ, (i : ℤ) < s →
              IsIso (PuncturedNeighbourhood.neighbourhoodToPuncturedLimit I J M hV i) ∧
                Nonempty (openCohomologyBase A (complementZeroLocus A J)
                    ((Scheme.Modules.restrictFunctor
                      ((Spec (CommRingCat.of A)).homOfLE
                        (le_complementZeroLocus_maximalIdeal
                          (PuncturedNeighbourhood.le_maximalIdeal_of_zeroLocus_inter hV)))).obj F)
                      i ≅
                  complementCohomologyBase (A := CommRingCat.of A) J M i) ∧
                (StalkDepthAddDimGt I F s →
                  Module.Finite A
                    (complementCohomologyBase (A := CommRingCat.of A) J M i))
```

**`Stacks.Algebraization.PuncturedNeighbourhood.exists_ideal_finite_neighbourhoodCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedNeighbourhoodCohomologyFiniteness.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedNeighbourhoodCohomologyFiniteness.lean#L270). The attribute's comment: “finiteness of H^i(V, ℱ) for i < s, with ℱ = M̃|_U”.

> **Stacks 0DXQ, the finiteness clause.** Let `(A, 𝔪)` be a Noetherian local ring which has a
> dualizing complex and is `I`-adically complete, let `M` be a finite `A`-module, and assume
> assumptions (1) and (2) of the theorem together with
> `depth(M_𝔭) + dim(A/𝔭) > s` for every prime `𝔭 ∈ V(I)` other than `𝔪` — the theorem's extra
> finiteness assumption, read at the points of `U ∩ Y`. Then there is an ideal `J₀` with
> `V(J₀) ∩ V(I) = {𝔪}`, that is an open `V₀ = Spec A ∖ V(J₀)` of the punctured spectrum containing
> `U ∩ V(I)`, such that for every `J ⊆ J₀` with `V(J) ∩ V(I) = {𝔪}` — that is, for every open
> `V = Spec A ∖ V(J)` inside `V₀` containing `U ∩ V(I)` — the `A`-module `H^i(V, M̃)` is finite in
> every degree `i < s`.
>
> Nothing beyond the hypotheses of the theorem is assumed: the stabilizing data of Stacks 0EFI is
> constructed, not assumed, from assumption (1); see the module documentation.

```lean
public theorem exists_ideal_finite_neighbourhoodCohomology (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A)) (H : Hypotheses (M := M) I s d omega)
    (hdepth : DepthAddDimGtAtMaximalIdeal (M := M) I s) :
    ∃ J₀ : Ideal A,
      PrimeSpectrum.zeroLocus (J₀ : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
          {closedPoint A} ∧
        ∀ J : Ideal A, J ≤ J₀ →
          PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
            {closedPoint A} →
          ∀ i : ℕ, (i : ℤ) < s → Module.Finite A (neighbourhoodCohomology (M := M) J i)
```

**`Stacks.Algebraization.PuncturedNeighbourhood.finite_neighbourhoodCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedNeighbourhoodCohomologyFiniteness.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedNeighbourhoodCohomologyFiniteness.lean#L354). The attribute's comment: “finiteness of H^i(V, ℱ) for i < s, with ℱ = M̃|_U, on the carried existence statement of Stacks 0EFI”.

> **Stacks 0DXQ, the finiteness clause.** Let `(A, 𝔪)` be a Noetherian local ring which has a
> dualizing complex and is `I`-adically complete, let `M` be a finite `A`-module, and assume
> assumptions (1) and (2) of the theorem together with
> `depth(M_𝔭) + dim(A/𝔭) > s` for every prime `𝔭 ∈ V(I)` other than `𝔪` — the theorem's extra
> finiteness assumption, read at the points of `U ∩ Y`. Then there is an ideal `J₀` with
> `V(J₀) ∩ V(I) = {𝔪}`, that is an open `V₀ = Spec A ∖ V(J₀)` of the punctured spectrum containing
> `U ∩ V(I)`, such that for every `J ⊆ J₀` with `V(J) ∩ V(I) = {𝔪}` — that is, for every open
> `V = Spec A ∖ V(J)` inside `V₀` containing `U ∩ V(I)` — the `A`-module `H^i(V, M̃)` is finite in
> every degree `i < s`.
>
> The hypothesis `hex` is the existence statement of Stacks 0EFI, carried as a general statement
> about its own data; it is unused, the same conclusion being
> `exists_ideal_finite_neighbourhoodCohomology` with nothing carried.

```lean
public theorem finite_neighbourhoodCohomology (I : Ideal A) (s d : ℤ)
    (omega : DerivedCategory (ModuleCat.{u} A)) (H : Hypotheses (M := M) I s d omega)
    (hdepth : DepthAddDimGtAtMaximalIdeal (M := M) I s) (hex : StabilizingDataExists.{u}) :
    ∃ J₀ : Ideal A,
      PrimeSpectrum.zeroLocus (J₀ : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
          {closedPoint A} ∧
        ∀ J : Ideal A, J ≤ J₀ →
          PrimeSpectrum.zeroLocus (J : Set A) ∩ PrimeSpectrum.zeroLocus (I : Set A) =
            {closedPoint A} →
          ∀ i : ℕ, (i : ℤ) < s → Module.Finite A (neighbourhoodCohomology (M := M) J i)
```

## Tag 0DXR, a lemma

[Tag 0DXR](https://stacks.math.columbia.edu/tag/0DXR) in the Stacks Project.

**`Stacks.Algebraization.mono_comparisonMap_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumFormalSections.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumFormalSections.lean#L233). The attribute's comment: “the injectivity half of the displayed map, proved with none of the source's hypotheses beyond Noetherian and coherent; the surjectivity half and the finiteness of the two modules hold at the source's own hypotheses, by `Stacks.Algebraization.isIso_comparisonModuleMap_and_finite_maximalIdeal`”.

> **Stacks 0DXR, the injectivity half.** The canonical map from the sections of a coherent
> module `ℱ` on the punctured spectrum `U = Spec(A) ∖ {𝔪}` defined near `U ∩ V(I)` to the
> compatible families of sections of `ℱ / Iⁿ ℱ` on all of `U` is injective. No hypothesis beyond
> `A` Noetherian and `ℱ` coherent is used: neither completeness, nor the dualizing complex, nor
> the dimension bound at the associated points.
>
> The surjectivity half, and with it the whole of the source's conclusion — the map is an
> isomorphism and both of its sides are finite `A`-modules — is
> `Stacks.Algebraization.isIso_comparisonModuleMap_and_finite_maximalIdeal` of
> `PuncturedSpectrumFormalSectionsWhole.lean`, at the source's own hypotheses.

```lean
public theorem mono_comparisonMap_maximalIdeal [F.IsCoherent] :
    Mono (comparisonMap A I (maximalIdeal A) F)
```

**`Stacks.Algebraization.mono_comparisonModuleMap_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumFormalSections.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumFormalSections.lean#L259). The attribute's comment: “the two sides of the displayed map are A-modules and the map is A-linear, and injective as a map of A-modules; its underlying map of abelian groups is the tag's map, by forget₂_comparisonModuleMap. The surjectivity half and the finiteness of the two A-modules hold at the source's own hypotheses, by `Stacks.Algebraization.isIso_comparisonModuleMap_and_finite_maximalIdeal`”.

> **Stacks 0DXR, the `A`-module structures and the `A`-linearity of the displayed map.** The
> source states its conclusion as an isomorphism *of finite `A`-modules*, so the two sides carry
> `A`-module structures and the map between them is `A`-linear. The two sides of
> `Stacks.Algebraization.comparisonMap` are a colimit and a limit of groups of sections, hence
> abelian groups; the `A`-module structures are
> `Stacks.Algebraization.sectionsNearVanishingColimit` and
> `Stacks.Algebraization.formalSectionsLimit`, obtained from the multiplication by `A` on
> sections induced by `A ⟶ Γ(U, 𝒪_U)`, and the displayed map is `A`-linear for them, by
> `Stacks.Algebraization.comparisonMap_comp_smul`. The statement below is that this `A`-linear
> map — whose underlying map of abelian groups is the tag's map, by
> `Stacks.Algebraization.forget₂_comparisonModuleMap` — is injective, that is, that the
> injectivity half holds in the category of `A`-modules.
>
> The source's surjectivity half and the finiteness of the two `A`-modules are supplied, for this
> same `A`-linear map and at the source's own hypotheses, by
> `Stacks.Algebraization.isIso_comparisonModuleMap_and_finite_maximalIdeal` of
> `PuncturedSpectrumFormalSectionsWhole.lean`.

```lean
public theorem mono_comparisonModuleMap_maximalIdeal [F.IsCoherent] :
    Mono (comparisonModuleMap A I (maximalIdeal A) F)
```

**`Stacks.Algebraization.isIso_comparisonModuleMap_and_finite_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumFormalSectionsWhole.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PuncturedSpectrumFormalSectionsWhole.lean#L298). The attribute's comment: “the whole statement: the displayed map colim_V H⁰(V, ℱ) ⟶ lim_n H⁰(U, ℱ/Iⁿℱ) is an isomorphism of A-modules, and both of its two sides are finite A-modules”.

> **Stacks 0DXR.** Let `(A, 𝔪)` be a Noetherian local ring which has a dualizing complex and is
> complete with respect to an ideal `I`. Put `X = Spec(A)`, `Y = V(I)` and `U = X ∖ {𝔪}`, and let
> `ℱ` be a coherent module on `U` such that every associated point `x ∈ U` of `ℱ` satisfies
> `dim(closure {x}) > cd(A, I) + 1`, the closure being taken in `X`. Then the canonical map
>
> `colim_V H⁰(V, ℱ) ⟶ lim_n H⁰(U, ℱ / Iⁿ ℱ)`,
>
> the colimit being over the opens `V ⊆ U` containing `U ∩ Y`, is an isomorphism of finite
> `A`-modules.
>
> The two sides are the `A`-modules `Stacks.Algebraization.sectionsNearVanishingColimit` and
> `Stacks.Algebraization.formalSectionsLimit`; the map is
> `Stacks.Algebraization.comparisonModuleMap`, whose underlying map of abelian groups is
> `Stacks.Algebraization.comparisonMap` by
> `Stacks.Algebraization.forget₂_comparisonModuleMap`. The source's dimension hypothesis is stated
> with `dim(closure {x}) = dim(A/𝔭)`, exactly as the source states it.
>
> The proof is the source's: apply Stacks 0DXQ with `s = 1`, getting the finiteness too. Stacks
> 0BK0 (1) presents `ℱ` as `M̃|_U` for a finite `A`-module `M`; the associated points of `M̃|_U` are
> the associated primes of `M`, so the dimension hypothesis becomes the hypothesis of Stacks 0DXP,
> which supplies an ideal `J₀`, and of the finiteness clause of Stacks 0DXQ, which supplies an
> ideal `J₁`. At `J = J₀ ∩ J₁` both apply: the canonical map `H¹_J(M) ⟶ lim_n H¹_J(M/IⁿM)` is onto
> by Stacks 0DXP together with the pinned form of Stacks 0DXJ, so the four-term diagram chase makes
> the comparison at the neighbourhood `X ∖ V(J)` onto; the displayed map is injective with no
> hypothesis beyond Noetherian and coherent, hence an isomorphism; and the colimit is a quotient of
> `H⁰(X ∖ V(J), ℱ)`, which is finite.

```lean
public theorem isIso_comparisonModuleMap_and_finite_maximalIdeal
    (hcomplete : IsAdicComplete I A)
    (hdualizing : ∃ K : DerivedCategory (ModuleCat.{u} A), Dualizing.IsDualizingComplex K)
    (F : (complementZeroLocus A (maximalIdeal A) : Scheme).Modules) [F.IsCoherent]
    (hdim : ∀ x : (complementZeroLocus A (maximalIdeal A) : Scheme),
      x ∈ Stacks.Divisors.associatedPoints F →
      ((cohomologicalDimension A I I.fg_of_isNoetherianRing + 1 : ℤ) : EInt) <
        krullDimToEInt (ringKrullDim (A ⧸ x.1.asIdeal))) :
    IsIso (comparisonModuleMap A I (maximalIdeal A) F) ∧
      Module.Finite A (sectionsNearVanishingColimit A I (maximalIdeal A) F) ∧
        Module.Finite A (formalSectionsLimit A I (maximalIdeal A) F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.11, Tag 0DXH](https://stacks.math.columbia.edu/tag/0DXH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
