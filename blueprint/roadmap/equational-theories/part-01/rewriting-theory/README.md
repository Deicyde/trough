# Rewriting theory

We briefly recall the basics of rewrite theory necessary to our exposition, following mostly Baader and Nipkow (Baader and Nipkow 1998), and generally omitting proofs when they can be found there.

We first work in the abstract taking an arbitrary set $A$, with a given equivalence relation over it which we denote $\approx$. We consider a relation $R$ over $A$.

- [Definition: We write $a \rightarrow b$ if $a\ R\ b$ holds…](definition-rewriting-1.md)

Note that $\leftrightarrow^*$ is an equivalence relation and the hope is for it to be equal to $\approx$, in order to deduce properties of the latter.

One should first note that if even $R$ is contained in $\approx$, then so are $\rightarrow^+, \rightarrow^*$ and $\leftrightarrow^*$ (as it is an equivalence relation), so we will focus on that case. Generally $a \rightarrow^* b$ can be seen as a way to *compute* the $\approx$ relation, as it is directed, in a way to constrain our search space.

However, in general, we cannot deduce the converse, so it may be the case that $a\approx b$ but neither $a\rightarrow^*b$ nor $b\rightarrow^*a$ nor even is there a single $c$ such that $a\rightarrow^* c\ {}^*\leftarrow b$, as the number of “left-right alternations” may be arbitrarily large.

The following properties are going to be very useful to deduce exactly such a converse.

- [Definition: We say that $R$ is Church-Rosser if whenever…](definition-rewriting-2.md)

It turns out that if $R$ is strongly normalizing and Church-Rosser, and effective (we can “compute” with it) then the problem of equivalence is decidable! This is because of the following lemma.

- [Lemma: If $R$ is Church-Rosser, then any normal…](lemma-rewriting-1.md)

This means that, in this situation, $a$ and $b$ reduce to an identical normal form $c$ *if and only if* $a\leftrightarrow^* b$! This means that we have the following algorithm to decide $a\leftrightarrow^* b$ (and therefore $a\approx b$ if these relations coincide):

1. Repeatedly apply $R$ to $a$ and $b$ until normal forms $a'$ and $b'$ are found for them (this is possible because $R$ is strongly normalizing).
2. Compare $a'$ and $b'$ for exact equality (sometimes called “syntactic equality”).
3. If $a' = b'$, we can conclude $a\leftrightarrow^* b$.
4. If $a' \neq b'$ can can conclude that they are *not* equivalent due to the lemma.

Note that weak normalization does not change much here except at step 1, where we need to pick reductions which eventually bring the elements to normal forms.

The strategy is therefore, for a given $\approx$ to find an $R$ which is (strongly) normalizing and Church-Rosser, and such that $\leftrightarrow^*\ =\ \approx$. This is roughly the goal of the entire field of *completion*. We call such an $R$ *complete for* $\approx$.

The task is helped by the following facts, which we state here also without proof.

- [Theorem: $R$ is Church-Rosser iff it is confluent.…](theorem-rewriting-1.md)

This can be leveraged by looking at the particulars of the equivalence relation of interest, namely quantified equations over syntactic trees as in [Some abstract nonsense](../some-abstract-nonsense/README.md), and a theory $\Gamma$, which we will usually take to be finite (usually it will have a single equation!).

We will therefore consider relations over the set of elements of the free magma $M_{X}$, and the aim is to find a rewrite system $R$ is complete for $\simeq$.

Certainly $\simeq$ is closed over substitutions, and be a *congruence*: if $a\simeq a'$ and $b\simeq b'$ under $\Gamma$, then $a\diamond b\simeq a'\diamond b'$ under $\Gamma$ as well.

We therefore consider $R$ to be both closed under substitutions and a congruence. A convenient way to represent this is via a *rewrite system*: simply a set of pairs of words $(l, r) \in M_{X}$ (we typically write $l\rightarrow r$) which represents the smallest congruence, closed by substitutions that contains those pairs.

Naturally, a set of laws $w \simeq w'$ can be seen, given a choice of orientation (left-to-right or right-to-left) for each law as such a rewrite system. In this case, it is very clear that the reflexive transitive closure $\leftrightarrow^*$ recovers the original equational theory $\Gamma\models \cdot\simeq\cdot$. However, it's clear that sometimes these systems will either be not strongly normalizing, or confluent, or both.

For example, it's clear that commutativity (the rule $x\cdot y\simeq y\cdot x$ cannot possibly be oriented. Here is a non-confluent example:

$$
x \cdot (y \cdot z) \rightarrow y
$$

We have $a\cdot (b \cdot (c \cdot d)) \rightarrow^* b$, but also $a\cdot (b\cdot (c\cdot d))\rightarrow^* a\cdot c$ for any $a, b, c, d$ (which are both in normal form).

Knuth and Bendix (Knuth and Bendix 1970) described a technique by which a theory or set of equations $\Gamma$ could be turned into a complete system. The crucial idea is the observation that the non-local-confluence of a rewrite system can be reduced to a finite (if the system is finite) set of “worst offenders” for confluence. If these pairs can be *joined* (reduced to the same term) then the system is confluent. It is possible to compute such pairs.

The high-level idea is therefore to identify such pairs, and add them as an unoriented equation, to be oriented if possible, and repeating until no un-joinable pairs exist. If this procedure succeeds and terminates, the system is successfully completed, and as a result the theory $\Gamma$ is decidable, via the completed system as described above.

We use the intuitive notions of “position in a word” and “word at a position $p$”. We denote by $w[w']_p$ the word $w$ with $w'$ inserted at position $p$.

- [Definition: Given a rewrite system $R$ and two rules…](definition-rewriting-3.md)

Note that, in the above setting, $t\leftarrow l_1\sigma\rightarrow u$, giving us a candidate for non-local-confluence. The next lemma states that these candidates are the most general ones.

- [Theorem: Given a rewrite system $R$, if for every…](theorem-rewriting-2.md)

Note that building critical pairs of a finite system is computable. Therefore the only step of the completion process which require genuine creativity is the choice of the orientation of the equations, along with the proof that the orientation is strongly normalizing.

As a capper to this section we can note that even in the event that such an orientation is not found, one can still partially apply the completion procedure, using any well-founded order on terms that is stable by substitution and congruence, to obtain a semi-decision procedure for equality. This process is sometimes called *unfailing completion* and is at the core of the *superposition calculus* used in Vampire.
