---
declaration: section
origin: cited
lean: OAI.InternalCatalan.catalan_irrational
statement: formalized
---

# 005. Irrationality of Catalan’s constant

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that Catalan's constant $G=\sum_{j\ge0}(-1)^j/(2j+1)^2$ is irrational.

## Catalan's constant is irrational

We prove that Catalan's constant $G=\sum_{j\geq0}(-1)^j/(2j+1)^2$ is irrational.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that Catalan's constant $G=\sum_{j=0}^{\infty}(-1)^j/(2j+1)^2$ is irrational. This is the mathematical assertion in the paper's title.

## Lean: Irrationality of Catalan's constant

```lean
theorem catalan_irrational :
    Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2)
```

Stated in [Catalan.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Catalan.lean#L7). Its proof is in [lean/OAI/NumberTheory/Catalan/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/Catalan/Main.lean) or a file it imports further down, which this chapter does not read.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/005.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/005.md)
