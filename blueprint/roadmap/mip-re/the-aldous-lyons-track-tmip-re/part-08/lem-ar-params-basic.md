---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Params.pL_ℓ, MIPRE.Tailored.AnsRed.Params.pL_dm, MIPRE.Tailored.AnsRed.Params.pL_r, MIPRE.Tailored.AnsRed.Params.pL_s, MIPRE.Tailored.AnsRed.Params.pL_oW, MIPRE.Tailored.AnsRed.Params.one_le_pQ, MIPRE.Tailored.AnsRed.Params.pL_m_lt, MIPRE.Tailored.AnsRed.Params.pL_m_le, MIPRE.Tailored.AnsRed.Params.pJ_le_pTw, MIPRE.Tailored.AnsRed.Params.one_le_pTw, MIPRE.Tailored.AnsRed.Params.pQ_le_pK, MIPRE.Tailored.AnsRed.Params.pOW_le_pK
statement: formalized
proof: formalized
---

# First facts about the parameters

$m < 2^j$; once $E_2 \geq 1$, $1 \leq t$ and $j \leq t$; once $E_1 \geq 1$, $Q \leq K$ and $o \leq K$.

## Depends on

- [The parameters of the answer reduction](def-ar-params.md)

## Proof

$m < 2^{\lceil \log_2 (m + 1) \rceil}$, and the other bounds are linear.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Params.pL_ℓ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_ℓ), [`MIPRE.Tailored.AnsRed.Params.pL_dm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_dm), [`MIPRE.Tailored.AnsRed.Params.pL_r`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_r), [`MIPRE.Tailored.AnsRed.Params.pL_s`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_s), [`MIPRE.Tailored.AnsRed.Params.pL_oW`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_oW), [`MIPRE.Tailored.AnsRed.Params.one_le_pQ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.one_le_pQ), [`MIPRE.Tailored.AnsRed.Params.pL_m_lt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_m_lt), [`MIPRE.Tailored.AnsRed.Params.pL_m_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pL_m_le), [`MIPRE.Tailored.AnsRed.Params.pJ_le_pTw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pJ_le_pTw), [`MIPRE.Tailored.AnsRed.Params.one_le_pTw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.one_le_pTw), [`MIPRE.Tailored.AnsRed.Params.pQ_le_pK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pQ_le_pK), [`MIPRE.Tailored.AnsRed.Params.pOW_le_pK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Params.pOW_le_pK).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 4036](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L4036)
