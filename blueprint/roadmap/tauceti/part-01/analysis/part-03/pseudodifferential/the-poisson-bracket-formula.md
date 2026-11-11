---
declaration: theorem
origin: cited
lean: TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar
statement: formalized
proof: formalized
---

# The Poisson bracket formula

For scalar classical symbols `a` and `b` of compact spatial
support, the commutator `a # b - b # a` is a classical symbol of order `m' + m - 1` whose principal
symbol is `-i {a_{m'}, b_m}`, with the Poisson bracket
`{p, q} = ∑ⱼ (∂_{ξⱼ} p ∂_{xⱼ} q - ∂_{xⱼ} p ∂_{ξⱼ} q)`.

```lean
TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar {n : ℕ} {m m' : ℝ}
  (a : TauCeti.ClassicalSymbol n ℂ ℂ m') (b : TauCeti.ClassicalSymbol n ℂ ℂ m)
  (ha : a.toSymbol.HasCompactSpatialSupport) (hb : b.toSymbol.HasCompactSpatialSupport) :
  ∃ c,
    (TauCeti.ClassicalSymbol.inclusion 1 ⋯) c = a.sharpCommutator b ha hb ∧
      ∀ (z : TauCeti.CoordinateSpace n × TauCeti.CoordinateSpace n),
        c.principal.coefficient z =
          -Complex.I •
            ∑ j,
              ((a.principal.frequencyDeriv (EuclideanSpace.single j 1)).coefficient z ∘SL
                  (b.principal.spatialDeriv (EuclideanSpace.single j 1)).coefficient z -
                (a.principal.spatialDeriv (EuclideanSpace.single j 1)).coefficient z ∘SL
                  (b.principal.frequencyDeriv (EuclideanSpace.single j 1)).coefficient z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Classical.html#TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Classical.html#TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar)
- [Source of `TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar` in TauCeti/Analysis/Pseudodifferential/Composition/Classical.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/Composition/Classical.lean#L310)
