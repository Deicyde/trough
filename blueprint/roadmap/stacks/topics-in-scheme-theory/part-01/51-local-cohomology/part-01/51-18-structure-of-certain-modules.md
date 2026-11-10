---
declaration: section
origin: cited
lean: MvPowerSeries.exists_linearEquiv_directSum_injectiveHull_of_leibniz, Dualizing.isIPowerTorsion_frobeniusStable_exists_equiv_directSum_injectiveHull
statement: formalized
proof: formalized
---

# 51.18 Structure of certain modules

Section 51.18 of the Stacks Project, [Tag 0EC1](https://stacks.math.columbia.edu/tag/0EC1). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EC2, a lemma

[Tag 0EC2](https://stacks.math.columbia.edu/tag/0EC2) in the Stacks Project.

**`MvPowerSeries.exists_linearEquiv_directSum_injectiveHull_of_leibniz`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/MvPowerSeries/LeibnizTorsionModule.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/MvPowerSeries/LeibnizTorsionModule.lean#L703).

> A maximal-ideal-power-torsion module over a characteristic-zero formal power series ring,
> equipped with additive operators satisfying the partial-derivative Leibniz rules, is a direct sum
> of copies of an injective hull of the residue field.

```lean
theorem exists_linearEquiv_directSum_injectiveHull_of_leibniz
    (k : Type u) [Field k] [CharZero k]
    (d : ℕ) (_hd : 0 < d)
    (M : Type v) [AddCommGroup M] [Module (MvPowerSeries (Fin d) k) M]
    (E : Type u) [AddCommGroup E] [Module (MvPowerSeries (Fin d) k) E]
    (i : (ModuleCat.restrictScalars
        (MvPowerSeries.constantCoeff : MvPowerSeries (Fin d) k →+* k)).obj
          (ModuleCat.of k k) ⟶ ModuleCat.of (MvPowerSeries (Fin d) k) E)
    [Mono i]
    (_hi : Module.IsInjectiveHull i)
    (_hM : IsIPowerTorsion (MvPowerSeries (Fin d) k) M
      (IsLocalRing.maximalIdeal (MvPowerSeries (Fin d) k)))
    (D : Fin d → M →+ M)
    (_hD : ∀ (j : Fin d) (f : MvPowerSeries (Fin d) k) (z : M),
      D j (f • z) = MvPowerSeries.pderiv (R := k) j f • z + f • D j z) :
    ∃ J : Type v, Nonempty (M ≃ₗ[MvPowerSeries (Fin d) k] ⨁ _ : J, E)
```

## Tag 0EC3, a lemma

[Tag 0EC3](https://stacks.math.columbia.edu/tag/0EC3) in the Stacks Project.

**`Dualizing.isIPowerTorsion_frobeniusStable_exists_equiv_directSum_injectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/FrobeniusStableTorsion.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FrobeniusStableTorsion.lean#L620).

> **Stacks Project, Tag 0EC3.** A maximal-ideal-power-torsion module over a regular local ring
> of prime characteristic which is invariant under extension of scalars by Frobenius is a direct
> sum of copies of the injective hull of the residue field.

```lean
public theorem isIPowerTorsion_frobeniusStable_exists_equiv_directSum_injectiveHull
    (p : ℕ) (hp : p.Prime)
    (A : Type u) [CommRing A] [IsRegularLocalRing A] (hchar : (p : A) = 0)
    (M : Type (max u v)) [AddCommGroup M] [Module A M]
    (hM : IsIPowerTorsion A M (IsLocalRing.maximalIdeal A))
    (hF : (ModuleCat.extendScalars (frobeniusOfPrime p hp hchar)).obj
      (ModuleCat.of A M) ≅ ModuleCat.of A M)
    (E : Type u) [AddCommGroup E] [Module A E]
    (i : ModuleCat.of A (IsLocalRing.ResidueField A) ⟶ ModuleCat.of A E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    ∃ J : Type (max u v), Nonempty (M ≃ₗ[A] ⨁ _ : J, E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.18, Tag 0EC1](https://stacks.math.columbia.edu/tag/0EC1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
