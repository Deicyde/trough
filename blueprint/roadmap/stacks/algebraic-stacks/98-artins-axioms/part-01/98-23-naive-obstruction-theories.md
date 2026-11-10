---
declaration: section
origin: cited
lean: DerivedCategory.extIntoFieldEquivDualBaseChangeHomology, DerivedCategory.extIntoFieldEquivDualBaseChangeHomology_smul, DerivedCategory.extIntoFieldEquivDualBaseChangeHomology_naturality, DerivedCategory.extIntoFieldEquivDualBaseChangeHomology_restrictScalars, Deformation.Artin.exists_squareZeroExtension_killing_cotangent_morphism, AlgebraicGeometry.finiteType_residueField_of_isClosed_singleton, Deformation.Artin.surjective_derivedFibre_neg_one_iff_injective_extOne, Deformation.Artin.injective_derivedFibre_zero_iff_surjective_extZero
statement: formalized
proof: formalized
---

# 98.23 Naive obstruction theories

Section 98.23 of the Stacks Project, [Tag 07YJ](https://stacks.math.columbia.edu/tag/07YJ). 7 tags here are carried by 54 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07YK, a lemma

[Tag 07YK](https://stacks.math.columbia.edu/tag/07YK) in the Stacks Project.

**`DerivedCategory.extIntoFieldEquivDualBaseChangeHomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean#L537). The attribute's comment: “equivalence”.

> Ext into a field is the linear dual of the cohomology of canonical derived base change.

```lean
public noncomputable def extIntoFieldEquivDualBaseChangeHomology
    {A : Type uA} {k : Type uk} [CommRing A] [Field k] (f : A →+* k)
    (E : DerivedCategory.Minus (ModuleCat.{max v uA uk} A)) (i : ℤ) :
    DerivedCategory.Ext E.1
        ((DerivedCategory.singleFunctor (ModuleCat.{max v uA uk} A) 0).obj
          ((ModuleCat.restrictScalars f).obj (ModuleCat.of k (ULift.{max v uA} k)))) i ≃+
      ((DerivedCategory.homologyFunctor (ModuleCat.{max v uA uk} k) (-i)).obj
        ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{uA, uk, v}
          f).functor.obj E.1) ⟶ ModuleCat.of k (ULift.{max v uA} k))
```

**`DerivedCategory.extIntoFieldEquivDualBaseChangeHomology_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean#L559). The attribute's comment: “k-linearity”.

> The Ext/base-change duality equivalence respects the intrinsic scalar action of `k`.

```lean
public theorem extIntoFieldEquivDualBaseChangeHomology_smul
    {A : Type uA} {k : Type uk} [CommRing A] [Field k] (f : A →+* k)
    (E : DerivedCategory.Minus (ModuleCat.{max v uA uk} A)) (i : ℤ)
    (x : k) (α : DerivedCategory.Ext E.1
      ((DerivedCategory.singleFunctor (ModuleCat.{max v uA uk} A) 0).obj
        ((ModuleCat.restrictScalars f).obj (ModuleCat.of k (ULift.{max v uA} k)))) i) :
  extIntoFieldEquivDualBaseChangeHomology f E i (x • α) =
      x • extIntoFieldEquivDualBaseChangeHomology f E i α
```

**`DerivedCategory.extIntoFieldEquivDualBaseChangeHomology_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean#L586). The attribute's comment: “naturality in the derived object”.

> The Ext/base-change duality equivalence is contravariantly natural in derived objects.

```lean
public theorem extIntoFieldEquivDualBaseChangeHomology_naturality
    {A : Type uA} {k : Type uk} [CommRing A] [Field k] (f : A →+* k)
    (E E' : DerivedCategory.Minus (ModuleCat.{max v uA uk} A)) (i : ℤ)
    (g : E'.1 ⟶ E.1)
    (α : DerivedCategory.Ext E.1
      ((DerivedCategory.singleFunctor (ModuleCat.{max v uA uk} A) 0).obj
        ((ModuleCat.restrictScalars f).obj (ModuleCat.of k (ULift.{max v uA} k)))) i) :
    extIntoFieldEquivDualBaseChangeHomology f E' i (g ≫ α) =
      (DerivedCategory.homologyFunctor (ModuleCat.{max v uA uk} k) (-i)).map
        ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{uA, uk, v}
          f).functor.map g) ≫
        extIntoFieldEquivDualBaseChangeHomology f E i α
```

**`DerivedCategory.extIntoFieldEquivDualBaseChangeHomology_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/IntoField.lean#L605). The attribute's comment: “naturality under change of source ring”.

> The duality intertwines pullback of Ext classes across `A → B` with the dual of the
> canonical map `E ⊗ᴸ_A k ⟶ F ⊗ᴸ_B k`.

```lean
public theorem extIntoFieldEquivDualBaseChangeHomology_restrictScalars
    {A : Type uA} {B : Type uB} {k : Type uk}
    [CommRing A] [CommRing B] [Field k] (f : A →+* B) (g : B →+* k)
    (E : DerivedCategory.Minus (ModuleCat.{max v uA uB uk} A))
    (F : DerivedCategory.Minus (ModuleCat.{max v uA uB uk} B))
    (h : E.1 ⟶ (ModuleCat.restrictScalars f).mapDerivedCategory.obj F.1) (i : ℤ)
    (α : DerivedCategory.Ext F.1
      ((DerivedCategory.singleFunctor (ModuleCat.{max v uA uB uk} B) 0).obj
        ((ModuleCat.restrictScalars g).obj (ModuleCat.of k (ULift.{max v uA uB} k)))) i) :
    extIntoFieldEquivDualBaseChangeHomology.{uA, uk, max v uB} (g.comp f) E i
        (extIntoFieldRestriction.{uA, uk, v, uB} f g E.1 F.1 h i α) =
        (DerivedCategory.homologyFunctor (ModuleCat.{max v uA uB uk} k) (-i)).map
        (derivedBaseChangeMap.{uA, uk, v, uB} f g E.1 F.1 h) ≫
        extIntoFieldEquivDualBaseChangeHomology.{uB, uk, max v uA} g F i α
```

## Tag 07YL, a lemma

[Tag 07YL](https://stacks.math.columbia.edu/tag/07YL) in the Stacks Project.

**`Deformation.Artin.exists_squareZeroExtension_killing_cotangent_morphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/NaiveCotangent/DerivedSquareZeroExtension.lean, line 1083](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/NaiveCotangent/DerivedSquareZeroExtension.lean#L1083).

> **Stacks Project, Tag 07YL.** Let `Λ → A → k = κ(𝔭)` be finite type maps of Noetherian
> rings and let `ξ : E ⟶ NL_{A/Λ}` be a morphism in `D⁻(A)` such that `H⁻¹(ξ ⊗ᴸ k)` is not
> surjective.  Then there is a surjection of `Λ`-algebras `A' → A` whose kernel `I` has square
> zero and is isomorphic to `k` as an `A`-module, which does not change differentials modulo
> `𝔭`, and for which the composite of `ξ` with `NL_{A/Λ} ⟶ NL_{A/A'}` vanishes.

```lean
public theorem exists_squareZeroExtension_killing_cotangent_morphism
    (Λ A : Type u) [CommRing Λ] [CommRing A] [Algebra Λ A]
    [IsNoetherianRing Λ] [IsNoetherianRing A] [Algebra.FiniteType Λ A]
    (p : Ideal A) [p.IsPrime] [Algebra.FiniteType A p.ResidueField]
    (T : DerivedTensorProduct A)
    (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t
      (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A)
    (hξ : ¬ Function.Surjective
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-1)).map
        ((T.tensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A p.ResidueField))).map ξ))) :
    ∃ (A' : Type u) (_ : CommRing A') (_ : Algebra Λ A') (_ : Algebra A' A)
      (_ : IsScalarTower Λ A' A),
      Function.Surjective (algebraMap A' A) ∧
      let I := RingHom.ker (algebraMap A' A)
      I ^ 2 = ⊥ ∧
      ∃ (_ : Module A I),
        (∀ (a' : A') (x : I), (algebraMap A' A a') • x = a' • x) ∧
        Nonempty (I ≃ₗ[A] p.ResidueField) ∧
        Function.Bijective (differentialsBaseChangeMap Λ A' A p.ResidueField) ∧
        ξ ≫ naiveCotangentBaseMap Λ A' A = 0
```

## Tag 07YM, a lemma

[Tag 07YM](https://stacks.math.columbia.edu/tag/07YM) in the Stacks Project.

**`AlgebraicGeometry.finiteType_residueField_of_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteTypePoint.lean#L151). The attribute's comment: “the use of closedness: the residue field at the point is of finite type”.

> The residue field at a closed point of an affine scheme is of finite type over the ring.
>
> This is the use that the converse direction of [Stacks, Tag 07YM] makes of closedness: it is
> the finiteness hypothesis under which [Stacks, Tag 07YL] builds its square-zero extension, and
> the source notes that the step "fails if `u₀` is not closed".

```lean
public theorem finiteType_residueField_of_isClosed_singleton {A : Type u} [CommRing A]
    {u₀ : Spec (CommRingCat.of A)}
    (hu₀ : IsClosed ({u₀} : Set (Spec (CommRingCat.of A)))) :
    letI : u₀.asIdeal.IsPrime := u₀.isPrime
    Algebra.FiniteType A u₀.asIdeal.ResidueField
```

**`Deformation.Artin.surjective_derivedFibre_neg_one_iff_injective_extOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersality.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersality.lean#L212). The attribute's comment: “condition (2) in degree -1 as injectivity of Ext¹(NL\_\{A/Λ}, k) → Ext¹(E, k)”.

> **Stacks 07YM, condition (2) in degree `-1`.** For a morphism `ξ : E ⟶ NL_{A/Λ}` of
> `D⁻(A)` and a ring map `A ⟶ k` to a field, the map
> `H^{-1}(E ⊗ᴸ_A k) ⟶ H^{-1}(NL_{A/Λ} ⊗ᴸ_A k)` is surjective exactly when the induced map
> `Ext¹_A(NL_{A/Λ}, k) ⟶ Ext¹_A(E, k)`, that is precomposition with `ξ`, is injective. This is
> the first of the two invocations of Stacks 07YK in the proof of Stacks 07YM: in the direction
> `(1) ⇒ (2)` a failure of the surjectivity produces a nonzero class of `Ext¹_A(NL_{A/Λ}, k)`
> killed by `ξ`, which is the input of Stacks 07YL, and in the direction `(2) ⇒ (1)` the
> injectivity is what forces the obstruction class to vanish.

```lean
public theorem surjective_derivedFibre_neg_one_iff_injective_extOne
    {Λ A k : Type u} [CommRing Λ] [CommRing A] [Field k] [Algebra Λ A] (f : A →+* k)
    (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A) :
    Function.Surjective
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) (-1)).map
          ((totalDerivedExtensionScalars.{u, u, u} f).functor.map ξ)) ↔
      Function.Injective
        (fun α : DerivedCategory.Ext (derivedNaiveCotangentComplex Λ A)
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              ((ModuleCat.restrictScalars f).obj (ModuleCat.of k (ULift.{u} k)))) 1 =>
          ξ ≫ α)
```

**`Deformation.Artin.injective_derivedFibre_zero_iff_surjective_extZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersality.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersality.lean#L236). The attribute's comment: “condition (2) in degree 0 as surjectivity of Ext⁰(NL\_\{A/Λ}, k) → Ext⁰(E, k)”.

> **Stacks 07YM, condition (2) in degree `0`.** For a morphism `ξ : E ⟶ NL_{A/Λ}` of
> `D⁻(A)` and a ring map `A ⟶ k` to a field, the map `H^0(E ⊗ᴸ_A k) ⟶ H^0(NL_{A/Λ} ⊗ᴸ_A k)` is
> injective exactly when the induced map `Ext⁰_A(NL_{A/Λ}, k) ⟶ Ext⁰_A(E, k)`, that is
> precomposition with `ξ`, is surjective. This is the second of the two invocations of Stacks
> 07YK in the proof of Stacks 07YM: condition (ii) identifies the right-hand map with the map
> `Der_Λ(A, k) ⟶ T_x(k)` from tangent vectors of `U` at `u₀` to infinitesimal deformations of
> `x₀`, whose surjectivity is what versality provides.

```lean
public theorem injective_derivedFibre_zero_iff_surjective_extZero
    {Λ A k : Type u} [CommRing Λ] [CommRing A] [Field k] [Algebra Λ A] (f : A →+* k)
    (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A) :
    Function.Injective
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) 0).map
          ((totalDerivedExtensionScalars.{u, u, u} f).functor.map ξ)) ↔
      Function.Surjective
        (fun α : DerivedCategory.Ext (derivedNaiveCotangentComplex Λ A)
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              ((ModuleCat.restrictScalars f).obj (ModuleCat.of k (ULift.{u} k)))) 0 =>
          ξ ≫ α)
```

**`Deformation.Artin.exists_pow_inf_eq_bot_of_mul_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersality.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersality.lean#L267). The attribute's comment: “the Artin–Rees step of (1) ⇒ (2): (p')^n ∩ I = 0 for some n > 1”.

> **Stacks 07YM, the Artin–Rees step of the implication `(1) ⇒ (2)`.** Let `A'` be a
> Noetherian ring and let `p'` and `I` be ideals with `p' · I = 0`. Then `(p')^n ∩ I = 0` for
> some `n > 1`.
>
> In the source `A' ⟶ A` is the square-zero extension supplied by Stacks 07YL, `I` is its
> kernel and `p' = Ker(A' ⟶ k)` is the prime over the closed point `u₀`; the kernel is a
> one-dimensional `k`-vector space, so it is annihilated by `p'`, and the conclusion is what
> makes the kernel of `A'/(p')^n ⟶ A/p^n` equal to `I` and hence that map a small extension of
> local Artinian rings. The proof is the Artin–Rees lemma (Stacks 00IN) applied to the ideal
> `p'` of `A'` and the submodule `I` of `A'`: beyond the Artin–Rees constant `c` the
> intersection `(p')^n ∩ I` is contained in `(p')^{n - c} · I`, which vanishes as soon as
> `n > c`.

```lean
public theorem exists_pow_inf_eq_bot_of_mul_eq_bot {A' : Type*} [CommRing A']
    [IsNoetherianRing A'] (p' I : Ideal A') (hpI : p' * I = ⊥) :
    ∃ n > 1, p' ^ n ⊓ I = ⊥
```

**`Deformation.Artin.surjective_derivedTensorFibre_neg_one_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeNegOne.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeNegOne.lean#L124). The attribute's comment: “(1) implies (2), degree -1”.

> **Stacks 07YM, `(1) ⇒ (2)` in degree `-1`.** Let `x` be a family over `Spec A` whose
> deformation theory is controlled by `ξ : E ⟶ NL_{A/Λ}` as in hypothesis (i) of the tag: `x` lifts
> across a deformation situation `A' → A` whenever `ξ` composed with `NL_{A/Λ} ⟶ NL_{A/A'}`
> vanishes. If `x` is versal at a *closed* point `u₀` of `Spec A`, then the map
> `H^{-1}(E ⊗ᴸ_A κ(u₀)) ⟶ H^{-1}(NL_{A/Λ} ⊗ᴸ_A κ(u₀))` on the derived fibre at `u₀` is surjective.
>
> Were it not, [Stacks, Tag 07YL] would supply a square-zero extension `A' → A` killing `ξ` and
> not changing differentials modulo `κ(u₀)`, hypothesis (i) would lift `x` to `Spec A'`, and the
> Artin–Rees step would turn the extension into a *small* extension
> `A' ⧸ (𝔭') ^ n ⟶ A ⧸ 𝔭 ^ n` of `𝒞_Λ` which [Stacks, Tag 06H0] makes an essential surjection.
> Versality applied to the arrow joining the restrictions of `x` and of its lift to the two
> Artinian quotients then lifts `A` through that extension, hence splits it — contradicting
> essential surjectivity.

```lean
public theorem surjective_derivedTensorFibre_neg_one_of_isVersalAt
    (hclosed : IsClosed ({u₀} : Set (Spec (CommRingCat.of A))))
    (hLifts : ∀ (A' : Type u) [CommRing A'] [Algebra Λ A'] [Algebra A' A]
      [IsScalarTower Λ A' A] (D : SquareZeroThickening A B S hS toS hA A'),
      D.q = algebraMap A' A →
      Spec.map (CommRingCat.ofHom (algebraMap Λ A')) ≫ baseMap = B.inclusion.map D.toS' →
      ξ ≫ naiveCotangentBaseMap Λ A' A = 0 →
      Nonempty ((Under.post p).Fiber (Under.mk (eqToHom hx ≫ D.arrow))))
    (hversal : IsVersalAt (Over.mk toS) (p ⋙ Over.post B.inclusion) u₀ x
      (by change (Over.post B.inclusion).obj (p.obj x) = _; rw [hx]; rfl)) :
    Function.Surjective
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-1)).map
        ((T.tensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A u₀.asIdeal.ResidueField))).map ξ))
```

**`Deformation.Artin.surjective_comp_of_liftsAtResiduePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZero.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZero.lean#L191). The attribute's comment: “(1) implies (2), degree 0: precomposition with xi is surjective”.

> **Stacks 07YM, the surjectivity hypothesis (ii) turns versality into.** If the lifting
> property defining versality holds at the point of `Spec A` determined by the `A`-algebra
> structure of a field `k`, then precomposition with `ξ` is surjective on morphisms
> `NL_{A/Λ} ⟶ k[0]` of `D(A)`.
>
> This is `Deformation.Artin.surjective_canonicalTangentMap_of_liftsAtResiduePoint`, the
> surjectivity of the map `Der_Λ(A, k) ⟶ T_x(k)` on tangent spaces, read through the functorial
> isomorphism of hypothesis (ii): by
> `Deformation.Artin.tangentEquiv_canonicalTangentMap` that isomorphism carries the image of a
> tangent vector `θ` to `ξ` followed by the augmentation followed by `θ`, so a surjection onto
> `T_x(k)` becomes a surjection onto the morphisms `E ⟶ k[0]` factoring through `ξ`. The two
> identifications of `T_x(k)` with classes of lifts are bijections, so the surjectivity of the
> composite in that statement is the surjectivity of the tangent map itself.

```lean
public theorem surjective_comp_of_liftsAtResiduePoint [Mono baseMap]
    (hlifts : LiftsAtResiduePoint (Λ := R) (k := k) iR (p ⋙ Over.post B.inclusion)
      (Over.mk toS) x hxS (Spec.map (CommRingCat.ofHom (algebraMap A k)))) :
    Function.Surjective (fun f : derivedNaiveCotangentComplex Λ A ⟶
        (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A k) =>
      ξ ≫ f)
```

**`Deformation.Artin.injective_derivedTensorFibre_zero_of_liftsAtResiduePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZero.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZero.lean#L268). The attribute's comment: “(1) implies (2), degree 0, at a field in the site”.

> **Stacks 07YM, condition (2) in degree `0` from the lifting property.** If the lifting
> property defining versality holds at the point of `Spec A` determined by the `A`-algebra
> structure of a field `k` no larger than `max ℵ₀ #A`, then the map
> `H^0(E ⊗ᴸ_A k) ⟶ H^0(NL_{A/Λ} ⊗ᴸ_A k)` is injective.
>
> `Deformation.Artin.injective_derivedTensorFibre_zero_iff_surjective_comp` turns the conclusion
> into the surjectivity of precomposition with `ξ` on morphisms into `ULift k`, restricted along
> `A ⟶ k`; `Deformation.Artin.uliftRestrictScalarsIso` identifies that coefficient module with
> the `A`-module `ULift k`, at which
> `Deformation.Artin.surjective_comp_of_liftsAtResiduePoint` supplies the surjectivity. The
> lifting property is moved from `k` to `ULift k` by
> `Deformation.Artin.liftsAtResiduePoint_changeResidueField`, and the three memberships in the
> site that the lift chain asks of `ULift k` are derived from the cardinality bound.

```lean
public theorem injective_derivedTensorFibre_zero_of_liftsAtResiduePoint [Mono baseMap]
    (hmk : Cardinal.mk k ≤ max Cardinal.aleph0 (Cardinal.mk A))
    (hlifts : LiftsAtResiduePoint (Λ := R) (k := k) iR (p ⋙ Over.post B.inclusion)
      (Over.mk toS) x hxS (Spec.map (CommRingCat.ofHom (algebraMap A k)))) :
    Function.Injective
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
        ((T.tensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A k))).map ξ))
```

**`Deformation.Artin.injective_derivedTensorFibre_zero_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZero.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZero.lean#L357). The attribute's comment: “(1) implies (2), degree 0”.

> **Stacks 07YM, `(1) ⇒ (2)` in degree `0`.** Let `x` be a family over `Spec A` whose tangent
> theory is represented by `ξ : E ⟶ NL_{A/Λ}` as in hypothesis (ii) of the tag. If `x` is versal
> at a point `u₀` of `Spec A`, then the map
> `H^0(E ⊗ᴸ_A κ(u₀)) ⟶ H^0(NL_{A/Λ} ⊗ᴸ_A κ(u₀))` on the derived fibre at `u₀` is injective.
>
> Versality is the lifting property at the residue-field point
> (`Deformation.Artin.liftsAtResiduePoint_of_isVersalAt`), the residue field at a prime of `A` is
> no larger than `max ℵ₀ #A` (`Cardinal.mk_residueField_le_max`), and
> `Deformation.Artin.specMap_primeResidueFieldAlgebra_comp_fromSpecStalk` is the compatibility of
> the residue-field point with the local ring of `S` at the image of `u₀`; with those,
> `Deformation.Artin.injective_derivedTensorFibre_zero_of_liftsAtResiduePoint` applies.
>
> No closedness of the point is used: the source invokes closedness only for the `H^{-1}` half of
> condition (2).

```lean
public theorem injective_derivedTensorFibre_zero_of_isVersalAt [Mono baseMap]
    (hversal : IsVersalAt (Over.mk toS) (p ⋙ Over.post B.inclusion) u₀ x
      (by change (Over.post B.inclusion).obj (p.obj x) = _; rw [hx]; rfl)) :
    Function.Injective
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
        ((T.tensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A u₀.asIdeal.ResidueField))).map ξ))
```

**`Deformation.Artin.bijective_comp_naiveCotangentToDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZeroConverse.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZeroConverse.lean#L343). The attribute's comment: “Ext^0\_A(NL\_\{A/Lambda}, M) = Der\_Lambda(A, M)”.

> **`Ext⁰_A(NL_{A/Λ}, M) = Der_Λ(A, M)`.** Composing the augmentation
> `NL_{A/Λ} ⟶ Ω_{A/Λ}[0]` with a module map `Ω_{A/Λ} ⟶ M` is a bijection onto the morphisms
> `NL_{A/Λ} ⟶ M[0]` of `D(A)`.
>
> This is the identification the proof of [Stacks, Tag 07YM] writes as
> `Ext⁰_A(NL_{A/Λ}, k) = Der_Λ(A, k)`. The naive cotangent complex lies in degrees `≤ 0` and
> `M[0]` in degrees `≥ 0`, so `H⁰` computes the morphisms between them
> (`DerivedCategory.bijective_homologyFunctor_map_of_isLE_of_isGE`); the augmentation is an
> isomorphism on `H⁰`
> (`Deformation.Artin.isIso_homologyFunctor_map_naiveCotangentToDifferentials`), and the single
> functor of `D(A)` is fully faithful, so a morphism `Ω_{A/Λ}[0] ⟶ M[0]` is a module map.

```lean
public theorem bijective_comp_naiveCotangentToDifferentials (M : ModuleCat.{u} A) :
    Function.Bijective (fun θ : differentialsModule Λ A ⟶ M =>
      naiveCotangentToDifferentials Λ A ≫
        (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).map θ)
```

**`Deformation.Artin.surjective_canonicalTangentMap_of_surjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZeroConverse.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZeroConverse.lean#L419). The attribute's comment: “(2) implies (1), degree 0: the map on tangent spaces is surjective”.

> **Stacks 07YM, `(2) ⇒ (1)` in degree `0`.** If precomposition with `ξ` is surjective on
> morphisms `NL_{A/Λ} ⟶ k[0]` of `D(A)`, then the map `Der_Λ(A, k) ⟶ T_x(k)` on tangent spaces
> is surjective.
>
> The hypothesis is condition (2) of the tag in degree `0`: by
> `Deformation.Artin.injective_derivedTensorFibre_zero_iff_surjective_comp` the injectivity of
> `H^0(ξ ⊗ᴸ_A k)` is exactly this surjectivity, and
> `DerivedCategory.surjective_extZero_comp_iff_surjective_comp` reads it on `Ext⁰` if wanted.
> The conclusion is the first condition of the versality criterion of Stacks 06IU, read through
> the identification of `T_x(k)` with the infinitesimal deformations of `x₀`.
>
> The source's sentence is that the map on tangent spaces is the dual of `H^0(ξ ⊗ᴸ_A k)` under
> `Ext⁰_A(NL_{A/Λ}, k) = Der_Λ(A, k)` and `Ext⁰_A(E, k) = T_x(k)`. The second identification is
> hypothesis (ii), and `Deformation.Artin.tangentEquiv_canonicalTangentMap` is its value on the
> map on tangent spaces: a tangent vector `θ` goes to `ξ` followed by the augmentation followed
> by `θ`. The first identification is
> `Deformation.Artin.bijective_comp_naiveCotangentToDifferentials`, which is what turns the
> arbitrary morphism `NL_{A/Λ} ⟶ k[0]` produced by the hypothesis into such a `θ`.

```lean
public theorem surjective_canonicalTangentMap_of_surjective_comp
    (hsurj : Function.Surjective (fun f : derivedNaiveCotangentComplex Λ A ⟶
        (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A k) =>
      ξ ≫ f)) :
    Function.Surjective (canonicalTangentMap Λ A k B S hS toS hA p x hx hp hRS hΩ hk baseMap
      baseFactorization)
```

**`Deformation.Artin.exists_extends_of_surjective_canonicalTangentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZeroConverse.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDegreeZeroConverse.lean#L481). The attribute's comment: “(2) implies (1): an infinitesimal deformation over the dual numbers extends”.

> **Stacks 07YM, `(2) ⇒ (1)` at the dual numbers.** If the map `Der_Λ(A, k) ⟶ T_x(k)` on
> tangent spaces is surjective, then every lift of `x₀` along the square-zero immersion
> `Spec k ⟶ Spec k[k]` extends to `x`: its structure arrow composes with an arrow from its
> target to `x` to give the chosen restriction arrow.
>
> This is the exact converse of `Deformation.Artin.exists_extends_of_liftsAtResiduePoint`, and
> is the dual-numbers content of the first condition of the versality criterion of Stacks 06IU.
>
> The class of the lift is hit by a tangent vector `θ`, through the two bijections
> `Deformation.Artin.canonicalFieldBaseChangeEquiv` and the tangent functor's `liftEquiv`. By
> `Deformation.Artin.canonicalFieldBaseChangeEquiv_canonicalTangentMap` that class is also the
> class of the connecting arrow `χ` attached to *any* lift `(y, φ)` of `x` along
> `Deformation.Artin.canonicalDualNumbersArrow θ`, one of which exists because `p` is fibred in
> groupoids (`Deformation.Artin.exists_canonicalDualNumbersLift`). Two lifts in one class are
> isomorphic over `k[k]` compatibly with their arrows from `x₀`, so the isomorphism's component
> at the target carries the given lift's structure arrow to `χ`, and
> `Deformation.Artin.canonicalDualNumbersConnectingArrow_fac` says `χ ≫ φ` is the chosen
> restriction arrow.
>
> `Mono baseMap` is not needed here, although the forward direction needs it: it enters the
> forward direction through `Deformation.Artin.exists_unique_eq_canonicalDualNumbersArrow`, which
> recovers a tangent vector from an arrow of the site, and this direction is handed the tangent
> vector instead.

```lean
public theorem exists_extends_of_surjective_canonicalTangentMap
    (hsurj : Function.Surjective (canonicalTangentMap Λ A k B S hS toS hA p x hx hp hRS hΩ hk
      baseMap baseFactorization)) :
    letI : p.IsFibered := hp.isFibered
    ∀ (w : (Under.post p).Fiber (Under.mk (eqToHom
          (((Functor.chosenPullbacks p).pullbackFunctor
            (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
              (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj ⟨x, hx⟩).2 ≫
        squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk
          (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B)))),
      ∃ b : w.1.right ⟶ x,
        w.1.hom ≫ b = (Functor.chosenPullbacks p).map
          (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
            (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl) ⟨x, hx⟩
```

**`Deformation.Artin.surjective_derivedTensorFibre_neg_one_iff_injective_extOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDerivedFibre.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDerivedFibre.lean#L84). The attribute's comment: “condition (2) in degree -1, through a chosen derived tensor product”.

> **Stacks 07YM, condition (2) in degree `-1`.** For a morphism `ξ : E ⟶ NL_{A/Λ}` of
> `D⁻(A)` and a field `k` which is an `A`-algebra, the map
> `H^{-1}(E ⊗ᴸ_A k) ⟶ H^{-1}(NL_{A/Λ} ⊗ᴸ_A k)`, formed through a chosen derived tensor product,
> is surjective exactly when precomposition with `ξ` is injective on
> `Ext¹_A(−, k)`, that is when `Ext¹_A(NL_{A/Λ}, k) ⟶ Ext¹_A(E, k)` is injective.
>
> This is `Deformation.Artin.surjective_derivedFibre_neg_one_iff_injective_extOne`, which proves
> the same statement for the total derived extension of scalars, composed with the comparison
> `Deformation.Artin.surjective_derivedTensorFibre_iff_surjective_derivedExtensionScalars` of
> the two presentations of the derived fibre.

```lean
public theorem surjective_derivedTensorFibre_neg_one_iff_injective_extOne
    (T : DerivedTensorProduct A) (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A) :
    Function.Surjective
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-1)).map
          ((T.tensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A k))).map ξ)) ↔
      Function.Injective
        (fun α : DerivedCategory.Ext (derivedNaiveCotangentComplex Λ A)
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              ((ModuleCat.restrictScalars (algebraMap A k)).obj
                (ModuleCat.of k (ULift.{u} k)))) 1 =>
          ξ ≫ α)
```

**`Deformation.Artin.injective_derivedTensorFibre_zero_iff_surjective_extZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDerivedFibre.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDerivedFibre.lean#L113). The attribute's comment: “condition (2) in degree 0, through a chosen derived tensor product”.

> **Stacks 07YM, condition (2) in degree `0`.** For a morphism `ξ : E ⟶ NL_{A/Λ}` of
> `D⁻(A)` and a field `k` which is an `A`-algebra, the map
> `H^0(E ⊗ᴸ_A k) ⟶ H^0(NL_{A/Λ} ⊗ᴸ_A k)`, formed through a chosen derived tensor product, is
> injective exactly when precomposition with `ξ` is surjective on `Ext⁰_A(−, k)`, that is when
> `Ext⁰_A(NL_{A/Λ}, k) ⟶ Ext⁰_A(E, k)` is surjective.
>
> This is `Deformation.Artin.injective_derivedFibre_zero_iff_surjective_extZero` composed with
> the comparison
> `Deformation.Artin.injective_derivedTensorFibre_iff_injective_derivedExtensionScalars` of the
> two presentations of the derived fibre.

```lean
public theorem injective_derivedTensorFibre_zero_iff_surjective_extZero
    (T : DerivedTensorProduct A) (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A) :
    Function.Injective
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
          ((T.tensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A k))).map ξ)) ↔
      Function.Surjective
        (fun α : DerivedCategory.Ext (derivedNaiveCotangentComplex Λ A)
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              ((ModuleCat.restrictScalars (algebraMap A k)).obj
                (ModuleCat.of k (ULift.{u} k)))) 0 =>
          ξ ≫ α)
```

**`Deformation.Artin.injective_derivedTensorFibre_zero_iff_surjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDerivedFibre.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityDerivedFibre.lean#L140). The attribute's comment: “condition (2) in degree 0, as a condition on morphisms”.

> **Stacks 07YM, condition (2) in degree `0`, as a condition on morphisms.** The injectivity
> of `H^0(ξ ⊗ᴸ_A k)` is the surjectivity of precomposition with `ξ` on morphisms
> `NL_{A/Λ} ⟶ k[0]` of `D(A)`.
>
> This is `Deformation.Artin.injective_derivedTensorFibre_zero_iff_surjective_extZero` followed
> by `DerivedCategory.surjective_extZero_comp_iff_surjective_comp`: in degree `0` an `Ext` class
> *is* a morphism. It is the form in which condition (2) meets the tangent-space description of
> versality, whose statements are about morphisms of the derived category.

```lean
public theorem injective_derivedTensorFibre_zero_iff_surjective_comp
    (T : DerivedTensorProduct A) (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A) :
    Function.Injective
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
          ((T.tensor.flip.obj
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A k))).map ξ)) ↔
      Function.Surjective
        (fun f : derivedNaiveCotangentComplex Λ A ⟶
            (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              ((ModuleCat.restrictScalars (algebraMap A k)).obj
                (ModuleCat.of k (ULift.{u} k))) =>
          ξ ≫ f)
```

**`Deformation.Artin.exists_unique_eq_canonicalDualNumbersArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldArrowShape.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldArrowShape.lean#L171). The attribute's comment: “the dual-numbers arrows over Spec A are the tangent vectors”.

> **Stacks 07YM.** An arrow `ν : Spec k[k] ⟶ Spec A` of the site over `S` whose restriction
> along the square-zero immersion `Spec k ⟶ Spec k[k]` is the point of `Spec A` determined by the
> `A`-algebra structure of `k` is `Deformation.Artin.canonicalDualNumbersArrow θ` for a unique
> `A`-linear map `θ : Ω[A⁄Λ] →ₗ[A] k`.
>
> The ring map `r : A ⟶ k[k]` underlying `ν` exists because the two objects are spectra and
> `Spec` is full; the compatibility of `ν` with the structure morphisms to `S`, combined with the
> factorization of `Spec A ⟶ S` through the monomorphism `baseMap`, makes `r` a `Λ`-algebra map,
> and the hypothesis on the augmentation says that composing it with the projection `k[k] ⟶ k` is
> the structure map `A ⟶ k`. By
> `Deformation.Artin.exists_unique_kaehler_of_fstHom_comp_eq` such an `r` is
> `a ↦ (a mod 𝔭, θ (d a))` for a unique `θ`, which is the ring map of
> `canonicalDualNumbersArrow θ` by `Deformation.Artin.canonicalDualNumbersMap_apply`.

```lean
public theorem exists_unique_eq_canonicalDualNumbersArrow [Mono baseMap]
    (ν : squareZeroOver k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS)
          (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B) ⟶
        algebraOver A B S hS toS hA)
    (hν : squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk
          (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B) ≫ ν =
        algebraOverMapOfRingHom (algebraMap A k) B S hS toS
          (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl) :
    ∃! θ : Ω[A⁄Λ] →ₗ[A] k,
      ν = canonicalDualNumbersArrow Λ A k B S hS toS hA p x hx hp hRS hΩ hkk baseMap
        baseFactorization θ
```

**`Deformation.Artin.canonicalFieldBaseChangeEquiv_canonicalTangentMap_of_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldClassEquationLift.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldClassEquationLift.lean#L85). The attribute's comment: “the class equation at an arbitrary connecting arrow”.

> **Stacks 07YM, the class equation at an arbitrary connecting arrow.** Let `(y, φ)` be a lift
> of `x` along `Deformation.Artin.canonicalDualNumbersArrow θ`, and let `χ : x₀ ⟶ y` be any arrow
> from the chosen pullback of `x` to `Spec k`, lying over the square-zero immersion
> `Spec k ⟶ Spec k[k]`, which factors the chosen restriction arrow `η : x₀ ⟶ x` through `φ`. Then
> the class of `χ` as an infinitesimal deformation of `x₀` over the dual numbers of `k` is the
> image of `θ` under the map on tangent spaces, moved across the identification
> `Deformation.Artin.canonicalFieldBaseChangeEquiv` of lift classes over `A[k]` with lift classes
> over `k[k]`.
>
> Such a `χ` is the chosen connecting arrow
> `Deformation.Artin.canonicalDualNumbersConnectingArrow`: both lie over the square-zero immersion
> and both factor `η` through `φ`, so both are the arrow produced by the universal property of the
> strongly Cartesian arrow `φ`. The statement then reduces to
> `Deformation.Artin.canonicalFieldBaseChangeEquiv_canonicalTangentMap`.

```lean
public theorem canonicalFieldBaseChangeEquiv_canonicalTangentMap_of_fac
    (θ : Ω[A⁄Λ] →ₗ[A] k) (y : X) (φ : y ⟶ x)
    (hφ : p.IsHomLift
      (canonicalDualNumbersArrow Λ A k B S hS toS hA p x hx hp hRS hΩ hkk baseMap
        baseFactorization θ) φ) :
    letI : p.IsFibered := hp.isFibered
    ∀ (χ : (((Functor.chosenPullbacks p).pullbackFunctor
          (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
            (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj
          ⟨x, hx⟩).1 ⟶ y),
      p.IsHomLift
          (squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk
            (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B)) χ →
        χ ≫ φ = (Functor.chosenPullbacks p).map
            (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
              (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl) ⟨x, hx⟩ →
          ∀ hmem : (Under.post p).obj (Under.mk χ) =
            Under.mk (eqToHom (((Functor.chosenPullbacks p).pullbackFunctor
                (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
                  (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj
                ⟨x, hx⟩).2 ≫
              squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk
                (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B)),
          canonicalFieldBaseChangeEquiv A k B S hS toS hA p x hx hp hRS hk hAk hkk
              ((tangentFunctor A B S hS toS hA p x hx hp hRS).liftEquiv
                (⟨ModuleCat.of A k, hk⟩ : SiteModule A B)
                (canonicalTangentMap Λ A k B S hS toS hA p x hx hp hRS hΩ hk baseMap
                  baseFactorization θ)) =
            Quotient.mk _ ⟨Under.mk χ, hmem⟩
```

**`Deformation.Artin.exists_canonicalTangentMap_eq_of_extends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldTangentImage.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldTangentImage.lean#L107). The attribute's comment: “an extendable infinitesimal deformation is in the image of the tangent map”.

> **Stacks 07YM.** Let `x₀` be the chosen pullback of `x` to `Spec k` and let `w` represent an
> infinitesimal deformation of `x₀` over the dual numbers `k[k]`, that is a lift of `x₀` along the
> square-zero immersion `Spec k ⟶ Spec k[k]`. If the representative extends to `x`, that is if
> there is an arrow `b` from its target to `x` composing with it to the chosen restriction arrow
> `η : x₀ ⟶ x`, then the class of `w` is the image of a tangent vector `θ : Ω[A⁄Λ] →ₗ[A] k` under
> the map on tangent spaces, moved across the identification
> `Deformation.Artin.canonicalFieldBaseChangeEquiv`.
>
> Versality of `x` at the point is exactly what supplies the extension `b`; no other property of
> it enters. The `θ` is the one attached to the arrow of the site that `b` lies over by
> `Deformation.Artin.exists_unique_eq_canonicalDualNumbersArrow`, which applies because the
> restriction of that arrow along the square-zero immersion is forced, by the factorization
> through `η`, to be the point of `Spec A` determined by the `A`-algebra structure of `k`; the
> class is then computed by
> `Deformation.Artin.canonicalFieldBaseChangeEquiv_canonicalTangentMap_of_fac`.

```lean
public theorem exists_canonicalTangentMap_eq_of_extends [Mono baseMap] :
    letI : p.IsFibered := hp.isFibered
    ∀ (w : (Under.post p).Fiber (Under.mk (eqToHom
          (((Functor.chosenPullbacks p).pullbackFunctor
            (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
              (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj ⟨x, hx⟩).2 ≫
        squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk
          (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B))))
      (b : w.1.right ⟶ x),
      w.1.hom ≫ b = (Functor.chosenPullbacks p).map
          (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
            (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl) ⟨x, hx⟩ →
        ∃ θ : Ω[A⁄Λ] →ₗ[A] k,
          canonicalFieldBaseChangeEquiv A k B S hS toS hA p x hx hp hRS hk hAk hkk
              ((tangentFunctor A B S hS toS hA p x hx hp hRS).liftEquiv
                (⟨ModuleCat.of A k, hk⟩ : SiteModule A B)
                (canonicalTangentMap Λ A k B S hS toS hA p x hx hp hRS hΩ hk baseMap
                  baseFactorization θ)) =
            Quotient.mk _ w
```

**`Deformation.Artin.exists_extends_of_liftsAtResiduePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldVersalLift.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldVersalLift.lean#L262). The attribute's comment: “versality tested at the dual numbers of a residue field”.

> **Stacks 07YM, the dual-numbers instance of versality.** Let `x₀` be the chosen pullback of
> `x` to `Spec k` and let `w` be a lift of `x₀` along the square-zero immersion
> `Spec k ⟶ Spec k[k]`. If the lifting property defining versality holds at the point of
> `Spec A` determined by the `A`-algebra structure of `k`, then `w`'s structure arrow extends to
> `x`: there is an arrow `b` from its target to `x` composing with it to the chosen restriction
> arrow.
>
> This is the instantiation of `Deformation.Artin.IsVersalAt` at the surjection
> `k[k] ⟶ k` of `𝒞_R`, which is `Deformation.Artin.squareZeroArtinianProjection`; the objects
> `Deformation.Artin.squareZeroArtinianObj` and `Deformation.Artin.fieldArtinianObj` are the
> site's own square-zero ring and the field, so the two descriptions of the base — the spectrum
> of an object of `𝒞_R` over `Spec R`, and the site's square-zero object over `Spec A` — agree
> by `Deformation.Artin.squareZeroOver_post_eq` and
> `Deformation.Artin.algebraOver_post_eq`.

```lean
public theorem exists_extends_of_liftsAtResiduePoint
    (hkk : B.Contains (Spec (squareZeroRing k (ModuleCat.of k k))))
    (hlifts : LiftsAtResiduePoint (Λ := R) (k := k) iR (p ⋙ Over.post B.inclusion)
      (Over.mk toS) x hxS (Spec.map (CommRingCat.ofHom (algebraMap A k)))) :
    letI : p.IsFibered := hp.isFibered
    ∀ (w : (Under.post p).Fiber (Under.mk (eqToHom
          (((Functor.chosenPullbacks p).pullbackFunctor
            (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
              (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl)).obj ⟨x, hx⟩).2 ≫
        squareZeroArrow k B S hS (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hAk
          (⟨ModuleCat.of k k, hkk⟩ : SiteModule k B)))),
      ∃ b : w.1.right ⟶ x,
        w.1.hom ≫ b = (Functor.chosenPullbacks p).map
          (algebraOverMapOfRingHom (algebraMap A k) B S hS toS
            (Spec.map (CommRingCat.ofHom (algebraMap A k)) ≫ toS) hA hAk rfl) ⟨x, hx⟩
```

**`Deformation.Artin.surjective_canonicalTangentMap_of_liftsAtResiduePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldVersalLift.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldVersalLift.lean#L388). The attribute's comment: “(1) implies (2), degree 0: the map on tangent spaces is surjective”.

> **Stacks 07YM, the surjectivity of the map on tangent spaces.** If the lifting property
> defining versality holds at the point of `Spec A` determined by the `A`-algebra structure of
> `k`, then every infinitesimal deformation of `x₀` over the dual numbers of `k` is the image of
> a tangent vector `θ : Ω[A⁄Λ] →ₗ[A] k` under the map on tangent spaces, moved across
> `Deformation.Artin.canonicalFieldBaseChangeEquiv`.
>
> This is `Deformation.Artin.exists_extends_of_liftsAtResiduePoint`, which produces from
> versality the extension of a lift's structure arrow to `x`, composed with
> `Deformation.Artin.exists_canonicalTangentMap_eq_of_extends`, which computes the class of an
> extendable lift as the image of a tangent vector. Dually — Stacks 07YK — this surjectivity is
> the injectivity of `H^0(ξ ⊗ᴸ_A k)`, which is condition (2) of the tag in degree `0`.

```lean
public theorem surjective_canonicalTangentMap_of_liftsAtResiduePoint [Mono baseMap]
    (hlifts : LiftsAtResiduePoint (Λ := R) (k := k) iR (p ⋙ Over.post B.inclusion)
      (Over.mk toS) x hxS (Spec.map (CommRingCat.ofHom (algebraMap A k)))) :
    letI : p.IsFibered := hp.isFibered
    Function.Surjective (fun θ : Ω[A⁄Λ] →ₗ[A] k =>
      canonicalFieldBaseChangeEquiv A k B S hS toS hA p x hx hp hRS hk hAk hkk
        ((tangentFunctor A B S hS toS hA p x hx hp hRS).liftEquiv
          (⟨ModuleCat.of A k, hk⟩ : SiteModule A B)
          (canonicalTangentMap Λ A k B S hS toS hA p x hx hp hRS hΩ hk baseMap
            baseFactorization θ)))
```

**`Deformation.Artin.liftsAtResiduePoint_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldVersalLift.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityFieldVersalLift.lean#L493). The attribute's comment: “versality as the lifting property at the residue field of the prime”.

> **Stacks 07YM.** Versality of `x` at `u₀` is the lifting property at the point of `Spec A`
> determined by the algebra structure of the residue field `Ideal.ResidueField u₀.asIdeal` of the
> prime -- the field in which the whole 07YM lift chain is written.
>
> `Deformation.Artin.IsVersalAt` is literally the lifting property at the canonical
> residue-field point `Spec (U.left.residueField u₀) ⟶ U.left`
> (`Deformation.Artin.isVersalAt_iff_liftsAtResiduePoint`), and the property transports along an
> isomorphism of residue fields over the local ring
> (`Deformation.Artin.liftsAtResiduePoint_changeResidueField`); the isomorphism is the one
> induced by `AlgebraicGeometry.Scheme.Spec.residueFieldIso`, and it carries the canonical point
> to the one written here.

```lean
public theorem liftsAtResiduePoint_of_isVersalAt
    (hversal : IsVersalAt (Over.mk toS) q u₀ x hx) :
    LiftsAtResiduePoint (Λ := S.presheaf.stalk (basePoint (Over.mk toS) u₀))
      (k := u₀.asIdeal.ResidueField) (alg := primeResidueFieldAlgebra toS u₀)
      (S.fromSpecStalk (basePoint (Over.mk toS) u₀)) q (Over.mk toS) x hx
      (Spec.map (CommRingCat.ofHom (algebraMap A u₀.asIdeal.ResidueField)))
```

**`Deformation.Artin.exists_algHom_section_of_surjective_derivedTensorFibre_neg_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityObstructionVanishing.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityObstructionVanishing.lean#L404). The attribute's comment: “(2) implies (1): condition (2) in degree -1 forces the obstruction class of a square-zero extension with one-dimensional kernel to vanish, so the extension splits”.

> **Stacks 07YM, the obstruction step of `(2) ⇒ (1)`.** Let `A' → A` be a square-zero
> surjection of `Λ`-algebras whose kernel `I` is one-dimensional over an `A`-algebra field `k`,
> and let `ξ : E ⟶ NL_{A/Λ}` be a morphism of `D⁻(A)` with `H^{-1}(ξ ⊗ᴸ_A k)` surjective. If
> `ξ` composed with `NL_{A/Λ} ⟶ NL_{A/A'}` vanishes, then `A' → A` admits a `Λ`-algebra
> section.
>
> Condition (2) in degree `-1` kills the extension class `NL_{A/Λ} ⟶ I[1]` of the thickening
> (`Deformation.Artin.cotangentExtensionClass_eq_zero_of_surjective_derivedTensorFibre_neg_one`).
> Computed through the canonical presentation of `A` over `Λ`
> (`Deformation.Artin.derivedNaiveCotangentComplexIso_hom_comp_cotangentExtensionClass`), that
> class is the map `J/J² → I`, `f ↦ f(a'_1, …)`, read in the derived category, and its
> vanishing makes that map factor through the differential `J/J² → ⊕_i A dx_i`
> (`Deformation.Artin.exists_comp_eq_of_Q_map_twoTermProjection_comp_eq_zero`). Correcting the
> chosen lifts of the generators by the factorization produces lifts at which every element of
> `J` vanishes, hence the section
> (`Deformation.Artin.exists_algHom_section_of_cotangentComplex_comp_eq`).

```lean
public theorem exists_algHom_section_of_surjective_derivedTensorFibre_neg_one
    (hq : Function.Surjective (algebraMap A' A))
    (hsq : RingHom.ker (algebraMap A' A) ^ 2 = ⊥)
    (eI : letI := Stacks.Smooth.kerModule hq hsq
      RingHom.ker (algebraMap A' A) ≃ₗ[A] k)
    (T : DerivedTensorProduct A) (E : DerivedCategory (ModuleCat.{u} A))
    (hE : (DerivedCategory.TStructure.t (C := ModuleCat.{u} A)).minus E)
    (ξ : E ⟶ derivedNaiveCotangentComplex Λ A)
    (hsurj : Function.Surjective
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-1)).map
        ((T.tensor.flip.obj
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
            (ModuleCat.of A k))).map ξ)))
    (hkill : ξ ≫ naiveCotangentBaseMap Λ A' A = 0) :
    ∃ σ : A →ₐ[Λ] A', (algebraMap A' A).comp (σ : A →+* A') = RingHom.id A
```

**`Deformation.ArtinianLocalAlgCat.isEssentialSurjection_powQuotientMap_of_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityPowQuotientEssential.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityPowQuotientEssential.lean#L68). The attribute's comment: “A'/(𝔭') ^ n ⟶ A/𝔭 ^ n is an essential surjection of 𝒞\_Λ”.

> **The essential surjection of [Stacks, Tag 07YM].** Let `Λ → A' → A → k` be a tower with `k`
> a field and both maps onto `k` surjective, let `𝔭` and `𝔭'` be the two augmentation ideals and
> let `n ≥ 2`. If `A' → A` does not change differentials modulo `k`, then the induced morphism
> `A' ⧸ (𝔭') ^ n ⟶ A ⧸ 𝔭 ^ n` of `𝒞_Λ` is an essential surjection.
>
> `Deformation.Artin.differentialsBaseChangeMap_bijective_powQuotient` transfers the bijectivity to
> the quotients and
> `Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_bijective_differentialsBaseChangeMap`
> is [Stacks, Tag 06H0]; what this adds is the identification of the algebra structures rebuilt from
> `ε`, `ε'` and `φ` with the ambient ones, which `Algebra.algebra_ext` provides and which the proof
> then substitutes.

```lean
public theorem isEssentialSurjection_powQuotientMap_of_bijective
    {Λ A' A k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [CommRing A'] [CommRing A]
    [Algebra Λ A'] [Algebra Λ A] [IsNoetherianRing A'] [IsNoetherianRing A]
    [Algebra A' A] [Algebra A' k] [Algebra A k]
    [IsScalarTower Λ A' A] [IsScalarTower Λ A' k] [IsScalarTower Λ A k] [IsScalarTower A' A k]
    (ε : A →ₐ[Λ] k) (hεeq : ∀ a, ε a = algebraMap A k a) (hε : Function.Surjective ε)
    (ε' : A' →ₐ[Λ] k) (hε'eq : ∀ a', ε' a' = algebraMap A' k a')
    (hε' : Function.Surjective ε')
    (φ : A' →ₐ[Λ] A) (hφeq : ∀ a', φ a' = algebraMap A' A a') (hφ : ε.comp φ = ε')
    (n : ℕ) [NeZero n] (hn : 2 ≤ n)
    (hbij : Function.Bijective (Deformation.Artin.differentialsBaseChangeMap Λ A' A k)) :
    IsEssentialSurjection (powQuotientMap hφ hε' hε n)
```

**`Deformation.Artin.liftsAtResiduePoint_prime_base_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityPrimeBase.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityPrimeBase.lean#L135). The attribute's comment: “versality over any affine base at the residue field of the prime”.

> **Stacks 07YM, versality in the form the degree `-1` endgame consumes.** If `x` is versal at
> a point `u₀` of `Spec A`, then the lifting property holds with *any* `Spec Λ ⟶ S` as deformation
> base, at the point of `Spec A` determined by the `A`-algebra structure of the residue field
> `Ideal.ResidueField u₀.asIdeal` of the prime.
>
> `Deformation.Artin.liftsAtResiduePoint_of_isVersalAt` is versality read at that field over the
> local ring `𝒪_{S,s}`, and `Deformation.Artin.liftsAtResiduePoint_changeBase` moves the base to
> `Λ`; the compatibility of the residue point with the local ring that the move asks for is
> `Deformation.Artin.specMap_primeResidueFieldAlgebra_comp_fromSpecStalk`, and the locality of the
> structure map is `Deformation.Artin.isLocalHom_primeResidueFieldAlgebra`.
>
> Nothing is asked of `Spec Λ ⟶ S`: not that it be an open immersion, nor a monomorphism.

```lean
public theorem liftsAtResiduePoint_prime_base_of_isVersalAt
    (hversal : IsVersalAt (Over.mk toS) q u₀ x hx) :
    LiftsAtResiduePoint (Λ := Λ) (k := u₀.asIdeal.ResidueField) iΛ q (Over.mk toS) x hx
      (Spec.map (CommRingCat.ofHom (algebraMap A u₀.asIdeal.ResidueField)))
```

**`Deformation.Artin.differentialsBaseChangeMap_bijective_powQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityQuotientDifferentials.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityQuotientDifferentials.lean#L156). The attribute's comment: “A'/(𝔭') ^ n ⟶ A/𝔭 ^ n does not change differentials either”.

> **The quotient transfer of [Stacks, Tag 07YL]'s bijectivity.** Let `A' → A` be a map of
> `Λ`-algebras with compatible surjective augmentations onto a field `k`, let `𝔭 = Ker ε` and
> `𝔭' = Ker ε'`, and let `n ≥ 2`. If `A' → A` does not change differentials modulo `k`, neither
> does the induced map `A' ⧸ (𝔭') ^ n ⟶ A ⧸ 𝔭 ^ n`.
>
> This is `Deformation.Artin.differentialsBaseChangeMap_bijective_of_square` at the square whose
> vertical maps are the two quotient maps: each is surjective, and the kernel of
> `A' → A' ⧸ (𝔭') ^ n` is `(𝔭') ^ n ≤ (𝔭') ^ 2`, the augmentation ideal being the kernel of
> `A' ⟶ k`. Composed with
> `Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_bijective_differentialsBaseChangeMap`
> it says that `A' ⧸ (𝔭') ^ n ⟶ A ⧸ 𝔭 ^ n` is an essential surjection of `𝒞_Λ`, which is the
> contradiction the direction `(1) ⇒ (2)` of [Stacks, Tag 07YM] drives at.

```lean
public theorem differentialsBaseChangeMap_bijective_powQuotient
    {ε' : A' →ₐ[Λ] k} {ε : A →ₐ[Λ] k} {φ : A' →ₐ[Λ] A} (hφ : ε.comp φ = ε')
    (n : ℕ) [NeZero n] (hn : 2 ≤ n) :
    letI : Algebra A' A := φ.toRingHom.toAlgebra
    letI : Algebra A' k := ε'.toRingHom.toAlgebra
    letI : Algebra A k := ε.toRingHom.toAlgebra
    letI : IsScalarTower Λ A' A := .of_algebraMap_eq fun l => (φ.commutes l).symm
    letI : IsScalarTower Λ A' k := .of_algebraMap_eq fun l => (ε'.commutes l).symm
    letI : IsScalarTower Λ A k := .of_algebraMap_eq fun l => (ε.commutes l).symm
    letI : IsScalarTower A' A k :=
      .of_algebraMap_eq fun a => (DFunLike.congr_fun hφ a).symm
    letI : Algebra (A' ⧸ RingHom.ker ε'.toRingHom ^ n) (A ⧸ RingHom.ker ε.toRingHom ^ n) :=
      (powQuotientMapAlgHom hφ n).toRingHom.toAlgebra
    letI : Algebra (A' ⧸ RingHom.ker ε'.toRingHom ^ n) k :=
      (powQuotientAug ε' n).toRingHom.toAlgebra
    letI : Algebra (A ⧸ RingHom.ker ε.toRingHom ^ n) k :=
      (powQuotientAug ε n).toRingHom.toAlgebra
    letI : IsScalarTower Λ (A' ⧸ RingHom.ker ε'.toRingHom ^ n)
        (A ⧸ RingHom.ker ε.toRingHom ^ n) :=
      .of_algebraMap_eq fun l => ((powQuotientMapAlgHom hφ n).commutes l).symm
    letI : IsScalarTower Λ (A' ⧸ RingHom.ker ε'.toRingHom ^ n) k :=
      .of_algebraMap_eq fun l => ((powQuotientAug ε' n).commutes l).symm
    letI : IsScalarTower Λ (A ⧸ RingHom.ker ε.toRingHom ^ n) k :=
      .of_algebraMap_eq fun l => ((powQuotientAug ε n).commutes l).symm
    letI : IsScalarTower (A' ⧸ RingHom.ker ε'.toRingHom ^ n)
        (A ⧸ RingHom.ker ε.toRingHom ^ n) k :=
      .of_algebraMap_eq fun b => (powQuotientAug_powQuotientMapAlgHom hφ n b).symm
    Function.Bijective (differentialsBaseChangeMap Λ A' A k) →
      Function.Bijective (differentialsBaseChangeMap Λ
        (A' ⧸ RingHom.ker ε'.toRingHom ^ n) (A ⧸ RingHom.ker ε.toRingHom ^ n) k)
```

**`Deformation.Artin.schemeMap_restrictAlongArrow_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityRestriction.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityRestriction.lean#L179). The attribute's comment: “the restriction of x along a ring map, over Spec of that map”.

> **The bridge from a ring map to an arrow of the fibred category.** For a ring map
> `φ : A → C` compatible with the structure morphisms, the restriction
> `Deformation.Artin.restrictAlong` is an object lying over `Spec C` whose structure arrow to
> `x` has underlying morphism of schemes exactly `Spec φ`.
>
> This is the shape `Deformation.Artin.LiftsAtResiduePoint` consumes, with the two bases
> presented as objects of the slice over `S`.

```lean
public theorem schemeMap_restrictAlongArrow_mk
    (hw : (p ⋙ Over.post B.inclusion).obj x = Over.mk toS) :
    schemeMap (p ⋙ Over.post B.inclusion)
        (restrictAlong_objS φ B S hS toS toSC hA hC hφ p x hx) hw
        (restrictAlongArrow φ B S hS toS toSC hA hC hφ p x hx) =
      Spec.map (CommRingCat.ofHom φ)
```

**`Deformation.Artin.comp_ringHom_of_schemeMap_of_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalitySquareLift.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalitySquareLift.lean#L117). The attribute's comment: “i ≫ b = a read as an identity of ring maps”.

> **An equation of arrows of the fibred category, read as an identity of ring maps.** Let
> `i : y ⟶ z`, `b : z ⟶ x` and `a : y ⟶ x` be arrows with `i ≫ b = a`, between objects presented
> over `S` by spectra of rings, and suppose the morphisms of schemes underlying `i` and `a` are the
> spectra of ring maps `f` and `g`. Then `f` composed with the ring map underlying `b` is `g`.
>
> Both ends being affine, `Deformation.Artin.schemeMap_comp` turns the equation into an equation of
> morphisms of affine schemes, and the faithfulness of `Scheme.Spec` turns that into the identity
> of ring maps. This is what converts the conclusion `i ≫ b = a` of
> `Deformation.Artin.LiftsAtResiduePoint` into the hypothesis
> `∀ a, f (σ a) = Ideal.Quotient.mk (𝔭 ^ n) a` of
> `Deformation.ArtinianLocalAlgCat.not_isEssentialSurjection_of_lift_powQuotient`.

```lean
public theorem comp_ringHom_of_schemeMap_of_comp_eq
    {A C C' : Type u} [CommRing A] [CommRing C] [CommRing C']
    {S : Scheme.{u}} {toS : Spec (CommRingCat.of A) ⟶ S}
    {toSC : Spec (CommRingCat.of C) ⟶ S} {toSC' : Spec (CommRingCat.of C') ⟶ S}
    {Y : Type v} [Category.{w} Y] (q : Y ⥤ Over S) {y z x : Y}
    (hy : q.obj y = Over.mk toSC) (hz : q.obj z = Over.mk toSC')
    (hx : q.obj x = Over.mk toS)
    {i : y ⟶ z} {b : z ⟶ x} {a : y ⟶ x} (hab : i ≫ b = a)
    {f : C' →+* C} (hi : schemeMap q hy hz i = Spec.map (CommRingCat.ofHom f))
    {g : A →+* C} (ha : schemeMap q hy hx a = Spec.map (CommRingCat.ofHom g)) :
    f.comp (ringHom_of_schemeMap (schemeMap q hz hx b)) = g
```

**`Deformation.Artin.exists_algHom_powQuotient_of_liftsAtResiduePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalitySquareLift.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalitySquareLift.lean#L158). The attribute's comment: “versality lifts A through A'/(𝔭') ^ n”.

> **The section of [Stacks, Tag 07YM].** Let `A' → A` be a map of augmented Noetherian
> `Λ`-algebras over a field `κ`, with `φ` surjective, let `x` be a family over `Spec A` and `x'` a
> lift of it to `Spec A'`, presented over `S` through the affine open `Spec Λ ⟶ S`. If the lifting
> property defining versality holds at the residue point of `A` determined by its augmentation,
> then the quotient map `A → A ⧸ 𝔭 ^ n` lifts through the small extension
> `A' ⧸ (𝔭') ^ n ⟶ A ⧸ 𝔭 ^ n` to a `Λ`-algebra map `σ : A →ₐ[Λ] A' ⧸ (𝔭') ^ n`.
>
> The two restrictions are the chosen pullbacks `Deformation.Artin.restrictAlong`, the arrow
> between them is `Deformation.Artin.exists_unique_schemeMap_eq_of_square` applied to the commuting
> square of rings `A' → A → A ⧸ 𝔭 ^ n` and `A' → A' ⧸ (𝔭') ^ n → A ⧸ 𝔭 ^ n`, the residue condition
> that versality asks of the arrow to `x` is the compatibility of the induced augmentation with the
> quotient map, and the ring map is read off the resulting arrow by
> `Deformation.Artin.algHom_of_schemeMap_over`, whose output is the identity
> `Deformation.Artin.comp_ringHom_of_schemeMap_of_comp_eq` converts.

```lean
public theorem exists_algHom_powQuotient_of_liftsAtResiduePoint
    (ε : A →ₐ[Λ] κ) (hε : Function.Surjective ε)
    (ε' : A' →ₐ[Λ] κ) (hε' : Function.Surjective ε')
    (φ : A' →ₐ[Λ] A) (hφ : ε.comp φ = ε') (hsurjφ : Function.Surjective φ)
    (n : ℕ) [NeZero n]
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (toS : Spec (CommRingCat.of A) ⟶ S) (hA : B.Contains (Spec (CommRingCat.of A)))
    (hA' : B.Contains (Spec (CommRingCat.of A')))
    (baseMap : Spec (CommRingCat.of Λ) ⟶ S) [Mono baseMap]
    (hbase : Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ baseMap = toS)
    (hC : B.Contains (Spec (CommRingCat.of (A ⧸ RingHom.ker ε.toRingHom ^ n))))
    (hC' : B.Contains (Spec (CommRingCat.of (A' ⧸ RingHom.ker ε'.toRingHom ^ n))))
    (p : X ⥤ BigFppfOver B S hS) (hp : p.IsFiberedInGroupoids) (x x' : X)
    (hx : p.obj x = algebraOver A B S hS toS hA)
    (hxS : (p ⋙ Over.post B.inclusion).obj x = Over.mk toS)
    (hx' : p.obj x' = algebraOver A' B S hS
      (Spec.map (CommRingCat.ofHom (algebraMap Λ A')) ≫ baseMap) hA')
    (hx'S : (p ⋙ Over.post B.inclusion).obj x' =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ A')) ≫ baseMap))
    (lift : x ⟶ x')
    (hlift : schemeMap (p ⋙ Over.post B.inclusion) hxS hx'S lift =
      Spec.map (CommRingCat.ofHom φ.toRingHom))
    (hlifts : LiftsAtResiduePoint (Λ := Λ) (k := κ) baseMap (p ⋙ Over.post B.inclusion)
      (Over.mk toS) x hxS (Spec.map (CommRingCat.ofHom ε.toRingHom))) :
    ∃ σ : A →ₐ[Λ] (powQuotientObj ε' hε' n : Type u),
      ∀ t : A, (powQuotientMap hφ hε' hε n).hom (σ t) =
        Ideal.Quotient.mk (RingHom.ker ε.toRingHom ^ n) t
```

**`Deformation.Artin.liftsAtResiduePoint_changeBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityStalkBase.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityStalkBase.lean#L337). The attribute's comment: “the lifting property over the local ring of S transfers to the affine open”.

> **The change of deformation base.** If the lifting property defining versality holds with
> the local ring of `S` at `s` as deformation base, it holds with any `Λ` whose spectrum maps to
> `S` compatibly with the chosen residue point.
>
> Every Artinian local `Λ`-algebra occurring in a lifting problem has its residue point at the
> chosen point of `S` — for the target because the lifting property already imposes that of the
> arrow `a`, read through `Deformation.Artin.schemeMap_over`, and for the source because the
> surjection is `Λ`-linear and respects the residue identifications — so each is canonically an
> `𝒪_{S,s}`-algebra (`Deformation.Artin.stalkObj`), the surjection between them is a morphism of
> `𝒞_{𝒪_{S,s}}` with the same underlying ring map (`Deformation.Artin.stalkHom`), and the two
> presentations of each base over `S` agree
> (`Deformation.Artin.specMap_stalkAlgebra_comp_fromSpecStalk`).
>
> Nothing is asked of `iΛ`: not that it be an open immersion, nor even a monomorphism. The
> factorization through the local ring is produced at the level of schemes, so `𝒪_{S,s}` is never
> identified with a localization of `Λ`.

```lean
public theorem liftsAtResiduePoint_changeBase
    (hstalk : LiftsAtResiduePoint (Λ := S.presheaf.stalk s) (k := k) (alg := algStalk)
      (S.fromSpecStalk s) q U x hx κ) :
    LiftsAtResiduePoint (Λ := Λ) (k := k) iΛ q U x hx κ
```

**`Deformation.Artin.liftsAtResiduePoint_base_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityStalkBase.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityStalkBase.lean#L404). The attribute's comment: “versality gives the lifting property over any affine deformation base”.

> **Versality at a point, read with an arbitrary affine deformation base.** If `x` is versal
> at `u₀` then the lifting property holds with *any* `Spec Λ ⟶ S` as deformation base, at the
> canonical residue-field point of `u₀`.
>
> `Deformation.Artin.IsVersalAt` is literally the lifting property with the local ring of `S` at
> the image of `u₀` as base (`Deformation.Artin.isVersalAt_iff_liftsAtResiduePoint`), and
> `Deformation.Artin.liftsAtResiduePoint_changeBase` moves the base; the one compatibility it
> asks of the residue point is that it factor through that local ring, which is
> `AlgebraicGeometry.Scheme.Spec_stalkClosedPointTo_fromSpecStalk`.
>
> This is the form the degree `-1` half of the direction `(1) ⇒ (2)` of [Stacks, Tag 07YM]
> consumes: the small extension it tests versality against is built from `Λ`-algebras, `Λ` being
> the ring of the affine open the family maps into, and the objects of `𝒞_{𝒪_{S,s}}` are not
> available to it. Nothing is asked of `iΛ` — in particular not that it be an open immersion.

```lean
public theorem liftsAtResiduePoint_base_of_isVersalAt
    (hversal : IsVersalAt U q u₀ x hx) :
    LiftsAtResiduePoint (Λ := Λ) (k := U.left.residueField u₀) iΛ q U x hx
      (U.left.fromSpecResidueField u₀)
```

**`Deformation.Artin.naiveVersalityCriterion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityTag.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityTag.lean#L94).

> **Stacks 07YM.** Let `S` be a locally Noetherian scheme, let `𝒳` be a category fibred in
> groupoids over the big fppf site of `S` satisfying (RS\*), let `U = Spec A` be affine of finite
> type over `S` mapping into an affine open `Spec Λ ⊆ S`, let `x` be an object of `𝒳` over `U`,
> and let `ξ : E ⟶ NL_{A/Λ}` be a morphism of `D⁻(A)` such that
>
> 1. for every deformation situation `(x, A' → A)` the object `x` lifts to `Spec A'` exactly
>    when `E ⟶ NL_{A/Λ} ⟶ NL_{A/A'}` is zero, and
> 2. there is an isomorphism of functors `T_x(−) ⟶ Ext⁰_A(E, −)` carrying the canonical element
>    to `E ⟶ NL_{A/Λ} ⟶ Ω_{A/Λ}`.
>
> Let `u₀ ∈ U` be a finite type point with residue field `k`. Then `x` is versal at `u₀` as soon
> as `ξ` induces a surjection `H^{-1}(E ⊗ᴸ_A k) ⟶ H^{-1}(NL_{A/Λ} ⊗ᴸ_A k)` and an injection
> `H^0(E ⊗ᴸ_A k) ⟶ H^0(NL_{A/Λ} ⊗ᴸ_A k)`; and conversely, if `u₀` is a closed point at which `x`
> is versal, then `ξ` induces such a surjection and such an injection.
>
> Both directions are stated at once, as the predicate
> `Deformation.Artin.NaiveVersalityCriterion` which [Stacks, Tag 07YN] and [Stacks, Tag 07YU]
> consume as a hypothesis.

```lean
public theorem naiveVersalityCriterion : NaiveVersalityCriterion hp hRS P hΩ E ξ
```

**`Deformation.Artin.tangentEquiv_canonicalTangentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityTangentFactorization.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityTangentFactorization.lean#L90). The attribute's comment: “the map on tangent spaces factors through the augmentation”.

> **Stacks 07YM, hypothesis (ii) in use.** Under the functorial isomorphism
> `T_x(-) ≅ Ext⁰_A(E, -)` of hypothesis (ii), the map on tangent spaces of Stacks 07YC sends a
> tangent vector `θ : Ω_{A/Λ} →ₗ[A] k` to `ξ` followed by the augmentation
> `Deformation.Artin.naiveCotangentToDifferentials` followed by `θ`.
>
> This is the naturality of the isomorphism at the morphism of site modules attached to `θ`,
> together with its prescribed value at the canonical element:
> `Deformation.Artin.canonicalTangentMap` is by definition the image of the canonical element
> under that morphism.

```lean
public theorem tangentEquiv_canonicalTangentMap (θ : Ω[A⁄Λ] →ₗ[A] k) :
    tangentEquiv (⟨ModuleCat.of A k, hk⟩ : SiteModule A B)
        (canonicalTangentMap Λ A k B S hS toS hA p x hx hp hRS hΩ hk baseMap
          baseFactorization θ) =
      ξ ≫ naiveCotangentToDifferentials Λ A ≫
        (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).map (ModuleCat.ofHom θ)
```

**`Deformation.Artin.length_ker_eq_one_of_linearEquiv_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityThickeningSite.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityThickeningSite.lean#L241). The attribute's comment: “the kernel `I` of `A' → A` has length one over `A'`”.

> **The length-one hypothesis of
> `Deformation.ArtinianLocalAlgCat.isSmallExtension_powQuotientMap`.** The kernel of the
> thickening of [Stacks, Tag 07YL] has length one over `A'`: it is a copy of the residue field
> at a maximal ideal of `A`, hence a simple `A`-module
> (`Deformation.Artin.isSimpleModule_residueField`), and the `A'`-submodules of it are its
> `A`-submodules because the two actions agree through the surjection `A' → A`
> (`isSimpleModule_iff_isSimpleModule_of_algebraMap_surjective`).

```lean
public theorem length_ker_eq_one_of_linearEquiv_residueField
    (p : Ideal A) [p.IsMaximal]
    (e : RingHom.ker (algebraMap A' A) ≃ₗ[A] p.ResidueField) :
    Module.length A' (RingHom.ker (algebraMap A' A)) = 1
```

**`Deformation.Artin.mul_ker_eq_bot_of_linearEquiv_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityThickeningSite.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityThickeningSite.lean#L262). The attribute's comment: “𝔭' annihilates the kernel I of A' → A”.

> **The Artin–Rees input of [Stacks, Tag 07YM].** An ideal of `A'` carried by the surjection
> `A' → A` into the kernel of `A ⟶ κ(𝔭)` annihilates the kernel `I` of that surjection: the two
> actions on `I` agree, and `I` is a copy of `κ(𝔭)`, on which `𝔭` acts by zero.
>
> Applied with `q = Ker(A' ⟶ κ(𝔭))` this is the hypothesis `𝔭' · I = 0` of
> `Deformation.Artin.exists_pow_inf_eq_bot_of_mul_eq_bot`, which produces the exponent `n > 1`
> with `(𝔭') ^ n ⊓ I = 0`. Only primality of `𝔭` is used.

```lean
public theorem mul_ker_eq_bot_of_linearEquiv_residueField
    (p : Ideal A) [p.IsPrime]
    (e : RingHom.ker (algebraMap A' A) ≃ₗ[A] p.ResidueField)
    (q : Ideal A')
    (hq : ∀ a' ∈ q, algebraMap A' A a' ∈ RingHom.ker (algebraMap A p.ResidueField)) :
    q * RingHom.ker (algebraMap A' A) = ⊥
```

**`Deformation.ArtinianLocalAlgCat.powQuotientObj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean#L143). The attribute's comment: “the object `A/𝔭 ^ n` of `𝒞_Λ` at a closed point”. References: EGA 0 (19.5.6.2), “special case”.

> The object `R ⧸ 𝔭 ^ n` of `𝒞_Λ`, for `𝔭 = Ker ε` the augmentation ideal of a surjective
> augmentation of a Noetherian `Λ`-algebra and `n ≠ 0`. The algebra `R` itself is not asked to
> be local or Artinian.

```lean
public noncomputable def powQuotientObj [IsNoetherianRing R] (ε : R →ₐ[Λ] k)
    (hε : Function.Surjective ε) (n : ℕ) [NeZero n] : ArtinianLocalAlgCat.{u, v, w} Λ k
```

**`Deformation.ArtinianLocalAlgCat.maximalIdeal_pow_powQuotientObj_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean#L169). The attribute's comment: “the maximal ideal of the object `A'/(𝔭') ^ n` of `𝒞_Λ` has vanishing power”.

> The `n`-th power of the maximal ideal of `R ⧸ 𝔭 ^ n` vanishes. This is the hypothesis
> `𝔪_{B'} ^ n = 0` of
> `Deformation.ArtinianLocalAlgCat.not_isEssentialSurjection_of_lift_powQuotient`, read at the
> object `Deformation.ArtinianLocalAlgCat.powQuotientObj` of `𝒞_Λ` rather than at the bare
> quotient ring; it is `IsLocalRing.maximalIdeal_quotient_pow_pow_eq_bot`, the augmentation
> ideal being maximal.

```lean
public theorem maximalIdeal_pow_powQuotientObj_eq_bot [IsNoetherianRing R] (ε : R →ₐ[Λ] k)
    (hε : Function.Surjective ε) (n : ℕ) [NeZero n] :
    maximalIdeal (powQuotientObj ε hε n : Type v) ^ n = ⊥
```

**`Deformation.ArtinianLocalAlgCat.ker_powQuotientMapAlgHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean#L235). The attribute's comment: “the kernel of `A'/(𝔭') ^ n ⟶ A/𝔭 ^ n` is the image of `I = Ker(A' → A)`”.

> **The kernel computation of [Stacks, Tag 07YM].** For `φ : R' ↠ R` surjective, the kernel
> of `R' ⧸ (𝔭') ^ n ⟶ R ⧸ 𝔭 ^ n` is the image of `Ker φ`.
>
> The preimage of `𝔭 ^ n` under `φ` is `(𝔭') ^ n + Ker φ`, because `𝔭 ^ n` is the image of
> `(𝔭') ^ n`; passing to `R' ⧸ (𝔭') ^ n` kills the first summand.

```lean
public theorem ker_powQuotientMapAlgHom {ε' : R' →ₐ[Λ] k} {ε : R →ₐ[Λ] k} {φ : R' →ₐ[Λ] R}
    (hφ : ε.comp φ = ε') (n : ℕ) (hsurj : Function.Surjective φ) :
    RingHom.ker (powQuotientMapAlgHom hφ n).toRingHom =
      (RingHom.ker φ.toRingHom).map
        (Ideal.Quotient.mk (RingHom.ker ε'.toRingHom ^ n))
```

**`Deformation.ArtinianLocalAlgCat.powQuotientMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean#L257). The attribute's comment: “the morphism `A'/(𝔭') ^ n ⟶ A/𝔭 ^ n` of `𝒞_Λ`”.

> The morphism `R' ⧸ (𝔭') ^ n ⟶ R ⧸ 𝔭 ^ n` of `𝒞_Λ` induced by a map of augmented
> Noetherian algebras.

```lean
public noncomputable def powQuotientMap [IsNoetherianRing R'] [IsNoetherianRing R]
    {ε' : R' →ₐ[Λ] k} {ε : R →ₐ[Λ] k} {φ : R' →ₐ[Λ] R} (hφ : ε.comp φ = ε')
    (hε' : Function.Surjective ε') (hε : Function.Surjective ε) (n : ℕ) [NeZero n] :
    powQuotientObj ε' hε' n ⟶ powQuotientObj ε hε n
```

**`Deformation.ArtinianLocalAlgCat.isSmallExtension_powQuotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotient.lean#L294). The attribute's comment: “`A'/(𝔭') ^ n ⟶ A/𝔭 ^ n` is a small extension”.

> **The small extension of [Stacks, Tag 07YM].** Let `φ : R' ↠ R` be a surjection of
> augmented Noetherian `Λ`-algebras whose kernel `I` has length one over `R'`, and suppose
> `(𝔭') ^ n ⊓ I = 0`. Then `R' ⧸ (𝔭') ^ n ⟶ R ⧸ 𝔭 ^ n` is a small extension of Artinian local
> rings.
>
> The kernel is the image of `I` by `ker_powQuotientMapAlgHom`, and `(𝔭') ^ n ⊓ I = 0` makes
> that image a copy of `I`, hence again of length one. In the source `I` is a one-dimensional
> `k`-vector space and the hypothesis `(𝔭') ^ n ⊓ I = 0` is the conclusion of the Artin–Rees
> step `Deformation.Artin.exists_pow_inf_eq_bot_of_mul_eq_bot`.

```lean
public theorem isSmallExtension_powQuotientMap [IsNoetherianRing R'] [IsNoetherianRing R]
    {ε' : R' →ₐ[Λ] k} {ε : R →ₐ[Λ] k} {φ : R' →ₐ[Λ] R} (hφ : ε.comp φ = ε')
    (hε' : Function.Surjective ε') (hε : Function.Surjective ε)
    (hsurj : Function.Surjective φ) (n : ℕ) [NeZero n]
    (hinf : RingHom.ker ε'.toRingHom ^ n ⊓ RingHom.ker φ.toRingHom = ⊥)
    (hlen : Module.length R' (RingHom.ker φ.toRingHom) = 1) :
    InfinitesimalLifting.IsSmallExtension
      (CommRingCat.ofHom (powQuotientMap hφ hε' hε n).hom.toRingHom)
```

**`Deformation.ArtinianLocalAlgCat.exists_section_of_lift_powQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotientSection.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotientSection.lean#L95). The attribute's comment: “the lift factors through A/𝔭 ^ n, giving a section of the small extension”.

> **The section of [Stacks, Tag 07YM].** If the quotient map `R → R ⧸ 𝔭 ^ n` lifts through a
> morphism `f : C ⟶ R ⧸ 𝔭 ^ n` of `𝒞_Λ` whose source has `𝔪_C ^ n = 0`, then `f` has a section
> in `𝒞_Λ`.
>
> The lift factors through `R ⧸ 𝔭 ^ n` by `IsLocalRing.exists_isLocalHom_comp_mk_pow`, and the
> factorization is a morphism of `𝒞_Λ`: it is a `Λ`-algebra map because `σ` is, it is local by
> that lemma, and it respects the identifications of the residue fields because `f` does.

```lean
public theorem exists_section_of_lift_powQuotient
    (hn : maximalIdeal (C : Type v) ^ n = ⊥) :
    ∃ s : powQuotientObj ε hε n ⟶ C, s ≫ f = 𝟙 (powQuotientObj ε hε n)
```

**`Deformation.ArtinianLocalAlgCat.not_isEssentialSurjection_of_lift_powQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotientSection.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/AugmentedPowQuotientSection.lean#L125). The attribute's comment: “a lift of A through A'/(𝔭') ^ n contradicts essential surjectivity”.

> **The contradiction of [Stacks, Tag 07YM].** A small extension `f : C ⟶ R ⧸ 𝔭 ^ n` of
> `𝒞_Λ` whose source has `𝔪_C ^ n = 0` and through which the quotient map `R → R ⧸ 𝔭 ^ n` lifts
> is not an essential surjection: the lift produces a section
> (`Deformation.ArtinianLocalAlgCat.exists_section_of_lift_powQuotient`), and a small extension
> with a section is not essential (`Deformation.not_isEssentialSurjection_iff_exists_section`).

```lean
public theorem not_isEssentialSurjection_of_lift_powQuotient
    (hn : maximalIdeal (C : Type v) ^ n = ⊥)
    (hf : InfinitesimalLifting.IsSmallExtension (CommRingCat.ofHom f.hom.toRingHom)) :
    ¬ IsEssentialSurjection f
```

**`isLocalRing_quotient_pow_of_isMaximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean#L109). The attribute's comment: “the local half of `A/𝔭 ^ n`, for `𝔭` the prime of a closed point”.

> For a maximal ideal `p` of a ring that need not be local and `n ≠ 0`, the ring `R ⧸ p ^ n`
> is local.

```lean
public theorem isLocalRing_quotient_pow_of_isMaximal (p : Ideal R) [p.IsMaximal] {n : ℕ}
    (hn : n ≠ 0) : IsLocalRing (R ⧸ p ^ n)
```

**`isArtinianRing_quotient_pow_of_isMaximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean#L116). The attribute's comment: “the Artinian half of `A/𝔭 ^ n`, for `𝔭` the prime of a closed point”.

> For a maximal ideal `p` of a Noetherian ring that need not be local and `n ≠ 0`, the ring
> `R ⧸ p ^ n` is Artinian.

```lean
public theorem isArtinianRing_quotient_pow_of_isMaximal [IsNoetherianRing R] (p : Ideal R)
    [p.IsMaximal] {n : ℕ} (hn : n ≠ 0) : IsArtinianRing (R ⧸ p ^ n)
```

**`IsLocalRing.maximalIdeal_quotient_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean#L143). The attribute's comment: “the maximal ideal of `A/𝔭 ^ n`, for `𝔭` the prime of a closed point”.

> For a maximal ideal `p` and `n ≠ 0`, the maximal ideal of `R ⧸ p ^ n` is the image of
> `p`.

```lean
public theorem IsLocalRing.maximalIdeal_quotient_pow (p : Ideal R) [p.IsMaximal] (n : ℕ)
    [NeZero n] :
    IsLocalRing.maximalIdeal (R ⧸ p ^ n) = p.map (Ideal.Quotient.mk (p ^ n))
```

**`IsLocalRing.maximalIdeal_quotient_pow_pow_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean#L159). The attribute's comment: “the maximal ideal of `A'/(𝔭') ^ n` has vanishing `n`-th power”.

> For a maximal ideal `p` and `n ≠ 0`, the `n`-th power of the maximal ideal of `R ⧸ p ^ n`
> vanishes: that maximal ideal is the image of `p`, so its `n`-th power is the image of `p ^ n`,
> which is the ideal being quotiented out.
>
> This is the hypothesis `𝔪_{B'} ^ n = 0` under which a lift of `R` through a morphism onto
> `R ⧸ p ^ n` factors (`IsLocalRing.exists_isLocalHom_comp_mk_pow`), and in [Stacks, Tag 07YM]
> it is the sentence "since the maximal ideal of `B'` has `n`th power equal to zero". The ring
> `R` is not asked to be local.

```lean
public theorem IsLocalRing.maximalIdeal_quotient_pow_pow_eq_bot (p : Ideal R) [p.IsMaximal]
    (n : ℕ) [NeZero n] : IsLocalRing.maximalIdeal (R ⧸ p ^ n) ^ n = ⊥
```

**`IsLocalRing.exists_isLocalHom_comp_mk_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RadicalMaximalQuotient.lean#L205). The attribute's comment: “σ : A → B' with 𝔪\_\{B'} ^ n = 0 factors through A/𝔭 ^ n”.

> **The local factorization of [Stacks, Tag 07YM].** A ring map `σ : R → S` into a local
> ring whose maximal ideal satisfies `𝔪_S ^ n = 0` factors through `R ⧸ p ^ n` for every ideal
> `p` whose image under `σ` lies in `𝔪_S`, and the factorization is a local homomorphism as soon
> as `p` is maximal and `n ≠ 0`.
>
> The ring `R` is not asked to be local: in the source `σ` goes from the finite-type algebra `A`
> to an Artinian local ring `B'` and `p` is the prime of the closed point, so the hypothesis
> `p.map σ ≤ 𝔪_S` — rather than `IsLocalHom σ` — is what is available. Maximality of `p` and
> `n ≠ 0` are used only to make `R ⧸ p ^ n` a local ring, hence only for the `IsLocalHom`
> half; the factorization itself is `Ideal.Quotient.lift` applied to
> `Ideal.pow_le_ker_of_map_le` and holds for an arbitrary ideal `p` and arbitrary `n`.

```lean
public theorem IsLocalRing.exists_isLocalHom_comp_mk_pow [IsLocalRing S] (f : R →+* S)
    (p : Ideal R) [p.IsMaximal] {n : ℕ} [NeZero n]
    (hp : p.map f ≤ IsLocalRing.maximalIdeal S)
    (hn : IsLocalRing.maximalIdeal S ^ n = ⊥) :
    ∃ F : R ⧸ p ^ n →+* S, IsLocalHom F ∧ F.comp (Ideal.Quotient.mk (p ^ n)) = f
```

## Tag 07YN, a lemma

[Tag 07YN](https://stacks.math.columbia.edu/tag/07YN) in the Stacks Project.

**`Deformation.Artin.isOpenVersalityAt_of_naiveObstructionAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityTag.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityTag.lean#L124).

> **Stacks 07YN**, with the versality criterion of Stacks 07YM discharged rather than assumed.
>
> `Deformation.Artin.exists_isOpen_isVersalAt_of_naiveObstructionAt` takes that criterion as a
> hypothesis, and must: it lives in a module this one imports, while the criterion is proved here,
> so it cannot apply it without a cycle. This is the same statement with the hypothesis supplied by
> `Deformation.Artin.naiveVersalityCriterion`, so the tag sits on a declaration that grants
> nothing.

```lean
public theorem isOpenVersalityAt_of_naiveObstructionAt
    (data : NaiveObstructionAt hp hRS P hΩ E ξ)
    (hFinite : ∀ n : ℤ,
      Module.Finite P.ring ((DerivedCategory.homologyFunctor (ModuleCat.{u} P.ring) n).obj E))
    (u₀ : Spec (.of P.ring)) (hu₀ : IsClosed ({u₀} : Set (Spec (.of P.ring))))
    (hversal : IsVersalAt (Over.mk P.obj.alg.toScheme) (p ⋙ Over.post B.inclusion) u₀ P.point
      P.overScheme_eq) :
    ∃ V : Set (Spec (.of P.ring)), IsOpen V ∧ u₀ ∈ V ∧
      ∀ u ∈ V, IsFiniteTypePoint u →
        IsVersalAt (Over.mk P.obj.alg.toScheme) (p ⋙ Over.post B.inclusion) u P.point
          P.overScheme_eq
```

## Tag 07YP, a definition

[Tag 07YP](https://stacks.math.columbia.edu/tag/07YP) in the Stacks Project.

**`Deformation.Artin.NaiveObstructionTheory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveTheory.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveTheory.lean#L474).

> **Stacks 07YP.** A naive obstruction theory for a category fibred in groupoids `𝒳` over
> the big fppf site of `S` satisfying (RS*), relative to a fixed affine chart `Spec Λ ⊆ S`: a
> complex `E_x ∈ D⁻(A)` with a map `ξ_x : E_x ⟶ NL_{A/Λ}` for every object `x` of `𝒳` over
> `Spec A`, identifications of `Inf_x` and `T_x` with `Ext^{-1}_A(E_x, −)` and
> `Ext^0_A(E_x, −)`, and a functoriality map `E_x ⟶ E_y` for every ring map `A ⟶ B`, subject to
> the five conditions of the source.

```lean
public structure NaiveObstructionTheory (hp : p.IsFiberedInGroupoids)
    (hRS : SatisfiesRSStar B S hS p hp) (c : AffineChart S)
```

## Tag 07YT, a lemma

[Tag 07YT](https://stacks.math.columbia.edu/tag/07YT) in the Stacks Project.

**`Deformation.Artin.NaiveObstructionTheory.functoriality_homology_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveTheoryFunctoriality.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveTheoryFunctoriality.lean#L175).

> **Stacks 07YT.** Let `𝒳` be fibred in groupoids over the big fppf site of `S`, satisfying
> (RS*) and endowed with a naive obstruction theory. Let `A ⟶ B` be a ring map in the site, let
> `y = x|_{Spec B}` be the restriction of an object `x` of `𝒳` over `Spec A`, and let `k` be a
> `B`-algebra which is a field whose two module structures occur in the site. Then the
> functoriality map `E_x ⟶ E_y` induces bijections
> `H^i(E_x ⊗ᴸ_A k) ⟶ H^i(E_y ⊗ᴸ_B k)` for `i = 0` and `i = 1`.
>
> Nothing about the comparison is assumed. The first step of the source proof is the (RS*)
> identification of the lifts of `x` over `A[k]` with the lifts of `y` over `B[k]`, on
> isomorphism classes by `Deformation.Artin.bijective_squareZeroLiftBaseChangeMap` and on the
> automorphisms of the trivial lift by
> `Deformation.Artin.bijective_of_isInfinitesimalAutomorphismBaseChange`; through clauses (2)
> and (iii) of Stacks 07YP these give bijectivity on `Ext^0` and on `Ext^{-1}`, and the duality
> of Stacks 07YK turns that into the conclusion in degrees `0` and `1`.

```lean
theorem NaiveObstructionTheory.functoriality_homology_bijective
    {hp : p.IsFiberedInGroupoids} {hRS : SatisfiesRSStar B S hS p hp} {c : AffineChart S}
    (N : NaiveObstructionTheory B S hS p hp hRS c) (P Q : ChartedObject B S hS p c)
    (hom : AffineObject.Hom P.obj Q.obj) [Algebra P.ring Q.ring]
    [IsScalarTower c.ring P.ring Q.ring] (halg : algebraMap P.ring Q.ring = hom.alg.ringMap)
    {k : Type u} [Field k] (g : Q.ring →+* k)
    (hM : IsSiteModule P.ring B
      ((ModuleCat.restrictScalars (g.comp (algebraMap P.ring Q.ring))).obj
        (ModuleCat.of k (ULift.{u} k))))
    (hN : IsSiteModule Q.ring B
      ((ModuleCat.restrictScalars g).obj (ModuleCat.of k (ULift.{u} k)))) :
    Function.Bijective (((DerivedCategory.homologyFunctor (ModuleCat.{u} k) 0).map
        (naiveObstructionFieldBaseChangeMap N P Q hom halg g)).hom) ∧
      Function.Bijective (((DerivedCategory.homologyFunctor (ModuleCat.{u} k) 1).map
        (naiveObstructionFieldBaseChangeMap N P Q hom halg g)).hom)
```

## Tag 07YU, a lemma

[Tag 07YU](https://stacks.math.columbia.edu/tag/07YU) in the Stacks Project.

**`Deformation.Artin.isOpenVersality_of_naiveObstructionTheory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveTheoryVersalityOpenness.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveTheoryVersalityOpenness.lean#L176).

> **Stacks 07YU.** Let `S` be a locally Noetherian scheme and `𝒳` a category fibred in
> groupoids over the big fppf site of `S`. Assume that `𝒳` satisfies (RS*) and that `𝒳` has a
> naive obstruction theory, and assume the proviso of the source: the complexes `E_x` of
> Stacks 07YP have finitely generated cohomology groups for the pairs `(A, x)` with `A` of finite
> type over `S`. Then openness of versality holds for `𝒳`: if `U` is a scheme locally of finite
> type over `S`, `x` an object of `𝒳` over `U` and `u₀` a finite type point of `U` at which `x`
> is versal, then there is an open neighbourhood of `u₀` at every finite type point of which `x`
> is versal.
>
> The conclusion is the body of `Deformation.Artin.IsOpenVersality`, written out; see the
> implementation notes of this file for why the predicate itself cannot be used.

```lean
public theorem isOpenVersality_of_naiveObstructionTheory [IsLocallyNoetherian S]
    (N : ∀ c : AffineChart S, NaiveObstructionTheory B S hS p hp hRS c)
    (hFinite : ∀ (c : AffineChart S) (Q : ChartedObject B S hS p c),
      Algebra.FiniteType c.ring Q.ring → ∀ n : ℤ, Module.Finite Q.ring
        ((DerivedCategory.homologyFunctor (ModuleCat.{u} Q.ring) n).obj ((N c).complex Q).obj))
    (U : Over S) (hUft : LocallyOfFiniteType U.hom) (x : X)
    (hx : (p ⋙ Over.post B.inclusion).obj x = U) (u₀ : U.left)
    (hu₀ : IsFiniteTypePoint u₀)
    (hversal : IsVersalAt U (p ⋙ Over.post B.inclusion) u₀ x hx) :
    ∃ V : U.left.Opens, u₀ ∈ V.1 ∧
      ∀ u ∈ V.1, IsFiniteTypePoint u →
        IsVersalAt U (p ⋙ Over.post B.inclusion) u x hx
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.23, Tag 07YJ](https://stacks.math.columbia.edu/tag/07YJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
