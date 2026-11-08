---
declaration: theorem
origin: cited
lean: TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero
statement: formalized
proof: formalized
---

# The residue theorem over a perfect field (Stichtenoth, Corollary 4.3.3 and Remark 4.3.7(d))

over a perfect exact constant field, choose a prime element `t_P` at each place
`P`. Then the trace residues of a Kähler differential `ω` sum to zero,
`∑_P Tr_{F_P/k} res_{P,t_P} (ω / dt_P) = 0`, a sum with finitely many nonzero terms
(`TauCeti.finite_support_traceResidue_kaehlerBasisOfSeparating_coord`). This is the residue
theorem for Weil differentials `TauCeti.finsum_traceResidue_coord_eq_zero` at `u = 1`, applied to
the Weil differential attached to `ω`. Unlike `TauCeti.finsum_kaehlerResidueOfPerfectField_eq_zero`,
places of every degree contribute, so this applies over finite fields.

```lean
TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero.{u_1, u_2} {k : Type u_1}
  {F : Type u_2} [Field k] [Field F] [Algebra k F] [PerfectField k]
  (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  [∀ (P : TauCeti.Place k F), Algebra.IsSeparable k P.ResidueField] (t : TauCeti.Place k F → F)
  (ht : ∀ (P : TauCeti.Place k F), P.ord (t P) = 1)
  [∀ (P : TauCeti.Place k F), Algebra.IsSeparable (↥k⟮t P⟯) F] (ω : Ω[F⁄k]) :
  have htr := ⋯;
  ∑ᶠ (P : TauCeti.Place k F),
      (P.traceResidue ⋯) (((TauCeti.kaehlerBasisOfSeparating ⋯).coord ()) ω) =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The abstract residue theorem (Stichtenoth, (1.45))](the-abstract-residue-theorem-stichtenoth-1-45.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem](riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [Stichtenoth's transformation formula](../function-field/part-01/stichtenoths-transformation-formula.md)
- [The weak approximation theorem](../function-field/part-01/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/Independence.html#TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/Independence.html#TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero)
- [Source of `TauCeti.finsum_traceResidue_kaehlerBasisOfSeparating_coord_eq_zero` in TauCeti/FieldTheory/FunctionField/Differential/Independence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/Independence.lean#L378)
