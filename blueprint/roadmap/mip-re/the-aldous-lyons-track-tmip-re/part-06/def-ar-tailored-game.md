---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.elt, MIPRE.Tailored.AnsRed.Typed.lenR, MIPRE.Tailored.AnsRed.Typed.lenL, MIPRE.Tailored.AnsRed.Typed.cw, MIPRE.Tailored.AnsRed.Typed.decAns, MIPRE.Tailored.AnsRed.Typed.vals, MIPRE.Tailored.AnsRed.Typed.regs, MIPRE.Tailored.AnsRed.Typed.ldQ, MIPRE.Tailored.AnsRed.Typed.ldCons, MIPRE.Tailored.AnsRed.Typed.consCons, MIPRE.Tailored.AnsRed.Typed.indCons, MIPRE.Tailored.AnsRed.Typed.proofCons, MIPRE.Tailored.AnsRed.Typed.cons, MIPRE.Tailored.AnsRed.Typed.tdata, MIPRE.Tailored.AnsRed.Typed.ArPred
statement: formalized
---

# The answer-reduced game as typed tailored data; defn:combi_ans_red

Fix $q = 2^t$, $M = 2^j$ dividing $q$, a degree $d$, a PCP layout with $m \leq M$ variables, the dimension $r$ of the input sampler at the index, a seed selector of the low-degree test (Definition [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md)), and a circuit polynomial $T_z$ for each $z \in \mathbb{F}_2^r$. The types are $\{A, B, O\} \times \{\mathrm{Point}, \mathrm{ALine}, \mathrm{DLine}\}$; a question carries an element of $\mathbb{F}_2^r$ and, over $\mathbb{F}_2$ through the Shoup basis, a question of the seeded low-degree test on $M$ variables. An answer is a codeword for each of its role's slots, readable first: one field element at a point, the $d + 1$ or $Md + 1$ coefficients of a polynomial at an axis-parallel or a diagonal line, each element as its $t$ canonical bits. The constraints at two typed questions are linear in the answer bits, with coefficients read off the questions and the readable answers:

1. at one role, the seeded low-degree test on the role's codewords;
2. at one low-degree type, an isolated role and the oracle, the isolated codewords are the oracle's in the same slots;
3. at an axis-parallel line in the direction $i$, the codewords whose blocks miss $i$ have their coefficients $1, \dots, d$ zero;
4. at the oracle's point $p$ with seed $z$, the thirteen checks of the PCP against $T_z$ at the first $m$ coordinates of $p$: the readable checks as a readable guard, and the linear checks as linear equations, the system check's coefficients read off $g_O(p)$ and the linear assignment checks linear because $g \mapsto g(1 - g)$ is additive in characteristic two.

## Depends on

- [The slots of a PCP](def-ar-slots.md)
- [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md)
- [Detyping a tailored game](../part-03/def-tailored-detyping.md)
- [The Pauli basis test as linear constraints](../part-04/lem-intro-pauli-cons.md)
- [Linear forms on windows, and the input's constraints re-indexed](../part-04/lem-intro-forms.md)
- [The PCP sampler of answer reduction](../../structure-of-the-proof/part-08/def-ar-pcp-sampler.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.elt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.elt), [`MIPRE.Tailored.AnsRed.Typed.lenR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenR), [`MIPRE.Tailored.AnsRed.Typed.lenL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.lenL), [`MIPRE.Tailored.AnsRed.Typed.cw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.cw), [`MIPRE.Tailored.AnsRed.Typed.decAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.decAns), [`MIPRE.Tailored.AnsRed.Typed.vals`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.vals), [`MIPRE.Tailored.AnsRed.Typed.regs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.regs), [`MIPRE.Tailored.AnsRed.Typed.ldQ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldQ), [`MIPRE.Tailored.AnsRed.Typed.ldCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldCons), [`MIPRE.Tailored.AnsRed.Typed.consCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.consCons), [`MIPRE.Tailored.AnsRed.Typed.indCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indCons), [`MIPRE.Tailored.AnsRed.Typed.proofCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofCons), [`MIPRE.Tailored.AnsRed.Typed.cons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.cons), [`MIPRE.Tailored.AnsRed.Typed.tdata`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.tdata), [`MIPRE.Tailored.AnsRed.Typed.ArPred`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArPred).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2869](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2869)
