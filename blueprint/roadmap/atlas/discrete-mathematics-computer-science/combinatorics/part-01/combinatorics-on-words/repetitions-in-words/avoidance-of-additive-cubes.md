---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.Letter, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.substitution, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.substitutionIterate, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.IsGeneratedFixedPoint, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.letterValue, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.factorSum, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.AvoidsPVHHCubes, MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.conjecture
statement: formalized
---

# Avoidance of additive cubes

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html).

## The alphabet $\{0, 1, 3, 4\}$

The alphabet with four distinct letters, written $0$, $1$,
$3$ and $4$.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.Letter`, an inductive type declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 17](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L17). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#letter).

## The substitution $0 \mapsto 03$, $1 \mapsto 43$, $3 \mapsto 1$, $4 \mapsto 01$

The map
sending each letter of the alphabet $\{0, 1, 3, 4\}$ to a word: $0$ to $03$, $1$ to $43$, $3$ to
$1$ and $4$ to $01$.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.substitution`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#substitution).

## Iterates of the substitution on $0$

For $k \ge 0$, the word $\sigma^k(0)$ obtained from
the one-letter word $0$ by applying the substitution $\sigma$ ($0 \mapsto 03$, $1 \mapsto 43$,
$3 \mapsto 1$, $4 \mapsto 01$) $k$ times, where $\sigma$ acts on a word by replacing each letter
with its image: $\sigma^0(0) = 0$ and $\sigma^{k+1}(0) = \sigma(\sigma^k(0))$.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.substitutionIterate`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#substitution-iterate).

## The fixed point generated from $0$

Let $\sigma$ be the substitution $0 \mapsto 03$,
$1 \mapsto 43$, $3 \mapsto 1$, $4 \mapsto 01$ on the alphabet $\{0, 1, 3, 4\}$, extended to words
by replacing each letter with its image. An infinite word $w = w_0 w_1 w_2 \cdots$ over
$\{0, 1, 3, 4\}$ is the fixed point generated from $0$ if the word $\sigma^k(0)$ is a prefix of $w$
for every $k \ge 0$.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.IsGeneratedFixedPoint`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#is-generated-fixed-point).

## Value of a letter

Each letter of the alphabet $\{0, 1, 3, 4\}$ has as its value the
integer it names: the letters $0$, $1$, $3$ and $4$ have values $0$, $1$, $3$ and $4$.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.letterValue`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#letter-value).

## Sum of a factor

For an infinite word $w = w_0 w_1 w_2 \cdots$ over the alphabet
$\{0, 1, 3, 4\}$ and natural numbers $s$ and $\ell$, the sum of the factor of length $\ell$
starting at position $s$ is the integer $\sum_{i=0}^{\ell-1} w_{s+i}$, where each letter counts
as its value.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.factorSum`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#factor-sum).

## Avoiding additive cubes

An infinite word $w = w_0 w_1 w_2 \cdots$ over the alphabet
$\{0, 1, 3, 4\}$ avoids PVHH-cubes (additive cubes) if there are no natural numbers $s$ and
$\ell \ge 1$ such that the three consecutive factors $w_s \cdots w_{s+\ell-1}$,
$w_{s+\ell} \cdots w_{s+2\ell-1}$ and $w_{s+2\ell} \cdots w_{s+3\ell-1}$ of length $\ell$ all have
the same sum of letter values.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.AvoidsPVHHCubes`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#avoids-pvhhcubes).

## Additive-cube-free fixed point conjecture

Let $\sigma$ be the substitution
$0 \mapsto 03$, $1 \mapsto 43$, $3 \mapsto 1$, $4 \mapsto 01$ on the alphabet $\{0, 1, 3, 4\}$,
extended to words by replacing each letter with its image. The proposition that there is an
infinite word $w$ over $\{0, 1, 3, 4\}$ such that $\sigma^k(0)$ is a prefix of $w$ for every
$k \ge 0$ and $w$ avoids PVHH-cubes (additive cubes): no three consecutive nonempty factors of $w$
of equal length have equal sums of letter values.

Formalized by `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#conjecture).

## The Cassaigne–Currie–Schaeffer–Shallit word avoids additive cubes

Let $\sigma$ be the
substitution $0 \mapsto 03$, $1 \mapsto 43$, $3 \mapsto 1$, $4 \mapsto 01$ on the alphabet
$\{0, 1, 3, 4\}$, extended to words by replacing each letter with its image. There is an infinite
word $w = w_0 w_1 w_2 \cdots$ over $\{0, 1, 3, 4\}$ such that $\sigma^k(0)$ is a prefix of $w$ for
every $k \ge 0$, and $w$ contains no additive cube: there are no natural numbers $s$ and
$\ell \ge 1$ such that the three consecutive factors of length $\ell$ starting at positions $s$,
$s + \ell$ and $s + 2\ell$ all have the same sum of letter values.

## Sources

- Julien Cassaigne, James D. Currie, Luke Schaeffer and Jeffrey Shallit, Avoiding three consecutive blocks of the same size and same sum, J. ACM 61(2) (2014), Article 10, arXiv:1106.5204, https://arxiv.org/abs/1106.5204.

Stated but not proved: `MathlibExt.Combinatorics.PVHHCubeMorphicWordWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PVHHCubeMorphicWordWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Avoidance of additive cubes](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/avoidance-of-additive-cubes)
