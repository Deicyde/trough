---
declaration: lemma
origin: cited
lean: MIPRE.Halting.lamOf, MIPRE.Halting.isBounded_comprStr, MIPRE.Halting.lamOf_ge, MIPRE.Halting.ansBound_le_lamOf, MIPRE.Halting.exists_compressorSpec, MIPRE.Halting.comprPoly, MIPRE.Cost.PolyBounded.absorb, MIPRE.Cost.PolyBounded.absorb_log, MIPRE.Cost.Prog.wrapCoreCost, MIPRE.Cost.Prog.wrapCore_cost', MIPRE.Halting.exists_lamBound, MIPRE.Halting.Lam0, MIPRE.Halting.Lam0_spec, MIPRE.Halting.esize_dec, MIPRE.Halting.dec_cost, MIPRE.Halting.exists_dec_cost_poly, MIPRE.Halting.decCostPoly, MIPRE.Halting.dec_cost_spec, MIPRE.Halting.Vhalt_decider_cost, MIPRE.Halting.wrapCoreCost_le_WZ, MIPRE.Halting.lamF, MIPRE.Halting.lamz
statement: formalized
proof: formalized
---

# The parameter of the halting verifier

There is a $\lambda$, computable from the description of $\mathcal{M}$ in polynomial time and of size $\mathrm{poly}(\left\vert {\mathcal{M}} \right\vert)$, such that $\mathsf{V}^{\mathsf{halt}}$ is $\lambda$-bounded and $\mathsf{TIME}_{\mathcal{D}^{\mathsf{halt}}}(n), \mathsf{TIME}_{\mathcal{S}^{\mathsf{halt}}}(n) = \mathrm{poly}(n, \left\vert {\mathcal{M}} \right\vert)$.

## Depends on

- [The self-referential decider is well defined](lem-halt-construction.md)
- [A uniform bound on the verifier's parameter](lem-lambda-bound.md)
- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)
- [Effective indexing and padding arithmetic](../part-07/lem-pcp-padding-programs.md)

## Proof depends on

- [Values of the halting verifier](lem-dhalt-values.md)

## Proof

`MIPRE.Halting.isBounded_comprStr`: the sampler clauses from the compression theorem's own bounds at $\lambda(n)$, the size clause from the criterion's slack $2\left\vert {c} \right\vert \leq n$ and `PolyBounded.absorb_log`, the decider clause from the explicit wrapper cost `Prog.wrapCore_cost'` around `innerBound` and `PolyBounded.absorb`; the parameter is computed in binary by `comprPoly`.

## Lean

Formalized as [`MIPRE.Halting.lamOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.lamOf), [`MIPRE.Halting.isBounded_comprStr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.isBounded_comprStr), [`MIPRE.Halting.lamOf_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.lamOf_ge), [`MIPRE.Halting.ansBound_le_lamOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.ansBound_le_lamOf), [`MIPRE.Halting.exists_compressorSpec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_compressorSpec), [`MIPRE.Halting.comprPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.comprPoly), [`MIPRE.Cost.PolyBounded.absorb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.PolyBounded.absorb), [`MIPRE.Cost.PolyBounded.absorb_log`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.PolyBounded.absorb_log), [`MIPRE.Cost.Prog.wrapCoreCost`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.wrapCoreCost), [`MIPRE.Cost.Prog.wrapCore_cost'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.wrapCore_cost'), [`MIPRE.Halting.exists_lamBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_lamBound), [`MIPRE.Halting.Lam0`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.Lam0), [`MIPRE.Halting.Lam0_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.Lam0_spec), [`MIPRE.Halting.esize_dec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.esize_dec), [`MIPRE.Halting.dec_cost`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.dec_cost), [`MIPRE.Halting.exists_dec_cost_poly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.exists_dec_cost_poly), [`MIPRE.Halting.decCostPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.decCostPoly), [`MIPRE.Halting.dec_cost_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.dec_cost_spec), [`MIPRE.Halting.Vhalt_decider_cost`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.Vhalt_decider_cost), [`MIPRE.Halting.wrapCoreCost_le_WZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.wrapCoreCost_le_WZ), [`MIPRE.Halting.lamF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.lamF), [`MIPRE.Halting.lamz`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.lamz).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 7188](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L7188)
