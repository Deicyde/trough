---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Halting.lp_runs_iff, MIPRE.Tailored.Halting.hasPerfectZPC_of_branch1, MIPRE.Tailored.Halting.valStar_eq_zero_of_branch2, MIPRE.Tailored.Halting.hasPerfectZPC_iff_W, MIPRE.Tailored.Halting.valStar_eq_W, MIPRE.Tailored.TailoredVerifier.hasPerfectZPC_congr, MIPRE.Tailored.TailoredVerifier.valStar_congr, MIPRE.Tailored.TailoredVerifier.valStar_eq_zero_of_rejects
statement: formalized
proof: formalized
---

# The values of the tailored halting verifier; II:1978

At the level $n$: if $\mathcal{M}$ halts within the budget, $\mathsf{V}^{\mathcal{M},\lambda}_n$ has a perfect ZPC strategy; otherwise, if the search halts within the budget, it has value $0$; otherwise it has a perfect ZPC strategy, and value, exactly when the compressed verifier of its own programs does at $n$.

## Depends on

- [The tailored halting verifier; II:1900–1925](def-tailored-halt-verifier.md)
- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](../part-01/def-zpc-strategy.md)
- [The trivial strategy; II:1148](../part-01/lem-tailored-trivial-zpc.md)

## Proof

The processor is the fixed point, so on an input of index $n$ it outputs what the three branches say. In the first, every constraint list is empty — the answer-length calculator halts at every question of the sampler, which is where its totality is spent — so the game accepts every answer pair of the right lengths, and the deterministic strategy is perfect (Lemma [The trivial strategy; II:1148](../part-01/lem-tailored-trivial-zpc.md)). In the second, every constraint list holds $J = 0$, so no answer pair is accepted. In the third, the two verifiers have the same sampler and answer-length calculator, and their processors output the same constraints at index $n$, so their $n$-th games coincide.

## Lean

Formalized as [`MIPRE.Tailored.Halting.lp_runs_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.lp_runs_iff), [`MIPRE.Tailored.Halting.hasPerfectZPC_of_branch1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.hasPerfectZPC_of_branch1), [`MIPRE.Tailored.Halting.valStar_eq_zero_of_branch2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.valStar_eq_zero_of_branch2), [`MIPRE.Tailored.Halting.hasPerfectZPC_iff_W`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.hasPerfectZPC_iff_W), [`MIPRE.Tailored.Halting.valStar_eq_W`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.valStar_eq_W), [`MIPRE.Tailored.TailoredVerifier.hasPerfectZPC_congr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.hasPerfectZPC_congr), [`MIPRE.Tailored.TailoredVerifier.valStar_congr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.valStar_congr), [`MIPRE.Tailored.TailoredVerifier.valStar_eq_zero_of_rejects`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.valStar_eq_zero_of_rejects).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 603](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L603)
