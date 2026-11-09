---
declaration: theorem
origin: cited
lean: TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero
statement: formalized
proof: formalized
---

# The Main Lemma, per character (Miyake, Lemma 4.6.8; Diamond–Shurman, Theorem 5.7.1)

a
cusp form in `S_k(Γ₁(N), χ)` whose Fourier coefficients vanish at every index coprime to `N`
lies in the old subspace. It is a sum, over the primes `p ∣ N`, of forms of the same nebentypus
supported on the multiples of `p`, and each of those is old.

```lean
TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero {N : ℕ} [NeZero N] {k : ℤ}
  {χ : (ZMod N)ˣ →* ℂˣ}
  {f : CuspForm (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) (CongruenceSubgroup.Gamma1 N)) k}
  (hf : f ∈ TauCeti.cuspFormCharSpace k χ)
  (hvan : ∀ (n : ℕ), n.Coprime N → (PowerSeries.coeff n) (UpperHalfPlane.qExpansion 1 ⇑f) = 0) :
  f ∈ TauCeti.cuspFormsOld N k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimura's decomposition of a double coset into right cosets](../../part-02/hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/MainLemma.html#TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/MainLemma.html#TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero)
- [Source of `TauCeti.mem_cuspFormsOld_of_forall_coprime_qExpansion_coeff_eq_zero` in TauCeti/NumberTheory/ModularForms/Newforms/MainLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Newforms/MainLemma.lean#L177)
