---
declaration: lemma
origin: cited
lean: Finset.exists_subset_addSpan_card_le_of_forall_addDissociated
statement: formalized
proof: formalized
---

# diss_span

If $A\subseteq G$ contains no dissociated set with $\geq K+1$ elements, then there is $A'\subseteq A$ of size $\left\lvert A'\right\rvert\le K$ such that

$$
A\subseteq \left\{ \sum_{a\in A'}c_aa : c_a\in \{-1,0,1\} \right\}.
$$

## Depends on

- [Dissociation](dissociated.md)

## Proof

Let $A'\subseteq A$ be a maximal dissociated subset (this exists and is non-empty, since trivially any singleton is dissociated). We have $\left\lvert A'\right\rvert\le K$ by assumption.

Let $S$ be the span on the right-hand side. It is obvious that $A'\subseteq S$. Suppose that $x\in A\backslash A'$. Then $A'\cup\{x\}$ is not dissociated by maximality. Therefore there exists some $y\in G$ and two distinct sets $B,C\subseteq A'\cup \{x\}$ such that

$$
\sum_{b\in B}b = y = \sum_{c\in C} c.
$$

If $x\not\in B$ and $x\not\in C$ then this contradicts the dissociativity of $A'$. If $x\in B$ and $x\in C$ then we have

$$
\sum_{b\in B\backslash x}b=y-x=\sum_{c\in C\backslash x}c,
$$

again contradicting the dissociativity of $A'$. Without loss of generality, therefore, $x\in B$ and $x\not\in C$. Therefore

$$
x=\sum_{c\in C}c - \sum_{b\in B\backslash x}b
$$

which is in the span as required.

## Lean

Formalized as [`Finset.exists_subset_addSpan_card_le_of_forall_addDissociated`](https://yaeldillies.github.io/apap/docs/find/#doc/Finset.exists_subset_addSpan_card_le_of_forall_addDissociated).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 188](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L188)
