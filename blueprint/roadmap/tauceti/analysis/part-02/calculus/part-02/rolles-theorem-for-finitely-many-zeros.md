---
declaration: theorem
origin: cited
lean: TauCeti.exists_finset_deriv_eq_zero
statement: formalized
proof: formalized
---

# Rolle's theorem for finitely many zeros

If a function `f : ℝ → ℝ`, continuous between
the smallest and largest points of a nonempty finite set `Z`, vanishes on `Z`, then `deriv f`
vanishes on a finite set `Z'` with one point fewer that separates the points of `Z`: every point of
`Z'` lies strictly between two points of `Z`, and strictly between any two points of `Z` lies a
point of `Z'`.

```lean
TauCeti.exists_finset_deriv_eq_zero {f : ℝ → ℝ} {Z : Finset ℝ} (hZ : Z.Nonempty)
  (hf : ContinuousOn f (Set.Icc (Z.min' hZ) (Z.max' hZ))) (hfZ : ∀ x ∈ Z, f x = 0) :
  ∃ Z',
    Z'.card + 1 = Z.card ∧
      (∀ z ∈ Z', deriv f z = 0) ∧
        (∀ z ∈ Z', ∃ x ∈ Z, ∃ y ∈ Z, x < z ∧ z < y) ∧
          ∀ x ∈ Z, ∀ y ∈ Z, x < y → ∃ z ∈ Z', x < z ∧ z < y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_finset_deriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalExtr/Rolle.html#TauCeti.exists_finset_deriv_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_finset_deriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalExtr/Rolle.html#TauCeti.exists_finset_deriv_eq_zero)
- [Source of `TauCeti.exists_finset_deriv_eq_zero` in TauCeti/Analysis/Calculus/LocalExtr/Rolle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/LocalExtr/Rolle.lean#L46)
