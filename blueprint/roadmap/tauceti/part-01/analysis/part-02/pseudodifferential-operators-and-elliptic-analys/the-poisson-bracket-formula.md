---
declaration: theorem
origin: cited
lean: TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar, TauCeti.Symbol.exists_coefficient_eq_sharp_sub_sharp_add_poissonBracket
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

- [TauCeti.ClassicalSymbol](tauceti-classicalsymbol.md)

## Proof depends on

- [Peetre's inequality (`TauCeti.one_add_norm_add_sq_rpow_le_mul`)](../../part-04/special-functions/peetres-inequality-tauceti-one-add-norm-add-sq-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Classical.html#TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar).

## Other forms

**The Poisson bracket formula for commutators.** Formalized in Tau Ceti as [`TauCeti.Symbol.exists_coefficient_eq_sharp_sub_sharp_add_poissonBracket`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Expansion.html#TauCeti.Symbol.exists_coefficient_eq_sharp_sub_sharp_add_poissonBracket).

```lean
TauCeti.Symbol.exists_coefficient_eq_sharp_sub_sharp_add_poissonBracket.{u_1} {n : ℕ} {m m' : ℝ}
  {V : Type u_1} [NormedAddCommGroup V] [NormedSpace ℂ V] [CompleteSpace V]
  {a : TauCeti.Symbol n V V m'} {b : TauCeti.Symbol n V V m} (ha : a.HasCompactSpatialSupport)
  (hb : b.HasCompactSpatialSupport)
  (hab :
    ∀ (p q : TauCeti.CoordinateSpace n × TauCeti.CoordinateSpace n),
      Commute (a.coefficient p) (b.coefficient q)) :
  ∃ r,
    r.coefficient =
      (a.sharp b hb).coefficient - (b.sharp a ha).coefficient +
        Complex.I • (a.poissonBracket b).coefficient
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/Composition/Classical.html#TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar)
- [Source of `TauCeti.ClassicalSymbol.exists_inclusion_eq_sharpCommutator_of_scalar` in TauCeti/Analysis/Pseudodifferential/Composition/Classical.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Pseudodifferential/Composition/Classical.lean#L359)
