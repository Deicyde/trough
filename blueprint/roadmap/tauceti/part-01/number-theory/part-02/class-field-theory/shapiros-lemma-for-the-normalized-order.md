---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind, NumberField.InfinitePlace.infiniteSemilocalUnitsTateCohomologyIsoPos, IsDedekindDomain.HeightOneSpectrum.semilocalUnitsTateCohomologyIsoPos, TauCeti.ClassFieldTheory.localEulerCharacteristic_galRepOfQuotient_ind, TauCeti.ClassFieldTheory.semilocalUnitsTateCohomologyIso
statement: formalized
proof: formalized
---

# Shapiro's lemma for the normalized order

For `L` the fixed field of `C ≤ G_K ⧸ V`, the
invariant `φ_K(A) = ‖#A‖_K = |#A|_p ^ [K : ℚ_p]` of the inflation of `Ind_C^{G_K ⧸ V} B` is that of
`B` over `L`: `#Ind B = #B ^ [L : K]` and `[L : ℚ_p] = [K : ℚ_p] [L : K]`.

```lean
TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind {K : Type} [Field K] {L : Type}
  [Field L] [Algebra K L] [FiniteDimensional K L] (σ : L →ₐ[K] SeparableClosure K) (n : ℕ)
  {V : OpenNormalSubgroup (Field.absoluteGaloisGroup K)}
  {C : Subgroup (Field.absoluteGaloisGroup K ⧸ ↑V.toOpenSubgroup)}
  (hσ :
    (TauCeti.absoluteGaloisGroupExtend K L σ).range =
      Subgroup.comap (QuotientGroup.mk' ↑V.toOpenSubgroup) C)
  (B : Rep.{0, 0, 0} (ZMod n) ↥C) (p : ℕ) [Fact (Nat.Prime p)] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [TauCeti.FinitePadicExtension K p] [ValuativeRel L]
  [TopologicalSpace L] [IsNonarchimedeanLocalField L] [TauCeti.FinitePadicExtension L p]
  [IsScalarTower ℚ_[p] K L] [Finite ↑B] :
  TauCeti.ClassFieldTheory.localCardNorm p
      ((TauCeti.ClassFieldTheory.galRepOfQuotient n K V).obj (Rep.ind C.subtype B)) =
    TauCeti.ClassFieldTheory.localCardNorm p (TauCeti.ClassFieldTheory.shapiroGalRep σ n hσ B)
```

## Depends on

- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)

## Proof depends on

- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Induced.html#TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind).

## Other forms

**Shapiro's lemma for infinite semi-local units in positive degrees.** Formalized in Tau Ceti as [`NumberField.InfinitePlace.infiniteSemilocalUnitsTateCohomologyIsoPos`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/SemilocalUnits.html#NumberField.InfinitePlace.infiniteSemilocalUnitsTateCohomologyIsoPos).

```lean
NumberField.InfinitePlace.infiniteSemilocalUnitsTateCohomologyIsoPos {K L : Type} [Field K]
  [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (v : NumberField.InfinitePlace K) (w : NumberField.InfinitePlace L) [w.LiesOver v] (n : ℕ)
  [NeZero n] :
  tateCohomology (TauCeti.GlobalNumberFields.infiniteSemilocalUnitsRep L v) ↑n ≅
    tateCohomology (Rep.ofAlgebraAutOnUnits v.Completion w.Completion) ↑n
```

**Shapiro's lemma for semi-local units in positive degrees.** Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.semilocalUnitsTateCohomologyIsoPos`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/SemilocalUnits.html#IsDedekindDomain.HeightOneSpectrum.semilocalUnitsTateCohomologyIsoPos).

```lean
IsDedekindDomain.HeightOneSpectrum.semilocalUnitsTateCohomologyIsoPos {K L : Type} [Field K]
  [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))
  (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L))
  [w.asIdeal.LiesOver v.asIdeal] (n : ℕ) [NeZero n] :
  tateCohomology (TauCeti.semilocalUnitsRep L v) ↑n ≅
    tateCohomology
      (Rep.ofAlgebraAutOnUnits (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
        (IsDedekindDomain.HeightOneSpectrum.adicCompletion L w))
      ↑n
```

**Shapiro's lemma for the local Euler characteristic.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localEulerCharacteristic_galRepOfQuotient_ind`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Induced.html#TauCeti.ClassFieldTheory.localEulerCharacteristic_galRepOfQuotient_ind).

```lean
TauCeti.ClassFieldTheory.localEulerCharacteristic_galRepOfQuotient_ind {K : Type} [Field K]
  {L : Type} [Field L] [Algebra K L] [FiniteDimensional K L] (σ : L →ₐ[K] SeparableClosure K)
  (n : ℕ) {V : OpenNormalSubgroup (Field.absoluteGaloisGroup K)}
  {C : Subgroup (Field.absoluteGaloisGroup K ⧸ ↑V.toOpenSubgroup)}
  (hσ :
    (TauCeti.absoluteGaloisGroupExtend K L σ).range =
      Subgroup.comap (QuotientGroup.mk' ↑V.toOpenSubgroup) C)
  (B : Rep.{0, 0, 0} (ZMod n) ↥C) [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] (hn : ↑n ≠ 0) [Finite ↑B] :
  TauCeti.ClassFieldTheory.localEulerCharacteristic hn
      ((TauCeti.ClassFieldTheory.galRepOfQuotient n K V).obj (Rep.ind C.subtype B)) =
    TauCeti.ClassFieldTheory.localEulerCharacteristic ⋯
      (TauCeti.ClassFieldTheory.shapiroGalRep σ n hσ B)
```

**Shapiro's lemma for the semi-local units.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.semilocalUnitsTateCohomologyIso`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/SemilocalUnits.html#TauCeti.ClassFieldTheory.semilocalUnitsTateCohomologyIso).

```lean
TauCeti.ClassFieldTheory.semilocalUnitsTateCohomologyIso {K : Type} [Field K] [NumberField K]
  {L : Type} [Field L] [NumberField L] [Algebra K L] [IsGalois K L] [IsCyclic Gal(L/K)]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))
  (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L))
  [w.asIdeal.LiesOver v.asIdeal] (n : ℤ) :
  tateCohomology (TauCeti.semilocalUnitsRep L v) n ≅
    tateCohomology
      (Rep.ofAlgebraAutOnUnits (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
        (IsDedekindDomain.HeightOneSpectrum.adicCompletion L w))
      n
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Induced.html#TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind)
- [Source of `TauCeti.ClassFieldTheory.localCardNorm_galRepOfQuotient_ind` in TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Induced.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Local/EulerCharacteristic/Induced.lean#L144)
