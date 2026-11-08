# Some local theory

We could work over a general nonarchimedean normed field but we still do not have them in mathlib, so we stick to the case of interest which is the completion of a number field $K$ at a finite place $v$. Such a completion is a topological field $K_v$ equipped with a discrete valuation, a ring of integers $\mathcal{O}_v$ having a principal maximal ideal $(\varpi)$, and a finite residue field $k_v:=\mathcal{O}_v/(\varpi)$.

There is no formal Lean code for the lemmas in this section; I am slightly dragging my feet because it would seem more sensible to prove them in the right generality, and we don't have a definition of nonarchimedean local field yet.

- [NumberField.isOpenAdicCompletionIntegers](numberfield-isopenadiccompletionintegers.md)

$\mathcal{O}_v$ is also a compact subring of $K_v$; we proved this in the adele miniproject.

- [M2.localFullLevel.isOpen](m2-localfulllevel-isopen.md)
- [M2.localFullLevel.isCompact](m2-localfulllevel-iscompact.md)

Recall that there is a projection $\mathcal{O}_v\to k_v$ where $k_v$ is the residue field of $v$, a finite field. This induces a ring homomorphism $M_2(\mathcal{O}_v)\to M_2(k_v)$ with kernel $M_2(\varpi\mathcal{O}_v)$, an ideal $I$ of $M_2(\mathcal{O}_v)$ isomorphic to $(\varpi\mathcal{O}_v)^4$ and hence also compact and open.

Say $\Gamma_v$ is a subgroup of $GL_2(k_v)$. Then $\Gamma_v$ is finite. Consider it as a submonoid of the multiplicative monoid $M_2(k_v)$. Its preimage $U_v$ in $M_2(\mathcal{O}_v)$ is easily checked to be a submonoid of $M_2(\mathcal{O}_v)$; furthermore it is a finite union of cosets of $I$ and is hence compact and open as a submonoid of $M_2(\mathcal{O}_v)$ and hence of $M_2(K_v)$.

Say now $\begin{pmatrix}1&*\\0&1\end{pmatrix}\subseteq\Gamma_v\subseteq\begin{pmatrix}*&*\\0&*\end{pmatrix}$ and let $U:=U_v$ be its preimage in $GL_2(\mathcal{O}_v)$, considered as a compact open subgroup of $GL_2(K_v)$. Choose $0\not=\alpha\in\mathcal{O}_v$ and define $g=\begin{pmatrix}\alpha&0\\0&1\end{pmatrix}\in GL_2(K_v)$. Let's do an explicit double coset decomposition in preparation for a calculation with Hecke operators.

- [bijOn_unipotent_mul_diagU1_U1diagU1](bijon-unipotent-mul-diagu1-u1diagu1.md)
