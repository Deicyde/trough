---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Additive.SarkozyWanted.initialSegmentCount, MathlibExt.Combinatorics.Additive.SarkozyWanted.furstenberg_sarkozy
statement: formalized
proof: formalized
---

# Furstenberg–Sárközy theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/furstenberg-s-rk-zy-theorem/index.html).

## Initial segment count

For a set $A$ of natural numbers and a natural number $N$, the
initial segment count of $A$ at $N$ is the number of elements of $A$ that are less than $N$, that
is, $|A \cap \{0, 1, \dots, N - 1\}|$.

Formalized by `MathlibExt.Combinatorics.Additive.SarkozyWanted.initialSegmentCount`, a definition declared in [MathlibExt/Combinatorics/Additive/Sarkozy.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Sarkozy.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/furstenberg-s-rk-zy-theorem/index.html#initial-segment-count).

## Furstenberg–Sárközy theorem

Let $A$ be a set of natural numbers, and suppose there is a real
number $\delta > 0$ such that for every natural number $M$ there is a natural number $N \ge M$
with $\delta N \le |A \cap \{0, 1, \dots, N - 1\}|$. Then there are $a, b \in A$ and a natural
number $k > 0$ with $a < b$ and $b = a + k^2$.

## Sources

- A. Sárközy, Acta Math. Acad. Sci. Hungar. 31 (1978) and H. Furstenberg, J. Analyse Math. 31 (1977); Lean states positive upper density via `initialSegmentCount` with arbitrarily large N.

Formalized by `MathlibExt.Combinatorics.Additive.SarkozyWanted.furstenberg_sarkozy`, a theorem declared in [MathlibExt/Combinatorics/Additive/Sarkozy.lean, line 1944](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/Sarkozy.lean#L1944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/furstenberg-s-rk-zy-theorem/index.html#furstenberg-sarkozy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Furstenberg–Sárközy theorem](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/furstenberg-s-rk-zy-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/furstenberg-s-rk-zy-theorem)
