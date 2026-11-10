---
declaration: section
origin: cited
lean: isFormallySmooth_mvPowerSeries, main_theorem_one, main_theorem_two, main_theorem_three, main_theorem_four, exists_powerSeries_presentation_of_isLocalHom, isNoetherianCompleteLocalRing_pullback
statement: formalized
proof: formalized
---

# 15.40 Some results on power series rings

Section 15.40 of the Stacks Project, [Tag 07NK](https://stacks.math.columbia.edu/tag/07NK). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07NL, a lemma

[Tag 07NL](https://stacks.math.columbia.edu/tag/07NL) in the Stacks Project.

**`isFormallySmooth_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesFormallySmooth.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesFormallySmooth.lean#L622).

> **Stacks 07NL.** Formal power series rings over a characteristic-zero field,
> over a field of characteristic `p`, and over a Cohen ring are formally smooth
> over `ℚ`, `𝔽_p`, and `ℤ`, respectively, for their maximal-ideal-adic topologies.

```lean
public theorem isFormallySmooth_mvPowerSeries.{u} (n p : ℕ)
    (K L Λ : Type*) [Field K] [CharZero K] [Field L] [Fact p.Prime] [CharP L p]
    [CommRing Λ] [IsDomain Λ] [IsCohenRing Λ] :
    letI : Algebra (ZMod p) L := ZMod.algebra L p
    @IsFormallySmooth.{u} ℚ (MvPowerSeries (Fin n) K) inferInstance
        (⊥ : Ideal ℚ).adicTopology (⊥ : Ideal ℚ).ringFilterBasis.isTopologicalRing
        (Ideal.isLinearTopology ⊥) inferInstance
        (IsLocalRing.maximalIdeal (MvPowerSeries (Fin n) K)).adicTopology
        (IsLocalRing.maximalIdeal (MvPowerSeries (Fin n) K)).ringFilterBasis.isTopologicalRing
        (Ideal.isLinearTopology _) (algebraMap ℚ (MvPowerSeries (Fin n) K)) ∧
      @IsFormallySmooth.{u} (ZMod p) (MvPowerSeries (Fin n) L) inferInstance
          (⊥ : Ideal (ZMod p)).adicTopology
          (⊥ : Ideal (ZMod p)).ringFilterBasis.isTopologicalRing
          (Ideal.isLinearTopology ⊥) inferInstance
          (IsLocalRing.maximalIdeal (MvPowerSeries (Fin n) L)).adicTopology
          (IsLocalRing.maximalIdeal (MvPowerSeries (Fin n) L)).ringFilterBasis.isTopologicalRing
          (Ideal.isLinearTopology _) (algebraMap (ZMod p) (MvPowerSeries (Fin n) L)) ∧
        @IsFormallySmooth.{u} ℤ (MvPowerSeries (Fin n) Λ) inferInstance
          (⊥ : Ideal ℤ).adicTopology (⊥ : Ideal ℤ).ringFilterBasis.isTopologicalRing
          (Ideal.isLinearTopology ⊥) inferInstance
          (IsLocalRing.maximalIdeal (MvPowerSeries (Fin n) Λ)).adicTopology
          (IsLocalRing.maximalIdeal (MvPowerSeries (Fin n) Λ)).ringFilterBasis.isTopologicalRing
          (Ideal.isLinearTopology _) (algebraMap ℤ (MvPowerSeries (Fin n) Λ))
```

## Tag 07NM, a lemma

[Tag 07NM](https://stacks.math.columbia.edu/tag/07NM) in the Stacks Project.

**`main_theorem_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean#L148). The attribute's comment: “(1)”. References: SGA 1 II (4.14), “special case”; SGA 1 III (2.3), “special case”; SGA 2 IV (5.5), “special case”; SGA 3 VIIB (5.5.2), “partial”.

> **Statement (1).** If `y_1, ..., y_n` is a regular system of parameters of
> `A = K[[x_1, ..., x_n]]`, then the canonical substitution map
> `K[[Y_1, ..., Y_n]] → A`, `Y_i ↦ y_i`, is an isomorphism.
>
> The canonical map is `MvPowerSeries.substAlgHom (hasSubst_of_mem_maximalIdeal y)`: the
> substitution `X i ↦ y i`, which is defined precisely because each `y i` lies in `m_A` and
> hence has zero constant coefficient, and which is the unique continuous `K`-algebra map
> sending `X i` to `y i`. The conclusion states that *this* map sends `X i` to `y i` and is
> bijective — i.e. is an isomorphism of `K`-algebras.

```lean
theorem main_theorem_one (K : Type*) [Field K] (n : ℕ)
    (y : Fin n → maximalIdeal (MvPowerSeries (Fin n) K)) (hy : IsRegularSystemOfParameters y) :
    (∀ i,
        (MvPowerSeries.substAlgHom (hasSubst_of_mem_maximalIdeal y) :
            MvPowerSeries (Fin n) K →ₐ[K] MvPowerSeries (Fin n) K)
          (MvPowerSeries.X i) = (y i : MvPowerSeries (Fin n) K)) ∧
      Function.Bijective
        ((MvPowerSeries.substAlgHom (hasSubst_of_mem_maximalIdeal y) :
          MvPowerSeries (Fin n) K →ₐ[K] MvPowerSeries (Fin n) K))
```

**`main_theorem_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean#L217). The attribute's comment: “(2)”. References: EGA 0 (17.1.4), “more general”; EGA 0 (17.1.7), “special case”.

> **Statement (2).** If `z_1, ..., z_r` form part of a regular system of parameters for
> `A = K[[x_1, ..., x_n]]`, then `r <= n` and `A/(z_1, ..., z_r)` is isomorphic (as a
> `K`-algebra) to the power series ring `K[[Y_1, ..., Y_{n-r}]]`.

```lean
theorem main_theorem_two (K : Type*) [Field K] (n r : ℕ)
    (z : Fin r → maximalIdeal (MvPowerSeries (Fin n) K))
    (hz : FormsPartOfRegularSystemOfParameters z) :
    r ≤ n ∧
      Nonempty
        ((MvPowerSeries (Fin n) K ⧸
            Ideal.span (Set.range (fun i => (z i : MvPowerSeries (Fin n) K)))) ≃ₐ[K]
          MvPowerSeries (Fin (n - r)) K)
```

**`main_theorem_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean#L594). The attribute's comment: “(3)”. References: SGA 1 III (2.3), “special case”.

> **Statement (3).** Let `Lambda` be a Cohen ring with uniformizer the prime number
> `pr`, and let `B = Lambda[[x_1, ..., x_n]]`. If `p, y_1, ..., y_n` is a regular system of
> parameters of `B` (where `p = pr` viewed in `B` via the coefficient inclusion), then the
> canonical `Lambda`-algebra homomorphism `Lambda[[Y_1, ..., Y_n]] -> B` sending `Y_i` to
> `y_i` — `cohenSubstAlgHom`, the `m_Λ`-adic translation followed by substitution of the
> normalized family — is an isomorphism: it sends `X i` to `y i` and it is bijective.

```lean
theorem main_theorem_three (Λ : Type*) [CommRing Λ] [IsDomain Λ] [IsDiscreteValuationRing Λ]
    (hΛ : IsCohenRing Λ) (n : ℕ) (pr : ℕ) (hunif : maximalIdeal Λ = Ideal.span {(pr : Λ)})
    (p : maximalIdeal (MvPowerSeries (Fin n) Λ))
    (hp : (p : MvPowerSeries (Fin n) Λ) = algebraMap Λ (MvPowerSeries (Fin n) Λ) (pr : Λ))
    (y : Fin n → maximalIdeal (MvPowerSeries (Fin n) Λ))
    (hrsp : IsRegularSystemOfParameters (Fin.cons p y)) :
    (∀ i, cohenSubstAlgHom hΛ y (MvPowerSeries.X i) = (y i : MvPowerSeries (Fin n) Λ)) ∧
      Function.Bijective (cohenSubstAlgHom hΛ y)
```

**`main_theorem_four`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean, line 778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesMaps.lean#L778). The attribute's comment: “(4)”. References: EGA 0 (17.1.7), “special case”.

> **Statement (4).** Let `Lambda` be a Cohen ring with uniformizer the prime number
> `pr`, and let `B = Lambda[[x_1, ..., x_n]]`. If `p, z_1, ..., z_r` form part of a regular
> system of parameters for `B` (the length-`(r+1)` sequence `p, z_1, ..., z_r`, with `p`
> the uniformizer viewed in `B`), then `r <= n` and `B/(z_1, ..., z_r)` is isomorphic (as a
> `Lambda`-algebra) to the power series ring `Lambda[[Y_1, ..., Y_{n-r}]]`.

```lean
theorem main_theorem_four (Λ : Type*) [CommRing Λ] [IsDomain Λ] [IsDiscreteValuationRing Λ]
    (hΛ : IsCohenRing Λ) (n r : ℕ) (pr : ℕ) (hunif : maximalIdeal Λ = Ideal.span {(pr : Λ)})
    (p : maximalIdeal (MvPowerSeries (Fin n) Λ))
    (hp : (p : MvPowerSeries (Fin n) Λ) = algebraMap Λ (MvPowerSeries (Fin n) Λ) (pr : Λ))
    (z : Fin r → maximalIdeal (MvPowerSeries (Fin n) Λ))
    (hz : FormsPartOfRegularSystemOfParameters (Fin.cons p z)) :
    r ≤ n ∧
      Nonempty
        ((MvPowerSeries (Fin n) Λ ⧸
            Ideal.span (Set.range (fun i => (z i : MvPowerSeries (Fin n) Λ)))) ≃ₐ[Λ]
          MvPowerSeries (Fin (n - r)) Λ)
```

## Tag 07NN, a lemma

[Tag 07NN](https://stacks.math.columbia.edu/tag/07NN) in the Stacks Project.

**`exists_powerSeries_presentation_of_isLocalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesFormallySmooth.lean, line 1087](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesFormallySmooth.lean#L1087). References: EGA 0 (19.8.8), “more general”; SGA 2 IV (4.8), “more general”; SGA 2 IX (2.3), “more general”.

> **Stacks 07NN.** A local homomorphism `A → B` of Noetherian complete local rings admits
> a commutative presentation by surjections from power series rings `R` and `S`. According to the
> residue characteristic, these are power series rings over fields or over Cohen rings. The map
> `R → S` carries a regular system of parameters to part of one, is flat, and has regular closed
> fibre.

```lean
public theorem exists_powerSeries_presentation_of_isLocalHom
    {A : Type u} {B : Type v}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    [CommRing B] [IsNoetherianRing B] [IsLocalRing B]
    [IsAdicComplete (IsLocalRing.maximalIdeal B) B]
    (f : A →+* B) [IsLocalHom f] :
    ∃ (R S : Type (max u v)) (_ : CommRing R) (_ : IsRegularLocalRing R)
      (_ : IsAdicComplete (IsLocalRing.maximalIdeal R) R)
      (_ : CommRing S) (_ : IsRegularLocalRing S)
      (_ : IsAdicComplete (IsLocalRing.maximalIdeal S) S)
      (g : R →+* S) (qA : R →+* A) (qB : S →+* B),
      Function.Surjective qA ∧ Function.Surjective qB ∧
      IsLocalHom g ∧ IsLocalHom qA ∧ IsLocalHom qB ∧
      f.comp qA = qB.comp g ∧
      (∃ (xs : List R) (ys : List S) (zs : List S),
        Ideal.ofList xs = IsLocalRing.maximalIdeal R ∧
        xs.length = (IsLocalRing.maximalIdeal R).spanFinrank ∧
        Ideal.ofList ys = IsLocalRing.maximalIdeal S ∧
        ys.length = (IsLocalRing.maximalIdeal S).spanFinrank ∧
        ys = xs.map g ++ zs ∧
        (ringChar (IsLocalRing.ResidueField A) = 0 →
          ∃ (nR nS : ℕ) (kR kS : Type (max u v)) (_ : Field kR) (_ : Field kS),
            Nonempty (R ≃+* MvPowerSeries (Fin nR) kR) ∧
            Nonempty (S ≃+* MvPowerSeries (Fin nS) kS)) ∧
        (∀ p : ℕ, 0 < p → ringChar (IsLocalRing.ResidueField A) = p →
          ∃ (nR nS : ℕ) (ΛR ΛS : Type (max u v))
            (_ : CommRing ΛR) (_ : IsDomain ΛR) (_ : IsCohenRing ΛR)
            (_ : CommRing ΛS) (_ : IsDomain ΛS) (_ : IsCohenRing ΛS),
            Nonempty (R ≃+* MvPowerSeries (Fin nR) ΛR) ∧
            Nonempty (S ≃+* MvPowerSeries (Fin nS) ΛS) ∧
            IsLocalRing.maximalIdeal ΛR = Ideal.span {(p : ΛR)} ∧
            IsLocalRing.maximalIdeal ΛS = Ideal.span {(p : ΛS)} ∧
            ∃ xs', xs = (p : R) :: xs')) ∧
      letI : Algebra R S := g.toAlgebra
      Module.Flat R S ∧
        IsRegularLocalRing (S ⧸ Ideal.map g (IsLocalRing.maximalIdeal R))
```

## Tag 09Q8, a lemma

[Tag 09Q8](https://stacks.math.columbia.edu/tag/09Q8) in the Stacks Project.

**`isNoetherianCompleteLocalRing_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesFormallySmooth.lean, line 1415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CompleteLocalRing/PowerSeriesFormallySmooth.lean#L1415). References: EGA IV (19.3.2.1), “(iii)”.

> **Stacks 09Q8.** The pullback of two surjective maps of complete Noetherian local rings is
> again a complete Noetherian local ring.

```lean
public theorem isNoetherianCompleteLocalRing_pullback.{u, v, w}
    {R : Type u} {S : Type v} {S' : Type w}
    [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    [CommRing S] [IsLocalRing S] [IsNoetherianRing S]
    [IsAdicComplete (IsLocalRing.maximalIdeal S) S]
    [CommRing S'] [IsLocalRing S'] [IsNoetherianRing S']
    [IsAdicComplete (IsLocalRing.maximalIdeal S') S']
    (f : S →+* R) (f' : S' →+* R)
    (hf : Function.Surjective f) (hf' : Function.Surjective f') :
    ∃ hlocal : IsLocalRing (f.pullback f'),
      letI := hlocal
      IsNoetherianRing (f.pullback f') ∧
        IsAdicComplete (IsLocalRing.maximalIdeal (f.pullback f')) (f.pullback f')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.40, Tag 07NK](https://stacks.math.columbia.edu/tag/07NK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
