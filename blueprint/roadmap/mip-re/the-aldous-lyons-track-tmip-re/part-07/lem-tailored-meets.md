---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.lenOf_eq_of_lenIs, MIPRE.Tailored.TailoredVerifier.MeetsAt.extends_, MIPRE.Tailored.TailoredVerifier.MeetsAt.valStar_eq, MIPRE.Tailored.TailoredVerifier.MeetsAt.hasPerfectZPC
statement: formalized
proof: formalized
---

# A tailored verifier meeting a game extends it

If $\mathsf{V}$ meets $G$ at $n$ along $e$, then $\mathsf{V}$'s $n$-th game extends $G$ along $e$. So it has $G$'s $\mathrm{val}^*$, and a perfect ZPC strategy of $G$'s doubled game gives one of $\mathsf{V}$'s $n$-th game.

## Depends on

- [A tailored verifier meeting a tailored game](def-tailored-meets.md)
- [Extending a tailored game along its questions](../part-02/lem-tailored-extend.md)

## Proof

The lengths of $\mathsf{V}$'s game at a question are what its calculator outputs there, and its constraints at a pair are what its processor outputs once the calculator halts at both questions at both kinds. Every question of $\mathsf{V}$ at $n$ is some $e(x)$, which is the support condition of an extension. Lemma [Extending a tailored game along its questions](../part-02/lem-tailored-extend.md) concludes.

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.lenOf_eq_of_lenIs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.lenOf_eq_of_lenIs), [`MIPRE.Tailored.TailoredVerifier.MeetsAt.extends_`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.MeetsAt.extends_), [`MIPRE.Tailored.TailoredVerifier.MeetsAt.valStar_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.MeetsAt.valStar_eq), [`MIPRE.Tailored.TailoredVerifier.MeetsAt.hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.MeetsAt.hasPerfectZPC).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3495](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3495)
