# Translation-invariant magmas

A *translation-invariant magma* is a magma whose carrier $G$ is an abelian group $(G,+,-,0)$, and whose magma operation takes the form

$$
y \diamond x = x + f(x-y)
$$

for some function $f: G \to G$. Thus the translations on $G$ become magma isomorphisms.

**Example.** A magma $G$ satisfying the left ([E4](https://teorth.github.io/equational_theories/implications/?4)) or right ([E5](https://teorth.github.io/equational_theories/implications/?5)) absorption laws is translation-invariant. Equip the carrier $G$ with an abelian group structure $(G,+,-,0)$ and define $f: G \to G$ as either $f(x) = -x$ or $f(x) = 0$.

**Example.** Linear magmas $x\diamond y = ax+by$ on a field $(\mathbb{F},+,-,\cdot,0,1)$ are translation-invariant if $a + b = 1$, since $(\mathbb{F},+,-,0)$ forms an abelian group, and one can set $f(x) = -ax$.

Note that if an example of the latter sort suffices to refute the implication between $P$ and $Q$ then by the Lefschetz principle one can construct a counterexample where the field $\mathbb{F}$ is finite. Consequently, $P$ and $Q$ cannot constitute an Austin pair. However, these linear magmas can still serve as starting points for the *modified translation-invariant* models studied in [A survey of examples](../a-survey-of-examples/README.md).
