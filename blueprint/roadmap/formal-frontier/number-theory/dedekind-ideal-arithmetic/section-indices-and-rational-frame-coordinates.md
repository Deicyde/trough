---
declaration: theorem
origin: cited
lean: Module.Invertible.finite_quotient_span_singleton, Module.Invertible.exists_nonzero_smul_eq, LinearEquiv.fibreCoordinate, LinearEquiv.coefficientIdeal, LinearEquiv.coefficientMap_injective
statement: formalized
---

# Section indices and rational-frame coordinates

Nonzero sections of invertible modules over commutative domains with finite quotients span finite-index submodules; any two nonzero sections of one invertible module over a commutative domain admit a common nonzero scalar multiple. A supplied frame on K tensor_R M extends to an F-linear coordinate on F tensor_R M through compatible algebras over commutative semirings R and K, with F not required commutative, without finiteness or norm hypotheses. A finitely generated module with a supplied frame over a fraction field has a nonzero coefficient fractional ideal; torsion-freeness makes the coefficient map injective, but is not required to construct the ideal.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml) of [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.Invertible.finite_quotient_span_singleton` (theorem), declared in [DedekindIdealArithmetic/Module/Index.lean, line 101](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/Index.lean#L101).
- `Module.Invertible.exists_nonzero_smul_eq` (theorem), declared in [DedekindIdealArithmetic/Module/Index.lean, line 122](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/Index.lean#L122).
- `LinearEquiv.fibreCoordinate` (def), declared in [DedekindIdealArithmetic/Module/CoefficientIdeal.lean, line 110](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/CoefficientIdeal.lean#L110).
- `LinearEquiv.coefficientIdeal` (def), declared in [DedekindIdealArithmetic/Module/CoefficientIdeal.lean, line 251](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/CoefficientIdeal.lean#L251).
- `LinearEquiv.coefficientMap_injective` (theorem), declared in [DedekindIdealArithmetic/Module/CoefficientIdeal.lean, line 236](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/CoefficientIdeal.lean#L236).

Read from the source at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), without running Lean.

## Sources

- [dedekind-ideal-arithmetic at c7630759: formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml)
- [Source of `Module.Invertible.finite_quotient_span_singleton` in DedekindIdealArithmetic/Module/Index.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/Index.lean#L101)
- [Source of `Module.Invertible.exists_nonzero_smul_eq` in DedekindIdealArithmetic/Module/Index.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/Index.lean#L122)
- [Source of `LinearEquiv.fibreCoordinate` in DedekindIdealArithmetic/Module/CoefficientIdeal.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/CoefficientIdeal.lean#L110)
- [Source of `LinearEquiv.coefficientIdeal` in DedekindIdealArithmetic/Module/CoefficientIdeal.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/CoefficientIdeal.lean#L251)
- [Source of `LinearEquiv.coefficientMap_injective` in DedekindIdealArithmetic/Module/CoefficientIdeal.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/CoefficientIdeal.lean#L236)
