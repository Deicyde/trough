---
declaration: theorem
origin: cited
lean: TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt
statement: formalized
proof: formalized
---

# Euler–Maclaurin formula of order `k ≥ 1`

Let `g 0 = f` and suppose that, on `[a, n]`
for integers `a ≤ n`, each `g i` with `i < k` is continuous and has derivative `g (i + 1)` at
every interior point, and that `g k` is interval integrable. Then
`∑_{j=a}^n f(j) = ∫_a^n f + (f(a) + f(n))/2 + ∑_{s=2}^k Bₛ/s! (g_{s-1}(n) - g_{s-1}(a))
  - (-1)^k/k! ∫_a^n Bₖ({x}) g_k(x) dx`,
where `Bₖ({x})`, with `{x} = x - ⌊x⌋` the fractional part, is the periodic Bernoulli
function.

```lean
TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [CompleteSpace E] {g : ℕ → ℝ → E} {a n : ℤ} (han : a ≤ n) {k : ℕ} (hk : 1 ≤ k)
  (hcont : ∀ i < k, ContinuousOn (g i) (Set.Icc ↑a ↑n))
  (hderiv : ∀ i < k, ∀ x ∈ Set.Ioo ↑a ↑n, HasDerivAt (g i) (g (i + 1) x) x)
  (hint : IntervalIntegrable (g k) MeasureTheory.volume ↑a ↑n) :
  ∑ j ∈ Finset.Icc a n, g 0 ↑j =
    (∫ (x : ℝ) in ↑a..↑n, g 0 x) + 2⁻¹ • (g 0 ↑a + g 0 ↑n) +
        ∑ s ∈ Finset.Icc 2 k, (↑(bernoulli s) / ↑s.factorial) • (g (s - 1) ↑n - g (s - 1) ↑a) -
      ((-1) ^ k / ↑k.factorial) • ∫ (x : ℝ) in ↑a..↑n, bernoulliFun k (Int.fract x) • g k x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.html#TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.html#TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt)
- [Source of `TauCeti.sum_Icc_eq_eulerMaclaurin_of_hasDerivAt` in TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.lean#L154)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
