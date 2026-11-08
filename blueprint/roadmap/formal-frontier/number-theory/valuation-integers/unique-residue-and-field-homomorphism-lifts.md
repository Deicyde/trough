---
declaration: theorem
origin: cited
lean: ValuationRing.existsUnique_residueAlgHom_lift_of_finrank_eq, ValuationRing.existsUnique_fieldAlgHom_lift_of_finrank_eq, ValuationRing.fieldAlgHom_eq_id_of_residue_eq_id, ValuationRing.fieldAlgHom_eq_comp_of_residue_eq_comp
statement: formalized
proof: formalized
---

# Unique residue and field homomorphism lifts

Over a Henselian valuation domain R with fraction field F, if local commutative R-algebras S and T embed in finite field extensions L/F and E/F with compatible given ambient and residue scalar towers, [L : F] = [κS : κR], [E : F] = [κT : κR] and κS/κR separable, then every κR-algebra homomorphism φ from κS to κT lifts uniquely to an R-algebra homomorphism ψ from S to T satisfying residue T (ψ s) = φ (residue S s) for every s in S and admits a unique F-algebra homomorphism ι from L to E with algebraMap T E (ψ s) = ι (algebraMap S L s) for every s in S.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/formalization.yaml) of [FormalFrontier/valuation-integers](https://github.com/FormalFrontier/valuation-integers) at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `ValuationRing.existsUnique_residueAlgHom_lift_of_finrank_eq` (theorem), declared in [ValuationIntegers/Valuation/ResidueHomFinite.lean, line 74](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFinite.lean#L74).
- `ValuationRing.existsUnique_fieldAlgHom_lift_of_finrank_eq` (theorem), declared in [ValuationIntegers/Valuation/ResidueHomFinite.lean, line 133](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFinite.lean#L133).
- `ValuationRing.fieldAlgHom_eq_id_of_residue_eq_id` (theorem), declared in [ValuationIntegers/Valuation/ResidueHomFunctorial.lean, line 68](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFunctorial.lean#L68).
- `ValuationRing.fieldAlgHom_eq_comp_of_residue_eq_comp` (theorem), declared in [ValuationIntegers/Valuation/ResidueHomFunctorial.lean, line 125](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFunctorial.lean#L125).

Read from the source at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74), without running Lean.

## Sources

- [valuation-integers at 212f1a04: formalization.yaml](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/formalization.yaml)
- [Source of `ValuationRing.existsUnique_residueAlgHom_lift_of_finrank_eq` in ValuationIntegers/Valuation/ResidueHomFinite.lean](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFinite.lean#L74)
- [Source of `ValuationRing.existsUnique_fieldAlgHom_lift_of_finrank_eq` in ValuationIntegers/Valuation/ResidueHomFinite.lean](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFinite.lean#L133)
- [Source of `ValuationRing.fieldAlgHom_eq_id_of_residue_eq_id` in ValuationIntegers/Valuation/ResidueHomFunctorial.lean](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFunctorial.lean#L68)
- [Source of `ValuationRing.fieldAlgHom_eq_comp_of_residue_eq_comp` in ValuationIntegers/Valuation/ResidueHomFunctorial.lean](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/ResidueHomFunctorial.lean#L125)
