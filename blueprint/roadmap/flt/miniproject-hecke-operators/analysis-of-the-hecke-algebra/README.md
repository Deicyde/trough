# Analysis of the Hecke algebra

First we discuss commutativity of the Hecke operators. First, assume that $v\not\in S$. Then $U=GL_2(\mathcal{O}_v)\times U'$ where $U'$ is a subgroup of the restricted product of $GL_2(F_w)$ for $w\not=v$. We can use RestrictedProduct.SubmonoidClass.isProductAt to express this concept of being an internal direct product. If $g$ is the element of $G$ used to make $T_v$ then $g$ is also supported at $w$, so the double coset space $UgU$ is just $(GL_2(\mathcal{O}_v)\begin{pmatrix}\varpi&0\\0&1\end{pmatrix}GL_2(\mathcal{O}_v))\times U'$ and in particular can be decomposed into single left $U$-cosets of the form $g_iU$ where $g_i$ is also supported at $v$. This is RestrictedProduct.mem\_coset\_and\_mulSupport\_subset\_of\_isProductAt.

Similarly if $v\in S$, if $0\not=\alpha\in\mathcal{O}_v$ and if $g_v=\begin{pmatrix}\alpha&0\\0&1\end{pmatrix}$ and is 1 elsewhere, then the double coset space $UgU$ can again be written as $\coprod_i g_iU$ with the $g_i$ supported only at $v$.

We deduce immediately from lemma [Lemma AbstractHeckeOperator.comm](../the-abstract-theory/abstractheckeoperator-comm.md) that two Hecke operators associated to different finite places of $F$ commute. What remains is to check that $U_{\alpha,v}$ and $U_{\beta,v}$ commute. In fact we claim more, namely that $U_{\alpha,v}U_{\beta,v}=U_{\alpha\beta,v}$. This will suffice because $\alpha\beta=\beta\alpha$.

- [nolean-product-of-U-alpha](nolean-product-of-u-alpha.md)
