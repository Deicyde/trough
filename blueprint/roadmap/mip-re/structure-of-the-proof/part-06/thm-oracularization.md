---
declaration: theorem
origin: cited
lean: MIPRE.Oracularization.construction, MIPRE.Oracularization.typed_soundness, MIPRE.Oracularization.typed_completeness, MIPRE.Oracularization.detyped, MIPRE.Oracularization.detyped_completeness, MIPRE.Oracularization.detyped_soundness
statement: formalized
proof: formalized
---

# Oracularization

The source theorem supplies a polynomial-time Turing machine ${\mathsf{ComputeOracleVerifier}}$ mapping an $\ell$-level normal form verifier $\mathsf{V} = (\mathcal{S}, \mathcal{D})$, whose decider is in standard timeout-counter form, to a *typed* verifier $\mathsf{V}^{\textsc{Orac}}$ such that, for some $\delta(\varepsilon) = O(\sqrt{\varepsilon})$ and all $n$:

1. (**Completeness**) If $\mathsf{V}_n$ has a value-$1$ PCC strategy then $\mathsf{V}^{\textsc{Orac}}_n$ has a value-$1$ PCC strategy, in which moreover both players measure with the same family of operators.
2. (**Soundness**) If $\mathrm{val}^*(\mathsf{V}^{\textsc{Orac}}_n) > 1 - \varepsilon$ then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - \delta(\varepsilon)$.
3. (**Complexity**) The sampler of $\mathsf{V}^{\textsc{Orac}}$ depends only on $\mathcal{S}$, with $\mathsf{TIME}_{\mathcal{S}^{\mathrm{ora}}}(n) = \mathrm{poly}(\mathsf{TIME}_\mathcal{S}(n))$ and $\ell$ typed levels. The decider has time $\mathrm{poly}(\mathsf{TIME}_\mathcal{S}(n),B_\mathcal{D}(n))$.

The oracularized decider's preamble performs a type check, a question-length check, and a bounded parse of each answer component against the decider's timeout bound $B_\mathcal{D}(n)$; answers failing the parse are grouped into one distinguished outcome, so the oracle families are projective measurements and not sub-measurements.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous strategy](../../foundations/part-01/def-sync-strategy.md)

## Proof depends on

- [Oracularization specification](../part-07/def-oracularization-contract.md)
- [The typed oracularized sampler](lem-oracle-typed-sampler.md)
- [The typed oracularized decider](../part-07/lem-oracle-typed-decider.md)
- [Running times of the typed oracularized decider](../part-07/lem-oracle-decider-time.md)
- [Value transfers of the typed oracularized game](lem-oracular-typed-transfers.md)
- [Detyping PCC completeness](../part-01/lem-detype-completeness.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)

## Proof

The typed oracularized verifier is the pair of Lemma [The typed oracularized sampler](lem-oracle-typed-sampler.md) and Lemma [The typed oracularized decider](../part-07/lem-oracle-typed-decider.md), and it inhabits the specification of Definition [Oracularization specification](../part-07/def-oracularization-contract.md), with the running times of Lemma [Running times of the typed oracularized decider](../part-07/lem-oracle-decider-time.md). Completeness and soundness of its typed game are the transfers of Lemma [Value transfers of the typed oracularized game](lem-oracular-typed-transfers.md), read through the decider's acceptance law, with $\delta(\varepsilon) = 24\sqrt{\varepsilon}$. Through the detyping compiler of Lemma [Effective detyping compiler](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L882), the verifier with $\ell + 3$ levels has the same completeness and soundness with $\delta(\varepsilon) = 1536\sqrt{\varepsilon}$: the factor $16^3$ of the three types, under the square root, times $24$.

## Lean

Formalized as [`MIPRE.Oracularization.construction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.construction), [`MIPRE.Oracularization.typed_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.typed_soundness), [`MIPRE.Oracularization.typed_completeness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.typed_completeness), [`MIPRE.Oracularization.detyped`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.detyped), [`MIPRE.Oracularization.detyped_completeness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.detyped_completeness), [`MIPRE.Oracularization.detyped_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.detyped_soundness).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4120](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4120)
