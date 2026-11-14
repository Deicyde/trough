---
declaration: definition
origin: cited
lean: Verifier.rbrSoundness
statement: formalized
---

# Round-by-Round Soundness

A protocol with verifier $\mathcal{V}$ satisfies **round-by-round soundness** with respect to input language $L_{\text{in}}$, output language $L_{\text{out}}$, and error function $\epsilon: \text{ChallengeIdx} \to \mathbb{R}_{\geq 0}$ if:

- there exists a state function for the verifier and the input/output languages, such that
- for all initial statements $x_{\text{in}} \notin L_{\text{in}}$,
- for all challenge rounds $i$,
- for all transcript prefixes $\tau$ up to round $i$,

the probability, over the next challenge $c$ chosen uniformly at random, that:

- the state function is false at $\tau$, and
- the state function is true at $\tau$ extended by $c$

is at most $\epsilon(i)$. This is the formulation of ([Canetti et al. 2019](https://doi.org/10.1145/3313276.3316380)) and ([Arnon et al. 2026](https://proximityprize.org/)).

## Depends on

- [Type Signature of a Verifier](../part-01/def-verifier.md)
- [State Function](def-state-function.md)

## Lean

Formalized as [`Verifier.rbrSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.rbrSoundness).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 671](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L671)
