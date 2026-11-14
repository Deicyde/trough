---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Params.ArConsts, MIPRE.Tailored.AnsRed.Params.pQ, MIPRE.Tailored.AnsRed.Params.pEll, MIPRE.Tailored.AnsRed.Params.pDm, MIPRE.Tailored.AnsRed.Params.pOW, MIPRE.Tailored.AnsRed.Params.pK, MIPRE.Tailored.AnsRed.Params.pT, MIPRE.Tailored.AnsRed.Params.pSig, MIPRE.Tailored.AnsRed.Params.pR, MIPRE.Tailored.AnsRed.Params.pS, MIPRE.Tailored.AnsRed.Params.pL, MIPRE.Tailored.AnsRed.Params.pJ, MIPRE.Tailored.AnsRed.Params.pD, MIPRE.Tailored.AnsRed.Params.pTw, MIPRE.Tailored.AnsRed.Params.pExtra
statement: formalized
---

# The parameters of the answer reduction

For constants $E_1, E_2, c_0$ and $(\lambda, \mu, \sigma)$, at the index $n$, with $Q = (\lambda n + 1)^\mu$ the input's budget: the window width $\ell = Q$; the copy width $\Delta = (\mu + 2)(Q + 4)$; the table width $o = 2\ell + 3\Delta + 6$; the description time $T = 2^K$, $K = E_1 (\mu + 1)(o + Q + 4)$; the size bound $\sigma' = c_0 + 5\sigma + 4(\ell + \Delta) + 8$ of the output indicator's program; the witness width $r$ and the gate count $s$ the window describer of Lemma [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md) gives at $(n, T, Q, \sigma')$; the selector width $j = \lceil \log_2 (m + 1) \rceil$, $m$ the PCP's variable count; the degree $d = 17$; and the field width $t = E_2 (j + r + Q + 1)$.

## Depends on

- [The PCP and its thirteen checks](../part-05/def-ar-pcp.md)
- [Decoupled 6SAT through three windows; prop:explicit-padded-succinct-deciders](../part-05/lem-ar-window-describer.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Params.ArConsts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.ArConsts), [`MIPRE.Tailored.AnsRed.Params.pQ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pQ), [`MIPRE.Tailored.AnsRed.Params.pEll`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pEll), [`MIPRE.Tailored.AnsRed.Params.pDm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pDm), [`MIPRE.Tailored.AnsRed.Params.pOW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pOW), [`MIPRE.Tailored.AnsRed.Params.pK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pK), [`MIPRE.Tailored.AnsRed.Params.pT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pT), [`MIPRE.Tailored.AnsRed.Params.pSig`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pSig), [`MIPRE.Tailored.AnsRed.Params.pR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pR), [`MIPRE.Tailored.AnsRed.Params.pS`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pS), [`MIPRE.Tailored.AnsRed.Params.pL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL), [`MIPRE.Tailored.AnsRed.Params.pJ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pJ), [`MIPRE.Tailored.AnsRed.Params.pD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pD), [`MIPRE.Tailored.AnsRed.Params.pTw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pTw), [`MIPRE.Tailored.AnsRed.Params.pExtra`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pExtra).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 4021](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L4021)
