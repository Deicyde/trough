---
navigation: transparent
---

# The three stage contracts to Detyping tailored games

- [The three stage contracts](def-tailored-stages.md)
- [Question reduction for tailored verifiers; II:5712](thm-tailored-qr.md)
- [Answer reduction for tailored verifiers; II:6883](thm-tailored-ar.md)
- [The $k$-fold tailored product; II:11377, direct form](def-tailored-product.md)
- [The canonical decider of the product](lem-tailored-product-accepts.md)
- [Tensor powers of permutation strategies; II:3043](lem-tensor-power-zpc.md)
- [Repeated tailored verifiers and the specification of their programs](def-tailored-rep-spec.md)
- [Completeness and soundness of repeated tailored verifiers](thm-tailored-rep-from-spec.md)
- [The repeated programs](def-tailored-rep-programs.md)
- [The repeated programs meet the specification](lem-tailored-rep-programs.md)
- [Running times of the repeated programs](lem-tailored-rep-programs-time.md)
- [Parallel repetition of tailored verifiers; II:11103, direct form](thm-tailored-rep.md)

## Question reduction: the honest strategy as a permutation strategy

Theorem [Question reduction for tailored verifiers; II:5712](thm-tailored-qr.md) is proved on Route A (Remark Route A: the two checks): the tailored question reduction is a tailored presentation of the introspection verifier of Section [Question reduction: introspection](../../structure-of-the-proof/README.md). Its completeness asks that the honest strategy of that verifier, built on a perfect permutation strategy for the input, be a permutation strategy itself. The honest strategy is a projective measurement at each question, whose outcomes are encoded as answer bits; the lemmas of this subsection supply the observables of those bits and show that they are signed permutations, in the three ways the honest strategy builds its measurements: eigenbasis measurements of the Weyl operators, read out linearly; the computational-basis measurement, read out arbitrarily; and controlled sums, applying one signed permutation for each computational-basis state of a control register.

- [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md)
- [Weyl measurements are read out by signed permutations; II:2938](lem-weyl-signed-perm.md)
- [Controlled signed permutations](lem-controlled-signed-perm.md)
- [Binary measurements, the qubit Paulis and the Magic Square grid](lem-binary-signed-perm.md)
- [The input strategy's answer bits](lem-input-answer-bits.md)
- [Presenting a game as a tailored game](lem-presentation-transport.md)
- [Detyping a tailored game](def-tailored-detyping.md)
- [Detyping tailored games](lem-tailored-detyping.md)
