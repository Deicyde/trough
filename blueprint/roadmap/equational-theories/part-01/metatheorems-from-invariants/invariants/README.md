# Invariants

Let $E, E_1$, and $E_2$ be equations. If $E \Rightarrow E_1$ and $E_1 \Rightarrow E_2$, then $E \Rightarrow E_2$. Very trivial. Rephrasing this, we see that if $E \Rightarrow E_1$ and $E \nRightarrow E_2$, then $E_1\nRightarrow E_2$.

Extending this idea, suppose we compute the set of all equations which are implied by $E$; we will call this set $\mathcal{Y}(E)$ (we use $\mathcal{Y}$ because this is an example of a [Yoneda embedding](https://en.wikipedia.org/wiki/Yoneda_lemma#The_Yoneda_embedding)). Then $\mathcal{Y}(E)$ is upwards closed, or closed under forward implication: no equation in $\mathcal{Y}(E)$ can imply an equation not in $\mathcal{Y}(E)$. If we know $\mathcal{Y}(E)$ well, this already settles a potentially large number of implications in the negative.

While computing $\mathcal{Y}(E)$ for an arbitrary equation $E$ may seem daunting, for some nice equations we can find *invariants*, which makes the task manageable. An *invariant* for $E$ is some sort of data associated with expressions $w$ so that

$$
\mathcal{Y}(E) = \{w = w' \mid \text{Invariant}(w) = \text{Invariant}(w')\}
$$

If we can find an invariant which is computable for each term $w$, then we can easily describe $\mathcal{Y}(E)$. The fact that $\mathcal{Y}(E)$ is upwards closed is rephrased as follows; this is called **the fundamental property of invariants**. Remember that an invariant is a function taking expressions and outputting some data.

**Meta-metatheorem (Fundamental property of invariants).** Let $I$ be an invariant of $E$. If $w = w'$ implies $w'' = w'''$ and $I(w) = I(w')$ (that is, $E$ implies $w = w'$), then $I(w'') = I(w''')$.

*Proof.* Let $\Pi$ denote the preorder of magma equations ordered by implication. If $I$ is an invariant then define

$$
I(w = w')\coloneqq \begin{cases}
\texttt{true} & \text{ if }I(w) = I(w')\\
\texttt{false} & \text{ otherwise}
\end{cases}.
$$

(In programming languages we would say $I(w = w') \coloneqq I(w) == I(w')$). Let $\textbf{Bool} = \{ \texttt{true}, \texttt{false}\}$ be the poset where $\texttt{false} \leq \texttt{true}$. Then $I$ becomes a function $\Pi \to \textbf{Bool}$, and the fundamental property of invariants just says that this function is monotone, i.e. functorial. Thus for every invariant $I$ we obtain a functor $\Pi \to \textbf{Bool}$.

Question 1: Does every functor $\Pi \to \textbf{Bool}$ come from an invariant?

Question 2: What can we say about the category of functors $\Pi \to \textbf{Bool}$? Give a nice interpretation of natural transformations between invariants.

More succinctly, for an invariant $I$ of $E$ we must have

$$
(w = w' \Rightarrow w'' = w''') \implies (I(w) = I(w') \Rightarrow I(w'') = I(w''')).
$$

When using this result, we commonly take the contrapositive: if $I(w) = I(w')$ and $I(w'') \neq I(w''')$, then $w=w'$ cannot imply $w'' = w'''$. Note that the conclusion is independent of the equation $E$; all we need to know is that $I$ is an invariant.

The fundamental property of invariants is not a theorem, nor a metatheorem: it is a meta-metatheorem, in the sense that it will allow us to get a metatheorem for every invariant we find.

### Example: absorption law

Let $E$ be the equation $x \diamond y = x$. Intuitively, we must have

$$
\mathcal{Y}(E) = \{w = w' \mid \text{the leftmost variable is the same for $w$ and $w'$}\}.
$$

We will talk about proving statements like this one (say in Lean) later on; take it as given for now. The invariant is clear: we define $I(w)$ to be the leftmost variable of $w$. Instantiating this invariant in the fundamental property of invariants, we get the following metatheorem.

**Metatheorem.** Let $w = w'$ be an equation such that the leftmost variable of $w$ is the same as the leftmost variable of $w'$. Then $w = w'$ cannot imply an equation that does not have the property from the last sentence.

### Example: associativity

For a more complicated example, let $E$ be the associativity equation $x \diamond (y \diamond z) = (x \diamond y) \diamond z$. Intuitively, we must have

$$
\mathcal{Y}(E) = \{\text{equations that, when we remove all parentheses, are of the form $w = w$}\}.
$$

There is an invariant lurking behind: it is the (ordered) list of variables appearing in an expression, counting repetitions. More formally, we define $I(w)$ to be the tuple of variables appearing in $w$, listed from left to right, say. Again, from the fundamental property of invariants we get the following.

**Metatheorem.** Let $w = w'$ be an equation such that the variables appearing in $w$, taking into account order and repetitions, are the same ones that appear in $w'$. Then $w = w'$ cannot imply an equation that does not have the property from the last sentence.

If we were coding a computer program that computes $I(w)$ given $w$, one could take the string of symbols that is $w$, ignore all parentheses, replace all symbols $\diamond$ by commas, and surround with an appropriate delimiter. (I imagine one could easily do this using [regular expressions](https://en.wikipedia.org/wiki/Regular_expression).)

We can compute other examples, but the invariant can get complicated even for simple equations. Exercise: what is the invariant for commutativity? Answer: To compute $I(w)$ from $w$ replace all parentheses with curly braces and all symbols $\diamond$ with commas, and interpret the result as nested sets.
