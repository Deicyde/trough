---
declaration: theorem
origin: cited
lean: TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton
statement: formalized
proof: formalized
---

# The Frobenius kernel meets each conjugate of `H` exactly in the identity

A nonidentity
element of `g H g⁻¹` lies in a conjugate of `H`, so it is outside the kernel.

```lean
TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton.{u_1} {G : Type u_1} [Group G] {H : Subgroup G}
  (g : G) : TauCeti.frobeniusKernel H ∩ MulAut.conj g • ↑H = {1}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FrobeniusKernel.html#TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton).

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FrobeniusKernel.html#TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton)
- [Source of `TauCeti.frobeniusKernel_inter_conj_smul_eq_singleton` in TauCeti/GroupTheory/FrobeniusKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/FrobeniusKernel.lean#L207)
