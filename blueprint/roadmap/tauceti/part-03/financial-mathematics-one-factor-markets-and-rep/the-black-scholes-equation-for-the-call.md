---
declaration: theorem
origin: cited
lean: TauCeti.BlackScholes.callPrice_pde
statement: formalized
proof: formalized
---

# The Black–Scholes equation for the call

In calendar time `t < T`, the call price
`C(s, t) = callPrice s r σ K (T - t)` satisfies
`∂C/∂t + σ² s² / 2 ∂²C/∂s² + r (s ∂C/∂s - C) = 0` at every spot `s > 0`.

```lean
TauCeti.BlackScholes.callPrice_pde {s r σ K : ℝ} (hs : 0 < s) (hK : 0 < K) (hσ : σ ≠ 0) {T t : ℝ}
  (ht : t < T) :
  deriv (fun u => TauCeti.BlackScholes.callPrice s r σ K (T - u)) t +
        σ ^ 2 * s ^ 2 / 2 *
          deriv (deriv fun x => TauCeti.BlackScholes.callPrice x r σ K (T - t)) s +
      r *
        (s * deriv (fun x => TauCeti.BlackScholes.callPrice x r σ K (T - t)) s -
          TauCeti.BlackScholes.callPrice s r σ K (T - t)) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.BlackScholes.mul\_gaussianPDFReal\_dPlus](tauceti-blackscholes-mul-gaussianpdfreal-dplus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.callPrice_pde`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Greeks.html#TauCeti.BlackScholes.callPrice_pde).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.callPrice_pde`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Greeks.html#TauCeti.BlackScholes.callPrice_pde)
- [Source of `TauCeti.BlackScholes.callPrice_pde` in TauCeti/Probability/Finance/BlackScholes/Greeks.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Finance/BlackScholes/Greeks.lean#L296)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FinancialMathematics/STATUS.md)
