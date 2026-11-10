---
declaration: section
origin: cited
lean: Stacks.Eta.DerivedFunctor.eta_commutes_shift_but_not_triangulated, Stacks.Decalage.Cohomology.tag_0F7P_iso, Stacks.Eta.QuasiIsoPreservation.quasiIso_etaPow_of_quasiIso, Stacks.Eta.GoodBaseChange.quasiIso_etaMap, Stacks.Eta.DerivedDescent.exists_additive_derived_eta, Stacks.Eta.Reduction.exists_boundary_subcomplex_of_etaQuotient, Stacks.EtaComplex.FractionalPowerBockstein.powerBocksteinOperator_eq_connectingHom_comp_reduction, EtaPow.Bockstein.bocksteinComplex
statement: formalized
proof: formalized
---

# 15.97 An operator introduced by Berthelot and Ogus

Section 15.97 of the Stacks Project, [Tag 0F7N](https://stacks.math.columbia.edu/tag/0F7N). 12 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GSN, an example

[Tag 0GSN](https://stacks.math.columbia.edu/tag/0GSN) in the Stacks Project.

**`Stacks.Eta.DerivedFunctor.eta_commutes_shift_but_not_triangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Derived.lean, line 908](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Derived.lean#L908).

> **Stacks 0GSN.** The cone triangle of multiplication by `f` on `A` in degree
> one is distinguished. Its eta cone is homotopic to zero. If `f` is not a unit,
> the first eta arrow is not invertible and the image triangle is not distinguished.
> The compatible shift comparison is the fixed multiplication-by-`f` map
> `etaShiftIso_one_hom_app_f_val`.

```lean
theorem eta_commutes_shift_but_not_triangulated
    (f : A) (hf : f ∈ nonZeroDivisors A) :
    let g := etaCounterexampleMap.{u, v} f hf
    let q := HomotopyCategory.quotient (FTorsionFreeModule.{u, v} f) (ComplexShape.up ℤ)
    let T := CochainComplex.mappingCone.triangleh g
    T ∈ distTriang (HomotopyCategory (FTorsionFreeModule.{u, v} f) (ComplexShape.up ℤ)) ∧
      IsZero ((etaHomotopyFunctor f).obj (q.obj (CochainComplex.mappingCone g))) ∧
      (¬ IsUnit f →
        ¬ IsIso ((etaHomotopyFunctor f).map (q.map g)) ∧
        (etaHomotopyFunctor f).mapTriangle.obj T ∉
          distTriang (HomotopyCategory (FTorsionFreeModule.{u, v} f) (ComplexShape.up ℤ)))
```

## Tag 0F7P, a lemma

[Tag 0F7P](https://stacks.math.columbia.edu/tag/0F7P) in the Stacks Project.

**`Stacks.Decalage.Cohomology.tag_0F7P_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Cohomology.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Cohomology.lean#L466).

> **Stacks Tag 0F7P (isomorphism form).** Multiplication by `f^{j+1}` descends to a canonical
> isomorphism `H^{j+1}(M^•) / H^{j+1}(M^•)[f] ≅ H^{j+1}(η_f M^•)`.

```lean
theorem tag_0F7P_iso (C : FTFComplex A f) (j : ℤ) :
    ∃ (Φ : Hcohom C j →ₗ[A] Heta C j)
      (e : (Hcohom C j ⧸ LinearMap.ker Φ) ≃ₗ[A] Heta C j),
      (∀ ξ : Hcohom C j, ξ ∈ LinearMap.ker Φ ↔ f • ξ = 0) ∧
      (∀ ξ : Hcohom C j, e (Submodule.Quotient.mk ξ) = Φ ξ)
```

## Tag 0F7Q, a lemma

[Tag 0F7Q](https://stacks.math.columbia.edu/tag/0F7Q) in the Stacks Project.

**`Stacks.Eta.QuasiIsoPreservation.quasiIso_etaPow_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Derived.lean, line 1076](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Derived.lean#L1076).

> **Stacks 0F7Q.** The Berthelot--Ogus décalage of a quasi-isomorphism of
> complexes of `f`-torsion-free modules is a quasi-isomorphism.

```lean
theorem quasiIso_etaPow_of_quasiIso
    {A : Type u} [CommRing A] {f : A} (_hf : f ∈ nonZeroDivisors A)
    (E : EtaFunctor.{u, v} f)
    {M N : CochainComplex (FTorsionFreeModule.{u, v} f) ℤ} (g : M ⟶ N)
    (hg : QuasiIso ((underlyingComplex f).map g)) :
    QuasiIso ((underlyingComplex f).map (E.functor.map g))
```

**`Stacks.Eta.GoodBaseChange.quasiIso_etaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Perfect/GoodBaseChange.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Perfect/GoodBaseChange.lean#L318). The attribute's comment: “stated for `EtaComplex.etaObject`”.

> The décalage `EtaComplex.etaMap f φ` of a quasi-isomorphism `φ` between complexes of
> `f`-torsion-free `A`-modules is a quasi-isomorphism.

```lean
theorem quasiIso_etaMap (f : A) (hf : f ∈ nonZeroDivisors A)
    {K L : CochainComplex (ModuleCat.{u} A) ℤ}
    (hK : EtaComplex.IsTorsionFree f K) (hL : EtaComplex.IsTorsionFree f L)
    (φ : K ⟶ L) (hφ : QuasiIso φ) :
    QuasiIso (EtaComplex.etaMap f φ)
```

## Tag 0F7R, a lemma

[Tag 0F7R](https://stacks.math.columbia.edu/tag/0F7R) in the Stacks Project.

**`Stacks.Eta.DerivedDescent.exists_additive_derived_eta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Derived.lean, line 1385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Derived.lean#L1385).

> **Stacks 0F7R.** For a nonzerodivisor `f`, the Berthelot--Ogus décalage
> descends to an additive endofunctor of the derived category. On every complex
> of `f`-torsion-free modules it is naturally isomorphic, on objects and
> morphisms, to the chain-level décalage.

```lean
theorem exists_additive_derived_eta
    {A : Type u} [CommRing A] [HasDerivedCategory.{w} (ModuleCat.{max u v} A)]
    (f : A) (hf : f ∈ nonZeroDivisors A) :
    ∃ (Leta : DerivedCategory (ModuleCat.{max u v} A) ⥤
        DerivedCategory (ModuleCat.{max u v} A)),
      Leta.Additive ∧
        ∃ E : EtaFunctor.{u, v} f,
          Nonempty (underlyingComplex f ⋙ DerivedCategory.Q ⋙ Leta ≅
            E.functor ⋙ underlyingComplex f ⋙ DerivedCategory.Q)
```

## Tag 0F7S, a remark

[Tag 0F7S](https://stacks.math.columbia.edu/tag/0F7S) in the Stacks Project.

**`Stacks.Eta.Reduction.exists_boundary_subcomplex_of_etaQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Reduction.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Reduction.lean#L688).

> **Stacks 0F7S.** Modulo a nonzerodivisor `f`, the eta complex has an acyclic
> subcomplex with degree-`i` term `B^(i+1) ⊕ B^i`, and the quotient complex has the
> cohomology modules of `M/fM` as its terms, with the induced differential transported
> along the equivalences `e`. The final three clauses give the
> representative formulas for the maps `t`, `s`, and `s'` from the source.

```lean
theorem exists_boundary_subcomplex_of_etaQuotient
    (f : A) (_hf : f ∈ nonZeroDivisors A)
    (C : EtaComplex.Complex.{u, v} A) (hC : EtaComplex.IsTorsionFree f C) :
    let barTerm : ℤ → Type (max u v) := fun i =>
      (C.X i) ⧸ LinearMap.range (EtaComplex.scalarMap f (C.X i))
    ∃ barD : ∀ i j, barTerm i →ₗ[A] barTerm j,
      (∀ i (x : C.X i),
        barD i (i + 1) (Submodule.Quotient.mk x) =
          Submodule.Quotient.mk ((C.d i (i + 1)).hom x)) ∧
      (∀ i j, i + 1 ≠ j → barD i j = 0) ∧
      (∀ i (x : barTerm i), barD (i + 1) (i + 1 + 1) (barD i (i + 1) x) = 0) ∧
      let B : ∀ i, Submodule A (barTerm i) := fun i =>
        LinearMap.range (barD (i - 1) i)
      let Z : ∀ i, Submodule A (barTerm i) := fun i => LinearMap.ker (barD i (i + 1))
      let H : ℤ → Type (max u v) := fun i =>
        (Z i) ⧸ (B i).comap (Z i).subtype
      let Q : ℤ → Type (max u v) := fun i => EtaComplex.QuotientTerm f C i
      ∃ (hBZ : ∀ i, B i ≤ Z i)
        (s : ∀ i, B (i + 1) →ₗ[A] Q i)
        (s' : ∀ i, B i →ₗ[A] Q i)
        (t : ∀ i, Q i →ₗ[A] Z i)
        (e : ∀ i,
          (Q i ⧸ LinearMap.range (LinearMap.coprod (s i) (s' i))) ≃ₗ[A] H i),
        (∀ i, Function.Injective (LinearMap.coprod (s i) (s' i))) ∧
        (∀ i, Function.Injective (s i)) ∧
        (∀ i, Function.Surjective (t i)) ∧
        (∀ i, Function.Exact (s i) (t i)) ∧
        (∀ i (bNext : B (i + 1)) (b : B i),
          t i (s i bNext + s' i b) = ⟨b, hBZ i b.2⟩) ∧
        (∀ i (bNext : B (i + 1)) (b : B i),
          EtaComplex.quotientDifferential f C i (s i bNext + s' i b) =
            s' (i + 1) bNext) ∧
        (∀ i, Function.Exact
          (fun p : B i × B (i - 1) => ((0 : B (i + 1)), p.1))
          (fun p : B (i + 1) × B i => ((0 : B (i + 1 + 1)), p.1))) ∧
        (∀ i (q : Q i),
          e i (Submodule.Quotient.mk q) = Submodule.Quotient.mk (t i q)) ∧
        (∃ dH : ∀ i, H i →ₗ[A] H (i + 1),
          (∀ i (q : Q i),
            e (i + 1) (Submodule.Quotient.mk
              (EtaComplex.quotientDifferential f C i q)) =
                dH i (e i (Submodule.Quotient.mk q))) ∧
          (∀ i (h : H i), dH (i + 1) (dH i h) = 0)) ∧
        (∀ i (x : C.X i)
            (hx : EtaPow.fpowMap f (C.X i) i x ∈ EtaComplex.term f C i),
          ∃ hz : Submodule.Quotient.mk x ∈ Z i,
            t i (Submodule.Quotient.mk
              (⟨EtaPow.fpowMap f (C.X i) i x, hx⟩ : EtaComplex.term f C i)) =
                ⟨Submodule.Quotient.mk x, hz⟩) ∧
        (∀ i (y : C.X (i + 1)) (hy : Submodule.Quotient.mk y ∈ B (i + 1))
            (y' : C.X (i + 1)) (x : C.X i)
            (_heq : y = f • y' + (C.d i (i + 1)).hom x),
          ∃ heta : EtaPow.fpowMap f (C.X i) (i + 1) x ∈ EtaComplex.term f C i,
            s i ⟨Submodule.Quotient.mk y, hy⟩ =
              Submodule.Quotient.mk
                (⟨EtaPow.fpowMap f (C.X i) (i + 1) x, heta⟩ :
                  EtaComplex.term f C i)) ∧
        (∀ i (x : C.X i) (hx : Submodule.Quotient.mk x ∈ B i)
            (x' : C.X i) (z : C.X (i - 1))
            (_heq : x = f • x' + (C.d (i - 1) i).hom z),
          ∃ heta : EtaPow.fpowMap f (C.X i) i ((C.d (i - 1) i).hom z) ∈
              EtaComplex.term f C i,
            s' i ⟨Submodule.Quotient.mk x, hx⟩ =
              Submodule.Quotient.mk
                (⟨EtaPow.fpowMap f (C.X i) i ((C.d (i - 1) i).hom z), heta⟩ :
                  EtaComplex.term f C i))
```

## Tag 0GSP, an equation

[Tag 0GSP](https://stacks.math.columbia.edu/tag/0GSP) in the Stacks Project.

**`Stacks.EtaComplex.FractionalPowerBockstein.powerBocksteinOperator_eq_connectingHom_comp_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Reduction.lean, line 1133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Reduction.lean#L1133).

> **Stacks 0GSP.** For the actual fractional power ideals in `A[1/f]`, the Bockstein
> operator for the successive-quotient row equals the connecting morphism of the unquotiented
> row followed by cohomology of the canonical reduction `fⁱ⁺¹A → fⁱ⁺¹A/fⁱ⁺²A`, after
> tensoring both rows with `M`. The definitions above formally identify every object and map
> with the power-ideal diagram in the source.

```lean
theorem powerBocksteinOperator_eq_connectingHom_comp_reduction
    (f : A) (hf : f ∈ nonZeroDivisors A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ) (hM : ∀ n, IsSMulRegular (M.X n) f)
    (i n : ℤ) :
    ∃ (hUpper : (powerIdealShortComplex M f i).ShortExact)
      (hLower : (successivePowerQuotientShortComplex M f i).ShortExact),
      powerBocksteinOperator M f i n hLower =
        hUpper.δ n (n + 1) (by simp [ComplexShape.up]) ≫
          HomologicalComplex.homologyMap
            ((tensorWithCochainComplex M).map
              (cokernel.π (fractionalPowerInclusion f (i + 1)))) (n + 1)
```

## Tag 0GSQ, an equation

[Tag 0GSQ](https://stacks.math.columbia.edu/tag/0GSQ) in the Stacks Project.

**`EtaPow.Bockstein.bocksteinComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Reduction.lean, line 1239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Reduction.lean#L1239).

> **Stacks 0GSQ.** The complex `Hᵇ(M/f)` has term
> `Hⁱ(M ⊗ fⁱA/fⁱ⁺¹A)` in degree `i` and the canonical Bockstein map as its differential.

```lean
def bocksteinComplex (f : A) (hf : f ∈ nonZeroDivisors A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hM : ∀ n, IsSMulRegular (M.X n) f) :
    CochainComplex (ModuleCat.{u} A) ℤ
```

## Tag 0F7T, a lemma

[Tag 0F7T](https://stacks.math.columbia.edu/tag/0F7T) in the Stacks Project.

**`Stacks.EtaComplex.ModNonzerodivisor.etaTensorMod_to_bockstein_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Reduction.lean, line 2099](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Reduction.lean#L2099).

> **Stacks 0F7T.** If `f` is a nonzerodivisor and every term of `M` is
> `f`-torsion-free, the canonical map from `η_f M ⊗_A A/fA` to the Bockstein
> complex of `M/f` is a quasi-isomorphism.

```lean
theorem etaTensorMod_to_bockstein_quasiIso
    (f : A) (hf : f ∈ nonZeroDivisors A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hM : ∀ i, IsSMulRegular (M.X i) f) :
    QuasiIso
      ((etaTensorQuotientIso f hf M hM).hom ≫ etaQuotientToBockstein f hf M hM)
```

## Tag 0F7Y, a lemma

[Tag 0F7Y](https://stacks.math.columbia.edu/tag/0F7Y) in the Stacks Project.

**`Stacks.Eta.BocksteinVanishing.cyclesReduction_epi_iff_powerBocksteinOperator_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Reduction.lean, line 2471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Reduction.lean#L2471).

> **Stacks 0F7Y.** For a complex of `f`-torsion-free modules, reduction from cycles
> modulo `f²` to cycles modulo `f` is surjective if and only if the corresponding Bockstein
> operator is zero. Moreover, these equivalent conditions hold if multiplication by `f` is
> injective on `Hⁱ⁺¹(M)`.

```lean
theorem cyclesReduction_epi_iff_powerBocksteinOperator_eq_zero
    (f : A) (hf : f ∈ nonZeroDivisors A)
    (M : CochainComplex (ModuleCat.{v} A) ℤ) (hM : ∀ n, IsSMulRegular (M.X n) f)
    (i : ℤ) :
    let K := commonUniverseComplex M
    let f' : ULift.{v} A := ULift.up f
    let hf' := ulift_mem_nonZeroDivisors f hf
    let hK := fun n => commonUniverseModules_regular (M.X n) f (hM n)
    let hLower := (powerIdealRows_shortExact f' hf' K hK i).2
    let cyclesReduction := HomologicalComplex.cyclesMap
      (literalPowerQuotientShortComplex K f').g i
    (Epi cyclesReduction ↔ powerBocksteinOperator K f' i i hLower = 0) ∧
      (IsSMulRegular (M.homology (i + 1)) f → Epi cyclesReduction)
```

## Tag 0F7Z, a lemma

[Tag 0F7Z](https://stacks.math.columbia.edu/tag/0F7Z) in the Stacks Project.

**`Stacks.Eta.ReductionDirectSum.etaQuotient_range_eq_prod_of_cyclesReduction_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Reduction.lean, line 2667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Reduction.lean#L2667).

> **Stacks 0F7Z.** If cycles modulo `f` lift to cycles modulo `f²`, the canonical
> map `(1, dⁱ)` embeds the degree-`i` eta term modulo `f` as a product of a submodule
> of `fⁱCⁱ/fⁱ⁺¹Cⁱ` and a submodule of `fⁱ⁺¹Cⁱ⁺¹/fⁱ⁺²Cⁱ⁺¹`.

```lean
theorem etaQuotient_range_eq_prod_of_cyclesReduction_surjective
    (f : A) (_hf : f ∈ nonZeroDivisors A)
    (C : EtaComplex.Complex.{u, v} A) (hC : EtaComplex.IsTorsionFree f C)
    (i : ℤ) :
    let mul : ∀ _n : ℕ, ∀ j : ℤ, C.X j →ₗ[A] C.X j := fun n j =>
      { toFun := fun x => (f ^ n) • x
        map_add' := fun x y => smul_add (f ^ n) x y
        map_smul' := fun a x => by simp only [RingHom.id_apply, smul_comm a (f ^ n)] }
    let modTerm : ℕ → ℤ → Type (max u v) := fun n j =>
      (C.X j) ⧸ LinearMap.range (mul n j)
    let dMod : ∀ n j, modTerm n j →ₗ[A] modTerm n (j + 1) := fun n j =>
      Submodule.mapQ _ _ (C.d j (j + 1)).hom (by
        rintro _ ⟨x, rfl⟩
        exact ⟨(C.d j (j + 1)).hom x, by
          exact (map_smul (C.d j (j + 1)).hom (f ^ n) x).symm⟩)
    let reduction : ∀ j, modTerm 2 j →ₗ[A] modTerm 1 j := fun j =>
      Submodule.mapQ _ _ LinearMap.id (by
        rintro _ ⟨x, rfl⟩
        refine ⟨f • x, ?_⟩
        change f ^ 1 • (f • x) = f ^ 2 • x
        simp only [pow_one, pow_two, mul_smul])
    (∀ x : modTerm 1 i, dMod 1 i x = 0 →
      ∃ y : modTerm 2 i, dMod 2 i y = 0 ∧ reduction i y = x) →
    let P₀ := EtaPow.fpowSub f (C.X i) i
    let P₁ := EtaPow.fpowSub f (C.X i) (i + 1)
    let Q₀ := EtaPow.fpowSub f (C.X (i + 1)) (i + 1)
    let Q₁ := EtaPow.fpowSub f (C.X (i + 1)) (i + 2)
    let leftPowerQuotient := P₀ ⧸ P₁.comap P₀.subtype
    let rightPowerQuotient := Q₀ ⧸ Q₁.comap Q₀.subtype
    ∃ (canonical : EtaComplex.QuotientTerm f C i →ₗ[A]
          leftPowerQuotient × rightPowerQuotient)
      (Z : Submodule A leftPowerQuotient) (B : Submodule A rightPowerQuotient),
      (∀ x : EtaComplex.term f C i,
        canonical (Submodule.Quotient.mk x) =
          (Submodule.Quotient.mk (⟨x.1, x.2.1⟩ : P₀),
            Submodule.Quotient.mk
              (⟨EtaPow.fLoc f (C.d i (i + 1)).hom x.1, x.2.2⟩ : Q₀))) ∧
      Function.Injective canonical ∧ LinearMap.range canonical = Z.prod B
```

## Tag 0F7U, a lemma

[Tag 0F7U](https://stacks.math.columbia.edu/tag/0F7U) in the Stacks Project.

**`EtaDecalage.etaFetaG_eq_etaFG_cochainComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Composition.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Composition.lean#L295).

> For a cochain complex `M^•` of `A`-modules, the cochain complexes `η_f (η_g M^•)` and
> `η_{fg} M^•` in `CochainComplex (ModuleCat A) ℤ` are equal.

```lean
theorem etaFetaG_eq_etaFG_cochainComplex (hdd : ∀ i, (d (i + 1)).comp (d i) = 0)
    (preserve : ∀ i, ((etaFetaG (f := f) (g := g) (d := d)) i).map (dLoc f g M d i)
      ≤ (etaFetaG (f := f) (g := g) (d := d)) (i + 1)) :
    (etaFetaG (f := f) (g := g) (d := d)).toCochainComplex preserve hdd
      = (etaFG (f := f) (g := g) (d := d)).toCochainComplex
          (by rw [← etaFetaG_eq_etaFG hdd]; exact preserve) hdd
```

## Tag 0GSR, a lemma

[Tag 0GSR](https://stacks.math.columbia.edu/tag/0GSR) in the Stacks Project.

**`Stacks.Eta.BaseChange.algebraMap_mem_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/BaseChange.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/BaseChange.lean#L168). The attribute's comment: “g is a nonzerodivisor”.

> **Statement 1.** If `f` is a nonzerodivisor in `A` and `A → B` is flat, then its image
> `g = algebraMap A B f` is a nonzerodivisor in `B`.

```lean
theorem algebraMap_mem_nonZeroDivisors (f : A) [Module.Flat A B] (hf : f ∈ nonZeroDivisors A) :
    (algebraMap A B f) ∈ nonZeroDivisors B
```

**`Stacks.Eta.BaseChange.isSMulRegular_baseChange_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/BaseChange.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/BaseChange.lean#L176). The attribute's comment: “the base change is g-torsion free”.

> **Statement 2.** For `A → B` flat and `M^•` a complex of `f`-torsion free `A`-modules, each
> base-changed term `M^i ⊗_A B` is `g`-torsion free, where `g = algebraMap A B f`.

```lean
theorem isSMulRegular_baseChange_X (f : A) [Module.Flat A B] (M : CochainComplex (ModuleCat A) ℤ)
    (hM : ∀ i, IsSMulRegular (M.X i) f) (i : ℤ) :
    IsSMulRegular (B ⊗[A] (M.X i : Type _)) (algebraMap A B f)
```

**`Stacks.Eta.BaseChange.etaBaseChangeTerm_eq_fetaTerm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/BaseChange.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/BaseChange.lean#L706). The attribute's comment: “eta commutes with the base change”.

> **Statement 3.** With the identification of Definition 4,
> `η_f M^• ⊗_A B = η_g (M^• ⊗_A B)` as complexes of `g`-torsion free `B`-modules.
>
> This is the equality, for every `i ∈ ℤ`, of two `B`-submodules of the common ambient module
> `(M^i ⊗_A B)_g = LocalizedModule (powers g) (B ⊗_A M^i)`:
>
> * the base change `(η_f M)^i ⊗_A B` (`etaBaseChangeTerm f M i`), and
> * the degree-`i` term `(η_g (M^• ⊗_A B))^i` of the décalage of the base-changed complex,
>   `fetaTerm g (d^i ⊗ id_B) i`.
>
> The second conjunct records compatibility with the differentials: the localized base-changed
> differential `d^i ⊗ id_B` carries the degree-`i` term into the degree-`(i+1)` term, exhibiting
> the equality as an equality of *subcomplexes*.

```lean
theorem etaBaseChangeTerm_eq_fetaTerm (f : A) [Module.Flat A B] (M : CochainComplex (ModuleCat A) ℤ)
    (i : ℤ) :
    (etaBaseChangeTerm f M i
        = fetaTerm (algebraMap A B f)
            (LinearMap.baseChange B (M.d i (i + 1)).hom) i) ∧
      Submodule.map (fLoc (algebraMap A B f) (LinearMap.baseChange B (M.d i (i + 1)).hom))
          (fetaTerm (algebraMap A B f) (LinearMap.baseChange B (M.d i (i + 1)).hom) i)
        ≤ fetaTerm (algebraMap A B f) (LinearMap.baseChange B (M.d (i + 1) (i + 1 + 1)).hom) (i +
            1)
```

**`Stacks.Eta.GoodBaseChange.isIso_etaBaseChangeMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Eta/Perfect/GoodBaseChangeFlat.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Eta/Perfect/GoodBaseChangeFlat.lean#L122). The attribute's comment: “the comparison `B ⊗_A (η_f K) ⟶ η_g (B ⊗_A K)` is an isomorphism of complexes, for a flat ring map and an arbitrary cochain complex”.

> **More on Algebra, Tag 0GSR as an isomorphism of complexes.**  Let `A → B` be a flat map of
> commutative rings, let `f ∈ A` with image `g = algebraMap A B f`, and let `K` be a cochain
> complex of `A`-modules.  Then the canonical comparison
>
> `B ⊗_A (η_f K) ⟶ η_g (B ⊗_A K)`
>
> is an isomorphism of complexes of `B`-modules: the décalage commutes with flat base change.
>
> The tag itself, `Stacks.Eta.BaseChange.etaBaseChangeTerm_eq_fetaTerm`, states this as an
> equality of `B`-submodules of one ambient localization in each degree; what is added here is
> that the comparison realizing that equality is a degreewise bijection, which is
> `Stacks.Eta.GoodBaseChange.bijective_psiTermMap_of_flat`.

```lean
theorem isIso_etaBaseChangeMap_of_flat (f : A) [Module.Flat A B]
    (K : CochainComplex (ModuleCat.{u} A) ℤ) :
    IsIso (etaBaseChangeMap (B := B) f K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.97, Tag 0F7N](https://stacks.math.columbia.edu/tag/0F7N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
