---
declaration: theorem
origin: cited
lean: Fri.foldingAgreementFailure_prob_le_powers, Fri.foldingAgreementFailure_prob_le_generalizedJohnson
statement: formalized
proof: formalized
---

# fri-folding-error

For every fixed word $f$, the probability of a bad uniform challenge is at most the MCA error of the powers generator $(1,\alpha,\ldots,\alpha^{m-1})$ for $C'$ at radius $\theta$.

## Depends on

- [fri-folding-failure](def-fri-folding-failure.md)
- [fri-coefficient-lift](lem-fri-coefficient-lift.md)

## Proof

A bad challenge is an MCA failure for the coefficient words: if every coefficient word agreed on the same $T$, Lemma [fri-coefficient-lift](lem-fri-coefficient-lift.md) would lift the agreement. No union bound over subsets is needed. The generalized-Johnson specialization instantiates the existing powers-MCA bound from ([Bordage et al. 2025](https://eprint.iacr.org/2025/2051)), retaining all its field-size, slack, and radius assumptions.

## Lean

Formalized as [`Fri.foldingAgreementFailure_prob_le_powers`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.foldingAgreementFailure_prob_le_powers), [`Fri.foldingAgreementFailure_prob_le_generalizedJohnson`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.foldingAgreementFailure_prob_le_generalizedJohnson).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 40](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L40)
