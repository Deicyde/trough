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

- [TauCeti.BlackScholes.mul_gaussianPDFReal_dPlus](tauceti-blackscholes-mul-gaussianpdfreal-dplus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BlackScholes.callPrice_pde`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Greeks.html#TauCeti.BlackScholes.callPrice_pde).

## Sources

- [Tau Ceti documentation: `TauCeti.BlackScholes.callPrice_pde`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/Greeks.html#TauCeti.BlackScholes.callPrice_pde)
- [Source of `TauCeti.BlackScholes.callPrice_pde` in TauCeti/Probability/Finance/BlackScholes/Greeks.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Finance/BlackScholes/Greeks.lean#L296)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FinancialMathematics/STATUS.md)
