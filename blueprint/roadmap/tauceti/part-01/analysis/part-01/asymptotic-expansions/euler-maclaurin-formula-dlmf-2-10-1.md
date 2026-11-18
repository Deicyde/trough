---
declaration: theorem
origin: cited
lean: TauCeti.sum_Icc_eq_eulerMaclaurin
statement: formalized
proof: formalized
---

# Euler–Maclaurin formula (DLMF 2.10.1)

For integers `a ≤ n`, `m ≥ 1` and `f` of class
`C^{2m}` on `[a, n]`, with derivatives `f^{(i)}` taken within `[a, n]`,
`∑_{j=a}^n f(j) = ∫_a^n f + f(a)/2 + f(n)/2
  + ∑_{s=1}^{m-1} B_{2s}/(2s)! (f^{(2s-1)}(n) - f^{(2s-1)}(a))
  + ∫_a^n (B_{2m} - B_{2m}({x}))/(2m)! f^{(2m)}(x) dx`,
where `B_{2m}({x})`, with `{x} = x - ⌊x⌋` the fractional part, is the periodic Bernoulli
function.

```lean
TauCeti.sum_Icc_eq_eulerMaclaurin.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] {f : ℝ → E} {a n : ℤ} (han : a ≤ n) {m : ℕ} (hm : 1 ≤ m)
  (hf : ContDiffOn ℝ (↑(2 * m)) f (Set.Icc ↑a ↑n)) :
  ∑ j ∈ Finset.Icc a n, f ↑j =
    (∫ (x : ℝ) in ↑a..↑n, f x) + 2⁻¹ • f ↑a + 2⁻¹ • f ↑n +
        ∑ s ∈ Finset.Ico 1 m,
          (↑(bernoulli (2 * s)) / ↑(2 * s).factorial) •
            (iteratedDerivWithin (2 * s - 1) f (Set.Icc ↑a ↑n) ↑n -
              iteratedDerivWithin (2 * s - 1) f (Set.Icc ↑a ↑n) ↑a) +
      ∫ (x : ℝ) in ↑a..↑n,
        ((↑(bernoulli (2 * m)) - bernoulliFun (2 * m) (Int.fract x)) / ↑(2 * m).factorial) •
          iteratedDerivWithin (2 * m) f (Set.Icc ↑a ↑n) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler–Maclaurin formula of order `k ≥ 1`](euler-maclaurin-formula-of-order-k-1.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_Icc_eq_eulerMaclaurin`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.html#TauCeti.sum_Icc_eq_eulerMaclaurin).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_Icc_eq_eulerMaclaurin`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.html#TauCeti.sum_Icc_eq_eulerMaclaurin)
- [Source of `TauCeti.sum_Icc_eq_eulerMaclaurin` in TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Asymptotics/Sum/EulerMaclaurin.lean#L212)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
