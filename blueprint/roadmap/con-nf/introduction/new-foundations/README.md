# New Foundations

New Foundations is a one-sorted first-order theory based on $\mathsf{TST}$. Its primitive propositions are equality and membership. There are no well-formedness constraints on these primitive propositions.

Its axioms are precisely the axioms of $\mathsf{TST}$ with all type annotations erased. That is, it has an axiom of extensionality

$$
\forall x,\, \forall y,\, (\forall z,\, z \in x \leftrightarrow z \in y) \to x = y
$$

and an axiom scheme of comprehension

$$
\exists x,\, \forall y,\, (y \in x \leftrightarrow \varphi(y))
$$

the latter of which is defined for those formulae $\varphi$ that can be obtained by erasing the type annotations of a well-formed formula of $\mathsf{TST}$. Such formulae are called *stratified*. To avoid the explicit dependence on $\mathsf{TST}$, we can equivalently characterise the stratified formulae as follows. A formula $\varphi$ is said to be stratified when there is a function $\sigma$ from the set of variables to the nonnegative integers, in such a way that for each subformula ${\text{‘}x = y\text{’}}$ of $\varphi$ we have $\sigma({\text{‘}x\text{’}}) = \sigma({\text{‘}y\text{’}})$, and for each subformula ${\text{‘}x \in y\text{’}}$ we have $\sigma({\text{‘}x\text{’}}) + 1 = \sigma({\text{‘}y\text{’}})$.

It is important to emphasise that while the axioms come from a many-sorted theory, $\mathsf{NF}$ is not one; it is well-formed to ask if any set is a member of, or equal to, any other.

Russell's paradox is avoided because the set $\{ x \mid x \notin x \}$ cannot be formed; indeed, $x \notin x$ is an unstratified formula. Note, however, that the set $\{ x \mid x = x \}$ is well-formed, and so we have a universal set $V$. Specker showed in ([Specker 1953](http://www.jstor.org/stable/88561)) that $\mathsf{NF}$ disproves the Axiom of Choice, and Hailperin showed in ([Hailperin 1944](https://doi.org/10.2307/2267307)) that $\mathsf{NF}$ is finitely axiomatisable.

While our main result is that New Foundations is consistent, we attack the problem by means of an indirection through a third theory.
