---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Slot, MIPRE.Tailored.AnsRed.Slot.readable, MIPRE.Tailored.AnsRed.Slot.emb, MIPRE.Tailored.AnsRed.slotsOf, MIPRE.Tailored.AnsRed.idxO, MIPRE.Tailored.AnsRed.Pcp.slot, MIPRE.Tailored.AnsRed.Pcp.slotEval, MIPRE.Tailored.AnsRed.PassesV, MIPRE.Tailored.AnsRed.PassesR, MIPRE.Tailored.AnsRed.PassesL, MIPRE.Tailored.AnsRed.Pcp.ofPolys
statement: formalized
---

# The slots of a PCP

A PCP (Definition [The PCP and its thirteen checks](../part-05/def-ar-pcp.md)) has a *slot* for each of its polynomials, readable or linear, with its *block*: the injection of the polynomial's variables into the PCP's. The codewords of the oracle are all the slots, the readable ones first (the paper's count of eq:def\_heartsuit, readable and linear); those of Alice are $g_A$ and $g_{L_a}$, those of Bob $g_B$ and $g_{L_b}$. The thirteen checks at a point read only the values of the slots there; they split into the *readable checks*, the formula check and the readable assignment checks, and the *linear checks*, the system check and the linear assignment checks. From polynomials on $N \geq m$ variables, one per slot, the *PCP of the polynomials* reads each on its slot's block.

## Depends on

- [The PCP and its thirteen checks](../part-05/def-ar-pcp.md)
- [The oracularized game](../../structure-of-the-proof/part-06/def-oracular-game.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Slot), [`MIPRE.Tailored.AnsRed.Slot.readable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Slot.readable), [`MIPRE.Tailored.AnsRed.Slot.emb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Slot.emb), [`MIPRE.Tailored.AnsRed.slotsOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.slotsOf), [`MIPRE.Tailored.AnsRed.idxO`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.idxO), [`MIPRE.Tailored.AnsRed.Pcp.slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp.slot), [`MIPRE.Tailored.AnsRed.Pcp.slotEval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp.slotEval), [`MIPRE.Tailored.AnsRed.PassesV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.PassesV), [`MIPRE.Tailored.AnsRed.PassesR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.PassesR), [`MIPRE.Tailored.AnsRed.PassesL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.PassesL), [`MIPRE.Tailored.AnsRed.Pcp.ofPolys`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Pcp.ofPolys).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2825](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2825)
