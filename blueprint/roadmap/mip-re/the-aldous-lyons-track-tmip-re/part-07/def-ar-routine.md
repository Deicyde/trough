---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ArParams, MIPRE.Tailored.AnsRed.Typed.arParams, MIPRE.Tailored.AnsRed.Typed.readParams, MIPRE.Tailored.AnsRed.Typed.readParams_encode, MIPRE.Tailored.AnsRed.Typed.ldPdF, MIPRE.Tailored.AnsRed.Typed.ldPdF_arParams, MIPRE.Tailored.AnsRed.Typed.CircIn, MIPRE.Tailored.AnsRed.Typed.ArRoutine, MIPRE.Tailored.AnsRed.Typed.ArRoutine.params, MIPRE.Tailored.AnsRed.Typed.ArRoutine.parCore_runs, MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore, MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore_runs, MIPRE.Tailored.AnsRed.Typed.ArRoutine.toLd, MIPRE.Tailored.AnsRed.Typed.ArRoutine.circ, MIPRE.Tailored.AnsRed.Typed.ArRoutine.circ_wires
statement: formalized
---

# The parameter routine of the answer-reduced verifier

The *parameters* of the answer-reduced verifier at an index are, in unary, the field width $t$, the selector width $j$, $M = 2^j$, the degree $d$, the four dimensions of the PCP of Definition [The PCP and its thirteen checks](../part-05/def-ar-pcp.md), and data for the circuits. A *parameter routine* consists of the parameters at each $(\lambda, \mu, \sigma)$ and index, with $m \leq M$; a closed program computing them from $((\lambda, \mu, \sigma), n)$; and a polynomial-time *circuit function*, giving from the input verifier's programs, $(\lambda, \mu, \sigma)$, $n$, the parameters and the two questions of a seed a well-formed circuit with the PCP's numbers of inputs and gates. The program followed by the projection to $(t, j)$ is a parameter routine of the low-degree half.

## Depends on

- [The answer-reduced sampler](def-ar-sampler.md)
- [The PCP and its thirteen checks](../part-05/def-ar-pcp.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ArParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArParams), [`MIPRE.Tailored.AnsRed.Typed.arParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arParams), [`MIPRE.Tailored.AnsRed.Typed.readParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.readParams), [`MIPRE.Tailored.AnsRed.Typed.readParams_encode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.readParams_encode), [`MIPRE.Tailored.AnsRed.Typed.ldPdF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldPdF), [`MIPRE.Tailored.AnsRed.Typed.ldPdF_arParams`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldPdF_arParams), [`MIPRE.Tailored.AnsRed.Typed.CircIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.CircIn), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.params`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.params), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.parCore_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.parCore_runs), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.ldCore_runs), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.toLd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.toLd), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.circ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.circ), [`MIPRE.Tailored.AnsRed.Typed.ArRoutine.circ_wires`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArRoutine.circ_wires).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3620](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3620)
