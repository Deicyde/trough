---
declaration: theorem
origin: cited
lean: TauCeti.hadamard_of_orderLE_one
statement: formalized
proof: formalized
---

# Hadamard's theorem at order at most one, with the product taken over all of `ℂ`

for
every `s` the family `ρ ↦ E₁(ρ⁻¹ s) ^ m_ρ` over `ℂ` is multipliable and
`f s = exp (a + b s) ∏' ρ, E₁(ρ⁻¹ s) ^ m_ρ`, where `m_ρ` is the divisor of `f`,
`exp a = f 0` and `b = logDeriv f 0`.

```lean
TauCeti.hadamard_of_orderLE_one {f : ℂ → ℂ} (h : TauCeti.OrderLE f 1) (hf : Differentiable ℂ f)
  (hf0 : f 0 ≠ 0) :
  ∃ a b,
    Complex.exp a = f 0 ∧
      b = logDeriv f 0 ∧
        ∀ (s : ℂ),
          (Multipliable fun ρ =>
              Complex.weierstrassFactor 1 (ρ⁻¹ * s) ^
                ((MeromorphicOn.divisor f Set.univ) ρ).toNat) ∧
            f s =
              Complex.exp (a + b * s) *
                ∏' (ρ : ℂ),
                  Complex.weierstrassFactor 1 (ρ⁻¹ * s) ^
                    ((MeromorphicOn.divisor f Set.univ) ρ).toNat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jensen's bound at a zero of the centre](jensens-bound-at-a-zero-of-the-centre.md)
- [Landau's local logarithmic-derivative lemma](landaus-local-logarithmic-derivative-lemma.md)
- [Liouville's theorem on a complex torus](../part-03/liouvilles-theorem-on-a-complex-torus.md)
- [TauCeti.divisor_divisorProductOne](../../../part-02/zeros-of-l-functions-growth-zero-free-regions-co/tauceti-divisor-divisorproductone.md)
- [TauCeti.logDeriv_divisorProductOne](../../../part-02/zeros-of-l-functions-growth-zero-free-regions-co/tauceti-logderiv-divisorproductone.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hadamard_of_orderLE_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hadamard/OrderOne.html#TauCeti.hadamard_of_orderLE_one).

## Sources

- [Tau Ceti documentation: `TauCeti.hadamard_of_orderLE_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hadamard/OrderOne.html#TauCeti.hadamard_of_orderLE_one)
- [Source of `TauCeti.hadamard_of_orderLE_one` in TauCeti/Analysis/Complex/Hadamard/OrderOne.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Hadamard/OrderOne.lean#L337)
