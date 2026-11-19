---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.typedSampler, MIPRE.Introspection.typedSampler_dim, MIPRE.Introspection.typedSampler_cl, MIPRE.Introspection.typedSampler_prog_independent, MIPRE.Introspection.detypedSampler, MIPRE.Introspection.detypedSampler_dim, MIPRE.Introspection.detypedSampler_cl, MIPRE.Introspection.typedSampler_haltsWithin, MIPRE.Introspection.typedSampler_timeBoundAt, MIPRE.Introspection.detypedSampler_timeBound
statement: formalized
proof: formalized
---

# The executable five-level introspection sampler

An actual three-level typed Pauli sampler extends to the complete typed introspection family and then to an actual five-level sampler. Its dimension is $4(|T_{\mathrm{Pauli}}|+2\ell+6)+s(n)$. Every marginal, linear and factor query agrees with the specified CL family, and malformed queries halt. The typed extension program is independent of $\ell$. Polynomial runtime transfers with an explicit index-dependent coefficient and an index-independent query degree. Lemma [The canonical sampler at every index](../part-06/lem-intro-canonical-sampler.md) supplies the uniform Pauli sampler and its parameter and size bounds for the actual compiler.

## Depends on

- [Introspection type graph and typed CL family](lem-intro-type-presentation.md)
- [Executable detyping sampler](../part-01/lem-detype-functional-sampler.md)

## Proof

Strip the sum tag and forward Pauli queries. Auxiliary queries produce the zero vectors or first-factor indicators of the supplied vector length. Dimension queries call the Pauli sampler. Apply the executable graph detyping compiler and compose its checked cost bound with the extension's cost bound.

## Lean

Formalized as [`MIPRE.Introspection.typedSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.typedSampler), [`MIPRE.Introspection.typedSampler_dim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.typedSampler_dim), [`MIPRE.Introspection.typedSampler_cl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.typedSampler_cl), [`MIPRE.Introspection.typedSampler_prog_independent`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.typedSampler_prog_independent), [`MIPRE.Introspection.detypedSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.detypedSampler), [`MIPRE.Introspection.detypedSampler_dim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.detypedSampler_dim), [`MIPRE.Introspection.detypedSampler_cl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.detypedSampler_cl), [`MIPRE.Introspection.typedSampler_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.typedSampler_haltsWithin), [`MIPRE.Introspection.typedSampler_timeBoundAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.typedSampler_timeBoundAt), [`MIPRE.Introspection.detypedSampler_timeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.detypedSampler_timeBound).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1134](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1134)
