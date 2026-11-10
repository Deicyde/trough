---
declaration: def
origin: cited
lean: Module.adicIntegralSpan, Module.adicIntegralSpanEquiv, Module.mem_adicIntegralSpan_self_iff, LinearEquiv.adicSeminorm, Module.adicSeminorm, Module.adicSeminorm_apply, Module.adicSeminorm_unique, Module.adicSeminorm_add_le_max, Module.adicSeminorm_self
statement: formalized
---

# Adic fibre seminorms and integral spans

Let R be an infinite Dedekind domain with finite quotients, K its fraction field, p a height-one prime and F = p.adicCompletion K with its selected residue-cardinality norm. An invertible R-module M has a canonical definite ultrametric F-seminorm on F tensor_R M. For every rational frame e and every fibre vector x, its value is q raised to FractionalIdeal.count K p e.coefficientIdeal times the norm of e.fibreCoordinate F x, where q is the residue cardinality. The signed count appears with a plus sign, in contrast to the finite-place height factor. The seminorm is frame-independent and uniquely determined by this weight at the image of e.symm 1. On M = R the whole seminorm is the completion norm composed with the tensor right-unit equivalence; the same vector 1 tensor 1 has value one in every scalar frame. The supplied-frame constructor only needs a finitely generated module and a rational frame, not integral invertibility, freeness or torsion-freeness. No number-field structure, finite-free presentation over the integers, norm on K or norm or metric instance on a fibre is required. Over any Dedekind domain and fraction field, the valuation-integer span of integral sections is the image of the integer tensor fibre and spans the whole field fibre. It is finite for a finite module; flatness makes the image map an equivalence, and the scalar model identifies the whole span with the valuation-integer ring. These algebraic statements need no norm, infinite-ring or finite-quotient hypothesis.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml) of [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.adicIntegralSpan` (def), declared in [DedekindIdealArithmetic/Module/AdicIntegralSpan.lean, line 49](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean#L49).
- `Module.adicIntegralSpanEquiv` (def), declared in [DedekindIdealArithmetic/Module/AdicIntegralSpan.lean, line 122](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean#L122).
- `Module.mem_adicIntegralSpan_self_iff` (theorem), declared in [DedekindIdealArithmetic/Module/AdicIntegralSpan.lean, line 140](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean#L140).
- `LinearEquiv.adicSeminorm` (def), declared in [DedekindIdealArithmetic/Module/AdicSeminorm.lean, line 73](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L73).
- `Module.adicSeminorm` (def), declared in [DedekindIdealArithmetic/Module/AdicSeminorm.lean, line 205](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L205).
- `Module.adicSeminorm_apply` (theorem), declared in [DedekindIdealArithmetic/Module/AdicSeminorm.lean, line 221](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L221).
- `Module.adicSeminorm_unique` (theorem), declared in [DedekindIdealArithmetic/Module/AdicSeminorm.lean, line 264](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L264).
- `Module.adicSeminorm_add_le_max` (theorem), declared in [DedekindIdealArithmetic/Module/AdicSeminorm.lean, line 282](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L282).
- `Module.adicSeminorm_self` (theorem), declared in [DedekindIdealArithmetic/Module/AdicSeminorm.lean, line 304](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L304).

Read from the source at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), without running Lean.

## Sources

- [dedekind-ideal-arithmetic at c7630759: formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml)
- [Source of `Module.adicIntegralSpan` in DedekindIdealArithmetic/Module/AdicIntegralSpan.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean#L49)
- [Source of `Module.adicIntegralSpanEquiv` in DedekindIdealArithmetic/Module/AdicIntegralSpan.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean#L122)
- [Source of `Module.mem_adicIntegralSpan_self_iff` in DedekindIdealArithmetic/Module/AdicIntegralSpan.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicIntegralSpan.lean#L140)
- [Source of `LinearEquiv.adicSeminorm` in DedekindIdealArithmetic/Module/AdicSeminorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L73)
- [Source of `Module.adicSeminorm` in DedekindIdealArithmetic/Module/AdicSeminorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L205)
- [Source of `Module.adicSeminorm_apply` in DedekindIdealArithmetic/Module/AdicSeminorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L221)
- [Source of `Module.adicSeminorm_unique` in DedekindIdealArithmetic/Module/AdicSeminorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L264)
- [Source of `Module.adicSeminorm_add_le_max` in DedekindIdealArithmetic/Module/AdicSeminorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L282)
- [Source of `Module.adicSeminorm_self` in DedekindIdealArithmetic/Module/AdicSeminorm.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/Module/AdicSeminorm.lean#L304)
