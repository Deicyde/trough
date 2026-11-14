---
declaration: lemma
origin: cited
lean: Representation.ind₁'_lequiv, Representation.ind₁'_lequiv_comm, Rep.ind₁'_obj_iso_ind₁
statement: formalized
proof: formalized
---

# ind₁' iso ind₁

The representations $\mathrm{ind}_1'(M)$ and $\mathrm{ind}_1(G,M)$ are isomorphic; more precisely the functors $\mathrm{ind}_1'$ and $\mathrm{ind}_1(G,-) \circ \mathbf{forget}$ are isomorphic.

## Depends on

- [ind'](def-ind.md)
- [induced](../coinduction-and-induction/def-induced.md)

## Proof

The data of the isomorphism is contained in the lean file; the isomorphism takes $f : G \to_0 M$ to the finitely supported function

$$
x \mapsto x \bullet f(x).
$$

It remains to check linearity and naturality.

## Lean

Formalized as [`Representation.ind₁'_lequiv`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.ind₁'_lequiv), [`Representation.ind₁'_lequiv_comm`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.ind₁'_lequiv_comm), [`Rep.ind₁'_obj_iso_ind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.ind₁'_obj_iso_ind₁).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1080](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1080)
