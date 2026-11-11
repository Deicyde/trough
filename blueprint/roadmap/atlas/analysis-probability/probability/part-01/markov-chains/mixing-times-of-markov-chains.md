---
declaration: section
origin: cited
lean: MathlibExt.Probability.MarkovMixing.Torus, MathlibExt.Probability.MarkovMixing.stepUp, MathlibExt.Probability.MarkovMixing.sgn, MathlibExt.Probability.MarkovMixing.tvDist, MathlibExt.Probability.MarkovMixing.tvRow, MathlibExt.Probability.MarkovMixing.IsMixedAt, MathlibExt.Probability.MarkovMixing.monoEdges, MathlibExt.Probability.MarkovMixing.HasCutoff
statement: formalized
proof: formalized
---

# Mixing times of Markov chains

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html).

## Discrete torus

For natural numbers $d$ and $n$, the vertices of the discrete torus
$\mathbb{Z}_n^d$ are the functions from $\{0, \dots, d-1\}$ to $\{0, \dots, n-1\}$, that is, the
$d$-tuples of residues modulo $n$.

Formalized by `MathlibExt.Probability.MarkovMixing.Torus`, an abbreviation declared in [MathlibExt/Probability/MarkovMixing.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#torus).

## Coordinate step on the discrete torus

For a vertex $x$ of the discrete torus
$\mathbb{Z}_n^d$ and a coordinate $k \in \{0, \dots, d-1\}$, the neighbour $x + e_k$ is obtained
from $x$ by replacing its $k$-th coordinate $x_k$ by $(x_k + 1) \bmod n$ and leaving the other
coordinates unchanged.

Formalized by `MathlibExt.Probability.MarkovMixing.stepUp`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#step-up).

## Sign of a Boolean spin

The sign of a Boolean spin is the real number $+1$ if the spin
is true and $-1$ if it is false.

Formalized by `MathlibExt.Probability.MarkovMixing.sgn`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#sgn).

## Total variation distance of functions on a finite set

For real-valued functions $\mu$
and $\nu$ on a finite set $S$, their total variation distance is
$\frac{1}{2} \sum_{y \in S} |\mu(y) - \nu(y)|$.

Formalized by `MathlibExt.Probability.MarkovMixing.tvDist`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#tv-dist).

## Total variation distance of a matrix row from a function

For a real $S \times S$ matrix
$Q$ indexed by a finite set $S$, a function $\pi : S \to \mathbb{R}$ and $x \in S$, this is the
total variation distance $\frac{1}{2} \sum_{y \in S} |Q(x, y) - \pi(y)|$ of the row $x$ of $Q$
from $\pi$.

Formalized by `MathlibExt.Probability.MarkovMixing.tvRow`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#tv-row).

## Being $1/4$-mixed at a given time

Let $S$ be a finite set, $P$ a real $S \times S$
matrix and $\pi : S \to \mathbb{R}$. Then $P$ is mixed at time $t \in \mathbb{N}$ with respect to
$\pi$ if for every $x \in S$ the total variation distance
$\frac{1}{2} \sum_{y \in S} |P^t(x, y) - \pi(y)|$ between the row $x$ of the matrix power $P^t$
and $\pi$ is at most $1/4$.

The mixing time is the least $t$ at which $P$ is mixed.

Formalized by `MathlibExt.Probability.MarkovMixing.IsMixedAt`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#is-mixed-at).

## Number of monochromatic edges

For a simple graph $G$ on the vertex set
$\{0, \dots, n-1\}$ and a colouring $\sigma$ of its vertices with colours in
$\{0, \dots, q-1\}$, this is the number of edges $uv$ of $G$ with $\sigma_u = \sigma_v$, as a real
number, each edge counted once.

Formalized by `MathlibExt.Probability.MarkovMixing.monoEdges`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#mono-edges).

## Cutoff for a family of distance profiles

A family of real numbers $d_n(t)$, indexed by
$n \in \mathbb{N}$ and times $t \in \mathbb{N}$, exhibits cutoff if there are real numbers $t_n$
with $t_n \to \infty$ such that for every $\eta$ with $0 < \eta < 1$, as $n \to \infty$,
$d_n(\lceil (1+\eta) t_n \rceil) \to 0$ and $d_n(\lfloor (1-\eta) t_n \rfloor) \to 1$. Here the
ceiling and floor are taken in $\mathbb{N}$, so a negative argument gives $0$.

Formalized by `MathlibExt.Probability.MarkovMixing.HasCutoff`, a definition declared in [MathlibExt/Probability/MarkovMixing.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/MarkovMixing.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html#has-cutoff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mixing times of Markov chains](https://deicyde.github.io/atlas-lean/roadmap/Probability/markov-chains/mixing-times-of-markov-chains/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/markov-chains/mixing-times-of-markov-chains)
