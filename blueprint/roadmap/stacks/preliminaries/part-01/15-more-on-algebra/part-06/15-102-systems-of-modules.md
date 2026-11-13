---
declaration: section
origin: cited
lean: Stacks.AdicSystem.ArtinReesHomology.exists_uniform_adic_homology_comparison, Stacks.PseudoCoherent.AdicCompletion.pseudoCoherent_mittagLeffler_and_isIso_adicCompletionToLimitDerivedReduction, Stacks.AdicSystem.DerivedReductionProIso.derivedReduction_proIsomorphic_adicReduction, Stacks.AdicSystem.HomComparison.hom_isom_quotient_systems_mittagLeffler_and_completion, Stacks.AdicSystem.CompletionIsomorphism.adicCompletion_linearEquiv_of_quotient_linearEquiv, Stacks.Modules.AdicSystem.AdicModuleSystem.delayedCategory, Stacks.AdicModuleSystem.IsomorphismCriterion.isIso_homOfRepresentative_iff, Stacks.AdicSystem.ExtDelayedIso.extAdicQuotientSystem_iso_extOfAdicQuotientsSystem
statement: formalized
proof: formalized
---

# 15.102 Systems of modules

Section 15.102 of the Stacks Project, [Tag 0EGT](https://stacks.math.columbia.edu/tag/0EGT). 11 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EGU, a lemma

[Tag 0EGU](https://stacks.math.columbia.edu/tag/0EGU) in the Stacks Project.

**`Stacks.AdicSystem.ArtinReesHomology.exists_uniform_adic_homology_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Homology/QuotientComparison.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Homology/QuotientComparison.lean#L152).

> **Stacks 0EGU.** For a complex of finite modules over a Noetherian ring, homology after
> reduction modulo `I ^ n` and the quotients by `I ^ n` of the original homology are canonically
> pro-isomorphic.  A single positive shift controls the inverse-system images, the comparison on
> ideal multiples, and the kernels and cokernels of all comparison maps.

```lean
theorem exists_uniform_adic_homology_comparison
    {A K L M : Type*} [CommRing A]
    [AddCommGroup K] [Module A K] [Module.Finite A K]
    [AddCommGroup L] [Module A L] [Module.Finite A L]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [IsNoetherianRing A]
    (I : Ideal A) (α : K →ₗ[A] L) (β : L →ₗ[A] M) (hcomplex : β.comp α = 0) :
    let H := (LinearMap.ker β) ⧸
      (LinearMap.range α).comap (LinearMap.ker β).subtype
    let cycles : ℕ → Submodule A L := fun n =>
      (I ^ n • (⊤ : Submodule A M)).comap β
    let boundaries : ℕ → Submodule A L := fun n =>
      LinearMap.range α ⊔ I ^ n • (⊤ : Submodule A L)
    let Hn : ℕ → Type _ := fun n =>
      cycles n ⧸ (boundaries n).comap (cycles n).subtype
    ∃ (toLevel : ∀ n, H →ₗ[A] Hn n)
      (transition : ∀ n, Hn (n + 1) →ₗ[A] Hn n)
      (quotTransition : ∀ n,
        (H ⧸ I ^ (n + 1) • (⊤ : Submodule A H)) →ₗ[A]
          (H ⧸ I ^ n • (⊤ : Submodule A H)))
      (fromQuotient : ∀ n,
        (H ⧸ I ^ n • (⊤ : Submodule A H)) →ₗ[A] Hn n),
      (∀ n (x : LinearMap.ker β) (y : cycles n), (y : L) = x →
        toLevel n (Submodule.Quotient.mk x) = Submodule.Quotient.mk y) ∧
      (∀ n (x : cycles (n + 1)) (y : cycles n), (y : L) = x →
        transition n (Submodule.Quotient.mk x) = Submodule.Quotient.mk y) ∧
      (∀ n (x : H),
        quotTransition n (Submodule.Quotient.mk x) = Submodule.Quotient.mk x) ∧
      (∀ n, transition n ∘ₗ toLevel (n + 1) = toLevel n) ∧
      (∀ n, fromQuotient n ∘ₗ (I ^ n • (⊤ : Submodule A H)).mkQ = toLevel n) ∧
      let Hsys : ℕᵒᵖ ⥤ ModuleCat A :=
        Functor.ofOpSequence (X := fun n => ModuleCat.of A (Hn n))
          (fun n => ModuleCat.ofHom (transition n))
      let Qsys : ℕᵒᵖ ⥤ ModuleCat A :=
        Functor.ofOpSequence
          (X := fun n => ModuleCat.of A (H ⧸ I ^ n • (⊤ : Submodule A H)))
          (fun n => ModuleCat.ofHom (quotTransition n))
      ∃ c : ℕ, 0 < c ∧
        (∃ back : ∀ n, c ≤ n → Hn n →ₗ[A]
            (H ⧸ I ^ (n - c) • (⊤ : Submodule A H)),
          (∀ n (hn : c ≤ n),
            (back n hn).comp (fromQuotient n) =
              (tr Qsys (Nat.sub_le n c)).hom) ∧
          (∀ n (hn : c ≤ n),
            (fromQuotient (n - c)).comp (back n hn) =
              (tr Hsys (Nat.sub_le n c)).hom) ∧
          Nonempty (ProIso Hsys Qsys) ∧
          Nonempty (limit Hsys ≅ limit Qsys) ∧
          (Hsys ⋙ forget (ModuleCat A)).IsMittagLeffler ∧
          (∀ n, LinearMap.range (tr Hsys (Nat.le_add_right n c)).hom =
            LinearMap.range (toLevel n)) ∧
          (∃ toLevelQuotient : ∀ n k,
              (H ⧸ I ^ k • (⊤ : Submodule A H)) →ₗ[A]
                (Hn n ⧸ I ^ k • (⊤ : Submodule A (Hn n))),
            (∀ n k, (toLevelQuotient n k).comp
                (I ^ k • (⊤ : Submodule A H)).mkQ =
              (I ^ k • (⊤ : Submodule A (Hn n))).mkQ.comp (toLevel n)) ∧
            (∀ n (hn : c ≤ n) (x : Hn n),
              x ∈ I ^ c • (⊤ : Submodule A (Hn n)) →
              toLevelQuotient n (n - c) (back n hn x) =
                (I ^ (n - c) • (⊤ : Submodule A (Hn n))).mkQ x)) ∧
          (∀ n,
            I ^ c ≤ Module.annihilator A (LinearMap.ker (fromQuotient n)) ∧
            I ^ c ≤ Module.annihilator A
              (Hn n ⧸ LinearMap.range (fromQuotient n))))
```

## Tag 0EGV, a lemma

[Tag 0EGV](https://stacks.math.columbia.edu/tag/0EGV) in the Stacks Project.

**`Stacks.PseudoCoherent.AdicCompletion.pseudoCoherent_mittagLeffler_and_isIso_adicCompletionToLimitDerivedReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/DerivedReductionCompletion.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/DerivedReductionCompletion.lean#L550).

> **Stacks 0EGV (Kollár--Kovács), canonical form.** Let `I` be an ideal of a Noetherian ring
> `A` and `K` a pseudo-coherent object of `D(A)`, and set `Kₙ = K ⊗ᴸ[A] A/Iⁿ⁺¹`. Then for every `i`
> the inverse system `Hⁱ(Kₙ)` is Mittag--Leffler, and the canonical map
> `lim Hⁱ(K)/IⁿHⁱ(K) ⟶ lim Hⁱ(Kₙ)`, induced by the reduction maps `K ⟶ Kₙ`
> (`adicCompletionToLimitDerivedReduction`), is an isomorphism.

```lean
theorem pseudoCoherent_mittagLeffler_and_isIso_adicCompletionToLimitDerivedReduction
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (K : DerivedCategory (ModuleCat.{u} A))
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) :
    ∀ i : ℤ,
      (((NoetherianAdicCompletion.idealPowerQuotientSystem I ⋙ T.tensor.obj K) ⋙
          DerivedCategory.homologyFunctor (ModuleCat.{u} A) i) ⋙
        forget (ModuleCat.{u} A)).IsMittagLeffler ∧
      IsIso (adicCompletionToLimitDerivedReduction I T K i)
```

## Tag 0G9M, a lemma

[Tag 0G9M](https://stacks.math.columbia.edu/tag/0G9M) in the Stacks Project.

**`Stacks.AdicSystem.DerivedReductionProIso.derivedReduction_proIsomorphic_adicReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/IdealPowerTensor.lean, line 2878](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/IdealPowerTensor.lean#L2878).

> **Stacks Project, Tag 0G9M.** Let `I` be an ideal of a Noetherian ring `A` and let `M` be a
> bounded complex of finite `A`-modules.  Then `M` admits a bounded-above resolution `p : P -> M`
> by finite free modules, and the canonical comparison from the derived reductions of `P` modulo
> the positive powers of `I` to the degreewise reductions of `M` is compatible with the
> transition maps and is an isomorphism of pro-objects in the derived category: each level
> acquires a two-sided inverse after passing to a later level.

```lean
public theorem derivedReduction_proIsomorphic_adicReduction
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i)) :
    ∃ (P : CochainComplex (ModuleCat.{u} A) ℤ) (p : P ⟶ M),
      (∃ b : ℤ, P.IsStrictlyLE b) ∧
      (∀ i : ℤ, Module.Finite A (P.X i) ∧ Module.Free A (P.X i)) ∧
      IsIso (DerivedCategory.Q.map p) ∧
      (∀ n : ℕ,
        adicReductionTransition I P (Nat.le_succ n) ≫ adicReductionComparison I p n =
          adicReductionComparison I p (n + 1) ≫
            adicReductionTransition I M (Nat.le_succ n)) ∧
      ∀ n : ℕ, ∃ (m : ℕ) (h : n ≤ m)
          (s : DerivedCategory.Q.obj ((reduceComplex (I ^ (m + 1))).obj M) ⟶
            DerivedCategory.Q.obj ((reduceComplex (I ^ (n + 1))).obj P)),
          adicReductionComparison I p m ≫ s =
              adicReductionTransition I P h ∧
            s ≫ adicReductionComparison I p n =
              adicReductionTransition I M h
```

## Tag 09BB, a lemma

[Tag 09BB](https://stacks.math.columbia.edu/tag/09BB) in the Stacks Project.

**`Stacks.AdicSystem.HomComparison.hom_isom_quotient_systems_mittagLeffler_and_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Hom/MittagLeffler.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Hom/MittagLeffler.lean#L588). References: EGA 0 (7.3.4), “Hom^ ≅ Hom(M^,N^)”; EGA 0 (7.8.2), “canonical isomorphism”.

> **Stacks 09BB.** Homomorphisms and isomorphisms between the adic quotients of two
> finite modules form Mittag--Leffler systems.  The canonical comparison from the adic
> quotients of `Hom` has uniformly bounded kernel and cokernel, and passage to the inverse
> limit identifies both homomorphisms and isomorphisms with those between the completed
> modules.

```lean
public theorem hom_isom_quotient_systems_mittagLeffler_and_completion
    {A : Type u} {M : Type v} {N : Type w} [CommRing A] [IsNoetherianRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [AddCommGroup N] [Module A N] [Module.Finite A N]
    (I : Ideal A) :
    let Mq : ℕ → Type _ := fun n => M ⧸ I ^ n • (⊤ : Submodule A M)
    let Nq : ℕ → Type _ := fun n => N ⧸ I ^ n • (⊤ : Submodule A N)
    let H : ℕ → Type _ := fun n => Mq n →ₗ[A] Nq n
    let E : ℕ → Type _ := fun n => Mq n ≃ₗ[A] Nq n
    ∃ (homTransition : ∀ n, H (n + 1) →ₗ[A] H n)
      (isoTransition : ∀ n, E (n + 1) → E n)
      (comparison : ∀ n,
        ((M →ₗ[A] N) ⧸ I ^ n • (⊤ : Submodule A (M →ₗ[A] N))) →ₗ[A] H n),
      (∀ n (f : H (n + 1)) (m : M),
        homTransition n f (Submodule.Quotient.mk m) =
          AdicCompletion.transitionMap I N (Nat.le_succ n)
            (f (Submodule.Quotient.mk m))) ∧
      (∀ n (e : E (n + 1)) (m : M),
        isoTransition n e (Submodule.Quotient.mk m) =
          AdicCompletion.transitionMap I N (Nat.le_succ n)
            (e (Submodule.Quotient.mk m))) ∧
      (∀ n (f : M →ₗ[A] N) (m : M),
        comparison n (Submodule.Quotient.mk f) (Submodule.Quotient.mk m) =
          Submodule.Quotient.mk (f m)) ∧
      let HomSys : ℕᵒᵖ ⥤ ModuleCat A :=
        Functor.ofOpSequence (X := fun n => ModuleCat.of A (H n))
          (fun n => ModuleCat.ofHom (homTransition n))
      let IsoSys : ℕᵒᵖ ⥤ Type (max v w) :=
        Functor.ofOpSequence (X := E) (fun n => TypeCat.ofHom (isoTransition n))
      (HomSys ⋙ forget (ModuleCat A)).IsMittagLeffler ∧
      IsoSys.IsMittagLeffler ∧
      (∃ c : ℕ, ∀ n,
        I ^ c ≤ Module.annihilator A (LinearMap.ker (comparison n)) ∧
        I ^ c ≤ Module.annihilator A
          (H n ⧸ LinearMap.range (comparison n))) ∧
      (∃ homLimitIso :
          limit HomSys ≅ ModuleCat.of A (AdicCompletion I (M →ₗ[A] N)),
        ∀ (f : ↥(limit HomSys)) n,
          comparison n
              (AdicCompletion.eval I (M →ₗ[A] N) n (homLimitIso.hom.hom f)) =
            (limit.π HomSys (op n)).hom f) ∧
      (∃ completedHomEquiv :
          AdicCompletion I (M →ₗ[A] N) ≃ₗ[AdicCompletion I A]
            (AdicCompletion I M →ₗ[AdicCompletion I A] AdicCompletion I N),
        ∀ (f : M →ₗ[A] N) (m : M),
          completedHomEquiv (AdicCompletion.of I (M →ₗ[A] N) f)
              (AdicCompletion.of I M m) =
            AdicCompletion.of I N (f m)) ∧
      ∃ isoLimitEquiv :
          { e : ∀ n, E n // ∀ n, isoTransition n (e (n + 1)) = e n } ≃
            (AdicCompletion I M ≃ₗ[AdicCompletion I A] AdicCompletion I N),
        ∀ (e : { e : ∀ n, E n // ∀ n, isoTransition n (e (n + 1)) = e n })
          (n : ℕ) (m : M),
          e.1 n (Submodule.Quotient.mk m) =
            AdicCompletion.eval I N n
              (isoLimitEquiv e (AdicCompletion.of I M m))
```

## Tag 09BC, a lemma

[Tag 09BC](https://stacks.math.columbia.edu/tag/09BC) in the Stacks Project.

**`Stacks.AdicSystem.CompletionIsomorphism.adicCompletion_linearEquiv_of_quotient_linearEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Hom/MittagLeffler.lean, line 672](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Hom/MittagLeffler.lean#L672).

> **Stacks 09BC.** If all quotients of two finite modules by powers of an ideal
> are linearly equivalent, then their adic completions are linearly equivalent over
> the completed ring.

```lean
public theorem adicCompletion_linearEquiv_of_quotient_linearEquiv
    {A : Type u} {M : Type v} {N : Type w} [CommRing A] [IsNoetherianRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [AddCommGroup N] [Module A N] [Module.Finite A N]
    (I : Ideal A)
    (h : ∀ n : ℕ,
      Nonempty ((M ⧸ I ^ n • (⊤ : Submodule A M)) ≃ₗ[A]
        (N ⧸ I ^ n • (⊤ : Submodule A N)))) :
    Nonempty (AdicCompletion I M ≃ₗ[AdicCompletion I A] AdicCompletion I N)
```

## Tag 0EGW, a remark

[Tag 0EGW](https://stacks.math.columbia.edu/tag/0EGW) in the Stacks Project.

**`Stacks.Modules.AdicSystem.AdicModuleSystem.delayedCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Category.lean, line 991](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Category.lean#L991).

> **Stacks 0EGW.** Systems of finite `A ⧸ I ^ n`-modules, with morphisms represented by
> maps `I ^ c Eₙ → Fₙ / Fₙ[I ^ c]` modulo increasing `c`, form a category. Composition is
> the induced composition at delay `c + c'`.

```lean
public noncomputable def delayedCategory : CategoryData (A := A) (I := I)
```

## Tag 0EGX, a lemma

[Tag 0EGX](https://stacks.math.columbia.edu/tag/0EGX) in the Stacks Project.

**`Stacks.AdicModuleSystem.IsomorphismCriterion.isIso_homOfRepresentative_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Category.lean, line 1415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Category.lean#L1415).

> **Stacks 0EGX.** A delayed representative induces an isomorphism in the category of
> systems if and only if, eventually, the kernels and cokernels of all its component maps are
> annihilated by a single fixed power of the ideal.

```lean
public theorem isIso_homOfRepresentative_iff (r : HomRepresentative E F) :
    letI := (AdicModuleSystem.delayedCategory (A := A) (I := I)).toCategory
    IsIso (show E ⟶ F from homOfRepresentative r) ↔
      ∃ c' : ℕ, ∀ᶠ n : ℕ+ in atTop, ∀ h : r.delay ≤ (n : ℕ),
        Module.IsTorsionBySet A (r.map n h).ker (↑(I ^ c') : Set A) ∧
          Module.IsTorsionBySet A
            ((underlying F n ⧸ torsionPart F n r.delay) ⧸
              LinearMap.range (r.map n h)) (↑(I ^ c') : Set A)
```

## Tag 0EGY, a lemma

[Tag 0EGY](https://stacks.math.columbia.edu/tag/0EGY) in the Stacks Project.

**`Stacks.AdicSystem.ExtDelayedIso.extAdicQuotientSystem_iso_extOfAdicQuotientsSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Ext/DelayedIso.lean, line 853](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Ext/DelayedIso.lean#L853).

> **Stacks 0EGY.** For finite modules over a Noetherian ring, the system of adic
> quotients of `Ext` is isomorphic, in the category of delayed morphisms, to the system of
> `Ext` groups over the corresponding quotient rings.

```lean
public theorem extAdicQuotientSystem_iso_extOfAdicQuotientsSystem
    (I : Ideal A) (M N : Type v)
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [AddCommGroup N] [Module A N] [Module.Finite A N] (i : ℕ) :
    letI := (AdicModuleSystem.delayedCategory (A := A) (I := I)).toCategory
    Nonempty (extAdicQuotientSystem I M N i ≅ extOfAdicQuotientsSystem I M N i)
```

## Tag 0EGZ, a remark

[Tag 0EGZ](https://stacks.math.columbia.edu/tag/0EGZ) in the Stacks Project.

**`Stacks.AdicSystem.ExtComparison.exists_eventually_extOfAdicQuotients_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Ext/Comparison.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Ext/Comparison.lean#L478). The attribute's comment: “corrected: the maps are defined on I^c-multiples and their kernels and cokernels are killed by a possibly larger power I^d; the single exponent claimed by Stacks fails”.

> **Stacks 0EGZ.** There are powers `I ^ c` and `I ^ d` such that, for `m ≫ n ≫ 0`, canonical
> maps from `I ^ c Ext_{A_m}^i(M_m,N_m) / I ^ n Ext_{A_m}^i(M_m,N_m)` to
> `Ext_{A_n}^i(M_n,N_n) / Ext_{A_n}^i(M_n,N_n)[I ^ c]` have kernel and cokernel annihilated
> by `I ^ d`. The displayed factorization characterizes these maps in terms of mutually
> inverse representatives of the isomorphism of Tag 0EGY.
>
> This is the corrected form of the remark. As printed, Stacks asks for one exponent `c` that
> both defines the maps and annihilates their kernels and cokernels; that is false, for any
> choice of maps (see `errata.md`): for `A = k[x, y, z]`, `I = (x, y, z)`, `M = A / (x)`,
> `N = A / (x²)` and `i = 0` it is refuted by
> `ExtComparisonCounterexample.not_exists_extOfAdicQuotients_comparison_one_exponent`.
> Here the maps live on `I ^ c`-multiples with `c` the total delay of the two representatives,
> and their kernels and cokernels are annihilated by a possibly larger power `I ^ d`.

```lean
public theorem exists_eventually_extOfAdicQuotients_comparison (I : Ideal A) (M N : Type v)
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    [AddCommGroup N] [Module A N] [Module.Finite A N] (i : ℕ) :
    letI := (AdicModuleSystem.delayedCategory (A := A) (I := I)).toCategory
    let E := extAdicQuotientSystem I M N i
    let F := extOfAdicQuotientsSystem I M N i
    ∃ (e : E ≅ F) (r : AdicModuleSystem.HomRepresentative E F)
        (s : AdicModuleSystem.HomRepresentative F E),
      AdicModuleSystem.homOfRepresentative r = e.hom ∧
      AdicModuleSystem.homOfRepresentative s = e.inv ∧
      let c := s.delay + r.delay
      ∃ d : ℕ,
      ∃ comparison : ∀ (n m : ℕ+) (_ : c ≤ (n : ℕ)) (_ : n ≤ m),
          (AdicModuleSystem.powerPart F m c ⧸
              (AdicModuleSystem.powerPart F m (n : ℕ)).comap
                (AdicModuleSystem.powerPart F m c).subtype) →ₗ[A]
            AdicModuleSystem.underlying F n ⧸ AdicModuleSystem.torsionPart F n c,
        ∀ᶠ n : ℕ+ in atTop, ∀ᶠ m : ℕ+ in atTop,
          ∀ (hn : c ≤ (n : ℕ)) (hnm : n ≤ m),
            (∀ z : AdicModuleSystem.powerPart F m c,
              ∃ (yₘ : AdicModuleSystem.powerPart E m r.delay)
                (yₙ : AdicModuleSystem.powerPart E n r.delay),
                s.map m (le_trans (Nat.le_add_right s.delay r.delay)
                    (le_trans hn (mod_cast hnm)))
                    ⟨z, AdicModuleSystem.powerPart_add_le_left F m s.delay r.delay z.2⟩ =
                  (AdicModuleSystem.torsionPart E m s.delay).mkQ yₘ.1 ∧
                extAdicQuotientTransition I M N i hnm yₘ = yₙ ∧
                comparison n m hn hnm
                    (Quotient.mk _ z) =
                  AdicModuleSystem.quotientTransitionOfLE F n
                    (Nat.le_add_left r.delay s.delay)
                    (r.map n (le_trans (Nat.le_add_left r.delay s.delay) hn) yₙ)) ∧
            Module.IsTorsionBySet A (comparison n m hn hnm).ker
              (↑(I ^ d) : Set A) ∧
            Module.IsTorsionBySet A
              ((AdicModuleSystem.underlying F n ⧸ AdicModuleSystem.torsionPart F n c) ⧸
                LinearMap.range (comparison n m hn hnm)) (↑(I ^ d) : Set A)
```

**`Stacks.AdicSystem.ExtComparisonCounterexample.not_exists_extOfAdicQuotients_comparison_one_exponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Ext/ComparisonCounterexample.lean, line 627](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Ext/ComparisonCounterexample.lean#L627). The attribute's comment: “counterexample: for A = k[x, y, z], I = (x, y, z), M = A/(x), N = A/(x²), i = 0, no c and no maps I^c E\_m / I^n E\_m → E\_n / E\_n[I^c] have kernel killed by I^c”.

> **Stacks 0EGZ is false as stated.** Remark 0EGZ asserts a single `c ≥ 0` such that for
> `m ≫ n ≫ 0` there are maps `I ^ c Eₘ / I ^ n Eₘ → Eₙ / Eₙ[I ^ c]`, with
> `Eₙ = Ext^i_{Aₙ}(Mₙ, Nₙ)`, whose kernel and cokernel are annihilated by `I ^ c`. For
> `A = k[x, y, z]`, `I = (x, y, z)`, `M = A / (x)`, `N = A / (x²)` and `i = 0` no such `c` exists,
> whatever maps are allowed: even the kernel condition alone fails. The corrected statement, with
> the kernel and cokernel killed by a possibly larger power, is
> `Stacks.AdicSystem.ExtComparison.exists_eventually_extOfAdicQuotients_comparison`.

```lean
public theorem not_exists_extOfAdicQuotients_comparison_one_exponent (k : Type u) [Field k] :
    let A := MvPolynomial (Fin 3) k
    let I : Ideal A := idealOfVars (Fin 3) k
    let M := A ⧸ Ideal.span {(X 0 : A)}
    let N := A ⧸ Ideal.span {(X 0 : A) ^ 2}
    let F := extOfAdicQuotientsSystem I M N 0
    ¬ ∃ c : ℕ, ∀ᶠ n : ℕ+ in atTop, ∀ᶠ m : ℕ+ in atTop, n ≤ m →
      ∃ f : (powerPart F m c ⧸ (powerPart F m (n : ℕ)).comap (powerPart F m c).subtype) →ₗ[A]
          underlying F n ⧸ torsionPart F n c,
        Module.IsTorsionBySet A (LinearMap.ker f) (↑(I ^ c) : Set A) ∧
        Module.IsTorsionBySet A
          ((underlying F n ⧸ torsionPart F n c) ⧸ LinearMap.range f) (↑(I ^ c) : Set A)
```

## Tag 0EH2, an example

[Tag 0EH2](https://stacks.math.columbia.edu/tag/0EH2) in the Stacks Project.

**`Stacks.AdicSystem.ExtCounterexample.extTwo_not_preserved_by_adicQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Ext/Counterexample.lean, line 742](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Ext/Counterexample.lean#L742).

> **Stacks 0EH2.** For `A = k[[x, y]] / (xy)` and `M = A / (y)`, the periodic
> resolution computes `Ext_A^2(M, N)` as `N[y] / xN`.  At the finite level the numerator
> is the intersection of the `y`-torsion and the `x^(n - 1)`-torsion.  In particular,
> for `N = M`, the original Ext group is additively isomorphic to `k`, while every
> finite-level Ext group vanishes.

```lean
public theorem extTwo_not_preserved_by_adicQuotients (k : Type u) [Field k] :
    let R := MvPowerSeries (Fin 2) k
    let X : R := MvPowerSeries.X 0
    let Y : R := MvPowerSeries.X 1
    let A := R ⧸ Ideal.span {X * Y}
    let x : A := Ideal.Quotient.mk _ X
    let y : A := Ideal.Quotient.mk _ Y
    let I : Ideal A := Ideal.span {x}
    let M := A ⧸ Ideal.span {y}
    Function.Exact (LinearMap.lsmul A A y) (LinearMap.lsmul A A x) ∧
      Function.Exact (LinearMap.lsmul A A x) (LinearMap.lsmul A A y) ∧
      Function.Exact (LinearMap.lsmul A A y) (Submodule.mkQ (Ideal.span {y})) ∧
      Function.Surjective (Submodule.mkQ (Ideal.span {y})) ∧
      (∀ (N : Type u) [AddCommGroup N] [Module A N],
        let Ky := LinearMap.ker (LinearMap.lsmul A N y)
        Nonempty (Ext (ModuleCat.of A M) (ModuleCat.of A N) 2 ≃ₗ[A]
          (Ky ⧸ ((I • (⊤ : Submodule A N)).comap Ky.subtype)))) ∧
      (∀ (n : ℕ+),
        let An := A ⧸ I ^ (n : ℕ)
        let xn : An := Ideal.Quotient.mk _ x
        let yn : An := Ideal.Quotient.mk _ y
        let Mn := M ⧸ (I ^ (n : ℕ) • (⊤ : Submodule A M))
        ∃ q : An →ₗ[An] Mn,
          q 1 = Submodule.Quotient.mk (Ideal.Quotient.mk (Ideal.span {y}) 1) ∧
          Function.Surjective q ∧
          Function.Exact (LinearMap.lsmul An An yn) q ∧
          Function.Exact (LinearMap.lsmul An An xn) (LinearMap.lsmul An An yn) ∧
          Function.Exact
            ((LinearMap.lsmul An An yn).coprod
              (LinearMap.lsmul An An (xn ^ ((n : ℕ) - 1))))
            (LinearMap.lsmul An An xn)) ∧
      (∀ (N : Type u) [AddCommGroup N] [Module A N] (n : ℕ+),
        let An := A ⧸ I ^ (n : ℕ)
        let anCommRing : CommRing An := Ideal.Quotient.commRing (I ^ (n : ℕ))
        letI : Ring An := anCommRing.toRing
        letI : CommSemiring An := anCommRing.toCommSemiring
        letI : Semiring An := anCommRing.toSemiring
        letI : Linear An (ModuleCat An) := ModuleCat.Algebra.instLinear
        let xn : An := Ideal.Quotient.mk _ x
        let yn : An := Ideal.Quotient.mk _ y
        let Nn := N ⧸ (I ^ (n : ℕ) • (⊤ : Submodule A N))
        let K := LinearMap.ker (LinearMap.lsmul An Nn yn) ⊓
          LinearMap.ker (LinearMap.lsmul An Nn (xn ^ ((n : ℕ) - 1)))
        let xNn : Submodule An Nn := Ideal.span {xn} • ⊤
        let xK : Submodule An K := xNn.comap K.subtype
        Nonempty (Ext (ModuleCat.of An
            (M ⧸ (I ^ (n : ℕ) • (⊤ : Submodule A M))))
          (ModuleCat.of An Nn) 2 ≃ₗ[An] (K ⧸ xK))) ∧
      letI : Module k (Ext (ModuleCat.of A M) (ModuleCat.of A M) 2) :=
        Module.compHom _ (algebraMap k A)
      Nonempty (Ext (ModuleCat.of A M) (ModuleCat.of A M) 2 ≃ₗ[k] k) ∧
      (∀ (n : ℕ+),
        let An := A ⧸ I ^ (n : ℕ)
        let xn : An := Ideal.Quotient.mk _ x
        let Mn := M ⧸ (I ^ (n : ℕ) • (⊤ : Submodule A M))
        Nonempty (Mn ≃ₗ[k] ((Polynomial k) ⧸
          (Ideal.span {Polynomial.X ^ (n : ℕ)} : Ideal (Polynomial k)))) ∧
          Function.Exact (LinearMap.lsmul An Mn xn)
            (LinearMap.lsmul An Mn (xn ^ ((n : ℕ) - 1))) ∧
          Subsingleton (Ext (ModuleCat.of An Mn) (ModuleCat.of An Mn) 2))
```

## Tag 0EH0, a lemma

[Tag 0EH0](https://stacks.math.columbia.edu/tag/0EH0) in the Stacks Project.

**`Stacks.AdicSystem.ExtFlatBaseChange.limit_ext_quotient_iso_limit_ext_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Ext/FlatBaseChange.lean, line 1151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/Ext/FlatBaseChange.lean#L1151). The attribute's comment: “canonical maps, pinned down by the injective comparison `extQuotientToBase`; `M`, `N` finite `B`-modules (the source's A-modules is a typo)”.

> **Stacks 0EH0.** Let `A → B` be a flat map of Noetherian rings, let `I ⊆ A` be an ideal and
> let `M`, `N` be finite `B`-modules; put `B_n = B / I^n B`, `M_n = M / I^n M`, `N_n = N / I^n N`.
> If `M` is flat over `A`, then for every `i`
> `lim_n Ext^i_B(M, N) / I^n Ext^i_B(M, N) = lim_n Ext^i_{B_n}(M_n, N_n)`.
>
> The identification is the one induced by the canonical maps. Write
> `ρ_n : Ext^i_{B_n}(M_n, N_n) → Ext^i_B(M, N_n)` for restriction of scalars along `B → B_n`
> followed by precomposition with `M → M_n` (`extQuotientToBase`); the first clause says that
> `ρ_n` is injective. The canonical reduction `Ext^i_B(M, N) → Ext^i_{B_n}(M_n, N_n)` is therefore
> the unique map `r_n` with `ρ_n ∘ r_n` equal to postcomposition with `N → N_n`, and the canonical
> transition `Ext^i_{B_{n+1}}(M_{n+1}, N_{n+1}) → Ext^i_{B_n}(M_n, N_n)` is the unique map `t_n`
> with `ρ_n ∘ t_n` equal to `ρ_{n+1}` followed by `N_{n+1} → N_n`. The second clause gives these
> maps, `A`-linear, a factorization `f_n` of `r_n` through `E / I^n E`, and says that the `f_n`
> induce an isomorphism from the limit of the `I`-adic quotients of `E = Ext^i_B(M, N)` (along the
> canonical maps `E / I^{n+1} E → E / I^n E`) to the limit of the `Ext^i_{B_n}(M_n, N_n)` along the
> `t_n`.
>
> `M` and `N` are lifted to a common universe with `ULift`, and `M_n` is written as the quotient
> `ULift M ⧸ I^n B • ULift M`.

```lean
public theorem limit_ext_quotient_iso_limit_ext_canonical
    {A : Type uA} {B : Type uB} {M : Type uM} {N : Type uN}
    [CommRing A] [CommRing B] [Algebra A B]
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M]
    [AddCommGroup N] [Module B N]
    [IsNoetherianRing A] [IsNoetherianRing B] [Module.Flat A B]
    [Module.Finite B M] [Module.Finite B N] [Module.Flat A M]
    (I : Ideal A) :
    let J := I.map (algebraMap A B)
    let X := ModuleCat.of B (ULift.{max uA uB uM uN} M)
    let Y := ModuleCat.of B (ULift.{max uA uB uM uN} N)
    let E : ℕ → Type (max uA uB uM uN) := fun i => Ext X Y i
    let _ : ∀ i, Module A (E i) := fun i => Module.compHom (E i) (algebraMap A B)
    let En : ℕ → ℕ → Type (max uA uB uM uN) := fun i n =>
      Ext (ModuleCat.of (B ⧸ J ^ n) (X ⧸ J ^ n • (⊤ : Submodule B X)))
        (ModuleCat.of (B ⧸ J ^ n) (Y ⧸ J ^ n • (⊤ : Submodule B Y))) i
    let _ : ∀ i n, Module A (En i n) := fun i n =>
      Module.compHom (En i n) (algebraMap A (B ⧸ J ^ n))
    (∀ i n, Function.Injective (extQuotientToBase (J ^ n) X Y i)) ∧
    ∃ (reduction : ∀ i n, E i →ₗ[A] En i n)
      (transition : ∀ i n, En i (n + 1) →ₗ[A] En i n)
      (comparison : ∀ i n, (E i ⧸ I ^ n • (⊤ : Submodule A (E i))) →ₗ[A] En i n),
      (∀ i n (x : E i), extQuotientToBase (J ^ n) X Y i (reduction i n x) =
        x.comp (Ext.mk₀ (toRestrictQuotient (J ^ n) Y)) (add_zero i)) ∧
      (∀ i n (y : En i (n + 1)), extQuotientToBase (J ^ n) X Y i (transition i n y) =
        (extQuotientToBase (J ^ (n + 1)) X Y i y).comp
          (Ext.mk₀ (restrictQuotientFactor (Ideal.pow_le_pow_right n.le_succ) Y)) (add_zero i)) ∧
      (∀ i n, (comparison i n).comp (I ^ n • (⊤ : Submodule A (E i))).mkQ = reduction i n) ∧
      ∀ i,
        let Qsys : Functor ℕᵒᵖ (ModuleCat.{max uA uB uM uN} A) :=
          Functor.ofOpSequence
            (X := fun n => ModuleCat.of A (E i ⧸ I ^ n • (⊤ : Submodule A (E i))))
            (fun n => ModuleCat.ofHom (Submodule.factorPowSucc I (E i) n))
        let Esys : Functor ℕᵒᵖ (ModuleCat.{max uA uB uM uN} A) :=
          Functor.ofOpSequence
            (X := fun n => ModuleCat.of A (En i n))
            (fun n => ModuleCat.ofHom (transition i n))
        ∃ e : limit Qsys ≅ limit Esys,
          ∀ n, e.hom ≫ limit.π Esys (op n) =
            limit.π Qsys (op n) ≫ ModuleCat.ofHom (comparison i n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.102, Tag 0EGT](https://stacks.math.columbia.edu/tag/0EGT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
