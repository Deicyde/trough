# Some abstract nonsense

This is an alternate presentation of the material of the previous section, where we use the “abstract nonsense” of free magmas in the presence of a theory as the conceptual foundation.

- [Free magma relative to a theory](free-theory.md)

Such magmas exist and are unique up to a suitable isomorphism:

- [Existence and uniqueness of free magmas](freemag-exist.md)

We remark that the ordinary free magma $M_X$ corresponds to the case when $\Gamma$ is the empty theory.

*The proof of [Existence and uniqueness of free magmas](freemag-exist.md) is shown with its statement.*

**Example (Free associative magma).** Let $\Gamma$ consist solely of the associative law, [E4512](https://teorth.github.io/equational_theories/implications/?4512) (so $X$ contains $0,1,2$). Then one can take $M_{X,\Gamma}$ to be the set of nonempty strings with alphabet $X$, with magma operation given by concatenation, and $\iota_{X,\Gamma}(x)$ being the length one string $x$. It is a routine matter to verify that this satisfies the axioms of a free magma subject to $\Gamma$.

**Example (Free associative commutative magma).** Let $\Gamma$ consist of the associative law ([E4512](https://teorth.github.io/equational_theories/implications/?4512)) and the commutative law ([E43](https://teorth.github.io/equational_theories/implications/?43)). Then one can take $M_{X,\Gamma}$ to be the free abelian monoid $\mathbb{N}_0^X \backslash 0$ of tuples $(n_x)_{x \in X}$ with the $n_x$ natural numbers, not all zero, with all but finitely many of the $n_x$ vanishing, with the magma operation given by vector addition, and with $\iota_{X,\Gamma}(x)$ being the standard generator of $\mathbb{N}^X$ associated to $x \in X$; one can think of this space as the space of formal non-empty commuting associating sums of $X$. It is a routine matter to verify that this satisfies the axioms of a free magma subject to $\Gamma$.

**Example (Free left absorptive magma).** Let $\Gamma$ consist of the left absorptive law ([E4](https://teorth.github.io/equational_theories/implications/?4)). Then one can take $M_{X,\Gamma}$ to be $X$ with the law $x \diamond y = x$, and $\iota_{X,\Gamma}$ to be the identity map. It is easy to see that this is indeed a free magma subject to $\Gamma$.

**Example (Free constant magma).** Let $\Gamma$ consist of the constant law ([E46](https://teorth.github.io/equational_theories/implications/?46)). Then one can take $M_{X,\Gamma}$ to be the disjoint union $X \uplus \{0\}$ of $X$ and another object $0$, with $\iota_{X,\Gamma}$ being the identity embedding, and with the zero magma law $x \diamond y = 0$ for all $x,y \in X \uplus \{0\}$.

Free magmas can be used to characterize entailment by $\Gamma$ in terms of a canonical invariant.

Every theory $\Gamma$ then gives a metatheorem about anti-implication:

**Example.** Let $\Gamma$ be the associative and commutative law, so that we can take $M_{X,\Gamma} = \mathbb{N}_0^X \backslash 0$ as in Free associative commutative magma. One can then check that for any word $w \in M_X$, that $\varphi_{\iota_{X,\Gamma}}(w)$ is the tuple that assigns to each letter $x$ of the alphabet, the number of times $x$ appears in $w$. We conclude that if $w,w'$ have the same number of occurrences of each letter of the alphabet, but $w'', w'''$ do not, then $w \simeq w'$ cannot imply $w'' \simeq w'''$. This recovers [Criterion for implication](../general-implications/variable-impl.md).

**Example.** Let $\Gamma$ consist of the left absorption law, so we can take $M_{X,\Gamma} = X$ as in Free left absorptive magma. Then $\varphi_{\iota_{X,\Gamma}}(w)$ is the first letter of $w$. We conclude that if $w,w'$ have the same first letter, but $w'', w'''$ do not, then $w \simeq w'$ cannot imply $w'' \simeq w'''$.

**Example.** Let $\Gamma$ consist of the constant law, so we can take $M_{X,\Gamma} = X \uplus \{0\}$ as in Free constant magma. Then $\varphi_{\iota_{X,\Gamma}}(w)$ is $x$ if $w$ is just a letter $x$ of the alphabet, and $0$ otherwise. We conclude that if $w,w', w'''$ have order at least one, but $w''$ has order zero, then $w \simeq w'$ cannot imply $w'' \simeq w'''$; this is basically [Laws implied by the constant law](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/general_implications.tex#L88).

**Example.** Let $\Gamma$ be the theory consisting of the commutative and associative laws, and an additional law $x^n \simeq y^n$ for a fixed $n$, where $x^n$ denotes the magma operation applied to $n$ copies of $x$ (the order is irrelevant thanks to associativity), then one can check (for finite $X$) that the free magma $M_{X,\Gamma}$ can be taken to be $(\mathbb{Z}/n\mathbb{Z})^X$ with the addition operation, and $\iota_{X,\Gamma}(x)$ being the standard generator associated to $x$. Then for any word $w$, $\varphi_{\iota_{X,\Gamma}}(w)$ corresponds to a tuple that assigns to each letter $x$ of the alphabet, the number of times $x$ occurs in $w$ modulo $n$. We conclude that if $w,w'$ have the same number of occurrences modulo $n$ of each letter of the alphabet, but $w'', w'''$ do not, then $w \simeq w'$ cannot imply $w'' \simeq w'''$. This is a stronger version of [Criterion for implication](../general-implications/variable-impl.md).
