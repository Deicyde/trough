---
declaration: section
origin: cited
lean: OAI.SquareRootDegree.main
statement: formalized
proof: formalized
---

# 192. Boolean functions violate the square-root degree bound by arbitrary factors

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves the proposed square-root bound relating a Boolean function's linear Fourier coefficients to its polynomial degree. For every *C* > 0, there is a sign-valued Boolean function *f* with $\sum_i\widehat f(\{i\})\gt C\sqrt{\deg(f)}$. Thus its total signed correlation with individual input bits can exceed the proposed bound by an arbitrary factor.

## Unbounded Violations of the Square-Root Degree Bound

We disprove the Gopalan–Servedio square-root conjecture, even up to an arbitrary constant factor. For every real *C* > 0, there is a nonconstant Boolean function $f:\{-1,1\}^n\to\{-1,1\}$ on a finite sign cube such that

$\displaystyle \sum_{i=1}^n \widehat f(\{i\})\gt C\sqrt{\deg(f)}.$

Here $\widehat f(\{i\})$ is the linear Fourier coefficient associated with the *i*th input, and $\deg(f)$ is the degree of the real multilinear polynomial representing *f*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026/Unbounded-Violations-of-the-Square-Root-Degree-Bound-September-26-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization disproves the Gopalan–Servedio square-root degree conjecture by an unbounded factor. For every $C>0$, it gives a nonconstant Boolean function on a finite sign cube for which the sum of its linear Fourier coefficients exceeds $C\sqrt{\deg f}$, where $\deg f$ is its real multilinear degree.

It also proves that the ratio of the sum of the absolute values of those coefficients to $\sqrt{\deg f}$ is unbounded among positive-degree Boolean functions.

## Lean: Unbounded violations of the square-root Fourier-degree bound

```lean
theorem main : SignedViolations ∧ ¬ BddAbove AbsoluteRatios
```

Stated in [SquareRootDegree.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SquareRootDegree.lean#L57). Proved in [lean/OAI/Combinatorics/BooleanFunctions/Main.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/BooleanFunctions/Main.lean#L20).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/192.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/192.md)
