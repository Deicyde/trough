---
declaration: theorem
origin: cited
lean: Rep.iso_ind₁
statement: formalized
proof: formalized
---

# additive field trivial

Let $l/k$ be a finite Galois extension of fields. Then there is an isomorphism of $\mathrm{Gal}(l/k)$-representations:

$$
l \cong \mathrm{ind}_1(k).
$$

In particular $l$ has trivial Tate cohomology as a representation of $\mathrm{Gal}(l/k)$.

## Depends on

- [induced trivial Tate](../../group-cohomology/coinduction-and-induction/lem-induced-trivial-tate.md)

## Proof

Recall from Galois theory that there is a normal basis for $l$ over $k$, i.e. a basis of the form

$$
\{x \bullet b_0 : x \in \mathrm{Gal}(l/k)\}.
$$

Define a map $\mathrm{ind}_1(k) \cong l$ by

$$
\Phi (f : G \to_0 k) = \sum_{x \in \mathrm{Gal}(l/k)} f(x) \cdot x^{-1} \bullet b_0.
$$

The map $\Phi$ is clearly a linear bijection; we check that it commutes with the Galois action:

$$
\Phi(g\bullet f)
= \sum_x f(xg) \cdot x^{-1} \bullet b_0
= \sum_x f(x) \cdot (xg^{-1})^{-1} \bullet b_0
= g \bullet \Phi(f).
$$

## Lean

Formalized as [`Rep.iso_ind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.iso_ind₁).

## Sources

- [Class field theory blueprint: _3_local.tex, line 108](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_3_local.tex#L108)
