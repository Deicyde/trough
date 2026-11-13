---
declaration: section
origin: cited
lean: formalSmoothness_maximalIdeal_characterizations, formallySmooth_adic_examples_with_inseparable_residueField, flat_of_isFormallySmooth_maximalIdeal_adic, exact_jacobiZariski_residueField_of_formallySmoothNAdic, RingHom.FormallySmoothNAdic.of_flat_of_specialFibre, flat_geometricallyRegular_specialFiber_formallySmooth_tfae, exists_completeLocal_formallySmooth_lift, exists_completeLocal_formallySmooth_lift_with_baseChange
statement: formalized
proof: formalized
---

# 15.41 Geometric regularity and formal smoothness

Section 15.41 of the Stacks Project, [Tag 07EK](https://stacks.math.columbia.edu/tag/07EK). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07EL, a theorem

[Tag 07EL](https://stacks.math.columbia.edu/tag/07EL) in the Stacks Project.

**`formalSmoothness_maximalIdeal_characterizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 1088](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L1088). References: EGA 0 (19.6.6), “a) <=> c)”; EGA 0 (19.6.4), “char 0: a) ⇔ c)”; EGA 0 (19.6.5), “form. smooth ⟹ geom reg”; EGA 0 (22.1.2), “base a field, Noetherian”; EGA 0 (22.2.2), “(i)&(ii), char p”; EGA 0 (22.2.3), “a) (char p)”; EGA 0 (22.7.2), “a) <=> c) char 0”; EGA 0 (22.5.8); EGA 0 (22.6.7), “(i) b) ⇔ d)”; EGA 0 (19.0.2), “special case”; EGA 0 (19.6.7), “19.6.7(ii), special case”.

> Let `A` be a Noetherian local algebra over a field `k`. In characteristic zero, `A` is a
> regular local ring if and only if `k → A` is formally smooth for the maximal-ideal adic
> topology. In prime characteristic `p`, the following are equivalent:
>
> 1. `A` is geometrically regular over `k`;
> 2. `k → A` is formally smooth for the maximal-ideal adic topology;
> 3. every finite intermediate extension in `k¹ᵖ` gives a regular base change;
> 4. `A` is regular and the canonical cotangent-complex map is injective;
> 5. `A` is regular and the canonical map on Kähler differentials is injective.

```lean
public theorem formalSmoothness_maximalIdeal_characterizations
    (k : Type u) (A : Type v) [Field k] [CommRing A] [Algebra k A]
    [IsNoetherianRing A] [IsLocalRing A] :
    (let m := IsLocalRing.maximalIdeal A
     letI : TopologicalSpace k := ⊥
     letI : DiscreteTopology k := ⟨rfl⟩
     letI : TopologicalSpace A := m.adicTopology
     letI : IsTopologicalRing A := m.ringFilterBasis.isTopologicalRing
     letI : IsLinearTopology A A := m.isLinearTopology
     ∀ [CharZero k],
       IsRegularLocalRing A ↔
         IsFormallySmooth.{max u v} (algebraMap k A)) ∧
    (∀ (p : ℕ) [Fact p.Prime] [CharP k p],
      letI : Algebra (ZMod p) k := ZMod.algebra k p
      letI : Algebra (ZMod p) A :=
        ((algebraMap k A).comp (algebraMap (ZMod p) k)).toAlgebra
      letI : IsScalarTower (ZMod p) k A := IsScalarTower.of_algebraMap_eq' rfl
      letI : Algebra k (PerfectClosure k p) := (PerfectClosure.of k p).toAlgebra
      let m := IsLocalRing.maximalIdeal A
      letI : TopologicalSpace k := ⊥
      letI : DiscreteTopology k := ⟨rfl⟩
      letI : TopologicalSpace A := m.adicTopology
      letI : IsTopologicalRing A := m.ringFilterBasis.isTopologicalRing
      letI : IsLinearTopology A A := m.isLinearTopology
      List.TFAE [
        Algebra.IsGeometricallyRegular k A,
        IsFormallySmooth.{max u v} (algebraMap k A),
        (∀ (k' : IntermediateField k (PerfectClosure k p)),
          FiniteDimensional k k' →
          (∀ x : k', (x : PerfectClosure k p) ^ p ∈
            Set.range (algebraMap k (PerfectClosure k p))) →
          IsRegularRing (A ⊗[k] k')),
        IsRegularLocalRing A ∧
          Function.Injective
            (Algebra.H1Cotangent.map k A (IsLocalRing.ResidueField A)
              (IsLocalRing.ResidueField A)),
        IsRegularLocalRing A ∧
          Function.Injective
            ((KaehlerDifferential.mapBaseChange (ZMod p) k A).baseChange
              (IsLocalRing.ResidueField A))])
```

## Tag 07EM, an example

[Tag 07EM](https://stacks.math.columbia.edu/tag/07EM) in the Stacks Project.

**`formallySmooth_adic_examples_with_inseparable_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 1746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L1746). References: EGA 0 (19.6.5.2), “existence of examples”.

> In characteristic `p`, the local ring
> `k[x, y]_(x, y ^ p - a) / (y ^ p - a - x)` is geometrically regular over `k`, formally
> smooth both algebraically and for its maximal-ideal-adic topology, and has purely inseparable
> residue field. Closely relatedly, if `K` is the perfect closure of `𝔽ₚ(t)`, there is a map
> `𝔽ₚ(s) → K[[x]]` sending `s` to `t + x` which is formally smooth for the `(x)`-adic topology.
> For the latter map, `ds` and `dx` are the indicated bases of the Kähler differentials and the
> map on differentials sends `ds` to `dx`.

```lean
public theorem formallySmooth_adic_examples_with_inseparable_residueField
    (p : ℕ) [Fact p.Prime] :
    (∀ (k : Type u) [Field k] [CharP k p] (a : k),
      a ∉ Set.range (fun b : k => b ^ p) →
      let P := MvPolynomial (Fin 2) k
      let m : Ideal P := Ideal.span
        {MvPolynomial.X 0, MvPolynomial.X 1 ^ p - MvPolynomial.C a}
      let g : P := MvPolynomial.X 1 ^ p - MvPolynomial.C a - MvPolynomial.X 0
      ∃ hm : m.IsPrime,
        letI : m.IsPrime := hm
        let B := Localization.AtPrime m
        let A := B ⧸ Ideal.span {algebraMap P B g}
        ∃ hlocal : IsLocalRing A,
          letI : IsLocalRing A := hlocal
          IsNoetherianRing A ∧
          Algebra.IsGeometricallyRegular k A ∧
          IsPurelyInseparable k (IsLocalRing.ResidueField A) ∧
          Algebra.FormallySmooth k A ∧
          let n := IsLocalRing.maximalIdeal A
          @IsAdicallyFormallySmooth k A _ _ n (algebraMap k A)) ∧
    (let k := RatFunc (ZMod p)
     let K := PerfectClosure k p
     letI : Algebra k K := (PerfectClosure.of k p).toAlgebra
     let A := PowerSeries K
     ∃ f : k →+* A,
       f RatFunc.X =
          PowerSeries.C (algebraMap k K RatFunc.X) + PowerSeries.X ∧
       letI : Algebra k A := f.toAlgebra
       letI : Algebra (ZMod p) A :=
         (f.comp (algebraMap (ZMod p) k)).toAlgebra
       letI : IsScalarTower (ZMod p) k A :=
         IsScalarTower.of_algebraMap_eq' rfl
       (∃ b : Module.Basis Unit k (KaehlerDifferential (ZMod p) k),
          b () = KaehlerDifferential.D (ZMod p) k RatFunc.X) ∧
       (∃ b : Module.Basis Unit A (KaehlerDifferential (ZMod p) A),
          b () = KaehlerDifferential.D (ZMod p) A PowerSeries.X) ∧
       KaehlerDifferential.map (ZMod p) (ZMod p) k A
           (KaehlerDifferential.D (ZMod p) k RatFunc.X) =
         KaehlerDifferential.D (ZMod p) A PowerSeries.X ∧
       let x : Ideal A := Ideal.span {PowerSeries.X}
       @IsAdicallyFormallySmooth k A _ _ x f)
```

## Tag 07NP, a lemma

[Tag 07NP](https://stacks.math.columbia.edu/tag/07NP) in the Stacks Project.

**`flat_of_isFormallySmooth_maximalIdeal_adic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L595). References: SGA 1 III (1.7), “only if, flatness”.

> **Stacks 07NP.** A formally smooth local homomorphism of Noetherian local rings, for the
> maximal-ideal-adic topologies on source and target, is flat.

```lean
public theorem flat_of_isFormallySmooth_maximalIdeal_adic.{v, w}
    {A : Type v} {B : Type w}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : RingHom.FormallySmoothNAdic.{max v w} f (maximalIdeal B)) :
    letI : Algebra A B := f.toAlgebra
    Module.Flat A B
```

## Tag 0DYH, a lemma

[Tag 0DYH](https://stacks.math.columbia.edu/tag/0DYH) in the Stacks Project.

**`exact_jacobiZariski_residueField_of_formallySmoothNAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 755](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L755). References: EGA 0 (20.6.23), “residue field, m-adic”.

> Let `A → B` be a local homomorphism of Noetherian local rings which is formally smooth for
> the maximal-ideal-adic topology on `B`, and let `K` be the residue field of `B`.  Then the
> canonical Jacobi–Zariski sequence
>
> `0 → H₁(L_{K/A}) → 𝔪_B/𝔪_B² → Ω[B⁄A] ⊗[B] K → Ω[K⁄A] → 0`
>
> is exact.

```lean
public theorem exact_jacobiZariski_residueField_of_formallySmoothNAdic
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f]
    (hf : RingHom.FormallySmoothNAdic.{max u v} f (maximalIdeal B)) :
    let K := ResidueField B
    letI : Algebra A B := f.toAlgebra
    letI : Algebra A K := ((residue B).comp f).toAlgebra
    letI : IsScalarTower A B K := IsScalarTower.of_algebraMap_eq' rfl
    let e : Algebra.H1Cotangent B K ≃ₗ[B] CotangentSpace B :=
      (h1Cotangent_equiv_cotangent_of_surjective B K residue_surjective).trans
        (Ideal.Cotangent.equivOfEq _ _ (ker_residue (R := B)))
    let i : Algebra.H1Cotangent A K → CotangentSpace B :=
      fun x ↦ e (Algebra.H1Cotangent.map A B K K x)
    let d : CotangentSpace B → K ⊗[B] Ω[B⁄A] :=
      fun x ↦ Algebra.H1Cotangent.δ A B K (e.symm x)
    Function.Injective i ∧
      Function.Exact i d ∧
      Function.Exact d (KaehlerDifferential.mapBaseChange A B K) ∧
      Function.Surjective (KaehlerDifferential.mapBaseChange A B K)
```

## Tag 07NQ, a proposition

[Tag 07NQ](https://stacks.math.columbia.edu/tag/07NQ) in the Stacks Project.

**`RingHom.FormallySmoothNAdic.of_flat_of_specialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/SpecialFibre.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/SpecialFibre.lean#L401). The attribute's comment: “(2) ⟹ (3)”. References: EGA 0 (19.0.2), “I, one direction”; EGA 0 (19.7.1), “b) ⇒ a)”; SGA 1 III (1.7), “if direction”.

> **Stacks 07NQ, (2) ⟹ (3).** A flat local homomorphism of Noetherian local rings whose
> special fibre is adically formally smooth over the residue field of the source is itself formally
> smooth for the maximal-ideal-adic topology.

```lean
theorem FormallySmoothNAdic.of_flat_of_specialFibre
    (A : Type u) (B : Type v)
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (hbar : FormallySmoothNAdic.{max u v}
      (algebraMap (ResidueField A) (ResidueField A ⊗[A] B))
      (maximalIdeal (ResidueField A ⊗[A] B))) :
    FormallySmoothNAdic.{max u v} (algebraMap A B) (maximalIdeal B)
```

**`flat_geometricallyRegular_specialFiber_formallySmooth_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 2254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L2254). References: EGA 0 (19.0.2), “I”; EGA 0 (19.7.1), “more general”; SGA 1 III (1.7), “Noetherian local rings”; SGA 1 III (1.3), “more general”.

> Let `f : A → B` be a local homomorphism of Noetherian local rings, let
> `k` be the residue field of `A`, and let `B̄ = k ⊗[A] B` be the special
> fibre. The following are equivalent:
>
> 1. `f` is flat and `B̄` is geometrically regular over `k`;
> 2. `f` is flat and `k → B̄` is formally smooth for the maximal-ideal-adic
>    topology;
> 3. `f` is formally smooth for the maximal-ideal-adic topology on `B`.

```lean
public theorem flat_geometricallyRegular_specialFiber_formallySmooth_tfae
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    (f : A →+* B) [IsLocalHom f] :
    letI : Algebra A B := f.toAlgebra
    let k := ResidueField A
    let Bbar := k ⊗[A] B
    List.TFAE [
      Module.Flat A B ∧ Algebra.IsGeometricallyRegular k Bbar,
      Module.Flat A B ∧
        RingHom.FormallySmoothNAdic.{max u v}
          (algebraMap k Bbar) (maximalIdeal Bbar),
      RingHom.FormallySmoothNAdic.{max u v} f (maximalIdeal B)]
```

## Tag 07NR, a lemma

[Tag 07NR](https://stacks.math.columbia.edu/tag/07NR) in the Stacks Project.

**`exists_completeLocal_formallySmooth_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 2513](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L2513). References: EGA 0 (19.7.2), “existence, J = 𝔪”; EGA 0 (19.0.2), “III existence”; EGA 0 (19.7.1.3), “A complete, B geom reg”; EGA 0 (19.8.2), “(ii) existence”; EGA 0 (22.2.7), “(i)”.

> **Stacks 07NR.** Let `A` be a Noetherian complete local ring and let `B` be a
> Noetherian complete local algebra over the residue field of `A`. If `B` is formally smooth for
> its maximal-ideal-adic topology, then it is the special fibre of a Noetherian complete local
> ring `C` that is adically formally smooth over `A` via a local homomorphism.

```lean
public theorem exists_completeLocal_formallySmooth_lift
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsAdicComplete (maximalIdeal A) A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    [IsAdicComplete (maximalIdeal B) B]
    [Algebra (ResidueField A) B]
    (hB : RingHom.FormallySmoothNAdic.{max u v}
      (algebraMap (ResidueField A) B) (maximalIdeal B)) :
    ∃ (C : Type (max u v)) (_ : CommRing C) (_ : IsNoetherianRing C)
      (_ : IsLocalRing C) (_ : IsAdicComplete (maximalIdeal C) C)
      (f : A →+* C) (_ : IsLocalHom f),
      RingHom.FormallySmoothNAdic.{max u v} f (maximalIdeal C) ∧
        letI : Algebra A C := f.toAlgebra
        Nonempty ((ResidueField A ⊗[A] C) ≃ₐ[ResidueField A] B)
```

## Tag 07NS, a remark

[Tag 07NS](https://stacks.math.columbia.edu/tag/07NS) in the Stacks Project.

**`exists_completeLocal_formallySmooth_lift_with_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean, line 3532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GeometricallyRegular/FormalSmoothness.lean#L3532). References: EGA 0 (22.2.7), “(i)”.

> **Stacks 07NS.** Consider local homomorphisms `A → A' → B` of Noetherian complete local
> rings such that `A → A'` induces an isomorphism on residue fields. If the special fibre of `B`
> over `A'` is formally smooth, then it is induced by an adically formally smooth Noetherian
> complete local `A`-algebra `C` mapping locally to `B`.
>
> The completed base change of `C` to `A'` is again Noetherian, complete, local, and flat over
> `A'`, and its induced map to `B` is surjective. Moreover, `C → B` is surjective when `A → A'`
> is, finite when `A → A'` is finite, and the completed base-change map is an isomorphism when
> `A' → B` is flat.

```lean
public theorem exists_completeLocal_formallySmooth_lift_with_baseChange
    {A : Type u} {A' : Type v} {B : Type w}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsAdicComplete (maximalIdeal A) A]
    [CommRing A'] [IsNoetherianRing A'] [IsLocalRing A']
    [IsAdicComplete (maximalIdeal A') A']
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    [IsAdicComplete (maximalIdeal B) B]
    (f : A →+* A') [IsLocalHom f]
    (g : A' →+* B) [IsLocalHom g]
    (hf : Function.Bijective (ResidueField.map f))
    (hB : letI : Algebra A' B := g.toAlgebra
      RingHom.FormallySmoothNAdic.{max u v w}
        (algebraMap (ResidueField A') (ResidueField A' ⊗[A'] B))
        (maximalIdeal (ResidueField A' ⊗[A'] B))) :
    ∃ (C : Type (max u v w)) (_ : CommRing C) (_ : IsNoetherianRing C)
      (_ : IsLocalRing C) (_ : IsAdicComplete (maximalIdeal C) C)
      (a : A →+* C) (_ : IsLocalHom a)
      (c : C →+* B) (_ : IsLocalHom c),
      c.comp a = g.comp f ∧
      RingHom.FormallySmoothNAdic.{max u v w} a (maximalIdeal C) ∧
      (letI : Algebra A A' := f.toAlgebra
       letI : Algebra A' B := g.toAlgebra
       letI : Algebra A C := a.toAlgebra
       letI : Algebra (ResidueField A) (ResidueField A') := (ResidueField.map f).toAlgebra
       ∃ e : (ResidueField A ⊗[A] C) ≃ₐ[ResidueField A]
           (ResidueField A' ⊗[A'] B),
         (∀ x : ResidueField A,
           e (Algebra.TensorProduct.includeLeft (R := A) (S := ResidueField A)
             (A := ResidueField A) (B := C) x) =
             Algebra.TensorProduct.includeLeft (R := A') (S := ResidueField A')
               (A := ResidueField A') (B := B) (ResidueField.map f x)) ∧
         (∀ y : C,
           e (Algebra.TensorProduct.includeRight (R := A)
             (A := ResidueField A) (B := C) y) =
           Algebra.TensorProduct.includeRight (R := A')
             (A := ResidueField A') (B := B) (c y))) ∧
      (letI : Algebra A A' := f.toAlgebra
       letI : Algebra A C := a.toAlgebra
       let T := C ⊗[A] A'
       let iA' : A' →+* T :=
         (Algebra.TensorProduct.includeRight (R := A) (A := C) (B := A')).toRingHom
       let J : Ideal T := (maximalIdeal A').map iA'
       let D := AdicCompletion J T
       ∃ (t : T →+* B) (q : D →+* B)
         (_ : IsNoetherianRing D) (_ : IsLocalRing D),
         t.comp (Algebra.TensorProduct.includeLeft (R := A) (S := A)
           (A := C) (B := A')).toRingHom = c ∧
         t.comp iA' = g ∧
         q.comp (algebraMap T D) = t ∧
         IsAdicComplete (maximalIdeal D) D ∧
         ((algebraMap T D).comp iA').Flat ∧
         Function.Surjective q ∧
         (Function.Surjective f → Function.Surjective c) ∧
         (f.Finite → c.Finite) ∧
         (g.Flat → Function.Bijective q))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.41, Tag 07EK](https://stacks.math.columbia.edu/tag/07EK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
