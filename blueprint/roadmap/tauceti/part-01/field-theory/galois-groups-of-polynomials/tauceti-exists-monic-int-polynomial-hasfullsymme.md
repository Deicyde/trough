---
declaration: theorem
origin: cited
lean: TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup
statement: formalized
proof: formalized
---

# TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup

Every positive degree occurs for a monic integral polynomial irreducible over `ℚ`
with full symmetric Galois group.

```lean
TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup (n : ℕ) (hn : 1 ≤ n) :
  ∃ f,
    f.Monic ∧
      f.natDegree = n ∧
        Irreducible (Polynomial.map (Int.castRingHom ℚ) f) ∧
          (Polynomial.map (Int.castRingHom ℚ) f).HasFullSymmetricGaloisGroup
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The polynomial form of Dedekind's theorem](../../number-theory/part-02/number-fields-ramification-frobenius-and-the-lmf/the-polynomial-form-of-dedekinds-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Symmetric/Realization.html#TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Symmetric/Realization.html#TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup)
- [Source of `TauCeti.exists_monic_int_polynomial_hasFullSymmetricGaloisGroup` in TauCeti/FieldTheory/GaloisGroups/Symmetric/Realization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/GaloisGroups/Symmetric/Realization.lean#L42)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PolynomialGaloisGroups/STATUS.md)
