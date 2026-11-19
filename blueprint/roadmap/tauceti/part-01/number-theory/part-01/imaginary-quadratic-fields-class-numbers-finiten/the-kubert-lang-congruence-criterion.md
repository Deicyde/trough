---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma
statement: formalized
proof: formalized
---

# The Kubert–Lang congruence criterion

Let `(a_i, m_i)` be a finite family of integral
numerators and integral exponents such that
* `gcd(2, N) N` divides `∑ mᵢ aᵢ₁²` and `∑ mᵢ aᵢ₂²`,
* `N` divides `∑ mᵢ aᵢ₁ aᵢ₂`, and
* `12` divides `gcd(12, N) ∑ mᵢ`.

Then the product `∏ g_{aᵢ/N}^{mᵢ}` of Siegel functions is invariant under `Γ(N)`. This removes
every root of unity from the transformation law: no power of the product needs to be taken.

```lean
TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma.{u_1} {N : ℕ} {ι : Type u_1}
  (s : Finset ι) (a : ι → Fin 2 → ℤ) (m : ι → ℤ)
  (h₀ : ↑(Nat.gcd 2 N * N) ∣ ∑ i ∈ s, m i * a i 0 ^ 2)
  (h₁ : ↑(Nat.gcd 2 N * N) ∣ ∑ i ∈ s, m i * a i 1 ^ 2) (h₀₁ : ↑N ∣ ∑ i ∈ s, m i * (a i 0 * a i 1))
  (h₁₂ : 12 ∣ ↑(Nat.gcd 12 N) * ∑ i ∈ s, m i) {γ : Matrix.SpecialLinearGroup (Fin 2) ℤ}
  (hγ : γ ∈ CongruenceSubgroup.Gamma N) (τ : UpperHalfPlane) :
  ∏ i ∈ s, TauCeti.ModularForm.siegelFunction (fun j => ↑(a i j) / ↑N) ↑(γ • τ) ^ m i =
    ∏ i ∈ s, TauCeti.ModularForm.siegelFunction (fun j => ↑(a i j) / ↑N) ↑τ ^ m i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's identity (`TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`)](../../../analysis/part-04/special-functions/eulers-identity-tauceti-tprod-one-add-pow-mul-tp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/Congruence.html#TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/Congruence.html#TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma)
- [Source of `TauCeti.ModularForm.prod_siegelFunction_div_zpow_smul_of_mem_Gamma` in TauCeti/NumberTheory/ModularForms/SiegelFunction/Congruence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/SiegelFunction/Congruence.lean#L442)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
