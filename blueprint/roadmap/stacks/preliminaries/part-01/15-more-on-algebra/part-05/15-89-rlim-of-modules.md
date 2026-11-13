---
declaration: section
origin: cited
lean: ModuleInverseLimit.inverseLimit_hasRightDerivedFunctor_and_computations, ModuleInverseLimitGlobalSections.derivedInverseLimitIsoDerivedGlobalSections, ModuleRightDerivedLimit.rightDerivedInverseLimit_isDerivedLimit, ModuleRightDerivedLimit.inverseLimit_hasRightDerivedFunctor_and_homology_shortExact, Stacks.InverseSystem.ModuleDerivedLift.exists_derivedObject_of_inverseSystem, ModuleDerivedLimitTriangle.derivedLimit_iso_and_homology_shortExact, ModuleSystemRepresentative.exists_representative_with_surjective_transition_maps, ModuleSystemKFlat.exists_representative_with_kFlat_components
statement: formalized
proof: formalized
---

# 15.89 Rlim of modules

Section 15.89 of the Stacks Project, [Tag 0CQC](https://stacks.math.columbia.edu/tag/0CQC). 12 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 091D, a lemma

[Tag 091D](https://stacks.math.columbia.edu/tag/091D) in the Stacks Project.

**`ModuleInverseLimit.inverseLimit_hasRightDerivedFunctor_and_computations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleInverseLimitFunctor/TermwiseComputation.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleInverseLimitFunctor/TermwiseComputation.lean#L426).

> **Stacks 091D.** For modules over an inverse system of rings, the inverse-limit functor has
> a right derived functor on the unbounded derived category. Higher derived limits vanish above
> degree one; the derived limit of a module system is represented by the two-term product complex
> with differential `(x_n) ↦ (x_n - f_{n+1}(x_{n+1}))`; Mittag--Leffler systems are right
> acyclic; every complex has a quasi-isomorphic complex of right-acyclic terms; and a termwise
> right-acyclic complex computes its derived limit by taking inverse limits termwise. For each
> right-acyclic system, the canonical limit cone and product differential form a natural short
> exact sequence.

```lean
public theorem inverseLimit_hasRightDerivedFunctor_and_computations
    (rings : ℕᵒᵖ ⥤ RingCat.{u}) :
    let baseRing := limit rings
    let functor : PresheafOfModules.{v} rings ⥤ ModuleCat.{v} baseRing := inverseLimit rings
    let productFamily (system : PresheafOfModules.{v} rings) : ModuleCat.{v} baseRing :=
      ∏ᶜ fun n : ℕ ↦ (moduleDiagram rings system).obj (Opposite.op n)
    let shift (system : PresheafOfModules.{v} rings) : productFamily system ⟶ productFamily system
      := Pi.lift fun n ↦
      Pi.π (fun n : ℕ ↦ (moduleDiagram rings system).obj (Opposite.op n)) (n + 1) ≫
        (moduleDiagram rings system).map (homOfLE (Nat.le_succ n)).op
    let delta (system : PresheafOfModules.{v} rings) : productFamily system ⟶ productFamily system
      := 𝟙 (productFamily system) - shift system
    ∃ (additive : functor.Additive),
      letI := additive
      ∃ (derivedFunctor : DerivedCategory (PresheafOfModules.{v} rings) ⥤
            DerivedCategory (ModuleCat.{v} baseRing))
          (unit : functor.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
            DerivedCategory.Qh ⋙ derivedFunctor),
          derivedFunctor.IsRightDerivedFunctor unit
              (HomotopyCategory.quasiIso (PresheafOfModules.{v} rings) (ComplexShape.up ℤ)) ∧
          (∀ (system : PresheafOfModules.{v} rings) (degree : ℤ), 1 < degree →
            IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} baseRing) degree).obj
              (derivedFunctor.obj ((DerivedCategory.singleFunctor (PresheafOfModules.{v} rings)
                0).obj system)))) ∧
          (∀ system : PresheafOfModules.{v} rings, ∃ (complex : CochainComplex (ModuleCat.{v}
            baseRing) ℤ)
              (zeroIso : complex.X 0 ≅ productFamily system) (oneIso : complex.X 1 ≅ productFamily
                system),
            (∀ index : ℤ, index ≠ 0 → index ≠ 1 → IsZero (complex.X index)) ∧
            zeroIso.inv ≫ complex.d 0 1 ≫ oneIso.hom = delta system ∧
            Nonempty (derivedFunctor.obj
              ((DerivedCategory.singleFunctor (PresheafOfModules.{v} rings) 0).obj system) ≅
                DerivedCategory.Q.obj complex)) ∧
          (∀ system : PresheafOfModules.{v} rings, (system.presheaf ⋙ forget Ab).IsMittagLeffler →
            IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} baseRing) 1).obj
              (derivedFunctor.obj ((DerivedCategory.singleFunctor (PresheafOfModules.{v} rings)
                0).obj system)))) ∧
          (∀ system : PresheafOfModules.{v} rings,
            IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} baseRing) 1).obj
              (derivedFunctor.obj ((DerivedCategory.singleFunctor (PresheafOfModules.{v} rings)
                0).obj system))) →
            ∃ zeroComposition : inverseLimitToProduct rings system ≫ delta system = 0,
              (ShortComplex.mk (inverseLimitToProduct rings system) (delta system)
                zeroComposition).ShortExact) ∧
          (∀ {system targetSystem : PresheafOfModules.{v} rings} (morphism : system ⟶ targetSystem),
            inverseLimitToProduct rings system ≫ productMap rings morphism =
              functor.map morphism ≫ inverseLimitToProduct rings targetSystem ∧
            delta system ≫ productMap rings morphism = productMap rings morphism ≫ delta
              targetSystem) ∧
          (∀ complex : CochainComplex (PresheafOfModules.{v} rings) ℤ,
            ∃ (replacement : CochainComplex (PresheafOfModules.{v} rings) ℤ) (morphism : complex ⟶
              replacement) (_ : QuasiIso morphism),
              ∀ degree : ℤ, IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} baseRing) 1).obj
                (derivedFunctor.obj
                  ((DerivedCategory.singleFunctor (PresheafOfModules.{v} rings) 0).obj
                    (replacement.X degree))))) ∧
          ∀ complex : CochainComplex (PresheafOfModules.{v} rings) ℤ,
            (∀ degree : ℤ, IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} baseRing) 1).obj
              (derivedFunctor.obj
                ((DerivedCategory.singleFunctor (PresheafOfModules.{v} rings) 0).obj (complex.X
                  degree))))) →
            Nonempty (derivedFunctor.obj (DerivedCategory.Q.obj complex) ≅
              DerivedCategory.Q.obj
                ((functor.mapHomologicalComplex (ComplexShape.up ℤ)).obj complex))
```

## Tag 091E, a remark

[Tag 091E](https://stacks.math.columbia.edu/tag/091E) in the Stacks Project.

**`ModuleInverseLimitGlobalSections.derivedInverseLimitIsoDerivedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleInverseLimitGlobalSections.lean, line 667](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleInverseLimitGlobalSections.lean#L667).

> On the site `ℕ` with its bottom topology, module sheaves over an inverse system of rings are
> compatible inverse systems of modules. Under this equivalence, the right derived inverse-limit
> functor is canonically the right-derived global-sections functor. After forgetting the module
> structure, it is canonically the right-derived global-sections functor of the underlying sheaf of
> abelian groups. The two comparison isomorphisms commute with the respective derived-functor
> structure transformations.

```lean
public theorem derivedInverseLimitIsoDerivedGlobalSections (A : ℕᵒᵖ ⥤ RingCat.{u}) :
    let R := inverseSystemRingSheaf A
    let e : SheafOfModules.{v} R ≌ PresheafOfModules.{v} A := moduleSheafBotEquivalence A
    let B : RingCat.{u} := limit A
    let limMod : PresheafOfModules.{v} A ⥤ ModuleCat.{v} B := ModuleInverseLimit.inverseLimit A
    let Γ : SheafOfModules.{v} R ⥤ ModuleCat.{v} B := e.functor ⋙ limMod
    let ΓAb : Sheaf (⊥ : GrothendieckTopology ℕ) Ab.{v} ⥤ Ab.{v} :=
      sheafToPresheaf (⊥ : GrothendieckTopology ℕ) Ab.{v} ⋙ lim
    ∃ (hE : e.functor.Additive),
      letI := hE
      ∃ (hLim : limMod.Additive),
      letI := hLim
      ∃ (Rlim : DerivedCategory (PresheafOfModules.{v} A) ⥤
            DerivedCategory (ModuleCat.{v} B))
          (α : limMod.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
            DerivedCategory.Qh ⋙ Rlim)
          (hΓ : Γ.Additive),
        letI := hΓ
        ∃ (hΓAb : ΓAb.Additive),
        letI := hΓAb
        ∃ (hToSheafAdd : (SheafOfModules.toSheaf.{v} R).Additive),
        letI := hToSheafAdd
        ∃ (hForgetFiniteColimits :
            PreservesFiniteColimits (forget₂ (ModuleCat.{v} B) Ab.{v})),
        letI := hForgetFiniteColimits
        ∃ (RΓ : DerivedCategory (SheafOfModules.{v} R) ⥤
              DerivedCategory (ModuleCat.{v} B))
            (β : Γ.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
              DerivedCategory.Qh ⋙ RΓ)
          (RΓAb : DerivedCategory (Sheaf (⊥ : GrothendieckTopology ℕ) Ab.{v}) ⥤
              DerivedCategory Ab.{v})
            (γ : ΓAb.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
              DerivedCategory.Qh ⋙ RΓAb)
            (hToSheaf : PreservesFiniteColimits (SheafOfModules.toSheaf.{v} R)),
          letI := hToSheaf
          Rlim.IsRightDerivedFunctor α
              (HomotopyCategory.quasiIso (PresheafOfModules.{v} A) (ComplexShape.up ℤ)) ∧
          RΓ.IsRightDerivedFunctor β
              (HomotopyCategory.quasiIso (SheafOfModules.{v} R) (ComplexShape.up ℤ)) ∧
          RΓAb.IsRightDerivedFunctor γ
              (HomotopyCategory.quasiIso
                (Sheaf (⊥ : GrothendieckTopology ℕ) Ab.{v}) (ComplexShape.up ℤ)) ∧
          ∃ (η : e.functor.mapDerivedCategory ⋙ Rlim ≅ RΓ)
              (θ : Γ ⋙ forget₂ (ModuleCat.{v} B) Ab.{v} ≅
                SheafOfModules.toSheaf.{v} R ⋙ ΓAb)
              (ζ : RΓ ⋙ (forget₂ (ModuleCat.{v} B) Ab.{v}).mapDerivedCategory ≅
                (SheafOfModules.toSheaf.{v} R).mapDerivedCategory ⋙ RΓAb),
            (∀ K,
              β.app K ≫ η.inv.app (DerivedCategory.Qh.obj K) =
                DerivedCategory.Qh.map
                    ((Functor.mapHomotopyCategoryCompIso (Iso.refl Γ)
                      (ComplexShape.up ℤ)).inv.app K) ≫
                  α.app ((e.functor.mapHomotopyCategory (ComplexShape.up ℤ)).obj K) ≫
                  Rlim.map (e.functor.mapDerivedCategoryFactorsh.inv.app K)) ∧
            ∀ K,
              (forget₂ (ModuleCat.{v} B) Ab.{v}).mapDerivedCategoryFactorsh.inv.app
                    ((Γ.mapHomotopyCategory (ComplexShape.up ℤ)).obj K) ≫
                  (forget₂ (ModuleCat.{v} B) Ab.{v}).mapDerivedCategory.map (β.app K) ≫
                  ζ.hom.app (DerivedCategory.Qh.obj K) =
                DerivedCategory.Qh.map
                    ((NatTrans.mapHomotopyCategory θ.hom (ComplexShape.up ℤ)).app K) ≫
                  γ.app (((SheafOfModules.toSheaf.{v} R).mapHomotopyCategory
                    (ComplexShape.up ℤ)).obj K) ≫
                  RΓAb.map
                    ((SheafOfModules.toSheaf.{v} R).mapDerivedCategoryFactorsh.inv.app K)
```

## Tag 0CQD, a lemma

[Tag 0CQD](https://stacks.math.columbia.edu/tag/0CQD) in the Stacks Project.

**`ModuleRightDerivedLimit.rightDerivedInverseLimit_isDerivedLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRightDerivedLimit.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRightDerivedLimit.lean#L406).

> **Stacks 0CQD.** The right-derived inverse-limit functor for compatible modules over an
> inverse system of rings is, on every object, a derived limit of the associated inverse system in
> the derived category of modules over the inverse-limit ring. Equivalently, its value fits in the
> canonical distinguished triangle
> `R lim K ⟶ ∏ Kₙ ⟶ ∏ Kₙ ⟶ (R lim K)⟦1⟧`, whose middle map is `1 - shift`.

```lean
public theorem rightDerivedInverseLimit_isDerivedLimit
    (A : ℕᵒᵖ ⥤ RingCat.{u}) :
    let B := limit A
    let F : PresheafOfModules.{v} A ⥤ ModuleCat.{v} B := ModuleInverseLimit.inverseLimit A
    ∀ (hF : F.Additive),
      letI := hF
      ∀ (RF : DerivedCategory (PresheafOfModules.{v} A) ⥤
            DerivedCategory (ModuleCat.{v} B))
          (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
            DerivedCategory.Qh ⋙ RF),
        RF.IsRightDerivedFunctor α
            (HomotopyCategory.quasiIso (PresheafOfModules.{v} A) (ComplexShape.up ℤ)) →
        ∀ K : DerivedCategory (PresheafOfModules.{v} A),
          ∃ _ : HasProduct fun n : ℕ => (derivedModuleDiagram A K).obj (Opposite.op n),
            Pretriangulated.IsDerivedLimit (derivedModuleDiagram A K) (RF.obj K)
```

## Tag 0CQE, a lemma

[Tag 0CQE](https://stacks.math.columbia.edu/tag/0CQE) in the Stacks Project.

**`ModuleRightDerivedLimit.inverseLimit_hasRightDerivedFunctor_and_homology_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRightDerivedLimit.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRightDerivedLimit.lean#L582).

> **Stacks 0CQE.** For a complex of compatible modules over an inverse system of rings, the
> long exact cohomology sequence of its canonical derived-limit triangle breaks into short exact
> sequences
> `0 ⟶ R¹ lim H^(p-1)(Kₙ) ⟶ H^p(R lim K) ⟶ lim H^p(Kₙ) ⟶ 0`.
>
> The displayed maps are the cokernel descent of the connecting morphism and the kernel lift of
> the following morphism in the long exact sequence.

```lean
public theorem inverseLimit_hasRightDerivedFunctor_and_homology_shortExact
    (A : ℕᵒᵖ ⥤ RingCat.{u}) :
    let B := limit A
    let F : PresheafOfModules.{v} A ⥤ ModuleCat.{v} B := ModuleInverseLimit.inverseLimit A
    ∃ (hF : F.Additive),
      letI := hF
      ∃ (RF : DerivedCategory (PresheafOfModules.{v} A) ⥤
            DerivedCategory (ModuleCat.{v} B))
          (α : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
            DerivedCategory.Qh ⋙ RF),
        RF.IsRightDerivedFunctor α
            (HomotopyCategory.quasiIso (PresheafOfModules.{v} A) (ComplexShape.up ℤ)) ∧
        ∀ K : DerivedCategory (PresheafOfModules.{v} A),
          ∃ _ : HasProduct fun n : ℕ ↦
              (ModuleRightDerivedLimit.derivedModuleDiagram A K).obj (Opposite.op n),
            let E := ModuleRightDerivedLimit.derivedModuleDiagram A K
            let P := ∏ᶜ fun n : ℕ ↦ E.obj (Opposite.op n)
            let d : P ⟶ P := Pi.lift fun n : ℕ ↦
              Pi.π (fun n : ℕ ↦ E.obj (Opposite.op n)) n -
                Pi.π (fun n : ℕ ↦ E.obj (Opposite.op n)) (n + 1) ≫
                  E.map (homOfLE (Nat.le_succ n)).op
            ∃ (a : RF.obj K ⟶ P) (b : P ⟶ (RF.obj K)⟦(1 : ℤ)⟧),
              Pretriangulated.Triangle.mk a d b ∈
                  distTriang (DerivedCategory (ModuleCat.{v} B)) ∧
              ∀ p : ℤ,
                let H : ℤ → PresheafOfModules.{v} A := fun q ↦
                  (DerivedCategory.homologyFunctor (PresheafOfModules.{v} A) q).obj K
                let EH : ℤ → (ℕᵒᵖ ⥤ ModuleCat.{v} B) := fun q ↦
                  E ⋙ DerivedCategory.homologyFunctor (ModuleCat.{v} B) q
                let MH : ℤ → (ℕᵒᵖ ⥤ ModuleCat.{v} B) := fun q ↦
                  ModuleInverseLimit.moduleDiagram A (H q)
                let HP : ℤ → ModuleCat.{v} B := fun q ↦
                  (DerivedCategory.homologyFunctor (ModuleCat.{v} B) q).obj P
                let PH : ℤ → ModuleCat.{v} B := fun q ↦
                  ∏ᶜ fun n : ℕ ↦ (MH q).obj (Opposite.op n)
                let δH : (q : ℤ) → (PH q ⟶ PH q) := fun q ↦ Pi.lift fun n : ℕ ↦
                  Pi.π (fun n : ℕ ↦ (MH q).obj (Opposite.op n)) n -
                    Pi.π (fun n : ℕ ↦ (MH q).obj (Opposite.op n)) (n + 1) ≫
                      (MH q).map (homOfLE (Nat.le_succ n)).op
                let R1lim := (DerivedCategory.homologyFunctor (ModuleCat.{v} B) 1).obj
                  (RF.obj ((DerivedCategory.singleFunctor (PresheafOfModules.{v} A) 0).obj
                    (H (p - 1))))
                let HpRlim :=
                  (DerivedCategory.homologyFunctor (ModuleCat.{v} B) p).obj (RF.obj K)
                let limHp := F.obj (H p)
                let T := Pretriangulated.Triangle.mk a d b
                let connecting : HP (p - 1) ⟶ HpRlim :=
                  (DerivedCategory.homologyFunctor (ModuleCat.{v} B) 0).homologySequenceδ
                    T (p - 1) p (by omega)
                ∃ (eHPrev : EH (p - 1) ≅ MH (p - 1)) (eHCurr : EH p ≅ MH p)
                    (ePrev : HP (p - 1) ≅ PH (p - 1)) (eCurr : HP p ≅ PH p),
                  (∀ n : ℕ, ePrev.hom ≫
                      Pi.π (fun n : ℕ ↦ (MH (p - 1)).obj (Opposite.op n)) n =
                    (DerivedCategory.homologyFunctor (ModuleCat.{v} B) (p - 1)).map
                        (Pi.π (fun n : ℕ ↦ E.obj (Opposite.op n)) n) ≫
                      eHPrev.hom.app (Opposite.op n)) ∧
                  (∀ n : ℕ, eCurr.hom ≫
                      Pi.π (fun n : ℕ ↦ (MH p).obj (Opposite.op n)) n =
                    (DerivedCategory.homologyFunctor (ModuleCat.{v} B) p).map
                        (Pi.π (fun n : ℕ ↦ E.obj (Opposite.op n)) n) ≫
                      eHCurr.hom.app (Opposite.op n)) ∧
                  (DerivedCategory.homologyFunctor (ModuleCat.{v} B) (p - 1)).map d ≫
                      ePrev.hom = ePrev.hom ≫ δH (p - 1) ∧
                  (DerivedCategory.homologyFunctor (ModuleCat.{v} B) p).map d ≫
                      eCurr.hom = eCurr.hom ≫ δH p ∧
                  ∃ (eR1 : R1lim ≅ cokernel (δH (p - 1)))
                    (eLim : limHp ≅ kernel (δH p))
                    (hConnecting : δH (p - 1) ≫ ePrev.inv ≫ connecting = 0)
                    (hKernel : (DerivedCategory.homologyFunctor (ModuleCat.{v} B) p).map a ≫
                      eCurr.hom ≫ δH p = 0),
                    (∀ n : ℕ, eLim.hom ≫ kernel.ι (δH p) ≫
                        Pi.π (fun n : ℕ ↦ (MH p).obj (Opposite.op n)) n =
                      limit.π (MH p) (Opposite.op n)) ∧
                    let i : R1lim ⟶ HpRlim := eR1.hom ≫
                      cokernel.desc (δH (p - 1)) (ePrev.inv ≫ connecting) hConnecting
                    let q : HpRlim ⟶ limHp :=
                      kernel.lift (δH p)
                        ((DerivedCategory.homologyFunctor (ModuleCat.{v} B) p).map a ≫
                          eCurr.hom)
                        hKernel ≫ eLim.inv
                    ∃ w : i ≫ q = 0, (ShortComplex.mk i q w).ShortExact
```

## Tag 091I, a lemma

[Tag 091I](https://stacks.math.columbia.edu/tag/091I) in the Stacks Project.

**`Stacks.InverseSystem.ModuleDerivedLift.exists_derivedObject_of_inverseSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/Modules.lean, line 1035](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/Modules.lean#L1035).

> **Stacks 091I**.
> Let `(A_n)` be an inverse system of commutative rings with transition maps
> `f n : A_{n+1} → A_n`, let `K n` be objects of `D(A_n)`, and let
> `φ n : K (n+1) ⟶ (Drestr n).obj (K n)` be morphisms in `D(A_{n+1})`. Then there are an object
> `M` of `D(Mod(ℕ, (A_n)))` and isomorphisms `ψ n : (Dcomp n).obj M ≅ K n` in `D(A_n)` such that
> `(transitionNT n).app M ≫ (Drestr n).map (ψ n).hom = (ψ (n+1)).hom ≫ φ n`.

```lean
theorem exists_derivedObject_of_inverseSystem
    (K : ∀ n, DerivedCategory (ModuleCat.{max u v} (A n)))
    (φ : ∀ n, K (n + 1) ⟶ (Drestr A f n).obj (K n)) :
    ∃ (M : DerivedCategory (PresheafOfModules.{max u v} (Rfun A f)))
      (ψ : ∀ n, (Dcomp A f n).obj M ≅ K n),
      ∀ n, (transitionNT A f n).app M ≫ (Drestr A f n).map (ψ n).hom
        = (ψ (n + 1)).hom ≫ φ n
```

## Tag 07KZ, a remark

[Tag 07KZ](https://stacks.math.columbia.edu/tag/07KZ) in the Stacks Project.

**`ModuleDerivedLimitTriangle.derivedLimit_iso_and_homology_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleDerivedLimitTriangle.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleDerivedLimitTriangle.lean#L68).

> **Stacks 07KZ.** Any two derived limits of the same countable inverse system of complexes of
> modules are isomorphic. Moreover, after exhibiting a derived limit by its defining distinguished
> triangle, for every `r : ℤ` there is a canonical short exact sequence
> `0 ⟶ R¹ lim H⁽ʳ⁻¹⁾(Fₙ) ⟶ Hʳ(K) ⟶ lim Hʳ(Fₙ) ⟶ 0`.
>
> Here `R¹ lim` is the cokernel of `1 - shift`. The left map is characterized as the factorization
> of the connecting map of the defining triangle through that cokernel (using the canonical
> comparison between the homology of a product and the product of the homologies), and the right
> map is characterized by all its composites with the limit projections.

```lean
public theorem derivedLimit_iso_and_homology_shortExact
    (R : Type u) [Ring R] [HasDerivedCategory.{w} (ModuleCat.{max v u} R)]
    (F : CategoryTheory.Functor ℕᵒᵖ (DerivedCategory (ModuleCat.{max v u} R)))
    [HasProduct fun n : ℕ => F.obj (op n)] :
    (∀ (K K' : DerivedCategory (ModuleCat.{max v u} R)),
      Pretriangulated.IsDerivedLimit F K →
        Pretriangulated.IsDerivedLimit F K' → Nonempty (K ≅ K')) ∧
      ∀ (K : DerivedCategory (ModuleCat.{max v u} R)),
        Pretriangulated.IsDerivedLimit F K →
          let X : ℕ → DerivedCategory (ModuleCat.{max v u} R) := fun n ↦ F.obj (op n)
          let d : (∏ᶜ X) ⟶ ∏ᶜ X := Pi.lift fun n : ℕ ↦
            Pi.π X n - Pi.π X (n + 1) ≫ F.map (homOfLE (Nat.le_succ n)).op
          ∃ (a : K ⟶ ∏ᶜ X) (b : (∏ᶜ X) ⟶ K⟦(1 : ℤ)⟧),
            let T := Pretriangulated.Triangle.mk a d b
            T ∈ distTriang (DerivedCategory (ModuleCat.{max v u} R)) ∧
              ∀ r : ℤ,
                let H := DerivedCategory.homologyFunctor (ModuleCat.{max v u} R) r
                let H₁ := DerivedCategory.homologyFunctor (ModuleCat.{max v u} R) (r - 1)
                let homologySystem : ℕᵒᵖ ⥤ ModuleCat.{max v u} R := F ⋙ H
                let shiftedHomologySystem : ℕᵒᵖ ⥤ ModuleCat.{max v u} R := F ⋙ H₁
                let P : ModuleCat.{max v u} R :=
                  ∏ᶜ fun n : ℕ ↦ shiftedHomologySystem.obj (op n)
                let δ : P ⟶ P := Pi.lift fun n : ℕ ↦
                  Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) n -
                    Pi.π (fun n : ℕ ↦ shiftedHomologySystem.obj (op n)) (n + 1) ≫
                      shiftedHomologySystem.map (homOfLE (Nat.le_succ n)).op
                ∃ (e : H₁.obj (∏ᶜ X) ≅ P)
                  (i : cokernel δ ⟶ H.obj K) (q : H.obj K ⟶ limit homologySystem)
                  (w : i ≫ q = 0),
                  e.hom = piComparison H₁ X ∧
                    cokernel.π δ ≫ i = e.inv ≫
                      DerivedCategory.HomologySequence.δ T (r - 1) r ∧
                    (∀ n : ℕ, q ≫ limit.π homologySystem (op n) =
                      H.map a ≫ H.map (Pi.π X n)) ∧
                    (ShortComplex.mk i q w).ShortExact
```

## Tag 091F, a lemma

[Tag 091F](https://stacks.math.columbia.edu/tag/091F) in the Stacks Project.

**`ModuleSystemRepresentative.exists_representative_with_surjective_transition_maps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRepresentatives.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRepresentatives.lean#L313).

> **Stacks 091F.** Every object of the derived category of inverse systems of modules over an
> inverse system of rings is represented by a complex whose transition maps are surjective in
> every degree.

```lean
public theorem exists_representative_with_surjective_transition_maps
    {A : ℕᵒᵖ ⥤ RingCat.{u}}
    [HasDerivedCategory.{w} (PresheafOfModules.{v} A)]
    (K : DerivedCategory (PresheafOfModules.{v} A)) :
    ∃ (M : CochainComplex (PresheafOfModules.{v} A) ℤ)
      (_ : DerivedCategory.Q.obj M ≅ K),
      ∀ (n : ℕ) (i : ℤ),
        Function.Surjective
          ((M.X i).map ((homOfLE (Nat.le_succ n)).op))
```

## Tag 091G, a lemma

[Tag 091G](https://stacks.math.columbia.edu/tag/091G) in the Stacks Project.

**`ModuleSystemKFlat.exists_representative_with_kFlat_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimDerived.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimDerived.lean#L138).

> **Stacks 091G.** Every object of the derived category of inverse systems of modules over an
> inverse system of commutative rings has a representative whose complex at every index is
> K-flat.

```lean
public theorem exists_representative_with_kFlat_components
    {A : Functor ℕᵒᵖ CommRingCat.{u}}
    [HasDerivedCategory.{w}
      (PresheafOfModules.{u} (A ⋙ forget₂ CommRingCat RingCat))]
    (K : DerivedCategory
      (PresheafOfModules.{u} (A ⋙ forget₂ CommRingCat RingCat))) :
    ∃ (M : CochainComplex
        (PresheafOfModules.{u} (A ⋙ forget₂ CommRingCat RingCat)) ℤ)
      (_ : DerivedCategory.Q.obj M ≅ K),
      ∀ n : ℕ,
        CochainComplex.KFlat
          (show CochainComplex (ModuleCat (A.obj (op n))) ℤ from
            ((PresheafOfModules.evaluation
              (A ⋙ forget₂ CommRingCat RingCat) (op n)).mapHomologicalComplex
                (ComplexShape.up ℤ)).obj M)
```

## Tag 091H, a lemma

[Tag 091H](https://stacks.math.columbia.edu/tag/091H) in the Stacks Project.

**`ModuleSystemKFlatComparison.derivedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleKFlatComparison/DerivedTensor.lean, line 714](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleKFlatComparison/DerivedTensor.lean#L714).

> **Stacks 091H.** The derived category of compatible module systems over an inverse system of
> commutative rings has a canonical symmetric derived tensor product. A componentwise K-flat
> representative computes the whole system by pointwise total tensor, compatibly with evaluation
> at every index. The bifunctor is exact in each variable.

```lean
public noncomputable def derivedTensorProduct
    (A : Functor ℕᵒᵖ CommRingCat.{u})
    [HasDerivedCategory.{w}
      (PresheafOfModules.{max u v} (A ⋙ forget₂ CommRingCat RingCat))] :
    DerivedTensorProduct A
```

## Tag 091J, a remark

[Tag 091J](https://stacks.math.columbia.edu/tag/091J) in the Stacks Project.

**`ModuleSystemRlimTensor.exists_exactFunctor_isDerivedLimit_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimTensorLimit.lean, line 936](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimTensorLimit.lean#L936).

> **Stacks 091J.** The construction is the composite of the constant-system functor,
> derived tensor product with a lift of `E` in the derived category of compatible systems,
> and derived inverse limit. Its value at `K` is a derived limit of `K ⊗ᴸ[A] Eₙ`.

```lean
public theorem exists_exactFunctor_isDerivedLimit_tensor
    (A : Type u) [CommRing A]
    (E : ℕᵒᵖ ⥤ CochainComplex.DerivedTensor.DObj A) :
    let AR : ℕᵒᵖ ⥤ CommRingCat.{u} := (Functor.const ℕᵒᵖ).obj (CommRingCat.of A)
    let R : ℕᵒᵖ ⥤ RingCat.{u} := AR ⋙ forget₂ CommRingCat RingCat
    let C := PresheafOfModules.{u} R
    let DA := CochainComplex.DerivedTensor.DObj A
    let DN := DerivedCategory C
    let DB := DerivedCategory (ModuleCat.{u} (limit R : RingCat.{u}))
    let T := CochainComplex.DerivedTensor.canonicalDerivedTensorProduct A
    let S := ModuleSystemKFlatComparison.derivedTensorProduct.{u, u} AR
    let L : C ⥤ ModuleCat.{u} (limit R : RingCat.{u}) := ModuleInverseLimit.inverseLimit R
    ∃ (ρ : (limit R : RingCat.{u}) ≅ RingCat.of A),
      letI : (ModuleCat.restrictScalars.{u} ρ.inv.hom).IsEquivalence :=
        ModuleCat.restrictScalars_isEquivalence_of_ringEquiv
          ρ.symm.ringCatIsoToRingEquiv
      let U : DB ⥤ DA := (ModuleCat.restrictScalars.{u} ρ.inv.hom).mapDerivedCategory
      ∃ (hL : L.Additive),
      letI := hL
      ∃ (Δ : DA ⥤ DN)
        (_ : ∀ n : ℕᵒᵖ,
          Δ ⋙ (PresheafOfModules.evaluation R n).mapDerivedCategory ≅ 𝟭 DA)
        (_ : ∀ K : DA,
          ModuleRightDerivedLimit.derivedModuleDiagram R (Δ.obj K) ⋙ U ≅
            (Functor.const ℕᵒᵖ).obj K)
        (Etilde : DN)
        (_ : ModuleRightDerivedLimit.derivedModuleDiagram R Etilde ⋙ U ≅ E)
        (RF : DN ⥤ DB)
        (α : L.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
          DerivedCategory.Qh ⋙ RF)
        (hRFShift : RF.CommShift ℤ),
        letI := hRFShift
        RF.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso C (ComplexShape.up ℤ)) ∧
        RF.IsTriangulated ∧
        (∀ X : DN, ∃ _ : HasProduct fun n : ℕ ↦
            (ModuleRightDerivedLimit.derivedModuleDiagram R X).obj ⟨n⟩,
          IsDerivedLimit (ModuleRightDerivedLimit.derivedModuleDiagram R X) (RF.obj X)) ∧
        let tensorE := S.tensor.flip.obj Etilde
        ∃ (_ : ∀ n : ℕᵒᵖ,
          tensorE ⋙ (PresheafOfModules.evaluation R n).mapDerivedCategory ≅
            (PresheafOfModules.evaluation R n).mapDerivedCategory ⋙
              T.tensor.flip.obj (E.obj n))
          (_ : ∀ K : DA,
            ModuleRightDerivedLimit.derivedModuleDiagram R (tensorE.obj (Δ.obj K)) ⋙ U ≅
              E ⋙ T.tensor.obj K),
        let F := (Δ ⋙ tensorE) ⋙ RF ⋙ U
        ∃ (hF : F.CommShift ℤ),
          letI := hF
          F.IsTriangulated ∧
            ∀ K, ∃ (_ : HasProduct fun n : ℕ ↦
              (E ⋙ T.tensor.obj K).obj ⟨n⟩),
              IsDerivedLimit (E ⋙ T.tensor.obj K) (F.obj K)
```

## Tag 091K, a lemma

[Tag 091K](https://stacks.math.columbia.edu/tag/091K) in the Stacks Project.

**`ModuleSystemRlimTensor.derivedLimit_tensor_mapTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimTensorLimit.lean, line 1066](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimTensorLimit.lean#L1066).

> **Stacks 091K.** The canonical composite `Rlim ∘ (ΔK ⊗ᴸ[A] -)` from `D(ℕ, A)` to
> `D(A)` is exact. Equivalently, its canonical image of every distinguished triangle is
> distinguished.

```lean
public theorem derivedLimit_tensor_mapTriangle_distinguished
    (A : Type u) [CommRing A]
    (K : CochainComplex.DerivedTensor.DObj A) :
    let AR : ℕᵒᵖ ⥤ CommRingCat.{u} := (Functor.const ℕᵒᵖ).obj (CommRingCat.of A)
    let R : ℕᵒᵖ ⥤ RingCat.{u} := AR ⋙ forget₂ CommRingCat RingCat
    let C := PresheafOfModules.{u} R
    let DA := CochainComplex.DerivedTensor.DObj A
    let DN := DerivedCategory C
    let S := ModuleSystemKFlatComparison.derivedTensorProduct.{u, u} AR
    let L : C ⥤ ModuleCat.{u} (limit R : RingCat.{u}) := ModuleInverseLimit.inverseLimit R
    ∃ (ρ : (limit R : RingCat.{u}) ≅ RingCat.of A),
      letI : (ModuleCat.restrictScalars.{u} ρ.inv.hom).IsEquivalence :=
        ModuleCat.restrictScalars_isEquivalence_of_ringEquiv
          ρ.symm.ringCatIsoToRingEquiv
      let U : DerivedCategory (ModuleCat.{u} (limit R : RingCat.{u})) ⥤ DA :=
        (ModuleCat.restrictScalars.{u} ρ.inv.hom).mapDerivedCategory
      ∃ (hL : L.Additive),
        letI := hL
        ∃ (Δ : DA ⥤ DN)
          (_ : ∀ n : ℕᵒᵖ,
            Δ ⋙ (PresheafOfModules.evaluation R n).mapDerivedCategory ≅ 𝟭 DA)
          (_ : ModuleRightDerivedLimit.derivedModuleDiagram R (Δ.obj K) ⋙ U ≅
            (Functor.const ℕᵒᵖ).obj K)
          (RF : DN ⥤ DerivedCategory (ModuleCat.{u} (limit R : RingCat.{u})))
          (α : L.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
            DerivedCategory.Qh ⋙ RF)
          (hRFShift : RF.CommShift ℤ),
          letI := hRFShift
          RF.IsRightDerivedFunctor α
              (HomotopyCategory.quasiIso C (ComplexShape.up ℤ)) ∧
            RF.IsTriangulated ∧
            let tensorK := S.tensor.obj (Δ.obj K)
            let hTensorShift : tensorK.CommShift ℤ := S.commShift_right (Δ.obj K)
            letI := hTensorShift
            let G := tensorK ⋙ RF ⋙ U
            let hGShift : G.CommShift ℤ := inferInstance
            letI := hGShift
            G.IsTriangulated
```

## Tag 091L, a lemma

[Tag 091L](https://stacks.math.columbia.edu/tag/091L) in the Stacks Project.

**`ModuleSystemRlimProTensor.derivedLimit_tensor_map_isIso_of_proIsomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimProTensor.lean, line 622](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/ModuleRlimProTensor.lean#L622).

> If the morphism between the systems in `D(A)` associated to a morphism in `D(ℕ, A)` is an
> isomorphism of pro-objects, then for every `K ∈ D(A)` the corresponding map between the derived
> limits of the pointwise derived tensor products is an isomorphism.

```lean
public theorem derivedLimit_tensor_map_isIso_of_proIsomorphism
    (A : Type u) [CommRing A]
    {E D : DerivedCategory
      (PresheafOfModules.{u} ((Functor.const ℕᵒᵖ).obj (RingCat.of A)))} (f : E ⟶ D)
    (hf : IsIso (colim.map (Functor.whiskerRight
      (NatTrans.op ((derivedEvaluationFunctor A).map f)) coyoneda)))
    (K : CochainComplex.DerivedTensor.DObj A) :
    let AR : ℕᵒᵖ ⥤ CommRingCat.{u} := (Functor.const ℕᵒᵖ).obj (CommRingCat.of A)
    let R : ℕᵒᵖ ⥤ RingCat.{u} := (Functor.const ℕᵒᵖ).obj (RingCat.of A)
    let C := PresheafOfModules.{u} R
    let DA := CochainComplex.DerivedTensor.DObj A
    let DN := DerivedCategory C
    let S := ModuleSystemKFlatComparison.derivedTensorProduct AR
    let L : C ⥤ ModuleCat.{u} (limit R : RingCat.{u}) := ModuleInverseLimit.inverseLimit R
    ∃ (ρ : (limit R : RingCat.{u}) ≅ RingCat.of A),
      letI : (ModuleCat.restrictScalars.{u} ρ.inv.hom).IsEquivalence :=
        ModuleCat.restrictScalars_isEquivalence_of_ringEquiv
          ρ.symm.ringCatIsoToRingEquiv
      let U : DerivedCategory (ModuleCat.{u} (limit R : RingCat.{u})) ⥤ DA :=
        (ModuleCat.restrictScalars.{u} ρ.inv.hom).mapDerivedCategory
      ∃ (hL : L.Additive),
      letI := hL
      ∃ (Δ : DA ⥤ DN)
        (_ : ModuleRightDerivedLimit.derivedModuleDiagram R (Δ.obj K) ⋙ U ≅
          (Functor.const ℕᵒᵖ).obj K)
        (Rlim : DN ⥤ DerivedCategory (ModuleCat.{u} (limit R : RingCat.{u})))
        (α : L.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
          DerivedCategory.Qh ⋙ Rlim),
      Rlim.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso C (ComplexShape.up ℤ)) ∧
        IsIso ((S.tensor.obj (Δ.obj K) ⋙ Rlim ⋙ U).map f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.89, Tag 0CQC](https://stacks.math.columbia.edu/tag/0CQC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
