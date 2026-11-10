---
declaration: theorem
origin: cited
lean: TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one
statement: formalized
proof: formalized
---

# Kolchin's theorem for `𝔾ₐ`

every nonzero vector of a comodule over the coordinate
algebra of the additive group produces a nonzero fixed vector, over an arbitrary base and with no
finiteness hypothesis. The witness is the top nonvanishing divided-power component `Nᵢ v`: by the
binomial composition rule each further component of it is a component of `v` of strictly larger
index, which vanishes by maximality.

```lean
TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one.{u, v} (R : Type u) [CommSemiring R]
  {V : Type v} [AddCommMonoid V] [_root_.Module R V] [TauCeti.Comodule R (SymmetricAlgebra R R) V]
  {v : V} (hv : v ≠ 0) : ∃ w, w ≠ 0 ∧ TauCeti.Comodule.coact w = w ⊗ₜ[R] 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/AdditiveGroup/Unipotent.html#TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one).

## Sources

- [Tau Ceti documentation: `TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/AdditiveGroup/Unipotent.html#TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one)
- [Source of `TauCeti.AdditiveGroup.exists_ne_zero_coact_eq_tmul_one` in TauCeti/Algebra/AlgebraicGroup/AdditiveGroup/Unipotent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/AdditiveGroup/Unipotent.lean#L299)
