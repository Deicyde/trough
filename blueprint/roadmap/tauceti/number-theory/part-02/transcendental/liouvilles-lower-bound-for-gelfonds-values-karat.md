---
declaration: theorem
origin: cited
lean: TauCeti.exists_one_le_pow_mul_norm_gelfond_value
statement: formalized
proof: formalized
---

# Liouville's lower bound for Gelfond's values (Karatarakis–Wiedijk, §3)

Let `K` be a
number field of degree `h`, `α, β, γ ∈ K`, `m ∈ ℕ` and `c ∈ ℝ`. There is `c₂ ≥ 1` with the
following property. Let `q ^ 2 = 2 m n`, `r ≥ n` and `t₀ ≤ m`, and let
`η_{ab} ∈ 𝓞 K`, `a, b < q`, have house at most `c ^ n n ^ ((n + 1) / 2)`, as for Gelfond's
auxiliary function. If
`ρ = ∑_{a, b} η_{ab} ((a + 1) + (b + 1) β) ^ r α ^ ((a + 1) t₀) γ ^ ((b + 1) t₀)` is nonzero, then
`1 ≤ c₂ ^ r r ^ ((h - 1) r) |σ ρ|` for every embedding `σ : K →+* ℂ`. In particular
`|σ ρ| ≥ c₂ ^ (-r) r ^ (-(h - 1) (r + 1))`.

```lean
TauCeti.exists_one_le_pow_mul_norm_gelfond_value.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (α β γ : K) (m : ℕ) (c : ℝ) :
  ∃ c₂,
    1 ≤ c₂ ∧
      ∀ (σ : K →+* ℂ) (n q r t₀ : ℕ) (η : Fin q → Fin q → NumberField.RingOfIntegers K),
        q ^ 2 = 2 * m * n →
          n ≤ r →
            t₀ ≤ m →
              (∀ (a b : Fin q), NumberField.house ↑(η a b) ≤ c ^ n * ↑n ^ ((↑n + 1) / 2)) →
                ∑ a,
                      ∑ b,
                        ↑(η a b) * (↑(↑a + 1) + ↑(↑b + 1) * β) ^ r *
                          (α ^ ((↑a + 1) * t₀) * γ ^ ((↑b + 1) * t₀)) ≠
                    0 →
                  1 ≤
                    c₂ ^ r * ↑r ^ ((Module.finrank ℚ K - 1) * r) *
                      ‖σ
                          (∑ a,
                            ∑ b,
                              ↑(η a b) * (↑(↑a + 1) + ↑(↑b + 1) * β) ^ r *
                                (α ^ ((↑a + 1) * t₀) * γ ^ ((↑b + 1) * t₀)))‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's inequality](../../part-01/diophantine-approximation-and-transcendence/part-01/liouvilles-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_one_le_pow_mul_norm_gelfond_value`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Value.html#TauCeti.exists_one_le_pow_mul_norm_gelfond_value).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_one_le_pow_mul_norm_gelfond_value`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Value.html#TauCeti.exists_one_le_pow_mul_norm_gelfond_value)
- [Source of `TauCeti.exists_one_le_pow_mul_norm_gelfond_value` in TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Value.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Transcendental/GelfondSchneider/Gelfond/Value.lean#L138)
