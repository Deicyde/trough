---
declaration: theorem
origin: cited
lean: TauCeti.finsum_residue_adicOfIrreducible_X_sub_C
statement: formalized
proof: formalized
---

# The residue theorem for `k(x)` (Stichtenoth, Corollary 4.3.3, for `k(x)`)

if every pole
of `z` is a rational place, then the residues of `z dx` over `ℙ¹(k)` sum to zero, in the form
`∑_{a ∈ k} res_{P_a, x - a} (z) = res_{P_∞, x⁻¹} (x² z)`.

The hypothesis is needed: over `ℚ`, `z = 2x / (x² - 2)` is integral at every place `P_a`, so the
left side vanishes, while `res_{P_∞, x⁻¹} (x² z) = 2`; the missing residue sits at the place of
`x² - 2`, which has degree two.

```lean
TauCeti.finsum_residue_adicOfIrreducible_X_sub_C.{u_1} {k : Type u_1} [Field k] {z : RatFunc k}
  (hz : ∀ (P : TauCeti.Place k (RatFunc k)), P.degree ≠ 1 → z ∈ P.integers) :
  ∑ᶠ (a : k), ((TauCeti.Place.adicOfIrreducible ⋯).residue ⋯ ⋯) z =
    ((TauCeti.Place.infty k).residue ⋯ ⋯) (RatFunc.X ^ 2 * z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The abstract residue theorem (Stichtenoth, (1.45))](../../algebraic-curves-function-fields-divisors-and-ri/the-abstract-residue-theorem-stichtenoth-1-45.md)
- [Riemann's theorem](../../algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finsum_residue_adicOfIrreducible_X_sub_C`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.html#TauCeti.finsum_residue_adicOfIrreducible_X_sub_C).

## Sources

- [Tau Ceti documentation: `TauCeti.finsum_residue_adicOfIrreducible_X_sub_C`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.html#TauCeti.finsum_residue_adicOfIrreducible_X_sub_C)
- [Source of `TauCeti.finsum_residue_adicOfIrreducible_X_sub_C` in TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.lean#L200)
