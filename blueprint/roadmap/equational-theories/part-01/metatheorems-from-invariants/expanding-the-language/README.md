# Expanding the language

The method of invariants really shines when we expand our formal language. Right now our language consists of variables, parentheses, the equal sign, and $\diamond$ (there is also an implicit use of $\forall$ but let's ignore that for now). Let $\Pi$ denote the preorder of equations (built from the language described) ordered by implication.

We will add the symbol $\wedge$ (‘and’) to our language. Then we consider a bigger preorder $\Pi' \supseteq \Pi$ which includes equations and also conjunctions of equations. Even if we only care about $\Pi$ it will be apparent that studying invariants in $\Pi'$ gives us useful metatheorems about $\Pi$. Equations and conjunctions of equations are examples of *formulas* (or formulae, according to taste).

If $\varphi$ is a formula, we can define $\mathcal{Y}(\varphi)$ to be the set of all formulae implied by $\varphi$; this agrees with our previous definition. Now define an invariant of $\varphi$ to be a function $I$ on terms such that

$$
\mathcal{Y}(\varphi) \cap \Pi = \{w = w' \mid I(w) = I(w')\}.
$$

Again, this clearly agrees with our previous definition. Although $\mathcal{Y}(\varphi) \cap \Pi$ might not be upwards closed in $\Pi'$, it is upwards closed in $\Pi$, which is enough to get the fundamental property of invariants *verbatim*. This leads to more metatheorems we didn't have access to before.

### Example: associativity and idempotency

Let $\varphi$ be the conjunction of the associative law and the idempotency law ($x \diamond x = x$). Again, we will rely on our intuition, which says that an invariant $I$ defined by taking $I(w)$ to be the set of all variables appearing in $w$, works. The corresponding metatheorem is the following

**Metatheorem.** Let $w = w'$ be an equation such that the set of variables appearing in $w$ is equal to the set of variables appearing on $w'$. Then $w = w'$ cannot imply an equation that does not have the property from the last sentence.

### Example: associativity and commutativity

For a similar example, we can let $\varphi$ be the conjunction of the associative and the commutative laws. Here we can define $I(w)$ to be the [multiset](https://en.wikipedia.org/wiki/Multiset) of variables appearing in $w$. We obtain the following metatheorem.

**Metatheorem.** Let $w = w'$ be an equation such that the variables appearing in $w$, taking into account multiplicity, are the same ones that appear in $w'$. Then $w = w'$ cannot imply an equation that does not have the property from the last sentence.

Trivia: this was the first example of a metatheorem obtained by use of an invariant.

### Example: associativity and commutativity with a twist

We can keep expanding our language if it helps us express more intricate invariants. For instance, we can add the symbol ‘1’ to our language. Let $\varphi$ be the conjunction of associativity, commutativity, the equations $1 \diamond x = x$, and

$$
\underbrace{x \diamond x \diamond \cdots \diamond x}_{m\text{ times}} = 1,
$$

for some fixed positive integer $m$. Pause to guess the invariant before we move on.

The invariant $I(w)$ is the multiset of variables appearing in $w$ but multiplicities are computed modulo $m$. Thus we have the pretty metatheorem:

**Metatheorem.** Fix some positive integer $m$. Let $w = w'$ be an equation such that every variable appearing in $w$ appears the same number of times in $w'$ modulo $m$. Then $w = w'$ cannot imply an equation that does not have the property from the last sentence.
