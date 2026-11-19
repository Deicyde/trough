---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Halting.esize_lpProg, MIPRE.Tailored.Halting.lp_cost, MIPRE.Tailored.Halting.exists_lp_cost_poly, MIPRE.Tailored.Halting.sampler_len_clauses, MIPRE.Tailored.Halting.lp_clause, MIPRE.Tailored.Halting.size_clause, MIPRE.Tailored.Halting.exists_lamBound, MIPRE.Tailored.Halting.Lam0, MIPRE.Tailored.Halting.Lam0_spec
statement: formalized
proof: formalized
---

# $\lambda$ for the tailored halting verifier; II:2002

There is a threshold $\Lambda_0$, depending on the compression, the universal machines and the search program alone, such that $\mathsf{V}^{\mathcal{M},\lambda}$ is $\lambda$-bounded (Definition [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)) for every machine $\mathcal{M}$ and every $\lambda \geq \Lambda_0 + 4\left\vert {\mathcal{M}} \right\vert$.

## Depends on

- [The tailored halting verifier; II:1900–1925](def-tailored-halt-verifier.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)
- [The parameter of the halting verifier](../../structure-of-the-proof/part-09/lem-lambda.md)

## Proof

The processor is a hardcoding of the fixed point's program to its own description, of size $2(\left\vert {\mathcal{M}} \right\vert + \left\vert {\lambda} \right\vert)$ plus a constant. On $(n, d)$ it runs within the fixed point's overhead on the hardcoded description, the branch computation, and the universal machine on the compressed processor, whose time is the compression's $\mathrm{poly}(n + \lambda)$; together a polynomial in $n + \left\vert {\mathcal{M}} \right\vert + \lambda$ times a power of $\left\vert {d} \right\vert + 1$. The sampler's and the answer-length calculator's clauses are the compression's bounds. Each clause is absorbed into $n^\lambda$, at degree $\lambda$, past a threshold on $\lambda$, and the size into $\lambda$ once $\lambda \geq \Lambda_0 + 4\left\vert {\mathcal{M}} \right\vert$.

## Lean

Formalized as [`MIPRE.Tailored.Halting.esize_lpProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.esize_lpProg), [`MIPRE.Tailored.Halting.lp_cost`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lp_cost), [`MIPRE.Tailored.Halting.exists_lp_cost_poly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.exists_lp_cost_poly), [`MIPRE.Tailored.Halting.sampler_len_clauses`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.sampler_len_clauses), [`MIPRE.Tailored.Halting.lp_clause`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lp_clause), [`MIPRE.Tailored.Halting.size_clause`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.size_clause), [`MIPRE.Tailored.Halting.exists_lamBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.exists_lamBound), [`MIPRE.Tailored.Halting.Lam0`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.Lam0), [`MIPRE.Tailored.Halting.Lam0_spec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.Lam0_spec).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 631](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L631)
