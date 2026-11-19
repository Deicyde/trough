---
declaration: lemma
origin: cited
lean: Rep.coind₁'_obj_iso_coind₁
statement: formalized
proof: formalized
---

# coind₁' iso coind₁

The representations $\mathrm{coind}_1'(M)$ and $\mathrm{coind}_1(G,M)$ of $G$ are isomorphic. More precisely there is an isomorphism of functors $\mathrm{coind}_1' \cong \mathrm{coind}_1(G,-) \circ \mathbf{forget}$, where $\mathbf{forget} : \mathbf{Rep}(R,G) \to \mathbf{Mod}(R)$ is the forgetful functor.

## Depends on

- [induced](../coinduction-and-induction/def-induced.md)
- [coind₁'](def-coind1.md)

## Proof

The map $f \mapsto (x \mapsto x \bullet f(x))$ is an isomorphism from $\mathrm{coind}_1'(M)$ to $\mathrm{coind}_1(G,M)$.

## Lean

Formalized as [`Rep.coind₁'_obj_iso_coind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.coind₁'_obj_iso_coind₁).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 944](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L944)
