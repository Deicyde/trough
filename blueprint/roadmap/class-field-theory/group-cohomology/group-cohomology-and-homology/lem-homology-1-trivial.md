---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: groupHomology.H1AddEquivOfIsTrivial
---

# homology 1 trivial

If $M$ is a trivial representation of $G$ then $H_1(G,M) \cong G^{\mathrm{ab}} \otimes {\mathbb Z} M$. The isomorphism takes a 1-cycle $\mathrm{single}(x,m)$ to $xG' \otimes m$ for $x \in G$ and $m \in M$. (This result is already in Mathlib).

## Depends on

- [group homology](def-group-homology.md)

## Proof

Since $M$ is trivial, the map $d_0 : C_1(G,M) \to C_0(G,M)$ is zero, so every $1$-chain is a 1-cycle. The map $d_1 : C_1(G,M) \to C_0(G,M)$ is given by

$$
d_1 \mathrm{single}((x,y),m)
= \mathrm{single}(y,x^{-1} \bullet m) - \mathrm{single}(xy,m) + \mathrm{single}(x,m).
$$

Therefore $H_1(G,M)$ is the quotient of $G \to_0 M$ by the relations

$$
\mathrm{single}(xy,m) = \mathrm{single}(x,m) + \mathrm{single}(y,m),
\qquad x,y \in G.
$$

If we fix an $m \in M$, then these relations imply that the map $G \to H_1(G,M)$ defined by $x \mapsto \mathrm{single}(x,m)$ is a group homomorphism. In particular this map descends to a homomorphism $G^{\mathrm{ab}} \to H_1(G,M)$. If we fix $x \in G$ and allow $m$ to vary, then $\mathrm{single}(x,m)$ is ${\mathbb Z}$-linear in $m$. It is therefore a ${\mathbb Z}$-bilinear map $G^\mathrm{ab} \times M \to H_1(G,M)$. Such a map lifts to a linear map $\Phi : G^{\mathrm{ab}} \otimes_{{\mathbb Z}} M \to H_1(G,M)$ given by

$$
xG' \otimes m \mapsto \mathrm{single}(x,m)
$$

To construct an inverse of $\Phi$, we note that all of the relations are in the kernel of the linear map $(G\to_0 M) \to (G^\mathrm{ab} \otimes_{\mathbb Z} M)$ defined by $\mathrm{single}(x,m) \mapsto xG' \otimes m$. Therefore this map descends to a linear map $\Psi : H_1(G,M) \to (G^\mathrm{ab} \otimes_{\mathbb Z} M)$. It is trivial to check that $\Phi$ and $\Psi$ are inverses.

## Lean

Formalized as [`groupHomology.H1AddEquivOfIsTrivial`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/groupHomology.H1AddEquivOfIsTrivial).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 359](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L359)
