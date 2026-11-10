---
declaration: theorem
origin: cited
lean: TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le
statement: formalized
proof: formalized
---

# Hoffman's error bound for a polyhedral cone

Let `a j` be finitely many functionals on a
finite-dimensional space. There is a constant `C` such that every `w` with `-c ≤ a j w` for all
`j`, where `0 ≤ c`, lies within `C * c` of the cone `{w' | ∀ j, 0 ≤ a j w'}`, as measured by
finitely many prescribed functionals `b k`. The constant `C` is nonnegative.

```lean
TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le.{u_1, u_2, u_3, u_4} {ι : Type u_1}
  {κ : Type u_2} {K : Type u_3} {V : Type u_4} [Field K] [AddCommGroup V] [_root_.Module K V]
  [LinearOrder K] [IsStrictOrderedRing K] [Finite ι] [Finite κ] [FiniteDimensional K V]
  (a : ι → Module.Dual K V) (b : κ → Module.Dual K V) :
  ∃ C,
    0 ≤ C ∧
      ∀ (c : K),
        0 ≤ c →
          ∀ (w : V),
            (∀ (j : ι), -c ≤ (a j) w) →
              ∃ w', (∀ (j : ι), 0 ≤ (a j) w') ∧ ∀ (k : κ), |(b k) (w - w')| ≤ C * c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Tucker's theorem](tuckers-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/ErrorBound.html#TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/Cone/ErrorBound.html#TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le)
- [Source of `TauCeti.exists_forall_abs_apply_sub_le_of_forall_neg_le` in TauCeti/Geometry/Convex/Cone/ErrorBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Convex/Cone/ErrorBound.lean#L100)
