# Finitely axiomatising tangled type theory

As mentioned above, Hailperin showed in ([Hailperin 1944](https://doi.org/10.2307/2267307)) that the comprehension scheme of $\mathsf{NF}$ is equivalent to a finite conjunction of its instances. In fact, the same proof shows that the comprehension scheme of $\mathsf{TST}$ (and hence that of $\mathsf{TTT}$) is equivalent to a finite conjunction of its instances, but instantiated at all possible type sequences.

We will exhibit one such collection of instances here, totalling eleven axioms. Our choice is inspired by those used in the Metamath implementation of Hailperin's algorithm in ([Fenton 2015](https://us.metamath.org/nfeuni/mmnf.html)). In the following table, the notation $\langle a, b \rangle$ denotes the Kuratowski pair $\{ \{ a \}, \{ a, b \} \}$. The first column is Hailperin's name for the axiom, and the second is (usually) the name from ([Fenton 2015](https://us.metamath.org/nfeuni/mmnf.html)).

| P1(a) | intersection | $\forall x^1 y^1,\, \exists z^1,\, \forall w^0,\, w \in z \leftrightarrow (w \in x \wedge w \in y)$ |
| --- | --- | --- |
| P1(b) | complement | $\forall x^1,\, \exists z^1,\, \forall w^0,\, w \in z \leftrightarrow w \notin x$ |
| $-$ | singleton | $\forall x^0,\, \exists y^1,\, \forall z^0,\, z \in y \leftrightarrow z = x$ |
| P2 | singleton image | $\forall x^3,\, \exists y^4,\, \forall z^0 w^0,\, \langle \{ z \}, \{ w \} \rangle \in y \leftrightarrow \langle z, w \rangle \in x$ |
| P3 | insertion two | $\forall x^3,\, \exists y^5,\, \forall z^0 w^0 t^0,\, \langle \{ \{ z \} \}, \langle w, t \rangle \rangle \in y \leftrightarrow \langle z, t \rangle \in x$ |
| P4 | insertion three | $\forall x^3,\, \exists y^5,\, \forall z^0 w^0 t^0,\, \langle \{ \{ z \} \}, \langle w, t \rangle \rangle \in y \leftrightarrow \langle z, w \rangle \in x$ |
| P5 | cross product | $\forall x^1,\, \exists y^3,\, \forall z^2,\, z \in y \leftrightarrow \exists w^0 t^0,\, z = \langle w, t \rangle \wedge t \in x$ |
| P6 | type lowering | $\forall x^4,\, \exists y^1,\, \forall z^0,\, z \in y \leftrightarrow \forall w^1,\, \langle w, \{ z \} \rangle \in x$ |
| P7 | converse | $\forall x^3,\, \exists y^3,\, \forall z^0 w^0,\, \langle z, w \rangle \in y \leftrightarrow \langle w, z \rangle \in x$ |
| P8 | cardinal one | $\exists x^2,\, \forall y^1,\, y \in x \leftrightarrow \exists z^0,\, \forall w,\, w \in y \leftrightarrow w = z$ |
| P9 | subset | $\exists x^4,\, \forall y^1 z^1,\, \langle y, z \rangle \in x \leftrightarrow \forall w^0,\, w \in y \to w \in z$ |

Axioms P1–P9 except for P6 are *predicative*: they stipulate the existence of a set with type at least that of all of the parameters. It is relatively straightforward to prove the consistency of predicative $\mathsf{TTT}$, and we will see later that the proof of P6 in our model takes a different form to the proofs of the other axioms.
