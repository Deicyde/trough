---
declaration: lemma
origin: cited
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/47
---

# MatrixRing.isCentralSimple

If $n\geq1$ then the $n\times n$ matrices $M_n(K)$ are a central simple algebra over $K$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We prove more generally that matrices with coefficients in $K$ and indexed by an arbitrary nonempty finite type are a central simple algebra over $K$.

They are clearly an algebra over $K$, with $K$ embedded via scalar matrices as usual (the injectivity of the map from $K$ comes from nonemptiness of the finite index type). The centre clearly contains $K$; to show that it equals $K$, we argue as follows. Let $e(i,j)$ be the matrix with a 1 in the $i$th row and $j$th column, and zeros everywhere else. An element $Z=(Z_{s,t})_{s,t}$ of the centre commutes with all matrices $e(i,j)$ for $i\not=j$ and these equations immediately imply that $Z_{i,j}=0$ if $i\not=j$ and that $Z_{i,i}=Z_{j,j}$.

It suffices to prove that any nonzero two-sided ideal $I$ is all of $M_n(K)$. So say $0\not=M\in I$ and let's fix $(i,j)$ such that $M_{i,j}\not=0$. One easily checks that $M_{i,j} \mathrm{id} = \sum_{k}e(k,i)\times M\times e(j,k)\in I$ (where $\mathrm{id} \in M_n(K)$ is the identity matrix). Therefore, $\mathrm{id} \in I$, so $I = M_n(K)$.

The definition also requires that the ring be non-zero, but this follows from the index type being nonempty.

## Lean

The blueprint marks this formalized but names no Lean declaration.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch06automorphicrepresentations.tex, line 51](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch06automorphicrepresentations.tex#L51)
