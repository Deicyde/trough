---
declaration: section
origin: cited
lean: StacksDraft.DerivedInverseLimit.derivedLimit_isPseudoCoherent_and_baseChange_iso, StacksDraft.DerivedInverseLimit.derivedLimit_isPseudoCoherent_isDerivedComplete_and_baseChange_iso, StacksDraft.DerivedInverseLimit.derivedLimit_isPerfect_and_baseChange_iso, StacksDraft.DerivedInverseLimit.derivedLimit_isPerfect_isDerivedComplete_and_baseChange_iso, Stacks.DerivedLimit.AdicSystem.isDerivedComplete_and_reduction_isIso_of_isDerivedLimit, Stacks.InverseSystem.AdicCompletionCohomology.isIso_adicCompletionToLimitHomology, Stacks.PseudoCoherent.AdicCompletion.isIso_adicCompletionToLimitDerivedReduction
statement: formalized
proof: formalized
---

# 15.99 Taking limits of complexes

Section 15.99 of the Stacks Project, [Tag 09B6](https://stacks.math.columbia.edu/tag/09B6). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CQF, a lemma

[Tag 0CQF](https://stacks.math.columbia.edu/tag/0CQF) in the Stacks Project.

**`StacksDraft.DerivedInverseLimit.derivedLimit_isPseudoCoherent_and_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/PseudoCoherent/DerivedLimit.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/PseudoCoherent/DerivedLimit.lean#L411).

> **Stacks 0CQF.** Suppose a tower of rings has surjective transition maps with locally
> nilpotent kernels, and its derived module objects are preserved by the base-change maps induced
> by their transitions. If all terms are pseudo-coherent, or one term is pseudo-coherent and all
> subsequent kernels are nilpotent, then every derived inverse limit is pseudo-coherent and its
> canonical base-change map to each term is an isomorphism.
>
> The limit ring is the vertex of the arbitrary limit cone `c`. The distinguished triangle has
> the prescribed product difference map for the transitions restricted to that vertex.

```lean
public theorem derivedLimit_isPseudoCoherent_and_baseChange_iso
    (A : ℕᵒᵖ ⥤ CommRingCat.{u}) (c : Cone A) (hc : IsLimit c)
    (Kₙ : ∀ n : ℕ, DerivedCategory (ModuleCat.{max u v} (A.obj (op n))))
    (φ : ∀ n : ℕ, Kₙ (n + 1) ⟶
      (ModuleCat.restrictScalars (A.map (homOfLE (Nat.le_succ n)).op).hom).mapDerivedCategory.obj
        (Kₙ n))
    (hSurjective : ∀ n : ℕ,
      Function.Surjective (A.map (homOfLE (Nat.le_succ n)).op).hom)
    (hLocallyNilpotent : ∀ n : ℕ,
      (RingHom.ker (A.map (homOfLE (Nat.le_succ n)).op).hom).IsLocallyNilpotent)
    (hPseudoCoherent : (∀ n : ℕ, PseudoCoherence.IsPseudoCoherent (Kₙ n)) ∨
      ∃ n₀ : ℕ, PseudoCoherence.IsPseudoCoherent (Kₙ n₀) ∧
        ∀ n : ℕ, n₀ ≤ n →
          IsNilpotent (RingHom.ker (A.map (homOfLE (Nat.le_succ n)).op).hom))
    (hBaseChange : ∀ n : ℕ,
      IsIso (derivedBaseChangeComparison (A.map (homOfLE (Nat.le_succ n)).op).hom (φ n))) :
    let X : ℕ → DerivedCategory (ModuleCat.{max u v} c.pt) := fun n ↦
      (ModuleCat.restrictScalars (c.π.app (op n)).hom).mapDerivedCategory.obj (Kₙ n)
    let t : ∀ n : ℕ, X (n + 1) ⟶ X n := fun n ↦
      (ModuleCat.restrictScalars (c.π.app (op (n + 1))).hom).mapDerivedCategory.map
          (φ n) ≫
        (derivedRestrictScalarsComp (c.π.app (op (n + 1))).hom
          (A.map (homOfLE (Nat.le_succ n)).op).hom (c.π.app (op n)).hom
          (congrArg CommRingCat.Hom.hom (c.w (homOfLE (Nat.le_succ n)).op)).symm).hom.app (Kₙ n)
    ∀ [HasProduct X] (K : DerivedCategory (ModuleCat.{max u v} c.pt))
      (p : K ⟶ ∏ᶜ X) (δ : ∏ᶜ X ⟶ K⟦(1 : ℤ)⟧),
      Pretriangulated.Triangle.mk p
        (Pi.lift fun n : ℕ ↦ Pi.π X n - Pi.π X (n + 1) ≫ t n) δ ∈
          distTriang (DerivedCategory (ModuleCat.{max u v} c.pt)) →
      PseudoCoherence.IsPseudoCoherent K ∧ ∀ n : ℕ,
        IsIso (derivedBaseChangeComparison (c.π.app (op n)).hom (p ≫ Pi.π X n))
```

## Tag 09AV, a lemma

[Tag 09AV](https://stacks.math.columbia.edu/tag/09AV) in the Stacks Project.

**`StacksDraft.DerivedInverseLimit.derivedLimit_isPseudoCoherent_isDerivedComplete_and_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/PseudoCoherent/AdicallyComplete.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/PseudoCoherent/AdicallyComplete.lean#L257).

> **Stacks 09AV.** Let `A` be `I`-adically complete and let `Kₙ n` be a derived object over
> `A ⧸ I ^ (n + 1)`. Suppose `Kₙ 0` is pseudo-coherent and every transition map becomes an
> isomorphism after derived base change. Then a derived inverse limit `K` over `A` is
> pseudo-coherent and derived complete, and its canonical derived base-change map to every
> `Kₙ n` is an isomorphism.

```lean
public theorem derivedLimit_isPseudoCoherent_isDerivedComplete_and_baseChange_iso
    (A : Type u) [CommRing A] (I : Ideal A) [IsAdicComplete I A]
    (Kₙ : ∀ n : ℕ, DerivedCategory (ModuleCat.{max u v} (A ⧸ I ^ (n + 1))))
    (φ : ∀ n : ℕ, Kₙ (n + 1) ⟶
      (ModuleCat.restrictScalars
        (Ideal.Quotient.factorPow I (Nat.le_succ (n + 1)))).mapDerivedCategory.obj (Kₙ n))
    (hPseudoCoherent : PseudoCoherence.IsPseudoCoherent (Kₙ 0))
    (hBaseChange : ∀ n : ℕ, IsIso (derivedBaseChangeComparison
      (Ideal.Quotient.factorPow I (Nat.le_succ (n + 1))) (φ n))) :
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat.{max u v} A) :=
      moduleCat_hasExactLimitsOfShape_discrete A ℕ
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{max u v} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let q : ∀ n : ℕ, A ⧸ I ^ (n + 2) →+* A ⧸ I ^ (n + 1) := fun n ↦
      Ideal.Quotient.factorPow I (Nat.le_succ (n + 1))
    let a : ∀ n : ℕ, A →+* A ⧸ I ^ (n + 1) := fun n ↦
      Ideal.Quotient.mk (I ^ (n + 1))
    let X : ℕ → DerivedCategory (ModuleCat.{max u v} A) := fun n ↦
      (ModuleCat.restrictScalars (a n)).mapDerivedCategory.obj (Kₙ n)
    let t : ∀ n : ℕ, X (n + 1) ⟶ X n := fun n ↦
      (ModuleCat.restrictScalars (a (n + 1))).mapDerivedCategory.map (φ n) ≫
        (derivedRestrictScalarsComp (a (n + 1)) (q n) (a n)
          (by ext x; rfl)).hom.app (Kₙ n)
    ∀ (K : DerivedCategory (ModuleCat.{max u v} A))
      (p : K ⟶ ∏ᶜ X) (δ : ∏ᶜ X ⟶ K⟦(1 : ℤ)⟧),
      Triangle.mk p (Pi.lift fun n : ℕ ↦ Pi.π X n - Pi.π X (n + 1) ≫ t n) δ ∈
          distTriang (DerivedCategory (ModuleCat.{max u v} A)) →
        PseudoCoherence.IsPseudoCoherent K ∧ _root_.IsDerivedComplete I K ∧
          ∀ n : ℕ, IsIso (derivedBaseChangeComparison
            (a n) (p ≫ Pi.π X n))
```

## Tag 0CQG, a lemma

[Tag 0CQG](https://stacks.math.columbia.edu/tag/0CQG) in the Stacks Project.

**`StacksDraft.DerivedInverseLimit.derivedLimit_isPerfect_and_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/Perfect.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/Perfect.lean#L269).

> Suppose a tower of rings has surjective transition maps with locally nilpotent kernels, and
> its derived module objects are preserved by the base-change maps induced by their transitions.
> If all terms are perfect, or one term is perfect and every subsequent transition kernel is
> nilpotent, then every derived inverse limit over the vertex of the limit cone `c` is perfect and
> its canonical base-change map to each term is an isomorphism.

```lean
public theorem derivedLimit_isPerfect_and_baseChange_iso
    (A : ℕᵒᵖ ⥤ CommRingCat.{u}) (c : Cone A) (hc : IsLimit c)
    (Kₙ : ∀ n : ℕ, DerivedCategory (ModuleCat.{max u v} (A.obj (op n))))
    (φ : ∀ n : ℕ, Kₙ (n + 1) ⟶
      (ModuleCat.restrictScalars (A.map (homOfLE (Nat.le_succ n)).op).hom).mapDerivedCategory.obj
        (Kₙ n))
    (hSurjective : ∀ n : ℕ,
      Function.Surjective (A.map (homOfLE (Nat.le_succ n)).op).hom)
    (hLocallyNilpotent : ∀ n : ℕ,
      (RingHom.ker (A.map (homOfLE (Nat.le_succ n)).op).hom).IsLocallyNilpotent)
    (hPerfect : (∀ n : ℕ, StacksDraft.Perfect.IsPerfect (Kₙ n)) ∨
      ∃ n₀ : ℕ, StacksDraft.Perfect.IsPerfect (Kₙ n₀) ∧
        ∀ n : ℕ, n₀ ≤ n →
          IsNilpotent (RingHom.ker (A.map (homOfLE (Nat.le_succ n)).op).hom))
    (hBaseChange : ∀ n : ℕ,
      IsIso (StacksDraft.DerivedInverseLimit.derivedBaseChangeComparison
        (A.map (homOfLE (Nat.le_succ n)).op).hom (φ n))) :
    let X : ℕ → DerivedCategory (ModuleCat.{max u v} c.pt) := fun n ↦
      (ModuleCat.restrictScalars (c.π.app (op n)).hom).mapDerivedCategory.obj (Kₙ n)
    let t : ∀ n : ℕ, X (n + 1) ⟶ X n := fun n ↦
      (ModuleCat.restrictScalars (c.π.app (op (n + 1))).hom).mapDerivedCategory.map
          (φ n) ≫
        (StacksDraft.DerivedInverseLimit.derivedRestrictScalarsComp (c.π.app (op (n + 1))).hom
          (A.map (homOfLE (Nat.le_succ n)).op).hom (c.π.app (op n)).hom
          (congrArg CommRingCat.Hom.hom (c.w (homOfLE (Nat.le_succ n)).op)).symm).hom.app (Kₙ n)
    ∀ [HasProduct X] (K : DerivedCategory (ModuleCat.{max u v} c.pt))
      (p : K ⟶ ∏ᶜ X) (δ : ∏ᶜ X ⟶ K⟦(1 : ℤ)⟧),
      Pretriangulated.Triangle.mk p
        (Pi.lift fun n : ℕ ↦ Pi.π X n - Pi.π X (n + 1) ≫ t n) δ ∈
          distTriang (DerivedCategory (ModuleCat.{max u v} c.pt)) →
      StacksDraft.Perfect.IsPerfect K ∧ ∀ n : ℕ,
        IsIso (StacksDraft.DerivedInverseLimit.derivedBaseChangeComparison
          (c.π.app (op n)).hom (p ≫ Pi.π X n))
```

## Tag 09AW, a lemma

[Tag 09AW](https://stacks.math.columbia.edu/tag/09AW) in the Stacks Project.

**`StacksDraft.DerivedInverseLimit.derivedLimit_isPerfect_isDerivedComplete_and_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/Perfect.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/Perfect.lean#L339).

> Let `A` be `I`-adically complete and let `Kₙ n` be a derived object over
> `A ⧸ I ^ (n + 1)`. Suppose `Kₙ 0` is perfect and every transition map becomes an isomorphism
> after derived base change. Then a derived inverse limit `K` over `A` is perfect and derived
> complete, and its canonical derived base-change map to every `Kₙ n` is an isomorphism.

```lean
public theorem derivedLimit_isPerfect_isDerivedComplete_and_baseChange_iso
    (A : Type u) [CommRing A] (I : Ideal A) [IsAdicComplete I A]
    (Kₙ : ∀ n : ℕ, DerivedCategory (ModuleCat.{max u v} (A ⧸ I ^ (n + 1))))
    (φ : ∀ n : ℕ, Kₙ (n + 1) ⟶
      (ModuleCat.restrictScalars
        (Ideal.Quotient.factorPow I (Nat.le_succ (n + 1)))).mapDerivedCategory.obj (Kₙ n))
    (hPerfect : StacksDraft.Perfect.IsPerfect (Kₙ 0))
    (hBaseChange : ∀ n : ℕ, IsIso (StacksDraft.DerivedInverseLimit.derivedBaseChangeComparison
      (Ideal.Quotient.factorPow I (Nat.le_succ (n + 1))) (φ n))) :
    letI : HasExactLimitsOfShape (Discrete ℕ) (ModuleCat.{max u v} A) :=
      moduleCat_hasExactLimitsOfShape_discrete.{max u v} A ℕ
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{max u v} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    let q : ∀ n : ℕ, A ⧸ I ^ (n + 2) →+* A ⧸ I ^ (n + 1) := fun n ↦
      Ideal.Quotient.factorPow I (Nat.le_succ (n + 1))
    let a : ∀ n : ℕ, A →+* A ⧸ I ^ (n + 1) := fun n ↦
      Ideal.Quotient.mk (I ^ (n + 1))
    let X : ℕ → DerivedCategory (ModuleCat.{max u v} A) := fun n ↦
      (ModuleCat.restrictScalars (a n)).mapDerivedCategory.obj (Kₙ n)
    let t : ∀ n : ℕ, X (n + 1) ⟶ X n := fun n ↦
      (ModuleCat.restrictScalars (a (n + 1))).mapDerivedCategory.map (φ n) ≫
        (StacksDraft.DerivedInverseLimit.derivedRestrictScalarsComp (a (n + 1)) (q n) (a n)
          (by ext x; rfl)).hom.app (Kₙ n)
    ∀ (K : DerivedCategory (ModuleCat.{max u v} A))
      (p : K ⟶ ∏ᶜ X) (δ : ∏ᶜ X ⟶ K⟦(1 : ℤ)⟧),
      Triangle.mk p (Pi.lift fun n : ℕ ↦ Pi.π X n - Pi.π X (n + 1) ≫ t n) δ ∈
          distTriang (DerivedCategory (ModuleCat.{max u v} A)) →
        StacksDraft.Perfect.IsPerfect K ∧ _root_.IsDerivedComplete I K ∧
          ∀ n : ℕ, IsIso (StacksDraft.DerivedInverseLimit.derivedBaseChangeComparison
            (a n) (p ≫ Pi.π X n))
```

## Tag 09AU, a lemma

[Tag 09AU](https://stacks.math.columbia.edu/tag/09AU) in the Stacks Project.

**`Stacks.DerivedLimit.AdicSystem.isDerivedComplete_and_reduction_isIso_of_isDerivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/AdicSystem.lean, line 1349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/AdicSystem.lean#L1349).

> **Stacks 09AU.** Let `A` be Noetherian and `I` an ideal. Suppose that `F` is an inverse
> system in `D(A)` whose `n`-th member is the restriction of an object `Kq n` of
> `D(A ⧸ I ^ (n + 1))`. If `Kq 0` is bounded above and every transition induces an isomorphism
> after derived reduction to the preceding quotient, then a derived limit `K` is bounded above
> and derived `I`-complete. Moreover, the canonical map from the derived reduction of `K` to
> `Kq n` is an isomorphism for every `n`.

```lean
public theorem isDerivedComplete_and_reduction_isIso_of_isDerivedLimit
    {A : Type u} [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (F : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{max u v} A))
    (Kq : ∀ n : ℕ, DerivedCategory (ModuleCat.{max u v} (A ⧸ I ^ (n + 1))))
    (e : ∀ n : ℕ, F.obj (.op n) ≅
      (ModuleCat.restrictScalars.{max u v} (Ideal.Quotient.mk (I ^ (n + 1)))).mapDerivedCategory.obj
        (Kq n))
    (adj : ∀ n : ℕ,
      (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, v}
          (Ideal.Quotient.mk (I ^ (n + 1)))).functor ⊣
        (ModuleCat.restrictScalars.{max u v}
          (Ideal.Quotient.mk (I ^ (n + 1)))).mapDerivedCategory)
    (hbounded : DerivedCategory.TStructure.t.minus (Kq 0))
    (t : ∀ n : ℕ, Kq (n + 1) ⟶
      (ModuleCat.restrictScalars.{max u v} (quotientTransition I n)).mapDerivedCategory.obj (Kq n))
    (htransition : ∀ n : ℕ,
      F.map (homOfLE (Nat.le_succ n)).op ≫ (e n).hom =
        (e (n + 1)).hom ≫
          (ModuleCat.restrictScalars.{max u v}
            (Ideal.Quotient.mk (I ^ (n + 2)))).mapDerivedCategory.map
            (t n) ≫ (restrictScalarsTransitionIso I n).hom.app (Kq n))
    (hcompat : ∀ n : ℕ,
      IsIso (StacksDraft.DerivedInverseLimit.derivedBaseChangeComparison.{u, v, u}
        (quotientTransition I n) (t n))) :
    letI : HasProductsOfShape ℕ (DerivedCategory (ModuleCat.{max u v} A)) :=
      Stacks.DerivedProducts.hasProductsOfShape_derivedCategory
    ∀ (K : DerivedCategory (ModuleCat.{max u v} A))
      (p : K ⟶ ∏ᶜ fun n : ℕ => F.obj (.op n))
      (δ : (∏ᶜ fun n : ℕ => F.obj (.op n)) ⟶ K⟦(1 : ℤ)⟧),
      Triangle.mk p
          (Pi.lift fun n : ℕ => Pi.π (fun n : ℕ => F.obj (.op n)) n -
            Pi.π (fun n : ℕ => F.obj (.op n)) (n + 1) ≫
              F.map (homOfLE (Nat.le_succ n)).op) δ ∈
            distTriang (DerivedCategory (ModuleCat.{max u v} A)) →
        DerivedCategory.TStructure.t.minus K ∧
          _root_.IsDerivedComplete I K ∧
          ∀ n : ℕ, IsIso (((adj n).homEquiv _ _).symm
            (p ≫ Pi.π (fun n : ℕ => F.obj (.op n)) n ≫ (e n).hom))
```

## Tag 0EGS, a lemma

[Tag 0EGS](https://stacks.math.columbia.edu/tag/0EGS) in the Stacks Project.

**`Stacks.InverseSystem.AdicCompletionCohomology.isIso_adicCompletionToLimitHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/AdicCompletionComparison.lean, line 490](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Limits/AdicCompletionComparison.lean#L490). The attribute's comment: “The equality `lim Hⁱ(K)/IⁿHⁱ(K) = lim Hⁱ(Kₙ)` is the statement that the canonical map induced by the reduction maps `K → Kₙ` is an isomorphism; positive powers of `I` are indexed by `n + 1`.”.

> **Stacks 0EGS (Kollár--Kovács).** Let `I` be an ideal of a Noetherian ring `A` and
> `K ∈ D(A)`, and set `Kₙ = K ⊗ᴸ[A] A/Iⁿ⁺¹`. Suppose that every cohomology module `Hⁱ(K)` is
> finite and that, in every degree, the system `Hⁱ(Kₙ)` is Mittag--Leffler. Then for every `i` the
> canonical map `lim Hⁱ(K)/Iⁿ⁺¹Hⁱ(K) ⟶ lim Hⁱ(Kₙ)`, induced by the reduction maps `K ⟶ Kₙ`, is an
> isomorphism.

```lean
public theorem isIso_adicCompletionToLimitHomology
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (K : DerivedCategory (ModuleCat.{u} A))
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    (hK : ∀ i : ℤ,
      Module.Finite A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K))
    (hML : ∀ i : ℤ,
      (((idealPowerQuotientSystem I ⋙ T.tensor.obj K) ⋙
          DerivedCategory.homologyFunctor (ModuleCat.{u} A) i) ⋙
        forget (ModuleCat.{u} A)).IsMittagLeffler) :
    ∀ i : ℤ, IsIso (adicCompletionToLimitHomology I T K i)
```

**`Stacks.PseudoCoherent.AdicCompletion.isIso_adicCompletionToLimitDerivedReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/DerivedReductionCompletion.lean, line 473](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/DerivedReductionCompletion.lean#L473).

> **Stacks 0EGS (Kollár--Kovács), canonical form.** Let `I` be an ideal of a Noetherian ring
> `A` and `K ∈ D(A)`, and set `Kₙ = K ⊗ᴸ[A] A/Iⁿ⁺¹`. Suppose that every cohomology module `Hⁱ(K)` is
> finite and that, in every degree, the inverse system `Hⁱ(Kₙ)` is Mittag--Leffler. Then for every
> `i` the canonical map `lim Hⁱ(K)/IⁿHⁱ(K) ⟶ lim Hⁱ(Kₙ)`, induced by the reduction maps
> `K ⟶ Kₙ` (`adicCompletionToLimitDerivedReduction`), is an isomorphism.

```lean
theorem isIso_adicCompletionToLimitDerivedReduction
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (K : DerivedCategory (ModuleCat.{u} A))
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    (hK : ∀ i : ℤ,
      Module.Finite A ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) i).obj K))
    (hML : ∀ i : ℤ,
      (((NoetherianAdicCompletion.idealPowerQuotientSystem I ⋙ T.tensor.obj K) ⋙
          DerivedCategory.homologyFunctor (ModuleCat.{u} A) i) ⋙
        forget (ModuleCat.{u} A)).IsMittagLeffler) :
    ∀ i : ℤ, IsIso (adicCompletionToLimitDerivedReduction I T K i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.99, Tag 09B6](https://stacks.math.columbia.edu/tag/09B6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
