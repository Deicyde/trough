---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.ldEqF, MIPRE.Tailored.AnsRed.Typed.ldEqF_eq, MIPRE.Tailored.AnsRed.Typed.ldLineF, MIPRE.Tailored.AnsRed.Typed.ldLineF_eq, MIPRE.Tailored.AnsRed.Typed.blocks1_ldPart, MIPRE.Tailored.AnsRed.Typed.ldConsF, MIPRE.Tailored.AnsRed.Typed.ldConsF_eq
statement: formalized
proof: formalized
---

# The low-degree checks, as programs

For a selector computed by the introspection stage's selector program, a program computes the constraints of the low-degree checks at two questions of one role from the parameters, the types, the two questions' low-degree bits and the layout of the answers: the equations that two answers agree codeword by codeword, each the difference of two windows, and the equations that the line polynomials at the line parameter are the point values, by Horner's rule.

## Depends on

- [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md)
- [The low-degree half of the answer-reduced sampler, directly answered](../part-07/lem-ar-ld-direct.md)
- [The answer-reduced game as typed tailored data; defn:combi_ans_red](../part-06/def-ar-tailored-game.md)
- [The constraint lists of the auxiliary checks, as programs](../part-05/lem-intro-aux-progs.md)

## Proof

A question's low-degree vector is read from the last bits of its vector part in runs of blocks, the point, the direction and the seed (Lemma [The low-degree half of the answer-reduced sampler, directly answered](../part-07/lem-ar-ld-direct.md)). The selected direction of an axis-parallel line is the seed's block, and the point-on-line guard and the line parameter are computed by the introspection stage's programs. Lemma [Field equations as constraints, and field arithmetic, as programs](lem-ar-field-cons.md) turns the equations' values into the constraints.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.ldEqF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldEqF), [`MIPRE.Tailored.AnsRed.Typed.ldEqF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldEqF_eq), [`MIPRE.Tailored.AnsRed.Typed.ldLineF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldLineF), [`MIPRE.Tailored.AnsRed.Typed.ldLineF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldLineF_eq), [`MIPRE.Tailored.AnsRed.Typed.blocks1_ldPart`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.blocks1_ldPart), [`MIPRE.Tailored.AnsRed.Typed.ldConsF`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldConsF), [`MIPRE.Tailored.AnsRed.Typed.ldConsF_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldConsF_eq).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3707](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3707)
