---
declaration: lemma
origin: cited
lean: Representation.herbrandQuotient_of_finite, Rep.herbrandQuotient_of_finite
statement: formalized
proof: formalized
---

# herbrand finite

If $M$ is finite then $h(G,M)=1$.

## Depends on

- [Tate cohomology is cohomology or homology](../tate-cohomology/lem-tate-cohomology-is-cohomology-or-homology.md)

## Proof

Let $\mathrm{gen}$ be a generator of $G$. Recall that $H^0_{\mathrm{Tate}}(G,M) \cong M^G / N_GM$. Also, we can write $M^G$ as $\ker(1-\mathrm{gen} : M \to M)$. Similarly $H^{-1}_{\mathrm{Tate}}(G,M)$ is isomorphic to $\ker (N_G : M \to M) / \mathrm{im} (1-\mathrm{gen} : M \to M)$. The result follows because

$$
\begin{aligned}
|\ker(N_G : M \to M)| \cdot |\mathrm{im}(N_G : M \to M)|
&=|M|\\
&=|\ker(1-g : M \to M)| \cdot |\mathrm{im}(1-g : M \to M)|.
\end{aligned}
$$

## Lean

Formalized as [`Representation.herbrandQuotient_of_finite`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.herbrandQuotient_of_finite), [`Rep.herbrandQuotient_of_finite`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.herbrandQuotient_of_finite).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1714](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1714)
