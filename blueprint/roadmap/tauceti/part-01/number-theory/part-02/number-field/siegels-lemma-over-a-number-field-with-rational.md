---
declaration: theorem
origin: cited
lean: NumberField.exists_ne_zero_int_vec_abs_le_of_house_le
statement: formalized
proof: formalized
---

# Siegel's lemma over a number field, with rational integer unknowns (Evertse, Theorem 3.20)

Let `K` be a number field of degree `d` and `a` a matrix over `𝓞 K` with `M` rows
and `N` columns, whose entries have house at most `A ≥ 1`. If `d * M < N`, there is a nonzero
`x ∈ ℤ^N` with `a x = 0` and `|xⱼ| ≤ (3 N A) ^ (d M / (N - d M))` for every `j`.

```lean
NumberField.exists_ne_zero_int_vec_abs_le_of_house_le.{u_1, u_2, u_3} {K : Type u_1} [Field K]
  [NumberField K] {α : Type u_2} {β : Type u_3} [Fintype α] [Fintype β]
  (a : Matrix α β (NumberField.RingOfIntegers K)) {A : ℝ} (hA : 1 ≤ A)
  (hcard : Module.finrank ℚ K * Fintype.card α < Fintype.card β)
  (ha : ∀ (i : α) (j : β), NumberField.house ↑(a i j) ≤ A) :
  ∃ x,
    x ≠ 0 ∧
      (a.mulVec fun j => ↑(x j)) = 0 ∧
        ∀ (j : β),
          |↑(x j)| ≤
            (3 * ↑(Fintype.card β) * A) ^
              (↑(Module.finrank ℚ K) * ↑(Fintype.card α) /
                (↑(Fintype.card β) - ↑(Module.finrank ℚ K) * ↑(Fintype.card α)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.exists_ne_zero_int_vec_abs_le_of_house_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SiegelsLemma.html#NumberField.exists_ne_zero_int_vec_abs_le_of_house_le).

## Sources

- [Tau Ceti documentation: `NumberField.exists_ne_zero_int_vec_abs_le_of_house_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/SiegelsLemma.html#NumberField.exists_ne_zero_int_vec_abs_le_of_house_le)
- [Source of `NumberField.exists_ne_zero_int_vec_abs_le_of_house_le` in TauCeti/NumberTheory/NumberField/SiegelsLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/SiegelsLemma.lean#L149)
