---
declaration: theorem
origin: cited
lean: TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one
statement: formalized
proof: formalized
---

# Cauchy's bound on the symmetric power

the points of an unordered tuple are bounded by one
more than the sup-norm of its elementary symmetric chart, because each of them is a root of the
monic polynomial those coordinates present.

```lean
TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one.{u_1} {K : Type u_1} [NormedField K]
  [IsAlgClosed K] {n : ℕ} (f : Fin n → K) :
  ‖f‖ ≤ ‖(TauCeti.Sym.coeffEquiv K n) (TauCeti.Sym.ofFn f)‖ + 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/SymmetricPower.html#TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Polynomial/SymmetricPower.html#TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one)
- [Source of `TauCeti.Sym.norm_le_norm_coeffEquiv_ofFn_add_one` in TauCeti/Analysis/Polynomial/SymmetricPower.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Polynomial/SymmetricPower.lean#L198)
