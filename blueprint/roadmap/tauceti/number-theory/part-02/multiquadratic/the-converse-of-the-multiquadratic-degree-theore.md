---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top
statement: formalized
proof: formalized
---

# The converse of the multiquadratic degree theorem

Let `2 ≠ 0` in `K` and let `L / K` be a
finite Galois extension whose Galois group has exponent dividing two. Then `L = K(√d₁, …, √dₙ)`
for radicands `d₁, …, dₙ ∈ K` that are square-class independent — no nonempty subset product is a
square — and consequently `[L : K] = 2ⁿ`.

```lean
TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [Field L] [Algebra K L] [FiniteDimensional K L] [IsGalois K L] [NeZero 2]
  (hexp : Monoid.exponent Gal(L/K) ∣ 2) :
  ∃ n d root,
    (∀ (i : Fin n), root i ^ 2 = (algebraMap K L) (d i)) ∧
      (∀ (S : Finset (Fin n)), S.Nonempty → ¬IsSquare (∏ i ∈ S, d i)) ∧
        IntermediateField.adjoin K (Set.range root) = ⊤ ∧ Module.finrank K L = 2 ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Degree of a multiquadratic field over a finite index](../../part-01/multiquadratic-fields-and-genus-theory/degree-of-a-multiquadratic-field-over-a-finite-i.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Galois/Kummer.html#TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Galois/Kummer.html#TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top)
- [Source of `TauCeti.Multiquadratic.exists_root_adjoin_range_eq_top` in TauCeti/NumberTheory/Multiquadratic/Galois/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/Galois/Kummer.lean#L205)
