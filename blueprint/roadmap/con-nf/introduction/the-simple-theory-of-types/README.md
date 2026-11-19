# The simple theory of types

In 1937, Quine introduced *New Foundations* ($\mathsf{NF}$) ([Quine 1937](https://api.semanticscholar.org/CorpusID:123927264)), a set theory with a very small collection of axioms. To give a proper exposition of the theory that we intend to prove consistent, we will first make a digression to introduce the related theory $\mathsf{TST}$, as explained in ([Holmes and Wilshaw 2024](https://arxiv.org/abs/1503.01406)).

The *simple theory of types* (known as *théorie simple des types* or $\mathsf{TST}$) is a first order set theory with several sorts, indexed by the nonnegative integers. Each sort, called a *type*, is comprised of *sets* of that type; each variable ${\text{‘}x\text{’}}$ has a nonnegative integer $\operatorname{\mathsf{type}}({\text{‘}x\text{’}})$ which denotes the type it belongs to. For convenience, we may write $x^n$ to denote a variable $x$ with type $n$.

The primitive predicates of this theory are equality and membership. An equality ${\text{‘}x = y\text{’}}$ is a well-formed formula precisely when $\operatorname{\mathsf{type}}({\text{‘}x\text{’}}) = \operatorname{\mathsf{type}}({\text{‘}y\text{’}})$, and similarly a membership formula ${\text{‘}x \in y\text{’}}$ is well-formed precisely when $\operatorname{\mathsf{type}}({\text{‘}x\text{’}}) + 1 = \operatorname{\mathsf{type}}({\text{‘}y\text{’}})$.

The axioms of this theory are extensionality

$$
\forall x^{n + 1},\, \forall y^{n + 1},\, (\forall z^n,\, z^n \in x^{n+1} \leftrightarrow z^n \in y^{n+1}) \to x^{n+1} = y^{n+1}
$$

and comprehension

$$
\exists x^{n + 1},\, \forall y^n,\, (y^n \in x^{n+1} \leftrightarrow \varphi(y^n))
$$

where $\varphi$ is any well-formed formula, possibly with parameters.

Note that these are both axiom schemes, with instances for all type levels $n$, and (in the latter case) for all well-formed formulae $\varphi$. Because extensionality at level $n + 1$ requires us to talk about sets at level $n$, the inhabitants of type 0, called *individuals*, cannot be examined using these axioms.

By comprehension, there is a set at each nonzero type that contains all sets of the previous type. However, Russell-style paradoxes are avoided as formulae of the form $x^n \in x^n$ are ill-formed.
