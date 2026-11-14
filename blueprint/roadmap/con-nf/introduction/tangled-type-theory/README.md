# Tangled type theory

Introduced by Holmes in ([Holmes 1995](http://www.jstor.org/stable/2275515)), *tangled type theory* ($\mathsf{TTT}$) is a multi-sorted first order theory based on $\mathsf{TST}$. This theory is parametrised by a limit ordinal $\lambda$, the elements of which will index the sorts; $\omega$ works, but we prefer generality. As in $\mathsf{TST}$, each variable ${\text{‘}x\text{’}}$ has a type that it belongs to, denoted $\operatorname{\mathsf{type}}({\text{‘}x\text{’}})$. However, in $\mathsf{TTT}$, this is not a positive integer, but an element of $\lambda$.

The primitive predicates of this theory are equality and membership. An equality ${\text{‘}x = y\text{’}}$ is a well-formed formula when $\operatorname{\mathsf{type}}({\text{‘}x\text{’}}) = \operatorname{\mathsf{type}}({\text{‘}y\text{’}})$. A membership formula ${\text{‘}x \in y\text{’}}$ is well-formed when $\operatorname{\mathsf{type}}({\text{‘}x\text{’}}) < \operatorname{\mathsf{type}}({\text{‘}y\text{’}})$.

The axioms of $\mathsf{TTT}$ are obtained by taking the axioms of $\mathsf{TST}$ and replacing all type indices in a consistent way with elements of $\lambda$. More precisely, for any order-embedding $s : \omega \to \lambda$, we can convert a well-formed formula $\varphi$ of $\mathsf{TST}$ into a well-formed formula $\varphi^s$ of $\mathsf{TTT}$ by replacing each type variable $\alpha$ with $s(\alpha)$.

It is important to note that membership across types in $\mathsf{TTT}$ behaves in some quite bizarre ways. Let $\alpha \in \lambda$, and let $x$ be a set of type $\alpha$. For any $\beta < \alpha$, the extensionality axiom implies that $x$ is uniquely determined by its type-$\beta$ elements. However, it is simultaneously determined by its type-$\gamma$ elements for any $\gamma < \alpha$. In this way, one extension of a set controls all of the other extensions.

The comprehension axiom allows a set to be built which has a specified extension in a single type. The elements not of this type may be considered ‘controlled junk’.

We now present the following striking theorem, which we will prove a version of in detail in [Model theory and verifying $\operatorname{\mathsf{Con}}({\mathsf{NF}})$](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/content.tex#L29).

**Theorem (Holmes).** $\mathsf{NF}$ is consistent if and only if $\mathsf{TTT}$ is consistent. ([Holmes 1995](http://www.jstor.org/stable/2275515))

Thus, our task of proving $\mathsf{NF}$ consistent is reduced to the task of proving $\mathsf{TTT}$ consistent. We will do this by exhibiting an explicit model (albeit one that requires a great deal of Choice to construct). As $\mathsf{TTT}$ has types indexed by a limit ordinal, and sets can only contain sets of lower type, we can construct a model by recursion over $\lambda$. In particular, a model of $\mathsf{TTT}$ is a well-founded structure. This was not an option with $\mathsf{NF}$ directly, as the universal set $V = \{ x \mid x = x \}$ would necessarily be constructed before many of its elements.
