---
declaration: section
origin: cited
lean: MetaMathlibExt.aronsonTransform_existsUnique_general, MetaMathlibExt.aronsonTransform_existsUnique
statement: formalized
proof: formalized
---

# Aronson transform

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/aronson-transform/index.html).

## Existence and uniqueness of the Aronson transform, general form

Let $n_0$ be a natural
number and let $\beta : \mathbb{N} \to \mathbb{N}$ be strictly increasing such that infinitely
many integers $m \ge n_0$ are not values of $\beta$. Then there is exactly one sequence
$\alpha : \mathbb{N} \to \mathbb{N}$ such that $\alpha$ is strictly increasing, $\alpha_i \ge n_0$
for every $i$, $\alpha_0$ is the least integer $m \ge n_0$ such that $m = n_0$ holds exactly when
$m$ is a value of $\beta$, and, for every $i \ge 0$, $\alpha_{i+1}$ is the least integer
$m > \alpha_i$ such that $n_0 + i + 1 \in \{\alpha_0, \dots, \alpha_i, m\}$ holds exactly when $m$
is a value of $\beta$.

The values of $\beta$ are not required to be at least $n_0$.

Formalized by `MetaMathlibExt.aronsonTransform_existsUnique_general`, a theorem declared in [MathlibExt/Combinatorics/Sequences/AronsonTransform.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Sequences/AronsonTransform.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/aronson-transform/index.html#aronson-transform-exists-unique-general).

## Existence and uniqueness of the Aronson transform

Let $n_0$ be a natural number and let
$\beta : \mathbb{N} \to \mathbb{N}$ be strictly increasing with $\beta_i \ge n_0$ for every $i$,
such that infinitely many integers $m \ge n_0$ are not values of $\beta$. Then there is exactly
one sequence $\alpha : \mathbb{N} \to \mathbb{N}$ such that $\alpha$ is strictly increasing,
$\alpha_i \ge n_0$ for every $i$, $\alpha_0$ is the least integer $m \ge n_0$ such that $m = n_0$
holds exactly when $m$ is a value of $\beta$, and, for every $i \ge 0$, $\alpha_{i+1}$ is the
least integer $m > \alpha_i$ such that $n_0 + i + 1 \in \{\alpha_0, \dots, \alpha_i, m\}$ holds
exactly when $m$ is a value of $\beta$.

The hypothesis $\beta_i \ge n_0$ is not used in the proof.

## Sources

- Benoit Cloitre, N. J. A. Sloane, and Matthew J. Vandermast, "Numerical Analogues of Aronson's Sequence," Journal of Integer Sequences 6 (2003), Article 03.2.2, Theorem `ThAT1`, lines 782–784 (transform defined lines 761–780), https://cs.uwaterloo.ca/journals/JIS/VOL6/Cloitre/cloitre2.tex

Formalized by `MetaMathlibExt.aronsonTransform_existsUnique`, a theorem declared in [MathlibExt/Combinatorics/Sequences/AronsonTransform.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Sequences/AronsonTransform.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/aronson-transform/index.html#aronson-transform-exists-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aronson transform](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/aronson-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/aronson-transform)
