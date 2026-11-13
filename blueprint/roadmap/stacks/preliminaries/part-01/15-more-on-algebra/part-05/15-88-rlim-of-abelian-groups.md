---
declaration: section
origin: cited
lean: Rlim.lim_hasRightDerivedFunctor_and_computations, Rlim.lim_hasRightDerivedFunctor, Rlim.exists_sixTerm_exact_sequence_lim_rightDerived_one, Rlim.comparisonHomologyLimit_isIso_of_isZero_rightDerivedLim, Rlim.Pro.exists_map_lim_and_cokernel_delta, Rlim.Hom.hom_into_isDerivedLimit_shortExact, Rlim.Pro.nonempty_iso_of_isDerivedLimit_of_pro_isomorphism, Rlim.Hom.shortExact_map_from_isHomotopyColimit
statement: formalized
proof: formalized
---

# 15.88 Rlim of abelian groups

Section 15.88 of the Stacks Project, [Tag 07KV](https://stacks.math.columbia.edu/tag/07KV). 17 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07KW, a lemma

[Tag 07KW](https://stacks.math.columbia.edu/tag/07KW) in the Stacks Project.

**`Rlim.lim_hasRightDerivedFunctor_and_computations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean, line 1769](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean#L1769).

> **Stacks 07KW.** The inverse-limit functor on inverse systems of abelian groups has a right
> derived functor on the unbounded derived category. Higher derived limits vanish above degree one;
> the derived limit of a system is represented by the two-term product complex with differential
> `(x_n) ↦ (x_n - f_{n+1}(x_{n+1}))`; Mittag--Leffler systems have vanishing first derived limit;
> every complex has a quasi-isomorphic complex of right-acyclic terms; and on such a complex the
> derived limit is represented by the termwise inverse-limit complex. Its shift structure and
> natural degree-zero comparison give an exact functor on the derived categories. The ordinary
> limit is the kernel of the product differential, its first derived limit is the cokernel, and
> the latter identification holds for any right-derived functor.

```lean
public theorem lim_hasRightDerivedFunctor_and_computations :
    let F : Rlim.InvSystemAb.{u} ⥤ Ab.{u} := lim
    let P := Rlim.product.{u}
    let δ := Rlim.delta.{u}
    ∃ (RF : DerivedCategory Rlim.InvSystemAb.{u} ⥤ DerivedCategory Ab.{u})
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α (HomotopyCategory.quasiIso Rlim.InvSystemAb.{u} (ComplexShape.up
        ℤ)) ∧
      (∀ (A : Rlim.InvSystemAb.{u}) (p : ℤ), 1 < p →
        IsZero ((DerivedCategory.homologyFunctor Ab.{u} p).obj
          (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A)))) ∧
      (∀ A : Rlim.InvSystemAb.{u}, ∃ (K : CochainComplex Ab.{u} ℤ)
          (e₀ : K.X 0 ≅ P A) (e₁ : K.X 1 ≅ P A),
        (∀ i : ℤ, i ≠ 0 → i ≠ 1 → IsZero (K.X i)) ∧
        e₀.inv ≫ K.d 0 1 ≫ e₁.hom = δ A ∧
        Nonempty (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A) ≅
          DerivedCategory.Q.obj K)) ∧
      (∀ A : Rlim.InvSystemAb.{u}, (A ⋙ forget Ab).IsMittagLeffler →
        IsZero ((DerivedCategory.homologyFunctor Ab.{u} 1).obj
          (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A)))) ∧
      (∀ K : CochainComplex Rlim.InvSystemAb.{u} ℤ,
        ∃ (L : CochainComplex Rlim.InvSystemAb.{u} ℤ) (f : K ⟶ L) (_ : QuasiIso f),
          ∀ p : ℤ, IsZero ((DerivedCategory.homologyFunctor Ab.{u} 1).obj
            (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj (L.X p))))) ∧
      (∀ K : CochainComplex Rlim.InvSystemAb.{u} ℤ,
        (∀ p : ℤ, IsZero ((DerivedCategory.homologyFunctor Ab.{u} 1).obj
          (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj (K.X p))))) →
        Nonempty (RF.obj (DerivedCategory.Q.obj K) ≅
          DerivedCategory.Q.obj ((F.mapHomologicalComplex (ComplexShape.up ℤ)).obj K))) ∧
      (∀ A : Rlim.InvSystemAb.{u},
        ∃ e : limit A ≅ kernel (δ A),
          ∀ n : ℕ, e.hom ≫ kernel.ι (δ A) ≫
            Pi.π (fun n : ℕ ↦ A.obj (Opposite.op n)) n =
              limit.π A (Opposite.op n)) ∧
      (∀ A : Rlim.InvSystemAb.{u},
        Nonempty (((DerivedCategory.homologyFunctor Ab.{u} 1).obj
          (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A))) ≅
            cokernel (δ A))) ∧
      (∀ A : Rlim.InvSystemAb.{u},
        IsZero ((DerivedCategory.homologyFunctor Ab.{u} 1).obj
          (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A))) →
        ∃ w : Rlim.limitToProduct A ≫ δ A = 0,
          (ShortComplex.mk (Rlim.limitToProduct A) (δ A) w).ShortExact) ∧
      (∀ (RF' : DerivedCategory Rlim.InvSystemAb.{u} ⥤ DerivedCategory Ab.{u})
        (α' : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
          DerivedCategory.Qh ⋙ RF'),
        RF'.IsRightDerivedFunctor α'
          (HomotopyCategory.quasiIso Rlim.InvSystemAb.{u} (ComplexShape.up ℤ)) →
        ∀ A : Rlim.InvSystemAb.{u},
          Nonempty (((DerivedCategory.homologyFunctor Ab.{u} 1).obj
            (RF'.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A))) ≅
              cokernel (δ A))) ∧
      ∃ (commShift : RF.CommShift ℤ),
        letI : RF.CommShift ℤ := commShift
        NatTrans.CommShift α ℤ ∧ RF.IsTriangulated ∧
          Nonempty (F ≅ DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0 ⋙ RF ⋙
            DerivedCategory.homologyFunctor Ab.{u} 0)
```

## Tag 08U4, an equation

[Tag 08U4](https://stacks.math.columbia.edu/tag/08U4) in the Stacks Project.

**`Rlim.lim_hasRightDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean, line 1979](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean#L1979).

> **Stacks 08U4.** The inverse-limit functor on inverse systems of abelian groups has a
> right derived functor from `D(Ab(N))` to `D(Ab)`.

```lean
public theorem lim_hasRightDerivedFunctor :
    let F : Rlim.InvSystemAb ⥤ Ab.{0} := lim
    ∃ (RF : DerivedCategory Rlim.InvSystemAb ⥤ DerivedCategory Ab.{0})
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α
        (HomotopyCategory.quasiIso Rlim.InvSystemAb (ComplexShape.up ℤ))
```

## Tag 0H31, a lemma

[Tag 0H31](https://stacks.math.columbia.edu/tag/0H31) in the Stacks Project.

**`Rlim.exists_sixTerm_exact_sequence_lim_rightDerived_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean, line 2023](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean#L2023).

> **Stacks 0H31.** A short exact sequence of inverse systems of abelian groups induces
> the exact sequence
> `0 ⟶ lim A ⟶ lim B ⟶ lim C ⟶ R¹lim A ⟶ R¹lim B ⟶ R¹lim C ⟶ 0`.
> The maps other than the connecting morphism are the functorial maps of `lim` and `R¹lim`.
> The connecting morphism is canonically obtained from the distinguished triangle of the short
> exact sequence and is natural in morphisms of short exact sequences.

```lean
public theorem exists_sixTerm_exact_sequence_lim_rightDerived_one
    {S : ShortComplex Rlim.InvSystemAb.{u}} (hS : S.ShortExact) :
    let F : Rlim.InvSystemAb.{u} ⥤ Ab.{u} := lim
    ∃ (RF : DerivedCategory Rlim.InvSystemAb.{u} ⥤ DerivedCategory Ab.{u})
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF) (commShift : RF.CommShift ℤ),
      letI : RF.CommShift ℤ := commShift
      RF.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso Rlim.InvSystemAb.{u} (ComplexShape.up ℤ)) ∧
        RF.IsTriangulated ∧
        let R (n : ℤ) : Rlim.InvSystemAb.{u} ⥤ Ab.{u} :=
          DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0 ⋙ RF ⋙
            DerivedCategory.homologyFunctor Ab.{u} n
        ∃ e : F ≅ R 0,
          let δ : ∀ {T : ShortComplex Rlim.InvSystemAb.{u}}, T.ShortExact →
              (F.obj T.X₃ ⟶ (R 1).obj T.X₁) := fun {T} (hT : T.ShortExact) ↦ by
            change F.obj T.X₃ ⟶
              (DerivedCategory.homologyFunctor Ab.{u} 1).obj
                (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj T.X₁))
            exact e.hom.app T.X₃ ≫
              DerivedCategory.HomologySequence.δ
                (RF.mapTriangle.obj hT.singleTriangle) 0 1 rfl
          (ComposableArrows.mk₅ (F.map S.f) (F.map S.g) (δ hS)
              ((R 1).map S.f) ((R 1).map S.g)).Exact ∧
            Mono (F.map S.f) ∧ Epi ((R 1).map S.g) ∧
            ∀ {T₁ T₂ : ShortComplex Rlim.InvSystemAb.{u}}
              (h₁ : T₁.ShortExact) (h₂ : T₂.ShortExact) (f : T₁ ⟶ T₂),
              δ h₁ ≫ (R 1).map f.τ₁ = F.map f.τ₃ ≫ δ h₂
```

## Tag 0918, a lemma

[Tag 0918](https://stacks.math.columbia.edu/tag/0918) in the Stacks Project.

**`Rlim.comparisonHomologyLimit_isIso_of_isZero_rightDerivedLim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean, line 2387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Rlim.lean#L2387).

> **Stacks 0918.** Let
> `A⁻² ⟶ A⁻¹ ⟶ A⁰ ⟶ A¹` be an inverse system of four-term complexes of
> abelian groups. If `R¹ lim` vanishes on `A⁻²`, on `A⁻¹`, and on the inverse system of
> degree `-1` cohomologies, then the canonical morphism from the degree-zero cohomology of the
> termwise inverse limit to the inverse limit of the degree-zero cohomologies is an isomorphism.

```lean
public theorem comparisonHomologyLimit_isIso_of_isZero_rightDerivedLim
    (A_neg2 A_neg1 A_0 A_1 : Rlim.InvSystemAb)
    (d_neg2 : A_neg2 ⟶ A_neg1) (d_neg1 : A_neg1 ⟶ A_0) (d_0 : A_0 ⟶ A_1)
    (h_neg1 : ∀ i, d_neg2.app i ≫ d_neg1.app i = 0)
    (h_0 : ∀ i, d_neg1.app i ≫ d_0.app i = 0)
    (RF : DerivedCategory Rlim.InvSystemAb ⥤ DerivedCategory Ab.{0})
    (α : (lim : Rlim.InvSystemAb ⥤ Ab.{0}).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    (hRF : RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso Rlim.InvSystemAb (ComplexShape.up ℤ)))
    (hA_neg2 : IsZero ((DerivedCategory.homologyFunctor Ab.{0} 1).obj
      (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb 0).obj A_neg2))))
    (hA_neg1 : IsZero ((DerivedCategory.homologyFunctor Ab.{0} 1).obj
      (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb 0).obj A_neg1))))
    (hH_neg1 : IsZero ((DerivedCategory.homologyFunctor Ab.{0} 1).obj
      (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb 0).obj
        (homologyInvSystem d_neg2 d_neg1 h_neg1))))) :
    IsIso (comparisonHomologyLimit d_neg1 d_0 h_0)
```

## Tag 0H9K, a lemma

[Tag 0H9K](https://stacks.math.columbia.edu/tag/0H9K) in the Stacks Project.

**`Rlim.Pro.exists_map_lim_and_cokernel_delta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/LimAndRlimOne.lean, line 657](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/LimAndRlimOne.lean#L657).

> **Stacks 0H9K.** Morphisms of pro-systems of abelian groups induce maps on inverse limits
> and first derived inverse limits. The maps are functorial in the pro-morphism, and both are
> isomorphisms when the pro-morphism is an isomorphism.

```lean
public theorem exists_map_lim_and_cokernel_delta :
    let Rlim.InvSystemAb := ℕᵒᵖ ⥤ Ab.{w}
    let proYoneda (A : Rlim.InvSystemAb) : Ab.{w} ⥤ Type w := colimit (A.op ⋙ coyoneda)
    let P (A : Rlim.InvSystemAb) : Ab.{w} := ∏ᶜ fun n : ℕ ↦ A.obj (op n)
    let shift (A : Rlim.InvSystemAb) : P A ⟶ P A := Pi.lift fun n ↦
      Pi.π (fun n : ℕ ↦ A.obj (op n)) (n + 1) ≫
        A.map (homOfLE (Nat.le_succ n)).op
    let δ (A : Rlim.InvSystemAb) : P A ⟶ P A := 𝟙 (P A) - shift A
    ∃ (mapLim : ∀ A B : Rlim.InvSystemAb,
          (proYoneda B ⟶ proYoneda A) → (limit A ⟶ limit B))
      (mapR1lim : ∀ A B : Rlim.InvSystemAb,
          (proYoneda B ⟶ proYoneda A) →
            (cokernel (δ A) ⟶ cokernel (δ B))),
      (∀ A : Rlim.InvSystemAb, mapLim A A (𝟙 _) = 𝟙 _) ∧
      (∀ A : Rlim.InvSystemAb, mapR1lim A A (𝟙 _) = 𝟙 _) ∧
      (∀ (A B C : Rlim.InvSystemAb) (φ : proYoneda B ⟶ proYoneda A)
          (ψ : proYoneda C ⟶ proYoneda B),
        mapLim A C (ψ ≫ φ) = mapLim A B φ ≫ mapLim B C ψ) ∧
      (∀ (A B C : Rlim.InvSystemAb) (φ : proYoneda B ⟶ proYoneda A)
          (ψ : proYoneda C ⟶ proYoneda B),
        mapR1lim A C (ψ ≫ φ) = mapR1lim A B φ ≫ mapR1lim B C ψ) ∧
      (∀ (A B : Rlim.InvSystemAb) (φ : proYoneda B ⟶ proYoneda A),
        IsIso φ → IsIso (mapLim A B φ) ∧ IsIso (mapR1lim A B φ)) ∧
      (∀ (A B : Rlim.InvSystemAb) (r : SequentialRep A B),
        Rlim.delta A ≫ r.productSecond = r.productFirst ≫ Rlim.delta B) ∧
      (∀ (A : Rlim.InvSystemAb),
        (SequentialRep.id A).productFirst = 𝟙 _ ∧
        (SequentialRep.id A).productSecond = 𝟙 _) ∧
      (∀ (A B C : Rlim.InvSystemAb) (r : SequentialRep A B) (s : SequentialRep B C),
        (r.comp s).productFirst = r.productFirst ≫ s.productFirst ∧
        (r.comp s).productSecond = r.productSecond ≫ s.productSecond) ∧
      (∀ (A B : Rlim.InvSystemAb) (r s : SequentialRep A B),
        r.Refines s → r.mapLim = s.mapLim ∧
          r.productSecond ≫ cokernel.π (Rlim.delta B) =
            s.productSecond ≫ cokernel.π (Rlim.delta B)) ∧
      (∀ (A B : Rlim.InvSystemAb) (φ : proYoneda B ⟶ proYoneda A),
        ∃ r : SequentialRep A B, r.Represents φ) ∧
      (∀ (A B : Rlim.InvSystemAb) (φ : proYoneda B ⟶ proYoneda A)
        (r : SequentialRep A B), r.Represents φ →
        ∃ hδ : Rlim.delta A ≫ r.productSecond =
            r.productFirst ≫ Rlim.delta B,
          mapLim A B φ = r.mapLim ∧
          mapR1lim A B φ = r.mapR1lim hδ ∧
          Rlim.limitToProduct A ≫ r.productFirst =
            mapLim A B φ ≫ Rlim.limitToProduct B ∧
          cokernel.π (Rlim.delta A) ≫ mapR1lim A B φ =
            r.productSecond ≫ cokernel.π (Rlim.delta B)) ∧
      (∀ (A B : Rlim.InvSystemAb) (a : InverseSequence.ProIso A B),
        ∃ (φ : proYoneda B ⟶ proYoneda A),
          proIsoRepresents a φ ∧ IsIso φ ∧
          IsIso (mapLim A B φ) ∧ IsIso (mapR1lim A B φ)) ∧
      (∀ {D : Type u} [Category.{w} D] [HasZeroObject D] [HasShift D ℤ]
          [Preadditive D] [∀ n : ℤ, (shiftFunctor D n).Additive]
          [Pretriangulated D]
          (F G : ℕᵒᵖ ⥤ D)
          [HasProduct fun n : ℕ => F.obj (op n)]
          [HasProduct fun n : ℕ => G.obj (op n)] (L : D)
          (f₁ f₂ : Rlim.Hom.systemProduct F ⟶ Rlim.Hom.systemProduct G)
          (φ₀ : proYoneda (Rlim.Hom.homSystem L G) ⟶
            proYoneda (Rlim.Hom.homSystem L F))
          (φ₁ : proYoneda (Rlim.Hom.shiftedHomSystem L G) ⟶
            proYoneda (Rlim.Hom.shiftedHomSystem L F))
          (r₀ : SequentialRep (Rlim.Hom.homSystem L F)
            (Rlim.Hom.homSystem L G))
          (r₁ : SequentialRep (Rlim.Hom.shiftedHomSystem L F)
            (Rlim.Hom.shiftedHomSystem L G)),
          r₀.Represents φ₀ → r₁.Represents φ₁ →
          r₀.productFirst = Rlim.Hom.homProductMap L F G f₁ →
          r₁.productFirst = Rlim.Hom.shiftedHomProductMap L F G f₁ →
          r₁.productSecond = Rlim.Hom.shiftedHomProductMap L F G f₂ →
          ∃ hδ : Rlim.delta (Rlim.Hom.shiftedHomSystem L F) ≫
              Rlim.Hom.shiftedHomProductMap L F G f₂ =
            Rlim.Hom.shiftedHomProductMap L F G f₁ ≫
              Rlim.delta (Rlim.Hom.shiftedHomSystem L G),
            Rlim.limitToProduct (Rlim.Hom.homSystem L F) ≫
                Rlim.Hom.homProductMap L F G f₁ =
              mapLim _ _ φ₀ ≫
                Rlim.limitToProduct (Rlim.Hom.homSystem L G) ∧
            mapR1lim _ _ φ₁ =
              cokernel.map (Rlim.delta (Rlim.Hom.shiftedHomSystem L F))
                (Rlim.delta (Rlim.Hom.shiftedHomSystem L G))
                (Rlim.Hom.shiftedHomProductMap L F G f₁)
                (Rlim.Hom.shiftedHomProductMap L F G f₂) hδ)
```

## Tag 0919, a lemma

[Tag 0919](https://stacks.math.columbia.edu/tag/0919) in the Stacks Project.

**`Rlim.Hom.hom_into_isDerivedLimit_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimHom.lean, line 422](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimHom.lean#L422).

> **Stacks 0919.** If `K` is a derived limit of an inverse system `F` in a triangulated
> category, then for every object `L` there is a short exact sequence
> `0 ⟶ R¹ lim Hom(L, Fₙ[-1]) ⟶ Hom(L, K) ⟶ lim Hom(L, Fₙ) ⟶ 0`.
>
> Here `R¹ lim` is the cokernel of the `1 - shift` endomorphism of the product of the shifted
> Hom-groups. The arrows are characterized by the connecting map and the triangle inclusion.
> For a morphism of defining triangles, the resulting Milnor sequences form a commutative diagram
> with the induced maps on the cokernel and inverse limit.

```lean
public theorem hom_into_isDerivedLimit_shortExact
    {D : Type u} [Category.{v} D] [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D]
    (F : ℕᵒᵖ ⥤ D) [HasProduct fun n : ℕ => F.obj (op n)] (K L : D)
    (hK : Pretriangulated.IsDerivedLimit F K) :
    ∃ (t : DerivedLimitTriangle F K) (S : MilnorSequence L F K t),
      ∀ (G : ℕᵒᵖ ⥤ D) [HasProduct fun n : ℕ => G.obj (op n)] (M : D)
        (tG : DerivedLimitTriangle G M) (a : t.triangle ⟶ tG.triangle)
        (b : limit (homSystem L F) ⟶ limit (homSystem L G))
        (_hb : Rlim.limitToProduct (homSystem L F) ≫ homProductMap L F G a.hom₂ =
          b ≫ Rlim.limitToProduct (homSystem L G)),
        ∃ (SG : MilnorSequence L G M tG)
          (hδ : Rlim.delta (shiftedHomSystem L F) ≫
              shiftedHomProductMap L F G a.hom₃ =
            shiftedHomProductMap L F G a.hom₂ ≫ Rlim.delta (shiftedHomSystem L G)),
          (cokernel.map (Rlim.delta (shiftedHomSystem L F))
              (Rlim.delta (shiftedHomSystem L G))
              (shiftedHomProductMap L F G a.hom₂)
              (shiftedHomProductMap L F G a.hom₃) hδ) ≫ SG.inclusion =
            S.inclusion ≫ (preadditiveCoyoneda.obj (op L)).map a.hom₁ ∧
          S.projection ≫ b =
            (preadditiveCoyoneda.obj (op L)).map a.hom₁ ≫ SG.projection
```

## Tag 0H9L, a lemma

[Tag 0H9L](https://stacks.math.columbia.edu/tag/0H9L) in the Stacks Project.

**`Rlim.Pro.nonempty_iso_of_isDerivedLimit_of_pro_isomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/DerivedLimit.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/DerivedLimit.lean#L251).

> **Stacks 0H9L.** Derived limits of pro-isomorphic inverse systems in a pretriangulated
> category are non-canonically isomorphic.

```lean
public theorem nonempty_iso_of_isDerivedLimit_of_pro_isomorphism
    {D : Type u} [Category.{v} D] [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D]
    (F G : CategoryTheory.Functor ℕᵒᵖ D) [HasProduct fun n : ℕ => F.obj (op n)]
    [HasProduct fun n : ℕ => G.obj (op n)] (K M : D)
    (hK : Pretriangulated.IsDerivedLimit F K) (hM : Pretriangulated.IsDerivedLimit G M)
    (a : InverseSequence.ProIso F G) : Nonempty (K ≅ M)
```

## Tag 0CQX, a lemma

[Tag 0CQX](https://stacks.math.columbia.edu/tag/0CQX) in the Stacks Project.

**`Rlim.Hom.shortExact_map_from_isHomotopyColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimHom.lean, line 693](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimHom.lean#L693).

> **Stacks 0CQX.** Let `F : ℕ ⥤ D` be a system in a pretriangulated category and let `K` be a
> derived colimit of `F`. For every `L` there is a short exact sequence
> `0 → R¹ lim Hom(Fₙ, L[-1]) → Hom(K, L) → lim Hom(Fₙ, L) → 0` coming from a defining triangle
> `∐ Fₙ ⟶ ∐ Fₙ ⟶ K ⟶ (∐ Fₙ)[1]` of `K`, with second map `j` and third map `c`: the second arrow is
> restriction along the coprojections `ιₙ ≫ j : Fₙ ⟶ K`, and the first arrow sends the class of
> the family `(ιₙ ≫ g)ₙ` of a map `g : ∐ Fₙ ⟶ L[-1]` to `c ≫ g[1]`, the image of `g` under the
> connecting morphism of the triangle. See `shortExact_map_from_homotopyColimit_triangle` for the
> same statement for any chosen defining triangle.
>
> Here `R¹ lim` is written as the cokernel of `1 - shift` on the product of the inverse system
> `Hom(Fₙ, L[-1])`, using the description of derived inverse limits from Tag 07KW.

```lean
public theorem shortExact_map_from_isHomotopyColimit
    {D : Type u} [Category.{v} D] [Preadditive D] [HasZeroObject D] [HasShift D ℤ]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D]
    (F : ℕ ⥤ D) [HasCoproduct F.obj] (K L : D) (hK : IsHomotopyColimit F K) :
    let A₀ : ℕᵒᵖ ⥤ AddCommGrpCat.{v} := F.op ⋙ preadditiveYoneda.obj L
    let A₁ : ℕᵒᵖ ⥤ AddCommGrpCat.{v} := F.op ⋙ preadditiveYoneda.obj (L⟦(-1 : ℤ)⟧)
    let P₁ : AddCommGrpCat.{v} := ∏ᶜ fun n : ℕ ↦ A₁.obj (Opposite.op n)
    let shift₁ : P₁ ⟶ P₁ := Pi.lift fun n ↦
      Pi.π (fun n : ℕ ↦ A₁.obj (Opposite.op n)) (n + 1) ≫
        A₁.map (homOfLE (Nat.le_succ n)).op
    let δ₁ : P₁ ⟶ P₁ := 𝟙 P₁ - shift₁
    let H : AddCommGrpCat.{v} := (preadditiveYoneda.obj L).obj (Opposite.op K)
    ∃ (j : ∐ F.obj ⟶ K) (c : K ⟶ (∐ F.obj)⟦(1 : ℤ)⟧),
      Triangle.mk (Sigma.desc fun n ↦ Sigma.ι F.obj n -
        F.map (homOfLE (Nat.le_succ n)) ≫ Sigma.ι F.obj (n + 1)) j c ∈ distTriang D ∧
      ∃ (i : cokernel δ₁ ⟶ H) (r : H ⟶ limit A₀) (z : i ≫ r = 0),
        (ShortComplex.mk i r z).ShortExact ∧
        (∀ (f : K ⟶ L) (n : ℕ),
          limit.π A₀ (Opposite.op n) (r f) = Sigma.ι F.obj n ≫ j ≫ f) ∧
        ∀ (g : ∐ F.obj ⟶ L⟦(-1 : ℤ)⟧) (x : P₁),
          (∀ n : ℕ, Pi.π (fun n : ℕ ↦ A₁.obj (Opposite.op n)) n x = Sigma.ι F.obj n ≫ g) →
            i (cokernel.π δ₁ x) =
              c ≫ g⟦(1 : ℤ)⟧' ≫
                (shiftFunctorCompIsoId D (-1 : ℤ) 1 (by norm_num)).hom.app L
```

## Tag 091A, a remark

[Tag 091A](https://stacks.math.columbia.edu/tag/091A) in the Stacks Project.

**`Rlim.ChaoticSite.diagramLimitAndRightDerivedIsoSiteCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimSiteCohomology.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimSiteCohomology.lean#L76).

> On the chaotic site on a small category, abelian sheaves are diagrams of abelian groups on
> its opposite category. Under the canonical equivalence, global sections are naturally isomorphic
> to the limit functor, and for every `p` the site-cohomology functor is naturally isomorphic to
> `R^p lim`.

```lean
public noncomputable def diagramLimitAndRightDerivedIsoSiteCohomology
    {C : Type u} [SmallCategory C] :
    let J : GrothendieckTopology C := ⊥
    let e := sheafBotEquivalence (C := C) Ab.{u}
    (e.functor ⋙ (lim : (Cᵒᵖ ⥤ Ab.{u}) ⥤ Ab.{u}) ≅
      Stacks.Cohomology.CompositeRightDerived.siteSections J) ×
      (∀ p : ℕ,
        e.functor ⋙ (lim : (Cᵒᵖ ⥤ Ab.{u}) ⥤ Ab.{u}).rightDerived p ≅
          Stacks.Cohomology.CompositeRightDerived.siteCohomology J p)
```

## Tag 07KX, a lemma

[Tag 07KX](https://stacks.math.columbia.edu/tag/07KX) in the Stacks Project.

**`Rlim.lim_hasRightDerivedFunctor_and_isDerivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimTriangle.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimTriangle.lean#L355).

> **Stacks 07KX.** The right-derived inverse-limit functor on inverse systems of abelian groups
> is, on every object, a derived limit of the associated inverse system in `D(Ab)`. Equivalently,
> its value fits in the canonical distinguished triangle
> `R lim K ⟶ ∏ Kₙ ⟶ ∏ Kₙ ⟶ (R lim K)⟦1⟧`, where the middle map is
> `1 - shift`.

```lean
public theorem lim_hasRightDerivedFunctor_and_isDerivedLimit :
    let F : Rlim.InvSystemAb.{u} ⥤ Ab.{u} := lim
    ∃ (RF : DerivedCategory Rlim.InvSystemAb.{u} ⥤ DerivedCategory Ab.{u})
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α
        (HomotopyCategory.quasiIso Rlim.InvSystemAb.{u} (ComplexShape.up ℤ)) ∧
      ∀ K : DerivedCategory Rlim.InvSystemAb.{u},
        ∃ _ : HasProduct fun n : ℕ => (derivedEvaluationSystem K).obj (Opposite.op n),
          Pretriangulated.IsDerivedLimit (derivedEvaluationSystem K) (RF.obj K)
```

## Tag 07KY, a lemma

[Tag 07KY](https://stacks.math.columbia.edu/tag/07KY) in the Stacks Project.

**`DerivedCategory.isDerivedLimit_homology_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/MilnorShortExact.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/MilnorShortExact.lean#L273).

> The canonical Milnor short exact sequence of a derived limit. The inclusion descends the
> connecting morphism through the cokernel of `1 - shift` in degree `r - 1`, and the projection to
> the inverse limit is characterized by the maps to the degree-`r` cohomologies of the terms.
>
> This is the direct long-exact-sequence argument of Stacks 07KY and 07KZ. It applies to every
> `IsDerivedLimit`, independently of any choice of right-derived inverse-limit functor.

```lean
public theorem isDerivedLimit_homology_shortExact
    (F : ℕᵒᵖ ⥤ DerivedCategory A) [HasProduct fun n : ℕ => F.obj ⟨n⟩]
    (K : DerivedCategory A) (hK : IsDerivedLimit F K) :
    let X : ℕ → DerivedCategory A := fun n ↦ F.obj (Opposite.op n)
    let d : (∏ᶜ X) ⟶ ∏ᶜ X := Pi.lift fun n : ℕ ↦
      Pi.π X n - Pi.π X (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
    ∃ (a : K ⟶ ∏ᶜ X) (b : (∏ᶜ X) ⟶ K⟦(1 : ℤ)⟧),
      let T := Pretriangulated.Triangle.mk a d b
      T ∈ distTriang (DerivedCategory A) ∧
        ∀ r : ℤ,
          let H := DerivedCategory.homologyFunctor A r
          let H₁ := DerivedCategory.homologyFunctor A (r - 1)
          let homologySystem : ℕᵒᵖ ⥤ A := F ⋙ H
          let shiftedHomologySystem : ℕᵒᵖ ⥤ A := F ⋙ H₁
          let P : A :=
            ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)
          let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
            Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)) n -
              Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (Opposite.op n)) (n + 1) ≫
                shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
          ∃ (e : H₁.obj (∏ᶜ X) ≅ P)
            (i : cokernel δ ⟶ H.obj K) (q : H.obj K ⟶ limit homologySystem)
            (w : i ≫ q = 0),
            e.hom = piComparison H₁ X ∧
              cokernel.π δ ≫ i = e.inv ≫
                DerivedCategory.HomologySequence.δ T (r - 1) r ∧
              (∀ n : ℕ, q ≫ limit.π homologySystem (Opposite.op n) =
                H.map a ≫ H.map (Pi.π X n)) ∧
              (ShortComplex.mk i q w).ShortExact
```

## Tag 0CQ9, a lemma

[Tag 0CQ9](https://stacks.math.columbia.edu/tag/0CQ9) in the Stacks Project.

**`Stacks.InverseSystem.AbelianGroupDerivedLift.exists_lift_of_inverseSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Ab.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Ab.lean#L393).

> **Stacks Tag 0CQ9 / Lemma 15.88.11.**
> Every inverse system `K : Nᵒᵖ ⥤ D(Ab)` of objects of the derived category `D(Ab)`
> lifts to an object `M` of `D(Ab(N))`: there exist an object `M` of `D(Ab(N))` and,
> for every index `n`, an isomorphism `ψ n : ev_n(M) ≅ K_n` in `D(Ab)`, such that for
> every morphism `f : a ⟶ b` of `Nᵒᵖ` the square
> `ev_a(M) → ev_b(M) → K_b` and `ev_a(M) → K_a → K_b` commutes, i.e. the isomorphisms
> `ψ` are compatible with the transition maps (the induced transition maps `evTrans f`
> of `M` on the source, the given transition maps `K.map f` of the system on the
> target).

```lean
theorem exists_lift_of_inverseSystem (K : ℕᵒᵖ ⥤ DerivedCategory Ab.{u}) :
    ∃ (M : DerivedCategory AbN.{u}) (ψ : ∀ n, (evD n).obj M ≅ K.obj n),
      ∀ ⦃a b : ℕᵒᵖ⦄ (f : a ⟶ b),
        (evTrans f).app M ≫ (ψ b).hom = (ψ a).hom ≫ K.map f
```

## Tag 08U5, a remark

[Tag 08U5](https://stacks.math.columbia.edu/tag/08U5) in the Stacks Project.

**`Rlim.derivedLimit_iso_rightDerivedLimit_and_homology_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimTriangle.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/RlimTriangle.lean#L511).

> **Stacks 08U5.** Let `E` be an inverse system in `D(Ab)` and let `K` be a derived
> limit of `E`.  The system has a lift to `D(Ab(N))`, and the value on every lift of a
> right-derived inverse-limit functor is isomorphic to `K`.  In particular this value is
> independent, up to isomorphism, of the chosen lift.
>
> For every `p`, the defining product triangle of `K` induces the canonical short exact sequence
> `0 ⟶ R¹ lim H^(p-1)(Eₙ) ⟶ H^p(K) ⟶ lim H^p(Eₙ) ⟶ 0`.  The two maps are
> specified by the connecting morphism and the map from `K` to the product, respectively.

```lean
public theorem derivedLimit_iso_rightDerivedLimit_and_homology_shortExact
(E : Functor ℕᵒᵖ (DerivedCategory Ab.{0})) :
    let F : Functor Rlim.InvSystemAb Ab.{0} := lim
    ∃ (RF : Functor (DerivedCategory Rlim.InvSystemAb) (DerivedCategory Ab.{0}))
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso Rlim.InvSystemAb (ComplexShape.up ℤ)) ∧
        (∃ K : DerivedCategory Ab.{0}, Pretriangulated.IsDerivedLimit E K) ∧
        (∃ (M : DerivedCategory Stacks.InverseSystem.AbelianGroupDerivedLift.AbN)
          (ψ : ∀ n, (Stacks.InverseSystem.AbelianGroupDerivedLift.evD n).obj M ≅ E.obj n),
          ∀ ⦃a b : ℕᵒᵖ⦄ (f : a ⟶ b),
            (Stacks.InverseSystem.AbelianGroupDerivedLift.evTrans f).app M ≫ (ψ b).hom = (ψ a).hom ≫
              E.map f) ∧
        ∀ (K : DerivedCategory Ab.{0}), Pretriangulated.IsDerivedLimit E K →
        (∀ (M : DerivedCategory Stacks.InverseSystem.AbelianGroupDerivedLift.AbN)
            (ψ : ∀ n, (Stacks.InverseSystem.AbelianGroupDerivedLift.evD n).obj M ≅ E.obj n),
            (∀ ⦃a b : ℕᵒᵖ⦄ (f : a ⟶ b),
              (Stacks.InverseSystem.AbelianGroupDerivedLift.evTrans f).app M ≫ (ψ b).hom = (ψ a).hom
                ≫ E.map f) →
            Nonempty (K ≅ RF.obj M)) ∧
        let P := ∏ᶜ fun n : ℕ => E.obj (Opposite.op n)
        let d : P ⟶ P := Pi.lift fun n : ℕ =>
          Pi.π (fun n : ℕ => E.obj (Opposite.op n)) n -
            Pi.π (fun n : ℕ => E.obj (Opposite.op n)) (n + 1) ≫
              E.map (homOfLE (Nat.le_succ n)).op
        ∃ (a : K ⟶ P) (b : P ⟶ K⟦(1 : ℤ)⟧),
          Pretriangulated.Triangle.mk a d b ∈ distTriang (DerivedCategory Ab.{0}) ∧
          ∀ p : ℤ,
            let H : ℤ → Rlim.InvSystemAb := fun q =>
              E ⋙ DerivedCategory.homologyFunctor Ab.{0} q
            let HP : ℤ → Ab.{0} := fun q =>
              (DerivedCategory.homologyFunctor Ab.{0} q).obj P
            let PH : ℤ → Ab.{0} := fun q =>
              ∏ᶜ fun n : ℕ => (H q).obj (Opposite.op n)
            let δH : (q : ℤ) → (PH q ⟶ PH q) := fun q => Rlim.delta (H q)
            let R1lim := Rlim.firstDerivedLimit (H (p - 1))
            let HpK := (DerivedCategory.homologyFunctor Ab.{0} p).obj K
            let limHp := lim.obj (H p)
            let T := Pretriangulated.Triangle.mk a d b
            let connecting : HP (p - 1) ⟶ HpK :=
              (DerivedCategory.homologyFunctor Ab.{0} 0).homologySequenceδ
                T (p - 1) p (by omega)
            ∃ (ePrev : HP (p - 1) ≅ PH (p - 1)) (eCurr : HP p ≅ PH p),
              (∀ n : ℕ, ePrev.hom ≫ Pi.π
                  (fun n : ℕ => (H (p - 1)).obj (Opposite.op n)) n =
                (DerivedCategory.homologyFunctor Ab.{0} (p - 1)).map
                  (Pi.π (fun n : ℕ => E.obj (Opposite.op n)) n)) ∧
              (∀ n : ℕ, eCurr.hom ≫ Pi.π
                  (fun n : ℕ => (H p).obj (Opposite.op n)) n =
                (DerivedCategory.homologyFunctor Ab.{0} p).map
                  (Pi.π (fun n : ℕ => E.obj (Opposite.op n)) n)) ∧
              (DerivedCategory.homologyFunctor Ab.{0} (p - 1)).map d ≫ ePrev.hom =
                ePrev.hom ≫ δH (p - 1) ∧
              (DerivedCategory.homologyFunctor Ab.{0} p).map d ≫ eCurr.hom =
                eCurr.hom ≫ δH p ∧
              ∃ (eLim : limHp ≅ kernel (δH p))
                (hConnecting : δH (p - 1) ≫ ePrev.inv ≫ connecting = 0)
                (hKernel : (DerivedCategory.homologyFunctor Ab.{0} p).map a ≫
                  eCurr.hom ≫ δH p = 0),
                (∀ n : ℕ, eLim.hom ≫ kernel.ι (δH p) ≫
                    Pi.π (fun n : ℕ => (H p).obj (Opposite.op n)) n =
                  limit.π (H p) (Opposite.op n)) ∧
                let i : R1lim ⟶ HpK :=
                  cokernel.desc (δH (p - 1)) (ePrev.inv ≫ connecting) hConnecting
                let q : HpK ⟶ limHp :=
                  kernel.lift (δH p)
                    ((DerivedCategory.homologyFunctor Ab.{0} p).map a ≫ eCurr.hom)
                    hKernel ≫ eLim.inv
                ∃ w : i ≫ q = 0, (ShortComplex.mk i q w).ShortExact
```

## Tag 091B, a lemma

[Tag 091B](https://stacks.math.columbia.edu/tag/091B) in the Stacks Project.

**`Rlim.Pro.lim_hasRightDerivedFunctor_and_maps_proIsomorphisms_to_isomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/RightDerivedLimit.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/RightDerivedLimit.lean#L477).

> **Stacks 091B.** The right-derived inverse-limit functor sends a morphism of derived inverse
> systems to an isomorphism if the induced morphism between their associated systems in `D(Ab)` is
> an isomorphism of pro-objects. Such a pro-isomorphism induces pro-isomorphisms between the
> cohomology inverse systems in every degree; the displayed degreewise criterion then gives the
> result.

```lean
public theorem lim_hasRightDerivedFunctor_and_maps_proIsomorphisms_to_isomorphisms :
    let F : Functor Rlim.InvSystemAb.{v} Ab.{v} := lim
    ∃ (RF : Functor (DerivedCategory Rlim.InvSystemAb.{v}) (DerivedCategory Ab.{v}))
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso Rlim.InvSystemAb.{v} (ComplexShape.up ℤ)) ∧
        MapsHomologyProIsomorphismsToIsomorphisms RF ∧
        ∀ {E D : DerivedCategory Rlim.InvSystemAb.{v}} (f : E ⟶ D),
          IsProIsomorphismOnDerivedEvaluationSystems f →
            (∀ p : ℤ,
              let H := DerivedCategory.homologyFunctor Rlim.InvSystemAb.{v} p
              IsIso (colim.map
                (Functor.whiskerRight (NatTrans.op (H.map f)) coyoneda))) ∧
            IsIso (RF.map f)
```

## Tag 0CQA, a lemma

[Tag 0CQA](https://stacks.math.columbia.edu/tag/0CQA) in the Stacks Project.

**`Rlim.isMittagLeffler_iff_isZero_rightDerivedLim_one_and_countable_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/MittagLeffler.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/MittagLeffler.lean#L322).

> **Stacks 0CQA (Emmanouil).** An inverse system of abelian groups is Mittag--Leffler if and
> only if the first derived inverse limit vanishes for it and for the countable direct sum of
> copies of it.

```lean
public theorem isMittagLeffler_iff_isZero_rightDerivedLim_one_and_countable_coproduct
    (A : Rlim.InvSystemAb.{v}) :
    let F : Rlim.InvSystemAb.{v} ⥤ Ab.{v} := lim
    ∀ (RF : DerivedCategory Rlim.InvSystemAb.{v} ⥤ DerivedCategory Ab.{v})
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso Rlim.InvSystemAb.{v} (ComplexShape.up ℤ)) →
        ((A ⋙ forget Ab).IsMittagLeffler ↔
          (IsZero ((DerivedCategory.homologyFunctor Ab.{v} 1).obj
            (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{v} 0).obj A))) ∧
          IsZero ((DerivedCategory.homologyFunctor Ab.{v} 1).obj
            (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{v} 0).obj
              (∐ fun _ : Discrete ℕ => A))))))
```

## Tag 0CQB, a lemma

[Tag 0CQB](https://stacks.math.columbia.edu/tag/0CQB) in the Stacks Project.

Declarations registered for the tag:

- [`isMittagLeffler_of_shortExact`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/InverseLimit.lean#L174), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Homology/DerivedCategory/InverseSystem/MittagLeffler.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/MittagLeffler.lean#L52) (StacksFrontier): “In a short exact sequence of inverse systems of abelian groups indexed by the natural numbers, if the outer two systems are Mittag-Leffler, then the middle system is Mittag-Leffler.”.

## Tag 091C, a lemma

[Tag 091C](https://stacks.math.columbia.edu/tag/091C) in the Stacks Project.

**`Rlim.Pro.isProZero_iff_isZero_lim_and_rightDerivedLim_one_and_countable_coproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/RightDerivedLimit.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ProIsomorphism/RightDerivedLimit.lean#L613).

> **Stacks 091C.** An inverse system of abelian groups is zero as a pro-object if and only if
> its inverse limit and first derived inverse limit vanish, and the same two vanishings hold for
> the countable direct sum of copies of the system.

```lean
public theorem isProZero_iff_isZero_lim_and_rightDerivedLim_one_and_countable_coproduct
    (A : Rlim.InvSystemAb.{u}) :
    let F : Rlim.InvSystemAb.{u} ⥤ Ab.{u} := lim
    ∀ (RF : DerivedCategory Rlim.InvSystemAb.{u} ⥤ DerivedCategory Ab.{u})
      (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
        DerivedCategory.Qh ⋙ RF),
      RF.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso Rlim.InvSystemAb.{u} (ComplexShape.up ℤ)) →
        ((∀ n : ℕ, ∃ (m : ℕ) (h : n ≤ m), A.map (homOfLE h).op = 0) ↔
          IsZero (limit A) ∧
          IsZero ((DerivedCategory.homologyFunctor Ab.{u} 1).obj
            (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj A))) ∧
          IsZero (limit (∐ fun _ : Discrete ℕ => A)) ∧
          IsZero ((DerivedCategory.homologyFunctor Ab.{u} 1).obj
            (RF.obj ((DerivedCategory.singleFunctor Rlim.InvSystemAb.{u} 0).obj
              (∐ fun _ : Discrete ℕ => A)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.88, Tag 07KV](https://stacks.math.columbia.edu/tag/07KV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
