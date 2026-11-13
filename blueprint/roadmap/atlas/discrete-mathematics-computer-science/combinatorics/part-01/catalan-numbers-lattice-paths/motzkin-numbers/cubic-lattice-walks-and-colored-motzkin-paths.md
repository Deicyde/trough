---
declaration: section
origin: cited
lean: MetaMathlibExt.cube_lattice_paths_card_eq_uldMotzkinNumber, MetaMathlibExt.cube_lattice_paths_card_eq_colored_motzkin_card
statement: formalized
proof: formalized
---

# Cubic lattice walks and colored Motzkin paths

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/cubic-lattice-walks-and-colored-motzkin-paths/index.html).

## Cubic lattice walks counted by a colored Motzkin number

Let $n$ and $k$ be natural numbers,
and let $e_0, \dots, e_n$ be the standard basis vectors of $\mathbb{Z}^{n+1}$. The number of walks
of $k$ steps in the cubic lattice $\mathbb{Z}^{n+1}$ that start at the origin, each step being
$+e_i$ or $-e_i$ for some $i \in \{0, \dots, n\}$, such that, counting only the steps in the last
coordinate $i = n$, every initial segment has at least as many $+e_n$ steps as $-e_n$ steps and
the whole walk has equally many, equals the $(u,l,d)$-Motzkin number of rank $1$ with
$u = d = 1$ and $l = 2n$ at length $k$, that is, the number of Motzkin paths of length $k$ with
one color of up step, $2n$ colors of level step and one color of down step.

## Sources

- Rigoberto Flórez, Leandro Junes, and José L. Ramírez, "Further Results on Paths in an n-Dimensional Cubic Lattice," Journal of Integer Sequences 21 (2018), Article 18.1.2, Theorem, lines 924–926, https://cs.uwaterloo.ca/journals/JIS/VOL21/Florez/florez4.tex

Formalized by `MetaMathlibExt.cube_lattice_paths_card_eq_uldMotzkinNumber`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CubicLatticeColoredMotzkin.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CubicLatticeColoredMotzkin.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/cubic-lattice-walks-and-colored-motzkin-paths/index.html#cube-lattice-paths-card-eq-uld-motzkin-n).

## Cubic lattice walks and colored Motzkin paths

Let $n$ and $k$ be natural numbers, and let
$e_0, \dots, e_n$ be the standard basis vectors of $\mathbb{Z}^{n+1}$. Count the walks of $k$
steps in the cubic lattice $\mathbb{Z}^{n+1}$ that start at the origin, in which each step is
$+e_i$ or $-e_i$ for some $i \in \{0, \dots, n\}$ and, counting only the steps in the last
coordinate $i = n$, every initial segment has at least as many $+e_n$ steps as $-e_n$ steps and
the whole walk has equally many. Their number equals the number of words of length $k$ in the
letters $U$, $D$ and $L_1, \dots, L_{2n}$ in which every initial segment has at least as many
letters $U$ as letters $D$ and the whole word has equally many, that is, the number of Motzkin
paths of length $k$ with one color of up step, one color of down step and $2n$ colors of level
step.

In the source's notation this is the theorem in dimension $n + 1$: only the last coordinate is
constrained, and the $2n$ steps $\pm e_i$ with $i < n$ correspond to the $2n$ level-step colors.

## Sources

- Rigoberto Flórez, Leandro Junes, and José L. Ramírez, "Further Results on Paths in an n-Dimensional Cubic Lattice," Journal of Integer Sequences 21 (2018), Article 18.1.2, Theorem, lines 924–926, https://cs.uwaterloo.ca/journals/JIS/VOL21/Florez/florez4.tex

Formalized by `MetaMathlibExt.cube_lattice_paths_card_eq_colored_motzkin_card`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/CubicLatticeColoredMotzkin.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/CubicLatticeColoredMotzkin.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/cubic-lattice-walks-and-colored-motzkin-paths/index.html#cube-lattice-paths-card-eq-colored-motzk).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cubic lattice walks and colored Motzkin paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/cubic-lattice-walks-and-colored-motzkin-paths/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/cubic-lattice-walks-and-colored-motzkin-paths)
