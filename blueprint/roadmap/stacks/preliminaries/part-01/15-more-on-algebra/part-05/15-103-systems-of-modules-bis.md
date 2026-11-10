---
declaration: section
origin: cited
lean: Stacks.AdicSystem.Homology.homologyIdealPowers_proIsomorphic, Stacks.AdicSystem.ExtIdealPowerRestriction.ext_ideal_power_restriction_factors, Stacks.AdicSystem.ExtRestrictionVanishing.ext_ideal_power_restriction_eq_zero_of_annihilated, Stacks.ExtIdealPowerImage.range_ext_map_ideal_pow_le, Stacks.AdicSystem.KoszulIdealPower.idealPowerSystem_proIso_koszulIdealComplexSystem, Stacks.AdicSystem.IdealPowerTensorComparison.derivedTensor_idealPowers_proIsomorphic, Stacks.AdicSystem.IdealPowerDerivedTensor.idealPowerInclusion_factors_through_derivedTensor
statement: formalized
proof: formalized
---

# 15.103 Systems of modules, bis

Section 15.103 of the Stacks Project, [Tag 0G3J](https://stacks.math.columbia.edu/tag/0G3J). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G3K, a lemma

[Tag 0G3K](https://stacks.math.columbia.edu/tag/0G3K) in the Stacks Project.

**`Stacks.AdicSystem.Homology.homologyIdealPowers_proIsomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/Homology/IdealPowerComparison.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/Homology/IdealPowerComparison.lean#L408).

> **Stacks 0G3K.** The homology of the complex of ideal powers is canonically
> pro-isomorphic to the ideal powers of the homology.

```lean
public theorem homologyIdealPowers_proIsomorphic
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {K : Type v} {L : Type w} {M : Type x}
    [AddCommGroup K] [AddCommGroup L] [AddCommGroup M]
    [Module A K] [Module A L] [Module A M]
    [Module.Finite A K] [Module.Finite A L] [Module.Finite A M]
    (I : Ideal A) (α : K →ₗ[A] L) (β : L →ₗ[A] M)
    (_hβα : β.comp α = 0) :
    let P : ℕ → Submodule A L := fun n =>
      LinearMap.ker β ⊓ (I ^ n • (⊤ : Submodule A L))
    let D : (n : ℕ) → Submodule A (P n) := fun n =>
      Submodule.comap (P n).subtype
        (Submodule.map α (I ^ n • (⊤ : Submodule A K)))
    let H : ℕ → Type _ := fun n => (P n) ⧸ D n
    let Q : ℕ → Type _ := fun n =>
      ↥(I ^ n • (⊤ : Submodule A (H 0)))
    ∃ (τ : ∀ (m n : ℕ), n ≤ m → H m →ₗ[A] H n),
      (∀ n, τ n n (le_refl n) = LinearMap.id) ∧
      (∀ (k m n : ℕ) (hkm : m ≤ k) (hmn : n ≤ m),
        (τ m n hmn).comp (τ k m hkm) = τ k n (hmn.trans hkm)) ∧
      (∀ (m n : ℕ) (hmn : n ≤ m) (y : P m),
        ∃ z : P n, z.1 = y.1 ∧
          τ m n hmn (Submodule.Quotient.mk y : H m) =
            (Submodule.Quotient.mk z : H n)) ∧
      ∃ c : ℕ, 0 < c ∧
        ∃ (ρ : ∀ (n : ℕ), c ≤ n → H n →ₗ[A]
              ↥(I ^ (n - c) • (⊤ : Submodule A (H 0))))
          (ψ : ∀ (n : ℕ), c ≤ n →
              ↥(I ^ n • (⊤ : Submodule A (H 0))) →ₗ[A] H (n - c)),
          (∀ (n : ℕ) (hn : c ≤ n) (z : H n),
            ((ρ n hn z : ↥(I ^ (n - c) • (⊤ : Submodule A (H 0)))) : H 0) =
              τ n 0 (Nat.zero_le n) z) ∧
          (∀ (n : ℕ) (hn : c ≤ n)
            (z : ↥(I ^ n • (⊤ : Submodule A (H 0)))) (y : P n),
            y.1 ∈ I ^ n • LinearMap.ker β →
            (z : H 0) = τ n 0 (Nat.zero_le n) (Submodule.Quotient.mk y : H n) →
            ψ n hn z = τ n (n - c) (Nat.sub_le n c)
              (Submodule.Quotient.mk y : H n)) ∧
          (∀ (m n : ℕ) (hmn : n ≤ m) (hm : c ≤ m) (hn : c ≤ n)
            (z : ↥(I ^ m • (⊤ : Submodule A (H 0))))
            (z' : ↥(I ^ n • (⊤ : Submodule A (H 0)))),
            (z' : H 0) = z →
            τ (m - c) (n - c) (Nat.sub_le_sub_right hmn c) (ψ m hm z) =
              ψ n hn z') ∧
          (∀ (n : ℕ) (hn : 2 * c ≤ n)
            (z : ↥(I ^ n • (⊤ : Submodule A (H 0)))),
            (((ρ (n - c) (by omega) (ψ n (by omega) z) :
                ↥(I ^ ((n - c) - c) • (⊤ : Submodule A (H 0)))) : H 0) = z.1)) ∧
          (∀ (n : ℕ) (hn : 2 * c ≤ n) (z : H n),
            ψ (n - c) (by omega) (ρ n (by omega) z) =
              τ n ((n - c) - c) (by omega) z) ∧
          -- The standard explicit witness that the two inverse systems are
          -- isomorphic as pro-objects, using the cofinal shift `n ↦ n + c`.
          ∃ (forward : ∀ m : ℕ, H (m + c) →ₗ[A] Q m)
              (backward : ∀ m : ℕ, Q (m + c) →ₗ[A] H m),
            (∀ (m m' : ℕ) (h : m ≤ m') (z : H (m' + c)),
              ((forward m (τ (m' + c) (m + c) (by omega) z) : Q m) : H 0) =
                (forward m' z : H 0)) ∧
            (∀ (m m' : ℕ) (h : m ≤ m') (z : Q (m' + c)) (z' : Q (m + c)),
              (z' : H 0) = z →
                backward m z' = τ m' m h (backward m' z)) ∧
            (∀ (m : ℕ) (z : H ((m + c) + c)),
              backward m (forward (m + c) z) =
                τ ((m + c) + c) m (by omega) z) ∧
            (∀ (m : ℕ) (z : Q ((m + c) + c)),
              ((forward m (backward (m + c) z) : Q m) : H 0) = z)
```

## Tag 0G3L, a lemma

[Tag 0G3L](https://stacks.math.columbia.edu/tag/0G3L) in the Stacks Project.

**`Stacks.AdicSystem.ExtIdealPowerRestriction.ext_ideal_power_restriction_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean#L527).

> **Stacks 0G3L.** Restriction on positive-degree Ext from a finite module to a sufficiently
> high ideal power factors through Ext into a shifted ideal power of the second module.

```lean
public theorem ext_ideal_power_restriction_factors
    {A : Type u} [CommRing A] [IsNoetherianRing A] [Small.{v} A]
    {M N : Type v} [AddCommGroup M] [Module A M]
    [AddCommGroup N] [Module A N] [Module.Finite A M]
    (I : Ideal A) (p : ℕ) (_hp : 0 < p) :
    ∃ c : ℕ, ∀ n : ℕ, c ≤ n →
      let P : Submodule A M := I ^ n • ⊤
      let Q : Submodule A N := I ^ (n - c) • ⊤
      ∃ lift : Ext (ModuleCat.of A M) (ModuleCat.of A N) p →+
          Ext (ModuleCat.of A P) (ModuleCat.of A Q) p,
        ((Ext.mk₀ (ModuleCat.ofHom Q.subtype)).postcomp
            (ModuleCat.of A P) (add_zero p)).comp lift =
          (Ext.mk₀ (ModuleCat.ofHom P.subtype)).precomp
            (ModuleCat.of A N) (zero_add p)
```

## Tag 0927, a lemma

[Tag 0927](https://stacks.math.columbia.edu/tag/0927) in the Stacks Project.

**`Stacks.AdicSystem.ExtRestrictionVanishing.ext_ideal_power_restriction_eq_zero_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean#L560).

> **Stacks 0927.** If a power of an ideal annihilates `N`, then in every positive degree,
> restriction on Ext from a finite module to some ideal power is zero.

```lean
public theorem ext_ideal_power_restriction_eq_zero_of_annihilated
    {A : Type u} [CommRing A] [IsNoetherianRing A] [Small.{v} A]
    {M N : Type v} [AddCommGroup M] [Module A M]
    [AddCommGroup N] [Module A N] [Module.Finite A M]
    (I : Ideal A) (hN : ∃ m : ℕ, 0 < m ∧ I ^ m • (⊤ : Submodule A N) = ⊥)
    (p : ℕ) (hp : 0 < p) :
    ∃ n : ℕ,
      let P : Submodule A M := I ^ n • ⊤
      (Ext.mk₀ (ModuleCat.ofHom P.subtype)).precomp
          (ModuleCat.of A N) (zero_add p) = 0
```

## Tag 0DYI, a lemma

[Tag 0DYI](https://stacks.math.columbia.edu/tag/0DYI) in the Stacks Project.

**`Stacks.ExtIdealPowerImage.range_ext_map_ideal_pow_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean, line 847](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean#L847).

> **Stacks 0DYI.** In each degree, the image in `Ext(K, M)` of the Ext group with second
> argument `I ^ n M` is eventually contained in `I ^ (n - c) Ext(K, M)`.

```lean
public theorem range_ext_map_ideal_pow_le
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (K : DerivedCategory (ModuleCat.{v} A))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (M : ModuleCat.{v} A)
    [Module.Finite A M] (p : ℤ) :
    ∃ c : ℕ, ∀ n : ℕ, c ≤ n →
      Set.range (fun x : DerivedCategory.Ext K
          ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
            (ModuleCat.of A ↥(I ^ n • (⊤ : Submodule A M)))) p ↦
        x ≫ ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).map
          (ModuleCat.ofHom (I ^ n • (⊤ : Submodule A M)).subtype))⟦p⟧') ⊆
        ((I ^ (n - c) • (⊤ : Submodule A
          (DerivedCategory.Ext K
            ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj M) p)) :
            Submodule A _) : Set _)
```

## Tag 0G3M, a lemma

[Tag 0G3M](https://stacks.math.columbia.edu/tag/0G3M) in the Stacks Project.

**`Stacks.AdicSystem.KoszulIdealPower.idealPowerSystem_proIso_koszulIdealComplexSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/IdealPowerTensor.lean, line 929](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/IdealPowerTensor.lean#L929).

> **Stacks Project, Tag 0G3M.** Over a Noetherian ring, the inverse system of positive
> powers of the ideal generated by a finite sequence and the inverse system of shifted,
> positive-degree Koszul complexes on its positive powers are pro-isomorphic in the derived
> category. The comparison is induced by the Koszul differential into the corresponding ideal
> power; the displayed identities express a two-sided inverse after cofinal refinement.

```lean
public theorem idealPowerSystem_proIso_koszulIdealComplexSystem
    {A : Type u} [CommRing A] [IsNoetherianRing A] {r : ℕ} (f : Fin r → A) :
    let I := Ideal.span (Set.range f)
    ∃ (ε : ∀ n : ℕ,
        koszulIdealComplex (fun i ↦ f i ^ (n + 1)) ⟶
          (ChainComplex.single₀ (ModuleCat.{u} A)).obj
            (ModuleCat.of A ↥(I ^ (n + 1))))
      (e : koszulIdealComplexSystem f ⟶ idealPowerSystem I),
      (∀ n,
        (ε n).f 0 ≫ ModuleCat.ofHom (I ^ (n + 1)).subtype =
          (koszulIdealComplexXIso (fun i ↦ f i ^ (n + 1)) 0).hom ≫
            (Koszul.seqComplex (fun i ↦ f i ^ (n + 1))).d 1 0 ≫
            ModuleCat.ofHom
              (exteriorPower.zeroEquiv A (Fin r → A)).toLinearMap) ∧
      (∀ n,
        e.app (op n) = DerivedCategory.Q.map
          (HomologicalComplex.extendMap (ε n) ComplexShape.embeddingDownNat)) ∧
      ∀ n : ℕ, ∃ (m : ℕ) (h : n ≤ m)
        (s : (idealPowerSystem I).obj (op m) ⟶
          (koszulIdealComplexSystem f).obj (op n)),
        e.app (op m) ≫ s =
            (koszulIdealComplexSystem f).map (homOfLE h).op ∧
          s ≫ e.app (op n) =
            (idealPowerSystem I).map (homOfLE h).op
```

## Tag 0G3N, a lemma

[Tag 0G3N](https://stacks.math.columbia.edu/tag/0G3N) in the Stacks Project.

**`Stacks.AdicSystem.IdealPowerTensorComparison.derivedTensor_idealPowers_proIsomorphic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/CanonicalDerivedTensor.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/CanonicalDerivedTensor.lean#L100).

> **Stacks Project, Tag 0G3N.** For a bounded complex of finite modules over a Noetherian
> ring, the inverse system of maps `Iⁿ ⊗ᴸ M → Iⁿ M` formed from the canonical derived tensor
> product is an isomorphism of pro-objects in the derived category. The displayed identities are
> the two-sided inverse identities after cofinal refinement.

```lean
public theorem derivedTensor_idealPowers_proIsomorphic {A : Type u} [CommRing A]
    [IsNoetherianRing A] (I : Ideal A) (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hbounded : ∃ a b : ℤ, a ≤ b ∧ ∀ i : ℤ, i < a ∨ b < i → IsZero (M.X i))
    (hfinite : ∀ i : ℤ, Module.Finite A (M.X i)) :
    ∃ (t : ∀ n, idealPowerComplex M I (n + 1) ⟶ idealPowerComplex M I n)
      (_ht : ∀ n, t n ≫ image.ι (idealPowerMultiplication M I n) =
        image.ι (idealPowerMultiplication M I (n + 1)))
      (α : derivedTensorIdealSystem (DerivedTensorData.canonicalDerivedTensorProduct A)
          (DerivedTensorData.canonicalSymmetry A) M I ⟶ idealPowerSystem M I t),
      (∀ n, α.app (op n) = derivedToIdealPowerMap
        (DerivedTensorData.canonicalDerivedTensorProduct A)
        (DerivedTensorData.canonicalSymmetry A) M I n) ∧
      ∀ n : ℕ, ∃ (m : ℕ) (h : n ≤ m)
        (s : (idealPowerSystem M I t).obj (op m) ⟶
          (derivedTensorIdealSystem (DerivedTensorData.canonicalDerivedTensorProduct A)
            (DerivedTensorData.canonicalSymmetry A) M I).obj (op n)),
        α.app (op m) ≫ s =
            (derivedTensorIdealSystem (DerivedTensorData.canonicalDerivedTensorProduct A)
              (DerivedTensorData.canonicalSymmetry A) M I).map (homOfLE h).op ∧
          s ≫ α.app (op n) = (idealPowerSystem M I t).map (homOfLE h).op
```

## Tag 0928, a lemma

[Tag 0928](https://stacks.math.columbia.edu/tag/0928) in the Stacks Project.

**`Stacks.AdicSystem.IdealPowerDerivedTensor.idealPowerInclusion_factors_through_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/CanonicalDerivedTensor.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/CanonicalDerivedTensor.lean#L134).

> **Stacks Project, Tag 0928.** For a finite module over a Noetherian ring, the inclusion of
> some positive ideal power factors through the canonical map from the canonical derived tensor
> product with the ideal. The index `n` represents the positive exponent `n + 1`.

```lean
public theorem idealPowerInclusion_factors_through_derivedTensor
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (M : ModuleCat.{v} A) [Module.Finite A M] :
    letI := Module.Finite.small.{u} A M
    let K := (CochainComplex.singleFunctor (ModuleCat.{u} A) 0).obj
      (ModuleCat.of A (Shrink.{u} M))
    ∃ n : ℕ,
      ∃ f : DerivedCategory.Q.obj
          (Stacks.AdicSystem.IdealPowerTensorComparison.idealPowerComplex K I n) ⟶
          (Stacks.AdicSystem.IdealPowerTensorComparison.derivedTensorIdealSystem
            (DerivedTensorData.canonicalDerivedTensorProduct A)
            (DerivedTensorData.canonicalSymmetry A) K I).obj (op 0),
        f ≫
            (Stacks.AdicSystem.IdealPowerTensorComparison.derivedToIdealPowerMap
                (DerivedTensorData.canonicalDerivedTensorProduct A)
                (DerivedTensorData.canonicalSymmetry A) K I 0 ≫
              DerivedCategory.Q.map
                (image.ι (Stacks.AdicSystem.IdealPowerTensorComparison.idealPowerMultiplication K I
                  0))) =
          DerivedCategory.Q.map
            (image.ι (Stacks.AdicSystem.IdealPowerTensorComparison.idealPowerMultiplication K I n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.103, Tag 0G3J](https://stacks.math.columbia.edu/tag/0G3J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
