---
declaration: theorem
origin: cited
lean: MIPRE.Repetition.tracialDensity
statement: formalized
proof: formalized
---

# Lin's tracial density theorem

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] Let ${\mathcal{X}}$ and ${\mathcal{A}}$ be finite nonempty sets. Call a correlation $q(a, b \mid x, y)$ on question alphabets ${\mathcal{X}}, {\mathcal{X}}$ and answer alphabets ${\mathcal{A}}, {\mathcal{A}}$ *tracially embeddable* if there are: a unital $*$-algebra ${\mathscr{A}}$ over $\mathbb{C}$ with a tracial state $\tau$ ($\tau(1) = 1$, $\tau(ab) = \tau(ba)$, $\tau(a^*) = \overline{\tau(a)}$); a Hilbert space $\mathcal{H}$ with a linear map $\iota : {\mathscr{A}} \to \mathcal{H}$ of dense range satisfying $\langle \iota a, \iota b \rangle = \tau(a^* b)$, on which ${\mathscr{A}}$ acts on the left by bounded operators $L(a)$ with $L(a)\, \iota b = \iota(ab)$; a positive element $\sigma \in {\mathscr{A}}$ with $\tau(\sigma^* \sigma) = 1$; POVMs $\{E^x_a\}_{a} \subseteq {\mathscr{A}}$ of positive elements summing to $1$; and POVMs $\{G^y_b\}_{b}$ of positive bounded operators on $\mathcal{H}$ summing to ${I}$ and commuting with $L({\mathscr{A}})$, such that

$$
q(a, b \mid x, y) = \bigl\langle \iota\sigma,\ L(E^x_a)\, G^y_b\, \iota\sigma \bigr\rangle\;.
$$

Then every commuting-operator correlation $p(a, b \mid x, y) = \langle\psi| E^x_a F^y_b |\psi\rangle$ on these alphabets (Definition [Commuting-operator strategy](def-co-strategy-bipartite.md)) is an $\ell^1$-limit of tracially embeddable correlations: for every $\delta > 0$ there is a tracially embeddable $q$ with $\sum_{x, y, a, b} \left\vert {p(a, b \mid x, y) - q(a, b \mid x, y)} \right\vert < \delta$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is Theorem 3.2 of (Lin23), as formalized in (Vid26) (the density programme of the vendored development, `Tracial/Density/Main.lean`). The statement above is that of the vendored development, in its own vocabulary — its tracially embeddable correlations have the shape of Lin's Definition 3.1, with Bob's measurement taken in the commutant of the left action; restating it through the definitions of Section [Foundations](../foundations/README.md) is pending.

## Lean

Formalized as [`MIPRE.Repetition.tracialDensity`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.tracialDensity).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 298](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L298)
