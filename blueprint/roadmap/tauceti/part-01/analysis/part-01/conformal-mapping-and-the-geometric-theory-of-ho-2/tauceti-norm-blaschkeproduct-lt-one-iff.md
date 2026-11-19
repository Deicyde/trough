---
declaration: theorem
origin: cited
lean: TauCeti.norm_blaschkeProduct_lt_one_iff
statement: formalized
proof: formalized
---

# TauCeti.norm_blaschkeProduct_lt_one_iff

On the open unit disc, a finite Blaschke product with parameters in the closed unit disc has
modulus less than one exactly when some interior parameter has positive multiplicity; otherwise
it has modulus one there.

```lean
TauCeti.norm_blaschkeProduct_lt_one_iff.{u_1} {z : ℂ} {ι : Type u_1} [Fintype ι] {a : ι → ℂ}
  {n : ι → ℕ} (ha : ∀ (i : ι), ‖a i‖ ≤ 1) (hz : ‖z‖ < 1) :
  ‖TauCeti.blaschkeProduct a n z‖ < 1 ↔ ∃ i, ‖a i‖ < 1 ∧ n i ≠ 0
```

## Depends on

- [TauCeti.blaschkeFactor](tauceti-blaschkefactor.md)

## Proof depends on

- [Poincaré defect identity (norm form)](../../part-03/complex/part-03/poincare-defect-identity-norm-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_blaschkeProduct_lt_one_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.html#TauCeti.norm_blaschkeProduct_lt_one_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_blaschkeProduct_lt_one_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.html#TauCeti.norm_blaschkeProduct_lt_one_iff)
- [Source of `TauCeti.norm_blaschkeProduct_lt_one_iff` in TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.lean#L234)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ConformalMappingPartII/STATUS.md)
