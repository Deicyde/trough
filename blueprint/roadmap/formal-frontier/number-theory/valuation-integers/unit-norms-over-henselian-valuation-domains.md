---
declaration: theorem
origin: cited
lean: ValuationRing.exists_isUnit_norm_eq_of_sub_one_mem, ValuationRing.exists_isUnit_norm_eq
statement: formalized
proof: formalized
---

# Unit norms over Henselian valuation domains

Let R be a Henselian valuation domain with fraction field F and S a local commutative R-algebra embedded in a finite extension L/F, with compatible given ambient and residue algebras. If field degree equals residue degree and the residue extension is separable, every u with u - 1 in an ideal I contained in the maximal ideal of R is the norm of a unit s of S with s - 1 in the extension of I to S. If the base residue field is finite, every unit of R is the norm of a unit of S, with residue separability derived from finiteness. Neither statement requires a Galois or invertible-degree hypothesis.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/formalization.yaml) of [FormalFrontier/valuation-integers](https://github.com/FormalFrontier/valuation-integers) at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `ValuationRing.exists_isUnit_norm_eq_of_sub_one_mem` (theorem), declared in [ValuationIntegers/Valuation/NormUnits.lean, line 93](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/NormUnits.lean#L93).
- `ValuationRing.exists_isUnit_norm_eq` (theorem), declared in [ValuationIntegers/Valuation/UnitNorm.lean, line 83](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/UnitNorm.lean#L83).

Read from the source at commit [212f1a04](https://github.com/FormalFrontier/valuation-integers/tree/212f1a045abb1dfb6e6da1796d16433db6d72d74), without running Lean.

## Sources

- [valuation-integers at 212f1a04: formalization.yaml](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/formalization.yaml)
- [Source of `ValuationRing.exists_isUnit_norm_eq_of_sub_one_mem` in ValuationIntegers/Valuation/NormUnits.lean](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/NormUnits.lean#L93)
- [Source of `ValuationRing.exists_isUnit_norm_eq` in ValuationIntegers/Valuation/UnitNorm.lean](https://github.com/FormalFrontier/valuation-integers/blob/212f1a045abb1dfb6e6da1796d16433db6d72d74/ValuationIntegers/Valuation/UnitNorm.lean#L83)
