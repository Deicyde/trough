---
declaration: section
origin: cited
lean: MetaMathlibExt.nearHookTheta, MetaMathlibExt.nearHookTheta_rowLens, MetaMathlibExt.firstQuadrantPaths, MetaMathlibExt.north_south_mem_firstQuadrantPaths_zero, MetaMathlibExt.nearHookTableauToPathPsi, MetaMathlibExt.length_nearHookTableauToPathPsi, MetaMathlibExt.nearHookTableauToPathXi, MetaMathlibExt.length_nearHookTableauToPathXi
statement: formalized
---

# Near-hook tableaux and first-quadrant lattice paths

10 results, 8 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html).

## The near-hook diagram $\theta^{(n)}$

For $n \in \mathbb{N}$, $\theta^{(n)}$ is the Young
diagram of the near-hook partition $(n + 2, 2, 1^n)$ of $2n + 4$: its rows have lengths $n + 2$
and $2$, followed by $n$ rows of length $1$.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 2.

Formalized by `MetaMathlibExt.nearHookTheta`, a definition declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#near-hook-theta).

## Row lengths of $\theta^{(n)}$

For every $n \in \mathbb{N}$, the row lengths of the Young
diagram $\theta^{(n)}$, from the top row down, are $n + 2$, $2$, and then $1$ repeated $n$ times.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 2.

Formalized by `MetaMathlibExt.nearHookTheta_rowLens`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#near-hook-theta-row-lens).

## First-quadrant paths $\mathcal{P}_n$

For $n \in \mathbb{N}$, $\mathcal{P}_n$ is the set of
words $(s_1, \dots, s_{2n+2})$ of $2n + 2$ steps, each one of $N = (0, 1)$, $S = (0, -1)$,
$E = (1, 0)$ and $W = (-1, 0)$ in $\mathbb{Z}^2$, such that every partial sum $s_1 + \dots + s_k$
with $0 \le k \le 2n + 2$ has both coordinates nonnegative and the total $s_1 + \dots + s_{2n+2}$
equals $(n, n)$.

These are the walks of Guy, Krattenthaler and Sagan.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 1.

Formalized by `MetaMathlibExt.firstQuadrantPaths`, a definition declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#first-quadrant-paths).

## The path $NS$ lies in $\mathcal{P}_0$

The two-step word consisting of a north step
$(0, 1)$ followed by a south step $(0, -1)$ belongs to the set $\mathcal{P}_0$ of first-quadrant
paths.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 1.

Formalized by `MetaMathlibExt.north_south_mem_firstQuadrantPaths_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#north-south-mem-first-quadrant-paths-zer).

## The map $\psi$ from near-hook tableaux to lattice paths

Let $n \in \mathbb{N}$ and let
$T$ be a semistandard Young tableau of shape $\theta^{(n)}$, with rows and columns numbered from
$0$; call row $0$ of $\theta^{(n)}$ the arm and column $0$ the leg. Then $\psi(T)$ is the word
$(s_1, \dots, s_{2n+2})$ of steps in $\mathbb{Z}^2$ in which $s_i$ is $E = (1, 0)$ if $i + 2$ is an
entry of $T$ in the arm; otherwise $s_i$ is $N = (0, 1)$ if $i + 2$ is an entry of $T$ in the leg;
otherwise $s_i$ is $S = (0, -1)$ if $2$ is an entry of $T$ in the arm, and $W = (-1, 0)$ if not.

For a standard Young tableau, the last two cases are those where $i + 2$ is the entry of the
heart, the cell in row $1$ and column $1$, and $2$ is then an entry of the arm or of the leg.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 3, equation (eq:psi).

Formalized by `MetaMathlibExt.nearHookTableauToPathPsi`, a definition declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#near-hook-tableau-to-path-psi).

## The path $\psi(T)$ has $2n + 2$ steps

For every $n \in \mathbb{N}$ and every
semistandard Young tableau $T$ of shape $\theta^{(n)}$, the word $\psi(T)$ has length $2n + 2$.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 3, equation (eq:psi).

Formalized by `MetaMathlibExt.length_nearHookTableauToPathPsi`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#length-near-hook-tableau-to-path-psi).

## The map $\xi$ from near-hook tableaux to lattice paths

Let $n \in \mathbb{N}$ and let
$T$ be a semistandard Young tableau of shape $\theta^{(n)}$, with rows and columns numbered from
$0$; call row $0$ of $\theta^{(n)}$ the arm and the cell in row $1$ and column $1$ the heart, and
let $H$ be the entry of $T$ in the heart. Then $\xi(T)$ is the word $(s_1, \dots, s_{2n+2})$ of
steps in $\mathbb{Z}^2$ given as follows, where $E = (1, 0)$, $N = (0, 1)$, $S = (0, -1)$ and
$W = (-1, 0)$. If $i + 2 < H$, then $s_i$ is $E$ if $i + 1$ is an entry of $T$ in the arm and
$N$ otherwise. If $i + 2 = H$, then $s_i$ is $S$ if $i + 1$ is an entry of $T$ in the arm and
$W$ otherwise. If $i + 2 > H$, then $s_i$ is $E$ if $i + 2$ is an entry of $T$ in the arm and
$N$ otherwise.

For a standard Young tableau the inspected value is never $1$ or $H$, so it lies in exactly one
of the arm and the leg, column $0$; "otherwise" then means that it lies in the leg.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 4.1, equation (eq:xi).

Formalized by `MetaMathlibExt.nearHookTableauToPathXi`, a definition declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#near-hook-tableau-to-path-xi).

## The path $\xi(T)$ has $2n + 2$ steps

For every $n \in \mathbb{N}$ and every
semistandard Young tableau $T$ of shape $\theta^{(n)}$, the word $\xi(T)$ has length $2n + 2$.

## Sources

- L. Ayres et al., *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Section 4.1, equation (eq:xi).

Formalized by `MetaMathlibExt.length_nearHookTableauToPathXi`, a theorem declared in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#length-near-hook-tableau-to-path-xi).

## The map $\psi$ is a bijection from near-hook tableaux to first-quadrant paths

For every
$n \in \mathbb{N}$, the map $\psi$ restricts to a bijection from the standard Young tableaux of
shape $\theta^{(n)}$ onto the set $\mathcal{P}_n$ of first-quadrant paths. Here a standard Young
tableau of shape $\theta^{(n)}$ is a semistandard Young tableau of that shape whose entries map
the $2n + 4$ cells of $\theta^{(n)}$ bijectively onto $\{1, \dots, 2n + 4\}$.

## Sources

- Liam Ayres, Evan Bialo, Alwin Chen, Aidan Cook, Matteus Froese, Erica Liu, Maryam Mohammadi Yekta, Oliver Pechenik and Benjamin Wong, *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Theorem 2 (`jis-2025-25.5.2-thm-2`).

Stated but not proved: `MetaMathlibExt.bijOn_nearHookTableauToPathPsi` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#bij-on-near-hook-tableau-to-path-psi).

## The map $\xi$ is a bijection from near-hook tableaux to first-quadrant paths

For every
$n \in \mathbb{N}$, the map $\xi$ restricts to a bijection from the standard Young tableaux of
shape $\theta^{(n)}$ onto the set $\mathcal{P}_n$ of first-quadrant paths. Here a standard Young
tableau of shape $\theta^{(n)}$ is a semistandard Young tableau of that shape whose entries map
the $2n + 4$ cells of $\theta^{(n)}$ bijectively onto $\{1, \dots, 2n + 4\}$.

## Sources

- Liam Ayres, Evan Bialo, Alwin Chen, Aidan Cook, Matteus Froese, Erica Liu, Maryam Mohammadi Yekta, Oliver Pechenik and Benjamin Wong, *An Exceptional Equinumerosity of Lattice Paths and Young Tableaux*, Journal of Integer Sequences 28 (2025), Article 25.5.2, Proposition 3 (`jis-2025-25.5.2-prop-3`).

Stated but not proved: `MetaMathlibExt.bijOn_nearHookTableauToPathXi` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/NearHookTableauxLatticePathsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html#bij-on-near-hook-tableau-to-path-xi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Near-hook tableaux and first-quadrant lattice paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/near-hook-tableaux-and-first-quadrant-lattice-pa)
