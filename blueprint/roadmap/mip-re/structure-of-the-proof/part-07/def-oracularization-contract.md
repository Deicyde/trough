---
declaration: definition
origin: cited
lean: MIPRE.Oracularization, MIPRE.Oracularization.inputSize
statement: formalized
---

# Oracularization specification

The structure `MIPRE.Oracularization`, parametrized by $\ell$, specifies the typed oracularized verifier of an $(\ell + 1)$-level normal form verifier. Its sampler is the typed sampler of Lemma [The typed oracularized sampler](../part-06/lem-oracle-typed-sampler.md), so the oracle form of the sampler is definitional. Its fields specify the decider: a typed decider over ${\mathcal{T}}^\textsc{Orac}$ of the programs of the input sampler and decider and of an index routine supplying a parse cut $B(n)$ and a simulation budget $K(n)$. The decider halts on every input, and its program is a polynomial-time function of the three programs. It accepts only answers that the bit-string predicate of Definition [The typed oracularized game](../part-06/def-oracular-typed-game.md) accepts at the cut $B(n)$: this is the oracle form of the decider. It accepts every such answer within an answer cut $T$ once $K(n) \geq c(W + 1)^m(Z + 1)^{e(k + 1)}$, where $W$ bounds the running-time coefficients of the input verifier at $n$, $k$ is their degree, and $Z$ is the sum of the description lengths of the input programs, the sizes of $B(n)$ and $n$, the dimension $s(n)$ and $T$. It runs within $c'(W' + 1)^{m'}(\left\vert {d} \right\vert + 1)^{e'}$ on inputs $(n, d)$, where $W'$ bounds $K(n)$, $B(n)$, the index routine's running time at $n$, the description lengths of the three programs and $n$.

## Depends on

- [The typed oracularized game](../part-06/def-oracular-typed-game.md)
- [Typed decider and normal verifier](../part-01/def-typed-normal-interface.md)

## Lean

Formalized as [`MIPRE.Oracularization`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization), [`MIPRE.Oracularization.inputSize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.inputSize).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4532](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4532)
