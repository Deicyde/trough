---
declaration: section
origin: cited
lean: OAI.Problem348.no_polynomial_removal_bound
statement: formalized
proof: formalized
---

# 190. Polynomial removal fails for ordered binary matrices

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves polynomial ordered binary matrix removal with one fixed $66\times66$ zero–one pattern. Matrices can require many binary-entry changes to become pattern-free while their copy density is smaller than every proposed polynomial bound in that distance. Copies preserve row and column orders and match both zeros and ones.

## Polynomial removal fails for ordered binary matrices

We construct a fixed $66\times66$ binary matrix for which ordered matrix removal has no polynomial bound. This disproves the polynomial ordered binary matrix-removal conjecture. Ordered copies preserve the separate row and column orders and match both zeros and ones; removal permits changing entries in either direction.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Polynomial-removal-fails-for-ordered-binary-matrices-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result disproves a polynomial removal bound for one explicit $66\times66$ binary pattern. For every $c,C>0$, there is an $n\times n$ binary matrix at normalized edit distance at least $\varepsilon>0$ from being pattern-free but with fewer than $c\varepsilon^C n^{132}$ induced ordered copies. Row and column indices are independently increasing, and every zero and one entry must match. The construction gives an explicit sequence of such matrices, allowing edits in both directions.

## Lean: Failure of polynomial removal for ordered binary matrices

```lean
theorem no_polynomial_removal_bound :
    ∀ c C : ℝ, 0 < c → 0 < C →
  ∃ n : ℕ, 1 ≤ n ∧
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧
      ∃ A : BinaryMatrix n,
        fixedDistance A ≥ ε ∧
        (copyCount fixedH A : ℝ) <
          c * Real.rpow ε C * ((n : ℝ) ^ 132)
```

Stated in [MatrixRemoval.lean, line 63](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MatrixRemoval.lean#L63). Proved in [lean/OAI/Combinatorics/MatrixRemoval/Main.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/MatrixRemoval/Main.lean#L26). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/190.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/190.md)
