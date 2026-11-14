---
declaration: definition
origin: cited
lean: MIPRE.CL.Sampler, MIPRE.CL.Sampler.Query, MIPRE.CL.Sampler.dist, MIPRE.CL.Sampler.TimeBound
statement: formalized
---

# Sampler

An *$\ell$-level sampler* (with field size $2$) is a Turing machine $\mathcal{S}$ together with, for each $n$, a dimension $s(n)$ and two $\ell$-level CL functions $L^\textsc{A}, L^\textsc{B}$ on $V = \mathbb{F}_2^{s(n)}$ given with exact decomposition data (Lemma [Structure of a CL function](../../structure-of-the-proof/part-01/lem-cl-structure.md)) such that, writing vectors and register subspaces of $V$ as bit strings of length $s(n)$ (coordinates, respectively indicator vectors), for all $w \in \{\textsc{A}, \textsc{B}\}$, $j \in \{1, \ldots, \ell\}$ and bit strings $z, u, y$ of length $s(n)$:

- on input $(n, \mathtt{dimension})$, $\mathcal{S}$ outputs $s(n)$;
- on input $(n, w, \mathtt{marginal}, j, z)$, it outputs the marginal $L^w_{\leq j}(z)$;
- on input $(n, w, \mathtt{linear}, j, u, y)$, it outputs $L^w_{j,u}(y)$, provided $u \in L^w_{\lt j}(V)$;
- on input $(n, w, \mathtt{factor}, j, u)$, it outputs the factor space $V^w_{j,u}$, provided $u \in L^w_{\lt j}(V)$;

and $\mathcal{S}$ halts on every input of the form $(n, \ldots)$, well formed or not; nothing is required of its outputs on other inputs. The *distribution of $\mathcal{S}$ at index $n$* is the CL distribution $\mu_n$ of $(L^\textsc{A}(x), L^\textsc{B}(x))$ for uniform $x \in V$ (Definition [Conditionally linear function](../../structure-of-the-proof/part-01/def-cl-function.md)). In the paper's Turing-machine model, $\mathsf{TIME}_\mathcal{S}(n)$ denotes the absolute supremum of the running times over all inputs of the form $(n, \ldots)$; totality alone does not make that supremum finite.

## Depends on

- [Conditionally linear function](../../structure-of-the-proof/part-01/def-cl-function.md)
- [Structure of a CL function](../../structure-of-the-proof/part-01/lem-cl-structure.md)

## Lean

Formalized as [`MIPRE.CL.Sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Sampler), [`MIPRE.CL.Sampler.Query`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Sampler.Query), [`MIPRE.CL.Sampler.dist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Sampler.dist), [`MIPRE.CL.Sampler.TimeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Sampler.TimeBound).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1394](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1394)
