---
declaration: definition
origin: cited
lean: Verifier.knowledgeSoundness, Verifier.knowledgeSoundnessWith
statement: formalized
---

# Knowledge Soundness

A reduction satisfies **(straightline) knowledge soundness** with error $\epsilon \geq 0$ and with respect to input relation $R_{\text{in}}$ and output relation $R_{\text{out}}$ if:

- there exists a straightline extractor $E$, such that
- for every input statement $x_{\text{in}}$, every private-input type and private input of the prover, and every (malicious) prover, all chosen after $E$,
- if the execution with the honest verifier results in a pair $(x_{\text{out}}, w_{\text{out}})$,

then the probability that $(x_{\text{out}}, w_{\text{out}})$ is valid for $R_{\text{out}}$ and yet the extractor fails to produce a witness $w'_{\text{in}}$ such that $(x_{\text{in}}, w'_{\text{in}})$ is valid for $R_{\text{in}}$ is at most $\epsilon$.

Note that the extractor failing outright (it is a partial computation) counts as a win for the adversary: whenever the prover convinces the verifier, the extractor is obliged to succeed and produce a valid witness. (Excluding extractor failure from the bad event would render the definition vacuous, as the always-failing extractor would satisfy it for any verifier.) In contrast, runs in which the protocol execution itself fails (e.g. the verifier aborts) impose no obligation on the extractor, matching the convention for plain soundness.

The same game for one named extractor $E$ is $\mathsf{knowledgeSoundnessWith}$; knowledge soundness is its existential closure over $E$.

## Depends on

- [Type Signature of a Verifier](../part-01/def-verifier.md)
- [Interactive Reduction Execution](../part-01/def-reduction-run.md)
- [Straightline Extractor](../part-01/def-straightline-extractor.md)

## Lean

Formalized as [`Verifier.knowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.knowledgeSoundness), [`Verifier.knowledgeSoundnessWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.knowledgeSoundnessWith).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 580](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L580)
