---
declaration: lemma
origin: cited
lean: MIPRE.Cost.Prog.wrapHead_cost_at, MIPRE.Cost.Prog.wrapPre_cost_at, MIPRE.Cost.Prog.wrapCore_cost_at, MIPRE.Cost.Prog.esize_wrapCore, MIPRE.Tailored.TailoredVerifier.ofTNFVT, MIPRE.Tailored.TailoredVerifier.ofTNFVT_accepts_iff_ofTNFV, MIPRE.Tailored.TailoredVerifier.ofTNFVT_accepts_iff, MIPRE.Tailored.TailoredVerifier.ofTNFVT_game, MIPRE.Tailored.TailoredVerifier.ofTNFVT_game_D, MIPRE.Tailored.TailoredVerifier.valStar_ofTNFVT, MIPRE.Tailored.TailoredVerifier.hasPerfectPCC_ofTNFVT, MIPRE.Tailored.dom_wrapCoreCost, MIPRE.Tailored.dom_le_pow, MIPRE.Tailored.TailoredVerifier.ofTNFVT_isBounded
statement: formalized
proof: formalized
---

# A tailored verifier as a bounded normal form verifier

Wrap the canonical decider with its total parse in front. The resulting normal form verifier has the games of that of Lemma [A tailored verifier and its normal form verifier have the same games](../part-01/lem-of-tnfv.md), so the same values and perfect PCC strategies, and there is a constant $C$, depending on the universal machine alone, such that it is $C\lambda$-bounded whenever the tailored verifier is $\lambda$-bounded.

## Depends on

- [A tailored verifier as a normal form verifier; II:1757–1787](../part-01/def-of-tnfv.md)
- [A tailored verifier and its normal form verifier have the same games](../part-01/lem-of-tnfv.md)
- [The running time of the canonical decider](lem-canonical-decider-cost.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)
- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)
- [The parameter of the halting verifier](../../structure-of-the-proof/part-09/lem-lambda.md)

## Proof

The two deciders accept the same inputs. The wrapper's cost at an index $n$ needs the sampler's bound at $n$ only; with the canonical decider's bound of Lemma [The running time of the canonical decider](lem-canonical-decider-cost.md), at $T = n^\lambda$ and exponent $\lambda$, every term of the wrapper's cost is dominated by $n^{A\lambda}$ for a constant $A$, and the domination tools turn the whole into $n^{C\lambda}(|d|+1)^{C\lambda}$. The description is that of the wrapper, plus four times that of the length calculator, plus that of the constraint processor, plus a constant.

## Lean

Formalized as [`MIPRE.Cost.Prog.wrapHead_cost_at`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.wrapHead_cost_at), [`MIPRE.Cost.Prog.wrapPre_cost_at`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.wrapPre_cost_at), [`MIPRE.Cost.Prog.wrapCore_cost_at`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.wrapCore_cost_at), [`MIPRE.Cost.Prog.esize_wrapCore`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.Prog.esize_wrapCore), [`MIPRE.Tailored.TailoredVerifier.ofTNFVT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFVT), [`MIPRE.Tailored.TailoredVerifier.ofTNFVT_accepts_iff_ofTNFV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFVT_accepts_iff_ofTNFV), [`MIPRE.Tailored.TailoredVerifier.ofTNFVT_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFVT_accepts_iff), [`MIPRE.Tailored.TailoredVerifier.ofTNFVT_game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFVT_game), [`MIPRE.Tailored.TailoredVerifier.ofTNFVT_game_D`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFVT_game_D), [`MIPRE.Tailored.TailoredVerifier.valStar_ofTNFVT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.valStar_ofTNFVT), [`MIPRE.Tailored.TailoredVerifier.hasPerfectPCC_ofTNFVT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.hasPerfectPCC_ofTNFVT), [`MIPRE.Tailored.dom_wrapCoreCost`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.dom_wrapCoreCost), [`MIPRE.Tailored.dom_le_pow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.dom_le_pow), [`MIPRE.Tailored.TailoredVerifier.ofTNFVT_isBounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFVT_isBounded).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1750](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1750)
