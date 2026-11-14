---
declaration: definition
origin: cited
lean: MIPRE.CL.TypedSampler, MIPRE.CL.TypedSampler.TimeBoundAt
statement: formalized
---

# Typed sampler and its distribution

Let $G=(T,E)$ be a finite undirected type graph with $m_G\geq1$ edges and $k_G$ loops. Sample an ordered adjacent type pair uniformly from its $2m_G-k_G$ possibilities, and independently a common uniform $z\in\mathbb{F}_{q(n)}^{s(n)}$. Output $((t,L_t^\textsc{A}(z)),(u,L_u^\textsc{B}(z)))$. A typed sampler exposes dimension, marginal, level-linear and factor-support queries for each type. It computes the prescribed bounds before parsing auxiliary inputs, inspects at most the bound plus one symbol per component, and halts with a fixed default on malformed input. Computing the bounds is charged in its runtime. Linear and factor-query correctness is required only on valid prefix images; image membership is not a parsing obligation. No field-size query is implicit in this interface. In the ambient model a typed sampler is binary, and bounded-prefix parsing is replaced by halting on every input together with a polynomial budget (`TypedSampler.TimeBoundAt`); linear and factor correctness are required on valid prefixes, as here.

## Depends on

- [Sampler](../../foundations/part-03/def-sampler.md)

## Lean

Formalized as [`MIPRE.CL.TypedSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.TypedSampler), [`MIPRE.CL.TypedSampler.TimeBoundAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.TypedSampler.TimeBoundAt).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 337](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L337)
