---
declaration: theorem
origin: cited
lean: TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed
statement: formalized
proof: formalized
---

# The residue theorem for `k(x)` over an algebraically closed field (Stichtenoth, Corollary 4.3.3, for `k(x)`)

`∑_{a ∈ k} res_{P_a, x - a} (z) = res_{P_∞, x⁻¹} (x² z)` for every
rational function `z`.

```lean
TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed.{u_1} {k : Type u_1} [Field k]
  [IsAlgClosed k] (z : RatFunc k) :
  ∑ᶠ (a : k), ((TauCeti.Place.adicOfIrreducible ⋯).residue ⋯ ⋯) z =
    ((TauCeti.Place.infty k).residue ⋯ ⋯) (RatFunc.X ^ 2 * z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The residue theorem for `k(x)` (Stichtenoth, Corollary 4.3.3, for `k(x)`)](the-residue-theorem-for-k-x-stichtenoth-corollar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.html#TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed).

## Sources

- [Tau Ceti documentation: `TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.html#TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed)
- [Source of `TauCeti.finsum_residue_adicOfIrreducible_X_sub_C_of_isAlgClosed` in TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/RatFunc/Residue.lean#L240)
