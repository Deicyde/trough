---
declaration: theorem
origin: cited
lean: TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero
statement: formalized
proof: formalized
---

# The residue theorem (Stichtenoth, Corollary 4.3.3)

over an algebraically closed field,
the residues of a Kähler differential `ω` at the places of `F` sum to zero,
`∑_P res_P (ω) = 0`. Every place is rational here, and only finitely many residues are nonzero
(`TauCeti.finite_support_kaehlerResidueOfPerfectField`).

Over a field that is not algebraically closed the rational places do not suffice: over `ℚ`, the
differential `2x / (x² - 2) dx` of `ℚ(x)` has residue zero at every rational place `x = a` and
residue `-2` at infinity; the missing residue sits at the place of `x² - 2`, which is not rational
(see `TauCeti.finsum_residue_adicOfIrreducible_X_sub_C`). Over a perfect field the trace residues
at the places of every degree sum to zero
(`TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero`).

```lean
TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] [IsAlgClosed k] (hF : TauCeti.IsFunctionField k F)
  (ω : Ω[F⁄k]) : ∑ᶠ (P : TauCeti.Place k F), (P.kaehlerResidueOfPerfectField ⋯ hF) ω = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The abstract residue theorem (Stichtenoth, (1.45))](the-abstract-residue-theorem-stichtenoth-1-45.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The residue theorem for trace residues (Stichtenoth, Corollary 4.3.3 and Remark 4.3.7(d))](the-residue-theorem-for-trace-residues-stichteno.md)
- [Riemann's theorem](../part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../../algebraic-geometry/algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [Stichtenoth's transformation formula](../part-02/stichtenoths-transformation-formula.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/Independence.html#TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/Independence.html#TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero)
- [Source of `TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero` in TauCeti/FieldTheory/FunctionField/Differential/Independence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Differential/Independence.lean#L438)
